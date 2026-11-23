# 00afb4cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afb404`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb404.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-f8cd069842e43d8e460c6c4fe16341ec)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb510`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb510.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-003c32c00f5f91b744c917942d214452)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb4cc",
  "name": "_ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fd7ac18a284de48696e4ad956c25278aa775f5946b14e110818240d96f666c9",
  "source_text_sha256": "5fd7ac18a284de48696e4ad956c25278aa775f5946b14e110818240d96f666c9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb4cc",
        "00afb5a7"
      ]
    ],
    "bytes_sha256": "841ab01641908f6c04e138577fc1f1948f6fff7b6fe50beaa7fbacb6b5e876f4",
    "instruction_count": 55,
    "instruction_bytes": 220,
    "body_bytes": 220,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1734 bytes

~~~c

void _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz
               (long *param_1,int param_2,undefined8 param_3,undefined8 param_4,undefined8 param_5,
               undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  int iVar2;
  undefined1 auStack_e0 [8];
  undefined8 local_d8;
  undefined8 uStack_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined1 *local_b0;
  undefined1 **ppuStack_a8;
  undefined1 *puStack_a0;
  undefined8 uStack_98;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  ppuStack_a8 = &local_b0;
  puStack_a0 = auStack_e0;
                    /* try { // try from 00afb528 to 00bfb52f has its CatchHandler @ 00b001d4 */
                    /* try { // try from 00afb530 to 00bfb53f has its CatchHandler @ 00b00224 */
                    /* try { // try from 00afb540 to 00bfb54b has its CatchHandler @ 00b0020c */
  uStack_98 = 0xffffff80ffffffd8;
  local_d8 = param_4;
  uStack_d0 = param_5;
  local_c8 = param_6;
  uStack_c0 = param_7;
  local_b8 = param_8;
  local_b0 = (undefined1 *)register0x00000008;
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
    ppuStack_68 = ppuStack_a8;
    local_70 = local_b0;
    uStack_58 = uStack_98;
    puStack_60 = puStack_a0;
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_70);
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00afb594 to 00bfb5d3 has its CatchHandler @ 00b000ec */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb4cc"></a> `00afb4cc` | `ff 83 05 d1` | sub sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00afb4d0"></a> `00afb4d0` | `fc 93 00 f9` | str x28,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afb4d4"></a> `00afb4d4` | `f6 57 13 a9` | stp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afb4d8"></a> `00afb4d8` | `f4 4f 14 a9` | stp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afb4dc"></a> `00afb4dc` | `fd 7b 15 a9` | stp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00afb4e0"></a> `00afb4e0` | `fd 43 05 91` | add x29,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00afb4e4"></a> `00afb4e4` | `e3 93 08 a9` | stp x3,x4,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00afb4e8"></a> `00afb4e8` | `e5 9b 09 a9` | stp x5,x6,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00afb4ec"></a> `00afb4ec` | `e7 57 00 f9` | str x7,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00afb4f0"></a> `00afb4f0` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00afb4f4"></a> `00afb4f4` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb4f8"></a> `00afb4f8` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afb4fc"></a> `00afb4fc` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb500"></a> `00afb500` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afb504"></a> `00afb504` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb508"></a> `00afb508` | `e9 23 02 91` | add x9,sp,#0x88 | `FALL_THROUGH`
<a id="insn-00afb50c"></a> `00afb50c` | `eb 04 80 92` | mov x11,#-0x28 | `FALL_THROUGH`
<a id="insn-00afb510"></a> `00afb510` | `aa 43 00 91` | add x10,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00afb514"></a> `00afb514` | `a8 83 1c f8` | stur x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00afb518"></a> `00afb518` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00afb51c"></a> `00afb51c` | `0b f0 df f2` | movk x11,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00afb520"></a> `00afb520` | `29 a1 00 91` | add x9,x9,#0x28 | `FALL_THROUGH`
<a id="insn-00afb524"></a> `00afb524` | `08 01 02 91` | add x8,x8,#0x80 | `FALL_THROUGH`
<a id="insn-00afb528"></a> `00afb528` | `aa 27 38 a9` | stp x10,x9,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00afb52c"></a> `00afb52c` | `a8 2f 39 a9` | stp x8,x11,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00afb530"></a> `00afb530` | `a1 03 7c ad` | ldp q1,q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00afb534"></a> `00afb534` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00afb538"></a> `00afb538` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afb53c"></a> `00afb53c` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00afb540"></a> `00afb540` | `a1 03 3b ad` | stp q1,q0,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00afb544"></a> `00afb544` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afb548"></a> `00afb548` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afb54c"></a> `00afb54c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb550"></a> `00afb550` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00afb554"></a> `00afb554` | `4c 01 00 54` | b.gt 0x00afb57c | `CONDITIONAL_JUMP`
<a id="insn-00afb558"></a> `00afb558` | `a0 07 7b ad` | ldp q0,q1,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00afb55c"></a> `00afb55c` | `a3 83 01 d1` | sub x3,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00afb560"></a> `00afb560` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afb564"></a> `00afb564` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afb568"></a> `00afb568` | `a0 07 3d ad` | stp q0,q1,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00afb56c"></a> `00afb56c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00afb570"></a> `00afb570` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00afb574"></a> `00afb574` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afb578"></a> `00afb578` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb57c"></a> `00afb57c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00afb580"></a> `00afb580` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00afb584"></a> `00afb584` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afb588"></a> `00afb588` | `e1 00 00 54` | b.ne 0x00afb5a4 | `CONDITIONAL_JUMP`
<a id="insn-00afb58c"></a> `00afb58c` | `fd 7b 55 a9` | ldp x29,x30,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00afb590"></a> `00afb590` | `f4 4f 54 a9` | ldp x20,x19,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afb594"></a> `00afb594` | `f6 57 53 a9` | ldp x22,x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afb598"></a> `00afb598` | `fc 93 40 f9` | ldr x28,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afb59c"></a> `00afb59c` | `ff 83 05 91` | add sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00afb5a0"></a> `00afb5a0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afb5a4"></a> `00afb5a4` | `a7 7e 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb4cc`](#insn-00afb4cc) 範囲 `[['00afb4cc', '00afb527']]`
  - `FALL_THROUGH` [`00afb524`](#insn-00afb524) → [`00afb528`](#insn-00afb528)
- ブロック [`00afb528`](#insn-00afb528) 範囲 `[['00afb528', '00afb52f']]`
  - `FALL_THROUGH` [`00afb52c`](#insn-00afb52c) → [`00afb530`](#insn-00afb530)
- ブロック [`00afb530`](#insn-00afb530) 範囲 `[['00afb530', '00afb53f']]`
  - `FALL_THROUGH` [`00afb53c`](#insn-00afb53c) → [`00afb540`](#insn-00afb540)
- ブロック [`00afb540`](#insn-00afb540) 範囲 `[['00afb540', '00afb557']]`
  - `CONDITIONAL_JUMP` [`00afb554`](#insn-00afb554) → [`00afb57c`](#insn-00afb57c)
  - `FALL_THROUGH` [`00afb554`](#insn-00afb554) → [`00afb558`](#insn-00afb558)
- ブロック [`00afb558`](#insn-00afb558) 範囲 `[['00afb558', '00afb57b']]`
  - `FALL_THROUGH` [`00afb578`](#insn-00afb578) → [`00afb57c`](#insn-00afb57c)
- ブロック [`00afb57c`](#insn-00afb57c) 範囲 `[['00afb57c', '00afb58b']]`
  - `CONDITIONAL_JUMP` [`00afb588`](#insn-00afb588) → [`00afb5a4`](#insn-00afb5a4)
  - `FALL_THROUGH` [`00afb588`](#insn-00afb588) → [`00afb58c`](#insn-00afb58c)
- ブロック [`00afb58c`](#insn-00afb58c) 範囲 `[['00afb58c', '00afb593']]`
  - `FALL_THROUGH` [`00afb590`](#insn-00afb590) → [`00afb594`](#insn-00afb594)
- ブロック [`00afb594`](#insn-00afb594) 範囲 `[['00afb594', '00afb5a3']]`
- ブロック [`00afb5a4`](#insn-00afb5a4) 範囲 `[['00afb5a4', '00afb5a7']]`

## 命令位置別の参照

- [`00afb4d0`](#insn-00afb4d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4d4`](#insn-00afb4d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4d8`](#insn-00afb4d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4dc`](#insn-00afb4dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4e4`](#insn-00afb4e4) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4e8`](#insn-00afb4e8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4ec`](#insn-00afb4ec) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4f0`](#insn-00afb4f0) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4f4`](#insn-00afb4f4) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4f8`](#insn-00afb4f8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4fc`](#insn-00afb4fc) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb514`](#insn-00afb514) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb528`](#insn-00afb528) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb52c`](#insn-00afb52c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb530`](#insn-00afb530) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb540`](#insn-00afb540) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb554`](#insn-00afb554) → [`00afb57c`](#insn-00afb57c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb558`](#insn-00afb558) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb568`](#insn-00afb568) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb580`](#insn-00afb580) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb588`](#insn-00afb588) → [`00afb5a4`](#insn-00afb5a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb58c`](#insn-00afb58c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb590`](#insn-00afb590) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb594`](#insn-00afb594) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb598`](#insn-00afb598) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5a4`](#insn-00afb5a4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb4d0`](#insn-00afb4d0)

~~~json
{
  "source": "00afb4d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4d4`](#insn-00afb4d4)

~~~json
{
  "source": "00afb4d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4d8`](#insn-00afb4d8)

~~~json
{
  "source": "00afb4d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4dc`](#insn-00afb4dc)

~~~json
{
  "source": "00afb4dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4e4`](#insn-00afb4e4)

~~~json
{
  "source": "00afb4e4",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4e8`](#insn-00afb4e8)

~~~json
{
  "source": "00afb4e8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4ec`](#insn-00afb4ec)

~~~json
{
  "source": "00afb4ec",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4f0`](#insn-00afb4f0)

~~~json
{
  "source": "00afb4f0",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4f4`](#insn-00afb4f4)

~~~json
{
  "source": "00afb4f4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4f8`](#insn-00afb4f8)

~~~json
{
  "source": "00afb4f8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4fc`](#insn-00afb4fc)

~~~json
{
  "source": "00afb4fc",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb514`](#insn-00afb514)

~~~json
{
  "source": "00afb514",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb528`](#insn-00afb528)

~~~json
{
  "source": "00afb528",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb52c`](#insn-00afb52c)

~~~json
{
  "source": "00afb52c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb530`](#insn-00afb530)

~~~json
{
  "source": "00afb530",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb540`](#insn-00afb540)

~~~json
{
  "source": "00afb540",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb554`](#insn-00afb554)

~~~json
{
  "source": "00afb554",
  "target": "00afb57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb558`](#insn-00afb558)

~~~json
{
  "source": "00afb558",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb568`](#insn-00afb568)

~~~json
{
  "source": "00afb568",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb580`](#insn-00afb580)

~~~json
{
  "source": "00afb580",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb588`](#insn-00afb588)

~~~json
{
  "source": "00afb588",
  "target": "00afb5a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb58c`](#insn-00afb58c)

~~~json
{
  "source": "00afb58c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb590`](#insn-00afb590)

~~~json
{
  "source": "00afb590",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb594`](#insn-00afb594)

~~~json
{
  "source": "00afb594",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb598`](#insn-00afb598)

~~~json
{
  "source": "00afb598",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5a4`](#insn-00afb5a4)

~~~json
{
  "source": "00afb5a4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
