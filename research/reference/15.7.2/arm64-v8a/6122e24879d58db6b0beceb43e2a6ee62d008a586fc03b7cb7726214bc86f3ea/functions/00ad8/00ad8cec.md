# 00ad8cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00ad8df8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8df8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00ad8cec",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f1f7f461c14eb610c983f6f92f52f7344a5b7181ee61e8e10f4978a1ed3290a0",
  "source_text_sha256": "f1f7f461c14eb610c983f6f92f52f7344a5b7181ee61e8e10f4978a1ed3290a0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 1800 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  byte local_58;
  undefined1 auStack_57 [15];
  undefined1 *local_48;
  undefined1 *local_40;
  long local_38;
  
                    /* catch() { ... } // from try @ 00ad8c38 with catch @ 00ad8cf4
                       catch() { ... } // from try @ 00ad8ce8 with catch @ 00ad8cf4
                       try { // try from 00ad8cf4 to 00bd8d27 has its CatchHandler @ 00ad8a6c */
                    /* catch() { ... } // from try @ 00ad8bd4 with catch @ 00ad8cf8
                       catch() { ... } // from try @ 00ad8ccc with catch @ 00ad8cf8 */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fdb0 != (long *)0x0) {
    FUN_00566a7c(&local_58,param_1,param_3);
                    /* try { // try from 00ad8d28 to 00bd8e8f has its CatchHandler @ 00ad8d28
                       catch() { ... } // from try @ 00ad8d28 with catch @ 00ad8d28
                       catch() { ... } // from try @ 00ad8ec0 with catch @ 00ad8d28
                       catch() { ... } // from try @ 00ad8fb0 with catch @ 00ad8d28 */
    local_40 = local_48;
    if ((local_58 & 1) == 0) {
      local_40 = auStack_57;
    }
    if (DAT_0109fdb0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8dc8;
    }
    (**(code **)(*DAT_0109fdb0 + 0x30))(DAT_0109fdb0,&local_40);
    if ((local_58 & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8dc8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
