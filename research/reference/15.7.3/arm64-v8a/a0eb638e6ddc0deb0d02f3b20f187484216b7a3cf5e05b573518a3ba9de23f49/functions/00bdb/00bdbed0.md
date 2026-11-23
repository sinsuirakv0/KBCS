# 00bdbed0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbe20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-5943ae721a61662af41ddd1b64119ab1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbf20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-6b6b9513ccc01106fd8cd75f4d76540f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbed0",
  "name": "_ZNK5Botan8CBC_Mode4nameEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90ccbc98f3907fdde1c3d40f40747c43120dd05bd6c7267135f9c71b060a8cf7",
  "source_text_sha256": "90ccbc98f3907fdde1c3d40f40747c43120dd05bd6c7267135f9c71b060a8cf7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbed0",
        "00bdbedf"
      ]
    ],
    "bytes_sha256": "446c0d1af6229161be8e6bd6c37c7db65a77d39464dfa573492d3e94deded983",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049a380](../0049a/0049a380.md)
- [0049af04](../0049a/0049af04.md)

## 呼び出し先

- [00499860](../00499/00499860.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 111 bytes

~~~c

void _ZNK5Botan8CBC_Mode4nameEv(void)

{
  (*(code *)PTR__ZNK5Botan8CBC_Mode4nameEv_00c1c7f8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbed0"></a> `00bdbed0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbed4"></a> `00bdbed4` | `11 fe 43 f9` | ldr x17,[x16, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bdbed8"></a> `00bdbed8` | `10 e2 1f 91` | add x16,x16,#0x7f8 | `FALL_THROUGH`
<a id="insn-00bdbedc"></a> `00bdbedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbed0`](#insn-00bdbed0) 範囲 `[['00bdbed0', '00bdbedf']]`

## 命令位置別の参照

- [`00bdbed4`](#insn-00bdbed4) → `00c1c7f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbedc`](#insn-00bdbedc) → [`00499860`](../00499/00499860.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00499860` · 推定シンボル `_ZNK5Botan8CBC_Mode4nameEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbed4`](#insn-00bdbed4)

~~~json
{
  "source": "00bdbed4",
  "target": "00c1c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbedc`](#insn-00bdbedc)

~~~json
{
  "source": "00bdbedc",
  "target": "00499860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
