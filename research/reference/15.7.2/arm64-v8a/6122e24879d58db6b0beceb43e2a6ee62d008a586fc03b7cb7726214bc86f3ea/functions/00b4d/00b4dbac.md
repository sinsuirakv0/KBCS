# 00b4dbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b4dbac.md)

## 関数情報

~~~json
{
  "address": "00b4dbac",
  "name": "firebase::messaging::UnsubscribeLastResult",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06bc397da24df9903bac7fe958da5f23744f37887a872b48c1caa0b8c05bd5e2",
  "source_text_sha256": "06bc397da24df9903bac7fe958da5f23744f37887a872b48c1caa0b8c05bd5e2"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddc80](../00bdd/00bddc80.md)
- [00bddd10](../00bdd/00bddd10.md)
- [00bdddf0](../00bdd/00bdddf0.md)
- [00bdde90](../00bdd/00bdde90.md)
- [00bde080](../00bde/00bde080.md)
- [00be0200](../00be0/00be0200.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~
## 疑似コード 1/1 / UTF-8 1947 bytes

~~~c

/* firebase::messaging::UnsubscribeLastResult() */

void __thiscall firebase::messaging::UnsubscribeLastResult(messaging *this)

{
  long lVar1;
  FutureBase *in_x8;
  long lVar2;
  
  if (DAT_010a0fa0 == 0) {
                    /* catch() { ... } // from try @ 00b4c46c with catch @ 00b4dc20 */
    LogAssert("internal::IsInitialized()");
                    /* catch() { ... } // from try @ 00b4c44c with catch @ 00b4dc24 */
    Mutex::Mutex();
                    /* catch() { ... } // from try @ 00b4c418 with catch @ 00b4dc34 */
    *(undefined8 *)(in_x8 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c3f4 with catch @ 00b4dc38 */
    FutureHandle::FutureHandle((FutureHandle *)(in_x8 + 0x30),0,(FutureApiInterface *)0x0);
  }
  else {
    lVar1 = FutureData::Get();
    Mutex::Acquire((Mutex *)(lVar1 + 8));
                    /* catch() { ... } // from try @ 00b4d37c with catch @ 00b4dbe0 */
    lVar2 = *(long *)(lVar1 + 0x50);
                    /* catch() { ... } // from try @ 00b4cfe4 with catch @ 00b4dbe4 */
    Mutex::Release((Mutex *)(lVar1 + 8));
    Mutex::Mutex();
                    /* catch() { ... } // from try @ 00b4ceec with catch @ 00b4dbf8 */
                    /* catch() { ... } // from try @ 00b4cbe0 with catch @ 00b4dbfc */
    *(undefined8 *)(in_x8 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c200 with catch @ 00b4dc00 */
                    /* catch() { ... } // from try @ 00b4bee8 with catch @ 00b4dc04 */
    FutureHandle::FutureHandle((FutureHandle *)(in_x8 + 0x30));
    FutureBase::operator=(in_x8,(FutureBase *)(lVar2 + 0x80));
  }
                    /* catch() { ... } // from try @ 00b4c7c0 with catch @ 00b4dc48 */
                    /* catch() { ... } // from try @ 00b4c624 with catch @ 00b4dc4c */
                    /* catch() { ... } // from try @ 00b4c3c8 with catch @ 00b4dc50 */
  return;
}

~~~
