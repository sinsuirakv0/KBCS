# 00baaeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baaeac.md)

## 関数情報

~~~json
{
  "address": "00baaeac",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEw",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84ac7bc31c266b3a170f5cb24f7a8a4fd0ca4633baa57a04de051e811182cfbd",
  "source_text_sha256": "84ac7bc31c266b3a170f5cb24f7a8a4fd0ca4633baa57a04de051e811182cfbd"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be19e0](../00be1/00be19e0.md)

## 疑似コード 1/1 / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towupper_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~
