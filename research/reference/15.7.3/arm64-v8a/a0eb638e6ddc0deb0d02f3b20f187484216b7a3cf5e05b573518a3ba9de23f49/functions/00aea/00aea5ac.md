# 00aea5ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aea4e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea4e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-9a360c8aa8b2cadafe44c76635f0c2a4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aea5f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-9329bd22462b87aac369695264058b61)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea5ac",
  "name": "_ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51c624d28d860acf7af795ef39553da6a9a95720480f5a3f38fb1a918cebd168",
  "source_text_sha256": "51c624d28d860acf7af795ef39553da6a9a95720480f5a3f38fb1a918cebd168",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea5ac",
        "00aea5ef"
      ]
    ],
    "bytes_sha256": "c58bb5c95934fe7f9b2b72c80a5fdb3beebaaf8ebfa6d6e11c683bd22d3d3a01",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/io/File"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 460 bytes

~~~c

long _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0790 == 0) {
    DAT_010a0790 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/io/File",param_3);
  }
  return DAT_010a0790;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea5ac"></a> `00aea5ac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea5b0"></a> `00aea5b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea5b4"></a> `00aea5b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea5b8"></a> `00aea5b8` | `b3 2d 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea5bc"></a> `00aea5bc` | `68 ca 43 f9` | ldr x8,[x19, #0x790] | `FALL_THROUGH`
<a id="insn-00aea5c0"></a> `00aea5c0` | `08 01 00 b5` | cbnz x8,0x00aea5e0 | `CONDITIONAL_JUMP`
<a id="insn-00aea5c4"></a> `00aea5c4` | `e3 bd ff 90` | adrp x3,0x2a6000 | `FALL_THROUGH`
<a id="insn-00aea5c8"></a> `00aea5c8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aea5cc"></a> `00aea5cc` | `63 60 03 91` | add x3,x3,#0xd8 | `FALL_THROUGH`
<a id="insn-00aea5d0"></a> `00aea5d0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aea5d4"></a> `00aea5d4` | `9b ce 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aea5d8"></a> `00aea5d8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aea5dc"></a> `00aea5dc` | `60 ca 03 f9` | str x0,[x19, #0x790] | `FALL_THROUGH`
<a id="insn-00aea5e0"></a> `00aea5e0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea5e4"></a> `00aea5e4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aea5e8"></a> `00aea5e8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aea5ec"></a> `00aea5ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea5ac`](#insn-00aea5ac) 範囲 `[['00aea5ac', '00aea5c3']]`
  - `CONDITIONAL_JUMP` [`00aea5c0`](#insn-00aea5c0) → [`00aea5e0`](#insn-00aea5e0)
  - `FALL_THROUGH` [`00aea5c0`](#insn-00aea5c0) → [`00aea5c4`](#insn-00aea5c4)
- ブロック [`00aea5c4`](#insn-00aea5c4) 範囲 `[['00aea5c4', '00aea5df']]`
  - `FALL_THROUGH` [`00aea5dc`](#insn-00aea5dc) → [`00aea5e0`](#insn-00aea5e0)
- ブロック [`00aea5e0`](#insn-00aea5e0) 範囲 `[['00aea5e0', '00aea5ef']]`

## 命令位置別の参照

- [`00aea5ac`](#insn-00aea5ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea5b0`](#insn-00aea5b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea5bc`](#insn-00aea5bc) → `010a0790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea5c0`](#insn-00aea5c0) → [`00aea5e0`](#insn-00aea5e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea5cc`](#insn-00aea5cc) → `002a60d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aea5d4`](#insn-00aea5d4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aea5dc`](#insn-00aea5dc) → `010a0790`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea5e0`](#insn-00aea5e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea5ac`](#insn-00aea5ac)

~~~json
{
  "source": "00aea5ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea5b0`](#insn-00aea5b0)

~~~json
{
  "source": "00aea5b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea5bc`](#insn-00aea5bc)

~~~json
{
  "source": "00aea5bc",
  "target": "010a0790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea5c0`](#insn-00aea5c0)

~~~json
{
  "source": "00aea5c0",
  "target": "00aea5e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea5cc`](#insn-00aea5cc)

~~~json
{
  "source": "00aea5cc",
  "target": "002a60d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a60d8",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "6a6176612f696f2f46696c6500",
  "capture_start": "002a60d8",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea5d4`](#insn-00aea5d4)

~~~json
{
  "source": "00aea5d4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea5dc`](#insn-00aea5dc)

~~~json
{
  "source": "00aea5dc",
  "target": "010a0790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0790",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea5e0`](#insn-00aea5e0)

~~~json
{
  "source": "00aea5e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
