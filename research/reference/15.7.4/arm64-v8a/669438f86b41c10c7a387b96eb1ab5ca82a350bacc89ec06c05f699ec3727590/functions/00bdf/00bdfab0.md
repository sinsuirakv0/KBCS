# 00bdfab0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfa60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-dce0368059c6e73346299be28f4640ab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c460`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c460.md) · 移動量 `+0x7c9b0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0015.md#compare-9a9b2c70cc17ff515a647637a1df3fb8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfab0",
  "name": "_ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6321b45cb28dbfcc793b35baf1fc5edd55c0eaa6848ae4e95dd731d3f79f8f1d",
  "source_text_sha256": "6321b45cb28dbfcc793b35baf1fc5edd55c0eaa6848ae4e95dd731d3f79f8f1d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfab0",
        "00bdfabf"
      ]
    ],
    "bytes_sha256": "7fd146476757798cd82878b8fe042e2e1d6f5f815c658fe3719a3e92de684f09",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b26b28](../00b26/00b26b28.md)

## 呼び出し先

- [00b46ec0](../00b46/00b46ec0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 279 bytes

~~~c

void _ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE_00c1e610
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfab0"></a> `00bdfab0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfab4"></a> `00bdfab4` | `11 0a 43 f9` | ldr x17,[x16, #0x610] | `FALL_THROUGH`
<a id="insn-00bdfab8"></a> `00bdfab8` | `10 42 18 91` | add x16,x16,#0x610 | `FALL_THROUGH`
<a id="insn-00bdfabc"></a> `00bdfabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfab0`](#insn-00bdfab0) 範囲 `[['00bdfab0', '00bdfabf']]`

## 命令位置別の参照

- [`00bdfab4`](#insn-00bdfab4) → `00c1e610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfabc`](#insn-00bdfabc) → [`00b46ec0`](../00b46/00b46ec0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b46ec0` · 推定シンボル `_ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfab4`](#insn-00bdfab4)

~~~json
{
  "source": "00bdfab4",
  "target": "00c1e610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e610",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfabc`](#insn-00bdfabc)

~~~json
{
  "source": "00bdfabc",
  "target": "00b46ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
