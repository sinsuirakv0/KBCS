# 00bdcfc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcfc0.md)

## 関数情報

~~~json
{
  "address": "00bdcfc0",
  "name": "Botan::PKIX::check_crl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39ac7ab501689c97bd13fd85adc656f6212b3df70255aecd60bb9545ecc28012",
  "source_text_sha256": "39ac7ab501689c97bd13fd85adc656f6212b3df70255aecd60bb9545ecc28012"
}
~~~
## 呼び出し元

- [00508860](../00508/00508860.md)

## 呼び出し先

- [005060a8](../00506/005060a8.md)

## 疑似コード 1/1 / UTF-8 109 bytes

~~~c

void __thiscall Botan::PKIX::check_crl(void)

{
  (*(code *)PTR_check_crl_00c1d018)();
  return;
}

~~~
