# 00ada5ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ada4e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada4e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0057.md#compare-9c31b2e250ba322196b7a927bdbf9774)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ada5ac",
  "name": "FUN_00ada5ac",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63c02477a73bfe31d139b138e323c4fa4fdfb1c16f29d87e8b2593199a804120",
  "source_text_sha256": "63c02477a73bfe31d139b138e323c4fa4fdfb1c16f29d87e8b2593199a804120"
}
~~~

## 呼び出し元

- [0085e130](../0085e/0085e130.md)
- [0085fc1c](../0085f/0085fc1c.md)
- [008710cc](../00871/008710cc.md)
- [00879ea8](../00879/00879ea8.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00adb874](../00adb/00adb874.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"tapjoyGetCurrencyBalance"
~~~

## 疑似コード / UTF-8 2143 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ada5ac(long *param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  long *plVar7;
  ulong *puVar8;
  undefined8 uVar9;
  long lVar10;
  byte local_90 [16];
  void *local_80;
  long local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  ulong *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar4 = FUN_00565f94();
  uVar5 = FUN_00566284();
  local_60 = (char *)_Znwm(0x20);
  uVar3 = s_tapjoyGetCurrencyBalance_00294121._16_8_;
  uVar2 = s_tapjoyGetCurrencyBalance_00294121._8_8_;
  uVar9 = s_tapjoyGetCurrencyBalance_00294121._0_8_;
  local_60[0x18] = '\0';
  *(undefined8 *)(local_60 + 0x10) = uVar3;
  *(undefined8 *)(local_60 + 8) = uVar2;
  *(undefined8 *)local_60 = uVar9;
  local_90[0] = 6;
  uStack_68 = _UNK_002b0c68;
  local_70 = _DAT_002b0c60;
  local_90[1] = 0x28;
  local_90[2] = 0x29;
  local_90[3] = 0x56;
  local_90[4] = 0;
  local_78 = FUN_00566448(uVar5,&local_70,local_90,uVar4);
  if ((local_90[0] & 1) != 0) {
    _ZdlPv(local_80);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  uVar6 = FUN_0056626c(&local_78);
  if ((uVar6 & 1) == 0) goto LAB_00ada710;
  plVar7 = (long *)param_1[4];
  if (plVar7 == (long *)0x0) {
    local_50 = (ulong *)0x0;
  }
  else if (plVar7 == param_1) {
    local_50 = &local_70;
    (**(code **)(*param_1 + 0x18))(param_1,&local_70);
  }
  else {
    local_50 = (ulong *)(**(code **)(*plVar7 + 0x10))();
  }
  FUN_00adb874(&local_70,&DAT_0109ff60);
  if (local_50 == &local_70) {
    lVar10 = 0x20;
    puVar8 = &local_70;
LAB_00ada6e8:
    (**(code **)(*puVar8 + lVar10))();
  }
  else if (local_50 != (ulong *)0x0) {
    lVar10 = 0x28;
    puVar8 = local_50;
    goto LAB_00ada6e8;
  }
  FUN_00566284();
  uVar9 = FUN_00566978();
  if (local_78 != 0) {
    FUN_00551e14(uVar4,uVar9);
  }
LAB_00ada710:
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
