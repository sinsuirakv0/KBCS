# 00beffb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00beffb4",
  "name": "_ZNSt6__ndk112bad_weak_ptrD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06",
  "source_text_sha256": "b61dccad7ab163de2d3dc60bbf4bccabaff1d67e9eb0b6bca32fe292b450fe06"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5a390](../00c5a/00c5a390.md)

## 疑似コード / UTF-8 317 bytes

~~~c

void _ZNSt6__ndk112bad_weak_ptrD0Ev(void *param_1)

{
                    /* try { // try from 00beffb8 to 00ceffdb has its CatchHandler @ 00bf006c */
  _ZNSt6__ndk112bad_weak_ptrD2Ev();
                    /* try { // try from 00beffdc to 00cf016b has its CatchHandler @ 00befce0 */
  _ZdlPv(param_1);
  return;
}

~~~
