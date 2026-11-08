# 00babdc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00babdc0",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6172d97489d9a40fd24f18750409769bbf7e5e5a827397710c1621b3f1b5e753",
  "source_text_sha256": "6172d97489d9a40fd24f18750409769bbf7e5e5a827397710c1621b3f1b5e753"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00babe28](../00bab/00babe28.md)

## 疑似コード / UTF-8 850 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE6do_outERS1_PKDsS5_RS5_PcS7_RS7_
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00babe04 to 00cabfd3 has its CatchHandler @ 00babe04
                       catch() { ... } // from try @ 00babe04 with catch @ 00babe04
                       catch() { ... } // from try @ 00babff0 with catch @ 00babe04
                       catch() { ... } // from try @ 00bac28c with catch @ 00babe04 */
  FUN_00babe28(param_3,param_4,&uStack_28,param_6,param_7,&local_30,0x10ffff,0);
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~
