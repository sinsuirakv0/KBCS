# 009afefc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "ce618ea68c80343d16a086fd7e265ba9a5ce92c9a769e3c7d3519cff3f0f2e63"
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
