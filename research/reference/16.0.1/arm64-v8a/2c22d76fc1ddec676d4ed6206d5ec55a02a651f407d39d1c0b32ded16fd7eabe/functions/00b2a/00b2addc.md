# 00b2addc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2a9b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a9b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0037.md#compare-261f3a078a291aa438aaeaf58ddce345)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0038.md#compare-c0754a2be9b35a614cd559b2af860bd0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2addc",
  "name": "FUN_00b2addc",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "504eb618cec28585a19c58aeacc12d214216529572e51bb7ec42d28249f2521d",
  "source_text_sha256": "504eb618cec28585a19c58aeacc12d214216529572e51bb7ec42d28249f2521d"
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [005e8198](../005e8/005e8198.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1743 bytes

~~~c

long * FUN_00b2addc(long *param_1,int *param_2,undefined8 param_3,undefined8 *param_4)

{
  undefined4 uVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  lVar2 = tpidr_el0;
  lVar6 = *(long *)(lVar2 + 0x28);
  plVar7 = param_1 + 1;
  plVar8 = plVar7;
  if ((long *)*plVar7 != (long *)0x0) {
    plVar3 = (long *)*plVar7;
    do {
      while (plVar4 = plVar3, plVar7 = plVar4, (int)plVar4[4] <= *param_2) {
        if (*param_2 <= (int)plVar4[4]) {
          uVar5 = 0;
          goto LAB_00b2aef0;
        }
        plVar3 = (long *)plVar4[1];
        if ((long *)plVar4[1] == (long *)0x0) {
          plVar8 = plVar4 + 1;
          goto LAB_00b2ae58;
        }
      }
      plVar3 = (long *)*plVar4;
      plVar8 = plVar4;
    } while ((long *)*plVar4 != (long *)0x0);
  }
LAB_00b2ae58:
  plVar4 = (long *)_Znwm(0x60);
  uVar1 = *(undefined4 *)*param_4;
  plVar4[0xb] = 0;
  *(undefined4 *)(plVar4 + 4) = uVar1;
  plVar4[10] = 0;
  plVar4[9] = 0;
  plVar4[8] = 0;
  plVar4[7] = 0;
  plVar4[6] = 0;
  plVar4[5] = 0;
  FUN_005e8198((long)plVar4 + 0x2c);
  *(undefined4 *)((long)plVar4 + 0x34) = 0;
  FUN_005e8198();
  plVar4[8] = 0;
  plVar4[9] = 0;
  plVar4[10] = 0;
  *plVar4 = 0;
  plVar4[1] = 0;
  plVar4[2] = (long)plVar7;
  *plVar8 = (long)plVar4;
  plVar7 = plVar4;
  if (*(long *)*param_1 != 0) {
    *param_1 = *(long *)*param_1;
    plVar7 = (long *)*plVar8;
  }
  plVar7 = (long *)FUN_0043bba4(param_1[1],plVar7);
  uVar5 = 1;
  param_1[2] = param_1[2] + 1;
  param_1 = plVar7;
LAB_00b2aef0:
  if (*(long *)(lVar2 + 0x28) == lVar6) {
    return plVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(param_1,uVar5);
}

~~~
