# 00bdddb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-534021d139a0ffa21848e223a912b0dd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a810`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-c4025c594e0a55c334664f2e13a5a595)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddb0",
  "name": "_ZN8firebase15CleanupNotifier16UnregisterObjectEPv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d697d2a3920f5a8c90069e019d6945fe6ca2b557333fbfc94c4336c82c35aca",
  "source_text_sha256": "1d697d2a3920f5a8c90069e019d6945fe6ca2b557333fbfc94c4336c82c35aca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddb0",
        "00bdddbf"
      ]
    ],
    "bytes_sha256": "441d1e071885db566b298c54e917bd0e6d14894b48322af2c62d5b6facaf782e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae01c0](../00ae0/00ae01c0.md)
- [00afc5f0](../00afc/00afc5f0.md)
- [00afc6d8](../00afc/00afc6d8.md)
- [00afe7a4](../00afe/00afe7a4.md)
- [00afed40](../00afe/00afed40.md)
- [00aff05c](../00aff/00aff05c.md)
- [00aff474](../00aff/00aff474.md)
- [00aff8a8](../00aff/00aff8a8.md)
- [00b0067c](../00b00/00b0067c.md)
- [00b00a84](../00b00/00b00a84.md)
- [00b00d08](../00b00/00b00d08.md)
- [00b00db8](../00b00/00b00db8.md)
- [00b00e44](../00b00/00b00e44.md)
- [00b00ea4](../00b00/00b00ea4.md)
- [00b00f38](../00b00/00b00f38.md)
- [00b010fc](../00b01/00b010fc.md)
- [00b012e0](../00b01/00b012e0.md)
- [00b48c48](../00b48/00b48c48.md)
- [00b528a8](../00b52/00b528a8.md)
- [00b5a7cc](../00b5a/00b5a7cc.md)
- [00b5a890](../00b5a/00b5a890.md)
- [00b5a8d8](../00b5a/00b5a8d8.md)
- [00b5a920](../00b5a/00b5a920.md)
- [00b5a984](../00b5a/00b5a984.md)
- [00b5b114](../00b5b/00b5b114.md)

## 呼び出し先

- [00afc93c](../00afc/00afc93c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 159 bytes

~~~c

void _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifier16UnregisterObjectEPv_00c1d790)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddb0"></a> `00bdddb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddb4"></a> `00bdddb4` | `11 ca 43 f9` | ldr x17,[x16, #0x790] | `FALL_THROUGH`
<a id="insn-00bdddb8"></a> `00bdddb8` | `10 42 1e 91` | add x16,x16,#0x790 | `FALL_THROUGH`
<a id="insn-00bdddbc"></a> `00bdddbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddb0`](#insn-00bdddb0) 範囲 `[['00bdddb0', '00bdddbf']]`

## 命令位置別の参照

- [`00bdddb4`](#insn-00bdddb4) → `00c1d790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddbc`](#insn-00bdddbc) → [`00afc93c`](../00afc/00afc93c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc93c` · 推定シンボル `_ZN8firebase15CleanupNotifier16UnregisterObjectEPv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddb4`](#insn-00bdddb4)

~~~json
{
  "source": "00bdddb4",
  "target": "00c1d790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d790",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddbc`](#insn-00bdddbc)

~~~json
{
  "source": "00bdddbc",
  "target": "00afc93c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
