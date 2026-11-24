# 00aeebf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aee7c8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-0c924bc9336dcf930202867b45be920c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeec8c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeec8c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-92cd9dbe66e9d6cacc9360724dd5a971)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeebf0",
  "name": "FUN_00aeebf0",
  "size": 644,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13551587354da5087eececb7f3c59fa513cb76ad35965dcc2bbfd7f567b316aa",
  "source_text_sha256": "13551587354da5087eececb7f3c59fa513cb76ad35965dcc2bbfd7f567b316aa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeebf0",
        "00aeee73"
      ]
    ],
    "bytes_sha256": "677a9855ae163875d3208916c924ca09de9f1ee0ee0cc53ecf7a4516835183c9",
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

- [00467b60](../00467/00467b60.md)
- [00469c04](../00469/00469c04.md)
- [0046daec](../0046d/0046daec.md)
- [00489f4c](../00489/00489f4c.md)
- [008514f8](../00851/008514f8.md)
- [008b6d9c](../008b6/008b6d9c.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9290](../008b9/008b9290.md)
- [008b92ec](../008b9/008b92ec.md)
- [008b980c](../008b9/008b980c.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4472 bytes

~~~c

void FUN_00aeebf0(long param_1,undefined8 *param_2,undefined8 *param_3)

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
  
  lVar8 = tpidr_el0;
  local_68 = *(long *)(lVar8 + 0x28);
  uVar17 = *param_2;
  uVar18 = *param_3;
  lVar20 = *(long *)(param_1 + 8);
  iVar10 = FUN_008b9290(uVar17);
  if (iVar10 != 0) {
    FUN_0046daec(local_78);
    if (DAT_00ca4978 == 0) {
      lVar11 = 0;
    }
    else {
                    /* try { // try from 00aeec54 to 00beec57 has its CatchHandler @ 00aeec70 */
                    /* catch() { ... } // from try @ 00aeeab0 with catch @ 00aeec58
                       try { // try from 00aeec58 to 00beecaf has its CatchHandler @ 00aee970 */
      lVar11 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                              &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
                    /* catch() { ... } // from try @ 00aee9d0 with catch @ 00aeec68 */
    }
                    /* catch() { ... } // from try @ 00aeea14 with catch @ 00aeec70
                       catch() { ... } // from try @ 00aeec54 with catch @ 00aeec70 */
    uVar19 = 0;
    bVar9 = true;
    do {
      bVar16 = bVar9;
      iVar10 = FUN_008b980c(uVar17,uVar19);
      auVar21 = FUN_008b92ec(uVar17,uVar19);
      local_78 = auVar21;
      lVar13 = FUN_00489f4c(*(undefined8 *)(lVar11 + 0x118),uVar19 | 0x2a);
      lVar14 = FUN_008514f8();
      if (bVar16) {
        lVar14 = FUN_008514f8();
        lVar15 = FUN_008514f8();
        lVar14 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + lVar15) * 0x2c;
        auVar21 = local_78;
        if ((int)((uint)(*(byte *)(lVar14 + 0xc5e2) ^ *(byte *)(lVar14 + 0xc5ba)) << 0x10 |
                  (uint)(*(byte *)(lVar14 + 0xc5e3) ^ *(byte *)(lVar14 + 0xc5bb)) << 0x18 |
                  (uint)(*(byte *)(lVar14 + 0xc5e1) ^ *(byte *)(lVar14 + 0xc5b9)) << 8 |
                 (uint)(*(byte *)(lVar14 + 0xc5e0) ^ *(byte *)(lVar14 + 0xc5b8))) < 2) {
LAB_00aeec84:
          FUN_00467b60(uVar18,0x7f,0x7f,0x7f,0xff);
          auVar21 = local_78;
        }
      }
      else {
        auVar21 = local_78;
        if (*(int *)((long)&fde_table_entry_00333b98.data_loc + lVar14) < 2) {
                    /* try { // try from 00aeee28 to 00beeeff has its CatchHandler @ 00aeee28
                       catch() { ... } // from try @ 00aeee28 with catch @ 00aeee28
                       catch() { ... } // from try @ 00aeef08 with catch @ 00aeee28 */
          lVar14 = FUN_008514f8();
          auVar21 = local_78;
          if ((*(byte *)(lVar14 + 0x33a5) & 1) == 0) goto LAB_00aeec84;
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
      FUN_00469c04(uVar18,*(undefined8 *)(lVar11 + 0x118),(iVar6 + iVar10) - (iVar4 >> 1),
                   (iVar7 + iVar1) - (iVar5 >> 1),iVar2,iVar3,uVar19 | 0x2a);
      FUN_00467b60(uVar18,0xff,0xff,0xff,0xff);
      uVar12 = FUN_008b79c8(lVar20 + 0x2f38,0x321);
      FUN_008b6d9c(uVar12,0,0);
      uVar12 = FUN_008b79c8(lVar20 + 0x2f38,800);
      FUN_008b6d9c(uVar12,0,0);
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
<a id="insn-00aeebf0"></a> `00aeebf0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00aeebf4"></a> `00aeebf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeebf8"></a> `00aeebf8` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeebfc"></a> `00aeebfc` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeec00"></a> `00aeec00` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeec04"></a> `00aeec04` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeec08"></a> `00aeec08` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeec0c"></a> `00aeec0c` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeec10"></a> `00aeec10` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeec14"></a> `00aeec14` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeec18"></a> `00aeec18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeec1c"></a> `00aeec1c` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aeec20"></a> `00aeec20` | `54 00 40 f9` | ldr x20,[x2] | `FALL_THROUGH`
<a id="insn-00aeec24"></a> `00aeec24` | `1b 04 40 f9` | ldr x27,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeec28"></a> `00aeec28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeec2c"></a> `00aeec2c` | `99 29 f7 97` | bl 0x008b9290 | `UNCONDITIONAL_CALL`
<a id="insn-00aeec30"></a> `00aeec30` | `80 10 00 34` | cbz w0,0x00aeee40 | `CONDITIONAL_JUMP`
<a id="insn-00aeec34"></a> `00aeec34` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aeec38"></a> `00aeec38` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00aeec3c"></a> `00aeec3c` | `ac fb e5 97` | bl 0x0046daec | `UNCONDITIONAL_CALL`
<a id="insn-00aeec40"></a> `00aeec40` | `a8 0d 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aeec44"></a> `00aeec44` | `00 bd 44 f9` | ldr x0,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-00aeec48"></a> `00aeec48` | `20 01 00 b4` | cbz x0,0x00aeec6c | `CONDITIONAL_JUMP`
<a id="insn-00aeec4c"></a> `00aeec4c` | `a1 0b 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aeec50"></a> `00aeec50` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-00aeec54"></a> `00aeec54` | `e2 0c 00 f0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aeec58"></a> `00aeec58` | `42 40 25 91` | add x2,x2,#0x950 | `FALL_THROUGH`
<a id="insn-00aeec5c"></a> `00aeec5c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aeec60"></a> `00aeec60` | `6c a6 05 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-00aeec64"></a> `00aeec64` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aeec68"></a> `00aeec68` | `02 00 00 14` | b 0x00aeec70 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeec6c"></a> `00aeec6c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aeec70"></a> `00aeec70` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00aeec74"></a> `00aeec74` | `19 e7 85 52` | mov w25,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aeec78"></a> `00aeec78` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeec7c"></a> `00aeec7c` | `5a 05 80 52` | mov w26,#0x2a | `FALL_THROUGH`
<a id="insn-00aeec80"></a> `00aeec80` | `36 00 00 14` | b 0x00aeed58 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeec84"></a> `00aeec84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeec88"></a> `00aeec88` | `e1 0f 80 52` | mov w1,#0x7f | `FALL_THROUGH`
<a id="insn-00aeec8c"></a> `00aeec8c` | `e2 0f 80 52` | mov w2,#0x7f | `FALL_THROUGH`
<a id="insn-00aeec90"></a> `00aeec90` | `e3 0f 80 52` | mov w3,#0x7f | `FALL_THROUGH`
<a id="insn-00aeec94"></a> `00aeec94` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aeec98"></a> `00aeec98` | `b2 e3 e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aeec9c"></a> `00aeec9c` | `e8 2b 42 29` | ldp w8,w10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeca0"></a> `00aeeca0` | `09 2f 41 29` | ldp w9,w11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeca4"></a> `00aeeca4` | `ee 3f 41 29` | ldp w14,w15,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeca8"></a> `00aeeca8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aeecac"></a> `00aeecac` | `a1 8e 40 f9` | ldr x1,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aeecb0"></a> `00aeecb0` | `c6 02 1a 2a` | orr w6,w22,w26 | `FALL_THROUGH`
<a id="insn-00aeecb4"></a> `00aeecb4` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-00aeecb8"></a> `00aeecb8` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00aeecbc"></a> `00aeecbc` | `24 01 17 0b` | add w4,w9,w23 | `FALL_THROUGH`
<a id="insn-00aeecc0"></a> `00aeecc0` | `2c a5 89 1a` | cinc w12,w9,lt | `FALL_THROUGH`
<a id="insn-00aeecc4"></a> `00aeecc4` | `ff 02 00 71` | cmp w23,#0x0 | `FALL_THROUGH`
<a id="insn-00aeecc8"></a> `00aeecc8` | `65 01 17 0b` | add w5,w11,w23 | `FALL_THROUGH`
<a id="insn-00aeeccc"></a> `00aeeccc` | `ed a6 97 1a` | cinc w13,w23,lt | `FALL_THROUGH`
<a id="insn-00aeecd0"></a> `00aeecd0` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00aeecd4"></a> `00aeecd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeecd8"></a> `00aeecd8` | `ad 7d 01 13` | asr w13,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00aeecdc"></a> `00aeecdc` | `4a a5 8a 1a` | cinc w10,w10,lt | `FALL_THROUGH`
<a id="insn-00aeece0"></a> `00aeece0` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-00aeece4"></a> `00aeece4` | `ce 01 0d 4b` | sub w14,w14,w13 | `FALL_THROUGH`
<a id="insn-00aeece8"></a> `00aeece8` | `ed 01 0d 4b` | sub w13,w15,w13 | `FALL_THROUGH`
<a id="insn-00aeecec"></a> `00aeecec` | `c8 05 88 0b` | add w8,w14,w8, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeecf0"></a> `00aeecf0` | `aa 05 8a 0b` | add w10,w13,w10, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeecf4"></a> `00aeecf4` | `6d a5 8b 1a` | cinc w13,w11,lt | `FALL_THROUGH`
<a id="insn-00aeecf8"></a> `00aeecf8` | `02 05 8c 4b` | sub w2,w8,w12, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeecfc"></a> `00aeecfc` | `43 05 8d 4b` | sub w3,w10,w13, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00aeed00"></a> `00aeed00` | `c1 eb e5 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed04"></a> `00aeed04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aeed08"></a> `00aeed08` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aeed0c"></a> `00aeed0c` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aeed10"></a> `00aeed10` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aeed14"></a> `00aeed14` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aeed18"></a> `00aeed18` | `92 e3 e5 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed1c"></a> `00aeed1c` | `60 03 19 8b` | add x0,x27,x25 | `FALL_THROUGH`
<a id="insn-00aeed20"></a> `00aeed20` | `21 64 80 52` | mov w1,#0x321 | `FALL_THROUGH`
<a id="insn-00aeed24"></a> `00aeed24` | `29 23 f7 97` | bl 0x008b79c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed28"></a> `00aeed28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeed2c"></a> `00aeed2c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeed30"></a> `00aeed30` | `1b 20 f7 97` | bl 0x008b6d9c | `UNCONDITIONAL_CALL`
<a id="insn-00aeed34"></a> `00aeed34` | `60 03 19 8b` | add x0,x27,x25 | `FALL_THROUGH`
<a id="insn-00aeed38"></a> `00aeed38` | `01 64 80 52` | mov w1,#0x320 | `FALL_THROUGH`
<a id="insn-00aeed3c"></a> `00aeed3c` | `23 23 f7 97` | bl 0x008b79c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed40"></a> `00aeed40` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aeed44"></a> `00aeed44` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aeed48"></a> `00aeed48` | `15 20 f7 97` | bl 0x008b6d9c | `UNCONDITIONAL_CALL`
<a id="insn-00aeed4c"></a> `00aeed4c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00aeed50"></a> `00aeed50` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00aeed54"></a> `00aeed54` | `5c 07 00 36` | tbz w28,#0x0,0x00aeee3c | `CONDITIONAL_JUMP`
<a id="insn-00aeed58"></a> `00aeed58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeed5c"></a> `00aeed5c` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aeed60"></a> `00aeed60` | `fc 03 08 2a` | mov w28,w8 | `FALL_THROUGH`
<a id="insn-00aeed64"></a> `00aeed64` | `aa 2a f7 97` | bl 0x008b980c | `UNCONDITIONAL_CALL`
<a id="insn-00aeed68"></a> `00aeed68` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aeed6c"></a> `00aeed6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeed70"></a> `00aeed70` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aeed74"></a> `00aeed74` | `5e 29 f7 97` | bl 0x008b92ec | `UNCONDITIONAL_CALL`
<a id="insn-00aeed78"></a> `00aeed78` | `a8 8e 40 f9` | ldr x8,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-00aeed7c"></a> `00aeed7c` | `e0 87 00 a9` | stp x0,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeed80"></a> `00aeed80` | `c1 02 1a 2a` | orr w1,w22,w26 | `FALL_THROUGH`
<a id="insn-00aeed84"></a> `00aeed84` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aeed88"></a> `00aeed88` | `71 6c e6 97` | bl 0x00489f4c | `UNCONDITIONAL_CALL`
<a id="insn-00aeed8c"></a> `00aeed8c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00aeed90"></a> `00aeed90` | `da 89 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed94"></a> `00aeed94` | `1c 04 00 36` | tbz w28,#0x0,0x00aeee14 | `CONDITIONAL_JUMP`
<a id="insn-00aeed98"></a> `00aeed98` | `d8 89 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeed9c"></a> `00aeed9c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00aeeda0"></a> `00aeeda0` | `d6 89 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeda4"></a> `00aeeda4` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aeeda8"></a> `00aeeda8` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00aeedac"></a> `00aeedac` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeedb0"></a> `00aeedb0` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeedb4"></a> `00aeedb4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aeedb8"></a> `00aeedb8` | `08 65 29 9b` | smaddl x8,w8,w9,x25 | `FALL_THROUGH`
<a id="insn-00aeedbc"></a> `00aeedbc` | `09 b7 98 52` | mov w9,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00aeedc0"></a> `00aeedc0` | `19 e7 85 52` | mov w25,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aeedc4"></a> `00aeedc4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aeedc8"></a> `00aeedc8` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aeedcc"></a> `00aeedcc` | `0a a9 40 39` | ldrb w10,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aeedd0"></a> `00aeedd0` | `0b ad 40 39` | ldrb w11,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aeedd4"></a> `00aeedd4` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aeedd8"></a> `00aeedd8` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aeeddc"></a> `00aeeddc` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aeede0"></a> `00aeede0` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00aeede4"></a> `00aeede4` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aeede8"></a> `00aeede8` | `0b a5 40 39` | ldrb w11,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aeedec"></a> `00aeedec` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aeedf0"></a> `00aeedf0` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00aeedf4"></a> `00aeedf4` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aeedf8"></a> `00aeedf8` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aeedfc"></a> `00aeedfc` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aeee00"></a> `00aeee00` | `08 01 0a 4a` | eor w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00aeee04"></a> `00aeee04` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aeee08"></a> `00aeee08` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeee0c"></a> `00aeee0c` | `cd f3 ff 54` | b.le 0x00aeec84 | `CONDITIONAL_JUMP`
<a id="insn-00aeee10"></a> `00aeee10` | `a3 ff ff 17` | b 0x00aeec9c | `UNCONDITIONAL_JUMP`
<a id="insn-00aeee14"></a> `00aeee14` | `88 73 87 52` | mov w8,#0x3b9c | `FALL_THROUGH`
<a id="insn-00aeee18"></a> `00aeee18` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeee1c"></a> `00aeee1c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aeee20"></a> `00aeee20` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aeee24"></a> `00aeee24` | `cc f3 ff 54` | b.gt 0x00aeec9c | `CONDITIONAL_JUMP`
<a id="insn-00aeee28"></a> `00aeee28` | `b4 89 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeee2c"></a> `00aeee2c` | `a8 74 86 52` | mov w8,#0x33a5 | `FALL_THROUGH`
<a id="insn-00aeee30"></a> `00aeee30` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00aeee34"></a> `00aeee34` | `48 f3 07 37` | tbnz w8,#0x0,0x00aeec9c | `CONDITIONAL_JUMP`
<a id="insn-00aeee38"></a> `00aeee38` | `93 ff ff 17` | b 0x00aeec84 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeee3c"></a> `00aeee3c` | `f5 03 40 f9` | ldr x21,[sp] | `FALL_THROUGH`
<a id="insn-00aeee40"></a> `00aeee40` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aeee44"></a> `00aeee44` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeee48"></a> `00aeee48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeee4c"></a> `00aeee4c` | `21 01 00 54` | b.ne 0x00aeee70 | `CONDITIONAL_JUMP`
<a id="insn-00aeee50"></a> `00aeee50` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeee54"></a> `00aeee54` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeee58"></a> `00aeee58` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeee5c"></a> `00aeee5c` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeee60"></a> `00aeee60` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeee64"></a> `00aeee64` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeee68"></a> `00aeee68` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00aeee6c"></a> `00aeee6c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeee70"></a> `00aeee70` | `1c a4 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeebf0`](#insn-00aeebf0) 範囲 `[['00aeebf0', '00aeec33']]`
  - `CONDITIONAL_JUMP` [`00aeec30`](#insn-00aeec30) → [`00aeee40`](#insn-00aeee40)
  - `FALL_THROUGH` [`00aeec30`](#insn-00aeec30) → [`00aeec34`](#insn-00aeec34)
- ブロック [`00aeec34`](#insn-00aeec34) 範囲 `[['00aeec34', '00aeec4b']]`
  - `CONDITIONAL_JUMP` [`00aeec48`](#insn-00aeec48) → [`00aeec6c`](#insn-00aeec6c)
  - `FALL_THROUGH` [`00aeec48`](#insn-00aeec48) → [`00aeec4c`](#insn-00aeec4c)
- ブロック [`00aeec4c`](#insn-00aeec4c) 範囲 `[['00aeec4c', '00aeec53']]`
  - `FALL_THROUGH` [`00aeec50`](#insn-00aeec50) → [`00aeec54`](#insn-00aeec54)
- ブロック [`00aeec54`](#insn-00aeec54) 範囲 `[['00aeec54', '00aeec57']]`
  - `FALL_THROUGH` [`00aeec54`](#insn-00aeec54) → [`00aeec58`](#insn-00aeec58)
- ブロック [`00aeec58`](#insn-00aeec58) 範囲 `[['00aeec58', '00aeec67']]`
  - `FALL_THROUGH` [`00aeec64`](#insn-00aeec64) → [`00aeec68`](#insn-00aeec68)
- ブロック [`00aeec68`](#insn-00aeec68) 範囲 `[['00aeec68', '00aeec6b']]`
  - `UNCONDITIONAL_JUMP` [`00aeec68`](#insn-00aeec68) → [`00aeec70`](#insn-00aeec70)
- ブロック [`00aeec6c`](#insn-00aeec6c) 範囲 `[['00aeec6c', '00aeec6f']]`
  - `FALL_THROUGH` [`00aeec6c`](#insn-00aeec6c) → [`00aeec70`](#insn-00aeec70)
- ブロック [`00aeec70`](#insn-00aeec70) 範囲 `[['00aeec70', '00aeec83']]`
  - `UNCONDITIONAL_JUMP` [`00aeec80`](#insn-00aeec80) → [`00aeed58`](#insn-00aeed58)
- ブロック [`00aeec84`](#insn-00aeec84) 範囲 `[['00aeec84', '00aeec9b']]`
  - `FALL_THROUGH` [`00aeec98`](#insn-00aeec98) → [`00aeec9c`](#insn-00aeec9c)
- ブロック [`00aeec9c`](#insn-00aeec9c) 範囲 `[['00aeec9c', '00aeed57']]`
  - `CONDITIONAL_JUMP` [`00aeed54`](#insn-00aeed54) → [`00aeee3c`](#insn-00aeee3c)
  - `FALL_THROUGH` [`00aeed54`](#insn-00aeed54) → [`00aeed58`](#insn-00aeed58)
- ブロック [`00aeed58`](#insn-00aeed58) 範囲 `[['00aeed58', '00aeed97']]`
  - `CONDITIONAL_JUMP` [`00aeed94`](#insn-00aeed94) → [`00aeee14`](#insn-00aeee14)
  - `FALL_THROUGH` [`00aeed94`](#insn-00aeed94) → [`00aeed98`](#insn-00aeed98)
- ブロック [`00aeed98`](#insn-00aeed98) 範囲 `[['00aeed98', '00aeee0f']]`
  - `CONDITIONAL_JUMP` [`00aeee0c`](#insn-00aeee0c) → [`00aeec84`](#insn-00aeec84)
  - `FALL_THROUGH` [`00aeee0c`](#insn-00aeee0c) → [`00aeee10`](#insn-00aeee10)
- ブロック [`00aeee10`](#insn-00aeee10) 範囲 `[['00aeee10', '00aeee13']]`
  - `UNCONDITIONAL_JUMP` [`00aeee10`](#insn-00aeee10) → [`00aeec9c`](#insn-00aeec9c)
- ブロック [`00aeee14`](#insn-00aeee14) 範囲 `[['00aeee14', '00aeee27']]`
  - `CONDITIONAL_JUMP` [`00aeee24`](#insn-00aeee24) → [`00aeec9c`](#insn-00aeec9c)
  - `FALL_THROUGH` [`00aeee24`](#insn-00aeee24) → [`00aeee28`](#insn-00aeee28)
- ブロック [`00aeee28`](#insn-00aeee28) 範囲 `[['00aeee28', '00aeee37']]`
  - `CONDITIONAL_JUMP` [`00aeee34`](#insn-00aeee34) → [`00aeec9c`](#insn-00aeec9c)
  - `FALL_THROUGH` [`00aeee34`](#insn-00aeee34) → [`00aeee38`](#insn-00aeee38)
- ブロック [`00aeee38`](#insn-00aeee38) 範囲 `[['00aeee38', '00aeee3b']]`
  - `UNCONDITIONAL_JUMP` [`00aeee38`](#insn-00aeee38) → [`00aeec84`](#insn-00aeec84)
- ブロック [`00aeee3c`](#insn-00aeee3c) 範囲 `[['00aeee3c', '00aeee3f']]`
  - `FALL_THROUGH` [`00aeee3c`](#insn-00aeee3c) → [`00aeee40`](#insn-00aeee40)
- ブロック [`00aeee40`](#insn-00aeee40) 範囲 `[['00aeee40', '00aeee4f']]`
  - `CONDITIONAL_JUMP` [`00aeee4c`](#insn-00aeee4c) → [`00aeee70`](#insn-00aeee70)
  - `FALL_THROUGH` [`00aeee4c`](#insn-00aeee4c) → [`00aeee50`](#insn-00aeee50)
- ブロック [`00aeee50`](#insn-00aeee50) 範囲 `[['00aeee50', '00aeee6f']]`
- ブロック [`00aeee70`](#insn-00aeee70) 範囲 `[['00aeee70', '00aeee73']]`

## 命令位置別の参照

- [`00aeebf4`](#insn-00aeebf4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebf8`](#insn-00aeebf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeebfc`](#insn-00aeebfc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec00`](#insn-00aeec00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec04`](#insn-00aeec04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec08`](#insn-00aeec08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec18`](#insn-00aeec18) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec2c`](#insn-00aeec2c) → [`008b9290`](../008b9/008b9290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9290` · 推定シンボル `None` · 推定型 `None`
- [`00aeec30`](#insn-00aeec30) → [`00aeee40`](#insn-00aeee40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec38`](#insn-00aeec38) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec3c`](#insn-00aeec3c) → [`0046daec`](../0046d/0046daec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046daec` · 推定シンボル `None` · 推定型 `None`
- [`00aeec44`](#insn-00aeec44) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeec48`](#insn-00aeec48) → [`00aeec6c`](#insn-00aeec6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec50`](#insn-00aeec50) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aeec58`](#insn-00aeec58) → `00c8d950`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aeec60`](#insn-00aeec60) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`00aeec68`](#insn-00aeec68) → [`00aeec70`](#insn-00aeec70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec80`](#insn-00aeec80) → [`00aeed58`](#insn-00aeed58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeec98`](#insn-00aeec98) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aeec9c`](#insn-00aeec9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeca4`](#insn-00aeeca4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed00`](#insn-00aeed00) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`00aeed18`](#insn-00aeed18) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`00aeed24`](#insn-00aeed24) → [`008b79c8`](../008b7/008b79c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79c8` · 推定シンボル `None` · 推定型 `None`
- [`00aeed30`](#insn-00aeed30) → [`008b6d9c`](../008b6/008b6d9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6d9c` · 推定シンボル `None` · 推定型 `None`
- [`00aeed3c`](#insn-00aeed3c) → [`008b79c8`](../008b7/008b79c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b79c8` · 推定シンボル `None` · 推定型 `None`
- [`00aeed48`](#insn-00aeed48) → [`008b6d9c`](../008b6/008b6d9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6d9c` · 推定シンボル `None` · 推定型 `None`
- [`00aeed54`](#insn-00aeed54) → [`00aeee3c`](#insn-00aeee3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed64`](#insn-00aeed64) → [`008b980c`](../008b9/008b980c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b980c` · 推定シンボル `None` · 推定型 `None`
- [`00aeed74`](#insn-00aeed74) → [`008b92ec`](../008b9/008b92ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b92ec` · 推定シンボル `None` · 推定型 `None`
- [`00aeed7c`](#insn-00aeed7c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed88`](#insn-00aeed88) → [`00489f4c`](../00489/00489f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f4c` · 推定シンボル `None` · 推定型 `None`
- [`00aeed90`](#insn-00aeed90) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeed94`](#insn-00aeed94) → [`00aeee14`](#insn-00aeee14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeed98`](#insn-00aeed98) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeeda0`](#insn-00aeeda0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeedb0`](#insn-00aeedb0) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aeee0c`](#insn-00aeee0c) → [`00aeec84`](#insn-00aeec84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee10`](#insn-00aeee10) → [`00aeec9c`](#insn-00aeec9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee1c`](#insn-00aeee1c) → `00333b9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aeee24`](#insn-00aeee24) → [`00aeec9c`](#insn-00aeec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee28`](#insn-00aeee28) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aeee34`](#insn-00aeee34) → [`00aeec9c`](#insn-00aeec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee38`](#insn-00aeee38) → [`00aeec84`](#insn-00aeec84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee3c`](#insn-00aeee3c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee44`](#insn-00aeee44) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee4c`](#insn-00aeee4c) → [`00aeee70`](#insn-00aeee70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee50`](#insn-00aeee50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee54`](#insn-00aeee54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee58`](#insn-00aeee58) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee5c`](#insn-00aeee5c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee60`](#insn-00aeee60) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee64`](#insn-00aeee64) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeee70`](#insn-00aeee70) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeebf4`](#insn-00aeebf4)

~~~json
{
  "source": "00aeebf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebf8`](#insn-00aeebf8)

~~~json
{
  "source": "00aeebf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeebfc`](#insn-00aeebfc)

~~~json
{
  "source": "00aeebfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec00`](#insn-00aeec00)

~~~json
{
  "source": "00aeec00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec04`](#insn-00aeec04)

~~~json
{
  "source": "00aeec04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec08`](#insn-00aeec08)

~~~json
{
  "source": "00aeec08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec18`](#insn-00aeec18)

~~~json
{
  "source": "00aeec18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec2c`](#insn-00aeec2c)

~~~json
{
  "source": "00aeec2c",
  "target": "008b9290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeec30`](#insn-00aeec30)

~~~json
{
  "source": "00aeec30",
  "target": "00aeee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec38`](#insn-00aeec38)

~~~json
{
  "source": "00aeec38",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec3c`](#insn-00aeec3c)

~~~json
{
  "source": "00aeec3c",
  "target": "0046daec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeec44`](#insn-00aeec44)

~~~json
{
  "source": "00aeec44",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeec48`](#insn-00aeec48)

~~~json
{
  "source": "00aeec48",
  "target": "00aeec6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec50`](#insn-00aeec50)

~~~json
{
  "source": "00aeec50",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeec58`](#insn-00aeec58)

~~~json
{
  "source": "00aeec58",
  "target": "00c8d950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d950",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeec60`](#insn-00aeec60)

~~~json
{
  "source": "00aeec60",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeec68`](#insn-00aeec68)

~~~json
{
  "source": "00aeec68",
  "target": "00aeec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec80`](#insn-00aeec80)

~~~json
{
  "source": "00aeec80",
  "target": "00aeed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeec98`](#insn-00aeec98)

~~~json
{
  "source": "00aeec98",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeec9c`](#insn-00aeec9c)

~~~json
{
  "source": "00aeec9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeca4`](#insn-00aeeca4)

~~~json
{
  "source": "00aeeca4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed00`](#insn-00aeed00)

~~~json
{
  "source": "00aeed00",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed18`](#insn-00aeed18)

~~~json
{
  "source": "00aeed18",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed24`](#insn-00aeed24)

~~~json
{
  "source": "00aeed24",
  "target": "008b79c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed30`](#insn-00aeed30)

~~~json
{
  "source": "00aeed30",
  "target": "008b6d9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed3c`](#insn-00aeed3c)

~~~json
{
  "source": "00aeed3c",
  "target": "008b79c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed48`](#insn-00aeed48)

~~~json
{
  "source": "00aeed48",
  "target": "008b6d9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed54`](#insn-00aeed54)

~~~json
{
  "source": "00aeed54",
  "target": "00aeee3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed64`](#insn-00aeed64)

~~~json
{
  "source": "00aeed64",
  "target": "008b980c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed74`](#insn-00aeed74)

~~~json
{
  "source": "00aeed74",
  "target": "008b92ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed7c`](#insn-00aeed7c)

~~~json
{
  "source": "00aeed7c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed88`](#insn-00aeed88)

~~~json
{
  "source": "00aeed88",
  "target": "00489f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed90`](#insn-00aeed90)

~~~json
{
  "source": "00aeed90",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeed94`](#insn-00aeed94)

~~~json
{
  "source": "00aeed94",
  "target": "00aeee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeed98`](#insn-00aeed98)

~~~json
{
  "source": "00aeed98",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeda0`](#insn-00aeeda0)

~~~json
{
  "source": "00aeeda0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeedb0`](#insn-00aeedb0)

~~~json
{
  "source": "00aeedb0",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "cc820500",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeee0c`](#insn-00aeee0c)

~~~json
{
  "source": "00aeee0c",
  "target": "00aeec84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee10`](#insn-00aeee10)

~~~json
{
  "source": "00aeee10",
  "target": "00aeec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee1c`](#insn-00aeee1c)

~~~json
{
  "source": "00aeee1c",
  "target": "00333b9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333b98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ecd26a00dc7d0900",
  "capture_start": "00333b98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeee24`](#insn-00aeee24)

~~~json
{
  "source": "00aeee24",
  "target": "00aeec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee28`](#insn-00aeee28)

~~~json
{
  "source": "00aeee28",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeee34`](#insn-00aeee34)

~~~json
{
  "source": "00aeee34",
  "target": "00aeec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee38`](#insn-00aeee38)

~~~json
{
  "source": "00aeee38",
  "target": "00aeec84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee3c`](#insn-00aeee3c)

~~~json
{
  "source": "00aeee3c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee44`](#insn-00aeee44)

~~~json
{
  "source": "00aeee44",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee4c`](#insn-00aeee4c)

~~~json
{
  "source": "00aeee4c",
  "target": "00aeee70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee50`](#insn-00aeee50)

~~~json
{
  "source": "00aeee50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee54`](#insn-00aeee54)

~~~json
{
  "source": "00aeee54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee58`](#insn-00aeee58)

~~~json
{
  "source": "00aeee58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee5c`](#insn-00aeee5c)

~~~json
{
  "source": "00aeee5c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee60`](#insn-00aeee60)

~~~json
{
  "source": "00aeee60",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee64`](#insn-00aeee64)

~~~json
{
  "source": "00aeee64",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeee70`](#insn-00aeee70)

~~~json
{
  "source": "00aeee70",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
