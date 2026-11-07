# 00bacf1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bace10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bace10.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bacf1c",
  "name": "_ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb741c22aa55fdca2c5fe28300e2f6e81bc58494b5f8a9f2f018d2f0284ff258",
  "source_text_sha256": "bb741c22aa55fdca2c5fe28300e2f6e81bc58494b5f8a9f2f018d2f0284ff258"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1be0](../00be1/00be1be0.md)

## 疑似コード / UTF-8 241 bytes

~~~c

void _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
                    /* try { // try from 00bacf34 to 00cacf3f has its CatchHandler @ 00bad064 */
  _ZdlPv(param_1);
  return;
}

~~~
