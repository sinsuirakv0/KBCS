# 00bdeea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdee50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-e5e84c8418cdde009f3da14ed6d4ed52)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5b950`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b950.md) · 移動量 `+0x7cab0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-f1c6473741a5cece3b94bfaaeb41305a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeea0",
  "name": "_ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "184c82270635f582b559885abf5d86cb913dd910a241506a59dfbb98bcc34823",
  "source_text_sha256": "184c82270635f582b559885abf5d86cb913dd910a241506a59dfbb98bcc34823",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeea0",
        "00bdeeaf"
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

- [00b014b4](../00b01/00b014b4.md)

## 呼び出し先

- [00b01560](../00b01/00b01560.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 233 bytes

~~~c

void _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em(void)

{
  (*(code *)
    PTR__ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em_00c1e008
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeea0"></a> `00bdeea0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdeea4"></a> `00bdeea4` | `11 06 40 f9` | ldr x17,[x16, #0x8] | `FALL_THROUGH`
<a id="insn-00bdeea8"></a> `00bdeea8` | `10 22 00 91` | add x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bdeeac"></a> `00bdeeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeea0`](#insn-00bdeea0) 範囲 `[['00bdeea0', '00bdeeaf']]`

## 命令位置別の参照

- [`00bdeea4`](#insn-00bdeea4) → `00c1e008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeeac`](#insn-00bdeeac) → [`00b01560`](../00b01/00b01560.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b01560` · 推定シンボル `_ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeea4`](#insn-00bdeea4)

~~~json
{
  "source": "00bdeea4",
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
- 参照命令 [`00bdeeac`](#insn-00bdeeac)

~~~json
{
  "source": "00bdeeac",
  "target": "00b01560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
