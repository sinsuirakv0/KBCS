# 009bedcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009bedcc",
  "name": "FUN_009bedcc",
  "size": 1096,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "814fbf19c8aeb9efdd1413349e5033bed418b882b1e61bf8263c64dba58f8e87",
  "source_text_sha256": "814fbf19c8aeb9efdd1413349e5033bed418b882b1e61bf8263c64dba58f8e87"
}
~~~

## 呼び出し元

- [00859b58](../00859/00859b58.md)

## 呼び出し先

- [00467b60](../00467/00467b60.md)
- [00468bdc](../00468/00468bdc.md)
- [00468c60](../00468/00468c60.md)
- [00468f88](../00468/00468f88.md)
- [00469c04](../00469/00469c04.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [0046d974](../0046d/0046d974.md)
- [0046d9ac](../0046d/0046d9ac.md)
- [008514f8](../00851/008514f8.md)
- [008614b0](../00861/008614b0.md)
- [009be2e0](../009be/009be2e0.md)
- [00ac977c](../00ac9/00ac977c.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 6207 bytes

~~~c

void FUN_009bedcc(long param_1,undefined8 param_2)

{
  int *piVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  uint uVar5;
  undefined *puVar6;
  int iVar7;
  undefined4 uVar8;
  long lVar9;
  undefined8 uVar10;
  float fVar11;
  
                    /* try { // try from 009bede0 to 00abee6f has its CatchHandler @ 009bdb00 */
  if ((DAT_00ca4978 != 0) &&
     (lVar9 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c89680,0),
     lVar9 != 0)) {
    piVar1 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
    FUN_00467b60(param_2,0x5c,0x9a,0x4a,0xff);
    uVar10 = *(undefined8 *)(lVar9 + 0x108);
    iVar7 = FUN_0046c9c4(param_1);
    FUN_008514f8();
                    /* try { // try from 009bee70 to 00abee73 has its CatchHandler @ 009bf354 */
    uVar8 = FUN_0046ca84();
    FUN_00469c04(param_2,uVar10,0xffffffd8,0,iVar7 + 0x50,uVar8,0);
                    /* try { // try from 009bee98 to 00abeecb has its CatchHandler @ 009bf334 */
    FUN_00467b60(param_2,0x6e,0xa6,0x59,0xff);
    fVar11 = (float)FUN_0046d9ac((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
                    /* try { // try from 009beecc to 00abefd7 has its CatchHandler @ 009bdb00 */
    FUN_00468bdc(param_2,(int)(fVar11 * 115.0) + 0x8c);
    uVar10 = *(undefined8 *)(lVar9 + 0x118);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0,uVar8,0x330,0);
    FUN_00467b60(param_2,0xff,0xff,0xff,0xff);
    FUN_00468c60(param_2,0);
    FUN_008614b0(param_1,*(undefined8 *)(lVar9 + 200),0,0);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0,uVar8,0x37,0);
    FUN_00468c60(param_2,2);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0x249,uVar8,0x37,0);
    FUN_00468c60(param_2,0);
    FUN_00468f88(param_2,*(undefined8 *)(lVar9 + 0x108),
                 8 - *(int *)((long)&fde_table_entry_00334170.initial_loc + param_1),3,6);
                    /* try { // try from 009befd8 to 00abefef has its CatchHandler @ 009bf32c */
    if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
        ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
       ((((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0 &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
        (((*(byte *)((long)&fde_table_entry_00332060.initial_loc + param_1) & 1) == 0 &&
         (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))) {
      uVar2 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar5 = -uVar2;
                    /* try { // try from 009bf014 to 00abf04f has its CatchHandler @ 009bf398 */
      uVar2 = uVar2 & 3;
      if (-1 < (int)uVar5) {
        uVar2 = -(uVar5 & 3);
      }
      FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    puVar6 = PTR_DAT_00c9b4a8;
                    /* try { // try from 009bf050 to 00abf19b has its CatchHandler @ 009bdb00 */
    iVar3 = *(int *)(PTR_DAT_00c9b4a8 +
                    (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
    iVar7 = iVar3;
    if (iVar3 < 0) {
      iVar7 = iVar3 + 1;
    }
    FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),*piVar1 - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar3,
                 *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar3,9);
    iVar4 = *(int *)(puVar6 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1)
                              * 4);
    iVar7 = iVar4 + 0x54;
    iVar3 = iVar4 + 0x3c;
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),(*piVar1 - (iVar4 >> 1)) + 4,
                 (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
                 0x11,iVar7,iVar3,3);
    FUN_00ac977c((long)&fde_table_entry_00337d90.initial_loc + param_1,
                 *(undefined8 *)(lVar9 + 0x138),*(undefined8 *)(lVar9 + 0x178));
    FUN_00467b60(param_2,0xff,0xff,0xff,0xff);
    FUN_00468bdc(param_2,0x72);
    if (0 < *(int *)((long)&fde_table_entry_00337670.initial_loc + param_1)) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      fVar11 = (float)FUN_0046d974((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
      FUN_00468f88(param_2,uVar10,(int)(fVar11 * 10.0 + 24.0),0x11a,8);
    }
    FUN_00468c60(param_2,1);
    if (*(int *)((long)&fde_table_entry_00337670.initial_loc + param_1) <
        *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1) + -1) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      iVar7 = FUN_0046c9c4(param_1);
      fVar11 = (float)FUN_0046d974((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
                    /* try { // try from 009bf19c to 00abf1a7 has its CatchHandler @ 009bf520 */
      FUN_00468f88(param_2,uVar10,(int)((float)(iVar7 + -0x56) + fVar11 * -10.0),0x11a,8);
    }
                    /* try { // try from 009bf1bc to 00abf1db has its CatchHandler @ 009bf414 */
    FUN_00468c60(param_2,0);
    FUN_00468bdc(param_2,0xff);
                    /* try { // try from 009bf1f0 to 00abf1f7 has its CatchHandler @ 009bf3f0 */
    FUN_009be2e0((long)&fde_table_entry_00337630.initial_loc + param_1);
    return;
  }
                    /* try { // try from 009bf20c to 00abf213 has its CatchHandler @ 009bf3ec */
  return;
}

~~~
