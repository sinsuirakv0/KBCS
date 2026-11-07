# 00aecaa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aecbb0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aecaa4",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1054a99ff487b417f60624aa848bc4003c8d135c306c9db2902a5de03d41b8b6",
  "source_text_sha256": "1054a99ff487b417f60624aa848bc4003c8d135c306c9db2902a5de03d41b8b6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 717 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a08a8 != 0) {
                    /* try { // try from 00aecacc to 00becad7 has its CatchHandler @ 00af1898 */
    if (DAT_010a08b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a08b0 = '\0';
    }
                    /* try { // try from 00aecae8 to 00becaef has its CatchHandler @ 00af1a38 */
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a08a8);
    DAT_010a08a8 = 0;
  }
  return;
}

~~~
