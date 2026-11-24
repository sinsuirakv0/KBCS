# 00abbbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ababd0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aba/00ababd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-cb0801467a300418ebcc0b4149a40e09)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abbbc4",
  "name": "FUN_00abbbc4",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e024db009c5aa530f8fe630be4a5dfed593c69a82a63a309c71ff2067589e1e5",
  "source_text_sha256": "e024db009c5aa530f8fe630be4a5dfed593c69a82a63a309c71ff2067589e1e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abbbc4",
        "00abbd3b"
      ]
    ],
    "bytes_sha256": "f86c9dd71c078c94adccd6ec29b00e83ce34b1ad2e64b914e9010e45c2a5073c",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [00aba21c](../00aba/00aba21c.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3400 bytes

~~~c

void FUN_00abbbc4(int param_1,int param_2)

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
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00abbb74 with catch @ 00abbc18 */
  if ((param_1 == 3) ||
     (lVar6 = FUN_008524fc(), puVar4 = PTR_DAT_00c9c570, lVar6 = lVar6 + (long)param_1 * 0x18,
     (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) - *(long *)((long)&uleb128_0029a6e0 + lVar6)
                  ) >> 4) * -0x55555555 < 1)) {
    iVar5 = 0;
                    /* catch() { ... } // from try @ 00abbe50 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc070 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc1f0 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc364 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc4b8 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc5b4 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc864 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abc954 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abca44 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abcc78 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abce0c with catch @ 00abbd00
                       catch() { ... } // from try @ 00abced4 with catch @ 00abbd00
                       catch() { ... } // from try @ 00abcf8c with catch @ 00abbd00 */
  }
  else {
    iVar8 = 0;
    do {
      lVar6 = 0;
      while( true ) {
        lVar7 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00abba50 with catch @ 00abbc5c */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        lVar7 = (long)local_98[0];
        if (local_90 != (void *)0x0) {
          local_88 = local_90;
                    /* catch() { ... } // from try @ 00abba2c with catch @ 00abbc78 */
          _ZdlPv(local_90);
        }
                    /* catch() { ... } // from try @ 00abbaa8 with catch @ 00abbc80 */
        if (lVar7 <= lVar6) break;
        lVar7 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00abbb54 with catch @ 00abbc88 */
                    /* catch() { ... } // from try @ 00abbacc with catch @ 00abbc90 */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar7,param_1,iVar8);
        iVar1 = *(int *)(puVar4 + (long)param_2 * 4);
        iVar2 = *(int *)((long)local_90 + lVar6 * 4);
        local_88 = local_90;
        _ZdlPv(local_90);
        lVar6 = lVar6 + 1;
        iVar5 = iVar8;
        if (iVar2 == iVar1) goto LAB_00abbd08;
      }
      iVar8 = iVar8 + 1;
      lVar6 = FUN_008524fc();
      lVar6 = lVar6 + (long)param_1 * 0x18;
      iVar5 = 0;
    } while (iVar8 < (int)((ulong)(*(long *)(&uleb128_0029a6e8 + lVar6) -
                                  *(long *)((long)&uleb128_0029a6e0 + lVar6)) >> 4) * -0x55555555);
  }
LAB_00abbd08:
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
<a id="insn-00abbbc4"></a> `00abbbc4` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abbbc8"></a> `00abbbc8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abbbcc"></a> `00abbbcc` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abbbd0"></a> `00abbbd0` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abbbd4"></a> `00abbbd4` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abbbd8"></a> `00abbbd8` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abbbdc"></a> `00abbbdc` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abbbe0"></a> `00abbbe0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abbbe4"></a> `00abbbe4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abbbe8"></a> `00abbbe8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abbbec"></a> `00abbbec` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00abbbf0"></a> `00abbbf0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abbbf4"></a> `00abbbf4` | `40 08 00 54` | b.eq 0x00abbcfc | `CONDITIONAL_JUMP`
<a id="insn-00abbbf8"></a> `00abbbf8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00abbbfc"></a> `00abbbfc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abbc00"></a> `00abbc00` | `3f 5a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbc04"></a> `00abbc04` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00abbc08"></a> `00abbc08` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00abbc0c"></a> `00abbc0c` | `08 69 4a 91` | add x8,x8,#0x29a, LSL #12 | `FALL_THROUGH`
<a id="insn-00abbc10"></a> `00abbc10` | `08 81 1b 91` | add x8,x8,#0x6e0 | `FALL_THROUGH`
<a id="insn-00abbc14"></a> `00abbc14` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abbc18"></a> `00abbc18` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00abbc1c"></a> `00abbc1c` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abbc20"></a> `00abbc20` | `08 fd 44 d3` | lsr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00abbc24"></a> `00abbc24` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00abbc28"></a> `00abbc28` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abbc2c"></a> `00abbc2c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abbc30"></a> `00abbc30` | `6b 06 00 54` | b.lt 0x00abbcfc | `CONDITIONAL_JUMP`
<a id="insn-00abbc34"></a> `00abbc34` | `19 0f 00 b0` | adrp x25,0xc9c000 | `FALL_THROUGH`
<a id="insn-00abbc38"></a> `00abbc38` | `98 7e 40 93` | sxtw x24,w20 | `FALL_THROUGH`
<a id="insn-00abbc3c"></a> `00abbc3c` | `1a dc 94 52` | mov w26,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00abbc40"></a> `00abbc40` | `39 bb 42 f9` | ldr x25,[x25, #0x570] | `FALL_THROUGH`
<a id="insn-00abbc44"></a> `00abbc44` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00abbc48"></a> `00abbc48` | `3a 05 a0 72` | movk w26,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00abbc4c"></a> `00abbc4c` | `fc 03 1f aa` | mov x28,xzr | `FALL_THROUGH`
<a id="insn-00abbc50"></a> `00abbc50` | `2b 5a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbc54"></a> `00abbc54` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbc58"></a> `00abbc58` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbc5c"></a> `00abbc5c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbc60"></a> `00abbc60` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00abbc64"></a> `00abbc64` | `6e f9 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbc68"></a> `00abbc68` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbc6c"></a> `00abbc6c` | `fb 0b 80 b9` | ldrsw x27,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abbc70"></a> `00abbc70` | `60 00 00 b4` | cbz x0,0x00abbc7c | `CONDITIONAL_JUMP`
<a id="insn-00abbc74"></a> `00abbc74` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbc78"></a> `00abbc78` | `b6 74 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abbc7c"></a> `00abbc7c` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00abbc80"></a> `00abbc80` | `0a 02 00 54` | b.ge 0x00abbcc0 | `CONDITIONAL_JUMP`
<a id="insn-00abbc84"></a> `00abbc84` | `1e 5a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbc88"></a> `00abbc88` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbc8c"></a> `00abbc8c` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbc90"></a> `00abbc90` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbc94"></a> `00abbc94` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00abbc98"></a> `00abbc98` | `61 f9 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbc9c"></a> `00abbc9c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbca0"></a> `00abbca0` | `37 db 73 b8` | ldr w23,[x25, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00abbca4"></a> `00abbca4` | `1b 78 7c b8` | ldr w27,[x0, x28, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abbca8"></a> `00abbca8` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbcac"></a> `00abbcac` | `a9 74 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abbcb0"></a> `00abbcb0` | `7f 03 17 6b` | cmp w27,w23 | `FALL_THROUGH`
<a id="insn-00abbcb4"></a> `00abbcb4` | `9c 07 00 91` | add x28,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00abbcb8"></a> `00abbcb8` | `c1 fc ff 54` | b.ne 0x00abbc50 | `CONDITIONAL_JUMP`
<a id="insn-00abbcbc"></a> `00abbcbc` | `12 00 00 14` | b 0x00abbd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbcc0"></a> `00abbcc0` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00abbcc4"></a> `00abbcc4` | `0e 5a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbcc8"></a> `00abbcc8` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00abbccc"></a> `00abbccc` | `08 03 28 9b` | smaddl x8,w24,w8,x0 | `FALL_THROUGH`
<a id="insn-00abbcd0"></a> `00abbcd0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00abbcd4"></a> `00abbcd4` | `08 01 1a 8b` | add x8,x8,x26 | `FALL_THROUGH`
<a id="insn-00abbcd8"></a> `00abbcd8` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abbcdc"></a> `00abbcdc` | `28 01 08 cb` | sub x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00abbce0"></a> `00abbce0` | `69 55 95 52` | mov w9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abbce4"></a> `00abbce4` | `08 fd 44 d3` | lsr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00abbce8"></a> `00abbce8` | `49 55 b5 72` | movk w9,#0xaaaa, LSL #16 | `FALL_THROUGH`
<a id="insn-00abbcec"></a> `00abbcec` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abbcf0"></a> `00abbcf0` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00abbcf4"></a> `00abbcf4` | `cb fa ff 54` | b.lt 0x00abbc4c | `CONDITIONAL_JUMP`
<a id="insn-00abbcf8"></a> `00abbcf8` | `04 00 00 14` | b 0x00abbd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbcfc"></a> `00abbcfc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00abbd00"></a> `00abbd00` | `02 00 00 14` | b 0x00abbd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbd04"></a> `00abbd04` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abbd08"></a> `00abbd08` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abbd0c"></a> `00abbd0c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abbd10"></a> `00abbd10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abbd14"></a> `00abbd14` | `21 01 00 54` | b.ne 0x00abbd38 | `CONDITIONAL_JUMP`
<a id="insn-00abbd18"></a> `00abbd18` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abbd1c"></a> `00abbd1c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abbd20"></a> `00abbd20` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abbd24"></a> `00abbd24` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abbd28"></a> `00abbd28` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abbd2c"></a> `00abbd2c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abbd30"></a> `00abbd30` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abbd34"></a> `00abbd34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abbd38"></a> `00abbd38` | `92 74 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abbbc4`](#insn-00abbbc4) 範囲 `[['00abbbc4', '00abbbf7']]`
  - `CONDITIONAL_JUMP` [`00abbbf4`](#insn-00abbbf4) → [`00abbcfc`](#insn-00abbcfc)
  - `FALL_THROUGH` [`00abbbf4`](#insn-00abbbf4) → [`00abbbf8`](#insn-00abbbf8)
- ブロック [`00abbbf8`](#insn-00abbbf8) 範囲 `[['00abbbf8', '00abbc17']]`
  - `FALL_THROUGH` [`00abbc14`](#insn-00abbc14) → [`00abbc18`](#insn-00abbc18)
- ブロック [`00abbc18`](#insn-00abbc18) 範囲 `[['00abbc18', '00abbc33']]`
  - `CONDITIONAL_JUMP` [`00abbc30`](#insn-00abbc30) → [`00abbcfc`](#insn-00abbcfc)
  - `FALL_THROUGH` [`00abbc30`](#insn-00abbc30) → [`00abbc34`](#insn-00abbc34)
- ブロック [`00abbc34`](#insn-00abbc34) 範囲 `[['00abbc34', '00abbc4b']]`
  - `FALL_THROUGH` [`00abbc48`](#insn-00abbc48) → [`00abbc4c`](#insn-00abbc4c)
- ブロック [`00abbc4c`](#insn-00abbc4c) 範囲 `[['00abbc4c', '00abbc4f']]`
  - `FALL_THROUGH` [`00abbc4c`](#insn-00abbc4c) → [`00abbc50`](#insn-00abbc50)
- ブロック [`00abbc50`](#insn-00abbc50) 範囲 `[['00abbc50', '00abbc5b']]`
  - `FALL_THROUGH` [`00abbc58`](#insn-00abbc58) → [`00abbc5c`](#insn-00abbc5c)
- ブロック [`00abbc5c`](#insn-00abbc5c) 範囲 `[['00abbc5c', '00abbc73']]`
  - `CONDITIONAL_JUMP` [`00abbc70`](#insn-00abbc70) → [`00abbc7c`](#insn-00abbc7c)
  - `FALL_THROUGH` [`00abbc70`](#insn-00abbc70) → [`00abbc74`](#insn-00abbc74)
- ブロック [`00abbc74`](#insn-00abbc74) 範囲 `[['00abbc74', '00abbc77']]`
  - `FALL_THROUGH` [`00abbc74`](#insn-00abbc74) → [`00abbc78`](#insn-00abbc78)
- ブロック [`00abbc78`](#insn-00abbc78) 範囲 `[['00abbc78', '00abbc7b']]`
  - `FALL_THROUGH` [`00abbc78`](#insn-00abbc78) → [`00abbc7c`](#insn-00abbc7c)
- ブロック [`00abbc7c`](#insn-00abbc7c) 範囲 `[['00abbc7c', '00abbc7f']]`
  - `FALL_THROUGH` [`00abbc7c`](#insn-00abbc7c) → [`00abbc80`](#insn-00abbc80)
- ブロック [`00abbc80`](#insn-00abbc80) 範囲 `[['00abbc80', '00abbc83']]`
  - `CONDITIONAL_JUMP` [`00abbc80`](#insn-00abbc80) → [`00abbcc0`](#insn-00abbcc0)
  - `FALL_THROUGH` [`00abbc80`](#insn-00abbc80) → [`00abbc84`](#insn-00abbc84)
- ブロック [`00abbc84`](#insn-00abbc84) 範囲 `[['00abbc84', '00abbc87']]`
  - `FALL_THROUGH` [`00abbc84`](#insn-00abbc84) → [`00abbc88`](#insn-00abbc88)
- ブロック [`00abbc88`](#insn-00abbc88) 範囲 `[['00abbc88', '00abbc8f']]`
  - `FALL_THROUGH` [`00abbc8c`](#insn-00abbc8c) → [`00abbc90`](#insn-00abbc90)
- ブロック [`00abbc90`](#insn-00abbc90) 範囲 `[['00abbc90', '00abbcbb']]`
  - `CONDITIONAL_JUMP` [`00abbcb8`](#insn-00abbcb8) → [`00abbc50`](#insn-00abbc50)
  - `FALL_THROUGH` [`00abbcb8`](#insn-00abbcb8) → [`00abbcbc`](#insn-00abbcbc)
- ブロック [`00abbcbc`](#insn-00abbcbc) 範囲 `[['00abbcbc', '00abbcbf']]`
  - `UNCONDITIONAL_JUMP` [`00abbcbc`](#insn-00abbcbc) → [`00abbd04`](#insn-00abbd04)
- ブロック [`00abbcc0`](#insn-00abbcc0) 範囲 `[['00abbcc0', '00abbcf7']]`
  - `CONDITIONAL_JUMP` [`00abbcf4`](#insn-00abbcf4) → [`00abbc4c`](#insn-00abbc4c)
  - `FALL_THROUGH` [`00abbcf4`](#insn-00abbcf4) → [`00abbcf8`](#insn-00abbcf8)
- ブロック [`00abbcf8`](#insn-00abbcf8) 範囲 `[['00abbcf8', '00abbcfb']]`
  - `UNCONDITIONAL_JUMP` [`00abbcf8`](#insn-00abbcf8) → [`00abbd08`](#insn-00abbd08)
- ブロック [`00abbcfc`](#insn-00abbcfc) 範囲 `[['00abbcfc', '00abbcff']]`
  - `FALL_THROUGH` [`00abbcfc`](#insn-00abbcfc) → [`00abbd00`](#insn-00abbd00)
- ブロック [`00abbd00`](#insn-00abbd00) 範囲 `[['00abbd00', '00abbd03']]`
  - `UNCONDITIONAL_JUMP` [`00abbd00`](#insn-00abbd00) → [`00abbd08`](#insn-00abbd08)
- ブロック [`00abbd04`](#insn-00abbd04) 範囲 `[['00abbd04', '00abbd07']]`
  - `FALL_THROUGH` [`00abbd04`](#insn-00abbd04) → [`00abbd08`](#insn-00abbd08)
- ブロック [`00abbd08`](#insn-00abbd08) 範囲 `[['00abbd08', '00abbd17']]`
  - `CONDITIONAL_JUMP` [`00abbd14`](#insn-00abbd14) → [`00abbd38`](#insn-00abbd38)
  - `FALL_THROUGH` [`00abbd14`](#insn-00abbd14) → [`00abbd18`](#insn-00abbd18)
- ブロック [`00abbd18`](#insn-00abbd18) 範囲 `[['00abbd18', '00abbd37']]`
- ブロック [`00abbd38`](#insn-00abbd38) 範囲 `[['00abbd38', '00abbd3b']]`

## 命令位置別の参照

- [`00abbbc8`](#insn-00abbbc8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbcc`](#insn-00abbbcc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbd0`](#insn-00abbbd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbd4`](#insn-00abbbd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbd8`](#insn-00abbbd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbdc`](#insn-00abbbdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbf0`](#insn-00abbbf0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbbf4`](#insn-00abbbf4) → [`00abbcfc`](#insn-00abbcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc00`](#insn-00abbc00) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbc14`](#insn-00abbc14) → `0029a6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abbc14`](#insn-00abbc14) → `0029a6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abbc30`](#insn-00abbc30) → [`00abbcfc`](#insn-00abbcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc40`](#insn-00abbc40) → `00c9c570`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abbc50`](#insn-00abbc50) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbc64`](#insn-00abbc64) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbc68`](#insn-00abbc68) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc6c`](#insn-00abbc6c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc70`](#insn-00abbc70) → [`00abbc7c`](#insn-00abbc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc74`](#insn-00abbc74) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc78`](#insn-00abbc78) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abbc80`](#insn-00abbc80) → [`00abbcc0`](#insn-00abbcc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbc84`](#insn-00abbc84) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbc98`](#insn-00abbc98) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbc9c`](#insn-00abbc9c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbca0`](#insn-00abbca0) → `00ca522c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00abbca8`](#insn-00abbca8) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbcac`](#insn-00abbcac) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abbcb8`](#insn-00abbcb8) → [`00abbc50`](#insn-00abbc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbcbc`](#insn-00abbcbc) → [`00abbd04`](#insn-00abbd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbcc4`](#insn-00abbcc4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbcd8`](#insn-00abbcd8) → `0029a6e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abbcd8`](#insn-00abbcd8) → `0029a6e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00abbcf4`](#insn-00abbcf4) → [`00abbc4c`](#insn-00abbc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbcf8`](#insn-00abbcf8) → [`00abbd08`](#insn-00abbd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd00`](#insn-00abbd00) → [`00abbd08`](#insn-00abbd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd0c`](#insn-00abbd0c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd14`](#insn-00abbd14) → [`00abbd38`](#insn-00abbd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd18`](#insn-00abbd18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd1c`](#insn-00abbd1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd20`](#insn-00abbd20) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd24`](#insn-00abbd24) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd28`](#insn-00abbd28) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd2c`](#insn-00abbd2c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd38`](#insn-00abbd38) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abbbc8`](#insn-00abbbc8)

~~~json
{
  "source": "00abbbc8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbcc`](#insn-00abbbcc)

~~~json
{
  "source": "00abbbcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbd0`](#insn-00abbbd0)

~~~json
{
  "source": "00abbbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbd4`](#insn-00abbbd4)

~~~json
{
  "source": "00abbbd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbd8`](#insn-00abbbd8)

~~~json
{
  "source": "00abbbd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbdc`](#insn-00abbbdc)

~~~json
{
  "source": "00abbbdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbf0`](#insn-00abbbf0)

~~~json
{
  "source": "00abbbf0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbbf4`](#insn-00abbbf4)

~~~json
{
  "source": "00abbbf4",
  "target": "00abbcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc00`](#insn-00abbc00)

~~~json
{
  "source": "00abbc00",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc14`](#insn-00abbc14)

~~~json
{
  "source": "00abbc14",
  "target": "0029a6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e0",
  "offset": 0,
  "size": 2,
  "datatype": "uleb128",
  "bytes": "bc02",
  "capture_start": "0029a6e0",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbc14`](#insn-00abbc14)

~~~json
{
  "source": "00abbc14",
  "target": "0029a6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "28",
  "capture_start": "0029a6e8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbc30`](#insn-00abbc30)

~~~json
{
  "source": "00abbc30",
  "target": "00abbcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc40`](#insn-00abbc40)

~~~json
{
  "source": "00abbc40",
  "target": "00c9c570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c570",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abbc50`](#insn-00abbc50)

~~~json
{
  "source": "00abbc50",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc64`](#insn-00abbc64)

~~~json
{
  "source": "00abbc64",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc68`](#insn-00abbc68)

~~~json
{
  "source": "00abbc68",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc6c`](#insn-00abbc6c)

~~~json
{
  "source": "00abbc6c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc70`](#insn-00abbc70)

~~~json
{
  "source": "00abbc70",
  "target": "00abbc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc74`](#insn-00abbc74)

~~~json
{
  "source": "00abbc74",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc78`](#insn-00abbc78)

~~~json
{
  "source": "00abbc78",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc80`](#insn-00abbc80)

~~~json
{
  "source": "00abbc80",
  "target": "00abbcc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbc84`](#insn-00abbc84)

~~~json
{
  "source": "00abbc84",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc98`](#insn-00abbc98)

~~~json
{
  "source": "00abbc98",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbc9c`](#insn-00abbc9c)

~~~json
{
  "source": "00abbc9c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbca0`](#insn-00abbca0)

~~~json
{
  "source": "00abbca0",
  "target": "00ca522c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca522c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abbca8`](#insn-00abbca8)

~~~json
{
  "source": "00abbca8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbcac`](#insn-00abbcac)

~~~json
{
  "source": "00abbcac",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbcb8`](#insn-00abbcb8)

~~~json
{
  "source": "00abbcb8",
  "target": "00abbc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbcbc`](#insn-00abbcbc)

~~~json
{
  "source": "00abbcbc",
  "target": "00abbd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbcc4`](#insn-00abbcc4)

~~~json
{
  "source": "00abbcc4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbcd8`](#insn-00abbcd8)

~~~json
{
  "source": "00abbcd8",
  "target": "0029a6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e0",
  "offset": 0,
  "size": 2,
  "datatype": "uleb128",
  "bytes": "bc02",
  "capture_start": "0029a6e0",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbcd8`](#insn-00abbcd8)

~~~json
{
  "source": "00abbcd8",
  "target": "0029a6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6e8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "28",
  "capture_start": "0029a6e8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbcf4`](#insn-00abbcf4)

~~~json
{
  "source": "00abbcf4",
  "target": "00abbc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbcf8`](#insn-00abbcf8)

~~~json
{
  "source": "00abbcf8",
  "target": "00abbd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd00`](#insn-00abbd00)

~~~json
{
  "source": "00abbd00",
  "target": "00abbd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd0c`](#insn-00abbd0c)

~~~json
{
  "source": "00abbd0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd14`](#insn-00abbd14)

~~~json
{
  "source": "00abbd14",
  "target": "00abbd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd18`](#insn-00abbd18)

~~~json
{
  "source": "00abbd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd1c`](#insn-00abbd1c)

~~~json
{
  "source": "00abbd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd20`](#insn-00abbd20)

~~~json
{
  "source": "00abbd20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd24`](#insn-00abbd24)

~~~json
{
  "source": "00abbd24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd28`](#insn-00abbd28)

~~~json
{
  "source": "00abbd28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd2c`](#insn-00abbd2c)

~~~json
{
  "source": "00abbd2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd38`](#insn-00abbd38)

~~~json
{
  "source": "00abbd38",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
