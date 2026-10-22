# 00ada6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ada6ac.md)

## 関数情報

~~~json
{
  "address": "00ada6ac",
  "name": "FUN_00ada6ac",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9224bda61287450262989e57a3a9fe3e70d0314ba0dd9094134cf642d900b8f2",
  "source_text_sha256": "9224bda61287450262989e57a3a9fe3e70d0314ba0dd9094134cf642d900b8f2"
}
~~~
## 呼び出し元

- [0085f63c](../0085f/0085f63c.md)
- [00871208](../00871/00871208.md)
- [00879fe4](../00879/00879fe4.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00adb7ac](../00adb/00adb7ac.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"tapjoySpendCurrency"
~~~
## 疑似コード 1/1 / UTF-8 2818 bytes

~~~c

void FUN_00ada6ac(undefined4 param_1,long *param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long *plVar5;
  byte *pbVar6;
  long lVar7;
  byte local_90 [16];
  void *local_80;
  long local_78;
  byte local_70;
  char acStack_6f [8];
  undefined7 uStack_67;
  undefined4 uStack_60;
  uint uStack_5c;
  byte *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar2 = FUN_00565f94();
  uVar3 = FUN_00566284();
  local_70 = 0x26;
  local_90[0] = 8;
  uStack_5c = uStack_5c & 0xffffff00;
  uStack_67 = (undefined7)s_tapjoySpendCurrency_0029523a._8_8_;
  uStack_60 = CONCAT31(0x79636e,SUB81(s_tapjoySpendCurrency_0029523a._8_8_,7));
  acStack_6f[0] = s_tapjoySpendCurrency_0029523a[0];
  acStack_6f[1] = s_tapjoySpendCurrency_0029523a[1];
  acStack_6f[2] = s_tapjoySpendCurrency_0029523a[2];
  acStack_6f[3] = s_tapjoySpendCurrency_0029523a[3];
  acStack_6f[4] = s_tapjoySpendCurrency_0029523a[4];
  acStack_6f[5] = s_tapjoySpendCurrency_0029523a[5];
  acStack_6f[6] = s_tapjoySpendCurrency_0029523a[6];
  acStack_6f[7] = s_tapjoySpendCurrency_0029523a[7];
  local_90[1] = 0x28;
  local_90[2] = 0x49;
  local_90[3] = 0x29;
  local_90[4] = 0x56;
  local_90[5] = 0;
  local_78 = FUN_00566448(uVar3,&local_70,local_90,uVar2);
  if ((local_90[0] & 1) != 0) {
    operator_delete(local_80);
  }
  if ((local_70 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_5c,uStack_60));
  }
                    /* try { // try from 00ada754 to 00bda8bb has its CatchHandler @ 00ada754
                       catch() { ... } // from try @ 00ada754 with catch @ 00ada754
                       catch() { ... } // from try @ 00ada8ec with catch @ 00ada754
                       catch() { ... } // from try @ 00ada9dc with catch @ 00ada754 */
  uVar4 = FUN_0056626c(&local_78);
  if ((uVar4 & 1) == 0) goto LAB_00ada808;
  plVar5 = (long *)param_2[4];
  if (plVar5 == (long *)0x0) {
    local_50 = (byte *)0x0;
  }
  else if (plVar5 == param_2) {
    local_50 = &local_70;
    (**(code **)(*param_2 + 0x18))(param_2,&local_70);
  }
  else {
    local_50 = (byte *)(**(code **)(*plVar5 + 0x10))();
  }
  FUN_00adb7ac(&local_70,&DAT_0109fed0);
  if (local_50 == &local_70) {
    lVar7 = 0x20;
    pbVar6 = &local_70;
LAB_00ada7dc:
    (**(code **)(*(long *)pbVar6 + lVar7))();
  }
  else if (local_50 != (byte *)0x0) {
    lVar7 = 0x28;
    pbVar6 = local_50;
    goto LAB_00ada7dc;
  }
  FUN_00566284();
  uVar3 = FUN_00566978();
  if (local_78 != 0) {
    FUN_00551e14(uVar2,uVar3,local_78,param_1);
  }
LAB_00ada808:
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
