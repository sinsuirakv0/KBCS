# 00bdbfe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbfe0.md)

## 関数情報

~~~json
{
  "address": "00bdbfe0",
  "name": "Botan::DataSink_Stream::~DataSink_Stream",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15a701d615d6b3e096ea9abdb95a8607ddd7c7ef6e24035f89da9680ef7c3993",
  "source_text_sha256": "15a701d615d6b3e096ea9abdb95a8607ddd7c7ef6e24035f89da9680ef7c3993"
}
~~~
## 呼び出し元

- [004a38b0](../004a3/004a38b0.md)

## 呼び出し先

- [004a3810](../004a3/004a3810.md)

## 疑似コード 1/1 / UTF-8 151 bytes

~~~c

void __thiscall Botan::DataSink_Stream::~DataSink_Stream(DataSink_Stream *this)

{
  (*(code *)PTR__DataSink_Stream_00c1c828)();
  return;
}

~~~
