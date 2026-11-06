# 00aebfac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aebfac",
  "name": "_ZN8firebase4util4list12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53ad75a8a3c8c20b330439316649414bc16d4e934a20cc9b4d0c2716e6669085",
  "source_text_sha256": "53ad75a8a3c8c20b330439316649414bc16d4e934a20cc9b4d0c2716e6669085"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 601 bytes

~~~c

void _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0820 != 0) {
    if (DAT_010a0828 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0828 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0820);
    DAT_010a0820 = 0;
  }
                    /* try { // try from 00aec03c to 00bec047 has its CatchHandler @ 00af1b68 */
  return;
}

~~~
