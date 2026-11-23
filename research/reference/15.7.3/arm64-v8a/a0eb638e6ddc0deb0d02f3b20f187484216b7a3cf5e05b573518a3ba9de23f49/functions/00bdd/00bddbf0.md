# 00bddbf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddb40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-e497c3cc45667e4e0a9ef2f3427e7e94)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddc40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-404a82df285e9b5fe51d876ee709d635)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbf0",
  "name": "_ZN8firebase12FutureHandleD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c5331982ab268af39aed760ee5540aea370887c9fd99591a2d9eb1007654409",
  "source_text_sha256": "5c5331982ab268af39aed760ee5540aea370887c9fd99591a2d9eb1007654409",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbf0",
        "00bddbff"
      ]
    ],
    "bytes_sha256": "1780f617159fa6fd626a8b9be0b2b6101655c1096c035913e116a94cb6c837ad",
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
- [00ae037c](../00ae0/00ae037c.md)
- [00ae2bc8](../00ae2/00ae2bc8.md)
- [00ae2f90](../00ae2/00ae2f90.md)
- [00ae3330](../00ae3/00ae3330.md)
- [00ae3894](../00ae3/00ae3894.md)
- [00ae3a08](../00ae3/00ae3a08.md)
- [00b013b0](../00b01/00b013b0.md)
- [00b01410](../00b01/00b01410.md)
- [00b0151c](../00b01/00b0151c.md)
- [00b016d0](../00b01/00b016d0.md)
- [00b02854](../00b02/00b02854.md)
- [00b0d740](../00b0d/00b0d740.md)
- [00b0db4c](../00b0d/00b0db4c.md)
- [00b0ddbc](../00b0d/00b0ddbc.md)
- [00b0df30](../00b0d/00b0df30.md)
- [00b0e1e8](../00b0e/00b0e1e8.md)
- [00b4b688](../00b4b/00b4b688.md)
- [00b4ce90](../00b4c/00b4ce90.md)
- [00b4d204](../00b4d/00b4d204.md)
- [00b4d4d4](../00b4d/00b4d4d4.md)
- [00b4d7a8](../00b4d/00b4d7a8.md)
- [00b4da78](../00b4d/00b4da78.md)
- [00b4de04](../00b4d/00b4de04.md)
- [00b4e0e0](../00b4e/00b4e0e0.md)
- [00b4e440](../00b4e/00b4e440.md)
- [00b4e6a8](../00b4e/00b4e6a8.md)
- [00b4e904](../00b4e/00b4e904.md)
- [00b4eb14](../00b4e/00b4eb14.md)
- [00b4ec70](../00b4e/00b4ec70.md)
- [00b55d08](../00b55/00b55d08.md)
- [00b55efc](../00b55/00b55efc.md)
- [00b5602c](../00b56/00b5602c.md)
- [00b564b0](../00b56/00b564b0.md)
- [00b567dc](../00b56/00b567dc.md)
- [00b56b08](../00b56/00b56b08.md)
- [00b56e34](../00b56/00b56e34.md)
- [00b5715c](../00b57/00b5715c.md)
- [00b573f4](../00b57/00b573f4.md)
- [00b57b08](../00b57/00b57b08.md)
- [00b580c4](../00b58/00b580c4.md)
- [00b5e244](../00b5e/00b5e244.md)
- [00b5e444](../00b5e/00b5e444.md)
- [00b5e75c](../00b5e/00b5e75c.md)
- [00b5e920](../00b5e/00b5e920.md)
- [00b5ea6c](../00b5e/00b5ea6c.md)
- [00b5eb70](../00b5e/00b5eb70.md)
- [00b5ed5c](../00b5e/00b5ed5c.md)
- [00b5ee20](../00b5e/00b5ee20.md)
- [00b5ef24](../00b5e/00b5ef24.md)
- [00b5f194](../00b5f/00b5f194.md)
- [00b5f320](../00b5f/00b5f320.md)
- [00b5f5ac](../00b5f/00b5f5ac.md)
- [00b5fb44](../00b5f/00b5fb44.md)
- [00b5fd90](../00b5f/00b5fd90.md)
- [00b600c0](../00b60/00b600c0.md)
- [00b603d8](../00b60/00b603d8.md)
- [00b607a0](../00b60/00b607a0.md)
- [00b60b54](../00b60/00b60b54.md)
- [00b6aaa4](../00b6a/00b6aaa4.md)
- [00b6bf28](../00b6b/00b6bf28.md)
- [00b6c200](../00b6c/00b6c200.md)
- [00b6c50c](../00b6c/00b6c50c.md)
- [00b6c7e4](../00b6c/00b6c7e4.md)
- [00b6d210](../00b6d/00b6d210.md)
- [00b6eeac](../00b6e/00b6eeac.md)
- [00b6f10c](../00b6f/00b6f10c.md)
- [00b6fde4](../00b6f/00b6fde4.md)
- [00b7000c](../00b70/00b7000c.md)
- [00b70434](../00b70/00b70434.md)
- [00b70690](../00b70/00b70690.md)
- [00b70898](../00b70/00b70898.md)
- [00b70ae4](../00b70/00b70ae4.md)
- [00b70cd4](../00b70/00b70cd4.md)
- [00b70ecc](../00b70/00b70ecc.md)
- [00b71128](../00b71/00b71128.md)
- [00b71318](../00b71/00b71318.md)
- [00b71540](../00b71/00b71540.md)
- [00b71a48](../00b71/00b71a48.md)

## 呼び出し先

- [00b00cc4](../00b00/00b00cc4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN8firebase12FutureHandleD1Ev(void)

{
  (*(code *)PTR__ZN8firebase12FutureHandleD1Ev_00c1d688)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbf0"></a> `00bddbf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbf4"></a> `00bddbf4` | `11 46 43 f9` | ldr x17,[x16, #0x688] | `FALL_THROUGH`
<a id="insn-00bddbf8"></a> `00bddbf8` | `10 22 1a 91` | add x16,x16,#0x688 | `FALL_THROUGH`
<a id="insn-00bddbfc"></a> `00bddbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbf0`](#insn-00bddbf0) 範囲 `[['00bddbf0', '00bddbff']]`

## 命令位置別の参照

- [`00bddbf4`](#insn-00bddbf4) → `00c1d688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbfc`](#insn-00bddbfc) → [`00b00cc4`](../00b00/00b00cc4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b00cc4` · 推定シンボル `_ZN8firebase12FutureHandleD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbf4`](#insn-00bddbf4)

~~~json
{
  "source": "00bddbf4",
  "target": "00c1d688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d688",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbfc`](#insn-00bddbfc)

~~~json
{
  "source": "00bddbfc",
  "target": "00b00cc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
