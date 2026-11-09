# 00af3ecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af3ecc",
  "name": "FUN_00af3ecc",
  "size": 740,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ee441d4aa745da94cea0cac763539eef90b56bdd8fd04ffc9c9b43662eb2ba1",
  "source_text_sha256": "7ee441d4aa745da94cea0cac763539eef90b56bdd8fd04ffc9c9b43662eb2ba1"
}
~~~

## 呼び出し元

- [00af4220](../00af4/00af4220.md)
- [00af42cc](../00af4/00af42cc.md)

## 呼び出し先

- [0046e6ec](../0046e/0046e6ec.md)
- [0046e76c](../0046e/0046e76c.md)
- [0046e774](../0046e/0046e774.md)
- [0046e77c](../0046e/0046e77c.md)
- [004700ec](../00470/004700ec.md)
- [005e0c80](../005e0/005e0c80.md)
- [005e0eac](../005e0/005e0eac.md)
- [005e2ac8](../005e2/005e2ac8.md)
- [005e73e0](../005e7/005e73e0.md)
- [0067d0c0](../0067d/0067d0c0.md)
- [008514b8](../00851/008514b8.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 3411 bytes

~~~c

void FUN_00af3ecc(undefined8 param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int iVar4;
  undefined4 uVar5;
  uint uVar6;
  undefined4 uVar7;
  int iVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  ulong uVar13;
  int extraout_w1;
  int extraout_w1_00;
  int extraout_w1_01;
  int local_70 [2];
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  uVar5 = FUN_005e0eac(param_2,param_3);
  lVar9 = FUN_008514b8();
  uVar6 = FUN_005e73e0(lVar9 + (long)param_2 * 0x1f0 + 0x2768);
  uVar10 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar10,uVar6 & 1);
  uVar10 = FUN_0046e76c();
  uVar11 = FUN_005e2ac8(param_1,param_2,uVar5);
  uVar12 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar12,uVar6 & 1);
  uVar7 = FUN_0046e774();
  uVar12 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar12,uVar6 & 1);
  uVar5 = FUN_0046e77c();
  FUN_0046e6ec(uVar10,uVar11,uVar7,uVar5,local_70);
  if (param_2 == 0) {
    lVar9 = FUN_008514b8();
    iVar1 = *(int *)(lVar9 + 0x9f690);
    lVar9 = FUN_008514b8();
    *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x84940) = iVar1 + local_70[0] * -0x14;
  }
  else {
    lVar9 = FUN_008514b8();
    *(int *)(lVar9 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x84940) = local_70[0] * 10;
    if (param_2 == 1) {
      lVar9 = FUN_008514b8();
      uVar13 = FUN_005e73e0(lVar9 + 0x2958);
      if ((uVar13 & 1) == 0) {
        lVar9 = FUN_008514b8();
        if (*(int *)(lVar9 + (long)param_3 * 0x3ec + 0x911cc) != 0) {
          lVar9 = FUN_008514b8();
          iVar1 = *(int *)(lVar9 + 0x910d8);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
                    /* try { // try from 00af405c to 00bf40df has its CatchHandler @ 00af405c
                       catch() { ... } // from try @ 00af405c with catch @ 00af405c
                       catch() { ... } // from try @ 00af40f4 with catch @ 00af405c */
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          iVar4 = (int)((ulong)((long)(extraout_w1 * 0x49c) * -0x51eb851f) >> 0x20);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
          iVar8 = FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
                    /* try { // try from 00af40e0 to 00bf40f3 has its CatchHandler @ 00af4124 */
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
                    /* try { // try from 00af40f4 to 00bf4143 has its CatchHandler @ 00af405c */
          lVar9 = FUN_008514b8();
          iVar2 = *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x91144);
                    /* catch() { ... } // from try @ 00af40e0 with catch @ 00af4124 */
          lVar9 = FUN_008514b8();
          *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x91144) =
               ((iVar4 >> 5) - (iVar4 >> 0x1f)) + iVar1 + (extraout_w1_00 * iVar8) / 10 + iVar2 +
               (extraout_w1_01 * 0x7f) / 10;
        }
      }
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
