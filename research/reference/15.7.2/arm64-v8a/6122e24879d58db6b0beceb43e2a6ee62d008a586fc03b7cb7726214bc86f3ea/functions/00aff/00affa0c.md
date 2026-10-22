# 00affa0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00affa0c.md)

## 関数情報

~~~json
{
  "address": "00affa0c",
  "name": "firebase::ReferenceCountedFutureImpl::GetFutureError",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9e963200c8872f68b628b3e4b4a5d6fd7519796ce1ab9376a58613934e165b6",
  "source_text_sha256": "d9e963200c8872f68b628b3e4b4a5d6fd7519796ce1ab9376a58613934e165b6"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード 1/1 / UTF-8 1841 bytes

~~~c

/* firebase::ReferenceCountedFutureImpl::GetFutureError(firebase::FutureHandle const&) const */

undefined4 __thiscall
firebase::ReferenceCountedFutureImpl::GetFutureError
          (ReferenceCountedFutureImpl *this,FutureHandle *param_1)

{
  Mutex *this_00;
  ReferenceCountedFutureImpl *pRVar1;
  ReferenceCountedFutureImpl *pRVar2;
  undefined4 uVar3;
  ReferenceCountedFutureImpl *pRVar4;
  long lVar5;
  ulong uVar6;
  
                    /* catch() { ... } // from try @ 00af6358 with catch @ 00affa0c */
                    /* catch() { ... } // from try @ 00af6284 with catch @ 00affa10 */
  this_00 = (Mutex *)(this + 8);
  Mutex::Acquire(this_00);
  uVar6 = *(ulong *)param_1;
                    /* catch() { ... } // from try @ 00af6188 with catch @ 00affa38 */
  Mutex::Acquire(this_00);
  pRVar4 = this + 0x38;
  pRVar2 = *(ReferenceCountedFutureImpl **)pRVar4;
  pRVar1 = pRVar4;
  if (pRVar2 == (ReferenceCountedFutureImpl *)0x0) {
LAB_00affa74:
    Mutex::Release(this_00);
  }
  else {
    do {
      if (*(ulong *)(pRVar2 + 0x20) >= uVar6) {
        pRVar1 = pRVar2;
      }
      pRVar2 = *(ReferenceCountedFutureImpl **)
                (pRVar2 + (ulong)(*(ulong *)(pRVar2 + 0x20) < uVar6) * 8);
    } while (pRVar2 != (ReferenceCountedFutureImpl *)0x0);
    if ((pRVar1 == pRVar4) || (uVar6 < *(ulong *)(pRVar1 + 0x20))) goto LAB_00affa74;
    lVar5 = *(long *)(pRVar1 + 0x28);
    Mutex::Release(this_00);
    if (lVar5 != 0) {
                    /* catch() { ... } // from try @ 00af612c with catch @ 00affaac */
      uVar3 = *(undefined4 *)(lVar5 + 4);
      goto LAB_00affa80;
    }
  }
  uVar3 = 0xffffffff;
LAB_00affa80:
  Mutex::Release(this_00);
                    /* catch() { ... } // from try @ 00af617c with catch @ 00affa8c */
  return uVar3;
}

~~~
