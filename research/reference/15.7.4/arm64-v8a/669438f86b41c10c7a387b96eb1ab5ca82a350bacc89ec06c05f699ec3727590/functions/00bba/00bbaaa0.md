# 00bbaaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bba994`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba994.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbaaa0",
  "name": "_ZSt15get_new_handlerv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e",
  "source_text_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e"
}
~~~

## 呼び出し元

- [00be1e20](../00be1/00be1e20.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 277 bytes

~~~c

undefined8 _ZSt15get_new_handlerv(void)

{
                    /* catch() { ... } // from try @ 00bb34c4 with catch @ 00bbaaac */
                    /* catch() { ... } // from try @ 00bb3490 with catch @ 00bbaab0 */
  return *(undefined8 *)PTR___cxa_new_handler_00c1c008;
}

~~~
