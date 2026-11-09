# 00aacca8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aacca8",
  "name": "FUN_00aacca8",
  "size": 1472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e791aaa4c4c12ae7cd86a88c9b22dee330c83b48e25fe189df5f41cc977d23",
  "source_text_sha256": "41e791aaa4c4c12ae7cd86a88c9b22dee330c83b48e25fe189df5f41cc977d23"
}
~~~

## 呼び出し元

- [0047373c](../00473/0047373c.md)
- [00769d44](../00769/00769d44.md)
- [0085bb30](../0085b/0085bb30.md)
- [0088c46c](../0088c/0088c46c.md)
- [008adcf4](../008ad/008adcf4.md)

## 呼び出し先

- [004476b4](../00447/004476b4.md)
- [005e0d28](../005e0/005e0d28.md)
- [00784240](../00784/00784240.md)
- [008514b8](../00851/008514b8.md)
- [00853c30](../00853/00853c30.md)
- [0087925c](../00879/0087925c.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57b50](../00c57/00c57b50.md)
- [00c5a430](../00c5a/00c5a430.md)
- [00c5a440](../00c5a/00c5a440.md)
- [00c5a4f0](../00c5a/00c5a4f0.md)

## 関連文字列（未確認候補）

~~~text
"BcLogPurchaseTrigger"
"Content"
"Select"
"Trigger"
"ex_id"
"ex_type"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

## 疑似コード / UTF-8 9377 bytes

~~~c

void FUN_00aacca8(uint param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  int iVar2;
  int iVar3;
  long lVar4;
  undefined1 auStack_220 [24];
  undefined1 auStack_208 [24];
  undefined1 auStack_1f0 [24];
  undefined1 auStack_1d8 [24];
  byte local_1c0;
  undefined4 local_1bf;
  undefined2 local_1bb;
  void *local_1b0;
  byte local_1a8 [16];
  void *local_198;
  undefined1 auStack_190 [24];
  byte local_178 [16];
  void *local_168;
  undefined1 auStack_160 [24];
  byte local_148;
  char local_147 [8];
  undefined7 uStack_13f;
  char cStack_138;
  undefined4 uStack_137;
  undefined1 uStack_133;
  undefined2 uStack_132;
  undefined4 local_130 [2];
  char *local_128;
  char *local_118;
  undefined4 local_110 [2];
  undefined8 local_108;
  char *local_f8;
  undefined4 local_f0 [2];
  undefined8 local_e8;
  char *local_d8;
  undefined4 local_d0 [2];
  undefined8 local_c8;
  char *local_b8;
  undefined4 local_b0 [2];
  undefined8 local_a8;
  char *local_98;
  undefined4 local_90 [2];
  undefined8 local_88;
  char *local_78;
  undefined4 local_70 [2];
  undefined8 local_68;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  if (param_1 < 3) {
    FUN_008514b8();
                    /* catch() { ... } // from try @ 00aacc08 with catch @ 00aacce8 */
    iVar2 = FUN_00853c30();
    if (iVar2 == 300) {
      iVar3 = FUN_005e0d28();
    }
    else {
      if (iVar2 != 100) goto LAB_00aad238;
                    /* catch() { ... } // from try @ 00aacbe8 with catch @ 00aacd00 */
      lVar4 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aacc84 with catch @ 00aacd04 */
                    /* catch() { ... } // from try @ 00aacc14 with catch @ 00aacd08
                       catch() { ... } // from try @ 00aacc44 with catch @ 00aacd08 */
                    /* catch() { ... } // from try @ 00aacb5c with catch @ 00aacd0c */
      iVar3 = *(int *)((long)&fde_table_entry_00333f48.data_loc + lVar4);
    }
    if (iVar3 < 0) goto LAB_00aad238;
    local_148 = 0x28;
    uStack_137 = 0x72656767;
    uStack_13f = (undefined7)s_BcLogPurchaseTrigger_002babe5._8_8_;
    cStack_138 = SUB81(s_BcLogPurchaseTrigger_002babe5._8_8_,7);
    uStack_133 = 0;
    local_118 = "sec1_type";
    local_110[0] = 0;
    local_108 = 0;
    local_130[0] = 0;
    local_147 = (char  [8])s_BcLogPurchaseTrigger_002babe5._0_8_;
                    /* try { // try from 00aacfc8 to 00bacfcf has its CatchHandler @ 00aad290 */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
                    /* try { // try from 00aacfd0 to 00bad0df has its CatchHandler @ 00aacdcc */
    local_128 = "Trigger";
    _ZN8firebase7VariantaSEOS0_(local_110,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    _ZNSt6__ndk19to_stringEi(local_178,param_1);
    FUN_00784240(auStack_160,local_178);
    local_f8 = "sec1_id";
    local_f0[0] = 0;
    local_e8 = 0;
    _ZN8firebase7VariantaSERKS0_(local_f0,auStack_160);
    local_d8 = "sec2_type";
    local_d0[0] = 0;
    local_c8 = 0;
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Select";
    _ZN8firebase7VariantaSEOS0_(local_d0,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    local_1c0 = 10;
    local_1bf = 0x252d6425;
    local_1bb = 100;
    FUN_004476b4(local_1a8,&local_1c0,0,iVar2,iVar3);
    FUN_00784240(auStack_190,local_1a8);
    local_b8 = "sec2_id";
    local_b0[0] = 0;
    local_a8 = 0;
                    /* try { // try from 00aad0e0 to 00bad103 has its CatchHandler @ 00aad2c4 */
    _ZN8firebase7VariantaSERKS0_(local_b0,auStack_190);
    local_98 = "ex_type";
    local_90[0] = 0;
    local_88 = 0;
                    /* try { // try from 00aad104 to 00bad16f has its CatchHandler @ 00aacdcc */
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Content";
    _ZN8firebase7VariantaSEOS0_(local_90,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    FUN_00784240(auStack_1d8,param_3);
    local_70[0] = 0;
    local_78 = "ex_id";
    local_68 = 0;
    _ZN8firebase7VariantaSERKS0_(local_70,auStack_1d8);
                    /* try { // try from 00aad170 to 00bad17b has its CatchHandler @ 00aad2a0 */
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_1d8,0);
                    /* try { // try from 00aad17c to 00bad253 has its CatchHandler @ 00aacdcc */
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_190,0);
    if ((local_1a8[0] & 1) != 0) {
      _ZdlPv(local_198);
    }
    if ((local_1c0 & 1) != 0) {
      _ZdlPv(local_1b0);
    }
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_160,0);
    if ((local_178[0] & 1) != 0) {
      _ZdlPv(local_168);
    }
    lVar4 = FUN_008514b8();
    FUN_0087925c(*(undefined8 *)(lVar4 + 0x22b0),(ulong)&local_148 | 1,&local_118,6);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_70,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_90,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_b0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_d0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_f0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_110,0);
  }
  else {
                    /* catch() { ... } // from try @ 00aacb90 with catch @ 00aacd2c */
    local_148 = 0x28;
    uStack_137 = 0x72656767;
    uStack_13f = (undefined7)s_BcLogPurchaseTrigger_002babe5._8_8_;
    cStack_138 = SUB81(s_BcLogPurchaseTrigger_002babe5._8_8_,7);
    local_147 = (char  [8])s_BcLogPurchaseTrigger_002babe5._0_8_;
    uStack_133 = 0;
    local_118 = "sec1_type";
    local_110[0] = 0;
    local_108 = 0;
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Trigger";
    _ZN8firebase7VariantaSEOS0_(local_110,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    _ZNSt6__ndk19to_stringEi(local_178,param_1);
    FUN_00784240(auStack_1f0,local_178);
    local_f8 = "sec1_id";
    local_f0[0] = 0;
    local_e8 = 0;
                    /* try { // try from 00aacdcc to 00bace57 has its CatchHandler @ 00aacdcc
                       catch() { ... } // from try @ 00aacdcc with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aace94 with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aacf28 with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aacfd0 with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aad104 with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aad17c with catch @ 00aacdcc
                       catch() { ... } // from try @ 00aad290 with catch @ 00aacdcc */
    _ZN8firebase7VariantaSERKS0_(local_f0,auStack_1f0);
    local_d8 = "sec2_type";
    local_d0[0] = 0;
    local_c8 = 0;
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Select";
    _ZN8firebase7VariantaSEOS0_(local_d0,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    FUN_00784240(auStack_208,param_2);
    local_b0[0] = 0;
    local_b8 = "sec2_id";
    local_a8 = 0;
    _ZN8firebase7VariantaSERKS0_(local_b0,auStack_208);
                    /* try { // try from 00aace58 to 00bace5f has its CatchHandler @ 00aad2b4 */
    local_98 = "ex_type";
    local_90[0] = 0;
    local_88 = 0;
    local_130[0] = 0;
                    /* try { // try from 00aace74 to 00bace7b has its CatchHandler @ 00aad2b0 */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
                    /* try { // try from 00aace80 to 00bace87 has its CatchHandler @ 00aad2a8 */
                    /* try { // try from 00aace88 to 00bace93 has its CatchHandler @ 00aad2ac */
    local_128 = "Content";
    _ZN8firebase7VariantaSEOS0_(local_90,local_130);
                    /* try { // try from 00aace94 to 00bacf23 has its CatchHandler @ 00aacdcc */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    FUN_00784240(auStack_220,param_3);
    local_70[0] = 0;
    local_78 = "ex_id";
    local_68 = 0;
    _ZN8firebase7VariantaSERKS0_(local_70,auStack_220);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_220,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_208,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_1f0,0);
    if ((local_178[0] & 1) != 0) {
      _ZdlPv(local_168);
    }
    lVar4 = FUN_008514b8();
    FUN_0087925c(*(undefined8 *)(lVar4 + 0x22b0),(ulong)&local_148 | 1,&local_118,6);
                    /* try { // try from 00aacf24 to 00bacf27 has its CatchHandler @ 00aad2ac */
                    /* try { // try from 00aacf28 to 00bacfc7 has its CatchHandler @ 00aacdcc */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_70,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_90,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_b0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_d0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_f0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_110,0);
  }
  if ((local_148 & 1) != 0) {
    _ZdlPv((void *)CONCAT26(uStack_132,CONCAT15(uStack_133,CONCAT41(uStack_137,cStack_138))));
  }
LAB_00aad238:
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* try { // try from 00aad254 to 00bad273 has its CatchHandler @ 00aad2a4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
