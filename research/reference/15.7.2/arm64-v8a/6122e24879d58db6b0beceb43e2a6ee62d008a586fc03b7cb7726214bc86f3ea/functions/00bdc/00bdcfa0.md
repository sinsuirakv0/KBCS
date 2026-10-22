# 00bdcfa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcfa0.md)

## 関数情報

~~~json
{
  "address": "00bdcfa0",
  "name": "Botan::PKIX::check_ocsp",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bb0e50d80d3381b2728e781514835c48a62491941feb0a4cb45b6765fca6530",
  "source_text_sha256": "6bb0e50d80d3381b2728e781514835c48a62491941feb0a4cb45b6765fca6530"
}
~~~
## 呼び出し元

- [00508860](../00508/00508860.md)

## 呼び出し先

- [00504f50](../00504/00504f50.md)

## 疑似コード 1/1 / UTF-8 111 bytes

~~~c

void __thiscall Botan::PKIX::check_ocsp(void)

{
  (*(code *)PTR_check_ocsp_00c1d008)();
  return;
}

~~~
