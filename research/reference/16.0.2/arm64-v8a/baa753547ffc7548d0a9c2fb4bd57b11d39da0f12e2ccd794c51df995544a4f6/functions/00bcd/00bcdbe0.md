# 00bcdbe0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcdbe0",
  "name": "_ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293",
  "source_text_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5dae0](../00c5d/00c5dae0.md)
- [00c5dd00](../00c5d/00c5dd00.md)

## 疑似コード / UTF-8 319 bytes

~~~c

void _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~
