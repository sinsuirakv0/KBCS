# 00c2dfbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2db94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2d/00c2db94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0089.md#compare-6d802cb79864bad7ad09868c8e59da00)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2e058`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0089.md#compare-5e2ba19b5349e7c6ea596f10a6686aa4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2dfbc",
  "name": "FUN_00c2dfbc",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ddeec2dbe61d8aff306e20858b27f44c22af314cbd8a75a2055deae19101c84f",
  "source_text_sha256": "ddeec2dbe61d8aff306e20858b27f44c22af314cbd8a75a2055deae19101c84f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2dfbc",
        "00c2e09b"
      ]
    ],
    "bytes_sha256": "f4512c405be209bc5fd27d128f2ea50d541df7b9ce128f6747104613173a2ec9",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c2df50](../00c2d/00c2df50.md)

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 873 bytes

~~~c

void FUN_00c2dfbc(void)

{
  int iVar1;
  undefined2 *puVar2;
  
  if (((DAT_01128718 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128718), iVar1 != 0)) {
    __cxa_atexit(FUN_00c35f20,0,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_01128718);
  }
  if ((DAT_011286e8 & 1) == 0) {
    DAT_011286e8 = 4;
    puVar2 = &DAT_011286e9;
  }
  else {
    DAT_011286f0 = 2;
    puVar2 = DAT_011286f8;
  }
  *(undefined1 *)(puVar2 + 1) = 0;
  *puVar2 = 0x4d41;
                    /* try { // try from 00c2e020 to 00d2e03b has its CatchHandler @ 00c2e474 */
  if ((DAT_01128700 & 1) == 0) {
    DAT_01128700 = 4;
    puVar2 = &DAT_01128701;
  }
  else {
                    /* try { // try from 00c2e03c to 00d2e117 has its CatchHandler @ 00c2dce0 */
    DAT_01128708 = 2;
    puVar2 = DAT_01128710;
  }
  *puVar2 = 0x4d50;
  *(undefined1 *)(puVar2 + 1) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2dfbc"></a> `00c2dfbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c2dfc0"></a> `00c2dfc0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00c2dfc4"></a> `00c2dfc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c2dfc8"></a> `00c2dfc8` | `c8 27 00 f0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2dfcc"></a> `00c2dfcc` | `08 61 1c 91` | add x8,x8,#0x718 | `FALL_THROUGH`
<a id="insn-00c2dfd0"></a> `00c2dfd0` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c2dfd4"></a> `00c2dfd4` | `88 04 00 36` | tbz w8,#0x0,0x00c2e064 | `CONDITIONAL_JUMP`
<a id="insn-00c2dfd8"></a> `00c2dfd8` | `c8 27 00 f0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2dfdc"></a> `00c2dfdc` | `08 a1 5b 39` | ldrb w8,[x8, #0x6e8] | `FALL_THROUGH`
<a id="insn-00c2dfe0"></a> `00c2dfe0` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2dff8 | `CONDITIONAL_JUMP`
<a id="insn-00c2dfe4"></a> `00c2dfe4` | `c8 27 00 f0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2dfe8"></a> `00c2dfe8` | `08 a1 1b 91` | add x8,x8,#0x6e8 | `FALL_THROUGH`
<a id="insn-00c2dfec"></a> `00c2dfec` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00c2dff0"></a> `00c2dff0` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2dff4"></a> `00c2dff4` | `06 00 00 14` | b 0x00c2e00c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2dff8"></a> `00c2dff8` | `c9 27 00 f0` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2dffc"></a> `00c2dffc` | `29 c1 1b 91` | add x9,x9,#0x6f0 | `FALL_THROUGH`
<a id="insn-00c2e000"></a> `00c2e000` | `4a 00 80 52` | mov w10,#0x2 | `FALL_THROUGH`
<a id="insn-00c2e004"></a> `00c2e004` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2e008"></a> `00c2e008` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2e00c"></a> `00c2e00c` | `29 a8 89 52` | mov w9,#0x4d41 | `FALL_THROUGH`
<a id="insn-00c2e010"></a> `00c2e010` | `1f 09 00 39` | strb wzr,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00c2e014"></a> `00c2e014` | `09 01 00 79` | strh w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2e018"></a> `00c2e018` | `c8 27 00 d0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e01c"></a> `00c2e01c` | `08 01 5c 39` | ldrb w8,[x8, #0x700] | `FALL_THROUGH`
<a id="insn-00c2e020"></a> `00c2e020` | `c8 00 00 37` | tbnz w8,#0x0,0x00c2e038 | `CONDITIONAL_JUMP`
<a id="insn-00c2e024"></a> `00c2e024` | `c8 27 00 d0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e028"></a> `00c2e028` | `08 01 1c 91` | add x8,x8,#0x700 | `FALL_THROUGH`
<a id="insn-00c2e02c"></a> `00c2e02c` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00c2e030"></a> `00c2e030` | `09 15 00 38` | strb w9,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c2e034"></a> `00c2e034` | `06 00 00 14` | b 0x00c2e04c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2e038"></a> `00c2e038` | `c9 27 00 d0` | adrp x9,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e03c"></a> `00c2e03c` | `29 21 1c 91` | add x9,x9,#0x708 | `FALL_THROUGH`
<a id="insn-00c2e040"></a> `00c2e040` | `4a 00 80 52` | mov w10,#0x2 | `FALL_THROUGH`
<a id="insn-00c2e044"></a> `00c2e044` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00c2e048"></a> `00c2e048` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00c2e04c"></a> `00c2e04c` | `09 aa 89 52` | mov w9,#0x4d50 | `FALL_THROUGH`
<a id="insn-00c2e050"></a> `00c2e050` | `09 01 00 79` | strh w9,[x8] | `FALL_THROUGH`
<a id="insn-00c2e054"></a> `00c2e054` | `1f 09 00 39` | strb wzr,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00c2e058"></a> `00c2e058` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00c2e05c"></a> `00c2e05c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c2e060"></a> `00c2e060` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c2e064"></a> `00c2e064` | `c0 27 00 d0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e068"></a> `00c2e068` | `00 60 1c 91` | add x0,x0,#0x718 | `FALL_THROUGH`
<a id="insn-00c2e06c"></a> `00c2e06c` | `79 a7 00 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e070"></a> `00c2e070` | `40 fb ff 34` | cbz w0,0x00c2dfd8 | `CONDITIONAL_JUMP`
<a id="insn-00c2e074"></a> `00c2e074` | `20 00 00 f0` | adrp x0,0xc35000 | `FALL_THROUGH`
<a id="insn-00c2e078"></a> `00c2e078` | `00 80 3c 91` | add x0,x0,#0xf20 | `FALL_THROUGH`
<a id="insn-00c2e07c"></a> `00c2e07c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c2e080"></a> `00c2e080` | `82 78 1a 10` | adr x2,0xc62f90 | `FALL_THROUGH`
<a id="insn-00c2e084"></a> `00c2e084` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00c2e088"></a> `00c2e088` | `6a a7 00 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e08c"></a> `00c2e08c` | `c0 27 00 d0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00c2e090"></a> `00c2e090` | `00 60 1c 91` | add x0,x0,#0x718 | `FALL_THROUGH`
<a id="insn-00c2e094"></a> `00c2e094` | `77 a7 00 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c2e098"></a> `00c2e098` | `d0 ff ff 17` | b 0x00c2dfd8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c2dfbc`](#insn-00c2dfbc) 範囲 `[['00c2dfbc', '00c2dfd7']]`
  - `CONDITIONAL_JUMP` [`00c2dfd4`](#insn-00c2dfd4) → [`00c2e064`](#insn-00c2e064)
  - `FALL_THROUGH` [`00c2dfd4`](#insn-00c2dfd4) → [`00c2dfd8`](#insn-00c2dfd8)
- ブロック [`00c2dfd8`](#insn-00c2dfd8) 範囲 `[['00c2dfd8', '00c2dfe3']]`
  - `CONDITIONAL_JUMP` [`00c2dfe0`](#insn-00c2dfe0) → [`00c2dff8`](#insn-00c2dff8)
  - `FALL_THROUGH` [`00c2dfe0`](#insn-00c2dfe0) → [`00c2dfe4`](#insn-00c2dfe4)
- ブロック [`00c2dfe4`](#insn-00c2dfe4) 範囲 `[['00c2dfe4', '00c2dff7']]`
  - `UNCONDITIONAL_JUMP` [`00c2dff4`](#insn-00c2dff4) → [`00c2e00c`](#insn-00c2e00c)
- ブロック [`00c2dff8`](#insn-00c2dff8) 範囲 `[['00c2dff8', '00c2e00b']]`
  - `FALL_THROUGH` [`00c2e008`](#insn-00c2e008) → [`00c2e00c`](#insn-00c2e00c)
- ブロック [`00c2e00c`](#insn-00c2e00c) 範囲 `[['00c2e00c', '00c2e01f']]`
  - `FALL_THROUGH` [`00c2e01c`](#insn-00c2e01c) → [`00c2e020`](#insn-00c2e020)
- ブロック [`00c2e020`](#insn-00c2e020) 範囲 `[['00c2e020', '00c2e023']]`
  - `CONDITIONAL_JUMP` [`00c2e020`](#insn-00c2e020) → [`00c2e038`](#insn-00c2e038)
  - `FALL_THROUGH` [`00c2e020`](#insn-00c2e020) → [`00c2e024`](#insn-00c2e024)
- ブロック [`00c2e024`](#insn-00c2e024) 範囲 `[['00c2e024', '00c2e037']]`
  - `UNCONDITIONAL_JUMP` [`00c2e034`](#insn-00c2e034) → [`00c2e04c`](#insn-00c2e04c)
- ブロック [`00c2e038`](#insn-00c2e038) 範囲 `[['00c2e038', '00c2e03b']]`
  - `FALL_THROUGH` [`00c2e038`](#insn-00c2e038) → [`00c2e03c`](#insn-00c2e03c)
- ブロック [`00c2e03c`](#insn-00c2e03c) 範囲 `[['00c2e03c', '00c2e04b']]`
  - `FALL_THROUGH` [`00c2e048`](#insn-00c2e048) → [`00c2e04c`](#insn-00c2e04c)
- ブロック [`00c2e04c`](#insn-00c2e04c) 範囲 `[['00c2e04c', '00c2e063']]`
- ブロック [`00c2e064`](#insn-00c2e064) 範囲 `[['00c2e064', '00c2e073']]`
  - `CONDITIONAL_JUMP` [`00c2e070`](#insn-00c2e070) → [`00c2dfd8`](#insn-00c2dfd8)
  - `FALL_THROUGH` [`00c2e070`](#insn-00c2e070) → [`00c2e074`](#insn-00c2e074)
- ブロック [`00c2e074`](#insn-00c2e074) 範囲 `[['00c2e074', '00c2e09b']]`
  - `UNCONDITIONAL_JUMP` [`00c2e098`](#insn-00c2e098) → [`00c2dfd8`](#insn-00c2dfd8)

## 命令位置別の参照

- [`00c2dfc0`](#insn-00c2dfc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2dfd0`](#insn-00c2dfd0) → `01128718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2dfd4`](#insn-00c2dfd4) → [`00c2e064`](#insn-00c2e064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2dfdc`](#insn-00c2dfdc) → `011286e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2dfe0`](#insn-00c2dfe0) → [`00c2dff8`](#insn-00c2dff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2dff0`](#insn-00c2dff0) → `011286e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2dff4`](#insn-00c2dff4) → [`00c2e00c`](#insn-00c2e00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e004`](#insn-00c2e004) → `011286f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e008`](#insn-00c2e008) → `011286f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e010`](#insn-00c2e010) → `011286eb`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e014`](#insn-00c2e014) → `011286e9`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2e01c`](#insn-00c2e01c) → `01128700`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e020`](#insn-00c2e020) → [`00c2e038`](#insn-00c2e038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e030`](#insn-00c2e030) → `01128700`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e034`](#insn-00c2e034) → [`00c2e04c`](#insn-00c2e04c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e044`](#insn-00c2e044) → `01128710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e048`](#insn-00c2e048) → `01128708`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c2e050`](#insn-00c2e050) → `01128701`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined2`
- [`00c2e054`](#insn-00c2e054) → `01128703`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e058`](#insn-00c2e058) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e068`](#insn-00c2e068) → `01128718`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e06c`](#insn-00c2e06c) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00c2e070`](#insn-00c2e070) → [`00c2dfd8`](#insn-00c2dfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2e078`](#insn-00c2e078) → [`00c35f20`](../00c35/00c35f20.md) · `PARAM` · `ANALYSIS` · 関数 `00c35f20` · 推定シンボル `None` · 推定型 `None`
- [`00c2e080`](#insn-00c2e080) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c2e088`](#insn-00c2e088) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00c2e090`](#insn-00c2e090) → `01128718`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c2e094`](#insn-00c2e094) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c2e098`](#insn-00c2e098) → [`00c2dfd8`](#insn-00c2dfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2dfc0`](#insn-00c2dfc0)

~~~json
{
  "source": "00c2dfc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2dfd0`](#insn-00c2dfd0)

~~~json
{
  "source": "00c2dfd0",
  "target": "01128718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128718",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2dfd4`](#insn-00c2dfd4)

~~~json
{
  "source": "00c2dfd4",
  "target": "00c2e064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2dfdc`](#insn-00c2dfdc)

~~~json
{
  "source": "00c2dfdc",
  "target": "011286e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2dfe0`](#insn-00c2dfe0)

~~~json
{
  "source": "00c2dfe0",
  "target": "00c2dff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2dff0`](#insn-00c2dff0)

~~~json
{
  "source": "00c2dff0",
  "target": "011286e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2dff4`](#insn-00c2dff4)

~~~json
{
  "source": "00c2dff4",
  "target": "00c2e00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e004`](#insn-00c2e004)

~~~json
{
  "source": "00c2e004",
  "target": "011286f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e008`](#insn-00c2e008)

~~~json
{
  "source": "00c2e008",
  "target": "011286f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e010`](#insn-00c2e010)

~~~json
{
  "source": "00c2e010",
  "target": "011286eb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286eb",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e014`](#insn-00c2e014)

~~~json
{
  "source": "00c2e014",
  "target": "011286e9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011286e9",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e01c`](#insn-00c2e01c)

~~~json
{
  "source": "00c2e01c",
  "target": "01128700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128700",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e020`](#insn-00c2e020)

~~~json
{
  "source": "00c2e020",
  "target": "00c2e038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e030`](#insn-00c2e030)

~~~json
{
  "source": "00c2e030",
  "target": "01128700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128700",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e034`](#insn-00c2e034)

~~~json
{
  "source": "00c2e034",
  "target": "00c2e04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e044`](#insn-00c2e044)

~~~json
{
  "source": "00c2e044",
  "target": "01128710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128710",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e048`](#insn-00c2e048)

~~~json
{
  "source": "00c2e048",
  "target": "01128708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e050`](#insn-00c2e050)

~~~json
{
  "source": "00c2e050",
  "target": "01128701",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128701",
  "offset": 0,
  "size": 2,
  "datatype": "undefined2",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e054`](#insn-00c2e054)

~~~json
{
  "source": "00c2e054",
  "target": "01128703",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128703",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e058`](#insn-00c2e058)

~~~json
{
  "source": "00c2e058",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e068`](#insn-00c2e068)

~~~json
{
  "source": "00c2e068",
  "target": "01128718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128718",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e06c`](#insn-00c2e06c)

~~~json
{
  "source": "00c2e06c",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e070`](#insn-00c2e070)

~~~json
{
  "source": "00c2e070",
  "target": "00c2dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2e078`](#insn-00c2e078)

~~~json
{
  "source": "00c2e078",
  "target": "00c35f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e080`](#insn-00c2e080)

~~~json
{
  "source": "00c2e080",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c2e088`](#insn-00c2e088)

~~~json
{
  "source": "00c2e088",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e090`](#insn-00c2e090)

~~~json
{
  "source": "00c2e090",
  "target": "01128718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128718",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c2e094`](#insn-00c2e094)

~~~json
{
  "source": "00c2e094",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c2e098`](#insn-00c2e098)

~~~json
{
  "source": "00c2e098",
  "target": "00c2dfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
