# 00bbac6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbac6c.md)

## 関数情報

~~~json
{
  "address": "00bbac6c",
  "name": "std::bad_exception::~bad_exception",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00c75ec8565de1a43f55fd31055e9183d38216b9c17fa8b498ef08d7de4d3221",
  "source_text_sha256": "00c75ec8565de1a43f55fd31055e9183d38216b9c17fa8b498ef08d7de4d3221"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1d50](../00be1/00be1d50.md)

## 疑似コード 1/1 / UTF-8 1381 bytes

~~~c

/* std::bad_exception::~bad_exception() */

void __thiscall std::bad_exception::~bad_exception(bad_exception *this)

{
                    /* catch() { ... } // from try @ 00bba0c8 with catch @ 00bbac70
                       catch() { ... } // from try @ 00bba218 with catch @ 00bbac70 */
                    /* catch() { ... } // from try @ 00bba0b0 with catch @ 00bbac74
                       catch() { ... } // from try @ 00bba200 with catch @ 00bbac74 */
                    /* catch() { ... } // from try @ 00bba094 with catch @ 00bbac78
                       catch() { ... } // from try @ 00bba1e8 with catch @ 00bbac78 */
                    /* catch() { ... } // from try @ 00bb7698 with catch @ 00bbac7c */
                    /* catch() { ... } // from try @ 00bb72e8 with catch @ 00bbac80 */
  bad_array_new_length::~bad_array_new_length((bad_array_new_length *)this);
                    /* catch() { ... } // from try @ 00bb6f34 with catch @ 00bbac84 */
                    /* catch() { ... } // from try @ 00bb6b80 with catch @ 00bbac88 */
                    /* catch() { ... } // from try @ 00bb67cc with catch @ 00bbac8c */
                    /* catch() { ... } // from try @ 00bb6418 with catch @ 00bbac90 */
                    /* catch() { ... } // from try @ 00bb6064 with catch @ 00bbac94 */
  operator_delete(this);
  return;
}

~~~
