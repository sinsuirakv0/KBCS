# 00baaec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baafcc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baafcc.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baaec0",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c2cae7208b07b6eb0af53db6d0f78dff85246cf304637afe61772b385f6acb0",
  "source_text_sha256": "6c2cae7208b07b6eb0af53db6d0f78dff85246cf304637afe61772b385f6acb0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be19e0](../00be1/00be19e0.md)

## 疑似コード / UTF-8 638 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw
                   (long param_1,wint_t *param_2,wint_t *param_3)

{
  wint_t *pwVar1;
  wint_t wVar2;
  
  pwVar1 = param_2;
                    /* try { // try from 00baaedc to 00cab103 has its CatchHandler @ 00baaedc
                       catch() { ... } // from try @ 00baaedc with catch @ 00baaedc
                       catch() { ... } // from try @ 00bab110 with catch @ 00baaedc */
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    wVar2 = towupper_l(*param_2,*(__locale_t *)(param_1 + 0x10));
    *param_2 = wVar2;
    pwVar1 = param_3;
  }
  return pwVar1;
}

~~~
