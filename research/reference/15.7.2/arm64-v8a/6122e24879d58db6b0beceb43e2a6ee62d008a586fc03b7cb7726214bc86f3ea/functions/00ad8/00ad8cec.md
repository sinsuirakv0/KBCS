# 00ad8cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ad8cec.md)

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
  "source_sha256": "818452c8a66b74e30fe33d21ff0f050a87797109e40f0e6c5db0ffc1fe4b283d",
  "source_text_sha256": "818452c8a66b74e30fe33d21ff0f050a87797109e40f0e6c5db0ffc1fe4b283d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1858 bytes

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
      operator_delete(local_48);
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
