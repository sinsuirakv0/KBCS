# 00afbc2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afbc2c",
  "name": "_ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c712b1cab17365974a8b8d6e38eb6c5692351caabc0aba147d7b0b38125aa0d2",
  "source_text_sha256": "c712b1cab17365974a8b8d6e38eb6c5692351caabc0aba147d7b0b38125aa0d2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb780](../00bdb/00bdb780.md)
- [00bdebe0](../00bde/00bdebe0.md)
- [00bdec40](../00bde/00bdec40.md)
- [00bdec50](../00bde/00bdec50.md)
- [00bdec60](../00bde/00bdec60.md)
- [00bdec80](../00bde/00bdec80.md)

## 疑似コード / UTF-8 1549 bytes

~~~c

void _ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE(long *param_1)

{
  long lVar1;
  undefined *puVar2;
  int iVar3;
  uint uVar4;
  pthread_t __thread1;
  ulong uVar5;
  long *plVar6;
  sem_t *local_50 [3];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_010a0cf8 == '\x01') {
    __thread1 = pthread_self();
    if ((__thread1 == 0) || (DAT_010a0d00 == 0)) {
      if (DAT_010a0d00 != 0 || __thread1 != 0) goto LAB_00afbcac;
    }
    else {
      iVar3 = pthread_equal(__thread1,DAT_010a0d00);
      if (iVar3 == 0) goto LAB_00afbcac;
    }
    uVar5 = (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbc98 to 00bfbcb3 has its CatchHandler @ 00aff410 */
      uVar5 = (**(code **)(*param_1 + 8))(param_1);
    }
  }
  else {
LAB_00afbcac:
    local_50[0] = (sem_t *)(local_50 + 1);
                    /* try { // try from 00afbcb4 to 00bfbd3f has its CatchHandler @ 00af560c */
    sem_init(local_50[0],0,0);
    plVar6 = (long *)_Znwm(0x18);
    puVar2 = PTR__ZTVN8firebase8callback16BlockingCallbackE_00c1b930;
    plVar6[2] = (long)local_50;
    *plVar6 = (long)(puVar2 + 0x10);
    plVar6[1] = (long)param_1;
    _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE();
    sem_wait(local_50[0]);
    uVar4 = sem_destroy(local_50[0]);
    uVar5 = (ulong)uVar4;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~
