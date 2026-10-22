# 00bdafd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdafd0.md)

## 関数情報

~~~json
{
  "address": "00bdafd0",
  "name": "__cxa_free_exception",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c65fbafebd983b0310e78a6f0fa2b4ebe1f7f7308d966efb98bec35135fa4441",
  "source_text_sha256": "c65fbafebd983b0310e78a6f0fa2b4ebe1f7f7308d966efb98bec35135fa4441"
}
~~~
## 呼び出し元

- [005054cc](../00505/005054cc.md)
- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [00bd4fe8](../00bd4/00bd4fe8.md)

## 疑似コード 1/1 / UTF-8 195 bytes

~~~c

void __cxa_free_exception(void)

{
                    /* catch() { ... } // from try @ 00bdaf74 with catch @ 00bdafdc */
  (*(code *)PTR___cxa_free_exception_00c1c020)();
  return;
}

~~~
