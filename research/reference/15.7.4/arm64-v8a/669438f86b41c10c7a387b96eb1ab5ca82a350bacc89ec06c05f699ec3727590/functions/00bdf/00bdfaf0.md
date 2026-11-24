# 00bdfaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfaa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfaa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-189d6852a82204e8754c09aef9b718b1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c4a0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4a0.md) · 移動量 `+0x7c9b0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0015.md#compare-f132d6bf22de5485787ffde4a4ff9454)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfaf0",
  "name": "_ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a01d38479e2a240ddbd8e26187d97ceddaea627074622025b4e438fb6891ae0",
  "source_text_sha256": "2a01d38479e2a240ddbd8e26187d97ceddaea627074622025b4e438fb6891ae0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfaf0",
        "00bdfaff"
      ]
    ],
    "bytes_sha256": "a6b27b293044fda7074800c15ad0302324f7ad9b082ff53c97ced056a7770dc5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b33b08](../00b33/00b33b08.md)

## 呼び出し先

- [00b33c60](../00b33/00b33c60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE(void)

{
  (*(code *)PTR__ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE_00c1e630)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfaf0"></a> `00bdfaf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfaf4"></a> `00bdfaf4` | `11 1a 43 f9` | ldr x17,[x16, #0x630] | `FALL_THROUGH`
<a id="insn-00bdfaf8"></a> `00bdfaf8` | `10 c2 18 91` | add x16,x16,#0x630 | `FALL_THROUGH`
<a id="insn-00bdfafc"></a> `00bdfafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfaf0`](#insn-00bdfaf0) 範囲 `[['00bdfaf0', '00bdfaff']]`

## 命令位置別の参照

- [`00bdfaf4`](#insn-00bdfaf4) → `00c1e630`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfafc`](#insn-00bdfafc) → [`00b33c60`](../00b33/00b33c60.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b33c60` · 推定シンボル `_ZN11flexbuffers7Builder10CreateBlobEPKvmmNS_4TypeE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfaf4`](#insn-00bdfaf4)

~~~json
{
  "source": "00bdfaf4",
  "target": "00c1e630",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e630",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfafc`](#insn-00bdfafc)

~~~json
{
  "source": "00bdfafc",
  "target": "00b33c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
