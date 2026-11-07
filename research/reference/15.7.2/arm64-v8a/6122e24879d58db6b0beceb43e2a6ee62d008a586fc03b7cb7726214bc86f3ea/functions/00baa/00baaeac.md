# 00baaeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baafb8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baafb8.md)
<!-- /kbcs-version-next -->

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

## 疑似コード / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towupper_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~
