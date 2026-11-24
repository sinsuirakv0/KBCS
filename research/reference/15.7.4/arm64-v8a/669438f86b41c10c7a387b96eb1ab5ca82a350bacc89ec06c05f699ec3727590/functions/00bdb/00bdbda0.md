# 00bdbda0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-2a1c74266fb1e5a037bc0f93486882b5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c587f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-b1a245b9fd37367c324d748fedb76903)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbda0",
  "name": "_ZN5Botan13base64_decodeEPhPKcmb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "282009bd746b027bd3271d70f66896e7284f6c2d85990db45e5eb63f8a190c7d",
  "source_text_sha256": "282009bd746b027bd3271d70f66896e7284f6c2d85990db45e5eb63f8a190c7d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbda0",
        "00bdbdaf"
      ]
    ],
    "bytes_sha256": "f118bf6a6c7086d3fb2e96e9b086098ce5f2d0e3016c6fd91d6ab6b80e3b5d08",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493268](../00493/00493268.md)
- [00493288](../00493/00493288.md)
- [00493354](../00493/00493354.md)
- [004c2f88](../004c2/004c2f88.md)

## 呼び出し先

- [00493150](../00493/00493150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN5Botan13base64_decodeEPhPKcmb(void)

{
  (*(code *)PTR__ZN5Botan13base64_decodeEPhPKcmb_00c1c788)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbda0"></a> `00bdbda0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbda4"></a> `00bdbda4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bdbda8"></a> `00bdbda8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdbdac"></a> `00bdbdac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbda0`](#insn-00bdbda0) 範囲 `[['00bdbda0', '00bdbdaf']]`

## 命令位置別の参照

- [`00bdbda4`](#insn-00bdbda4) → `00c1c788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdac`](#insn-00bdbdac) → [`00493150`](../00493/00493150.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00493150` · 推定シンボル `_ZN5Botan13base64_decodeEPhPKcmb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbda4`](#insn-00bdbda4)

~~~json
{
  "source": "00bdbda4",
  "target": "00c1c788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdac`](#insn-00bdbdac)

~~~json
{
  "source": "00bdbdac",
  "target": "00493150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
