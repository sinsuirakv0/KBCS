# 00bbaef4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaef4.md)

## 関数情報

~~~json
{
  "address": "00bbaef4",
  "name": "std::out_of_range::~out_of_range",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18e7ab8fc457c6bd755efeefc7eb5694c7fcc5ef41dd3df5a266c0e4f426050d",
  "source_text_sha256": "18e7ab8fc457c6bd755efeefc7eb5694c7fcc5ef41dd3df5a266c0e4f426050d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb150](../00bdb/00bdb150.md)

## 疑似コード 1/1 / UTF-8 312 bytes

~~~c

/* std::out_of_range::~out_of_range() */

void __thiscall std::out_of_range::~out_of_range(out_of_range *this)

{
                    /* try { // try from 00bbaf00 to 00cbaf13 has its CatchHandler @ 00bbb778 */
  logic_error::~logic_error((logic_error *)this);
  operator_delete(this);
  return;
}

~~~
