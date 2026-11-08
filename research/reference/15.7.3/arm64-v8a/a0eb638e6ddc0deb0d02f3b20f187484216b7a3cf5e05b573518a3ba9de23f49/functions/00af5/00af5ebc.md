# 00af5ebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00af5ebc",
  "name": "_ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7578960214fbb73b11328c9113b23c532ceca2f5e0d0103459447f4b910222c8",
  "source_text_sha256": "7578960214fbb73b11328c9113b23c532ceca2f5e0d0103459447f4b910222c8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bde050](../00bde/00bde050.md)
- [00bde7d0](../00bde/00bde7d0.md)
- [00bde7e0](../00bde/00bde7e0.md)

## 疑似コード / UTF-8 1588 bytes

~~~c

void _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll
               (long *param_1,undefined8 param_2,undefined8 param_3,char param_4,char param_5,
               undefined8 param_6,code *param_7,long *param_8)

{
  void *pvVar1;
  long *__ptr;
  long lVar2;
  long lVar3;
  long lVar4;
  long lVar5;
  undefined4 uVar6;
  byte local_80 [16];
  void *local_70;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
                    /* try { // try from 00af5ee8 to 00bf5eef has its CatchHandler @ 00affb10 */
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a0a88);
  lVar3 = param_8[1];
  uVar6 = 1;
  *(undefined1 *)(param_8 + 4) = 1;
  if (*param_8 != 0) {
    (**(code **)(*param_1 + 0xb0))(param_1);
    __ptr = (long *)param_8[2];
    lVar4 = param_8[3];
    lVar2 = *__ptr;
    *(long *)(lVar2 + 8) = __ptr[1];
    *(long *)__ptr[1] = lVar2;
    *(long *)(lVar4 + 0x10) = *(long *)(lVar4 + 0x10) + -1;
    _ZdlPv(__ptr);
  }
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a0a88);
  _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(local_80,param_1,param_6);
  if (param_5 != '\0') {
    uVar6 = 2;
  }
  if (param_4 != '\0') {
    uVar6 = 0;
  }
  pvVar1 = (void *)((ulong)local_80 | 1);
  if ((local_80[0] & 1) != 0) {
    pvVar1 = local_70;
  }
  (*param_7)(param_1,param_3,uVar6,pvVar1,lVar3);
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar5 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
