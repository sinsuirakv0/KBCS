# 00b4dbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b4dcb8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dcb8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b4dbac",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f34a339f713174c77ab300a55fe87c7ec4b7775dfebfae79fdeb249904136e7",
  "source_text_sha256": "1f34a339f713174c77ab300a55fe87c7ec4b7775dfebfae79fdeb249904136e7"
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

## 疑似コード / UTF-8 1913 bytes

~~~c

void _ZN8firebase9messaging21UnsubscribeLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_010a0fa0 == 0) {
                    /* catch() { ... } // from try @ 00b4c46c with catch @ 00b4dc20 */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
                    /* catch() { ... } // from try @ 00b4c44c with catch @ 00b4dc24 */
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
                    /* catch() { ... } // from try @ 00b4c418 with catch @ 00b4dc34 */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c3f4 with catch @ 00b4dc38 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
                    /* catch() { ... } // from try @ 00b4d37c with catch @ 00b4dbe0 */
    lVar2 = *(long *)(lVar1 + 0x50);
                    /* catch() { ... } // from try @ 00b4cfe4 with catch @ 00b4dbe4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
                    /* catch() { ... } // from try @ 00b4ceec with catch @ 00b4dbf8 */
                    /* catch() { ... } // from try @ 00b4cbe0 with catch @ 00b4dbfc */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* catch() { ... } // from try @ 00b4c200 with catch @ 00b4dc00 */
                    /* catch() { ... } // from try @ 00b4bee8 with catch @ 00b4dc04 */
    _ZN8firebase12FutureHandleC1Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x80);
  }
                    /* catch() { ... } // from try @ 00b4c7c0 with catch @ 00b4dc48 */
                    /* catch() { ... } // from try @ 00b4c624 with catch @ 00b4dc4c */
                    /* catch() { ... } // from try @ 00b4c3c8 with catch @ 00b4dc50 */
  return;
}

~~~
