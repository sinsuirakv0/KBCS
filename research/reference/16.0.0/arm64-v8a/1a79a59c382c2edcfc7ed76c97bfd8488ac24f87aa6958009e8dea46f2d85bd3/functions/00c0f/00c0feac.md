# 00c0feac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b93464`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0073.md#compare-654041a77067543893d4136c6fc777bf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0feac",
  "name": "_ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20efaef8f39cd423b30662954889cb1028ca9b581d15a870efddf0bb30b06de9",
  "source_text_sha256": "20efaef8f39cd423b30662954889cb1028ca9b581d15a870efddf0bb30b06de9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c05b30](../00c05/00c05b30.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c5dae0](../00c5d/00c5dae0.md)

## 疑似コード / UTF-8 3048 bytes

~~~c

long * _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb
                 (long *param_1,long *param_2,long param_3,undefined8 param_4,ulong param_5)

{
  long lVar1;
  ulong uVar2;
  int *piVar3;
  undefined *puVar4;
  bool bVar5;
  int iVar6;
  long *plVar7;
  int *piVar8;
  ulong uVar9;
  ulong uVar10;
  int *piVar11;
  undefined **local_60;
  ulong local_58;
  int *piStack_50;
  long local_48;
  undefined *local_40;
  undefined1 *local_38;
  
  if ((*(byte *)(param_3 + 8) & 1) == 0) {
                    /* WARNING: Could not recover jumptable at 0x00c0fef8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    plVar7 = (long *)(**(code **)(*param_1 + 0x30))(param_1,param_2,param_3,param_4,param_5 & 1);
    return plVar7;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(&local_48,param_3);
  puVar4 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8;
  local_40 = PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8;
  if (*(long *)PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8 != -1) {
    local_60 = &local_40;
    local_38 = (undefined1 *)&local_60;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk18numpunctIwE2idE_00c9b7c8,&local_38,FUN_00c35b90);
  }
  if (((long)*(int *)(puVar4 + 8) - 1U <
       (ulong)(*(long *)(local_48 + 0x18) - *(long *)(local_48 + 0x10) >> 3)) &&
     (plVar7 = *(long **)(*(long *)(local_48 + 0x10) + ((long)*(int *)(puVar4 + 8) - 1U) * 8),
     plVar7 != (long *)0x0)) {
    _ZNSt6__ndk16localeD1Ev(&local_48);
    lVar1 = 0x30;
    if ((param_5 & 1) == 0) {
      lVar1 = 0x38;
    }
    (**(code **)(*plVar7 + lVar1))(&local_60,plVar7);
    uVar9 = (ulong)local_60 & 0xff;
    bVar5 = ((ulong)local_60 & 1) != 0;
    uVar10 = (ulong)local_60 >> 1 & 0x7f;
    if (bVar5) {
      uVar10 = local_58;
    }
    piVar8 = piStack_50;
    if (uVar10 != 0) {
      uVar10 = local_58;
      plVar7 = param_2;
      piVar11 = (int *)((ulong)&local_60 | 4);
      if (bVar5) {
        piVar11 = piStack_50;
      }
      do {
        param_2 = plVar7;
        if (plVar7 != (long *)0x0) {
          piVar8 = (int *)plVar7[6];
          iVar6 = *piVar11;
          if (piVar8 == (int *)plVar7[7]) {
            iVar6 = (**(code **)(*plVar7 + 0x68))(plVar7);
          }
          else {
            *piVar8 = iVar6;
            plVar7[6] = (long)(piVar8 + 1);
          }
          uVar9 = (ulong)local_60 & 0xff;
          piVar8 = piStack_50;
          uVar10 = local_58;
          param_2 = (long *)0x0;
          if (iVar6 != -1) {
            param_2 = plVar7;
          }
        }
        piVar11 = piVar11 + 1;
        uVar2 = uVar9 >> 1;
        piVar3 = (int *)((ulong)&local_60 | 4);
        if ((uVar9 & 1) != 0) {
          uVar2 = uVar10;
          piVar3 = piVar8;
        }
        plVar7 = param_2;
      } while (piVar11 != piVar3 + uVar2);
    }
    if ((uVar9 & 1) != 0) {
      _ZdlPv(piVar8);
    }
    return param_2;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05b30();
}

~~~
