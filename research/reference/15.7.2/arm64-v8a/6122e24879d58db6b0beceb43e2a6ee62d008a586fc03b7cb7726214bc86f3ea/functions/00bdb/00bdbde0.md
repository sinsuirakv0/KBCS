# 00bdbde0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbde0.md)

## 関数情報

~~~json
{
  "address": "00bdbde0",
  "name": "Botan::BlockCipher::create",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9aa36b7757e7733b146a1264661a51f09714a0d2b8101fddb9c2ecd95b5090d8",
  "source_text_sha256": "9aa36b7757e7733b146a1264661a51f09714a0d2b8101fddb9c2ecd95b5090d8"
}
~~~
## 呼び出し元

- [00499128](../00499/00499128.md)
- [004993a0](../00499/004993a0.md)
- [004a3d70](../004a3/004a3d70.md)

## 呼び出し先

- [00498d9c](../00498/00498d9c.md)

## 疑似コード 1/1 / UTF-8 168 bytes

~~~c

void __thiscall
Botan::BlockCipher::create(BlockCipher *this,basic_string *param_1,basic_string *param_2)

{
  (*(code *)PTR_create_00c1c728)();
  return;
}

~~~
