# 00bddea0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdddf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-3301a2380ed39c108a3fb701bdcd15c8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddef0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-4a30a2ebc50e5f5a7dc8aed0187661f2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddea0",
  "name": "_ZN8firebase10FutureBaseaSERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "498b18b7bfd614b3bc9ad415b87a7708a27053df4a550cab70a5a5a90d14955f",
  "source_text_sha256": "498b18b7bfd614b3bc9ad415b87a7708a27053df4a550cab70a5a5a90d14955f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddea0",
        "00bddeaf"
      ]
    ],
    "bytes_sha256": "fa405274c6b085218c1fa11658c989b266614c6b2546c2cd39202ec0f2251688",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2e1c](../00ae2/00ae2e1c.md)
- [00ae3258](../00ae3/00ae3258.md)
- [00b00638](../00b00/00b00638.md)
- [00b0151c](../00b01/00b0151c.md)
- [00b018ac](../00b01/00b018ac.md)
- [00b0e154](../00b0e/00b0e154.md)
- [00b4b7b0](../00b4b/00b4b7b0.md)
- [00b4d6d0](../00b4d/00b4d6d0.md)
- [00b4dc74](../00b4d/00b4dc74.md)
- [00b4e368](../00b4e/00b4e368.md)
- [00b4e7c0](../00b4e/00b4e7c0.md)
- [00b5674c](../00b56/00b5674c.md)
- [00b56a78](../00b56/00b56a78.md)
- [00b56da4](../00b56/00b56da4.md)
- [00b570cc](../00b57/00b570cc.md)
- [00b58034](../00b58/00b58034.md)
- [00b58488](../00b58/00b58488.md)
- [00b5c038](../00b5c/00b5c038.md)
- [00b5c0c8](../00b5c/00b5c0c8.md)
- [00b5c158](../00b5c/00b5c158.md)
- [00b5c1e8](../00b5c/00b5c1e8.md)
- [00b5c278](../00b5c/00b5c278.md)
- [00b5c308](../00b5c/00b5c308.md)
- [00b5c398](../00b5c/00b5c398.md)
- [00b6abc8](../00b6a/00b6abc8.md)
- [00b71f6c](../00b71/00b71f6c.md)
- [00b71ffc](../00b71/00b71ffc.md)
- [00b7208c](../00b72/00b7208c.md)
- [00b7211c](../00b72/00b7211c.md)
- [00b721ac](../00b72/00b721ac.md)
- [00b7223c](../00b72/00b7223c.md)
- [00b722cc](../00b72/00b722cc.md)
- [00b7235c](../00b72/00b7235c.md)
- [00b723ec](../00b72/00b723ec.md)
- [00b7247c](../00b72/00b7247c.md)
- [00b7250c](../00b72/00b7250c.md)
- [00b7259c](../00b72/00b7259c.md)
- [00b7262c](../00b72/00b7262c.md)

## 呼び出し先

- [00ae3894](../00ae3/00ae3894.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN8firebase10FutureBaseaSERKS0_(void)

{
  (*(code *)PTR__ZN8firebase10FutureBaseaSERKS0__00c1d7e0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddea0"></a> `00bddea0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddea4"></a> `00bddea4` | `11 f2 43 f9` | ldr x17,[x16, #0x7e0] | `FALL_THROUGH`
<a id="insn-00bddea8"></a> `00bddea8` | `10 82 1f 91` | add x16,x16,#0x7e0 | `FALL_THROUGH`
<a id="insn-00bddeac"></a> `00bddeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddea0`](#insn-00bddea0) 範囲 `[['00bddea0', '00bddeaf']]`

## 命令位置別の参照

- [`00bddea4`](#insn-00bddea4) → `00c1d7e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddeac`](#insn-00bddeac) → [`00ae3894`](../00ae3/00ae3894.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae3894` · 推定シンボル `_ZN8firebase10FutureBaseaSERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddea4`](#insn-00bddea4)

~~~json
{
  "source": "00bddea4",
  "target": "00c1d7e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddeac`](#insn-00bddeac)

~~~json
{
  "source": "00bddeac",
  "target": "00ae3894",
  "target_space": "ram",
  "resolution": "function"
}
~~~
