# 00aeae2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aeae2c",
  "name": "_ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2143cce59006ce100954b483854bbb002173e1fc9e722566a9c2206d76f8ba59",
  "source_text_sha256": "2143cce59006ce100954b483854bbb002173e1fc9e722566a9c2206d76f8ba59"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 508 bytes

~~~c

void _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0810 != 0) {
    if (DAT_010a0818 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0818 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0810);
    DAT_010a0810 = 0;
  }
  return;
}

~~~
