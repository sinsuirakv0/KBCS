# 00aacea4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aacea4",
  "name": "FUN_00aacea4",
  "size": 1472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ddc0919fca516344ab66bac187517e0a3a2f3c5ce78fa78c29da855d9e34610",
  "source_text_sha256": "7ddc0919fca516344ab66bac187517e0a3a2f3c5ce78fa78c29da855d9e34610"
}
~~~

## 呼び出し元

- [0047377c](../00473/0047377c.md)
- [00769d84](../00769/00769d84.md)
- [0085bb70](../0085b/0085bb70.md)
- [0088c4ac](../0088c/0088c4ac.md)
- [008add38](../008ad/008add38.md)

## 呼び出し先

- [004476f4](../00447/004476f4.md)
- [005e0d68](../005e0/005e0d68.md)
- [00784280](../00784/00784280.md)
- [008514f8](../00851/008514f8.md)
- [00853c70](../00853/00853c70.md)
- [0087929c](../00879/0087929c.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c5a830](../00c5a/00c5a830.md)
- [00c5a840](../00c5a/00c5a840.md)
- [00c5a8f0](../00c5a/00c5a8f0.md)

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

## 疑似コード / UTF-8 10171 bytes

~~~c

void FUN_00aacea4(uint param_1,undefined8 param_2,undefined8 param_3)

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
  
                    /* catch() { ... } // from try @ 00aacdb0 with catch @ 00aacea4
                       catch() { ... } // from try @ 00aacde0 with catch @ 00aacea4 */
                    /* catch() { ... } // from try @ 00aaccf8 with catch @ 00aacea8 */
                    /* catch() { ... } // from try @ 00aaccf0 with catch @ 00aaceb0 */
  lVar1 = tpidr_el0;
                    /* catch() { ... } // from try @ 00aacd2c with catch @ 00aacec8 */
  local_58 = *(long *)(lVar1 + 0x28);
  if (param_1 < 3) {
    FUN_008514f8();
    iVar2 = FUN_00853c70();
    if (iVar2 == 300) {
                    /* try { // try from 00aad16c to 00bad27b has its CatchHandler @ 00aacf68 */
      iVar3 = FUN_005e0d68();
    }
    else {
      if (iVar2 != 100) goto LAB_00aad434;
      lVar4 = FUN_008514f8();
      iVar3 = *(int *)((long)&fde_table_entry_00333f48.data_loc + lVar4);
    }
    if (iVar3 < 0) goto LAB_00aad434;
    local_148 = 0x28;
    uStack_137 = 0x72656767;
    uStack_13f = (undefined7)s_BcLogPurchaseTrigger_002bac25._8_8_;
    cStack_138 = SUB81(s_BcLogPurchaseTrigger_002bac25._8_8_,7);
    uStack_133 = 0;
    local_118 = "sec1_type";
    local_110[0] = 0;
    local_108 = 0;
    local_130[0] = 0;
    local_147 = (char  [8])s_BcLogPurchaseTrigger_002bac25._0_8_;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Trigger";
    _ZN8firebase7VariantaSEOS0_(local_110,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    _ZNSt6__ndk19to_stringEi(local_178,param_1);
    FUN_00784280(auStack_160,local_178);
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
                    /* try { // try from 00aad27c to 00bad29f has its CatchHandler @ 00aad460 */
    local_1c0 = 10;
    local_1bf = 0x252d6425;
    local_1bb = 100;
                    /* try { // try from 00aad2a0 to 00bad30b has its CatchHandler @ 00aacf68 */
    FUN_004476f4(local_1a8,&local_1c0,0,iVar2,iVar3);
    FUN_00784280(auStack_190,local_1a8);
    local_b8 = "sec2_id";
    local_b0[0] = 0;
    local_a8 = 0;
    _ZN8firebase7VariantaSERKS0_(local_b0,auStack_190);
    local_98 = "ex_type";
    local_90[0] = 0;
    local_88 = 0;
    local_130[0] = 0;
                    /* try { // try from 00aad30c to 00bad317 has its CatchHandler @ 00aad43c */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
                    /* try { // try from 00aad318 to 00bad3ef has its CatchHandler @ 00aacf68 */
    local_128 = "Content";
    _ZN8firebase7VariantaSEOS0_(local_90,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    FUN_00784280(auStack_1d8,param_3);
    local_70[0] = 0;
    local_78 = "ex_id";
    local_68 = 0;
    _ZN8firebase7VariantaSERKS0_(local_70,auStack_1d8);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_1d8,0);
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
    lVar4 = FUN_008514f8();
    FUN_0087929c(*(undefined8 *)(lVar4 + 0x22b0),(ulong)&local_148 | 1,&local_118,6);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_70,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_90,0);
                    /* try { // try from 00aad3f0 to 00bad40f has its CatchHandler @ 00aad440 */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_b0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_d0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_f0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_110,0);
  }
  else {
    local_148 = 0x28;
    uStack_137 = 0x72656767;
    uStack_13f = (undefined7)s_BcLogPurchaseTrigger_002bac25._8_8_;
    cStack_138 = SUB81(s_BcLogPurchaseTrigger_002bac25._8_8_,7);
    local_147 = (char  [8])s_BcLogPurchaseTrigger_002bac25._0_8_;
    uStack_133 = 0;
    local_118 = "sec1_type";
    local_110[0] = 0;
    local_108 = 0;
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
                    /* try { // try from 00aacf68 to 00bacff3 has its CatchHandler @ 00aacf68
                       catch() { ... } // from try @ 00aacf68 with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad030 with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad0c4 with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad16c with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad2a0 with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad318 with catch @ 00aacf68
                       catch() { ... } // from try @ 00aad42c with catch @ 00aacf68 */
    local_128 = "Trigger";
    _ZN8firebase7VariantaSEOS0_(local_110,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    _ZNSt6__ndk19to_stringEi(local_178,param_1);
    FUN_00784280(auStack_1f0,local_178);
    local_f8 = "sec1_id";
    local_f0[0] = 0;
    local_e8 = 0;
    _ZN8firebase7VariantaSERKS0_(local_f0,auStack_1f0);
    local_d8 = "sec2_type";
    local_d0[0] = 0;
    local_c8 = 0;
    local_130[0] = 0;
                    /* try { // try from 00aacff4 to 00bacffb has its CatchHandler @ 00aad450 */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Select";
    _ZN8firebase7VariantaSEOS0_(local_d0,local_130);
                    /* try { // try from 00aad010 to 00bad017 has its CatchHandler @ 00aad44c */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
                    /* try { // try from 00aad01c to 00bad023 has its CatchHandler @ 00aad444 */
                    /* try { // try from 00aad024 to 00bad02f has its CatchHandler @ 00aad448 */
    FUN_00784280(auStack_208,param_2);
                    /* try { // try from 00aad030 to 00bad0bf has its CatchHandler @ 00aacf68 */
    local_b0[0] = 0;
    local_b8 = "sec2_id";
    local_a8 = 0;
    _ZN8firebase7VariantaSERKS0_(local_b0,auStack_208);
    local_98 = "ex_type";
    local_90[0] = 0;
    local_88 = 0;
    local_130[0] = 0;
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,4);
    local_128 = "Content";
    _ZN8firebase7VariantaSEOS0_(local_90,local_130);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_130,0);
    FUN_00784280(auStack_220,param_3);
    local_70[0] = 0;
    local_78 = "ex_id";
    local_68 = 0;
                    /* try { // try from 00aad0c0 to 00bad0c3 has its CatchHandler @ 00aad448 */
                    /* try { // try from 00aad0c4 to 00bad163 has its CatchHandler @ 00aacf68 */
    _ZN8firebase7VariantaSERKS0_(local_70,auStack_220);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_220,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_208,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_1f0,0);
    if ((local_178[0] & 1) != 0) {
      _ZdlPv(local_168);
    }
    lVar4 = FUN_008514f8();
    FUN_0087929c(*(undefined8 *)(lVar4 + 0x22b0),(ulong)&local_148 | 1,&local_118,6);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_70,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_90,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_b0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_d0,0);
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_f0,0);
                    /* try { // try from 00aad164 to 00bad16b has its CatchHandler @ 00aad42c */
    _ZN8firebase7Variant5ClearENS0_4TypeE(local_110,0);
  }
                    /* try { // try from 00aad424 to 00bad42b has its CatchHandler @ 00aad42c */
  if ((local_148 & 1) != 0) {
                    /* catch() { ... } // from try @ 00aad164 with catch @ 00aad42c
                       catch() { ... } // from try @ 00aad424 with catch @ 00aad42c
                       try { // try from 00aad42c to 00bad4a3 has its CatchHandler @ 00aacf68 */
    _ZdlPv((void *)CONCAT26(uStack_132,CONCAT15(uStack_133,CONCAT41(uStack_137,cStack_138))));
  }
LAB_00aad434:
                    /* catch() { ... } // from try @ 00aad30c with catch @ 00aad43c */
                    /* catch() { ... } // from try @ 00aad3f0 with catch @ 00aad440 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00aad01c with catch @ 00aad444 */
                    /* catch() { ... } // from try @ 00aad024 with catch @ 00aad448
                       catch() { ... } // from try @ 00aad0c0 with catch @ 00aad448 */
                    /* catch() { ... } // from try @ 00aad010 with catch @ 00aad44c */
                    /* catch() { ... } // from try @ 00aacff4 with catch @ 00aad450 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
