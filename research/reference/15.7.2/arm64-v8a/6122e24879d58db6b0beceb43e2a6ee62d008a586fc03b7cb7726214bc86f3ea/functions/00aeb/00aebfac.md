# 00aebfac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebfac.md)

## 関数情報

~~~json
{
  "address": "00aebfac",
  "name": "firebase::util::list::ReleaseClass",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f25cc1977bff9581a9dda06dbf21d10a27382600dc26c1c324cf7bbc91c45783",
  "source_text_sha256": "f25cc1977bff9581a9dda06dbf21d10a27382600dc26c1c324cf7bbc91c45783"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 709 bytes

~~~c

/* firebase::util::list::ReleaseClass(_JNIEnv*) */

void firebase::util::list::ReleaseClass(_JNIEnv *param_1)

{
  char cVar1;
  
  if (DAT_010a0820 != 0) {
    if (DAT_010a0828 != '\0') {
      (**(code **)(*(long *)param_1 + 0x6c0))(param_1);
      DAT_010a0828 = '\0';
    }
    cVar1 = (**(code **)(*(long *)param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*(long *)param_1 + 0x80))(param_1);
      (**(code **)(*(long *)param_1 + 0x88))(param_1);
    }
    (**(code **)(*(long *)param_1 + 0xb0))(param_1,DAT_010a0820);
    DAT_010a0820 = 0;
  }
                    /* try { // try from 00aec03c to 00bec047 has its CatchHandler @ 00af1b68 */
  return;
}

~~~
