# 00ac9abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac98c0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98c0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-4815452b901e8bc99a73f87b61b11e73)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac9b2c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9b2c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-4b9156e90e0c1798c223157eccfa2573)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9abc",
  "name": "FUN_00ac9abc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b38ce4491f7fe27984be5fd0847ae052e798c9282b3a1b71e26f494066dfff83",
  "source_text_sha256": "b38ce4491f7fe27984be5fd0847ae052e798c9282b3a1b71e26f494066dfff83",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9abc",
        "00ac9ad3"
      ]
    ],
    "bytes_sha256": "9ab25c617a9318f2fefce849173e4fe25cdefe44a8d11b394276efa591625a9b",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 468 bytes

~~~c

void FUN_00ac9abc(long param_1,undefined8 param_2,undefined4 param_3,undefined8 param_4,
                 undefined4 param_5)

{
  *(undefined4 *)(param_1 + 0x1b0) = param_3;
  *(undefined8 *)(param_1 + 0x1a0) = param_2;
  *(undefined8 *)(param_1 + 0x1a8) = param_4;
                    /* try { // try from 00ac9ac8 to 00bc9acf has its CatchHandler @ 00ac9b60 */
  *(undefined4 *)(param_1 + 0x1b4) = param_5;
  *(undefined2 *)(param_1 + 0x1b8) = 0x101;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac9abc"></a> `00ac9abc` | `28 20 80 52` | mov w8,#0x101 | `FALL_THROUGH`
<a id="insn-00ac9ac0"></a> `00ac9ac0` | `02 b0 01 b9` | str w2,[x0, #0x1b0] | `FALL_THROUGH`
<a id="insn-00ac9ac4"></a> `00ac9ac4` | `01 0c 1a a9` | stp x1,x3,[x0, #0x1a0] | `FALL_THROUGH`
<a id="insn-00ac9ac8"></a> `00ac9ac8` | `04 b4 01 b9` | str w4,[x0, #0x1b4] | `FALL_THROUGH`
<a id="insn-00ac9acc"></a> `00ac9acc` | `08 70 03 79` | strh w8,[x0, #0x1b8] | `FALL_THROUGH`
<a id="insn-00ac9ad0"></a> `00ac9ad0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9abc`](#insn-00ac9abc) 範囲 `[['00ac9abc', '00ac9ac7']]`
  - `FALL_THROUGH` [`00ac9ac4`](#insn-00ac9ac4) → [`00ac9ac8`](#insn-00ac9ac8)
- ブロック [`00ac9ac8`](#insn-00ac9ac8) 範囲 `[['00ac9ac8', '00ac9ad3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

