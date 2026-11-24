# 00bdcff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcfa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-2a8805c20e0ecbec9c869a0e1e8fd003)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59a40`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a40.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0010.md#compare-c276322cf65a116014adc24c984537b7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcff0",
  "name": "_ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d722e723b585d92fccd50f22aa5514bea477f94fadfa7acc0a39cbb64952663",
  "source_text_sha256": "5d722e723b585d92fccd50f22aa5514bea477f94fadfa7acc0a39cbb64952663",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcff0",
        "00bdcfff"
      ]
    ],
    "bytes_sha256": "0d958a08d5bca1f8b9fb57cb1cd0068695edd238c41323eac1587bc3e1d10585",
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
    PTR__ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB__00c1d0b0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcff0"></a> `00bdcff0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcff4"></a> `00bdcff4` | `11 5a 40 f9` | ldr x17,[x16, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdcff8"></a> `00bdcff8` | `10 c2 02 91` | add x16,x16,#0xb0 | `FALL_THROUGH`
<a id="insn-00bdcffc"></a> `00bdcffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcff0`](#insn-00bdcff0) 範囲 `[['00bdcff0', '00bdcfff']]`

## 命令位置別の参照

- [`00bdcff4`](#insn-00bdcff4) → `00c1d0b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcffc`](#insn-00bdcffc) → [`004f78a4`](../004f7/004f78a4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f78a4` · 推定シンボル `_ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcff4`](#insn-00bdcff4)

~~~json
{
  "source": "00bdcff4",
  "target": "00c1d0b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d0b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcffc`](#insn-00bdcffc)

~~~json
{
  "source": "00bdcffc",
  "target": "004f78a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
