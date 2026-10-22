# 00bdaef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdaef0.md)

## 関数情報

~~~json
{
  "address": "00bdaef0",
  "name": "<EXTERNAL>::__register_atfork",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "572ba44fe6a012eb07b0a002bbf8281723f43237604c8f7da274302cbe4a6f88",
  "source_text_sha256": "572ba44fe6a012eb07b0a002bbf8281723f43237604c8f7da274302cbe4a6f88"
}
~~~
## 呼び出し元

- [00418320](../00418/00418320.md)

## 呼び出し先

- [010a5010](../010a5/010a5010.md)

## 疑似コード 1/1 / UTF-8 101 bytes

~~~c

void __register_atfork(void)

{
  (*(code *)PTR___register_atfork_00c1bfb0)();
  return;
}

~~~
