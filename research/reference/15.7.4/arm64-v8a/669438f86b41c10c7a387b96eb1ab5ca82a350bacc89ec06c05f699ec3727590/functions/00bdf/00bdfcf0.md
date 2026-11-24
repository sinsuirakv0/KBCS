# 00bdfcf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfca0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-80464e9e1b9b95bb700fc85bba702b22)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c6d0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6d0.md) · 移動量 `+0x7c9e0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0015.md#compare-8ce65465ff6bb14516b60b4c7ba25b70)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfcf0",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64c58614ae2e61cb1b5be1b4a01a30aa808c1c1688c2b1e62b24ad3086c0499e",
  "source_text_sha256": "64c58614ae2e61cb1b5be1b4a01a30aa808c1c1688c2b1e62b24ad3086c0499e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfcf0",
        "00bdfcff"
      ]
    ],
    "bytes_sha256": "bec6529152ee32bd268a0d26f7be7acb5079c8c88fbf88bea8db7fd5c15e59b6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0f84c](../00b0f/00b0f84c.md)

## 呼び出し先

- [00b3edac](../00b3e/00b3edac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 295 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA__00c1e730
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfcf0"></a> `00bdfcf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfcf4"></a> `00bdfcf4` | `11 9a 43 f9` | ldr x17,[x16, #0x730] | `FALL_THROUGH`
<a id="insn-00bdfcf8"></a> `00bdfcf8` | `10 c2 1c 91` | add x16,x16,#0x730 | `FALL_THROUGH`
<a id="insn-00bdfcfc"></a> `00bdfcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfcf0`](#insn-00bdfcf0) 範囲 `[['00bdfcf0', '00bdfcff']]`

## 命令位置別の参照

- [`00bdfcf4`](#insn-00bdfcf4) → `00c1e730`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcfc`](#insn-00bdfcfc) → [`00b3edac`](../00b3e/00b3edac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3edac` · 推定シンボル `_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfcf4`](#insn-00bdfcf4)

~~~json
{
  "source": "00bdfcf4",
  "target": "00c1e730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e730",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcfc`](#insn-00bdfcfc)

~~~json
{
  "source": "00bdfcfc",
  "target": "00b3edac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
