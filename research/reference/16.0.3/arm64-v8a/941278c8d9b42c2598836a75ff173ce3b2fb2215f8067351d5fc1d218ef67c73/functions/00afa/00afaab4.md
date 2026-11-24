# 00afaab4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9ac0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9ac0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-6e1c3a71dad804611d1f9414b85c1ca4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaab4",
  "name": "FUN_00afaab4",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4448b2c21938e38811015add502fcd655b24379f78e9989f202dda2e9bc96951",
  "source_text_sha256": "4448b2c21938e38811015add502fcd655b24379f78e9989f202dda2e9bc96951",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaab4",
        "00afab23"
      ]
    ],
    "bytes_sha256": "e6be56a7760c169f94099355c3fee48ff3f9f645a892b46c2fed0b5e11f8a6cb",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 445 bytes

~~~c

void FUN_00afaab4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afaad4 to 00bfaadb has its CatchHandler @ 00afac70 */
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b4c) = param_3 & 1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaab4"></a> `00afaab4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaab8"></a> `00afaab8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaabc"></a> `00afaabc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaac0"></a> `00afaac0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaac4"></a> `00afaac4` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afaac8"></a> `00afaac8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaacc"></a> `00afaacc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afaad0"></a> `00afaad0` | `8b 5e f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaad4"></a> `00afaad4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afaad8"></a> `00afaad8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afaadc"></a> `00afaadc` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaae0"></a> `00afaae0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afaae4"></a> `00afaae4` | `4b b3 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afaae8"></a> `00afaae8` | `60 01 00 36` | tbz w0,#0x0,0x00afab14 | `CONDITIONAL_JUMP`
<a id="insn-00afaaec"></a> `00afaaec` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afaaf0"></a> `00afaaf0` | `94 02 00 12` | and w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afaaf4"></a> `00afaaf4` | `82 5e f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaaf8"></a> `00afaaf8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afab00"></a> `00afab00` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afab04"></a> `00afab04` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `89 69 89 52` | mov w9,#0x4b4c | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afab10"></a> `00afab10` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afab14"></a> `00afab14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afab18"></a> `00afab18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afab1c"></a> `00afab1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afab20"></a> `00afab20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaab4`](#insn-00afaab4) 範囲 `[['00afaab4', '00afaad3']]`
  - `FALL_THROUGH` [`00afaad0`](#insn-00afaad0) → [`00afaad4`](#insn-00afaad4)
- ブロック [`00afaad4`](#insn-00afaad4) 範囲 `[['00afaad4', '00afaaeb']]`
  - `CONDITIONAL_JUMP` [`00afaae8`](#insn-00afaae8) → [`00afab14`](#insn-00afab14)
  - `FALL_THROUGH` [`00afaae8`](#insn-00afaae8) → [`00afaaec`](#insn-00afaaec)
- ブロック [`00afaaec`](#insn-00afaaec) 範囲 `[['00afaaec', '00afab13']]`
  - `FALL_THROUGH` [`00afab10`](#insn-00afab10) → [`00afab14`](#insn-00afab14)
- ブロック [`00afab14`](#insn-00afab14) 範囲 `[['00afab14', '00afab23']]`

## 命令位置別の参照

- [`00afaab4`](#insn-00afaab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab8`](#insn-00afaab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaabc`](#insn-00afaabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaad0`](#insn-00afaad0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaae4`](#insn-00afaae4) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afaae8`](#insn-00afaae8) → [`00afab14`](#insn-00afab14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaf4`](#insn-00afaaf4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afab14`](#insn-00afab14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab18`](#insn-00afab18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab1c`](#insn-00afab1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaab4`](#insn-00afaab4)

~~~json
{
  "source": "00afaab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab8`](#insn-00afaab8)

~~~json
{
  "source": "00afaab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaabc`](#insn-00afaabc)

~~~json
{
  "source": "00afaabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaad0`](#insn-00afaad0)

~~~json
{
  "source": "00afaad0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaae4`](#insn-00afaae4)

~~~json
{
  "source": "00afaae4",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaae8`](#insn-00afaae8)

~~~json
{
  "source": "00afaae8",
  "target": "00afab14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaf4`](#insn-00afaaf4)

~~~json
{
  "source": "00afaaf4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab14`](#insn-00afab14)

~~~json
{
  "source": "00afab14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab18`](#insn-00afab18)

~~~json
{
  "source": "00afab18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab1c`](#insn-00afab1c)

~~~json
{
  "source": "00afab1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
