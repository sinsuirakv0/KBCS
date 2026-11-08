# 00ae5dbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae5dbc",
  "name": "_ZN8firebase4util3log12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f179d79431745754eaadfe5cd77fe8b81e06911a0ae90f354c3162a0b500948",
  "source_text_sha256": "4f179d79431745754eaadfe5cd77fe8b81e06911a0ae90f354c3162a0b500948"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 697 bytes

~~~c

void _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a03d8 != 0) {
                    /* try { // try from 00ae5de4 to 00be5deb has its CatchHandler @ 00ae5ee4 */
    if (DAT_010a03e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a03e0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a03d8);
    DAT_010a03d8 = 0;
  }
                    /* try { // try from 00ae5e58 to 00be5e5f has its CatchHandler @ 00ae5ee8 */
  return;
}

~~~
