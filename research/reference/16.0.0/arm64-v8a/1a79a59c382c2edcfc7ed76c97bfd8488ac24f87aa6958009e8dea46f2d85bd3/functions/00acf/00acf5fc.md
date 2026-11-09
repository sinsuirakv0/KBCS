# 00acf5fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acf5fc",
  "name": "FUN_00acf5fc",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03a834c3b54ee483a7aa85f8b202ce4f7b462a4d33b0deffa3051b14012cd924",
  "source_text_sha256": "03a834c3b54ee483a7aa85f8b202ce4f7b462a4d33b0deffa3051b14012cd924"
}
~~~

## 呼び出し元

- [00acc3d4](../00acc/00acc3d4.md)
- [00ae0814](../00ae0/00ae0814.md)
- [00aec538](../00aec/00aec538.md)
- [00aeec98](../00aee/00aeec98.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [0047e89c](../0047e/0047e89c.md)
- [008514b8](../00851/008514b8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 5572 bytes

~~~c

void FUN_00acf5fc(long param_1)

{
  byte bVar1;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  long *plVar10;
  byte *pbVar11;
  long *plVar12;
  byte *pbVar13;
  undefined8 local_70;
  long *plStack_68;
  long local_58;
  
                    /* catch() { ... } // from try @ 00acd88c with catch @ 00acf5fc */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00acea68 with catch @ 00acf7d0 */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
                    /* catch() { ... } // from try @ 00acce14 with catch @ 00acf7e4 */
                    /* catch() { ... } // from try @ 00accde0 with catch @ 00acf7ec */
                    /* catch() { ... } // from try @ 00acce20 with catch @ 00acf7f4 */
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  lVar5 = FUN_008514b8();
  lVar6 = FUN_008514b8();
  lVar7 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00acd5cc with catch @ 00acf64c */
                    /* catch() { ... } // from try @ 00acd848 with catch @ 00acf650 */
                    /* catch() { ... } // from try @ 00acd5b8 with catch @ 00acf660 */
  bVar1 = BYTE_ARRAY_004347ed[lVar6 + (long)*(int *)((long)&DWORD_0039b97c + lVar7) * 3 + 0xb];
                    /* catch() { ... } // from try @ 00acd83c with catch @ 00acf670 */
  pbVar9 = *(byte **)(BYTE_ARRAY_0043616d + lVar5 + 0x33);
  if (*(byte **)(BYTE_ARRAY_0043616d + lVar5 + 0x33) == (byte *)0x0) {
    pbVar11 = BYTE_ARRAY_0043616d + lVar5 + 0x33;
    pbVar13 = BYTE_ARRAY_0043616d + lVar5 + 0x33;
  }
  else {
    do {
      while( true ) {
        pbVar8 = pbVar9;
        pbVar11 = pbVar8;
        if ((int)(char)bVar1 < *(int *)(pbVar8 + 0x20)) break;
        if ((int)(char)bVar1 <= *(int *)(pbVar8 + 0x20)) goto LAB_00acf700;
                    /* catch() { ... } // from try @ 00acd558 with catch @ 00acf6a4 */
        pbVar9 = *(byte **)(pbVar8 + 8);
        if (*(byte **)(pbVar8 + 8) == (byte *)0x0) {
                    /* catch() { ... } // from try @ 00acd544 with catch @ 00acf6a8 */
          pbVar13 = pbVar8 + 8;
          goto LAB_00acf6ac;
        }
      }
                    /* catch() { ... } // from try @ 00acd564 with catch @ 00acf684 */
      pbVar9 = *(byte **)pbVar8;
      pbVar13 = pbVar8;
    } while (*(byte **)pbVar8 != (byte *)0x0);
  }
LAB_00acf6ac:
  pbVar8 = (byte *)_Znwm(0x40);
                    /* catch() { ... } // from try @ 00acd454 with catch @ 00acf6b8 */
  pbVar8[0x30] = 0;
  pbVar8[0x31] = 0;
  pbVar8[0x32] = 0;
  pbVar8[0x33] = 0;
  pbVar8[0x34] = 0;
  pbVar8[0x35] = 0;
  pbVar8[0x36] = 0;
  pbVar8[0x37] = 0;
  pbVar8[0x38] = 0;
  pbVar8[0x39] = 0;
  pbVar8[0x3a] = 0;
  pbVar8[0x3b] = 0;
  pbVar8[0x3c] = 0;
  pbVar8[0x3d] = 0;
  pbVar8[0x3e] = 0;
  pbVar8[0x3f] = 0;
  pbVar8[0x28] = 0;
  pbVar8[0x29] = 0;
  pbVar8[0x2a] = 0;
  pbVar8[0x2b] = 0;
  pbVar8[0x2c] = 0;
  pbVar8[0x2d] = 0;
  pbVar8[0x2e] = 0;
  pbVar8[0x2f] = 0;
  pbVar8[0] = 0;
  pbVar8[1] = 0;
  pbVar8[2] = 0;
  pbVar8[3] = 0;
  pbVar8[4] = 0;
  pbVar8[5] = 0;
  pbVar8[6] = 0;
  pbVar8[7] = 0;
  pbVar8[8] = 0;
  pbVar8[9] = 0;
  pbVar8[10] = 0;
  pbVar8[0xb] = 0;
  pbVar8[0xc] = 0;
  pbVar8[0xd] = 0;
  pbVar8[0xe] = 0;
  pbVar8[0xf] = 0;
  *(byte **)(pbVar8 + 0x10) = pbVar11;
  *(byte **)pbVar13 = pbVar8;
  plVar10 = *(long **)(BYTE_ARRAY_0043616d + lVar5 + 0x2b);
  *(int *)(pbVar8 + 0x20) = (int)(char)bVar1;
  pbVar9 = pbVar8;
  if (*plVar10 != 0) {
    *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x2b) = *plVar10;
    pbVar9 = *(byte **)pbVar13;
  }
  FUN_0043bb64(*(undefined8 *)(BYTE_ARRAY_0043616d + lVar5 + 0x33),pbVar9);
                    /* catch() { ... } // from try @ 00acd448 with catch @ 00acf6f4 */
  *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x3b) = *(long *)(BYTE_ARRAY_0043616d + lVar5 + 0x3b) + 1;
LAB_00acf700:
                    /* catch() { ... } // from try @ 00acd434 with catch @ 00acf714 */
  FUN_0047e89c(&local_70,&DAT_00ca4b00,*(long *)(pbVar8 + 0x28) + 0x60,PTR_DAT_00c9a8a0,0x12,1,0,0);
  plVar10 = plStack_68;
  uVar3 = local_70;
                    /* catch() { ... } // from try @ 00acd400 with catch @ 00acf734 */
  plVar12 = *(long **)(param_1 + 0x4b0);
  local_70 = 0;
  plStack_68 = (long *)0x0;
  *(long **)(param_1 + 0x4b0) = plVar10;
  *(undefined8 *)(param_1 + 0x4a8) = uVar3;
  if ((plVar12 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar12 + 1), lVar5 == 0)
     ) {
                    /* catch() { ... } // from try @ 00acd3ec with catch @ 00acf758 */
    (**(code **)(*plVar12 + 0x10))(plVar12);
                    /* catch() { ... } // from try @ 00aceacc with catch @ 00acf768 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar12);
  }
  plVar10 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar10 + 0x10))(plVar10);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar10);
  }
                    /* catch() { ... } // from try @ 00accbac with catch @ 00acf7a8 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
