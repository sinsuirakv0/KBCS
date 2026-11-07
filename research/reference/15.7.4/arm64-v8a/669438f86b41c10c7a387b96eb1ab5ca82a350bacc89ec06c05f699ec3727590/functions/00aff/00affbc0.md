# 00affbc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00affab4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00affbc0",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f5f8c341bb802da606a6ac9b2aee797874514b1a88c455042cedfaab4f98b5d",
  "source_text_sha256": "1f5f8c341bb802da606a6ac9b2aee797874514b1a88c455042cedfaab4f98b5d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

## 関連文字列（未確認候補）

~~~text
"Invalid Future"
~~~

## 疑似コード / UTF-8 2330 bytes

~~~c

undefined *
_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  undefined *puVar5;
  long lVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af5cf4 with catch @ 00affbc8 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5ce8 with catch @ 00affbd4 */
                    /* catch() { ... } // from try @ 00af5cdc with catch @ 00affbe0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5cd0 with catch @ 00affbec */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af5c78 with catch @ 00affc04 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5c6c with catch @ 00affc1c */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b9b0;
      if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5c3c with catch @ 00affc64 */
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
                    /* catch() { ... } // from try @ 00af5c30 with catch @ 00affc70 */
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affc38;
    }
  }
                    /* catch() { ... } // from try @ 00af5c60 with catch @ 00affc28 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b9b0;
LAB_00affc38:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5c54 with catch @ 00affc40 */
                    /* catch() { ... } // from try @ 00af5c48 with catch @ 00affc4c */
  return puVar5;
}

~~~
