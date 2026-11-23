# 00af5fec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af5f24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-a8225eef77d577dc206c26375814867c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af6030`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af6/00af6030.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/reference_unresolved-0016.md#compare-c9d0069649a4c2751f58bf7ae2855b2d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5fec",
  "name": "_ZN8firebase4util41CppThreadDispatcherContext_nativeFunctionEP7_JNIEnvP8_jobjectll",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d3c72ed1325d26fdfd5f2711b21de2bf04ced983990768c8af4f2ec2af2e63f",
  "source_text_sha256": "7d3c72ed1325d26fdfd5f2711b21de2bf04ced983990768c8af4f2ec2af2e63f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5fec",
        "00af5ff3"
      ]
    ],
    "bytes_sha256": "c51a5ed262bdf072a2ccc19059345c87bb94bf00bb90e8a946d6622576cec05b",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 519 bytes

~~~c

void _ZN8firebase4util41CppThreadDispatcherContext_nativeFunctionEP7_JNIEnvP8_jobjectll
               (undefined8 param_1,undefined8 param_2,code *UNRECOVERED_JUMPTABLE,undefined8 param_4
               )

{
                    /* WARNING: Could not recover jumptable at 0x00af5ff0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* try { // try from 00af5ff0 to 00bf5ff7 has its CatchHandler @ 00affb08 */
  (*UNRECOVERED_JUMPTABLE)(param_4);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5fec"></a> `00af5fec` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00af5ff0"></a> `00af5ff0` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af5fec`](#insn-00af5fec) 範囲 `[['00af5fec', '00af5fef']]`
  - `FALL_THROUGH` [`00af5fec`](#insn-00af5fec) → [`00af5ff0`](#insn-00af5ff0)
- ブロック [`00af5ff0`](#insn-00af5ff0) 範囲 `[['00af5ff0', '00af5ff3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

