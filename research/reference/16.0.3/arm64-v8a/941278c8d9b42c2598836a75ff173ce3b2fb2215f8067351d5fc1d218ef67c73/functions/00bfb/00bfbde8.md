# 00bfbde8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbde8",
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

- [00c59470](../00c59/00c59470.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD1Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~
