# 00af8bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af8bec.md)

## 関数情報

~~~json
{
  "address": "00af8bec",
  "name": "firebase::internal::JObjectReference::Set",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "449e5cf4d87a2ae268551d5927a4a270eec0af84584978deba5f9ffa9d9dbb43",
  "source_text_sha256": "449e5cf4d87a2ae268551d5927a4a270eec0af84584978deba5f9ffa9d9dbb43"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1154 bytes

~~~c

/* firebase::internal::JObjectReference::Set(_JNIEnv*, _jobject*) */

void __thiscall
firebase::internal::JObjectReference::Set(JObjectReference *this,_JNIEnv *param_1,_jobject *param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if ((param_1 != (_JNIEnv *)0x0) && (*(long *)(this + 8) != 0)) {
    (**(code **)(*(long *)param_1 + 0xb0))(param_1);
  }
                    /* try { // try from 00af8c34 to 00bf8c3f has its CatchHandler @ 00aff768 */
  *(undefined8 *)(this + 8) = 0;
  local_40 = 0;
                    /* try { // try from 00af8c40 to 00bf8c53 has its CatchHandler @ 00aff764 */
  (**(code **)(*(long *)param_1 + 0x6d8))(param_1,&local_40);
  *(undefined8 *)this = local_40;
  *(undefined8 *)(this + 8) = 0;
  if (param_2 != (_jobject *)0x0) {
    uVar2 = (**(code **)(*(long *)param_1 + 0xa8))(param_1,param_2);
    *(undefined8 *)(this + 8) = uVar2;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
