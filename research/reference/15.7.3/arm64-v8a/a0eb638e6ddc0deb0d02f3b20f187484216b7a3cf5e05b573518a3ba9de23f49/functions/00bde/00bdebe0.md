# 00bdebe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdeb30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-fd7f19bb20a665238c84777537f2d54c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdec30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-47337643798aa8c1e8529766442b6473)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebe0",
  "name": "_ZN8firebase8callback11AddCallbackEPNS0_8CallbackE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c42dbc6dcde9d2fe2aeca7bf48ea2b2858d10cdaac0c27e880aa74506564bbdf",
  "source_text_sha256": "c42dbc6dcde9d2fe2aeca7bf48ea2b2858d10cdaac0c27e880aa74506564bbdf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebe0",
        "00bdebef"
      ]
    ],
    "bytes_sha256": "21a0f20d00a74400b445030e58918429b49fce4dadb42eea7b4a55330c66faa6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afbba4](../00afb/00afbba4.md)
- [00afbc2c](../00afb/00afbc2c.md)

## 呼び出し先

- [00afba04](../00afb/00afba04.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 159 bytes

~~~c

void _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(void)

{
  (*(code *)PTR__ZN8firebase8callback11AddCallbackEPNS0_8CallbackE_00c1de80)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebe0"></a> `00bdebe0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdebe4"></a> `00bdebe4` | `11 42 47 f9` | ldr x17,[x16, #0xe80] | `FALL_THROUGH`
<a id="insn-00bdebe8"></a> `00bdebe8` | `10 02 3a 91` | add x16,x16,#0xe80 | `FALL_THROUGH`
<a id="insn-00bdebec"></a> `00bdebec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebe0`](#insn-00bdebe0) 範囲 `[['00bdebe0', '00bdebef']]`

## 命令位置別の参照

- [`00bdebe4`](#insn-00bdebe4) → `00c1de80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdebec`](#insn-00bdebec) → [`00afba04`](../00afb/00afba04.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afba04` · 推定シンボル `_ZN8firebase8callback11AddCallbackEPNS0_8CallbackE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebe4`](#insn-00bdebe4)

~~~json
{
  "source": "00bdebe4",
  "target": "00c1de80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdebec`](#insn-00bdebec)

~~~json
{
  "source": "00bdebec",
  "target": "00afba04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
