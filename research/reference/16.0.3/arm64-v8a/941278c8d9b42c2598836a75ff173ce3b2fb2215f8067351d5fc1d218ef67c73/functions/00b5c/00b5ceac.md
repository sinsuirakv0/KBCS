# 00b5ceac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b5ceac",
  "name": "_ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5150549079e943c0218f5b1d22dcd499ab4f9bb70695e237f27ca6feb79d80c2",
  "source_text_sha256": "5150549079e943c0218f5b1d22dcd499ab4f9bb70695e237f27ca6feb79d80c2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596c0](../00c59/00c596c0.md)
- [00c5cb90](../00c5c/00c5cb90.md)
- [00c5cbf0](../00c5c/00c5cbf0.md)
- [00c5cc00](../00c5c/00c5cc00.md)
- [00c5cc10](../00c5c/00c5cc10.md)
- [00c5cc30](../00c5c/00c5cc30.md)

## 疑似コード / UTF-8 1355 bytes

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
  if (DAT_011270b8 == '\x01') {
    __thread1 = pthread_self();
    if ((__thread1 == 0) || (DAT_011270c0 == 0)) {
      if (DAT_011270c0 != 0 || __thread1 != 0) goto LAB_00b5cf2c;
    }
    else {
      iVar3 = pthread_equal(__thread1,DAT_011270c0);
      if (iVar3 == 0) goto LAB_00b5cf2c;
    }
    uVar5 = (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
      uVar5 = (**(code **)(*param_1 + 8))(param_1);
    }
  }
  else {
LAB_00b5cf2c:
    local_50[0] = (sem_t *)(local_50 + 1);
    sem_init(local_50[0],0,0);
    plVar6 = (long *)_Znwm(0x18);
    puVar2 = PTR__ZTVN8firebase8callback16BlockingCallbackE_00c9c820;
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
