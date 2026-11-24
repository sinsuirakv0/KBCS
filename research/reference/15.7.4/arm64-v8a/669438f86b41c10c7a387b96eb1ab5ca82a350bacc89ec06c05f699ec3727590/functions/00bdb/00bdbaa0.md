# 00bdbaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdba50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-ffc62a3e721290b71a6fa8365e0cc51a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c584f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-42485c5293ba3aee1338d48642103958)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbaa0",
  "name": "_ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ac18de452aa87f6a2b39a7ed899fb889baae8be95a0b4499bbe7467b3a24742",
  "source_text_sha256": "0ac18de452aa87f6a2b39a7ed899fb889baae8be95a0b4499bbe7467b3a24742",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbaa0",
        "00bdbaaf"
      ]
    ],
    "bytes_sha256": "63512d21074b61ce206775ff4f99658023c05af64dcd156626b5a2441e73dd9b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00485f54](../00485/00485f54.md)
- [004e40b8](../004e4/004e40b8.md)
- [004eb16c](../004eb/004eb16c.md)
- [004f11e0](../004f1/004f11e0.md)

## 呼び出し先

- [0048a208](../0048a/0048a208.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 271 bytes

~~~c

void _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1c608
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbaa0"></a> `00bdbaa0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbaa4"></a> `00bdbaa4` | `11 06 43 f9` | ldr x17,[x16, #0x608] | `FALL_THROUGH`
<a id="insn-00bdbaa8"></a> `00bdbaa8` | `10 22 18 91` | add x16,x16,#0x608 | `FALL_THROUGH`
<a id="insn-00bdbaac"></a> `00bdbaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbaa0`](#insn-00bdbaa0) 範囲 `[['00bdbaa0', '00bdbaaf']]`

## 命令位置別の参照

- [`00bdbaa4`](#insn-00bdbaa4) → `00c1c608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbaac`](#insn-00bdbaac) → [`0048a208`](../0048a/0048a208.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048a208` · 推定シンボル `_ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbaa4`](#insn-00bdbaa4)

~~~json
{
  "source": "00bdbaa4",
  "target": "00c1c608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c608",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbaac`](#insn-00bdbaac)

~~~json
{
  "source": "00bdbaac",
  "target": "0048a208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
