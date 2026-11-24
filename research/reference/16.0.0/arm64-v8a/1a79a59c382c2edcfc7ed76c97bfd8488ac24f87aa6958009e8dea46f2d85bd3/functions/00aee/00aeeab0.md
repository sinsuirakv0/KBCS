# 00aeeab0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0163.md#review-4f1840b86fa18cb9bb951ec16b4228a8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0043.md#review-4f1840b86fa18cb9bb951ec16b4228a8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeeab0",
  "name": "FUN_00aeeab0",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "538cf5337134cfd5903c664793a25b88caa27e836ee19e65de170f3cd5101ebe",
  "source_text_sha256": "538cf5337134cfd5903c664793a25b88caa27e836ee19e65de170f3cd5101ebe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeeab0",
        "00aeeac7"
      ]
    ],
    "bytes_sha256": "4fce0e59fcdbd78584e96cc612ece851718cb81b07662f9cd8058d15c1b976a8",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
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

## 疑似コード / UTF-8 512 bytes

~~~c

void FUN_00aeeab0(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
                    /* try { // try from 00aeeab8 to 00beeabb has its CatchHandler @ 00aeead4 */
  *param_2 = &PTR_FUN_00c8daf8;
                    /* catch() { ... } // from try @ 00aee914 with catch @ 00aeeabc
                       try { // try from 00aeeabc to 00beeb13 has its CatchHandler @ 00aee7d4 */
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[2] = *(undefined8 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeeab0"></a> `00aeeab0` | `e8 0c 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeeab4"></a> `00aeeab4` | `08 e1 2b 91` | add x8,x8,#0xaf8 | `FALL_THROUGH`
<a id="insn-00aeeab8"></a> `00aeeab8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aeeabc"></a> `00aeeabc` | `00 80 c0 3c` | ldur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeac0"></a> `00aeeac0` | `20 80 80 3c` | stur q0,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeac4"></a> `00aeeac4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeeab0`](#insn-00aeeab0) 範囲 `[['00aeeab0', '00aeeab7']]`
  - `FALL_THROUGH` [`00aeeab4`](#insn-00aeeab4) → [`00aeeab8`](#insn-00aeeab8)
- ブロック [`00aeeab8`](#insn-00aeeab8) 範囲 `[['00aeeab8', '00aeeabb']]`
  - `FALL_THROUGH` [`00aeeab8`](#insn-00aeeab8) → [`00aeeabc`](#insn-00aeeabc)
- ブロック [`00aeeabc`](#insn-00aeeabc) 範囲 `[['00aeeabc', '00aeeac7']]`

## 命令位置別の参照

- [`00aeeab8`](#insn-00aeeab8) → `00c8daf8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeeab8`](#insn-00aeeab8)

~~~json
{
  "source": "00aeeab8",
  "target": "00c8daf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8daf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
