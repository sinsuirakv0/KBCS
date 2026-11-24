# 00af0efc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeff08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aeff08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-9ed18d3ba671b44e153fb0cf9b4aa59f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0efc",
  "name": "FUN_00af0efc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5319cc6c270a77c9e9c40b4222d8d3789a4042d322c3f7f284dbd8d9709e5db",
  "source_text_sha256": "f5319cc6c270a77c9e9c40b4222d8d3789a4042d322c3f7f284dbd8d9709e5db",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af0efc",
        "00af0fe3"
      ]
    ],
    "bytes_sha256": "865742357d3b3b9e2286a07442f5a99d98383d1d744d79c878530b5036e9d9f7",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008b7ea8](../008b7/008b7ea8.md)
- [008ba7a4](../008ba/008ba7a4.md)
- [00a47938](../00a47/00a47938.md)
- [00a47c00](../00a47/00a47c00.md)
- [00aeb3e4](../00aeb/00aeb3e4.md)
- [00aeb640](../00aeb/00aeb640.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1160 bytes

~~~c

void FUN_00af0efc(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*param_3 == 3) {
    uVar4 = *param_2;
    lVar5 = *(long *)(param_1 + 8);
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,0xb,0);
    *(byte *)(lVar5 + 0x9ec) = *(byte *)(lVar5 + 0x9ec) ^ 1;
    uVar2 = FUN_008b7ea8(uVar4);
    uVar2 = FUN_00a47938(uVar2,0);
    uVar3 = 0x90;
    if (*(char *)(lVar5 + 0x9ec) == '\0') {
      uVar3 = 0x91;
    }
    FUN_00a47c00(uVar2,uVar3);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aeb3e4(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
                    /* try { // try from 00af0f98 to 00bf0f9b has its CatchHandler @ 00af14d0 */
                    /* try { // try from 00af0f9c to 00bf10c7 has its CatchHandler @ 00af0de8 */
    FUN_008ba7a4(uVar2,0,uVar1 & 1);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aeb640(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008ba7a4(uVar2,1,uVar1 & 1);
    return;
  }
  if (*param_3 == 0) {
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,10,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af0efc"></a> `00af0efc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af0f00"></a> `00af0f00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0f04"></a> `00af0f04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0f08"></a> `00af0f08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af0f0c"></a> `00af0f0c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00af0f10"></a> `00af0f10` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00af0f14"></a> `00af0f14` | `20 01 00 54` | b.eq 0x00af0f38 | `CONDITIONAL_JUMP`
<a id="insn-00af0f18"></a> `00af0f18` | `e8 05 00 35` | cbnz w8,0x00af0fd4 | `CONDITIONAL_JUMP`
<a id="insn-00af0f1c"></a> `00af0f1c` | `4e 28 e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f20"></a> `00af0f20` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00af0f24"></a> `00af0f24` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00af0f28"></a> `00af0f28` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0f2c"></a> `00af0f2c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0f30"></a> `00af0f30` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0f34"></a> `00af0f34` | `80 30 e6 17` | b 0x0047d134 | `CALL_TERMINATOR`
<a id="insn-00af0f38"></a> `00af0f38` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00af0f3c"></a> `00af0f3c` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af0f40"></a> `00af0f40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af0f44"></a> `00af0f44` | `44 28 e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f48"></a> `00af0f48` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00af0f4c"></a> `00af0f4c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00af0f50"></a> `00af0f50` | `79 30 e6 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f54"></a> `00af0f54` | `88 b2 67 39` | ldrb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00af0f58"></a> `00af0f58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0f5c"></a> `00af0f5c` | `08 01 00 52` | eor w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af0f60"></a> `00af0f60` | `88 b2 27 39` | strb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00af0f64"></a> `00af0f64` | `d1 1b f7 97` | bl 0x008b7ea8 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f68"></a> `00af0f68` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af0f6c"></a> `00af0f6c` | `73 5a fd 97` | bl 0x00a47938 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f70"></a> `00af0f70` | `88 b2 67 39` | ldrb w8,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00af0f74"></a> `00af0f74` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af0f78"></a> `00af0f78` | `08 12 80 52` | mov w8,#0x90 | `FALL_THROUGH`
<a id="insn-00af0f7c"></a> `00af0f7c` | `01 15 88 1a` | cinc w1,w8,eq | `FALL_THROUGH`
<a id="insn-00af0f80"></a> `00af0f80` | `20 5b fd 97` | bl 0x00a47c00 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f84"></a> `00af0f84` | `81 b2 67 39` | ldrb w1,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00af0f88"></a> `00af0f88` | `b3 0a 40 f9` | ldr x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00af0f8c"></a> `00af0f8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af0f90"></a> `00af0f90` | `15 e9 ff 97` | bl 0x00aeb3e4 | `UNCONDITIONAL_CALL`
<a id="insn-00af0f94"></a> `00af0f94` | `02 00 00 12` | and w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00af0f98"></a> `00af0f98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0f9c"></a> `00af0f9c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af0fa0"></a> `00af0fa0` | `01 26 f7 97` | bl 0x008ba7a4 | `UNCONDITIONAL_CALL`
<a id="insn-00af0fa4"></a> `00af0fa4` | `81 b2 67 39` | ldrb w1,[x20, #0x9ec] | `FALL_THROUGH`
<a id="insn-00af0fa8"></a> `00af0fa8` | `b3 0a 40 f9` | ldr x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00af0fac"></a> `00af0fac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af0fb0"></a> `00af0fb0` | `a4 e9 ff 97` | bl 0x00aeb640 | `UNCONDITIONAL_CALL`
<a id="insn-00af0fb4"></a> `00af0fb4` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00af0fb8"></a> `00af0fb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0fbc"></a> `00af0fbc` | `02 01 00 12` | and w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af0fc0"></a> `00af0fc0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00af0fc4"></a> `00af0fc4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0fc8"></a> `00af0fc8` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0fcc"></a> `00af0fcc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0fd0"></a> `00af0fd0` | `f5 25 f7 17` | b 0x008ba7a4 | `CALL_TERMINATOR`
<a id="insn-00af0fd4"></a> `00af0fd4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0fd8"></a> `00af0fd8` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af0fdc"></a> `00af0fdc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af0fe0"></a> `00af0fe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af0efc`](#insn-00af0efc) 範囲 `[['00af0efc', '00af0f17']]`
  - `CONDITIONAL_JUMP` [`00af0f14`](#insn-00af0f14) → [`00af0f38`](#insn-00af0f38)
  - `FALL_THROUGH` [`00af0f14`](#insn-00af0f14) → [`00af0f18`](#insn-00af0f18)
- ブロック [`00af0f18`](#insn-00af0f18) 範囲 `[['00af0f18', '00af0f1b']]`
  - `CONDITIONAL_JUMP` [`00af0f18`](#insn-00af0f18) → [`00af0fd4`](#insn-00af0fd4)
  - `FALL_THROUGH` [`00af0f18`](#insn-00af0f18) → [`00af0f1c`](#insn-00af0f1c)
- ブロック [`00af0f1c`](#insn-00af0f1c) 範囲 `[['00af0f1c', '00af0f37']]`
- ブロック [`00af0f38`](#insn-00af0f38) 範囲 `[['00af0f38', '00af0f97']]`
  - `FALL_THROUGH` [`00af0f94`](#insn-00af0f94) → [`00af0f98`](#insn-00af0f98)
- ブロック [`00af0f98`](#insn-00af0f98) 範囲 `[['00af0f98', '00af0f9b']]`
  - `FALL_THROUGH` [`00af0f98`](#insn-00af0f98) → [`00af0f9c`](#insn-00af0f9c)
- ブロック [`00af0f9c`](#insn-00af0f9c) 範囲 `[['00af0f9c', '00af0fd3']]`
- ブロック [`00af0fd4`](#insn-00af0fd4) 範囲 `[['00af0fd4', '00af0fe3']]`

## 命令位置別の参照

- [`00af0efc`](#insn-00af0efc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f00`](#insn-00af0f00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f04`](#insn-00af0f04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f14`](#insn-00af0f14) → [`00af0f38`](#insn-00af0f38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f18`](#insn-00af0f18) → [`00af0fd4`](#insn-00af0fd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f1c`](#insn-00af0f1c) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00af0f28`](#insn-00af0f28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f2c`](#insn-00af0f2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f30`](#insn-00af0f30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0f34`](#insn-00af0f34) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00af0f44`](#insn-00af0f44) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00af0f50`](#insn-00af0f50) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00af0f64`](#insn-00af0f64) → [`008b7ea8`](../008b7/008b7ea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7ea8` · 推定シンボル `None` · 推定型 `None`
- [`00af0f6c`](#insn-00af0f6c) → [`00a47938`](../00a47/00a47938.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47938` · 推定シンボル `None` · 推定型 `None`
- [`00af0f80`](#insn-00af0f80) → [`00a47c00`](../00a47/00a47c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47c00` · 推定シンボル `None` · 推定型 `None`
- [`00af0f90`](#insn-00af0f90) → [`00aeb3e4`](../00aeb/00aeb3e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aeb3e4` · 推定シンボル `None` · 推定型 `None`
- [`00af0fa0`](#insn-00af0fa0) → [`008ba7a4`](../008ba/008ba7a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba7a4` · 推定シンボル `None` · 推定型 `None`
- [`00af0fb0`](#insn-00af0fb0) → [`00aeb640`](../00aeb/00aeb640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aeb640` · 推定シンボル `None` · 推定型 `None`
- [`00af0fc4`](#insn-00af0fc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0fc8`](#insn-00af0fc8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0fcc`](#insn-00af0fcc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0fd0`](#insn-00af0fd0) → [`008ba7a4`](../008ba/008ba7a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba7a4` · 推定シンボル `None` · 推定型 `None`
- [`00af0fd4`](#insn-00af0fd4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0fd8`](#insn-00af0fd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0fdc`](#insn-00af0fdc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af0efc`](#insn-00af0efc)

~~~json
{
  "source": "00af0efc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f00`](#insn-00af0f00)

~~~json
{
  "source": "00af0f00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f04`](#insn-00af0f04)

~~~json
{
  "source": "00af0f04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f14`](#insn-00af0f14)

~~~json
{
  "source": "00af0f14",
  "target": "00af0f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f18`](#insn-00af0f18)

~~~json
{
  "source": "00af0f18",
  "target": "00af0fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f1c`](#insn-00af0f1c)

~~~json
{
  "source": "00af0f1c",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f28`](#insn-00af0f28)

~~~json
{
  "source": "00af0f28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f2c`](#insn-00af0f2c)

~~~json
{
  "source": "00af0f2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f30`](#insn-00af0f30)

~~~json
{
  "source": "00af0f30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0f34`](#insn-00af0f34)

~~~json
{
  "source": "00af0f34",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f44`](#insn-00af0f44)

~~~json
{
  "source": "00af0f44",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f50`](#insn-00af0f50)

~~~json
{
  "source": "00af0f50",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f64`](#insn-00af0f64)

~~~json
{
  "source": "00af0f64",
  "target": "008b7ea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f6c`](#insn-00af0f6c)

~~~json
{
  "source": "00af0f6c",
  "target": "00a47938",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f80`](#insn-00af0f80)

~~~json
{
  "source": "00af0f80",
  "target": "00a47c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0f90`](#insn-00af0f90)

~~~json
{
  "source": "00af0f90",
  "target": "00aeb3e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0fa0`](#insn-00af0fa0)

~~~json
{
  "source": "00af0fa0",
  "target": "008ba7a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0fb0`](#insn-00af0fb0)

~~~json
{
  "source": "00af0fb0",
  "target": "00aeb640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0fc4`](#insn-00af0fc4)

~~~json
{
  "source": "00af0fc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0fc8`](#insn-00af0fc8)

~~~json
{
  "source": "00af0fc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0fcc`](#insn-00af0fcc)

~~~json
{
  "source": "00af0fcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0fd0`](#insn-00af0fd0)

~~~json
{
  "source": "00af0fd0",
  "target": "008ba7a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0fd4`](#insn-00af0fd4)

~~~json
{
  "source": "00af0fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0fd8`](#insn-00af0fd8)

~~~json
{
  "source": "00af0fd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0fdc`](#insn-00af0fdc)

~~~json
{
  "source": "00af0fdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
