# 00adad0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00adad0c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "405da835612ac695f21eb4936043978e35e2c0ce9ca62ee010310e27ff766a62",
  "source_text_sha256": "405da835612ac695f21eb4936043978e35e2c0ce9ca62ee010310e27ff766a62"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba20](../00adb/00adba20.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

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
  
                    /* try { // try from 00adad10 to 00bdad4f has its CatchHandler @ 00adad10
                       catch() { ... } // from try @ 00adad10 with catch @ 00adad10
                       catch() { ... } // from try @ 00adad60 with catch @ 00adad10 */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba20(&DAT_0109ff38,local_40);
                    /* try { // try from 00adad50 to 00bdad5f has its CatchHandler @ 00adada0 */
  if ((puVar2 != &DAT_0109ff40) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
                    /* try { // try from 00adad60 to 00bdaddf has its CatchHandler @ 00adad10 */
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
