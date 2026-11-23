# 00bdeef0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdee40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-1c01d5217d3da1c26fc3970413ec1106)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdef40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-cec8c4ef6f67bcd2b6221846d447801c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeef0",
  "name": "_ZNK8firebase7VarianteqERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "623f4d147488cd3b725f1481a3d399449e0d100d8f0bcce3c377085dbb4c3bf4",
  "source_text_sha256": "623f4d147488cd3b725f1481a3d399449e0d100d8f0bcce3c377085dbb4c3bf4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeef0",
        "00bdeeff"
      ]
    ],
    "bytes_sha256": "c7fff1bc5ad61ba13103526c0d5e26c1417b199e4119e43903d3387c0ad52aec",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b03ca4](../00b03/00b03ca4.md)
- [00b04ab4](../00b04/00b04ab4.md)

## 呼び出し先

- [00b03728](../00b03/00b03728.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 117 bytes

~~~c

void _ZNK8firebase7VarianteqERKS0_(void)

{
  (*(code *)PTR__ZNK8firebase7VarianteqERKS0__00c1e008)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeef0"></a> `00bdeef0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdeef4"></a> `00bdeef4` | `11 06 40 f9` | ldr x17,[x16, #0x8] | `FALL_THROUGH`
<a id="insn-00bdeef8"></a> `00bdeef8` | `10 22 00 91` | add x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bdeefc"></a> `00bdeefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeef0`](#insn-00bdeef0) 範囲 `[['00bdeef0', '00bdeeff']]`

## 命令位置別の参照

- [`00bdeef4`](#insn-00bdeef4) → `00c1e008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeefc`](#insn-00bdeefc) → [`00b03728`](../00b03/00b03728.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b03728` · 推定シンボル `_ZNK8firebase7VarianteqERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeef4`](#insn-00bdeef4)

~~~json
{
  "source": "00bdeef4",
  "target": "00c1e008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeefc`](#insn-00bdeefc)

~~~json
{
  "source": "00bdeefc",
  "target": "00b03728",
  "target_space": "ram",
  "resolution": "function"
}
~~~
