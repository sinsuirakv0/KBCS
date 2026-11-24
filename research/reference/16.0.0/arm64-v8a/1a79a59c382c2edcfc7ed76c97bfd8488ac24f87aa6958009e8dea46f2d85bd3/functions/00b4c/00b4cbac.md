# 00b4cbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aece28`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-98177213aead501d8ac4c26abe85981c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4cfd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0073.md#compare-a1ac703cff9ce4615dbb6623314b8311)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cbac",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef88dea072b892fe8fab9d7681823bda1688b3e9f7932cb13b0c7f8192cd9dd5",
  "source_text_sha256": "ef88dea072b892fe8fab9d7681823bda1688b3e9f7932cb13b0c7f8192cd9dd5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cbac",
        "00b4cbef"
      ]
    ],
    "bytes_sha256": "62c707f3312bf86adfdcf255311e0877de642f6c7cf07c5e4c3cc9bb1c5f8f92",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 460 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01125888 == 0) {
    DAT_01125888 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",param_3);
  }
  return DAT_01125888;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cbac"></a> `00b4cbac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4cbb0"></a> `00b4cbb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cbb4"></a> `00b4cbb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4cbb8"></a> `00b4cbb8` | `d3 2e 00 b0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4cbbc"></a> `00b4cbbc` | `68 46 44 f9` | ldr x8,[x19, #0x888] | `FALL_THROUGH`
<a id="insn-00b4cbc0"></a> `00b4cbc0` | `08 01 00 b5` | cbnz x8,0x00b4cbe0 | `CONDITIONAL_JUMP`
<a id="insn-00b4cbc4"></a> `00b4cbc4` | `23 bb ff 90` | adrp x3,0x2b0000 | `FALL_THROUGH`
<a id="insn-00b4cbc8"></a> `00b4cbc8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00b4cbcc"></a> `00b4cbcc` | `63 1c 15 91` | add x3,x3,#0x547 | `FALL_THROUGH`
<a id="insn-00b4cbd0"></a> `00b4cbd0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4cbd4"></a> `00b4cbd4` | `cf 37 04 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cbd8"></a> `00b4cbd8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4cbdc"></a> `00b4cbdc` | `60 46 04 f9` | str x0,[x19, #0x888] | `FALL_THROUGH`
<a id="insn-00b4cbe0"></a> `00b4cbe0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cbe4"></a> `00b4cbe4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4cbe8"></a> `00b4cbe8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4cbec"></a> `00b4cbec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cbac`](#insn-00b4cbac) 範囲 `[['00b4cbac', '00b4cbc3']]`
  - `CONDITIONAL_JUMP` [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbe0`](#insn-00b4cbe0)
  - `FALL_THROUGH` [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbc4`](#insn-00b4cbc4)
- ブロック [`00b4cbc4`](#insn-00b4cbc4) 範囲 `[['00b4cbc4', '00b4cbdf']]`
  - `FALL_THROUGH` [`00b4cbdc`](#insn-00b4cbdc) → [`00b4cbe0`](#insn-00b4cbe0)
- ブロック [`00b4cbe0`](#insn-00b4cbe0) 範囲 `[['00b4cbe0', '00b4cbef']]`

## 命令位置別の参照

- [`00b4cbac`](#insn-00b4cbac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbb0`](#insn-00b4cbb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbbc`](#insn-00b4cbbc) → `01125888`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cbc0`](#insn-00b4cbc0) → [`00b4cbe0`](#insn-00b4cbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbcc`](#insn-00b4cbcc) → `002b0547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4cbd4`](#insn-00b4cbd4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00b4cbdc`](#insn-00b4cbdc) → `01125888`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cbe0`](#insn-00b4cbe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cbac`](#insn-00b4cbac)

~~~json
{
  "source": "00b4cbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbb0`](#insn-00b4cbb0)

~~~json
{
  "source": "00b4cbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbbc`](#insn-00b4cbbc)

~~~json
{
  "source": "00b4cbbc",
  "target": "01125888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125888",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cbc0`](#insn-00b4cbc0)

~~~json
{
  "source": "00b4cbc0",
  "target": "00b4cbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cbcc`](#insn-00b4cbcc)

~~~json
{
  "source": "00b4cbcc",
  "target": "002b0547",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0547",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "002b0547",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4cbd4`](#insn-00b4cbd4)

~~~json
{
  "source": "00b4cbd4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cbdc`](#insn-00b4cbdc)

~~~json
{
  "source": "00b4cbdc",
  "target": "01125888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125888",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cbe0`](#insn-00b4cbe0)

~~~json
{
  "source": "00b4cbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
