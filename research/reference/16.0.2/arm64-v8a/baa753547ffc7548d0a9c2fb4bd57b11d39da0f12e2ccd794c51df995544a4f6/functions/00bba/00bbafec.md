# 00bbafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbafec",
  "name": "FUN_00bbafec",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b7bcd5fa9b252715451d3cf3af988e1c53ea8bd24c29682bba192efc8472890",
  "source_text_sha256": "2b7bcd5fa9b252715451d3cf3af988e1c53ea8bd24c29682bba192efc8472890"
}
~~~

## 呼び出し元

- [00bba6c4](../00bba/00bba6c4.md)
- [00bbae40](../00bba/00bbae40.md)

## 呼び出し先

- [0087b414](../0087b/0087b414.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5d690](../00c5d/00c5d690.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1343 bytes

~~~c

void FUN_00bbafec(void)

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
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
      puVar2 = (undefined8 *)_Znwm(0x10);
      *puVar2 = FUN_00bbd434;
      puVar2[1] = 0;
      (**(code **)(*local_40 + 0x40))
                (auStack_80,local_40,auStack_38,
                 PTR__ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv_00c9b9e0
                 ,puVar2,
                 PTR__ZN8firebase6detail33DeleteTypedCompletionCallbackDataINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c9b9d8
                 ,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
    FUN_0087b414(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
