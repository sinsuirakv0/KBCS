# 00baeffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00baeffc.md)

## 関数情報

~~~json
{
  "address": "00baeffc",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4050c51bece412fd7c60ff1def9d0c32140759c11c5fe670b0e0ab81ae8ca733",
  "source_text_sha256": "4050c51bece412fd7c60ff1def9d0c32140759c11c5fe670b0e0ab81ae8ca733"
}
~~~
## 呼び出し元

- [00be1810](../00be1/00be1810.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c1bfb8;
  *(undefined2 *)(param_1 + 2) = 0x2c2e;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~
