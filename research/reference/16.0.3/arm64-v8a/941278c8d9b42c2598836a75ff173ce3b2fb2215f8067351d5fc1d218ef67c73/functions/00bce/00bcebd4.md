# 00bcebd4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcebd4",
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

- [00c5eab0](../00c5e/00c5eab0.md)
- [00c5ecd0](../00c5e/00c5ecd0.md)

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
