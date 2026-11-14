# 00bbbfe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbbfe0",
  "name": "FUN_00bbbfe0",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a1fa926a65111dd2003adfdaa256d85f2cfd32fd545f18b86af06a50091e2ed",
  "source_text_sha256": "9a1fa926a65111dd2003adfdaa256d85f2cfd32fd545f18b86af06a50091e2ed"
}
~~~

## 呼び出し元

- [00bbb6b8](../00bbb/00bbb6b8.md)
- [00bbbe34](../00bbb/00bbbe34.md)

## 呼び出し先

- [0087c3c0](../0087c/0087c3c0.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5e660](../00c5e/00c5e660.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1343 bytes

~~~c

void FUN_00bbbfe0(void)

{
  long lVar1;
  undefined8 *puVar2;
  undefined1 auStack_80 [24];
  undefined1 auStack_68 [40];
  long *local_40;
  undefined1 auStack_38 [16];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_01127420 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
      puVar2 = (undefined8 *)_Znwm(0x10);
      *puVar2 = FUN_00bbe428;
      puVar2[1] = 0;
      (**(code **)(*local_40 + 0x40))
                (auStack_80,local_40,auStack_38,
                 PTR__ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv_00c9c9b0
                 ,puVar2,
                 PTR__ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c9c9a8
                 ,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
    FUN_0087c3c0(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
