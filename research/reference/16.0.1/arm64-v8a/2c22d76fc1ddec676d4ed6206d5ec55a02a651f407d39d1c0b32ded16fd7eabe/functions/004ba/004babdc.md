# 004babdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004bab9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bab9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0006.md#compare-c10fbb60458d02671026e6cbf8a8eaaa)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bac1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bac1c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0006.md#compare-6caa57ce40d8a7b0bf89ad39f7784613)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004babdc",
  "name": "_ZN5Botan6BigIntC1Em",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c",
  "source_text_sha256": "4a3843c37d2054e7e4b5a5594349ca285909d1c3c07092c844ab9e9eedf49b7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004babdc",
        "004bac1f"
      ]
    ],
    "bytes_sha256": "28668fefeafaec0a1b6fed47e96611278f7de27c2a581d832588780e1e67d2bc",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58920](../00c58/00c58920.md)

## 呼び出し先

- [00540920](../00540/00540920.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 253 bytes

~~~c

void _ZN5Botan6BigIntC1Em(undefined8 *param_1,long param_2)

{
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  *(undefined4 *)(param_1 + 3) = 1;
  if (param_2 != 0) {
    FUN_00540920(param_1,8);
    *(long *)*param_1 = param_2;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004babdc"></a> `004babdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-004babe0"></a> `004babe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004babe4"></a> `004babe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004babe8"></a> `004babe8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-004babec"></a> `004babec` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-004babf0"></a> `004babf0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004babf4"></a> `004babf4` | `08 18 00 b9` | str w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-004babf8"></a> `004babf8` | `e1 00 00 b4` | cbz x1,0x004bac14 | `CONDITIONAL_JUMP`
<a id="insn-004babfc"></a> `004babfc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004bac00"></a> `004bac00` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-004bac04"></a> `004bac04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bac08"></a> `004bac08` | `46 17 02 94` | bl 0x00540920 | `UNCONDITIONAL_CALL`
<a id="insn-004bac0c"></a> `004bac0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-004bac10"></a> `004bac10` | `14 01 00 f9` | str x20,[x8] | `FALL_THROUGH`
<a id="insn-004bac14"></a> `004bac14` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bac18"></a> `004bac18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-004bac1c"></a> `004bac1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004babdc`](#insn-004babdc) 範囲 `[['004babdc', '004babfb']]`
  - `CONDITIONAL_JUMP` [`004babf8`](#insn-004babf8) → [`004bac14`](#insn-004bac14)
  - `FALL_THROUGH` [`004babf8`](#insn-004babf8) → [`004babfc`](#insn-004babfc)
- ブロック [`004babfc`](#insn-004babfc) 範囲 `[['004babfc', '004bac13']]`
  - `FALL_THROUGH` [`004bac10`](#insn-004bac10) → [`004bac14`](#insn-004bac14)
- ブロック [`004bac14`](#insn-004bac14) 範囲 `[['004bac14', '004bac1f']]`

## 命令位置別の参照

- [`004babdc`](#insn-004babdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babe0`](#insn-004babe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babf8`](#insn-004babf8) → [`004bac14`](#insn-004bac14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac08`](#insn-004bac08) → [`00540920`](../00540/00540920.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00540920` · 推定シンボル `None` · 推定型 `None`
- [`004bac14`](#insn-004bac14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac18`](#insn-004bac18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004babdc`](#insn-004babdc)

~~~json
{
  "source": "004babdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babe0`](#insn-004babe0)

~~~json
{
  "source": "004babe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babf8`](#insn-004babf8)

~~~json
{
  "source": "004babf8",
  "target": "004bac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac08`](#insn-004bac08)

~~~json
{
  "source": "004bac08",
  "target": "00540920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bac14`](#insn-004bac14)

~~~json
{
  "source": "004bac14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac18`](#insn-004bac18)

~~~json
{
  "source": "004bac18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
