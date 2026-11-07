# 00af8bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00af8cf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af8/00af8cf8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00af8bec",
  "name": "_ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5099c55f14fd35940836c12529c39ed06d32fa32b583df20577af1fbb0ac8a92",
  "source_text_sha256": "5099c55f14fd35940836c12529c39ed06d32fa32b583df20577af1fbb0ac8a92"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 959 bytes

~~~c

void _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject
               (undefined8 *param_1,long *param_2,long param_3)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if ((param_2 != (long *)0x0) && (param_1[1] != 0)) {
    (**(code **)(*param_2 + 0xb0))(param_2);
  }
                    /* try { // try from 00af8c34 to 00bf8c3f has its CatchHandler @ 00aff768 */
  param_1[1] = 0;
  local_40 = 0;
                    /* try { // try from 00af8c40 to 00bf8c53 has its CatchHandler @ 00aff764 */
  (**(code **)(*param_2 + 0x6d8))(param_2,&local_40);
  *param_1 = local_40;
  param_1[1] = 0;
  if (param_3 != 0) {
    uVar2 = (**(code **)(*param_2 + 0xa8))(param_2,param_3);
    param_1[1] = uVar2;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
