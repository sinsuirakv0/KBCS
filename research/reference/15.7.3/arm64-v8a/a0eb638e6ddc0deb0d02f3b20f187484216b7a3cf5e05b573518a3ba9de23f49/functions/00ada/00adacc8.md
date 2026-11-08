# 00adacc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00adacc8",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7374003f99f66fa28d2fea19bd9d5906a185c8dbcf3f7f37861d658c2a0d53f1",
  "source_text_sha256": "7374003f99f66fa28d2fea19bd9d5906a185c8dbcf3f7f37861d658c2a0d53f1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adb9dc](../00adb/00adb9dc.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 1253 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
                    /* try { // try from 00adaccc to 00bdad0b has its CatchHandler @ 00adaccc
                       catch() { ... } // from try @ 00adaccc with catch @ 00adaccc
                       catch() { ... } // from try @ 00adad1c with catch @ 00adaccc */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adb9dc(&DAT_0109fef8,local_40);
                    /* try { // try from 00adad0c to 00bdad1b has its CatchHandler @ 00adad5c */
  if ((puVar2 != &DAT_0109ff00) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
                    /* try { // try from 00adad1c to 00bdad9b has its CatchHandler @ 00adaccc */
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
