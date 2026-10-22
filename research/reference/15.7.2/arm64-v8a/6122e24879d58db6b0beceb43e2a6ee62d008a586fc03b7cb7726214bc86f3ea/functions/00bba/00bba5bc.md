# 00bba5bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bba5bc.md)

## 関数情報

~~~json
{
  "address": "00bba5bc",
  "name": "__cxa_throw_bad_array_new_length",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0f8a2d9b397cc0cf983dc41cb04d6b548deea01eb97c0095b38b3f85a8c42c9",
  "source_text_sha256": "d0f8a2d9b397cc0cf983dc41cb04d6b548deea01eb97c0095b38b3f85a8c42c9"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdafa0](../00bda/00bdafa0.md)
- [00bdafc0](../00bda/00bdafc0.md)
- [00bdb0e0](../00bdb/00bdb0e0.md)

## 疑似コード 1/1 / UTF-8 619 bytes

~~~c

void __cxa_throw_bad_array_new_length(void)

{
  bad_array_new_length *this;
  
                    /* catch() { ... } // from try @ 00bb6d68 with catch @ 00bba5cc */
  this = (bad_array_new_length *)__cxa_allocate_exception(8);
  std::bad_array_new_length::bad_array_new_length(this);
                    /* catch() { ... } // from try @ 00bb6d5c with catch @ 00bba5e0 */
                    /* catch() { ... } // from try @ 00bb69c4 with catch @ 00bba5e4 */
                    /* WARNING: Subroutine does not return */
  __cxa_throw(this,PTR_typeinfo_00c1ace0,PTR__bad_array_new_length_00c1ace8);
}

~~~
