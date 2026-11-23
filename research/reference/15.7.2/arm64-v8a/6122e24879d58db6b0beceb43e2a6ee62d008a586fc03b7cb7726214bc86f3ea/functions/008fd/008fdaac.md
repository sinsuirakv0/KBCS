# 008fdaac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `008fdaac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdaac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0047.md#compare-7f209dc787645a833bb493c81f95798c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fdaac",
  "name": "FUN_008fdaac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbe6da75e386b741ed21d79393edda218275680aa697fe6d27b11fd8517cc579",
  "source_text_sha256": "dbe6da75e386b741ed21d79393edda218275680aa697fe6d27b11fd8517cc579",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fdaac",
        "008fdabb"
      ]
    ],
    "bytes_sha256": "cb7bb3caa676b3c0f98c9b403b291eed5de570cf9183c938a44709d6994c9f7a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_008fdaac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c08ce0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fdaac"></a> `008fdaac` | `48 18 00 f0` | adrp x8,0xc08000 | `FALL_THROUGH`
<a id="insn-008fdab0"></a> `008fdab0` | `08 81 33 91` | add x8,x8,#0xce0 | `FALL_THROUGH`
<a id="insn-008fdab4"></a> `008fdab4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008fdab8"></a> `008fdab8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fdaac`](#insn-008fdaac) 範囲 `[['008fdaac', '008fdabb']]`

## 命令位置別の参照

- [`008fdab4`](#insn-008fdab4) → `00c08ce0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fdab4`](#insn-008fdab4)

~~~json
{
  "source": "008fdab4",
  "target": "00c08ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c08ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
