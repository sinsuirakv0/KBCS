# 00b4ddec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b4ddec",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c7da6c31876c9fbd0abdf50670e05d17a9ec9cecb550dedfd46ff54a083063e",
  "source_text_sha256": "9c7da6c31876c9fbd0abdf50670e05d17a9ec9cecb550dedfd46ff54a083063e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 523 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01126d28 != 0) {
    if (DAT_01126d30 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126d30 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126d28);
    DAT_01126d28 = 0;
  }
  return;
}

~~~
