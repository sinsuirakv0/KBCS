# 00aecb6c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aecb6c",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72a9e0fa9b22e30594f1a9fdc2389fc93894842f29e4e057bc7c98a0285e7600",
  "source_text_sha256": "72a9e0fa9b22e30594f1a9fdc2389fc93894842f29e4e057bc7c98a0285e7600"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 620 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
                    /* try { // try from 00aecb70 to 00becb7f has its CatchHandler @ 00af1a40 */
  if (DAT_010a0968 != 0) {
    if (DAT_010a0970 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0970 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0968);
    DAT_010a0968 = 0;
  }
  return;
}

~~~
