# 00befa8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00befa8c",
  "name": "_ZNSt13exception_ptrD1Ev",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a0b858b86959e82f35387494de7c7962a8fd4ea76780b9a84cc227380241865",
  "source_text_sha256": "3a0b858b86959e82f35387494de7c7962a8fd4ea76780b9a84cc227380241865"
}
~~~

## 呼び出し元

- [00c582f0](../00c58/00c582f0.md)

## 呼び出し先

- [00c5df10](../00c5d/00c5df10.md)

## 疑似コード / UTF-8 116 bytes

~~~c

void _ZNSt13exception_ptrD1Ev(undefined8 *param_1)

{
  __cxa_decrement_exception_refcount(*param_1);
  return;
}

~~~
