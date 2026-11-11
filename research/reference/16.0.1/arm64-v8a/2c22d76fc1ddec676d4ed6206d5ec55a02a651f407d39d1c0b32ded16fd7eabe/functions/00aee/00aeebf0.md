# 00aeebf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
  "source_text_sha256": "13551587354da5087eececb7f3c59fa513cb76ad35965dcc2bbfd7f567b316aa"
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
