# 00b6babc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b6babc.md)

## 関数情報

~~~json
{
  "address": "00b6babc",
  "name": "firebase::auth::JniAuthPhoneListener::nativeOnCodeAutoRetrievalTimeOut",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64e6f14d7a57e45f3a29bc66d1a84d83436af004080dc73cdd95ae60dd7bf64b",
  "source_text_sha256": "64e6f14d7a57e45f3a29bc66d1a84d83436af004080dc73cdd95ae60dd7bf64b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde410](../00bde/00bde410.md)

## 疑似コード 1/1 / UTF-8 996 bytes

~~~c

/* firebase::auth::JniAuthPhoneListener::nativeOnCodeAutoRetrievalTimeOut(_JNIEnv*, _jobject*, long,
   _jstring*) */

void firebase::auth::JniAuthPhoneListener::nativeOnCodeAutoRetrievalTimeOut
               (_JNIEnv *param_1,_jobject *param_2,long param_3,_jstring *param_4)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  util::JniStringToString((util *)param_1,(_JNIEnv *)param_4,(_jobject *)param_3);
                    /* try { // try from 00b6baf4 to 00c6bb0b has its CatchHandler @ 00b6bcf8 */
  (**(code **)(*(long *)param_3 + 0x28))(param_3,local_40);
  if ((local_40[0] & 1) != 0) {
    operator_delete(local_30);
  }
                    /* try { // try from 00b6bb14 to 00c6bb43 has its CatchHandler @ 00b6bd54 */
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
