# 00adacc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adacc0.md)

## 関数情報

~~~json
{
  "address": "00adacc0",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f03e382ade56bf17d98b9163712a298ac6fe1388e8558d339e89d1b01cf52cc5",
  "source_text_sha256": "f03e382ade56bf17d98b9163712a298ac6fe1388e8558d339e89d1b01cf52cc5"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adb914](../00adb/00adb914.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 1549 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_68 [16];
  void *local_58;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
                    /* try { // try from 00adaccc to 00bdad0b has its CatchHandler @ 00adaccc
                       catch() { ... } // from try @ 00adaccc with catch @ 00adaccc
                       catch() { ... } // from try @ 00adad1c with catch @ 00adaccc */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_50,param_1,param_3);
  FUN_00566a7c(local_68,param_1,param_3);
                    /* try { // try from 00adad0c to 00bdad1b has its CatchHandler @ 00adad5c */
  puVar2 = (undefined8 *)FUN_00adb914(&DAT_0109fe38,local_50);
                    /* try { // try from 00adad1c to 00bdad9b has its CatchHandler @ 00adaccc */
  if ((puVar2 != &DAT_0109fe40) && (plVar3 = (long *)puVar2[0x12], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_50,local_68);
  }
  if ((local_68[0] & 1) != 0) {
    operator_delete(local_58);
  }
  if ((local_50[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 00adad0c with catch @ 00adad5c */
    operator_delete(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
