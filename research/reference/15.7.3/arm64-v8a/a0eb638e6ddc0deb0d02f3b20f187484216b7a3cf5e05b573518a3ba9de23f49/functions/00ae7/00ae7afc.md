# 00ae7afc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae7afc",
  "name": "_ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72e82865c2e9adff28487d5ef7cc612c465d2807b25e5a8bfbf363e87cd4c787",
  "source_text_sha256": "72e82865c2e9adff28487d5ef7cc612c465d2807b25e5a8bfbf363e87cd4c787"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 716 bytes

~~~c

void _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0560 != 0) {
    if (DAT_010a0568 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0568 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7b6c to 00be7b6f has its CatchHandler @ 00ae8d98 */
                    /* try { // try from 00ae7b70 to 00be7d0b has its CatchHandler @ 00ae6000 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0560);
    DAT_010a0560 = 0;
  }
  return;
}

~~~
