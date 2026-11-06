# 00affee4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00affee4.md)

## 関数情報

~~~json
{
  "address": "00affee4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b80094f26639ed2b8dfa719ee08010211de3de40361d3b38c4c86b49a805d1bf",
  "source_text_sha256": "b80094f26639ed2b8dfa719ee08010211de3de40361d3b38c4c86b49a805d1bf"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

## 疑似コード 1/1 / UTF-8 6511 bytes

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
  
                    /* catch() { ... } // from try @ 00af5958 with catch @ 00affee8 */
                    /* catch() { ... } // from try @ 00af594c with catch @ 00affef0 */
                    /* catch() { ... } // from try @ 00af5940 with catch @ 00affef8 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00af5934 with catch @ 00afff00 */
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5928 with catch @ 00afff08 */
                    /* catch() { ... } // from try @ 00af591c with catch @ 00afff10 */
                    /* catch() { ... } // from try @ 00af5910 with catch @ 00afff18 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af5904 with catch @ 00afff20 */
  uVar8 = *param_2;
                    /* catch() { ... } // from try @ 00af58f8 with catch @ 00afff28 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar6 = (long *)(param_1 + 0x38);
  plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00af58ec with catch @ 00afff30 */
  plVar4 = plVar6;
  if (plVar5 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af58e0 with catch @ 00afff38 */
                    /* catch() { ... } // from try @ 00af586c with catch @ 00afff40 */
      if ((ulong)plVar5[4] >= uVar8) {
        plVar4 = plVar5;
      }
                    /* catch() { ... } // from try @ 00af5860 with catch @ 00afff48 */
      plVar5 = (long *)plVar5[(ulong)plVar5[4] < uVar8];
    } while (plVar5 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5854 with catch @ 00afff50 */
                    /* catch() { ... } // from try @ 00af5848 with catch @ 00afff58 */
                    /* catch() { ... } // from try @ 00af5794 with catch @ 00afff60 */
    if ((plVar4 != plVar6) && ((ulong)plVar4[4] <= uVar8)) {
      lVar7 = plVar4[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      if (lVar7 == 0) goto LAB_00afff6c;
      local_60 = *param_3;
      lStack_58 = param_3[1];
      local_50 = (code *)param_3[2];
      plVar4 = *(long **)(lVar7 + 0x48);
      local_70 = (undefined1 *)&local_70;
      local_68 = &local_70;
                    /* catch() { ... } // from try @ 00af5d70 with catch @ 00afffd8 */
      if ((((plVar4 != (long *)0x0) &&
           (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[2] == local_60)) &&
          (local_70 = (undefined1 *)&local_70, local_68 = &local_70, plVar4[3] == lStack_58)) &&
         (local_70 = (undefined1 *)&local_70, local_68 = &local_70, (code *)plVar4[4] == local_50))
      {
        local_70 = (undefined1 *)&local_70;
        local_68 = &local_70;
        if (local_50 == (code *)0x0) {
LAB_00b00004:
          lVar2 = *plVar4;
          *(long *)(lVar2 + 8) = plVar4[1];
          *(long *)plVar4[1] = lVar2;
          _ZdlPv(plVar4);
        }
        else {
          local_70 = (undefined1 *)&local_70;
          local_68 = &local_70;
          (*local_50)(lStack_58);
          plVar4 = *(long **)(lVar7 + 0x48);
          if (plVar4 != (long *)0x0) goto LAB_00b00004;
        }
                    /* catch() { ... } // from try @ 00af5d48 with catch @ 00b0001c */
        *(undefined8 *)(lVar7 + 0x48) = 0;
        *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
      }
      plVar5 = (long *)(lVar7 + 0x50);
      plVar4 = (long *)*plVar5;
      if (plVar5 != plVar4) {
        do {
          plVar6 = (long *)((long)plVar4 - *(long *)(lVar7 + 0x60));
                    /* catch() { ... } // from try @ 00af5a7c with catch @ 00b00060 */
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
                    /* catch() { ... } // from try @ 00af6134 with catch @ 00b000a4 */
              *(long *)(lVar2 + 8) = plVar6[1];
              *(long *)plVar6[1] = lVar2;
              _ZdlPv(plVar6);
                    /* catch() { ... } // from try @ 00af5ba0 with catch @ 00b000b4 */
              *(int *)(lVar7 + 0x20) = *(int *)(lVar7 + 0x20) + -1;
            }
            break;
          }
          plVar4 = (long *)*plVar4;
        } while (plVar5 != plVar4);
      }
      *(undefined8 **)(local_70 + 8) = local_68;
      *local_68 = local_70;
      goto LAB_00afff6c;
    }
  }
                    /* catch() { ... } // from try @ 00af5768 with catch @ 00afff68 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
LAB_00afff6c:
                    /* catch() { ... } // from try @ 00af5704 with catch @ 00afff70 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af56a4 with catch @ 00afff78 */
                    /* catch() { ... } // from try @ 00afacc0 with catch @ 00afff80 */
  if (*(long *)(lVar3 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00afaaf4 with catch @ 00afff84 */
                    /* catch() { ... } // from try @ 00afa8cc with catch @ 00afff88
                       catch() { ... } // from try @ 00afa93c with catch @ 00afff88 */
                    /* catch() { ... } // from try @ 00afa8b8 with catch @ 00afff8c
                       catch() { ... } // from try @ 00afa928 with catch @ 00afff8c */
                    /* catch() { ... } // from try @ 00afa880 with catch @ 00afff90
                       catch() { ... } // from try @ 00afa900 with catch @ 00afff90 */
                    /* catch() { ... } // from try @ 00af73dc with catch @ 00afff94 */
                    /* catch() { ... } // from try @ 00af61a4 with catch @ 00afff98 */
  return;
}

~~~
