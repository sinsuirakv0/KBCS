# 00bdafd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bdb0d0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0d0.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "8f4a4b255c15d2deca908ab65233b092b0f920fbd51c7718fbbaa107fd7918d3",
  "source_text_sha256": "8f4a4b255c15d2deca908ab65233b092b0f920fbd51c7718fbbaa107fd7918d3"
}
~~~

## 呼び出し元

- [005054cc](../00505/005054cc.md)
- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [00bd4fe8](../00bd4/00bd4fe8.md)

## 疑似コード / UTF-8 186 bytes

~~~c

void __cxa_free_exception(void)

{
                    /* catch() { ... } // from try @ 00bdaf74 with catch @ 00bdafdc */
  (*(code *)PTR___cxa_free_exception_00c1c020)();
  return;
}

~~~
