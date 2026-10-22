# 00ae7ddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae7ddc.md)

## 関数情報

~~~json
{
  "address": "00ae7ddc",
  "name": "firebase::util::boolean_class::ReleaseClass",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "abcfb0b1c675a434f8796f82a90e166680e8e5f5cbf67075e5b91e858ca4a1eb",
  "source_text_sha256": "abcfb0b1c675a434f8796f82a90e166680e8e5f5cbf67075e5b91e858ca4a1eb"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1021 bytes

~~~c

/* firebase::util::boolean_class::ReleaseClass(_JNIEnv*) */

void firebase::util::boolean_class::ReleaseClass(_JNIEnv *param_1)

{
  char cVar1;
  
  if (DAT_010a04c0 != 0) {
                    /* try { // try from 00ae7df8 to 00be7e03 has its CatchHandler @ 00ae8c20 */
    if (DAT_010a04c8 != '\0') {
                    /* try { // try from 00ae7e08 to 00be7e17 has its CatchHandler @ 00ae8c1c */
      (**(code **)(*(long *)param_1 + 0x6c0))(param_1);
      DAT_010a04c8 = '\0';
    }
                    /* try { // try from 00ae7e1c to 00be7e2f has its CatchHandler @ 00ae8c08 */
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7e48 to 00be7e4f has its CatchHandler @ 00ae8bf0 */
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    (**(code **)(*(long *)param_1 + 0xb0))(param_1,DAT_010a04c0);
    DAT_010a04c0 = 0;
  }
  return;
}

~~~
