# 00bdcdc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ff4a5e6b888bed776958bce3c89bc007dd95f72ae91d09bb4ef56becee4deff",
  "source_text_sha256": "2ff4a5e6b888bed776958bce3c89bc007dd95f72ae91d09bb4ef56becee4deff"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5de30](../00c5d/00c5de30.md)

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_(undefined8 *param_1)

{
  *param_1 = 0;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_();
  return;
}

~~~
