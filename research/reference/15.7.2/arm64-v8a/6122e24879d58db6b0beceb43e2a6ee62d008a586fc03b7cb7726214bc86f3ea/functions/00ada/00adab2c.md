# 00adab2c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00adac38`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00adab2c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ea7b608b3dff791e063c3e8a577b27e949d0d472f7a01a8c310b64e21e1ca71",
  "source_text_sha256": "9ea7b608b3dff791e063c3e8a577b27e949d0d472f7a01a8c310b64e21e1ca71"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 1145 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  undefined4 local_3c;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fef0 != (long *)0x0) {
    FUN_00566a7c(local_58,param_1,param_3);
    local_3c = param_4;
    if (DAT_0109fef0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00adabfc;
    }
                    /* try { // try from 00adab78 to 00bdaba7 has its CatchHandler @ 00adac9c */
    (**(code **)(*DAT_0109fef0 + 0x30))(DAT_0109fef0,local_58,&local_3c);
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00adaba8 to 00bdabdb has its CatchHandler @ 00adaa10 */
    return;
  }
LAB_00adabfc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
