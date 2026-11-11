# 00bcdb6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcdb6c",
  "name": "_ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ace90afe5e708fb2676ca8c06d5311774b28d0adaf89135ed019f791c13a1ff7",
  "source_text_sha256": "ace90afe5e708fb2676ca8c06d5311774b28d0adaf89135ed019f791c13a1ff7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5d9f0](../00c5d/00c5d9f0.md)
- [00c5dc30](../00c5d/00c5dc30.md)

## 疑似コード / UTF-8 441 bytes

~~~c

void _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,long param_3)

{
  _ZN8firebase5Mutex7AcquireEv(param_3 + 700);
  *(undefined1 *)(param_3 + 0x2b8) = 0;
  _ZN8firebase5Mutex7ReleaseEv(param_3 + 700);
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~
