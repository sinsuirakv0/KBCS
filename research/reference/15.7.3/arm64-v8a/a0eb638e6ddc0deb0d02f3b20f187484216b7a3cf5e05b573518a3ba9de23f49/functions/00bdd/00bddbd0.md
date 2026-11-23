# 00bddbd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddb20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-111f73325de7fb8222045a4cbd8ea430)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddc20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-08f683f13daea917d7076fbf47014dae)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbd0",
  "name": "_ZN8firebase5Mutex7AcquireEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "945cd1c5b8cdecd47b1001d5554e1ef4fc693cef6e6b87d15d4ede8eebe371e9",
  "source_text_sha256": "945cd1c5b8cdecd47b1001d5554e1ef4fc693cef6e6b87d15d4ede8eebe371e9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbd0",
        "00bddbdf"
      ]
    ],
    "bytes_sha256": "2fa26f5b70a0ae396f7716c241d3b83986643666ffb6812b2246ce28112accdb",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00848b34](../00848/00848b34.md)
- [00848bc0](../00848/00848bc0.md)
- [0084914c](../00849/0084914c.md)
- [008496cc](../00849/008496cc.md)
- [00849cd4](../00849/00849cd4.md)
- [00ad4ff4](../00ad4/00ad4ff4.md)
- [00ad5578](../00ad5/00ad5578.md)
- [00ae037c](../00ae0/00ae037c.md)
- [00ae2e1c](../00ae2/00ae2e1c.md)
- [00ae3258](../00ae3/00ae3258.md)
- [00ae3554](../00ae3/00ae3554.md)
- [00ae3894](../00ae3/00ae3894.md)
- [00ae3b80](../00ae3/00ae3b80.md)
- [00ae3ca4](../00ae3/00ae3ca4.md)
- [00ae3e0c](../00ae3/00ae3e0c.md)
- [00ae3f60](../00ae3/00ae3f60.md)
- [00af8e50](../00af8/00af8e50.md)
- [00af91c4](../00af9/00af91c4.md)
- [00af9330](../00af9/00af9330.md)
- [00af9398](../00af9/00af9398.md)
- [00af9550](../00af9/00af9550.md)
- [00af9760](../00af9/00af9760.md)
- [00af9a1c](../00af9/00af9a1c.md)
- [00afa148](../00afa/00afa148.md)
- [00afa2a0](../00afa/00afa2a0.md)
- [00afa3b0](../00afa/00afa3b0.md)
- [00afa430](../00afa/00afa430.md)
- [00afa59c](../00afa/00afa59c.md)
- [00afa88c](../00afa/00afa88c.md)
- [00afb754](../00afb/00afb754.md)
- [00afb7e8](../00afb/00afb7e8.md)
- [00afb83c](../00afb/00afb83c.md)
- [00afb944](../00afb/00afb944.md)
- [00afba04](../00afb/00afba04.md)
- [00afbabc](../00afb/00afbabc.md)
- [00afbd1c](../00afb/00afbd1c.md)
- [00afbe48](../00afb/00afbe48.md)
- [00afbf34](../00afb/00afbf34.md)
- [00afc06c](../00afc/00afc06c.md)
- [00afc204](../00afc/00afc204.md)
- [00afc280](../00afc/00afc280.md)
- [00afc304](../00afc/00afc304.md)
- [00afc428](../00afc/00afc428.md)
- [00afc52c](../00afc/00afc52c.md)
- [00afc5ac](../00afc/00afc5ac.md)
- [00afc694](../00afc/00afc694.md)
- [00afc704](../00afc/00afc704.md)
- [00afc7c8](../00afc/00afc7c8.md)
- [00afc8f8](../00afc/00afc8f8.md)
- [00afc9d8](../00afc/00afc9d8.md)
- [00afca54](../00afc/00afca54.md)
- [00afcc50](../00afc/00afcc50.md)
- [00afcd70](../00afc/00afcd70.md)
- [00afe760](../00afe/00afe760.md)
- [00afeae0](../00afe/00afeae0.md)
- [00afecfc](../00afe/00afecfc.md)
- [00aff018](../00aff/00aff018.md)
- [00aff21c](../00aff/00aff21c.md)
- [00aff2fc](../00aff/00aff2fc.md)
- [00aff3ac](../00aff/00aff3ac.md)
- [00aff430](../00aff/00aff430.md)
- [00aff764](../00aff/00aff764.md)
- [00aff7c8](../00aff/00aff7c8.md)
- [00aff810](../00aff/00aff810.md)
- [00aff86c](../00aff/00aff86c.md)
- [00aff908](../00aff/00aff908.md)
- [00affa2c](../00aff/00affa2c.md)
- [00affad4](../00aff/00affad4.md)
- [00affb7c](../00aff/00affb7c.md)
- [00affc3c](../00aff/00affc3c.md)
- [00affcec](../00aff/00affcec.md)
- [00affea0](../00aff/00affea0.md)
- [00b00094](../00b00/00b00094.md)
- [00b0032c](../00b00/00b0032c.md)
- [00b003ec](../00b00/00b003ec.md)
- [00b00424](../00b00/00b00424.md)
- [00b00578](../00b00/00b00578.md)
- [00b00638](../00b00/00b00638.md)
- [00b00a40](../00b00/00b00a40.md)
- [00b00b70](../00b00/00b00b70.md)
- [00b00c28](../00b00/00b00c28.md)
- [00b00f3c](../00b00/00b00f3c.md)
- [00b0129c](../00b01/00b0129c.md)
- [00b0151c](../00b01/00b0151c.md)
- [00b016d0](../00b01/00b016d0.md)
- [00b018ac](../00b01/00b018ac.md)
- [00b0190c](../00b01/00b0190c.md)
- [00b01ae4](../00b01/00b01ae4.md)
- [00b01bb8](../00b01/00b01bb8.md)
- [00b01d00](../00b01/00b01d00.md)
- [00b01e80](../00b01/00b01e80.md)
- [00b0221c](../00b02/00b0221c.md)
- [00b02330](../00b02/00b02330.md)
- [00b02854](../00b02/00b02854.md)
- [00b0e154](../00b0e/00b0e154.md)
- [00b48c44](../00b48/00b48c44.md)
- [00b48d48](../00b48/00b48d48.md)
- [00b48da0](../00b48/00b48da0.md)
- [00b48e10](../00b48/00b48e10.md)
- [00b490a0](../00b49/00b490a0.md)
- [00b491b4](../00b49/00b491b4.md)
- [00b49228](../00b49/00b49228.md)
- [00b49370](../00b49/00b49370.md)
- [00b4b4dc](../00b4b/00b4b4dc.md)
- [00b4b7b0](../00b4b/00b4b7b0.md)
- [00b4b884](../00b4b/00b4b884.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b4ca64](../00b4c/00b4ca64.md)
- [00b4cda8](../00b4c/00b4cda8.md)
- [00b4ce90](../00b4c/00b4ce90.md)
- [00b4d204](../00b4d/00b4d204.md)
- [00b4d6d0](../00b4d/00b4d6d0.md)
- [00b4d7a8](../00b4d/00b4d7a8.md)
- [00b4dc74](../00b4d/00b4dc74.md)
- [00b4de04](../00b4d/00b4de04.md)
- [00b4e0e0](../00b4e/00b4e0e0.md)
- [00b4e368](../00b4e/00b4e368.md)
- [00b4e440](../00b4e/00b4e440.md)
- [00b4e6a8](../00b4e/00b4e6a8.md)
- [00b4e7c0](../00b4e/00b4e7c0.md)
- [00b4e89c](../00b4e/00b4e89c.md)
- [00b4ea4c](../00b4e/00b4ea4c.md)
- [00b5257c](../00b52/00b5257c.md)
- [00b527d0](../00b52/00b527d0.md)
- [00b52864](../00b52/00b52864.md)
- [00b54af4](../00b54/00b54af4.md)
- [00b55700](../00b55/00b55700.md)
- [00b55964](../00b55/00b55964.md)
- [00b561b4](../00b56/00b561b4.md)
- [00b5674c](../00b56/00b5674c.md)
- [00b56a78](../00b56/00b56a78.md)
- [00b56da4](../00b56/00b56da4.md)
- [00b570cc](../00b57/00b570cc.md)
- [00b58034](../00b58/00b58034.md)
- [00b58488](../00b58/00b58488.md)
- [00b58d80](../00b58/00b58d80.md)
- [00b5a058](../00b5a/00b5a058.md)
- [00b5a184](../00b5a/00b5a184.md)
- [00b5a2b4](../00b5a/00b5a2b4.md)
- [00b5a468](../00b5a/00b5a468.md)
- [00b5ab78](../00b5a/00b5ab78.md)
- [00b5ad94](../00b5a/00b5ad94.md)
- [00b5b0d0](../00b5b/00b5b0d0.md)
- [00b5b4c8](../00b5b/00b5b4c8.md)
- [00b5b698](../00b5b/00b5b698.md)
- [00b5b870](../00b5b/00b5b870.md)
- [00b5b984](../00b5b/00b5b984.md)
- [00b5bbe8](../00b5b/00b5bbe8.md)
- [00b5be10](../00b5b/00b5be10.md)
- [00b5c038](../00b5c/00b5c038.md)
- [00b5c0c8](../00b5c/00b5c0c8.md)
- [00b5c158](../00b5c/00b5c158.md)
- [00b5c1e8](../00b5c/00b5c1e8.md)
- [00b5c278](../00b5c/00b5c278.md)
- [00b5c308](../00b5c/00b5c308.md)
- [00b5c398](../00b5c/00b5c398.md)
- [00b5da44](../00b5d/00b5da44.md)
- [00b5e200](../00b5e/00b5e200.md)
- [00b5f838](../00b5f/00b5f838.md)
- [00b5faac](../00b5f/00b5faac.md)
- [00b5ffb8](../00b5f/00b5ffb8.md)
- [00b60194](../00b60/00b60194.md)
- [00b604ac](../00b60/00b604ac.md)
- [00b60698](../00b60/00b60698.md)
- [00b60874](../00b60/00b60874.md)
- [00b60a4c](../00b60/00b60a4c.md)
- [00b60c28](../00b60/00b60c28.md)
- [00b6abc8](../00b6a/00b6abc8.md)
- [00b6cae8](../00b6c/00b6cae8.md)
- [00b6d2ec](../00b6d/00b6d2ec.md)
- [00b6ed38](../00b6e/00b6ed38.md)
- [00b6eeac](../00b6e/00b6eeac.md)
- [00b71940](../00b71/00b71940.md)
- [00b71b1c](../00b71/00b71b1c.md)
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

- [00b05474](../00b05/00b05474.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZN8firebase5Mutex7AcquireEv(void)

{
  (*(code *)PTR__ZN8firebase5Mutex7AcquireEv_00c1d678)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbd0"></a> `00bddbd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbd4"></a> `00bddbd4` | `11 3e 43 f9` | ldr x17,[x16, #0x678] | `FALL_THROUGH`
<a id="insn-00bddbd8"></a> `00bddbd8` | `10 e2 19 91` | add x16,x16,#0x678 | `FALL_THROUGH`
<a id="insn-00bddbdc"></a> `00bddbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbd0`](#insn-00bddbd0) 範囲 `[['00bddbd0', '00bddbdf']]`

## 命令位置別の参照

- [`00bddbd4`](#insn-00bddbd4) → `00c1d678`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbdc`](#insn-00bddbdc) → [`00b05474`](../00b05/00b05474.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b05474` · 推定シンボル `_ZN8firebase5Mutex7AcquireEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbd4`](#insn-00bddbd4)

~~~json
{
  "source": "00bddbd4",
  "target": "00c1d678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d678",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbdc`](#insn-00bddbdc)

~~~json
{
  "source": "00bddbdc",
  "target": "00b05474",
  "target_space": "ram",
  "resolution": "function"
}
~~~
