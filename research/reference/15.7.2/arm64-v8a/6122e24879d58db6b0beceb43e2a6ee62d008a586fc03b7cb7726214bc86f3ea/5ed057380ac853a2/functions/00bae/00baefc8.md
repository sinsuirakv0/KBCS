# 00baefc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baefc8.md)

## 関数情報

~~~json
{
  "address": "00baefc8",
  "name": "_ZNSt6__ndk18numpunctIwED1Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5919f904ce1447580872d7288890fa1ce5c907ce500360a978adbfb960fe3931",
  "source_text_sha256": "5919f904ce1447580872d7288890fa1ce5c907ce500360a978adbfb960fe3931"
}
~~~
## 呼び出し元

- [00be1b50](../00be1/00be1b50.md)
- [00be1b60](../00be1/00be1b60.md)
- [00be1bb0](../00be1/00be1bb0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

## 疑似コード 1/1 / UTF-8 265 bytes

~~~c

void _ZNSt6__ndk18numpunctIwED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bec0 + 0x10);
  if ((*(byte *)(param_1 + 3) & 1) != 0) {
    _ZdlPv((void *)param_1[5]);
  }
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~
