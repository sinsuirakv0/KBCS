# 00bdbfa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-e69e83cd9aa30da16fb6fc2fb1422b9b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c589f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-cc5a33b45f8ae790e6b585414781b40a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfa0",
  "name": "_ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b7cae1a0f33e178e9d882132bccb24dd76f2389a48cec958a05c487cf30343e",
  "source_text_sha256": "2b7cae1a0f33e178e9d882132bccb24dd76f2389a48cec958a05c487cf30343e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfa0",
        "00bdbfaf"
      ]
    ],
    "bytes_sha256": "420d41011db23f7632231fb730eede059f2157140ff47dbf4f3627cb6dc62907",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049e24c](../0049e/0049e24c.md)
- [004a19c4](../004a1/004a19c4.md)
- [004a9174](../004a9/004a9174.md)
- [004ab3f4](../004ab/004ab3f4.md)
- [004c3c00](../004c3/004c3c00.md)
- [004def78](../004de/004def78.md)
- [004df290](../004df/004df290.md)
- [004e939c](../004e9/004e939c.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00501274](../00501/00501274.md)
- [0055f8e0](../0055f/0055f8e0.md)

## 呼び出し先

- [0049e3f4](../0049e/0049e3f4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 289 bytes

~~~c

void _ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9__00c1c888
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfa0"></a> `00bdbfa0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfa4"></a> `00bdbfa4` | `11 46 44 f9` | ldr x17,[x16, #0x888] | `FALL_THROUGH`
<a id="insn-00bdbfa8"></a> `00bdbfa8` | `10 22 22 91` | add x16,x16,#0x888 | `FALL_THROUGH`
<a id="insn-00bdbfac"></a> `00bdbfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfa0`](#insn-00bdbfa0) 範囲 `[['00bdbfa0', '00bdbfaf']]`

## 命令位置別の参照

- [`00bdbfa4`](#insn-00bdbfa4) → `00c1c888`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfac`](#insn-00bdbfac) → [`0049e3f4`](../0049e/0049e3f4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0049e3f4` · 推定シンボル `_ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfa4`](#insn-00bdbfa4)

~~~json
{
  "source": "00bdbfa4",
  "target": "00c1c888",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c888",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfac`](#insn-00bdbfac)

~~~json
{
  "source": "00bdbfac",
  "target": "0049e3f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
