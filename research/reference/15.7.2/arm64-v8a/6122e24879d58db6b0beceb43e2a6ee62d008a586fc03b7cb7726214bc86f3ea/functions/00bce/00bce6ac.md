# 00bce6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bce774`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-c4c2f3fcff001c0e4e67628fc50e4086)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce6ac",
  "name": "FUN_00bce6ac",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75f03ace31b89b2aed055d88a535a23a5dc0f1fe756c7a6eaabbd5903b1df673",
  "source_text_sha256": "75f03ace31b89b2aed055d88a535a23a5dc0f1fe756c7a6eaabbd5903b1df673",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce6ac",
        "00bce82f"
      ]
    ],
    "bytes_sha256": "baec9038758a7d47765a785d8952f99221dcb83bf7803d44594b8ca1ceec6366",
    "instruction_count": 97,
    "instruction_bytes": 388,
    "body_bytes": 388,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc66f0](../00bc6/00bc66f0.md)
- [00bce830](../00bce/00bce830.md)

## 呼び出し先

- [00bc1bc0](../00bc1/00bc1bc0.md)
- [00bc1f84](../00bc1/00bc1f84.md)
- [00bc20b8](../00bc2/00bc20b8.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2444 bytes

~~~c

void FUN_00bce6ac(long *param_1)

{
  char cVar1;
  long lVar2;
  long *__ptr;
  void *__dest;
  size_t __n;
  long *plVar3;
  long *plVar4;
  
  if ((char *)param_1[1] == (char *)*param_1) {
LAB_00bce730:
    FUN_00bc20b8();
    return;
  }
  cVar1 = *(char *)*param_1;
  if (cVar1 == 'D') {
    lVar2 = FUN_00bc1f84();
    if (lVar2 == 0) {
      return;
    }
    plVar4 = (long *)param_1[0x26];
    if (plVar4 != (long *)param_1[0x27]) goto LAB_00bce804;
    plVar3 = (long *)param_1[0x25];
    __n = (long)plVar4 - (long)plVar3;
    if (plVar3 == param_1 + 0x28) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (plVar4 != plVar3) {
        memmove(__dest,plVar3,__n);
      }
LAB_00bce7e8:
      param_1[0x25] = (long)__dest;
    }
    else {
      __dest = realloc(plVar3,__n * 2);
      param_1[0x25] = (long)__dest;
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
  }
  else {
    if (cVar1 != 'T') goto LAB_00bce730;
                    /* try { // try from 00bce6e8 to 00cce6f7 has its CatchHandler @ 00bcf2e0 */
    lVar2 = FUN_00bc1bc0();
    if (lVar2 == 0) {
      return;
    }
    plVar4 = (long *)param_1[0x26];
                    /* try { // try from 00bce6f8 to 00cce703 has its CatchHandler @ 00bcf2c0 */
    if (plVar4 != (long *)param_1[0x27]) goto LAB_00bce804;
    __ptr = (long *)param_1[0x25];
                    /* try { // try from 00bce708 to 00cce723 has its CatchHandler @ 00bcf274 */
    plVar3 = param_1 + 0x28;
    __n = (long)plVar4 - (long)__ptr;
    if (__ptr == plVar3) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (plVar4 != plVar3) {
        memcpy(__dest,plVar3,__n);
      }
      goto LAB_00bce7e8;
    }
    __dest = realloc(__ptr,__n * 2);
                    /* try { // try from 00bce724 to 00cce887 has its CatchHandler @ 00bce4cc */
    param_1[0x25] = (long)__dest;
    if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
  }
  plVar4 = (long *)((long)__dest + __n);
  param_1[0x27] = (long)((long)__dest + ((long)__n >> 2) * 8);
LAB_00bce804:
  param_1[0x26] = (long)(plVar4 + 1);
  *plVar4 = lVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bce6ac"></a> `00bce6ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bce6b0"></a> `00bce6b0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bce6b4"></a> `00bce6b4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce6b8"></a> `00bce6b8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce6bc"></a> `00bce6bc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce6c0"></a> `00bce6c0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bce6c4"></a> `00bce6c4` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bce6c8"></a> `00bce6c8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce6cc"></a> `00bce6cc` | `20 03 00 54` | b.eq 0x00bce730 | `CONDITIONAL_JUMP`
<a id="insn-00bce6d0"></a> `00bce6d0` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bce6d4"></a> `00bce6d4` | `1f 11 01 71` | cmp w8,#0x44 | `FALL_THROUGH`
<a id="insn-00bce6d8"></a> `00bce6d8` | `80 03 00 54` | b.eq 0x00bce748 | `CONDITIONAL_JUMP`
<a id="insn-00bce6dc"></a> `00bce6dc` | `1f 51 01 71` | cmp w8,#0x54 | `FALL_THROUGH`
<a id="insn-00bce6e0"></a> `00bce6e0` | `81 02 00 54` | b.ne 0x00bce730 | `CONDITIONAL_JUMP`
<a id="insn-00bce6e4"></a> `00bce6e4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bce6e8"></a> `00bce6e8` | `36 cd ff 97` | bl 0x00bc1bc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce6ec"></a> `00bce6ec` | `20 09 00 b4` | cbz x0,0x00bce810 | `CONDITIONAL_JUMP`
<a id="insn-00bce6f0"></a> `00bce6f0` | `f5 26 53 a9` | ldp x21,x9,[x23, #0x130] | `FALL_THROUGH`
<a id="insn-00bce6f4"></a> `00bce6f4` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bce6f8"></a> `00bce6f8` | `bf 02 09 eb` | cmp x21,x9 | `FALL_THROUGH`
<a id="insn-00bce6fc"></a> `00bce6fc` | `41 08 00 54` | b.ne 0x00bce804 | `CONDITIONAL_JUMP`
<a id="insn-00bce700"></a> `00bce700` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bce704"></a> `00bce704` | `00 95 40 f9` | ldr x0,[x8, #0x128] | `FALL_THROUGH`
<a id="insn-00bce708"></a> `00bce708` | `14 01 05 91` | add x20,x8,#0x140 | `FALL_THROUGH`
<a id="insn-00bce70c"></a> `00bce70c` | `b3 02 00 cb` | sub x19,x21,x0 | `FALL_THROUGH`
<a id="insn-00bce710"></a> `00bce710` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00bce714"></a> `00bce714` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bce718"></a> `00bce718` | `00 04 00 54` | b.eq 0x00bce798 | `CONDITIONAL_JUMP`
<a id="insn-00bce71c"></a> `00bce71c` | `8d 3a 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bce720"></a> `00bce720` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bce724"></a> `00bce724` | `e0 96 00 f9` | str x0,[x23, #0x128] | `FALL_THROUGH`
<a id="insn-00bce728"></a> `00bce728` | `40 06 00 b5` | cbnz x0,0x00bce7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bce72c"></a> `00bce72c` | `a5 3e 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce730"></a> `00bce730` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce734"></a> `00bce734` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce738"></a> `00bce738` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce73c"></a> `00bce73c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bce740"></a> `00bce740` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce744"></a> `00bce744` | `5d ce ff 17` | b 0x00bc20b8 | `CALL_TERMINATOR`
<a id="insn-00bce748"></a> `00bce748` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bce74c"></a> `00bce74c` | `0e ce ff 97` | bl 0x00bc1f84 | `UNCONDITIONAL_CALL`
<a id="insn-00bce750"></a> `00bce750` | `00 06 00 b4` | cbz x0,0x00bce810 | `CONDITIONAL_JUMP`
<a id="insn-00bce754"></a> `00bce754` | `f5 26 53 a9` | ldp x21,x9,[x23, #0x130] | `FALL_THROUGH`
<a id="insn-00bce758"></a> `00bce758` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bce75c"></a> `00bce75c` | `bf 02 09 eb` | cmp x21,x9 | `FALL_THROUGH`
<a id="insn-00bce760"></a> `00bce760` | `21 05 00 54` | b.ne 0x00bce804 | `CONDITIONAL_JUMP`
<a id="insn-00bce764"></a> `00bce764` | `14 95 40 f9` | ldr x20,[x8, #0x128] | `FALL_THROUGH`
<a id="insn-00bce768"></a> `00bce768` | `08 01 05 91` | add x8,x8,#0x140 | `FALL_THROUGH`
<a id="insn-00bce76c"></a> `00bce76c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bce770"></a> `00bce770` | `b3 02 14 cb` | sub x19,x21,x20 | `FALL_THROUGH`
<a id="insn-00bce774"></a> `00bce774` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bce778"></a> `00bce778` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bce77c"></a> `00bce77c` | `20 02 00 54` | b.eq 0x00bce7c0 | `CONDITIONAL_JUMP`
<a id="insn-00bce780"></a> `00bce780` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce784"></a> `00bce784` | `73 3a 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bce788"></a> `00bce788` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bce78c"></a> `00bce78c` | `e0 96 00 f9` | str x0,[x23, #0x128] | `FALL_THROUGH`
<a id="insn-00bce790"></a> `00bce790` | `00 03 00 b5` | cbnz x0,0x00bce7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bce794"></a> `00bce794` | `8b 3e 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce798"></a> `00bce798` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bce79c"></a> `00bce79c` | `4d 3a 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce7a0"></a> `00bce7a0` | `40 04 00 b4` | cbz x0,0x00bce828 | `CONDITIONAL_JUMP`
<a id="insn-00bce7a4"></a> `00bce7a4` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bce7a8"></a> `00bce7a8` | `00 02 00 54` | b.eq 0x00bce7e8 | `CONDITIONAL_JUMP`
<a id="insn-00bce7ac"></a> `00bce7ac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bce7b0"></a> `00bce7b0` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bce7b4"></a> `00bce7b4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bce7b8"></a> `00bce7b8` | `3e 32 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce7bc"></a> `00bce7bc` | `0a 00 00 14` | b 0x00bce7e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce7c0"></a> `00bce7c0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bce7c4"></a> `00bce7c4` | `43 3a 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce7c8"></a> `00bce7c8` | `20 03 00 b4` | cbz x0,0x00bce82c | `CONDITIONAL_JUMP`
<a id="insn-00bce7cc"></a> `00bce7cc` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bce7d0"></a> `00bce7d0` | `c0 00 00 54` | b.eq 0x00bce7e8 | `CONDITIONAL_JUMP`
<a id="insn-00bce7d4"></a> `00bce7d4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bce7d8"></a> `00bce7d8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bce7dc"></a> `00bce7dc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bce7e0"></a> `00bce7e0` | `04 32 00 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce7e4"></a> `00bce7e4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bce7e8"></a> `00bce7e8` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bce7ec"></a> `00bce7ec` | `e0 96 00 f9` | str x0,[x23, #0x128] | `FALL_THROUGH`
<a id="insn-00bce7f0"></a> `00bce7f0` | `69 fe 42 93` | asr x9,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00bce7f4"></a> `00bce7f4` | `15 00 13 8b` | add x21,x0,x19 | `FALL_THROUGH`
<a id="insn-00bce7f8"></a> `00bce7f8` | `09 0c 09 8b` | add x9,x0,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bce7fc"></a> `00bce7fc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bce800"></a> `00bce800` | `09 9d 00 f9` | str x9,[x8, #0x138] | `FALL_THROUGH`
<a id="insn-00bce804"></a> `00bce804` | `a9 22 00 91` | add x9,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bce808"></a> `00bce808` | `09 99 00 f9` | str x9,[x8, #0x130] | `FALL_THROUGH`
<a id="insn-00bce80c"></a> `00bce80c` | `a0 02 00 f9` | str x0,[x21] | `FALL_THROUGH`
<a id="insn-00bce810"></a> `00bce810` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce814"></a> `00bce814` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce818"></a> `00bce818` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce81c"></a> `00bce81c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bce820"></a> `00bce820` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce824"></a> `00bce824` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce828"></a> `00bce828` | `66 3e 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce82c"></a> `00bce82c` | `65 3e 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bce6ac`](#insn-00bce6ac) 範囲 `[['00bce6ac', '00bce6cf']]`
  - `CONDITIONAL_JUMP` [`00bce6cc`](#insn-00bce6cc) → [`00bce730`](#insn-00bce730)
  - `FALL_THROUGH` [`00bce6cc`](#insn-00bce6cc) → [`00bce6d0`](#insn-00bce6d0)
- ブロック [`00bce6d0`](#insn-00bce6d0) 範囲 `[['00bce6d0', '00bce6db']]`
  - `CONDITIONAL_JUMP` [`00bce6d8`](#insn-00bce6d8) → [`00bce748`](#insn-00bce748)
  - `FALL_THROUGH` [`00bce6d8`](#insn-00bce6d8) → [`00bce6dc`](#insn-00bce6dc)
- ブロック [`00bce6dc`](#insn-00bce6dc) 範囲 `[['00bce6dc', '00bce6e3']]`
  - `CONDITIONAL_JUMP` [`00bce6e0`](#insn-00bce6e0) → [`00bce730`](#insn-00bce730)
  - `FALL_THROUGH` [`00bce6e0`](#insn-00bce6e0) → [`00bce6e4`](#insn-00bce6e4)
- ブロック [`00bce6e4`](#insn-00bce6e4) 範囲 `[['00bce6e4', '00bce6e7']]`
  - `FALL_THROUGH` [`00bce6e4`](#insn-00bce6e4) → [`00bce6e8`](#insn-00bce6e8)
- ブロック [`00bce6e8`](#insn-00bce6e8) 範囲 `[['00bce6e8', '00bce6ef']]`
  - `CONDITIONAL_JUMP` [`00bce6ec`](#insn-00bce6ec) → [`00bce810`](#insn-00bce810)
  - `FALL_THROUGH` [`00bce6ec`](#insn-00bce6ec) → [`00bce6f0`](#insn-00bce6f0)
- ブロック [`00bce6f0`](#insn-00bce6f0) 範囲 `[['00bce6f0', '00bce6f7']]`
  - `FALL_THROUGH` [`00bce6f4`](#insn-00bce6f4) → [`00bce6f8`](#insn-00bce6f8)
- ブロック [`00bce6f8`](#insn-00bce6f8) 範囲 `[['00bce6f8', '00bce6ff']]`
  - `CONDITIONAL_JUMP` [`00bce6fc`](#insn-00bce6fc) → [`00bce804`](#insn-00bce804)
  - `FALL_THROUGH` [`00bce6fc`](#insn-00bce6fc) → [`00bce700`](#insn-00bce700)
- ブロック [`00bce700`](#insn-00bce700) 範囲 `[['00bce700', '00bce707']]`
  - `FALL_THROUGH` [`00bce704`](#insn-00bce704) → [`00bce708`](#insn-00bce708)
- ブロック [`00bce708`](#insn-00bce708) 範囲 `[['00bce708', '00bce71b']]`
  - `CONDITIONAL_JUMP` [`00bce718`](#insn-00bce718) → [`00bce798`](#insn-00bce798)
  - `FALL_THROUGH` [`00bce718`](#insn-00bce718) → [`00bce71c`](#insn-00bce71c)
- ブロック [`00bce71c`](#insn-00bce71c) 範囲 `[['00bce71c', '00bce723']]`
  - `FALL_THROUGH` [`00bce720`](#insn-00bce720) → [`00bce724`](#insn-00bce724)
- ブロック [`00bce724`](#insn-00bce724) 範囲 `[['00bce724', '00bce72b']]`
  - `CONDITIONAL_JUMP` [`00bce728`](#insn-00bce728) → [`00bce7f0`](#insn-00bce7f0)
  - `FALL_THROUGH` [`00bce728`](#insn-00bce728) → [`00bce72c`](#insn-00bce72c)
- ブロック [`00bce72c`](#insn-00bce72c) 範囲 `[['00bce72c', '00bce72f']]`
- ブロック [`00bce730`](#insn-00bce730) 範囲 `[['00bce730', '00bce747']]`
- ブロック [`00bce748`](#insn-00bce748) 範囲 `[['00bce748', '00bce753']]`
  - `CONDITIONAL_JUMP` [`00bce750`](#insn-00bce750) → [`00bce810`](#insn-00bce810)
  - `FALL_THROUGH` [`00bce750`](#insn-00bce750) → [`00bce754`](#insn-00bce754)
- ブロック [`00bce754`](#insn-00bce754) 範囲 `[['00bce754', '00bce763']]`
  - `CONDITIONAL_JUMP` [`00bce760`](#insn-00bce760) → [`00bce804`](#insn-00bce804)
  - `FALL_THROUGH` [`00bce760`](#insn-00bce760) → [`00bce764`](#insn-00bce764)
- ブロック [`00bce764`](#insn-00bce764) 範囲 `[['00bce764', '00bce77f']]`
  - `CONDITIONAL_JUMP` [`00bce77c`](#insn-00bce77c) → [`00bce7c0`](#insn-00bce7c0)
  - `FALL_THROUGH` [`00bce77c`](#insn-00bce77c) → [`00bce780`](#insn-00bce780)
- ブロック [`00bce780`](#insn-00bce780) 範囲 `[['00bce780', '00bce793']]`
  - `CONDITIONAL_JUMP` [`00bce790`](#insn-00bce790) → [`00bce7f0`](#insn-00bce7f0)
  - `FALL_THROUGH` [`00bce790`](#insn-00bce790) → [`00bce794`](#insn-00bce794)
- ブロック [`00bce794`](#insn-00bce794) 範囲 `[['00bce794', '00bce797']]`
- ブロック [`00bce798`](#insn-00bce798) 範囲 `[['00bce798', '00bce7a3']]`
  - `CONDITIONAL_JUMP` [`00bce7a0`](#insn-00bce7a0) → [`00bce828`](#insn-00bce828)
  - `FALL_THROUGH` [`00bce7a0`](#insn-00bce7a0) → [`00bce7a4`](#insn-00bce7a4)
- ブロック [`00bce7a4`](#insn-00bce7a4) 範囲 `[['00bce7a4', '00bce7ab']]`
  - `CONDITIONAL_JUMP` [`00bce7a8`](#insn-00bce7a8) → [`00bce7e8`](#insn-00bce7e8)
  - `FALL_THROUGH` [`00bce7a8`](#insn-00bce7a8) → [`00bce7ac`](#insn-00bce7ac)
- ブロック [`00bce7ac`](#insn-00bce7ac) 範囲 `[['00bce7ac', '00bce7bf']]`
  - `UNCONDITIONAL_JUMP` [`00bce7bc`](#insn-00bce7bc) → [`00bce7e4`](#insn-00bce7e4)
- ブロック [`00bce7c0`](#insn-00bce7c0) 範囲 `[['00bce7c0', '00bce7cb']]`
  - `CONDITIONAL_JUMP` [`00bce7c8`](#insn-00bce7c8) → [`00bce82c`](#insn-00bce82c)
  - `FALL_THROUGH` [`00bce7c8`](#insn-00bce7c8) → [`00bce7cc`](#insn-00bce7cc)
- ブロック [`00bce7cc`](#insn-00bce7cc) 範囲 `[['00bce7cc', '00bce7d3']]`
  - `CONDITIONAL_JUMP` [`00bce7d0`](#insn-00bce7d0) → [`00bce7e8`](#insn-00bce7e8)
  - `FALL_THROUGH` [`00bce7d0`](#insn-00bce7d0) → [`00bce7d4`](#insn-00bce7d4)
- ブロック [`00bce7d4`](#insn-00bce7d4) 範囲 `[['00bce7d4', '00bce7e3']]`
  - `FALL_THROUGH` [`00bce7e0`](#insn-00bce7e0) → [`00bce7e4`](#insn-00bce7e4)
- ブロック [`00bce7e4`](#insn-00bce7e4) 範囲 `[['00bce7e4', '00bce7e7']]`
  - `FALL_THROUGH` [`00bce7e4`](#insn-00bce7e4) → [`00bce7e8`](#insn-00bce7e8)
- ブロック [`00bce7e8`](#insn-00bce7e8) 範囲 `[['00bce7e8', '00bce7ef']]`
  - `FALL_THROUGH` [`00bce7ec`](#insn-00bce7ec) → [`00bce7f0`](#insn-00bce7f0)
- ブロック [`00bce7f0`](#insn-00bce7f0) 範囲 `[['00bce7f0', '00bce803']]`
  - `FALL_THROUGH` [`00bce800`](#insn-00bce800) → [`00bce804`](#insn-00bce804)
- ブロック [`00bce804`](#insn-00bce804) 範囲 `[['00bce804', '00bce80f']]`
  - `FALL_THROUGH` [`00bce80c`](#insn-00bce80c) → [`00bce810`](#insn-00bce810)
- ブロック [`00bce810`](#insn-00bce810) 範囲 `[['00bce810', '00bce827']]`
- ブロック [`00bce828`](#insn-00bce828) 範囲 `[['00bce828', '00bce82b']]`
- ブロック [`00bce82c`](#insn-00bce82c) 範囲 `[['00bce82c', '00bce82f']]`

## 命令位置別の参照

- [`00bce6b0`](#insn-00bce6b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6b4`](#insn-00bce6b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6b8`](#insn-00bce6b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6bc`](#insn-00bce6bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6cc`](#insn-00bce6cc) → [`00bce730`](#insn-00bce730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6d8`](#insn-00bce6d8) → [`00bce748`](#insn-00bce748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6e0`](#insn-00bce6e0) → [`00bce730`](#insn-00bce730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6e8`](#insn-00bce6e8) → [`00bc1bc0`](../00bc1/00bc1bc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1bc0` · 推定シンボル `None` · 推定型 `None`
- [`00bce6ec`](#insn-00bce6ec) → [`00bce810`](#insn-00bce810) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6fc`](#insn-00bce6fc) → [`00bce804`](#insn-00bce804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce718`](#insn-00bce718) → [`00bce798`](#insn-00bce798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce71c`](#insn-00bce71c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bce728`](#insn-00bce728) → [`00bce7f0`](#insn-00bce7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce72c`](#insn-00bce72c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce730`](#insn-00bce730) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce734`](#insn-00bce734) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce738`](#insn-00bce738) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce73c`](#insn-00bce73c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce744`](#insn-00bce744) → [`00bc20b8`](../00bc2/00bc20b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc20b8` · 推定シンボル `None` · 推定型 `None`
- [`00bce74c`](#insn-00bce74c) → [`00bc1f84`](../00bc1/00bc1f84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1f84` · 推定シンボル `None` · 推定型 `None`
- [`00bce750`](#insn-00bce750) → [`00bce810`](#insn-00bce810) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce760`](#insn-00bce760) → [`00bce804`](#insn-00bce804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce77c`](#insn-00bce77c) → [`00bce7c0`](#insn-00bce7c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce784`](#insn-00bce784) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bce790`](#insn-00bce790) → [`00bce7f0`](#insn-00bce7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce794`](#insn-00bce794) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce79c`](#insn-00bce79c) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bce7a0`](#insn-00bce7a0) → [`00bce828`](#insn-00bce828) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce7a8`](#insn-00bce7a8) → [`00bce7e8`](#insn-00bce7e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce7b8`](#insn-00bce7b8) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bce7bc`](#insn-00bce7bc) → [`00bce7e4`](#insn-00bce7e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce7c4`](#insn-00bce7c4) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bce7c8`](#insn-00bce7c8) → [`00bce82c`](#insn-00bce82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce7d0`](#insn-00bce7d0) → [`00bce7e8`](#insn-00bce7e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce7e0`](#insn-00bce7e0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00bce810`](#insn-00bce810) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce814`](#insn-00bce814) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce818`](#insn-00bce818) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce81c`](#insn-00bce81c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce828`](#insn-00bce828) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce82c`](#insn-00bce82c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce6b0`](#insn-00bce6b0)

~~~json
{
  "source": "00bce6b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6b4`](#insn-00bce6b4)

~~~json
{
  "source": "00bce6b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6b8`](#insn-00bce6b8)

~~~json
{
  "source": "00bce6b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6bc`](#insn-00bce6bc)

~~~json
{
  "source": "00bce6bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6cc`](#insn-00bce6cc)

~~~json
{
  "source": "00bce6cc",
  "target": "00bce730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6d8`](#insn-00bce6d8)

~~~json
{
  "source": "00bce6d8",
  "target": "00bce748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6e0`](#insn-00bce6e0)

~~~json
{
  "source": "00bce6e0",
  "target": "00bce730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6e8`](#insn-00bce6e8)

~~~json
{
  "source": "00bce6e8",
  "target": "00bc1bc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce6ec`](#insn-00bce6ec)

~~~json
{
  "source": "00bce6ec",
  "target": "00bce810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6fc`](#insn-00bce6fc)

~~~json
{
  "source": "00bce6fc",
  "target": "00bce804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce718`](#insn-00bce718)

~~~json
{
  "source": "00bce718",
  "target": "00bce798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce71c`](#insn-00bce71c)

~~~json
{
  "source": "00bce71c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce728`](#insn-00bce728)

~~~json
{
  "source": "00bce728",
  "target": "00bce7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce72c`](#insn-00bce72c)

~~~json
{
  "source": "00bce72c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce730`](#insn-00bce730)

~~~json
{
  "source": "00bce730",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce734`](#insn-00bce734)

~~~json
{
  "source": "00bce734",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce738`](#insn-00bce738)

~~~json
{
  "source": "00bce738",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce73c`](#insn-00bce73c)

~~~json
{
  "source": "00bce73c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce744`](#insn-00bce744)

~~~json
{
  "source": "00bce744",
  "target": "00bc20b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce74c`](#insn-00bce74c)

~~~json
{
  "source": "00bce74c",
  "target": "00bc1f84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce750`](#insn-00bce750)

~~~json
{
  "source": "00bce750",
  "target": "00bce810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce760`](#insn-00bce760)

~~~json
{
  "source": "00bce760",
  "target": "00bce804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce77c`](#insn-00bce77c)

~~~json
{
  "source": "00bce77c",
  "target": "00bce7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce784`](#insn-00bce784)

~~~json
{
  "source": "00bce784",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce790`](#insn-00bce790)

~~~json
{
  "source": "00bce790",
  "target": "00bce7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce794`](#insn-00bce794)

~~~json
{
  "source": "00bce794",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce79c`](#insn-00bce79c)

~~~json
{
  "source": "00bce79c",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce7a0`](#insn-00bce7a0)

~~~json
{
  "source": "00bce7a0",
  "target": "00bce828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce7a8`](#insn-00bce7a8)

~~~json
{
  "source": "00bce7a8",
  "target": "00bce7e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce7b8`](#insn-00bce7b8)

~~~json
{
  "source": "00bce7b8",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce7bc`](#insn-00bce7bc)

~~~json
{
  "source": "00bce7bc",
  "target": "00bce7e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce7c4`](#insn-00bce7c4)

~~~json
{
  "source": "00bce7c4",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce7c8`](#insn-00bce7c8)

~~~json
{
  "source": "00bce7c8",
  "target": "00bce82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce7d0`](#insn-00bce7d0)

~~~json
{
  "source": "00bce7d0",
  "target": "00bce7e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce7e0`](#insn-00bce7e0)

~~~json
{
  "source": "00bce7e0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce810`](#insn-00bce810)

~~~json
{
  "source": "00bce810",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce814`](#insn-00bce814)

~~~json
{
  "source": "00bce814",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce818`](#insn-00bce818)

~~~json
{
  "source": "00bce818",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce81c`](#insn-00bce81c)

~~~json
{
  "source": "00bce81c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce828`](#insn-00bce828)

~~~json
{
  "source": "00bce828",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce82c`](#insn-00bce82c)

~~~json
{
  "source": "00bce82c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
