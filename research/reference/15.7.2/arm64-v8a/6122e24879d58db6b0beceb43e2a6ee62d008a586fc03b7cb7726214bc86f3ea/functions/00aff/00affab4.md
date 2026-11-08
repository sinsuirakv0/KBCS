# 00affab4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00affab4",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "991fcb4e75c099f43faceeab9951db384533d3d2510038e55bed70d8394ea4dc",
  "source_text_sha256": "991fcb4e75c099f43faceeab9951db384533d3d2510038e55bed70d8394ea4dc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 関連文字列（未確認候補）

~~~text
"Invalid Future"
~~~

## 疑似コード / UTF-8 2852 bytes

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
  
                    /* catch() { ... } // from try @ 00af60a4 with catch @ 00affabc */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af6094 with catch @ 00affac8 */
                    /* catch() { ... } // from try @ 00af6078 with catch @ 00affad0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af6068 with catch @ 00affad8 */
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6058 with catch @ 00affae0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00af6048 with catch @ 00affae8 */
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af6038 with catch @ 00affaf0 */
                    /* catch() { ... } // from try @ 00af6028 with catch @ 00affaf8 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
                    /* catch() { ... } // from try @ 00af6000 with catch @ 00affb00 */
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5ff0 with catch @ 00affb08 */
                    /* catch() { ... } // from try @ 00af5ee8 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00af5d5c with catch @ 00affb18 */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
                    /* catch() { ... } // from try @ 00af5ce0 with catch @ 00affb48 */
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5cd4 with catch @ 00affb54 */
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b8b0;
      if (lVar6 != 0) {
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
                    /* catch() { ... } // from try @ 00af5cc8 with catch @ 00affb6c */
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affb2c;
    }
  }
                    /* catch() { ... } // from try @ 00af5d20 with catch @ 00affb20 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b8b0;
LAB_00affb2c:
                    /* catch() { ... } // from try @ 00af5cec with catch @ 00affb30 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  return puVar5;
}

~~~
