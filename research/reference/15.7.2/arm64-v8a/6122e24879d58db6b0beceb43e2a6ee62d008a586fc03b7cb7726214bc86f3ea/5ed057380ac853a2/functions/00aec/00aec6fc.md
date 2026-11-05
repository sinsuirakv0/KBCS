# 00aec6fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aec6fc.md)

## 関数情報

~~~json
{
  "address": "00aec6fc",
  "name": "_ZN8firebase4util3map12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb3f6321f0a4505243facb2544bb804d178d9072cdb1c4ee8bd9cc3f9385fe25",
  "source_text_sha256": "eb3f6321f0a4505243facb2544bb804d178d9072cdb1c4ee8bd9cc3f9385fe25"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0878 != 0) {
    if (DAT_010a0880 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0880 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0878);
    DAT_010a0878 = 0;
  }
  return;
}

~~~
