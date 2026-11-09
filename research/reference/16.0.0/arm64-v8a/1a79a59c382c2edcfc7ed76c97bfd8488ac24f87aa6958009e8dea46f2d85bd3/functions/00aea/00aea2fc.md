# 00aea2fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aea2fc",
  "name": "FUN_00aea2fc",
  "size": 1400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a8590865c3f077d31cc3c14a80e2e7fc523e2f0878e8e654813f87bfed858e3c",
  "source_text_sha256": "a8590865c3f077d31cc3c14a80e2e7fc523e2f0878e8e654813f87bfed858e3c"
}
~~~

## 呼び出し元

- [00ae0e64](../00ae0/00ae0e64.md)
- [00af0928](../00af0/00af0928.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467ab0](../00467/00467ab0.md)
- [00467aec](../00467/00467aec.md)
- [00467b20](../00467/00467b20.md)
- [00467f14](../00467/00467f14.md)
- [00468b9c](../00468/00468b9c.md)
- [00468f48](../00468/00468f48.md)
- [00469bc4](../00469/00469bc4.md)
- [0046da7c](../0046d/0046da7c.md)
- [005c04b0](../005c0/005c04b0.md)
- [00743d50](../00743/00743d50.md)
- [00743eec](../00743/00743eec.md)
- [00744158](../00744/00744158.md)
- [007441c8](../00744/007441c8.md)
- [00a41e38](../00a41/00a41e38.md)
- [00a41ec4](../00a41/00a41ec4.md)
- [00a41f9c](../00a41/00a41f9c.md)
- [00adee94](../00ade/00adee94.md)
- [00b09234](../00b09/00b09234.md)
- [00b0a8ec](../00b0a/00b0a8ec.md)
- [00c58210](../00c58/00c58210.md)

## 疑似コード / UTF-8 9624 bytes

~~~c

void FUN_00aea2fc(long param_1,uint param_2)

{
  int iVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  undefined4 uVar6;
  long lVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  long lVar13;
  long lVar14;
  ulong uVar15;
  
                    /* try { // try from 00aea2fc to 00bea31f has its CatchHandler @ 00aea780 */
                    /* try { // try from 00aea320 to 00bea3bf has its CatchHandler @ 00aea1c8 */
  if (DAT_00ca4578 == 0) {
    lVar7 = 0;
  }
  else {
    lVar7 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d550,0);
  }
  uVar8 = FUN_00467820();
  if (*(int *)((long)&fde_table_entry_00333a88.initial_loc + param_1) - 1U == param_2) {
    return;
  }
  lVar14 = param_1 + 0xc5b8;
  uVar15 = -(ulong)(param_2 >> 0x1f) & 0xfffffffc00000000 | (ulong)param_2 << 2;
  lVar13 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
  pbVar2 = (byte *)(lVar13 + uVar15);
                    /* try { // try from 00aea3c0 to 00bea3cf has its CatchHandler @ 00aea744 */
  if (((uint)(*(byte *)(lVar13 + 0x2a) ^ pbVar2[2]) << 0x10 |
       (uint)(*(byte *)(lVar13 + 0x2b) ^ pbVar2[3]) << 0x18 |
       (uint)(*(byte *)(lVar13 + 0x29) ^ pbVar2[1]) << 8 |
      (uint)(*(byte *)(lVar13 + 0x28) ^ *pbVar2)) == 0xffffffff) {
    return;
  }
                    /* try { // try from 00aea3e0 to 00bea3e7 has its CatchHandler @ 00aea758 */
  lVar13 = (long)(int)param_2;
  uVar9 = FUN_00adee94(param_1,param_2);
  if ((uVar9 & 1) == 0) {
    iVar5 = 0xff;
    lVar10 = *(long *)(lVar7 + lVar13 * 0x10 + 0x340);
    iVar4 = 0xff;
    if (lVar10 != 0) goto LAB_00aea454;
  }
  else {
    iVar5 = FUN_0046da7c(*(int *)(param_1 + 0x1188) * -0x11 + 0xff,0);
    lVar3 = lVar7 + lVar13 * 0x10;
    lVar10 = *(long *)(lVar3 + 0x340);
    if (lVar10 != 0) {
      iVar4 = iVar5;
      if (iVar5 < 0xff) {
        FUN_00468b9c(uVar8,iVar5);
        lVar10 = *(long *)(lVar3 + 0x340);
                    /* try { // try from 00aea440 to 00bea447 has its CatchHandler @ 00aea750 */
      }
LAB_00aea454:
      iVar5 = iVar4;
                    /* try { // try from 00aea484 to 00bea4cf has its CatchHandler @ 00aea77c */
      FUN_00469bc4(uVar8,lVar10,
                   *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1) +
                   *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1),
                   *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1) +
                   *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1),0x6e,0x55
                   ,0);
      FUN_00467b20(uVar8,0xff,0xff,0xff,0xff);
    }
  }
  if ((*(uint *)(param_1 + 0x3398) & 0xfffffffe) == 2) {
    uVar6 = FUN_00a41e38((long)&DWORD_00347348 + param_1);
    uVar9 = FUN_00a41ec4((long)&DWORD_00347348 + param_1,uVar6);
    if (((uVar9 & 1) == 0) ||
       (uVar9 = FUN_00a41f9c((long)&DWORD_00347348 + param_1,param_2,1), (uVar9 & 1) != 0)) {
      lVar10 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
                    /* try { // try from 00aea500 to 00bea523 has its CatchHandler @ 00aea74c */
      pbVar2 = (byte *)(lVar10 + uVar15);
      iVar4 = CONCAT13(*(byte *)(lVar10 + 0x2b) ^ pbVar2[3],
                       CONCAT12(*(byte *)(lVar10 + 0x2a) ^ pbVar2[2],
                                CONCAT11(*(byte *)(lVar10 + 0x29) ^ pbVar2[1],
                                         *(byte *)(lVar10 + 0x28) ^ *pbVar2))) + -2;
      uVar9 = FUN_007441c8(param_1 + 0xbe0);
      if ((((uVar9 & 1) == 0) || (uVar9 = FUN_00743d50(param_1 + 0xbe0,iVar4), (uVar9 & 1) != 0)) &&
         ((uVar9 = FUN_00b09234(param_1 + 0x3d8), (uVar9 & 1) == 0 ||
          (uVar9 = FUN_00b0a8ec(param_1 + 0x3d8,iVar4), (uVar9 & 1) != 0)))) goto LAB_00aea744;
    }
    lVar10 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
    pbVar2 = (byte *)(lVar10 + uVar15);
                    /* try { // try from 00aea5a4 to 00bea5af has its CatchHandler @ 00aea740 */
                    /* try { // try from 00aea5b0 to 00bea6fb has its CatchHandler @ 00aea1c8 */
    iVar4 = CONCAT13(*(byte *)(lVar10 + 0x2b) ^ pbVar2[3],
                     CONCAT12(*(byte *)(lVar10 + 0x2a) ^ pbVar2[2],
                              CONCAT11(*(byte *)(lVar10 + 0x29) ^ pbVar2[1],
                                       *(byte *)(lVar10 + 0x28) ^ *pbVar2))) + -2;
    uVar9 = FUN_007441c8(param_1 + 0xbe0);
    if ((((uVar9 & 1) == 0) || (uVar9 = FUN_00743d50(param_1 + 0xbe0,iVar4), (uVar9 & 1) != 0)) &&
       ((uVar9 = FUN_00b09234(param_1 + 0x3d8), (uVar9 & 1) == 0 ||
        (uVar9 = FUN_00b0a8ec(param_1 + 0x3d8,iVar4), (uVar9 & 1) != 0)))) {
      iVar5 = 0xff - iVar5;
      iVar4 = (iVar5 * 0x35) / 0xff + 0xca;
      iVar1 = (iVar5 * 0x6b) / 0xff + 0x94;
      iVar5 = (iVar5 * 0x71) / 0xff + 0x8e;
    }
    else {
      iVar5 = 0xff - iVar5;
      iVar4 = (iVar5 * 0x71) / 0xff + 0x8e;
      iVar1 = (iVar5 * 0x56) / 0xff + 0xa9;
      iVar5 = (iVar5 * 0x7b) / 0xff + 0x84;
    }
    FUN_00467aec(uVar8,iVar4,iVar1,iVar5,0xff);
                    /* try { // try from 00aea6fc to 00bea6ff has its CatchHandler @ 00aea798 */
                    /* try { // try from 00aea700 to 00bea727 has its CatchHandler @ 00aea1c8 */
    FUN_00467ab0(uVar8,2);
                    /* try { // try from 00aea728 to 00bea72b has its CatchHandler @ 00aea77c */
    FUN_00467f14(uVar8,*(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1
                               ) +
                       *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1),
                 *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1) +
                 *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1),0x6e,0x55);
                    /* try { // try from 00aea73c to 00bea73f has its CatchHandler @ 00aea758 */
                    /* catch() { ... } // from try @ 00aea5a4 with catch @ 00aea740
                       try { // try from 00aea740 to 00bea7d7 has its CatchHandler @ 00aea1c8 */
    FUN_00467ab0(uVar8,0);
  }
LAB_00aea744:
                    /* catch() { ... } // from try @ 00aea3c0 with catch @ 00aea744 */
  uVar9 = FUN_007441c8(param_1 + 0xbe0);
                    /* catch() { ... } // from try @ 00aea500 with catch @ 00aea74c */
  if ((uVar9 & 1) != 0) {
                    /* catch() { ... } // from try @ 00aea440 with catch @ 00aea750 */
                    /* catch() { ... } // from try @ 00aea3e0 with catch @ 00aea758
                       catch() { ... } // from try @ 00aea73c with catch @ 00aea758 */
    uVar6 = FUN_00744158(param_1 + 0xbe0,param_2);
    uVar9 = FUN_00743eec(param_1 + 0xbe0,uVar6);
    if ((uVar9 & 1) != 0) {
      uVar11 = *(undefined8 *)(lVar7 + 0x118);
                    /* catch() { ... } // from try @ 00aea484 with catch @ 00aea77c
                       catch() { ... } // from try @ 00aea728 with catch @ 00aea77c */
                    /* catch() { ... } // from try @ 00aea2fc with catch @ 00aea780 */
      iVar5 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1) +
              *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1);
                    /* catch() { ... } // from try @ 00aea224 with catch @ 00aea790 */
      iVar4 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1) +
              *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1);
      uVar12 = 0x83;
      goto LAB_00aea83c;
    }
  }
  lVar14 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
  pbVar2 = (byte *)(lVar14 + uVar15);
                    /* try { // try from 00aea7d8 to 00bea823 has its CatchHandler @ 00aea7d8
                       catch() { ... } // from try @ 00aea7d8 with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aea8ac with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aeabd0 with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aead28 with catch @ 00aea7d8 */
  uVar15 = FUN_005c04b0(param_1 + 0x4a0,(long)*(int *)((long)&DWORD_0039b97c + param_1),
                        CONCAT13(*(byte *)(lVar14 + 0x2b) ^ pbVar2[3],
                                 CONCAT12(*(byte *)(lVar14 + 0x2a) ^ pbVar2[2],
                                          CONCAT11(*(byte *)(lVar14 + 0x29) ^ pbVar2[1],
                                                   *(byte *)(lVar14 + 0x28) ^ *pbVar2))) + -2);
  if ((uVar15 & 1) == 0) {
                    /* try { // try from 00aea858 to 00bea86b has its CatchHandler @ 00aead84 */
    return;
  }
  uVar11 = *(undefined8 *)(lVar7 + 0x118);
                    /* try { // try from 00aea824 to 00bea82b has its CatchHandler @ 00aeada0 */
  iVar5 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1) +
          *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1);
  iVar4 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1) +
          *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1);
  uVar12 = 0x8e;
LAB_00aea83c:
                    /* catch() { ... } // from try @ 00aea268 with catch @ 00aea798
                       catch() { ... } // from try @ 00aea6fc with catch @ 00aea798 */
  FUN_00468f48(uVar8,uVar11,iVar5 + 2,iVar4 + 2,uVar12);
  return;
}

~~~
