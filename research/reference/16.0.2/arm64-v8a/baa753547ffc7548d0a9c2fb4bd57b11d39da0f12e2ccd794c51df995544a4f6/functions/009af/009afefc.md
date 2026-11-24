# 009afefc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009afea8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009afea8.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0057.md#compare-f3ee3eb0a5933466aa5315e32283f7b1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009b0ea8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0058.md#compare-be72188d73be4ca54db10ebbcfd9b8c9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009afefc",
  "name": "FUN_009afefc",
  "size": 1224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce618ea68c80343d16a086fd7e265ba9a5ce92c9a769e3c7d3519cff3f0f2e63",
  "source_text_sha256": "ce618ea68c80343d16a086fd7e265ba9a5ce92c9a769e3c7d3519cff3f0f2e63",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009afefc",
        "009b03bf"
      ],
      [
        "009b0524",
        "009b0527"
      ]
    ],
    "bytes_sha256": "14a092c4373abc7fa9d630f02684f7b132f7dac8ad4e60df630d84558cc40e2d",
    "instruction_count": 306,
    "instruction_bytes": 1224,
    "body_bytes": 1224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0089e8d4](../0089e/0089e8d4.md)

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [0048cd38](../0048c/0048cd38.md)
- [0048ce94](../0048c/0048ce94.md)
- [00492d0c](../00492/00492d0c.md)
- [007299cc](../00729/007299cc.md)
- [0074a82c](../0074a/0074a82c.md)
- [00869f4c](../00869/00869f4c.md)
- [008ae85c](../008ae/008ae85c.md)
- [009aadfc](../009aa/009aadfc.md)
- [009aae10](../009aa/009aae10.md)
- [009aae24](../009aa/009aae24.md)
- [009ad9d4](../009ad/009ad9d4.md)
- [009b0558](../009b0/009b0558.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58040](../00c58/00c58040.md)
- [00c58050](../00c58/00c58050.md)

## 関連文字列（未確認候補）

~~~text
"/%02d（%d:%02d）〜%d/%02d/%02d（%d:%02d）\")"
"d（%d:%02d）\")"
"ranking_no_reward"
"setData(%d, \"%@\", \"%@\")"
"setDate(\"%d/%02d/%02d（%d:%02d）〜%d/%02d/%02d（%d:%02d）\")"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 11716 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_009afefc(void)

{
  byte *pbVar1;
  long lVar2;
  undefined8 uVar3;
  byte *pbVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong uVar7;
  void *pvVar8;
  undefined8 uVar9;
  int in_w3;
  ulong uVar10;
  uint uVar11;
  undefined8 uVar12;
  char *pcVar13;
  ulong uVar14;
  void *pvVar15;
  long lVar16;
  byte local_178 [16];
  void *local_168;
  ulong local_160;
  ulong uStack_158;
  void *local_150;
  ulong local_140;
  undefined8 uStack_138;
  char *local_130;
  uint local_128;
  undefined4 uStack_124;
  undefined4 local_120;
  undefined4 uStack_11c;
  undefined4 local_118;
  undefined4 uStack_114;
  undefined8 local_110;
  undefined8 uStack_108;
  void *local_100;
  uint local_f8 [2];
  byte local_f0 [8];
  void *local_e8;
  void *local_e0;
  void *local_d0;
  byte *local_b8;
  byte *local_b0;
  void *local_a0;
  void *pvStack_98;
  undefined8 *local_90;
  void *local_88;
  void *local_80;
  long local_70;
  
                    /* try { // try from 009aff14 to 00aaff1b has its CatchHandler @ 009b0188 */
                    /* try { // try from 009aff1c to 00aaff3f has its CatchHandler @ 009af994 */
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  FUN_009ad9d4(&local_88);
                    /* try { // try from 009aff40 to 00aaff7f has its CatchHandler @ 009b0190 */
  if ((local_88 != local_80) && ((ulong)(long)in_w3 < (ulong)((long)local_80 - (long)local_88 >> 3))
     ) {
    uVar9 = FUN_0048cd38();
    uVar12 = *(undefined8 *)((long)local_88 + (long)in_w3 * 8);
    FUN_009aadfc(&local_110,uVar12);
    FUN_009aae10(&local_128,uVar12);
    local_90 = (undefined8 *)_Znwm(0x48);
    uVar6 = _UNK_002a492d;
    uVar3 = _DAT_002a4925;
    uVar5 = _DAT_002a4915;
                    /* try { // try from 009affa4 to 00aaffab has its CatchHandler @ 009b0174 */
    local_90[1] = _UNK_002a491d;
    *local_90 = uVar5;
    local_90[3] = uVar6;
    local_90[2] = uVar3;
    uVar6 = _UNK_002a494d;
    uVar3 = _DAT_002a4945;
    uVar5 = _DAT_002a4935;
    local_90[5] = _UNK_002a493d;
    local_90[4] = uVar5;
    local_90[7] = uVar6;
    local_90[6] = uVar3;
    pvStack_98 = _UNK_002c3298;
    local_a0 = _DAT_002c3290;
    *(undefined1 *)(local_90 + 8) = 0;
                    /* try { // try from 009affe0 to 00aaffe7 has its CatchHandler @ 009b0160 */
    FUN_008ae85c(local_f8,&local_a0,0,local_110 & 0xffffffff,local_110._4_4_,uStack_108 & 0xffffffff
                 ,uStack_108._4_4_,(ulong)local_100 & 0xffffffff,local_128,uStack_124,local_120,
                 uStack_11c,local_118);
                    /* try { // try from 009affec to 00aafffb has its CatchHandler @ 009b0140 */
    if (((ulong)local_a0 & 1) != 0) {
      _ZdlPv(local_90);
    }
                    /* try { // try from 009afffc to 00ab000b has its CatchHandler @ 009b013c */
    FUN_00492d0c(uVar9,local_f8);
    if ((local_f8[0] & 1) != 0) {
      _ZdlPv(local_e8);
    }
    FUN_009aae24(&local_a0,uVar12);
    pvVar8 = pvStack_98;
    uVar5 = _UNK_002c2498;
    uVar7 = _DAT_002c2490;
    if (local_a0 != pvStack_98) {
                    /* try { // try from 009b003c to 00ab004f has its CatchHandler @ 009b016c */
      pcVar13 = (char *)((ulong)&local_140 | 1);
      pvVar15 = local_a0;
                    /* try { // try from 009b0054 to 00ab009b has its CatchHandler @ 009b017c */
      do {
        FUN_0074a82c(local_f8,pvVar15);
        local_110 = 0;
        uStack_108 = 0;
        local_100 = (void *)0x0;
                    /* try { // try from 009b009c to 00ab0107 has its CatchHandler @ 009af994 */
        if (local_b0 == local_b8) {
                    /* catch() { ... } // from try @ 009afd50 with catch @ 009b0148 */
          uVar11 = 0;
        }
        else {
          uVar14 = *(ulong *)(local_b8 + 8);
          pbVar1 = *(byte **)(local_b8 + 0x10);
          if ((*local_b8 & 1) == 0) {
            pbVar1 = local_b8 + 1;
            uVar14 = (ulong)(*local_b8 >> 1);
          }
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                    (&local_110,pbVar1,uVar14);
          if (1 < (ulong)(((long)local_b0 - (long)local_b8 >> 3) * -0x5555555555555555)) {
            lVar16 = 0;
            uVar14 = 1;
            do {
              _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                        (&local_110,&DAT_002b6881);
                    /* try { // try from 009b0108 to 00ab010f has its CatchHandler @ 009b01a0 */
              uVar10 = (ulong)(local_b8[lVar16 + 0x18] >> 1);
              pbVar1 = local_b8 + lVar16 + 0x19;
              if ((local_b8[lVar16 + 0x18] & 1) != 0) {
                uVar10 = *(ulong *)(local_b8 + lVar16 + 0x20);
                pbVar1 = *(byte **)(local_b8 + lVar16 + 0x28);
              }
              _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                        (&local_110,pbVar1,uVar10);
                    /* try { // try from 009b0120 to 00ab0127 has its CatchHandler @ 009b0188 */
              uVar14 = uVar14 + 1;
              lVar16 = lVar16 + 0x18;
                    /* catch() { ... } // from try @ 009afd1c with catch @ 009b0128
                       try { // try from 009b0128 to 00ab01f7 has its CatchHandler @ 009af994 */
                    /* catch() { ... } // from try @ 009afce0 with catch @ 009b0130 */
              uVar10 = ((long)local_b0 - (long)local_b8 >> 3) * -0x5555555555555555;
                    /* catch() { ... } // from try @ 009afcd0 with catch @ 009b0134 */
            } while (uVar14 <= uVar10 && uVar10 - uVar14 != 0);
          }
                    /* catch() { ... } // from try @ 009afffc with catch @ 009b013c */
          uVar11 = (uint)(byte)local_110;
                    /* catch() { ... } // from try @ 009afbcc with catch @ 009b0140
                       catch() { ... } // from try @ 009affec with catch @ 009b0140 */
        }
        uVar6 = s_ranking_no_reward_002b2320._8_8_;
        uVar3 = s_ranking_no_reward_002b2320._0_8_;
                    /* catch() { ... } // from try @ 009afb88 with catch @ 009b0150 */
                    /* catch() { ... } // from try @ 009afb78 with catch @ 009b0154 */
        uVar14 = (ulong)(uVar11 >> 1);
        if ((uVar11 & 1) != 0) {
          uVar14 = uStack_108;
        }
                    /* catch() { ... } // from try @ 009afcb4 with catch @ 009b015c */
        if (uVar14 == 0) {
                    /* catch() { ... } // from try @ 009affe0 with catch @ 009b0160 */
                    /* catch() { ... } // from try @ 009afe38 with catch @ 009b0164 */
          local_130._0_3_ = (uint3)(ushort)local_130;
                    /* catch() { ... } // from try @ 009afd68 with catch @ 009b0168 */
          local_140 = CONCAT71(local_140._1_7_,0x22);
                    /* catch() { ... } // from try @ 009b003c with catch @ 009b016c */
                    /* catch() { ... } // from try @ 009affa4 with catch @ 009b0174 */
                    /* catch() { ... } // from try @ 009b0054 with catch @ 009b017c */
          pcVar13[0x10] = 'd';
                    /* catch() { ... } // from try @ 009afdb4 with catch @ 009b0180 */
          *(undefined8 *)(pcVar13 + 8) = uVar6;
          *(undefined8 *)pcVar13 = uVar3;
                    /* catch() { ... } // from try @ 009afb18 with catch @ 009b0184 */
                    /* catch() { ... } // from try @ 009aff14 with catch @ 009b0188
                       catch() { ... } // from try @ 009b0120 with catch @ 009b0188 */
          FUN_0048ce94(&local_128,&local_140);
                    /* catch() { ... } // from try @ 009aff40 with catch @ 009b0190 */
          uVar14 = (ulong)((byte)local_128 >> 1);
          uVar10 = (ulong)&local_128 | 1;
                    /* catch() { ... } // from try @ 009afe5c with catch @ 009b01a0
                       catch() { ... } // from try @ 009b0108 with catch @ 009b01a0 */
          if ((local_128 & 1) != 0) {
            uVar14 = CONCAT44(uStack_11c,local_120);
            uVar10 = CONCAT44(uStack_114,local_118);
          }
                    /* catch() { ... } // from try @ 009afea4 with catch @ 009b01a8 */
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                    (&local_110,uVar10,uVar14);
          if ((local_128 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_114,local_118));
          }
          if ((local_140 & 1) != 0) {
            _ZdlPv(local_130);
          }
        }
        local_130 = (char *)_Znwm(0x19);
        uVar11 = local_f8[0];
        uVar6 = s_setData__d______________002b2332._0_8_;
        uVar3 = CONCAT71(s_setData__d______________002b2332._16_7_,
                         s_setData__d______________002b2332[0xf]);
        uStack_138 = uVar5;
        local_140 = uVar7;
                    /* try { // try from 009b01f8 to 00ab036f has its CatchHandler @ 009b01f8
                       catch() { ... } // from try @ 009b01f8 with catch @ 009b01f8
                       catch() { ... } // from try @ 009b0430 with catch @ 009b01f8
                       catch() { ... } // from try @ 009b06b4 with catch @ 009b01f8
                       catch() { ... } // from try @ 009b0764 with catch @ 009b01f8
                       catch() { ... } // from try @ 009b08d4 with catch @ 009b01f8
                       catch() { ... } // from try @ 009b0960 with catch @ 009b01f8 */
        *(ulong *)(local_130 + 8) =
             CONCAT17(s_setData__d______________002b2332[0xf],
                      s_setData__d______________002b2332._8_7_);
        *(undefined8 *)local_130 = uVar6;
        *(undefined8 *)(local_130 + 0xf) = uVar3;
        local_130[0x17] = '\0';
        if ((local_110 & 1) == 0) {
          uStack_158 = uStack_108;
          local_160 = local_110;
          local_150 = local_100;
        }
        else {
          FUN_0043bb60(&local_160,local_100,uStack_108);
        }
        FUN_0048ce94(local_178,local_f0);
        FUN_007299cc(&local_128,&local_140,uVar11,&local_160,local_178);
        FUN_00492d0c(uVar9,&local_128);
        if ((local_128 & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_114,local_118));
        }
        if ((local_178[0] & 1) != 0) {
          _ZdlPv(local_168);
        }
        if ((local_160 & 1) != 0) {
          _ZdlPv(local_150);
        }
        if ((local_140 & 1) != 0) {
          _ZdlPv(local_130);
        }
        pbVar1 = local_b8;
        if ((local_110 & 1) != 0) {
          _ZdlPv(local_100);
          pbVar1 = local_b8;
        }
        local_b8 = pbVar1;
        if (pbVar1 != (byte *)0x0) {
          while (pbVar4 = local_b0, pbVar4 != pbVar1) {
            local_b0 = pbVar4 + -0x18;
            if ((*local_b0 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar4 + -8));
            }
          }
          local_b0 = pbVar1;
          _ZdlPv(local_b8);
        }
        if (local_d0 != (void *)0x0) {
          _ZdlPv(local_d0);
        }
        if ((local_f0[0] & 1) != 0) {
          _ZdlPv(local_e0);
        }
        pvVar15 = (void *)((long)pvVar15 + 0x58);
      } while (pvVar15 != pvVar8);
    }
    if (local_a0 != (void *)0x0) {
      FUN_00869f4c(&local_a0,local_a0);
      _ZdlPv(local_a0);
    }
                    /* try { // try from 009b0370 to 00ab037b has its CatchHandler @ 009b09bc */
    FUN_009b0558();
  }
  if (local_88 != (void *)0x0) {
    _ZdlPv(local_88);
  }
  if (*(long *)(lVar2 + 0x28) == local_70) {
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
<a id="insn-009afefc"></a> `009afefc` | `ff 83 07 d1` | sub sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-009aff00"></a> `009aff00` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009aff04"></a> `009aff04` | `fc 6f 19 a9` | stp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009aff08"></a> `009aff08` | `fa 67 1a a9` | stp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-009aff0c"></a> `009aff0c` | `f8 5f 1b a9` | stp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-009aff10"></a> `009aff10` | `f6 57 1c a9` | stp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-009aff14"></a> `009aff14` | `f4 4f 1d a9` | stp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-009aff18"></a> `009aff18` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-009aff1c"></a> `009aff1c` | `e1 23 00 f9` | str x1,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009aff20"></a> `009aff20` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009aff24"></a> `009aff24` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-009aff28"></a> `009aff28` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009aff2c"></a> `009aff2c` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-009aff30"></a> `009aff30` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009aff34"></a> `009aff34` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-009aff38"></a> `009aff38` | `a7 f6 ff 97` | bl 0x009ad9d4 | `UNCONDITIONAL_CALL`
<a id="insn-009aff3c"></a> `009aff3c` | `a0 a3 7d a9` | ldp x0,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-009aff40"></a> `009aff40` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-009aff44"></a> `009aff44` | `00 22 00 54` | b.eq 0x009b0384 | `CONDITIONAL_JUMP`
<a id="insn-009aff48"></a> `009aff48` | `b3 7e 40 93` | sxtw x19,w21 | `FALL_THROUGH`
<a id="insn-009aff4c"></a> `009aff4c` | `08 01 00 cb` | sub x8,x8,x0 | `FALL_THROUGH`
<a id="insn-009aff50"></a> `009aff50` | `7f 0e 88 eb` | cmp x19,x8, ASR #0x3 | `FALL_THROUGH`
<a id="insn-009aff54"></a> `009aff54` | `82 21 00 54` | b.cs 0x009b0384 | `CONDITIONAL_JUMP`
<a id="insn-009aff58"></a> `009aff58` | `78 73 eb 97` | bl 0x0048cd38 | `UNCONDITIONAL_CALL`
<a id="insn-009aff5c"></a> `009aff5c` | `a8 83 5d f8` | ldur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-009aff60"></a> `009aff60` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-009aff64"></a> `009aff64` | `13 79 73 f8` | ldr x19,[x8, x19, LSL #0x3] | `FALL_THROUGH`
<a id="insn-009aff68"></a> `009aff68` | `a8 c3 02 d1` | sub x8,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-009aff6c"></a> `009aff6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009aff70"></a> `009aff70` | `a3 eb ff 97` | bl 0x009aadfc | `UNCONDITIONAL_CALL`
<a id="insn-009aff74"></a> `009aff74` | `e8 e3 02 91` | add x8,sp,#0xb8 | `FALL_THROUGH`
<a id="insn-009aff78"></a> `009aff78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009aff7c"></a> `009aff7c` | `a5 eb ff 97` | bl 0x009aae10 | `UNCONDITIONAL_CALL`
<a id="insn-009aff80"></a> `009aff80` | `00 09 80 52` | mov w0,#0x48 | `FALL_THROUGH`
<a id="insn-009aff84"></a> `009aff84` | `f7 9f 0a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-009aff88"></a> `009aff88` | `a8 c7 ff b0` | adrp x8,0x2a4000 | `FALL_THROUGH`
<a id="insn-009aff8c"></a> `009aff8c` | `08 55 24 91` | add x8,x8,#0x915 | `FALL_THROUGH`
<a id="insn-009aff90"></a> `009aff90` | `a6 03 56 b8` | ldur w6,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-009aff94"></a> `009aff94` | `00 05 40 ad` | ldp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-009aff98"></a> `009aff98` | `eb cb 40 b9` | ldr w11,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-009aff9c"></a> `009aff9c` | `a2 0f 6a 29` | ldp w2,w3,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009affa0"></a> `009affa0` | `a4 17 6b 29` | ldp w4,w5,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-009affa4"></a> `009affa4` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-009affa8"></a> `009affa8` | `02 01 41 ad` | ldp q2,q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-009affac"></a> `009affac` | `a8 c8 ff 90` | adrp x8,0x2c3000 | `FALL_THROUGH`
<a id="insn-009affb0"></a> `009affb0` | `a0 03 1d f8` | stur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009affb4"></a> `009affb4` | `e7 27 57 29` | ldp w7,w9,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-009affb8"></a> `009affb8` | `02 00 01 ad` | stp q2,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-009affbc"></a> `009affbc` | `00 a5 c0 3d` | ldr q0,[x8, #0x290] | `FALL_THROUGH`
<a id="insn-009affc0"></a> `009affc0` | `ea 23 58 29` | ldp w10,w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-009affc4"></a> `009affc4` | `1f 00 01 39` | strb wzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-009affc8"></a> `009affc8` | `a0 03 9c 3c` | stur q0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-009affcc"></a> `009affcc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-009affd0"></a> `009affd0` | `e8 13 00 b9` | str w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009affd4"></a> `009affd4` | `a8 63 02 d1` | sub x8,x29,#0x98 | `FALL_THROUGH`
<a id="insn-009affd8"></a> `009affd8` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-009affdc"></a> `009affdc` | `eb 1b 00 b9` | str w11,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009affe0"></a> `009affe0` | `ea 0b 00 b9` | str w10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009affe4"></a> `009affe4` | `e9 03 00 b9` | str w9,[sp] | `FALL_THROUGH`
<a id="insn-009affe8"></a> `009affe8` | `1d fa fb 97` | bl 0x008ae85c | `UNCONDITIONAL_CALL`
<a id="insn-009affec"></a> `009affec` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-009afff0"></a> `009afff0` | `68 00 00 36` | tbz w8,#0x0,0x009afffc | `CONDITIONAL_JUMP`
<a id="insn-009afff4"></a> `009afff4` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009afff8"></a> `009afff8` | `e2 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009afffc"></a> `009afffc` | `a1 63 02 d1` | sub x1,x29,#0x98 | `FALL_THROUGH`
<a id="insn-009b0000"></a> `009b0000` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009b0004"></a> `009b0004` | `42 8b eb 97` | bl 0x00492d0c | `UNCONDITIONAL_CALL`
<a id="insn-009b0008"></a> `009b0008` | `a8 83 56 38` | ldurb w8,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-009b000c"></a> `009b000c` | `68 00 00 36` | tbz w8,#0x0,0x009b0018 | `CONDITIONAL_JUMP`
<a id="insn-009b0010"></a> `009b0010` | `a0 83 57 f8` | ldur x0,[x29, #-0x88] | `FALL_THROUGH`
<a id="insn-009b0014"></a> `009b0014` | `db 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0018"></a> `009b0018` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-009b001c"></a> `009b001c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009b0020"></a> `009b0020` | `f7 53 03 a9` | stp x23,x20,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009b0024"></a> `009b0024` | `80 eb ff 97` | bl 0x009aae24 | `UNCONDITIONAL_CALL`
<a id="insn-009b0028"></a> `009b0028` | `b7 6f 7c a9` | ldp x23,x27,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-009b002c"></a> `009b002c` | `ff 02 1b eb` | cmp x23,x27 | `FALL_THROUGH`
<a id="insn-009b0030"></a> `009b0030` | `20 19 00 54` | b.eq 0x009b0354 | `CONDITIONAL_JUMP`
<a id="insn-009b0034"></a> `009b0034` | `e8 83 02 91` | add x8,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-009b0038"></a> `009b0038` | `e9 e3 02 91` | add x9,sp,#0xb8 | `FALL_THROUGH`
<a id="insn-009b003c"></a> `009b003c` | `fa f3 01 b2` | orr x26,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-009b0040"></a> `009b0040` | `14 01 40 b2` | orr x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-009b0044"></a> `009b0044` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-009b0048"></a> `009b0048` | `f3 17 00 f9` | str x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009b004c"></a> `009b004c` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009b0050"></a> `009b0050` | `88 c8 ff d0` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-009b0054"></a> `009b0054` | `bc 63 02 d1` | sub x28,x29,#0x98 | `FALL_THROUGH`
<a id="insn-009b0058"></a> `009b0058` | `00 25 c1 3d` | ldr q0,[x8, #0x490] | `FALL_THROUGH`
<a id="insn-009b005c"></a> `009b005c` | `13 c8 ff d0` | adrp x19,0x2b2000 | `FALL_THROUGH`
<a id="insn-009b0060"></a> `009b0060` | `73 ca 0c 91` | add x19,x19,#0x332 | `FALL_THROUGH`
<a id="insn-009b0064"></a> `009b0064` | `7a 55 95 f2` | movk x26,#0xaaab | `FALL_THROUGH`
<a id="insn-009b0068"></a> `009b0068` | `38 c8 ff d0` | adrp x24,0x2b6000 | `FALL_THROUGH`
<a id="insn-009b006c"></a> `009b006c` | `18 07 22 91` | add x24,x24,#0x881 | `FALL_THROUGH`
<a id="insn-009b0070"></a> `009b0070` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009b0074"></a> `009b0074` | `04 00 00 14` | b 0x009b0084 | `UNCONDITIONAL_JUMP`
<a id="insn-009b0078"></a> `009b0078` | `f7 62 01 91` | add x23,x23,#0x58 | `FALL_THROUGH`
<a id="insn-009b007c"></a> `009b007c` | `ff 02 1b eb` | cmp x23,x27 | `FALL_THROUGH`
<a id="insn-009b0080"></a> `009b0080` | `60 16 00 54` | b.eq 0x009b034c | `CONDITIONAL_JUMP`
<a id="insn-009b0084"></a> `009b0084` | `a0 63 02 d1` | sub x0,x29,#0x98 | `FALL_THROUGH`
<a id="insn-009b0088"></a> `009b0088` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-009b008c"></a> `009b008c` | `e8 69 f6 97` | bl 0x0074a82c | `UNCONDITIONAL_CALL`
<a id="insn-009b0090"></a> `009b0090` | `a8 a7 7a a9` | ldp x8,x9,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b0094"></a> `009b0094` | `bf 7f 35 a9` | stp xzr,xzr,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b0098"></a> `009b0098` | `bf 03 16 f8` | stur xzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-009b009c"></a> `009b009c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009b00a0"></a> `009b00a0` | `40 05 00 54` | b.eq 0x009b0148 | `CONDITIONAL_JUMP`
<a id="insn-009b00a4"></a> `009b00a4` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-009b00a8"></a> `009b00a8` | `0a ad 40 a9` | ldp x10,x11,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009b00ac"></a> `009b00ac` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-009b00b0"></a> `009b00b0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-009b00b4"></a> `009b00b4` | `61 15 88 9a` | csinc x1,x11,x8,ne | `FALL_THROUGH`
<a id="insn-009b00b8"></a> `009b00b8` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-009b00bc"></a> `009b00bc` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-009b00c0"></a> `009b00c0` | `e4 9f 0a 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-009b00c4"></a> `009b00c4` | `a9 a3 7a a9` | ldp x9,x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b00c8"></a> `009b00c8` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-009b00cc"></a> `009b00cc` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-009b00d0"></a> `009b00d0` | `08 7d 1a 9b` | mul x8,x8,x26 | `FALL_THROUGH`
<a id="insn-009b00d4"></a> `009b00d4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-009b00d8"></a> `009b00d8` | `23 03 00 54` | b.cc 0x009b013c | `CONDITIONAL_JUMP`
<a id="insn-009b00dc"></a> `009b00dc` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-009b00e0"></a> `009b00e0` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-009b00e4"></a> `009b00e4` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-009b00e8"></a> `009b00e8` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-009b00ec"></a> `009b00ec` | `d5 9f 0a 94` | bl 0x00c58040 | `UNCONDITIONAL_CALL`
<a id="insn-009b00f0"></a> `009b00f0` | `a8 83 5a f8` | ldur x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b00f4"></a> `009b00f4` | `08 01 19 8b` | add x8,x8,x25 | `FALL_THROUGH`
<a id="insn-009b00f8"></a> `009b00f8` | `09 61 40 39` | ldrb w9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-009b00fc"></a> `009b00fc` | `0a 2d 42 a9` | ldp x10,x11,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-009b0100"></a> `009b0100` | `08 65 00 91` | add x8,x8,#0x19 | `FALL_THROUGH`
<a id="insn-009b0104"></a> `009b0104` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-009b0108"></a> `009b0108` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-009b010c"></a> `009b010c` | `01 01 8b 9a` | csel x1,x8,x11,eq | `FALL_THROUGH`
<a id="insn-009b0110"></a> `009b0110` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-009b0114"></a> `009b0114` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-009b0118"></a> `009b0118` | `ce 9f 0a 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-009b011c"></a> `009b011c` | `a9 a3 7a a9` | ldp x9,x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b0120"></a> `009b0120` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-009b0124"></a> `009b0124` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-009b0128"></a> `009b0128` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-009b012c"></a> `009b012c` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-009b0130"></a> `009b0130` | `08 7d 1a 9b` | mul x8,x8,x26 | `FALL_THROUGH`
<a id="insn-009b0134"></a> `009b0134` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-009b0138"></a> `009b0138` | `68 fd ff 54` | b.hi 0x009b00e4 | `CONDITIONAL_JUMP`
<a id="insn-009b013c"></a> `009b013c` | `a9 03 55 38` | ldurb w9,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b0140"></a> `009b0140` | `a8 83 55 f8` | ldur x8,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-009b0144"></a> `009b0144` | `03 00 00 14` | b 0x009b0150 | `UNCONDITIONAL_JUMP`
<a id="insn-009b0148"></a> `009b0148` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-009b014c"></a> `009b014c` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-009b0150"></a> `009b0150` | `2a 7d 01 53` | lsr w10,w9,#0x1 | `FALL_THROUGH`
<a id="insn-009b0154"></a> `009b0154` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-009b0158"></a> `009b0158` | `48 01 88 9a` | csel x8,x10,x8,eq | `FALL_THROUGH`
<a id="insn-009b015c"></a> `009b015c` | `c8 03 00 b5` | cbnz x8,0x009b01d4 | `CONDITIONAL_JUMP`
<a id="insn-009b0160"></a> `009b0160` | `48 04 80 52` | mov w8,#0x22 | `FALL_THROUGH`
<a id="insn-009b0164"></a> `009b0164` | `ff cb 02 39` | strb wzr,[sp, #0xb2] | `FALL_THROUGH`
<a id="insn-009b0168"></a> `009b0168` | `e8 83 02 39` | strb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009b016c"></a> `009b016c` | `08 c8 ff d0` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-009b0170"></a> `009b0170` | `08 81 0c 91` | add x8,x8,#0x320 | `FALL_THROUGH`
<a id="insn-009b0174"></a> `009b0174` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-009b0178"></a> `009b0178` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-009b017c"></a> `009b017c` | `88 42 00 39` | strb w8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-009b0180"></a> `009b0180` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-009b0184"></a> `009b0184` | `e8 e3 02 91` | add x8,sp,#0xb8 | `FALL_THROUGH`
<a id="insn-009b0188"></a> `009b0188` | `e0 83 02 91` | add x0,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-009b018c"></a> `009b018c` | `42 73 eb 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-009b0190"></a> `009b0190` | `e8 e3 42 39` | ldrb w8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-009b0194"></a> `009b0194` | `ea 27 4c a9` | ldp x10,x9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-009b0198"></a> `009b0198` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-009b019c"></a> `009b019c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-009b01a0"></a> `009b01a0` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009b01a4"></a> `009b01a4` | `01 01 89 9a` | csel x1,x8,x9,eq | `FALL_THROUGH`
<a id="insn-009b01a8"></a> `009b01a8` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-009b01ac"></a> `009b01ac` | `a0 c3 02 d1` | sub x0,x29,#0xb0 | `FALL_THROUGH`
<a id="insn-009b01b0"></a> `009b01b0` | `a8 9f 0a 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-009b01b4"></a> `009b01b4` | `e8 e3 42 39` | ldrb w8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-009b01b8"></a> `009b01b8` | `68 00 00 36` | tbz w8,#0x0,0x009b01c4 | `CONDITIONAL_JUMP`
<a id="insn-009b01bc"></a> `009b01bc` | `e0 67 40 f9` | ldr x0,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-009b01c0"></a> `009b01c0` | `70 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b01c4"></a> `009b01c4` | `e8 83 42 39` | ldrb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009b01c8"></a> `009b01c8` | `68 00 00 36` | tbz w8,#0x0,0x009b01d4 | `CONDITIONAL_JUMP`
<a id="insn-009b01cc"></a> `009b01cc` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009b01d0"></a> `009b01d0` | `6c 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b01d4"></a> `009b01d4` | `20 03 80 52` | mov w0,#0x19 | `FALL_THROUGH`
<a id="insn-009b01d8"></a> `009b01d8` | `62 9f 0a 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-009b01dc"></a> `009b01dc` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-009b01e0"></a> `009b01e0` | `e1 17 c0 3d` | ldr q1,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009b01e4"></a> `009b01e4` | `68 f2 40 f8` | ldur x8,[x19, #0xf] | `FALL_THROUGH`
<a id="insn-009b01e8"></a> `009b01e8` | `a9 03 55 38` | ldurb w9,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b01ec"></a> `009b01ec` | `b9 83 56 b8` | ldur w25,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-009b01f0"></a> `009b01f0` | `e0 5b 00 f9` | str x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009b01f4"></a> `009b01f4` | `e1 2b 80 3d` | str q1,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009b01f8"></a> `009b01f8` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-009b01fc"></a> `009b01fc` | `08 f0 00 f8` | stur x8,[x0, #0xf] | `FALL_THROUGH`
<a id="insn-009b0200"></a> `009b0200` | `1f 5c 00 39` | strb wzr,[x0, #0x17] | `FALL_THROUGH`
<a id="insn-009b0204"></a> `009b0204` | `c9 00 00 37` | tbnz w9,#0x0,0x009b021c | `CONDITIONAL_JUMP`
<a id="insn-009b0208"></a> `009b0208` | `a0 03 d5 3c` | ldur q0,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b020c"></a> `009b020c` | `a8 03 56 f8` | ldur x8,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-009b0210"></a> `009b0210` | `e0 23 80 3d` | str q0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009b0214"></a> `009b0214` | `e8 4b 00 f9` | str x8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009b0218"></a> `009b0218` | `04 00 00 14` | b 0x009b0228 | `UNCONDITIONAL_JUMP`
<a id="insn-009b021c"></a> `009b021c` | `a2 87 75 a9` | ldp x2,x1,[x29, #-0xa8] | `FALL_THROUGH`
<a id="insn-009b0220"></a> `009b0220` | `e0 03 02 91` | add x0,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009b0224"></a> `009b0224` | `4f 2e ea 97` | bl 0x0043bb60 | `UNCONDITIONAL_CALL`
<a id="insn-009b0228"></a> `009b0228` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-009b022c"></a> `009b022c` | `80 23 00 91` | add x0,x28,#0x8 | `FALL_THROUGH`
<a id="insn-009b0230"></a> `009b0230` | `19 73 eb 97` | bl 0x0048ce94 | `UNCONDITIONAL_CALL`
<a id="insn-009b0234"></a> `009b0234` | `e8 e3 02 91` | add x8,sp,#0xb8 | `FALL_THROUGH`
<a id="insn-009b0238"></a> `009b0238` | `e0 83 02 91` | add x0,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-009b023c"></a> `009b023c` | `e2 03 02 91` | add x2,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009b0240"></a> `009b0240` | `e3 a3 01 91` | add x3,sp,#0x68 | `FALL_THROUGH`
<a id="insn-009b0244"></a> `009b0244` | `e1 03 19 2a` | mov w1,w25 | `FALL_THROUGH`
<a id="insn-009b0248"></a> `009b0248` | `e1 e5 f5 97` | bl 0x007299cc | `UNCONDITIONAL_CALL`
<a id="insn-009b024c"></a> `009b024c` | `e1 e3 02 91` | add x1,sp,#0xb8 | `FALL_THROUGH`
<a id="insn-009b0250"></a> `009b0250` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009b0254"></a> `009b0254` | `ae 8a eb 97` | bl 0x00492d0c | `UNCONDITIONAL_CALL`
<a id="insn-009b0258"></a> `009b0258` | `e8 e3 42 39` | ldrb w8,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-009b025c"></a> `009b025c` | `28 03 00 37` | tbnz w8,#0x0,0x009b02c0 | `CONDITIONAL_JUMP`
<a id="insn-009b0260"></a> `009b0260` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-009b0264"></a> `009b0264` | `68 03 00 37` | tbnz w8,#0x0,0x009b02d0 | `CONDITIONAL_JUMP`
<a id="insn-009b0268"></a> `009b0268` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009b026c"></a> `009b026c` | `a8 03 00 37` | tbnz w8,#0x0,0x009b02e0 | `CONDITIONAL_JUMP`
<a id="insn-009b0270"></a> `009b0270` | `e8 83 42 39` | ldrb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009b0274"></a> `009b0274` | `e8 03 00 37` | tbnz w8,#0x0,0x009b02f0 | `CONDITIONAL_JUMP`
<a id="insn-009b0278"></a> `009b0278` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b027c"></a> `009b027c` | `28 04 00 37` | tbnz w8,#0x0,0x009b0300 | `CONDITIONAL_JUMP`
<a id="insn-009b0280"></a> `009b0280` | `b5 83 5a f8` | ldur x21,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b0284"></a> `009b0284` | `75 04 00 b4` | cbz x21,0x009b0310 | `CONDITIONAL_JUMP`
<a id="insn-009b0288"></a> `009b0288` | `a8 03 5b f8` | ldur x8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-009b028c"></a> `009b028c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009b0290"></a> `009b0290` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-009b0294"></a> `009b0294` | `20 05 00 54` | b.eq 0x009b0338 | `CONDITIONAL_JUMP`
<a id="insn-009b0298"></a> `009b0298` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-009b029c"></a> `009b029c` | `04 00 00 14` | b 0x009b02ac | `UNCONDITIONAL_JUMP`
<a id="insn-009b02a0"></a> `009b02a0` | `3f 03 15 eb` | cmp x25,x21 | `FALL_THROUGH`
<a id="insn-009b02a4"></a> `009b02a4` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-009b02a8"></a> `009b02a8` | `60 04 00 54` | b.eq 0x009b0334 | `CONDITIONAL_JUMP`
<a id="insn-009b02ac"></a> `009b02ac` | `29 8f 5e 38` | ldrb w9,[x25, #-0x18]! | `FALL_THROUGH`
<a id="insn-009b02b0"></a> `009b02b0` | `89 ff 07 36` | tbz w9,#0x0,0x009b02a0 | `CONDITIONAL_JUMP`
<a id="insn-009b02b4"></a> `009b02b4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-009b02b8"></a> `009b02b8` | `32 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b02bc"></a> `009b02bc` | `f9 ff ff 17` | b 0x009b02a0 | `UNCONDITIONAL_JUMP`
<a id="insn-009b02c0"></a> `009b02c0` | `e0 67 40 f9` | ldr x0,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-009b02c4"></a> `009b02c4` | `2f 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b02c8"></a> `009b02c8` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-009b02cc"></a> `009b02cc` | `e8 fc 07 36` | tbz w8,#0x0,0x009b0268 | `CONDITIONAL_JUMP`
<a id="insn-009b02d0"></a> `009b02d0` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-009b02d4"></a> `009b02d4` | `2b 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b02d8"></a> `009b02d8` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009b02dc"></a> `009b02dc` | `a8 fc 07 36` | tbz w8,#0x0,0x009b0270 | `CONDITIONAL_JUMP`
<a id="insn-009b02e0"></a> `009b02e0` | `e0 4b 40 f9` | ldr x0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009b02e4"></a> `009b02e4` | `27 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b02e8"></a> `009b02e8` | `e8 83 42 39` | ldrb w8,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009b02ec"></a> `009b02ec` | `68 fc 07 36` | tbz w8,#0x0,0x009b0278 | `CONDITIONAL_JUMP`
<a id="insn-009b02f0"></a> `009b02f0` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009b02f4"></a> `009b02f4` | `23 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b02f8"></a> `009b02f8` | `a8 03 55 38` | ldurb w8,[x29, #-0xb0] | `FALL_THROUGH`
<a id="insn-009b02fc"></a> `009b02fc` | `28 fc 07 36` | tbz w8,#0x0,0x009b0280 | `CONDITIONAL_JUMP`
<a id="insn-009b0300"></a> `009b0300` | `a0 03 56 f8` | ldur x0,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-009b0304"></a> `009b0304` | `1f 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0308"></a> `009b0308` | `b5 83 5a f8` | ldur x21,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b030c"></a> `009b030c` | `f5 fb ff b5` | cbnz x21,0x009b0288 | `CONDITIONAL_JUMP`
<a id="insn-009b0310"></a> `009b0310` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-009b0314"></a> `009b0314` | `60 00 00 b4` | cbz x0,0x009b0320 | `CONDITIONAL_JUMP`
<a id="insn-009b0318"></a> `009b0318` | `a0 83 19 f8` | stur x0,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-009b031c"></a> `009b031c` | `19 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0320"></a> `009b0320` | `a8 03 57 38` | ldurb w8,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-009b0324"></a> `009b0324` | `a8 ea 07 36` | tbz w8,#0x0,0x009b0078 | `CONDITIONAL_JUMP`
<a id="insn-009b0328"></a> `009b0328` | `a0 03 58 f8` | ldur x0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-009b032c"></a> `009b032c` | `15 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0330"></a> `009b0330` | `52 ff ff 17` | b 0x009b0078 | `UNCONDITIONAL_JUMP`
<a id="insn-009b0334"></a> `009b0334` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-009b0338"></a> `009b0338` | `b5 03 1b f8` | stur x21,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-009b033c"></a> `009b033c` | `11 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0340"></a> `009b0340` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-009b0344"></a> `009b0344` | `a0 fe ff b5` | cbnz x0,0x009b0318 | `CONDITIONAL_JUMP`
<a id="insn-009b0348"></a> `009b0348` | `f6 ff ff 17` | b 0x009b0320 | `UNCONDITIONAL_JUMP`
<a id="insn-009b034c"></a> `009b034c` | `b7 03 5c f8` | ldur x23,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-009b0350"></a> `009b0350` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009b0354"></a> `009b0354` | `d7 00 00 b4` | cbz x23,0x009b036c | `CONDITIONAL_JUMP`
<a id="insn-009b0358"></a> `009b0358` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-009b035c"></a> `009b035c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-009b0360"></a> `009b0360` | `fb e6 fa 97` | bl 0x00869f4c | `UNCONDITIONAL_CALL`
<a id="insn-009b0364"></a> `009b0364` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-009b0368"></a> `009b0368` | `06 9f 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b036c"></a> `009b036c` | `e1 23 40 f9` | ldr x1,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009b0370"></a> `009b0370` | `e2 1b 40 f9` | ldr x2,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009b0374"></a> `009b0374` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-009b0378"></a> `009b0378` | `78 00 00 94` | bl 0x009b0558 | `UNCONDITIONAL_CALL`
<a id="insn-009b037c"></a> `009b037c` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-009b0380"></a> `009b0380` | `f4 1f 40 f9` | ldr x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-009b0384"></a> `009b0384` | `60 00 00 b4` | cbz x0,0x009b0390 | `CONDITIONAL_JUMP`
<a id="insn-009b0388"></a> `009b0388` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-009b038c"></a> `009b038c` | `fd 9e 0a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-009b0390"></a> `009b0390` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009b0394"></a> `009b0394` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-009b0398"></a> `009b0398` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009b039c"></a> `009b039c` | `41 0c 00 54` | b.ne 0x009b0524 | `CONDITIONAL_JUMP`
<a id="insn-009b03a0"></a> `009b03a0` | `f4 4f 5d a9` | ldp x20,x19,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-009b03a4"></a> `009b03a4` | `f6 57 5c a9` | ldp x22,x21,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-009b03a8"></a> `009b03a8` | `f8 5f 5b a9` | ldp x24,x23,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-009b03ac"></a> `009b03ac` | `fa 67 5a a9` | ldp x26,x25,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-009b03b0"></a> `009b03b0` | `fc 6f 59 a9` | ldp x28,x27,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009b03b4"></a> `009b03b4` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009b03b8"></a> `009b03b8` | `ff 83 07 91` | add sp,sp,#0x1e0 | `FALL_THROUGH`
<a id="insn-009b03bc"></a> `009b03bc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009b0524"></a> `009b0524` | `a3 9e 0a 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009afefc`](#insn-009afefc) 範囲 `[['009afefc', '009aff13']]`
  - `FALL_THROUGH` [`009aff10`](#insn-009aff10) → [`009aff14`](#insn-009aff14)
- ブロック [`009aff14`](#insn-009aff14) 範囲 `[['009aff14', '009aff1b']]`
  - `FALL_THROUGH` [`009aff18`](#insn-009aff18) → [`009aff1c`](#insn-009aff1c)
- ブロック [`009aff1c`](#insn-009aff1c) 範囲 `[['009aff1c', '009aff3f']]`
  - `FALL_THROUGH` [`009aff3c`](#insn-009aff3c) → [`009aff40`](#insn-009aff40)
- ブロック [`009aff40`](#insn-009aff40) 範囲 `[['009aff40', '009aff47']]`
  - `CONDITIONAL_JUMP` [`009aff44`](#insn-009aff44) → [`009b0384`](#insn-009b0384)
  - `FALL_THROUGH` [`009aff44`](#insn-009aff44) → [`009aff48`](#insn-009aff48)
- ブロック [`009aff48`](#insn-009aff48) 範囲 `[['009aff48', '009aff57']]`
  - `CONDITIONAL_JUMP` [`009aff54`](#insn-009aff54) → [`009b0384`](#insn-009b0384)
  - `FALL_THROUGH` [`009aff54`](#insn-009aff54) → [`009aff58`](#insn-009aff58)
- ブロック [`009aff58`](#insn-009aff58) 範囲 `[['009aff58', '009affa3']]`
  - `FALL_THROUGH` [`009affa0`](#insn-009affa0) → [`009affa4`](#insn-009affa4)
- ブロック [`009affa4`](#insn-009affa4) 範囲 `[['009affa4', '009affdf']]`
  - `FALL_THROUGH` [`009affdc`](#insn-009affdc) → [`009affe0`](#insn-009affe0)
- ブロック [`009affe0`](#insn-009affe0) 範囲 `[['009affe0', '009affeb']]`
  - `FALL_THROUGH` [`009affe8`](#insn-009affe8) → [`009affec`](#insn-009affec)
- ブロック [`009affec`](#insn-009affec) 範囲 `[['009affec', '009afff3']]`
  - `CONDITIONAL_JUMP` [`009afff0`](#insn-009afff0) → [`009afffc`](#insn-009afffc)
  - `FALL_THROUGH` [`009afff0`](#insn-009afff0) → [`009afff4`](#insn-009afff4)
- ブロック [`009afff4`](#insn-009afff4) 範囲 `[['009afff4', '009afffb']]`
  - `FALL_THROUGH` [`009afff8`](#insn-009afff8) → [`009afffc`](#insn-009afffc)
- ブロック [`009afffc`](#insn-009afffc) 範囲 `[['009afffc', '009b000f']]`
  - `CONDITIONAL_JUMP` [`009b000c`](#insn-009b000c) → [`009b0018`](#insn-009b0018)
  - `FALL_THROUGH` [`009b000c`](#insn-009b000c) → [`009b0010`](#insn-009b0010)
- ブロック [`009b0010`](#insn-009b0010) 範囲 `[['009b0010', '009b0017']]`
  - `FALL_THROUGH` [`009b0014`](#insn-009b0014) → [`009b0018`](#insn-009b0018)
- ブロック [`009b0018`](#insn-009b0018) 範囲 `[['009b0018', '009b0033']]`
  - `CONDITIONAL_JUMP` [`009b0030`](#insn-009b0030) → [`009b0354`](#insn-009b0354)
  - `FALL_THROUGH` [`009b0030`](#insn-009b0030) → [`009b0034`](#insn-009b0034)
- ブロック [`009b0034`](#insn-009b0034) 範囲 `[['009b0034', '009b003b']]`
  - `FALL_THROUGH` [`009b0038`](#insn-009b0038) → [`009b003c`](#insn-009b003c)
- ブロック [`009b003c`](#insn-009b003c) 範囲 `[['009b003c', '009b0053']]`
  - `FALL_THROUGH` [`009b0050`](#insn-009b0050) → [`009b0054`](#insn-009b0054)
- ブロック [`009b0054`](#insn-009b0054) 範囲 `[['009b0054', '009b0077']]`
  - `UNCONDITIONAL_JUMP` [`009b0074`](#insn-009b0074) → [`009b0084`](#insn-009b0084)
- ブロック [`009b0078`](#insn-009b0078) 範囲 `[['009b0078', '009b0083']]`
  - `CONDITIONAL_JUMP` [`009b0080`](#insn-009b0080) → [`009b034c`](#insn-009b034c)
  - `FALL_THROUGH` [`009b0080`](#insn-009b0080) → [`009b0084`](#insn-009b0084)
- ブロック [`009b0084`](#insn-009b0084) 範囲 `[['009b0084', '009b009b']]`
  - `FALL_THROUGH` [`009b0098`](#insn-009b0098) → [`009b009c`](#insn-009b009c)
- ブロック [`009b009c`](#insn-009b009c) 範囲 `[['009b009c', '009b00a3']]`
  - `CONDITIONAL_JUMP` [`009b00a0`](#insn-009b00a0) → [`009b0148`](#insn-009b0148)
  - `FALL_THROUGH` [`009b00a0`](#insn-009b00a0) → [`009b00a4`](#insn-009b00a4)
- ブロック [`009b00a4`](#insn-009b00a4) 範囲 `[['009b00a4', '009b00db']]`
  - `CONDITIONAL_JUMP` [`009b00d8`](#insn-009b00d8) → [`009b013c`](#insn-009b013c)
  - `FALL_THROUGH` [`009b00d8`](#insn-009b00d8) → [`009b00dc`](#insn-009b00dc)
- ブロック [`009b00dc`](#insn-009b00dc) 範囲 `[['009b00dc', '009b00e3']]`
  - `FALL_THROUGH` [`009b00e0`](#insn-009b00e0) → [`009b00e4`](#insn-009b00e4)
- ブロック [`009b00e4`](#insn-009b00e4) 範囲 `[['009b00e4', '009b0107']]`
  - `FALL_THROUGH` [`009b0104`](#insn-009b0104) → [`009b0108`](#insn-009b0108)
- ブロック [`009b0108`](#insn-009b0108) 範囲 `[['009b0108', '009b011f']]`
  - `FALL_THROUGH` [`009b011c`](#insn-009b011c) → [`009b0120`](#insn-009b0120)
- ブロック [`009b0120`](#insn-009b0120) 範囲 `[['009b0120', '009b0127']]`
  - `FALL_THROUGH` [`009b0124`](#insn-009b0124) → [`009b0128`](#insn-009b0128)
- ブロック [`009b0128`](#insn-009b0128) 範囲 `[['009b0128', '009b012f']]`
  - `FALL_THROUGH` [`009b012c`](#insn-009b012c) → [`009b0130`](#insn-009b0130)
- ブロック [`009b0130`](#insn-009b0130) 範囲 `[['009b0130', '009b0133']]`
  - `FALL_THROUGH` [`009b0130`](#insn-009b0130) → [`009b0134`](#insn-009b0134)
- ブロック [`009b0134`](#insn-009b0134) 範囲 `[['009b0134', '009b013b']]`
  - `CONDITIONAL_JUMP` [`009b0138`](#insn-009b0138) → [`009b00e4`](#insn-009b00e4)
  - `FALL_THROUGH` [`009b0138`](#insn-009b0138) → [`009b013c`](#insn-009b013c)
- ブロック [`009b013c`](#insn-009b013c) 範囲 `[['009b013c', '009b013f']]`
  - `FALL_THROUGH` [`009b013c`](#insn-009b013c) → [`009b0140`](#insn-009b0140)
- ブロック [`009b0140`](#insn-009b0140) 範囲 `[['009b0140', '009b0147']]`
  - `UNCONDITIONAL_JUMP` [`009b0144`](#insn-009b0144) → [`009b0150`](#insn-009b0150)
- ブロック [`009b0148`](#insn-009b0148) 範囲 `[['009b0148', '009b014f']]`
  - `FALL_THROUGH` [`009b014c`](#insn-009b014c) → [`009b0150`](#insn-009b0150)
- ブロック [`009b0150`](#insn-009b0150) 範囲 `[['009b0150', '009b0153']]`
  - `FALL_THROUGH` [`009b0150`](#insn-009b0150) → [`009b0154`](#insn-009b0154)
- ブロック [`009b0154`](#insn-009b0154) 範囲 `[['009b0154', '009b015b']]`
  - `FALL_THROUGH` [`009b0158`](#insn-009b0158) → [`009b015c`](#insn-009b015c)
- ブロック [`009b015c`](#insn-009b015c) 範囲 `[['009b015c', '009b015f']]`
  - `CONDITIONAL_JUMP` [`009b015c`](#insn-009b015c) → [`009b01d4`](#insn-009b01d4)
  - `FALL_THROUGH` [`009b015c`](#insn-009b015c) → [`009b0160`](#insn-009b0160)
- ブロック [`009b0160`](#insn-009b0160) 範囲 `[['009b0160', '009b0163']]`
  - `FALL_THROUGH` [`009b0160`](#insn-009b0160) → [`009b0164`](#insn-009b0164)
- ブロック [`009b0164`](#insn-009b0164) 範囲 `[['009b0164', '009b0167']]`
  - `FALL_THROUGH` [`009b0164`](#insn-009b0164) → [`009b0168`](#insn-009b0168)
- ブロック [`009b0168`](#insn-009b0168) 範囲 `[['009b0168', '009b016b']]`
  - `FALL_THROUGH` [`009b0168`](#insn-009b0168) → [`009b016c`](#insn-009b016c)
- ブロック [`009b016c`](#insn-009b016c) 範囲 `[['009b016c', '009b0173']]`
  - `FALL_THROUGH` [`009b0170`](#insn-009b0170) → [`009b0174`](#insn-009b0174)
- ブロック [`009b0174`](#insn-009b0174) 範囲 `[['009b0174', '009b017b']]`
  - `FALL_THROUGH` [`009b0178`](#insn-009b0178) → [`009b017c`](#insn-009b017c)
- ブロック [`009b017c`](#insn-009b017c) 範囲 `[['009b017c', '009b017f']]`
  - `FALL_THROUGH` [`009b017c`](#insn-009b017c) → [`009b0180`](#insn-009b0180)
- ブロック [`009b0180`](#insn-009b0180) 範囲 `[['009b0180', '009b0183']]`
  - `FALL_THROUGH` [`009b0180`](#insn-009b0180) → [`009b0184`](#insn-009b0184)
- ブロック [`009b0184`](#insn-009b0184) 範囲 `[['009b0184', '009b0187']]`
  - `FALL_THROUGH` [`009b0184`](#insn-009b0184) → [`009b0188`](#insn-009b0188)
- ブロック [`009b0188`](#insn-009b0188) 範囲 `[['009b0188', '009b018f']]`
  - `FALL_THROUGH` [`009b018c`](#insn-009b018c) → [`009b0190`](#insn-009b0190)
- ブロック [`009b0190`](#insn-009b0190) 範囲 `[['009b0190', '009b019f']]`
  - `FALL_THROUGH` [`009b019c`](#insn-009b019c) → [`009b01a0`](#insn-009b01a0)
- ブロック [`009b01a0`](#insn-009b01a0) 範囲 `[['009b01a0', '009b01a7']]`
  - `FALL_THROUGH` [`009b01a4`](#insn-009b01a4) → [`009b01a8`](#insn-009b01a8)
- ブロック [`009b01a8`](#insn-009b01a8) 範囲 `[['009b01a8', '009b01bb']]`
  - `CONDITIONAL_JUMP` [`009b01b8`](#insn-009b01b8) → [`009b01c4`](#insn-009b01c4)
  - `FALL_THROUGH` [`009b01b8`](#insn-009b01b8) → [`009b01bc`](#insn-009b01bc)
- ブロック [`009b01bc`](#insn-009b01bc) 範囲 `[['009b01bc', '009b01c3']]`
  - `FALL_THROUGH` [`009b01c0`](#insn-009b01c0) → [`009b01c4`](#insn-009b01c4)
- ブロック [`009b01c4`](#insn-009b01c4) 範囲 `[['009b01c4', '009b01cb']]`
  - `CONDITIONAL_JUMP` [`009b01c8`](#insn-009b01c8) → [`009b01d4`](#insn-009b01d4)
  - `FALL_THROUGH` [`009b01c8`](#insn-009b01c8) → [`009b01cc`](#insn-009b01cc)
- ブロック [`009b01cc`](#insn-009b01cc) 範囲 `[['009b01cc', '009b01d3']]`
  - `FALL_THROUGH` [`009b01d0`](#insn-009b01d0) → [`009b01d4`](#insn-009b01d4)
- ブロック [`009b01d4`](#insn-009b01d4) 範囲 `[['009b01d4', '009b01f7']]`
  - `FALL_THROUGH` [`009b01f4`](#insn-009b01f4) → [`009b01f8`](#insn-009b01f8)
- ブロック [`009b01f8`](#insn-009b01f8) 範囲 `[['009b01f8', '009b0207']]`
  - `CONDITIONAL_JUMP` [`009b0204`](#insn-009b0204) → [`009b021c`](#insn-009b021c)
  - `FALL_THROUGH` [`009b0204`](#insn-009b0204) → [`009b0208`](#insn-009b0208)
- ブロック [`009b0208`](#insn-009b0208) 範囲 `[['009b0208', '009b021b']]`
  - `UNCONDITIONAL_JUMP` [`009b0218`](#insn-009b0218) → [`009b0228`](#insn-009b0228)
- ブロック [`009b021c`](#insn-009b021c) 範囲 `[['009b021c', '009b0227']]`
  - `FALL_THROUGH` [`009b0224`](#insn-009b0224) → [`009b0228`](#insn-009b0228)
- ブロック [`009b0228`](#insn-009b0228) 範囲 `[['009b0228', '009b025f']]`
  - `CONDITIONAL_JUMP` [`009b025c`](#insn-009b025c) → [`009b02c0`](#insn-009b02c0)
  - `FALL_THROUGH` [`009b025c`](#insn-009b025c) → [`009b0260`](#insn-009b0260)
- ブロック [`009b0260`](#insn-009b0260) 範囲 `[['009b0260', '009b0267']]`
  - `CONDITIONAL_JUMP` [`009b0264`](#insn-009b0264) → [`009b02d0`](#insn-009b02d0)
  - `FALL_THROUGH` [`009b0264`](#insn-009b0264) → [`009b0268`](#insn-009b0268)
- ブロック [`009b0268`](#insn-009b0268) 範囲 `[['009b0268', '009b026f']]`
  - `CONDITIONAL_JUMP` [`009b026c`](#insn-009b026c) → [`009b02e0`](#insn-009b02e0)
  - `FALL_THROUGH` [`009b026c`](#insn-009b026c) → [`009b0270`](#insn-009b0270)
- ブロック [`009b0270`](#insn-009b0270) 範囲 `[['009b0270', '009b0277']]`
  - `CONDITIONAL_JUMP` [`009b0274`](#insn-009b0274) → [`009b02f0`](#insn-009b02f0)
  - `FALL_THROUGH` [`009b0274`](#insn-009b0274) → [`009b0278`](#insn-009b0278)
- ブロック [`009b0278`](#insn-009b0278) 範囲 `[['009b0278', '009b027f']]`
  - `CONDITIONAL_JUMP` [`009b027c`](#insn-009b027c) → [`009b0300`](#insn-009b0300)
  - `FALL_THROUGH` [`009b027c`](#insn-009b027c) → [`009b0280`](#insn-009b0280)
- ブロック [`009b0280`](#insn-009b0280) 範囲 `[['009b0280', '009b0287']]`
  - `CONDITIONAL_JUMP` [`009b0284`](#insn-009b0284) → [`009b0310`](#insn-009b0310)
  - `FALL_THROUGH` [`009b0284`](#insn-009b0284) → [`009b0288`](#insn-009b0288)
- ブロック [`009b0288`](#insn-009b0288) 範囲 `[['009b0288', '009b0297']]`
  - `CONDITIONAL_JUMP` [`009b0294`](#insn-009b0294) → [`009b0338`](#insn-009b0338)
  - `FALL_THROUGH` [`009b0294`](#insn-009b0294) → [`009b0298`](#insn-009b0298)
- ブロック [`009b0298`](#insn-009b0298) 範囲 `[['009b0298', '009b029f']]`
  - `UNCONDITIONAL_JUMP` [`009b029c`](#insn-009b029c) → [`009b02ac`](#insn-009b02ac)
- ブロック [`009b02a0`](#insn-009b02a0) 範囲 `[['009b02a0', '009b02ab']]`
  - `CONDITIONAL_JUMP` [`009b02a8`](#insn-009b02a8) → [`009b0334`](#insn-009b0334)
  - `FALL_THROUGH` [`009b02a8`](#insn-009b02a8) → [`009b02ac`](#insn-009b02ac)
- ブロック [`009b02ac`](#insn-009b02ac) 範囲 `[['009b02ac', '009b02b3']]`
  - `CONDITIONAL_JUMP` [`009b02b0`](#insn-009b02b0) → [`009b02a0`](#insn-009b02a0)
  - `FALL_THROUGH` [`009b02b0`](#insn-009b02b0) → [`009b02b4`](#insn-009b02b4)
- ブロック [`009b02b4`](#insn-009b02b4) 範囲 `[['009b02b4', '009b02bf']]`
  - `UNCONDITIONAL_JUMP` [`009b02bc`](#insn-009b02bc) → [`009b02a0`](#insn-009b02a0)
- ブロック [`009b02c0`](#insn-009b02c0) 範囲 `[['009b02c0', '009b02cf']]`
  - `CONDITIONAL_JUMP` [`009b02cc`](#insn-009b02cc) → [`009b0268`](#insn-009b0268)
  - `FALL_THROUGH` [`009b02cc`](#insn-009b02cc) → [`009b02d0`](#insn-009b02d0)
- ブロック [`009b02d0`](#insn-009b02d0) 範囲 `[['009b02d0', '009b02df']]`
  - `CONDITIONAL_JUMP` [`009b02dc`](#insn-009b02dc) → [`009b0270`](#insn-009b0270)
  - `FALL_THROUGH` [`009b02dc`](#insn-009b02dc) → [`009b02e0`](#insn-009b02e0)
- ブロック [`009b02e0`](#insn-009b02e0) 範囲 `[['009b02e0', '009b02ef']]`
  - `CONDITIONAL_JUMP` [`009b02ec`](#insn-009b02ec) → [`009b0278`](#insn-009b0278)
  - `FALL_THROUGH` [`009b02ec`](#insn-009b02ec) → [`009b02f0`](#insn-009b02f0)
- ブロック [`009b02f0`](#insn-009b02f0) 範囲 `[['009b02f0', '009b02ff']]`
  - `CONDITIONAL_JUMP` [`009b02fc`](#insn-009b02fc) → [`009b0280`](#insn-009b0280)
  - `FALL_THROUGH` [`009b02fc`](#insn-009b02fc) → [`009b0300`](#insn-009b0300)
- ブロック [`009b0300`](#insn-009b0300) 範囲 `[['009b0300', '009b030f']]`
  - `CONDITIONAL_JUMP` [`009b030c`](#insn-009b030c) → [`009b0288`](#insn-009b0288)
  - `FALL_THROUGH` [`009b030c`](#insn-009b030c) → [`009b0310`](#insn-009b0310)
- ブロック [`009b0310`](#insn-009b0310) 範囲 `[['009b0310', '009b0317']]`
  - `CONDITIONAL_JUMP` [`009b0314`](#insn-009b0314) → [`009b0320`](#insn-009b0320)
  - `FALL_THROUGH` [`009b0314`](#insn-009b0314) → [`009b0318`](#insn-009b0318)
- ブロック [`009b0318`](#insn-009b0318) 範囲 `[['009b0318', '009b031f']]`
  - `FALL_THROUGH` [`009b031c`](#insn-009b031c) → [`009b0320`](#insn-009b0320)
- ブロック [`009b0320`](#insn-009b0320) 範囲 `[['009b0320', '009b0327']]`
  - `CONDITIONAL_JUMP` [`009b0324`](#insn-009b0324) → [`009b0078`](#insn-009b0078)
  - `FALL_THROUGH` [`009b0324`](#insn-009b0324) → [`009b0328`](#insn-009b0328)
- ブロック [`009b0328`](#insn-009b0328) 範囲 `[['009b0328', '009b0333']]`
  - `UNCONDITIONAL_JUMP` [`009b0330`](#insn-009b0330) → [`009b0078`](#insn-009b0078)
- ブロック [`009b0334`](#insn-009b0334) 範囲 `[['009b0334', '009b0337']]`
  - `FALL_THROUGH` [`009b0334`](#insn-009b0334) → [`009b0338`](#insn-009b0338)
- ブロック [`009b0338`](#insn-009b0338) 範囲 `[['009b0338', '009b0347']]`
  - `CONDITIONAL_JUMP` [`009b0344`](#insn-009b0344) → [`009b0318`](#insn-009b0318)
  - `FALL_THROUGH` [`009b0344`](#insn-009b0344) → [`009b0348`](#insn-009b0348)
- ブロック [`009b0348`](#insn-009b0348) 範囲 `[['009b0348', '009b034b']]`
  - `UNCONDITIONAL_JUMP` [`009b0348`](#insn-009b0348) → [`009b0320`](#insn-009b0320)
- ブロック [`009b034c`](#insn-009b034c) 範囲 `[['009b034c', '009b0353']]`
  - `FALL_THROUGH` [`009b0350`](#insn-009b0350) → [`009b0354`](#insn-009b0354)
- ブロック [`009b0354`](#insn-009b0354) 範囲 `[['009b0354', '009b0357']]`
  - `CONDITIONAL_JUMP` [`009b0354`](#insn-009b0354) → [`009b036c`](#insn-009b036c)
  - `FALL_THROUGH` [`009b0354`](#insn-009b0354) → [`009b0358`](#insn-009b0358)
- ブロック [`009b0358`](#insn-009b0358) 範囲 `[['009b0358', '009b036b']]`
  - `FALL_THROUGH` [`009b0368`](#insn-009b0368) → [`009b036c`](#insn-009b036c)
- ブロック [`009b036c`](#insn-009b036c) 範囲 `[['009b036c', '009b036f']]`
  - `FALL_THROUGH` [`009b036c`](#insn-009b036c) → [`009b0370`](#insn-009b0370)
- ブロック [`009b0370`](#insn-009b0370) 範囲 `[['009b0370', '009b0383']]`
  - `FALL_THROUGH` [`009b0380`](#insn-009b0380) → [`009b0384`](#insn-009b0384)
- ブロック [`009b0384`](#insn-009b0384) 範囲 `[['009b0384', '009b0387']]`
  - `CONDITIONAL_JUMP` [`009b0384`](#insn-009b0384) → [`009b0390`](#insn-009b0390)
  - `FALL_THROUGH` [`009b0384`](#insn-009b0384) → [`009b0388`](#insn-009b0388)
- ブロック [`009b0388`](#insn-009b0388) 範囲 `[['009b0388', '009b038f']]`
  - `FALL_THROUGH` [`009b038c`](#insn-009b038c) → [`009b0390`](#insn-009b0390)
- ブロック [`009b0390`](#insn-009b0390) 範囲 `[['009b0390', '009b039f']]`
  - `CONDITIONAL_JUMP` [`009b039c`](#insn-009b039c) → [`009b0524`](#insn-009b0524)
  - `FALL_THROUGH` [`009b039c`](#insn-009b039c) → [`009b03a0`](#insn-009b03a0)
- ブロック [`009b03a0`](#insn-009b03a0) 範囲 `[['009b03a0', '009b03bf']]`
- ブロック [`009b0524`](#insn-009b0524) 範囲 `[['009b0524', '009b0527']]`

## 命令位置別の参照

- [`009aff00`](#insn-009aff00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff04`](#insn-009aff04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff08`](#insn-009aff08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff0c`](#insn-009aff0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff10`](#insn-009aff10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff14`](#insn-009aff14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff1c`](#insn-009aff1c) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff30`](#insn-009aff30) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff38`](#insn-009aff38) → [`009ad9d4`](../009ad/009ad9d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ad9d4` · 推定シンボル `None` · 推定型 `None`
- [`009aff3c`](#insn-009aff3c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff44`](#insn-009aff44) → [`009b0384`](#insn-009b0384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff54`](#insn-009aff54) → [`009b0384`](#insn-009b0384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff58`](#insn-009aff58) → [`0048cd38`](../0048c/0048cd38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048cd38` · 推定シンボル `None` · 推定型 `None`
- [`009aff5c`](#insn-009aff5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff70`](#insn-009aff70) → [`009aadfc`](../009aa/009aadfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009aadfc` · 推定シンボル `None` · 推定型 `None`
- [`009aff7c`](#insn-009aff7c) → [`009aae10`](../009aa/009aae10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009aae10` · 推定シンボル `None` · 推定型 `None`
- [`009aff84`](#insn-009aff84) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`009aff90`](#insn-009aff90) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff94`](#insn-009aff94) → `002a4915`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff94`](#insn-009aff94) → `002a4925`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff98`](#insn-009aff98) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aff9c`](#insn-009aff9c) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affa0`](#insn-009affa0) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affa8`](#insn-009affa8) → `002a4935`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affa8`](#insn-009affa8) → `002a4945`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affb0`](#insn-009affb0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affb4`](#insn-009affb4) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affbc`](#insn-009affbc) → `002c3290`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affc0`](#insn-009affc0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affc8`](#insn-009affc8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affd0`](#insn-009affd0) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affdc`](#insn-009affdc) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affe0`](#insn-009affe0) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affe4`](#insn-009affe4) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009affe8`](#insn-009affe8) → [`008ae85c`](../008ae/008ae85c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ae85c` · 推定シンボル `None` · 推定型 `None`
- [`009affec`](#insn-009affec) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009afff0`](#insn-009afff0) → [`009afffc`](#insn-009afffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009afff4`](#insn-009afff4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009afff8`](#insn-009afff8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0004`](#insn-009b0004) → [`00492d0c`](../00492/00492d0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492d0c` · 推定シンボル `None` · 推定型 `None`
- [`009b0008`](#insn-009b0008) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b000c`](#insn-009b000c) → [`009b0018`](#insn-009b0018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0010`](#insn-009b0010) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0014`](#insn-009b0014) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0020`](#insn-009b0020) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0024`](#insn-009b0024) → [`009aae24`](../009aa/009aae24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009aae24` · 推定シンボル `None` · 推定型 `None`
- [`009b0028`](#insn-009b0028) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0030`](#insn-009b0030) → [`009b0354`](#insn-009b0354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0048`](#insn-009b0048) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b004c`](#insn-009b004c) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0058`](#insn-009b0058) → `002c2490`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0070`](#insn-009b0070) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0074`](#insn-009b0074) → [`009b0084`](#insn-009b0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0080`](#insn-009b0080) → [`009b034c`](#insn-009b034c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b008c`](#insn-009b008c) → [`0074a82c`](../0074a/0074a82c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0074a82c` · 推定シンボル `None` · 推定型 `None`
- [`009b0090`](#insn-009b0090) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0094`](#insn-009b0094) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0098`](#insn-009b0098) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00a0`](#insn-009b00a0) → [`009b0148`](#insn-009b0148) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00c0`](#insn-009b00c0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`009b00c4`](#insn-009b00c4) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00d8`](#insn-009b00d8) → [`009b013c`](#insn-009b013c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00e8`](#insn-009b00e8) → `002b6881`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b00ec`](#insn-009b00ec) → [`00c58040`](../00c58/00c58040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58040` · 推定シンボル `None` · 推定型 `None`
- [`009b00f0`](#insn-009b00f0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0118`](#insn-009b0118) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`009b011c`](#insn-009b011c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0138`](#insn-009b0138) → [`009b00e4`](#insn-009b00e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b013c`](#insn-009b013c) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0140`](#insn-009b0140) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0144`](#insn-009b0144) → [`009b0150`](#insn-009b0150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b015c`](#insn-009b015c) → [`009b01d4`](#insn-009b01d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0164`](#insn-009b0164) → `Stack[-0x12e]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0168`](#insn-009b0168) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0174`](#insn-009b0174) → `002b2320`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009b018c`](#insn-009b018c) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`009b0190`](#insn-009b0190) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0194`](#insn-009b0194) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01a0`](#insn-009b01a0) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01b0`](#insn-009b01b0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`009b01b4`](#insn-009b01b4) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01b8`](#insn-009b01b8) → [`009b01c4`](#insn-009b01c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01bc`](#insn-009b01bc) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01c0`](#insn-009b01c0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b01c4`](#insn-009b01c4) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01c8`](#insn-009b01c8) → [`009b01d4`](#insn-009b01d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01cc`](#insn-009b01cc) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01d0`](#insn-009b01d0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b01d8`](#insn-009b01d8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`009b01dc`](#insn-009b01dc) → `002b2332`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009b01e0`](#insn-009b01e0) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01e4`](#insn-009b01e4) → `002b2341`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009b01e8`](#insn-009b01e8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01ec`](#insn-009b01ec) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01f0`](#insn-009b01f0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b01f4`](#insn-009b01f4) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0204`](#insn-009b0204) → [`009b021c`](#insn-009b021c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0208`](#insn-009b0208) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b020c`](#insn-009b020c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0210`](#insn-009b0210) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0214`](#insn-009b0214) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0218`](#insn-009b0218) → [`009b0228`](#insn-009b0228) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b021c`](#insn-009b021c) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0224`](#insn-009b0224) → [`0043bb60`](../0043b/0043bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb60` · 推定シンボル `None` · 推定型 `None`
- [`009b0230`](#insn-009b0230) → [`0048ce94`](../0048c/0048ce94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce94` · 推定シンボル `None` · 推定型 `None`
- [`009b0248`](#insn-009b0248) → [`007299cc`](../00729/007299cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007299cc` · 推定シンボル `None` · 推定型 `None`
- [`009b0254`](#insn-009b0254) → [`00492d0c`](../00492/00492d0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492d0c` · 推定シンボル `None` · 推定型 `None`
- [`009b0258`](#insn-009b0258) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b025c`](#insn-009b025c) → [`009b02c0`](#insn-009b02c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0260`](#insn-009b0260) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0264`](#insn-009b0264) → [`009b02d0`](#insn-009b02d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0268`](#insn-009b0268) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b026c`](#insn-009b026c) → [`009b02e0`](#insn-009b02e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0270`](#insn-009b0270) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0274`](#insn-009b0274) → [`009b02f0`](#insn-009b02f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0278`](#insn-009b0278) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b027c`](#insn-009b027c) → [`009b0300`](#insn-009b0300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0280`](#insn-009b0280) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0284`](#insn-009b0284) → [`009b0310`](#insn-009b0310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0288`](#insn-009b0288) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0294`](#insn-009b0294) → [`009b0338`](#insn-009b0338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b029c`](#insn-009b029c) → [`009b02ac`](#insn-009b02ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02a8`](#insn-009b02a8) → [`009b0334`](#insn-009b0334) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02b0`](#insn-009b02b0) → [`009b02a0`](#insn-009b02a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02b8`](#insn-009b02b8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b02bc`](#insn-009b02bc) → [`009b02a0`](#insn-009b02a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02c0`](#insn-009b02c0) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02c4`](#insn-009b02c4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b02c8`](#insn-009b02c8) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02cc`](#insn-009b02cc) → [`009b0268`](#insn-009b0268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02d0`](#insn-009b02d0) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02d4`](#insn-009b02d4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b02d8`](#insn-009b02d8) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02dc`](#insn-009b02dc) → [`009b0270`](#insn-009b0270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02e0`](#insn-009b02e0) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02e4`](#insn-009b02e4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b02e8`](#insn-009b02e8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02ec`](#insn-009b02ec) → [`009b0278`](#insn-009b0278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02f0`](#insn-009b02f0) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02f4`](#insn-009b02f4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b02f8`](#insn-009b02f8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b02fc`](#insn-009b02fc) → [`009b0280`](#insn-009b0280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0300`](#insn-009b0300) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0304`](#insn-009b0304) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0308`](#insn-009b0308) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b030c`](#insn-009b030c) → [`009b0288`](#insn-009b0288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0310`](#insn-009b0310) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0314`](#insn-009b0314) → [`009b0320`](#insn-009b0320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0318`](#insn-009b0318) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b031c`](#insn-009b031c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0320`](#insn-009b0320) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0324`](#insn-009b0324) → [`009b0078`](#insn-009b0078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0328`](#insn-009b0328) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b032c`](#insn-009b032c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0330`](#insn-009b0330) → [`009b0078`](#insn-009b0078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0334`](#insn-009b0334) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0338`](#insn-009b0338) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b033c`](#insn-009b033c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0340`](#insn-009b0340) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0344`](#insn-009b0344) → [`009b0318`](#insn-009b0318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0348`](#insn-009b0348) → [`009b0320`](#insn-009b0320) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b034c`](#insn-009b034c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0350`](#insn-009b0350) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0354`](#insn-009b0354) → [`009b036c`](#insn-009b036c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0360`](#insn-009b0360) → [`00869f4c`](../00869/00869f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00869f4c` · 推定シンボル `None` · 推定型 `None`
- [`009b0364`](#insn-009b0364) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0368`](#insn-009b0368) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b036c`](#insn-009b036c) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0370`](#insn-009b0370) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0378`](#insn-009b0378) → [`009b0558`](../009b0/009b0558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b0558` · 推定シンボル `None` · 推定型 `None`
- [`009b037c`](#insn-009b037c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0380`](#insn-009b0380) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0384`](#insn-009b0384) → [`009b0390`](#insn-009b0390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0388`](#insn-009b0388) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b038c`](#insn-009b038c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`009b0394`](#insn-009b0394) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b039c`](#insn-009b039c) → [`009b0524`](#insn-009b0524) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03a0`](#insn-009b03a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03a4`](#insn-009b03a4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03a8`](#insn-009b03a8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03ac`](#insn-009b03ac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03b0`](#insn-009b03b0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b03b4`](#insn-009b03b4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009b0524`](#insn-009b0524) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009aff00`](#insn-009aff00)

~~~json
{
  "source": "009aff00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff04`](#insn-009aff04)

~~~json
{
  "source": "009aff04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff08`](#insn-009aff08)

~~~json
{
  "source": "009aff08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff0c`](#insn-009aff0c)

~~~json
{
  "source": "009aff0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff10`](#insn-009aff10)

~~~json
{
  "source": "009aff10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff14`](#insn-009aff14)

~~~json
{
  "source": "009aff14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff1c`](#insn-009aff1c)

~~~json
{
  "source": "009aff1c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff30`](#insn-009aff30)

~~~json
{
  "source": "009aff30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff38`](#insn-009aff38)

~~~json
{
  "source": "009aff38",
  "target": "009ad9d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aff3c`](#insn-009aff3c)

~~~json
{
  "source": "009aff3c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff44`](#insn-009aff44)

~~~json
{
  "source": "009aff44",
  "target": "009b0384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff54`](#insn-009aff54)

~~~json
{
  "source": "009aff54",
  "target": "009b0384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff58`](#insn-009aff58)

~~~json
{
  "source": "009aff58",
  "target": "0048cd38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aff5c`](#insn-009aff5c)

~~~json
{
  "source": "009aff5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff70`](#insn-009aff70)

~~~json
{
  "source": "009aff70",
  "target": "009aadfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aff7c`](#insn-009aff7c)

~~~json
{
  "source": "009aff7c",
  "target": "009aae10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aff84`](#insn-009aff84)

~~~json
{
  "source": "009aff84",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aff90`](#insn-009aff90)

~~~json
{
  "source": "009aff90",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff94`](#insn-009aff94)

~~~json
{
  "source": "009aff94",
  "target": "002a4915",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff94`](#insn-009aff94)

~~~json
{
  "source": "009aff94",
  "target": "002a4925",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff98`](#insn-009aff98)

~~~json
{
  "source": "009aff98",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aff9c`](#insn-009aff9c)

~~~json
{
  "source": "009aff9c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affa0`](#insn-009affa0)

~~~json
{
  "source": "009affa0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affa8`](#insn-009affa8)

~~~json
{
  "source": "009affa8",
  "target": "002a4935",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affa8`](#insn-009affa8)

~~~json
{
  "source": "009affa8",
  "target": "002a4945",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affb0`](#insn-009affb0)

~~~json
{
  "source": "009affb0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affb4`](#insn-009affb4)

~~~json
{
  "source": "009affb4",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affbc`](#insn-009affbc)

~~~json
{
  "source": "009affbc",
  "target": "002c3290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affc0`](#insn-009affc0)

~~~json
{
  "source": "009affc0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affc8`](#insn-009affc8)

~~~json
{
  "source": "009affc8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affd0`](#insn-009affd0)

~~~json
{
  "source": "009affd0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affdc`](#insn-009affdc)

~~~json
{
  "source": "009affdc",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affe0`](#insn-009affe0)

~~~json
{
  "source": "009affe0",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affe4`](#insn-009affe4)

~~~json
{
  "source": "009affe4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009affe8`](#insn-009affe8)

~~~json
{
  "source": "009affe8",
  "target": "008ae85c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009affec`](#insn-009affec)

~~~json
{
  "source": "009affec",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009afff0`](#insn-009afff0)

~~~json
{
  "source": "009afff0",
  "target": "009afffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009afff4`](#insn-009afff4)

~~~json
{
  "source": "009afff4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009afff8`](#insn-009afff8)

~~~json
{
  "source": "009afff8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0004`](#insn-009b0004)

~~~json
{
  "source": "009b0004",
  "target": "00492d0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0008`](#insn-009b0008)

~~~json
{
  "source": "009b0008",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b000c`](#insn-009b000c)

~~~json
{
  "source": "009b000c",
  "target": "009b0018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0010`](#insn-009b0010)

~~~json
{
  "source": "009b0010",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0014`](#insn-009b0014)

~~~json
{
  "source": "009b0014",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0020`](#insn-009b0020)

~~~json
{
  "source": "009b0020",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0024`](#insn-009b0024)

~~~json
{
  "source": "009b0024",
  "target": "009aae24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0028`](#insn-009b0028)

~~~json
{
  "source": "009b0028",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0030`](#insn-009b0030)

~~~json
{
  "source": "009b0030",
  "target": "009b0354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0048`](#insn-009b0048)

~~~json
{
  "source": "009b0048",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b004c`](#insn-009b004c)

~~~json
{
  "source": "009b004c",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0058`](#insn-009b0058)

~~~json
{
  "source": "009b0058",
  "target": "002c2490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0070`](#insn-009b0070)

~~~json
{
  "source": "009b0070",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0074`](#insn-009b0074)

~~~json
{
  "source": "009b0074",
  "target": "009b0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0080`](#insn-009b0080)

~~~json
{
  "source": "009b0080",
  "target": "009b034c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b008c`](#insn-009b008c)

~~~json
{
  "source": "009b008c",
  "target": "0074a82c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0090`](#insn-009b0090)

~~~json
{
  "source": "009b0090",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0094`](#insn-009b0094)

~~~json
{
  "source": "009b0094",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0098`](#insn-009b0098)

~~~json
{
  "source": "009b0098",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00a0`](#insn-009b00a0)

~~~json
{
  "source": "009b00a0",
  "target": "009b0148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00c0`](#insn-009b00c0)

~~~json
{
  "source": "009b00c0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b00c4`](#insn-009b00c4)

~~~json
{
  "source": "009b00c4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00d8`](#insn-009b00d8)

~~~json
{
  "source": "009b00d8",
  "target": "009b013c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00e8`](#insn-009b00e8)

~~~json
{
  "source": "009b00e8",
  "target": "002b6881",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b00ec`](#insn-009b00ec)

~~~json
{
  "source": "009b00ec",
  "target": "00c58040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b00f0`](#insn-009b00f0)

~~~json
{
  "source": "009b00f0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0118`](#insn-009b0118)

~~~json
{
  "source": "009b0118",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b011c`](#insn-009b011c)

~~~json
{
  "source": "009b011c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0138`](#insn-009b0138)

~~~json
{
  "source": "009b0138",
  "target": "009b00e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b013c`](#insn-009b013c)

~~~json
{
  "source": "009b013c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0140`](#insn-009b0140)

~~~json
{
  "source": "009b0140",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0144`](#insn-009b0144)

~~~json
{
  "source": "009b0144",
  "target": "009b0150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b015c`](#insn-009b015c)

~~~json
{
  "source": "009b015c",
  "target": "009b01d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0164`](#insn-009b0164)

~~~json
{
  "source": "009b0164",
  "target": "Stack[-0x12e]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0168`](#insn-009b0168)

~~~json
{
  "source": "009b0168",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0174`](#insn-009b0174)

~~~json
{
  "source": "009b0174",
  "target": "002b2320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2320",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "72616e6b696e675f6e6f5f72657761726400",
  "capture_start": "002b2320",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009b018c`](#insn-009b018c)

~~~json
{
  "source": "009b018c",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0190`](#insn-009b0190)

~~~json
{
  "source": "009b0190",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0194`](#insn-009b0194)

~~~json
{
  "source": "009b0194",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01a0`](#insn-009b01a0)

~~~json
{
  "source": "009b01a0",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01b0`](#insn-009b01b0)

~~~json
{
  "source": "009b01b0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b01b4`](#insn-009b01b4)

~~~json
{
  "source": "009b01b4",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01b8`](#insn-009b01b8)

~~~json
{
  "source": "009b01b8",
  "target": "009b01c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01bc`](#insn-009b01bc)

~~~json
{
  "source": "009b01bc",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01c0`](#insn-009b01c0)

~~~json
{
  "source": "009b01c0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b01c4`](#insn-009b01c4)

~~~json
{
  "source": "009b01c4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01c8`](#insn-009b01c8)

~~~json
{
  "source": "009b01c8",
  "target": "009b01d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01cc`](#insn-009b01cc)

~~~json
{
  "source": "009b01cc",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01d0`](#insn-009b01d0)

~~~json
{
  "source": "009b01d0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b01d8`](#insn-009b01d8)

~~~json
{
  "source": "009b01d8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b01dc`](#insn-009b01dc)

~~~json
{
  "source": "009b01dc",
  "target": "002b2332",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2332",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "736574446174612825642c20222540222c20222540222900",
  "capture_start": "002b2332",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009b01e0`](#insn-009b01e0)

~~~json
{
  "source": "009b01e0",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01e4`](#insn-009b01e4)

~~~json
{
  "source": "009b01e4",
  "target": "002b2341",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2332",
  "offset": 15,
  "size": 24,
  "datatype": "string",
  "bytes": "736574446174612825642c20222540222c20222540222900",
  "capture_start": "002b2332",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009b01e8`](#insn-009b01e8)

~~~json
{
  "source": "009b01e8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01ec`](#insn-009b01ec)

~~~json
{
  "source": "009b01ec",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01f0`](#insn-009b01f0)

~~~json
{
  "source": "009b01f0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b01f4`](#insn-009b01f4)

~~~json
{
  "source": "009b01f4",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0204`](#insn-009b0204)

~~~json
{
  "source": "009b0204",
  "target": "009b021c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0208`](#insn-009b0208)

~~~json
{
  "source": "009b0208",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b020c`](#insn-009b020c)

~~~json
{
  "source": "009b020c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0210`](#insn-009b0210)

~~~json
{
  "source": "009b0210",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0214`](#insn-009b0214)

~~~json
{
  "source": "009b0214",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0218`](#insn-009b0218)

~~~json
{
  "source": "009b0218",
  "target": "009b0228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b021c`](#insn-009b021c)

~~~json
{
  "source": "009b021c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0224`](#insn-009b0224)

~~~json
{
  "source": "009b0224",
  "target": "0043bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0230`](#insn-009b0230)

~~~json
{
  "source": "009b0230",
  "target": "0048ce94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0248`](#insn-009b0248)

~~~json
{
  "source": "009b0248",
  "target": "007299cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0254`](#insn-009b0254)

~~~json
{
  "source": "009b0254",
  "target": "00492d0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0258`](#insn-009b0258)

~~~json
{
  "source": "009b0258",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b025c`](#insn-009b025c)

~~~json
{
  "source": "009b025c",
  "target": "009b02c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0260`](#insn-009b0260)

~~~json
{
  "source": "009b0260",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0264`](#insn-009b0264)

~~~json
{
  "source": "009b0264",
  "target": "009b02d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0268`](#insn-009b0268)

~~~json
{
  "source": "009b0268",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b026c`](#insn-009b026c)

~~~json
{
  "source": "009b026c",
  "target": "009b02e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0270`](#insn-009b0270)

~~~json
{
  "source": "009b0270",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0274`](#insn-009b0274)

~~~json
{
  "source": "009b0274",
  "target": "009b02f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0278`](#insn-009b0278)

~~~json
{
  "source": "009b0278",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b027c`](#insn-009b027c)

~~~json
{
  "source": "009b027c",
  "target": "009b0300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0280`](#insn-009b0280)

~~~json
{
  "source": "009b0280",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0284`](#insn-009b0284)

~~~json
{
  "source": "009b0284",
  "target": "009b0310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0288`](#insn-009b0288)

~~~json
{
  "source": "009b0288",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0294`](#insn-009b0294)

~~~json
{
  "source": "009b0294",
  "target": "009b0338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b029c`](#insn-009b029c)

~~~json
{
  "source": "009b029c",
  "target": "009b02ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02a8`](#insn-009b02a8)

~~~json
{
  "source": "009b02a8",
  "target": "009b0334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02b0`](#insn-009b02b0)

~~~json
{
  "source": "009b02b0",
  "target": "009b02a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02b8`](#insn-009b02b8)

~~~json
{
  "source": "009b02b8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b02bc`](#insn-009b02bc)

~~~json
{
  "source": "009b02bc",
  "target": "009b02a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02c0`](#insn-009b02c0)

~~~json
{
  "source": "009b02c0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02c4`](#insn-009b02c4)

~~~json
{
  "source": "009b02c4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b02c8`](#insn-009b02c8)

~~~json
{
  "source": "009b02c8",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02cc`](#insn-009b02cc)

~~~json
{
  "source": "009b02cc",
  "target": "009b0268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02d0`](#insn-009b02d0)

~~~json
{
  "source": "009b02d0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02d4`](#insn-009b02d4)

~~~json
{
  "source": "009b02d4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b02d8`](#insn-009b02d8)

~~~json
{
  "source": "009b02d8",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02dc`](#insn-009b02dc)

~~~json
{
  "source": "009b02dc",
  "target": "009b0270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02e0`](#insn-009b02e0)

~~~json
{
  "source": "009b02e0",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02e4`](#insn-009b02e4)

~~~json
{
  "source": "009b02e4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b02e8`](#insn-009b02e8)

~~~json
{
  "source": "009b02e8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02ec`](#insn-009b02ec)

~~~json
{
  "source": "009b02ec",
  "target": "009b0278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02f0`](#insn-009b02f0)

~~~json
{
  "source": "009b02f0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02f4`](#insn-009b02f4)

~~~json
{
  "source": "009b02f4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b02f8`](#insn-009b02f8)

~~~json
{
  "source": "009b02f8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b02fc`](#insn-009b02fc)

~~~json
{
  "source": "009b02fc",
  "target": "009b0280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0300`](#insn-009b0300)

~~~json
{
  "source": "009b0300",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0304`](#insn-009b0304)

~~~json
{
  "source": "009b0304",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0308`](#insn-009b0308)

~~~json
{
  "source": "009b0308",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b030c`](#insn-009b030c)

~~~json
{
  "source": "009b030c",
  "target": "009b0288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0310`](#insn-009b0310)

~~~json
{
  "source": "009b0310",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0314`](#insn-009b0314)

~~~json
{
  "source": "009b0314",
  "target": "009b0320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0318`](#insn-009b0318)

~~~json
{
  "source": "009b0318",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b031c`](#insn-009b031c)

~~~json
{
  "source": "009b031c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0320`](#insn-009b0320)

~~~json
{
  "source": "009b0320",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0324`](#insn-009b0324)

~~~json
{
  "source": "009b0324",
  "target": "009b0078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0328`](#insn-009b0328)

~~~json
{
  "source": "009b0328",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b032c`](#insn-009b032c)

~~~json
{
  "source": "009b032c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0330`](#insn-009b0330)

~~~json
{
  "source": "009b0330",
  "target": "009b0078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0334`](#insn-009b0334)

~~~json
{
  "source": "009b0334",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0338`](#insn-009b0338)

~~~json
{
  "source": "009b0338",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b033c`](#insn-009b033c)

~~~json
{
  "source": "009b033c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0340`](#insn-009b0340)

~~~json
{
  "source": "009b0340",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0344`](#insn-009b0344)

~~~json
{
  "source": "009b0344",
  "target": "009b0318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0348`](#insn-009b0348)

~~~json
{
  "source": "009b0348",
  "target": "009b0320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b034c`](#insn-009b034c)

~~~json
{
  "source": "009b034c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0350`](#insn-009b0350)

~~~json
{
  "source": "009b0350",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0354`](#insn-009b0354)

~~~json
{
  "source": "009b0354",
  "target": "009b036c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0360`](#insn-009b0360)

~~~json
{
  "source": "009b0360",
  "target": "00869f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0364`](#insn-009b0364)

~~~json
{
  "source": "009b0364",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0368`](#insn-009b0368)

~~~json
{
  "source": "009b0368",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b036c`](#insn-009b036c)

~~~json
{
  "source": "009b036c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0370`](#insn-009b0370)

~~~json
{
  "source": "009b0370",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0378`](#insn-009b0378)

~~~json
{
  "source": "009b0378",
  "target": "009b0558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b037c`](#insn-009b037c)

~~~json
{
  "source": "009b037c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0380`](#insn-009b0380)

~~~json
{
  "source": "009b0380",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0384`](#insn-009b0384)

~~~json
{
  "source": "009b0384",
  "target": "009b0390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0388`](#insn-009b0388)

~~~json
{
  "source": "009b0388",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b038c`](#insn-009b038c)

~~~json
{
  "source": "009b038c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009b0394`](#insn-009b0394)

~~~json
{
  "source": "009b0394",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b039c`](#insn-009b039c)

~~~json
{
  "source": "009b039c",
  "target": "009b0524",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03a0`](#insn-009b03a0)

~~~json
{
  "source": "009b03a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03a4`](#insn-009b03a4)

~~~json
{
  "source": "009b03a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03a8`](#insn-009b03a8)

~~~json
{
  "source": "009b03a8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03ac`](#insn-009b03ac)

~~~json
{
  "source": "009b03ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03b0`](#insn-009b03b0)

~~~json
{
  "source": "009b03b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b03b4`](#insn-009b03b4)

~~~json
{
  "source": "009b03b4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009b0524`](#insn-009b0524)

~~~json
{
  "source": "009b0524",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
