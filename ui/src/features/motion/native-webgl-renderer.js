const TEXTURE_VERTEX_SHADER = `
  attribute vec2 a_position;
  attribute vec2 a_uv;
  attribute float a_opacity;
  uniform vec2 u_resolution;
  varying vec2 v_uv;
  varying float v_opacity;

  void main() {
    vec2 clip = a_position / u_resolution * 2.0 - 1.0;
    gl_Position = vec4(clip.x, -clip.y, 0.0, 1.0);
    v_uv = a_uv;
    v_opacity = a_opacity;
  }
`;

const TEXTURE_FRAGMENT_SHADER = `
  precision mediump float;
  uniform sampler2D u_texture;
  uniform vec3 u_tint;
  varying vec2 v_uv;
  varying float v_opacity;

  void main() {
    gl_FragColor = texture2D(u_texture, v_uv) * v_opacity * vec4(u_tint, 1.0);
  }
`;

const COLOR_VERTEX_SHADER = `
  attribute vec2 a_position;
  uniform vec2 u_resolution;

  void main() {
    vec2 clip = a_position / u_resolution * 2.0 - 1.0;
    gl_Position = vec4(clip.x, -clip.y, 0.0, 1.0);
  }
`;

const COLOR_FRAGMENT_SHADER = `
  precision mediump float;
  uniform vec4 u_color;

  void main() {
    gl_FragColor = u_color;
  }
`;

const PREVIEW_BACKGROUND = [46 / 255, 49 / 255, 58 / 255, 1];

export class NativeWebGLRenderer {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.gl = canvas.getContext("webgl", {
      alpha: false,
      antialias: true,
      premultipliedAlpha: true,
      preserveDrawingBuffer: options.preserveDrawingBuffer ?? true,
    });
    if (!this.gl) throw new Error("WebGLを初期化できません");

    const gl = this.gl;
    this.textureProgram = createProgram(gl, TEXTURE_VERTEX_SHADER, TEXTURE_FRAGMENT_SHADER);
    this.colorProgram = createProgram(gl, COLOR_VERTEX_SHADER, COLOR_FRAGMENT_SHADER);
    this.vertexBuffer = gl.createBuffer();
    this.indexBuffer = gl.createBuffer();
    this.colorBuffer = gl.createBuffer();
    this.textureCache = new WeakMap();
    this.textures = options.trackTextures ? new Set() : null;
    this.packetCapacity = 0;
    this.vertexData = new Float32Array(0);
    this.indexData = new Uint16Array(0);
    this.logicalWidth = 1;
    this.logicalHeight = 1;

    gl.enable(gl.BLEND);
    gl.disable(gl.DEPTH_TEST);
    gl.disable(gl.CULL_FACE);
  }

  beginFrame(logicalWidth, logicalHeight, backgroundColor = PREVIEW_BACKGROUND) {
    const gl = this.gl;
    this.logicalWidth = logicalWidth;
    this.logicalHeight = logicalHeight;
    gl.viewport(0, 0, this.canvas.width, this.canvas.height);
    gl.clearColor(...backgroundColor);
    gl.clear(gl.COLOR_BUFFER_BIT);
  }

  drawPackets(image, packets) {
    if (packets.length === 0) return;
    if (packets.length * 4 > 0xffff) {
      throw new Error("1回の描画バッチで扱えるパーツ数を超えました");
    }

    const gl = this.gl;
    const texture = this.getTexture(image);
    this.ensurePacketCapacity(packets.length);
    const vertices = this.vertexData;
    const batches = [];

    for (let packetIndex = 0; packetIndex < packets.length; packetIndex += 1) {
      const packet = packets[packetIndex];
      let batch = batches.at(-1);
      if (!batch || batch.blendMode !== packet.blendMode || batch.tintKey !== (packet.tintKey || "")) {
        batch = { tintKey: packet.tintKey || "", tint: packet.tint || [1,1,1], blendMode: packet.blendMode, indexOffset: packetIndex * 6, indexCount: 0 };
        batches.push(batch);
      }
      batch.indexCount += 6;

      const vertexOffset = packetIndex * 20;
      for (let vertexIndex = 0; vertexIndex < 4; vertexIndex += 1) {
        const offset = vertexOffset + vertexIndex * 5;
        vertices[offset] = packet.positions[vertexIndex * 2];
        vertices[offset + 1] = packet.positions[vertexIndex * 2 + 1];
        vertices[offset + 2] = packet.uvs[vertexIndex * 2];
        vertices[offset + 3] = packet.uvs[vertexIndex * 2 + 1];
        vertices[offset + 4] = packet.opacity;
      }
    }

    gl.useProgram(this.textureProgram.program);
    gl.uniform2f(this.textureProgram.resolution, this.logicalWidth, this.logicalHeight);
    gl.uniform1i(this.textureProgram.texture, 0);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.bindBuffer(gl.ARRAY_BUFFER, this.vertexBuffer);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      vertices.subarray(0, packets.length * 20),
      gl.DYNAMIC_DRAW,
    );
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.indexBuffer);

    gl.enableVertexAttribArray(this.textureProgram.position);
    gl.vertexAttribPointer(this.textureProgram.position, 2, gl.FLOAT, false, 20, 0);
    gl.enableVertexAttribArray(this.textureProgram.uv);
    gl.vertexAttribPointer(this.textureProgram.uv, 2, gl.FLOAT, false, 20, 8);
    gl.enableVertexAttribArray(this.textureProgram.opacity);
    gl.vertexAttribPointer(this.textureProgram.opacity, 1, gl.FLOAT, false, 20, 16);

    for (const batch of batches) {
      gl.uniform3fv(this.textureProgram.tint, batch.tint);
      setNativeBlendMode(gl, batch.blendMode);
      gl.drawElements(
        gl.TRIANGLES,
        batch.indexCount,
        gl.UNSIGNED_SHORT,
        batch.indexOffset * Uint16Array.BYTES_PER_ELEMENT,
      );
    }
  }

  ensurePacketCapacity(packetCount) {
    if (packetCount <= this.packetCapacity) return;

    let capacity = Math.max(16, this.packetCapacity);
    while (capacity < packetCount) capacity *= 2;
    this.packetCapacity = capacity;
    this.vertexData = new Float32Array(capacity * 20);
    this.indexData = new Uint16Array(capacity * 6);

    for (let packetIndex = 0; packetIndex < capacity; packetIndex += 1) {
      const baseVertex = packetIndex * 4;
      const indexOffset = packetIndex * 6;
      this.indexData[indexOffset] = baseVertex;
      this.indexData[indexOffset + 1] = baseVertex + 1;
      this.indexData[indexOffset + 2] = baseVertex + 2;
      this.indexData[indexOffset + 3] = baseVertex;
      this.indexData[indexOffset + 4] = baseVertex + 2;
      this.indexData[indexOffset + 5] = baseVertex + 3;
    }

    // indexの並びはパーツ数に依存しないため、容量拡張時だけGPUへ転送する。
    const gl = this.gl;
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, this.indexData, gl.STATIC_DRAW);
  }

  drawColorGeometry(positions, color, mode, blendMode = 0) {
    const gl = this.gl;
    gl.useProgram(this.colorProgram.program);
    gl.uniform2f(this.colorProgram.resolution, this.logicalWidth, this.logicalHeight);
    gl.uniform4f(
      this.colorProgram.color,
      color[0] * color[3],
      color[1] * color[3],
      color[2] * color[3],
      color[3],
    );
    setNativeBlendMode(gl, blendMode);
    gl.bindBuffer(gl.ARRAY_BUFFER, this.colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.DYNAMIC_DRAW);
    gl.enableVertexAttribArray(this.colorProgram.position);
    gl.vertexAttribPointer(this.colorProgram.position, 2, gl.FLOAT, false, 0, 0);
    gl.drawArrays(mode, 0, positions.length / 2);
  }

  // 小さなプレビューへコピーした後、元アトラスのGPUメモリを解放する。
  releaseTexture(image) {
    const texture=this.textureCache.get(image);
    if(texture)this.gl.deleteTexture(texture);
    this.textures?.delete(texture);
    this.textureCache.delete(image);
  }

  getTexture(image) {
    const cached = this.textureCache.get(image);
    if (cached) return cached;

    const gl = this.gl;
    const texture = gl.createTexture();
    this.textures?.add(texture);
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
    gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    this.textureCache.set(image, texture);
    return texture;
  }
  dispose() {
    for(const texture of this.textures||[])this.gl.deleteTexture(texture);
    this.textures?.clear();
    for(const buffer of [this.vertexBuffer,this.indexBuffer,this.colorBuffer])this.gl.deleteBuffer(buffer);
    this.gl.deleteProgram(this.textureProgram.program);this.gl.deleteProgram(this.colorProgram.program);
  }
}

function createProgram(gl, vertexSource, fragmentSource) {
  const vertexShader = compileShader(gl, gl.VERTEX_SHADER, vertexSource);
  const fragmentShader = compileShader(gl, gl.FRAGMENT_SHADER, fragmentSource);
  const program = gl.createProgram();
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  gl.deleteShader(vertexShader);
  gl.deleteShader(fragmentShader);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    const message = gl.getProgramInfoLog(program) || "WebGLプログラムのリンクに失敗しました";
    gl.deleteProgram(program);
    throw new Error(message);
  }

  return {
    program,
    position: gl.getAttribLocation(program, "a_position"),
    uv: gl.getAttribLocation(program, "a_uv"),
    opacity: gl.getAttribLocation(program, "a_opacity"),
    resolution: gl.getUniformLocation(program, "u_resolution"),
    texture: gl.getUniformLocation(program, "u_texture"),
    tint: gl.getUniformLocation(program, "u_tint"),
    color: gl.getUniformLocation(program, "u_color"),
  };
}

function compileShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    const message = gl.getShaderInfoLog(shader) || "WebGLシェーダーのコンパイルに失敗しました";
    gl.deleteShader(shader);
    throw new Error(message);
  }
  return shader;
}

// 0x0090fa20のジャンプテーブルとglBlendFunc呼出をそのまま対応させる。
function setNativeBlendMode(gl, blendMode) {
  if (blendMode === 1) gl.blendFunc(gl.ONE, gl.ONE);
  else if (blendMode === 2) gl.blendFunc(gl.DST_COLOR, gl.ZERO);
  else if (blendMode === 3) gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_COLOR);
  else gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
}
