# 00bdcff0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcff0.md)

## 関数情報

~~~json
{
  "address": "00bdcff0",
  "name": "Botan::x509_path_validate",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "584ea6cc3be15c4085c41dfd2815682529c482f803caff2eb64a91d1474bd548",
  "source_text_sha256": "584ea6cc3be15c4085c41dfd2815682529c482f803caff2eb64a91d1474bd548"
}
~~~
## 呼び出し元

- [00509740](../00509/00509740.md)
- [0050986c](../00509/0050986c.md)
- [0050995c](../00509/0050995c.md)

## 呼び出し先

- [00508860](../00508/00508860.md)

## 疑似コード 1/1 / UTF-8 121 bytes

~~~c

void __thiscall Botan::x509_path_validate(void)

{
  (*(code *)PTR_x509_path_validate_00c1d030)();
  return;
}

~~~
