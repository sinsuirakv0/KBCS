# 009bfdcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "009bfdcc",
  "name": "FUN_009bfdcc",
  "size": 1096,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f48f40826f1bc3d2697e59dba8ffe363602ddfbf3d55df2a29c35ae049ebdb9b",
  "source_text_sha256": "f48f40826f1bc3d2697e59dba8ffe363602ddfbf3d55df2a29c35ae049ebdb9b"
}
~~~

## 呼び出し元

- [0085ab5c](../0085a/0085ab5c.md)

## 呼び出し先

- [00467ec0](../00467/00467ec0.md)
- [00468f3c](../00468/00468f3c.md)
- [00468fc0](../00468/00468fc0.md)
- [004692e8](../00469/004692e8.md)
- [00469f64](../00469/00469f64.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [0046dcd4](../0046d/0046dcd4.md)
- [0046dd0c](../0046d/0046dd0c.md)
- [008524fc](../00852/008524fc.md)
- [008624b4](../00862/008624b4.md)
- [009bf2e0](../009bf/009bf2e0.md)
- [00aca7e0](../00aca/00aca7e0.md)
- [00c596b0](../00c59/00c596b0.md)

## 疑似コード / UTF-8 6207 bytes

~~~c

void FUN_009bfdcc(long param_1,undefined8 param_2)

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
  
                    /* try { // try from 009bfde4 to 00abfe73 has its CatchHandler @ 009beb04 */
  if ((DAT_00ca5a38 != 0) &&
     (lVar9 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8a720,0),
     lVar9 != 0)) {
    piVar1 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
    FUN_00467ec0(param_2,0x5c,0x9a,0x4a,0xff);
    uVar10 = *(undefined8 *)(lVar9 + 0x108);
    iVar7 = FUN_0046cd24(param_1);
    FUN_008524fc();
    uVar8 = FUN_0046cde4();
                    /* try { // try from 009bfe74 to 00abfe77 has its CatchHandler @ 009c0358 */
    FUN_00469f64(param_2,uVar10,0xffffffd8,0,iVar7 + 0x50,uVar8,0);
                    /* try { // try from 009bfe9c to 00abfecf has its CatchHandler @ 009c0338 */
    FUN_00467ec0(param_2,0x6e,0xa6,0x59,0xff);
    fVar11 = (float)FUN_0046dd0c((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
                    /* try { // try from 009bfed0 to 00abffdb has its CatchHandler @ 009beb04 */
    FUN_00468f3c(param_2,(int)(fVar11 * 115.0) + 0x8c);
    uVar10 = *(undefined8 *)(lVar9 + 0x118);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0,uVar8,0x330,0);
    FUN_00467ec0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468fc0(param_2,0);
    FUN_008624b4(param_1,*(undefined8 *)(lVar9 + 200),0,0);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0,uVar8,0x37,0);
    FUN_00468fc0(param_2,2);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0x249,uVar8,0x37,0);
    FUN_00468fc0(param_2,0);
    FUN_004692e8(param_2,*(undefined8 *)(lVar9 + 0x108),
                 8 - *(int *)((long)&fde_table_entry_00334170.initial_loc + param_1),3,6);
                    /* try { // try from 009bffdc to 00abfff3 has its CatchHandler @ 009c0330 */
    if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
        ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
       ((((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0 &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
        (((*(byte *)((long)&fde_table_entry_00332060.initial_loc + param_1) & 1) == 0 &&
         (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))) {
      uVar2 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar5 = -uVar2;
                    /* try { // try from 009c0018 to 00ac0053 has its CatchHandler @ 009c039c */
      uVar2 = uVar2 & 3;
      if (-1 < (int)uVar5) {
        uVar2 = -(uVar5 & 3);
      }
      FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    puVar6 = PTR_DAT_00c9c548;
                    /* try { // try from 009c0054 to 00ac019f has its CatchHandler @ 009beb04 */
    iVar3 = *(int *)(PTR_DAT_00c9c548 +
                    (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
    iVar7 = iVar3;
    if (iVar3 < 0) {
      iVar7 = iVar3 + 1;
    }
    FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),*piVar1 - (iVar7 >> 1),
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
    FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),(*piVar1 - (iVar4 >> 1)) + 4,
                 (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
                 0x11,iVar7,iVar3,3);
    FUN_00aca7e0((long)&fde_table_entry_00337d90.initial_loc + param_1,
                 *(undefined8 *)(lVar9 + 0x138),*(undefined8 *)(lVar9 + 0x178));
    FUN_00467ec0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468f3c(param_2,0x72);
    if (0 < *(int *)((long)&fde_table_entry_00337670.initial_loc + param_1)) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      fVar11 = (float)FUN_0046dcd4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
      FUN_004692e8(param_2,uVar10,(int)(fVar11 * 10.0 + 24.0),0x11a,8);
    }
    FUN_00468fc0(param_2,1);
    if (*(int *)((long)&fde_table_entry_00337670.initial_loc + param_1) <
        *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1) + -1) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      iVar7 = FUN_0046cd24(param_1);
      fVar11 = (float)FUN_0046dcd4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
                    /* try { // try from 009c01a0 to 00ac01ab has its CatchHandler @ 009c0524 */
      FUN_004692e8(param_2,uVar10,(int)((float)(iVar7 + -0x56) + fVar11 * -10.0),0x11a,8);
    }
    FUN_00468fc0(param_2,0);
                    /* try { // try from 009c01c0 to 00ac01df has its CatchHandler @ 009c0418 */
    FUN_00468f3c(param_2,0xff);
    FUN_009bf2e0((long)&fde_table_entry_00337630.initial_loc + param_1);
    return;
  }
                    /* try { // try from 009c01f4 to 00ac01fb has its CatchHandler @ 009c03f4 */
                    /* try { // try from 009c0210 to 00ac0217 has its CatchHandler @ 009c03f0 */
  return;
}

~~~
