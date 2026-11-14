# 00bfbea0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfbea0",
  "name": "_ZNKSt6__ndk113random_device7entropyEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3f1a54a1eb8f46069a89bcca62ecec5b9e95a8b7f64eaa4f098b64385926700",
  "source_text_sha256": "b3f1a54a1eb8f46069a89bcca62ecec5b9e95a8b7f64eaa4f098b64385926700"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f350](../00c5f/00c5f350.md)

## 疑似コード / UTF-8 417 bytes

~~~c

undefined1  [16] _ZNKSt6__ndk113random_device7entropyEv(int *param_1)

{
  int iVar1;
  double dVar2;
  undefined1 auVar3 [16];
  uint local_14;
  
  iVar1 = ioctl(*param_1,0x80045200,&local_14);
  dVar2 = 0.0;
  if ((-1 < iVar1) && (-1 < (int)local_14)) {
    if (0x1f < local_14) {
      local_14 = 0x20;
    }
    dVar2 = (double)(int)local_14;
  }
  auVar3._8_8_ = 0;
  auVar3._0_8_ = dVar2;
  return auVar3;
}

~~~
