# 00bdbee0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-5fd6a52bf18c48342208e78d6b0af38a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58930`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58930.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-50c60ecc4ebec825430ca98442653829)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbee0",
  "name": "_ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57c5681b1c1aca300224c892884606165869e2b90cbabee79e1602cd7244ff4f",
  "source_text_sha256": "57c5681b1c1aca300224c892884606165869e2b90cbabee79e1602cd7244ff4f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbee0",
        "00bdbeef"
      ]
    ],
    "bytes_sha256": "68da4bf5d3546fb0b24c85bf56efe173a6fbab6a7c128be93cb6655f01bf091a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00499128](../00499/00499128.md)
- [004993a0](../00499/004993a0.md)
- [004a3d70](../004a3/004a3d70.md)

## 呼び出し先

- [00498d9c](../00498/00498d9c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9__00c1c828
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbee0"></a> `00bdbee0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbee4"></a> `00bdbee4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bdbee8"></a> `00bdbee8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bdbeec"></a> `00bdbeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbee0`](#insn-00bdbee0) 範囲 `[['00bdbee0', '00bdbeef']]`

## 命令位置別の参照

- [`00bdbee4`](#insn-00bdbee4) → `00c1c828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbeec`](#insn-00bdbeec) → [`00498d9c`](../00498/00498d9c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498d9c` · 推定シンボル `_ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbee4`](#insn-00bdbee4)

~~~json
{
  "source": "00bdbee4",
  "target": "00c1c828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbeec`](#insn-00bdbeec)

~~~json
{
  "source": "00bdbeec",
  "target": "00498d9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
