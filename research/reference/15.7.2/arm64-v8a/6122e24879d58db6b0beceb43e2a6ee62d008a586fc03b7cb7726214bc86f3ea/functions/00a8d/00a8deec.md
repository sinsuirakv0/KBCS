# 00a8deec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0020.md#review-654e4d952bf6ebae811ebdf578d7edf2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8deec",
  "name": "FUN_00a8deec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88190a846c3657b850d775ae74a32c1a2bd8f9052b960048555e8737c9d23530",
  "source_text_sha256": "88190a846c3657b850d775ae74a32c1a2bd8f9052b960048555e8737c9d23530",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8deec",
        "00a8deff"
      ]
    ],
    "bytes_sha256": "b381960f8c63a37bb56021786d398186e73ad4223a3c1b184900627ca9de878a",
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

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_00a8deec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a8def4 to 00b8defb has its CatchHandler @ 00a8fafc */
  *param_2 = &PTR_FUN_00c0e058;
  param_2[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8deec"></a> `00a8deec` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a8def0"></a> `00a8def0` | `09 0c 00 b0` | adrp x9,0xc0e000 | `FALL_THROUGH`
<a id="insn-00a8def4"></a> `00a8def4` | `29 61 01 91` | add x9,x9,#0x58 | `FALL_THROUGH`
<a id="insn-00a8def8"></a> `00a8def8` | `29 20 00 a9` | stp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-00a8defc"></a> `00a8defc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a8deec`](#insn-00a8deec) 範囲 `[['00a8deec', '00a8def3']]`
  - `FALL_THROUGH` [`00a8def0`](#insn-00a8def0) → [`00a8def4`](#insn-00a8def4)
- ブロック [`00a8def4`](#insn-00a8def4) 範囲 `[['00a8def4', '00a8deff']]`

## 命令位置別の参照

- [`00a8def8`](#insn-00a8def8) → `00c0e058`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8def8`](#insn-00a8def8)

~~~json
{
  "source": "00a8def8",
  "target": "00c0e058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0e058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
