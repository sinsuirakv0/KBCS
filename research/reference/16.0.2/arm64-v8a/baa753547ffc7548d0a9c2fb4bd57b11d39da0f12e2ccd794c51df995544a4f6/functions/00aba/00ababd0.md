# 00ababd0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abab60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abab60.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-33759bc39f88ed796e17258643689ef3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00abbbc4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abb/00abbbc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-cb0801467a300418ebcc0b4149a40e09)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ababd0",
  "name": "FUN_00ababd0",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d",
  "source_text_sha256": "0a5d7a715e7299efb119dc5d9fa16ce3bdf2317732f130f7be9fc50e2fd8254d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ababd0",
        "00abad47"
      ]
    ],
    "bytes_sha256": "ff93eb7aa552be614196b0ca70456d0d0159af4c5887e61b2303e0aca0cc41f8",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe6ac](../005fe/005fe6ac.md)

## 呼び出し先

- [00851550](../00851/00851550.md)
- [00ab9228](../00ab9/00ab9228.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2370 bytes

~~~c

void FUN_00ababd0(int param_1,int param_2)

{
  int iVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  int iVar8;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
                    /* try { // try from 00ababe0 to 00bbad53 has its CatchHandler @ 00aba9b0 */
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  if ((param_1 == 3) ||
     (lVar6 = FUN_00851550(), puVar4 = PTR_DAT_00c9b5a0, lVar6 = lVar6 + (long)param_1 * 0x18,
     (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) - *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4
          ) * -0x55555555 < 1)) {
    iVar5 = 0;
  }
  else {
    iVar8 = 0;
    do {
      lVar6 = 0;
      while( true ) {
        lVar7 = FUN_00851550();
                    /* catch() { ... } // from try @ 00ababc8 with catch @ 00abac6c */
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        lVar7 = (long)local_98[0];
        if (local_90 != (void *)0x0) {
          local_88 = local_90;
          _ZdlPv(local_90);
        }
        if (lVar7 <= lVar6) break;
        lVar7 = FUN_00851550();
        FUN_00ab9228(local_98,&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        iVar1 = *(int *)(puVar4 + (long)param_2 * 4);
                    /* catch() { ... } // from try @ 00abaaa4 with catch @ 00abacb0 */
        iVar2 = *(int *)((long)local_90 + lVar6 * 4);
        local_88 = local_90;
        _ZdlPv(local_90);
        lVar6 = lVar6 + 1;
        iVar5 = iVar8;
        if (iVar2 == iVar1) goto LAB_00abad14;
      }
                    /* catch() { ... } // from try @ 00abaa80 with catch @ 00abaccc */
      iVar8 = iVar8 + 1;
      lVar6 = FUN_00851550();
                    /* catch() { ... } // from try @ 00abaafc with catch @ 00abacd4 */
      lVar6 = lVar6 + (long)param_1 * 0x18;
                    /* catch() { ... } // from try @ 00ababa8 with catch @ 00abacdc */
                    /* catch() { ... } // from try @ 00abab20 with catch @ 00abace4 */
      iVar5 = 0;
    } while (iVar8 < (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) -
                                  *(long *)(&uleb128_0029a6e0 + lVar6)) >> 4) * -0x55555555);
  }
LAB_00abad14:
  if (*(long *)(lVar3 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(iVar5);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ababd0"></a> `00ababd0` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00ababd4"></a> `00ababd4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ababd8"></a> `00ababd8` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ababdc"></a> `00ababdc` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ababe0"></a> `00ababe0` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ababe4"></a> `00ababe4` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ababe8"></a> `00ababe8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ababec"></a> `00ababec` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ababf0"></a> `00ababf0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ababf4"></a> `00ababf4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ababf8"></a> `00ababf8` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00ababfc"></a> `00ababfc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abac00"></a> `00abac00` | `40 08 00 54` | b.eq 0x00abad08 | `CONDITIONAL_JUMP`
<a id="insn-00abac04"></a> `00abac04` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00abac08"></a> `00abac08` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abac0c"></a> `00abac0c` | `51 5a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00abac10"></a> `00abac10` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00abac14"></a> `00abac14` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00abac18"></a> `00abac18` | `08 69 4a 91` | add x8,x8,#0x29a, LSL #12 | `FALL_THROUGH`
<a id="insn-00abac1c"></a> `00abac1c` | `08 81 1b 91` | add x8,x8,#0x6e0 | `FALL_THROUGH`
<a id="insn-00abac20"></a> `00abac20` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abac24"></a> `00abac24` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00abac28"></a> `00abac28` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abac2c"></a> `00abac2c` | `08 fd 44 d3` | lsr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00abac30"></a> `00abac30` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00abac34"></a> `00abac34` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abac38"></a> `00abac38` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abac3c"></a> `00abac3c` | `6b 06 00 54` | b.lt 0x00abad08 | `CONDITIONAL_JUMP`
<a id="insn-00abac40"></a> `00abac40` | `19 0f 00 b0` | adrp x25,0xc9b000 | `FALL_THROUGH`
<a id="insn-00abac44"></a> `00abac44` | `98 7e 40 93` | sxtw x24,w20 | `FALL_THROUGH`
<a id="insn-00abac48"></a> `00abac48` | `1a dc 94 52` | mov w26,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00abac4c"></a> `00abac4c` | `39 d3 42 f9` | ldr x25,[x25, #0x5a0] | `FALL_THROUGH`
<a id="insn-00abac50"></a> `00abac50` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00abac54"></a> `00abac54` | `3a 05 a0 72` | movk w26,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00abac58"></a> `00abac58` | `fc 03 1f aa` | mov x28,xzr | `FALL_THROUGH`
<a id="insn-00abac5c"></a> `00abac5c` | `3d 5a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00abac60"></a> `00abac60` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abac64"></a> `00abac64` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abac68"></a> `00abac68` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abac6c"></a> `00abac6c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00abac70"></a> `00abac70` | `6e f9 ff 97` | bl 0x00ab9228 | `UNCONDITIONAL_CALL`
<a id="insn-00abac74"></a> `00abac74` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abac78"></a> `00abac78` | `fb 0b 80 b9` | ldrsw x27,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abac7c"></a> `00abac7c` | `60 00 00 b4` | cbz x0,0x00abac88 | `CONDITIONAL_JUMP`
<a id="insn-00abac80"></a> `00abac80` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abac84"></a> `00abac84` | `bf 74 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00abac88"></a> `00abac88` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00abac8c"></a> `00abac8c` | `0a 02 00 54` | b.ge 0x00abaccc | `CONDITIONAL_JUMP`
<a id="insn-00abac90"></a> `00abac90` | `30 5a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00abac94"></a> `00abac94` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abac98"></a> `00abac98` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abac9c"></a> `00abac9c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abaca0"></a> `00abaca0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00abaca4"></a> `00abaca4` | `61 f9 ff 97` | bl 0x00ab9228 | `UNCONDITIONAL_CALL`
<a id="insn-00abaca8"></a> `00abaca8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abacac"></a> `00abacac` | `37 db 73 b8` | ldr w23,[x25, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00abacb0"></a> `00abacb0` | `1b 78 7c b8` | ldr w27,[x0, x28, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abacb4"></a> `00abacb4` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abacb8"></a> `00abacb8` | `b2 74 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00abacbc"></a> `00abacbc` | `7f 03 17 6b` | cmp w27,w23 | `FALL_THROUGH`
<a id="insn-00abacc0"></a> `00abacc0` | `9c 07 00 91` | add x28,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00abacc4"></a> `00abacc4` | `c1 fc ff 54` | b.ne 0x00abac5c | `CONDITIONAL_JUMP`
<a id="insn-00abacc8"></a> `00abacc8` | `12 00 00 14` | b 0x00abad10 | `UNCONDITIONAL_JUMP`
<a id="insn-00abaccc"></a> `00abaccc` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00abacd0"></a> `00abacd0` | `20 5a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00abacd4"></a> `00abacd4` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00abacd8"></a> `00abacd8` | `08 03 28 9b` | smaddl x8,w24,w8,x0 | `FALL_THROUGH`
<a id="insn-00abacdc"></a> `00abacdc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00abace0"></a> `00abace0` | `08 01 1a 8b` | add x8,x8,x26 | `FALL_THROUGH`
<a id="insn-00abace4"></a> `00abace4` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abace8"></a> `00abace8` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00abacec"></a> `00abacec` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abacf0"></a> `00abacf0` | `08 fd 44 d3` | lsr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00abacf4"></a> `00abacf4` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00abacf8"></a> `00abacf8` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abacfc"></a> `00abacfc` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00abad00"></a> `00abad00` | `cb fa ff 54` | b.lt 0x00abac58 | `CONDITIONAL_JUMP`
<a id="insn-00abad04"></a> `00abad04` | `04 00 00 14` | b 0x00abad14 | `UNCONDITIONAL_JUMP`
<a id="insn-00abad08"></a> `00abad08` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00abad0c"></a> `00abad0c` | `02 00 00 14` | b 0x00abad14 | `UNCONDITIONAL_JUMP`
<a id="insn-00abad10"></a> `00abad10` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abad14"></a> `00abad14` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abad18"></a> `00abad18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abad1c"></a> `00abad1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abad20"></a> `00abad20` | `21 01 00 54` | b.ne 0x00abad44 | `CONDITIONAL_JUMP`
<a id="insn-00abad24"></a> `00abad24` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abad28"></a> `00abad28` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abad2c"></a> `00abad2c` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abad30"></a> `00abad30` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abad34"></a> `00abad34` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abad38"></a> `00abad38` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abad3c"></a> `00abad3c` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abad40"></a> `00abad40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abad44"></a> `00abad44` | `9b 74 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ababd0`](#insn-00ababd0) 範囲 `[['00ababd0', '00ababdf']]`
  - `FALL_THROUGH` [`00ababdc`](#insn-00ababdc) → [`00ababe0`](#insn-00ababe0)
- ブロック [`00ababe0`](#insn-00ababe0) 範囲 `[['00ababe0', '00abac03']]`
  - `CONDITIONAL_JUMP` [`00abac00`](#insn-00abac00) → [`00abad08`](#insn-00abad08)
  - `FALL_THROUGH` [`00abac00`](#insn-00abac00) → [`00abac04`](#insn-00abac04)
- ブロック [`00abac04`](#insn-00abac04) 範囲 `[['00abac04', '00abac3f']]`
  - `CONDITIONAL_JUMP` [`00abac3c`](#insn-00abac3c) → [`00abad08`](#insn-00abad08)
  - `FALL_THROUGH` [`00abac3c`](#insn-00abac3c) → [`00abac40`](#insn-00abac40)
- ブロック [`00abac40`](#insn-00abac40) 範囲 `[['00abac40', '00abac57']]`
  - `FALL_THROUGH` [`00abac54`](#insn-00abac54) → [`00abac58`](#insn-00abac58)
- ブロック [`00abac58`](#insn-00abac58) 範囲 `[['00abac58', '00abac5b']]`
  - `FALL_THROUGH` [`00abac58`](#insn-00abac58) → [`00abac5c`](#insn-00abac5c)
- ブロック [`00abac5c`](#insn-00abac5c) 範囲 `[['00abac5c', '00abac6b']]`
  - `FALL_THROUGH` [`00abac68`](#insn-00abac68) → [`00abac6c`](#insn-00abac6c)
- ブロック [`00abac6c`](#insn-00abac6c) 範囲 `[['00abac6c', '00abac7f']]`
  - `CONDITIONAL_JUMP` [`00abac7c`](#insn-00abac7c) → [`00abac88`](#insn-00abac88)
  - `FALL_THROUGH` [`00abac7c`](#insn-00abac7c) → [`00abac80`](#insn-00abac80)
- ブロック [`00abac80`](#insn-00abac80) 範囲 `[['00abac80', '00abac87']]`
  - `FALL_THROUGH` [`00abac84`](#insn-00abac84) → [`00abac88`](#insn-00abac88)
- ブロック [`00abac88`](#insn-00abac88) 範囲 `[['00abac88', '00abac8f']]`
  - `CONDITIONAL_JUMP` [`00abac8c`](#insn-00abac8c) → [`00abaccc`](#insn-00abaccc)
  - `FALL_THROUGH` [`00abac8c`](#insn-00abac8c) → [`00abac90`](#insn-00abac90)
- ブロック [`00abac90`](#insn-00abac90) 範囲 `[['00abac90', '00abacaf']]`
  - `FALL_THROUGH` [`00abacac`](#insn-00abacac) → [`00abacb0`](#insn-00abacb0)
- ブロック [`00abacb0`](#insn-00abacb0) 範囲 `[['00abacb0', '00abacc7']]`
  - `CONDITIONAL_JUMP` [`00abacc4`](#insn-00abacc4) → [`00abac5c`](#insn-00abac5c)
  - `FALL_THROUGH` [`00abacc4`](#insn-00abacc4) → [`00abacc8`](#insn-00abacc8)
- ブロック [`00abacc8`](#insn-00abacc8) 範囲 `[['00abacc8', '00abaccb']]`
  - `UNCONDITIONAL_JUMP` [`00abacc8`](#insn-00abacc8) → [`00abad10`](#insn-00abad10)
- ブロック [`00abaccc`](#insn-00abaccc) 範囲 `[['00abaccc', '00abacd3']]`
  - `FALL_THROUGH` [`00abacd0`](#insn-00abacd0) → [`00abacd4`](#insn-00abacd4)
- ブロック [`00abacd4`](#insn-00abacd4) 範囲 `[['00abacd4', '00abacdb']]`
  - `FALL_THROUGH` [`00abacd8`](#insn-00abacd8) → [`00abacdc`](#insn-00abacdc)
- ブロック [`00abacdc`](#insn-00abacdc) 範囲 `[['00abacdc', '00abace3']]`
  - `FALL_THROUGH` [`00abace0`](#insn-00abace0) → [`00abace4`](#insn-00abace4)
- ブロック [`00abace4`](#insn-00abace4) 範囲 `[['00abace4', '00abad03']]`
  - `CONDITIONAL_JUMP` [`00abad00`](#insn-00abad00) → [`00abac58`](#insn-00abac58)
  - `FALL_THROUGH` [`00abad00`](#insn-00abad00) → [`00abad04`](#insn-00abad04)
- ブロック [`00abad04`](#insn-00abad04) 範囲 `[['00abad04', '00abad07']]`
  - `UNCONDITIONAL_JUMP` [`00abad04`](#insn-00abad04) → [`00abad14`](#insn-00abad14)
- ブロック [`00abad08`](#insn-00abad08) 範囲 `[['00abad08', '00abad0f']]`
  - `UNCONDITIONAL_JUMP` [`00abad0c`](#insn-00abad0c) → [`00abad14`](#insn-00abad14)
- ブロック [`00abad10`](#insn-00abad10) 範囲 `[['00abad10', '00abad13']]`
  - `FALL_THROUGH` [`00abad10`](#insn-00abad10) → [`00abad14`](#insn-00abad14)
- ブロック [`00abad14`](#insn-00abad14) 範囲 `[['00abad14', '00abad23']]`
  - `CONDITIONAL_JUMP` [`00abad20`](#insn-00abad20) → [`00abad44`](#insn-00abad44)
  - `FALL_THROUGH` [`00abad20`](#insn-00abad20) → [`00abad24`](#insn-00abad24)
- ブロック [`00abad24`](#insn-00abad24) 範囲 `[['00abad24', '00abad43']]`
- ブロック [`00abad44`](#insn-00abad44) 範囲 `[['00abad44', '00abad47']]`

## 命令位置別の参照

- [`00ababd4`](#insn-00ababd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababd8`](#insn-00ababd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababdc`](#insn-00ababdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe0`](#insn-00ababe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe4`](#insn-00ababe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababe8`](#insn-00ababe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ababfc`](#insn-00ababfc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac00`](#insn-00abac00) → [`00abad08`](#insn-00abad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac0c`](#insn-00abac0c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00abac20`](#insn-00abac20) → `0029a6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abac20`](#insn-00abac20) → `0029a6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abac3c`](#insn-00abac3c) → [`00abad08`](#insn-00abad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac4c`](#insn-00abac4c) → `00c9b5a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abac5c`](#insn-00abac5c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00abac70`](#insn-00abac70) → [`00ab9228`](../00ab9/00ab9228.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab9228` · 推定シンボル `None` · 推定型 `None`
- [`00abac74`](#insn-00abac74) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac78`](#insn-00abac78) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac7c`](#insn-00abac7c) → [`00abac88`](#insn-00abac88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac80`](#insn-00abac80) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac84`](#insn-00abac84) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00abac8c`](#insn-00abac8c) → [`00abaccc`](#insn-00abaccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abac90`](#insn-00abac90) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00abaca4`](#insn-00abaca4) → [`00ab9228`](../00ab9/00ab9228.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab9228` · 推定シンボル `None` · 推定型 `None`
- [`00abaca8`](#insn-00abaca8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacac`](#insn-00abacac) → `00ca425c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00abacb4`](#insn-00abacb4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacb8`](#insn-00abacb8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00abacc4`](#insn-00abacc4) → [`00abac5c`](#insn-00abac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacc8`](#insn-00abacc8) → [`00abad10`](#insn-00abad10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abacd0`](#insn-00abacd0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00abace4`](#insn-00abace4) → `0029a6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abace4`](#insn-00abace4) → `0029a6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abad00`](#insn-00abad00) → [`00abac58`](#insn-00abac58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad04`](#insn-00abad04) → [`00abad14`](#insn-00abad14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad0c`](#insn-00abad0c) → [`00abad14`](#insn-00abad14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad18`](#insn-00abad18) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad20`](#insn-00abad20) → [`00abad44`](#insn-00abad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad24`](#insn-00abad24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad28`](#insn-00abad28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad2c`](#insn-00abad2c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad30`](#insn-00abad30) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad34`](#insn-00abad34) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad38`](#insn-00abad38) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abad44`](#insn-00abad44) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ababd4`](#insn-00ababd4)

~~~json
{
  "source": "00ababd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababd8`](#insn-00ababd8)

~~~json
{
  "source": "00ababd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababdc`](#insn-00ababdc)

~~~json
{
  "source": "00ababdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe0`](#insn-00ababe0)

~~~json
{
  "source": "00ababe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe4`](#insn-00ababe4)

~~~json
{
  "source": "00ababe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababe8`](#insn-00ababe8)

~~~json
{
  "source": "00ababe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ababfc`](#insn-00ababfc)

~~~json
{
  "source": "00ababfc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac00`](#insn-00abac00)

~~~json
{
  "source": "00abac00",
  "target": "00abad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac0c`](#insn-00abac0c)

~~~json
{
  "source": "00abac0c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac20`](#insn-00abac20)

~~~json
{
  "source": "00abac20",
  "target": "0029a6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e0",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0029a6e0",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abac20`](#insn-00abac20)

~~~json
{
  "source": "00abac20",
  "target": "0029a6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0029a6e8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abac3c`](#insn-00abac3c)

~~~json
{
  "source": "00abac3c",
  "target": "00abad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac4c`](#insn-00abac4c)

~~~json
{
  "source": "00abac4c",
  "target": "00c9b5a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abac5c`](#insn-00abac5c)

~~~json
{
  "source": "00abac5c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac70`](#insn-00abac70)

~~~json
{
  "source": "00abac70",
  "target": "00ab9228",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac74`](#insn-00abac74)

~~~json
{
  "source": "00abac74",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac78`](#insn-00abac78)

~~~json
{
  "source": "00abac78",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac7c`](#insn-00abac7c)

~~~json
{
  "source": "00abac7c",
  "target": "00abac88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac80`](#insn-00abac80)

~~~json
{
  "source": "00abac80",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac84`](#insn-00abac84)

~~~json
{
  "source": "00abac84",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abac8c`](#insn-00abac8c)

~~~json
{
  "source": "00abac8c",
  "target": "00abaccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abac90`](#insn-00abac90)

~~~json
{
  "source": "00abac90",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaca4`](#insn-00abaca4)

~~~json
{
  "source": "00abaca4",
  "target": "00ab9228",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abaca8`](#insn-00abaca8)

~~~json
{
  "source": "00abaca8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacac`](#insn-00abacac)

~~~json
{
  "source": "00abacac",
  "target": "00ca425c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca425c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abacb4`](#insn-00abacb4)

~~~json
{
  "source": "00abacb4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacb8`](#insn-00abacb8)

~~~json
{
  "source": "00abacb8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abacc4`](#insn-00abacc4)

~~~json
{
  "source": "00abacc4",
  "target": "00abac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacc8`](#insn-00abacc8)

~~~json
{
  "source": "00abacc8",
  "target": "00abad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abacd0`](#insn-00abacd0)

~~~json
{
  "source": "00abacd0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abace4`](#insn-00abace4)

~~~json
{
  "source": "00abace4",
  "target": "0029a6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e0",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0029a6e0",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abace4`](#insn-00abace4)

~~~json
{
  "source": "00abace4",
  "target": "0029a6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0029a6e8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abad00`](#insn-00abad00)

~~~json
{
  "source": "00abad00",
  "target": "00abac58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad04`](#insn-00abad04)

~~~json
{
  "source": "00abad04",
  "target": "00abad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad0c`](#insn-00abad0c)

~~~json
{
  "source": "00abad0c",
  "target": "00abad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad18`](#insn-00abad18)

~~~json
{
  "source": "00abad18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad20`](#insn-00abad20)

~~~json
{
  "source": "00abad20",
  "target": "00abad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad24`](#insn-00abad24)

~~~json
{
  "source": "00abad24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad28`](#insn-00abad28)

~~~json
{
  "source": "00abad28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad2c`](#insn-00abad2c)

~~~json
{
  "source": "00abad2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad30`](#insn-00abad30)

~~~json
{
  "source": "00abad30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad34`](#insn-00abad34)

~~~json
{
  "source": "00abad34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad38`](#insn-00abad38)

~~~json
{
  "source": "00abad38",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abad44`](#insn-00abad44)

~~~json
{
  "source": "00abad44",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
