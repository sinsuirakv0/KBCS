# 00baece0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00baedec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baedec.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00baece0",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da5a424c7b74816960d92f78e8c319b2b1b75a45fbe465f432da523cb6a7b040",
  "source_text_sha256": "da5a424c7b74816960d92f78e8c319b2b1b75a45fbe465f432da523cb6a7b040"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 206 bytes

~~~c

undefined4 _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x18) & 4) != 0) {
    uVar1 = 7;
  }
  return uVar1;
}

~~~
