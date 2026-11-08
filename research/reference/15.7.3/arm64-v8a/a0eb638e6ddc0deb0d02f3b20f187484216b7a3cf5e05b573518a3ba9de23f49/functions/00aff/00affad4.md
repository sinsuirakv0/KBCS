# 00affad4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00affad4",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1837549c645d27ffa23ed9d041f1f4635943f5b2a86e9581de77c54214664a39",
  "source_text_sha256": "1837549c645d27ffa23ed9d041f1f4635943f5b2a86e9581de77c54214664a39"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

## 疑似コード / UTF-8 2453 bytes

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
  
                    /* catch() { ... } // from try @ 00af6068 with catch @ 00affad8 */
                    /* catch() { ... } // from try @ 00af6058 with catch @ 00affae0 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af6048 with catch @ 00affae8 */
                    /* catch() { ... } // from try @ 00af6038 with catch @ 00affaf0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af6028 with catch @ 00affaf8 */
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6000 with catch @ 00affb00 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00af5ff0 with catch @ 00affb08 */
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affb3c:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af5ee8 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00af5d5c with catch @ 00affb18 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
                    /* catch() { ... } // from try @ 00af5d20 with catch @ 00affb20 */
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5cf8 with catch @ 00affb28 */
                    /* catch() { ... } // from try @ 00af5cec with catch @ 00affb30 */
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affb3c;
    lVar6 = plVar2[5];
                    /* catch() { ... } // from try @ 00af5cc8 with catch @ 00affb6c */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (lVar6 != 0) {
      uVar4 = *(undefined4 *)(lVar6 + 4);
                    /* catch() { ... } // from try @ 00af5cbc with catch @ 00affb78 */
      goto LAB_00affb48;
    }
  }
  uVar4 = 0xffffffff;
LAB_00affb48:
                    /* catch() { ... } // from try @ 00af5ce0 with catch @ 00affb48 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5cd4 with catch @ 00affb54 */
  return uVar4;
}

~~~
