# 00bd4fbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bd4fbc",
  "name": "_ZdaPvSt11align_val_t",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb1d7e0ec5098b7df0ab981a2e64ed4cdae378704644dd6f7f59f498049ac8c5",
  "source_text_sha256": "cb1d7e0ec5098b7df0ab981a2e64ed4cdae378704644dd6f7f59f498049ac8c5"
}
~~~

## 呼び出し元

- [00be1f40](../00be1/00be1f40.md)

## 呼び出し先

- [00be1f30](../00be1/00be1f30.md)

## 疑似コード / UTF-8 167 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdaPvSt11align_val_t(void *__ptr)

{
  _ZdlPvSt11align_val_t(__ptr);
  return;
}

~~~
