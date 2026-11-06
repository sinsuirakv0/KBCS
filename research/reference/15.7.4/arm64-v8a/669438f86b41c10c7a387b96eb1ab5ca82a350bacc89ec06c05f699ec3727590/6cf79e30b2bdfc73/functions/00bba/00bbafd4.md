# 00bbafd4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbafd4.md)

## 関数情報

~~~json
{
  "address": "00bbafd4",
  "name": "_ZNSt12length_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a574187e8e657dcd6789b89616a66bac3c60637a6084ba6382fabd225757976c",
  "source_text_sha256": "a574187e8e657dcd6789b89616a66bac3c60637a6084ba6382fabd225757976c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 疑似コード 1/1 / UTF-8 302 bytes

~~~c

void _ZNSt12length_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
                    /* try { // try from 00bbaff0 to 00cbaffb has its CatchHandler @ 00bbb8d4 */
                    /* try { // try from 00bbaffc to 00cbb00b has its CatchHandler @ 00bbb89c */
  _ZdlPv(param_1);
  return;
}

~~~
