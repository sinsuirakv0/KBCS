# 00bdccb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-7099bc784a5a9d1571a82d30beff702e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59700`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-84b7fbcc8dfc165ef17212cc568fe945)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccb0",
  "name": "_ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58468e8c3571a37d1a9304d51171decebfedf1e6439713ee75712912e9ae1676",
  "source_text_sha256": "58468e8c3571a37d1a9304d51171decebfedf1e6439713ee75712912e9ae1676",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccb0",
        "00bdccbf"
      ]
    ],
    "bytes_sha256": "e9fc084a77bb70dada2c0b33ca5c9455a1e5891620749650ead7f02092137118",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e1f38](../004e1/004e1f38.md)
- [004e20fc](../004e2/004e20fc.md)
- [004e40b8](../004e4/004e40b8.md)
- [004e5850](../004e5/004e5850.md)
- [004f10f4](../004f1/004f10f4.md)
- [004f1394](../004f1/004f1394.md)
- [0050af44](../0050a/0050af44.md)

## 呼び出し先

- [004f11e0](../004f1/004f11e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE_00c1cf10
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccb0"></a> `00bdccb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccb4"></a> `00bdccb4` | `11 8a 47 f9` | ldr x17,[x16, #0xf10] | `FALL_THROUGH`
<a id="insn-00bdccb8"></a> `00bdccb8` | `10 42 3c 91` | add x16,x16,#0xf10 | `FALL_THROUGH`
<a id="insn-00bdccbc"></a> `00bdccbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccb0`](#insn-00bdccb0) 範囲 `[['00bdccb0', '00bdccbf']]`

## 命令位置別の参照

- [`00bdccb4`](#insn-00bdccb4) → `00c1cf10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccbc`](#insn-00bdccbc) → [`004f11e0`](../004f1/004f11e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f11e0` · 推定シンボル `_ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccb4`](#insn-00bdccb4)

~~~json
{
  "source": "00bdccb4",
  "target": "00c1cf10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdccbc`](#insn-00bdccbc)

~~~json
{
  "source": "00bdccbc",
  "target": "004f11e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
