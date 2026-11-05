# 00baaf8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaf8c.md)

## 関数情報

~~~json
{
  "address": "00baaf8c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE8do_widenEc",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b66b908968eaaa4169a67308ae0ede514c0387b3e9bedf61bd0215e386f34552",
  "source_text_sha256": "b66b908968eaaa4169a67308ae0ede514c0387b3e9bedf61bd0215e386f34552"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

## 疑似コード 1/1 / UTF-8 301 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc(long param_1,uint param_2)

{
  wint_t wVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  wVar1 = btowc(param_2 & 0xff);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  return wVar1;
}

~~~
