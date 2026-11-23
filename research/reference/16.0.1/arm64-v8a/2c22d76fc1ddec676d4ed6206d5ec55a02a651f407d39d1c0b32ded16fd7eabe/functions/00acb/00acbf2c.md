# 00acbf2c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbd30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd30.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0035.md#compare-e046a5cf660bb26f513d9a8e88783459)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0035.md#compare-7d57a8ede36054e241b968350c8b1402)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbf2c",
  "name": "FUN_00acbf2c",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "584d98049768cd3e608ed0ef0eb70492bc41d2b7b1fcb4a95c53468c533cabf4",
  "source_text_sha256": "584d98049768cd3e608ed0ef0eb70492bc41d2b7b1fcb4a95c53468c533cabf4"
}
~~~

## 呼び出し元

- [009b96e4](../009b9/009b96e4.md)
- [00acbf2c](../00acb/00acbf2c.md)

## 呼び出し先

- [00acbf2c](../00acb/00acbf2c.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 951 bytes

~~~c

void FUN_00acbf2c(long param_1,byte param_2)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  
  lVar5 = tpidr_el0;
  lVar7 = *(long *)(lVar5 + 0x28);
  puVar1 = *(undefined8 **)(param_1 + 0x40);
  puVar3 = *(undefined8 **)(param_1 + 0x48);
  *(byte *)(param_1 + 0x28) = param_2;
  for (; puVar1 != puVar3; puVar1 = puVar1 + 2) {
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c53cd0(1,plVar4 + 1);
    }
    FUN_00acbf2c(uVar2,param_2 & 1);
    if ((plVar4 != (long *)0x0) && (lVar6 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
  }
  if (*(long *)(lVar5 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
