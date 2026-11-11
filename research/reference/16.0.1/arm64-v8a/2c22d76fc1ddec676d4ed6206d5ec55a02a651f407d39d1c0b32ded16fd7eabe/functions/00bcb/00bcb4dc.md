# 00bcb4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcb4dc",
  "name": "_ZN8firebase4auth15IdTokenListenerD1Ev",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "479ab731a25513e2927709e59d19ae7d772d32c14fb9112be1109f1554be815e",
  "source_text_sha256": "479ab731a25513e2927709e59d19ae7d772d32c14fb9112be1109f1554be815e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5da60](../00c5d/00c5da60.md)

## 疑似コード / UTF-8 482 bytes

~~~c

void _ZN8firebase4auth15IdTokenListenerD1Ev(long *param_1)

{
  undefined8 *__ptr;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth15IdTokenListenerE_00c9b9b0 + 0x10);
  while( true ) {
    __ptr = (undefined8 *)param_1[1];
    if (__ptr == (undefined8 *)param_1[2]) break;
    _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE(*__ptr,param_1);
  }
  if (__ptr != (undefined8 *)0x0) {
    param_1[2] = (long)__ptr;
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
