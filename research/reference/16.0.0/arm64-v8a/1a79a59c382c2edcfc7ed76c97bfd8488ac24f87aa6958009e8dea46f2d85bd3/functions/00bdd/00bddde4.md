# 00bddde4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6e8e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e8e4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0005.md#compare-e954123efb10b39b3fcd3cb815860064)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bde20c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde20c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-176753650a878ea310e10612d91261de)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddde4",
  "name": "_ZN8firebase4auth4UserC1ERKS1_",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3b9685558555ef792fa4e2e89aa898f8d7f6223f0ab9febcc81a56e3c714b5b",
  "source_text_sha256": "a3b9685558555ef792fa4e2e89aa898f8d7f6223f0ab9febcc81a56e3c714b5b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddde4",
        "00bdde27"
      ]
    ],
    "bytes_sha256": "47749795ac2331ca9ccebdf24afbc78a16cf1f74e27995e04196c3ca3b947b9f",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a640](../00c5a/00c5a640.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 581 bytes

~~~c

void _ZN8firebase4auth4UserC1ERKS1_(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9b5c0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[1] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[0x13] = *(long *)(param_2 + 0x98);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddde4"></a> `00bddde4` | `e8 05 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bddde8"></a> `00bddde8` | `08 e1 42 f9` | ldr x8,[x8, #0x5c0] | `FALL_THROUGH`
<a id="insn-00bdddec"></a> `00bdddec` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdddf0"></a> `00bdddf0` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `00 80 87 3c` | stur q0,[x0, #0x78] | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00bdde00"></a> `00bdde00` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00bdde04"></a> `00bdde04` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bdde08"></a> `00bdde08` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00bdde0c"></a> `00bdde0c` | `00 80 82 3c` | stur q0,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bdde10"></a> `00bdde10` | `00 80 81 3c` | stur q0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bdde14"></a> `00bdde14` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bdde18"></a> `00bdde18` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdde1c"></a> `00bdde1c` | `28 4c 40 f9` | ldr x8,[x1, #0x98] | `FALL_THROUGH`
<a id="insn-00bdde20"></a> `00bdde20` | `08 4c 00 f9` | str x8,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdde24"></a> `00bdde24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddde4`](#insn-00bddde4) 範囲 `[['00bddde4', '00bdde27']]`

## 命令位置別の参照

- [`00bddde8`](#insn-00bddde8) → `00c9b5c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdde18`](#insn-00bdde18) → `00c924a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddde8`](#insn-00bddde8)

~~~json
{
  "source": "00bddde8",
  "target": "00c9b5c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdde18`](#insn-00bdde18)

~~~json
{
  "source": "00bdde18",
  "target": "00c924a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92498",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
