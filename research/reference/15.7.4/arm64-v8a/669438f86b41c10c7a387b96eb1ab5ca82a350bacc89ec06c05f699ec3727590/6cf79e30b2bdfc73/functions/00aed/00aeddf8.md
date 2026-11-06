# 00aeddf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aeddf8.md)

## 関数情報

~~~json
{
  "address": "00aeddf8",
  "name": "_ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed34ff4736e415cbdb390da2539337b84b9920fd5d1fb3fa2daee090e22a58cc",
  "source_text_sha256": "ed34ff4736e415cbdb390da2539337b84b9920fd5d1fb3fa2daee090e22a58cc"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0a60 != 0) {
    if (DAT_010a0a68 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0a68 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0a60);
    DAT_010a0a60 = 0;
  }
  return;
}

~~~
