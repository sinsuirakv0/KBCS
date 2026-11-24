# 00bdbff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbfa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-27dc7d3fa3e21fa4bd558e570676d471)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-e1650cef63cac1264a67bc305b3617fc)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbff0",
  "name": "_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca904d33db33178c6e3791956e23c0588414fa8634853766a98c2bb17d953063",
  "source_text_sha256": "ca904d33db33178c6e3791956e23c0588414fa8634853766a98c2bb17d953063",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbff0",
        "00bdbfff"
      ]
    ],
    "bytes_sha256": "c56554925a62ec88ea83e59b89fa3759dcda8a88658bf0722f3c21660c431d8a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a0c64](../004a0/004a0c64.md)

## 呼び出し先

- [004a0a28](../004a0/004a0a28.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE_00c1c8b0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbff0"></a> `00bdbff0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbff4"></a> `00bdbff4` | `11 5a 44 f9` | ldr x17,[x16, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bdbff8"></a> `00bdbff8` | `10 c2 22 91` | add x16,x16,#0x8b0 | `FALL_THROUGH`
<a id="insn-00bdbffc"></a> `00bdbffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbff0`](#insn-00bdbff0) 範囲 `[['00bdbff0', '00bdbfff']]`

## 命令位置別の参照

- [`00bdbff4`](#insn-00bdbff4) → `00c1c8b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbffc`](#insn-00bdbffc) → [`004a0a28`](../004a0/004a0a28.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004a0a28` · 推定シンボル `_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbff4`](#insn-00bdbff4)

~~~json
{
  "source": "00bdbff4",
  "target": "00c1c8b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c8b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbffc`](#insn-00bdbffc)

~~~json
{
  "source": "00bdbffc",
  "target": "004a0a28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
