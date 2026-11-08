# 00adabf4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00adabf4",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a860d264e9b0092b14ba4e71380fe46dde89aa6ac8d7e755a0f4ce89ddbf063b",
  "source_text_sha256": "a860d264e9b0092b14ba4e71380fe46dde89aa6ac8d7e755a0f4ce89ddbf063b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

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
  if (DAT_0109ffb0 != (long *)0x0) {
    FUN_00566a7c(local_58,param_1,param_3);
    local_3c = param_4;
    if (DAT_0109ffb0 == (long *)0x0) {
                    /* try { // try from 00adac8c to 00bdac97 has its CatchHandler @ 00adac98 */
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00adacc4;
    }
    (**(code **)(*DAT_0109ffb0 + 0x30))(DAT_0109ffb0,local_58,&local_3c);
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00adac70 to 00bdac7b has its CatchHandler @ 00adac9c */
    return;
  }
LAB_00adacc4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
