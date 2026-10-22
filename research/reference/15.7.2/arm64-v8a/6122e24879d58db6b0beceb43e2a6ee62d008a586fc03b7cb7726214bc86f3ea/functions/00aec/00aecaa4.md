# 00aecaa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecaa4.md)

## 関数情報

~~~json
{
  "address": "00aecaa4",
  "name": "firebase::util::parcel_file_descriptor::ReleaseClass",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cea6a36502dae9122d119cbab576101d0ecd6319bb791d05a45ca78dd2962fe0",
  "source_text_sha256": "cea6a36502dae9122d119cbab576101d0ecd6319bb791d05a45ca78dd2962fe0"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 843 bytes

~~~c

/* firebase::util::parcel_file_descriptor::ReleaseClass(_JNIEnv*) */

void firebase::util::parcel_file_descriptor::ReleaseClass(_JNIEnv *param_1)

{
  char cVar1;
  
  if (DAT_010a08a8 != 0) {
                    /* try { // try from 00aecacc to 00becad7 has its CatchHandler @ 00af1898 */
    if (DAT_010a08b0 != '\0') {
      (**(code **)(*(long *)param_1 + 0x6c0))(param_1);
      DAT_010a08b0 = '\0';
    }
                    /* try { // try from 00aecae8 to 00becaef has its CatchHandler @ 00af1a38 */
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    (**(code **)(*(long *)param_1 + 0xb0))(param_1,DAT_010a08a8);
    DAT_010a08a8 = 0;
  }
  return;
}

~~~
