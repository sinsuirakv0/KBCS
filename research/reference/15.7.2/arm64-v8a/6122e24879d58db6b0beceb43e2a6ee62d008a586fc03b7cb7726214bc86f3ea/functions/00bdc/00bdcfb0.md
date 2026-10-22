# 00bdcfb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcfb0.md)

## 関数情報

~~~json
{
  "address": "00bdcfb0",
  "name": "Botan::PKIX::check_crl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c250b0d4a69de1f32899ad54d505250ddafbb21041e9a945a713cae88e950702",
  "source_text_sha256": "c250b0d4a69de1f32899ad54d505250ddafbb21041e9a945a713cae88e950702"
}
~~~
## 呼び出し元

- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [005054cc](../00505/005054cc.md)

## 疑似コード 1/1 / UTF-8 207 bytes

~~~c

void __thiscall Botan::PKIX::check_crl(void)

{
                    /* try { // try from 00bdcfb0 to 00cdd21b has its CatchHandler @ 00bdcbcc */
  (*(code *)PTR_check_crl_00c1d010)();
  return;
}

~~~
