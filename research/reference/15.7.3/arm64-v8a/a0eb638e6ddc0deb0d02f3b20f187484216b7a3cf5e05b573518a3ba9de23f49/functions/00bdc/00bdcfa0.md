# 00bdcfa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcef0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-856e793b7d3eb71a8031a0f9d664928c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcff0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-2a8805c20e0ecbec9c869a0e1e8fd003)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfa0",
  "name": "_ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5705964a60b386e4ef186b7e9f9ac89d9856414fda86b3178b41f447d383fdd0",
  "source_text_sha256": "5705964a60b386e4ef186b7e9f9ac89d9856414fda86b3178b41f447d383fdd0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfa0",
        "00bdcfaf"
      ]
    ],
    "bytes_sha256": "43154558886781ff4daa482b996ce39701e9fe984003d979f8d2fd048f6bbcd4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004f73a8](../004f7/004f73a8.md)

## 呼び出し先

- [004f78a4](../004f7/004f78a4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 325 bytes

~~~c

void _ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB__00c1d060
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfa0"></a> `00bdcfa0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfa4"></a> `00bdcfa4` | `11 32 40 f9` | ldr x17,[x16, #0x60] | `FALL_THROUGH`
<a id="insn-00bdcfa8"></a> `00bdcfa8` | `10 82 01 91` | add x16,x16,#0x60 | `FALL_THROUGH`
<a id="insn-00bdcfac"></a> `00bdcfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfa0`](#insn-00bdcfa0) 範囲 `[['00bdcfa0', '00bdcfaf']]`

## 命令位置別の参照

- [`00bdcfa4`](#insn-00bdcfa4) → `00c1d060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfac`](#insn-00bdcfac) → [`004f78a4`](../004f7/004f78a4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f78a4` · 推定シンボル `_ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfa4`](#insn-00bdcfa4)

~~~json
{
  "source": "00bdcfa4",
  "target": "00c1d060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfac`](#insn-00bdcfac)

~~~json
{
  "source": "00bdcfac",
  "target": "004f78a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
