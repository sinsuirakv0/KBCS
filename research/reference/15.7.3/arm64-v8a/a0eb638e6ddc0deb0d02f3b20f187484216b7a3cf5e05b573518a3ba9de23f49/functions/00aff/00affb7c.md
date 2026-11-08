# 00affb7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00affb7c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "935deff46d6ce643a92565a3a7bbf9c6424c28034bd0c2630e73c7cc14548ad6",
  "source_text_sha256": "935deff46d6ce643a92565a3a7bbf9c6424c28034bd0c2630e73c7cc14548ad6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

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
  
                    /* catch() { ... } // from try @ 00af5cb0 with catch @ 00affb84 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5ca4 with catch @ 00affb90 */
                    /* catch() { ... } // from try @ 00af5c98 with catch @ 00affb9c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5c8c with catch @ 00affba8 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af5c34 with catch @ 00affbc0 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5c28 with catch @ 00affbd8 */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b960;
      if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5bf8 with catch @ 00affc20 */
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
                    /* catch() { ... } // from try @ 00af5bec with catch @ 00affc2c */
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affbf4;
    }
  }
                    /* catch() { ... } // from try @ 00af5c1c with catch @ 00affbe4 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b960;
LAB_00affbf4:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5c10 with catch @ 00affbfc */
                    /* catch() { ... } // from try @ 00af5c04 with catch @ 00affc08 */
  return puVar5;
}

~~~
