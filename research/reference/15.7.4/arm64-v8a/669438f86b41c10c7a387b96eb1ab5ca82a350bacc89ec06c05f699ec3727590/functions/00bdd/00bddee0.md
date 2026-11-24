# 00bddee0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdde90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-c62429a0111172db9caddcfc651b4c01)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a940`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a940.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-d4f8312ab093e8daef6d882137e5fc8c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddee0",
  "name": "_ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6401cdef1519a2a267467860c43e80217e566383de3338141f1e4585dfa4990b",
  "source_text_sha256": "6401cdef1519a2a267467860c43e80217e566383de3338141f1e4585dfa4990b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddee0",
        "00bddeef"
      ]
    ],
    "bytes_sha256": "45271d3d958400bfc8434e24288674ab32237de8f14779278bdc4c5d043092ce",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae020c](../00ae0/00ae020c.md)

## 呼び出し先

- [00ae02f0](../00ae0/00ae02f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 193 bytes

~~~c

void _ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em(void)

{
  (*(code *)PTR__ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em_00c1d828)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddee0"></a> `00bddee0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddee4"></a> `00bddee4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bddee8"></a> `00bddee8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bddeec"></a> `00bddeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddee0`](#insn-00bddee0) 範囲 `[['00bddee0', '00bddeef']]`

## 命令位置別の参照

- [`00bddee4`](#insn-00bddee4) → `00c1d828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddeec`](#insn-00bddeec) → [`00ae02f0`](../00ae0/00ae02f0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae02f0` · 推定シンボル `_ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddee4`](#insn-00bddee4)

~~~json
{
  "source": "00bddee4",
  "target": "00c1d828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddeec`](#insn-00bddeec)

~~~json
{
  "source": "00bddeec",
  "target": "00ae02f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
