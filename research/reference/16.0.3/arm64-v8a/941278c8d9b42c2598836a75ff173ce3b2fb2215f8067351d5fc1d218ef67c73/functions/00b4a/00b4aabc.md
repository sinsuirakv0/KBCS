# 00b4aabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b4aabc",
  "name": "_ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3cbbabe6f8f0b7dee8fc091fcd2107cc885076f7ec09c7124e6aa492cb224f7",
  "source_text_sha256": "c3cbbabe6f8f0b7dee8fc091fcd2107cc885076f7ec09c7124e6aa492cb224f7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 603 bytes

~~~c

void _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01126a98 != 0) {
    if (DAT_01126aa0 != '\0') {
                    /* try { // try from 00b4aaec to 00c4aaf7 has its CatchHandler @ 00b500c4 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126aa0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a98);
    DAT_01126a98 = 0;
  }
  return;
}

~~~
