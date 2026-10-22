# 00bdcaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcaf0.md)

## 関数情報

~~~json
{
  "address": "00bdcaf0",
  "name": "Botan::Certificate_Store_In_Memory::add_crl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "daa3d96918d06a8ab689a4a1c7e2a273b6355ffdb4dfa4f7bad704fa398de277",
  "source_text_sha256": "daa3d96918d06a8ab689a4a1c7e2a273b6355ffdb4dfa4f7bad704fa398de277"
}
~~~
## 呼び出し元

- [004df5b0](../004df/004df5b0.md)

## 呼び出し先

- [004df724](../004df/004df724.md)

## 疑似コード 1/1 / UTF-8 128 bytes

~~~c

void __thiscall Botan::Certificate_Store_In_Memory::add_crl(void)

{
  (*(code *)PTR_add_crl_00c1cdb0)();
  return;
}

~~~
