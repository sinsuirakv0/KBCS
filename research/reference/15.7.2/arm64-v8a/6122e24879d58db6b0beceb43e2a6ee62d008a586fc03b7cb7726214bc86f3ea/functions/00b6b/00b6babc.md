# 00b6babc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b6bbc8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bbc8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b6babc",
  "name": "_ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "189ba4e074b3b982830eff58ff642190835d832c0cfbb03bb8edfd78bffcb496",
  "source_text_sha256": "189ba4e074b3b982830eff58ff642190835d832c0cfbb03bb8edfd78bffcb496"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde410](../00bde/00bde410.md)

## 疑似コード / UTF-8 873 bytes

~~~c

void _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring
               (undefined8 param_1,undefined8 param_2,long *param_3,undefined8 param_4)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(local_40,param_1,param_4);
                    /* try { // try from 00b6baf4 to 00c6bb0b has its CatchHandler @ 00b6bcf8 */
  (**(code **)(*param_3 + 0x28))(param_3,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
                    /* try { // try from 00b6bb14 to 00c6bb43 has its CatchHandler @ 00b6bd54 */
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
