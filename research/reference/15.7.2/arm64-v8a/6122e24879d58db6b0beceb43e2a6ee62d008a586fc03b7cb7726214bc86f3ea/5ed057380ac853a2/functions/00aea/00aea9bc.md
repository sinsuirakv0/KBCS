# 00aea9bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aea9bc.md)

## 関数情報

~~~json
{
  "address": "00aea9bc",
  "name": "_ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "27bfc38a9cf324673dce9334da7470ab852ed12382d03542e733ce2c9249a8e3",
  "source_text_sha256": "27bfc38a9cf324673dce9334da7470ab852ed12382d03542e733ce2c9249a8e3"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 599 bytes

~~~c

void _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0728 != 0) {
    if (DAT_010a0730 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0730 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
                    /* catch() { ... } // from try @ 00aeac14 with catch @ 00aeaa38 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0728);
    DAT_010a0728 = 0;
  }
  return;
}

~~~
