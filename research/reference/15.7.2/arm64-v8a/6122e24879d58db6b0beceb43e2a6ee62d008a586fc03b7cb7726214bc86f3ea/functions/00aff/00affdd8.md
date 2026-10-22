# 00affdd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00affdd8.md)

## 関数情報

~~~json
{
  "address": "00affdd8",
  "name": "firebase::ReferenceCountedFutureImpl::RemoveCompletionCallback",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d3ff9c9ea379a16315e96804046c6cdcc8c44d15b1e0acc56baa413c6055159",
  "source_text_sha256": "5d3ff9c9ea379a16315e96804046c6cdcc8c44d15b1e0acc56baa413c6055159"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード 1/1 / UTF-8 8729 bytes

~~~c

/* firebase::ReferenceCountedFutureImpl::RemoveCompletionCallback(firebase::FutureHandle const&,
   firebase::detail::CompletionCallbackHandle) */

void __thiscall
firebase::ReferenceCountedFutureImpl::RemoveCompletionCallback
          (ReferenceCountedFutureImpl *this,ulong *param_1,long *param_3)

{
  Mutex *this_00;
  long lVar1;
  long lVar2;
  long *plVar3;
  ReferenceCountedFutureImpl *pRVar4;
  ReferenceCountedFutureImpl *pRVar5;
  long *plVar6;
  long *plVar7;
  long lVar8;
  ulong uVar9;
  undefined1 *local_70;
  undefined8 *local_68;
  long local_60;
  long lStack_58;
  code *local_50;
  long local_48;
  
                    /* catch() { ... } // from try @ 00af5a50 with catch @ 00affddc */
                    /* catch() { ... } // from try @ 00af5a2c with catch @ 00affde8 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af5a1c with catch @ 00affdf4 */
  local_48 = *(long *)(lVar2 + 0x28);
  this_00 = (Mutex *)(this + 8);
                    /* catch() { ... } // from try @ 00af5a10 with catch @ 00affdfc */
                    /* catch() { ... } // from try @ 00af5a04 with catch @ 00affe04 */
                    /* catch() { ... } // from try @ 00af59f8 with catch @ 00affe0c */
  Mutex::Acquire(this_00);
                    /* catch() { ... } // from try @ 00af59ec with catch @ 00affe14 */
  uVar9 = *param_1;
                    /* catch() { ... } // from try @ 00af59e0 with catch @ 00affe1c */
  Mutex::Acquire(this_00);
  this = this + 0x38;
  pRVar5 = *(ReferenceCountedFutureImpl **)this;
                    /* catch() { ... } // from try @ 00af59d4 with catch @ 00affe24 */
  pRVar4 = this;
  if (pRVar5 != (ReferenceCountedFutureImpl *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af59c8 with catch @ 00affe2c */
                    /* catch() { ... } // from try @ 00af59bc with catch @ 00affe34 */
      if (*(ulong *)(pRVar5 + 0x20) >= uVar9) {
        pRVar4 = pRVar5;
      }
                    /* catch() { ... } // from try @ 00af59b0 with catch @ 00affe3c */
      pRVar5 = *(ReferenceCountedFutureImpl **)
                (pRVar5 + (ulong)(*(ulong *)(pRVar5 + 0x20) < uVar9) * 8);
    } while (pRVar5 != (ReferenceCountedFutureImpl *)0x0);
                    /* catch() { ... } // from try @ 00af59a4 with catch @ 00affe44 */
                    /* catch() { ... } // from try @ 00af5998 with catch @ 00affe4c */
                    /* catch() { ... } // from try @ 00af598c with catch @ 00affe54 */
    if ((pRVar4 != this) && (*(ulong *)(pRVar4 + 0x20) <= uVar9)) {
      lVar8 = *(long *)(pRVar4 + 0x28);
                    /* catch() { ... } // from try @ 00af592c with catch @ 00affe94 */
      Mutex::Release(this_00);
                    /* catch() { ... } // from try @ 00af5920 with catch @ 00affe9c */
      if (lVar8 == 0) goto LAB_00affe60;
      local_60 = *param_3;
      lStack_58 = param_3[1];
                    /* catch() { ... } // from try @ 00af5914 with catch @ 00affea4 */
      local_50 = (code *)param_3[2];
                    /* catch() { ... } // from try @ 00af5908 with catch @ 00affeac */
                    /* catch() { ... } // from try @ 00af58fc with catch @ 00affeb4 */
      plVar3 = *(long **)(lVar8 + 0x48);
                    /* catch() { ... } // from try @ 00af58f0 with catch @ 00affebc */
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58e4 with catch @ 00affec4 */
                    /* catch() { ... } // from try @ 00af58d8 with catch @ 00affecc */
                    /* catch() { ... } // from try @ 00af58cc with catch @ 00affed4 */
                    /* catch() { ... } // from try @ 00af58c0 with catch @ 00affedc */
      if ((((plVar3 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar3[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar3[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar3[4] == local_50))
      {
                    /* catch() { ... } // from try @ 00af58b4 with catch @ 00affee4 */
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00affef8:
          lVar1 = *plVar3;
                    /* catch() { ... } // from try @ 00af5828 with catch @ 00affefc */
          *(long *)(lVar1 + 8) = plVar3[1];
                    /* catch() { ... } // from try @ 00af581c with catch @ 00afff04 */
          *(long *)plVar3[1] = lVar1;
          operator_delete(plVar3);
        }
        else {
          local_70 = (undefined1 *)&local_70;
          local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58a8 with catch @ 00affeec */
          (*local_50)(lStack_58);
          plVar3 = *(long **)(lVar8 + 0x48);
                    /* catch() { ... } // from try @ 00af589c with catch @ 00affef4 */
          if (plVar3 != (long *)0x0) goto LAB_00affef8;
        }
                    /* catch() { ... } // from try @ 00af5810 with catch @ 00afff0c */
        *(undefined8 *)(lVar8 + 0x48) = 0;
                    /* catch() { ... } // from try @ 00af5804 with catch @ 00afff14 */
        *(int *)(lVar8 + 0x20) = *(int *)(lVar8 + 0x20) + -1;
      }
                    /* catch() { ... } // from try @ 00af5750 with catch @ 00afff1c */
      plVar6 = (long *)(lVar8 + 0x50);
      plVar3 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af5724 with catch @ 00afff24 */
      if (plVar6 != plVar3) {
                    /* catch() { ... } // from try @ 00af56c0 with catch @ 00afff2c */
                    /* catch() { ... } // from try @ 00af5660 with catch @ 00afff34 */
        do {
                    /* catch() { ... } // from try @ 00afa874 with catch @ 00afff48
                       catch() { ... } // from try @ 00afa8e4 with catch @ 00afff48 */
          plVar7 = (long *)((long)plVar3 - *(long *)(lVar8 + 0x60));
                    /* catch() { ... } // from try @ 00afa83c with catch @ 00afff4c
                       catch() { ... } // from try @ 00afa8bc with catch @ 00afff4c */
                    /* catch() { ... } // from try @ 00af7398 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af6160 with catch @ 00afff54 */
          if (((plVar7[2] == local_60) && (plVar7[3] == lStack_58)) &&
             ((code *)plVar7[4] == local_50)) {
            lVar1 = *plVar3;
            *(long *)(lVar1 + 8) = plVar3[1];
            *(long *)plVar3[1] = lVar1;
            *plVar3 = (long)plVar3;
            plVar3[1] = (long)plVar3;
            if (plVar7 != (long *)0x0) {
              if (local_50 != (code *)0x0) {
                (*local_50)();
              }
              lVar1 = *plVar7;
                    /* catch() { ... } // from try @ 00af5d2c with catch @ 00afff94 */
              *(long *)(lVar1 + 8) = plVar7[1];
              *(long *)plVar7[1] = lVar1;
              operator_delete(plVar7);
              *(int *)(lVar8 + 0x20) = *(int *)(lVar8 + 0x20) + -1;
            }
            break;
          }
                    /* catch() { ... } // from try @ 00afac7c with catch @ 00afff3c */
          plVar3 = (long *)*plVar3;
                    /* catch() { ... } // from try @ 00afaab0 with catch @ 00afff40 */
                    /* catch() { ... } // from try @ 00afa888 with catch @ 00afff44
                       catch() { ... } // from try @ 00afa8f8 with catch @ 00afff44 */
        } while (plVar6 != plVar3);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00affe60;
    }
  }
                    /* catch() { ... } // from try @ 00af5980 with catch @ 00affe5c */
  Mutex::Release(this_00);
LAB_00affe60:
                    /* catch() { ... } // from try @ 00af5974 with catch @ 00affe64 */
  Mutex::Release(this_00);
                    /* catch() { ... } // from try @ 00af5968 with catch @ 00affe6c */
                    /* catch() { ... } // from try @ 00af595c with catch @ 00affe74 */
  if (*(long *)(lVar2 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00af5950 with catch @ 00affe7c */
                    /* catch() { ... } // from try @ 00af5944 with catch @ 00affe84 */
                    /* catch() { ... } // from try @ 00af5938 with catch @ 00affe8c */
  return;
}

~~~
