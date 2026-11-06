# 00b4afdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b4afdc.md)

## 関数情報

~~~json
{
  "address": "00b4afdc",
  "name": "_ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3",
  "source_text_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

## 疑似コード 1/1 / UTF-8 698 bytes

~~~c

void _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00b4aff4 to 00c4afff has its CatchHandler @ 00b4b1b0 */
  if (DAT_010a1058 != 0) {
    if (DAT_010a1060 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a1060 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00b4b024 to 00c4b02f has its CatchHandler @ 00b4b188 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a1058);
    DAT_010a1058 = 0;
  }
                    /* try { // try from 00b4b044 to 00c4b04f has its CatchHandler @ 00b4b184 */
  return;
}

~~~
