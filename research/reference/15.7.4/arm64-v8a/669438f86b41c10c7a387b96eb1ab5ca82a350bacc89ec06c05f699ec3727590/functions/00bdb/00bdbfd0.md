# 00bdbfd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-85d8c4011d8d2b61f3c6dcf6a30dfab7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58a20`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a20.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-1c30d1507c694f276827ade39a25188f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfd0",
  "name": "_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "517c449f978138de74ecd406c2080973edff596bf7b30f8d9282016a99fd6b20",
  "source_text_sha256": "517c449f978138de74ecd406c2080973edff596bf7b30f8d9282016a99fd6b20",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfd0",
        "00bdbfdf"
      ]
    ],
    "bytes_sha256": "6779caa6831ba9c47d68d727b383fff71ad5e28a9c7c0d5eb2aa7f18a3ebd7e8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049f624](../0049f/0049f624.md)
- [004bf57c](../004bf/004bf57c.md)
- [004fcb38](../004fc/004fcb38.md)

## 呼び出し先

- [0047f40c](../0047f/0047f40c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 337 bytes

~~~c

void _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE_00c1c8a0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfd0"></a> `00bdbfd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfd4"></a> `00bdbfd4` | `11 52 44 f9` | ldr x17,[x16, #0x8a0] | `FALL_THROUGH`
<a id="insn-00bdbfd8"></a> `00bdbfd8` | `10 82 22 91` | add x16,x16,#0x8a0 | `FALL_THROUGH`
<a id="insn-00bdbfdc"></a> `00bdbfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfd0`](#insn-00bdbfd0) 範囲 `[['00bdbfd0', '00bdbfdf']]`

## 命令位置別の参照

- [`00bdbfd4`](#insn-00bdbfd4) → `00c1c8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfdc`](#insn-00bdbfdc) → [`0047f40c`](../0047f/0047f40c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0047f40c` · 推定シンボル `_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfd4`](#insn-00bdbfd4)

~~~json
{
  "source": "00bdbfd4",
  "target": "00c1c8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfdc`](#insn-00bdbfdc)

~~~json
{
  "source": "00bdbfdc",
  "target": "0047f40c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
