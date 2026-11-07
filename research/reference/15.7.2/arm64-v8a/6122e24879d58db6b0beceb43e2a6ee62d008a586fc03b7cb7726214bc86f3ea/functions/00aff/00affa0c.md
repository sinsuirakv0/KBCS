# 00affa0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00affb18`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00affa0c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "471c76ad571c7eca2f5f3d9e0c6d435583d40bc33e83968a30a08cd1c6b809be",
  "source_text_sha256": "471c76ad571c7eca2f5f3d9e0c6d435583d40bc33e83968a30a08cd1c6b809be"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード / UTF-8 1496 bytes

~~~c

undefined4
_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined4 uVar4;
  long *plVar5;
  long lVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af6358 with catch @ 00affa0c */
                    /* catch() { ... } // from try @ 00af6284 with catch @ 00affa10 */
  lVar1 = param_1 + 8;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6188 with catch @ 00affa38 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affa74:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affa74;
    lVar6 = plVar2[5];
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af612c with catch @ 00affaac */
      uVar4 = *(undefined4 *)(lVar6 + 4);
      goto LAB_00affa80;
    }
  }
  uVar4 = 0xffffffff;
LAB_00affa80:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af617c with catch @ 00affa8c */
  return uVar4;
}

~~~
