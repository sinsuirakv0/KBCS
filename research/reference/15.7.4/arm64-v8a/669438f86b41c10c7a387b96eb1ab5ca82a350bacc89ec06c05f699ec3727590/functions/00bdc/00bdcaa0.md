# 00bdcaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdca50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-1f9e03f00bfe6707a752c4173ebb2ba1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c594f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-323f4cd178f27f2988bb8f929746c2e5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcaa0",
  "name": "_ZN5Botan13x500_name_cmpERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c6e989b76e89ddbe5ebeeb4fab957e297333cddb2784bfc9db0c45644b28264a",
  "source_text_sha256": "c6e989b76e89ddbe5ebeeb4fab957e297333cddb2784bfc9db0c45644b28264a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcaa0",
        "00bdcaaf"
      ]
    ],
    "bytes_sha256": "e756275d9ca5678507da7c74c1cc4c4528c9b3e8032db62edc2b4b116523ab32",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004deb5c](../004de/004deb5c.md)

## 呼び出し先

- [004da1b8](../004da/004da1b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 277 bytes

~~~c

void _ZN5Botan13x500_name_cmpERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_
               (void)

{
  (*(code *)
    PTR__ZN5Botan13x500_name_cmpERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8__00c1ce08
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcaa0"></a> `00bdcaa0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcaa4"></a> `00bdcaa4` | `11 06 47 f9` | ldr x17,[x16, #0xe08] | `FALL_THROUGH`
<a id="insn-00bdcaa8"></a> `00bdcaa8` | `10 22 38 91` | add x16,x16,#0xe08 | `FALL_THROUGH`
<a id="insn-00bdcaac"></a> `00bdcaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcaa0`](#insn-00bdcaa0) 範囲 `[['00bdcaa0', '00bdcaaf']]`

## 命令位置別の参照

- [`00bdcaa4`](#insn-00bdcaa4) → `00c1ce08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcaac`](#insn-00bdcaac) → [`004da1b8`](../004da/004da1b8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004da1b8` · 推定シンボル `_ZN5Botan13x500_name_cmpERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcaa4`](#insn-00bdcaa4)

~~~json
{
  "source": "00bdcaa4",
  "target": "00c1ce08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcaac`](#insn-00bdcaac)

~~~json
{
  "source": "00bdcaac",
  "target": "004da1b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
