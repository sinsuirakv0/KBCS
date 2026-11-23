# 00bdbee0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbe30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-95095abc2c6c4478ccdd78e5ee158909)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbf30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-adba642f8e8feb5df3e9a4d445e07df7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbee0",
  "name": "_ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a9efec5af8b536bad28d2164edaf2dd4ceef1621ff891842d759e330978c0ee",
  "source_text_sha256": "7a9efec5af8b536bad28d2164edaf2dd4ceef1621ff891842d759e330978c0ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbee0",
        "00bdbeef"
      ]
    ],
    "bytes_sha256": "0cbd193c16caf53db1cf637ff53cb43b4860b03fc97fe6e019a2846109e6a080",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00499b28](../00499/00499b28.md)
- [00513138](../00513/00513138.md)

## 呼び出し先

- [004d7d1c](../004d7/004d7d1c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm
               (void)

{
  (*(code *)
    PTR__ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm_00c1c800
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbee0"></a> `00bdbee0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbee4"></a> `00bdbee4` | `11 02 44 f9` | ldr x17,[x16, #0x800] | `FALL_THROUGH`
<a id="insn-00bdbee8"></a> `00bdbee8` | `10 02 20 91` | add x16,x16,#0x800 | `FALL_THROUGH`
<a id="insn-00bdbeec"></a> `00bdbeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbee0`](#insn-00bdbee0) 範囲 `[['00bdbee0', '00bdbeef']]`

## 命令位置別の参照

- [`00bdbee4`](#insn-00bdbee4) → `00c1c800`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbeec`](#insn-00bdbeec) → [`004d7d1c`](../004d7/004d7d1c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004d7d1c` · 推定シンボル `_ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbee4`](#insn-00bdbee4)

~~~json
{
  "source": "00bdbee4",
  "target": "00c1c800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c800",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbeec`](#insn-00bdbeec)

~~~json
{
  "source": "00bdbeec",
  "target": "004d7d1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
