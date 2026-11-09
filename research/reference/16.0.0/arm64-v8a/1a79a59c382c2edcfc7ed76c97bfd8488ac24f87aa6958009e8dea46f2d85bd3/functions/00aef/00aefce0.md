# 00aefce0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aefce0",
  "name": "FUN_00aefce0",
  "size": 896,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3e6009581566d5c777b1da5e6e40c3ee288b143852f21bbb396110866fb4361",
  "source_text_sha256": "d3e6009581566d5c777b1da5e6e40c3ee288b143852f21bbb396110866fb4361"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [0048ce14](../0048c/0048ce14.md)
- [005bc78c](../005bc/005bc78c.md)
- [007441c8](../00744/007441c8.md)
- [008514b8](../00851/008514b8.md)
- [008b6f0c](../008b6/008b6f0c.md)
- [008b9814](../008b9/008b9814.md)
- [008bac84](../008ba/008bac84.md)
- [008bb0a8](../008bb/008bb0a8.md)
- [00ad688c](../00ad6/00ad688c.md)
- [00aeb76c](../00aeb/00aeb76c.md)
- [00af01cc](../00af0/00af01cc.md)
- [00af01d0](../00af0/00af01d0.md)
- [00af0290](../00af0/00af0290.md)
- [00af0294](../00af0/00af0294.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57d90](../00c57/00c57d90.md)

## 関連文字列（未確認候補）

~~~text
"slot_autoset_confirm"
"slot_autoset_error_1"
"slot_autoset_error_2"
"slot_autoset_error_3"
~~~

## 疑似コード / UTF-8 5863 bytes

~~~c

void FUN_00aefce0(long param_1,undefined8 *param_2,int *param_3)

{
  ulong uVar1;
  byte *pbVar2;
  char *pcVar3;
  char *pcVar4;
  long lVar5;
  uint uVar6;
  int iVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined ***pppuVar12;
  undefined4 uVar13;
  long lVar14;
  undefined8 uVar15;
  bool bVar16;
  long lVar17;
  byte local_d0;
  char local_cf [8];
  undefined7 uStack_c7;
  char cStack_c0;
  undefined4 uStack_bf;
  undefined1 uStack_bb;
  undefined2 uStack_ba;
  ushort local_b8 [8];
  void *local_a8;
  undefined **local_a0;
  long lStack_98;
  undefined ***local_80;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  iVar7 = *param_3;
  uVar15 = *param_2;
  if (iVar7 == 4) {
    lVar14 = *(long *)(param_1 + 8);
    uVar9 = FUN_008b6f0c(uVar15);
    if ((uVar9 & 1) == 0) {
      iVar7 = FUN_00ad688c(lVar14);
      local_b8[0] = 0;
      pcVar3 = "slot_autoset_error_3";
      if (iVar7 != 1) {
        pcVar3 = "slot_autoset_error_2";
      }
      pcVar4 = "slot_autoset_error_1";
      if (iVar7 != 0) {
        pcVar4 = pcVar3;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc(local_b8,pcVar4)
      ;
      FUN_0048ce14(&local_d0,local_b8);
      local_a0 = &PTR_FUN_00c8df68;
      local_80 = &local_a0;
      FUN_008bac84(lVar14 + 0x2f08,&local_d0,0,0,4,&local_a0);
      if (local_80 == &local_a0) {
        lVar14 = 0x20;
        pppuVar12 = &local_a0;
LAB_00aeff40:
        (**(code **)((long)*pppuVar12 + lVar14))();
      }
      else {
                    /* try { // try from 00aeff2c to 00beff2f has its CatchHandler @ 00af0330 */
        if (local_80 != (undefined ***)0x0) {
                    /* try { // try from 00aeff30 to 00beff9f has its CatchHandler @ 00aefc4c */
          lVar14 = 0x28;
          pppuVar12 = local_80;
          goto LAB_00aeff40;
        }
      }
      if ((local_d0 & 1) != 0) {
        _ZdlPv((void *)CONCAT26(uStack_ba,CONCAT15(uStack_bb,CONCAT41(uStack_bf,cStack_c0))));
      }
      if ((local_b8[0] & 1) == 0) goto LAB_00af002c;
    }
    else {
      bVar16 = false;
      lVar17 = 0xc5b9;
      uVar9 = 0;
      do {
        lVar10 = FUN_008514b8();
        lVar11 = FUN_008514b8();
        lVar10 = lVar10 + (long)*(int *)((long)&DWORD_0039b97c + lVar11) * 0x2c;
        pbVar2 = (byte *)(lVar10 + lVar17);
                    /* try { // try from 00aefdfc to 00befdff has its CatchHandler @ 00af0334 */
                    /* try { // try from 00aefe00 to 00beff2b has its CatchHandler @ 00aefc4c */
        if (1 < (int)((uint)(*(byte *)(lVar10 + 0xc5e2) ^ pbVar2[1]) << 0x10 |
                      (uint)(*(byte *)(lVar10 + 0xc5e3) ^ pbVar2[2]) << 0x18 |
                      (uint)(*(byte *)(lVar10 + 0xc5e1) ^ *pbVar2) << 8 |
                     (uint)(*(byte *)(lVar10 + 0xc5e0) ^ pbVar2[-1]))) break;
        uVar1 = uVar9 + 1;
        lVar17 = lVar17 + 4;
        bVar16 = 8 < uVar9;
        uVar9 = uVar1;
      } while (uVar1 != 10);
      if ((*(char *)(lVar14 + 0x11a4) == '\0') ||
         (uVar6 = FUN_007441c8(lVar14 + 0xbe0), bVar16 || (uVar6 & 1) != 0)) {
        FUN_005bc78c(lVar14 + 0x428,0);
        if (*(long *)(lVar5 + 0x28) == local_68) {
          FUN_00aeb76c(lVar14);
          return;
        }
        goto LAB_00af0168;
      }
      local_d0 = 0x28;
      uStack_bf = 0x6d726966;
      uStack_c7 = (undefined7)s_slot_autoset_confirm_002a8213._8_8_;
      cStack_c0 = SUB81(s_slot_autoset_confirm_002a8213._8_8_,7);
      local_cf[0] = s_slot_autoset_confirm_002a8213[0];
      local_cf[1] = s_slot_autoset_confirm_002a8213[1];
      local_cf[2] = s_slot_autoset_confirm_002a8213[2];
      local_cf[3] = s_slot_autoset_confirm_002a8213[3];
      local_cf[4] = s_slot_autoset_confirm_002a8213[4];
      local_cf[5] = s_slot_autoset_confirm_002a8213[5];
      local_cf[6] = s_slot_autoset_confirm_002a8213[6];
      local_cf[7] = s_slot_autoset_confirm_002a8213[7];
      uStack_bb = 0;
      FUN_0048ce14(local_b8,&local_d0);
                    /* try { // try from 00aeffa0 to 00beffab has its CatchHandler @ 00af02f0 */
      local_80 = &local_a0;
      local_a0 = &PTR_FUN_00c8dfe8;
      lStack_98 = lVar14;
      uVar15 = FUN_008bb0a8(lVar14 + 0x2f08,local_b8,0,0,4,&local_a0);
                    /* try { // try from 00aeffd8 to 00beffe3 has its CatchHandler @ 00af02f4 */
      FUN_008b9814(uVar15,1);
      if (local_80 == &local_a0) {
        lVar14 = 0x20;
        pppuVar12 = &local_a0;
LAB_00af0000:
        (**(code **)((long)*pppuVar12 + lVar14))();
      }
      else if (local_80 != (undefined ***)0x0) {
        lVar14 = 0x28;
        pppuVar12 = local_80;
        goto LAB_00af0000;
      }
                    /* try { // try from 00af0010 to 00bf0017 has its CatchHandler @ 00af02ec */
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
      }
      if ((local_d0 & 1) == 0) goto LAB_00af002c;
      local_a8 = (void *)CONCAT26(uStack_ba,CONCAT15(uStack_bb,CONCAT41(uStack_bf,cStack_c0)));
    }
    _ZdlPv(local_a8);
  }
  else {
    if (iVar7 == 3) {
      uVar8 = FUN_0047acb4();
      uVar9 = FUN_008b6f0c(uVar15);
      uVar13 = 0xb;
      if ((uVar9 & 1) == 0) {
        uVar13 = 0xf;
      }
      if (*(long *)(lVar5 + 0x28) == local_68) {
LAB_00aefd78:
        FUN_0047cd94(uVar8,uVar13,0);
        return;
      }
      goto LAB_00af0168;
    }
    if (iVar7 == 0) {
      uVar8 = FUN_0047acb4();
      if (*(long *)(lVar5 + 0x28) == local_68) {
        uVar13 = 10;
        goto LAB_00aefd78;
      }
      goto LAB_00af0168;
    }
  }
LAB_00af002c:
  if (*(long *)(lVar5 + 0x28) == local_68) {
                    /* try { // try from 00af0044 to 00bf005b has its CatchHandler @ 00af02cc */
    return;
  }
LAB_00af0168:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
