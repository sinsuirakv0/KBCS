# 00aed3bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aed3bc",
  "name": "FUN_00aed3bc",
  "size": 476,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba8310597489924ac0468489ad9f44e95340398384a97ba368d6562236cf6e06",
  "source_text_sha256": "ba8310597489924ac0468489ad9f44e95340398384a97ba368d6562236cf6e06"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [0068c610](../0068c/0068c610.md)
- [006d1fe4](../006d1/006d1fe4.md)
- [008514f8](../00851/008514f8.md)
- [008b6f18](../008b6/008b6f18.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 3639 bytes

~~~c

void FUN_00aed3bc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined4 uVar2;
  long lVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  undefined8 uVar8;
  undefined8 local_48;
  long *local_40;
  long local_38;
  
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    if (DAT_00ca4978 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
    }
    lVar7 = FUN_008514f8();
    if (*(int *)(&DAT_00477ddc + lVar7) != -1) {
      lVar7 = FUN_008514f8();
      uVar2 = *(undefined4 *)(&DAT_00477ddc + lVar7);
      lVar7 = FUN_008514f8();
      *(undefined4 *)(&DAT_00477dd8 + lVar7) = uVar2;
    }
    lVar7 = FUN_008514f8();
    iVar1 = *(int *)(&DAT_00477dd8 + lVar7);
    lVar7 = FUN_008514f8();
    if (iVar1 == 0) {
                    /* catch() { ... } // from try @ 00aed178 with catch @ 00aed56c */
                    /* catch() { ... } // from try @ 00aed304 with catch @ 00aed574
                       catch() { ... } // from try @ 00aed54c with catch @ 00aed574 */
      if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00aed1bc with catch @ 00aed578
                       catch() { ... } // from try @ 00aed538 with catch @ 00aed578 */
        FUN_006d1fe4(&DAT_00477730 + lVar7);
        return;
      }
      goto LAB_00aed5b8;
    }
    local_48 = *(undefined8 *)(lVar6 + 0x228);
    local_40 = *(long **)(lVar6 + 0x230);
    if (local_40 != (long *)0x0) {
      FUN_00c53cd0(1,local_40 + 1);
    }
    FUN_0068c610(lVar7 + 0x17d8,&local_48);
    plVar4 = local_40;
    if ((local_40 != (long *)0x0) &&
       (lVar6 = FUN_00c53d00(0xffffffffffffffff,local_40 + 1), lVar6 == 0)) {
                    /* try { // try from 00aed538 to 00bed53b has its CatchHandler @ 00aed578 */
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
  }
  else {
    if (iVar1 == 3) {
      uVar8 = *param_2;
      uVar5 = FUN_0047acf4();
      FUN_0047cdd4(uVar5,0xb,0);
      if (*(long *)(lVar3 + 0x28) == local_38) {
        FUN_008b6f18(uVar8,0);
        return;
      }
      goto LAB_00aed5b8;
    }
    if (iVar1 == 0) {
      uVar5 = FUN_0047acf4();
      if (*(long *)(lVar3 + 0x28) == local_38) {
        FUN_0047cdd4(uVar5,10,0);
        return;
      }
      goto LAB_00aed5b8;
    }
  }
                    /* try { // try from 00aed54c to 00bed54f has its CatchHandler @ 00aed574 */
                    /* catch() { ... } // from try @ 00aed394 with catch @ 00aed550
                       try { // try from 00aed550 to 00bed5b7 has its CatchHandler @ 00aed118 */
  if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00aed2bc with catch @ 00aed554 */
                    /* catch() { ... } // from try @ 00aed258 with catch @ 00aed55c */
    return;
  }
LAB_00aed5b8:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00aed5b8 to 00bed5fb has its CatchHandler @ 00aed5b8
                       catch() { ... } // from try @ 00aed5b8 with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aed680 with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aed92c with catch @ 00aed5b8
                       catch() { ... } // from try @ 00aeda6c with catch @ 00aed5b8 */
  __stack_chk_fail();
}

~~~
