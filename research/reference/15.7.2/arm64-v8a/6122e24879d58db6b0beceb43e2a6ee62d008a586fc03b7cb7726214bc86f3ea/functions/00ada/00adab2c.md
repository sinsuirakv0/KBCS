# 00adab2c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adab2c.md)

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
  "source_sha256": "351dfd61aceae2e72abc3fe047ec9a8cfa033f9480f3a251c0ca5874de3e5b4b",
  "source_text_sha256": "351dfd61aceae2e72abc3fe047ec9a8cfa033f9480f3a251c0ca5874de3e5b4b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1192 bytes

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
      operator_delete(local_48);
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
