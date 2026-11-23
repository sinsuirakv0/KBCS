# 007fafac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `007fafac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fafac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0037.md#compare-6d6de8d53b3443c5b79ee8d8ef3470d1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `007fafac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fa/007fafac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0038.md#compare-58f642bbc99e85069b42c5a2c461dbbd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fafac",
  "name": "FUN_007fafac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f2072f08fab8ce0c84e83c5ad383f4af535e9b942bb929afde861d4a6b791334",
  "source_text_sha256": "f2072f08fab8ce0c84e83c5ad383f4af535e9b942bb929afde861d4a6b791334",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fafac",
        "007fafbb"
      ]
    ],
    "bytes_sha256": "d2511fade4ebc3d1c2e690548560934d6631824b6bd8e4d6df1a8778d290e112",
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

- [00bdb000](../00bdb/00bdb000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void FUN_007fafac(undefined8 *param_1)

{
  *param_1 = &PTR_FUN_00c003f8;
  _ZNSt6__ndk119__shared_weak_countD2Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fafac"></a> `007fafac` | `28 20 00 d0` | adrp x8,0xc00000 | `FALL_THROUGH`
<a id="insn-007fafb0"></a> `007fafb0` | `08 e1 0f 91` | add x8,x8,#0x3f8 | `FALL_THROUGH`
<a id="insn-007fafb4"></a> `007fafb4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007fafb8"></a> `007fafb8` | `12 80 0f 14` | b 0x00bdb000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fafac`](#insn-007fafac) 範囲 `[['007fafac', '007fafbb']]`

## 命令位置別の参照

- [`007fafb4`](#insn-007fafb4) → `00c003f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007fafb8`](#insn-007fafb8) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fafb4`](#insn-007fafb4)

~~~json
{
  "source": "007fafb4",
  "target": "00c003f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c003f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fafb8`](#insn-007fafb8)

~~~json
{
  "source": "007fafb8",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
