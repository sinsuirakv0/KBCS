# 00aecbb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aecbb0.md)

## 関数情報

~~~json
{
  "address": "00aecbb0",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6015ebc3d0f590f5ba960a70ad89f920522a56f7176b725409a6622649a81f4b",
  "source_text_sha256": "6015ebc3d0f590f5ba960a70ad89f920522a56f7176b725409a6622649a81f4b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 620 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
                    /* try { // try from 00aecbb4 to 00becbc3 has its CatchHandler @ 00af1a84 */
  if (DAT_010a09a8 != 0) {
    if (DAT_010a09b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a09b0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a09a8);
    DAT_010a09a8 = 0;
  }
  return;
}

~~~
