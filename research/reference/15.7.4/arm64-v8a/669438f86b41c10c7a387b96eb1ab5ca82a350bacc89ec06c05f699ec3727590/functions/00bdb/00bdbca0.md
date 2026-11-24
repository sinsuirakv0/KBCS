# 00bdbca0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-3ca9ee0b59de330586dc1666f6b6e2bb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-57f152323aae02a52d53fd27e5b7495b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbca0",
  "name": "_ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd503ee5366bc608ceb87c24f20caf980920d724f1e583fd31d99ed01e2ebc2e",
  "source_text_sha256": "cd503ee5366bc608ceb87c24f20caf980920d724f1e583fd31d99ed01e2ebc2e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbca0",
        "00bdbcaf"
      ]
    ],
    "bytes_sha256": "5f728c6be1459a1ce0bf1813326cf3a09b23538cdb6611309fcc2fab9530fd77",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048e994](../0048e/0048e994.md)
- [0048ec7c](../0048e/0048ec7c.md)

## 呼び出し先

- [00483728](../00483/00483728.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 297 bytes

~~~c

void _ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE_00c1c708
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbca0"></a> `00bdbca0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbca4"></a> `00bdbca4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bdbca8"></a> `00bdbca8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bdbcac"></a> `00bdbcac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbca0`](#insn-00bdbca0) 範囲 `[['00bdbca0', '00bdbcaf']]`

## 命令位置別の参照

- [`00bdbca4`](#insn-00bdbca4) → `00c1c708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcac`](#insn-00bdbcac) → [`00483728`](../00483/00483728.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00483728` · 推定シンボル `_ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbca4`](#insn-00bdbca4)

~~~json
{
  "source": "00bdbca4",
  "target": "00c1c708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcac`](#insn-00bdbcac)

~~~json
{
  "source": "00bdbcac",
  "target": "00483728",
  "target_space": "ram",
  "resolution": "function"
}
~~~
