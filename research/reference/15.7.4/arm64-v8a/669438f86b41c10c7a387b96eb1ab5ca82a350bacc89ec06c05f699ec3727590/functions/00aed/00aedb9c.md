# 00aedb9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedb58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-0918e1bc934f087711d96acae2692adb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4d920`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-623d8f1b0f89c58ad32418a7b5d9afb6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedb9c",
  "name": "_ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3178e408f4ef7ecaf0917f74ceaf212229f0adc298e9d0223f156785a3ad2533",
  "source_text_sha256": "3178e408f4ef7ecaf0917f74ceaf212229f0adc298e9d0223f156785a3ad2533",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedb9c",
        "00aedc0b"
      ]
    ],
    "bytes_sha256": "131dca56503b93a0de9b27d7f5402ffd097d3014ff2bdd2b3c7da789db1b9bbf",
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
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 597 bytes

~~~c

void _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a30 == 0) {
    DAT_010a0a30 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0a30,&DAT_002f5de8,1,&DAT_010a0a58,"java/lang/Throwable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedb9c"></a> `00aedb9c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedba0"></a> `00aedba0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedba4"></a> `00aedba4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedba8"></a> `00aedba8` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedbac"></a> `00aedbac` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aedbb0"></a> `00aedbb0` | `81 1a 45 f9` | ldr x1,[x20, #0xa30] | `FALL_THROUGH`
<a id="insn-00aedbb4"></a> `00aedbb4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedbb8"></a> `00aedbb8` | `41 01 00 b5` | cbnz x1,0x00aedbe0 | `CONDITIONAL_JUMP`
<a id="insn-00aedbbc"></a> `00aedbbc` | `c3 bd ff f0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedbc0"></a> `00aedbc0` | `63 90 32 91` | add x3,x3,#0xca4 | `FALL_THROUGH`
<a id="insn-00aedbc4"></a> `00aedbc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedbc8"></a> `00aedbc8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aedbcc"></a> `00aedbcc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedbd0"></a> `00aedbd0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedbd4"></a> `00aedbd4` | `2f c1 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aedbd8"></a> `00aedbd8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aedbdc"></a> `00aedbdc` | `80 1a 05 f9` | str x0,[x20, #0xa30] | `FALL_THROUGH`
<a id="insn-00aedbe0"></a> `00aedbe0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedbe4"></a> `00aedbe4` | `42 c0 ff 90` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aedbe8"></a> `00aedbe8` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedbec"></a> `00aedbec` | `c5 bd ff f0` | adrp x5,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedbf0"></a> `00aedbf0` | `42 a0 37 91` | add x2,x2,#0xde8 | `FALL_THROUGH`
<a id="insn-00aedbf4"></a> `00aedbf4` | `84 60 29 91` | add x4,x4,#0xa58 | `FALL_THROUGH`
<a id="insn-00aedbf8"></a> `00aedbf8` | `a5 90 32 91` | add x5,x5,#0xca4 | `FALL_THROUGH`
<a id="insn-00aedbfc"></a> `00aedbfc` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aedc00"></a> `00aedc00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedc04"></a> `00aedc04` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedc08"></a> `00aedc08` | `1a c1 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedb9c`](#insn-00aedb9c) 範囲 `[['00aedb9c', '00aedbbb']]`
  - `CONDITIONAL_JUMP` [`00aedbb8`](#insn-00aedbb8) → [`00aedbe0`](#insn-00aedbe0)
  - `FALL_THROUGH` [`00aedbb8`](#insn-00aedbb8) → [`00aedbbc`](#insn-00aedbbc)
- ブロック [`00aedbbc`](#insn-00aedbbc) 範囲 `[['00aedbbc', '00aedbdf']]`
  - `FALL_THROUGH` [`00aedbdc`](#insn-00aedbdc) → [`00aedbe0`](#insn-00aedbe0)
- ブロック [`00aedbe0`](#insn-00aedbe0) 範囲 `[['00aedbe0', '00aedc0b']]`

## 命令位置別の参照

- [`00aedb9c`](#insn-00aedb9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedba0`](#insn-00aedba0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbb0`](#insn-00aedbb0) → `010a0a30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedbb8`](#insn-00aedbb8) → [`00aedbe0`](#insn-00aedbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbc0`](#insn-00aedbc0) → `002a8ca4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedbd4`](#insn-00aedbd4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aedbdc`](#insn-00aedbdc) → `010a0a30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedbe0`](#insn-00aedbe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbf0`](#insn-00aedbf0) → `002f5de8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbf4`](#insn-00aedbf4) → `010a0a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedbf8`](#insn-00aedbf8) → `002a8ca4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedc08`](#insn-00aedc08) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedb9c`](#insn-00aedb9c)

~~~json
{
  "source": "00aedb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedba0`](#insn-00aedba0)

~~~json
{
  "source": "00aedba0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbb0`](#insn-00aedbb0)

~~~json
{
  "source": "00aedbb0",
  "target": "010a0a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedbb8`](#insn-00aedbb8)

~~~json
{
  "source": "00aedbb8",
  "target": "00aedbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbc0`](#insn-00aedbc0)

~~~json
{
  "source": "00aedbc0",
  "target": "002a8ca4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8ca4",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8ca4",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedbd4`](#insn-00aedbd4)

~~~json
{
  "source": "00aedbd4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedbdc`](#insn-00aedbdc)

~~~json
{
  "source": "00aedbdc",
  "target": "010a0a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedbe0`](#insn-00aedbe0)

~~~json
{
  "source": "00aedbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbf0`](#insn-00aedbf0)

~~~json
{
  "source": "00aedbf0",
  "target": "002f5de8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbf4`](#insn-00aedbf4)

~~~json
{
  "source": "00aedbf4",
  "target": "010a0a58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedbf8`](#insn-00aedbf8)

~~~json
{
  "source": "00aedbf8",
  "target": "002a8ca4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8ca4",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8ca4",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedc08`](#insn-00aedc08)

~~~json
{
  "source": "00aedc08",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
