# 00bbaec8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaec8.md)

## 関数情報

~~~json
{
  "address": "00bbaec8",
  "name": "std::length_error::~length_error",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "66bc0765082f7cd3d1a557523585afa528b304d03114a7ce3301419246312351",
  "source_text_sha256": "66bc0765082f7cd3d1a557523585afa528b304d03114a7ce3301419246312351"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdafb0](../00bda/00bdafb0.md)

## 疑似コード 1/1 / UTF-8 410 bytes

~~~c

/* std::length_error::~length_error() */

void __thiscall std::length_error::~length_error(length_error *this)

{
  logic_error::~logic_error((logic_error *)this);
                    /* try { // try from 00bbaee4 to 00cbaeef has its CatchHandler @ 00bbb7c8 */
                    /* try { // try from 00bbaef0 to 00cbaeff has its CatchHandler @ 00bbb790 */
  operator_delete(this);
  return;
}

~~~
