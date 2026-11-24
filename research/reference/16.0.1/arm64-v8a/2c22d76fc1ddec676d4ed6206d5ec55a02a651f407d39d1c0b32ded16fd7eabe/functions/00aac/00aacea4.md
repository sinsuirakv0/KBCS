# 00aacea4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aacca8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aacca8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-e77ecb2e507432b400d78db60275444c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aacf14`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aac/00aacf14.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-ff517ae84e3dfd8c7c7f783a62f13392)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "7ddc0919fca516344ab66bac187517e0a3a2f3c5ce78fa78c29da855d9e34610",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aacea4",
        "00aad45f"
      ],
      [
        "00aad690",
        "00aad693"
      ]
    ],
    "bytes_sha256": "2d35ea97f55dde7dcb1c0541ac5405c98f00efcdb8150641b5d8bf145c1e2f07",
    "instruction_count": 368,
    "instruction_bytes": 1472,
    "body_bytes": 1472,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aacea4"></a> `00aacea4` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00aacea8"></a> `00aacea8` | `fc 67 01 a9` | stp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaceac"></a> `00aaceac` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaceb0"></a> `00aaceb0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaceb4"></a> `00aaceb4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaceb8"></a> `00aaceb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aacebc"></a> `00aacebc` | `ff 43 07 d1` | sub sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00aacec0"></a> `00aacec0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aacec4"></a> `00aacec4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00aacec8"></a> `00aacec8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aacecc"></a> `00aacecc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00aaced0"></a> `00aaced0` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aaced4"></a> `00aaced4` | `f9 63 03 91` | add x25,sp,#0xd8 | `FALL_THROUGH`
<a id="insn-00aaced8"></a> `00aaced8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aacedc"></a> `00aacedc` | `c8 01 00 54` | b.hi 0x00aacf14 | `CONDITIONAL_JUMP`
<a id="insn-00aacee0"></a> `00aacee0` | `86 91 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aacee4"></a> `00aacee4` | `63 9b f6 97` | bl 0x00853c70 | `UNCONDITIONAL_CALL`
<a id="insn-00aacee8"></a> `00aacee8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaceec"></a> `00aaceec` | `1f b0 04 71` | cmp w0,#0x12c | `FALL_THROUGH`
<a id="insn-00aacef0"></a> `00aacef0` | `e0 13 00 54` | b.eq 0x00aad16c | `CONDITIONAL_JUMP`
<a id="insn-00aacef4"></a> `00aacef4` | `bf 92 01 71` | cmp w21,#0x64 | `FALL_THROUGH`
<a id="insn-00aacef8"></a> `00aacef8` | `e1 29 00 54` | b.ne 0x00aad434 | `CONDITIONAL_JUMP`
<a id="insn-00aacefc"></a> `00aacefc` | `7f 91 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf00"></a> `00aacf00` | `88 e9 87 52` | mov w8,#0x3f4c | `FALL_THROUGH`
<a id="insn-00aacf04"></a> `00aacf04` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aacf08"></a> `00aacf08` | `17 68 68 b8` | ldr w23,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aacf0c"></a> `00aacf0c` | `77 13 f8 36` | tbz w23,#0x1f,0x00aad178 | `CONDITIONAL_JUMP`
<a id="insn-00aacf10"></a> `00aacf10` | `49 01 00 14` | b 0x00aad434 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacf14"></a> `00aacf14` | `69 c0 ff d0` | adrp x9,0x2ba000 | `FALL_THROUGH`
<a id="insn-00aacf18"></a> `00aacf18` | `29 95 30 91` | add x9,x9,#0xc25 | `FALL_THROUGH`
<a id="insn-00aacf1c"></a> `00aacf1c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aacf20"></a> `00aacf20` | `ea ec 8c 52` | mov w10,#0x6767 | `FALL_THROUGH`
<a id="insn-00aacf24"></a> `00aacf24` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacf28"></a> `00aacf28` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00aacf2c"></a> `00aacf2c` | `aa 4c ae 72` | movk w10,#0x7265, LSL #16 | `FALL_THROUGH`
<a id="insn-00aacf30"></a> `00aacf30` | `e8 63 03 39` | strb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aacf34"></a> `00aacf34` | `08 c0 ff d0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aacf38"></a> `00aacf38` | `08 d1 2b 91` | add x8,x8,#0xaf4 | `FALL_THROUGH`
<a id="insn-00aacf3c"></a> `00aacf3c` | `b4 23 03 d1` | sub x20,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacf40"></a> `00aacf40` | `2a 13 01 b8` | stur w10,[x25, #0x11] | `FALL_THROUGH`
<a id="insn-00aacf44"></a> `00aacf44` | `20 13 80 3c` | stur q0,[x25, #0x1] | `FALL_THROUGH`
<a id="insn-00aacf48"></a> `00aacf48` | `ff b7 03 39` | strb wzr,[sp, #0xed] | `FALL_THROUGH`
<a id="insn-00aacf4c"></a> `00aacf4c` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-00aacf50"></a> `00aacf50` | `bf 03 14 b8` | stur wzr,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-00aacf54"></a> `00aacf54` | `bf 83 14 f8` | stur xzr,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-00aacf58"></a> `00aacf58` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aacf5c"></a> `00aacf5c` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacf60"></a> `00aacf60` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aacf64"></a> `00aacf64` | `33 b6 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf68"></a> `00aacf68` | `48 c0 ff f0` | adrp x8,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aacf6c"></a> `00aacf6c` | `08 1d 2e 91` | add x8,x8,#0xb87 | `FALL_THROUGH`
<a id="insn-00aacf70"></a> `00aacf70` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aacf74"></a> `00aacf74` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacf78"></a> `00aacf78` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aacf7c"></a> `00aacf7c` | `31 b6 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf80"></a> `00aacf80` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacf84"></a> `00aacf84` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacf88"></a> `00aacf88` | `2a b6 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf8c"></a> `00aacf8c` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacf90"></a> `00aacf90` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacf94"></a> `00aacf94` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacf98"></a> `00aacf98` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aacf9c"></a> `00aacf9c` | `ed ab 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfa0"></a> `00aacfa0` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aacfa4"></a> `00aacfa4` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aacfa8"></a> `00aacfa8` | `b6 5c f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfac"></a> `00aacfac` | `28 c0 ff b0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aacfb0"></a> `00aacfb0` | `08 21 39 91` | add x8,x8,#0xe48 | `FALL_THROUGH`
<a id="insn-00aacfb4"></a> `00aacfb4` | `b6 23 03 d1` | sub x22,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aacfb8"></a> `00aacfb8` | `a8 83 15 f8` | stur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00aacfbc"></a> `00aacfbc` | `bf 03 16 b8` | stur wzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00aacfc0"></a> `00aacfc0` | `bf 83 16 f8` | stur xzr,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-00aacfc4"></a> `00aacfc4` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00aacfc8"></a> `00aacfc8` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aacfcc"></a> `00aacfcc` | `49 b6 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfd0"></a> `00aacfd0` | `c8 bf ff f0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aacfd4"></a> `00aacfd4` | `08 e9 2a 91` | add x8,x8,#0xaba | `FALL_THROUGH`
<a id="insn-00aacfd8"></a> `00aacfd8` | `d4 02 01 91` | add x20,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00aacfdc"></a> `00aacfdc` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-00aacfe0"></a> `00aacfe0` | `bf 03 18 b8` | stur wzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00aacfe4"></a> `00aacfe4` | `bf 83 18 f8` | stur xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00aacfe8"></a> `00aacfe8` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aacfec"></a> `00aacfec` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aacff0"></a> `00aacff0` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aacff4"></a> `00aacff4` | `0f b6 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aacff8"></a> `00aacff8` | `a8 bf ff b0` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-00aacffc"></a> `00aacffc` | `08 f5 21 91` | add x8,x8,#0x87d | `FALL_THROUGH`
<a id="insn-00aad000"></a> `00aad000` | `c0 22 01 91` | add x0,x22,#0x48 | `FALL_THROUGH`
<a id="insn-00aad004"></a> `00aad004` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad008"></a> `00aad008` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad00c"></a> `00aad00c` | `0d b6 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aad010"></a> `00aad010` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad014"></a> `00aad014` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad018"></a> `00aad018` | `06 b6 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad01c"></a> `00aad01c` | `d4 82 01 91` | add x20,x22,#0x60 | `FALL_THROUGH`
<a id="insn-00aad020"></a> `00aad020` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad024"></a> `00aad024` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aad028"></a> `00aad028` | `96 5c f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aad02c"></a> `00aad02c` | `08 c0 ff d0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aad030"></a> `00aad030` | `08 ad 30 91` | add x8,x8,#0xc2b | `FALL_THROUGH`
<a id="insn-00aad034"></a> `00aad034` | `bf 03 1a b8` | stur wzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00aad038"></a> `00aad038` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00aad03c"></a> `00aad03c` | `bf 83 1a f8` | stur xzr,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00aad040"></a> `00aad040` | `c0 a2 01 91` | add x0,x22,#0x68 | `FALL_THROUGH`
<a id="insn-00aad044"></a> `00aad044` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad048"></a> `00aad048` | `2a b6 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad04c"></a> `00aad04c` | `b5 23 03 d1` | sub x21,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad050"></a> `00aad050` | `c8 bf ff f0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aad054"></a> `00aad054` | `08 dd 37 91` | add x8,x8,#0xdf7 | `FALL_THROUGH`
<a id="insn-00aad058"></a> `00aad058` | `b4 02 02 91` | add x20,x21,#0x80 | `FALL_THROUGH`
<a id="insn-00aad05c"></a> `00aad05c` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00aad060"></a> `00aad060` | `bf 03 1c b8` | stur wzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aad064"></a> `00aad064` | `bf 83 1c f8` | stur xzr,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aad068"></a> `00aad068` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad06c"></a> `00aad06c` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad070"></a> `00aad070` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad074"></a> `00aad074` | `ef b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad078"></a> `00aad078` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad07c"></a> `00aad07c` | `08 d5 0e 91` | add x8,x8,#0x3b5 | `FALL_THROUGH`
<a id="insn-00aad080"></a> `00aad080` | `a0 22 02 91` | add x0,x21,#0x88 | `FALL_THROUGH`
<a id="insn-00aad084"></a> `00aad084` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad088"></a> `00aad088` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad08c"></a> `00aad08c` | `ed b5 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aad090"></a> `00aad090` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad094"></a> `00aad094` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad098"></a> `00aad098` | `e6 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad09c"></a> `00aad09c` | `b4 82 02 91` | add x20,x21,#0xa0 | `FALL_THROUGH`
<a id="insn-00aad0a0"></a> `00aad0a0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad0a4"></a> `00aad0a4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aad0a8"></a> `00aad0a8` | `76 5c f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0ac"></a> `00aad0ac` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad0b0"></a> `00aad0b0` | `08 35 3c 91` | add x8,x8,#0xf0d | `FALL_THROUGH`
<a id="insn-00aad0b4"></a> `00aad0b4` | `bf 03 1e b8` | stur wzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aad0b8"></a> `00aad0b8` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aad0bc"></a> `00aad0bc` | `bf 83 1e f8` | stur xzr,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aad0c0"></a> `00aad0c0` | `a0 a2 02 91` | add x0,x21,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad0c4"></a> `00aad0c4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aad0c8"></a> `00aad0c8` | `0a b6 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0cc"></a> `00aad0cc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad0d0"></a> `00aad0d0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad0d4"></a> `00aad0d4` | `d7 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0d8"></a> `00aad0d8` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad0dc"></a> `00aad0dc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad0e0"></a> `00aad0e0` | `d4 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0e4"></a> `00aad0e4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aad0e8"></a> `00aad0e8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad0ec"></a> `00aad0ec` | `d1 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad0f0"></a> `00aad0f0` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aad0f4"></a> `00aad0f4` | `68 00 00 36` | tbz w8,#0x0,0x00aad100 | `CONDITIONAL_JUMP`
<a id="insn-00aad0f8"></a> `00aad0f8` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00aad0fc"></a> `00aad0fc` | `6d ab 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad100"></a> `00aad100` | `fe 90 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aad104"></a> `00aad104` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aad108"></a> `00aad108` | `21 03 40 b2` | orr x1,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00aad10c"></a> `00aad10c` | `a2 23 03 d1` | sub x2,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad110"></a> `00aad110` | `c3 00 80 52` | mov w3,#0x6 | `FALL_THROUGH`
<a id="insn-00aad114"></a> `00aad114` | `b3 23 03 d1` | sub x19,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad118"></a> `00aad118` | `61 30 f7 97` | bl 0x0087929c | `UNCONDITIONAL_CALL`
<a id="insn-00aad11c"></a> `00aad11c` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad120"></a> `00aad120` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad124"></a> `00aad124` | `c3 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad128"></a> `00aad128` | `60 22 02 91` | add x0,x19,#0x88 | `FALL_THROUGH`
<a id="insn-00aad12c"></a> `00aad12c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad130"></a> `00aad130` | `c0 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad134"></a> `00aad134` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aad138"></a> `00aad138` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad13c"></a> `00aad13c` | `bd b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad140"></a> `00aad140` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aad144"></a> `00aad144` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad148"></a> `00aad148` | `ba b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad14c"></a> `00aad14c` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aad150"></a> `00aad150` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad154"></a> `00aad154` | `b7 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad158"></a> `00aad158` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad15c"></a> `00aad15c` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aad160"></a> `00aad160` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad164"></a> `00aad164` | `b3 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad168"></a> `00aad168` | `af 00 00 14` | b 0x00aad424 | `UNCONDITIONAL_JUMP`
<a id="insn-00aad16c"></a> `00aad16c` | `ff ce ec 97` | bl 0x005e0d68 | `UNCONDITIONAL_CALL`
<a id="insn-00aad170"></a> `00aad170` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aad174"></a> `00aad174` | `17 16 f8 37` | tbnz w23,#0x1f,0x00aad434 | `CONDITIONAL_JUMP`
<a id="insn-00aad178"></a> `00aad178` | `69 c0 ff b0` | adrp x9,0x2ba000 | `FALL_THROUGH`
<a id="insn-00aad17c"></a> `00aad17c` | `29 95 30 91` | add x9,x9,#0xc25 | `FALL_THROUGH`
<a id="insn-00aad180"></a> `00aad180` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aad184"></a> `00aad184` | `ea ec 8c 52` | mov w10,#0x6767 | `FALL_THROUGH`
<a id="insn-00aad188"></a> `00aad188` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aad18c"></a> `00aad18c` | `e8 63 03 39` | strb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aad190"></a> `00aad190` | `aa 4c ae 72` | movk w10,#0x7265, LSL #16 | `FALL_THROUGH`
<a id="insn-00aad194"></a> `00aad194` | `08 c0 ff b0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aad198"></a> `00aad198` | `08 d1 2b 91` | add x8,x8,#0xaf4 | `FALL_THROUGH`
<a id="insn-00aad19c"></a> `00aad19c` | `b4 23 03 d1` | sub x20,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad1a0"></a> `00aad1a0` | `2a 13 01 b8` | stur w10,[x25, #0x11] | `FALL_THROUGH`
<a id="insn-00aad1a4"></a> `00aad1a4` | `20 13 80 3c` | stur q0,[x25, #0x1] | `FALL_THROUGH`
<a id="insn-00aad1a8"></a> `00aad1a8` | `ff b7 03 39` | strb wzr,[sp, #0xed] | `FALL_THROUGH`
<a id="insn-00aad1ac"></a> `00aad1ac` | `a8 83 13 f8` | stur x8,[x29, #-0xc8] | `FALL_THROUGH`
<a id="insn-00aad1b0"></a> `00aad1b0` | `bf 03 14 b8` | stur wzr,[x29, #-0xc0] | `FALL_THROUGH`
<a id="insn-00aad1b4"></a> `00aad1b4` | `bf 83 14 f8` | stur xzr,[x29, #-0xb8] | `FALL_THROUGH`
<a id="insn-00aad1b8"></a> `00aad1b8` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad1bc"></a> `00aad1bc` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad1c0"></a> `00aad1c0` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad1c4"></a> `00aad1c4` | `9b b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1c8"></a> `00aad1c8` | `48 c0 ff d0` | adrp x8,0x2b7000 | `FALL_THROUGH`
<a id="insn-00aad1cc"></a> `00aad1cc` | `08 1d 2e 91` | add x8,x8,#0xb87 | `FALL_THROUGH`
<a id="insn-00aad1d0"></a> `00aad1d0` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aad1d4"></a> `00aad1d4` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad1d8"></a> `00aad1d8` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad1dc"></a> `00aad1dc` | `99 b5 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1e0"></a> `00aad1e0` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad1e4"></a> `00aad1e4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad1e8"></a> `00aad1e8` | `92 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad1ec"></a> `00aad1ec` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad1f0"></a> `00aad1f0` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aad1f4"></a> `00aad1f4` | `e8 a3 02 91` | add x8,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad1f8"></a> `00aad1f8` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aad1fc"></a> `00aad1fc` | `55 ab 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00aad200"></a> `00aad200` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad204"></a> `00aad204` | `e1 a3 02 91` | add x1,sp,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad208"></a> `00aad208` | `1e 5c f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aad20c"></a> `00aad20c` | `28 c0 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aad210"></a> `00aad210` | `08 21 39 91` | add x8,x8,#0xe48 | `FALL_THROUGH`
<a id="insn-00aad214"></a> `00aad214` | `b6 23 03 d1` | sub x22,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad218"></a> `00aad218` | `a8 83 15 f8` | stur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-00aad21c"></a> `00aad21c` | `bf 03 16 b8` | stur wzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00aad220"></a> `00aad220` | `bf 83 16 f8` | stur xzr,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-00aad224"></a> `00aad224` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00aad228"></a> `00aad228` | `e1 03 03 91` | add x1,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad22c"></a> `00aad22c` | `b1 b5 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad230"></a> `00aad230` | `c8 bf ff d0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aad234"></a> `00aad234` | `08 e9 2a 91` | add x8,x8,#0xaba | `FALL_THROUGH`
<a id="insn-00aad238"></a> `00aad238` | `d4 02 01 91` | add x20,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00aad23c"></a> `00aad23c` | `a8 83 17 f8` | stur x8,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-00aad240"></a> `00aad240` | `bf 03 18 b8` | stur wzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00aad244"></a> `00aad244` | `bf 83 18 f8` | stur xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00aad248"></a> `00aad248` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad24c"></a> `00aad24c` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad250"></a> `00aad250` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad254"></a> `00aad254` | `77 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad258"></a> `00aad258` | `a8 bf ff 90` | adrp x8,0x2a1000 | `FALL_THROUGH`
<a id="insn-00aad25c"></a> `00aad25c` | `08 f5 21 91` | add x8,x8,#0x87d | `FALL_THROUGH`
<a id="insn-00aad260"></a> `00aad260` | `c0 22 01 91` | add x0,x22,#0x48 | `FALL_THROUGH`
<a id="insn-00aad264"></a> `00aad264` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad268"></a> `00aad268` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad26c"></a> `00aad26c` | `75 b5 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aad270"></a> `00aad270` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad274"></a> `00aad274` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad278"></a> `00aad278` | `6e b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad27c"></a> `00aad27c` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00aad280"></a> `00aad280` | `a9 84 8c 52` | mov w9,#0x6425 | `FALL_THROUGH`
<a id="insn-00aad284"></a> `00aad284` | `8a 0c 80 52` | mov w10,#0x64 | `FALL_THROUGH`
<a id="insn-00aad288"></a> `00aad288` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aad28c"></a> `00aad28c` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad290"></a> `00aad290` | `a9 a5 a4 72` | movk w9,#0x252d, LSL #16 | `FALL_THROUGH`
<a id="insn-00aad294"></a> `00aad294` | `14 81 01 91` | add x20,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aad298"></a> `00aad298` | `e9 13 06 b8` | stur w9,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-00aad29c"></a> `00aad29c` | `ea 53 06 78` | sturh w10,[sp, #0x65] | `FALL_THROUGH`
<a id="insn-00aad2a0"></a> `00aad2a0` | `e8 e3 01 91` | add x8,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00aad2a4"></a> `00aad2a4` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aad2a8"></a> `00aad2a8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aad2ac"></a> `00aad2ac` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aad2b0"></a> `00aad2b0` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-00aad2b4"></a> `00aad2b4` | `10 69 e6 97` | bl 0x004476f4 | `UNCONDITIONAL_CALL`
<a id="insn-00aad2b8"></a> `00aad2b8` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad2bc"></a> `00aad2bc` | `e1 e3 01 91` | add x1,sp,#0x78 | `FALL_THROUGH`
<a id="insn-00aad2c0"></a> `00aad2c0` | `f0 5b f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aad2c4"></a> `00aad2c4` | `08 c0 ff d0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aad2c8"></a> `00aad2c8` | `08 ad 30 91` | add x8,x8,#0xc2b | `FALL_THROUGH`
<a id="insn-00aad2cc"></a> `00aad2cc` | `b5 23 03 d1` | sub x21,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad2d0"></a> `00aad2d0` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00aad2d4"></a> `00aad2d4` | `bf 03 1a b8` | stur wzr,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00aad2d8"></a> `00aad2d8` | `bf 83 1a f8` | stur xzr,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00aad2dc"></a> `00aad2dc` | `a0 a2 01 91` | add x0,x21,#0x68 | `FALL_THROUGH`
<a id="insn-00aad2e0"></a> `00aad2e0` | `e1 43 02 91` | add x1,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad2e4"></a> `00aad2e4` | `83 b5 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad2e8"></a> `00aad2e8` | `c8 bf ff f0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aad2ec"></a> `00aad2ec` | `08 dd 37 91` | add x8,x8,#0xdf7 | `FALL_THROUGH`
<a id="insn-00aad2f0"></a> `00aad2f0` | `b4 02 02 91` | add x20,x21,#0x80 | `FALL_THROUGH`
<a id="insn-00aad2f4"></a> `00aad2f4` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00aad2f8"></a> `00aad2f8` | `bf 03 1c b8` | stur wzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aad2fc"></a> `00aad2fc` | `bf 83 1c f8` | stur xzr,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aad300"></a> `00aad300` | `bf 03 12 b8` | stur wzr,[x29, #-0xe0] | `FALL_THROUGH`
<a id="insn-00aad304"></a> `00aad304` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad308"></a> `00aad308` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad30c"></a> `00aad30c` | `49 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad310"></a> `00aad310` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad314"></a> `00aad314` | `08 d5 0e 91` | add x8,x8,#0x3b5 | `FALL_THROUGH`
<a id="insn-00aad318"></a> `00aad318` | `a0 22 02 91` | add x0,x21,#0x88 | `FALL_THROUGH`
<a id="insn-00aad31c"></a> `00aad31c` | `a1 83 03 d1` | sub x1,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad320"></a> `00aad320` | `a8 83 12 f8` | stur x8,[x29, #-0xd8] | `FALL_THROUGH`
<a id="insn-00aad324"></a> `00aad324` | `47 b5 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aad328"></a> `00aad328` | `a0 83 03 d1` | sub x0,x29,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad32c"></a> `00aad32c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad330"></a> `00aad330` | `40 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad334"></a> `00aad334` | `b4 82 02 91` | add x20,x21,#0xa0 | `FALL_THROUGH`
<a id="insn-00aad338"></a> `00aad338` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad33c"></a> `00aad33c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00aad340"></a> `00aad340` | `d0 5b f3 97` | bl 0x00784280 | `UNCONDITIONAL_CALL`
<a id="insn-00aad344"></a> `00aad344` | `88 c0 ff b0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-00aad348"></a> `00aad348` | `08 35 3c 91` | add x8,x8,#0xf0d | `FALL_THROUGH`
<a id="insn-00aad34c"></a> `00aad34c` | `bf 03 1e b8` | stur wzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aad350"></a> `00aad350` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aad354"></a> `00aad354` | `bf 83 1e f8` | stur xzr,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aad358"></a> `00aad358` | `a0 a2 02 91` | add x0,x21,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad35c"></a> `00aad35c` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad360"></a> `00aad360` | `64 b5 06 94` | bl 0x00c5a8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad364"></a> `00aad364` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aad368"></a> `00aad368` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad36c"></a> `00aad36c` | `31 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad370"></a> `00aad370` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aad374"></a> `00aad374` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad378"></a> `00aad378` | `2e b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad37c"></a> `00aad37c` | `e8 e3 41 39` | ldrb w8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aad380"></a> `00aad380` | `68 00 00 36` | tbz w8,#0x0,0x00aad38c | `CONDITIONAL_JUMP`
<a id="insn-00aad384"></a> `00aad384` | `e0 47 40 f9` | ldr x0,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aad388"></a> `00aad388` | `ca aa 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad38c"></a> `00aad38c` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aad390"></a> `00aad390` | `68 00 00 36` | tbz w8,#0x0,0x00aad39c | `CONDITIONAL_JUMP`
<a id="insn-00aad394"></a> `00aad394` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aad398"></a> `00aad398` | `c6 aa 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad39c"></a> `00aad39c` | `e0 03 03 91` | add x0,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aad3a0"></a> `00aad3a0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad3a4"></a> `00aad3a4` | `23 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3a8"></a> `00aad3a8` | `e8 a3 42 39` | ldrb w8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aad3ac"></a> `00aad3ac` | `68 00 00 36` | tbz w8,#0x0,0x00aad3b8 | `CONDITIONAL_JUMP`
<a id="insn-00aad3b0"></a> `00aad3b0` | `e0 5f 40 f9` | ldr x0,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00aad3b4"></a> `00aad3b4` | `bf aa 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3b8"></a> `00aad3b8` | `50 90 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3bc"></a> `00aad3bc` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aad3c0"></a> `00aad3c0` | `e8 63 03 91` | add x8,sp,#0xd8 | `FALL_THROUGH`
<a id="insn-00aad3c4"></a> `00aad3c4` | `01 01 40 b2` | orr x1,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aad3c8"></a> `00aad3c8` | `a2 23 03 d1` | sub x2,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad3cc"></a> `00aad3cc` | `c3 00 80 52` | mov w3,#0x6 | `FALL_THROUGH`
<a id="insn-00aad3d0"></a> `00aad3d0` | `b3 23 03 d1` | sub x19,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad3d4"></a> `00aad3d4` | `b2 2f f7 97` | bl 0x0087929c | `UNCONDITIONAL_CALL`
<a id="insn-00aad3d8"></a> `00aad3d8` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00aad3dc"></a> `00aad3dc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad3e0"></a> `00aad3e0` | `14 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3e4"></a> `00aad3e4` | `60 22 02 91` | add x0,x19,#0x88 | `FALL_THROUGH`
<a id="insn-00aad3e8"></a> `00aad3e8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad3ec"></a> `00aad3ec` | `11 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3f0"></a> `00aad3f0` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aad3f4"></a> `00aad3f4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad3f8"></a> `00aad3f8` | `0e b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3fc"></a> `00aad3fc` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aad400"></a> `00aad400` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad404"></a> `00aad404` | `0b b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad408"></a> `00aad408` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aad40c"></a> `00aad40c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad410"></a> `00aad410` | `08 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad414"></a> `00aad414` | `a8 23 03 d1` | sub x8,x29,#0xc8 | `FALL_THROUGH`
<a id="insn-00aad418"></a> `00aad418` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aad41c"></a> `00aad41c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad420"></a> `00aad420` | `04 b5 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aad424"></a> `00aad424` | `e8 63 43 39` | ldrb w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aad428"></a> `00aad428` | `68 00 00 36` | tbz w8,#0x0,0x00aad434 | `CONDITIONAL_JUMP`
<a id="insn-00aad42c"></a> `00aad42c` | `e0 77 40 f9` | ldr x0,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00aad430"></a> `00aad430` | `a0 aa 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad434"></a> `00aad434` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00aad438"></a> `00aad438` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aad43c"></a> `00aad43c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aad440"></a> `00aad440` | `81 12 00 54` | b.ne 0x00aad690 | `CONDITIONAL_JUMP`
<a id="insn-00aad444"></a> `00aad444` | `ff 43 07 91` | add sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00aad448"></a> `00aad448` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aad44c"></a> `00aad44c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aad450"></a> `00aad450` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aad454"></a> `00aad454` | `fc 67 41 a9` | ldp x28,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aad458"></a> `00aad458` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00aad45c"></a> `00aad45c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aad690"></a> `00aad690` | `14 aa 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aacea4`](#insn-00aacea4) 範囲 `[['00aacea4', '00aacea7']]`
  - `FALL_THROUGH` [`00aacea4`](#insn-00aacea4) → [`00aacea8`](#insn-00aacea8)
- ブロック [`00aacea8`](#insn-00aacea8) 範囲 `[['00aacea8', '00aaceaf']]`
  - `FALL_THROUGH` [`00aaceac`](#insn-00aaceac) → [`00aaceb0`](#insn-00aaceb0)
- ブロック [`00aaceb0`](#insn-00aaceb0) 範囲 `[['00aaceb0', '00aacec7']]`
  - `FALL_THROUGH` [`00aacec4`](#insn-00aacec4) → [`00aacec8`](#insn-00aacec8)
- ブロック [`00aacec8`](#insn-00aacec8) 範囲 `[['00aacec8', '00aacedf']]`
  - `CONDITIONAL_JUMP` [`00aacedc`](#insn-00aacedc) → [`00aacf14`](#insn-00aacf14)
  - `FALL_THROUGH` [`00aacedc`](#insn-00aacedc) → [`00aacee0`](#insn-00aacee0)
- ブロック [`00aacee0`](#insn-00aacee0) 範囲 `[['00aacee0', '00aacef3']]`
  - `CONDITIONAL_JUMP` [`00aacef0`](#insn-00aacef0) → [`00aad16c`](#insn-00aad16c)
  - `FALL_THROUGH` [`00aacef0`](#insn-00aacef0) → [`00aacef4`](#insn-00aacef4)
- ブロック [`00aacef4`](#insn-00aacef4) 範囲 `[['00aacef4', '00aacefb']]`
  - `CONDITIONAL_JUMP` [`00aacef8`](#insn-00aacef8) → [`00aad434`](#insn-00aad434)
  - `FALL_THROUGH` [`00aacef8`](#insn-00aacef8) → [`00aacefc`](#insn-00aacefc)
- ブロック [`00aacefc`](#insn-00aacefc) 範囲 `[['00aacefc', '00aacf0f']]`
  - `CONDITIONAL_JUMP` [`00aacf0c`](#insn-00aacf0c) → [`00aad178`](#insn-00aad178)
  - `FALL_THROUGH` [`00aacf0c`](#insn-00aacf0c) → [`00aacf10`](#insn-00aacf10)
- ブロック [`00aacf10`](#insn-00aacf10) 範囲 `[['00aacf10', '00aacf13']]`
  - `UNCONDITIONAL_JUMP` [`00aacf10`](#insn-00aacf10) → [`00aad434`](#insn-00aad434)
- ブロック [`00aacf14`](#insn-00aacf14) 範囲 `[['00aacf14', '00aacf67']]`
  - `FALL_THROUGH` [`00aacf64`](#insn-00aacf64) → [`00aacf68`](#insn-00aacf68)
- ブロック [`00aacf68`](#insn-00aacf68) 範囲 `[['00aacf68', '00aacff3']]`
  - `FALL_THROUGH` [`00aacff0`](#insn-00aacff0) → [`00aacff4`](#insn-00aacff4)
- ブロック [`00aacff4`](#insn-00aacff4) 範囲 `[['00aacff4', '00aad00f']]`
  - `FALL_THROUGH` [`00aad00c`](#insn-00aad00c) → [`00aad010`](#insn-00aad010)
- ブロック [`00aad010`](#insn-00aad010) 範囲 `[['00aad010', '00aad01b']]`
  - `FALL_THROUGH` [`00aad018`](#insn-00aad018) → [`00aad01c`](#insn-00aad01c)
- ブロック [`00aad01c`](#insn-00aad01c) 範囲 `[['00aad01c', '00aad023']]`
  - `FALL_THROUGH` [`00aad020`](#insn-00aad020) → [`00aad024`](#insn-00aad024)
- ブロック [`00aad024`](#insn-00aad024) 範囲 `[['00aad024', '00aad02f']]`
  - `FALL_THROUGH` [`00aad02c`](#insn-00aad02c) → [`00aad030`](#insn-00aad030)
- ブロック [`00aad030`](#insn-00aad030) 範囲 `[['00aad030', '00aad0bf']]`
  - `FALL_THROUGH` [`00aad0bc`](#insn-00aad0bc) → [`00aad0c0`](#insn-00aad0c0)
- ブロック [`00aad0c0`](#insn-00aad0c0) 範囲 `[['00aad0c0', '00aad0c3']]`
  - `FALL_THROUGH` [`00aad0c0`](#insn-00aad0c0) → [`00aad0c4`](#insn-00aad0c4)
- ブロック [`00aad0c4`](#insn-00aad0c4) 範囲 `[['00aad0c4', '00aad0f7']]`
  - `CONDITIONAL_JUMP` [`00aad0f4`](#insn-00aad0f4) → [`00aad100`](#insn-00aad100)
  - `FALL_THROUGH` [`00aad0f4`](#insn-00aad0f4) → [`00aad0f8`](#insn-00aad0f8)
- ブロック [`00aad0f8`](#insn-00aad0f8) 範囲 `[['00aad0f8', '00aad0ff']]`
  - `FALL_THROUGH` [`00aad0fc`](#insn-00aad0fc) → [`00aad100`](#insn-00aad100)
- ブロック [`00aad100`](#insn-00aad100) 範囲 `[['00aad100', '00aad163']]`
  - `FALL_THROUGH` [`00aad160`](#insn-00aad160) → [`00aad164`](#insn-00aad164)
- ブロック [`00aad164`](#insn-00aad164) 範囲 `[['00aad164', '00aad16b']]`
  - `UNCONDITIONAL_JUMP` [`00aad168`](#insn-00aad168) → [`00aad424`](#insn-00aad424)
- ブロック [`00aad16c`](#insn-00aad16c) 範囲 `[['00aad16c', '00aad177']]`
  - `CONDITIONAL_JUMP` [`00aad174`](#insn-00aad174) → [`00aad434`](#insn-00aad434)
  - `FALL_THROUGH` [`00aad174`](#insn-00aad174) → [`00aad178`](#insn-00aad178)
- ブロック [`00aad178`](#insn-00aad178) 範囲 `[['00aad178', '00aad27b']]`
  - `FALL_THROUGH` [`00aad278`](#insn-00aad278) → [`00aad27c`](#insn-00aad27c)
- ブロック [`00aad27c`](#insn-00aad27c) 範囲 `[['00aad27c', '00aad29f']]`
  - `FALL_THROUGH` [`00aad29c`](#insn-00aad29c) → [`00aad2a0`](#insn-00aad2a0)
- ブロック [`00aad2a0`](#insn-00aad2a0) 範囲 `[['00aad2a0', '00aad30b']]`
  - `FALL_THROUGH` [`00aad308`](#insn-00aad308) → [`00aad30c`](#insn-00aad30c)
- ブロック [`00aad30c`](#insn-00aad30c) 範囲 `[['00aad30c', '00aad317']]`
  - `FALL_THROUGH` [`00aad314`](#insn-00aad314) → [`00aad318`](#insn-00aad318)
- ブロック [`00aad318`](#insn-00aad318) 範囲 `[['00aad318', '00aad383']]`
  - `CONDITIONAL_JUMP` [`00aad380`](#insn-00aad380) → [`00aad38c`](#insn-00aad38c)
  - `FALL_THROUGH` [`00aad380`](#insn-00aad380) → [`00aad384`](#insn-00aad384)
- ブロック [`00aad384`](#insn-00aad384) 範囲 `[['00aad384', '00aad38b']]`
  - `FALL_THROUGH` [`00aad388`](#insn-00aad388) → [`00aad38c`](#insn-00aad38c)
- ブロック [`00aad38c`](#insn-00aad38c) 範囲 `[['00aad38c', '00aad393']]`
  - `CONDITIONAL_JUMP` [`00aad390`](#insn-00aad390) → [`00aad39c`](#insn-00aad39c)
  - `FALL_THROUGH` [`00aad390`](#insn-00aad390) → [`00aad394`](#insn-00aad394)
- ブロック [`00aad394`](#insn-00aad394) 範囲 `[['00aad394', '00aad39b']]`
  - `FALL_THROUGH` [`00aad398`](#insn-00aad398) → [`00aad39c`](#insn-00aad39c)
- ブロック [`00aad39c`](#insn-00aad39c) 範囲 `[['00aad39c', '00aad3af']]`
  - `CONDITIONAL_JUMP` [`00aad3ac`](#insn-00aad3ac) → [`00aad3b8`](#insn-00aad3b8)
  - `FALL_THROUGH` [`00aad3ac`](#insn-00aad3ac) → [`00aad3b0`](#insn-00aad3b0)
- ブロック [`00aad3b0`](#insn-00aad3b0) 範囲 `[['00aad3b0', '00aad3b7']]`
  - `FALL_THROUGH` [`00aad3b4`](#insn-00aad3b4) → [`00aad3b8`](#insn-00aad3b8)
- ブロック [`00aad3b8`](#insn-00aad3b8) 範囲 `[['00aad3b8', '00aad3ef']]`
  - `FALL_THROUGH` [`00aad3ec`](#insn-00aad3ec) → [`00aad3f0`](#insn-00aad3f0)
- ブロック [`00aad3f0`](#insn-00aad3f0) 範囲 `[['00aad3f0', '00aad423']]`
  - `FALL_THROUGH` [`00aad420`](#insn-00aad420) → [`00aad424`](#insn-00aad424)
- ブロック [`00aad424`](#insn-00aad424) 範囲 `[['00aad424', '00aad42b']]`
  - `CONDITIONAL_JUMP` [`00aad428`](#insn-00aad428) → [`00aad434`](#insn-00aad434)
  - `FALL_THROUGH` [`00aad428`](#insn-00aad428) → [`00aad42c`](#insn-00aad42c)
- ブロック [`00aad42c`](#insn-00aad42c) 範囲 `[['00aad42c', '00aad433']]`
  - `FALL_THROUGH` [`00aad430`](#insn-00aad430) → [`00aad434`](#insn-00aad434)
- ブロック [`00aad434`](#insn-00aad434) 範囲 `[['00aad434', '00aad43b']]`
  - `FALL_THROUGH` [`00aad438`](#insn-00aad438) → [`00aad43c`](#insn-00aad43c)
- ブロック [`00aad43c`](#insn-00aad43c) 範囲 `[['00aad43c', '00aad43f']]`
  - `FALL_THROUGH` [`00aad43c`](#insn-00aad43c) → [`00aad440`](#insn-00aad440)
- ブロック [`00aad440`](#insn-00aad440) 範囲 `[['00aad440', '00aad443']]`
  - `CONDITIONAL_JUMP` [`00aad440`](#insn-00aad440) → [`00aad690`](#insn-00aad690)
  - `FALL_THROUGH` [`00aad440`](#insn-00aad440) → [`00aad444`](#insn-00aad444)
- ブロック [`00aad444`](#insn-00aad444) 範囲 `[['00aad444', '00aad447']]`
  - `FALL_THROUGH` [`00aad444`](#insn-00aad444) → [`00aad448`](#insn-00aad448)
- ブロック [`00aad448`](#insn-00aad448) 範囲 `[['00aad448', '00aad44b']]`
  - `FALL_THROUGH` [`00aad448`](#insn-00aad448) → [`00aad44c`](#insn-00aad44c)
- ブロック [`00aad44c`](#insn-00aad44c) 範囲 `[['00aad44c', '00aad44f']]`
  - `FALL_THROUGH` [`00aad44c`](#insn-00aad44c) → [`00aad450`](#insn-00aad450)
- ブロック [`00aad450`](#insn-00aad450) 範囲 `[['00aad450', '00aad45f']]`
- ブロック [`00aad690`](#insn-00aad690) 範囲 `[['00aad690', '00aad693']]`

## 命令位置別の参照

- [`00aacea4`](#insn-00aacea4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacea8`](#insn-00aacea8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaceac`](#insn-00aaceac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaceb0`](#insn-00aaceb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaceb4`](#insn-00aaceb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaced8`](#insn-00aaced8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacedc`](#insn-00aacedc) → [`00aacf14`](#insn-00aacf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacee0`](#insn-00aacee0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aacee4`](#insn-00aacee4) → [`00853c70`](../00853/00853c70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00853c70` · 推定シンボル `None` · 推定型 `None`
- [`00aacef0`](#insn-00aacef0) → [`00aad16c`](#insn-00aad16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacef8`](#insn-00aacef8) → [`00aad434`](#insn-00aad434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacefc`](#insn-00aacefc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aacf08`](#insn-00aacf08) → `00333f4c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aacf0c`](#insn-00aacf0c) → [`00aad178`](#insn-00aad178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf10`](#insn-00aacf10) → [`00aad434`](#insn-00aad434) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf24`](#insn-00aacf24) → `002bac25`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacf30`](#insn-00aacf30) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf40`](#insn-00aacf40) → `Stack[-0x137]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf44`](#insn-00aacf44) → `Stack[-0x147]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf48`](#insn-00aacf48) → `Stack[-0x133]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf4c`](#insn-00aacf4c) → `002aeaf4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacf4c`](#insn-00aacf4c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf50`](#insn-00aacf50) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf54`](#insn-00aacf54) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf58`](#insn-00aacf58) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf64`](#insn-00aacf64) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aacf78`](#insn-00aacf78) → `002b7b87`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacf78`](#insn-00aacf78) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf7c`](#insn-00aacf7c) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aacf88`](#insn-00aacf88) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aacf9c`](#insn-00aacf9c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa8`](#insn-00aacfa8) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb8`](#insn-00aacfb8) → `002b1e48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacfb8`](#insn-00aacfb8) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfbc`](#insn-00aacfbc) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfc0`](#insn-00aacfc0) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfcc`](#insn-00aacfcc) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aacfdc`](#insn-00aacfdc) → `002a7aba`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacfdc`](#insn-00aacfdc) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe0`](#insn-00aacfe0) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe4`](#insn-00aacfe4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe8`](#insn-00aacfe8) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacff4`](#insn-00aacff4) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad008`](#insn-00aad008) → `002a187d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad008`](#insn-00aad008) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad00c`](#insn-00aad00c) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aad018`](#insn-00aad018) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad028`](#insn-00aad028) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aad034`](#insn-00aad034) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad038`](#insn-00aad038) → `002afc2b`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad038`](#insn-00aad038) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad03c`](#insn-00aad03c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad048`](#insn-00aad048) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad05c`](#insn-00aad05c) → `002a8df7`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad05c`](#insn-00aad05c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad060`](#insn-00aad060) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad064`](#insn-00aad064) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad068`](#insn-00aad068) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad074`](#insn-00aad074) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad088`](#insn-00aad088) → `002be3b5`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad088`](#insn-00aad088) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad08c`](#insn-00aad08c) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aad098`](#insn-00aad098) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad0a8`](#insn-00aad0a8) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aad0b4`](#insn-00aad0b4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0b8`](#insn-00aad0b8) → `002bef0d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad0b8`](#insn-00aad0b8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0bc`](#insn-00aad0bc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0c8`](#insn-00aad0c8) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad0d4`](#insn-00aad0d4) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad0e0`](#insn-00aad0e0) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad0ec`](#insn-00aad0ec) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad0f0`](#insn-00aad0f0) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0f4`](#insn-00aad0f4) → [`00aad100`](#insn-00aad100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0f8`](#insn-00aad0f8) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad0fc`](#insn-00aad0fc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aad100`](#insn-00aad100) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aad118`](#insn-00aad118) → [`0087929c`](../00879/0087929c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087929c` · 推定シンボル `None` · 推定型 `None`
- [`00aad124`](#insn-00aad124) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad130`](#insn-00aad130) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad13c`](#insn-00aad13c) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad148`](#insn-00aad148) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad154`](#insn-00aad154) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad164`](#insn-00aad164) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad168`](#insn-00aad168) → [`00aad424`](#insn-00aad424) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad16c`](#insn-00aad16c) → [`005e0d68`](../005e0/005e0d68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0d68` · 推定シンボル `None` · 推定型 `None`
- [`00aad174`](#insn-00aad174) → [`00aad434`](#insn-00aad434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad188`](#insn-00aad188) → `002bac25`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad18c`](#insn-00aad18c) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1a0`](#insn-00aad1a0) → `Stack[-0x137]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1a4`](#insn-00aad1a4) → `Stack[-0x147]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1a8`](#insn-00aad1a8) → `Stack[-0x133]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1ac`](#insn-00aad1ac) → `002aeaf4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad1ac`](#insn-00aad1ac) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b0`](#insn-00aad1b0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b4`](#insn-00aad1b4) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1b8`](#insn-00aad1b8) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1c4`](#insn-00aad1c4) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad1d8`](#insn-00aad1d8) → `002b7b87`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad1d8`](#insn-00aad1d8) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad1dc`](#insn-00aad1dc) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aad1e8`](#insn-00aad1e8) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad1fc`](#insn-00aad1fc) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00aad208`](#insn-00aad208) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aad218`](#insn-00aad218) → `002b1e48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad218`](#insn-00aad218) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad21c`](#insn-00aad21c) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad220`](#insn-00aad220) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad22c`](#insn-00aad22c) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad23c`](#insn-00aad23c) → `002a7aba`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad23c`](#insn-00aad23c) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad240`](#insn-00aad240) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad244`](#insn-00aad244) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad248`](#insn-00aad248) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad254`](#insn-00aad254) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad268`](#insn-00aad268) → `002a187d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad268`](#insn-00aad268) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad26c`](#insn-00aad26c) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aad278`](#insn-00aad278) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad288`](#insn-00aad288) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad298`](#insn-00aad298) → `Stack[-0x1bf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad29c`](#insn-00aad29c) → `Stack[-0x1bb]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2b4`](#insn-00aad2b4) → [`004476f4`](../00447/004476f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004476f4` · 推定シンボル `None` · 推定型 `None`
- [`00aad2c0`](#insn-00aad2c0) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aad2d0`](#insn-00aad2d0) → `002afc2b`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad2d0`](#insn-00aad2d0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2d4`](#insn-00aad2d4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2d8`](#insn-00aad2d8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2e4`](#insn-00aad2e4) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad2f4`](#insn-00aad2f4) → `002a8df7`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad2f4`](#insn-00aad2f4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2f8`](#insn-00aad2f8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2fc`](#insn-00aad2fc) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad300`](#insn-00aad300) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad30c`](#insn-00aad30c) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad320`](#insn-00aad320) → `002be3b5`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad320`](#insn-00aad320) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad324`](#insn-00aad324) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aad330`](#insn-00aad330) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad340`](#insn-00aad340) → [`00784280`](../00784/00784280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784280` · 推定シンボル `None` · 推定型 `None`
- [`00aad34c`](#insn-00aad34c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad350`](#insn-00aad350) → `002bef0d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad350`](#insn-00aad350) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad354`](#insn-00aad354) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad360`](#insn-00aad360) → [`00c5a8f0`](../00c5a/00c5a8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8f0` · 推定シンボル `None` · 推定型 `None`
- [`00aad36c`](#insn-00aad36c) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad378`](#insn-00aad378) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad37c`](#insn-00aad37c) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad380`](#insn-00aad380) → [`00aad38c`](#insn-00aad38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad384`](#insn-00aad384) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad388`](#insn-00aad388) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aad38c`](#insn-00aad38c) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad390`](#insn-00aad390) → [`00aad39c`](#insn-00aad39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad394`](#insn-00aad394) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad398`](#insn-00aad398) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aad3a4`](#insn-00aad3a4) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad3a8`](#insn-00aad3a8) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3ac`](#insn-00aad3ac) → [`00aad3b8`](#insn-00aad3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3b0`](#insn-00aad3b0) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3b4`](#insn-00aad3b4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aad3b8`](#insn-00aad3b8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aad3d4`](#insn-00aad3d4) → [`0087929c`](../00879/0087929c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087929c` · 推定シンボル `None` · 推定型 `None`
- [`00aad3e0`](#insn-00aad3e0) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad3ec`](#insn-00aad3ec) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad3f8`](#insn-00aad3f8) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad404`](#insn-00aad404) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad410`](#insn-00aad410) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad420`](#insn-00aad420) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aad424`](#insn-00aad424) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad428`](#insn-00aad428) → [`00aad434`](#insn-00aad434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad42c`](#insn-00aad42c) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad430`](#insn-00aad430) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aad438`](#insn-00aad438) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad440`](#insn-00aad440) → [`00aad690`](#insn-00aad690) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad448`](#insn-00aad448) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad44c`](#insn-00aad44c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad450`](#insn-00aad450) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad454`](#insn-00aad454) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad458`](#insn-00aad458) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad690`](#insn-00aad690) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aacea4`](#insn-00aacea4)

~~~json
{
  "source": "00aacea4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacea8`](#insn-00aacea8)

~~~json
{
  "source": "00aacea8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaceac`](#insn-00aaceac)

~~~json
{
  "source": "00aaceac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaceb0`](#insn-00aaceb0)

~~~json
{
  "source": "00aaceb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaceb4`](#insn-00aaceb4)

~~~json
{
  "source": "00aaceb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaced8`](#insn-00aaced8)

~~~json
{
  "source": "00aaced8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacedc`](#insn-00aacedc)

~~~json
{
  "source": "00aacedc",
  "target": "00aacf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacee0`](#insn-00aacee0)

~~~json
{
  "source": "00aacee0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacee4`](#insn-00aacee4)

~~~json
{
  "source": "00aacee4",
  "target": "00853c70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacef0`](#insn-00aacef0)

~~~json
{
  "source": "00aacef0",
  "target": "00aad16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacef8`](#insn-00aacef8)

~~~json
{
  "source": "00aacef8",
  "target": "00aad434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacefc`](#insn-00aacefc)

~~~json
{
  "source": "00aacefc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf08`](#insn-00aacf08)

~~~json
{
  "source": "00aacf08",
  "target": "00333f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f48",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8a66c00d48c0900",
  "capture_start": "00333f48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacf0c`](#insn-00aacf0c)

~~~json
{
  "source": "00aacf0c",
  "target": "00aad178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf10`](#insn-00aacf10)

~~~json
{
  "source": "00aacf10",
  "target": "00aad434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf24`](#insn-00aacf24)

~~~json
{
  "source": "00aacf24",
  "target": "002bac25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bac25",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "42634c6f6750757263686173655472696767657200",
  "capture_start": "002bac25",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacf30`](#insn-00aacf30)

~~~json
{
  "source": "00aacf30",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf40`](#insn-00aacf40)

~~~json
{
  "source": "00aacf40",
  "target": "Stack[-0x137]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf44`](#insn-00aacf44)

~~~json
{
  "source": "00aacf44",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf48`](#insn-00aacf48)

~~~json
{
  "source": "00aacf48",
  "target": "Stack[-0x133]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf4c`](#insn-00aacf4c)

~~~json
{
  "source": "00aacf4c",
  "target": "002aeaf4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeaf4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeaf4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacf4c`](#insn-00aacf4c)

~~~json
{
  "source": "00aacf4c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf50`](#insn-00aacf50)

~~~json
{
  "source": "00aacf50",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf54`](#insn-00aacf54)

~~~json
{
  "source": "00aacf54",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf58`](#insn-00aacf58)

~~~json
{
  "source": "00aacf58",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf64`](#insn-00aacf64)

~~~json
{
  "source": "00aacf64",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf78`](#insn-00aacf78)

~~~json
{
  "source": "00aacf78",
  "target": "002b7b87",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7b87",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5472696767657200",
  "capture_start": "002b7b87",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacf78`](#insn-00aacf78)

~~~json
{
  "source": "00aacf78",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf7c`](#insn-00aacf7c)

~~~json
{
  "source": "00aacf7c",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf88`](#insn-00aacf88)

~~~json
{
  "source": "00aacf88",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf9c`](#insn-00aacf9c)

~~~json
{
  "source": "00aacf9c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfa8`](#insn-00aacfa8)

~~~json
{
  "source": "00aacfa8",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfb8`](#insn-00aacfb8)

~~~json
{
  "source": "00aacfb8",
  "target": "002b1e48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e48",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacfb8`](#insn-00aacfb8)

~~~json
{
  "source": "00aacfb8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfbc`](#insn-00aacfbc)

~~~json
{
  "source": "00aacfbc",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfc0`](#insn-00aacfc0)

~~~json
{
  "source": "00aacfc0",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfcc`](#insn-00aacfcc)

~~~json
{
  "source": "00aacfcc",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfdc`](#insn-00aacfdc)

~~~json
{
  "source": "00aacfdc",
  "target": "002a7aba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7aba",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a7aba",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacfdc`](#insn-00aacfdc)

~~~json
{
  "source": "00aacfdc",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe0`](#insn-00aacfe0)

~~~json
{
  "source": "00aacfe0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe4`](#insn-00aacfe4)

~~~json
{
  "source": "00aacfe4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe8`](#insn-00aacfe8)

~~~json
{
  "source": "00aacfe8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacff4`](#insn-00aacff4)

~~~json
{
  "source": "00aacff4",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad008`](#insn-00aad008)

~~~json
{
  "source": "00aad008",
  "target": "002a187d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a187d",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "53656c65637400",
  "capture_start": "002a187d",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad008`](#insn-00aad008)

~~~json
{
  "source": "00aad008",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad00c`](#insn-00aad00c)

~~~json
{
  "source": "00aad00c",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad018`](#insn-00aad018)

~~~json
{
  "source": "00aad018",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad028`](#insn-00aad028)

~~~json
{
  "source": "00aad028",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad034`](#insn-00aad034)

~~~json
{
  "source": "00aad034",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad038`](#insn-00aad038)

~~~json
{
  "source": "00aad038",
  "target": "002afc2b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afc2b",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afc2b",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad038`](#insn-00aad038)

~~~json
{
  "source": "00aad038",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad03c`](#insn-00aad03c)

~~~json
{
  "source": "00aad03c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad048`](#insn-00aad048)

~~~json
{
  "source": "00aad048",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad05c`](#insn-00aad05c)

~~~json
{
  "source": "00aad05c",
  "target": "002a8df7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8df7",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "65785f7479706500",
  "capture_start": "002a8df7",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad05c`](#insn-00aad05c)

~~~json
{
  "source": "00aad05c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad060`](#insn-00aad060)

~~~json
{
  "source": "00aad060",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad064`](#insn-00aad064)

~~~json
{
  "source": "00aad064",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad068`](#insn-00aad068)

~~~json
{
  "source": "00aad068",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad074`](#insn-00aad074)

~~~json
{
  "source": "00aad074",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad088`](#insn-00aad088)

~~~json
{
  "source": "00aad088",
  "target": "002be3b5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be3b5",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "436f6e74656e7400",
  "capture_start": "002be3b5",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad088`](#insn-00aad088)

~~~json
{
  "source": "00aad088",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad08c`](#insn-00aad08c)

~~~json
{
  "source": "00aad08c",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad098`](#insn-00aad098)

~~~json
{
  "source": "00aad098",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0a8`](#insn-00aad0a8)

~~~json
{
  "source": "00aad0a8",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0b4`](#insn-00aad0b4)

~~~json
{
  "source": "00aad0b4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0b8`](#insn-00aad0b8)

~~~json
{
  "source": "00aad0b8",
  "target": "002bef0d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bef0d",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "65785f696400",
  "capture_start": "002bef0d",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad0b8`](#insn-00aad0b8)

~~~json
{
  "source": "00aad0b8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0bc`](#insn-00aad0bc)

~~~json
{
  "source": "00aad0bc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0c8`](#insn-00aad0c8)

~~~json
{
  "source": "00aad0c8",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0d4`](#insn-00aad0d4)

~~~json
{
  "source": "00aad0d4",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0e0`](#insn-00aad0e0)

~~~json
{
  "source": "00aad0e0",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0ec`](#insn-00aad0ec)

~~~json
{
  "source": "00aad0ec",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad0f0`](#insn-00aad0f0)

~~~json
{
  "source": "00aad0f0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0f4`](#insn-00aad0f4)

~~~json
{
  "source": "00aad0f4",
  "target": "00aad100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0f8`](#insn-00aad0f8)

~~~json
{
  "source": "00aad0f8",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad0fc`](#insn-00aad0fc)

~~~json
{
  "source": "00aad0fc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad100`](#insn-00aad100)

~~~json
{
  "source": "00aad100",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad118`](#insn-00aad118)

~~~json
{
  "source": "00aad118",
  "target": "0087929c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad124`](#insn-00aad124)

~~~json
{
  "source": "00aad124",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad130`](#insn-00aad130)

~~~json
{
  "source": "00aad130",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad13c`](#insn-00aad13c)

~~~json
{
  "source": "00aad13c",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad148`](#insn-00aad148)

~~~json
{
  "source": "00aad148",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad154`](#insn-00aad154)

~~~json
{
  "source": "00aad154",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad164`](#insn-00aad164)

~~~json
{
  "source": "00aad164",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad168`](#insn-00aad168)

~~~json
{
  "source": "00aad168",
  "target": "00aad424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad16c`](#insn-00aad16c)

~~~json
{
  "source": "00aad16c",
  "target": "005e0d68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad174`](#insn-00aad174)

~~~json
{
  "source": "00aad174",
  "target": "00aad434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad188`](#insn-00aad188)

~~~json
{
  "source": "00aad188",
  "target": "002bac25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bac25",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "42634c6f6750757263686173655472696767657200",
  "capture_start": "002bac25",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad18c`](#insn-00aad18c)

~~~json
{
  "source": "00aad18c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1a0`](#insn-00aad1a0)

~~~json
{
  "source": "00aad1a0",
  "target": "Stack[-0x137]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1a4`](#insn-00aad1a4)

~~~json
{
  "source": "00aad1a4",
  "target": "Stack[-0x147]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1a8`](#insn-00aad1a8)

~~~json
{
  "source": "00aad1a8",
  "target": "Stack[-0x133]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1ac`](#insn-00aad1ac)

~~~json
{
  "source": "00aad1ac",
  "target": "002aeaf4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeaf4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeaf4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad1ac`](#insn-00aad1ac)

~~~json
{
  "source": "00aad1ac",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b0`](#insn-00aad1b0)

~~~json
{
  "source": "00aad1b0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b4`](#insn-00aad1b4)

~~~json
{
  "source": "00aad1b4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1b8`](#insn-00aad1b8)

~~~json
{
  "source": "00aad1b8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1c4`](#insn-00aad1c4)

~~~json
{
  "source": "00aad1c4",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1d8`](#insn-00aad1d8)

~~~json
{
  "source": "00aad1d8",
  "target": "002b7b87",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7b87",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "5472696767657200",
  "capture_start": "002b7b87",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad1d8`](#insn-00aad1d8)

~~~json
{
  "source": "00aad1d8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad1dc`](#insn-00aad1dc)

~~~json
{
  "source": "00aad1dc",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1e8`](#insn-00aad1e8)

~~~json
{
  "source": "00aad1e8",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad1fc`](#insn-00aad1fc)

~~~json
{
  "source": "00aad1fc",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad208`](#insn-00aad208)

~~~json
{
  "source": "00aad208",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad218`](#insn-00aad218)

~~~json
{
  "source": "00aad218",
  "target": "002b1e48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e48",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad218`](#insn-00aad218)

~~~json
{
  "source": "00aad218",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad21c`](#insn-00aad21c)

~~~json
{
  "source": "00aad21c",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad220`](#insn-00aad220)

~~~json
{
  "source": "00aad220",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad22c`](#insn-00aad22c)

~~~json
{
  "source": "00aad22c",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad23c`](#insn-00aad23c)

~~~json
{
  "source": "00aad23c",
  "target": "002a7aba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7aba",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a7aba",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad23c`](#insn-00aad23c)

~~~json
{
  "source": "00aad23c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad240`](#insn-00aad240)

~~~json
{
  "source": "00aad240",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad244`](#insn-00aad244)

~~~json
{
  "source": "00aad244",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad248`](#insn-00aad248)

~~~json
{
  "source": "00aad248",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad254`](#insn-00aad254)

~~~json
{
  "source": "00aad254",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad268`](#insn-00aad268)

~~~json
{
  "source": "00aad268",
  "target": "002a187d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a187d",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "53656c65637400",
  "capture_start": "002a187d",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad268`](#insn-00aad268)

~~~json
{
  "source": "00aad268",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad26c`](#insn-00aad26c)

~~~json
{
  "source": "00aad26c",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad278`](#insn-00aad278)

~~~json
{
  "source": "00aad278",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad288`](#insn-00aad288)

~~~json
{
  "source": "00aad288",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad298`](#insn-00aad298)

~~~json
{
  "source": "00aad298",
  "target": "Stack[-0x1bf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad29c`](#insn-00aad29c)

~~~json
{
  "source": "00aad29c",
  "target": "Stack[-0x1bb]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2b4`](#insn-00aad2b4)

~~~json
{
  "source": "00aad2b4",
  "target": "004476f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad2c0`](#insn-00aad2c0)

~~~json
{
  "source": "00aad2c0",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad2d0`](#insn-00aad2d0)

~~~json
{
  "source": "00aad2d0",
  "target": "002afc2b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afc2b",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afc2b",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad2d0`](#insn-00aad2d0)

~~~json
{
  "source": "00aad2d0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2d4`](#insn-00aad2d4)

~~~json
{
  "source": "00aad2d4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2d8`](#insn-00aad2d8)

~~~json
{
  "source": "00aad2d8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2e4`](#insn-00aad2e4)

~~~json
{
  "source": "00aad2e4",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad2f4`](#insn-00aad2f4)

~~~json
{
  "source": "00aad2f4",
  "target": "002a8df7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8df7",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "65785f7479706500",
  "capture_start": "002a8df7",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad2f4`](#insn-00aad2f4)

~~~json
{
  "source": "00aad2f4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2f8`](#insn-00aad2f8)

~~~json
{
  "source": "00aad2f8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2fc`](#insn-00aad2fc)

~~~json
{
  "source": "00aad2fc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad300`](#insn-00aad300)

~~~json
{
  "source": "00aad300",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad30c`](#insn-00aad30c)

~~~json
{
  "source": "00aad30c",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad320`](#insn-00aad320)

~~~json
{
  "source": "00aad320",
  "target": "002be3b5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be3b5",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "436f6e74656e7400",
  "capture_start": "002be3b5",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad320`](#insn-00aad320)

~~~json
{
  "source": "00aad320",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad324`](#insn-00aad324)

~~~json
{
  "source": "00aad324",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad330`](#insn-00aad330)

~~~json
{
  "source": "00aad330",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad340`](#insn-00aad340)

~~~json
{
  "source": "00aad340",
  "target": "00784280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad34c`](#insn-00aad34c)

~~~json
{
  "source": "00aad34c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad350`](#insn-00aad350)

~~~json
{
  "source": "00aad350",
  "target": "002bef0d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bef0d",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "65785f696400",
  "capture_start": "002bef0d",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad350`](#insn-00aad350)

~~~json
{
  "source": "00aad350",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad354`](#insn-00aad354)

~~~json
{
  "source": "00aad354",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad360`](#insn-00aad360)

~~~json
{
  "source": "00aad360",
  "target": "00c5a8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad36c`](#insn-00aad36c)

~~~json
{
  "source": "00aad36c",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad378`](#insn-00aad378)

~~~json
{
  "source": "00aad378",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad37c`](#insn-00aad37c)

~~~json
{
  "source": "00aad37c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad380`](#insn-00aad380)

~~~json
{
  "source": "00aad380",
  "target": "00aad38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad384`](#insn-00aad384)

~~~json
{
  "source": "00aad384",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad388`](#insn-00aad388)

~~~json
{
  "source": "00aad388",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad38c`](#insn-00aad38c)

~~~json
{
  "source": "00aad38c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad390`](#insn-00aad390)

~~~json
{
  "source": "00aad390",
  "target": "00aad39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad394`](#insn-00aad394)

~~~json
{
  "source": "00aad394",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad398`](#insn-00aad398)

~~~json
{
  "source": "00aad398",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3a4`](#insn-00aad3a4)

~~~json
{
  "source": "00aad3a4",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3a8`](#insn-00aad3a8)

~~~json
{
  "source": "00aad3a8",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3ac`](#insn-00aad3ac)

~~~json
{
  "source": "00aad3ac",
  "target": "00aad3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3b0`](#insn-00aad3b0)

~~~json
{
  "source": "00aad3b0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3b4`](#insn-00aad3b4)

~~~json
{
  "source": "00aad3b4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3b8`](#insn-00aad3b8)

~~~json
{
  "source": "00aad3b8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3d4`](#insn-00aad3d4)

~~~json
{
  "source": "00aad3d4",
  "target": "0087929c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3e0`](#insn-00aad3e0)

~~~json
{
  "source": "00aad3e0",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3ec`](#insn-00aad3ec)

~~~json
{
  "source": "00aad3ec",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3f8`](#insn-00aad3f8)

~~~json
{
  "source": "00aad3f8",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad404`](#insn-00aad404)

~~~json
{
  "source": "00aad404",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad410`](#insn-00aad410)

~~~json
{
  "source": "00aad410",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad420`](#insn-00aad420)

~~~json
{
  "source": "00aad420",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad424`](#insn-00aad424)

~~~json
{
  "source": "00aad424",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad428`](#insn-00aad428)

~~~json
{
  "source": "00aad428",
  "target": "00aad434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad42c`](#insn-00aad42c)

~~~json
{
  "source": "00aad42c",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad430`](#insn-00aad430)

~~~json
{
  "source": "00aad430",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad438`](#insn-00aad438)

~~~json
{
  "source": "00aad438",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad440`](#insn-00aad440)

~~~json
{
  "source": "00aad440",
  "target": "00aad690",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad448`](#insn-00aad448)

~~~json
{
  "source": "00aad448",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad44c`](#insn-00aad44c)

~~~json
{
  "source": "00aad44c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad450`](#insn-00aad450)

~~~json
{
  "source": "00aad450",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad454`](#insn-00aad454)

~~~json
{
  "source": "00aad454",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad458`](#insn-00aad458)

~~~json
{
  "source": "00aad458",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad690`](#insn-00aad690)

~~~json
{
  "source": "00aad690",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
