# 00adae8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adae8c.md)

## 関数情報

~~~json
{
  "address": "00adae8c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5309ecac10e4dca884c3a921486ff47845718f41e53b66c31011a79cc7fb195",
  "source_text_sha256": "e5309ecac10e4dca884c3a921486ff47845718f41e53b66c31011a79cc7fb195"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba18](../00adb/00adba18.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 911 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
                    /* catch() { ... } // from try @ 00adae70 with catch @ 00adae8c */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba18(&DAT_0109fe50,local_40);
  if ((puVar2 != &DAT_0109fe58) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    operator_delete(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
