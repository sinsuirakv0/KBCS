# 00aeec8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeebf0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeebf0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-92cd9dbe66e9d6cacc9360724dd5a971)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aefc80`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefc80.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-81f4c1a124b1a3d51e0b5e63a2c2406e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeec8c",
  "name": "FUN_00aeec8c",
  "size": 644,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "613129abf52f2c22bbb7df435e1459ed63668ac0aa48c3b1ca69c0eb7620cbf3",
  "source_text_sha256": "613129abf52f2c22bbb7df435e1459ed63668ac0aa48c3b1ca69c0eb7620cbf3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeec8c",
        "00aeef0f"
      ]
    ],
    "bytes_sha256": "ef6317d434d00b65c04cea1da633793b232a4acfbb5163c99dc01191e69870e2",
    "instruction_count": 161,
    "instruction_bytes": 644,
    "body_bytes": 644,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00467ba0](../00467/00467ba0.md)
- [00469c44](../00469/00469c44.md)
- [0046db2c](../0046d/0046db2c.md)
- [00489f8c](../00489/00489f8c.md)
- [00851550](../00851/00851550.md)
- [008b6df4](../008b6/008b6df4.md)
- [008b7a20](../008b7/008b7a20.md)
- [008b92e8](../008b9/008b92e8.md)
- [008b9344](../008b9/008b9344.md)
- [008b9864](../008b9/008b9864.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4474 bytes

~~~c

void FUN_00aeec8c(long param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  bool bVar9;
  int iVar10;
  long lVar11;
  undefined8 uVar12;
  long lVar13;
  long lVar14;
  long lVar15;
  bool bVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  uint uVar19;
  long lVar20;
  undefined1 auVar21 [16];
  undefined1 local_78 [16];
  long local_68;
  
                    /* try { // try from 00aeeca8 to 00beecab has its CatchHandler @ 00aeecc4 */
                    /* catch() { ... } // from try @ 00aeeb04 with catch @ 00aeecac
                       try { // try from 00aeecac to 00beed03 has its CatchHandler @ 00aee9c4 */
  lVar8 = tpidr_el0;
  local_68 = *(long *)(lVar8 + 0x28);
  uVar17 = *param_2;
                    /* catch() { ... } // from try @ 00aeea24 with catch @ 00aeecbc */
  uVar18 = *param_3;
  lVar20 = *(long *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00aeea68 with catch @ 00aeecc4
                       catch() { ... } // from try @ 00aeeca8 with catch @ 00aeecc4 */
  iVar10 = FUN_008b92e8(uVar17);
  if (iVar10 != 0) {
    FUN_0046db2c(local_78);
    if (DAT_00ca4a78 == 0) {
      lVar11 = 0;
    }
    else {
      lVar11 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                              &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
    }
    uVar19 = 0;
    bVar9 = true;
    do {
      bVar16 = bVar9;
      iVar10 = FUN_008b9864(uVar17,uVar19);
      auVar21 = FUN_008b9344(uVar17,uVar19);
      local_78 = auVar21;
      lVar13 = FUN_00489f8c(*(undefined8 *)(lVar11 + 0x118),uVar19 | 0x2a);
      lVar14 = FUN_00851550();
      if (bVar16) {
        lVar14 = FUN_00851550();
        lVar15 = FUN_00851550();
        lVar14 = lVar14 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar15 + 3) * 0x2c;
                    /* try { // try from 00aeee7c to 00beef53 has its CatchHandler @ 00aeee7c
                       catch() { ... } // from try @ 00aeee7c with catch @ 00aeee7c
                       catch() { ... } // from try @ 00aeef5c with catch @ 00aeee7c */
        auVar21 = local_78;
        if ((int)((uint)(*(byte *)(lVar14 + 0xc5e2) ^ *(byte *)(lVar14 + 0xc5ba)) << 0x10 |
                  (uint)(*(byte *)(lVar14 + 0xc5e3) ^ *(byte *)(lVar14 + 0xc5bb)) << 0x18 |
                  (uint)(*(byte *)(lVar14 + 0xc5e1) ^ *(byte *)(lVar14 + 0xc5b9)) << 8 |
                 (uint)(*(byte *)(lVar14 + 0xc5e0) ^ *(byte *)(lVar14 + 0xc5b8))) < 2) {
LAB_00aeed20:
          FUN_00467ba0(uVar18,0x7f,0x7f,0x7f,0xff);
          auVar21 = local_78;
        }
      }
      else {
        auVar21 = local_78;
        if (*(int *)((long)&fde_table_entry_00333b98.data_loc + lVar14) < 2) {
          lVar14 = FUN_00851550();
          auVar21 = local_78;
          if ((*(byte *)(lVar14 + 0x33a5) & 1) == 0) goto LAB_00aeed20;
        }
      }
      local_78._8_8_ = auVar21._8_8_;
      uVar12 = local_78._8_8_;
      local_78._8_4_ = auVar21._8_4_;
      local_78._12_4_ = auVar21._12_4_;
      iVar4 = *(int *)(lVar13 + 8);
      iVar5 = *(int *)(lVar13 + 0xc);
      local_78._0_4_ = auVar21._0_4_;
      local_78._4_4_ = auVar21._4_4_;
      if ((int)local_78._8_4_ < 0) {
        local_78._8_4_ = local_78._8_4_ + 1;
      }
      iVar2 = iVar4 + iVar10;
      if (iVar4 < 0) {
        iVar4 = iVar4 + 1;
      }
      iVar3 = iVar5 + iVar10;
      if (iVar10 < 0) {
        iVar10 = iVar10 + 1;
      }
      if ((long)uVar12 < 0) {
        local_78._12_4_ = local_78._12_4_ + 1;
      }
      iVar6 = local_78._0_4_ - (iVar10 >> 1);
      iVar7 = local_78._4_4_ - (iVar10 >> 1);
      iVar10 = (int)local_78._8_4_ >> 1;
      iVar1 = (int)local_78._12_4_ >> 1;
      if (iVar5 < 0) {
        iVar5 = iVar5 + 1;
      }
      local_78 = auVar21;
      FUN_00469c44(uVar18,*(undefined8 *)(lVar11 + 0x118),(iVar6 + iVar10) - (iVar4 >> 1),
                   (iVar7 + iVar1) - (iVar5 >> 1),iVar2,iVar3,uVar19 | 0x2a);
      FUN_00467ba0(uVar18,0xff,0xff,0xff,0xff);
      uVar12 = FUN_008b7a20(lVar20 + 0x2f38,0x321);
      FUN_008b6df4(uVar12,0,0);
      uVar12 = FUN_008b7a20(lVar20 + 0x2f38,800);
      FUN_008b6df4(uVar12,0,0);
      uVar19 = 1;
      bVar9 = false;
    } while (bVar16);
  }
  if (*(long *)(lVar8 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeec8c"></a> `00aeec8c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00aeec90"></a> `00aeec90` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeec94"></a> `00aeec94` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeec98"></a> `00aeec98` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeec9c"></a> `00aeec9c` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeeca0"></a> `00aeeca0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeeca4"></a> `00aeeca4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeeca8"></a> `00aeeca8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeecac"></a> `00aeecac` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeecb0"></a> `00aeecb0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeecb4"></a> `00aeecb4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeecb8"></a> `00aeecb8` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aeecbc"></a> `00aeecbc` | `54 00 40 f9` | ldr x20,[x2] | `FALL_THROUGH`
<a id="insn-00aeecc0"></a> `00aeecc0` | `1b 04 40 f9` | ldr x27,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeecc4"></a> `00aeecc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeecc8"></a> `00aeecc8` | `88 29 f7 97` | bl 0x008b92e8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeccc"></a> `00aeeccc` | `80 10 00 34` | cbz w0,0x00aeeedc | `CONDITIONAL_JUMP`
<a id="insn-00aeecd0"></a> `00aeecd0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aeecd4"></a> `00aeecd4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00aeecd8"></a> `00aeecd8` | `95 fb e5 97` | bl 0x0046db2c | `UNCONDITIONAL_CALL`
<a id="insn-00aeecdc"></a> `00aeecdc` | `a8 0d 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aeece0"></a> `00aeece0` | `00 3d 45 f9` | ldr x0,[x8, #0xa78] | `FALL_THROUGH`
<a id="insn-00aeece4"></a> `00aeece4` | `20 01 00 b4` | cbz x0,0x00aeed08 | `CONDITIONAL_JUMP`
<a id="insn-00aeece8"></a> `00aeece8` | `a1 0b 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aeecec"></a> `00aeecec` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-00aeecf0"></a> `00aeecf0` | `e2 0c 00 f0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeecf4"></a> `00aeecf4` | `42 80 28 91` | add x2,x2,#0xa20 | `FALL_THROUGH`
<a id="insn-00aeecf8"></a> `00aeecf8` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aeecfc"></a> `00aeecfc` | `79 a6 05 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed00"></a> `00aeed00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aeed04"></a> `00aeed04` | `02 00 00 14` | b 0x00aeed0c | `UNCONDITIONAL_JUMP`
<a id="insn-00aeed08"></a> `00aeed08` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aeed0c"></a> `00aeed0c` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00aeed10"></a> `00aeed10` | `19 e7 85 52` | mov w25,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aeed14"></a> `00aeed14` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeed18"></a> `00aeed18` | `5a 05 80 52` | mov w26,#0x2a | `FALL_THROUGH`
<a id="insn-00aeed1c"></a> `00aeed1c` | `36 00 00 14` | b 0x00aeedf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeed20"></a> `00aeed20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeed24"></a> `00aeed24` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aeed28"></a> `00aeed28` | `e2 0f 80 52` | mov w2,#0x7f | `FALL_THROUGH`
<a id="insn-00aeed2c"></a> `00aeed2c` | `e3 0f 80 52` | mov w3,#0x7f | `FALL_THROUGH`
<a id="insn-00aeed30"></a> `00aeed30` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aeed34"></a> `00aeed34` | `9b e3 e5 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed38"></a> `00aeed38` | `e8 2b 42 29` | ldp w8,w10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeed3c"></a> `00aeed3c` | `09 2f 41 29` | ldp w9,w11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00aeed40"></a> `00aeed40` | `ee 3f 41 29` | ldp w14,w15,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeed44"></a> `00aeed44` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aeed48"></a> `00aeed48` | `a1 8e 40 f9` | ldr x1,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aeed4c"></a> `00aeed4c` | `c6 02 1a 2a` | orr w6,w22,w26 | `FALL_THROUGH`
<a id="insn-00aeed50"></a> `00aeed50` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00aeed54"></a> `00aeed54` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00aeed58"></a> `00aeed58` | `24 01 17 0b` | add w4,w9,w23 | `FALL_THROUGH`
<a id="insn-00aeed5c"></a> `00aeed5c` | `2c a5 89 1a` | cinc w12,w9,lt | `FALL_THROUGH`
<a id="insn-00aeed60"></a> `00aeed60` | `ff 02 00 71` | cmp w23,#0x0 | `FALL_THROUGH`
<a id="insn-00aeed64"></a> `00aeed64` | `65 01 17 0b` | add w5,w11,w23 | `FALL_THROUGH`
<a id="insn-00aeed68"></a> `00aeed68` | `ed a6 97 1a` | cinc w13,w23,lt | `FALL_THROUGH`
<a id="insn-00aeed6c"></a> `00aeed6c` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00aeed70"></a> `00aeed70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeed74"></a> `00aeed74` | `ad 7d 01 13` | asr w13,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00aeed78"></a> `00aeed78` | `4a a5 8a 1a` | cinc w10,w10,lt | `FALL_THROUGH`
<a id="insn-00aeed7c"></a> `00aeed7c` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-00aeed80"></a> `00aeed80` | `ce 01 0d 4b` | sub w14,w14,w13 | `FALL_THROUGH`
<a id="insn-00aeed84"></a> `00aeed84` | `ed 01 0d 4b` | sub w13,w15,w13 | `FALL_THROUGH`
<a id="insn-00aeed88"></a> `00aeed88` | `c8 05 88 0b` | add w8,w14,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeed8c"></a> `00aeed8c` | `aa 05 8a 0b` | add w10,w13,w10, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeed90"></a> `00aeed90` | `6d a5 8b 1a` | cinc w13,w11,lt | `FALL_THROUGH`
<a id="insn-00aeed94"></a> `00aeed94` | `02 05 8c 4b` | sub w2,w8,w12, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeed98"></a> `00aeed98` | `43 05 8d 4b` | sub w3,w10,w13, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeed9c"></a> `00aeed9c` | `aa eb e5 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeda0"></a> `00aeeda0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeeda4"></a> `00aeeda4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aeeda8"></a> `00aeeda8` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aeedac"></a> `00aeedac` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aeedb0"></a> `00aeedb0` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aeedb4"></a> `00aeedb4` | `7b e3 e5 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeedb8"></a> `00aeedb8` | `60 03 19 8b` | add x0,x27,x25 | `FALL_THROUGH`
<a id="insn-00aeedbc"></a> `00aeedbc` | `21 64 80 52` | mov w1,#0x321 | `FALL_THROUGH`
<a id="insn-00aeedc0"></a> `00aeedc0` | `18 23 f7 97` | bl 0x008b7a20 | `UNCONDITIONAL_CALL`
<a id="insn-00aeedc4"></a> `00aeedc4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeedc8"></a> `00aeedc8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeedcc"></a> `00aeedcc` | `0a 20 f7 97` | bl 0x008b6df4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeedd0"></a> `00aeedd0` | `60 03 19 8b` | add x0,x27,x25 | `FALL_THROUGH`
<a id="insn-00aeedd4"></a> `00aeedd4` | `01 64 80 52` | mov w1,#0x320 | `FALL_THROUGH`
<a id="insn-00aeedd8"></a> `00aeedd8` | `12 23 f7 97` | bl 0x008b7a20 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeddc"></a> `00aeeddc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeede0"></a> `00aeede0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeede4"></a> `00aeede4` | `04 20 f7 97` | bl 0x008b6df4 | `UNCONDITIONAL_CALL`
<a id="insn-00aeede8"></a> `00aeede8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00aeedec"></a> `00aeedec` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00aeedf0"></a> `00aeedf0` | `5c 07 00 36` | tbz w28,#0x0,0x00aeeed8 | `CONDITIONAL_JUMP`
<a id="insn-00aeedf4"></a> `00aeedf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeedf8"></a> `00aeedf8` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aeedfc"></a> `00aeedfc` | `fc 03 08 2a` | mov w28,w8 | `FALL_THROUGH`
<a id="insn-00aeee00"></a> `00aeee00` | `99 2a f7 97` | bl 0x008b9864 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee04"></a> `00aeee04` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aeee08"></a> `00aeee08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeee0c"></a> `00aeee0c` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aeee10"></a> `00aeee10` | `4d 29 f7 97` | bl 0x008b9344 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee14"></a> `00aeee14` | `a8 8e 40 f9` | ldr x8,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aeee18"></a> `00aeee18` | `e0 87 00 a9` | stp x0,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeee1c"></a> `00aeee1c` | `c1 02 1a 2a` | orr w1,w22,w26 | `FALL_THROUGH`
<a id="insn-00aeee20"></a> `00aeee20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeee24"></a> `00aeee24` | `5a 6c e6 97` | bl 0x00489f8c | `UNCONDITIONAL_CALL`
<a id="insn-00aeee28"></a> `00aeee28` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aeee2c"></a> `00aeee2c` | `c9 89 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee30"></a> `00aeee30` | `1c 04 00 36` | tbz w28,#0x0,0x00aeeeb0 | `CONDITIONAL_JUMP`
<a id="insn-00aeee34"></a> `00aeee34` | `c7 89 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee38"></a> `00aeee38` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00aeee3c"></a> `00aeee3c` | `c5 89 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee40"></a> `00aeee40` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aeee44"></a> `00aeee44` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00aeee48"></a> `00aeee48` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeee4c"></a> `00aeee4c` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeee50"></a> `00aeee50` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aeee54"></a> `00aeee54` | `08 65 29 9b` | smaddl x8,w8,w9,x25 | `FALL_THROUGH`
<a id="insn-00aeee58"></a> `00aeee58` | `09 b7 98 52` | mov w9,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00aeee5c"></a> `00aeee5c` | `19 e7 85 52` | mov w25,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aeee60"></a> `00aeee60` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aeee64"></a> `00aeee64` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aeee68"></a> `00aeee68` | `0a a9 40 39` | ldrb w10,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aeee6c"></a> `00aeee6c` | `0b ad 40 39` | ldrb w11,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aeee70"></a> `00aeee70` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aeee74"></a> `00aeee74` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aeee78"></a> `00aeee78` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aeee7c"></a> `00aeee7c` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00aeee80"></a> `00aeee80` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aeee84"></a> `00aeee84` | `0b a5 40 39` | ldrb w11,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aeee88"></a> `00aeee88` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aeee8c"></a> `00aeee8c` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00aeee90"></a> `00aeee90` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aeee94"></a> `00aeee94` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aeee98"></a> `00aeee98` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aeee9c"></a> `00aeee9c` | `08 01 0a 4a` | eor w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00aeeea0"></a> `00aeeea0` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aeeea4"></a> `00aeeea4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeeea8"></a> `00aeeea8` | `cd f3 ff 54` | b.le 0x00aeed20 | `CONDITIONAL_JUMP`
<a id="insn-00aeeeac"></a> `00aeeeac` | `a3 ff ff 17` | b 0x00aeed38 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeeeb0"></a> `00aeeeb0` | `88 73 87 52` | mov w8,#0x3b9c | `FALL_THROUGH`
<a id="insn-00aeeeb4"></a> `00aeeeb4` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeeeb8"></a> `00aeeeb8` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeeebc"></a> `00aeeebc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeeec0"></a> `00aeeec0` | `cc f3 ff 54` | b.gt 0x00aeed38 | `CONDITIONAL_JUMP`
<a id="insn-00aeeec4"></a> `00aeeec4` | `a3 89 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeec8"></a> `00aeeec8` | `a8 74 86 52` | mov w8,#0x33a5 | `FALL_THROUGH`
<a id="insn-00aeeecc"></a> `00aeeecc` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00aeeed0"></a> `00aeeed0` | `48 f3 07 37` | tbnz w8,#0x0,0x00aeed38 | `CONDITIONAL_JUMP`
<a id="insn-00aeeed4"></a> `00aeeed4` | `93 ff ff 17` | b 0x00aeed20 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeeed8"></a> `00aeeed8` | `f5 03 40 f9` | ldr x21,[sp] | `FALL_THROUGH`
<a id="insn-00aeeedc"></a> `00aeeedc` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeeee0"></a> `00aeeee0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeeee4"></a> `00aeeee4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeeee8"></a> `00aeeee8` | `21 01 00 54` | b.ne 0x00aeef0c | `CONDITIONAL_JUMP`
<a id="insn-00aeeeec"></a> `00aeeeec` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeeef0"></a> `00aeeef0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeeef4"></a> `00aeeef4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeeef8"></a> `00aeeef8` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeeefc"></a> `00aeeefc` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeef00"></a> `00aeef00` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeef04"></a> `00aeef04` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00aeef08"></a> `00aeef08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeef0c"></a> `00aeef0c` | `29 a4 05 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeec8c`](#insn-00aeec8c) 範囲 `[['00aeec8c', '00aeeca7']]`
  - `FALL_THROUGH` [`00aeeca4`](#insn-00aeeca4) → [`00aeeca8`](#insn-00aeeca8)
- ブロック [`00aeeca8`](#insn-00aeeca8) 範囲 `[['00aeeca8', '00aeecab']]`
  - `FALL_THROUGH` [`00aeeca8`](#insn-00aeeca8) → [`00aeecac`](#insn-00aeecac)
- ブロック [`00aeecac`](#insn-00aeecac) 範囲 `[['00aeecac', '00aeecbb']]`
  - `FALL_THROUGH` [`00aeecb8`](#insn-00aeecb8) → [`00aeecbc`](#insn-00aeecbc)
- ブロック [`00aeecbc`](#insn-00aeecbc) 範囲 `[['00aeecbc', '00aeecc3']]`
  - `FALL_THROUGH` [`00aeecc0`](#insn-00aeecc0) → [`00aeecc4`](#insn-00aeecc4)
- ブロック [`00aeecc4`](#insn-00aeecc4) 範囲 `[['00aeecc4', '00aeeccf']]`
  - `CONDITIONAL_JUMP` [`00aeeccc`](#insn-00aeeccc) → [`00aeeedc`](#insn-00aeeedc)
  - `FALL_THROUGH` [`00aeeccc`](#insn-00aeeccc) → [`00aeecd0`](#insn-00aeecd0)
- ブロック [`00aeecd0`](#insn-00aeecd0) 範囲 `[['00aeecd0', '00aeece7']]`
  - `CONDITIONAL_JUMP` [`00aeece4`](#insn-00aeece4) → [`00aeed08`](#insn-00aeed08)
  - `FALL_THROUGH` [`00aeece4`](#insn-00aeece4) → [`00aeece8`](#insn-00aeece8)
- ブロック [`00aeece8`](#insn-00aeece8) 範囲 `[['00aeece8', '00aeed07']]`
  - `UNCONDITIONAL_JUMP` [`00aeed04`](#insn-00aeed04) → [`00aeed0c`](#insn-00aeed0c)
- ブロック [`00aeed08`](#insn-00aeed08) 範囲 `[['00aeed08', '00aeed0b']]`
  - `FALL_THROUGH` [`00aeed08`](#insn-00aeed08) → [`00aeed0c`](#insn-00aeed0c)
- ブロック [`00aeed0c`](#insn-00aeed0c) 範囲 `[['00aeed0c', '00aeed1f']]`
  - `UNCONDITIONAL_JUMP` [`00aeed1c`](#insn-00aeed1c) → [`00aeedf4`](#insn-00aeedf4)
- ブロック [`00aeed20`](#insn-00aeed20) 範囲 `[['00aeed20', '00aeed37']]`
  - `FALL_THROUGH` [`00aeed34`](#insn-00aeed34) → [`00aeed38`](#insn-00aeed38)
- ブロック [`00aeed38`](#insn-00aeed38) 範囲 `[['00aeed38', '00aeedf3']]`
  - `CONDITIONAL_JUMP` [`00aeedf0`](#insn-00aeedf0) → [`00aeeed8`](#insn-00aeeed8)
  - `FALL_THROUGH` [`00aeedf0`](#insn-00aeedf0) → [`00aeedf4`](#insn-00aeedf4)
- ブロック [`00aeedf4`](#insn-00aeedf4) 範囲 `[['00aeedf4', '00aeee33']]`
  - `CONDITIONAL_JUMP` [`00aeee30`](#insn-00aeee30) → [`00aeeeb0`](#insn-00aeeeb0)
  - `FALL_THROUGH` [`00aeee30`](#insn-00aeee30) → [`00aeee34`](#insn-00aeee34)
- ブロック [`00aeee34`](#insn-00aeee34) 範囲 `[['00aeee34', '00aeee7b']]`
  - `FALL_THROUGH` [`00aeee78`](#insn-00aeee78) → [`00aeee7c`](#insn-00aeee7c)
- ブロック [`00aeee7c`](#insn-00aeee7c) 範囲 `[['00aeee7c', '00aeeeab']]`
  - `CONDITIONAL_JUMP` [`00aeeea8`](#insn-00aeeea8) → [`00aeed20`](#insn-00aeed20)
  - `FALL_THROUGH` [`00aeeea8`](#insn-00aeeea8) → [`00aeeeac`](#insn-00aeeeac)
- ブロック [`00aeeeac`](#insn-00aeeeac) 範囲 `[['00aeeeac', '00aeeeaf']]`
  - `UNCONDITIONAL_JUMP` [`00aeeeac`](#insn-00aeeeac) → [`00aeed38`](#insn-00aeed38)
- ブロック [`00aeeeb0`](#insn-00aeeeb0) 範囲 `[['00aeeeb0', '00aeeec3']]`
  - `CONDITIONAL_JUMP` [`00aeeec0`](#insn-00aeeec0) → [`00aeed38`](#insn-00aeed38)
  - `FALL_THROUGH` [`00aeeec0`](#insn-00aeeec0) → [`00aeeec4`](#insn-00aeeec4)
- ブロック [`00aeeec4`](#insn-00aeeec4) 範囲 `[['00aeeec4', '00aeeed3']]`
  - `CONDITIONAL_JUMP` [`00aeeed0`](#insn-00aeeed0) → [`00aeed38`](#insn-00aeed38)
  - `FALL_THROUGH` [`00aeeed0`](#insn-00aeeed0) → [`00aeeed4`](#insn-00aeeed4)
- ブロック [`00aeeed4`](#insn-00aeeed4) 範囲 `[['00aeeed4', '00aeeed7']]`
  - `UNCONDITIONAL_JUMP` [`00aeeed4`](#insn-00aeeed4) → [`00aeed20`](#insn-00aeed20)
- ブロック [`00aeeed8`](#insn-00aeeed8) 範囲 `[['00aeeed8', '00aeeedb']]`
  - `FALL_THROUGH` [`00aeeed8`](#insn-00aeeed8) → [`00aeeedc`](#insn-00aeeedc)
- ブロック [`00aeeedc`](#insn-00aeeedc) 範囲 `[['00aeeedc', '00aeeeeb']]`
  - `CONDITIONAL_JUMP` [`00aeeee8`](#insn-00aeeee8) → [`00aeef0c`](#insn-00aeef0c)
  - `FALL_THROUGH` [`00aeeee8`](#insn-00aeeee8) → [`00aeeeec`](#insn-00aeeeec)
- ブロック [`00aeeeec`](#insn-00aeeeec) 範囲 `[['00aeeeec', '00aeef0b']]`
- ブロック [`00aeef0c`](#insn-00aeef0c) 範囲 `[['00aeef0c', '00aeef0f']]`

## 命令位置別の参照

- [`00aeec90`](#insn-00aeec90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec94`](#insn-00aeec94) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec98`](#insn-00aeec98) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec9c`](#insn-00aeec9c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeca0`](#insn-00aeeca0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeca4`](#insn-00aeeca4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecb4`](#insn-00aeecb4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecc8`](#insn-00aeecc8) → [`008b92e8`](../008b9/008b92e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92e8` · 推定シンボル `None` · 推定型 `None`
- [`00aeeccc`](#insn-00aeeccc) → [`00aeeedc`](#insn-00aeeedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecd4`](#insn-00aeecd4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecd8`](#insn-00aeecd8) → [`0046db2c`](../0046d/0046db2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046db2c` · 推定シンボル `None` · 推定型 `None`
- [`00aeece0`](#insn-00aeece0) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeece4`](#insn-00aeece4) → [`00aeed08`](#insn-00aeed08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeecec`](#insn-00aeecec) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aeecf4`](#insn-00aeecf4) → `00c8da20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aeecfc`](#insn-00aeecfc) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`00aeed04`](#insn-00aeed04) → [`00aeed0c`](#insn-00aeed0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed1c`](#insn-00aeed1c) → [`00aeedf4`](#insn-00aeedf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed34`](#insn-00aeed34) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`00aeed38`](#insn-00aeed38) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed40`](#insn-00aeed40) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed9c`](#insn-00aeed9c) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`00aeedb4`](#insn-00aeedb4) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`00aeedc0`](#insn-00aeedc0) → [`008b7a20`](../008b7/008b7a20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7a20` · 推定シンボル `None` · 推定型 `None`
- [`00aeedcc`](#insn-00aeedcc) → [`008b6df4`](../008b6/008b6df4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6df4` · 推定シンボル `None` · 推定型 `None`
- [`00aeedd8`](#insn-00aeedd8) → [`008b7a20`](../008b7/008b7a20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7a20` · 推定シンボル `None` · 推定型 `None`
- [`00aeede4`](#insn-00aeede4) → [`008b6df4`](../008b6/008b6df4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6df4` · 推定シンボル `None` · 推定型 `None`
- [`00aeedf0`](#insn-00aeedf0) → [`00aeeed8`](#insn-00aeeed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee00`](#insn-00aeee00) → [`008b9864`](../008b9/008b9864.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9864` · 推定シンボル `None` · 推定型 `None`
- [`00aeee10`](#insn-00aeee10) → [`008b9344`](../008b9/008b9344.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9344` · 推定シンボル `None` · 推定型 `None`
- [`00aeee18`](#insn-00aeee18) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee24`](#insn-00aeee24) → [`00489f8c`](../00489/00489f8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f8c` · 推定シンボル `None` · 推定型 `None`
- [`00aeee2c`](#insn-00aeee2c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aeee30`](#insn-00aeee30) → [`00aeeeb0`](#insn-00aeeeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee34`](#insn-00aeee34) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aeee3c`](#insn-00aeee3c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aeee4c`](#insn-00aeee4c) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00aeeea8`](#insn-00aeeea8) → [`00aeed20`](#insn-00aeed20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeeac`](#insn-00aeeeac) → [`00aeed38`](#insn-00aeed38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeeb8`](#insn-00aeeeb8) → `00333b9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aeeec0`](#insn-00aeeec0) → [`00aeed38`](#insn-00aeed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeec4`](#insn-00aeeec4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aeeed0`](#insn-00aeeed0) → [`00aeed38`](#insn-00aeed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeed4`](#insn-00aeeed4) → [`00aeed20`](#insn-00aeed20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeed8`](#insn-00aeeed8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeee0`](#insn-00aeeee0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeee8`](#insn-00aeeee8) → [`00aeef0c`](#insn-00aeef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeeec`](#insn-00aeeeec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeef0`](#insn-00aeeef0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeef4`](#insn-00aeeef4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeef8`](#insn-00aeeef8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeefc`](#insn-00aeeefc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef00`](#insn-00aeef00) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeef0c`](#insn-00aeef0c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeec90`](#insn-00aeec90)

~~~json
{
  "source": "00aeec90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec94`](#insn-00aeec94)

~~~json
{
  "source": "00aeec94",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec98`](#insn-00aeec98)

~~~json
{
  "source": "00aeec98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec9c`](#insn-00aeec9c)

~~~json
{
  "source": "00aeec9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeca0`](#insn-00aeeca0)

~~~json
{
  "source": "00aeeca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeca4`](#insn-00aeeca4)

~~~json
{
  "source": "00aeeca4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecb4`](#insn-00aeecb4)

~~~json
{
  "source": "00aeecb4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecc8`](#insn-00aeecc8)

~~~json
{
  "source": "00aeecc8",
  "target": "008b92e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeccc`](#insn-00aeeccc)

~~~json
{
  "source": "00aeeccc",
  "target": "00aeeedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecd4`](#insn-00aeecd4)

~~~json
{
  "source": "00aeecd4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecd8`](#insn-00aeecd8)

~~~json
{
  "source": "00aeecd8",
  "target": "0046db2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeece0`](#insn-00aeece0)

~~~json
{
  "source": "00aeece0",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeece4`](#insn-00aeece4)

~~~json
{
  "source": "00aeece4",
  "target": "00aeed08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeecec`](#insn-00aeecec)

~~~json
{
  "source": "00aeecec",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeecf4`](#insn-00aeecf4)

~~~json
{
  "source": "00aeecf4",
  "target": "00c8da20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8da20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeecfc`](#insn-00aeecfc)

~~~json
{
  "source": "00aeecfc",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed04`](#insn-00aeed04)

~~~json
{
  "source": "00aeed04",
  "target": "00aeed0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed1c`](#insn-00aeed1c)

~~~json
{
  "source": "00aeed1c",
  "target": "00aeedf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed34`](#insn-00aeed34)

~~~json
{
  "source": "00aeed34",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed38`](#insn-00aeed38)

~~~json
{
  "source": "00aeed38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed40`](#insn-00aeed40)

~~~json
{
  "source": "00aeed40",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed9c`](#insn-00aeed9c)

~~~json
{
  "source": "00aeed9c",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedb4`](#insn-00aeedb4)

~~~json
{
  "source": "00aeedb4",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedc0`](#insn-00aeedc0)

~~~json
{
  "source": "00aeedc0",
  "target": "008b7a20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedcc`](#insn-00aeedcc)

~~~json
{
  "source": "00aeedcc",
  "target": "008b6df4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedd8`](#insn-00aeedd8)

~~~json
{
  "source": "00aeedd8",
  "target": "008b7a20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeede4`](#insn-00aeede4)

~~~json
{
  "source": "00aeede4",
  "target": "008b6df4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedf0`](#insn-00aeedf0)

~~~json
{
  "source": "00aeedf0",
  "target": "00aeeed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee00`](#insn-00aeee00)

~~~json
{
  "source": "00aeee00",
  "target": "008b9864",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee10`](#insn-00aeee10)

~~~json
{
  "source": "00aeee10",
  "target": "008b9344",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee18`](#insn-00aeee18)

~~~json
{
  "source": "00aeee18",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee24`](#insn-00aeee24)

~~~json
{
  "source": "00aeee24",
  "target": "00489f8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee2c`](#insn-00aeee2c)

~~~json
{
  "source": "00aeee2c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee30`](#insn-00aeee30)

~~~json
{
  "source": "00aeee30",
  "target": "00aeeeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee34`](#insn-00aeee34)

~~~json
{
  "source": "00aeee34",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee3c`](#insn-00aeee3c)

~~~json
{
  "source": "00aeee3c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee4c`](#insn-00aeee4c)

~~~json
{
  "source": "00aeee4c",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b979",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0039b979",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeeea8`](#insn-00aeeea8)

~~~json
{
  "source": "00aeeea8",
  "target": "00aeed20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeeac`](#insn-00aeeeac)

~~~json
{
  "source": "00aeeeac",
  "target": "00aeed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeeb8`](#insn-00aeeeb8)

~~~json
{
  "source": "00aeeeb8",
  "target": "00333b9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333b98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44cf6a001c7d0900",
  "capture_start": "00333b98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeeec0`](#insn-00aeeec0)

~~~json
{
  "source": "00aeeec0",
  "target": "00aeed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeec4`](#insn-00aeeec4)

~~~json
{
  "source": "00aeeec4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeed0`](#insn-00aeeed0)

~~~json
{
  "source": "00aeeed0",
  "target": "00aeed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeed4`](#insn-00aeeed4)

~~~json
{
  "source": "00aeeed4",
  "target": "00aeed20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeed8`](#insn-00aeeed8)

~~~json
{
  "source": "00aeeed8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeee0`](#insn-00aeeee0)

~~~json
{
  "source": "00aeeee0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeee8`](#insn-00aeeee8)

~~~json
{
  "source": "00aeeee8",
  "target": "00aeef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeeec`](#insn-00aeeeec)

~~~json
{
  "source": "00aeeeec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeef0`](#insn-00aeeef0)

~~~json
{
  "source": "00aeeef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeef4`](#insn-00aeeef4)

~~~json
{
  "source": "00aeeef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeef8`](#insn-00aeeef8)

~~~json
{
  "source": "00aeeef8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeefc`](#insn-00aeeefc)

~~~json
{
  "source": "00aeeefc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef00`](#insn-00aeef00)

~~~json
{
  "source": "00aeef00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeef0c`](#insn-00aeef0c)

~~~json
{
  "source": "00aeef0c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
