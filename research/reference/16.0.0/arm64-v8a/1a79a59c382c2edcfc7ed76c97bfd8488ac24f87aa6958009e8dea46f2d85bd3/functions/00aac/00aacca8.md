# 00aacca8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a4ec84`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-0dbd3f1ded0bd97f9fd715b1b82cd6ef)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aacea4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aac/00aacea4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-e77ecb2e507432b400d78db60275444c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "41e791aaa4c4c12ae7cd86a88c9b22dee330c83b48e25fe189df5f41cc977d23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aacca8",
        "00aad263"
      ],
      [
        "00aad494",
        "00aad497"
      ]
    ],
    "bytes_sha256": "78b55ef8a282f624b05efca5845e3a479506269a5c5564affaf25f549200fa07",
    "instruction_count": 368,
    "instruction_bytes": 1472,
    "body_bytes": 1472,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aacca8"></a> `00aacca8` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00aaccac"></a> `00aaccac` | `fc 67 01 a9` | stp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaccb0"></a> `00aaccb0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaccb4"></a> `00aaccb4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaccb8"></a> `00aaccb8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaccbc"></a> `00aaccbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaccc0"></a> `00aaccc0` | `ff 43 07 d1` | sub sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00aaccc4"></a> `00aaccc4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaccc8"></a> `00aaccc8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00aacccc"></a> `00aacccc` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aaccd0"></a> `00aaccd0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00aaccd4"></a> `00aaccd4` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aaccd8"></a> `00aaccd8` | `f9 63 03 91` | add x25,sp,#0xd8 | `FALL_THROUGH`
<a id="insn-00aaccdc"></a> `00aaccdc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aacce0"></a> `00aacce0` | `c8 01 00 54` | b.hi 0x00aacd18 | `CONDITIONAL_JUMP`
<a id="insn-00aacce4"></a> `00aacce4` | `f5 91 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aacce8"></a> `00aacce8` | `d2 9b f6 97` | bl 0x00853c30 | `UNCONDITIONAL_CALL`
<a id="insn-00aaccec"></a> `00aaccec` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaccf0"></a> `00aaccf0` | `1f b0 04 71` | cmp w0,#0x12c | `FALL_THROUGH`
<a id="insn-00aaccf4"></a> `00aaccf4` | `e0 13 00 54` | b.eq 0x00aacf70 | `CONDITIONAL_JUMP`
<a id="insn-00aaccf8"></a> `00aaccf8` | `bf 92 01 71` | cmp w21,#0x64 | `FALL_THROUGH`
<a id="insn-00aaccfc"></a> `00aaccfc` | `e1 29 00 54` | b.ne 0x00aad238 | `CONDITIONAL_JUMP`
<a id="insn-00aacd00"></a> `00aacd00` | `ee 91 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aacd04"></a> `00aacd04` | `88 e9 87 52` | mov w8,#0x3f4c | `FALL_THROUGH`
<a id="insn-00aacd08"></a> `00aacd08` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aacd0c"></a> `00aacd0c` | `17 68 68 b8` | ldr w23,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aacd10"></a> `00aacd10` | `77 13 f8 36` | tbz w23,#0x1f,0x00aacf7c | `CONDITIONAL_JUMP`
<a id="insn-00aacd14"></a> `00aacd14` | `49 01 00 14` | b 0x00aad238 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacd18"></a> `00aacd18` | `69 c0 ff d0` | adrp x9,0x2ba000 | `FALL_THROUGH`
<a id="insn-00aacd1c"></a> `00aacd1c` | `29 95 2f 91` | add x9,x9,#0xbe5 | `FALL_THROUGH`
<a id="insn-00aacd20"></a> `00aacd20` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aacd24"></a> `00aacd24` | `ea ec 8c 52` | mov w10,#0x6767 | `FALL_THROUGH`
<a id="insn-00aacd28"></a> `00aacd28` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacd2c"></a> `00aacd2c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00aacd30"></a> `00aacd30` | `aa 4c ae 72` | movk w10,#0x7265, LSL #16 | `FALL_THROUGH`
<a id="insn-00aacd34"></a> `00aacd34` | `e8 63 03 39` | strb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aacd38"></a> `00aacd38` | `08 c0 ff d0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aacd3c"></a> `00aacd3c` | `08 d1 2a 91` | add x8,x8,#0xab4 | `FALL_THROUGH`
<a id="insn-00aacd40"></a> `00aacd40` | `b4 23 03 d1` | sub x20,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacd44"></a> `00aacd44` | `2a 13 01 b8` | stur w10,[x25, #0x11] | `FALL_THROUGH`
<a id="insn-00aacd48"></a> `00aacd48` | `20 13 80 3c` | stur q0,[x25, #0x1] | `FALL_THROUGH`
<a id="insn-00aacd4c"></a> `00aacd4c` | `ff b7 03 39` | strb wzr,[sp, #0xed] | `FALL_THROUGH`
<a id="insn-00aacd50"></a> `00aacd50` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-00aacd54"></a> `00aacd54` | `bf 03 14 b8` | stur wzr,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-00aacd58"></a> `00aacd58` | `bf 83 14 f8` | stur xzr,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-00aacd5c"></a> `00aacd5c` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aacd60"></a> `00aacd60` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacd64"></a> `00aacd64` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aacd68"></a> `00aacd68` | `b2 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacd6c"></a> `00aacd6c` | `48 c0 ff f0` | adrp x8,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aacd70"></a> `00aacd70` | `08 1d 2d 91` | add x8,x8,#0xb47 | `FALL_THROUGH`
<a id="insn-00aacd74"></a> `00aacd74` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aacd78"></a> `00aacd78` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacd7c"></a> `00aacd7c` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aacd80"></a> `00aacd80` | `b0 b5 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aacd84"></a> `00aacd84` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacd88"></a> `00aacd88` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacd8c"></a> `00aacd8c` | `a9 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacd90"></a> `00aacd90` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacd94"></a> `00aacd94` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacd98"></a> `00aacd98` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacd9c"></a> `00aacd9c` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aacda0"></a> `00aacda0` | `6c ab 06 94` | bl 0x00c57b50 | `UNCONDITIONAL_CALL`
<a id="insn-00aacda4"></a> `00aacda4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aacda8"></a> `00aacda8` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacdac"></a> `00aacdac` | `25 5d f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aacdb0"></a> `00aacdb0` | `28 c0 ff b0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aacdb4"></a> `00aacdb4` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00aacdb8"></a> `00aacdb8` | `b6 23 03 d1` | sub x22,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacdbc"></a> `00aacdbc` | `a8 83 15 f8` | stur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00aacdc0"></a> `00aacdc0` | `bf 03 16 b8` | stur wzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00aacdc4"></a> `00aacdc4` | `bf 83 16 f8` | stur xzr,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-00aacdc8"></a> `00aacdc8` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00aacdcc"></a> `00aacdcc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aacdd0"></a> `00aacdd0` | `c8 b5 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aacdd4"></a> `00aacdd4` | `c8 bf ff f0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aacdd8"></a> `00aacdd8` | `08 79 27 91` | add x8,x8,#0x9de | `FALL_THROUGH`
<a id="insn-00aacddc"></a> `00aacddc` | `d4 02 01 91` | add x20,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00aacde0"></a> `00aacde0` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-00aacde4"></a> `00aacde4` | `bf 03 18 b8` | stur wzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00aacde8"></a> `00aacde8` | `bf 83 18 f8` | stur xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00aacdec"></a> `00aacdec` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aacdf0"></a> `00aacdf0` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacdf4"></a> `00aacdf4` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aacdf8"></a> `00aacdf8` | `8e b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacdfc"></a> `00aacdfc` | `a8 bf ff b0` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-00aace00"></a> `00aace00` | `08 c1 1e 91` | add x8,x8,#0x7b0 | `FALL_THROUGH`
<a id="insn-00aace04"></a> `00aace04` | `c0 22 01 91` | add x0,x22,#0x48 | `FALL_THROUGH`
<a id="insn-00aace08"></a> `00aace08` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aace0c"></a> `00aace0c` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aace10"></a> `00aace10` | `8c b5 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aace14"></a> `00aace14` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aace18"></a> `00aace18` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aace1c"></a> `00aace1c` | `85 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aace20"></a> `00aace20` | `d4 82 01 91` | add x20,x22,#0x60 | `FALL_THROUGH`
<a id="insn-00aace24"></a> `00aace24` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aace28"></a> `00aace28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aace2c"></a> `00aace2c` | `05 5d f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aace30"></a> `00aace30` | `08 c0 ff f0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aace34"></a> `00aace34` | `08 ad 2f 91` | add x8,x8,#0xbeb | `FALL_THROUGH`
<a id="insn-00aace38"></a> `00aace38` | `bf 03 1a b8` | stur wzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00aace3c"></a> `00aace3c` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00aace40"></a> `00aace40` | `bf 83 1a f8` | stur xzr,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00aace44"></a> `00aace44` | `c0 a2 01 91` | add x0,x22,#0x68 | `FALL_THROUGH`
<a id="insn-00aace48"></a> `00aace48` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aace4c"></a> `00aace4c` | `a9 b5 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aace50"></a> `00aace50` | `b5 23 03 d1` | sub x21,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aace54"></a> `00aace54` | `e8 bf ff 90` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aace58"></a> `00aace58` | `08 a9 34 91` | add x8,x8,#0xd2a | `FALL_THROUGH`
<a id="insn-00aace5c"></a> `00aace5c` | `b4 02 02 91` | add x20,x21,#0x80 | `FALL_THROUGH`
<a id="insn-00aace60"></a> `00aace60` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00aace64"></a> `00aace64` | `bf 03 1c b8` | stur wzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aace68"></a> `00aace68` | `bf 83 1c f8` | stur xzr,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aace6c"></a> `00aace6c` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aace70"></a> `00aace70` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aace74"></a> `00aace74` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aace78"></a> `00aace78` | `6e b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aace7c"></a> `00aace7c` | `88 c0 ff d0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aace80"></a> `00aace80` | `08 d5 0d 91` | add x8,x8,#0x375 | `FALL_THROUGH`
<a id="insn-00aace84"></a> `00aace84` | `a0 22 02 91` | add x0,x21,#0x88 | `FALL_THROUGH`
<a id="insn-00aace88"></a> `00aace88` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aace8c"></a> `00aace8c` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aace90"></a> `00aace90` | `6c b5 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aace94"></a> `00aace94` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aace98"></a> `00aace98` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aace9c"></a> `00aace9c` | `65 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacea0"></a> `00aacea0` | `b4 82 02 91` | add x20,x21,#0xa0 | `FALL_THROUGH`
<a id="insn-00aacea4"></a> `00aacea4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aacea8"></a> `00aacea8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aaceac"></a> `00aaceac` | `e5 5c f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aaceb0"></a> `00aaceb0` | `88 c0 ff d0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aaceb4"></a> `00aaceb4` | `08 35 3b 91` | add x8,x8,#0xecd | `FALL_THROUGH`
<a id="insn-00aaceb8"></a> `00aaceb8` | `bf 03 1e b8` | stur wzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aacebc"></a> `00aacebc` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aacec0"></a> `00aacec0` | `bf 83 1e f8` | stur xzr,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aacec4"></a> `00aacec4` | `a0 a2 02 91` | add x0,x21,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacec8"></a> `00aacec8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aacecc"></a> `00aacecc` | `89 b5 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaced0"></a> `00aaced0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aaced4"></a> `00aaced4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aaced8"></a> `00aaced8` | `56 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacedc"></a> `00aacedc` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aacee0"></a> `00aacee0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacee4"></a> `00aacee4` | `53 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacee8"></a> `00aacee8` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aaceec"></a> `00aaceec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacef0"></a> `00aacef0` | `50 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacef4"></a> `00aacef4` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aacef8"></a> `00aacef8` | `68 00 00 36` | tbz w8,#0x0,0x00aacf04 | `CONDITIONAL_JUMP`
<a id="insn-00aacefc"></a> `00aacefc` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00aacf00"></a> `00aacf00` | `ec aa 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf04"></a> `00aacf04` | `6d 91 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf08"></a> `00aacf08` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aacf0c"></a> `00aacf0c` | `21 03 40 b2` | orr x1,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00aacf10"></a> `00aacf10` | `a2 23 03 d1` | sub x2,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacf14"></a> `00aacf14` | `c3 00 80 52` | mov w3,#0x6 | `FALL_THROUGH`
<a id="insn-00aacf18"></a> `00aacf18` | `b3 23 03 d1` | sub x19,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacf1c"></a> `00aacf1c` | `d0 30 f7 97` | bl 0x0087925c | `UNCONDITIONAL_CALL`
<a id="insn-00aacf20"></a> `00aacf20` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacf24"></a> `00aacf24` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf28"></a> `00aacf28` | `42 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf2c"></a> `00aacf2c` | `60 22 02 91` | add x0,x19,#0x88 | `FALL_THROUGH`
<a id="insn-00aacf30"></a> `00aacf30` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf34"></a> `00aacf34` | `3f b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf38"></a> `00aacf38` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aacf3c"></a> `00aacf3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf40"></a> `00aacf40` | `3c b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf44"></a> `00aacf44` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aacf48"></a> `00aacf48` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf4c"></a> `00aacf4c` | `39 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf50"></a> `00aacf50` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aacf54"></a> `00aacf54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf58"></a> `00aacf58` | `36 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf5c"></a> `00aacf5c` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacf60"></a> `00aacf60` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aacf64"></a> `00aacf64` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf68"></a> `00aacf68` | `32 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf6c"></a> `00aacf6c` | `af 00 00 14` | b 0x00aad228 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacf70"></a> `00aacf70` | `6e cf ec 97` | bl 0x005e0d28 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf74"></a> `00aacf74` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aacf78"></a> `00aacf78` | `17 16 f8 37` | tbnz w23,#0x1f,0x00aad238 | `CONDITIONAL_JUMP`
<a id="insn-00aacf7c"></a> `00aacf7c` | `69 c0 ff d0` | adrp x9,0x2ba000 | `FALL_THROUGH`
<a id="insn-00aacf80"></a> `00aacf80` | `29 95 2f 91` | add x9,x9,#0xbe5 | `FALL_THROUGH`
<a id="insn-00aacf84"></a> `00aacf84` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aacf88"></a> `00aacf88` | `ea ec 8c 52` | mov w10,#0x6767 | `FALL_THROUGH`
<a id="insn-00aacf8c"></a> `00aacf8c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacf90"></a> `00aacf90` | `e8 63 03 39` | strb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aacf94"></a> `00aacf94` | `aa 4c ae 72` | movk w10,#0x7265, LSL #16 | `FALL_THROUGH`
<a id="insn-00aacf98"></a> `00aacf98` | `08 c0 ff d0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aacf9c"></a> `00aacf9c` | `08 d1 2a 91` | add x8,x8,#0xab4 | `FALL_THROUGH`
<a id="insn-00aacfa0"></a> `00aacfa0` | `b4 23 03 d1` | sub x20,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacfa4"></a> `00aacfa4` | `2a 13 01 b8` | stur w10,[x25, #0x11] | `FALL_THROUGH`
<a id="insn-00aacfa8"></a> `00aacfa8` | `20 13 80 3c` | stur q0,[x25, #0x1] | `FALL_THROUGH`
<a id="insn-00aacfac"></a> `00aacfac` | `ff b7 03 39` | strb wzr,[sp, #0xed] | `FALL_THROUGH`
<a id="insn-00aacfb0"></a> `00aacfb0` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-00aacfb4"></a> `00aacfb4` | `bf 03 14 b8` | stur wzr,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-00aacfb8"></a> `00aacfb8` | `bf 83 14 f8` | stur xzr,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-00aacfbc"></a> `00aacfbc` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aacfc0"></a> `00aacfc0` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacfc4"></a> `00aacfc4` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aacfc8"></a> `00aacfc8` | `1a b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfcc"></a> `00aacfcc` | `48 c0 ff f0` | adrp x8,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aacfd0"></a> `00aacfd0` | `08 1d 2d 91` | add x8,x8,#0xb47 | `FALL_THROUGH`
<a id="insn-00aacfd4"></a> `00aacfd4` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aacfd8"></a> `00aacfd8` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacfdc"></a> `00aacfdc` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aacfe0"></a> `00aacfe0` | `18 b5 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfe4"></a> `00aacfe4` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacfe8"></a> `00aacfe8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacfec"></a> `00aacfec` | `11 b5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aacff0"></a> `00aacff0` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacff4"></a> `00aacff4` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacff8"></a> `00aacff8` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacffc"></a> `00aacffc` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aad000"></a> `00aad000` | `d4 aa 06 94` | bl 0x00c57b50 | `UNCONDITIONAL_CALL`
<a id="insn-00aad004"></a> `00aad004` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad008"></a> `00aad008` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad00c"></a> `00aad00c` | `8d 5c f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aad010"></a> `00aad010` | `28 c0 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aad014"></a> `00aad014` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00aad018"></a> `00aad018` | `b6 23 03 d1` | sub x22,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad01c"></a> `00aad01c` | `a8 83 15 f8` | stur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00aad020"></a> `00aad020` | `bf 03 16 b8` | stur wzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00aad024"></a> `00aad024` | `bf 83 16 f8` | stur xzr,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-00aad028"></a> `00aad028` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00aad02c"></a> `00aad02c` | `e1 03 03 91` | add x1,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad030"></a> `00aad030` | `30 b5 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad034"></a> `00aad034` | `c8 bf ff d0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aad038"></a> `00aad038` | `08 79 27 91` | add x8,x8,#0x9de | `FALL_THROUGH`
<a id="insn-00aad03c"></a> `00aad03c` | `d4 02 01 91` | add x20,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00aad040"></a> `00aad040` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-00aad044"></a> `00aad044` | `bf 03 18 b8` | stur wzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00aad048"></a> `00aad048` | `bf 83 18 f8` | stur xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00aad04c"></a> `00aad04c` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad050"></a> `00aad050` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad054"></a> `00aad054` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad058"></a> `00aad058` | `f6 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad05c"></a> `00aad05c` | `a8 bf ff 90` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-00aad060"></a> `00aad060` | `08 c1 1e 91` | add x8,x8,#0x7b0 | `FALL_THROUGH`
<a id="insn-00aad064"></a> `00aad064` | `c0 22 01 91` | add x0,x22,#0x48 | `FALL_THROUGH`
<a id="insn-00aad068"></a> `00aad068` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad06c"></a> `00aad06c` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad070"></a> `00aad070` | `f4 b4 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aad074"></a> `00aad074` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad078"></a> `00aad078` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad07c"></a> `00aad07c` | `ed b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad080"></a> `00aad080` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00aad084"></a> `00aad084` | `a9 84 8c 52` | mov w9,#0x6425 | `FALL_THROUGH`
<a id="insn-00aad088"></a> `00aad088` | `8a 0c 80 52` | mov w10,#0x64 | `FALL_THROUGH`
<a id="insn-00aad08c"></a> `00aad08c` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aad090"></a> `00aad090` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad094"></a> `00aad094` | `a9 a5 a4 72` | movk w9,#0x252d, LSL #16 | `FALL_THROUGH`
<a id="insn-00aad098"></a> `00aad098` | `14 81 01 91` | add x20,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aad09c"></a> `00aad09c` | `e9 13 06 b8` | stur w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aad0a0"></a> `00aad0a0` | `ea 53 06 78` | sturh w10,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00aad0a4"></a> `00aad0a4` | `e8 e3 01 91` | add x8,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00aad0a8"></a> `00aad0a8` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aad0ac"></a> `00aad0ac` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aad0b0"></a> `00aad0b0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aad0b4"></a> `00aad0b4` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-00aad0b8"></a> `00aad0b8` | `7f 69 e6 97` | bl 0x004476b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0bc"></a> `00aad0bc` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad0c0"></a> `00aad0c0` | `e1 e3 01 91` | add x1,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00aad0c4"></a> `00aad0c4` | `5f 5c f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0c8"></a> `00aad0c8` | `08 c0 ff d0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aad0cc"></a> `00aad0cc` | `08 ad 2f 91` | add x8,x8,#0xbeb | `FALL_THROUGH`
<a id="insn-00aad0d0"></a> `00aad0d0` | `b5 23 03 d1` | sub x21,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad0d4"></a> `00aad0d4` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00aad0d8"></a> `00aad0d8` | `bf 03 1a b8` | stur wzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00aad0dc"></a> `00aad0dc` | `bf 83 1a f8` | stur xzr,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00aad0e0"></a> `00aad0e0` | `a0 a2 01 91` | add x0,x21,#0x68 | `FALL_THROUGH`
<a id="insn-00aad0e4"></a> `00aad0e4` | `e1 43 02 91` | add x1,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad0e8"></a> `00aad0e8` | `02 b5 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0ec"></a> `00aad0ec` | `c8 bf ff f0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aad0f0"></a> `00aad0f0` | `08 a9 34 91` | add x8,x8,#0xd2a | `FALL_THROUGH`
<a id="insn-00aad0f4"></a> `00aad0f4` | `b4 02 02 91` | add x20,x21,#0x80 | `FALL_THROUGH`
<a id="insn-00aad0f8"></a> `00aad0f8` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00aad0fc"></a> `00aad0fc` | `bf 03 1c b8` | stur wzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aad100"></a> `00aad100` | `bf 83 1c f8` | stur xzr,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aad104"></a> `00aad104` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad108"></a> `00aad108` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad10c"></a> `00aad10c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad110"></a> `00aad110` | `c8 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad114"></a> `00aad114` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad118"></a> `00aad118` | `08 d5 0d 91` | add x8,x8,#0x375 | `FALL_THROUGH`
<a id="insn-00aad11c"></a> `00aad11c` | `a0 22 02 91` | add x0,x21,#0x88 | `FALL_THROUGH`
<a id="insn-00aad120"></a> `00aad120` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad124"></a> `00aad124` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad128"></a> `00aad128` | `c6 b4 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aad12c"></a> `00aad12c` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad130"></a> `00aad130` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad134"></a> `00aad134` | `bf b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad138"></a> `00aad138` | `b4 82 02 91` | add x20,x21,#0xa0 | `FALL_THROUGH`
<a id="insn-00aad13c"></a> `00aad13c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad140"></a> `00aad140` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aad144"></a> `00aad144` | `3f 5c f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aad148"></a> `00aad148` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad14c"></a> `00aad14c` | `08 35 3b 91` | add x8,x8,#0xecd | `FALL_THROUGH`
<a id="insn-00aad150"></a> `00aad150` | `bf 03 1e b8` | stur wzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aad154"></a> `00aad154` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aad158"></a> `00aad158` | `bf 83 1e f8` | stur xzr,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aad15c"></a> `00aad15c` | `a0 a2 02 91` | add x0,x21,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad160"></a> `00aad160` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad164"></a> `00aad164` | `e3 b4 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad168"></a> `00aad168` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad16c"></a> `00aad16c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad170"></a> `00aad170` | `b0 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad174"></a> `00aad174` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad178"></a> `00aad178` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad17c"></a> `00aad17c` | `ad b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad180"></a> `00aad180` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aad184"></a> `00aad184` | `68 00 00 36` | tbz w8,#0x0,0x00aad190 | `CONDITIONAL_JUMP`
<a id="insn-00aad188"></a> `00aad188` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aad18c"></a> `00aad18c` | `49 aa 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad190"></a> `00aad190` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aad194"></a> `00aad194` | `68 00 00 36` | tbz w8,#0x0,0x00aad1a0 | `CONDITIONAL_JUMP`
<a id="insn-00aad198"></a> `00aad198` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aad19c"></a> `00aad19c` | `45 aa 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1a0"></a> `00aad1a0` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad1a4"></a> `00aad1a4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad1a8"></a> `00aad1a8` | `a2 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1ac"></a> `00aad1ac` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aad1b0"></a> `00aad1b0` | `68 00 00 36` | tbz w8,#0x0,0x00aad1bc | `CONDITIONAL_JUMP`
<a id="insn-00aad1b4"></a> `00aad1b4` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00aad1b8"></a> `00aad1b8` | `3e aa 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1bc"></a> `00aad1bc` | `bf 90 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1c0"></a> `00aad1c0` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aad1c4"></a> `00aad1c4` | `e8 63 03 91` | add x8,sp,#0xd8 | `FALL_THROUGH`
<a id="insn-00aad1c8"></a> `00aad1c8` | `01 01 40 b2` | orr x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aad1cc"></a> `00aad1cc` | `a2 23 03 d1` | sub x2,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad1d0"></a> `00aad1d0` | `c3 00 80 52` | mov w3,#0x6 | `FALL_THROUGH`
<a id="insn-00aad1d4"></a> `00aad1d4` | `b3 23 03 d1` | sub x19,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad1d8"></a> `00aad1d8` | `21 30 f7 97` | bl 0x0087925c | `UNCONDITIONAL_CALL`
<a id="insn-00aad1dc"></a> `00aad1dc` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad1e0"></a> `00aad1e0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad1e4"></a> `00aad1e4` | `93 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1e8"></a> `00aad1e8` | `60 22 02 91` | add x0,x19,#0x88 | `FALL_THROUGH`
<a id="insn-00aad1ec"></a> `00aad1ec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad1f0"></a> `00aad1f0` | `90 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1f4"></a> `00aad1f4` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aad1f8"></a> `00aad1f8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad1fc"></a> `00aad1fc` | `8d b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad200"></a> `00aad200` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aad204"></a> `00aad204` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad208"></a> `00aad208` | `8a b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad20c"></a> `00aad20c` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aad210"></a> `00aad210` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad214"></a> `00aad214` | `87 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad218"></a> `00aad218` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad21c"></a> `00aad21c` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aad220"></a> `00aad220` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad224"></a> `00aad224` | `83 b4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aad228"></a> `00aad228` | `e8 63 43 39` | ldrb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aad22c"></a> `00aad22c` | `68 00 00 36` | tbz w8,#0x0,0x00aad238 | `CONDITIONAL_JUMP`
<a id="insn-00aad230"></a> `00aad230` | `e0 77 40 f9` | ldr x0,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00aad234"></a> `00aad234` | `1f aa 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad238"></a> `00aad238` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00aad23c"></a> `00aad23c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aad240"></a> `00aad240` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aad244"></a> `00aad244` | `81 12 00 54` | b.ne 0x00aad494 | `CONDITIONAL_JUMP`
<a id="insn-00aad248"></a> `00aad248` | `ff 43 07 91` | add sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00aad24c"></a> `00aad24c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aad250"></a> `00aad250` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aad254"></a> `00aad254` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aad258"></a> `00aad258` | `fc 67 41 a9` | ldp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aad25c"></a> `00aad25c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00aad260"></a> `00aad260` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aad494"></a> `00aad494` | `93 a9 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aacca8`](#insn-00aacca8) 範囲 `[['00aacca8', '00aacce3']]`
  - `CONDITIONAL_JUMP` [`00aacce0`](#insn-00aacce0) → [`00aacd18`](#insn-00aacd18)
  - `FALL_THROUGH` [`00aacce0`](#insn-00aacce0) → [`00aacce4`](#insn-00aacce4)
- ブロック [`00aacce4`](#insn-00aacce4) 範囲 `[['00aacce4', '00aacce7']]`
  - `FALL_THROUGH` [`00aacce4`](#insn-00aacce4) → [`00aacce8`](#insn-00aacce8)
- ブロック [`00aacce8`](#insn-00aacce8) 範囲 `[['00aacce8', '00aaccf7']]`
  - `CONDITIONAL_JUMP` [`00aaccf4`](#insn-00aaccf4) → [`00aacf70`](#insn-00aacf70)
  - `FALL_THROUGH` [`00aaccf4`](#insn-00aaccf4) → [`00aaccf8`](#insn-00aaccf8)
- ブロック [`00aaccf8`](#insn-00aaccf8) 範囲 `[['00aaccf8', '00aaccff']]`
  - `CONDITIONAL_JUMP` [`00aaccfc`](#insn-00aaccfc) → [`00aad238`](#insn-00aad238)
  - `FALL_THROUGH` [`00aaccfc`](#insn-00aaccfc) → [`00aacd00`](#insn-00aacd00)
- ブロック [`00aacd00`](#insn-00aacd00) 範囲 `[['00aacd00', '00aacd03']]`
  - `FALL_THROUGH` [`00aacd00`](#insn-00aacd00) → [`00aacd04`](#insn-00aacd04)
- ブロック [`00aacd04`](#insn-00aacd04) 範囲 `[['00aacd04', '00aacd07']]`
  - `FALL_THROUGH` [`00aacd04`](#insn-00aacd04) → [`00aacd08`](#insn-00aacd08)
- ブロック [`00aacd08`](#insn-00aacd08) 範囲 `[['00aacd08', '00aacd0b']]`
  - `FALL_THROUGH` [`00aacd08`](#insn-00aacd08) → [`00aacd0c`](#insn-00aacd0c)
- ブロック [`00aacd0c`](#insn-00aacd0c) 範囲 `[['00aacd0c', '00aacd13']]`
  - `CONDITIONAL_JUMP` [`00aacd10`](#insn-00aacd10) → [`00aacf7c`](#insn-00aacf7c)
  - `FALL_THROUGH` [`00aacd10`](#insn-00aacd10) → [`00aacd14`](#insn-00aacd14)
- ブロック [`00aacd14`](#insn-00aacd14) 範囲 `[['00aacd14', '00aacd17']]`
  - `UNCONDITIONAL_JUMP` [`00aacd14`](#insn-00aacd14) → [`00aad238`](#insn-00aad238)
- ブロック [`00aacd18`](#insn-00aacd18) 範囲 `[['00aacd18', '00aacd2b']]`
  - `FALL_THROUGH` [`00aacd28`](#insn-00aacd28) → [`00aacd2c`](#insn-00aacd2c)
- ブロック [`00aacd2c`](#insn-00aacd2c) 範囲 `[['00aacd2c', '00aacdcb']]`
  - `FALL_THROUGH` [`00aacdc8`](#insn-00aacdc8) → [`00aacdcc`](#insn-00aacdcc)
- ブロック [`00aacdcc`](#insn-00aacdcc) 範囲 `[['00aacdcc', '00aace57']]`
  - `FALL_THROUGH` [`00aace54`](#insn-00aace54) → [`00aace58`](#insn-00aace58)
- ブロック [`00aace58`](#insn-00aace58) 範囲 `[['00aace58', '00aace73']]`
  - `FALL_THROUGH` [`00aace70`](#insn-00aace70) → [`00aace74`](#insn-00aace74)
- ブロック [`00aace74`](#insn-00aace74) 範囲 `[['00aace74', '00aace7f']]`
  - `FALL_THROUGH` [`00aace7c`](#insn-00aace7c) → [`00aace80`](#insn-00aace80)
- ブロック [`00aace80`](#insn-00aace80) 範囲 `[['00aace80', '00aace87']]`
  - `FALL_THROUGH` [`00aace84`](#insn-00aace84) → [`00aace88`](#insn-00aace88)
- ブロック [`00aace88`](#insn-00aace88) 範囲 `[['00aace88', '00aace93']]`
  - `FALL_THROUGH` [`00aace90`](#insn-00aace90) → [`00aace94`](#insn-00aace94)
- ブロック [`00aace94`](#insn-00aace94) 範囲 `[['00aace94', '00aacefb']]`
  - `CONDITIONAL_JUMP` [`00aacef8`](#insn-00aacef8) → [`00aacf04`](#insn-00aacf04)
  - `FALL_THROUGH` [`00aacef8`](#insn-00aacef8) → [`00aacefc`](#insn-00aacefc)
- ブロック [`00aacefc`](#insn-00aacefc) 範囲 `[['00aacefc', '00aacf03']]`
  - `FALL_THROUGH` [`00aacf00`](#insn-00aacf00) → [`00aacf04`](#insn-00aacf04)
- ブロック [`00aacf04`](#insn-00aacf04) 範囲 `[['00aacf04', '00aacf23']]`
  - `FALL_THROUGH` [`00aacf20`](#insn-00aacf20) → [`00aacf24`](#insn-00aacf24)
- ブロック [`00aacf24`](#insn-00aacf24) 範囲 `[['00aacf24', '00aacf27']]`
  - `FALL_THROUGH` [`00aacf24`](#insn-00aacf24) → [`00aacf28`](#insn-00aacf28)
- ブロック [`00aacf28`](#insn-00aacf28) 範囲 `[['00aacf28', '00aacf6f']]`
  - `UNCONDITIONAL_JUMP` [`00aacf6c`](#insn-00aacf6c) → [`00aad228`](#insn-00aad228)
- ブロック [`00aacf70`](#insn-00aacf70) 範囲 `[['00aacf70', '00aacf7b']]`
  - `CONDITIONAL_JUMP` [`00aacf78`](#insn-00aacf78) → [`00aad238`](#insn-00aad238)
  - `FALL_THROUGH` [`00aacf78`](#insn-00aacf78) → [`00aacf7c`](#insn-00aacf7c)
- ブロック [`00aacf7c`](#insn-00aacf7c) 範囲 `[['00aacf7c', '00aacfc7']]`
  - `FALL_THROUGH` [`00aacfc4`](#insn-00aacfc4) → [`00aacfc8`](#insn-00aacfc8)
- ブロック [`00aacfc8`](#insn-00aacfc8) 範囲 `[['00aacfc8', '00aacfcf']]`
  - `FALL_THROUGH` [`00aacfcc`](#insn-00aacfcc) → [`00aacfd0`](#insn-00aacfd0)
- ブロック [`00aacfd0`](#insn-00aacfd0) 範囲 `[['00aacfd0', '00aad0df']]`
  - `FALL_THROUGH` [`00aad0dc`](#insn-00aad0dc) → [`00aad0e0`](#insn-00aad0e0)
- ブロック [`00aad0e0`](#insn-00aad0e0) 範囲 `[['00aad0e0', '00aad103']]`
  - `FALL_THROUGH` [`00aad100`](#insn-00aad100) → [`00aad104`](#insn-00aad104)
- ブロック [`00aad104`](#insn-00aad104) 範囲 `[['00aad104', '00aad16f']]`
  - `FALL_THROUGH` [`00aad16c`](#insn-00aad16c) → [`00aad170`](#insn-00aad170)
- ブロック [`00aad170`](#insn-00aad170) 範囲 `[['00aad170', '00aad17b']]`
  - `FALL_THROUGH` [`00aad178`](#insn-00aad178) → [`00aad17c`](#insn-00aad17c)
- ブロック [`00aad17c`](#insn-00aad17c) 範囲 `[['00aad17c', '00aad187']]`
  - `CONDITIONAL_JUMP` [`00aad184`](#insn-00aad184) → [`00aad190`](#insn-00aad190)
  - `FALL_THROUGH` [`00aad184`](#insn-00aad184) → [`00aad188`](#insn-00aad188)
- ブロック [`00aad188`](#insn-00aad188) 範囲 `[['00aad188', '00aad18f']]`
  - `FALL_THROUGH` [`00aad18c`](#insn-00aad18c) → [`00aad190`](#insn-00aad190)
- ブロック [`00aad190`](#insn-00aad190) 範囲 `[['00aad190', '00aad197']]`
  - `CONDITIONAL_JUMP` [`00aad194`](#insn-00aad194) → [`00aad1a0`](#insn-00aad1a0)
  - `FALL_THROUGH` [`00aad194`](#insn-00aad194) → [`00aad198`](#insn-00aad198)
- ブロック [`00aad198`](#insn-00aad198) 範囲 `[['00aad198', '00aad19f']]`
  - `FALL_THROUGH` [`00aad19c`](#insn-00aad19c) → [`00aad1a0`](#insn-00aad1a0)
- ブロック [`00aad1a0`](#insn-00aad1a0) 範囲 `[['00aad1a0', '00aad1b3']]`
  - `CONDITIONAL_JUMP` [`00aad1b0`](#insn-00aad1b0) → [`00aad1bc`](#insn-00aad1bc)
  - `FALL_THROUGH` [`00aad1b0`](#insn-00aad1b0) → [`00aad1b4`](#insn-00aad1b4)
- ブロック [`00aad1b4`](#insn-00aad1b4) 範囲 `[['00aad1b4', '00aad1bb']]`
  - `FALL_THROUGH` [`00aad1b8`](#insn-00aad1b8) → [`00aad1bc`](#insn-00aad1bc)
- ブロック [`00aad1bc`](#insn-00aad1bc) 範囲 `[['00aad1bc', '00aad227']]`
  - `FALL_THROUGH` [`00aad224`](#insn-00aad224) → [`00aad228`](#insn-00aad228)
- ブロック [`00aad228`](#insn-00aad228) 範囲 `[['00aad228', '00aad22f']]`
  - `CONDITIONAL_JUMP` [`00aad22c`](#insn-00aad22c) → [`00aad238`](#insn-00aad238)
  - `FALL_THROUGH` [`00aad22c`](#insn-00aad22c) → [`00aad230`](#insn-00aad230)
- ブロック [`00aad230`](#insn-00aad230) 範囲 `[['00aad230', '00aad237']]`
  - `FALL_THROUGH` [`00aad234`](#insn-00aad234) → [`00aad238`](#insn-00aad238)
- ブロック [`00aad238`](#insn-00aad238) 範囲 `[['00aad238', '00aad247']]`
  - `CONDITIONAL_JUMP` [`00aad244`](#insn-00aad244) → [`00aad494`](#insn-00aad494)
  - `FALL_THROUGH` [`00aad244`](#insn-00aad244) → [`00aad248`](#insn-00aad248)
- ブロック [`00aad248`](#insn-00aad248) 範囲 `[['00aad248', '00aad253']]`
  - `FALL_THROUGH` [`00aad250`](#insn-00aad250) → [`00aad254`](#insn-00aad254)
- ブロック [`00aad254`](#insn-00aad254) 範囲 `[['00aad254', '00aad263']]`
- ブロック [`00aad494`](#insn-00aad494) 範囲 `[['00aad494', '00aad497']]`

## 命令位置別の参照

- [`00aacca8`](#insn-00aacca8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccac`](#insn-00aaccac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccb0`](#insn-00aaccb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccb4`](#insn-00aaccb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccb8`](#insn-00aaccb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccdc`](#insn-00aaccdc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacce0`](#insn-00aacce0) → [`00aacd18`](#insn-00aacd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacce4`](#insn-00aacce4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aacce8`](#insn-00aacce8) → [`00853c30`](../00853/00853c30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00853c30` · 推定シンボル `None` · 推定型 `None`
- [`00aaccf4`](#insn-00aaccf4) → [`00aacf70`](#insn-00aacf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaccfc`](#insn-00aaccfc) → [`00aad238`](#insn-00aad238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd00`](#insn-00aacd00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aacd0c`](#insn-00aacd0c) → `00333f4c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aacd10`](#insn-00aacd10) → [`00aacf7c`](#insn-00aacf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd14`](#insn-00aacd14) → [`00aad238`](#insn-00aad238) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd28`](#insn-00aacd28) → `002babe5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacd34`](#insn-00aacd34) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd44`](#insn-00aacd44) → `Stack[-0x137]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd48`](#insn-00aacd48) → `Stack[-0x147]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd4c`](#insn-00aacd4c) → `Stack[-0x133]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd50`](#insn-00aacd50) → `002aeab4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacd50`](#insn-00aacd50) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd54`](#insn-00aacd54) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd58`](#insn-00aacd58) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd5c`](#insn-00aacd5c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd68`](#insn-00aacd68) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacd7c`](#insn-00aacd7c) → `002b7b47`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacd7c`](#insn-00aacd7c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd80`](#insn-00aacd80) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aacd8c`](#insn-00aacd8c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacda0`](#insn-00aacda0) → [`00c57b50`](../00c57/00c57b50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b50` · 推定シンボル `None` · 推定型 `None`
- [`00aacdac`](#insn-00aacdac) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aacdbc`](#insn-00aacdbc) → `002b1e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacdbc`](#insn-00aacdbc) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdc0`](#insn-00aacdc0) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdc4`](#insn-00aacdc4) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdd0`](#insn-00aacdd0) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aacde0`](#insn-00aacde0) → `002a79de`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacde0`](#insn-00aacde0) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacde4`](#insn-00aacde4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacde8`](#insn-00aacde8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdec`](#insn-00aacdec) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdf8`](#insn-00aacdf8) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aace0c`](#insn-00aace0c) → `002a17b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aace0c`](#insn-00aace0c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace10`](#insn-00aace10) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aace1c`](#insn-00aace1c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aace2c`](#insn-00aace2c) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aace38`](#insn-00aace38) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace3c`](#insn-00aace3c) → `002afbeb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aace3c`](#insn-00aace3c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace40`](#insn-00aace40) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace4c`](#insn-00aace4c) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aace60`](#insn-00aace60) → `002a8d2a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aace60`](#insn-00aace60) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace64`](#insn-00aace64) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace68`](#insn-00aace68) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace6c`](#insn-00aace6c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace78`](#insn-00aace78) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aace8c`](#insn-00aace8c) → `002be375`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aace8c`](#insn-00aace8c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace90`](#insn-00aace90) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aace9c`](#insn-00aace9c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aaceac`](#insn-00aaceac) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aaceb8`](#insn-00aaceb8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacebc`](#insn-00aacebc) → `002beecd`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacebc`](#insn-00aacebc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacec0`](#insn-00aacec0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacecc`](#insn-00aacecc) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aaced8`](#insn-00aaced8) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacee4`](#insn-00aacee4) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacef0`](#insn-00aacef0) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacef4`](#insn-00aacef4) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacef8`](#insn-00aacef8) → [`00aacf04`](#insn-00aacf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacefc`](#insn-00aacefc) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf00`](#insn-00aacf00) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aacf04`](#insn-00aacf04) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aacf1c`](#insn-00aacf1c) → [`0087925c`](../00879/0087925c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087925c` · 推定シンボル `None` · 推定型 `None`
- [`00aacf28`](#insn-00aacf28) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf34`](#insn-00aacf34) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf40`](#insn-00aacf40) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf4c`](#insn-00aacf4c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf58`](#insn-00aacf58) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf68`](#insn-00aacf68) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacf6c`](#insn-00aacf6c) → [`00aad228`](#insn-00aad228) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf70`](#insn-00aacf70) → [`005e0d28`](../005e0/005e0d28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0d28` · 推定シンボル `None` · 推定型 `None`
- [`00aacf78`](#insn-00aacf78) → [`00aad238`](#insn-00aad238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf8c`](#insn-00aacf8c) → `002babe5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacf90`](#insn-00aacf90) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa4`](#insn-00aacfa4) → `Stack[-0x137]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa8`](#insn-00aacfa8) → `Stack[-0x147]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfac`](#insn-00aacfac) → `Stack[-0x133]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb0`](#insn-00aacfb0) → `002aeab4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacfb0`](#insn-00aacfb0) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb4`](#insn-00aacfb4) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb8`](#insn-00aacfb8) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfbc`](#insn-00aacfbc) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfc8`](#insn-00aacfc8) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aacfdc`](#insn-00aacfdc) → `002b7b47`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacfdc`](#insn-00aacfdc) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe0`](#insn-00aacfe0) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aacfec`](#insn-00aacfec) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad000`](#insn-00aad000) → [`00c57b50`](../00c57/00c57b50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b50` · 推定シンボル `None` · 推定型 `None`
- [`00aad00c`](#insn-00aad00c) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aad01c`](#insn-00aad01c) → `002b1e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad01c`](#insn-00aad01c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad020`](#insn-00aad020) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad024`](#insn-00aad024) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad030`](#insn-00aad030) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad040`](#insn-00aad040) → `002a79de`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad040`](#insn-00aad040) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad044`](#insn-00aad044) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad048`](#insn-00aad048) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad04c`](#insn-00aad04c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad058`](#insn-00aad058) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad06c`](#insn-00aad06c) → `002a17b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad06c`](#insn-00aad06c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad070`](#insn-00aad070) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aad07c`](#insn-00aad07c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad08c`](#insn-00aad08c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad09c`](#insn-00aad09c) → `Stack[-0x1bf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0a0`](#insn-00aad0a0) → `Stack[-0x1bb]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0b8`](#insn-00aad0b8) → [`004476b4`](../00447/004476b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004476b4` · 推定シンボル `None` · 推定型 `None`
- [`00aad0c4`](#insn-00aad0c4) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aad0d4`](#insn-00aad0d4) → `002afbeb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad0d4`](#insn-00aad0d4) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0d8`](#insn-00aad0d8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0dc`](#insn-00aad0dc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0e8`](#insn-00aad0e8) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad0f8`](#insn-00aad0f8) → `002a8d2a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad0f8`](#insn-00aad0f8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0fc`](#insn-00aad0fc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad100`](#insn-00aad100) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad104`](#insn-00aad104) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad110`](#insn-00aad110) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad124`](#insn-00aad124) → `002be375`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad124`](#insn-00aad124) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad128`](#insn-00aad128) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aad134`](#insn-00aad134) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad144`](#insn-00aad144) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aad150`](#insn-00aad150) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad154`](#insn-00aad154) → `002beecd`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad154`](#insn-00aad154) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad158`](#insn-00aad158) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad164`](#insn-00aad164) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad170`](#insn-00aad170) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad17c`](#insn-00aad17c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad180`](#insn-00aad180) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad184`](#insn-00aad184) → [`00aad190`](#insn-00aad190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad188`](#insn-00aad188) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad18c`](#insn-00aad18c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aad190`](#insn-00aad190) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad194`](#insn-00aad194) → [`00aad1a0`](#insn-00aad1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad198`](#insn-00aad198) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad19c`](#insn-00aad19c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aad1a8`](#insn-00aad1a8) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad1ac`](#insn-00aad1ac) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b0`](#insn-00aad1b0) → [`00aad1bc`](#insn-00aad1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b4`](#insn-00aad1b4) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b8`](#insn-00aad1b8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aad1bc`](#insn-00aad1bc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aad1d8`](#insn-00aad1d8) → [`0087925c`](../00879/0087925c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087925c` · 推定シンボル `None` · 推定型 `None`
- [`00aad1e4`](#insn-00aad1e4) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad1f0`](#insn-00aad1f0) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad1fc`](#insn-00aad1fc) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad208`](#insn-00aad208) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad214`](#insn-00aad214) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad224`](#insn-00aad224) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aad228`](#insn-00aad228) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad22c`](#insn-00aad22c) → [`00aad238`](#insn-00aad238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad230`](#insn-00aad230) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad234`](#insn-00aad234) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aad23c`](#insn-00aad23c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad244`](#insn-00aad244) → [`00aad494`](#insn-00aad494) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad24c`](#insn-00aad24c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad250`](#insn-00aad250) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad254`](#insn-00aad254) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad258`](#insn-00aad258) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad25c`](#insn-00aad25c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad494`](#insn-00aad494) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aacca8`](#insn-00aacca8)

~~~json
{
  "source": "00aacca8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccac`](#insn-00aaccac)

~~~json
{
  "source": "00aaccac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccb0`](#insn-00aaccb0)

~~~json
{
  "source": "00aaccb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccb4`](#insn-00aaccb4)

~~~json
{
  "source": "00aaccb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccb8`](#insn-00aaccb8)

~~~json
{
  "source": "00aaccb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccdc`](#insn-00aaccdc)

~~~json
{
  "source": "00aaccdc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacce0`](#insn-00aacce0)

~~~json
{
  "source": "00aacce0",
  "target": "00aacd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacce4`](#insn-00aacce4)

~~~json
{
  "source": "00aacce4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacce8`](#insn-00aacce8)

~~~json
{
  "source": "00aacce8",
  "target": "00853c30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaccf4`](#insn-00aaccf4)

~~~json
{
  "source": "00aaccf4",
  "target": "00aacf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaccfc`](#insn-00aaccfc)

~~~json
{
  "source": "00aaccfc",
  "target": "00aad238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd00`](#insn-00aacd00)

~~~json
{
  "source": "00aacd00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacd0c`](#insn-00aacd0c)

~~~json
{
  "source": "00aacd0c",
  "target": "00333f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f48",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4cb66c00dc8d0900",
  "capture_start": "00333f48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacd10`](#insn-00aacd10)

~~~json
{
  "source": "00aacd10",
  "target": "00aacf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd14`](#insn-00aacd14)

~~~json
{
  "source": "00aacd14",
  "target": "00aad238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd28`](#insn-00aacd28)

~~~json
{
  "source": "00aacd28",
  "target": "002babe5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002babe5",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "42634c6f6750757263686173655472696767657200",
  "capture_start": "002babe5",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacd34`](#insn-00aacd34)

~~~json
{
  "source": "00aacd34",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd44`](#insn-00aacd44)

~~~json
{
  "source": "00aacd44",
  "target": "Stack[-0x137]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd48`](#insn-00aacd48)

~~~json
{
  "source": "00aacd48",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd4c`](#insn-00aacd4c)

~~~json
{
  "source": "00aacd4c",
  "target": "Stack[-0x133]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd50`](#insn-00aacd50)

~~~json
{
  "source": "00aacd50",
  "target": "002aeab4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeab4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeab4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacd50`](#insn-00aacd50)

~~~json
{
  "source": "00aacd50",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd54`](#insn-00aacd54)

~~~json
{
  "source": "00aacd54",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd58`](#insn-00aacd58)

~~~json
{
  "source": "00aacd58",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd5c`](#insn-00aacd5c)

~~~json
{
  "source": "00aacd5c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd68`](#insn-00aacd68)

~~~json
{
  "source": "00aacd68",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacd7c`](#insn-00aacd7c)

~~~json
{
  "source": "00aacd7c",
  "target": "002b7b47",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7b47",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5472696767657200",
  "capture_start": "002b7b47",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacd7c`](#insn-00aacd7c)

~~~json
{
  "source": "00aacd7c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd80`](#insn-00aacd80)

~~~json
{
  "source": "00aacd80",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacd8c`](#insn-00aacd8c)

~~~json
{
  "source": "00aacd8c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacda0`](#insn-00aacda0)

~~~json
{
  "source": "00aacda0",
  "target": "00c57b50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdac`](#insn-00aacdac)

~~~json
{
  "source": "00aacdac",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdbc`](#insn-00aacdbc)

~~~json
{
  "source": "00aacdbc",
  "target": "002b1e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e08",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacdbc`](#insn-00aacdbc)

~~~json
{
  "source": "00aacdbc",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdc0`](#insn-00aacdc0)

~~~json
{
  "source": "00aacdc0",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdc4`](#insn-00aacdc4)

~~~json
{
  "source": "00aacdc4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdd0`](#insn-00aacdd0)

~~~json
{
  "source": "00aacdd0",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacde0`](#insn-00aacde0)

~~~json
{
  "source": "00aacde0",
  "target": "002a79de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a79de",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a79de",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacde0`](#insn-00aacde0)

~~~json
{
  "source": "00aacde0",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacde4`](#insn-00aacde4)

~~~json
{
  "source": "00aacde4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacde8`](#insn-00aacde8)

~~~json
{
  "source": "00aacde8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdec`](#insn-00aacdec)

~~~json
{
  "source": "00aacdec",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdf8`](#insn-00aacdf8)

~~~json
{
  "source": "00aacdf8",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace0c`](#insn-00aace0c)

~~~json
{
  "source": "00aace0c",
  "target": "002a17b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a17b0",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "53656c65637400",
  "capture_start": "002a17b0",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aace0c`](#insn-00aace0c)

~~~json
{
  "source": "00aace0c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace10`](#insn-00aace10)

~~~json
{
  "source": "00aace10",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace1c`](#insn-00aace1c)

~~~json
{
  "source": "00aace1c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace2c`](#insn-00aace2c)

~~~json
{
  "source": "00aace2c",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace38`](#insn-00aace38)

~~~json
{
  "source": "00aace38",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace3c`](#insn-00aace3c)

~~~json
{
  "source": "00aace3c",
  "target": "002afbeb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afbeb",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afbeb",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aace3c`](#insn-00aace3c)

~~~json
{
  "source": "00aace3c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace40`](#insn-00aace40)

~~~json
{
  "source": "00aace40",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace4c`](#insn-00aace4c)

~~~json
{
  "source": "00aace4c",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace60`](#insn-00aace60)

~~~json
{
  "source": "00aace60",
  "target": "002a8d2a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8d2a",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "65785f7479706500",
  "capture_start": "002a8d2a",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aace60`](#insn-00aace60)

~~~json
{
  "source": "00aace60",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace64`](#insn-00aace64)

~~~json
{
  "source": "00aace64",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace68`](#insn-00aace68)

~~~json
{
  "source": "00aace68",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace6c`](#insn-00aace6c)

~~~json
{
  "source": "00aace6c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace78`](#insn-00aace78)

~~~json
{
  "source": "00aace78",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace8c`](#insn-00aace8c)

~~~json
{
  "source": "00aace8c",
  "target": "002be375",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be375",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "436f6e74656e7400",
  "capture_start": "002be375",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aace8c`](#insn-00aace8c)

~~~json
{
  "source": "00aace8c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace90`](#insn-00aace90)

~~~json
{
  "source": "00aace90",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace9c`](#insn-00aace9c)

~~~json
{
  "source": "00aace9c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaceac`](#insn-00aaceac)

~~~json
{
  "source": "00aaceac",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaceb8`](#insn-00aaceb8)

~~~json
{
  "source": "00aaceb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacebc`](#insn-00aacebc)

~~~json
{
  "source": "00aacebc",
  "target": "002beecd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002beecd",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "65785f696400",
  "capture_start": "002beecd",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacebc`](#insn-00aacebc)

~~~json
{
  "source": "00aacebc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacec0`](#insn-00aacec0)

~~~json
{
  "source": "00aacec0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacecc`](#insn-00aacecc)

~~~json
{
  "source": "00aacecc",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaced8`](#insn-00aaced8)

~~~json
{
  "source": "00aaced8",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacee4`](#insn-00aacee4)

~~~json
{
  "source": "00aacee4",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacef0`](#insn-00aacef0)

~~~json
{
  "source": "00aacef0",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacef4`](#insn-00aacef4)

~~~json
{
  "source": "00aacef4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacef8`](#insn-00aacef8)

~~~json
{
  "source": "00aacef8",
  "target": "00aacf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacefc`](#insn-00aacefc)

~~~json
{
  "source": "00aacefc",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf00`](#insn-00aacf00)

~~~json
{
  "source": "00aacf00",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf04`](#insn-00aacf04)

~~~json
{
  "source": "00aacf04",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf1c`](#insn-00aacf1c)

~~~json
{
  "source": "00aacf1c",
  "target": "0087925c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf28`](#insn-00aacf28)

~~~json
{
  "source": "00aacf28",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf34`](#insn-00aacf34)

~~~json
{
  "source": "00aacf34",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf40`](#insn-00aacf40)

~~~json
{
  "source": "00aacf40",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf4c`](#insn-00aacf4c)

~~~json
{
  "source": "00aacf4c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf58`](#insn-00aacf58)

~~~json
{
  "source": "00aacf58",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf68`](#insn-00aacf68)

~~~json
{
  "source": "00aacf68",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf6c`](#insn-00aacf6c)

~~~json
{
  "source": "00aacf6c",
  "target": "00aad228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf70`](#insn-00aacf70)

~~~json
{
  "source": "00aacf70",
  "target": "005e0d28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf78`](#insn-00aacf78)

~~~json
{
  "source": "00aacf78",
  "target": "00aad238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf8c`](#insn-00aacf8c)

~~~json
{
  "source": "00aacf8c",
  "target": "002babe5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002babe5",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "42634c6f6750757263686173655472696767657200",
  "capture_start": "002babe5",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacf90`](#insn-00aacf90)

~~~json
{
  "source": "00aacf90",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfa4`](#insn-00aacfa4)

~~~json
{
  "source": "00aacfa4",
  "target": "Stack[-0x137]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfa8`](#insn-00aacfa8)

~~~json
{
  "source": "00aacfa8",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfac`](#insn-00aacfac)

~~~json
{
  "source": "00aacfac",
  "target": "Stack[-0x133]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb0`](#insn-00aacfb0)

~~~json
{
  "source": "00aacfb0",
  "target": "002aeab4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeab4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeab4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacfb0`](#insn-00aacfb0)

~~~json
{
  "source": "00aacfb0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb4`](#insn-00aacfb4)

~~~json
{
  "source": "00aacfb4",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb8`](#insn-00aacfb8)

~~~json
{
  "source": "00aacfb8",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfbc`](#insn-00aacfbc)

~~~json
{
  "source": "00aacfbc",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfc8`](#insn-00aacfc8)

~~~json
{
  "source": "00aacfc8",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfdc`](#insn-00aacfdc)

~~~json
{
  "source": "00aacfdc",
  "target": "002b7b47",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7b47",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5472696767657200",
  "capture_start": "002b7b47",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacfdc`](#insn-00aacfdc)

~~~json
{
  "source": "00aacfdc",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe0`](#insn-00aacfe0)

~~~json
{
  "source": "00aacfe0",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfec`](#insn-00aacfec)

~~~json
{
  "source": "00aacfec",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad000`](#insn-00aad000)

~~~json
{
  "source": "00aad000",
  "target": "00c57b50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad00c`](#insn-00aad00c)

~~~json
{
  "source": "00aad00c",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad01c`](#insn-00aad01c)

~~~json
{
  "source": "00aad01c",
  "target": "002b1e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e08",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad01c`](#insn-00aad01c)

~~~json
{
  "source": "00aad01c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad020`](#insn-00aad020)

~~~json
{
  "source": "00aad020",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad024`](#insn-00aad024)

~~~json
{
  "source": "00aad024",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad030`](#insn-00aad030)

~~~json
{
  "source": "00aad030",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad040`](#insn-00aad040)

~~~json
{
  "source": "00aad040",
  "target": "002a79de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a79de",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a79de",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad040`](#insn-00aad040)

~~~json
{
  "source": "00aad040",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad044`](#insn-00aad044)

~~~json
{
  "source": "00aad044",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad048`](#insn-00aad048)

~~~json
{
  "source": "00aad048",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad04c`](#insn-00aad04c)

~~~json
{
  "source": "00aad04c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad058`](#insn-00aad058)

~~~json
{
  "source": "00aad058",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad06c`](#insn-00aad06c)

~~~json
{
  "source": "00aad06c",
  "target": "002a17b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a17b0",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "53656c65637400",
  "capture_start": "002a17b0",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad06c`](#insn-00aad06c)

~~~json
{
  "source": "00aad06c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad070`](#insn-00aad070)

~~~json
{
  "source": "00aad070",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad07c`](#insn-00aad07c)

~~~json
{
  "source": "00aad07c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad08c`](#insn-00aad08c)

~~~json
{
  "source": "00aad08c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad09c`](#insn-00aad09c)

~~~json
{
  "source": "00aad09c",
  "target": "Stack[-0x1bf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0a0`](#insn-00aad0a0)

~~~json
{
  "source": "00aad0a0",
  "target": "Stack[-0x1bb]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0b8`](#insn-00aad0b8)

~~~json
{
  "source": "00aad0b8",
  "target": "004476b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0c4`](#insn-00aad0c4)

~~~json
{
  "source": "00aad0c4",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0d4`](#insn-00aad0d4)

~~~json
{
  "source": "00aad0d4",
  "target": "002afbeb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afbeb",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afbeb",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad0d4`](#insn-00aad0d4)

~~~json
{
  "source": "00aad0d4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0d8`](#insn-00aad0d8)

~~~json
{
  "source": "00aad0d8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0dc`](#insn-00aad0dc)

~~~json
{
  "source": "00aad0dc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0e8`](#insn-00aad0e8)

~~~json
{
  "source": "00aad0e8",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0f8`](#insn-00aad0f8)

~~~json
{
  "source": "00aad0f8",
  "target": "002a8d2a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8d2a",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "65785f7479706500",
  "capture_start": "002a8d2a",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad0f8`](#insn-00aad0f8)

~~~json
{
  "source": "00aad0f8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0fc`](#insn-00aad0fc)

~~~json
{
  "source": "00aad0fc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad100`](#insn-00aad100)

~~~json
{
  "source": "00aad100",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad104`](#insn-00aad104)

~~~json
{
  "source": "00aad104",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad110`](#insn-00aad110)

~~~json
{
  "source": "00aad110",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad124`](#insn-00aad124)

~~~json
{
  "source": "00aad124",
  "target": "002be375",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be375",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "436f6e74656e7400",
  "capture_start": "002be375",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad124`](#insn-00aad124)

~~~json
{
  "source": "00aad124",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad128`](#insn-00aad128)

~~~json
{
  "source": "00aad128",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad134`](#insn-00aad134)

~~~json
{
  "source": "00aad134",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad144`](#insn-00aad144)

~~~json
{
  "source": "00aad144",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad150`](#insn-00aad150)

~~~json
{
  "source": "00aad150",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad154`](#insn-00aad154)

~~~json
{
  "source": "00aad154",
  "target": "002beecd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002beecd",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "65785f696400",
  "capture_start": "002beecd",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad154`](#insn-00aad154)

~~~json
{
  "source": "00aad154",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad158`](#insn-00aad158)

~~~json
{
  "source": "00aad158",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad164`](#insn-00aad164)

~~~json
{
  "source": "00aad164",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad170`](#insn-00aad170)

~~~json
{
  "source": "00aad170",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad17c`](#insn-00aad17c)

~~~json
{
  "source": "00aad17c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad180`](#insn-00aad180)

~~~json
{
  "source": "00aad180",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad184`](#insn-00aad184)

~~~json
{
  "source": "00aad184",
  "target": "00aad190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad188`](#insn-00aad188)

~~~json
{
  "source": "00aad188",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad18c`](#insn-00aad18c)

~~~json
{
  "source": "00aad18c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad190`](#insn-00aad190)

~~~json
{
  "source": "00aad190",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad194`](#insn-00aad194)

~~~json
{
  "source": "00aad194",
  "target": "00aad1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad198`](#insn-00aad198)

~~~json
{
  "source": "00aad198",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad19c`](#insn-00aad19c)

~~~json
{
  "source": "00aad19c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1a8`](#insn-00aad1a8)

~~~json
{
  "source": "00aad1a8",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1ac`](#insn-00aad1ac)

~~~json
{
  "source": "00aad1ac",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b0`](#insn-00aad1b0)

~~~json
{
  "source": "00aad1b0",
  "target": "00aad1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b4`](#insn-00aad1b4)

~~~json
{
  "source": "00aad1b4",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b8`](#insn-00aad1b8)

~~~json
{
  "source": "00aad1b8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1bc`](#insn-00aad1bc)

~~~json
{
  "source": "00aad1bc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1d8`](#insn-00aad1d8)

~~~json
{
  "source": "00aad1d8",
  "target": "0087925c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1e4`](#insn-00aad1e4)

~~~json
{
  "source": "00aad1e4",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1f0`](#insn-00aad1f0)

~~~json
{
  "source": "00aad1f0",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1fc`](#insn-00aad1fc)

~~~json
{
  "source": "00aad1fc",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad208`](#insn-00aad208)

~~~json
{
  "source": "00aad208",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad214`](#insn-00aad214)

~~~json
{
  "source": "00aad214",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad224`](#insn-00aad224)

~~~json
{
  "source": "00aad224",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad228`](#insn-00aad228)

~~~json
{
  "source": "00aad228",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad22c`](#insn-00aad22c)

~~~json
{
  "source": "00aad22c",
  "target": "00aad238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad230`](#insn-00aad230)

~~~json
{
  "source": "00aad230",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad234`](#insn-00aad234)

~~~json
{
  "source": "00aad234",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad23c`](#insn-00aad23c)

~~~json
{
  "source": "00aad23c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad244`](#insn-00aad244)

~~~json
{
  "source": "00aad244",
  "target": "00aad494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad24c`](#insn-00aad24c)

~~~json
{
  "source": "00aad24c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad250`](#insn-00aad250)

~~~json
{
  "source": "00aad250",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad254`](#insn-00aad254)

~~~json
{
  "source": "00aad254",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad258`](#insn-00aad258)

~~~json
{
  "source": "00aad258",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad25c`](#insn-00aad25c)

~~~json
{
  "source": "00aad25c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad494`](#insn-00aad494)

~~~json
{
  "source": "00aad494",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
