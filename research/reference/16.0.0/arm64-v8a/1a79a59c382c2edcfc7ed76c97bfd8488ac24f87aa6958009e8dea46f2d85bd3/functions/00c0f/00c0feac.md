# 00c0feac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
