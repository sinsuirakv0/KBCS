# 005efbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](005efbac.md)

## 関数情報

~~~json
{
  "address": "005efbac",
  "name": "FUN_005efbac",
  "size": 828,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc60064482468ce59a74ea4266b4f2f6c6d543487f7e704e4a3a3d521a5039ca",
  "source_text_sha256": "dc60064482468ce59a74ea4266b4f2f6c6d543487f7e704e4a3a3d521a5039ca"
}
~~~
## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)

## 呼び出し先

- [00444c18](../00444/00444c18.md)
- [00444c54](../00444/00444c54.md)
- [0044507c](../00445/0044507c.md)
- [004460b0](../00446/004460b0.md)
- [00448034](../00448/00448034.md)
- [00449aec](../00449/00449aec.md)
- [00467074](../00467/00467074.md)
- [0081f580](../0081f/0081f580.md)
- [00883bb8](../00883/00883bb8.md)
- [008847e4](../00884/008847e4.md)
- [00a0b03c](../00a0b/00a0b03c.md)
- [00a0b818](../00a0b/00a0b818.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 5617 bytes

~~~c

void FUN_005efbac(long param_1,long param_2,undefined8 param_3)

{
  int *piVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  uint uVar6;
  undefined *puVar7;
  int iVar8;
  undefined4 uVar9;
  ulong uVar10;
  long lVar11;
  undefined8 uVar12;
  float local_8c;
  float fStack_88;
  long local_78;
  
  lVar5 = tpidr_el0;
                    /* try { // try from 005efbd4 to 006efbdb has its CatchHandler @ 005efcd4 */
  local_78 = *(long *)(lVar5 + 0x28);
  piVar1 = (int *)(param_1 + 0x83e38);
  if (0 < *piVar1) {
    uVar2 = *(uint *)(param_1 + 0x83e3c);
    uVar12 = *(undefined8 *)(param_2 + 0x410);
    if (0xb < uVar2) {
      uVar2 = 0xc;
    }
    if (*piVar1 != 1) {
      uVar2 = 0xc;
    }
    iVar8 = FUN_00449aec();
    puVar7 = PTR_DAT_00c1b5f0;
    if (iVar8 < 0) {
      iVar8 = iVar8 + 1;
    }
                    /* try { // try from 005efc3c to 006efc43 has its CatchHandler @ 005efcbc */
                    /* try { // try from 005efc48 to 006efc53 has its CatchHandler @ 005efcac */
    FUN_004460b0(param_3,uVar12,
                 ((iVar8 >> 1) - *(int *)(PTR_DAT_00c1b5f0 + (ulong)uVar2 * 4)) + -0xef,0xbe,0xc);
    if (1 < *piVar1) {
      uVar2 = *(uint *)(param_1 + 0x83e3c);
      if (0xb < uVar2) {
        uVar2 = 0xc;
      }
                    /* try { // try from 005efc70 to 006efc7b has its CatchHandler @ 005efca8 */
      if (*piVar1 != 2) {
        uVar2 = 0xc;
      }
      FUN_00444c18(param_3,2);
                    /* try { // try from 005efc7c to 006efd03 has its CatchHandler @ 005efb8c */
      FUN_00444c54(param_3,0x28,0x28,0x4d,0xff);
      iVar8 = *(int *)(puVar7 + (ulong)uVar2 * 4);
      uVar9 = FUN_00449aec(param_1);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc70 with catch @ 005efca8
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc48 with catch @ 005efcac
                        */
      FUN_0044507c(param_3,-iVar8,0x13b,uVar9,0x37);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc3c with catch @ 005efcbc
                        */
      FUN_00444c18(param_3,0);
      uVar10 = FUN_00a0b03c(*(undefined8 *)(param_1 + 0x7e8));
      if ((uVar10 & 1) != 0) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efbd4 with catch @ 005efcd4
                        */
        uVar12 = *(undefined8 *)(param_2 + 800);
        FUN_0081f580();
        iVar8 = FUN_00449aec();
        iVar4 = *(int *)(puVar7 + (ulong)uVar2 * 4);
        if (iVar8 < 0) {
          iVar8 = iVar8 + 1;
        }
        uVar9 = FUN_00a0b818(*(undefined8 *)(param_1 + 0x7e8));
                    /* catch() { ... } // from try @ 005efdac with catch @ 005efd04 */
        lVar11 = FUN_00467074(*(undefined8 *)(param_2 + 0x410),5);
        iVar3 = *(int *)(lVar11 + 8);
        lVar11 = FUN_00467074(*(undefined8 *)(param_2 + 0x410),4);
                    /* try { // try from 005efd4c to 006efd53 has its CatchHandler @ 005efe00 */
        FUN_00448034(&local_8c,(float)((iVar8 >> 1) - iVar4),0x43a08000,0xbf800000,param_3,uVar12,0,
                     uVar9,iVar3 + 0x14,*(int *)(lVar11 + 8) + 0x14,1,0);
        uVar12 = *(undefined8 *)(param_2 + 0x410);
        lVar11 = FUN_00467074(uVar12,0xb);
                    /* try { // try from 005efd90 to 006efd9f has its CatchHandler @ 005efde8 */
                    /* try { // try from 005efda0 to 006efdab has its CatchHandler @ 005efdd8 */
        FUN_004460b0(param_3,uVar12,(int)((local_8c - (float)*(int *)(lVar11 + 8)) + -20.0),0x144,
                     0xb);
                    /* try { // try from 005efdac to 006efe2f has its CatchHandler @ 005efd04 */
        FUN_004460b0(param_3,*(undefined8 *)(param_2 + 0x410),(int)(fStack_88 + 20.0),0x143,4);
        if (*piVar1 == 2) goto LAB_005efeb0;
                    /* catch() { ... } // from try @ 005efda0 with catch @ 005efdd8 */
        if (*(int *)(param_1 + 0x83e58) == 1) {
                    /* catch() { ... } // from try @ 005efd90 with catch @ 005efde8 */
          uVar12 = *(undefined8 *)(param_2 + 0x410);
                    /* catch() { ... } // from try @ 005efd4c with catch @ 005efe00 */
          lVar11 = FUN_00467074(uVar12,6);
          iVar8 = *(int *)(lVar11 + 8);
          uVar2 = *(uint *)(BYTE_ARRAY_003c3369 + param_1 + 3) & 3;
          if (iVar8 < 0) {
            iVar8 = iVar8 + 1;
          }
          uVar6 = -*(uint *)(BYTE_ARRAY_003c3369 + param_1 + 3);
                    /* catch() { ... } // from try @ 005f0028 with catch @ 005efe30 */
          if (-1 < (int)uVar6) {
            uVar2 = -(uVar6 & 3);
          }
          FUN_004460b0(param_3,uVar12,
                       (int)((local_8c + (fStack_88 - local_8c) * 0.5) - (float)(iVar8 >> 1)),300,
                       ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 6 &
                       0xff);
        }
      }
      if ((*piVar1 == 7) && ((*(byte *)((long)&DWORD_0032e038 + param_1) & 1) == 0)) {
        uVar12 = FUN_008847e4(param_1 + 0x2e48,200);
        FUN_00883bb8(uVar12,0,0);
        uVar12 = FUN_008847e4(param_1 + 0x2e48,0xc9);
                    /* try { // try from 005efea8 to 006efeaf has its CatchHandler @ 005f0068 */
        FUN_00883bb8(uVar12,0,0);
      }
    }
  }
LAB_005efeb0:
  if (*(long *)(lVar5 + 0x28) == local_78) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
