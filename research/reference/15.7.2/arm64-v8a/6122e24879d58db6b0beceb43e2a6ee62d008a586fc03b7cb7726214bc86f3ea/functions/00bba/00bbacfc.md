# 00bbacfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbacfc.md)

## 関数情報

~~~json
{
  "address": "00bbacfc",
  "name": "std::bad_array_new_length::bad_array_new_length",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fadd85b101243367f895d3c3fd87049c889f00141c84b1c5e7c50dbada82b124",
  "source_text_sha256": "fadd85b101243367f895d3c3fd87049c889f00141c84b1c5e7c50dbada82b124"
}
~~~
## 呼び出し元

- [00bdb0e0](../00bdb/00bdb0e0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 668 bytes

~~~c

/* std::bad_array_new_length::bad_array_new_length() */

void __thiscall std::bad_array_new_length::bad_array_new_length(bad_array_new_length *this)

{
                    /* catch() { ... } // from try @ 00bb4c88 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb4ca0 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb48c0 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bb48a8 with catch @ 00bbad0c */
  *(undefined **)this = PTR_vtable_00c1bf20 + 0x10;
                    /* catch() { ... } // from try @ 00bb4500 with catch @ 00bbad10 */
  return;
}

~~~
