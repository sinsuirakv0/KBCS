# 00bd5ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bd5ccc",
  "name": "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5f7f433c47db5903671a92f4b6c789d65c12267216ea3b4a8e423c0f288cd4c",
  "source_text_sha256": "f5f7f433c47db5903671a92f4b6c789d65c12267216ea3b4a8e423c0f288cd4c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bad0](../00c5b/00c5bad0.md)
- [00c5baf0](../00c5b/00c5baf0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5ee50](../00c5e/00c5ee50.md)

## 疑似コード / UTF-8 1427 bytes

~~~c

void _ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv
               (long param_1,long param_2,ulong param_3,undefined8 param_4)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  undefined1 auStack_f8 [160];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x10));
  if ((param_1 != 0) && ((param_3 & 1) != 0)) {
    lVar3 = FUN_00497b94(plVar2,param_1,DAT_01127918);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
    lVar5 = *(long *)(param_2 + 0x10);
    if (*(long *)(lVar5 + 0x200) != 0) {
      (**(code **)(*plVar2 + 0xb0))(plVar2);
      *(undefined8 *)(lVar5 + 0x200) = 0;
    }
    if (lVar3 != 0) {
      uVar4 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar3);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar3);
      *(undefined8 *)(lVar5 + 0x200) = uVar4;
    }
  }
  _ZN8firebase4auth4Auth12current_userEv(auStack_f8,*(undefined8 *)(*(long *)(param_2 + 0x10) + 8));
  _ZN8firebase4auth4UseraSERKS1_(param_4,auStack_f8);
                    /* try { // try from 00bd5dac to 00cd5f97 has its CatchHandler @ 00bd7a18 */
  _ZN8firebase4auth4UserD2Ev(auStack_f8);
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
