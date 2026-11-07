# 00affdd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00affee4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00affdd8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d3145cffe383b7a23f41376e208be744de3e194e346fc6a32a87c702e31f662",
  "source_text_sha256": "4d3145cffe383b7a23f41376e208be744de3e194e346fc6a32a87c702e31f662"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード / UTF-8 8251 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE
               (long param_1,ulong *param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  ulong uVar8;
  undefined1 *local_70;
  undefined8 *local_68;
  long local_60;
  long lStack_58;
  code *local_50;
  long local_48;
  
                    /* catch() { ... } // from try @ 00af5a50 with catch @ 00affddc */
                    /* catch() { ... } // from try @ 00af5a2c with catch @ 00affde8 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af5a1c with catch @ 00affdf4 */
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5a10 with catch @ 00affdfc */
                    /* catch() { ... } // from try @ 00af5a04 with catch @ 00affe04 */
                    /* catch() { ... } // from try @ 00af59f8 with catch @ 00affe0c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af59ec with catch @ 00affe14 */
  uVar8 = *param_2;
                    /* catch() { ... } // from try @ 00af59e0 with catch @ 00affe1c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar6 = (long *)(param_1 + 0x38);
  plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af59d4 with catch @ 00affe24 */
  plVar4 = plVar6;
  if (plVar5 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af59c8 with catch @ 00affe2c */
                    /* catch() { ... } // from try @ 00af59bc with catch @ 00affe34 */
      if ((ulong)plVar5[4] >= uVar8) {
        plVar4 = plVar5;
      }
                    /* catch() { ... } // from try @ 00af59b0 with catch @ 00affe3c */
      plVar5 = (long *)plVar5[(ulong)plVar5[4] < uVar8];
    } while (plVar5 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af59a4 with catch @ 00affe44 */
                    /* catch() { ... } // from try @ 00af5998 with catch @ 00affe4c */
                    /* catch() { ... } // from try @ 00af598c with catch @ 00affe54 */
    if ((plVar4 != plVar6) && ((ulong)plVar4[4] <= uVar8)) {
      lVar7 = plVar4[5];
                    /* catch() { ... } // from try @ 00af592c with catch @ 00affe94 */
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5920 with catch @ 00affe9c */
      if (lVar7 == 0) goto LAB_00affe60;
      local_60 = *param_3;
      lStack_58 = param_3[1];
                    /* catch() { ... } // from try @ 00af5914 with catch @ 00affea4 */
      local_50 = (code *)param_3[2];
                    /* catch() { ... } // from try @ 00af5908 with catch @ 00affeac */
                    /* catch() { ... } // from try @ 00af58fc with catch @ 00affeb4 */
      plVar4 = *(long **)(lVar7 + 0x48);
                    /* catch() { ... } // from try @ 00af58f0 with catch @ 00affebc */
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58e4 with catch @ 00affec4 */
                    /* catch() { ... } // from try @ 00af58d8 with catch @ 00affecc */
                    /* catch() { ... } // from try @ 00af58cc with catch @ 00affed4 */
                    /* catch() { ... } // from try @ 00af58c0 with catch @ 00affedc */
      if ((((plVar4 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar4[4] == local_50))
      {
                    /* catch() { ... } // from try @ 00af58b4 with catch @ 00affee4 */
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00affef8:
          lVar2 = *plVar4;
                    /* catch() { ... } // from try @ 00af5828 with catch @ 00affefc */
          *(long *)(lVar2 + 8) = plVar4[1];
                    /* catch() { ... } // from try @ 00af581c with catch @ 00afff04 */
          *(long *)plVar4[1] = lVar2;
          _ZdlPv(plVar4);
        }
        else {
          local_70 = (undefined1 *)&local_70;
          local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af58a8 with catch @ 00affeec */
          (*local_50)(lStack_58);
          plVar4 = *(long **)(lVar7 + 0x48);
                    /* catch() { ... } // from try @ 00af589c with catch @ 00affef4 */
          if (plVar4 != (long *)0x0) goto LAB_00affef8;
        }
                    /* catch() { ... } // from try @ 00af5810 with catch @ 00afff0c */
        *(undefined8 *)(lVar7 + 0x48) = 0;
                    /* catch() { ... } // from try @ 00af5804 with catch @ 00afff14 */
        *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
      }
                    /* catch() { ... } // from try @ 00af5750 with catch @ 00afff1c */
      plVar5 = (long *)(lVar7 + 0x50);
      plVar4 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00af5724 with catch @ 00afff24 */
      if (plVar5 != plVar4) {
                    /* catch() { ... } // from try @ 00af56c0 with catch @ 00afff2c */
                    /* catch() { ... } // from try @ 00af5660 with catch @ 00afff34 */
        do {
                    /* catch() { ... } // from try @ 00afa874 with catch @ 00afff48
                       catch() { ... } // from try @ 00afa8e4 with catch @ 00afff48 */
          plVar6 = (long *)((long)plVar4 - *(long *)(lVar7 + 0x60));
                    /* catch() { ... } // from try @ 00afa83c with catch @ 00afff4c
                       catch() { ... } // from try @ 00afa8bc with catch @ 00afff4c */
                    /* catch() { ... } // from try @ 00af7398 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af6160 with catch @ 00afff54 */
          if (((plVar6[2] == local_60) && (plVar6[3] == lStack_58)) &&
             ((code *)plVar6[4] == local_50)) {
            lVar2 = *plVar4;
            *(long *)(lVar2 + 8) = plVar4[1];
            *(long *)plVar4[1] = lVar2;
            *plVar4 = (long)plVar4;
            plVar4[1] = (long)plVar4;
            if (plVar6 != (long *)0x0) {
              if (local_50 != (code *)0x0) {
                (*local_50)();
              }
              lVar2 = *plVar6;
                    /* catch() { ... } // from try @ 00af5d2c with catch @ 00afff94 */
              *(long *)(lVar2 + 8) = plVar6[1];
              *(long *)plVar6[1] = lVar2;
              _ZdlPv(plVar6);
              *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
            }
            break;
          }
                    /* catch() { ... } // from try @ 00afac7c with catch @ 00afff3c */
          plVar4 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00afaab0 with catch @ 00afff40 */
                    /* catch() { ... } // from try @ 00afa888 with catch @ 00afff44
                       catch() { ... } // from try @ 00afa8f8 with catch @ 00afff44 */
        } while (plVar5 != plVar4);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00affe60;
    }
  }
                    /* catch() { ... } // from try @ 00af5980 with catch @ 00affe5c */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
LAB_00affe60:
                    /* catch() { ... } // from try @ 00af5974 with catch @ 00affe64 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5968 with catch @ 00affe6c */
                    /* catch() { ... } // from try @ 00af595c with catch @ 00affe74 */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00af5950 with catch @ 00affe7c */
                    /* catch() { ... } // from try @ 00af5944 with catch @ 00affe84 */
                    /* catch() { ... } // from try @ 00af5938 with catch @ 00affe8c */
  return;
}

~~~
