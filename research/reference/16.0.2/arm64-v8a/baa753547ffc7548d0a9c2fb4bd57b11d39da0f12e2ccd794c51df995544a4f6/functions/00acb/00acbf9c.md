# 00acbf9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbf2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbf2c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0034.md#compare-7d57a8ede36054e241b968350c8b1402)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0028.md#compare-a2a52cd015f1e0588551a4c9e355fbff)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbf9c",
  "name": "FUN_00acbf9c",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f43dd37e86b4a452d43f3ff02fe8eced714140f4bc65b3a049f43b34c1242ed",
  "source_text_sha256": "0f43dd37e86b4a452d43f3ff02fe8eced714140f4bc65b3a049f43b34c1242ed"
}
~~~

## 呼び出し元

- [009b9738](../009b9/009b9738.md)
- [00acbf9c](../00acb/00acbf9c.md)

## 呼び出し先

- [00acbf9c](../00acb/00acbf9c.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 951 bytes

~~~c

void FUN_00acbf9c(long param_1,byte param_2)

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
      FUN_00c53d70(1,plVar4 + 1);
    }
    FUN_00acbf9c(uVar2,param_2 & 1);
    if ((plVar4 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)
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
