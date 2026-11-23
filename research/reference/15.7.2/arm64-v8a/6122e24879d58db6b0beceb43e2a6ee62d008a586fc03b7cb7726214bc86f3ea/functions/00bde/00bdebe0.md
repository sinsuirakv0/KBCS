# 00bdebe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdec90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-46519a93d1b83f6858c1a8cade16da7d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebe0",
  "name": "_ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fe766d279b5b1589c59f28ab96a9a4c3473d9d155f0bae38e5000fc2bb96cba",
  "source_text_sha256": "3fe766d279b5b1589c59f28ab96a9a4c3473d9d155f0bae38e5000fc2bb96cba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebe0",
        "00bdebef"
      ]
    ],
    "bytes_sha256": "4c959aa972955fd636dda9a2193ebf79ddbb9ae3234a1e4cd70efa983977a2ff",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afc63c](../00afc/00afc63c.md)
- [00afc910](../00afc/00afc910.md)
- [00afc98c](../00afc/00afc98c.md)

## 呼び出し先

- [00afcb88](../00afc/00afcb88.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 393 bytes

~~~c

void _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE
               (void)

{
  (*(code *)
    PTR__ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE_00c1de28
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebe0"></a> `00bdebe0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdebe4"></a> `00bdebe4` | `11 16 47 f9` | ldr x17,[x16, #0xe28] | `FALL_THROUGH`
<a id="insn-00bdebe8"></a> `00bdebe8` | `10 a2 38 91` | add x16,x16,#0xe28 | `FALL_THROUGH`
<a id="insn-00bdebec"></a> `00bdebec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebe0`](#insn-00bdebe0) 範囲 `[['00bdebe0', '00bdebef']]`

## 命令位置別の参照

- [`00bdebe4`](#insn-00bdebe4) → `00c1de28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdebec`](#insn-00bdebec) → [`00afcb88`](../00afc/00afcb88.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afcb88` · 推定シンボル `_ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebe4`](#insn-00bdebe4)

~~~json
{
  "source": "00bdebe4",
  "target": "00c1de28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdebec`](#insn-00bdebec)

~~~json
{
  "source": "00bdebec",
  "target": "00afcb88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
