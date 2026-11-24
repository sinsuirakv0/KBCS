# 00bddcc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-15681712b56935e15381a96e21cbd6e1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a710`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a710.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-8dc1f4a987f5175f1abdf078736b6d4b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcc0",
  "name": "_ZNK8firebase7Variant8AsStringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1447cd5e2d20c4f93293dd3a9aa48e0717fe732deaf8f746e738008933e246cf",
  "source_text_sha256": "1447cd5e2d20c4f93293dd3a9aa48e0717fe732deaf8f746e738008933e246cf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcc0",
        "00bddccf"
      ]
    ],
    "bytes_sha256": "830380e60d1b508bcd14670a749081e9e36a623e8a37cac58420b5ddb25adddd",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a9ec](../0084a/0084a9ec.md)

## 呼び出し先

- [00b046d0](../00b04/00b046d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZNK8firebase7Variant8AsStringEv(void)

{
  (*(code *)PTR__ZNK8firebase7Variant8AsStringEv_00c1d718)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcc0"></a> `00bddcc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcc4"></a> `00bddcc4` | `11 8e 43 f9` | ldr x17,[x16, #0x718] | `FALL_THROUGH`
<a id="insn-00bddcc8"></a> `00bddcc8` | `10 62 1c 91` | add x16,x16,#0x718 | `FALL_THROUGH`
<a id="insn-00bddccc"></a> `00bddccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcc0`](#insn-00bddcc0) 範囲 `[['00bddcc0', '00bddccf']]`

## 命令位置別の参照

- [`00bddcc4`](#insn-00bddcc4) → `00c1d718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddccc`](#insn-00bddccc) → [`00b046d0`](../00b04/00b046d0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b046d0` · 推定シンボル `_ZNK8firebase7Variant8AsStringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcc4`](#insn-00bddcc4)

~~~json
{
  "source": "00bddcc4",
  "target": "00c1d718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d718",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddccc`](#insn-00bddccc)

~~~json
{
  "source": "00bddccc",
  "target": "00b046d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
