# 00bab1bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bab0b0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab0b0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bab1bc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528",
  "source_text_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1580](../00be1/00be1580.md)
- [00be1b10](../00be1/00be1b10.md)

## 疑似コード / UTF-8 449 bytes

~~~c

int _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc(long param_1,wint_t param_2,int param_3)

{
  int iVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  iVar1 = wctob(param_2);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  if (iVar1 != -1) {
    param_3 = iVar1;
  }
                    /* try { // try from 00bab210 to 00cab21b has its CatchHandler @ 00bab494 */
  return param_3;
}

~~~
