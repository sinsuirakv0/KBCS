# 00aeccfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeccb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-4b0006e55cc754d206928f2d76083132)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4ca80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-d821e4926b1a7f55cc737a61ddf53157)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeccfc",
  "name": "_ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c52a06d8280f22c6c4169319413b116d07db936773fdce0e80ab7f4caab910b3",
  "source_text_sha256": "c52a06d8280f22c6c4169319413b116d07db936773fdce0e80ab7f4caab910b3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeccfc",
        "00aecd6b"
      ]
    ],
    "bytes_sha256": "51dd32b37e76460f7b0bce47fb2ea971f5e8cea2180920a228cf0315ba8fe8c2",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 732 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aecd00 to 00becd6b has its CatchHandler @ 00af1a7c */
  if (DAT_010a09a8 == 0) {
    DAT_010a09a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a09a8,&DAT_002f5d88,1,&DAT_010a09c0,"android/os/ParcelFileDescriptor");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeccfc"></a> `00aeccfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecd00"></a> `00aecd00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd04"></a> `00aecd04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecd08"></a> `00aecd08` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecd0c"></a> `00aecd0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aecd10"></a> `00aecd10` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecd14"></a> `00aecd14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecd18"></a> `00aecd18` | `41 01 00 b5` | cbnz x1,0x00aecd40 | `CONDITIONAL_JUMP`
<a id="insn-00aecd1c"></a> `00aecd1c` | `43 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00aecd20"></a> `00aecd20` | `63 4c 07 91` | add x3,x3,#0x1d3 | `FALL_THROUGH`
<a id="insn-00aecd24"></a> `00aecd24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecd28"></a> `00aecd28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aecd2c"></a> `00aecd2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecd30"></a> `00aecd30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aecd34"></a> `00aecd34` | `d7 c4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aecd38"></a> `00aecd38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aecd3c"></a> `00aecd3c` | `80 d6 04 f9` | str x0,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aecd40"></a> `00aecd40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd44"></a> `00aecd44` | `42 c0 ff b0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aecd48"></a> `00aecd48` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecd4c"></a> `00aecd4c` | `45 bd ff 90` | adrp x5,0x294000 | `FALL_THROUGH`
<a id="insn-00aecd50"></a> `00aecd50` | `42 20 36 91` | add x2,x2,#0xd88 | `FALL_THROUGH`
<a id="insn-00aecd54"></a> `00aecd54` | `84 00 27 91` | add x4,x4,#0x9c0 | `FALL_THROUGH`
<a id="insn-00aecd58"></a> `00aecd58` | `a5 4c 07 91` | add x5,x5,#0x1d3 | `FALL_THROUGH`
<a id="insn-00aecd5c"></a> `00aecd5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aecd60"></a> `00aecd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecd64"></a> `00aecd64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecd68"></a> `00aecd68` | `c2 c4 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeccfc`](#insn-00aeccfc) 範囲 `[['00aeccfc', '00aeccff']]`
  - `FALL_THROUGH` [`00aeccfc`](#insn-00aeccfc) → [`00aecd00`](#insn-00aecd00)
- ブロック [`00aecd00`](#insn-00aecd00) 範囲 `[['00aecd00', '00aecd1b']]`
  - `CONDITIONAL_JUMP` [`00aecd18`](#insn-00aecd18) → [`00aecd40`](#insn-00aecd40)
  - `FALL_THROUGH` [`00aecd18`](#insn-00aecd18) → [`00aecd1c`](#insn-00aecd1c)
- ブロック [`00aecd1c`](#insn-00aecd1c) 範囲 `[['00aecd1c', '00aecd3f']]`
  - `FALL_THROUGH` [`00aecd3c`](#insn-00aecd3c) → [`00aecd40`](#insn-00aecd40)
- ブロック [`00aecd40`](#insn-00aecd40) 範囲 `[['00aecd40', '00aecd6b']]`

## 命令位置別の参照

- [`00aeccfc`](#insn-00aeccfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd00`](#insn-00aecd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd10`](#insn-00aecd10) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecd18`](#insn-00aecd18) → [`00aecd40`](#insn-00aecd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd20`](#insn-00aecd20) → `002941d3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecd34`](#insn-00aecd34) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aecd3c`](#insn-00aecd3c) → `010a09a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecd40`](#insn-00aecd40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd50`](#insn-00aecd50) → `002f5d88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd54`](#insn-00aecd54) → `010a09c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd58`](#insn-00aecd58) → `002941d3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecd68`](#insn-00aecd68) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeccfc`](#insn-00aeccfc)

~~~json
{
  "source": "00aeccfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd00`](#insn-00aecd00)

~~~json
{
  "source": "00aecd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd10`](#insn-00aecd10)

~~~json
{
  "source": "00aecd10",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecd18`](#insn-00aecd18)

~~~json
{
  "source": "00aecd18",
  "target": "00aecd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd20`](#insn-00aecd20)

~~~json
{
  "source": "00aecd20",
  "target": "002941d3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002941d3",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002941d3",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecd34`](#insn-00aecd34)

~~~json
{
  "source": "00aecd34",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecd3c`](#insn-00aecd3c)

~~~json
{
  "source": "00aecd3c",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecd40`](#insn-00aecd40)

~~~json
{
  "source": "00aecd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd50`](#insn-00aecd50)

~~~json
{
  "source": "00aecd50",
  "target": "002f5d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd54`](#insn-00aecd54)

~~~json
{
  "source": "00aecd54",
  "target": "010a09c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd58`](#insn-00aecd58)

~~~json
{
  "source": "00aecd58",
  "target": "002941d3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002941d3",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "616e64726f69642f6f732f50617263656c46696c6544657363726970746f7200",
  "capture_start": "002941d3",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecd68`](#insn-00aecd68)

~~~json
{
  "source": "00aecd68",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
