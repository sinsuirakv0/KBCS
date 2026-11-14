# 00bcebfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcebfc",
  "name": "_ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e39dd7aee7500a646f35854bb33ec343c7150838a9b3fe209f2b5275559c6a6c",
  "source_text_sha256": "e39dd7aee7500a646f35854bb33ec343c7150838a9b3fe209f2b5275559c6a6c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5ea90](../00c5e/00c5ea90.md)
- [00c5ecd0](../00c5e/00c5ecd0.md)

## 疑似コード / UTF-8 635 bytes

~~~c

void _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,long param_3)

{
  _ZN8firebase5Mutex7AcquireEv(param_3 + 700);
                    /* try { // try from 00bcec18 to 00ccec1f has its CatchHandler @ 00bcfa80 */
  *(undefined1 *)(param_3 + 0x2b8) = 0;
                    /* try { // try from 00bcec20 to 00ccedc3 has its CatchHandler @ 00bcd634 */
  _ZN8firebase5Mutex7ReleaseEv(param_3 + 700);
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~
