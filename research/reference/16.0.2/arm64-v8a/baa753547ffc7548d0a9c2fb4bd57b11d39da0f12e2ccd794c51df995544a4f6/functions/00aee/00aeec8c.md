# 00aeec8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "613129abf52f2c22bbb7df435e1459ed63668ac0aa48c3b1ca69c0eb7620cbf3"
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
