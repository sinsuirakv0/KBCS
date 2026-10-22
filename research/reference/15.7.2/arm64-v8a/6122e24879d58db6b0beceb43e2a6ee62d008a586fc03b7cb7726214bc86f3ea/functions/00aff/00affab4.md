# 00affab4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00affab4.md)

## 関数情報

~~~json
{
  "address": "00affab4",
  "name": "firebase::ReferenceCountedFutureImpl::GetFutureErrorMessage",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3e57ec6f7d884d762c14745623817440bae4032542328634978ee0c86335ffb",
  "source_text_sha256": "e3e57ec6f7d884d762c14745623817440bae4032542328634978ee0c86335ffb"
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
## 疑似コード 1/1 / UTF-8 3129 bytes

~~~c

/* firebase::ReferenceCountedFutureImpl::GetFutureErrorMessage(firebase::FutureHandle const&) const
    */

undefined * __thiscall
firebase::ReferenceCountedFutureImpl::GetFutureErrorMessage
          (ReferenceCountedFutureImpl *this,FutureHandle *param_1)

{
  Mutex *this_00;
  ReferenceCountedFutureImpl *pRVar1;
  ReferenceCountedFutureImpl *pRVar2;
  ReferenceCountedFutureImpl *pRVar3;
  undefined *puVar4;
  long lVar5;
  ulong uVar6;
  
                    /* catch() { ... } // from try @ 00af60a4 with catch @ 00affabc */
  this_00 = (Mutex *)(this + 8);
                    /* catch() { ... } // from try @ 00af6094 with catch @ 00affac8 */
                    /* catch() { ... } // from try @ 00af6078 with catch @ 00affad0 */
  Mutex::Acquire(this_00);
                    /* catch() { ... } // from try @ 00af6068 with catch @ 00affad8 */
  uVar6 = *(ulong *)param_1;
                    /* catch() { ... } // from try @ 00af6058 with catch @ 00affae0 */
  Mutex::Acquire(this_00);
  pRVar3 = this + 0x38;
  pRVar2 = *(ReferenceCountedFutureImpl **)pRVar3;
                    /* catch() { ... } // from try @ 00af6048 with catch @ 00affae8 */
  pRVar1 = pRVar3;
  if (pRVar2 != (ReferenceCountedFutureImpl *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af6038 with catch @ 00affaf0 */
                    /* catch() { ... } // from try @ 00af6028 with catch @ 00affaf8 */
      if (*(ulong *)(pRVar2 + 0x20) >= uVar6) {
        pRVar1 = pRVar2;
      }
                    /* catch() { ... } // from try @ 00af6000 with catch @ 00affb00 */
      pRVar2 = *(ReferenceCountedFutureImpl **)
                (pRVar2 + (ulong)(*(ulong *)(pRVar2 + 0x20) < uVar6) * 8);
    } while (pRVar2 != (ReferenceCountedFutureImpl *)0x0);
                    /* catch() { ... } // from try @ 00af5ff0 with catch @ 00affb08 */
                    /* catch() { ... } // from try @ 00af5ee8 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00af5d5c with catch @ 00affb18 */
    if ((pRVar1 != pRVar3) && (*(ulong *)(pRVar1 + 0x20) <= uVar6)) {
                    /* catch() { ... } // from try @ 00af5ce0 with catch @ 00affb48 */
      lVar5 = *(long *)(pRVar1 + 0x28);
      Mutex::Release(this_00);
                    /* catch() { ... } // from try @ 00af5cd4 with catch @ 00affb54 */
      puVar4 = PTR_kErrorMessageFutureIsNoLongerValid_00c1b8b0;
      if (lVar5 != 0) {
        if ((*(byte *)(lVar5 + 8) & 1) == 0) {
          puVar4 = (undefined *)(lVar5 + 9);
        }
        else {
                    /* catch() { ... } // from try @ 00af5cc8 with catch @ 00affb6c */
          puVar4 = *(undefined **)(lVar5 + 0x18);
        }
      }
      goto LAB_00affb2c;
    }
  }
                    /* catch() { ... } // from try @ 00af5d20 with catch @ 00affb20 */
  Mutex::Release(this_00);
  puVar4 = PTR_kErrorMessageFutureIsNoLongerValid_00c1b8b0;
LAB_00affb2c:
                    /* catch() { ... } // from try @ 00af5cec with catch @ 00affb30 */
  Mutex::Release(this_00);
  return puVar4;
}

~~~
