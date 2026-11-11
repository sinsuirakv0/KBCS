# 006acaec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "006acaec",
  "name": "FUN_006acaec",
  "size": 1136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45473c2ae722ab12b886d48f69e9d870b234626afd31970cceb3348fbed31ec9",
  "source_text_sha256": "45473c2ae722ab12b886d48f69e9d870b234626afd31970cceb3348fbed31ec9"
}
~~~

## 呼び出し元

- [0099703c](../00997/0099703c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00467af0](../00467/00467af0.md)
- [00467b2c](../00467/00467b2c.md)
- [00467f54](../00467/00467f54.md)
- [004688b8](../00468/004688b8.md)
- [00469c04](../00469/00469c04.md)
- [0046bd54](../0046b/0046bd54.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [0046e72c](../0046e/0046e72c.md)
- [0046e7ac](../0046e/0046e7ac.md)
- [0046e7b4](../0046e/0046e7b4.md)
- [0046e7bc](../0046e/0046e7bc.md)
- [004700b4](../00470/004700b4.md)
- [0047012c](../00470/0047012c.md)
- [006acf5c](../006ac/006acf5c.md)
- [006ad414](../006ad/006ad414.md)
- [006c119c](../006c1/006c119c.md)
- [008514f8](../00851/008514f8.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 6866 bytes

~~~c

void FUN_006acaec(char *param_1)

{
  byte *pbVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  undefined8 uVar9;
  long lVar10;
  char *pcVar11;
  undefined8 uVar12;
  int local_70;
  int iStack_6c;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  if (DAT_00ca4978 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c711c0,0);
  }
  uVar9 = FUN_00467860();
  if (*param_1 == '\0') goto LAB_006acf28;
  if ((param_1[0x4e0] & 1U) == 0) {
    uVar12 = *(undefined8 *)(param_1 + 0x208);
                    /* try { // try from 006acb6c to 007acb73 has its CatchHandler @ 006acde8 */
    FUN_008514f8();
    uVar3 = FUN_0046c9c4();
    FUN_008514f8();
    uVar4 = FUN_0046ca84();
                    /* try { // try from 006acb94 to 007acbbf has its CatchHandler @ 006acdf0 */
    uVar5 = 0x62;
    if (*(int *)(param_1 + 0x4e8) != 3) {
      uVar5 = 2;
    }
    FUN_00469c04(uVar9,uVar12,0,0,uVar3,uVar4,uVar5);
    iVar6 = *(int *)(param_1 + 0x4ec);
    if (iVar6 == 1) {
                    /* try { // try from 006acbc0 to 007acc37 has its CatchHandler @ 006aca44 */
      FUN_00467af0(uVar9,1);
      FUN_00467b2c(uVar9,0xab,0x2c,0,0x40);
      lVar10 = FUN_008514f8();
      iVar6 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar10);
      FUN_008514f8();
      uVar5 = FUN_0046c9c4();
      FUN_008514f8();
      uVar3 = FUN_0046ca84();
      FUN_00467f54(uVar9,0,-iVar6,uVar5,uVar3);
      FUN_00467b2c(uVar9,0xff,0xff,0xff,0xff);
                    /* try { // try from 006acc38 to 007acc3f has its CatchHandler @ 006acd78 */
      FUN_00467af0(uVar9,0);
                    /* try { // try from 006acc44 to 007acc4b has its CatchHandler @ 006acdc8 */
      iVar6 = *(int *)(param_1 + 0x4ec);
    }
    FUN_004700b4(param_1 + (long)iVar6 * 0xa8 + 0x38,param_1 + (long)iVar6 * 0x38 + 0x188,
                 *(undefined4 *)(param_1 + 0x4f4),0);
    FUN_0047012c(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,0);
    uVar12 = FUN_0046e7ac();
    iVar6 = *(int *)(param_1 + 0x4ec);
                    /* try { // try from 006acc88 to 007acc8f has its CatchHandler @ 006acd58 */
    FUN_0047012c(param_1 + (long)iVar6 * 0xa8 + 0x38,1);
    uVar5 = FUN_0046e7b4();
                    /* try { // try from 006acc9c to 007accab has its CatchHandler @ 006acd90 */
                    /* try { // try from 006accac to 007ace2f has its CatchHandler @ 006aca44 */
    FUN_0047012c(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,1);
    uVar3 = FUN_0046e7bc();
    FUN_0046e72c(uVar12,param_1 + (long)iVar6 * 0xa8 + 0x38,uVar5,uVar3,&local_70);
    FUN_008514f8();
    iVar6 = FUN_0046c9c4();
    if (iVar6 < 0) {
      iVar6 = iVar6 + 1;
    }
    lVar10 = FUN_008514f8();
    lVar10 = lVar10 + (long)*(int *)(param_1 + 0x4e4) * 0x100;
    pbVar1 = (byte *)(lVar10 + 0x4b278 +
                     (long)(*(int *)(param_1 + 0x4e8) + *(int *)(param_1 + 0x4ec) + 0x33) * 4);
                    /* catch() { ... } // from try @ 006acc88 with catch @ 006acd58 */
    FUN_0046bd54(uVar9,param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,
                 (iVar6 >> 1) - local_70,
                 ((uint)CONCAT12(*(byte *)(lVar10 + 0x4b376) ^ pbVar1[2],
                                 CONCAT11(*(byte *)(lVar10 + 0x4b375) ^ pbVar1[1],
                                          *(byte *)(lVar10 + 0x4b374) ^ *pbVar1)) - iStack_6c) +
                 (uint)(*(byte *)(lVar10 + 0x4b377) ^ pbVar1[3]) * 0x1000000 + 0x1d4);
    iVar6 = *(int *)(param_1 + 0x4f0);
    if (iVar6 < 3) {
      if (iVar6 == 1) {
                    /* try { // try from 006acec0 to 007acf93 has its CatchHandler @ 006acec0
                       catch() { ... } // from try @ 006acec0 with catch @ 006acec0
                       catch() { ... } // from try @ 006acfc0 with catch @ 006acec0
                       catch() { ... } // from try @ 006ad0e8 with catch @ 006acec0 */
        FUN_004700b4(param_1 + 0x268,param_1 + 0x310,*(undefined4 *)(param_1 + 0x4f8),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        pcVar11 = param_1 + 0x268;
      }
      else {
                    /* catch() { ... } // from try @ 006acc38 with catch @ 006acd78 */
        if (iVar6 != 2) goto LAB_006acf0c;
                    /* catch() { ... } // from try @ 006acc9c with catch @ 006acd90 */
        FUN_004700b4(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        pcVar11 = param_1 + 0x380;
      }
      if (iVar7 < 0) {
        iVar7 = iVar7 + 1;
      }
      FUN_0046bd54(uVar9,pcVar11,iVar6 >> 1,iVar7 >> 1);
    }
    else {
                    /* catch() { ... } // from try @ 006acc44 with catch @ 006acdc8 */
      if ((iVar6 == 3) || (iVar6 == 4)) {
        FUN_004700b4(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
                    /* catch() { ... } // from try @ 006acb6c with catch @ 006acde8 */
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
                    /* catch() { ... } // from try @ 006acb94 with catch @ 006acdf0 */
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        if (iVar7 < 0) {
          iVar7 = iVar7 + 1;
        }
        FUN_0046bd54(uVar9,param_1 + 0x380,iVar6 >> 1,iVar7 >> 1);
        FUN_006c119c(param_1 + 0x460);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469c04(uVar9,uVar12,(iVar6 >> 1) + -0xd7,0x1f8,0xdc,0x3e,1);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469c04(uVar9,uVar12,iVar6 >> 1,0x1f8,0xdc,0x3e,2);
        uVar12 = *(undefined8 *)(param_1 + 0x1f8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_004688b8(uVar9,uVar12,iVar6 >> 1,0x217,0x1a4,5);
      }
    }
LAB_006acf0c:
    FUN_006acf5c();
  }
  if ((*(uint *)(param_1 + 0x4f0) | 4) == 4) {
    FUN_006ad414(param_1);
  }
LAB_006acf28:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
