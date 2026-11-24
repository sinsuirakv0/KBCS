# 008daefc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008daea8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008daea8.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0029.md#compare-d63c7ac88469182a555812bbe73c1910)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0023.md#compare-16781a8ddb08bedfca050b880658aa0e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008daefc",
  "name": "FUN_008daefc",
  "size": 628,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85714ac848f44af08802d4f35383a538d8111db9ca8bd3468de05b9b9b86902b",
  "source_text_sha256": "85714ac848f44af08802d4f35383a538d8111db9ca8bd3468de05b9b9b86902b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459db4](../00459/00459db4.md)
- [00596f6c](../00596/00596f6c.md)
- [00865b4c](../00865/00865b4c.md)
- [008d615c](../008d6/008d615c.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 3826 bytes

~~~c

void FUN_008daefc(long param_1,undefined8 *param_2,ulong *param_3)

{
  long lVar1;
  int iVar2;
  int iVar3;
  undefined4 uVar4;
  long *plVar5;
  long lVar6;
  undefined4 *puVar7;
  ulong local_70;
  long *local_68;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 uStack_54;
  long *local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  puVar7 = *(undefined4 **)(param_1 + 0x10);
  *(undefined1 *)((long)puVar7 + 0x91) = 0;
  iVar2 = (*(code *)**(undefined8 **)*param_2)();
  iVar3 = (*(code *)**(undefined8 **)*param_2)((undefined8 *)*param_2);
  if (iVar2 == 0x199) {
    plVar5 = *(long **)(param_1 + 0x40);
    local_58 = 2;
    local_70 = CONCAT44(local_70._4_4_,iVar3);
joined_r0x008db0b0:
    if (plVar5 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
        FUN_00459db4();
      }
      goto LAB_008db1a0;
    }
    (**(code **)(*plVar5 + 0x30))(plVar5,&local_58,&local_70);
  }
  else {
    if (iVar3 != 200) {
      puVar7[1] = 0;
      puVar7[2] = 0;
      *(undefined1 *)(puVar7 + 0x1c) = 0;
      local_58 = 0;
      *(undefined8 *)(puVar7 + 6) = 0;
      *(undefined8 *)(puVar7 + 4) = 0;
      *(undefined8 *)(puVar7 + 10) = 0;
      *(undefined8 *)(puVar7 + 8) = 0;
      *(undefined8 *)(puVar7 + 0xe) = 0;
      *(undefined8 *)(puVar7 + 0xc) = 0;
      *(undefined8 *)(puVar7 + 0x12) = 0;
      *(undefined8 *)(puVar7 + 0x10) = 0;
      *(undefined8 *)(puVar7 + 0x16) = 0;
      *(undefined8 *)(puVar7 + 0x14) = 0;
      *(undefined8 *)(puVar7 + 0x1a) = 0;
      *(undefined8 *)(puVar7 + 0x18) = 0;
      FUN_00865b4c(&local_58);
      *(undefined1 *)(puVar7 + 0x24) = 0;
      *puVar7 = 0xffffffff;
      *(ulong *)(puVar7 + 0x1d) = CONCAT44(uStack_54,local_58);
      *(undefined1 *)(puVar7 + 0x1c) = 1;
      uVar4 = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_58 = 1;
      local_70 = CONCAT44(local_70._4_4_,uVar4);
      goto joined_r0x008db0b0;
    }
    local_70 = *param_3;
    local_68 = (long *)param_3[1];
    if (local_68 != (long *)0x0) {
      FUN_00c53d70(1,local_68 + 1);
    }
    FUN_00596f6c(&local_58,&local_70);
    plVar5 = local_68;
    if ((local_68 == (long *)0x0) ||
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,local_68 + 1), lVar6 != 0)) {
      if (CONCAT44(uStack_54,local_58) == 0) goto LAB_008db0e8;
LAB_008db004:
      FUN_008d615c(puVar7);
      puVar7[2] = 1;
      local_5c = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_70 = local_70 & 0xffffffff00000000;
      if (plVar5 == (long *)0x0) {
LAB_008db158:
        if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
          FUN_00459db4();
        }
        goto LAB_008db1a0;
      }
      (**(code **)(*plVar5 + 0x30))(plVar5,&local_70,&local_5c);
    }
    else {
      (**(code **)(*plVar5 + 0x10))(plVar5);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
      if (CONCAT44(uStack_54,local_58) != 0) goto LAB_008db004;
LAB_008db0e8:
      local_5c = (*(code *)**(undefined8 **)*param_2)();
      plVar5 = *(long **)(param_1 + 0x40);
      local_70 = CONCAT44(local_70._4_4_,1);
      if (plVar5 == (long *)0x0) goto LAB_008db158;
      (**(code **)(*plVar5 + 0x30))(plVar5,&local_70,&local_5c);
    }
    if ((local_50 != (long *)0x0) &&
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,local_50 + 1), lVar6 == 0)) {
      (**(code **)(*local_50 + 0x10))(local_50);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_50);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
LAB_008db1a0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
