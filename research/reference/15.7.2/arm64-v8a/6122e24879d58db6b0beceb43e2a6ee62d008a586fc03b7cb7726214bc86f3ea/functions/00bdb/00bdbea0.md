# 00bdbea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbea0.md)

## 関数情報

~~~json
{
  "address": "00bdbea0",
  "name": "Botan::HashFunction::create",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a41cb2000e823ea866a83669e86e2c21593ae99bb745463a4441872c74f2514e",
  "source_text_sha256": "a41cb2000e823ea866a83669e86e2c21593ae99bb745463a4441872c74f2514e"
}
~~~
## 呼び出し元

- [0049e24c](../0049e/0049e24c.md)
- [004a19c4](../004a1/004a19c4.md)
- [004a9174](../004a9/004a9174.md)
- [004ab3f4](../004ab/004ab3f4.md)
- [004c3c00](../004c3/004c3c00.md)
- [004def78](../004de/004def78.md)
- [004df290](../004df/004df290.md)
- [004e939c](../004e9/004e939c.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00501274](../00501/00501274.md)
- [0055f8e0](../0055f/0055f8e0.md)

## 呼び出し先

- [0049e3f4](../0049e/0049e3f4.md)

## 疑似コード 1/1 / UTF-8 170 bytes

~~~c

void __thiscall
Botan::HashFunction::create(HashFunction *this,basic_string *param_1,basic_string *param_2)

{
  (*(code *)PTR_create_00c1c788)();
  return;
}

~~~
