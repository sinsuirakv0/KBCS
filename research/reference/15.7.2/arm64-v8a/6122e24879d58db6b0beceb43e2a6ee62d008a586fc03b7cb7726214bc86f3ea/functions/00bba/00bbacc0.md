# 00bbacc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbacc0.md)

## 関数情報

~~~json
{
  "address": "00bbacc0",
  "name": "std::bad_alloc::~bad_alloc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1d28a019b38884451c6da4743f46cf5da796a7abe41cd58387d27caf47f8742",
  "source_text_sha256": "e1d28a019b38884451c6da4743f46cf5da796a7abe41cd58387d27caf47f8742"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdbb00](../00bdb/00bdbb00.md)

## 疑似コード 1/1 / UTF-8 1106 bytes

~~~c

/* std::bad_alloc::~bad_alloc() */

void __thiscall std::bad_alloc::~bad_alloc(bad_alloc *this)

{
                    /* catch() { ... } // from try @ 00bb6e48 with catch @ 00bbacc4 */
                    /* catch() { ... } // from try @ 00bb6a94 with catch @ 00bbacc8 */
                    /* catch() { ... } // from try @ 00bb6a7c with catch @ 00bbaccc */
                    /* catch() { ... } // from try @ 00bb66c8 with catch @ 00bbacd0 */
                    /* catch() { ... } // from try @ 00bb66e0 with catch @ 00bbacd4 */
  bad_array_new_length::~bad_array_new_length((bad_array_new_length *)this);
                    /* catch() { ... } // from try @ 00bb6314 with catch @ 00bbacd8 */
                    /* catch() { ... } // from try @ 00bb632c with catch @ 00bbacdc */
                    /* catch() { ... } // from try @ 00bb5f78 with catch @ 00bbace0 */
                    /* catch() { ... } // from try @ 00bb5f60 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb5bb8 with catch @ 00bbace8 */
  operator_delete(this);
  return;
}

~~~
