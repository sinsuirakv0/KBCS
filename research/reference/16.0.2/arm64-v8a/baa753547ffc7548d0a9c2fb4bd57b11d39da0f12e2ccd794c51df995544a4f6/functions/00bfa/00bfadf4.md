# 00bfadf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfadf4",
  "name": "_ZNSt6__ndk113random_deviceD1Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3",
  "source_text_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3"
}
~~~

## 呼び出し元

- [00c584a0](../00c58/00c584a0.md)

## 呼び出し先

- [00c598a0](../00c59/00c598a0.md)

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD1Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~
