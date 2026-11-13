# 00aed9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aed9ec",
  "name": "FUN_00aed9ec",
  "size": 804,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fb529ae8bd58bd7578171f288bdcc580b5732c83eb290e6e0721fb59bb1d58a",
  "source_text_sha256": "1fb529ae8bd58bd7578171f288bdcc580b5732c83eb290e6e0721fb59bb1d58a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00447f34](../00447/00447f34.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00489f8c](../00489/00489f8c.md)
- [0048ce94](../0048c/0048ce94.md)
- [00851550](../00851/00851550.md)
- [008b96fc](../008b9/008b96fc.md)
- [008b97d4](../008b9/008b97d4.md)
- [008b97f8](../008b9/008b97f8.md)
- [008b98b0](../008b9/008b98b0.md)
- [008bb144](../008bb/008bb144.md)
- [008bb568](../008bb/008bb568.md)
- [00aede74](../00aed/00aede74.md)
- [00aede78](../00aed/00aede78.md)
- [00aeec84](../00aee/00aeec84.md)
- [00aeec88](../00aee/00aeec88.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"slot_copy_select"
~~~

## 疑似コード / UTF-8 6639 bytes

~~~c

void FUN_00aed9ec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  long lVar5;
  undefined ***pppuVar6;
  undefined8 uVar7;
  long lVar8;
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined1 uStack_bf;
  undefined6 uStack_be;
  byte local_b8 [16];
  void *local_a8;
  undefined **local_a0;
  long lStack_98;
  void *local_90;
  undefined ***local_80;
  undefined **local_70;
  long lStack_68;
  undefined ***local_50;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar8 = *(long *)(param_1 + 8);
    uStack_bf = 0;
    local_d0 = 0x20;
    uStack_c7 = (undefined7)s_slot_copy_select_0029f825._8_8_;
    cStack_c0 = SUB81(s_slot_copy_select_0029f825._8_8_,7);
    local_cf = (char  [8])s_slot_copy_select_0029f825._0_8_;
                    /* try { // try from 00aeda94 to 00beda97 has its CatchHandler @ 00aedb1c */
    FUN_0048ce94(local_b8,&local_d0);
    lVar4 = FUN_00851550();
                    /* try { // try from 00aedaa8 to 00bedaab has its CatchHandler @ 00aedad0 */
                    /* try { // try from 00aedabc to 00bedabf has its CatchHandler @ 00aedac8 */
    FUN_00447f34(&local_a0,local_b8,0,*(int *)(BYTE_ARRAY_0039b979 + lVar4 + 3) + 1);
                    /* catch() { ... } // from try @ 00aed928 with catch @ 00aedac0
                       try { // try from 00aedac0 to 00bedb8f has its CatchHandler @ 00aed60c */
                    /* catch() { ... } // from try @ 00aed8bc with catch @ 00aedac4 */
                    /* catch() { ... } // from try @ 00aed974 with catch @ 00aedac8
                       catch() { ... } // from try @ 00aedabc with catch @ 00aedac8 */
    local_50 = &local_70;
                    /* catch() { ... } // from try @ 00aed74c with catch @ 00aedacc */
                    /* catch() { ... } // from try @ 00aed908 with catch @ 00aedad0
                       catch() { ... } // from try @ 00aedaa8 with catch @ 00aedad0 */
    local_70 = &PTR_FUN_00c8dd38;
    lStack_68 = lVar8;
                    /* catch() { ... } // from try @ 00aed714 with catch @ 00aedae8 */
                    /* catch() { ... } // from try @ 00aed6c8 with catch @ 00aedaec */
    uVar3 = FUN_008bb144(lVar8 + 0x2f08,&local_a0,0,0,0x5c,&local_70);
    FUN_008b98b0(uVar3,0xfffffffe);
                    /* catch() { ... } // from try @ 00aed6bc with catch @ 00aedafc */
    if (local_50 == &local_70) {
      lVar4 = 0x20;
                    /* catch() { ... } // from try @ 00aed898 with catch @ 00aedb1c
                       catch() { ... } // from try @ 00aeda94 with catch @ 00aedb1c */
      pppuVar6 = &local_70;
LAB_00aedb20:
                    /* catch() { ... } // from try @ 00aed684 with catch @ 00aedb20 */
      (**(code **)((long)*pppuVar6 + lVar4))();
    }
    else {
                    /* catch() { ... } // from try @ 00aed84c with catch @ 00aedb0c */
      if (local_50 != (undefined ***)0x0) {
        lVar4 = 0x28;
        pppuVar6 = local_50;
                    /* catch() { ... } // from try @ 00aed6b0 with catch @ 00aedb14 */
        goto LAB_00aedb20;
      }
    }
    if (((byte)local_a0 & 1) != 0) {
      _ZdlPv(local_90);
    }
    if ((local_b8[0] & 1) != 0) {
      _ZdlPv(local_a8);
    }
                    /* catch() { ... } // from try @ 00aed808 with catch @ 00aedb40 */
    if ((local_d0 & 1) != 0) {
                    /* catch() { ... } // from try @ 00aed7e4 with catch @ 00aedb44 */
      _ZdlPv((void *)CONCAT62(uStack_be,CONCAT11(uStack_bf,cStack_c0)));
    }
    lVar4 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aed7b4 with catch @ 00aedb60 */
    if ((*(int *)((long)&fde_table_entry_00333b98.data_loc + lVar4) < 2) &&
       (lVar4 = FUN_00851550(), (*(byte *)(lVar4 + 0x33a5) & 1) == 0)) {
      uVar3 = FUN_008bb568(lVar8 + 0x2f08);
      FUN_008b97f8(uVar3,1,0);
    }
    FUN_00851550();
    lVar4 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aedcdc with catch @ 00aedb90
                       catch() { ... } // from try @ 00aede38 with catch @ 00aedb90
                       catch() { ... } // from try @ 00aedee4 with catch @ 00aedb90 */
    lVar5 = FUN_00851550();
    lVar4 = lVar4 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar5 + 3) * 0x2c;
                    /* try { // try from 00aedbf0 to 00bedbf7 has its CatchHandler @ 00aedefc */
    if ((int)((uint)(*(byte *)(lVar4 + 0xc5e2) ^ *(byte *)(lVar4 + 0xc5ba)) << 0x10 |
              (uint)(*(byte *)(lVar4 + 0xc5e3) ^ *(byte *)(lVar4 + 0xc5bb)) << 0x18 |
              (uint)(*(byte *)(lVar4 + 0xc5e1) ^ *(byte *)(lVar4 + 0xc5b9)) << 8 |
             (uint)(*(byte *)(lVar4 + 0xc5e0) ^ *(byte *)(lVar4 + 0xc5b8))) < 2) {
      uVar3 = FUN_008bb568(lVar8 + 0x2f08);
      FUN_008b97f8(uVar3,0,0);
    }
    if (DAT_00ca4a78 == 0) {
      lVar4 = 0;
    }
    else {
                    /* try { // try from 00aedc34 to 00bedc83 has its CatchHandler @ 00aedf08 */
      lVar4 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
    }
    uVar3 = FUN_008bb568(lVar8 + 0x2f08);
    lVar4 = FUN_00489f8c(*(undefined8 *)(lVar4 + 0x118),0x2b);
    FUN_008b97d4(uVar3,1,*(int *)(lVar4 + 8) + 0x1e);
    uVar3 = FUN_008bb568(lVar8 + 0x2f08);
    local_a0 = &PTR_FUN_00c8df38;
    lStack_98 = lVar8;
    local_80 = &local_a0;
    FUN_008b96fc(uVar3,&local_a0);
    if (local_80 == &local_a0) {
      lVar4 = 0x20;
      pppuVar6 = &local_a0;
    }
    else {
      if (local_80 == (undefined ***)0x0) goto LAB_00aedce8;
      lVar4 = 0x28;
      pppuVar6 = local_80;
                    /* try { // try from 00aedcd0 to 00bedcdb has its CatchHandler @ 00aedee4 */
    }
                    /* try { // try from 00aedcdc to 00bede0b has its CatchHandler @ 00aedb90 */
    (**(code **)((long)*pppuVar6 + lVar4))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047ad34();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar7 = 0xb;
LAB_00aeda58:
        FUN_0047ce14(uVar3,uVar7,0);
        return;
      }
      goto LAB_00aeddac;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047ad34();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar7 = 10;
        goto LAB_00aeda58;
      }
      goto LAB_00aeddac;
    }
  }
LAB_00aedce8:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_00aeddac:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
