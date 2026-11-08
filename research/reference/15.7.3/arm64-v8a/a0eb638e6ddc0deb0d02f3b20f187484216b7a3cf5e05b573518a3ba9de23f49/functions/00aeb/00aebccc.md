# 00aebccc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aebccc",
  "name": "_ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e719b4cd04c57461a9760ba51773225c6baba5d8b9424eed28d3d56992f464a",
  "source_text_sha256": "3e719b4cd04c57461a9760ba51773225c6baba5d8b9424eed28d3d56992f464a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 508 bytes

~~~c

void _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a08b8 != 0) {
    if (DAT_010a08c0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a08c0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a08b8);
    DAT_010a08b8 = 0;
  }
  return;
}

~~~
