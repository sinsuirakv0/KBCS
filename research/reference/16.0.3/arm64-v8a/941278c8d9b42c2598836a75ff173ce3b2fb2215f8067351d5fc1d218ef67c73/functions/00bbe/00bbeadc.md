# 00bbeadc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbdae8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbdae8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-9add5372f9674d0da7f336852b2148d7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbeadc",
  "name": "_ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE",
  "size": 3584,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be38e3f143a57876a89ea966a07798c6331dce0bb9a6859ac24faf08d4208d7f",
  "source_text_sha256": "be38e3f143a57876a89ea966a07798c6331dce0bb9a6859ac24faf08d4208d7f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbeadc",
        "00bbf8db"
      ]
    ],
    "bytes_sha256": "f9db44206d01656703098f1fd7e0a2ea3e309b39d2aaf9e13b52ccdaeff94324",
    "instruction_count": 896,
    "instruction_bytes": 3584,
    "body_bytes": 3584,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5e5e0](../00c5e/00c5e5e0.md)

## 呼び出し先

- [0046d908](../0046d/0046d908.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59080](../00c59/00c59080.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5c150](../00c5c/00c5c150.md)
- [00c5c660](../00c5c/00c5c660.md)
- [00c5c680](../00c5c/00c5c680.md)
- [00c5e370](../00c5e/00c5e370.md)
- [00c5e490](../00c5e/00c5e490.md)
- [00c5e600](../00c5e/00c5e600.md)
- [00c5e610](../00c5e/00c5e610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 29971 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE
               (undefined8 *param_1,uint *param_2)

{
  char *__s;
  int *piVar1;
  char *__s_00;
  uint uVar2;
  byte bVar3;
  ushort uVar4;
  long lVar5;
  byte *pbVar6;
  byte *pbVar7;
  undefined8 uVar8;
  void *pvVar9;
  long lVar10;
  byte *pbVar11;
  size_t sVar12;
  undefined8 *puVar13;
  void *__dest;
  char *pcVar14;
  undefined8 *puVar15;
  long lVar16;
  ulong uVar17;
  uint *puVar18;
  ulong uVar19;
  ushort *puVar20;
  ulong uVar21;
  byte *pbVar22;
  undefined8 *puVar23;
  long local_330;
  uint *local_328;
  ulong local_320;
  undefined8 uStack_318;
  void *local_310;
  ulong local_308;
  undefined8 local_300;
  void *local_2f8;
  undefined8 local_2f0;
  undefined8 uStack_2e8;
  undefined8 uStack_2e0;
  undefined8 uStack_2d8;
  undefined8 local_2d0;
  undefined8 uStack_2c8;
  undefined8 uStack_2c0;
  undefined8 uStack_2b8;
  undefined8 local_2b0;
  undefined8 uStack_2a8;
  undefined8 uStack_2a0;
  undefined8 uStack_298;
  undefined8 local_290;
  undefined8 uStack_288;
  undefined8 uStack_280;
  undefined8 uStack_278;
  undefined8 local_270;
  undefined8 uStack_268;
  undefined8 uStack_260;
  undefined8 uStack_258;
  undefined8 local_250;
  undefined8 uStack_248;
  undefined8 uStack_240;
  undefined8 uStack_238;
  undefined8 local_230;
  undefined8 uStack_228;
  undefined8 uStack_220;
  long local_218;
  byte *local_210;
  undefined8 uStack_208;
  undefined8 uStack_200;
  undefined8 uStack_1f8;
  undefined8 local_1f0;
  long lStack_1e8;
  byte *local_1e0;
  undefined8 uStack_1d8;
  ulong *local_1d0;
  undefined8 local_1c0;
  undefined8 uStack_1b8;
  undefined8 uStack_1b0;
  undefined8 uStack_1a8;
  undefined8 local_1a0;
  undefined8 uStack_198;
  undefined8 uStack_190;
  undefined8 uStack_188;
  undefined8 local_180;
  undefined8 *local_178;
  undefined8 local_170;
  long local_168;
  void *local_160;
  long lStack_158;
  long local_150;
  undefined8 uStack_148;
  undefined8 local_140;
  undefined8 uStack_138;
  undefined8 uStack_130;
  undefined8 uStack_128;
  undefined8 local_120;
  undefined8 uStack_118;
  undefined8 uStack_110;
  undefined8 uStack_108;
  undefined4 local_100;
  undefined8 local_f8;
  undefined8 uStack_f0;
  undefined8 local_e8;
  undefined8 uStack_e0;
  undefined8 local_d8;
  undefined1 uStack_d0;
  undefined7 uStack_cf;
  undefined1 local_c8;
  undefined7 uStack_c7;
  bool local_c0;
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 uStack_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 local_80;
  long local_78;
  
                    /* try { // try from 00bbeadc to 00cbeae7 has its CatchHandler @ 00bbf06c */
  lVar5 = tpidr_el0;
  local_78 = *(long *)(lVar5 + 0x28);
  local_178 = &local_170;
  local_170 = 0;
  local_168 = 0;
                    /* try { // try from 00bbeb1c to 00cbeb23 has its CatchHandler @ 00bbf068 */
  uStack_1b8 = 0;
  local_1c0 = 0;
  uStack_1a8 = 0;
  uStack_1b0 = 0;
  uStack_198 = 0;
  local_1a0 = 0;
  uStack_188 = 0;
  uStack_190 = 0;
  local_180 = 0;
  lStack_158 = 0;
  local_160 = (void *)0x0;
  uStack_148 = 0;
  local_150 = 0;
  uStack_138 = 0;
  local_140 = 0;
  uStack_128 = 0;
  uStack_130 = 0;
  uStack_118 = 0;
  local_120 = 0;
  uStack_108 = 0;
  uStack_110 = 0;
  local_100 = 0;
  uStack_f0 = 0;
  local_f8 = 0;
  uStack_e0 = 0;
  local_e8 = 0;
  uStack_d0 = 0;
  local_d8 = 0;
  uStack_c7 = 0;
  local_c0 = false;
  uStack_cf = 0;
  local_c8 = 0;
  local_88 = 0;
  uStack_a0 = 0;
  local_a8 = 0;
  uStack_90 = 0;
  uStack_98 = 0;
  uStack_b0 = 0;
  local_b8 = 0;
  local_1d0 = (ulong *)0x0;
  lStack_1e8 = 0;
  local_1f0 = 0;
  uStack_1d8 = 0;
  local_1e0 = (byte *)0x0;
  uStack_208 = 0;
  local_210 = (byte *)0x0;
  uStack_1f8 = 0;
  uStack_200 = 0;
  uStack_228 = 0;
  local_230 = 0;
  local_218 = 0;
  uStack_220 = 0;
  uStack_248 = 0;
  local_250 = 0;
  uStack_238 = 0;
  uStack_240 = 0;
  uStack_268 = 0;
  local_270 = 0;
  uStack_258 = 0;
  uStack_260 = 0;
  uStack_288 = 0;
  local_290 = 0;
  uStack_278 = 0;
  uStack_280 = 0;
  uStack_2a8 = 0;
  local_2b0 = 0;
  uStack_298 = 0;
  uStack_2a0 = 0;
  uStack_2c8 = 0;
  local_2d0 = 0;
  uStack_2b8 = 0;
  uStack_2c0 = 0;
  uStack_2e8 = 0;
  local_2f0 = 0;
  uStack_2d8 = 0;
  uStack_2e0 = 0;
  local_300 = 0;
  local_2f8 = (void *)0x0;
  local_308 = 0;
  lVar16 = 0;
  if (4 < *(ushort *)((long)param_2 - (long)(int)*param_2)) {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[2];
                    /* try { // try from 00bbeba8 to 00cbebab has its CatchHandler @ 00bbf02c */
    lVar16 = 0;
    if (uVar17 != 0) {
                    /* try { // try from 00bbebac to 00cbec37 has its CatchHandler @ 00bbe950 */
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  __s = "";
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_1c0,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 7) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[3];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
                    /* try { // try from 00bbec38 to 00cbec6f has its CatchHandler @ 00bbf078 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_1a8,pcVar14,sVar12);
  uVar17 = (ulong)(int)*param_2;
  lVar16 = -uVar17;
  if ((((10 < *(ushort *)((long)param_2 - uVar17)) &&
       (uVar21 = (ulong)((ushort *)((long)param_2 - uVar17))[5], uVar21 != 0)) &&
      (puVar18 = (uint *)((long)param_2 + uVar21),
      puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18), puVar18 != (uint *)0x0)) &&
     (uVar2 = *puVar18, uVar2 != 0)) {
    uVar21 = 0;
    do {
      puVar18 = (uint *)((long)param_2 +
                        (ulong)*(ushort *)((long)param_2 + (10 - (long)(int)uVar17)));
      puVar18 = (uint *)((long)puVar18 + (uVar21 & 0xfffffffc) + (ulong)*puVar18 + 4);
      piVar1 = (int *)((long)puVar18 + (ulong)*puVar18);
      puVar20 = (ushort *)((long)piVar1 - (long)*piVar1);
      if (*puVar20 < 5) {
        lVar16 = 0;
        pcVar14 = "";
      }
      else {
        lVar16 = 0;
        if ((ulong)puVar20[2] != 0) {
          puVar18 = (uint *)((long)piVar1 + (ulong)puVar20[2]);
          lVar16 = (long)puVar18 + (ulong)*puVar18;
        }
                    /* try { // try from 00bbecec to 00cbecef has its CatchHandler @ 00bbf038 */
                    /* try { // try from 00bbecf0 to 00cbedbf has its CatchHandler @ 00bbe950 */
        pcVar14 = __s;
        if (lVar16 != 0) {
          pcVar14 = (char *)(lVar16 + 4);
        }
        if ((*puVar20 < 7) || ((ulong)puVar20[3] == 0)) {
          lVar16 = 0;
        }
        else {
          puVar18 = (uint *)((long)piVar1 + (ulong)puVar20[3]);
          lVar16 = (long)puVar18 + (ulong)*puVar18;
        }
      }
      __s_00 = __s;
      if (lVar16 != 0) {
        __s_00 = (char *)(lVar16 + 4);
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                (&local_320,pcVar14);
      puVar13 = (undefined8 *)FUN_0046d908(&local_178,&local_80,&local_320);
      puVar23 = (undefined8 *)*puVar13;
      if (puVar23 == (undefined8 *)0x0) {
        puVar23 = (undefined8 *)_Znwm(0x50);
        pvVar9 = local_310;
        uVar8 = uStack_318;
        uVar17 = local_320;
        uStack_318 = 0;
        local_310 = (void *)0x0;
        local_320 = 0;
        puVar23[8] = 0;
        puVar23[9] = 0;
        *puVar23 = 0;
        puVar23[1] = 0;
        puVar23[5] = uVar8;
        puVar23[4] = uVar17;
        puVar23[6] = pvVar9;
        puVar23[7] = 0;
        puVar23[2] = local_80;
        *puVar13 = puVar23;
        puVar15 = puVar23;
        if ((undefined8 *)*local_178 != (undefined8 *)0x0) {
          puVar15 = (undefined8 *)*puVar13;
          local_178 = (undefined8 *)*local_178;
        }
        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                  (local_170,puVar15);
        local_168 = local_168 + 1;
      }
                    /* try { // try from 00bbedc0 to 00cbedc7 has its CatchHandler @ 00bbefe4 */
                    /* try { // try from 00bbedc8 to 00cbee1b has its CatchHandler @ 00bbe950 */
      sVar12 = strlen(__s_00);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (puVar23 + 7,__s_00,sVar12);
      if ((local_320 & 1) != 0) {
        _ZdlPv(local_310);
      }
      uVar17 = (ulong)*param_2;
      uVar21 = uVar21 + 4;
    } while ((ulong)uVar2 * 4 - uVar21 != 0);
    lVar16 = -(long)(int)*param_2;
  }
  lVar10 = lStack_158;
  pvVar9 = local_160;
                    /* try { // try from 00bbee1c to 00cbee2f has its CatchHandler @ 00bbf010 */
  if (((0xc < *(ushort *)((long)param_2 + lVar16)) &&
      (uVar17 = (ulong)((ushort *)((long)param_2 + lVar16))[6], uVar17 != 0)) &&
     (puVar18 = (uint *)((long)param_2 + uVar17),
     puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18), puVar18 != (uint *)0x0)) {
    uVar17 = (ulong)*puVar18;
    if ((ulong)(local_150 - (long)local_160) < uVar17) {
      __dest = (void *)_Znwm(uVar17);
      sVar12 = lVar10 - (long)pvVar9;
                    /* try { // try from 00bbee5c to 00cbee63 has its CatchHandler @ 00bbf03c */
      if (0 < (long)sVar12) {
        memcpy(__dest,pvVar9,sVar12);
      }
      local_160 = __dest;
      lStack_158 = (long)__dest + sVar12;
      local_150 = (long)__dest + uVar17;
      if (pvVar9 != (void *)0x0) {
                    /* try { // try from 00bbee78 to 00cbee7f has its CatchHandler @ 00bbefe8 */
        _ZdlPv(pvVar9);
      }
    }
    uVar4 = *(ushort *)((long)param_2 + (0xc - (long)(int)*param_2));
    puVar18 = (uint *)((long)param_2 + (ulong)uVar4);
    puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18);
    local_328 = (uint *)0x0;
    if (uVar4 != 0) {
      local_328 = puVar18;
    }
    local_328 = local_328 + 1;
    local_330 = (long)puVar18 + (ulong)*puVar18 + 4;
    _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsISB_E9referenceEEE5valueEvE4typeESB_SB_
              (&local_160,&local_328,&local_330);
    lVar16 = -(long)(int)*param_2;
  }
  if (*(ushort *)((long)param_2 + lVar16) < 0xf) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 + lVar16))[7];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_148,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x11) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[8];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
                    /* try { // try from 00bbef58 to 00cbef5f has its CatchHandler @ 00bbf064 */
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
                    /* try { // try from 00bbef74 to 00cbef97 has its CatchHandler @ 00bbf070 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_130,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x17) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xb];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
                    /* try { // try from 00bbefac to 00cbefb3 has its CatchHandler @ 00bbf044 */
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
                    /* try { // try from 00bbefc8 to 00cbefcb has its CatchHandler @ 00bbf070 */
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_f8,pcVar14,sVar12);
                    /* try { // try from 00bbefe0 to 00cbefe3 has its CatchHandler @ 00bbf044 */
                    /* catch() { ... } // from try @ 00bbedc0 with catch @ 00bbefe4
                       try { // try from 00bbefe4 to 00cbf0bb has its CatchHandler @ 00bbe950 */
                    /* catch() { ... } // from try @ 00bbee78 with catch @ 00bbefe8 */
                    /* catch() { ... } // from try @ 00bbea00 with catch @ 00bbefec */
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x19) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xc];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
                    /* catch() { ... } // from try @ 00bbe9f4 with catch @ 00bbeffc */
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
                    /* catch() { ... } // from try @ 00bbe9e8 with catch @ 00bbf00c */
                    /* catch() { ... } // from try @ 00bbee1c with catch @ 00bbf010 */
  pcVar14 = __s;
                    /* catch() { ... } // from try @ 00bbe9bc with catch @ 00bbf014 */
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
                    /* catch() { ... } // from try @ 00bbeba8 with catch @ 00bbf02c */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_e0,pcVar14,sVar12);
                    /* catch() { ... } // from try @ 00bbecec with catch @ 00bbf038 */
                    /* catch() { ... } // from try @ 00bbee5c with catch @ 00bbf03c */
  puVar20 = (ushort *)((long)param_2 - (long)(int)*param_2);
                    /* catch() { ... } // from try @ 00bbefac with catch @ 00bbf044
                       catch() { ... } // from try @ 00bbefe0 with catch @ 00bbf044 */
  if (*puVar20 < 0x1d) {
    lVar16 = 0;
    local_c0 = false;
  }
  else {
    local_c0 = false;
    if ((ulong)puVar20[0xe] != 0) {
      local_c0 = *(char *)((long)param_2 + (ulong)puVar20[0xe]) != '\0';
    }
                    /* catch() { ... } // from try @ 00bbef58 with catch @ 00bbf064 */
                    /* catch() { ... } // from try @ 00bbeb1c with catch @ 00bbf068 */
    if (*puVar20 < 0x1f) {
      lVar16 = 0;
    }
    else {
                    /* catch() { ... } // from try @ 00bbeadc with catch @ 00bbf06c */
                    /* catch() { ... } // from try @ 00bbef74 with catch @ 00bbf070
                       catch() { ... } // from try @ 00bbefc8 with catch @ 00bbf070 */
      lVar16 = 0;
      if ((ulong)puVar20[0xf] != 0) {
        puVar18 = (uint *)((long)param_2 + (ulong)puVar20[0xf]);
                    /* catch() { ... } // from try @ 00bbec38 with catch @ 00bbf078 */
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_b8,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 9) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[4];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_190,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x13) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[9];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_118,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x23) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0x11];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_a0,pcVar14,sVar12);
  puVar20 = (ushort *)((long)param_2 - (long)(int)*param_2);
  uVar4 = *puVar20;
  if (uVar4 < 0x21) {
    local_88 = 0;
    if (uVar4 < 0x15) {
      local_100 = 0;
      goto LAB_00bbf86c;
    }
    uVar17 = (ulong)puVar20[10];
    local_100 = 0;
    if (uVar17 != 0) goto LAB_00bbf210;
  }
  else {
    local_88 = 0;
    if ((ulong)puVar20[0x10] != 0) {
      local_88 = *(undefined8 *)((long)param_2 + (ulong)puVar20[0x10]);
    }
    uVar17 = (ulong)puVar20[10];
    if (uVar17 == 0) {
      local_100 = 0;
    }
    else {
LAB_00bbf210:
      local_100 = *(undefined4 *)((long)param_2 + uVar17);
    }
  }
  if (((0x1a < uVar4) && ((ulong)puVar20[0xd] != 0)) &&
     (param_2 = (uint *)((long)param_2 + (ulong)puVar20[0xd]),
     piVar1 = (int *)((long)param_2 + (ulong)*param_2), piVar1 != (int *)0x0)) {
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 5) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[2];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_2f0,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 7) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[3];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_2d8,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 9) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[4];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_2c0,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0xb) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[5];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_2a8,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0xd) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[6];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_290,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0xf) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[7];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_278,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x11) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[8];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_260,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x13) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[9];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_248,pcVar14,sVar12);
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x15) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[10];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_230,pcVar14,sVar12);
    if ((0x16 < *(ushort *)((long)piVar1 - (long)*piVar1)) &&
       (uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xb], uVar17 != 0)) {
      puVar18 = (uint *)((long)piVar1 + uVar17);
      uVar2 = *(uint *)((long)puVar18 + (ulong)*puVar18);
      uVar21 = (ulong)uVar2;
      lVar16 = (long)local_210 - local_218 >> 3;
      uVar17 = lVar16 * -0x5555555555555555;
      if (uVar17 < uVar21) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (&local_218,uVar21 + lVar16 * 0x5555555555555555);
        pbVar22 = local_210;
      }
      else {
        pbVar22 = local_210;
        if ((uVar17 - uVar21 != 0) &&
           (pbVar22 = (byte *)(local_218 + uVar21 * 0x18), pbVar22 != local_210)) {
          bVar3 = local_210[-0x18];
          pbVar11 = local_210 + -0x18;
          pbVar7 = local_210;
          while( true ) {
            pbVar6 = pbVar11;
            if ((bVar3 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar7 + -8));
            }
            if (pbVar22 == pbVar6) break;
            bVar3 = pbVar6[-0x18];
            pbVar11 = pbVar6 + -0x18;
            pbVar7 = pbVar6;
          }
        }
      }
      local_210 = pbVar22;
      if (uVar2 != 0) {
        uVar17 = 0;
        do {
          if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x17) {
            lVar16 = 0;
          }
          else {
            uVar19 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xb];
            lVar16 = 0;
            if (uVar19 != 0) {
              puVar18 = (uint *)((long)piVar1 + uVar19);
              lVar16 = (long)puVar18 + (ulong)*puVar18;
            }
          }
          puVar18 = (uint *)(lVar16 + (ulong)(uint)((int)uVar17 << 2) + 4);
          pcVar14 = (char *)((long)puVar18 + (ulong)*puVar18 + 4);
          lVar16 = local_218 + uVar17 * 0x18;
          sVar12 = strlen(pcVar14);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                    (lVar16,pcVar14,sVar12);
          uVar17 = uVar17 + 1;
        } while (uVar17 != uVar21);
      }
    }
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x19) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xc];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    pcVar14 = __s;
    if (lVar16 != 0) {
      pcVar14 = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(pcVar14);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&uStack_200,pcVar14,sVar12);
    if ((0x1a < *(ushort *)((long)piVar1 - (long)*piVar1)) &&
       (uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xd], uVar17 != 0)) {
      puVar18 = (uint *)((long)piVar1 + uVar17);
      uVar2 = *(uint *)((long)puVar18 + (ulong)*puVar18);
      uVar21 = (ulong)uVar2;
      lVar16 = (long)local_1e0 - lStack_1e8 >> 3;
      uVar17 = lVar16 * -0x5555555555555555;
      if (uVar17 < uVar21) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (&lStack_1e8,uVar21 + lVar16 * 0x5555555555555555);
        pbVar22 = local_1e0;
      }
      else {
        pbVar22 = local_1e0;
        if ((uVar17 - uVar21 != 0) &&
           (pbVar22 = (byte *)(lStack_1e8 + uVar21 * 0x18), pbVar22 != local_1e0)) {
          bVar3 = local_1e0[-0x18];
          pbVar11 = local_1e0 + -0x18;
          pbVar7 = local_1e0;
          while( true ) {
            pbVar6 = pbVar11;
            if ((bVar3 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar7 + -8));
            }
            if (pbVar22 == pbVar6) break;
            bVar3 = pbVar6[-0x18];
            pbVar11 = pbVar6 + -0x18;
            pbVar7 = pbVar6;
          }
        }
      }
      local_1e0 = pbVar22;
      if (uVar2 != 0) {
        uVar17 = 0;
        do {
          if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x1b) {
            lVar16 = 0;
          }
          else {
            uVar19 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xd];
            lVar16 = 0;
            if (uVar19 != 0) {
              puVar18 = (uint *)((long)piVar1 + uVar19);
              lVar16 = (long)puVar18 + (ulong)*puVar18;
            }
          }
          puVar18 = (uint *)(lVar16 + (ulong)(uint)((int)uVar17 << 2) + 4);
          pcVar14 = (char *)((long)puVar18 + (ulong)*puVar18 + 4);
          lVar16 = lStack_1e8 + uVar17 * 0x18;
          sVar12 = strlen(pcVar14);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                    (lVar16,pcVar14,sVar12);
          uVar17 = uVar17 + 1;
        } while (uVar17 != uVar21);
      }
    }
    if (*(ushort *)((long)piVar1 - (long)*piVar1) < 0x1d) {
      lVar16 = 0;
    }
    else {
      uVar17 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[0xe];
      lVar16 = 0;
      if (uVar17 != 0) {
        puVar18 = (uint *)((long)piVar1 + uVar17);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
    if (lVar16 != 0) {
      __s = (char *)(lVar16 + 4);
    }
    sVar12 = strlen(__s);
                    /* try { // try from 00bbf85c to 00cbfb7b has its CatchHandler @ 00bbf85c
                       catch() { ... } // from try @ 00bbf85c with catch @ 00bbf85c
                       catch() { ... } // from try @ 00bbfbcc with catch @ 00bbf85c
                       catch() { ... } // from try @ 00bbfcec with catch @ 00bbf85c
                       catch() { ... } // from try @ 00bbfdb4 with catch @ 00bbf85c
                       catch() { ... } // from try @ 00bc01b0 with catch @ 00bbf85c
                       catch() { ... } // from try @ 00bc0404 with catch @ 00bbf85c */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_308,__s,sVar12);
    local_c8 = SUB81(&local_2f0,0);
    uStack_c7 = (undefined7)((ulong)&local_2f0 >> 8);
    local_1d0 = &local_308;
  }
LAB_00bbf86c:
  (*(code *)*param_1)(&local_1c0,param_1[1]);
  if (CONCAT71(uStack_c7,local_c8) != 0) {
    *(undefined8 *)(CONCAT71(uStack_c7,local_c8) + 0x120) = 0;
    local_c8 = 0;
    uStack_c7 = 0;
  }
  if ((local_308 & 1) != 0) {
    _ZdlPv(local_2f8);
  }
  _ZN8firebase9messaging12NotificationD2Ev(&local_2f0);
  _ZN8firebase9messaging7MessageD2Ev(&local_1c0);
  if (*(long *)(lVar5 + 0x28) == local_78) {
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
<a id="insn-00bbeadc"></a> `00bbeadc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbeae0"></a> `00bbeae0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeae4"></a> `00bbeae4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbeae8"></a> `00bbeae8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbeaec"></a> `00bbeaec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbeaf0"></a> `00bbeaf0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbeaf4"></a> `00bbeaf4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbeaf8"></a> `00bbeaf8` | `ff 83 0b d1` | sub sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbeafc"></a> `00bbeafc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbeb00"></a> `00bbeb00` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbeb04"></a> `00bbeb04` | `fc 03 06 91` | add x28,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbeb08"></a> `00bbeb08` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbeb0c"></a> `00bbeb0c` | `89 43 01 91` | add x9,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00bbeb10"></a> `00bbeb10` | `95 23 04 91` | add x21,x28,#0x108 | `FALL_THROUGH`
<a id="insn-00bbeb14"></a> `00bbeb14` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbeb18"></a> `00bbeb18` | `ff 7f 1d a9` | stp xzr,xzr,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbeb1c"></a> `00bbeb1c` | `e0 03 0c ad` | stp q0,q0,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00bbeb20"></a> `00bbeb20` | `e0 03 0d ad` | stp q0,q0,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bbeb24"></a> `00bbeb24` | `ff 27 1c a9` | stp xzr,x9,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bbeb28"></a> `00bbeb28` | `e0 03 0f ad` | stp q0,q0,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbeb2c"></a> `00bbeb2c` | `e0 03 10 ad` | stp q0,q0,[sp, #0x200] | `FALL_THROUGH`
<a id="insn-00bbeb30"></a> `00bbeb30` | `e0 03 11 ad` | stp q0,q0,[sp, #0x220] | `FALL_THROUGH`
<a id="insn-00bbeb34"></a> `00bbeb34` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbeb38"></a> `00bbeb38` | `80 83 8c 3c` | stur q0,[x28, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbeb3c"></a> `00bbeb3c` | `80 83 8d 3c` | stur q0,[x28, #0xd8] | `FALL_THROUGH`
<a id="insn-00bbeb40"></a> `00bbeb40` | `80 83 8e 3c` | stur q0,[x28, #0xe8] | `FALL_THROUGH`
<a id="insn-00bbeb44"></a> `00bbeb44` | `80 13 8f 3c` | stur q0,[x28, #0xf1] | `FALL_THROUGH`
<a id="insn-00bbeb48"></a> `00bbeb48` | `bf 1a 00 f9` | str xzr,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00bbeb4c"></a> `00bbeb4c` | `a0 82 00 ad` | stp q0,q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeb50"></a> `00bbeb50` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bbeb54"></a> `00bbeb54` | `ff bb 00 f9` | str xzr,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbeb58"></a> `00bbeb58` | `e0 83 0a ad` | stp q0,q0,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbeb5c"></a> `00bbeb5c` | `e0 83 09 ad` | stp q0,q0,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbeb60"></a> `00bbeb60` | `e0 83 08 ad` | stp q0,q0,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bbeb64"></a> `00bbeb64` | `e0 83 07 ad` | stp q0,q0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bbeb68"></a> `00bbeb68` | `e0 83 06 ad` | stp q0,q0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bbeb6c"></a> `00bbeb6c` | `e0 83 05 ad` | stp q0,q0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbeb70"></a> `00bbeb70` | `e0 83 04 ad` | stp q0,q0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbeb74"></a> `00bbeb74` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbeb78"></a> `00bbeb78` | `e0 83 02 ad` | stp q0,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbeb7c"></a> `00bbeb7c` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbeb80"></a> `00bbeb80` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbeb84"></a> `00bbeb84` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbeb88"></a> `00bbeb88` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbeb8c"></a> `00bbeb8c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bbeb90"></a> `00bbeb90` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbeb94"></a> `00bbeb94` | `28 01 40 79` | ldrh w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbeb98"></a> `00bbeb98` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbeb9c"></a> `00bbeb9c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbeba0"></a> `00bbeba0` | `c3 00 00 54` | b.cc 0x00bbebb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbeba4"></a> `00bbeba4` | `28 09 40 79` | ldrh w8,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbeba8"></a> `00bbeba8` | `88 00 00 b4` | cbz x8,0x00bbebb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbebac"></a> `00bbebac` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbebb0"></a> `00bbebb0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbebb4"></a> `00bbebb4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbebb8"></a> `00bbebb8` | `5b b7 ff 90` | adrp x27,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbebbc"></a> `00bbebbc` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbebc0"></a> `00bbebc0` | `7b 9b 13 91` | add x27,x27,#0x4e6 | `FALL_THROUGH`
<a id="insn-00bbebc4"></a> `00bbebc4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbebc8"></a> `00bbebc8` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbebcc"></a> `00bbebcc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbebd0"></a> `00bbebd0` | `2c 69 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbebd4"></a> `00bbebd4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbebd8"></a> `00bbebd8` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbebdc"></a> `00bbebdc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbebe0"></a> `00bbebe0` | `5c 75 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbebe4"></a> `00bbebe4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbebe8"></a> `00bbebe8` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbebec"></a> `00bbebec` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbebf0"></a> `00bbebf0` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbebf4"></a> `00bbebf4` | `e3 00 00 54` | b.cc 0x00bbec10 | `CONDITIONAL_JUMP`
<a id="insn-00bbebf8"></a> `00bbebf8` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbebfc"></a> `00bbebfc` | `c8 00 00 b4` | cbz x8,0x00bbec14 | `CONDITIONAL_JUMP`
<a id="insn-00bbec00"></a> `00bbec00` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbec04"></a> `00bbec04` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbec08"></a> `00bbec08` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbec0c"></a> `00bbec0c` | `02 00 00 14` | b 0x00bbec14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbec10"></a> `00bbec10` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbec14"></a> `00bbec14` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbec18"></a> `00bbec18` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbec1c"></a> `00bbec1c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbec20"></a> `00bbec20` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbec24"></a> `00bbec24` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbec28"></a> `00bbec28` | `17 61 00 91` | add x23,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbec2c"></a> `00bbec2c` | `15 69 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbec30"></a> `00bbec30` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbec34"></a> `00bbec34` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbec38"></a> `00bbec38` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbec3c"></a> `00bbec3c` | `45 75 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbec40"></a> `00bbec40` | `89 02 80 b9` | ldrsw x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbec44"></a> `00bbec44` | `8a 02 09 cb` | sub x10,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbec48"></a> `00bbec48` | `48 01 40 79` | ldrh w8,[x10] | `FALL_THROUGH`
<a id="insn-00bbec4c"></a> `00bbec4c` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bbec50"></a> `00bbec50` | `e8 03 09 cb` | neg x8,x9 | `FALL_THROUGH`
<a id="insn-00bbec54"></a> `00bbec54` | `43 0d 00 54` | b.cc 0x00bbedfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec58"></a> `00bbec58` | `4a 15 40 79` | ldrh w10,[x10, #0xa] | `FALL_THROUGH`
<a id="insn-00bbec5c"></a> `00bbec5c` | `0a 0d 00 b4` | cbz x10,0x00bbedfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec60"></a> `00bbec60` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00bbec64"></a> `00bbec64` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbec68"></a> `00bbec68` | `4a 01 0b ab` | adds x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbec6c"></a> `00bbec6c` | `80 0c 00 54` | b.eq 0x00bbedfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec70"></a> `00bbec70` | `4a 01 40 b9` | ldr w10,[x10] | `FALL_THROUGH`
<a id="insn-00bbec74"></a> `00bbec74` | `4a 0c 00 34` | cbz w10,0x00bbedfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec78"></a> `00bbec78` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbec7c"></a> `00bbec7c` | `fa 67 00 a9` | stp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbec80"></a> `00bbec80` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbec84"></a> `00bbec84` | `16 21 01 91` | add x22,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbec88"></a> `00bbec88` | `53 f5 7e d3` | lsl x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbec8c"></a> `00bbec8c` | `05 00 00 14` | b 0x00bbeca0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbec90"></a> `00bbec90` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bbec94"></a> `00bbec94` | `5a 13 00 91` | add x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-00bbec98"></a> `00bbec98` | `7f 02 1a eb` | cmp x19,x26 | `FALL_THROUGH`
<a id="insn-00bbec9c"></a> `00bbec9c` | `a0 0a 00 54` | b.eq 0x00bbedf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbeca0"></a> `00bbeca0` | `88 c2 29 cb` | sub x8,x20,w9, SXTW  | `FALL_THROUGH`
<a id="insn-00bbeca4"></a> `00bbeca4` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbeca8"></a> `00bbeca8` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbecac"></a> `00bbecac` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbecb0"></a> `00bbecb0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbecb4"></a> `00bbecb4` | `49 77 7e 92` | and x9,x26,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00bbecb8"></a> `00bbecb8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbecbc"></a> `00bbecbc` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbecc0"></a> `00bbecc0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbecc4"></a> `00bbecc4` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00bbecc8"></a> `00bbecc8` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbeccc"></a> `00bbeccc` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbecd0"></a> `00bbecd0` | `5f 15 00 71` | cmp w10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbecd4"></a> `00bbecd4` | `23 02 00 54` | b.cc 0x00bbed18 | `CONDITIONAL_JUMP`
<a id="insn-00bbecd8"></a> `00bbecd8` | `2b 09 40 79` | ldrh w11,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbecdc"></a> `00bbecdc` | `8b 00 00 b4` | cbz x11,0x00bbecec | `CONDITIONAL_JUMP`
<a id="insn-00bbece0"></a> `00bbece0` | `0b 01 0b 8b` | add x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbece4"></a> `00bbece4` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbece8"></a> `00bbece8` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbecec"></a> `00bbecec` | `6c 11 00 91` | add x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbecf0"></a> `00bbecf0` | `7f 01 00 f1` | cmp x11,#0x0 | `FALL_THROUGH`
<a id="insn-00bbecf4"></a> `00bbecf4` | `61 03 8c 9a` | csel x1,x27,x12,eq | `FALL_THROUGH`
<a id="insn-00bbecf8"></a> `00bbecf8` | `5f 1d 00 71` | cmp w10,#0x7 | `FALL_THROUGH`
<a id="insn-00bbecfc"></a> `00bbecfc` | `43 01 00 54` | b.cc 0x00bbed24 | `CONDITIONAL_JUMP`
<a id="insn-00bbed00"></a> `00bbed00` | `29 0d 40 79` | ldrh w9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bbed04"></a> `00bbed04` | `09 01 00 b4` | cbz x9,0x00bbed24 | `CONDITIONAL_JUMP`
<a id="insn-00bbed08"></a> `00bbed08` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbed0c"></a> `00bbed0c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbed10"></a> `00bbed10` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbed14"></a> `00bbed14` | `05 00 00 14` | b 0x00bbed28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbed18"></a> `00bbed18` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbed1c"></a> `00bbed1c` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00bbed20"></a> `00bbed20` | `02 00 00 14` | b 0x00bbed28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbed24"></a> `00bbed24` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbed28"></a> `00bbed28` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbed2c"></a> `00bbed2c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbed30"></a> `00bbed30` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbed34"></a> `00bbed34` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbed38"></a> `00bbed38` | `4a 76 02 94` | bl 0x00c5c660 | `UNCONDITIONAL_CALL`
<a id="insn-00bbed3c"></a> `00bbed3c` | `a1 c3 01 d1` | sub x1,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bbed40"></a> `00bbed40` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbed44"></a> `00bbed44` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbed48"></a> `00bbed48` | `f0 ba e2 97` | bl 0x0046d908 | `UNCONDITIONAL_CALL`
<a id="insn-00bbed4c"></a> `00bbed4c` | `18 00 40 f9` | ldr x24,[x0] | `FALL_THROUGH`
<a id="insn-00bbed50"></a> `00bbed50` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bbed54"></a> `00bbed54` | `78 03 00 b5` | cbnz x24,0x00bbedc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbed58"></a> `00bbed58` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bbed5c"></a> `00bbed5c` | `75 68 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbed60"></a> `00bbed60` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbed64"></a> `00bbed64` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbed68"></a> `00bbed68` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbed6c"></a> `00bbed6c` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbed70"></a> `00bbed70` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbed74"></a> `00bbed74` | `1f 7c 04 a9` | stp xzr,xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bbed78"></a> `00bbed78` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbed7c"></a> `00bbed7c` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbed80"></a> `00bbed80` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbed84"></a> `00bbed84` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbed88"></a> `00bbed88` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00bbed8c"></a> `00bbed8c` | `e8 e7 40 f9` | ldr x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbed90"></a> `00bbed90` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbed94"></a> `00bbed94` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbed98"></a> `00bbed98` | `88 00 00 b4` | cbz x8,0x00bbeda8 | `CONDITIONAL_JUMP`
<a id="insn-00bbed9c"></a> `00bbed9c` | `e8 e7 00 f9` | str x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbeda0"></a> `00bbeda0` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00bbeda4"></a> `00bbeda4` | `02 00 00 14` | b 0x00bbedac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeda8"></a> `00bbeda8` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bbedac"></a> `00bbedac` | `e0 eb 40 f9` | ldr x0,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbedb0"></a> `00bbedb0` | `34 76 02 94` | bl 0x00c5c680 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedb4"></a> `00bbedb4` | `e8 ef 40 f9` | ldr x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbedb8"></a> `00bbedb8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbedbc"></a> `00bbedbc` | `e8 ef 00 f9` | str x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbedc0"></a> `00bbedc0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbedc4"></a> `00bbedc4` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-00bbedc8"></a> `00bbedc8` | `ae 68 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedcc"></a> `00bbedcc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbedd0"></a> `00bbedd0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbedd4"></a> `00bbedd4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbedd8"></a> `00bbedd8` | `de 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeddc"></a> `00bbeddc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbede0"></a> `00bbede0` | `88 f5 07 36` | tbz w8,#0x0,0x00bbec90 | `CONDITIONAL_JUMP`
<a id="insn-00bbede4"></a> `00bbede4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbede8"></a> `00bbede8` | `5a 68 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedec"></a> `00bbedec` | `a9 ff ff 17` | b 0x00bbec90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbedf0"></a> `00bbedf0` | `fa 67 40 a9` | ldp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbedf4"></a> `00bbedf4` | `28 7d 40 93` | sxtw x8,w9 | `FALL_THROUGH`
<a id="insn-00bbedf8"></a> `00bbedf8` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbedfc"></a> `00bbedfc` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbee00"></a> `00bbee00` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbee04"></a> `00bbee04` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00bbee08"></a> `00bbee08` | `43 06 00 54` | b.cc 0x00bbeed0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee0c"></a> `00bbee0c` | `29 19 40 79` | ldrh w9,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00bbee10"></a> `00bbee10` | `09 06 00 b4` | cbz x9,0x00bbeed0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee14"></a> `00bbee14` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbee18"></a> `00bbee18` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbee1c"></a> `00bbee1c` | `29 01 0a ab` | adds x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbee20"></a> `00bbee20` | `80 05 00 54` | b.eq 0x00bbeed0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee24"></a> `00bbee24` | `e8 fb 40 f9` | ldr x8,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbee28"></a> `00bbee28` | `f6 f3 40 f9` | ldr x22,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbee2c"></a> `00bbee2c` | `37 01 40 b9` | ldr w23,[x9] | `FALL_THROUGH`
<a id="insn-00bbee30"></a> `00bbee30` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00bbee34"></a> `00bbee34` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bbee38"></a> `00bbee38` | `42 02 00 54` | b.cs 0x00bbee80 | `CONDITIONAL_JUMP`
<a id="insn-00bbee3c"></a> `00bbee3c` | `f3 f7 40 f9` | ldr x19,[sp, #0x1e8] | `FALL_THROUGH`
<a id="insn-00bbee40"></a> `00bbee40` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbee44"></a> `00bbee44` | `3b 68 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee48"></a> `00bbee48` | `62 02 16 cb` | sub x2,x19,x22 | `FALL_THROUGH`
<a id="insn-00bbee4c"></a> `00bbee4c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbee50"></a> `00bbee50` | `13 00 02 8b` | add x19,x0,x2 | `FALL_THROUGH`
<a id="insn-00bbee54"></a> `00bbee54` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee58"></a> `00bbee58` | `17 00 17 8b` | add x23,x0,x23 | `FALL_THROUGH`
<a id="insn-00bbee5c"></a> `00bbee5c` | `8b 00 00 54` | b.lt 0x00bbee6c | `CONDITIONAL_JUMP`
<a id="insn-00bbee60"></a> `00bbee60` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbee64"></a> `00bbee64` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbee68"></a> `00bbee68` | `8e 68 02 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee6c"></a> `00bbee6c` | `f8 4f 1e a9` | stp x24,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbee70"></a> `00bbee70` | `f7 fb 00 f9` | str x23,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbee74"></a> `00bbee74` | `76 00 00 b4` | cbz x22,0x00bbee80 | `CONDITIONAL_JUMP`
<a id="insn-00bbee78"></a> `00bbee78` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbee7c"></a> `00bbee7c` | `35 68 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee80"></a> `00bbee80` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbee84"></a> `00bbee84` | `80 83 01 91` | add x0,x28,#0x60 | `FALL_THROUGH`
<a id="insn-00bbee88"></a> `00bbee88` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbee8c"></a> `00bbee8c` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbee90"></a> `00bbee90` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbee94"></a> `00bbee94` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbee98"></a> `00bbee98` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbee9c"></a> `00bbee9c` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbeea0"></a> `00bbeea0` | `e8 03 89 9a` | csel x8,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-00bbeea4"></a> `00bbeea4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbeea8"></a> `00bbeea8` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbeeac"></a> `00bbeeac` | `28 01 40 b9` | ldr w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbeeb0"></a> `00bbeeb0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbeeb4"></a> `00bbeeb4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbeeb8"></a> `00bbeeb8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeebc"></a> `00bbeebc` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbeec0"></a> `00bbeec0` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeec4"></a> `00bbeec4` | `d3 7d 02 94` | bl 0x00c5e610 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeec8"></a> `00bbeec8` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbeecc"></a> `00bbeecc` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbeed0"></a> `00bbeed0` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbeed4"></a> `00bbeed4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbeed8"></a> `00bbeed8` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbeedc"></a> `00bbeedc` | `e3 00 00 54` | b.cc 0x00bbeef8 | `CONDITIONAL_JUMP`
<a id="insn-00bbeee0"></a> `00bbeee0` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbeee4"></a> `00bbeee4` | `c8 00 00 b4` | cbz x8,0x00bbeefc | `CONDITIONAL_JUMP`
<a id="insn-00bbeee8"></a> `00bbeee8` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbeeec"></a> `00bbeeec` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbeef0"></a> `00bbeef0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbeef4"></a> `00bbeef4` | `02 00 00 14` | b 0x00bbeefc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeef8"></a> `00bbeef8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbeefc"></a> `00bbeefc` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbef00"></a> `00bbef00` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbef04"></a> `00bbef04` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbef08"></a> `00bbef08` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbef0c"></a> `00bbef0c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbef10"></a> `00bbef10` | `17 e1 01 91` | add x23,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbef14"></a> `00bbef14` | `5b 68 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbef18"></a> `00bbef18` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbef1c"></a> `00bbef1c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbef20"></a> `00bbef20` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbef24"></a> `00bbef24` | `8b 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbef28"></a> `00bbef28` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbef2c"></a> `00bbef2c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbef30"></a> `00bbef30` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbef34"></a> `00bbef34` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbef38"></a> `00bbef38` | `e3 00 00 54` | b.cc 0x00bbef54 | `CONDITIONAL_JUMP`
<a id="insn-00bbef3c"></a> `00bbef3c` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbef40"></a> `00bbef40` | `c8 00 00 b4` | cbz x8,0x00bbef58 | `CONDITIONAL_JUMP`
<a id="insn-00bbef44"></a> `00bbef44` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbef48"></a> `00bbef48` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbef4c"></a> `00bbef4c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbef50"></a> `00bbef50` | `02 00 00 14` | b 0x00bbef58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbef54"></a> `00bbef54` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbef58"></a> `00bbef58` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbef5c"></a> `00bbef5c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbef60"></a> `00bbef60` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbef64"></a> `00bbef64` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbef68"></a> `00bbef68` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbef6c"></a> `00bbef6c` | `17 41 02 91` | add x23,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbef70"></a> `00bbef70` | `44 68 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbef74"></a> `00bbef74` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbef78"></a> `00bbef78` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbef7c"></a> `00bbef7c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbef80"></a> `00bbef80` | `74 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbef84"></a> `00bbef84` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbef88"></a> `00bbef88` | `96 23 03 91` | add x22,x28,#0xc8 | `FALL_THROUGH`
<a id="insn-00bbef8c"></a> `00bbef8c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbef90"></a> `00bbef90` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbef94"></a> `00bbef94` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbef98"></a> `00bbef98` | `e3 00 00 54` | b.cc 0x00bbefb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbef9c"></a> `00bbef9c` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbefa0"></a> `00bbefa0` | `c8 00 00 b4` | cbz x8,0x00bbefb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbefa4"></a> `00bbefa4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbefa8"></a> `00bbefa8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbefac"></a> `00bbefac` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbefb0"></a> `00bbefb0` | `02 00 00 14` | b 0x00bbefb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbefb4"></a> `00bbefb4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbefb8"></a> `00bbefb8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbefbc"></a> `00bbefbc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbefc0"></a> `00bbefc0` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbefc4"></a> `00bbefc4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbefc8"></a> `00bbefc8` | `2e 68 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbefcc"></a> `00bbefcc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbefd0"></a> `00bbefd0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbefd4"></a> `00bbefd4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbefd8"></a> `00bbefd8` | `5e 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbefdc"></a> `00bbefdc` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbefe0"></a> `00bbefe0` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbefe4"></a> `00bbefe4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbefe8"></a> `00bbefe8` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbefec"></a> `00bbefec` | `e3 00 00 54` | b.cc 0x00bbf008 | `CONDITIONAL_JUMP`
<a id="insn-00bbeff0"></a> `00bbeff0` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbeff4"></a> `00bbeff4` | `c8 00 00 b4` | cbz x8,0x00bbf00c | `CONDITIONAL_JUMP`
<a id="insn-00bbeff8"></a> `00bbeff8` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbeffc"></a> `00bbeffc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf000"></a> `00bbf000` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf004"></a> `00bbf004` | `02 00 00 14` | b 0x00bbf00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf008"></a> `00bbf008` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf00c"></a> `00bbf00c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf010"></a> `00bbf010` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf014"></a> `00bbf014` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf018"></a> `00bbf018` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf01c"></a> `00bbf01c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbf020"></a> `00bbf020` | `17 81 03 91` | add x23,x8,#0xe0 | `FALL_THROUGH`
<a id="insn-00bbf024"></a> `00bbf024` | `17 68 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf028"></a> `00bbf028` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf02c"></a> `00bbf02c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbf030"></a> `00bbf030` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbf034"></a> `00bbf034` | `47 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf038"></a> `00bbf038` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf03c"></a> `00bbf03c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf040"></a> `00bbf040` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf044"></a> `00bbf044` | `3f 71 00 71` | cmp w9,#0x1c | `FALL_THROUGH`
<a id="insn-00bbf048"></a> `00bbf048` | `e9 01 00 54` | b.ls 0x00bbf084 | `CONDITIONAL_JUMP`
<a id="insn-00bbf04c"></a> `00bbf04c` | `0a 39 40 79` | ldrh w10,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbf050"></a> `00bbf050` | `8a 00 00 b4` | cbz x10,0x00bbf060 | `CONDITIONAL_JUMP`
<a id="insn-00bbf054"></a> `00bbf054` | `8a 6a 6a 38` | ldrb w10,[x20, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf058"></a> `00bbf058` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf05c"></a> `00bbf05c` | `ea 07 9f 1a` | cset w10,ne | `FALL_THROUGH`
<a id="insn-00bbf060"></a> `00bbf060` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00bbf064"></a> `00bbf064` | `ea 03 0a 39` | strb w10,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbf068"></a> `00bbf068` | `43 01 00 54` | b.cc 0x00bbf090 | `CONDITIONAL_JUMP`
<a id="insn-00bbf06c"></a> `00bbf06c` | `08 3d 40 79` | ldrh w8,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00bbf070"></a> `00bbf070` | `28 01 00 b4` | cbz x8,0x00bbf094 | `CONDITIONAL_JUMP`
<a id="insn-00bbf074"></a> `00bbf074` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf078"></a> `00bbf078` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf07c"></a> `00bbf07c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf080"></a> `00bbf080` | `05 00 00 14` | b 0x00bbf094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf084"></a> `00bbf084` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf088"></a> `00bbf088` | `ff 03 0a 39` | strb wzr,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbf08c"></a> `00bbf08c` | `02 00 00 14` | b 0x00bbf094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf090"></a> `00bbf090` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf094"></a> `00bbf094` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf098"></a> `00bbf098` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf09c"></a> `00bbf09c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf0a0"></a> `00bbf0a0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbf0a4"></a> `00bbf0a4` | `f7 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf0a8"></a> `00bbf0a8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf0ac"></a> `00bbf0ac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf0b0"></a> `00bbf0b0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbf0b4"></a> `00bbf0b4` | `27 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf0b8"></a> `00bbf0b8` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf0bc"></a> `00bbf0bc` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf0c0"></a> `00bbf0c0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf0c4"></a> `00bbf0c4` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbf0c8"></a> `00bbf0c8` | `e3 00 00 54` | b.cc 0x00bbf0e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0cc"></a> `00bbf0cc` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf0d0"></a> `00bbf0d0` | `c8 00 00 b4` | cbz x8,0x00bbf0e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf0d4"></a> `00bbf0d4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf0d8"></a> `00bbf0d8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf0dc"></a> `00bbf0dc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf0e0"></a> `00bbf0e0` | `02 00 00 14` | b 0x00bbf0e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf0e4"></a> `00bbf0e4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf0e8"></a> `00bbf0e8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf0ec"></a> `00bbf0ec` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf0f0"></a> `00bbf0f0` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf0f4"></a> `00bbf0f4` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf0f8"></a> `00bbf0f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf0fc"></a> `00bbf0fc` | `16 c1 00 91` | add x22,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbf100"></a> `00bbf100` | `e0 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf104"></a> `00bbf104` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf108"></a> `00bbf108` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbf10c"></a> `00bbf10c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbf110"></a> `00bbf110` | `10 74 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf114"></a> `00bbf114` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf118"></a> `00bbf118` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf11c"></a> `00bbf11c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf120"></a> `00bbf120` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbf124"></a> `00bbf124` | `e3 00 00 54` | b.cc 0x00bbf140 | `CONDITIONAL_JUMP`
<a id="insn-00bbf128"></a> `00bbf128` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbf12c"></a> `00bbf12c` | `c8 00 00 b4` | cbz x8,0x00bbf144 | `CONDITIONAL_JUMP`
<a id="insn-00bbf130"></a> `00bbf130` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf134"></a> `00bbf134` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf138"></a> `00bbf138` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf13c"></a> `00bbf13c` | `02 00 00 14` | b 0x00bbf144 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf140"></a> `00bbf140` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf144"></a> `00bbf144` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf148"></a> `00bbf148` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf14c"></a> `00bbf14c` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf150"></a> `00bbf150` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf154"></a> `00bbf154` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf158"></a> `00bbf158` | `16 a1 02 91` | add x22,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbf15c"></a> `00bbf15c` | `c9 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf160"></a> `00bbf160` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf164"></a> `00bbf164` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbf168"></a> `00bbf168` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbf16c"></a> `00bbf16c` | `f9 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf170"></a> `00bbf170` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf174"></a> `00bbf174` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf178"></a> `00bbf178` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf17c"></a> `00bbf17c` | `3f 8d 00 71` | cmp w9,#0x23 | `FALL_THROUGH`
<a id="insn-00bbf180"></a> `00bbf180` | `e3 00 00 54` | b.cc 0x00bbf19c | `CONDITIONAL_JUMP`
<a id="insn-00bbf184"></a> `00bbf184` | `08 45 40 79` | ldrh w8,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00bbf188"></a> `00bbf188` | `c8 00 00 b4` | cbz x8,0x00bbf1a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf18c"></a> `00bbf18c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf190"></a> `00bbf190` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf194"></a> `00bbf194` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf198"></a> `00bbf198` | `02 00 00 14` | b 0x00bbf1a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf19c"></a> `00bbf19c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf1a0"></a> `00bbf1a0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf1a4"></a> `00bbf1a4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf1a8"></a> `00bbf1a8` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf1ac"></a> `00bbf1ac` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf1b0"></a> `00bbf1b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf1b4"></a> `00bbf1b4` | `16 81 04 91` | add x22,x8,#0x120 | `FALL_THROUGH`
<a id="insn-00bbf1b8"></a> `00bbf1b8` | `b2 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf1bc"></a> `00bbf1bc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf1c0"></a> `00bbf1c0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbf1c4"></a> `00bbf1c4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbf1c8"></a> `00bbf1c8` | `e2 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf1cc"></a> `00bbf1cc` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbf1d0"></a> `00bbf1d0` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf1d4"></a> `00bbf1d4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf1d8"></a> `00bbf1d8` | `3f 85 00 71` | cmp w9,#0x21 | `FALL_THROUGH`
<a id="insn-00bbf1dc"></a> `00bbf1dc` | `03 01 00 54` | b.cc 0x00bbf1fc | `CONDITIONAL_JUMP`
<a id="insn-00bbf1e0"></a> `00bbf1e0` | `0a 41 40 79` | ldrh w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf1e4"></a> `00bbf1e4` | `4a 00 00 b4` | cbz x10,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbf1e8"></a> `00bbf1e8` | `8a 6a 6a f8` | ldr x10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf1ec"></a> `00bbf1ec` | `ea 5f 01 f9` | str x10,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbf1f0"></a> `00bbf1f0` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbf1f4"></a> `00bbf1f4` | `ea 00 00 b5` | cbnz x10,0x00bbf210 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1f8"></a> `00bbf1f8` | `07 00 00 14` | b 0x00bbf214 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf1fc"></a> `00bbf1fc` | `3f 51 00 71` | cmp w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bbf200"></a> `00bbf200` | `ff 5f 01 f9` | str xzr,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbf204"></a> `00bbf204` | `09 03 00 54` | b.ls 0x00bbf264 | `CONDITIONAL_JUMP`
<a id="insn-00bbf208"></a> `00bbf208` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbf20c"></a> `00bbf20c` | `4a 00 00 b4` | cbz x10,0x00bbf214 | `CONDITIONAL_JUMP`
<a id="insn-00bbf210"></a> `00bbf210` | `8a 6a 6a b8` | ldr w10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf214"></a> `00bbf214` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbf218"></a> `00bbf218` | `ea 43 02 b9` | str w10,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbf21c"></a> `00bbf21c` | `83 32 00 54` | b.cc 0x00bbf86c | `CONDITIONAL_JUMP`
<a id="insn-00bbf220"></a> `00bbf220` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbf224"></a> `00bbf224` | `48 32 00 b4` | cbz x8,0x00bbf86c | `CONDITIONAL_JUMP`
<a id="insn-00bbf228"></a> `00bbf228` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf22c"></a> `00bbf22c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf230"></a> `00bbf230` | `16 01 09 ab` | adds x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf234"></a> `00bbf234` | `c0 31 00 54` | b.eq 0x00bbf86c | `CONDITIONAL_JUMP`
<a id="insn-00bbf238"></a> `00bbf238` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf23c"></a> `00bbf23c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf240"></a> `00bbf240` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf244"></a> `00bbf244` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf248"></a> `00bbf248` | `23 01 00 54` | b.cc 0x00bbf26c | `CONDITIONAL_JUMP`
<a id="insn-00bbf24c"></a> `00bbf24c` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbf250"></a> `00bbf250` | `08 01 00 b4` | cbz x8,0x00bbf270 | `CONDITIONAL_JUMP`
<a id="insn-00bbf254"></a> `00bbf254` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf258"></a> `00bbf258` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf25c"></a> `00bbf25c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf260"></a> `00bbf260` | `04 00 00 14` | b 0x00bbf270 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf264"></a> `00bbf264` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbf268"></a> `00bbf268` | `81 01 00 14` | b 0x00bbf86c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf26c"></a> `00bbf26c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf270"></a> `00bbf270` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf274"></a> `00bbf274` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf278"></a> `00bbf278` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf27c"></a> `00bbf27c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf280"></a> `00bbf280` | `80 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf284"></a> `00bbf284` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf288"></a> `00bbf288` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf28c"></a> `00bbf28c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf290"></a> `00bbf290` | `b0 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf294"></a> `00bbf294` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf298"></a> `00bbf298` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf29c"></a> `00bbf29c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf2a0"></a> `00bbf2a0` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbf2a4"></a> `00bbf2a4` | `e3 00 00 54` | b.cc 0x00bbf2c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2a8"></a> `00bbf2a8` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbf2ac"></a> `00bbf2ac` | `c8 00 00 b4` | cbz x8,0x00bbf2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf2b0"></a> `00bbf2b0` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf2b4"></a> `00bbf2b4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf2b8"></a> `00bbf2b8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf2bc"></a> `00bbf2bc` | `02 00 00 14` | b 0x00bbf2c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf2c0"></a> `00bbf2c0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf2c4"></a> `00bbf2c4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf2c8"></a> `00bbf2c8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf2cc"></a> `00bbf2cc` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf2d0"></a> `00bbf2d0` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf2d4"></a> `00bbf2d4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf2d8"></a> `00bbf2d8` | `15 61 00 91` | add x21,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf2dc"></a> `00bbf2dc` | `69 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf2e0"></a> `00bbf2e0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf2e4"></a> `00bbf2e4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf2e8"></a> `00bbf2e8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf2ec"></a> `00bbf2ec` | `99 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf2f0"></a> `00bbf2f0` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf2f4"></a> `00bbf2f4` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf2f8"></a> `00bbf2f8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf2fc"></a> `00bbf2fc` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbf300"></a> `00bbf300` | `e3 00 00 54` | b.cc 0x00bbf31c | `CONDITIONAL_JUMP`
<a id="insn-00bbf304"></a> `00bbf304` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf308"></a> `00bbf308` | `c8 00 00 b4` | cbz x8,0x00bbf320 | `CONDITIONAL_JUMP`
<a id="insn-00bbf30c"></a> `00bbf30c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf310"></a> `00bbf310` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf314"></a> `00bbf314` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf318"></a> `00bbf318` | `02 00 00 14` | b 0x00bbf320 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf31c"></a> `00bbf31c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf320"></a> `00bbf320` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf324"></a> `00bbf324` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf328"></a> `00bbf328` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf32c"></a> `00bbf32c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf330"></a> `00bbf330` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf334"></a> `00bbf334` | `15 c1 00 91` | add x21,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbf338"></a> `00bbf338` | `52 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf33c"></a> `00bbf33c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf340"></a> `00bbf340` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf344"></a> `00bbf344` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf348"></a> `00bbf348` | `82 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf34c"></a> `00bbf34c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf350"></a> `00bbf350` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf354"></a> `00bbf354` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf358"></a> `00bbf358` | `3f 2d 00 71` | cmp w9,#0xb | `FALL_THROUGH`
<a id="insn-00bbf35c"></a> `00bbf35c` | `e3 00 00 54` | b.cc 0x00bbf378 | `CONDITIONAL_JUMP`
<a id="insn-00bbf360"></a> `00bbf360` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbf364"></a> `00bbf364` | `c8 00 00 b4` | cbz x8,0x00bbf37c | `CONDITIONAL_JUMP`
<a id="insn-00bbf368"></a> `00bbf368` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf36c"></a> `00bbf36c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf370"></a> `00bbf370` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf374"></a> `00bbf374` | `02 00 00 14` | b 0x00bbf37c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf378"></a> `00bbf378` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf37c"></a> `00bbf37c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf380"></a> `00bbf380` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf384"></a> `00bbf384` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf388"></a> `00bbf388` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf38c"></a> `00bbf38c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf390"></a> `00bbf390` | `15 21 01 91` | add x21,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbf394"></a> `00bbf394` | `3b 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf398"></a> `00bbf398` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf39c"></a> `00bbf39c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf3a0"></a> `00bbf3a0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf3a4"></a> `00bbf3a4` | `6b 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf3a8"></a> `00bbf3a8` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf3ac"></a> `00bbf3ac` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf3b0"></a> `00bbf3b0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf3b4"></a> `00bbf3b4` | `3f 35 00 71` | cmp w9,#0xd | `FALL_THROUGH`
<a id="insn-00bbf3b8"></a> `00bbf3b8` | `e3 00 00 54` | b.cc 0x00bbf3d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3bc"></a> `00bbf3bc` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbf3c0"></a> `00bbf3c0` | `c8 00 00 b4` | cbz x8,0x00bbf3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf3c4"></a> `00bbf3c4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf3c8"></a> `00bbf3c8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf3cc"></a> `00bbf3cc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf3d0"></a> `00bbf3d0` | `02 00 00 14` | b 0x00bbf3d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf3d4"></a> `00bbf3d4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf3d8"></a> `00bbf3d8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf3dc"></a> `00bbf3dc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf3e0"></a> `00bbf3e0` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf3e4"></a> `00bbf3e4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf3e8"></a> `00bbf3e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf3ec"></a> `00bbf3ec` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf3f0"></a> `00bbf3f0` | `24 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf3f4"></a> `00bbf3f4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf3f8"></a> `00bbf3f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf3fc"></a> `00bbf3fc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf400"></a> `00bbf400` | `54 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf404"></a> `00bbf404` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf408"></a> `00bbf408` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf40c"></a> `00bbf40c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf410"></a> `00bbf410` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbf414"></a> `00bbf414` | `e3 00 00 54` | b.cc 0x00bbf430 | `CONDITIONAL_JUMP`
<a id="insn-00bbf418"></a> `00bbf418` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbf41c"></a> `00bbf41c` | `c8 00 00 b4` | cbz x8,0x00bbf434 | `CONDITIONAL_JUMP`
<a id="insn-00bbf420"></a> `00bbf420` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf424"></a> `00bbf424` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf428"></a> `00bbf428` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf42c"></a> `00bbf42c` | `02 00 00 14` | b 0x00bbf434 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf430"></a> `00bbf430` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf434"></a> `00bbf434` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf438"></a> `00bbf438` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf43c"></a> `00bbf43c` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf440"></a> `00bbf440` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf444"></a> `00bbf444` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf448"></a> `00bbf448` | `15 e1 01 91` | add x21,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbf44c"></a> `00bbf44c` | `0d 67 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf450"></a> `00bbf450` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf454"></a> `00bbf454` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf458"></a> `00bbf458` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf45c"></a> `00bbf45c` | `3d 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf460"></a> `00bbf460` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf464"></a> `00bbf464` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf468"></a> `00bbf468` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf46c"></a> `00bbf46c` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbf470"></a> `00bbf470` | `e3 00 00 54` | b.cc 0x00bbf48c | `CONDITIONAL_JUMP`
<a id="insn-00bbf474"></a> `00bbf474` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf478"></a> `00bbf478` | `c8 00 00 b4` | cbz x8,0x00bbf490 | `CONDITIONAL_JUMP`
<a id="insn-00bbf47c"></a> `00bbf47c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf480"></a> `00bbf480` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf484"></a> `00bbf484` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf488"></a> `00bbf488` | `02 00 00 14` | b 0x00bbf490 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf48c"></a> `00bbf48c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf490"></a> `00bbf490` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf494"></a> `00bbf494` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf498"></a> `00bbf498` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf49c"></a> `00bbf49c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf4a0"></a> `00bbf4a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf4a4"></a> `00bbf4a4` | `15 41 02 91` | add x21,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbf4a8"></a> `00bbf4a8` | `f6 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf4ac"></a> `00bbf4ac` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf4b0"></a> `00bbf4b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf4b4"></a> `00bbf4b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf4b8"></a> `00bbf4b8` | `26 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf4bc"></a> `00bbf4bc` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf4c0"></a> `00bbf4c0` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf4c4"></a> `00bbf4c4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf4c8"></a> `00bbf4c8` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbf4cc"></a> `00bbf4cc` | `e3 00 00 54` | b.cc 0x00bbf4e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf4d0"></a> `00bbf4d0` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbf4d4"></a> `00bbf4d4` | `c8 00 00 b4` | cbz x8,0x00bbf4ec | `CONDITIONAL_JUMP`
<a id="insn-00bbf4d8"></a> `00bbf4d8` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf4dc"></a> `00bbf4dc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf4e0"></a> `00bbf4e0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf4e4"></a> `00bbf4e4` | `02 00 00 14` | b 0x00bbf4ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf4e8"></a> `00bbf4e8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf4ec"></a> `00bbf4ec` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf4f0"></a> `00bbf4f0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf4f4"></a> `00bbf4f4` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf4f8"></a> `00bbf4f8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf4fc"></a> `00bbf4fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf500"></a> `00bbf500` | `15 a1 02 91` | add x21,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbf504"></a> `00bbf504` | `df 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf508"></a> `00bbf508` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf50c"></a> `00bbf50c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf510"></a> `00bbf510` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf514"></a> `00bbf514` | `0f 73 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf518"></a> `00bbf518` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf51c"></a> `00bbf51c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf520"></a> `00bbf520` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf524"></a> `00bbf524` | `3f 55 00 71` | cmp w9,#0x15 | `FALL_THROUGH`
<a id="insn-00bbf528"></a> `00bbf528` | `e3 00 00 54` | b.cc 0x00bbf544 | `CONDITIONAL_JUMP`
<a id="insn-00bbf52c"></a> `00bbf52c` | `08 29 40 79` | ldrh w8,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbf530"></a> `00bbf530` | `c8 00 00 b4` | cbz x8,0x00bbf548 | `CONDITIONAL_JUMP`
<a id="insn-00bbf534"></a> `00bbf534` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf538"></a> `00bbf538` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf53c"></a> `00bbf53c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf540"></a> `00bbf540` | `02 00 00 14` | b 0x00bbf548 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf544"></a> `00bbf544` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf548"></a> `00bbf548` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf54c"></a> `00bbf54c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf550"></a> `00bbf550` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf554"></a> `00bbf554` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf558"></a> `00bbf558` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf55c"></a> `00bbf55c` | `15 01 03 91` | add x21,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbf560"></a> `00bbf560` | `c8 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf564"></a> `00bbf564` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf568"></a> `00bbf568` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf56c"></a> `00bbf56c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf570"></a> `00bbf570` | `f8 72 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf574"></a> `00bbf574` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf578"></a> `00bbf578` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf57c"></a> `00bbf57c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf580"></a> `00bbf580` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbf584"></a> `00bbf584` | `63 08 00 54` | b.cc 0x00bbf690 | `CONDITIONAL_JUMP`
<a id="insn-00bbf588"></a> `00bbf588` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbf58c"></a> `00bbf58c` | `28 08 00 b4` | cbz x8,0x00bbf690 | `CONDITIONAL_JUMP`
<a id="insn-00bbf590"></a> `00bbf590` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf594"></a> `00bbf594` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbf598"></a> `00bbf598` | `e9 a3 52 a9` | ldp x9,x8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbf59c"></a> `00bbf59c` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf5a0"></a> `00bbf5a0` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf5a4"></a> `00bbf5a4` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbf5a8"></a> `00bbf5a8` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf5ac"></a> `00bbf5ac` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbf5b0"></a> `00bbf5b0` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbf5b4"></a> `00bbf5b4` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbf5b8"></a> `00bbf5b8` | `c2 00 00 54` | b.cs 0x00bbf5d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5bc"></a> `00bbf5bc` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf5c0"></a> `00bbf5c0` | `00 61 03 91` | add x0,x8,#0xd8 | `FALL_THROUGH`
<a id="insn-00bbf5c4"></a> `00bbf5c4` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbf5c8"></a> `00bbf5c8` | `0e 7c 02 94` | bl 0x00c5e600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf5cc"></a> `00bbf5cc` | `12 00 00 14` | b 0x00bbf614 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf5d0"></a> `00bbf5d0` | `29 02 00 54` | b.ls 0x00bbf614 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5d4"></a> `00bbf5d4` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf5d8"></a> `00bbf5d8` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbf5dc"></a> `00bbf5dc` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf5e0"></a> `00bbf5e0` | `80 01 00 54` | b.eq 0x00bbf610 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5e4"></a> `00bbf5e4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbf5e8"></a> `00bbf5e8` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbf5ec"></a> `00bbf5ec` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbf604 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5f0"></a> `00bbf5f0` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbf5f4"></a> `00bbf5f4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbf5f8"></a> `00bbf5f8` | `c0 00 00 54` | b.eq 0x00bbf610 | `CONDITIONAL_JUMP`
<a id="insn-00bbf5fc"></a> `00bbf5fc` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbf600"></a> `00bbf600` | `89 ff 07 36` | tbz w9,#0x0,0x00bbf5f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf604"></a> `00bbf604` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbf608"></a> `00bbf608` | `52 66 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf60c"></a> `00bbf60c` | `f9 ff ff 17` | b 0x00bbf5f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf610"></a> `00bbf610` | `f4 9b 00 f9` | str x20,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbf614"></a> `00bbf614` | `f3 03 00 34` | cbz w19,0x00bbf690 | `CONDITIONAL_JUMP`
<a id="insn-00bbf618"></a> `00bbf618` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbf61c"></a> `00bbf61c` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf620"></a> `00bbf620` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf624"></a> `00bbf624` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf628"></a> `00bbf628` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf62c"></a> `00bbf62c` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbf630"></a> `00bbf630` | `e3 00 00 54` | b.cc 0x00bbf64c | `CONDITIONAL_JUMP`
<a id="insn-00bbf634"></a> `00bbf634` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbf638"></a> `00bbf638` | `c8 00 00 b4` | cbz x8,0x00bbf650 | `CONDITIONAL_JUMP`
<a id="insn-00bbf63c"></a> `00bbf63c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf640"></a> `00bbf640` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf644"></a> `00bbf644` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf648"></a> `00bbf648` | `02 00 00 14` | b 0x00bbf650 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf64c"></a> `00bbf64c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf650"></a> `00bbf650` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf654"></a> `00bbf654` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf658"></a> `00bbf658` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbf65c"></a> `00bbf65c` | `ea 97 40 f9` | ldr x10,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbf660"></a> `00bbf660` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf664"></a> `00bbf664` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf668"></a> `00bbf668` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf66c"></a> `00bbf66c` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbf670"></a> `00bbf670` | `84 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf674"></a> `00bbf674` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf678"></a> `00bbf678` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf67c"></a> `00bbf67c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf680"></a> `00bbf680` | `b4 72 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf684"></a> `00bbf684` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf688"></a> `00bbf688` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbf68c"></a> `00bbf68c` | `a1 fc ff 54` | b.ne 0x00bbf620 | `CONDITIONAL_JUMP`
<a id="insn-00bbf690"></a> `00bbf690` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf694"></a> `00bbf694` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf698"></a> `00bbf698` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf69c"></a> `00bbf69c` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbf6a0"></a> `00bbf6a0` | `e3 00 00 54` | b.cc 0x00bbf6bc | `CONDITIONAL_JUMP`
<a id="insn-00bbf6a4"></a> `00bbf6a4` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf6a8"></a> `00bbf6a8` | `c8 00 00 b4` | cbz x8,0x00bbf6c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf6ac"></a> `00bbf6ac` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf6b0"></a> `00bbf6b0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf6b4"></a> `00bbf6b4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf6b8"></a> `00bbf6b8` | `02 00 00 14` | b 0x00bbf6c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf6bc"></a> `00bbf6bc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf6c0"></a> `00bbf6c0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf6c4"></a> `00bbf6c4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf6c8"></a> `00bbf6c8` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf6cc"></a> `00bbf6cc` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf6d0"></a> `00bbf6d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf6d4"></a> `00bbf6d4` | `15 c1 03 91` | add x21,x8,#0xf0 | `FALL_THROUGH`
<a id="insn-00bbf6d8"></a> `00bbf6d8` | `6a 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf6dc"></a> `00bbf6dc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf6e0"></a> `00bbf6e0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf6e4"></a> `00bbf6e4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf6e8"></a> `00bbf6e8` | `9a 72 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf6ec"></a> `00bbf6ec` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf6f0"></a> `00bbf6f0` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf6f4"></a> `00bbf6f4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf6f8"></a> `00bbf6f8` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbf6fc"></a> `00bbf6fc` | `63 08 00 54` | b.cc 0x00bbf808 | `CONDITIONAL_JUMP`
<a id="insn-00bbf700"></a> `00bbf700` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbf704"></a> `00bbf704` | `28 08 00 b4` | cbz x8,0x00bbf808 | `CONDITIONAL_JUMP`
<a id="insn-00bbf708"></a> `00bbf708` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf70c"></a> `00bbf70c` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbf710"></a> `00bbf710` | `e9 a3 55 a9` | ldp x9,x8,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbf714"></a> `00bbf714` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf718"></a> `00bbf718` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf71c"></a> `00bbf71c` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbf720"></a> `00bbf720` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf724"></a> `00bbf724` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbf728"></a> `00bbf728` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbf72c"></a> `00bbf72c` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbf730"></a> `00bbf730` | `c2 00 00 54` | b.cs 0x00bbf748 | `CONDITIONAL_JUMP`
<a id="insn-00bbf734"></a> `00bbf734` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf738"></a> `00bbf738` | `00 21 04 91` | add x0,x8,#0x108 | `FALL_THROUGH`
<a id="insn-00bbf73c"></a> `00bbf73c` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbf740"></a> `00bbf740` | `b0 7b 02 94` | bl 0x00c5e600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf744"></a> `00bbf744` | `12 00 00 14` | b 0x00bbf78c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf748"></a> `00bbf748` | `29 02 00 54` | b.ls 0x00bbf78c | `CONDITIONAL_JUMP`
<a id="insn-00bbf74c"></a> `00bbf74c` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf750"></a> `00bbf750` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbf754"></a> `00bbf754` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbf758"></a> `00bbf758` | `80 01 00 54` | b.eq 0x00bbf788 | `CONDITIONAL_JUMP`
<a id="insn-00bbf75c"></a> `00bbf75c` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbf760"></a> `00bbf760` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbf764"></a> `00bbf764` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbf77c | `CONDITIONAL_JUMP`
<a id="insn-00bbf768"></a> `00bbf768` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbf76c"></a> `00bbf76c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbf770"></a> `00bbf770` | `c0 00 00 54` | b.eq 0x00bbf788 | `CONDITIONAL_JUMP`
<a id="insn-00bbf774"></a> `00bbf774` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbf778"></a> `00bbf778` | `89 ff 07 36` | tbz w9,#0x0,0x00bbf768 | `CONDITIONAL_JUMP`
<a id="insn-00bbf77c"></a> `00bbf77c` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbf780"></a> `00bbf780` | `f4 65 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf784"></a> `00bbf784` | `f9 ff ff 17` | b 0x00bbf768 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf788"></a> `00bbf788` | `f4 b3 00 f9` | str x20,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbf78c"></a> `00bbf78c` | `f3 03 00 34` | cbz w19,0x00bbf808 | `CONDITIONAL_JUMP`
<a id="insn-00bbf790"></a> `00bbf790` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbf794"></a> `00bbf794` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf798"></a> `00bbf798` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf79c"></a> `00bbf79c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf7a0"></a> `00bbf7a0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf7a4"></a> `00bbf7a4` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbf7a8"></a> `00bbf7a8` | `e3 00 00 54` | b.cc 0x00bbf7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7ac"></a> `00bbf7ac` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbf7b0"></a> `00bbf7b0` | `c8 00 00 b4` | cbz x8,0x00bbf7c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7b4"></a> `00bbf7b4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf7b8"></a> `00bbf7b8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf7bc"></a> `00bbf7bc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf7c0"></a> `00bbf7c0` | `02 00 00 14` | b 0x00bbf7c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf7c4"></a> `00bbf7c4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf7c8"></a> `00bbf7c8` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf7cc"></a> `00bbf7cc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf7d0"></a> `00bbf7d0` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbf7d4"></a> `00bbf7d4` | `ea af 40 f9` | ldr x10,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbf7d8"></a> `00bbf7d8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf7dc"></a> `00bbf7dc` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf7e0"></a> `00bbf7e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf7e4"></a> `00bbf7e4` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbf7e8"></a> `00bbf7e8` | `26 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf7ec"></a> `00bbf7ec` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf7f0"></a> `00bbf7f0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbf7f4"></a> `00bbf7f4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf7f8"></a> `00bbf7f8` | `56 72 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf7fc"></a> `00bbf7fc` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf800"></a> `00bbf800` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbf804"></a> `00bbf804` | `a1 fc ff 54` | b.ne 0x00bbf798 | `CONDITIONAL_JUMP`
<a id="insn-00bbf808"></a> `00bbf808` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbf80c"></a> `00bbf80c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf810"></a> `00bbf810` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf814"></a> `00bbf814` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bbf818"></a> `00bbf818` | `e3 00 00 54` | b.cc 0x00bbf834 | `CONDITIONAL_JUMP`
<a id="insn-00bbf81c"></a> `00bbf81c` | `08 39 40 79` | ldrh w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbf820"></a> `00bbf820` | `c8 00 00 b4` | cbz x8,0x00bbf838 | `CONDITIONAL_JUMP`
<a id="insn-00bbf824"></a> `00bbf824` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbf828"></a> `00bbf828` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf82c"></a> `00bbf82c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf830"></a> `00bbf830` | `02 00 00 14` | b 0x00bbf838 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf834"></a> `00bbf834` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbf838"></a> `00bbf838` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf83c"></a> `00bbf83c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbf840"></a> `00bbf840` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbf844"></a> `00bbf844` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbf848"></a> `00bbf848` | `0e 66 02 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf84c"></a> `00bbf84c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbf850"></a> `00bbf850` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbf854"></a> `00bbf854` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbf858"></a> `00bbf858` | `f3 e3 00 91` | add x19,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbf85c"></a> `00bbf85c` | `3d 72 02 94` | bl 0x00c5c150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf860"></a> `00bbf860` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf864"></a> `00bbf864` | `f3 bb 00 f9` | str x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbf868"></a> `00bbf868` | `e8 3f 01 f9` | str x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbf86c"></a> `00bbf86c` | `48 07 40 a9` | ldp x8,x1,[x26] | `FALL_THROUGH`
<a id="insn-00bbf870"></a> `00bbf870` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf874"></a> `00bbf874` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbf878"></a> `00bbf878` | `e8 3f 41 f9` | ldr x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbf87c"></a> `00bbf87c` | `68 00 00 b4` | cbz x8,0x00bbf888 | `CONDITIONAL_JUMP`
<a id="insn-00bbf880"></a> `00bbf880` | `1f 91 00 f9` | str xzr,[x8, #0x120] | `FALL_THROUGH`
<a id="insn-00bbf884"></a> `00bbf884` | `ff 3f 01 f9` | str xzr,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbf888"></a> `00bbf888` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbf88c"></a> `00bbf88c` | `68 00 00 36` | tbz w8,#0x0,0x00bbf898 | `CONDITIONAL_JUMP`
<a id="insn-00bbf890"></a> `00bbf890` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbf894"></a> `00bbf894` | `af 65 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf898"></a> `00bbf898` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbf89c"></a> `00bbf89c` | `b5 7a 02 94` | bl 0x00c5e370 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf8a0"></a> `00bbf8a0` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbf8a4"></a> `00bbf8a4` | `fb 7a 02 94` | bl 0x00c5e490 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf8a8"></a> `00bbf8a8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbf8ac"></a> `00bbf8ac` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbf8b0"></a> `00bbf8b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf8b4"></a> `00bbf8b4` | `21 01 00 54` | b.ne 0x00bbf8d8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8b8"></a> `00bbf8b8` | `ff 83 0b 91` | add sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbf8bc"></a> `00bbf8bc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf8c0"></a> `00bbf8c0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf8c4"></a> `00bbf8c4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf8c8"></a> `00bbf8c8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf8cc"></a> `00bbf8cc` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf8d0"></a> `00bbf8d0` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bbf8d4"></a> `00bbf8d4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbf8d8"></a> `00bbf8d8` | `aa 65 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbeadc`](#insn-00bbeadc) 範囲 `[['00bbeadc', '00bbeb1b']]`
  - `FALL_THROUGH` [`00bbeb18`](#insn-00bbeb18) → [`00bbeb1c`](#insn-00bbeb1c)
- ブロック [`00bbeb1c`](#insn-00bbeb1c) 範囲 `[['00bbeb1c', '00bbeba3']]`
  - `CONDITIONAL_JUMP` [`00bbeba0`](#insn-00bbeba0) → [`00bbebb8`](#insn-00bbebb8)
  - `FALL_THROUGH` [`00bbeba0`](#insn-00bbeba0) → [`00bbeba4`](#insn-00bbeba4)
- ブロック [`00bbeba4`](#insn-00bbeba4) 範囲 `[['00bbeba4', '00bbeba7']]`
  - `FALL_THROUGH` [`00bbeba4`](#insn-00bbeba4) → [`00bbeba8`](#insn-00bbeba8)
- ブロック [`00bbeba8`](#insn-00bbeba8) 範囲 `[['00bbeba8', '00bbebab']]`
  - `CONDITIONAL_JUMP` [`00bbeba8`](#insn-00bbeba8) → [`00bbebb8`](#insn-00bbebb8)
  - `FALL_THROUGH` [`00bbeba8`](#insn-00bbeba8) → [`00bbebac`](#insn-00bbebac)
- ブロック [`00bbebac`](#insn-00bbebac) 範囲 `[['00bbebac', '00bbebb7']]`
  - `FALL_THROUGH` [`00bbebb4`](#insn-00bbebb4) → [`00bbebb8`](#insn-00bbebb8)
- ブロック [`00bbebb8`](#insn-00bbebb8) 範囲 `[['00bbebb8', '00bbebf7']]`
  - `CONDITIONAL_JUMP` [`00bbebf4`](#insn-00bbebf4) → [`00bbec10`](#insn-00bbec10)
  - `FALL_THROUGH` [`00bbebf4`](#insn-00bbebf4) → [`00bbebf8`](#insn-00bbebf8)
- ブロック [`00bbebf8`](#insn-00bbebf8) 範囲 `[['00bbebf8', '00bbebff']]`
  - `CONDITIONAL_JUMP` [`00bbebfc`](#insn-00bbebfc) → [`00bbec14`](#insn-00bbec14)
  - `FALL_THROUGH` [`00bbebfc`](#insn-00bbebfc) → [`00bbec00`](#insn-00bbec00)
- ブロック [`00bbec00`](#insn-00bbec00) 範囲 `[['00bbec00', '00bbec0f']]`
  - `UNCONDITIONAL_JUMP` [`00bbec0c`](#insn-00bbec0c) → [`00bbec14`](#insn-00bbec14)
- ブロック [`00bbec10`](#insn-00bbec10) 範囲 `[['00bbec10', '00bbec13']]`
  - `FALL_THROUGH` [`00bbec10`](#insn-00bbec10) → [`00bbec14`](#insn-00bbec14)
- ブロック [`00bbec14`](#insn-00bbec14) 範囲 `[['00bbec14', '00bbec37']]`
  - `FALL_THROUGH` [`00bbec34`](#insn-00bbec34) → [`00bbec38`](#insn-00bbec38)
- ブロック [`00bbec38`](#insn-00bbec38) 範囲 `[['00bbec38', '00bbec57']]`
  - `CONDITIONAL_JUMP` [`00bbec54`](#insn-00bbec54) → [`00bbedfc`](#insn-00bbedfc)
  - `FALL_THROUGH` [`00bbec54`](#insn-00bbec54) → [`00bbec58`](#insn-00bbec58)
- ブロック [`00bbec58`](#insn-00bbec58) 範囲 `[['00bbec58', '00bbec5f']]`
  - `CONDITIONAL_JUMP` [`00bbec5c`](#insn-00bbec5c) → [`00bbedfc`](#insn-00bbedfc)
  - `FALL_THROUGH` [`00bbec5c`](#insn-00bbec5c) → [`00bbec60`](#insn-00bbec60)
- ブロック [`00bbec60`](#insn-00bbec60) 範囲 `[['00bbec60', '00bbec6f']]`
  - `CONDITIONAL_JUMP` [`00bbec6c`](#insn-00bbec6c) → [`00bbedfc`](#insn-00bbedfc)
  - `FALL_THROUGH` [`00bbec6c`](#insn-00bbec6c) → [`00bbec70`](#insn-00bbec70)
- ブロック [`00bbec70`](#insn-00bbec70) 範囲 `[['00bbec70', '00bbec77']]`
  - `CONDITIONAL_JUMP` [`00bbec74`](#insn-00bbec74) → [`00bbedfc`](#insn-00bbedfc)
  - `FALL_THROUGH` [`00bbec74`](#insn-00bbec74) → [`00bbec78`](#insn-00bbec78)
- ブロック [`00bbec78`](#insn-00bbec78) 範囲 `[['00bbec78', '00bbec8f']]`
  - `UNCONDITIONAL_JUMP` [`00bbec8c`](#insn-00bbec8c) → [`00bbeca0`](#insn-00bbeca0)
- ブロック [`00bbec90`](#insn-00bbec90) 範囲 `[['00bbec90', '00bbec9f']]`
  - `CONDITIONAL_JUMP` [`00bbec9c`](#insn-00bbec9c) → [`00bbedf0`](#insn-00bbedf0)
  - `FALL_THROUGH` [`00bbec9c`](#insn-00bbec9c) → [`00bbeca0`](#insn-00bbeca0)
- ブロック [`00bbeca0`](#insn-00bbeca0) 範囲 `[['00bbeca0', '00bbecd7']]`
  - `CONDITIONAL_JUMP` [`00bbecd4`](#insn-00bbecd4) → [`00bbed18`](#insn-00bbed18)
  - `FALL_THROUGH` [`00bbecd4`](#insn-00bbecd4) → [`00bbecd8`](#insn-00bbecd8)
- ブロック [`00bbecd8`](#insn-00bbecd8) 範囲 `[['00bbecd8', '00bbecdf']]`
  - `CONDITIONAL_JUMP` [`00bbecdc`](#insn-00bbecdc) → [`00bbecec`](#insn-00bbecec)
  - `FALL_THROUGH` [`00bbecdc`](#insn-00bbecdc) → [`00bbece0`](#insn-00bbece0)
- ブロック [`00bbece0`](#insn-00bbece0) 範囲 `[['00bbece0', '00bbeceb']]`
  - `FALL_THROUGH` [`00bbece8`](#insn-00bbece8) → [`00bbecec`](#insn-00bbecec)
- ブロック [`00bbecec`](#insn-00bbecec) 範囲 `[['00bbecec', '00bbecef']]`
  - `FALL_THROUGH` [`00bbecec`](#insn-00bbecec) → [`00bbecf0`](#insn-00bbecf0)
- ブロック [`00bbecf0`](#insn-00bbecf0) 範囲 `[['00bbecf0', '00bbecff']]`
  - `CONDITIONAL_JUMP` [`00bbecfc`](#insn-00bbecfc) → [`00bbed24`](#insn-00bbed24)
  - `FALL_THROUGH` [`00bbecfc`](#insn-00bbecfc) → [`00bbed00`](#insn-00bbed00)
- ブロック [`00bbed00`](#insn-00bbed00) 範囲 `[['00bbed00', '00bbed07']]`
  - `CONDITIONAL_JUMP` [`00bbed04`](#insn-00bbed04) → [`00bbed24`](#insn-00bbed24)
  - `FALL_THROUGH` [`00bbed04`](#insn-00bbed04) → [`00bbed08`](#insn-00bbed08)
- ブロック [`00bbed08`](#insn-00bbed08) 範囲 `[['00bbed08', '00bbed17']]`
  - `UNCONDITIONAL_JUMP` [`00bbed14`](#insn-00bbed14) → [`00bbed28`](#insn-00bbed28)
- ブロック [`00bbed18`](#insn-00bbed18) 範囲 `[['00bbed18', '00bbed23']]`
  - `UNCONDITIONAL_JUMP` [`00bbed20`](#insn-00bbed20) → [`00bbed28`](#insn-00bbed28)
- ブロック [`00bbed24`](#insn-00bbed24) 範囲 `[['00bbed24', '00bbed27']]`
  - `FALL_THROUGH` [`00bbed24`](#insn-00bbed24) → [`00bbed28`](#insn-00bbed28)
- ブロック [`00bbed28`](#insn-00bbed28) 範囲 `[['00bbed28', '00bbed57']]`
  - `CONDITIONAL_JUMP` [`00bbed54`](#insn-00bbed54) → [`00bbedc0`](#insn-00bbedc0)
  - `FALL_THROUGH` [`00bbed54`](#insn-00bbed54) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbed58`](#insn-00bbed58) 範囲 `[['00bbed58', '00bbed9b']]`
  - `CONDITIONAL_JUMP` [`00bbed98`](#insn-00bbed98) → [`00bbeda8`](#insn-00bbeda8)
  - `FALL_THROUGH` [`00bbed98`](#insn-00bbed98) → [`00bbed9c`](#insn-00bbed9c)
- ブロック [`00bbed9c`](#insn-00bbed9c) 範囲 `[['00bbed9c', '00bbeda7']]`
  - `UNCONDITIONAL_JUMP` [`00bbeda4`](#insn-00bbeda4) → [`00bbedac`](#insn-00bbedac)
- ブロック [`00bbeda8`](#insn-00bbeda8) 範囲 `[['00bbeda8', '00bbedab']]`
  - `FALL_THROUGH` [`00bbeda8`](#insn-00bbeda8) → [`00bbedac`](#insn-00bbedac)
- ブロック [`00bbedac`](#insn-00bbedac) 範囲 `[['00bbedac', '00bbedbf']]`
  - `FALL_THROUGH` [`00bbedbc`](#insn-00bbedbc) → [`00bbedc0`](#insn-00bbedc0)
- ブロック [`00bbedc0`](#insn-00bbedc0) 範囲 `[['00bbedc0', '00bbedc7']]`
  - `FALL_THROUGH` [`00bbedc4`](#insn-00bbedc4) → [`00bbedc8`](#insn-00bbedc8)
- ブロック [`00bbedc8`](#insn-00bbedc8) 範囲 `[['00bbedc8', '00bbede3']]`
  - `CONDITIONAL_JUMP` [`00bbede0`](#insn-00bbede0) → [`00bbec90`](#insn-00bbec90)
  - `FALL_THROUGH` [`00bbede0`](#insn-00bbede0) → [`00bbede4`](#insn-00bbede4)
- ブロック [`00bbede4`](#insn-00bbede4) 範囲 `[['00bbede4', '00bbedef']]`
  - `UNCONDITIONAL_JUMP` [`00bbedec`](#insn-00bbedec) → [`00bbec90`](#insn-00bbec90)
- ブロック [`00bbedf0`](#insn-00bbedf0) 範囲 `[['00bbedf0', '00bbedfb']]`
  - `FALL_THROUGH` [`00bbedf8`](#insn-00bbedf8) → [`00bbedfc`](#insn-00bbedfc)
- ブロック [`00bbedfc`](#insn-00bbedfc) 範囲 `[['00bbedfc', '00bbee0b']]`
  - `CONDITIONAL_JUMP` [`00bbee08`](#insn-00bbee08) → [`00bbeed0`](#insn-00bbeed0)
  - `FALL_THROUGH` [`00bbee08`](#insn-00bbee08) → [`00bbee0c`](#insn-00bbee0c)
- ブロック [`00bbee0c`](#insn-00bbee0c) 範囲 `[['00bbee0c', '00bbee13']]`
  - `CONDITIONAL_JUMP` [`00bbee10`](#insn-00bbee10) → [`00bbeed0`](#insn-00bbeed0)
  - `FALL_THROUGH` [`00bbee10`](#insn-00bbee10) → [`00bbee14`](#insn-00bbee14)
- ブロック [`00bbee14`](#insn-00bbee14) 範囲 `[['00bbee14', '00bbee1b']]`
  - `FALL_THROUGH` [`00bbee18`](#insn-00bbee18) → [`00bbee1c`](#insn-00bbee1c)
- ブロック [`00bbee1c`](#insn-00bbee1c) 範囲 `[['00bbee1c', '00bbee23']]`
  - `CONDITIONAL_JUMP` [`00bbee20`](#insn-00bbee20) → [`00bbeed0`](#insn-00bbeed0)
  - `FALL_THROUGH` [`00bbee20`](#insn-00bbee20) → [`00bbee24`](#insn-00bbee24)
- ブロック [`00bbee24`](#insn-00bbee24) 範囲 `[['00bbee24', '00bbee3b']]`
  - `CONDITIONAL_JUMP` [`00bbee38`](#insn-00bbee38) → [`00bbee80`](#insn-00bbee80)
  - `FALL_THROUGH` [`00bbee38`](#insn-00bbee38) → [`00bbee3c`](#insn-00bbee3c)
- ブロック [`00bbee3c`](#insn-00bbee3c) 範囲 `[['00bbee3c', '00bbee5b']]`
  - `FALL_THROUGH` [`00bbee58`](#insn-00bbee58) → [`00bbee5c`](#insn-00bbee5c)
- ブロック [`00bbee5c`](#insn-00bbee5c) 範囲 `[['00bbee5c', '00bbee5f']]`
  - `CONDITIONAL_JUMP` [`00bbee5c`](#insn-00bbee5c) → [`00bbee6c`](#insn-00bbee6c)
  - `FALL_THROUGH` [`00bbee5c`](#insn-00bbee5c) → [`00bbee60`](#insn-00bbee60)
- ブロック [`00bbee60`](#insn-00bbee60) 範囲 `[['00bbee60', '00bbee6b']]`
  - `FALL_THROUGH` [`00bbee68`](#insn-00bbee68) → [`00bbee6c`](#insn-00bbee6c)
- ブロック [`00bbee6c`](#insn-00bbee6c) 範囲 `[['00bbee6c', '00bbee77']]`
  - `CONDITIONAL_JUMP` [`00bbee74`](#insn-00bbee74) → [`00bbee80`](#insn-00bbee80)
  - `FALL_THROUGH` [`00bbee74`](#insn-00bbee74) → [`00bbee78`](#insn-00bbee78)
- ブロック [`00bbee78`](#insn-00bbee78) 範囲 `[['00bbee78', '00bbee7f']]`
  - `FALL_THROUGH` [`00bbee7c`](#insn-00bbee7c) → [`00bbee80`](#insn-00bbee80)
- ブロック [`00bbee80`](#insn-00bbee80) 範囲 `[['00bbee80', '00bbeecf']]`
  - `FALL_THROUGH` [`00bbeecc`](#insn-00bbeecc) → [`00bbeed0`](#insn-00bbeed0)
- ブロック [`00bbeed0`](#insn-00bbeed0) 範囲 `[['00bbeed0', '00bbeedf']]`
  - `CONDITIONAL_JUMP` [`00bbeedc`](#insn-00bbeedc) → [`00bbeef8`](#insn-00bbeef8)
  - `FALL_THROUGH` [`00bbeedc`](#insn-00bbeedc) → [`00bbeee0`](#insn-00bbeee0)
- ブロック [`00bbeee0`](#insn-00bbeee0) 範囲 `[['00bbeee0', '00bbeee7']]`
  - `CONDITIONAL_JUMP` [`00bbeee4`](#insn-00bbeee4) → [`00bbeefc`](#insn-00bbeefc)
  - `FALL_THROUGH` [`00bbeee4`](#insn-00bbeee4) → [`00bbeee8`](#insn-00bbeee8)
- ブロック [`00bbeee8`](#insn-00bbeee8) 範囲 `[['00bbeee8', '00bbeef7']]`
  - `UNCONDITIONAL_JUMP` [`00bbeef4`](#insn-00bbeef4) → [`00bbeefc`](#insn-00bbeefc)
- ブロック [`00bbeef8`](#insn-00bbeef8) 範囲 `[['00bbeef8', '00bbeefb']]`
  - `FALL_THROUGH` [`00bbeef8`](#insn-00bbeef8) → [`00bbeefc`](#insn-00bbeefc)
- ブロック [`00bbeefc`](#insn-00bbeefc) 範囲 `[['00bbeefc', '00bbef3b']]`
  - `CONDITIONAL_JUMP` [`00bbef38`](#insn-00bbef38) → [`00bbef54`](#insn-00bbef54)
  - `FALL_THROUGH` [`00bbef38`](#insn-00bbef38) → [`00bbef3c`](#insn-00bbef3c)
- ブロック [`00bbef3c`](#insn-00bbef3c) 範囲 `[['00bbef3c', '00bbef43']]`
  - `CONDITIONAL_JUMP` [`00bbef40`](#insn-00bbef40) → [`00bbef58`](#insn-00bbef58)
  - `FALL_THROUGH` [`00bbef40`](#insn-00bbef40) → [`00bbef44`](#insn-00bbef44)
- ブロック [`00bbef44`](#insn-00bbef44) 範囲 `[['00bbef44', '00bbef53']]`
  - `UNCONDITIONAL_JUMP` [`00bbef50`](#insn-00bbef50) → [`00bbef58`](#insn-00bbef58)
- ブロック [`00bbef54`](#insn-00bbef54) 範囲 `[['00bbef54', '00bbef57']]`
  - `FALL_THROUGH` [`00bbef54`](#insn-00bbef54) → [`00bbef58`](#insn-00bbef58)
- ブロック [`00bbef58`](#insn-00bbef58) 範囲 `[['00bbef58', '00bbef73']]`
  - `FALL_THROUGH` [`00bbef70`](#insn-00bbef70) → [`00bbef74`](#insn-00bbef74)
- ブロック [`00bbef74`](#insn-00bbef74) 範囲 `[['00bbef74', '00bbef9b']]`
  - `CONDITIONAL_JUMP` [`00bbef98`](#insn-00bbef98) → [`00bbefb4`](#insn-00bbefb4)
  - `FALL_THROUGH` [`00bbef98`](#insn-00bbef98) → [`00bbef9c`](#insn-00bbef9c)
- ブロック [`00bbef9c`](#insn-00bbef9c) 範囲 `[['00bbef9c', '00bbefa3']]`
  - `CONDITIONAL_JUMP` [`00bbefa0`](#insn-00bbefa0) → [`00bbefb8`](#insn-00bbefb8)
  - `FALL_THROUGH` [`00bbefa0`](#insn-00bbefa0) → [`00bbefa4`](#insn-00bbefa4)
- ブロック [`00bbefa4`](#insn-00bbefa4) 範囲 `[['00bbefa4', '00bbefab']]`
  - `FALL_THROUGH` [`00bbefa8`](#insn-00bbefa8) → [`00bbefac`](#insn-00bbefac)
- ブロック [`00bbefac`](#insn-00bbefac) 範囲 `[['00bbefac', '00bbefb3']]`
  - `UNCONDITIONAL_JUMP` [`00bbefb0`](#insn-00bbefb0) → [`00bbefb8`](#insn-00bbefb8)
- ブロック [`00bbefb4`](#insn-00bbefb4) 範囲 `[['00bbefb4', '00bbefb7']]`
  - `FALL_THROUGH` [`00bbefb4`](#insn-00bbefb4) → [`00bbefb8`](#insn-00bbefb8)
- ブロック [`00bbefb8`](#insn-00bbefb8) 範囲 `[['00bbefb8', '00bbefc7']]`
  - `FALL_THROUGH` [`00bbefc4`](#insn-00bbefc4) → [`00bbefc8`](#insn-00bbefc8)
- ブロック [`00bbefc8`](#insn-00bbefc8) 範囲 `[['00bbefc8', '00bbefdf']]`
  - `FALL_THROUGH` [`00bbefdc`](#insn-00bbefdc) → [`00bbefe0`](#insn-00bbefe0)
- ブロック [`00bbefe0`](#insn-00bbefe0) 範囲 `[['00bbefe0', '00bbefe3']]`
  - `FALL_THROUGH` [`00bbefe0`](#insn-00bbefe0) → [`00bbefe4`](#insn-00bbefe4)
- ブロック [`00bbefe4`](#insn-00bbefe4) 範囲 `[['00bbefe4', '00bbefe7']]`
  - `FALL_THROUGH` [`00bbefe4`](#insn-00bbefe4) → [`00bbefe8`](#insn-00bbefe8)
- ブロック [`00bbefe8`](#insn-00bbefe8) 範囲 `[['00bbefe8', '00bbefeb']]`
  - `FALL_THROUGH` [`00bbefe8`](#insn-00bbefe8) → [`00bbefec`](#insn-00bbefec)
- ブロック [`00bbefec`](#insn-00bbefec) 範囲 `[['00bbefec', '00bbefef']]`
  - `CONDITIONAL_JUMP` [`00bbefec`](#insn-00bbefec) → [`00bbf008`](#insn-00bbf008)
  - `FALL_THROUGH` [`00bbefec`](#insn-00bbefec) → [`00bbeff0`](#insn-00bbeff0)
- ブロック [`00bbeff0`](#insn-00bbeff0) 範囲 `[['00bbeff0', '00bbeff7']]`
  - `CONDITIONAL_JUMP` [`00bbeff4`](#insn-00bbeff4) → [`00bbf00c`](#insn-00bbf00c)
  - `FALL_THROUGH` [`00bbeff4`](#insn-00bbeff4) → [`00bbeff8`](#insn-00bbeff8)
- ブロック [`00bbeff8`](#insn-00bbeff8) 範囲 `[['00bbeff8', '00bbeffb']]`
  - `FALL_THROUGH` [`00bbeff8`](#insn-00bbeff8) → [`00bbeffc`](#insn-00bbeffc)
- ブロック [`00bbeffc`](#insn-00bbeffc) 範囲 `[['00bbeffc', '00bbf007']]`
  - `UNCONDITIONAL_JUMP` [`00bbf004`](#insn-00bbf004) → [`00bbf00c`](#insn-00bbf00c)
- ブロック [`00bbf008`](#insn-00bbf008) 範囲 `[['00bbf008', '00bbf00b']]`
  - `FALL_THROUGH` [`00bbf008`](#insn-00bbf008) → [`00bbf00c`](#insn-00bbf00c)
- ブロック [`00bbf00c`](#insn-00bbf00c) 範囲 `[['00bbf00c', '00bbf00f']]`
  - `FALL_THROUGH` [`00bbf00c`](#insn-00bbf00c) → [`00bbf010`](#insn-00bbf010)
- ブロック [`00bbf010`](#insn-00bbf010) 範囲 `[['00bbf010', '00bbf013']]`
  - `FALL_THROUGH` [`00bbf010`](#insn-00bbf010) → [`00bbf014`](#insn-00bbf014)
- ブロック [`00bbf014`](#insn-00bbf014) 範囲 `[['00bbf014', '00bbf02b']]`
  - `FALL_THROUGH` [`00bbf028`](#insn-00bbf028) → [`00bbf02c`](#insn-00bbf02c)
- ブロック [`00bbf02c`](#insn-00bbf02c) 範囲 `[['00bbf02c', '00bbf037']]`
  - `FALL_THROUGH` [`00bbf034`](#insn-00bbf034) → [`00bbf038`](#insn-00bbf038)
- ブロック [`00bbf038`](#insn-00bbf038) 範囲 `[['00bbf038', '00bbf03b']]`
  - `FALL_THROUGH` [`00bbf038`](#insn-00bbf038) → [`00bbf03c`](#insn-00bbf03c)
- ブロック [`00bbf03c`](#insn-00bbf03c) 範囲 `[['00bbf03c', '00bbf043']]`
  - `FALL_THROUGH` [`00bbf040`](#insn-00bbf040) → [`00bbf044`](#insn-00bbf044)
- ブロック [`00bbf044`](#insn-00bbf044) 範囲 `[['00bbf044', '00bbf04b']]`
  - `CONDITIONAL_JUMP` [`00bbf048`](#insn-00bbf048) → [`00bbf084`](#insn-00bbf084)
  - `FALL_THROUGH` [`00bbf048`](#insn-00bbf048) → [`00bbf04c`](#insn-00bbf04c)
- ブロック [`00bbf04c`](#insn-00bbf04c) 範囲 `[['00bbf04c', '00bbf053']]`
  - `CONDITIONAL_JUMP` [`00bbf050`](#insn-00bbf050) → [`00bbf060`](#insn-00bbf060)
  - `FALL_THROUGH` [`00bbf050`](#insn-00bbf050) → [`00bbf054`](#insn-00bbf054)
- ブロック [`00bbf054`](#insn-00bbf054) 範囲 `[['00bbf054', '00bbf05f']]`
  - `FALL_THROUGH` [`00bbf05c`](#insn-00bbf05c) → [`00bbf060`](#insn-00bbf060)
- ブロック [`00bbf060`](#insn-00bbf060) 範囲 `[['00bbf060', '00bbf063']]`
  - `FALL_THROUGH` [`00bbf060`](#insn-00bbf060) → [`00bbf064`](#insn-00bbf064)
- ブロック [`00bbf064`](#insn-00bbf064) 範囲 `[['00bbf064', '00bbf067']]`
  - `FALL_THROUGH` [`00bbf064`](#insn-00bbf064) → [`00bbf068`](#insn-00bbf068)
- ブロック [`00bbf068`](#insn-00bbf068) 範囲 `[['00bbf068', '00bbf06b']]`
  - `CONDITIONAL_JUMP` [`00bbf068`](#insn-00bbf068) → [`00bbf090`](#insn-00bbf090)
  - `FALL_THROUGH` [`00bbf068`](#insn-00bbf068) → [`00bbf06c`](#insn-00bbf06c)
- ブロック [`00bbf06c`](#insn-00bbf06c) 範囲 `[['00bbf06c', '00bbf06f']]`
  - `FALL_THROUGH` [`00bbf06c`](#insn-00bbf06c) → [`00bbf070`](#insn-00bbf070)
- ブロック [`00bbf070`](#insn-00bbf070) 範囲 `[['00bbf070', '00bbf073']]`
  - `CONDITIONAL_JUMP` [`00bbf070`](#insn-00bbf070) → [`00bbf094`](#insn-00bbf094)
  - `FALL_THROUGH` [`00bbf070`](#insn-00bbf070) → [`00bbf074`](#insn-00bbf074)
- ブロック [`00bbf074`](#insn-00bbf074) 範囲 `[['00bbf074', '00bbf077']]`
  - `FALL_THROUGH` [`00bbf074`](#insn-00bbf074) → [`00bbf078`](#insn-00bbf078)
- ブロック [`00bbf078`](#insn-00bbf078) 範囲 `[['00bbf078', '00bbf083']]`
  - `UNCONDITIONAL_JUMP` [`00bbf080`](#insn-00bbf080) → [`00bbf094`](#insn-00bbf094)
- ブロック [`00bbf084`](#insn-00bbf084) 範囲 `[['00bbf084', '00bbf08f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf08c`](#insn-00bbf08c) → [`00bbf094`](#insn-00bbf094)
- ブロック [`00bbf090`](#insn-00bbf090) 範囲 `[['00bbf090', '00bbf093']]`
  - `FALL_THROUGH` [`00bbf090`](#insn-00bbf090) → [`00bbf094`](#insn-00bbf094)
- ブロック [`00bbf094`](#insn-00bbf094) 範囲 `[['00bbf094', '00bbf0cb']]`
  - `CONDITIONAL_JUMP` [`00bbf0c8`](#insn-00bbf0c8) → [`00bbf0e4`](#insn-00bbf0e4)
  - `FALL_THROUGH` [`00bbf0c8`](#insn-00bbf0c8) → [`00bbf0cc`](#insn-00bbf0cc)
- ブロック [`00bbf0cc`](#insn-00bbf0cc) 範囲 `[['00bbf0cc', '00bbf0d3']]`
  - `CONDITIONAL_JUMP` [`00bbf0d0`](#insn-00bbf0d0) → [`00bbf0e8`](#insn-00bbf0e8)
  - `FALL_THROUGH` [`00bbf0d0`](#insn-00bbf0d0) → [`00bbf0d4`](#insn-00bbf0d4)
- ブロック [`00bbf0d4`](#insn-00bbf0d4) 範囲 `[['00bbf0d4', '00bbf0e3']]`
  - `UNCONDITIONAL_JUMP` [`00bbf0e0`](#insn-00bbf0e0) → [`00bbf0e8`](#insn-00bbf0e8)
- ブロック [`00bbf0e4`](#insn-00bbf0e4) 範囲 `[['00bbf0e4', '00bbf0e7']]`
  - `FALL_THROUGH` [`00bbf0e4`](#insn-00bbf0e4) → [`00bbf0e8`](#insn-00bbf0e8)
- ブロック [`00bbf0e8`](#insn-00bbf0e8) 範囲 `[['00bbf0e8', '00bbf127']]`
  - `CONDITIONAL_JUMP` [`00bbf124`](#insn-00bbf124) → [`00bbf140`](#insn-00bbf140)
  - `FALL_THROUGH` [`00bbf124`](#insn-00bbf124) → [`00bbf128`](#insn-00bbf128)
- ブロック [`00bbf128`](#insn-00bbf128) 範囲 `[['00bbf128', '00bbf12f']]`
  - `CONDITIONAL_JUMP` [`00bbf12c`](#insn-00bbf12c) → [`00bbf144`](#insn-00bbf144)
  - `FALL_THROUGH` [`00bbf12c`](#insn-00bbf12c) → [`00bbf130`](#insn-00bbf130)
- ブロック [`00bbf130`](#insn-00bbf130) 範囲 `[['00bbf130', '00bbf13f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf13c`](#insn-00bbf13c) → [`00bbf144`](#insn-00bbf144)
- ブロック [`00bbf140`](#insn-00bbf140) 範囲 `[['00bbf140', '00bbf143']]`
  - `FALL_THROUGH` [`00bbf140`](#insn-00bbf140) → [`00bbf144`](#insn-00bbf144)
- ブロック [`00bbf144`](#insn-00bbf144) 範囲 `[['00bbf144', '00bbf183']]`
  - `CONDITIONAL_JUMP` [`00bbf180`](#insn-00bbf180) → [`00bbf19c`](#insn-00bbf19c)
  - `FALL_THROUGH` [`00bbf180`](#insn-00bbf180) → [`00bbf184`](#insn-00bbf184)
- ブロック [`00bbf184`](#insn-00bbf184) 範囲 `[['00bbf184', '00bbf18b']]`
  - `CONDITIONAL_JUMP` [`00bbf188`](#insn-00bbf188) → [`00bbf1a0`](#insn-00bbf1a0)
  - `FALL_THROUGH` [`00bbf188`](#insn-00bbf188) → [`00bbf18c`](#insn-00bbf18c)
- ブロック [`00bbf18c`](#insn-00bbf18c) 範囲 `[['00bbf18c', '00bbf19b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf198`](#insn-00bbf198) → [`00bbf1a0`](#insn-00bbf1a0)
- ブロック [`00bbf19c`](#insn-00bbf19c) 範囲 `[['00bbf19c', '00bbf19f']]`
  - `FALL_THROUGH` [`00bbf19c`](#insn-00bbf19c) → [`00bbf1a0`](#insn-00bbf1a0)
- ブロック [`00bbf1a0`](#insn-00bbf1a0) 範囲 `[['00bbf1a0', '00bbf1df']]`
  - `CONDITIONAL_JUMP` [`00bbf1dc`](#insn-00bbf1dc) → [`00bbf1fc`](#insn-00bbf1fc)
  - `FALL_THROUGH` [`00bbf1dc`](#insn-00bbf1dc) → [`00bbf1e0`](#insn-00bbf1e0)
- ブロック [`00bbf1e0`](#insn-00bbf1e0) 範囲 `[['00bbf1e0', '00bbf1e7']]`
  - `CONDITIONAL_JUMP` [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1e8`](#insn-00bbf1e8)
- ブロック [`00bbf1e8`](#insn-00bbf1e8) 範囲 `[['00bbf1e8', '00bbf1eb']]`
  - `FALL_THROUGH` [`00bbf1e8`](#insn-00bbf1e8) → [`00bbf1ec`](#insn-00bbf1ec)
- ブロック [`00bbf1ec`](#insn-00bbf1ec) 範囲 `[['00bbf1ec', '00bbf1f7']]`
  - `CONDITIONAL_JUMP` [`00bbf1f4`](#insn-00bbf1f4) → [`00bbf210`](#insn-00bbf210)
  - `FALL_THROUGH` [`00bbf1f4`](#insn-00bbf1f4) → [`00bbf1f8`](#insn-00bbf1f8)
- ブロック [`00bbf1f8`](#insn-00bbf1f8) 範囲 `[['00bbf1f8', '00bbf1fb']]`
  - `UNCONDITIONAL_JUMP` [`00bbf1f8`](#insn-00bbf1f8) → [`00bbf214`](#insn-00bbf214)
- ブロック [`00bbf1fc`](#insn-00bbf1fc) 範囲 `[['00bbf1fc', '00bbf207']]`
  - `CONDITIONAL_JUMP` [`00bbf204`](#insn-00bbf204) → [`00bbf264`](#insn-00bbf264)
  - `FALL_THROUGH` [`00bbf204`](#insn-00bbf204) → [`00bbf208`](#insn-00bbf208)
- ブロック [`00bbf208`](#insn-00bbf208) 範囲 `[['00bbf208', '00bbf20f']]`
  - `CONDITIONAL_JUMP` [`00bbf20c`](#insn-00bbf20c) → [`00bbf214`](#insn-00bbf214)
  - `FALL_THROUGH` [`00bbf20c`](#insn-00bbf20c) → [`00bbf210`](#insn-00bbf210)
- ブロック [`00bbf210`](#insn-00bbf210) 範囲 `[['00bbf210', '00bbf213']]`
  - `FALL_THROUGH` [`00bbf210`](#insn-00bbf210) → [`00bbf214`](#insn-00bbf214)
- ブロック [`00bbf214`](#insn-00bbf214) 範囲 `[['00bbf214', '00bbf21f']]`
  - `CONDITIONAL_JUMP` [`00bbf21c`](#insn-00bbf21c) → [`00bbf86c`](#insn-00bbf86c)
  - `FALL_THROUGH` [`00bbf21c`](#insn-00bbf21c) → [`00bbf220`](#insn-00bbf220)
- ブロック [`00bbf220`](#insn-00bbf220) 範囲 `[['00bbf220', '00bbf227']]`
  - `CONDITIONAL_JUMP` [`00bbf224`](#insn-00bbf224) → [`00bbf86c`](#insn-00bbf86c)
  - `FALL_THROUGH` [`00bbf224`](#insn-00bbf224) → [`00bbf228`](#insn-00bbf228)
- ブロック [`00bbf228`](#insn-00bbf228) 範囲 `[['00bbf228', '00bbf237']]`
  - `CONDITIONAL_JUMP` [`00bbf234`](#insn-00bbf234) → [`00bbf86c`](#insn-00bbf86c)
  - `FALL_THROUGH` [`00bbf234`](#insn-00bbf234) → [`00bbf238`](#insn-00bbf238)
- ブロック [`00bbf238`](#insn-00bbf238) 範囲 `[['00bbf238', '00bbf24b']]`
  - `CONDITIONAL_JUMP` [`00bbf248`](#insn-00bbf248) → [`00bbf26c`](#insn-00bbf26c)
  - `FALL_THROUGH` [`00bbf248`](#insn-00bbf248) → [`00bbf24c`](#insn-00bbf24c)
- ブロック [`00bbf24c`](#insn-00bbf24c) 範囲 `[['00bbf24c', '00bbf253']]`
  - `CONDITIONAL_JUMP` [`00bbf250`](#insn-00bbf250) → [`00bbf270`](#insn-00bbf270)
  - `FALL_THROUGH` [`00bbf250`](#insn-00bbf250) → [`00bbf254`](#insn-00bbf254)
- ブロック [`00bbf254`](#insn-00bbf254) 範囲 `[['00bbf254', '00bbf263']]`
  - `UNCONDITIONAL_JUMP` [`00bbf260`](#insn-00bbf260) → [`00bbf270`](#insn-00bbf270)
- ブロック [`00bbf264`](#insn-00bbf264) 範囲 `[['00bbf264', '00bbf26b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf268`](#insn-00bbf268) → [`00bbf86c`](#insn-00bbf86c)
- ブロック [`00bbf26c`](#insn-00bbf26c) 範囲 `[['00bbf26c', '00bbf26f']]`
  - `FALL_THROUGH` [`00bbf26c`](#insn-00bbf26c) → [`00bbf270`](#insn-00bbf270)
- ブロック [`00bbf270`](#insn-00bbf270) 範囲 `[['00bbf270', '00bbf2a7']]`
  - `CONDITIONAL_JUMP` [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf2c0`](#insn-00bbf2c0)
  - `FALL_THROUGH` [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf2a8`](#insn-00bbf2a8)
- ブロック [`00bbf2a8`](#insn-00bbf2a8) 範囲 `[['00bbf2a8', '00bbf2af']]`
  - `CONDITIONAL_JUMP` [`00bbf2ac`](#insn-00bbf2ac) → [`00bbf2c4`](#insn-00bbf2c4)
  - `FALL_THROUGH` [`00bbf2ac`](#insn-00bbf2ac) → [`00bbf2b0`](#insn-00bbf2b0)
- ブロック [`00bbf2b0`](#insn-00bbf2b0) 範囲 `[['00bbf2b0', '00bbf2bf']]`
  - `UNCONDITIONAL_JUMP` [`00bbf2bc`](#insn-00bbf2bc) → [`00bbf2c4`](#insn-00bbf2c4)
- ブロック [`00bbf2c0`](#insn-00bbf2c0) 範囲 `[['00bbf2c0', '00bbf2c3']]`
  - `FALL_THROUGH` [`00bbf2c0`](#insn-00bbf2c0) → [`00bbf2c4`](#insn-00bbf2c4)
- ブロック [`00bbf2c4`](#insn-00bbf2c4) 範囲 `[['00bbf2c4', '00bbf303']]`
  - `CONDITIONAL_JUMP` [`00bbf300`](#insn-00bbf300) → [`00bbf31c`](#insn-00bbf31c)
  - `FALL_THROUGH` [`00bbf300`](#insn-00bbf300) → [`00bbf304`](#insn-00bbf304)
- ブロック [`00bbf304`](#insn-00bbf304) 範囲 `[['00bbf304', '00bbf30b']]`
  - `CONDITIONAL_JUMP` [`00bbf308`](#insn-00bbf308) → [`00bbf320`](#insn-00bbf320)
  - `FALL_THROUGH` [`00bbf308`](#insn-00bbf308) → [`00bbf30c`](#insn-00bbf30c)
- ブロック [`00bbf30c`](#insn-00bbf30c) 範囲 `[['00bbf30c', '00bbf31b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf318`](#insn-00bbf318) → [`00bbf320`](#insn-00bbf320)
- ブロック [`00bbf31c`](#insn-00bbf31c) 範囲 `[['00bbf31c', '00bbf31f']]`
  - `FALL_THROUGH` [`00bbf31c`](#insn-00bbf31c) → [`00bbf320`](#insn-00bbf320)
- ブロック [`00bbf320`](#insn-00bbf320) 範囲 `[['00bbf320', '00bbf35f']]`
  - `CONDITIONAL_JUMP` [`00bbf35c`](#insn-00bbf35c) → [`00bbf378`](#insn-00bbf378)
  - `FALL_THROUGH` [`00bbf35c`](#insn-00bbf35c) → [`00bbf360`](#insn-00bbf360)
- ブロック [`00bbf360`](#insn-00bbf360) 範囲 `[['00bbf360', '00bbf367']]`
  - `CONDITIONAL_JUMP` [`00bbf364`](#insn-00bbf364) → [`00bbf37c`](#insn-00bbf37c)
  - `FALL_THROUGH` [`00bbf364`](#insn-00bbf364) → [`00bbf368`](#insn-00bbf368)
- ブロック [`00bbf368`](#insn-00bbf368) 範囲 `[['00bbf368', '00bbf377']]`
  - `UNCONDITIONAL_JUMP` [`00bbf374`](#insn-00bbf374) → [`00bbf37c`](#insn-00bbf37c)
- ブロック [`00bbf378`](#insn-00bbf378) 範囲 `[['00bbf378', '00bbf37b']]`
  - `FALL_THROUGH` [`00bbf378`](#insn-00bbf378) → [`00bbf37c`](#insn-00bbf37c)
- ブロック [`00bbf37c`](#insn-00bbf37c) 範囲 `[['00bbf37c', '00bbf3bb']]`
  - `CONDITIONAL_JUMP` [`00bbf3b8`](#insn-00bbf3b8) → [`00bbf3d4`](#insn-00bbf3d4)
  - `FALL_THROUGH` [`00bbf3b8`](#insn-00bbf3b8) → [`00bbf3bc`](#insn-00bbf3bc)
- ブロック [`00bbf3bc`](#insn-00bbf3bc) 範囲 `[['00bbf3bc', '00bbf3c3']]`
  - `CONDITIONAL_JUMP` [`00bbf3c0`](#insn-00bbf3c0) → [`00bbf3d8`](#insn-00bbf3d8)
  - `FALL_THROUGH` [`00bbf3c0`](#insn-00bbf3c0) → [`00bbf3c4`](#insn-00bbf3c4)
- ブロック [`00bbf3c4`](#insn-00bbf3c4) 範囲 `[['00bbf3c4', '00bbf3d3']]`
  - `UNCONDITIONAL_JUMP` [`00bbf3d0`](#insn-00bbf3d0) → [`00bbf3d8`](#insn-00bbf3d8)
- ブロック [`00bbf3d4`](#insn-00bbf3d4) 範囲 `[['00bbf3d4', '00bbf3d7']]`
  - `FALL_THROUGH` [`00bbf3d4`](#insn-00bbf3d4) → [`00bbf3d8`](#insn-00bbf3d8)
- ブロック [`00bbf3d8`](#insn-00bbf3d8) 範囲 `[['00bbf3d8', '00bbf417']]`
  - `CONDITIONAL_JUMP` [`00bbf414`](#insn-00bbf414) → [`00bbf430`](#insn-00bbf430)
  - `FALL_THROUGH` [`00bbf414`](#insn-00bbf414) → [`00bbf418`](#insn-00bbf418)
- ブロック [`00bbf418`](#insn-00bbf418) 範囲 `[['00bbf418', '00bbf41f']]`
  - `CONDITIONAL_JUMP` [`00bbf41c`](#insn-00bbf41c) → [`00bbf434`](#insn-00bbf434)
  - `FALL_THROUGH` [`00bbf41c`](#insn-00bbf41c) → [`00bbf420`](#insn-00bbf420)
- ブロック [`00bbf420`](#insn-00bbf420) 範囲 `[['00bbf420', '00bbf42f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf42c`](#insn-00bbf42c) → [`00bbf434`](#insn-00bbf434)
- ブロック [`00bbf430`](#insn-00bbf430) 範囲 `[['00bbf430', '00bbf433']]`
  - `FALL_THROUGH` [`00bbf430`](#insn-00bbf430) → [`00bbf434`](#insn-00bbf434)
- ブロック [`00bbf434`](#insn-00bbf434) 範囲 `[['00bbf434', '00bbf473']]`
  - `CONDITIONAL_JUMP` [`00bbf470`](#insn-00bbf470) → [`00bbf48c`](#insn-00bbf48c)
  - `FALL_THROUGH` [`00bbf470`](#insn-00bbf470) → [`00bbf474`](#insn-00bbf474)
- ブロック [`00bbf474`](#insn-00bbf474) 範囲 `[['00bbf474', '00bbf47b']]`
  - `CONDITIONAL_JUMP` [`00bbf478`](#insn-00bbf478) → [`00bbf490`](#insn-00bbf490)
  - `FALL_THROUGH` [`00bbf478`](#insn-00bbf478) → [`00bbf47c`](#insn-00bbf47c)
- ブロック [`00bbf47c`](#insn-00bbf47c) 範囲 `[['00bbf47c', '00bbf48b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf488`](#insn-00bbf488) → [`00bbf490`](#insn-00bbf490)
- ブロック [`00bbf48c`](#insn-00bbf48c) 範囲 `[['00bbf48c', '00bbf48f']]`
  - `FALL_THROUGH` [`00bbf48c`](#insn-00bbf48c) → [`00bbf490`](#insn-00bbf490)
- ブロック [`00bbf490`](#insn-00bbf490) 範囲 `[['00bbf490', '00bbf4cf']]`
  - `CONDITIONAL_JUMP` [`00bbf4cc`](#insn-00bbf4cc) → [`00bbf4e8`](#insn-00bbf4e8)
  - `FALL_THROUGH` [`00bbf4cc`](#insn-00bbf4cc) → [`00bbf4d0`](#insn-00bbf4d0)
- ブロック [`00bbf4d0`](#insn-00bbf4d0) 範囲 `[['00bbf4d0', '00bbf4d7']]`
  - `CONDITIONAL_JUMP` [`00bbf4d4`](#insn-00bbf4d4) → [`00bbf4ec`](#insn-00bbf4ec)
  - `FALL_THROUGH` [`00bbf4d4`](#insn-00bbf4d4) → [`00bbf4d8`](#insn-00bbf4d8)
- ブロック [`00bbf4d8`](#insn-00bbf4d8) 範囲 `[['00bbf4d8', '00bbf4e7']]`
  - `UNCONDITIONAL_JUMP` [`00bbf4e4`](#insn-00bbf4e4) → [`00bbf4ec`](#insn-00bbf4ec)
- ブロック [`00bbf4e8`](#insn-00bbf4e8) 範囲 `[['00bbf4e8', '00bbf4eb']]`
  - `FALL_THROUGH` [`00bbf4e8`](#insn-00bbf4e8) → [`00bbf4ec`](#insn-00bbf4ec)
- ブロック [`00bbf4ec`](#insn-00bbf4ec) 範囲 `[['00bbf4ec', '00bbf52b']]`
  - `CONDITIONAL_JUMP` [`00bbf528`](#insn-00bbf528) → [`00bbf544`](#insn-00bbf544)
  - `FALL_THROUGH` [`00bbf528`](#insn-00bbf528) → [`00bbf52c`](#insn-00bbf52c)
- ブロック [`00bbf52c`](#insn-00bbf52c) 範囲 `[['00bbf52c', '00bbf533']]`
  - `CONDITIONAL_JUMP` [`00bbf530`](#insn-00bbf530) → [`00bbf548`](#insn-00bbf548)
  - `FALL_THROUGH` [`00bbf530`](#insn-00bbf530) → [`00bbf534`](#insn-00bbf534)
- ブロック [`00bbf534`](#insn-00bbf534) 範囲 `[['00bbf534', '00bbf543']]`
  - `UNCONDITIONAL_JUMP` [`00bbf540`](#insn-00bbf540) → [`00bbf548`](#insn-00bbf548)
- ブロック [`00bbf544`](#insn-00bbf544) 範囲 `[['00bbf544', '00bbf547']]`
  - `FALL_THROUGH` [`00bbf544`](#insn-00bbf544) → [`00bbf548`](#insn-00bbf548)
- ブロック [`00bbf548`](#insn-00bbf548) 範囲 `[['00bbf548', '00bbf587']]`
  - `CONDITIONAL_JUMP` [`00bbf584`](#insn-00bbf584) → [`00bbf690`](#insn-00bbf690)
  - `FALL_THROUGH` [`00bbf584`](#insn-00bbf584) → [`00bbf588`](#insn-00bbf588)
- ブロック [`00bbf588`](#insn-00bbf588) 範囲 `[['00bbf588', '00bbf58f']]`
  - `CONDITIONAL_JUMP` [`00bbf58c`](#insn-00bbf58c) → [`00bbf690`](#insn-00bbf690)
  - `FALL_THROUGH` [`00bbf58c`](#insn-00bbf58c) → [`00bbf590`](#insn-00bbf590)
- ブロック [`00bbf590`](#insn-00bbf590) 範囲 `[['00bbf590', '00bbf5bb']]`
  - `CONDITIONAL_JUMP` [`00bbf5b8`](#insn-00bbf5b8) → [`00bbf5d0`](#insn-00bbf5d0)
  - `FALL_THROUGH` [`00bbf5b8`](#insn-00bbf5b8) → [`00bbf5bc`](#insn-00bbf5bc)
- ブロック [`00bbf5bc`](#insn-00bbf5bc) 範囲 `[['00bbf5bc', '00bbf5cf']]`
  - `UNCONDITIONAL_JUMP` [`00bbf5cc`](#insn-00bbf5cc) → [`00bbf614`](#insn-00bbf614)
- ブロック [`00bbf5d0`](#insn-00bbf5d0) 範囲 `[['00bbf5d0', '00bbf5d3']]`
  - `CONDITIONAL_JUMP` [`00bbf5d0`](#insn-00bbf5d0) → [`00bbf614`](#insn-00bbf614)
  - `FALL_THROUGH` [`00bbf5d0`](#insn-00bbf5d0) → [`00bbf5d4`](#insn-00bbf5d4)
- ブロック [`00bbf5d4`](#insn-00bbf5d4) 範囲 `[['00bbf5d4', '00bbf5e3']]`
  - `CONDITIONAL_JUMP` [`00bbf5e0`](#insn-00bbf5e0) → [`00bbf610`](#insn-00bbf610)
  - `FALL_THROUGH` [`00bbf5e0`](#insn-00bbf5e0) → [`00bbf5e4`](#insn-00bbf5e4)
- ブロック [`00bbf5e4`](#insn-00bbf5e4) 範囲 `[['00bbf5e4', '00bbf5ef']]`
  - `CONDITIONAL_JUMP` [`00bbf5ec`](#insn-00bbf5ec) → [`00bbf604`](#insn-00bbf604)
  - `FALL_THROUGH` [`00bbf5ec`](#insn-00bbf5ec) → [`00bbf5f0`](#insn-00bbf5f0)
- ブロック [`00bbf5f0`](#insn-00bbf5f0) 範囲 `[['00bbf5f0', '00bbf5fb']]`
  - `CONDITIONAL_JUMP` [`00bbf5f8`](#insn-00bbf5f8) → [`00bbf610`](#insn-00bbf610)
  - `FALL_THROUGH` [`00bbf5f8`](#insn-00bbf5f8) → [`00bbf5fc`](#insn-00bbf5fc)
- ブロック [`00bbf5fc`](#insn-00bbf5fc) 範囲 `[['00bbf5fc', '00bbf603']]`
  - `CONDITIONAL_JUMP` [`00bbf600`](#insn-00bbf600) → [`00bbf5f0`](#insn-00bbf5f0)
  - `FALL_THROUGH` [`00bbf600`](#insn-00bbf600) → [`00bbf604`](#insn-00bbf604)
- ブロック [`00bbf604`](#insn-00bbf604) 範囲 `[['00bbf604', '00bbf60f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf60c`](#insn-00bbf60c) → [`00bbf5f0`](#insn-00bbf5f0)
- ブロック [`00bbf610`](#insn-00bbf610) 範囲 `[['00bbf610', '00bbf613']]`
  - `FALL_THROUGH` [`00bbf610`](#insn-00bbf610) → [`00bbf614`](#insn-00bbf614)
- ブロック [`00bbf614`](#insn-00bbf614) 範囲 `[['00bbf614', '00bbf617']]`
  - `CONDITIONAL_JUMP` [`00bbf614`](#insn-00bbf614) → [`00bbf690`](#insn-00bbf690)
  - `FALL_THROUGH` [`00bbf614`](#insn-00bbf614) → [`00bbf618`](#insn-00bbf618)
- ブロック [`00bbf618`](#insn-00bbf618) 範囲 `[['00bbf618', '00bbf61f']]`
  - `FALL_THROUGH` [`00bbf61c`](#insn-00bbf61c) → [`00bbf620`](#insn-00bbf620)
- ブロック [`00bbf620`](#insn-00bbf620) 範囲 `[['00bbf620', '00bbf633']]`
  - `CONDITIONAL_JUMP` [`00bbf630`](#insn-00bbf630) → [`00bbf64c`](#insn-00bbf64c)
  - `FALL_THROUGH` [`00bbf630`](#insn-00bbf630) → [`00bbf634`](#insn-00bbf634)
- ブロック [`00bbf634`](#insn-00bbf634) 範囲 `[['00bbf634', '00bbf63b']]`
  - `CONDITIONAL_JUMP` [`00bbf638`](#insn-00bbf638) → [`00bbf650`](#insn-00bbf650)
  - `FALL_THROUGH` [`00bbf638`](#insn-00bbf638) → [`00bbf63c`](#insn-00bbf63c)
- ブロック [`00bbf63c`](#insn-00bbf63c) 範囲 `[['00bbf63c', '00bbf64b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf648`](#insn-00bbf648) → [`00bbf650`](#insn-00bbf650)
- ブロック [`00bbf64c`](#insn-00bbf64c) 範囲 `[['00bbf64c', '00bbf64f']]`
  - `FALL_THROUGH` [`00bbf64c`](#insn-00bbf64c) → [`00bbf650`](#insn-00bbf650)
- ブロック [`00bbf650`](#insn-00bbf650) 範囲 `[['00bbf650', '00bbf68f']]`
  - `CONDITIONAL_JUMP` [`00bbf68c`](#insn-00bbf68c) → [`00bbf620`](#insn-00bbf620)
  - `FALL_THROUGH` [`00bbf68c`](#insn-00bbf68c) → [`00bbf690`](#insn-00bbf690)
- ブロック [`00bbf690`](#insn-00bbf690) 範囲 `[['00bbf690', '00bbf6a3']]`
  - `CONDITIONAL_JUMP` [`00bbf6a0`](#insn-00bbf6a0) → [`00bbf6bc`](#insn-00bbf6bc)
  - `FALL_THROUGH` [`00bbf6a0`](#insn-00bbf6a0) → [`00bbf6a4`](#insn-00bbf6a4)
- ブロック [`00bbf6a4`](#insn-00bbf6a4) 範囲 `[['00bbf6a4', '00bbf6ab']]`
  - `CONDITIONAL_JUMP` [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6c0`](#insn-00bbf6c0)
  - `FALL_THROUGH` [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6ac`](#insn-00bbf6ac)
- ブロック [`00bbf6ac`](#insn-00bbf6ac) 範囲 `[['00bbf6ac', '00bbf6bb']]`
  - `UNCONDITIONAL_JUMP` [`00bbf6b8`](#insn-00bbf6b8) → [`00bbf6c0`](#insn-00bbf6c0)
- ブロック [`00bbf6bc`](#insn-00bbf6bc) 範囲 `[['00bbf6bc', '00bbf6bf']]`
  - `FALL_THROUGH` [`00bbf6bc`](#insn-00bbf6bc) → [`00bbf6c0`](#insn-00bbf6c0)
- ブロック [`00bbf6c0`](#insn-00bbf6c0) 範囲 `[['00bbf6c0', '00bbf6ff']]`
  - `CONDITIONAL_JUMP` [`00bbf6fc`](#insn-00bbf6fc) → [`00bbf808`](#insn-00bbf808)
  - `FALL_THROUGH` [`00bbf6fc`](#insn-00bbf6fc) → [`00bbf700`](#insn-00bbf700)
- ブロック [`00bbf700`](#insn-00bbf700) 範囲 `[['00bbf700', '00bbf707']]`
  - `CONDITIONAL_JUMP` [`00bbf704`](#insn-00bbf704) → [`00bbf808`](#insn-00bbf808)
  - `FALL_THROUGH` [`00bbf704`](#insn-00bbf704) → [`00bbf708`](#insn-00bbf708)
- ブロック [`00bbf708`](#insn-00bbf708) 範囲 `[['00bbf708', '00bbf733']]`
  - `CONDITIONAL_JUMP` [`00bbf730`](#insn-00bbf730) → [`00bbf748`](#insn-00bbf748)
  - `FALL_THROUGH` [`00bbf730`](#insn-00bbf730) → [`00bbf734`](#insn-00bbf734)
- ブロック [`00bbf734`](#insn-00bbf734) 範囲 `[['00bbf734', '00bbf747']]`
  - `UNCONDITIONAL_JUMP` [`00bbf744`](#insn-00bbf744) → [`00bbf78c`](#insn-00bbf78c)
- ブロック [`00bbf748`](#insn-00bbf748) 範囲 `[['00bbf748', '00bbf74b']]`
  - `CONDITIONAL_JUMP` [`00bbf748`](#insn-00bbf748) → [`00bbf78c`](#insn-00bbf78c)
  - `FALL_THROUGH` [`00bbf748`](#insn-00bbf748) → [`00bbf74c`](#insn-00bbf74c)
- ブロック [`00bbf74c`](#insn-00bbf74c) 範囲 `[['00bbf74c', '00bbf75b']]`
  - `CONDITIONAL_JUMP` [`00bbf758`](#insn-00bbf758) → [`00bbf788`](#insn-00bbf788)
  - `FALL_THROUGH` [`00bbf758`](#insn-00bbf758) → [`00bbf75c`](#insn-00bbf75c)
- ブロック [`00bbf75c`](#insn-00bbf75c) 範囲 `[['00bbf75c', '00bbf767']]`
  - `CONDITIONAL_JUMP` [`00bbf764`](#insn-00bbf764) → [`00bbf77c`](#insn-00bbf77c)
  - `FALL_THROUGH` [`00bbf764`](#insn-00bbf764) → [`00bbf768`](#insn-00bbf768)
- ブロック [`00bbf768`](#insn-00bbf768) 範囲 `[['00bbf768', '00bbf773']]`
  - `CONDITIONAL_JUMP` [`00bbf770`](#insn-00bbf770) → [`00bbf788`](#insn-00bbf788)
  - `FALL_THROUGH` [`00bbf770`](#insn-00bbf770) → [`00bbf774`](#insn-00bbf774)
- ブロック [`00bbf774`](#insn-00bbf774) 範囲 `[['00bbf774', '00bbf77b']]`
  - `CONDITIONAL_JUMP` [`00bbf778`](#insn-00bbf778) → [`00bbf768`](#insn-00bbf768)
  - `FALL_THROUGH` [`00bbf778`](#insn-00bbf778) → [`00bbf77c`](#insn-00bbf77c)
- ブロック [`00bbf77c`](#insn-00bbf77c) 範囲 `[['00bbf77c', '00bbf787']]`
  - `UNCONDITIONAL_JUMP` [`00bbf784`](#insn-00bbf784) → [`00bbf768`](#insn-00bbf768)
- ブロック [`00bbf788`](#insn-00bbf788) 範囲 `[['00bbf788', '00bbf78b']]`
  - `FALL_THROUGH` [`00bbf788`](#insn-00bbf788) → [`00bbf78c`](#insn-00bbf78c)
- ブロック [`00bbf78c`](#insn-00bbf78c) 範囲 `[['00bbf78c', '00bbf78f']]`
  - `CONDITIONAL_JUMP` [`00bbf78c`](#insn-00bbf78c) → [`00bbf808`](#insn-00bbf808)
  - `FALL_THROUGH` [`00bbf78c`](#insn-00bbf78c) → [`00bbf790`](#insn-00bbf790)
- ブロック [`00bbf790`](#insn-00bbf790) 範囲 `[['00bbf790', '00bbf797']]`
  - `FALL_THROUGH` [`00bbf794`](#insn-00bbf794) → [`00bbf798`](#insn-00bbf798)
- ブロック [`00bbf798`](#insn-00bbf798) 範囲 `[['00bbf798', '00bbf7ab']]`
  - `CONDITIONAL_JUMP` [`00bbf7a8`](#insn-00bbf7a8) → [`00bbf7c4`](#insn-00bbf7c4)
  - `FALL_THROUGH` [`00bbf7a8`](#insn-00bbf7a8) → [`00bbf7ac`](#insn-00bbf7ac)
- ブロック [`00bbf7ac`](#insn-00bbf7ac) 範囲 `[['00bbf7ac', '00bbf7b3']]`
  - `CONDITIONAL_JUMP` [`00bbf7b0`](#insn-00bbf7b0) → [`00bbf7c8`](#insn-00bbf7c8)
  - `FALL_THROUGH` [`00bbf7b0`](#insn-00bbf7b0) → [`00bbf7b4`](#insn-00bbf7b4)
- ブロック [`00bbf7b4`](#insn-00bbf7b4) 範囲 `[['00bbf7b4', '00bbf7c3']]`
  - `UNCONDITIONAL_JUMP` [`00bbf7c0`](#insn-00bbf7c0) → [`00bbf7c8`](#insn-00bbf7c8)
- ブロック [`00bbf7c4`](#insn-00bbf7c4) 範囲 `[['00bbf7c4', '00bbf7c7']]`
  - `FALL_THROUGH` [`00bbf7c4`](#insn-00bbf7c4) → [`00bbf7c8`](#insn-00bbf7c8)
- ブロック [`00bbf7c8`](#insn-00bbf7c8) 範囲 `[['00bbf7c8', '00bbf807']]`
  - `CONDITIONAL_JUMP` [`00bbf804`](#insn-00bbf804) → [`00bbf798`](#insn-00bbf798)
  - `FALL_THROUGH` [`00bbf804`](#insn-00bbf804) → [`00bbf808`](#insn-00bbf808)
- ブロック [`00bbf808`](#insn-00bbf808) 範囲 `[['00bbf808', '00bbf81b']]`
  - `CONDITIONAL_JUMP` [`00bbf818`](#insn-00bbf818) → [`00bbf834`](#insn-00bbf834)
  - `FALL_THROUGH` [`00bbf818`](#insn-00bbf818) → [`00bbf81c`](#insn-00bbf81c)
- ブロック [`00bbf81c`](#insn-00bbf81c) 範囲 `[['00bbf81c', '00bbf823']]`
  - `CONDITIONAL_JUMP` [`00bbf820`](#insn-00bbf820) → [`00bbf838`](#insn-00bbf838)
  - `FALL_THROUGH` [`00bbf820`](#insn-00bbf820) → [`00bbf824`](#insn-00bbf824)
- ブロック [`00bbf824`](#insn-00bbf824) 範囲 `[['00bbf824', '00bbf833']]`
  - `UNCONDITIONAL_JUMP` [`00bbf830`](#insn-00bbf830) → [`00bbf838`](#insn-00bbf838)
- ブロック [`00bbf834`](#insn-00bbf834) 範囲 `[['00bbf834', '00bbf837']]`
  - `FALL_THROUGH` [`00bbf834`](#insn-00bbf834) → [`00bbf838`](#insn-00bbf838)
- ブロック [`00bbf838`](#insn-00bbf838) 範囲 `[['00bbf838', '00bbf85b']]`
  - `FALL_THROUGH` [`00bbf858`](#insn-00bbf858) → [`00bbf85c`](#insn-00bbf85c)
- ブロック [`00bbf85c`](#insn-00bbf85c) 範囲 `[['00bbf85c', '00bbf86b']]`
  - `FALL_THROUGH` [`00bbf868`](#insn-00bbf868) → [`00bbf86c`](#insn-00bbf86c)
- ブロック [`00bbf86c`](#insn-00bbf86c) 範囲 `[['00bbf86c', '00bbf87f']]`
  - `CONDITIONAL_JUMP` [`00bbf87c`](#insn-00bbf87c) → [`00bbf888`](#insn-00bbf888)
  - `FALL_THROUGH` [`00bbf87c`](#insn-00bbf87c) → [`00bbf880`](#insn-00bbf880)
- ブロック [`00bbf880`](#insn-00bbf880) 範囲 `[['00bbf880', '00bbf887']]`
  - `FALL_THROUGH` [`00bbf884`](#insn-00bbf884) → [`00bbf888`](#insn-00bbf888)
- ブロック [`00bbf888`](#insn-00bbf888) 範囲 `[['00bbf888', '00bbf88f']]`
  - `CONDITIONAL_JUMP` [`00bbf88c`](#insn-00bbf88c) → [`00bbf898`](#insn-00bbf898)
  - `FALL_THROUGH` [`00bbf88c`](#insn-00bbf88c) → [`00bbf890`](#insn-00bbf890)
- ブロック [`00bbf890`](#insn-00bbf890) 範囲 `[['00bbf890', '00bbf897']]`
  - `FALL_THROUGH` [`00bbf894`](#insn-00bbf894) → [`00bbf898`](#insn-00bbf898)
- ブロック [`00bbf898`](#insn-00bbf898) 範囲 `[['00bbf898', '00bbf8b7']]`
  - `CONDITIONAL_JUMP` [`00bbf8b4`](#insn-00bbf8b4) → [`00bbf8d8`](#insn-00bbf8d8)
  - `FALL_THROUGH` [`00bbf8b4`](#insn-00bbf8b4) → [`00bbf8b8`](#insn-00bbf8b8)
- ブロック [`00bbf8b8`](#insn-00bbf8b8) 範囲 `[['00bbf8b8', '00bbf8d7']]`
- ブロック [`00bbf8d8`](#insn-00bbf8d8) 範囲 `[['00bbf8d8', '00bbf8db']]`

## 命令位置別の参照

- [`00bbeadc`](#insn-00bbeadc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeae0`](#insn-00bbeae0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeae4`](#insn-00bbeae4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeae8`](#insn-00bbeae8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeaec`](#insn-00bbeaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeaf0`](#insn-00bbeaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb14`](#insn-00bbeb14) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb18`](#insn-00bbeb18) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb1c`](#insn-00bbeb1c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb20`](#insn-00bbeb20) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb24`](#insn-00bbeb24) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb28`](#insn-00bbeb28) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb2c`](#insn-00bbeb2c) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb30`](#insn-00bbeb30) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb34`](#insn-00bbeb34) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb38`](#insn-00bbeb38) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb3c`](#insn-00bbeb3c) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb40`](#insn-00bbeb40) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb44`](#insn-00bbeb44) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb48`](#insn-00bbeb48) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb4c`](#insn-00bbeb4c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb50`](#insn-00bbeb50) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb54`](#insn-00bbeb54) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb58`](#insn-00bbeb58) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb5c`](#insn-00bbeb5c) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb60`](#insn-00bbeb60) → `Stack[-0x230]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb64`](#insn-00bbeb64) → `Stack[-0x250]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb68`](#insn-00bbeb68) → `Stack[-0x270]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb6c`](#insn-00bbeb6c) → `Stack[-0x290]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb70`](#insn-00bbeb70) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb74`](#insn-00bbeb74) → `Stack[-0x2d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb78`](#insn-00bbeb78) → `Stack[-0x2f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb7c`](#insn-00bbeb7c) → `Stack[-0x300]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb80`](#insn-00bbeb80) → `Stack[-0x308]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeba0`](#insn-00bbeba0) → [`00bbebb8`](#insn-00bbebb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeba8`](#insn-00bbeba8) → [`00bbebb8`](#insn-00bbebb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebcc`](#insn-00bbebcc) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbebd0`](#insn-00bbebd0) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbebe0`](#insn-00bbebe0) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbebf4`](#insn-00bbebf4) → [`00bbec10`](#insn-00bbec10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebfc`](#insn-00bbebfc) → [`00bbec14`](#insn-00bbec14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec0c`](#insn-00bbec0c) → [`00bbec14`](#insn-00bbec14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec24`](#insn-00bbec24) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbec2c`](#insn-00bbec2c) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbec3c`](#insn-00bbec3c) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbec54`](#insn-00bbec54) → [`00bbedfc`](#insn-00bbedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec5c`](#insn-00bbec5c) → [`00bbedfc`](#insn-00bbedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec6c`](#insn-00bbec6c) → [`00bbedfc`](#insn-00bbedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec74`](#insn-00bbec74) → [`00bbedfc`](#insn-00bbedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec7c`](#insn-00bbec7c) → `Stack[-0x340]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec8c`](#insn-00bbec8c) → [`00bbeca0`](#insn-00bbeca0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec9c`](#insn-00bbec9c) → [`00bbedf0`](#insn-00bbedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecd4`](#insn-00bbecd4) → [`00bbed18`](#insn-00bbed18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecdc`](#insn-00bbecdc) → [`00bbecec`](#insn-00bbecec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecfc`](#insn-00bbecfc) → [`00bbed24`](#insn-00bbed24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed04`](#insn-00bbed04) → [`00bbed24`](#insn-00bbed24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed14`](#insn-00bbed14) → [`00bbed28`](#insn-00bbed28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed1c`](#insn-00bbed1c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbed20`](#insn-00bbed20) → [`00bbed28`](#insn-00bbed28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed38`](#insn-00bbed38) → [`00c5c660`](../00c5c/00c5c660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c660` · 推定シンボル `None` · 推定型 `None`
- [`00bbed48`](#insn-00bbed48) → [`0046d908`](../0046d/0046d908.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d908` · 推定シンボル `None` · 推定型 `None`
- [`00bbed54`](#insn-00bbed54) → [`00bbedc0`](#insn-00bbedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed5c`](#insn-00bbed5c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbed60`](#insn-00bbed60) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed64`](#insn-00bbed64) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed6c`](#insn-00bbed6c) → `Stack[-0x318]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed70`](#insn-00bbed70) → `Stack[-0x320]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed8c`](#insn-00bbed8c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed94`](#insn-00bbed94) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed98`](#insn-00bbed98) → [`00bbeda8`](#insn-00bbeda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed9c`](#insn-00bbed9c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeda4`](#insn-00bbeda4) → [`00bbedac`](#insn-00bbedac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedac`](#insn-00bbedac) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb0`](#insn-00bbedb0) → [`00c5c680`](../00c5c/00c5c680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c680` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb4`](#insn-00bbedb4) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedbc`](#insn-00bbedbc) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedc8`](#insn-00bbedc8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbedd8`](#insn-00bbedd8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbeddc`](#insn-00bbeddc) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbede0`](#insn-00bbede0) → [`00bbec90`](#insn-00bbec90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbede4`](#insn-00bbede4) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbede8`](#insn-00bbede8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbedec`](#insn-00bbedec) → [`00bbec90`](#insn-00bbec90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedf0`](#insn-00bbedf0) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee08`](#insn-00bbee08) → [`00bbeed0`](#insn-00bbeed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee10`](#insn-00bbee10) → [`00bbeed0`](#insn-00bbeed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee20`](#insn-00bbee20) → [`00bbeed0`](#insn-00bbeed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee24`](#insn-00bbee24) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee28`](#insn-00bbee28) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee38`](#insn-00bbee38) → [`00bbee80`](#insn-00bbee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee3c`](#insn-00bbee3c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee44`](#insn-00bbee44) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbee5c`](#insn-00bbee5c) → [`00bbee6c`](#insn-00bbee6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee68`](#insn-00bbee68) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbee6c`](#insn-00bbee6c) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee70`](#insn-00bbee70) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee74`](#insn-00bbee74) → [`00bbee80`](#insn-00bbee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee7c`](#insn-00bbee7c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbeea8`](#insn-00bbeea8) → `Stack[-0x328]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeeb8`](#insn-00bbeeb8) → `Stack[-0x330]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeec4`](#insn-00bbeec4) → [`00c5e610`](../00c5e/00c5e610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e610` · 推定シンボル `None` · 推定型 `None`
- [`00bbeedc`](#insn-00bbeedc) → [`00bbeef8`](#insn-00bbeef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeee4`](#insn-00bbeee4) → [`00bbeefc`](#insn-00bbeefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeef4`](#insn-00bbeef4) → [`00bbeefc`](#insn-00bbeefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef0c`](#insn-00bbef0c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbef14`](#insn-00bbef14) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbef24`](#insn-00bbef24) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbef38`](#insn-00bbef38) → [`00bbef54`](#insn-00bbef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef40`](#insn-00bbef40) → [`00bbef58`](#insn-00bbef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef50`](#insn-00bbef50) → [`00bbef58`](#insn-00bbef58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef68`](#insn-00bbef68) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbef70`](#insn-00bbef70) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbef80`](#insn-00bbef80) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbef98`](#insn-00bbef98) → [`00bbefb4`](#insn-00bbefb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefa0`](#insn-00bbefa0) → [`00bbefb8`](#insn-00bbefb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefb0`](#insn-00bbefb0) → [`00bbefb8`](#insn-00bbefb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefc4`](#insn-00bbefc4) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbefc8`](#insn-00bbefc8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbefd8`](#insn-00bbefd8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbefec`](#insn-00bbefec) → [`00bbf008`](#insn-00bbf008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeff4`](#insn-00bbeff4) → [`00bbf00c`](#insn-00bbf00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf004`](#insn-00bbf004) → [`00bbf00c`](#insn-00bbf00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf01c`](#insn-00bbf01c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf024`](#insn-00bbf024) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf034`](#insn-00bbf034) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf048`](#insn-00bbf048) → [`00bbf084`](#insn-00bbf084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf050`](#insn-00bbf050) → [`00bbf060`](#insn-00bbf060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf064`](#insn-00bbf064) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf068`](#insn-00bbf068) → [`00bbf090`](#insn-00bbf090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf070`](#insn-00bbf070) → [`00bbf094`](#insn-00bbf094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf080`](#insn-00bbf080) → [`00bbf094`](#insn-00bbf094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf088`](#insn-00bbf088) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf08c`](#insn-00bbf08c) → [`00bbf094`](#insn-00bbf094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0a0`](#insn-00bbf0a0) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf0a4`](#insn-00bbf0a4) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0b4`](#insn-00bbf0b4) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0c8`](#insn-00bbf0c8) → [`00bbf0e4`](#insn-00bbf0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0d0`](#insn-00bbf0d0) → [`00bbf0e8`](#insn-00bbf0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0e0`](#insn-00bbf0e0) → [`00bbf0e8`](#insn-00bbf0e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0f8`](#insn-00bbf0f8) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf100`](#insn-00bbf100) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf110`](#insn-00bbf110) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf124`](#insn-00bbf124) → [`00bbf140`](#insn-00bbf140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf12c`](#insn-00bbf12c) → [`00bbf144`](#insn-00bbf144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf13c`](#insn-00bbf13c) → [`00bbf144`](#insn-00bbf144) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf154`](#insn-00bbf154) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf15c`](#insn-00bbf15c) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf16c`](#insn-00bbf16c) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf180`](#insn-00bbf180) → [`00bbf19c`](#insn-00bbf19c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf188`](#insn-00bbf188) → [`00bbf1a0`](#insn-00bbf1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf198`](#insn-00bbf198) → [`00bbf1a0`](#insn-00bbf1a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1b0`](#insn-00bbf1b0) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf1b8`](#insn-00bbf1b8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1c8`](#insn-00bbf1c8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1dc`](#insn-00bbf1dc) → [`00bbf1fc`](#insn-00bbf1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1e4`](#insn-00bbf1e4) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1ec`](#insn-00bbf1ec) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1f4`](#insn-00bbf1f4) → [`00bbf210`](#insn-00bbf210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1f8`](#insn-00bbf1f8) → [`00bbf214`](#insn-00bbf214) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf200`](#insn-00bbf200) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf204`](#insn-00bbf204) → [`00bbf264`](#insn-00bbf264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf20c`](#insn-00bbf20c) → [`00bbf214`](#insn-00bbf214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf218`](#insn-00bbf218) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf21c`](#insn-00bbf21c) → [`00bbf86c`](#insn-00bbf86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf224`](#insn-00bbf224) → [`00bbf86c`](#insn-00bbf86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf234`](#insn-00bbf234) → [`00bbf86c`](#insn-00bbf86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf248`](#insn-00bbf248) → [`00bbf26c`](#insn-00bbf26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf250`](#insn-00bbf250) → [`00bbf270`](#insn-00bbf270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf260`](#insn-00bbf260) → [`00bbf270`](#insn-00bbf270) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf264`](#insn-00bbf264) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf268`](#insn-00bbf268) → [`00bbf86c`](#insn-00bbf86c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf27c`](#insn-00bbf27c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf280`](#insn-00bbf280) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf290`](#insn-00bbf290) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2a4`](#insn-00bbf2a4) → [`00bbf2c0`](#insn-00bbf2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2ac`](#insn-00bbf2ac) → [`00bbf2c4`](#insn-00bbf2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2bc`](#insn-00bbf2bc) → [`00bbf2c4`](#insn-00bbf2c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2d4`](#insn-00bbf2d4) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf2dc`](#insn-00bbf2dc) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf2ec`](#insn-00bbf2ec) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf300`](#insn-00bbf300) → [`00bbf31c`](#insn-00bbf31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf308`](#insn-00bbf308) → [`00bbf320`](#insn-00bbf320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf318`](#insn-00bbf318) → [`00bbf320`](#insn-00bbf320) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf330`](#insn-00bbf330) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf338`](#insn-00bbf338) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf348`](#insn-00bbf348) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf35c`](#insn-00bbf35c) → [`00bbf378`](#insn-00bbf378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf364`](#insn-00bbf364) → [`00bbf37c`](#insn-00bbf37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf374`](#insn-00bbf374) → [`00bbf37c`](#insn-00bbf37c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf38c`](#insn-00bbf38c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf394`](#insn-00bbf394) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3a4`](#insn-00bbf3a4) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3b8`](#insn-00bbf3b8) → [`00bbf3d4`](#insn-00bbf3d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3c0`](#insn-00bbf3c0) → [`00bbf3d8`](#insn-00bbf3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3d0`](#insn-00bbf3d0) → [`00bbf3d8`](#insn-00bbf3d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf3e8`](#insn-00bbf3e8) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf3f0`](#insn-00bbf3f0) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf400`](#insn-00bbf400) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf414`](#insn-00bbf414) → [`00bbf430`](#insn-00bbf430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf41c`](#insn-00bbf41c) → [`00bbf434`](#insn-00bbf434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf42c`](#insn-00bbf42c) → [`00bbf434`](#insn-00bbf434) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf444`](#insn-00bbf444) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf44c`](#insn-00bbf44c) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf45c`](#insn-00bbf45c) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf470`](#insn-00bbf470) → [`00bbf48c`](#insn-00bbf48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf478`](#insn-00bbf478) → [`00bbf490`](#insn-00bbf490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf488`](#insn-00bbf488) → [`00bbf490`](#insn-00bbf490) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4a0`](#insn-00bbf4a0) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf4a8`](#insn-00bbf4a8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4b8`](#insn-00bbf4b8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4cc`](#insn-00bbf4cc) → [`00bbf4e8`](#insn-00bbf4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4d4`](#insn-00bbf4d4) → [`00bbf4ec`](#insn-00bbf4ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4e4`](#insn-00bbf4e4) → [`00bbf4ec`](#insn-00bbf4ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf4fc`](#insn-00bbf4fc) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf504`](#insn-00bbf504) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf514`](#insn-00bbf514) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf528`](#insn-00bbf528) → [`00bbf544`](#insn-00bbf544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf530`](#insn-00bbf530) → [`00bbf548`](#insn-00bbf548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf540`](#insn-00bbf540) → [`00bbf548`](#insn-00bbf548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf558`](#insn-00bbf558) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf560`](#insn-00bbf560) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf570`](#insn-00bbf570) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf584`](#insn-00bbf584) → [`00bbf690`](#insn-00bbf690) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf58c`](#insn-00bbf58c) → [`00bbf690`](#insn-00bbf690) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf598`](#insn-00bbf598) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5b8`](#insn-00bbf5b8) → [`00bbf5d0`](#insn-00bbf5d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5c8`](#insn-00bbf5c8) → [`00c5e600`](../00c5e/00c5e600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e600` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5cc`](#insn-00bbf5cc) → [`00bbf614`](#insn-00bbf614) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5d0`](#insn-00bbf5d0) → [`00bbf614`](#insn-00bbf614) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5e0`](#insn-00bbf5e0) → [`00bbf610`](#insn-00bbf610) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5ec`](#insn-00bbf5ec) → [`00bbf604`](#insn-00bbf604) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf5f8`](#insn-00bbf5f8) → [`00bbf610`](#insn-00bbf610) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf600`](#insn-00bbf600) → [`00bbf5f0`](#insn-00bbf5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf608`](#insn-00bbf608) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbf60c`](#insn-00bbf60c) → [`00bbf5f0`](#insn-00bbf5f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf610`](#insn-00bbf610) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf614`](#insn-00bbf614) → [`00bbf690`](#insn-00bbf690) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf630`](#insn-00bbf630) → [`00bbf64c`](#insn-00bbf64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf638`](#insn-00bbf638) → [`00bbf650`](#insn-00bbf650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf648`](#insn-00bbf648) → [`00bbf650`](#insn-00bbf650) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf65c`](#insn-00bbf65c) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf670`](#insn-00bbf670) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf680`](#insn-00bbf680) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf68c`](#insn-00bbf68c) → [`00bbf620`](#insn-00bbf620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6a0`](#insn-00bbf6a0) → [`00bbf6bc`](#insn-00bbf6bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6a8`](#insn-00bbf6a8) → [`00bbf6c0`](#insn-00bbf6c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6b8`](#insn-00bbf6b8) → [`00bbf6c0`](#insn-00bbf6c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6d0`](#insn-00bbf6d0) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf6d8`](#insn-00bbf6d8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6e8`](#insn-00bbf6e8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf6fc`](#insn-00bbf6fc) → [`00bbf808`](#insn-00bbf808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf704`](#insn-00bbf704) → [`00bbf808`](#insn-00bbf808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf710`](#insn-00bbf710) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf730`](#insn-00bbf730) → [`00bbf748`](#insn-00bbf748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf740`](#insn-00bbf740) → [`00c5e600`](../00c5e/00c5e600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e600` · 推定シンボル `None` · 推定型 `None`
- [`00bbf744`](#insn-00bbf744) → [`00bbf78c`](#insn-00bbf78c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf748`](#insn-00bbf748) → [`00bbf78c`](#insn-00bbf78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf758`](#insn-00bbf758) → [`00bbf788`](#insn-00bbf788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf764`](#insn-00bbf764) → [`00bbf77c`](#insn-00bbf77c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf770`](#insn-00bbf770) → [`00bbf788`](#insn-00bbf788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf778`](#insn-00bbf778) → [`00bbf768`](#insn-00bbf768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf780`](#insn-00bbf780) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbf784`](#insn-00bbf784) → [`00bbf768`](#insn-00bbf768) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf788`](#insn-00bbf788) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf78c`](#insn-00bbf78c) → [`00bbf808`](#insn-00bbf808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7a8`](#insn-00bbf7a8) → [`00bbf7c4`](#insn-00bbf7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7b0`](#insn-00bbf7b0) → [`00bbf7c8`](#insn-00bbf7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7c0`](#insn-00bbf7c0) → [`00bbf7c8`](#insn-00bbf7c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7d4`](#insn-00bbf7d4) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7e8`](#insn-00bbf7e8) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7f8`](#insn-00bbf7f8) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf804`](#insn-00bbf804) → [`00bbf798`](#insn-00bbf798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf818`](#insn-00bbf818) → [`00bbf834`](#insn-00bbf834) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf820`](#insn-00bbf820) → [`00bbf838`](#insn-00bbf838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf830`](#insn-00bbf830) → [`00bbf838`](#insn-00bbf838) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf844`](#insn-00bbf844) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbf848`](#insn-00bbf848) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00bbf85c`](#insn-00bbf85c) → [`00c5c150`](../00c5c/00c5c150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c150` · 推定シンボル `None` · 推定型 `None`
- [`00bbf864`](#insn-00bbf864) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf868`](#insn-00bbf868) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf878`](#insn-00bbf878) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf87c`](#insn-00bbf87c) → [`00bbf888`](#insn-00bbf888) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf880`](#insn-00bbf880) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf884`](#insn-00bbf884) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf888`](#insn-00bbf888) → `Stack[-0x308]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf88c`](#insn-00bbf88c) → [`00bbf898`](#insn-00bbf898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf890`](#insn-00bbf890) → `Stack[-0x2f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf894`](#insn-00bbf894) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbf89c`](#insn-00bbf89c) → [`00c5e370`](../00c5e/00c5e370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e370` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8a4`](#insn-00bbf8a4) → [`00c5e490`](../00c5e/00c5e490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e490` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8ac`](#insn-00bbf8ac) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8b4`](#insn-00bbf8b4) → [`00bbf8d8`](#insn-00bbf8d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8bc`](#insn-00bbf8bc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8c0`](#insn-00bbf8c0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8c4`](#insn-00bbf8c4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8c8`](#insn-00bbf8c8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8cc`](#insn-00bbf8cc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8d8`](#insn-00bbf8d8) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbeadc`](#insn-00bbeadc)

~~~json
{
  "source": "00bbeadc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeae0`](#insn-00bbeae0)

~~~json
{
  "source": "00bbeae0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeae4`](#insn-00bbeae4)

~~~json
{
  "source": "00bbeae4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeae8`](#insn-00bbeae8)

~~~json
{
  "source": "00bbeae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeaec`](#insn-00bbeaec)

~~~json
{
  "source": "00bbeaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeaf0`](#insn-00bbeaf0)

~~~json
{
  "source": "00bbeaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb14`](#insn-00bbeb14)

~~~json
{
  "source": "00bbeb14",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb18`](#insn-00bbeb18)

~~~json
{
  "source": "00bbeb18",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb1c`](#insn-00bbeb1c)

~~~json
{
  "source": "00bbeb1c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb20`](#insn-00bbeb20)

~~~json
{
  "source": "00bbeb20",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb24`](#insn-00bbeb24)

~~~json
{
  "source": "00bbeb24",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb28`](#insn-00bbeb28)

~~~json
{
  "source": "00bbeb28",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb2c`](#insn-00bbeb2c)

~~~json
{
  "source": "00bbeb2c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb30`](#insn-00bbeb30)

~~~json
{
  "source": "00bbeb30",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb34`](#insn-00bbeb34)

~~~json
{
  "source": "00bbeb34",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb38`](#insn-00bbeb38)

~~~json
{
  "source": "00bbeb38",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb3c`](#insn-00bbeb3c)

~~~json
{
  "source": "00bbeb3c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb40`](#insn-00bbeb40)

~~~json
{
  "source": "00bbeb40",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb44`](#insn-00bbeb44)

~~~json
{
  "source": "00bbeb44",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb48`](#insn-00bbeb48)

~~~json
{
  "source": "00bbeb48",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb4c`](#insn-00bbeb4c)

~~~json
{
  "source": "00bbeb4c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb50`](#insn-00bbeb50)

~~~json
{
  "source": "00bbeb50",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb54`](#insn-00bbeb54)

~~~json
{
  "source": "00bbeb54",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb58`](#insn-00bbeb58)

~~~json
{
  "source": "00bbeb58",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb5c`](#insn-00bbeb5c)

~~~json
{
  "source": "00bbeb5c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb60`](#insn-00bbeb60)

~~~json
{
  "source": "00bbeb60",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb64`](#insn-00bbeb64)

~~~json
{
  "source": "00bbeb64",
  "target": "Stack[-0x250]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb68`](#insn-00bbeb68)

~~~json
{
  "source": "00bbeb68",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb6c`](#insn-00bbeb6c)

~~~json
{
  "source": "00bbeb6c",
  "target": "Stack[-0x290]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb70`](#insn-00bbeb70)

~~~json
{
  "source": "00bbeb70",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb74`](#insn-00bbeb74)

~~~json
{
  "source": "00bbeb74",
  "target": "Stack[-0x2d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb78`](#insn-00bbeb78)

~~~json
{
  "source": "00bbeb78",
  "target": "Stack[-0x2f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb7c`](#insn-00bbeb7c)

~~~json
{
  "source": "00bbeb7c",
  "target": "Stack[-0x300]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb80`](#insn-00bbeb80)

~~~json
{
  "source": "00bbeb80",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeba0`](#insn-00bbeba0)

~~~json
{
  "source": "00bbeba0",
  "target": "00bbebb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeba8`](#insn-00bbeba8)

~~~json
{
  "source": "00bbeba8",
  "target": "00bbebb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebcc`](#insn-00bbebcc)

~~~json
{
  "source": "00bbebcc",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbebd0`](#insn-00bbebd0)

~~~json
{
  "source": "00bbebd0",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbebe0`](#insn-00bbebe0)

~~~json
{
  "source": "00bbebe0",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbebf4`](#insn-00bbebf4)

~~~json
{
  "source": "00bbebf4",
  "target": "00bbec10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebfc`](#insn-00bbebfc)

~~~json
{
  "source": "00bbebfc",
  "target": "00bbec14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec0c`](#insn-00bbec0c)

~~~json
{
  "source": "00bbec0c",
  "target": "00bbec14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec24`](#insn-00bbec24)

~~~json
{
  "source": "00bbec24",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbec2c`](#insn-00bbec2c)

~~~json
{
  "source": "00bbec2c",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbec3c`](#insn-00bbec3c)

~~~json
{
  "source": "00bbec3c",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbec54`](#insn-00bbec54)

~~~json
{
  "source": "00bbec54",
  "target": "00bbedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec5c`](#insn-00bbec5c)

~~~json
{
  "source": "00bbec5c",
  "target": "00bbedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec6c`](#insn-00bbec6c)

~~~json
{
  "source": "00bbec6c",
  "target": "00bbedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec74`](#insn-00bbec74)

~~~json
{
  "source": "00bbec74",
  "target": "00bbedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec7c`](#insn-00bbec7c)

~~~json
{
  "source": "00bbec7c",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec8c`](#insn-00bbec8c)

~~~json
{
  "source": "00bbec8c",
  "target": "00bbeca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec9c`](#insn-00bbec9c)

~~~json
{
  "source": "00bbec9c",
  "target": "00bbedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecd4`](#insn-00bbecd4)

~~~json
{
  "source": "00bbecd4",
  "target": "00bbed18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecdc`](#insn-00bbecdc)

~~~json
{
  "source": "00bbecdc",
  "target": "00bbecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecfc`](#insn-00bbecfc)

~~~json
{
  "source": "00bbecfc",
  "target": "00bbed24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed04`](#insn-00bbed04)

~~~json
{
  "source": "00bbed04",
  "target": "00bbed24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed14`](#insn-00bbed14)

~~~json
{
  "source": "00bbed14",
  "target": "00bbed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed1c`](#insn-00bbed1c)

~~~json
{
  "source": "00bbed1c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed20`](#insn-00bbed20)

~~~json
{
  "source": "00bbed20",
  "target": "00bbed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed38`](#insn-00bbed38)

~~~json
{
  "source": "00bbed38",
  "target": "00c5c660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbed48`](#insn-00bbed48)

~~~json
{
  "source": "00bbed48",
  "target": "0046d908",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbed54`](#insn-00bbed54)

~~~json
{
  "source": "00bbed54",
  "target": "00bbedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed5c`](#insn-00bbed5c)

~~~json
{
  "source": "00bbed5c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbed60`](#insn-00bbed60)

~~~json
{
  "source": "00bbed60",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed64`](#insn-00bbed64)

~~~json
{
  "source": "00bbed64",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed6c`](#insn-00bbed6c)

~~~json
{
  "source": "00bbed6c",
  "target": "Stack[-0x318]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed70`](#insn-00bbed70)

~~~json
{
  "source": "00bbed70",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed8c`](#insn-00bbed8c)

~~~json
{
  "source": "00bbed8c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed94`](#insn-00bbed94)

~~~json
{
  "source": "00bbed94",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed98`](#insn-00bbed98)

~~~json
{
  "source": "00bbed98",
  "target": "00bbeda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed9c`](#insn-00bbed9c)

~~~json
{
  "source": "00bbed9c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeda4`](#insn-00bbeda4)

~~~json
{
  "source": "00bbeda4",
  "target": "00bbedac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedac`](#insn-00bbedac)

~~~json
{
  "source": "00bbedac",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb0`](#insn-00bbedb0)

~~~json
{
  "source": "00bbedb0",
  "target": "00c5c680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedb4`](#insn-00bbedb4)

~~~json
{
  "source": "00bbedb4",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedbc`](#insn-00bbedbc)

~~~json
{
  "source": "00bbedbc",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedc8`](#insn-00bbedc8)

~~~json
{
  "source": "00bbedc8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedd8`](#insn-00bbedd8)

~~~json
{
  "source": "00bbedd8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeddc`](#insn-00bbeddc)

~~~json
{
  "source": "00bbeddc",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede0`](#insn-00bbede0)

~~~json
{
  "source": "00bbede0",
  "target": "00bbec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede4`](#insn-00bbede4)

~~~json
{
  "source": "00bbede4",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede8`](#insn-00bbede8)

~~~json
{
  "source": "00bbede8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedec`](#insn-00bbedec)

~~~json
{
  "source": "00bbedec",
  "target": "00bbec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedf0`](#insn-00bbedf0)

~~~json
{
  "source": "00bbedf0",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee08`](#insn-00bbee08)

~~~json
{
  "source": "00bbee08",
  "target": "00bbeed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee10`](#insn-00bbee10)

~~~json
{
  "source": "00bbee10",
  "target": "00bbeed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee20`](#insn-00bbee20)

~~~json
{
  "source": "00bbee20",
  "target": "00bbeed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee24`](#insn-00bbee24)

~~~json
{
  "source": "00bbee24",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee28`](#insn-00bbee28)

~~~json
{
  "source": "00bbee28",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee38`](#insn-00bbee38)

~~~json
{
  "source": "00bbee38",
  "target": "00bbee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee3c`](#insn-00bbee3c)

~~~json
{
  "source": "00bbee3c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee44`](#insn-00bbee44)

~~~json
{
  "source": "00bbee44",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee5c`](#insn-00bbee5c)

~~~json
{
  "source": "00bbee5c",
  "target": "00bbee6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee68`](#insn-00bbee68)

~~~json
{
  "source": "00bbee68",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee6c`](#insn-00bbee6c)

~~~json
{
  "source": "00bbee6c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee70`](#insn-00bbee70)

~~~json
{
  "source": "00bbee70",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee74`](#insn-00bbee74)

~~~json
{
  "source": "00bbee74",
  "target": "00bbee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee7c`](#insn-00bbee7c)

~~~json
{
  "source": "00bbee7c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeea8`](#insn-00bbeea8)

~~~json
{
  "source": "00bbeea8",
  "target": "Stack[-0x328]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeeb8`](#insn-00bbeeb8)

~~~json
{
  "source": "00bbeeb8",
  "target": "Stack[-0x330]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeec4`](#insn-00bbeec4)

~~~json
{
  "source": "00bbeec4",
  "target": "00c5e610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeedc`](#insn-00bbeedc)

~~~json
{
  "source": "00bbeedc",
  "target": "00bbeef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeee4`](#insn-00bbeee4)

~~~json
{
  "source": "00bbeee4",
  "target": "00bbeefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeef4`](#insn-00bbeef4)

~~~json
{
  "source": "00bbeef4",
  "target": "00bbeefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef0c`](#insn-00bbef0c)

~~~json
{
  "source": "00bbef0c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbef14`](#insn-00bbef14)

~~~json
{
  "source": "00bbef14",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef24`](#insn-00bbef24)

~~~json
{
  "source": "00bbef24",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef38`](#insn-00bbef38)

~~~json
{
  "source": "00bbef38",
  "target": "00bbef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef40`](#insn-00bbef40)

~~~json
{
  "source": "00bbef40",
  "target": "00bbef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef50`](#insn-00bbef50)

~~~json
{
  "source": "00bbef50",
  "target": "00bbef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef68`](#insn-00bbef68)

~~~json
{
  "source": "00bbef68",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbef70`](#insn-00bbef70)

~~~json
{
  "source": "00bbef70",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef80`](#insn-00bbef80)

~~~json
{
  "source": "00bbef80",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef98`](#insn-00bbef98)

~~~json
{
  "source": "00bbef98",
  "target": "00bbefb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefa0`](#insn-00bbefa0)

~~~json
{
  "source": "00bbefa0",
  "target": "00bbefb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefb0`](#insn-00bbefb0)

~~~json
{
  "source": "00bbefb0",
  "target": "00bbefb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefc4`](#insn-00bbefc4)

~~~json
{
  "source": "00bbefc4",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbefc8`](#insn-00bbefc8)

~~~json
{
  "source": "00bbefc8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefd8`](#insn-00bbefd8)

~~~json
{
  "source": "00bbefd8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefec`](#insn-00bbefec)

~~~json
{
  "source": "00bbefec",
  "target": "00bbf008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeff4`](#insn-00bbeff4)

~~~json
{
  "source": "00bbeff4",
  "target": "00bbf00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf004`](#insn-00bbf004)

~~~json
{
  "source": "00bbf004",
  "target": "00bbf00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf01c`](#insn-00bbf01c)

~~~json
{
  "source": "00bbf01c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf024`](#insn-00bbf024)

~~~json
{
  "source": "00bbf024",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf034`](#insn-00bbf034)

~~~json
{
  "source": "00bbf034",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf048`](#insn-00bbf048)

~~~json
{
  "source": "00bbf048",
  "target": "00bbf084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf050`](#insn-00bbf050)

~~~json
{
  "source": "00bbf050",
  "target": "00bbf060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf064`](#insn-00bbf064)

~~~json
{
  "source": "00bbf064",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf068`](#insn-00bbf068)

~~~json
{
  "source": "00bbf068",
  "target": "00bbf090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf070`](#insn-00bbf070)

~~~json
{
  "source": "00bbf070",
  "target": "00bbf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf080`](#insn-00bbf080)

~~~json
{
  "source": "00bbf080",
  "target": "00bbf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf088`](#insn-00bbf088)

~~~json
{
  "source": "00bbf088",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf08c`](#insn-00bbf08c)

~~~json
{
  "source": "00bbf08c",
  "target": "00bbf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0a0`](#insn-00bbf0a0)

~~~json
{
  "source": "00bbf0a0",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf0a4`](#insn-00bbf0a4)

~~~json
{
  "source": "00bbf0a4",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf0b4`](#insn-00bbf0b4)

~~~json
{
  "source": "00bbf0b4",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf0c8`](#insn-00bbf0c8)

~~~json
{
  "source": "00bbf0c8",
  "target": "00bbf0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0d0`](#insn-00bbf0d0)

~~~json
{
  "source": "00bbf0d0",
  "target": "00bbf0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0e0`](#insn-00bbf0e0)

~~~json
{
  "source": "00bbf0e0",
  "target": "00bbf0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0f8`](#insn-00bbf0f8)

~~~json
{
  "source": "00bbf0f8",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf100`](#insn-00bbf100)

~~~json
{
  "source": "00bbf100",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf110`](#insn-00bbf110)

~~~json
{
  "source": "00bbf110",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf124`](#insn-00bbf124)

~~~json
{
  "source": "00bbf124",
  "target": "00bbf140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf12c`](#insn-00bbf12c)

~~~json
{
  "source": "00bbf12c",
  "target": "00bbf144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf13c`](#insn-00bbf13c)

~~~json
{
  "source": "00bbf13c",
  "target": "00bbf144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf154`](#insn-00bbf154)

~~~json
{
  "source": "00bbf154",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf15c`](#insn-00bbf15c)

~~~json
{
  "source": "00bbf15c",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf16c`](#insn-00bbf16c)

~~~json
{
  "source": "00bbf16c",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf180`](#insn-00bbf180)

~~~json
{
  "source": "00bbf180",
  "target": "00bbf19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf188`](#insn-00bbf188)

~~~json
{
  "source": "00bbf188",
  "target": "00bbf1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf198`](#insn-00bbf198)

~~~json
{
  "source": "00bbf198",
  "target": "00bbf1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1b0`](#insn-00bbf1b0)

~~~json
{
  "source": "00bbf1b0",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf1b8`](#insn-00bbf1b8)

~~~json
{
  "source": "00bbf1b8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf1c8`](#insn-00bbf1c8)

~~~json
{
  "source": "00bbf1c8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf1dc`](#insn-00bbf1dc)

~~~json
{
  "source": "00bbf1dc",
  "target": "00bbf1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1e4`](#insn-00bbf1e4)

~~~json
{
  "source": "00bbf1e4",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1ec`](#insn-00bbf1ec)

~~~json
{
  "source": "00bbf1ec",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1f4`](#insn-00bbf1f4)

~~~json
{
  "source": "00bbf1f4",
  "target": "00bbf210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1f8`](#insn-00bbf1f8)

~~~json
{
  "source": "00bbf1f8",
  "target": "00bbf214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf200`](#insn-00bbf200)

~~~json
{
  "source": "00bbf200",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf204`](#insn-00bbf204)

~~~json
{
  "source": "00bbf204",
  "target": "00bbf264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf20c`](#insn-00bbf20c)

~~~json
{
  "source": "00bbf20c",
  "target": "00bbf214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf218`](#insn-00bbf218)

~~~json
{
  "source": "00bbf218",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf21c`](#insn-00bbf21c)

~~~json
{
  "source": "00bbf21c",
  "target": "00bbf86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf224`](#insn-00bbf224)

~~~json
{
  "source": "00bbf224",
  "target": "00bbf86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf234`](#insn-00bbf234)

~~~json
{
  "source": "00bbf234",
  "target": "00bbf86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf248`](#insn-00bbf248)

~~~json
{
  "source": "00bbf248",
  "target": "00bbf26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf250`](#insn-00bbf250)

~~~json
{
  "source": "00bbf250",
  "target": "00bbf270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf260`](#insn-00bbf260)

~~~json
{
  "source": "00bbf260",
  "target": "00bbf270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf264`](#insn-00bbf264)

~~~json
{
  "source": "00bbf264",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf268`](#insn-00bbf268)

~~~json
{
  "source": "00bbf268",
  "target": "00bbf86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf27c`](#insn-00bbf27c)

~~~json
{
  "source": "00bbf27c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf280`](#insn-00bbf280)

~~~json
{
  "source": "00bbf280",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf290`](#insn-00bbf290)

~~~json
{
  "source": "00bbf290",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf2a4`](#insn-00bbf2a4)

~~~json
{
  "source": "00bbf2a4",
  "target": "00bbf2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2ac`](#insn-00bbf2ac)

~~~json
{
  "source": "00bbf2ac",
  "target": "00bbf2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2bc`](#insn-00bbf2bc)

~~~json
{
  "source": "00bbf2bc",
  "target": "00bbf2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf2d4`](#insn-00bbf2d4)

~~~json
{
  "source": "00bbf2d4",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf2dc`](#insn-00bbf2dc)

~~~json
{
  "source": "00bbf2dc",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf2ec`](#insn-00bbf2ec)

~~~json
{
  "source": "00bbf2ec",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf300`](#insn-00bbf300)

~~~json
{
  "source": "00bbf300",
  "target": "00bbf31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf308`](#insn-00bbf308)

~~~json
{
  "source": "00bbf308",
  "target": "00bbf320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf318`](#insn-00bbf318)

~~~json
{
  "source": "00bbf318",
  "target": "00bbf320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf330`](#insn-00bbf330)

~~~json
{
  "source": "00bbf330",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf338`](#insn-00bbf338)

~~~json
{
  "source": "00bbf338",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf348`](#insn-00bbf348)

~~~json
{
  "source": "00bbf348",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf35c`](#insn-00bbf35c)

~~~json
{
  "source": "00bbf35c",
  "target": "00bbf378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf364`](#insn-00bbf364)

~~~json
{
  "source": "00bbf364",
  "target": "00bbf37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf374`](#insn-00bbf374)

~~~json
{
  "source": "00bbf374",
  "target": "00bbf37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf38c`](#insn-00bbf38c)

~~~json
{
  "source": "00bbf38c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf394`](#insn-00bbf394)

~~~json
{
  "source": "00bbf394",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf3a4`](#insn-00bbf3a4)

~~~json
{
  "source": "00bbf3a4",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf3b8`](#insn-00bbf3b8)

~~~json
{
  "source": "00bbf3b8",
  "target": "00bbf3d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3c0`](#insn-00bbf3c0)

~~~json
{
  "source": "00bbf3c0",
  "target": "00bbf3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3d0`](#insn-00bbf3d0)

~~~json
{
  "source": "00bbf3d0",
  "target": "00bbf3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf3e8`](#insn-00bbf3e8)

~~~json
{
  "source": "00bbf3e8",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf3f0`](#insn-00bbf3f0)

~~~json
{
  "source": "00bbf3f0",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf400`](#insn-00bbf400)

~~~json
{
  "source": "00bbf400",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf414`](#insn-00bbf414)

~~~json
{
  "source": "00bbf414",
  "target": "00bbf430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf41c`](#insn-00bbf41c)

~~~json
{
  "source": "00bbf41c",
  "target": "00bbf434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf42c`](#insn-00bbf42c)

~~~json
{
  "source": "00bbf42c",
  "target": "00bbf434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf444`](#insn-00bbf444)

~~~json
{
  "source": "00bbf444",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf44c`](#insn-00bbf44c)

~~~json
{
  "source": "00bbf44c",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf45c`](#insn-00bbf45c)

~~~json
{
  "source": "00bbf45c",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf470`](#insn-00bbf470)

~~~json
{
  "source": "00bbf470",
  "target": "00bbf48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf478`](#insn-00bbf478)

~~~json
{
  "source": "00bbf478",
  "target": "00bbf490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf488`](#insn-00bbf488)

~~~json
{
  "source": "00bbf488",
  "target": "00bbf490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4a0`](#insn-00bbf4a0)

~~~json
{
  "source": "00bbf4a0",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf4a8`](#insn-00bbf4a8)

~~~json
{
  "source": "00bbf4a8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf4b8`](#insn-00bbf4b8)

~~~json
{
  "source": "00bbf4b8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf4cc`](#insn-00bbf4cc)

~~~json
{
  "source": "00bbf4cc",
  "target": "00bbf4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4d4`](#insn-00bbf4d4)

~~~json
{
  "source": "00bbf4d4",
  "target": "00bbf4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4e4`](#insn-00bbf4e4)

~~~json
{
  "source": "00bbf4e4",
  "target": "00bbf4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf4fc`](#insn-00bbf4fc)

~~~json
{
  "source": "00bbf4fc",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf504`](#insn-00bbf504)

~~~json
{
  "source": "00bbf504",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf514`](#insn-00bbf514)

~~~json
{
  "source": "00bbf514",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf528`](#insn-00bbf528)

~~~json
{
  "source": "00bbf528",
  "target": "00bbf544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf530`](#insn-00bbf530)

~~~json
{
  "source": "00bbf530",
  "target": "00bbf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf540`](#insn-00bbf540)

~~~json
{
  "source": "00bbf540",
  "target": "00bbf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf558`](#insn-00bbf558)

~~~json
{
  "source": "00bbf558",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf560`](#insn-00bbf560)

~~~json
{
  "source": "00bbf560",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf570`](#insn-00bbf570)

~~~json
{
  "source": "00bbf570",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf584`](#insn-00bbf584)

~~~json
{
  "source": "00bbf584",
  "target": "00bbf690",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf58c`](#insn-00bbf58c)

~~~json
{
  "source": "00bbf58c",
  "target": "00bbf690",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf598`](#insn-00bbf598)

~~~json
{
  "source": "00bbf598",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5b8`](#insn-00bbf5b8)

~~~json
{
  "source": "00bbf5b8",
  "target": "00bbf5d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5c8`](#insn-00bbf5c8)

~~~json
{
  "source": "00bbf5c8",
  "target": "00c5e600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf5cc`](#insn-00bbf5cc)

~~~json
{
  "source": "00bbf5cc",
  "target": "00bbf614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5d0`](#insn-00bbf5d0)

~~~json
{
  "source": "00bbf5d0",
  "target": "00bbf614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5e0`](#insn-00bbf5e0)

~~~json
{
  "source": "00bbf5e0",
  "target": "00bbf610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5ec`](#insn-00bbf5ec)

~~~json
{
  "source": "00bbf5ec",
  "target": "00bbf604",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf5f8`](#insn-00bbf5f8)

~~~json
{
  "source": "00bbf5f8",
  "target": "00bbf610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf600`](#insn-00bbf600)

~~~json
{
  "source": "00bbf600",
  "target": "00bbf5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf608`](#insn-00bbf608)

~~~json
{
  "source": "00bbf608",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf60c`](#insn-00bbf60c)

~~~json
{
  "source": "00bbf60c",
  "target": "00bbf5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf610`](#insn-00bbf610)

~~~json
{
  "source": "00bbf610",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf614`](#insn-00bbf614)

~~~json
{
  "source": "00bbf614",
  "target": "00bbf690",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf630`](#insn-00bbf630)

~~~json
{
  "source": "00bbf630",
  "target": "00bbf64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf638`](#insn-00bbf638)

~~~json
{
  "source": "00bbf638",
  "target": "00bbf650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf648`](#insn-00bbf648)

~~~json
{
  "source": "00bbf648",
  "target": "00bbf650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf65c`](#insn-00bbf65c)

~~~json
{
  "source": "00bbf65c",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf670`](#insn-00bbf670)

~~~json
{
  "source": "00bbf670",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf680`](#insn-00bbf680)

~~~json
{
  "source": "00bbf680",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf68c`](#insn-00bbf68c)

~~~json
{
  "source": "00bbf68c",
  "target": "00bbf620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6a0`](#insn-00bbf6a0)

~~~json
{
  "source": "00bbf6a0",
  "target": "00bbf6bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6a8`](#insn-00bbf6a8)

~~~json
{
  "source": "00bbf6a8",
  "target": "00bbf6c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6b8`](#insn-00bbf6b8)

~~~json
{
  "source": "00bbf6b8",
  "target": "00bbf6c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf6d0`](#insn-00bbf6d0)

~~~json
{
  "source": "00bbf6d0",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf6d8`](#insn-00bbf6d8)

~~~json
{
  "source": "00bbf6d8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf6e8`](#insn-00bbf6e8)

~~~json
{
  "source": "00bbf6e8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf6fc`](#insn-00bbf6fc)

~~~json
{
  "source": "00bbf6fc",
  "target": "00bbf808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf704`](#insn-00bbf704)

~~~json
{
  "source": "00bbf704",
  "target": "00bbf808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf710`](#insn-00bbf710)

~~~json
{
  "source": "00bbf710",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf730`](#insn-00bbf730)

~~~json
{
  "source": "00bbf730",
  "target": "00bbf748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf740`](#insn-00bbf740)

~~~json
{
  "source": "00bbf740",
  "target": "00c5e600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf744`](#insn-00bbf744)

~~~json
{
  "source": "00bbf744",
  "target": "00bbf78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf748`](#insn-00bbf748)

~~~json
{
  "source": "00bbf748",
  "target": "00bbf78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf758`](#insn-00bbf758)

~~~json
{
  "source": "00bbf758",
  "target": "00bbf788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf764`](#insn-00bbf764)

~~~json
{
  "source": "00bbf764",
  "target": "00bbf77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf770`](#insn-00bbf770)

~~~json
{
  "source": "00bbf770",
  "target": "00bbf788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf778`](#insn-00bbf778)

~~~json
{
  "source": "00bbf778",
  "target": "00bbf768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf780`](#insn-00bbf780)

~~~json
{
  "source": "00bbf780",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf784`](#insn-00bbf784)

~~~json
{
  "source": "00bbf784",
  "target": "00bbf768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf788`](#insn-00bbf788)

~~~json
{
  "source": "00bbf788",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf78c`](#insn-00bbf78c)

~~~json
{
  "source": "00bbf78c",
  "target": "00bbf808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7a8`](#insn-00bbf7a8)

~~~json
{
  "source": "00bbf7a8",
  "target": "00bbf7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7b0`](#insn-00bbf7b0)

~~~json
{
  "source": "00bbf7b0",
  "target": "00bbf7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7c0`](#insn-00bbf7c0)

~~~json
{
  "source": "00bbf7c0",
  "target": "00bbf7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7d4`](#insn-00bbf7d4)

~~~json
{
  "source": "00bbf7d4",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7e8`](#insn-00bbf7e8)

~~~json
{
  "source": "00bbf7e8",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf7f8`](#insn-00bbf7f8)

~~~json
{
  "source": "00bbf7f8",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf804`](#insn-00bbf804)

~~~json
{
  "source": "00bbf804",
  "target": "00bbf798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf818`](#insn-00bbf818)

~~~json
{
  "source": "00bbf818",
  "target": "00bbf834",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf820`](#insn-00bbf820)

~~~json
{
  "source": "00bbf820",
  "target": "00bbf838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf830`](#insn-00bbf830)

~~~json
{
  "source": "00bbf830",
  "target": "00bbf838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf844`](#insn-00bbf844)

~~~json
{
  "source": "00bbf844",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf848`](#insn-00bbf848)

~~~json
{
  "source": "00bbf848",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf85c`](#insn-00bbf85c)

~~~json
{
  "source": "00bbf85c",
  "target": "00c5c150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf864`](#insn-00bbf864)

~~~json
{
  "source": "00bbf864",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf868`](#insn-00bbf868)

~~~json
{
  "source": "00bbf868",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf878`](#insn-00bbf878)

~~~json
{
  "source": "00bbf878",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf87c`](#insn-00bbf87c)

~~~json
{
  "source": "00bbf87c",
  "target": "00bbf888",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf880`](#insn-00bbf880)

~~~json
{
  "source": "00bbf880",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf884`](#insn-00bbf884)

~~~json
{
  "source": "00bbf884",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf888`](#insn-00bbf888)

~~~json
{
  "source": "00bbf888",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf88c`](#insn-00bbf88c)

~~~json
{
  "source": "00bbf88c",
  "target": "00bbf898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf890`](#insn-00bbf890)

~~~json
{
  "source": "00bbf890",
  "target": "Stack[-0x2f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf894`](#insn-00bbf894)

~~~json
{
  "source": "00bbf894",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf89c`](#insn-00bbf89c)

~~~json
{
  "source": "00bbf89c",
  "target": "00c5e370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf8a4`](#insn-00bbf8a4)

~~~json
{
  "source": "00bbf8a4",
  "target": "00c5e490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf8ac`](#insn-00bbf8ac)

~~~json
{
  "source": "00bbf8ac",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8b4`](#insn-00bbf8b4)

~~~json
{
  "source": "00bbf8b4",
  "target": "00bbf8d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8bc`](#insn-00bbf8bc)

~~~json
{
  "source": "00bbf8bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8c0`](#insn-00bbf8c0)

~~~json
{
  "source": "00bbf8c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8c4`](#insn-00bbf8c4)

~~~json
{
  "source": "00bbf8c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8c8`](#insn-00bbf8c8)

~~~json
{
  "source": "00bbf8c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8cc`](#insn-00bbf8cc)

~~~json
{
  "source": "00bbf8cc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8d8`](#insn-00bbf8d8)

~~~json
{
  "source": "00bbf8d8",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
