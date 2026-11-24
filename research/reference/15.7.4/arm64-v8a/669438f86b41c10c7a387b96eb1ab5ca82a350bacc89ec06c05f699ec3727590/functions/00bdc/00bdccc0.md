# 00bdccc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-2565ebdbae6bd9aac2b0dc2f47039838)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59710`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59710.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-dd86363c96621cbd73dce7cd4b19c49c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccc0",
  "name": "_ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "746f5e4a5073f402d9a5e61b2007ea9e959e4511e14eb79ab89c090ab13a1611",
  "source_text_sha256": "746f5e4a5073f402d9a5e61b2007ea9e959e4511e14eb79ab89c090ab13a1611",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccc0",
        "00bdcccf"
      ]
    ],
    "bytes_sha256": "bb101edb063256aeba8f56b1b44c0f749314e53454105780c6ed13d9144b20c9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e21a8](../004e2/004e21a8.md)
- [004f27ec](../004f2/004f27ec.md)
- [004fb978](../004fb/004fb978.md)
- [0050a638](../0050a/0050a638.md)
- [0050af44](../0050a/0050af44.md)
- [0050b45c](../0050b/0050b45c.md)
- [005185dc](../00518/005185dc.md)
- [0051a694](../0051a/0051a694.md)
- [0051ac6c](../0051a/0051ac6c.md)

## 呼び出し先

- [004dbf98](../004db/004dbf98.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 297 bytes

~~~c

void _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9__00c1cf18
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccc0"></a> `00bdccc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccc4"></a> `00bdccc4` | `11 8e 47 f9` | ldr x17,[x16, #0xf18] | `FALL_THROUGH`
<a id="insn-00bdccc8"></a> `00bdccc8` | `10 62 3c 91` | add x16,x16,#0xf18 | `FALL_THROUGH`
<a id="insn-00bdcccc"></a> `00bdcccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccc0`](#insn-00bdccc0) 範囲 `[['00bdccc0', '00bdcccf']]`

## 命令位置別の参照

- [`00bdccc4`](#insn-00bdccc4) → `00c1cf18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcccc`](#insn-00bdcccc) → [`004dbf98`](../004db/004dbf98.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004dbf98` · 推定シンボル `_ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccc4`](#insn-00bdccc4)

~~~json
{
  "source": "00bdccc4",
  "target": "00c1cf18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcccc`](#insn-00bdcccc)

~~~json
{
  "source": "00bdcccc",
  "target": "004dbf98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
