# 00aeaac8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aea9bc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea9bc.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aeaac8",
  "name": "_ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1f36e689659c81a222175c1834bf9a35fdbd7d79717816b328225282938d0a6",
  "source_text_sha256": "d1f36e689659c81a222175c1834bf9a35fdbd7d79717816b328225282938d0a6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0828 != 0) {
    if (DAT_010a0830 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0830 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0828);
    DAT_010a0828 = 0;
  }
  return;
}

~~~
