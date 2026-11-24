# 00bbafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbaf50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0079.md#compare-4c3152d5c81e7c53f46cc1d3a2f444bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0091.md#compare-bc12d65634f308657ee61f83d53c52eb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
