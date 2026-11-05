# 00aedcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aedcec.md)

## 関数情報

~~~json
{
  "address": "00aedcec",
  "name": "_ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e02cc55d42c6fca49b1ed4b92ced25df40cb13d2f0f926736c98d4c7ceb96e6",
  "source_text_sha256": "1e02cc55d42c6fca49b1ed4b92ced25df40cb13d2f0f926736c98d4c7ceb96e6"
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
  
  if (DAT_010a0960 != 0) {
    if (DAT_010a0968 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0968 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0960);
    DAT_010a0960 = 0;
  }
  return;
}

~~~
