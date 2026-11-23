# 00a1fbec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a1fbec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a1f/00a1fbec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0052.md#compare-5ee2148d67a06c4cf5f68b66b711dfc5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a1fc30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1f/00a1fc30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0054.md#compare-ee69f64cc8003f8cd2faca4a2999b0c6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a1fbec",
  "name": "FUN_00a1fbec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b954bab20b24cb32410c4ed4a1000f66395e9b14d8911500dbcd8118defc3c5e",
  "source_text_sha256": "b954bab20b24cb32410c4ed4a1000f66395e9b14d8911500dbcd8118defc3c5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a1fbec",
        "00a1fbff"
      ]
    ],
    "bytes_sha256": "ca99d11413e9653805f11108fb1634c5050d7d798e2b138d7824ef7786008188",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
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

## 疑似コード / UTF-8 186 bytes

~~~c

void FUN_00a1fbec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0c2b0;
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a1fbec"></a> `00a1fbec` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a1fbf0"></a> `00a1fbf0` | `69 0f 00 b0` | adrp x9,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a1fbf4"></a> `00a1fbf4` | `29 c1 0a 91` | add x9,x9,#0x2b0 | `FALL_THROUGH`
<a id="insn-00a1fbf8"></a> `00a1fbf8` | `29 20 00 a9` | stp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-00a1fbfc"></a> `00a1fbfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a1fbec`](#insn-00a1fbec) 範囲 `[['00a1fbec', '00a1fbff']]`

## 命令位置別の参照

- [`00a1fbf8`](#insn-00a1fbf8) → `00c0c2b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a1fbf8`](#insn-00a1fbf8)

~~~json
{
  "source": "00a1fbf8",
  "target": "00c0c2b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c2b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
