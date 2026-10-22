# 00bbaca8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaca8.md)

## 関数情報

~~~json
{
  "address": "00bbaca8",
  "name": "std::bad_alloc::bad_alloc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69d939e11965d4e9afffad669cb30fd73c0b3c97ed64e8779841097b896a7af7",
  "source_text_sha256": "69d939e11965d4e9afffad669cb30fd73c0b3c97ed64e8779841097b896a7af7"
}
~~~
## 呼び出し元

- [00bdbaf0](../00bdb/00bdbaf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 613 bytes

~~~c

/* std::bad_alloc::bad_alloc() */

void __thiscall std::bad_alloc::bad_alloc(bad_alloc *this)

{
                    /* catch() { ... } // from try @ 00bb45ec with catch @ 00bbacac */
                    /* catch() { ... } // from try @ 00bb7594 with catch @ 00bbacb0 */
                    /* catch() { ... } // from try @ 00bb75ac with catch @ 00bbacb4 */
                    /* catch() { ... } // from try @ 00bb71e4 with catch @ 00bbacb8 */
  *(undefined **)this = PTR_vtable_00c1bf18 + 0x10;
                    /* catch() { ... } // from try @ 00bb71fc with catch @ 00bbacbc */
  return;
}

~~~
