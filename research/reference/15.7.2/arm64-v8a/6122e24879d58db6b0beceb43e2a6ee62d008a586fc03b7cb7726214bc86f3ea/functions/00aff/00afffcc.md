# 00afffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00afffcc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "746b748ed254e012116856fbe5849263c3db6c24d568d68ab2f8648a82481a72",
  "source_text_sha256": "746b748ed254e012116856fbe5849263c3db6c24d568d68ab2f8648a82481a72"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddf10](../00bdd/00bddf10.md)

## 疑似コード / UTF-8 4774 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb
               (long *param_1,long param_2,ulong *param_3,long *param_4,uint param_5)

{
  undefined8 *puVar1;
  long *__ptr;
  long lVar2;
  undefined8 uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  ulong uVar8;
  int *piVar9;
  long lVar10;
  
                    /* catch() { ... } // from try @ 00af5d04 with catch @ 00afffd8 */
  __ptr = (long *)_Znwm(0x28);
  lVar2 = _Znwm(0x30);
  plVar5 = (long *)param_4[4];
  if (plVar5 == (long *)0x0) {
    *(undefined8 *)(lVar2 + 0x20) = 0;
  }
  else {
                    /* catch() { ... } // from try @ 00af5a38 with catch @ 00b0001c */
    if (param_4 == plVar5) {
      *(long *)(lVar2 + 0x20) = lVar2;
      (**(code **)(*plVar5 + 0x18))(plVar5,lVar2);
    }
    else {
      uVar3 = (**(code **)(*plVar5 + 0x10))(plVar5);
      *(undefined8 *)(lVar2 + 0x20) = uVar3;
    }
  }
                    /* catch() { ... } // from try @ 00af60f0 with catch @ 00b00060 */
  __ptr[2] = (long)FUN_00b001dc;
  __ptr[3] = lVar2;
  lVar2 = param_2 + 8;
                    /* catch() { ... } // from try @ 00af5b5c with catch @ 00b00070 */
  *__ptr = (long)__ptr;
  __ptr[1] = (long)__ptr;
  __ptr[4] = (long)FUN_00b00214;
  _ZN8firebase5Mutex7AcquireEv(lVar2);
  uVar8 = *param_3;
  _ZN8firebase5Mutex7AcquireEv(lVar2);
  plVar6 = (long *)(param_2 + 0x38);
  plVar7 = (long *)*plVar6;
  plVar5 = plVar6;
  if (plVar7 == (long *)0x0) {
LAB_00b000c8:
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
  }
  else {
    do {
      if ((ulong)plVar7[4] >= uVar8) {
        plVar5 = plVar7;
      }
      plVar7 = (long *)plVar7[(ulong)plVar7[4] < uVar8];
    } while (plVar7 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5730 with catch @ 00b000b4 */
    if ((plVar5 == plVar6) || (uVar8 < (ulong)plVar5[4])) goto LAB_00b000c8;
    piVar9 = (int *)plVar5[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
    if (piVar9 != (int *)0x0) {
      if ((param_5 & 1) == 0) {
        puVar1 = *(undefined8 **)(piVar9 + 0x16);
                    /* catch() { ... } // from try @ 00af566c with catch @ 00b0017c */
        plVar5 = (long *)((long)__ptr + *(long *)(piVar9 + 0x18));
        piVar9[8] = piVar9[8] + 1;
        *puVar1 = plVar5;
        *plVar5 = (long)(piVar9 + 0x14);
        plVar5[1] = (long)puVar1;
        *(long **)(piVar9 + 0x16) = plVar5;
        iVar4 = *piVar9;
      }
      else {
        plVar5 = *(long **)(piVar9 + 0x12);
        if (plVar5 == (long *)0x0) {
          iVar4 = piVar9[8];
        }
        else {
          if ((code *)plVar5[4] == (code *)0x0) {
LAB_00b00144:
            lVar10 = *plVar5;
            *(long *)(lVar10 + 8) = plVar5[1];
                    /* catch() { ... } // from try @ 00af56cc with catch @ 00b0014c */
            *(long *)plVar5[1] = lVar10;
            _ZdlPv(plVar5);
          }
          else {
            (*(code *)plVar5[4])(plVar5[3]);
                    /* catch() { ... } // from try @ 00afd330 with catch @ 00b0013c */
            plVar5 = *(long **)(piVar9 + 0x12);
            if (plVar5 != (long *)0x0) goto LAB_00b00144;
          }
          piVar9[0x12] = 0;
          piVar9[0x13] = 0;
          iVar4 = piVar9[8] + -1;
          piVar9[8] = iVar4;
        }
        piVar9[8] = iVar4 + 1;
        *(long **)(piVar9 + 0x12) = __ptr;
        iVar4 = *piVar9;
      }
      if (iVar4 != 0) {
        _ZN8firebase5Mutex7ReleaseEv(lVar2);
        lVar10 = __ptr[2];
        lVar2 = __ptr[4];
        param_1[1] = __ptr[3];
        *param_1 = lVar10;
                    /* catch() { ... } // from try @ 00af575c with catch @ 00b001ac */
        param_1[2] = lVar2;
        return;
      }
                    /* catch() { ... } // from try @ 00afb528 with catch @ 00b001d4 */
      _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
                (param_2,param_3);
      goto LAB_00b000f0;
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar2);
  lVar2 = *__ptr;
  *(long *)(lVar2 + 8) = __ptr[1];
                    /* catch() { ... } // from try @ 00afd224 with catch @ 00b000e4 */
                    /* catch() { ... } // from try @ 00afba5c with catch @ 00b000e8 */
  *(long *)__ptr[1] = lVar2;
                    /* catch() { ... } // from try @ 00afb594 with catch @ 00b000ec */
  _ZdlPv(__ptr);
LAB_00b000f0:
                    /* catch() { ... } // from try @ 00afa7f8 with catch @ 00b000f0 */
  *param_1 = 0;
  param_1[1] = 0;
                    /* catch() { ... } // from try @ 00af8d44 with catch @ 00b000f4 */
  param_1[2] = 0;
                    /* catch() { ... } // from try @ 00af5a6c with catch @ 00b000f8 */
  return;
}

~~~
