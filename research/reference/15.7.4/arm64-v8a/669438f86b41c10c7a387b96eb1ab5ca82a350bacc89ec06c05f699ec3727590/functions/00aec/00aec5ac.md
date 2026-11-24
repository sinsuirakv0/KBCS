# 00aec5ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aec568`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-3c518fc102bf129b68775aa9d852f41f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4c330`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-f09b63e75f6883fdef067fc36aa4120a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec5ac",
  "name": "_ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70011405ae902fcf54fb6fde66390ff2c2a86bc71c9ded79a9f214fea980fcdf",
  "source_text_sha256": "70011405ae902fcf54fb6fde66390ff2c2a86bc71c9ded79a9f214fea980fcdf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec5ac",
        "00aec61b"
      ]
    ],
    "bytes_sha256": "51a230bf861936cd13af7e209017c1b0b2476f1298c7b8a5df96c9ba46166288",
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
"java/lang/Long"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 589 bytes

~~~c

void _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0950 == 0) {
    DAT_010a0950 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Long",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0950,&DAT_002f5d58,1,&DAT_010a0970,"java/lang/Long");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec5ac"></a> `00aec5ac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec5b0"></a> `00aec5b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec5b4"></a> `00aec5b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec5b8"></a> `00aec5b8` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec5bc"></a> `00aec5bc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aec5c0"></a> `00aec5c0` | `81 aa 44 f9` | ldr x1,[x20, #0x950] | `FALL_THROUGH`
<a id="insn-00aec5c4"></a> `00aec5c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec5c8"></a> `00aec5c8` | `41 01 00 b5` | cbnz x1,0x00aec5f0 | `CONDITIONAL_JUMP`
<a id="insn-00aec5cc"></a> `00aec5cc` | `c3 bd ff f0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec5d0"></a> `00aec5d0` | `63 c0 37 91` | add x3,x3,#0xdf0 | `FALL_THROUGH`
<a id="insn-00aec5d4"></a> `00aec5d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec5d8"></a> `00aec5d8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aec5dc"></a> `00aec5dc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aec5e0"></a> `00aec5e0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aec5e4"></a> `00aec5e4` | `ab c6 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aec5e8"></a> `00aec5e8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aec5ec"></a> `00aec5ec` | `80 aa 04 f9` | str x0,[x20, #0x950] | `FALL_THROUGH`
<a id="insn-00aec5f0"></a> `00aec5f0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec5f4"></a> `00aec5f4` | `42 c0 ff b0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aec5f8"></a> `00aec5f8` | `a4 2d 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec5fc"></a> `00aec5fc` | `c5 bd ff f0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aec600"></a> `00aec600` | `42 60 35 91` | add x2,x2,#0xd58 | `FALL_THROUGH`
<a id="insn-00aec604"></a> `00aec604` | `84 c0 25 91` | add x4,x4,#0x970 | `FALL_THROUGH`
<a id="insn-00aec608"></a> `00aec608` | `a5 c0 37 91` | add x5,x5,#0xdf0 | `FALL_THROUGH`
<a id="insn-00aec60c"></a> `00aec60c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aec610"></a> `00aec610` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec614"></a> `00aec614` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec618"></a> `00aec618` | `96 c6 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec5ac`](#insn-00aec5ac) 範囲 `[['00aec5ac', '00aec5cb']]`
  - `CONDITIONAL_JUMP` [`00aec5c8`](#insn-00aec5c8) → [`00aec5f0`](#insn-00aec5f0)
  - `FALL_THROUGH` [`00aec5c8`](#insn-00aec5c8) → [`00aec5cc`](#insn-00aec5cc)
- ブロック [`00aec5cc`](#insn-00aec5cc) 範囲 `[['00aec5cc', '00aec5ef']]`
  - `FALL_THROUGH` [`00aec5ec`](#insn-00aec5ec) → [`00aec5f0`](#insn-00aec5f0)
- ブロック [`00aec5f0`](#insn-00aec5f0) 範囲 `[['00aec5f0', '00aec61b']]`

## 命令位置別の参照

- [`00aec5ac`](#insn-00aec5ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5b0`](#insn-00aec5b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5c0`](#insn-00aec5c0) → `010a0950`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec5c8`](#insn-00aec5c8) → [`00aec5f0`](#insn-00aec5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec5d0`](#insn-00aec5d0) → `002a7df0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec5e4`](#insn-00aec5e4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aec5ec`](#insn-00aec5ec) → `010a0950`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec5f0`](#insn-00aec5f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec600`](#insn-00aec600) → `002f5d58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec604`](#insn-00aec604) → `010a0970`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec608`](#insn-00aec608) → `002a7df0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec618`](#insn-00aec618) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec5ac`](#insn-00aec5ac)

~~~json
{
  "source": "00aec5ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5b0`](#insn-00aec5b0)

~~~json
{
  "source": "00aec5b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5c0`](#insn-00aec5c0)

~~~json
{
  "source": "00aec5c0",
  "target": "010a0950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0950",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec5c8`](#insn-00aec5c8)

~~~json
{
  "source": "00aec5c8",
  "target": "00aec5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec5d0`](#insn-00aec5d0)

~~~json
{
  "source": "00aec5d0",
  "target": "002a7df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7df0",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4c6f6e6700",
  "capture_start": "002a7df0",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec5e4`](#insn-00aec5e4)

~~~json
{
  "source": "00aec5e4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec5ec`](#insn-00aec5ec)

~~~json
{
  "source": "00aec5ec",
  "target": "010a0950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0950",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec5f0`](#insn-00aec5f0)

~~~json
{
  "source": "00aec5f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec600`](#insn-00aec600)

~~~json
{
  "source": "00aec600",
  "target": "002f5d58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec604`](#insn-00aec604)

~~~json
{
  "source": "00aec604",
  "target": "010a0970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec608`](#insn-00aec608)

~~~json
{
  "source": "00aec608",
  "target": "002a7df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7df0",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4c6f6e6700",
  "capture_start": "002a7df0",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aec618`](#insn-00aec618)

~~~json
{
  "source": "00aec618",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
