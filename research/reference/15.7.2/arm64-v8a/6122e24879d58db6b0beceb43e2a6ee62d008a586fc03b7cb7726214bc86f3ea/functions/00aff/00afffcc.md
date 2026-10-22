# 00afffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afffcc.md)

## 関数情報

~~~json
{
  "address": "00afffcc",
  "name": "firebase::ReferenceCountedFutureImpl::AddCompletionCallbackLambda",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fc0145a60d022bfc3a87801fcab13b03dc7c485613225c37ac9ea7550d4c056",
  "source_text_sha256": "9fc0145a60d022bfc3a87801fcab13b03dc7c485613225c37ac9ea7550d4c056"
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

## 疑似コード 1/1 / UTF-8 5307 bytes

~~~c

/* firebase::ReferenceCountedFutureImpl::AddCompletionCallbackLambda(firebase::FutureHandle const&,
   std::__ndk1::function<void (firebase::FutureBase const&)>, bool) */

void firebase::ReferenceCountedFutureImpl::AddCompletionCallbackLambda
               (long *param_1_00,ReferenceCountedFutureImpl *param_1,FutureHandle *param_3,
               long *param_4,uint param_5)

{
  Mutex *this;
  undefined8 *puVar1;
  long *plVar2;
  void *pvVar3;
  undefined8 uVar4;
  int iVar5;
  long *plVar6;
  ReferenceCountedFutureImpl *pRVar7;
  long lVar8;
  ReferenceCountedFutureImpl *pRVar9;
  ReferenceCountedFutureImpl *pRVar10;
  ulong uVar11;
  int *piVar12;
  long lVar13;
  
                    /* catch() { ... } // from try @ 00af5d04 with catch @ 00afffd8 */
  plVar2 = operator_new(0x28);
  pvVar3 = operator_new(0x30);
  plVar6 = (long *)param_4[4];
  if (plVar6 == (long *)0x0) {
    *(undefined8 *)((long)pvVar3 + 0x20) = 0;
  }
  else {
                    /* catch() { ... } // from try @ 00af5a38 with catch @ 00b0001c */
    if (param_4 == plVar6) {
      *(void **)((long)pvVar3 + 0x20) = pvVar3;
      (**(code **)(*plVar6 + 0x18))(plVar6,pvVar3);
    }
    else {
      uVar4 = (**(code **)(*plVar6 + 0x10))(plVar6);
      *(undefined8 *)((long)pvVar3 + 0x20) = uVar4;
    }
  }
                    /* catch() { ... } // from try @ 00af60f0 with catch @ 00b00060 */
  plVar2[2] = (long)FUN_00b001dc;
  plVar2[3] = (long)pvVar3;
  this = (Mutex *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00af5b5c with catch @ 00b00070 */
  *plVar2 = (long)plVar2;
  plVar2[1] = (long)plVar2;
  plVar2[4] = (long)FUN_00b00214;
  Mutex::Acquire(this);
  uVar11 = *(ulong *)param_3;
  Mutex::Acquire(this);
  pRVar9 = param_1 + 0x38;
  pRVar10 = *(ReferenceCountedFutureImpl **)pRVar9;
  pRVar7 = pRVar9;
  if (pRVar10 == (ReferenceCountedFutureImpl *)0x0) {
LAB_00b000c8:
    Mutex::Release(this);
  }
  else {
    do {
      if (*(ulong *)(pRVar10 + 0x20) >= uVar11) {
        pRVar7 = pRVar10;
      }
      pRVar10 = *(ReferenceCountedFutureImpl **)
                 (pRVar10 + (ulong)(*(ulong *)(pRVar10 + 0x20) < uVar11) * 8);
    } while (pRVar10 != (ReferenceCountedFutureImpl *)0x0);
                    /* catch() { ... } // from try @ 00af5730 with catch @ 00b000b4 */
    if ((pRVar7 == pRVar9) || (uVar11 < *(ulong *)(pRVar7 + 0x20))) goto LAB_00b000c8;
    piVar12 = *(int **)(pRVar7 + 0x28);
    Mutex::Release(this);
    if (piVar12 != (int *)0x0) {
      if ((param_5 & 1) == 0) {
        puVar1 = *(undefined8 **)(piVar12 + 0x16);
                    /* catch() { ... } // from try @ 00af566c with catch @ 00b0017c */
        plVar6 = (long *)((long)plVar2 + *(long *)(piVar12 + 0x18));
        piVar12[8] = piVar12[8] + 1;
        *puVar1 = plVar6;
        *plVar6 = (long)(piVar12 + 0x14);
        plVar6[1] = (long)puVar1;
        *(long **)(piVar12 + 0x16) = plVar6;
        iVar5 = *piVar12;
      }
      else {
        plVar6 = *(long **)(piVar12 + 0x12);
        if (plVar6 == (long *)0x0) {
          iVar5 = piVar12[8];
        }
        else {
          if ((code *)plVar6[4] == (code *)0x0) {
LAB_00b00144:
            lVar8 = *plVar6;
            *(long *)(lVar8 + 8) = plVar6[1];
                    /* catch() { ... } // from try @ 00af56cc with catch @ 00b0014c */
            *(long *)plVar6[1] = lVar8;
            operator_delete(plVar6);
          }
          else {
            (*(code *)plVar6[4])(plVar6[3]);
                    /* catch() { ... } // from try @ 00afd330 with catch @ 00b0013c */
            plVar6 = *(long **)(piVar12 + 0x12);
            if (plVar6 != (long *)0x0) goto LAB_00b00144;
          }
          piVar12[0x12] = 0;
          piVar12[0x13] = 0;
          iVar5 = piVar12[8] + -1;
          piVar12[8] = iVar5;
        }
        piVar12[8] = iVar5 + 1;
        *(long **)(piVar12 + 0x12) = plVar2;
        iVar5 = *piVar12;
      }
      if (iVar5 != 0) {
        Mutex::Release(this);
        lVar13 = plVar2[2];
        lVar8 = plVar2[4];
        param_1_00[1] = plVar2[3];
        *param_1_00 = lVar13;
                    /* catch() { ... } // from try @ 00af575c with catch @ 00b001ac */
        param_1_00[2] = lVar8;
        return;
      }
                    /* catch() { ... } // from try @ 00afb528 with catch @ 00b001d4 */
      ReleaseMutexAndRunCallbacks(param_1,param_3);
      goto LAB_00b000f0;
    }
  }
  Mutex::Release(this);
  lVar8 = *plVar2;
  *(long *)(lVar8 + 8) = plVar2[1];
                    /* catch() { ... } // from try @ 00afd224 with catch @ 00b000e4 */
                    /* catch() { ... } // from try @ 00afba5c with catch @ 00b000e8 */
  *(long *)plVar2[1] = lVar8;
                    /* catch() { ... } // from try @ 00afb594 with catch @ 00b000ec */
  operator_delete(plVar2);
LAB_00b000f0:
                    /* catch() { ... } // from try @ 00afa7f8 with catch @ 00b000f0 */
  *param_1_00 = 0;
  param_1_00[1] = 0;
                    /* catch() { ... } // from try @ 00af8d44 with catch @ 00b000f4 */
  param_1_00[2] = 0;
                    /* catch() { ... } // from try @ 00af5a6c with catch @ 00b000f8 */
  return;
}

~~~
