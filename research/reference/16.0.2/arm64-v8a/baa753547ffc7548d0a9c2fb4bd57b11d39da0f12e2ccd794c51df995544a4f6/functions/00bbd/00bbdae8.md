# 00bbdae8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbda4c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-4ac594f18f4fe61e92243c74c76710b9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbeadc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbeadc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-9add5372f9674d0da7f336852b2148d7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdae8",
  "name": "_ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE",
  "size": 3584,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b475c53e15c3e6449c1d1fb8f27cfc7fa8ec33a29807967fd08ade564e8d2693",
  "source_text_sha256": "b475c53e15c3e6449c1d1fb8f27cfc7fa8ec33a29807967fd08ade564e8d2693",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdae8",
        "00bbe8e7"
      ]
    ],
    "bytes_sha256": "b0168bb65bc36934c1e4e0aa8c62f93744b91c45d8467075946960c12af94645",
    "instruction_count": 896,
    "instruction_bytes": 3584,
    "body_bytes": 3584,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5d610](../00c5d/00c5d610.md)

## 呼び出し先

- [0046d5e8](../0046d/0046d5e8.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580b0](../00c58/00c580b0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c5b180](../00c5b/00c5b180.md)
- [00c5b690](../00c5b/00c5b690.md)
- [00c5b6b0](../00c5b/00c5b6b0.md)
- [00c5d3a0](../00c5d/00c5d3a0.md)
- [00c5d4c0](../00c5d/00c5d4c0.md)
- [00c5d630](../00c5d/00c5d630.md)
- [00c5d640](../00c5d/00c5d640.md)

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
  
                    /* try { // try from 00bbdae8 to 00cbdaf3 has its CatchHandler @ 00bbe078 */
  lVar5 = tpidr_el0;
  local_78 = *(long *)(lVar5 + 0x28);
  local_178 = &local_170;
  local_170 = 0;
  local_168 = 0;
                    /* try { // try from 00bbdb28 to 00cbdb2f has its CatchHandler @ 00bbe074 */
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
                    /* try { // try from 00bbdbb4 to 00cbdbb7 has its CatchHandler @ 00bbe038 */
    lVar16 = 0;
    if (uVar17 != 0) {
                    /* try { // try from 00bbdbb8 to 00cbdc43 has its CatchHandler @ 00bbd95c */
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
                    /* try { // try from 00bbdc44 to 00cbdc7b has its CatchHandler @ 00bbe084 */
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
                    /* try { // try from 00bbdcf8 to 00cbdcfb has its CatchHandler @ 00bbe044 */
                    /* try { // try from 00bbdcfc to 00cbddcb has its CatchHandler @ 00bbd95c */
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
      puVar13 = (undefined8 *)FUN_0046d5e8(&local_178,&local_80,&local_320);
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
                    /* try { // try from 00bbddcc to 00cbddd3 has its CatchHandler @ 00bbdff0 */
                    /* try { // try from 00bbddd4 to 00cbde27 has its CatchHandler @ 00bbd95c */
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
                    /* try { // try from 00bbde28 to 00cbde3b has its CatchHandler @ 00bbe01c */
  if (((0xc < *(ushort *)((long)param_2 + lVar16)) &&
      (uVar17 = (ulong)((ushort *)((long)param_2 + lVar16))[6], uVar17 != 0)) &&
     (puVar18 = (uint *)((long)param_2 + uVar17),
     puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18), puVar18 != (uint *)0x0)) {
    uVar17 = (ulong)*puVar18;
    if ((ulong)(local_150 - (long)local_160) < uVar17) {
      __dest = (void *)_Znwm(uVar17);
      sVar12 = lVar10 - (long)pvVar9;
                    /* try { // try from 00bbde68 to 00cbde6f has its CatchHandler @ 00bbe048 */
      if (0 < (long)sVar12) {
        memcpy(__dest,pvVar9,sVar12);
      }
      local_160 = __dest;
      lStack_158 = (long)__dest + sVar12;
      local_150 = (long)__dest + uVar17;
      if (pvVar9 != (void *)0x0) {
                    /* try { // try from 00bbde84 to 00cbde8b has its CatchHandler @ 00bbdff4 */
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
                    /* try { // try from 00bbdf64 to 00cbdf6b has its CatchHandler @ 00bbe070 */
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
                    /* try { // try from 00bbdf80 to 00cbdfa3 has its CatchHandler @ 00bbe07c */
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
                    /* try { // try from 00bbdfb8 to 00cbdfbf has its CatchHandler @ 00bbe050 */
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
                    /* try { // try from 00bbdfd4 to 00cbdfd7 has its CatchHandler @ 00bbe07c */
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_f8,pcVar14,sVar12);
                    /* try { // try from 00bbdfec to 00cbdfef has its CatchHandler @ 00bbe050 */
                    /* catch() { ... } // from try @ 00bbddcc with catch @ 00bbdff0
                       try { // try from 00bbdff0 to 00cbe0c7 has its CatchHandler @ 00bbd95c */
                    /* catch() { ... } // from try @ 00bbde84 with catch @ 00bbdff4 */
                    /* catch() { ... } // from try @ 00bbda0c with catch @ 00bbdff8 */
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x19) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xc];
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
                    /* catch() { ... } // from try @ 00bbda00 with catch @ 00bbe008 */
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
                    /* catch() { ... } // from try @ 00bbd9f4 with catch @ 00bbe018 */
                    /* catch() { ... } // from try @ 00bbde28 with catch @ 00bbe01c */
  pcVar14 = __s;
                    /* catch() { ... } // from try @ 00bbd9c8 with catch @ 00bbe020 */
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
                    /* catch() { ... } // from try @ 00bbdbb4 with catch @ 00bbe038 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_e0,pcVar14,sVar12);
                    /* catch() { ... } // from try @ 00bbdcf8 with catch @ 00bbe044 */
                    /* catch() { ... } // from try @ 00bbde68 with catch @ 00bbe048 */
  puVar20 = (ushort *)((long)param_2 - (long)(int)*param_2);
                    /* catch() { ... } // from try @ 00bbdfb8 with catch @ 00bbe050
                       catch() { ... } // from try @ 00bbdfec with catch @ 00bbe050 */
  if (*puVar20 < 0x1d) {
    lVar16 = 0;
    local_c0 = false;
  }
  else {
    local_c0 = false;
    if ((ulong)puVar20[0xe] != 0) {
      local_c0 = *(char *)((long)param_2 + (ulong)puVar20[0xe]) != '\0';
    }
                    /* catch() { ... } // from try @ 00bbdf64 with catch @ 00bbe070 */
                    /* catch() { ... } // from try @ 00bbdb28 with catch @ 00bbe074 */
    if (*puVar20 < 0x1f) {
      lVar16 = 0;
    }
    else {
                    /* catch() { ... } // from try @ 00bbdae8 with catch @ 00bbe078 */
                    /* catch() { ... } // from try @ 00bbdf80 with catch @ 00bbe07c
                       catch() { ... } // from try @ 00bbdfd4 with catch @ 00bbe07c */
      lVar16 = 0;
      if ((ulong)puVar20[0xf] != 0) {
        puVar18 = (uint *)((long)param_2 + (ulong)puVar20[0xf]);
                    /* catch() { ... } // from try @ 00bbdc44 with catch @ 00bbe084 */
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
      goto LAB_00bbe878;
    }
    uVar17 = (ulong)puVar20[10];
    local_100 = 0;
    if (uVar17 != 0) goto LAB_00bbe21c;
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
LAB_00bbe21c:
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
                    /* try { // try from 00bbe868 to 00cbeb87 has its CatchHandler @ 00bbe868
                       catch() { ... } // from try @ 00bbe868 with catch @ 00bbe868
                       catch() { ... } // from try @ 00bbebd8 with catch @ 00bbe868
                       catch() { ... } // from try @ 00bbecf8 with catch @ 00bbe868
                       catch() { ... } // from try @ 00bbedc0 with catch @ 00bbe868
                       catch() { ... } // from try @ 00bbf1bc with catch @ 00bbe868
                       catch() { ... } // from try @ 00bbf410 with catch @ 00bbe868 */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_308,__s,sVar12);
    local_c8 = SUB81(&local_2f0,0);
    uStack_c7 = (undefined7)((ulong)&local_2f0 >> 8);
    local_1d0 = &local_308;
  }
LAB_00bbe878:
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
<a id="insn-00bbdae8"></a> `00bbdae8` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbdaec"></a> `00bbdaec` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdaf0"></a> `00bbdaf0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdaf4"></a> `00bbdaf4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdaf8"></a> `00bbdaf8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbdafc"></a> `00bbdafc` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbdb00"></a> `00bbdb00` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbdb04"></a> `00bbdb04` | `ff 83 0b d1` | sub sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbdb08"></a> `00bbdb08` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbdb0c"></a> `00bbdb0c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdb10"></a> `00bbdb10` | `fc 03 06 91` | add x28,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdb14"></a> `00bbdb14` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdb18"></a> `00bbdb18` | `89 43 01 91` | add x9,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00bbdb1c"></a> `00bbdb1c` | `95 23 04 91` | add x21,x28,#0x108 | `FALL_THROUGH`
<a id="insn-00bbdb20"></a> `00bbdb20` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbdb24"></a> `00bbdb24` | `ff 7f 1d a9` | stp xzr,xzr,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbdb28"></a> `00bbdb28` | `e0 03 0c ad` | stp q0,q0,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00bbdb2c"></a> `00bbdb2c` | `e0 03 0d ad` | stp q0,q0,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bbdb30"></a> `00bbdb30` | `ff 27 1c a9` | stp xzr,x9,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bbdb34"></a> `00bbdb34` | `e0 03 0f ad` | stp q0,q0,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbdb38"></a> `00bbdb38` | `e0 03 10 ad` | stp q0,q0,[sp, #0x200] | `FALL_THROUGH`
<a id="insn-00bbdb3c"></a> `00bbdb3c` | `e0 03 11 ad` | stp q0,q0,[sp, #0x220] | `FALL_THROUGH`
<a id="insn-00bbdb40"></a> `00bbdb40` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbdb44"></a> `00bbdb44` | `80 83 8c 3c` | stur q0,[x28, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbdb48"></a> `00bbdb48` | `80 83 8d 3c` | stur q0,[x28, #0xd8] | `FALL_THROUGH`
<a id="insn-00bbdb4c"></a> `00bbdb4c` | `80 83 8e 3c` | stur q0,[x28, #0xe8] | `FALL_THROUGH`
<a id="insn-00bbdb50"></a> `00bbdb50` | `80 13 8f 3c` | stur q0,[x28, #0xf1] | `FALL_THROUGH`
<a id="insn-00bbdb54"></a> `00bbdb54` | `bf 1a 00 f9` | str xzr,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdb58"></a> `00bbdb58` | `a0 82 00 ad` | stp q0,q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdb5c"></a> `00bbdb5c` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bbdb60"></a> `00bbdb60` | `ff bb 00 f9` | str xzr,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbdb64"></a> `00bbdb64` | `e0 83 0a ad` | stp q0,q0,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbdb68"></a> `00bbdb68` | `e0 83 09 ad` | stp q0,q0,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbdb6c"></a> `00bbdb6c` | `e0 83 08 ad` | stp q0,q0,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bbdb70"></a> `00bbdb70` | `e0 83 07 ad` | stp q0,q0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bbdb74"></a> `00bbdb74` | `e0 83 06 ad` | stp q0,q0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bbdb78"></a> `00bbdb78` | `e0 83 05 ad` | stp q0,q0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbdb7c"></a> `00bbdb7c` | `e0 83 04 ad` | stp q0,q0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbdb80"></a> `00bbdb80` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbdb84"></a> `00bbdb84` | `e0 83 02 ad` | stp q0,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbdb88"></a> `00bbdb88` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbdb8c"></a> `00bbdb8c` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbdb90"></a> `00bbdb90` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbdb94"></a> `00bbdb94` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbdb98"></a> `00bbdb98` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bbdb9c"></a> `00bbdb9c` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbdba0"></a> `00bbdba0` | `28 01 40 79` | ldrh w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbdba4"></a> `00bbdba4` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbdba8"></a> `00bbdba8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdbac"></a> `00bbdbac` | `c3 00 00 54` | b.cc 0x00bbdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdbb0"></a> `00bbdbb0` | `28 09 40 79` | ldrh w8,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbdbb4"></a> `00bbdbb4` | `88 00 00 b4` | cbz x8,0x00bbdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdbb8"></a> `00bbdbb8` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdbbc"></a> `00bbdbbc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdbc0"></a> `00bbdbc0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdbc4"></a> `00bbdbc4` | `5b b7 ff b0` | adrp x27,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbdbc8"></a> `00bbdbc8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdbcc"></a> `00bbdbcc` | `7b 3b 0e 91` | add x27,x27,#0x38e | `FALL_THROUGH`
<a id="insn-00bbdbd0"></a> `00bbdbd0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdbd4"></a> `00bbdbd4` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdbd8"></a> `00bbdbd8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdbdc"></a> `00bbdbdc` | `35 69 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdbe0"></a> `00bbdbe0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdbe4"></a> `00bbdbe4` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdbe8"></a> `00bbdbe8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdbec"></a> `00bbdbec` | `65 75 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdbf0"></a> `00bbdbf0` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdbf4"></a> `00bbdbf4` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdbf8"></a> `00bbdbf8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdbfc"></a> `00bbdbfc` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbdc00"></a> `00bbdc00` | `e3 00 00 54` | b.cc 0x00bbdc1c | `CONDITIONAL_JUMP`
<a id="insn-00bbdc04"></a> `00bbdc04` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbdc08"></a> `00bbdc08` | `c8 00 00 b4` | cbz x8,0x00bbdc20 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc0c"></a> `00bbdc0c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdc10"></a> `00bbdc10` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdc14"></a> `00bbdc14` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc18"></a> `00bbdc18` | `02 00 00 14` | b 0x00bbdc20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdc1c"></a> `00bbdc1c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdc20"></a> `00bbdc20` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdc24"></a> `00bbdc24` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdc28"></a> `00bbdc28` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdc2c"></a> `00bbdc2c` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdc30"></a> `00bbdc30` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdc34"></a> `00bbdc34` | `17 61 00 91` | add x23,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdc38"></a> `00bbdc38` | `1e 69 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdc3c"></a> `00bbdc3c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdc40"></a> `00bbdc40` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdc44"></a> `00bbdc44` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdc48"></a> `00bbdc48` | `4e 75 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdc4c"></a> `00bbdc4c` | `89 02 80 b9` | ldrsw x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbdc50"></a> `00bbdc50` | `8a 02 09 cb` | sub x10,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbdc54"></a> `00bbdc54` | `48 01 40 79` | ldrh w8,[x10] | `FALL_THROUGH`
<a id="insn-00bbdc58"></a> `00bbdc58` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bbdc5c"></a> `00bbdc5c` | `e8 03 09 cb` | neg x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc60"></a> `00bbdc60` | `43 0d 00 54` | b.cc 0x00bbde08 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc64"></a> `00bbdc64` | `4a 15 40 79` | ldrh w10,[x10, #0xa] | `FALL_THROUGH`
<a id="insn-00bbdc68"></a> `00bbdc68` | `0a 0d 00 b4` | cbz x10,0x00bbde08 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc6c"></a> `00bbdc6c` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00bbdc70"></a> `00bbdc70` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdc74"></a> `00bbdc74` | `4a 01 0b ab` | adds x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbdc78"></a> `00bbdc78` | `80 0c 00 54` | b.eq 0x00bbde08 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc7c"></a> `00bbdc7c` | `4a 01 40 b9` | ldr w10,[x10] | `FALL_THROUGH`
<a id="insn-00bbdc80"></a> `00bbdc80` | `4a 0c 00 34` | cbz w10,0x00bbde08 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc84"></a> `00bbdc84` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdc88"></a> `00bbdc88` | `fa 67 00 a9` | stp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbdc8c"></a> `00bbdc8c` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbdc90"></a> `00bbdc90` | `16 21 01 91` | add x22,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbdc94"></a> `00bbdc94` | `53 f5 7e d3` | lsl x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbdc98"></a> `00bbdc98` | `05 00 00 14` | b 0x00bbdcac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdc9c"></a> `00bbdc9c` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bbdca0"></a> `00bbdca0` | `5a 13 00 91` | add x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdca4"></a> `00bbdca4` | `7f 02 1a eb` | cmp x19,x26 | `FALL_THROUGH`
<a id="insn-00bbdca8"></a> `00bbdca8` | `a0 0a 00 54` | b.eq 0x00bbddfc | `CONDITIONAL_JUMP`
<a id="insn-00bbdcac"></a> `00bbdcac` | `88 c2 29 cb` | sub x8,x20,w9, SXTW  | `FALL_THROUGH`
<a id="insn-00bbdcb0"></a> `00bbdcb0` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbdcb4"></a> `00bbdcb4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdcb8"></a> `00bbdcb8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdcbc"></a> `00bbdcbc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdcc0"></a> `00bbdcc0` | `49 77 7e 92` | and x9,x26,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00bbdcc4"></a> `00bbdcc4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdcc8"></a> `00bbdcc8` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbdccc"></a> `00bbdccc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdcd0"></a> `00bbdcd0` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdcd4"></a> `00bbdcd4` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdcd8"></a> `00bbdcd8` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbdcdc"></a> `00bbdcdc` | `5f 15 00 71` | cmp w10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbdce0"></a> `00bbdce0` | `23 02 00 54` | b.cc 0x00bbdd24 | `CONDITIONAL_JUMP`
<a id="insn-00bbdce4"></a> `00bbdce4` | `2b 09 40 79` | ldrh w11,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbdce8"></a> `00bbdce8` | `8b 00 00 b4` | cbz x11,0x00bbdcf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbdcec"></a> `00bbdcec` | `0b 01 0b 8b` | add x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbdcf0"></a> `00bbdcf0` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbdcf4"></a> `00bbdcf4` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbdcf8"></a> `00bbdcf8` | `6c 11 00 91` | add x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdcfc"></a> `00bbdcfc` | `7f 01 00 f1` | cmp x11,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdd00"></a> `00bbdd00` | `61 03 8c 9a` | csel x1,x27,x12,eq | `FALL_THROUGH`
<a id="insn-00bbdd04"></a> `00bbdd04` | `5f 1d 00 71` | cmp w10,#0x7 | `FALL_THROUGH`
<a id="insn-00bbdd08"></a> `00bbdd08` | `43 01 00 54` | b.cc 0x00bbdd30 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd0c"></a> `00bbdd0c` | `29 0d 40 79` | ldrh w9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bbdd10"></a> `00bbdd10` | `09 01 00 b4` | cbz x9,0x00bbdd30 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd14"></a> `00bbdd14` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdd18"></a> `00bbdd18` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd1c"></a> `00bbdd1c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdd20"></a> `00bbdd20` | `05 00 00 14` | b 0x00bbdd34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdd24"></a> `00bbdd24` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdd28"></a> `00bbdd28` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00bbdd2c"></a> `00bbdd2c` | `02 00 00 14` | b 0x00bbdd34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdd30"></a> `00bbdd30` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdd34"></a> `00bbdd34` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdd38"></a> `00bbdd38` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdd3c"></a> `00bbdd3c` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdd40"></a> `00bbdd40` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdd44"></a> `00bbdd44` | `53 76 02 94` | bl 0x00c5b690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd48"></a> `00bbdd48` | `a1 c3 01 d1` | sub x1,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bbdd4c"></a> `00bbdd4c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdd50"></a> `00bbdd50` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdd54"></a> `00bbdd54` | `25 be e2 97` | bl 0x0046d5e8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd58"></a> `00bbdd58` | `18 00 40 f9` | ldr x24,[x0] | `FALL_THROUGH`
<a id="insn-00bbdd5c"></a> `00bbdd5c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bbdd60"></a> `00bbdd60` | `78 03 00 b5` | cbnz x24,0x00bbddcc | `CONDITIONAL_JUMP`
<a id="insn-00bbdd64"></a> `00bbdd64` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bbdd68"></a> `00bbdd68` | `7e 68 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd6c"></a> `00bbdd6c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd70"></a> `00bbdd70` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdd74"></a> `00bbdd74` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbdd78"></a> `00bbdd78` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdd7c"></a> `00bbdd7c` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd80"></a> `00bbdd80` | `1f 7c 04 a9` | stp xzr,xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bbdd84"></a> `00bbdd84` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbdd88"></a> `00bbdd88` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd8c"></a> `00bbdd8c` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdd90"></a> `00bbdd90` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdd94"></a> `00bbdd94` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00bbdd98"></a> `00bbdd98` | `e8 e7 40 f9` | ldr x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbdd9c"></a> `00bbdd9c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbdda0"></a> `00bbdda0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbdda4"></a> `00bbdda4` | `88 00 00 b4` | cbz x8,0x00bbddb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdda8"></a> `00bbdda8` | `e8 e7 00 f9` | str x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbddac"></a> `00bbddac` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00bbddb0"></a> `00bbddb0` | `02 00 00 14` | b 0x00bbddb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbddb4"></a> `00bbddb4` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bbddb8"></a> `00bbddb8` | `e0 eb 40 f9` | ldr x0,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbddbc"></a> `00bbddbc` | `3d 76 02 94` | bl 0x00c5b6b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddc0"></a> `00bbddc0` | `e8 ef 40 f9` | ldr x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbddc4"></a> `00bbddc4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbddc8"></a> `00bbddc8` | `e8 ef 00 f9` | str x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbddcc"></a> `00bbddcc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbddd0"></a> `00bbddd0` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-00bbddd4"></a> `00bbddd4` | `b7 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddd8"></a> `00bbddd8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdddc"></a> `00bbdddc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbdde0"></a> `00bbdde0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbdde4"></a> `00bbdde4` | `e7 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdde8"></a> `00bbdde8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbddec"></a> `00bbddec` | `88 f5 07 36` | tbz w8,#0x0,0x00bbdc9c | `CONDITIONAL_JUMP`
<a id="insn-00bbddf0"></a> `00bbddf0` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbddf4"></a> `00bbddf4` | `63 68 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddf8"></a> `00bbddf8` | `a9 ff ff 17` | b 0x00bbdc9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbddfc"></a> `00bbddfc` | `fa 67 40 a9` | ldp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbde00"></a> `00bbde00` | `28 7d 40 93` | sxtw x8,w9 | `FALL_THROUGH`
<a id="insn-00bbde04"></a> `00bbde04` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbde08"></a> `00bbde08` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbde0c"></a> `00bbde0c` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbde10"></a> `00bbde10` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00bbde14"></a> `00bbde14` | `43 06 00 54` | b.cc 0x00bbdedc | `CONDITIONAL_JUMP`
<a id="insn-00bbde18"></a> `00bbde18` | `29 19 40 79` | ldrh w9,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00bbde1c"></a> `00bbde1c` | `09 06 00 b4` | cbz x9,0x00bbdedc | `CONDITIONAL_JUMP`
<a id="insn-00bbde20"></a> `00bbde20` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbde24"></a> `00bbde24` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbde28"></a> `00bbde28` | `29 01 0a ab` | adds x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbde2c"></a> `00bbde2c` | `80 05 00 54` | b.eq 0x00bbdedc | `CONDITIONAL_JUMP`
<a id="insn-00bbde30"></a> `00bbde30` | `e8 fb 40 f9` | ldr x8,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbde34"></a> `00bbde34` | `f6 f3 40 f9` | ldr x22,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbde38"></a> `00bbde38` | `37 01 40 b9` | ldr w23,[x9] | `FALL_THROUGH`
<a id="insn-00bbde3c"></a> `00bbde3c` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00bbde40"></a> `00bbde40` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bbde44"></a> `00bbde44` | `42 02 00 54` | b.cs 0x00bbde8c | `CONDITIONAL_JUMP`
<a id="insn-00bbde48"></a> `00bbde48` | `f3 f7 40 f9` | ldr x19,[sp, #0x1e8] | `FALL_THROUGH`
<a id="insn-00bbde4c"></a> `00bbde4c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbde50"></a> `00bbde50` | `44 68 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde54"></a> `00bbde54` | `62 02 16 cb` | sub x2,x19,x22 | `FALL_THROUGH`
<a id="insn-00bbde58"></a> `00bbde58` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbde5c"></a> `00bbde5c` | `13 00 02 8b` | add x19,x0,x2 | `FALL_THROUGH`
<a id="insn-00bbde60"></a> `00bbde60` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-00bbde64"></a> `00bbde64` | `17 00 17 8b` | add x23,x0,x23 | `FALL_THROUGH`
<a id="insn-00bbde68"></a> `00bbde68` | `8b 00 00 54` | b.lt 0x00bbde78 | `CONDITIONAL_JUMP`
<a id="insn-00bbde6c"></a> `00bbde6c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbde70"></a> `00bbde70` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbde74"></a> `00bbde74` | `97 68 02 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde78"></a> `00bbde78` | `f8 4f 1e a9` | stp x24,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbde7c"></a> `00bbde7c` | `f7 fb 00 f9` | str x23,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbde80"></a> `00bbde80` | `76 00 00 b4` | cbz x22,0x00bbde8c | `CONDITIONAL_JUMP`
<a id="insn-00bbde84"></a> `00bbde84` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbde88"></a> `00bbde88` | `3e 68 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde8c"></a> `00bbde8c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbde90"></a> `00bbde90` | `80 83 01 91` | add x0,x28,#0x60 | `FALL_THROUGH`
<a id="insn-00bbde94"></a> `00bbde94` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbde98"></a> `00bbde98` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbde9c"></a> `00bbde9c` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdea0"></a> `00bbdea0` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbdea4"></a> `00bbdea4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdea8"></a> `00bbdea8` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdeac"></a> `00bbdeac` | `e8 03 89 9a` | csel x8,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdeb0"></a> `00bbdeb0` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdeb4"></a> `00bbdeb4` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdeb8"></a> `00bbdeb8` | `28 01 40 b9` | ldr w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbdebc"></a> `00bbdebc` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbdec0"></a> `00bbdec0` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdec4"></a> `00bbdec4` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdec8"></a> `00bbdec8` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdecc"></a> `00bbdecc` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbded0"></a> `00bbded0` | `dc 7d 02 94` | bl 0x00c5d640 | `UNCONDITIONAL_CALL`
<a id="insn-00bbded4"></a> `00bbded4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbded8"></a> `00bbded8` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbdedc"></a> `00bbdedc` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdee0"></a> `00bbdee0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdee4"></a> `00bbdee4` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbdee8"></a> `00bbdee8` | `e3 00 00 54` | b.cc 0x00bbdf04 | `CONDITIONAL_JUMP`
<a id="insn-00bbdeec"></a> `00bbdeec` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbdef0"></a> `00bbdef0` | `c8 00 00 b4` | cbz x8,0x00bbdf08 | `CONDITIONAL_JUMP`
<a id="insn-00bbdef4"></a> `00bbdef4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdef8"></a> `00bbdef8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdefc"></a> `00bbdefc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdf00"></a> `00bbdf00` | `02 00 00 14` | b 0x00bbdf08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdf04"></a> `00bbdf04` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdf08"></a> `00bbdf08` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdf0c"></a> `00bbdf0c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdf10"></a> `00bbdf10` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf14"></a> `00bbdf14` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdf18"></a> `00bbdf18` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdf1c"></a> `00bbdf1c` | `17 e1 01 91` | add x23,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbdf20"></a> `00bbdf20` | `64 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf24"></a> `00bbdf24` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdf28"></a> `00bbdf28` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdf2c"></a> `00bbdf2c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdf30"></a> `00bbdf30` | `94 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf34"></a> `00bbdf34` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdf38"></a> `00bbdf38` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf3c"></a> `00bbdf3c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf40"></a> `00bbdf40` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbdf44"></a> `00bbdf44` | `e3 00 00 54` | b.cc 0x00bbdf60 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf48"></a> `00bbdf48` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdf4c"></a> `00bbdf4c` | `c8 00 00 b4` | cbz x8,0x00bbdf64 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf50"></a> `00bbdf50` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf54"></a> `00bbdf54` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf58"></a> `00bbdf58` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdf5c"></a> `00bbdf5c` | `02 00 00 14` | b 0x00bbdf64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdf60"></a> `00bbdf60` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdf64"></a> `00bbdf64` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdf68"></a> `00bbdf68` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdf6c"></a> `00bbdf6c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf70"></a> `00bbdf70` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdf74"></a> `00bbdf74` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdf78"></a> `00bbdf78` | `17 41 02 91` | add x23,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbdf7c"></a> `00bbdf7c` | `4d 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf80"></a> `00bbdf80` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdf84"></a> `00bbdf84` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdf88"></a> `00bbdf88` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdf8c"></a> `00bbdf8c` | `7d 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf90"></a> `00bbdf90` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdf94"></a> `00bbdf94` | `96 23 03 91` | add x22,x28,#0xc8 | `FALL_THROUGH`
<a id="insn-00bbdf98"></a> `00bbdf98` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf9c"></a> `00bbdf9c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdfa0"></a> `00bbdfa0` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbdfa4"></a> `00bbdfa4` | `e3 00 00 54` | b.cc 0x00bbdfc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfa8"></a> `00bbdfa8` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbdfac"></a> `00bbdfac` | `c8 00 00 b4` | cbz x8,0x00bbdfc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfb0"></a> `00bbdfb0` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdfb4"></a> `00bbdfb4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdfb8"></a> `00bbdfb8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdfbc"></a> `00bbdfbc` | `02 00 00 14` | b 0x00bbdfc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdfc0"></a> `00bbdfc0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdfc4"></a> `00bbdfc4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdfc8"></a> `00bbdfc8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdfcc"></a> `00bbdfcc` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdfd0"></a> `00bbdfd0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdfd4"></a> `00bbdfd4` | `37 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfd8"></a> `00bbdfd8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdfdc"></a> `00bbdfdc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdfe0"></a> `00bbdfe0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbdfe4"></a> `00bbdfe4` | `67 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfe8"></a> `00bbdfe8` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdfec"></a> `00bbdfec` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdff0"></a> `00bbdff0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdff4"></a> `00bbdff4` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbdff8"></a> `00bbdff8` | `e3 00 00 54` | b.cc 0x00bbe014 | `CONDITIONAL_JUMP`
<a id="insn-00bbdffc"></a> `00bbdffc` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe000"></a> `00bbe000` | `c8 00 00 b4` | cbz x8,0x00bbe018 | `CONDITIONAL_JUMP`
<a id="insn-00bbe004"></a> `00bbe004` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe008"></a> `00bbe008` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe00c"></a> `00bbe00c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe010"></a> `00bbe010` | `02 00 00 14` | b 0x00bbe018 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe014"></a> `00bbe014` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe018"></a> `00bbe018` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe01c"></a> `00bbe01c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe020"></a> `00bbe020` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe024"></a> `00bbe024` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe028"></a> `00bbe028` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe02c"></a> `00bbe02c` | `17 81 03 91` | add x23,x8,#0xe0 | `FALL_THROUGH`
<a id="insn-00bbe030"></a> `00bbe030` | `20 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe034"></a> `00bbe034` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe038"></a> `00bbe038` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbe03c"></a> `00bbe03c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbe040"></a> `00bbe040` | `50 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe044"></a> `00bbe044` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe048"></a> `00bbe048` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe04c"></a> `00bbe04c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe050"></a> `00bbe050` | `3f 71 00 71` | cmp w9,#0x1c | `FALL_THROUGH`
<a id="insn-00bbe054"></a> `00bbe054` | `e9 01 00 54` | b.ls 0x00bbe090 | `CONDITIONAL_JUMP`
<a id="insn-00bbe058"></a> `00bbe058` | `0a 39 40 79` | ldrh w10,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbe05c"></a> `00bbe05c` | `8a 00 00 b4` | cbz x10,0x00bbe06c | `CONDITIONAL_JUMP`
<a id="insn-00bbe060"></a> `00bbe060` | `8a 6a 6a 38` | ldrb w10,[x20, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00bbe064"></a> `00bbe064` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe068"></a> `00bbe068` | `ea 07 9f 1a` | cset w10,ne | `FALL_THROUGH`
<a id="insn-00bbe06c"></a> `00bbe06c` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00bbe070"></a> `00bbe070` | `ea 03 0a 39` | strb w10,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbe074"></a> `00bbe074` | `43 01 00 54` | b.cc 0x00bbe09c | `CONDITIONAL_JUMP`
<a id="insn-00bbe078"></a> `00bbe078` | `08 3d 40 79` | ldrh w8,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00bbe07c"></a> `00bbe07c` | `28 01 00 b4` | cbz x8,0x00bbe0a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe080"></a> `00bbe080` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe084"></a> `00bbe084` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe088"></a> `00bbe088` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe08c"></a> `00bbe08c` | `05 00 00 14` | b 0x00bbe0a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe090"></a> `00bbe090` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe094"></a> `00bbe094` | `ff 03 0a 39` | strb wzr,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbe098"></a> `00bbe098` | `02 00 00 14` | b 0x00bbe0a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe09c"></a> `00bbe09c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe0a0"></a> `00bbe0a0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe0a4"></a> `00bbe0a4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe0a8"></a> `00bbe0a8` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe0ac"></a> `00bbe0ac` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe0b0"></a> `00bbe0b0` | `00 68 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe0b4"></a> `00bbe0b4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe0b8"></a> `00bbe0b8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe0bc"></a> `00bbe0bc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbe0c0"></a> `00bbe0c0` | `30 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe0c4"></a> `00bbe0c4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe0c8"></a> `00bbe0c8` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe0cc"></a> `00bbe0cc` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe0d0"></a> `00bbe0d0` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbe0d4"></a> `00bbe0d4` | `e3 00 00 54` | b.cc 0x00bbe0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe0d8"></a> `00bbe0d8` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe0dc"></a> `00bbe0dc` | `c8 00 00 b4` | cbz x8,0x00bbe0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe0e0"></a> `00bbe0e0` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe0e4"></a> `00bbe0e4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe0e8"></a> `00bbe0e8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe0ec"></a> `00bbe0ec` | `02 00 00 14` | b 0x00bbe0f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe0f0"></a> `00bbe0f0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe0f4"></a> `00bbe0f4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe0f8"></a> `00bbe0f8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe0fc"></a> `00bbe0fc` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe100"></a> `00bbe100` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe104"></a> `00bbe104` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe108"></a> `00bbe108` | `16 c1 00 91` | add x22,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe10c"></a> `00bbe10c` | `e9 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe110"></a> `00bbe110` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe114"></a> `00bbe114` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe118"></a> `00bbe118` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe11c"></a> `00bbe11c` | `19 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe120"></a> `00bbe120` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe124"></a> `00bbe124` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe128"></a> `00bbe128` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe12c"></a> `00bbe12c` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbe130"></a> `00bbe130` | `e3 00 00 54` | b.cc 0x00bbe14c | `CONDITIONAL_JUMP`
<a id="insn-00bbe134"></a> `00bbe134` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbe138"></a> `00bbe138` | `c8 00 00 b4` | cbz x8,0x00bbe150 | `CONDITIONAL_JUMP`
<a id="insn-00bbe13c"></a> `00bbe13c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe140"></a> `00bbe140` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe144"></a> `00bbe144` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe148"></a> `00bbe148` | `02 00 00 14` | b 0x00bbe150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe14c"></a> `00bbe14c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe150"></a> `00bbe150` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe154"></a> `00bbe154` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe158"></a> `00bbe158` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe15c"></a> `00bbe15c` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe160"></a> `00bbe160` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe164"></a> `00bbe164` | `16 a1 02 91` | add x22,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbe168"></a> `00bbe168` | `d2 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe16c"></a> `00bbe16c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe170"></a> `00bbe170` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe174"></a> `00bbe174` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe178"></a> `00bbe178` | `02 74 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe17c"></a> `00bbe17c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe180"></a> `00bbe180` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe184"></a> `00bbe184` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe188"></a> `00bbe188` | `3f 8d 00 71` | cmp w9,#0x23 | `FALL_THROUGH`
<a id="insn-00bbe18c"></a> `00bbe18c` | `e3 00 00 54` | b.cc 0x00bbe1a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe190"></a> `00bbe190` | `08 45 40 79` | ldrh w8,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00bbe194"></a> `00bbe194` | `c8 00 00 b4` | cbz x8,0x00bbe1ac | `CONDITIONAL_JUMP`
<a id="insn-00bbe198"></a> `00bbe198` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe19c"></a> `00bbe19c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe1a0"></a> `00bbe1a0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe1a4"></a> `00bbe1a4` | `02 00 00 14` | b 0x00bbe1ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe1a8"></a> `00bbe1a8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe1ac"></a> `00bbe1ac` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe1b0"></a> `00bbe1b0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe1b4"></a> `00bbe1b4` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe1b8"></a> `00bbe1b8` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe1bc"></a> `00bbe1bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe1c0"></a> `00bbe1c0` | `16 81 04 91` | add x22,x8,#0x120 | `FALL_THROUGH`
<a id="insn-00bbe1c4"></a> `00bbe1c4` | `bb 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe1c8"></a> `00bbe1c8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe1cc"></a> `00bbe1cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe1d0"></a> `00bbe1d0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe1d4"></a> `00bbe1d4` | `eb 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe1d8"></a> `00bbe1d8` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe1dc"></a> `00bbe1dc` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe1e0"></a> `00bbe1e0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe1e4"></a> `00bbe1e4` | `3f 85 00 71` | cmp w9,#0x21 | `FALL_THROUGH`
<a id="insn-00bbe1e8"></a> `00bbe1e8` | `03 01 00 54` | b.cc 0x00bbe208 | `CONDITIONAL_JUMP`
<a id="insn-00bbe1ec"></a> `00bbe1ec` | `0a 41 40 79` | ldrh w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe1f0"></a> `00bbe1f0` | `4a 00 00 b4` | cbz x10,0x00bbe1f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe1f4"></a> `00bbe1f4` | `8a 6a 6a f8` | ldr x10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe1f8"></a> `00bbe1f8` | `ea 5f 01 f9` | str x10,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbe1fc"></a> `00bbe1fc` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe200"></a> `00bbe200` | `ea 00 00 b5` | cbnz x10,0x00bbe21c | `CONDITIONAL_JUMP`
<a id="insn-00bbe204"></a> `00bbe204` | `07 00 00 14` | b 0x00bbe220 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe208"></a> `00bbe208` | `3f 51 00 71` | cmp w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bbe20c"></a> `00bbe20c` | `ff 5f 01 f9` | str xzr,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbe210"></a> `00bbe210` | `09 03 00 54` | b.ls 0x00bbe270 | `CONDITIONAL_JUMP`
<a id="insn-00bbe214"></a> `00bbe214` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe218"></a> `00bbe218` | `4a 00 00 b4` | cbz x10,0x00bbe220 | `CONDITIONAL_JUMP`
<a id="insn-00bbe21c"></a> `00bbe21c` | `8a 6a 6a b8` | ldr w10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe220"></a> `00bbe220` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe224"></a> `00bbe224` | `ea 43 02 b9` | str w10,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbe228"></a> `00bbe228` | `83 32 00 54` | b.cc 0x00bbe878 | `CONDITIONAL_JUMP`
<a id="insn-00bbe22c"></a> `00bbe22c` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe230"></a> `00bbe230` | `48 32 00 b4` | cbz x8,0x00bbe878 | `CONDITIONAL_JUMP`
<a id="insn-00bbe234"></a> `00bbe234` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe238"></a> `00bbe238` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe23c"></a> `00bbe23c` | `16 01 09 ab` | adds x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe240"></a> `00bbe240` | `c0 31 00 54` | b.eq 0x00bbe878 | `CONDITIONAL_JUMP`
<a id="insn-00bbe244"></a> `00bbe244` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe248"></a> `00bbe248` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe24c"></a> `00bbe24c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe250"></a> `00bbe250` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbe254"></a> `00bbe254` | `23 01 00 54` | b.cc 0x00bbe278 | `CONDITIONAL_JUMP`
<a id="insn-00bbe258"></a> `00bbe258` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbe25c"></a> `00bbe25c` | `08 01 00 b4` | cbz x8,0x00bbe27c | `CONDITIONAL_JUMP`
<a id="insn-00bbe260"></a> `00bbe260` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe264"></a> `00bbe264` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe268"></a> `00bbe268` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe26c"></a> `00bbe26c` | `04 00 00 14` | b 0x00bbe27c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe270"></a> `00bbe270` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbe274"></a> `00bbe274` | `81 01 00 14` | b 0x00bbe878 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe278"></a> `00bbe278` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe27c"></a> `00bbe27c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe280"></a> `00bbe280` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe284"></a> `00bbe284` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe288"></a> `00bbe288` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe28c"></a> `00bbe28c` | `89 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe290"></a> `00bbe290` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe294"></a> `00bbe294` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe298"></a> `00bbe298` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe29c"></a> `00bbe29c` | `b9 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2a0"></a> `00bbe2a0` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe2a4"></a> `00bbe2a4` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe2a8"></a> `00bbe2a8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe2ac"></a> `00bbe2ac` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbe2b0"></a> `00bbe2b0` | `e3 00 00 54` | b.cc 0x00bbe2cc | `CONDITIONAL_JUMP`
<a id="insn-00bbe2b4"></a> `00bbe2b4` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbe2b8"></a> `00bbe2b8` | `c8 00 00 b4` | cbz x8,0x00bbe2d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe2bc"></a> `00bbe2bc` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe2c0"></a> `00bbe2c0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe2c4"></a> `00bbe2c4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe2c8"></a> `00bbe2c8` | `02 00 00 14` | b 0x00bbe2d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe2cc"></a> `00bbe2cc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe2d0"></a> `00bbe2d0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe2d4"></a> `00bbe2d4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe2d8"></a> `00bbe2d8` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe2dc"></a> `00bbe2dc` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe2e0"></a> `00bbe2e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe2e4"></a> `00bbe2e4` | `15 61 00 91` | add x21,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe2e8"></a> `00bbe2e8` | `72 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2ec"></a> `00bbe2ec` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe2f0"></a> `00bbe2f0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe2f4"></a> `00bbe2f4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe2f8"></a> `00bbe2f8` | `a2 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2fc"></a> `00bbe2fc` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe300"></a> `00bbe300` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe304"></a> `00bbe304` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe308"></a> `00bbe308` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbe30c"></a> `00bbe30c` | `e3 00 00 54` | b.cc 0x00bbe328 | `CONDITIONAL_JUMP`
<a id="insn-00bbe310"></a> `00bbe310` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe314"></a> `00bbe314` | `c8 00 00 b4` | cbz x8,0x00bbe32c | `CONDITIONAL_JUMP`
<a id="insn-00bbe318"></a> `00bbe318` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe31c"></a> `00bbe31c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe320"></a> `00bbe320` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe324"></a> `00bbe324` | `02 00 00 14` | b 0x00bbe32c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe328"></a> `00bbe328` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe32c"></a> `00bbe32c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe330"></a> `00bbe330` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe334"></a> `00bbe334` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe338"></a> `00bbe338` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe33c"></a> `00bbe33c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe340"></a> `00bbe340` | `15 c1 00 91` | add x21,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe344"></a> `00bbe344` | `5b 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe348"></a> `00bbe348` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe34c"></a> `00bbe34c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe350"></a> `00bbe350` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe354"></a> `00bbe354` | `8b 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe358"></a> `00bbe358` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe35c"></a> `00bbe35c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe360"></a> `00bbe360` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe364"></a> `00bbe364` | `3f 2d 00 71` | cmp w9,#0xb | `FALL_THROUGH`
<a id="insn-00bbe368"></a> `00bbe368` | `e3 00 00 54` | b.cc 0x00bbe384 | `CONDITIONAL_JUMP`
<a id="insn-00bbe36c"></a> `00bbe36c` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbe370"></a> `00bbe370` | `c8 00 00 b4` | cbz x8,0x00bbe388 | `CONDITIONAL_JUMP`
<a id="insn-00bbe374"></a> `00bbe374` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe378"></a> `00bbe378` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe37c"></a> `00bbe37c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe380"></a> `00bbe380` | `02 00 00 14` | b 0x00bbe388 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe384"></a> `00bbe384` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe388"></a> `00bbe388` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe38c"></a> `00bbe38c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe390"></a> `00bbe390` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe394"></a> `00bbe394` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe398"></a> `00bbe398` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe39c"></a> `00bbe39c` | `15 21 01 91` | add x21,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbe3a0"></a> `00bbe3a0` | `44 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe3a4"></a> `00bbe3a4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe3a8"></a> `00bbe3a8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe3ac"></a> `00bbe3ac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe3b0"></a> `00bbe3b0` | `74 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe3b4"></a> `00bbe3b4` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe3b8"></a> `00bbe3b8` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe3bc"></a> `00bbe3bc` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe3c0"></a> `00bbe3c0` | `3f 35 00 71` | cmp w9,#0xd | `FALL_THROUGH`
<a id="insn-00bbe3c4"></a> `00bbe3c4` | `e3 00 00 54` | b.cc 0x00bbe3e0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe3c8"></a> `00bbe3c8` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbe3cc"></a> `00bbe3cc` | `c8 00 00 b4` | cbz x8,0x00bbe3e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe3d0"></a> `00bbe3d0` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe3d4"></a> `00bbe3d4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe3d8"></a> `00bbe3d8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe3dc"></a> `00bbe3dc` | `02 00 00 14` | b 0x00bbe3e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe3e0"></a> `00bbe3e0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe3e4"></a> `00bbe3e4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe3e8"></a> `00bbe3e8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe3ec"></a> `00bbe3ec` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe3f0"></a> `00bbe3f0` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe3f4"></a> `00bbe3f4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe3f8"></a> `00bbe3f8` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbe3fc"></a> `00bbe3fc` | `2d 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe400"></a> `00bbe400` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe404"></a> `00bbe404` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe408"></a> `00bbe408` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe40c"></a> `00bbe40c` | `5d 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe410"></a> `00bbe410` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe414"></a> `00bbe414` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe418"></a> `00bbe418` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe41c"></a> `00bbe41c` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbe420"></a> `00bbe420` | `e3 00 00 54` | b.cc 0x00bbe43c | `CONDITIONAL_JUMP`
<a id="insn-00bbe424"></a> `00bbe424` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbe428"></a> `00bbe428` | `c8 00 00 b4` | cbz x8,0x00bbe440 | `CONDITIONAL_JUMP`
<a id="insn-00bbe42c"></a> `00bbe42c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe430"></a> `00bbe430` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe434"></a> `00bbe434` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe438"></a> `00bbe438` | `02 00 00 14` | b 0x00bbe440 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe43c"></a> `00bbe43c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe440"></a> `00bbe440` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe444"></a> `00bbe444` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe448"></a> `00bbe448` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe44c"></a> `00bbe44c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe450"></a> `00bbe450` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe454"></a> `00bbe454` | `15 e1 01 91` | add x21,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbe458"></a> `00bbe458` | `16 67 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe45c"></a> `00bbe45c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe460"></a> `00bbe460` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe464"></a> `00bbe464` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe468"></a> `00bbe468` | `46 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe46c"></a> `00bbe46c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe470"></a> `00bbe470` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe474"></a> `00bbe474` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe478"></a> `00bbe478` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbe47c"></a> `00bbe47c` | `e3 00 00 54` | b.cc 0x00bbe498 | `CONDITIONAL_JUMP`
<a id="insn-00bbe480"></a> `00bbe480` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe484"></a> `00bbe484` | `c8 00 00 b4` | cbz x8,0x00bbe49c | `CONDITIONAL_JUMP`
<a id="insn-00bbe488"></a> `00bbe488` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe48c"></a> `00bbe48c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe490"></a> `00bbe490` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe494"></a> `00bbe494` | `02 00 00 14` | b 0x00bbe49c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe498"></a> `00bbe498` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe49c"></a> `00bbe49c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe4a0"></a> `00bbe4a0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe4a4"></a> `00bbe4a4` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe4a8"></a> `00bbe4a8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe4ac"></a> `00bbe4ac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe4b0"></a> `00bbe4b0` | `15 41 02 91` | add x21,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbe4b4"></a> `00bbe4b4` | `ff 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe4b8"></a> `00bbe4b8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe4bc"></a> `00bbe4bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe4c0"></a> `00bbe4c0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe4c4"></a> `00bbe4c4` | `2f 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe4c8"></a> `00bbe4c8` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe4cc"></a> `00bbe4cc` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe4d0"></a> `00bbe4d0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe4d4"></a> `00bbe4d4` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbe4d8"></a> `00bbe4d8` | `e3 00 00 54` | b.cc 0x00bbe4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4dc"></a> `00bbe4dc` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbe4e0"></a> `00bbe4e0` | `c8 00 00 b4` | cbz x8,0x00bbe4f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4e4"></a> `00bbe4e4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe4e8"></a> `00bbe4e8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe4ec"></a> `00bbe4ec` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe4f0"></a> `00bbe4f0` | `02 00 00 14` | b 0x00bbe4f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe4f4"></a> `00bbe4f4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe4f8"></a> `00bbe4f8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe4fc"></a> `00bbe4fc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe500"></a> `00bbe500` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe504"></a> `00bbe504` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe508"></a> `00bbe508` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe50c"></a> `00bbe50c` | `15 a1 02 91` | add x21,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbe510"></a> `00bbe510` | `e8 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe514"></a> `00bbe514` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe518"></a> `00bbe518` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe51c"></a> `00bbe51c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe520"></a> `00bbe520` | `18 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe524"></a> `00bbe524` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe528"></a> `00bbe528` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe52c"></a> `00bbe52c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe530"></a> `00bbe530` | `3f 55 00 71` | cmp w9,#0x15 | `FALL_THROUGH`
<a id="insn-00bbe534"></a> `00bbe534` | `e3 00 00 54` | b.cc 0x00bbe550 | `CONDITIONAL_JUMP`
<a id="insn-00bbe538"></a> `00bbe538` | `08 29 40 79` | ldrh w8,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe53c"></a> `00bbe53c` | `c8 00 00 b4` | cbz x8,0x00bbe554 | `CONDITIONAL_JUMP`
<a id="insn-00bbe540"></a> `00bbe540` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe544"></a> `00bbe544` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe548"></a> `00bbe548` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe54c"></a> `00bbe54c` | `02 00 00 14` | b 0x00bbe554 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe550"></a> `00bbe550` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe554"></a> `00bbe554` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe558"></a> `00bbe558` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe55c"></a> `00bbe55c` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe560"></a> `00bbe560` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe564"></a> `00bbe564` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe568"></a> `00bbe568` | `15 01 03 91` | add x21,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbe56c"></a> `00bbe56c` | `d1 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe570"></a> `00bbe570` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe574"></a> `00bbe574` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe578"></a> `00bbe578` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe57c"></a> `00bbe57c` | `01 73 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe580"></a> `00bbe580` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe584"></a> `00bbe584` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe588"></a> `00bbe588` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe58c"></a> `00bbe58c` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbe590"></a> `00bbe590` | `63 08 00 54` | b.cc 0x00bbe69c | `CONDITIONAL_JUMP`
<a id="insn-00bbe594"></a> `00bbe594` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbe598"></a> `00bbe598` | `28 08 00 b4` | cbz x8,0x00bbe69c | `CONDITIONAL_JUMP`
<a id="insn-00bbe59c"></a> `00bbe59c` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe5a0"></a> `00bbe5a0` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbe5a4"></a> `00bbe5a4` | `e9 a3 52 a9` | ldp x9,x8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe5a8"></a> `00bbe5a8` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe5ac"></a> `00bbe5ac` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe5b0"></a> `00bbe5b0` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbe5b4"></a> `00bbe5b4` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe5b8"></a> `00bbe5b8` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbe5bc"></a> `00bbe5bc` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbe5c0"></a> `00bbe5c0` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbe5c4"></a> `00bbe5c4` | `c2 00 00 54` | b.cs 0x00bbe5dc | `CONDITIONAL_JUMP`
<a id="insn-00bbe5c8"></a> `00bbe5c8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe5cc"></a> `00bbe5cc` | `00 61 03 91` | add x0,x8,#0xd8 | `FALL_THROUGH`
<a id="insn-00bbe5d0"></a> `00bbe5d0` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbe5d4"></a> `00bbe5d4` | `17 7c 02 94` | bl 0x00c5d630 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe5d8"></a> `00bbe5d8` | `12 00 00 14` | b 0x00bbe620 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe5dc"></a> `00bbe5dc` | `29 02 00 54` | b.ls 0x00bbe620 | `CONDITIONAL_JUMP`
<a id="insn-00bbe5e0"></a> `00bbe5e0` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe5e4"></a> `00bbe5e4` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbe5e8"></a> `00bbe5e8` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe5ec"></a> `00bbe5ec` | `80 01 00 54` | b.eq 0x00bbe61c | `CONDITIONAL_JUMP`
<a id="insn-00bbe5f0"></a> `00bbe5f0` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbe5f4"></a> `00bbe5f4` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe5f8"></a> `00bbe5f8` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbe610 | `CONDITIONAL_JUMP`
<a id="insn-00bbe5fc"></a> `00bbe5fc` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbe600"></a> `00bbe600` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbe604"></a> `00bbe604` | `c0 00 00 54` | b.eq 0x00bbe61c | `CONDITIONAL_JUMP`
<a id="insn-00bbe608"></a> `00bbe608` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe60c"></a> `00bbe60c` | `89 ff 07 36` | tbz w9,#0x0,0x00bbe5fc | `CONDITIONAL_JUMP`
<a id="insn-00bbe610"></a> `00bbe610` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbe614"></a> `00bbe614` | `5b 66 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe618"></a> `00bbe618` | `f9 ff ff 17` | b 0x00bbe5fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe61c"></a> `00bbe61c` | `f4 9b 00 f9` | str x20,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbe620"></a> `00bbe620` | `f3 03 00 34` | cbz w19,0x00bbe69c | `CONDITIONAL_JUMP`
<a id="insn-00bbe624"></a> `00bbe624` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbe628"></a> `00bbe628` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe62c"></a> `00bbe62c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe630"></a> `00bbe630` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe634"></a> `00bbe634` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe638"></a> `00bbe638` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbe63c"></a> `00bbe63c` | `e3 00 00 54` | b.cc 0x00bbe658 | `CONDITIONAL_JUMP`
<a id="insn-00bbe640"></a> `00bbe640` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbe644"></a> `00bbe644` | `c8 00 00 b4` | cbz x8,0x00bbe65c | `CONDITIONAL_JUMP`
<a id="insn-00bbe648"></a> `00bbe648` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe64c"></a> `00bbe64c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe650"></a> `00bbe650` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe654"></a> `00bbe654` | `02 00 00 14` | b 0x00bbe65c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe658"></a> `00bbe658` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe65c"></a> `00bbe65c` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe660"></a> `00bbe660` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe664"></a> `00bbe664` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbe668"></a> `00bbe668` | `ea 97 40 f9` | ldr x10,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe66c"></a> `00bbe66c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe670"></a> `00bbe670` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe674"></a> `00bbe674` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe678"></a> `00bbe678` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbe67c"></a> `00bbe67c` | `8d 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe680"></a> `00bbe680` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe684"></a> `00bbe684` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe688"></a> `00bbe688` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe68c"></a> `00bbe68c` | `bd 72 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe690"></a> `00bbe690` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe694"></a> `00bbe694` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbe698"></a> `00bbe698` | `a1 fc ff 54` | b.ne 0x00bbe62c | `CONDITIONAL_JUMP`
<a id="insn-00bbe69c"></a> `00bbe69c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe6a0"></a> `00bbe6a0` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe6a4"></a> `00bbe6a4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe6a8"></a> `00bbe6a8` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbe6ac"></a> `00bbe6ac` | `e3 00 00 54` | b.cc 0x00bbe6c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6b0"></a> `00bbe6b0` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe6b4"></a> `00bbe6b4` | `c8 00 00 b4` | cbz x8,0x00bbe6cc | `CONDITIONAL_JUMP`
<a id="insn-00bbe6b8"></a> `00bbe6b8` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe6bc"></a> `00bbe6bc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe6c0"></a> `00bbe6c0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe6c4"></a> `00bbe6c4` | `02 00 00 14` | b 0x00bbe6cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6c8"></a> `00bbe6c8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe6cc"></a> `00bbe6cc` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe6d0"></a> `00bbe6d0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe6d4"></a> `00bbe6d4` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe6d8"></a> `00bbe6d8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe6dc"></a> `00bbe6dc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe6e0"></a> `00bbe6e0` | `15 c1 03 91` | add x21,x8,#0xf0 | `FALL_THROUGH`
<a id="insn-00bbe6e4"></a> `00bbe6e4` | `73 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6e8"></a> `00bbe6e8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe6ec"></a> `00bbe6ec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe6f0"></a> `00bbe6f0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe6f4"></a> `00bbe6f4` | `a3 72 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6f8"></a> `00bbe6f8` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe6fc"></a> `00bbe6fc` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe700"></a> `00bbe700` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe704"></a> `00bbe704` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe708"></a> `00bbe708` | `63 08 00 54` | b.cc 0x00bbe814 | `CONDITIONAL_JUMP`
<a id="insn-00bbe70c"></a> `00bbe70c` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe710"></a> `00bbe710` | `28 08 00 b4` | cbz x8,0x00bbe814 | `CONDITIONAL_JUMP`
<a id="insn-00bbe714"></a> `00bbe714` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe718"></a> `00bbe718` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbe71c"></a> `00bbe71c` | `e9 a3 55 a9` | ldp x9,x8,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbe720"></a> `00bbe720` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe724"></a> `00bbe724` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe728"></a> `00bbe728` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbe72c"></a> `00bbe72c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe730"></a> `00bbe730` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbe734"></a> `00bbe734` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbe738"></a> `00bbe738` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbe73c"></a> `00bbe73c` | `c2 00 00 54` | b.cs 0x00bbe754 | `CONDITIONAL_JUMP`
<a id="insn-00bbe740"></a> `00bbe740` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe744"></a> `00bbe744` | `00 21 04 91` | add x0,x8,#0x108 | `FALL_THROUGH`
<a id="insn-00bbe748"></a> `00bbe748` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbe74c"></a> `00bbe74c` | `b9 7b 02 94` | bl 0x00c5d630 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe750"></a> `00bbe750` | `12 00 00 14` | b 0x00bbe798 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe754"></a> `00bbe754` | `29 02 00 54` | b.ls 0x00bbe798 | `CONDITIONAL_JUMP`
<a id="insn-00bbe758"></a> `00bbe758` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe75c"></a> `00bbe75c` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbe760"></a> `00bbe760` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe764"></a> `00bbe764` | `80 01 00 54` | b.eq 0x00bbe794 | `CONDITIONAL_JUMP`
<a id="insn-00bbe768"></a> `00bbe768` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbe76c"></a> `00bbe76c` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe770"></a> `00bbe770` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbe788 | `CONDITIONAL_JUMP`
<a id="insn-00bbe774"></a> `00bbe774` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbe778"></a> `00bbe778` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbe77c"></a> `00bbe77c` | `c0 00 00 54` | b.eq 0x00bbe794 | `CONDITIONAL_JUMP`
<a id="insn-00bbe780"></a> `00bbe780` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe784"></a> `00bbe784` | `89 ff 07 36` | tbz w9,#0x0,0x00bbe774 | `CONDITIONAL_JUMP`
<a id="insn-00bbe788"></a> `00bbe788` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbe78c"></a> `00bbe78c` | `fd 65 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe790"></a> `00bbe790` | `f9 ff ff 17` | b 0x00bbe774 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe794"></a> `00bbe794` | `f4 b3 00 f9` | str x20,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbe798"></a> `00bbe798` | `f3 03 00 34` | cbz w19,0x00bbe814 | `CONDITIONAL_JUMP`
<a id="insn-00bbe79c"></a> `00bbe79c` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbe7a0"></a> `00bbe7a0` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe7a4"></a> `00bbe7a4` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe7a8"></a> `00bbe7a8` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe7ac"></a> `00bbe7ac` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe7b0"></a> `00bbe7b0` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe7b4"></a> `00bbe7b4` | `e3 00 00 54` | b.cc 0x00bbe7d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7b8"></a> `00bbe7b8` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe7bc"></a> `00bbe7bc` | `c8 00 00 b4` | cbz x8,0x00bbe7d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7c0"></a> `00bbe7c0` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe7c4"></a> `00bbe7c4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe7c8"></a> `00bbe7c8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe7cc"></a> `00bbe7cc` | `02 00 00 14` | b 0x00bbe7d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe7d0"></a> `00bbe7d0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe7d4"></a> `00bbe7d4` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe7d8"></a> `00bbe7d8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe7dc"></a> `00bbe7dc` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbe7e0"></a> `00bbe7e0` | `ea af 40 f9` | ldr x10,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbe7e4"></a> `00bbe7e4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe7e8"></a> `00bbe7e8` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe7ec"></a> `00bbe7ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe7f0"></a> `00bbe7f0` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbe7f4"></a> `00bbe7f4` | `2f 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe7f8"></a> `00bbe7f8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe7fc"></a> `00bbe7fc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe800"></a> `00bbe800` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe804"></a> `00bbe804` | `5f 72 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe808"></a> `00bbe808` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe80c"></a> `00bbe80c` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbe810"></a> `00bbe810` | `a1 fc ff 54` | b.ne 0x00bbe7a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe814"></a> `00bbe814` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe818"></a> `00bbe818` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe81c"></a> `00bbe81c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe820"></a> `00bbe820` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bbe824"></a> `00bbe824` | `e3 00 00 54` | b.cc 0x00bbe840 | `CONDITIONAL_JUMP`
<a id="insn-00bbe828"></a> `00bbe828` | `08 39 40 79` | ldrh w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbe82c"></a> `00bbe82c` | `c8 00 00 b4` | cbz x8,0x00bbe844 | `CONDITIONAL_JUMP`
<a id="insn-00bbe830"></a> `00bbe830` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe834"></a> `00bbe834` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe838"></a> `00bbe838` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe83c"></a> `00bbe83c` | `02 00 00 14` | b 0x00bbe844 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe840"></a> `00bbe840` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe844"></a> `00bbe844` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe848"></a> `00bbe848` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe84c"></a> `00bbe84c` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe850"></a> `00bbe850` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe854"></a> `00bbe854` | `17 66 02 94` | bl 0x00c580b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe858"></a> `00bbe858` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe85c"></a> `00bbe85c` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbe860"></a> `00bbe860` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe864"></a> `00bbe864` | `f3 e3 00 91` | add x19,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbe868"></a> `00bbe868` | `46 72 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe86c"></a> `00bbe86c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe870"></a> `00bbe870` | `f3 bb 00 f9` | str x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbe874"></a> `00bbe874` | `e8 3f 01 f9` | str x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe878"></a> `00bbe878` | `48 07 40 a9` | ldp x8,x1,[x26] | `FALL_THROUGH`
<a id="insn-00bbe87c"></a> `00bbe87c` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe880"></a> `00bbe880` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbe884"></a> `00bbe884` | `e8 3f 41 f9` | ldr x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe888"></a> `00bbe888` | `68 00 00 b4` | cbz x8,0x00bbe894 | `CONDITIONAL_JUMP`
<a id="insn-00bbe88c"></a> `00bbe88c` | `1f 91 00 f9` | str xzr,[x8, #0x120] | `FALL_THROUGH`
<a id="insn-00bbe890"></a> `00bbe890` | `ff 3f 01 f9` | str xzr,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe894"></a> `00bbe894` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbe898"></a> `00bbe898` | `68 00 00 36` | tbz w8,#0x0,0x00bbe8a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe89c"></a> `00bbe89c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbe8a0"></a> `00bbe8a0` | `b8 65 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8a4"></a> `00bbe8a4` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe8a8"></a> `00bbe8a8` | `be 7a 02 94` | bl 0x00c5d3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8ac"></a> `00bbe8ac` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe8b0"></a> `00bbe8b0` | `04 7b 02 94` | bl 0x00c5d4c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8b4"></a> `00bbe8b4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbe8b8"></a> `00bbe8b8` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbe8bc"></a> `00bbe8bc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe8c0"></a> `00bbe8c0` | `21 01 00 54` | b.ne 0x00bbe8e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8c4"></a> `00bbe8c4` | `ff 83 0b 91` | add sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbe8c8"></a> `00bbe8c8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbe8cc"></a> `00bbe8cc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbe8d0"></a> `00bbe8d0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbe8d4"></a> `00bbe8d4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe8d8"></a> `00bbe8d8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe8dc"></a> `00bbe8dc` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bbe8e0"></a> `00bbe8e0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbe8e4"></a> `00bbe8e4` | `b3 65 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdae8`](#insn-00bbdae8) 範囲 `[['00bbdae8', '00bbdb27']]`
  - `FALL_THROUGH` [`00bbdb24`](#insn-00bbdb24) → [`00bbdb28`](#insn-00bbdb28)
- ブロック [`00bbdb28`](#insn-00bbdb28) 範囲 `[['00bbdb28', '00bbdbaf']]`
  - `CONDITIONAL_JUMP` [`00bbdbac`](#insn-00bbdbac) → [`00bbdbc4`](#insn-00bbdbc4)
  - `FALL_THROUGH` [`00bbdbac`](#insn-00bbdbac) → [`00bbdbb0`](#insn-00bbdbb0)
- ブロック [`00bbdbb0`](#insn-00bbdbb0) 範囲 `[['00bbdbb0', '00bbdbb3']]`
  - `FALL_THROUGH` [`00bbdbb0`](#insn-00bbdbb0) → [`00bbdbb4`](#insn-00bbdbb4)
- ブロック [`00bbdbb4`](#insn-00bbdbb4) 範囲 `[['00bbdbb4', '00bbdbb7']]`
  - `CONDITIONAL_JUMP` [`00bbdbb4`](#insn-00bbdbb4) → [`00bbdbc4`](#insn-00bbdbc4)
  - `FALL_THROUGH` [`00bbdbb4`](#insn-00bbdbb4) → [`00bbdbb8`](#insn-00bbdbb8)
- ブロック [`00bbdbb8`](#insn-00bbdbb8) 範囲 `[['00bbdbb8', '00bbdbc3']]`
  - `FALL_THROUGH` [`00bbdbc0`](#insn-00bbdbc0) → [`00bbdbc4`](#insn-00bbdbc4)
- ブロック [`00bbdbc4`](#insn-00bbdbc4) 範囲 `[['00bbdbc4', '00bbdc03']]`
  - `CONDITIONAL_JUMP` [`00bbdc00`](#insn-00bbdc00) → [`00bbdc1c`](#insn-00bbdc1c)
  - `FALL_THROUGH` [`00bbdc00`](#insn-00bbdc00) → [`00bbdc04`](#insn-00bbdc04)
- ブロック [`00bbdc04`](#insn-00bbdc04) 範囲 `[['00bbdc04', '00bbdc0b']]`
  - `CONDITIONAL_JUMP` [`00bbdc08`](#insn-00bbdc08) → [`00bbdc20`](#insn-00bbdc20)
  - `FALL_THROUGH` [`00bbdc08`](#insn-00bbdc08) → [`00bbdc0c`](#insn-00bbdc0c)
- ブロック [`00bbdc0c`](#insn-00bbdc0c) 範囲 `[['00bbdc0c', '00bbdc1b']]`
  - `UNCONDITIONAL_JUMP` [`00bbdc18`](#insn-00bbdc18) → [`00bbdc20`](#insn-00bbdc20)
- ブロック [`00bbdc1c`](#insn-00bbdc1c) 範囲 `[['00bbdc1c', '00bbdc1f']]`
  - `FALL_THROUGH` [`00bbdc1c`](#insn-00bbdc1c) → [`00bbdc20`](#insn-00bbdc20)
- ブロック [`00bbdc20`](#insn-00bbdc20) 範囲 `[['00bbdc20', '00bbdc43']]`
  - `FALL_THROUGH` [`00bbdc40`](#insn-00bbdc40) → [`00bbdc44`](#insn-00bbdc44)
- ブロック [`00bbdc44`](#insn-00bbdc44) 範囲 `[['00bbdc44', '00bbdc63']]`
  - `CONDITIONAL_JUMP` [`00bbdc60`](#insn-00bbdc60) → [`00bbde08`](#insn-00bbde08)
  - `FALL_THROUGH` [`00bbdc60`](#insn-00bbdc60) → [`00bbdc64`](#insn-00bbdc64)
- ブロック [`00bbdc64`](#insn-00bbdc64) 範囲 `[['00bbdc64', '00bbdc6b']]`
  - `CONDITIONAL_JUMP` [`00bbdc68`](#insn-00bbdc68) → [`00bbde08`](#insn-00bbde08)
  - `FALL_THROUGH` [`00bbdc68`](#insn-00bbdc68) → [`00bbdc6c`](#insn-00bbdc6c)
- ブロック [`00bbdc6c`](#insn-00bbdc6c) 範囲 `[['00bbdc6c', '00bbdc7b']]`
  - `CONDITIONAL_JUMP` [`00bbdc78`](#insn-00bbdc78) → [`00bbde08`](#insn-00bbde08)
  - `FALL_THROUGH` [`00bbdc78`](#insn-00bbdc78) → [`00bbdc7c`](#insn-00bbdc7c)
- ブロック [`00bbdc7c`](#insn-00bbdc7c) 範囲 `[['00bbdc7c', '00bbdc83']]`
  - `CONDITIONAL_JUMP` [`00bbdc80`](#insn-00bbdc80) → [`00bbde08`](#insn-00bbde08)
  - `FALL_THROUGH` [`00bbdc80`](#insn-00bbdc80) → [`00bbdc84`](#insn-00bbdc84)
- ブロック [`00bbdc84`](#insn-00bbdc84) 範囲 `[['00bbdc84', '00bbdc9b']]`
  - `UNCONDITIONAL_JUMP` [`00bbdc98`](#insn-00bbdc98) → [`00bbdcac`](#insn-00bbdcac)
- ブロック [`00bbdc9c`](#insn-00bbdc9c) 範囲 `[['00bbdc9c', '00bbdcab']]`
  - `CONDITIONAL_JUMP` [`00bbdca8`](#insn-00bbdca8) → [`00bbddfc`](#insn-00bbddfc)
  - `FALL_THROUGH` [`00bbdca8`](#insn-00bbdca8) → [`00bbdcac`](#insn-00bbdcac)
- ブロック [`00bbdcac`](#insn-00bbdcac) 範囲 `[['00bbdcac', '00bbdce3']]`
  - `CONDITIONAL_JUMP` [`00bbdce0`](#insn-00bbdce0) → [`00bbdd24`](#insn-00bbdd24)
  - `FALL_THROUGH` [`00bbdce0`](#insn-00bbdce0) → [`00bbdce4`](#insn-00bbdce4)
- ブロック [`00bbdce4`](#insn-00bbdce4) 範囲 `[['00bbdce4', '00bbdceb']]`
  - `CONDITIONAL_JUMP` [`00bbdce8`](#insn-00bbdce8) → [`00bbdcf8`](#insn-00bbdcf8)
  - `FALL_THROUGH` [`00bbdce8`](#insn-00bbdce8) → [`00bbdcec`](#insn-00bbdcec)
- ブロック [`00bbdcec`](#insn-00bbdcec) 範囲 `[['00bbdcec', '00bbdcf7']]`
  - `FALL_THROUGH` [`00bbdcf4`](#insn-00bbdcf4) → [`00bbdcf8`](#insn-00bbdcf8)
- ブロック [`00bbdcf8`](#insn-00bbdcf8) 範囲 `[['00bbdcf8', '00bbdcfb']]`
  - `FALL_THROUGH` [`00bbdcf8`](#insn-00bbdcf8) → [`00bbdcfc`](#insn-00bbdcfc)
- ブロック [`00bbdcfc`](#insn-00bbdcfc) 範囲 `[['00bbdcfc', '00bbdd0b']]`
  - `CONDITIONAL_JUMP` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd30`](#insn-00bbdd30)
  - `FALL_THROUGH` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd0c`](#insn-00bbdd0c)
- ブロック [`00bbdd0c`](#insn-00bbdd0c) 範囲 `[['00bbdd0c', '00bbdd13']]`
  - `CONDITIONAL_JUMP` [`00bbdd10`](#insn-00bbdd10) → [`00bbdd30`](#insn-00bbdd30)
  - `FALL_THROUGH` [`00bbdd10`](#insn-00bbdd10) → [`00bbdd14`](#insn-00bbdd14)
- ブロック [`00bbdd14`](#insn-00bbdd14) 範囲 `[['00bbdd14', '00bbdd23']]`
  - `UNCONDITIONAL_JUMP` [`00bbdd20`](#insn-00bbdd20) → [`00bbdd34`](#insn-00bbdd34)
- ブロック [`00bbdd24`](#insn-00bbdd24) 範囲 `[['00bbdd24', '00bbdd2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbdd2c`](#insn-00bbdd2c) → [`00bbdd34`](#insn-00bbdd34)
- ブロック [`00bbdd30`](#insn-00bbdd30) 範囲 `[['00bbdd30', '00bbdd33']]`
  - `FALL_THROUGH` [`00bbdd30`](#insn-00bbdd30) → [`00bbdd34`](#insn-00bbdd34)
- ブロック [`00bbdd34`](#insn-00bbdd34) 範囲 `[['00bbdd34', '00bbdd63']]`
  - `CONDITIONAL_JUMP` [`00bbdd60`](#insn-00bbdd60) → [`00bbddcc`](#insn-00bbddcc)
  - `FALL_THROUGH` [`00bbdd60`](#insn-00bbdd60) → [`00bbdd64`](#insn-00bbdd64)
- ブロック [`00bbdd64`](#insn-00bbdd64) 範囲 `[['00bbdd64', '00bbdda7']]`
  - `CONDITIONAL_JUMP` [`00bbdda4`](#insn-00bbdda4) → [`00bbddb4`](#insn-00bbddb4)
  - `FALL_THROUGH` [`00bbdda4`](#insn-00bbdda4) → [`00bbdda8`](#insn-00bbdda8)
- ブロック [`00bbdda8`](#insn-00bbdda8) 範囲 `[['00bbdda8', '00bbddb3']]`
  - `UNCONDITIONAL_JUMP` [`00bbddb0`](#insn-00bbddb0) → [`00bbddb8`](#insn-00bbddb8)
- ブロック [`00bbddb4`](#insn-00bbddb4) 範囲 `[['00bbddb4', '00bbddb7']]`
  - `FALL_THROUGH` [`00bbddb4`](#insn-00bbddb4) → [`00bbddb8`](#insn-00bbddb8)
- ブロック [`00bbddb8`](#insn-00bbddb8) 範囲 `[['00bbddb8', '00bbddcb']]`
  - `FALL_THROUGH` [`00bbddc8`](#insn-00bbddc8) → [`00bbddcc`](#insn-00bbddcc)
- ブロック [`00bbddcc`](#insn-00bbddcc) 範囲 `[['00bbddcc', '00bbddd3']]`
  - `FALL_THROUGH` [`00bbddd0`](#insn-00bbddd0) → [`00bbddd4`](#insn-00bbddd4)
- ブロック [`00bbddd4`](#insn-00bbddd4) 範囲 `[['00bbddd4', '00bbddef']]`
  - `CONDITIONAL_JUMP` [`00bbddec`](#insn-00bbddec) → [`00bbdc9c`](#insn-00bbdc9c)
  - `FALL_THROUGH` [`00bbddec`](#insn-00bbddec) → [`00bbddf0`](#insn-00bbddf0)
- ブロック [`00bbddf0`](#insn-00bbddf0) 範囲 `[['00bbddf0', '00bbddfb']]`
  - `UNCONDITIONAL_JUMP` [`00bbddf8`](#insn-00bbddf8) → [`00bbdc9c`](#insn-00bbdc9c)
- ブロック [`00bbddfc`](#insn-00bbddfc) 範囲 `[['00bbddfc', '00bbde07']]`
  - `FALL_THROUGH` [`00bbde04`](#insn-00bbde04) → [`00bbde08`](#insn-00bbde08)
- ブロック [`00bbde08`](#insn-00bbde08) 範囲 `[['00bbde08', '00bbde17']]`
  - `CONDITIONAL_JUMP` [`00bbde14`](#insn-00bbde14) → [`00bbdedc`](#insn-00bbdedc)
  - `FALL_THROUGH` [`00bbde14`](#insn-00bbde14) → [`00bbde18`](#insn-00bbde18)
- ブロック [`00bbde18`](#insn-00bbde18) 範囲 `[['00bbde18', '00bbde1f']]`
  - `CONDITIONAL_JUMP` [`00bbde1c`](#insn-00bbde1c) → [`00bbdedc`](#insn-00bbdedc)
  - `FALL_THROUGH` [`00bbde1c`](#insn-00bbde1c) → [`00bbde20`](#insn-00bbde20)
- ブロック [`00bbde20`](#insn-00bbde20) 範囲 `[['00bbde20', '00bbde27']]`
  - `FALL_THROUGH` [`00bbde24`](#insn-00bbde24) → [`00bbde28`](#insn-00bbde28)
- ブロック [`00bbde28`](#insn-00bbde28) 範囲 `[['00bbde28', '00bbde2f']]`
  - `CONDITIONAL_JUMP` [`00bbde2c`](#insn-00bbde2c) → [`00bbdedc`](#insn-00bbdedc)
  - `FALL_THROUGH` [`00bbde2c`](#insn-00bbde2c) → [`00bbde30`](#insn-00bbde30)
- ブロック [`00bbde30`](#insn-00bbde30) 範囲 `[['00bbde30', '00bbde47']]`
  - `CONDITIONAL_JUMP` [`00bbde44`](#insn-00bbde44) → [`00bbde8c`](#insn-00bbde8c)
  - `FALL_THROUGH` [`00bbde44`](#insn-00bbde44) → [`00bbde48`](#insn-00bbde48)
- ブロック [`00bbde48`](#insn-00bbde48) 範囲 `[['00bbde48', '00bbde67']]`
  - `FALL_THROUGH` [`00bbde64`](#insn-00bbde64) → [`00bbde68`](#insn-00bbde68)
- ブロック [`00bbde68`](#insn-00bbde68) 範囲 `[['00bbde68', '00bbde6b']]`
  - `CONDITIONAL_JUMP` [`00bbde68`](#insn-00bbde68) → [`00bbde78`](#insn-00bbde78)
  - `FALL_THROUGH` [`00bbde68`](#insn-00bbde68) → [`00bbde6c`](#insn-00bbde6c)
- ブロック [`00bbde6c`](#insn-00bbde6c) 範囲 `[['00bbde6c', '00bbde77']]`
  - `FALL_THROUGH` [`00bbde74`](#insn-00bbde74) → [`00bbde78`](#insn-00bbde78)
- ブロック [`00bbde78`](#insn-00bbde78) 範囲 `[['00bbde78', '00bbde83']]`
  - `CONDITIONAL_JUMP` [`00bbde80`](#insn-00bbde80) → [`00bbde8c`](#insn-00bbde8c)
  - `FALL_THROUGH` [`00bbde80`](#insn-00bbde80) → [`00bbde84`](#insn-00bbde84)
- ブロック [`00bbde84`](#insn-00bbde84) 範囲 `[['00bbde84', '00bbde8b']]`
  - `FALL_THROUGH` [`00bbde88`](#insn-00bbde88) → [`00bbde8c`](#insn-00bbde8c)
- ブロック [`00bbde8c`](#insn-00bbde8c) 範囲 `[['00bbde8c', '00bbdedb']]`
  - `FALL_THROUGH` [`00bbded8`](#insn-00bbded8) → [`00bbdedc`](#insn-00bbdedc)
- ブロック [`00bbdedc`](#insn-00bbdedc) 範囲 `[['00bbdedc', '00bbdeeb']]`
  - `CONDITIONAL_JUMP` [`00bbdee8`](#insn-00bbdee8) → [`00bbdf04`](#insn-00bbdf04)
  - `FALL_THROUGH` [`00bbdee8`](#insn-00bbdee8) → [`00bbdeec`](#insn-00bbdeec)
- ブロック [`00bbdeec`](#insn-00bbdeec) 範囲 `[['00bbdeec', '00bbdef3']]`
  - `CONDITIONAL_JUMP` [`00bbdef0`](#insn-00bbdef0) → [`00bbdf08`](#insn-00bbdf08)
  - `FALL_THROUGH` [`00bbdef0`](#insn-00bbdef0) → [`00bbdef4`](#insn-00bbdef4)
- ブロック [`00bbdef4`](#insn-00bbdef4) 範囲 `[['00bbdef4', '00bbdf03']]`
  - `UNCONDITIONAL_JUMP` [`00bbdf00`](#insn-00bbdf00) → [`00bbdf08`](#insn-00bbdf08)
- ブロック [`00bbdf04`](#insn-00bbdf04) 範囲 `[['00bbdf04', '00bbdf07']]`
  - `FALL_THROUGH` [`00bbdf04`](#insn-00bbdf04) → [`00bbdf08`](#insn-00bbdf08)
- ブロック [`00bbdf08`](#insn-00bbdf08) 範囲 `[['00bbdf08', '00bbdf47']]`
  - `CONDITIONAL_JUMP` [`00bbdf44`](#insn-00bbdf44) → [`00bbdf60`](#insn-00bbdf60)
  - `FALL_THROUGH` [`00bbdf44`](#insn-00bbdf44) → [`00bbdf48`](#insn-00bbdf48)
- ブロック [`00bbdf48`](#insn-00bbdf48) 範囲 `[['00bbdf48', '00bbdf4f']]`
  - `CONDITIONAL_JUMP` [`00bbdf4c`](#insn-00bbdf4c) → [`00bbdf64`](#insn-00bbdf64)
  - `FALL_THROUGH` [`00bbdf4c`](#insn-00bbdf4c) → [`00bbdf50`](#insn-00bbdf50)
- ブロック [`00bbdf50`](#insn-00bbdf50) 範囲 `[['00bbdf50', '00bbdf5f']]`
  - `UNCONDITIONAL_JUMP` [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf64`](#insn-00bbdf64)
- ブロック [`00bbdf60`](#insn-00bbdf60) 範囲 `[['00bbdf60', '00bbdf63']]`
  - `FALL_THROUGH` [`00bbdf60`](#insn-00bbdf60) → [`00bbdf64`](#insn-00bbdf64)
- ブロック [`00bbdf64`](#insn-00bbdf64) 範囲 `[['00bbdf64', '00bbdf7f']]`
  - `FALL_THROUGH` [`00bbdf7c`](#insn-00bbdf7c) → [`00bbdf80`](#insn-00bbdf80)
- ブロック [`00bbdf80`](#insn-00bbdf80) 範囲 `[['00bbdf80', '00bbdfa7']]`
  - `CONDITIONAL_JUMP` [`00bbdfa4`](#insn-00bbdfa4) → [`00bbdfc0`](#insn-00bbdfc0)
  - `FALL_THROUGH` [`00bbdfa4`](#insn-00bbdfa4) → [`00bbdfa8`](#insn-00bbdfa8)
- ブロック [`00bbdfa8`](#insn-00bbdfa8) 範囲 `[['00bbdfa8', '00bbdfaf']]`
  - `CONDITIONAL_JUMP` [`00bbdfac`](#insn-00bbdfac) → [`00bbdfc4`](#insn-00bbdfc4)
  - `FALL_THROUGH` [`00bbdfac`](#insn-00bbdfac) → [`00bbdfb0`](#insn-00bbdfb0)
- ブロック [`00bbdfb0`](#insn-00bbdfb0) 範囲 `[['00bbdfb0', '00bbdfb7']]`
  - `FALL_THROUGH` [`00bbdfb4`](#insn-00bbdfb4) → [`00bbdfb8`](#insn-00bbdfb8)
- ブロック [`00bbdfb8`](#insn-00bbdfb8) 範囲 `[['00bbdfb8', '00bbdfbf']]`
  - `UNCONDITIONAL_JUMP` [`00bbdfbc`](#insn-00bbdfbc) → [`00bbdfc4`](#insn-00bbdfc4)
- ブロック [`00bbdfc0`](#insn-00bbdfc0) 範囲 `[['00bbdfc0', '00bbdfc3']]`
  - `FALL_THROUGH` [`00bbdfc0`](#insn-00bbdfc0) → [`00bbdfc4`](#insn-00bbdfc4)
- ブロック [`00bbdfc4`](#insn-00bbdfc4) 範囲 `[['00bbdfc4', '00bbdfd3']]`
  - `FALL_THROUGH` [`00bbdfd0`](#insn-00bbdfd0) → [`00bbdfd4`](#insn-00bbdfd4)
- ブロック [`00bbdfd4`](#insn-00bbdfd4) 範囲 `[['00bbdfd4', '00bbdfeb']]`
  - `FALL_THROUGH` [`00bbdfe8`](#insn-00bbdfe8) → [`00bbdfec`](#insn-00bbdfec)
- ブロック [`00bbdfec`](#insn-00bbdfec) 範囲 `[['00bbdfec', '00bbdfef']]`
  - `FALL_THROUGH` [`00bbdfec`](#insn-00bbdfec) → [`00bbdff0`](#insn-00bbdff0)
- ブロック [`00bbdff0`](#insn-00bbdff0) 範囲 `[['00bbdff0', '00bbdff3']]`
  - `FALL_THROUGH` [`00bbdff0`](#insn-00bbdff0) → [`00bbdff4`](#insn-00bbdff4)
- ブロック [`00bbdff4`](#insn-00bbdff4) 範囲 `[['00bbdff4', '00bbdff7']]`
  - `FALL_THROUGH` [`00bbdff4`](#insn-00bbdff4) → [`00bbdff8`](#insn-00bbdff8)
- ブロック [`00bbdff8`](#insn-00bbdff8) 範囲 `[['00bbdff8', '00bbdffb']]`
  - `CONDITIONAL_JUMP` [`00bbdff8`](#insn-00bbdff8) → [`00bbe014`](#insn-00bbe014)
  - `FALL_THROUGH` [`00bbdff8`](#insn-00bbdff8) → [`00bbdffc`](#insn-00bbdffc)
- ブロック [`00bbdffc`](#insn-00bbdffc) 範囲 `[['00bbdffc', '00bbe003']]`
  - `CONDITIONAL_JUMP` [`00bbe000`](#insn-00bbe000) → [`00bbe018`](#insn-00bbe018)
  - `FALL_THROUGH` [`00bbe000`](#insn-00bbe000) → [`00bbe004`](#insn-00bbe004)
- ブロック [`00bbe004`](#insn-00bbe004) 範囲 `[['00bbe004', '00bbe007']]`
  - `FALL_THROUGH` [`00bbe004`](#insn-00bbe004) → [`00bbe008`](#insn-00bbe008)
- ブロック [`00bbe008`](#insn-00bbe008) 範囲 `[['00bbe008', '00bbe013']]`
  - `UNCONDITIONAL_JUMP` [`00bbe010`](#insn-00bbe010) → [`00bbe018`](#insn-00bbe018)
- ブロック [`00bbe014`](#insn-00bbe014) 範囲 `[['00bbe014', '00bbe017']]`
  - `FALL_THROUGH` [`00bbe014`](#insn-00bbe014) → [`00bbe018`](#insn-00bbe018)
- ブロック [`00bbe018`](#insn-00bbe018) 範囲 `[['00bbe018', '00bbe01b']]`
  - `FALL_THROUGH` [`00bbe018`](#insn-00bbe018) → [`00bbe01c`](#insn-00bbe01c)
- ブロック [`00bbe01c`](#insn-00bbe01c) 範囲 `[['00bbe01c', '00bbe01f']]`
  - `FALL_THROUGH` [`00bbe01c`](#insn-00bbe01c) → [`00bbe020`](#insn-00bbe020)
- ブロック [`00bbe020`](#insn-00bbe020) 範囲 `[['00bbe020', '00bbe037']]`
  - `FALL_THROUGH` [`00bbe034`](#insn-00bbe034) → [`00bbe038`](#insn-00bbe038)
- ブロック [`00bbe038`](#insn-00bbe038) 範囲 `[['00bbe038', '00bbe043']]`
  - `FALL_THROUGH` [`00bbe040`](#insn-00bbe040) → [`00bbe044`](#insn-00bbe044)
- ブロック [`00bbe044`](#insn-00bbe044) 範囲 `[['00bbe044', '00bbe047']]`
  - `FALL_THROUGH` [`00bbe044`](#insn-00bbe044) → [`00bbe048`](#insn-00bbe048)
- ブロック [`00bbe048`](#insn-00bbe048) 範囲 `[['00bbe048', '00bbe04f']]`
  - `FALL_THROUGH` [`00bbe04c`](#insn-00bbe04c) → [`00bbe050`](#insn-00bbe050)
- ブロック [`00bbe050`](#insn-00bbe050) 範囲 `[['00bbe050', '00bbe057']]`
  - `CONDITIONAL_JUMP` [`00bbe054`](#insn-00bbe054) → [`00bbe090`](#insn-00bbe090)
  - `FALL_THROUGH` [`00bbe054`](#insn-00bbe054) → [`00bbe058`](#insn-00bbe058)
- ブロック [`00bbe058`](#insn-00bbe058) 範囲 `[['00bbe058', '00bbe05f']]`
  - `CONDITIONAL_JUMP` [`00bbe05c`](#insn-00bbe05c) → [`00bbe06c`](#insn-00bbe06c)
  - `FALL_THROUGH` [`00bbe05c`](#insn-00bbe05c) → [`00bbe060`](#insn-00bbe060)
- ブロック [`00bbe060`](#insn-00bbe060) 範囲 `[['00bbe060', '00bbe06b']]`
  - `FALL_THROUGH` [`00bbe068`](#insn-00bbe068) → [`00bbe06c`](#insn-00bbe06c)
- ブロック [`00bbe06c`](#insn-00bbe06c) 範囲 `[['00bbe06c', '00bbe06f']]`
  - `FALL_THROUGH` [`00bbe06c`](#insn-00bbe06c) → [`00bbe070`](#insn-00bbe070)
- ブロック [`00bbe070`](#insn-00bbe070) 範囲 `[['00bbe070', '00bbe073']]`
  - `FALL_THROUGH` [`00bbe070`](#insn-00bbe070) → [`00bbe074`](#insn-00bbe074)
- ブロック [`00bbe074`](#insn-00bbe074) 範囲 `[['00bbe074', '00bbe077']]`
  - `CONDITIONAL_JUMP` [`00bbe074`](#insn-00bbe074) → [`00bbe09c`](#insn-00bbe09c)
  - `FALL_THROUGH` [`00bbe074`](#insn-00bbe074) → [`00bbe078`](#insn-00bbe078)
- ブロック [`00bbe078`](#insn-00bbe078) 範囲 `[['00bbe078', '00bbe07b']]`
  - `FALL_THROUGH` [`00bbe078`](#insn-00bbe078) → [`00bbe07c`](#insn-00bbe07c)
- ブロック [`00bbe07c`](#insn-00bbe07c) 範囲 `[['00bbe07c', '00bbe07f']]`
  - `CONDITIONAL_JUMP` [`00bbe07c`](#insn-00bbe07c) → [`00bbe0a0`](#insn-00bbe0a0)
  - `FALL_THROUGH` [`00bbe07c`](#insn-00bbe07c) → [`00bbe080`](#insn-00bbe080)
- ブロック [`00bbe080`](#insn-00bbe080) 範囲 `[['00bbe080', '00bbe083']]`
  - `FALL_THROUGH` [`00bbe080`](#insn-00bbe080) → [`00bbe084`](#insn-00bbe084)
- ブロック [`00bbe084`](#insn-00bbe084) 範囲 `[['00bbe084', '00bbe08f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe08c`](#insn-00bbe08c) → [`00bbe0a0`](#insn-00bbe0a0)
- ブロック [`00bbe090`](#insn-00bbe090) 範囲 `[['00bbe090', '00bbe09b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe098`](#insn-00bbe098) → [`00bbe0a0`](#insn-00bbe0a0)
- ブロック [`00bbe09c`](#insn-00bbe09c) 範囲 `[['00bbe09c', '00bbe09f']]`
  - `FALL_THROUGH` [`00bbe09c`](#insn-00bbe09c) → [`00bbe0a0`](#insn-00bbe0a0)
- ブロック [`00bbe0a0`](#insn-00bbe0a0) 範囲 `[['00bbe0a0', '00bbe0d7']]`
  - `CONDITIONAL_JUMP` [`00bbe0d4`](#insn-00bbe0d4) → [`00bbe0f0`](#insn-00bbe0f0)
  - `FALL_THROUGH` [`00bbe0d4`](#insn-00bbe0d4) → [`00bbe0d8`](#insn-00bbe0d8)
- ブロック [`00bbe0d8`](#insn-00bbe0d8) 範囲 `[['00bbe0d8', '00bbe0df']]`
  - `CONDITIONAL_JUMP` [`00bbe0dc`](#insn-00bbe0dc) → [`00bbe0f4`](#insn-00bbe0f4)
  - `FALL_THROUGH` [`00bbe0dc`](#insn-00bbe0dc) → [`00bbe0e0`](#insn-00bbe0e0)
- ブロック [`00bbe0e0`](#insn-00bbe0e0) 範囲 `[['00bbe0e0', '00bbe0ef']]`
  - `UNCONDITIONAL_JUMP` [`00bbe0ec`](#insn-00bbe0ec) → [`00bbe0f4`](#insn-00bbe0f4)
- ブロック [`00bbe0f0`](#insn-00bbe0f0) 範囲 `[['00bbe0f0', '00bbe0f3']]`
  - `FALL_THROUGH` [`00bbe0f0`](#insn-00bbe0f0) → [`00bbe0f4`](#insn-00bbe0f4)
- ブロック [`00bbe0f4`](#insn-00bbe0f4) 範囲 `[['00bbe0f4', '00bbe133']]`
  - `CONDITIONAL_JUMP` [`00bbe130`](#insn-00bbe130) → [`00bbe14c`](#insn-00bbe14c)
  - `FALL_THROUGH` [`00bbe130`](#insn-00bbe130) → [`00bbe134`](#insn-00bbe134)
- ブロック [`00bbe134`](#insn-00bbe134) 範囲 `[['00bbe134', '00bbe13b']]`
  - `CONDITIONAL_JUMP` [`00bbe138`](#insn-00bbe138) → [`00bbe150`](#insn-00bbe150)
  - `FALL_THROUGH` [`00bbe138`](#insn-00bbe138) → [`00bbe13c`](#insn-00bbe13c)
- ブロック [`00bbe13c`](#insn-00bbe13c) 範囲 `[['00bbe13c', '00bbe14b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe148`](#insn-00bbe148) → [`00bbe150`](#insn-00bbe150)
- ブロック [`00bbe14c`](#insn-00bbe14c) 範囲 `[['00bbe14c', '00bbe14f']]`
  - `FALL_THROUGH` [`00bbe14c`](#insn-00bbe14c) → [`00bbe150`](#insn-00bbe150)
- ブロック [`00bbe150`](#insn-00bbe150) 範囲 `[['00bbe150', '00bbe18f']]`
  - `CONDITIONAL_JUMP` [`00bbe18c`](#insn-00bbe18c) → [`00bbe1a8`](#insn-00bbe1a8)
  - `FALL_THROUGH` [`00bbe18c`](#insn-00bbe18c) → [`00bbe190`](#insn-00bbe190)
- ブロック [`00bbe190`](#insn-00bbe190) 範囲 `[['00bbe190', '00bbe197']]`
  - `CONDITIONAL_JUMP` [`00bbe194`](#insn-00bbe194) → [`00bbe1ac`](#insn-00bbe1ac)
  - `FALL_THROUGH` [`00bbe194`](#insn-00bbe194) → [`00bbe198`](#insn-00bbe198)
- ブロック [`00bbe198`](#insn-00bbe198) 範囲 `[['00bbe198', '00bbe1a7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe1ac`](#insn-00bbe1ac)
- ブロック [`00bbe1a8`](#insn-00bbe1a8) 範囲 `[['00bbe1a8', '00bbe1ab']]`
  - `FALL_THROUGH` [`00bbe1a8`](#insn-00bbe1a8) → [`00bbe1ac`](#insn-00bbe1ac)
- ブロック [`00bbe1ac`](#insn-00bbe1ac) 範囲 `[['00bbe1ac', '00bbe1eb']]`
  - `CONDITIONAL_JUMP` [`00bbe1e8`](#insn-00bbe1e8) → [`00bbe208`](#insn-00bbe208)
  - `FALL_THROUGH` [`00bbe1e8`](#insn-00bbe1e8) → [`00bbe1ec`](#insn-00bbe1ec)
- ブロック [`00bbe1ec`](#insn-00bbe1ec) 範囲 `[['00bbe1ec', '00bbe1f3']]`
  - `CONDITIONAL_JUMP` [`00bbe1f0`](#insn-00bbe1f0) → [`00bbe1f8`](#insn-00bbe1f8)
  - `FALL_THROUGH` [`00bbe1f0`](#insn-00bbe1f0) → [`00bbe1f4`](#insn-00bbe1f4)
- ブロック [`00bbe1f4`](#insn-00bbe1f4) 範囲 `[['00bbe1f4', '00bbe1f7']]`
  - `FALL_THROUGH` [`00bbe1f4`](#insn-00bbe1f4) → [`00bbe1f8`](#insn-00bbe1f8)
- ブロック [`00bbe1f8`](#insn-00bbe1f8) 範囲 `[['00bbe1f8', '00bbe203']]`
  - `CONDITIONAL_JUMP` [`00bbe200`](#insn-00bbe200) → [`00bbe21c`](#insn-00bbe21c)
  - `FALL_THROUGH` [`00bbe200`](#insn-00bbe200) → [`00bbe204`](#insn-00bbe204)
- ブロック [`00bbe204`](#insn-00bbe204) 範囲 `[['00bbe204', '00bbe207']]`
  - `UNCONDITIONAL_JUMP` [`00bbe204`](#insn-00bbe204) → [`00bbe220`](#insn-00bbe220)
- ブロック [`00bbe208`](#insn-00bbe208) 範囲 `[['00bbe208', '00bbe213']]`
  - `CONDITIONAL_JUMP` [`00bbe210`](#insn-00bbe210) → [`00bbe270`](#insn-00bbe270)
  - `FALL_THROUGH` [`00bbe210`](#insn-00bbe210) → [`00bbe214`](#insn-00bbe214)
- ブロック [`00bbe214`](#insn-00bbe214) 範囲 `[['00bbe214', '00bbe21b']]`
  - `CONDITIONAL_JUMP` [`00bbe218`](#insn-00bbe218) → [`00bbe220`](#insn-00bbe220)
  - `FALL_THROUGH` [`00bbe218`](#insn-00bbe218) → [`00bbe21c`](#insn-00bbe21c)
- ブロック [`00bbe21c`](#insn-00bbe21c) 範囲 `[['00bbe21c', '00bbe21f']]`
  - `FALL_THROUGH` [`00bbe21c`](#insn-00bbe21c) → [`00bbe220`](#insn-00bbe220)
- ブロック [`00bbe220`](#insn-00bbe220) 範囲 `[['00bbe220', '00bbe22b']]`
  - `CONDITIONAL_JUMP` [`00bbe228`](#insn-00bbe228) → [`00bbe878`](#insn-00bbe878)
  - `FALL_THROUGH` [`00bbe228`](#insn-00bbe228) → [`00bbe22c`](#insn-00bbe22c)
- ブロック [`00bbe22c`](#insn-00bbe22c) 範囲 `[['00bbe22c', '00bbe233']]`
  - `CONDITIONAL_JUMP` [`00bbe230`](#insn-00bbe230) → [`00bbe878`](#insn-00bbe878)
  - `FALL_THROUGH` [`00bbe230`](#insn-00bbe230) → [`00bbe234`](#insn-00bbe234)
- ブロック [`00bbe234`](#insn-00bbe234) 範囲 `[['00bbe234', '00bbe243']]`
  - `CONDITIONAL_JUMP` [`00bbe240`](#insn-00bbe240) → [`00bbe878`](#insn-00bbe878)
  - `FALL_THROUGH` [`00bbe240`](#insn-00bbe240) → [`00bbe244`](#insn-00bbe244)
- ブロック [`00bbe244`](#insn-00bbe244) 範囲 `[['00bbe244', '00bbe257']]`
  - `CONDITIONAL_JUMP` [`00bbe254`](#insn-00bbe254) → [`00bbe278`](#insn-00bbe278)
  - `FALL_THROUGH` [`00bbe254`](#insn-00bbe254) → [`00bbe258`](#insn-00bbe258)
- ブロック [`00bbe258`](#insn-00bbe258) 範囲 `[['00bbe258', '00bbe25f']]`
  - `CONDITIONAL_JUMP` [`00bbe25c`](#insn-00bbe25c) → [`00bbe27c`](#insn-00bbe27c)
  - `FALL_THROUGH` [`00bbe25c`](#insn-00bbe25c) → [`00bbe260`](#insn-00bbe260)
- ブロック [`00bbe260`](#insn-00bbe260) 範囲 `[['00bbe260', '00bbe26f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe26c`](#insn-00bbe26c) → [`00bbe27c`](#insn-00bbe27c)
- ブロック [`00bbe270`](#insn-00bbe270) 範囲 `[['00bbe270', '00bbe277']]`
  - `UNCONDITIONAL_JUMP` [`00bbe274`](#insn-00bbe274) → [`00bbe878`](#insn-00bbe878)
- ブロック [`00bbe278`](#insn-00bbe278) 範囲 `[['00bbe278', '00bbe27b']]`
  - `FALL_THROUGH` [`00bbe278`](#insn-00bbe278) → [`00bbe27c`](#insn-00bbe27c)
- ブロック [`00bbe27c`](#insn-00bbe27c) 範囲 `[['00bbe27c', '00bbe2b3']]`
  - `CONDITIONAL_JUMP` [`00bbe2b0`](#insn-00bbe2b0) → [`00bbe2cc`](#insn-00bbe2cc)
  - `FALL_THROUGH` [`00bbe2b0`](#insn-00bbe2b0) → [`00bbe2b4`](#insn-00bbe2b4)
- ブロック [`00bbe2b4`](#insn-00bbe2b4) 範囲 `[['00bbe2b4', '00bbe2bb']]`
  - `CONDITIONAL_JUMP` [`00bbe2b8`](#insn-00bbe2b8) → [`00bbe2d0`](#insn-00bbe2d0)
  - `FALL_THROUGH` [`00bbe2b8`](#insn-00bbe2b8) → [`00bbe2bc`](#insn-00bbe2bc)
- ブロック [`00bbe2bc`](#insn-00bbe2bc) 範囲 `[['00bbe2bc', '00bbe2cb']]`
  - `UNCONDITIONAL_JUMP` [`00bbe2c8`](#insn-00bbe2c8) → [`00bbe2d0`](#insn-00bbe2d0)
- ブロック [`00bbe2cc`](#insn-00bbe2cc) 範囲 `[['00bbe2cc', '00bbe2cf']]`
  - `FALL_THROUGH` [`00bbe2cc`](#insn-00bbe2cc) → [`00bbe2d0`](#insn-00bbe2d0)
- ブロック [`00bbe2d0`](#insn-00bbe2d0) 範囲 `[['00bbe2d0', '00bbe30f']]`
  - `CONDITIONAL_JUMP` [`00bbe30c`](#insn-00bbe30c) → [`00bbe328`](#insn-00bbe328)
  - `FALL_THROUGH` [`00bbe30c`](#insn-00bbe30c) → [`00bbe310`](#insn-00bbe310)
- ブロック [`00bbe310`](#insn-00bbe310) 範囲 `[['00bbe310', '00bbe317']]`
  - `CONDITIONAL_JUMP` [`00bbe314`](#insn-00bbe314) → [`00bbe32c`](#insn-00bbe32c)
  - `FALL_THROUGH` [`00bbe314`](#insn-00bbe314) → [`00bbe318`](#insn-00bbe318)
- ブロック [`00bbe318`](#insn-00bbe318) 範囲 `[['00bbe318', '00bbe327']]`
  - `UNCONDITIONAL_JUMP` [`00bbe324`](#insn-00bbe324) → [`00bbe32c`](#insn-00bbe32c)
- ブロック [`00bbe328`](#insn-00bbe328) 範囲 `[['00bbe328', '00bbe32b']]`
  - `FALL_THROUGH` [`00bbe328`](#insn-00bbe328) → [`00bbe32c`](#insn-00bbe32c)
- ブロック [`00bbe32c`](#insn-00bbe32c) 範囲 `[['00bbe32c', '00bbe36b']]`
  - `CONDITIONAL_JUMP` [`00bbe368`](#insn-00bbe368) → [`00bbe384`](#insn-00bbe384)
  - `FALL_THROUGH` [`00bbe368`](#insn-00bbe368) → [`00bbe36c`](#insn-00bbe36c)
- ブロック [`00bbe36c`](#insn-00bbe36c) 範囲 `[['00bbe36c', '00bbe373']]`
  - `CONDITIONAL_JUMP` [`00bbe370`](#insn-00bbe370) → [`00bbe388`](#insn-00bbe388)
  - `FALL_THROUGH` [`00bbe370`](#insn-00bbe370) → [`00bbe374`](#insn-00bbe374)
- ブロック [`00bbe374`](#insn-00bbe374) 範囲 `[['00bbe374', '00bbe383']]`
  - `UNCONDITIONAL_JUMP` [`00bbe380`](#insn-00bbe380) → [`00bbe388`](#insn-00bbe388)
- ブロック [`00bbe384`](#insn-00bbe384) 範囲 `[['00bbe384', '00bbe387']]`
  - `FALL_THROUGH` [`00bbe384`](#insn-00bbe384) → [`00bbe388`](#insn-00bbe388)
- ブロック [`00bbe388`](#insn-00bbe388) 範囲 `[['00bbe388', '00bbe3c7']]`
  - `CONDITIONAL_JUMP` [`00bbe3c4`](#insn-00bbe3c4) → [`00bbe3e0`](#insn-00bbe3e0)
  - `FALL_THROUGH` [`00bbe3c4`](#insn-00bbe3c4) → [`00bbe3c8`](#insn-00bbe3c8)
- ブロック [`00bbe3c8`](#insn-00bbe3c8) 範囲 `[['00bbe3c8', '00bbe3cf']]`
  - `CONDITIONAL_JUMP` [`00bbe3cc`](#insn-00bbe3cc) → [`00bbe3e4`](#insn-00bbe3e4)
  - `FALL_THROUGH` [`00bbe3cc`](#insn-00bbe3cc) → [`00bbe3d0`](#insn-00bbe3d0)
- ブロック [`00bbe3d0`](#insn-00bbe3d0) 範囲 `[['00bbe3d0', '00bbe3df']]`
  - `UNCONDITIONAL_JUMP` [`00bbe3dc`](#insn-00bbe3dc) → [`00bbe3e4`](#insn-00bbe3e4)
- ブロック [`00bbe3e0`](#insn-00bbe3e0) 範囲 `[['00bbe3e0', '00bbe3e3']]`
  - `FALL_THROUGH` [`00bbe3e0`](#insn-00bbe3e0) → [`00bbe3e4`](#insn-00bbe3e4)
- ブロック [`00bbe3e4`](#insn-00bbe3e4) 範囲 `[['00bbe3e4', '00bbe423']]`
  - `CONDITIONAL_JUMP` [`00bbe420`](#insn-00bbe420) → [`00bbe43c`](#insn-00bbe43c)
  - `FALL_THROUGH` [`00bbe420`](#insn-00bbe420) → [`00bbe424`](#insn-00bbe424)
- ブロック [`00bbe424`](#insn-00bbe424) 範囲 `[['00bbe424', '00bbe42b']]`
  - `CONDITIONAL_JUMP` [`00bbe428`](#insn-00bbe428) → [`00bbe440`](#insn-00bbe440)
  - `FALL_THROUGH` [`00bbe428`](#insn-00bbe428) → [`00bbe42c`](#insn-00bbe42c)
- ブロック [`00bbe42c`](#insn-00bbe42c) 範囲 `[['00bbe42c', '00bbe43b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe438`](#insn-00bbe438) → [`00bbe440`](#insn-00bbe440)
- ブロック [`00bbe43c`](#insn-00bbe43c) 範囲 `[['00bbe43c', '00bbe43f']]`
  - `FALL_THROUGH` [`00bbe43c`](#insn-00bbe43c) → [`00bbe440`](#insn-00bbe440)
- ブロック [`00bbe440`](#insn-00bbe440) 範囲 `[['00bbe440', '00bbe47f']]`
  - `CONDITIONAL_JUMP` [`00bbe47c`](#insn-00bbe47c) → [`00bbe498`](#insn-00bbe498)
  - `FALL_THROUGH` [`00bbe47c`](#insn-00bbe47c) → [`00bbe480`](#insn-00bbe480)
- ブロック [`00bbe480`](#insn-00bbe480) 範囲 `[['00bbe480', '00bbe487']]`
  - `CONDITIONAL_JUMP` [`00bbe484`](#insn-00bbe484) → [`00bbe49c`](#insn-00bbe49c)
  - `FALL_THROUGH` [`00bbe484`](#insn-00bbe484) → [`00bbe488`](#insn-00bbe488)
- ブロック [`00bbe488`](#insn-00bbe488) 範囲 `[['00bbe488', '00bbe497']]`
  - `UNCONDITIONAL_JUMP` [`00bbe494`](#insn-00bbe494) → [`00bbe49c`](#insn-00bbe49c)
- ブロック [`00bbe498`](#insn-00bbe498) 範囲 `[['00bbe498', '00bbe49b']]`
  - `FALL_THROUGH` [`00bbe498`](#insn-00bbe498) → [`00bbe49c`](#insn-00bbe49c)
- ブロック [`00bbe49c`](#insn-00bbe49c) 範囲 `[['00bbe49c', '00bbe4db']]`
  - `CONDITIONAL_JUMP` [`00bbe4d8`](#insn-00bbe4d8) → [`00bbe4f4`](#insn-00bbe4f4)
  - `FALL_THROUGH` [`00bbe4d8`](#insn-00bbe4d8) → [`00bbe4dc`](#insn-00bbe4dc)
- ブロック [`00bbe4dc`](#insn-00bbe4dc) 範囲 `[['00bbe4dc', '00bbe4e3']]`
  - `CONDITIONAL_JUMP` [`00bbe4e0`](#insn-00bbe4e0) → [`00bbe4f8`](#insn-00bbe4f8)
  - `FALL_THROUGH` [`00bbe4e0`](#insn-00bbe4e0) → [`00bbe4e4`](#insn-00bbe4e4)
- ブロック [`00bbe4e4`](#insn-00bbe4e4) 範囲 `[['00bbe4e4', '00bbe4f3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe4f0`](#insn-00bbe4f0) → [`00bbe4f8`](#insn-00bbe4f8)
- ブロック [`00bbe4f4`](#insn-00bbe4f4) 範囲 `[['00bbe4f4', '00bbe4f7']]`
  - `FALL_THROUGH` [`00bbe4f4`](#insn-00bbe4f4) → [`00bbe4f8`](#insn-00bbe4f8)
- ブロック [`00bbe4f8`](#insn-00bbe4f8) 範囲 `[['00bbe4f8', '00bbe537']]`
  - `CONDITIONAL_JUMP` [`00bbe534`](#insn-00bbe534) → [`00bbe550`](#insn-00bbe550)
  - `FALL_THROUGH` [`00bbe534`](#insn-00bbe534) → [`00bbe538`](#insn-00bbe538)
- ブロック [`00bbe538`](#insn-00bbe538) 範囲 `[['00bbe538', '00bbe53f']]`
  - `CONDITIONAL_JUMP` [`00bbe53c`](#insn-00bbe53c) → [`00bbe554`](#insn-00bbe554)
  - `FALL_THROUGH` [`00bbe53c`](#insn-00bbe53c) → [`00bbe540`](#insn-00bbe540)
- ブロック [`00bbe540`](#insn-00bbe540) 範囲 `[['00bbe540', '00bbe54f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe54c`](#insn-00bbe54c) → [`00bbe554`](#insn-00bbe554)
- ブロック [`00bbe550`](#insn-00bbe550) 範囲 `[['00bbe550', '00bbe553']]`
  - `FALL_THROUGH` [`00bbe550`](#insn-00bbe550) → [`00bbe554`](#insn-00bbe554)
- ブロック [`00bbe554`](#insn-00bbe554) 範囲 `[['00bbe554', '00bbe593']]`
  - `CONDITIONAL_JUMP` [`00bbe590`](#insn-00bbe590) → [`00bbe69c`](#insn-00bbe69c)
  - `FALL_THROUGH` [`00bbe590`](#insn-00bbe590) → [`00bbe594`](#insn-00bbe594)
- ブロック [`00bbe594`](#insn-00bbe594) 範囲 `[['00bbe594', '00bbe59b']]`
  - `CONDITIONAL_JUMP` [`00bbe598`](#insn-00bbe598) → [`00bbe69c`](#insn-00bbe69c)
  - `FALL_THROUGH` [`00bbe598`](#insn-00bbe598) → [`00bbe59c`](#insn-00bbe59c)
- ブロック [`00bbe59c`](#insn-00bbe59c) 範囲 `[['00bbe59c', '00bbe5c7']]`
  - `CONDITIONAL_JUMP` [`00bbe5c4`](#insn-00bbe5c4) → [`00bbe5dc`](#insn-00bbe5dc)
  - `FALL_THROUGH` [`00bbe5c4`](#insn-00bbe5c4) → [`00bbe5c8`](#insn-00bbe5c8)
- ブロック [`00bbe5c8`](#insn-00bbe5c8) 範囲 `[['00bbe5c8', '00bbe5db']]`
  - `UNCONDITIONAL_JUMP` [`00bbe5d8`](#insn-00bbe5d8) → [`00bbe620`](#insn-00bbe620)
- ブロック [`00bbe5dc`](#insn-00bbe5dc) 範囲 `[['00bbe5dc', '00bbe5df']]`
  - `CONDITIONAL_JUMP` [`00bbe5dc`](#insn-00bbe5dc) → [`00bbe620`](#insn-00bbe620)
  - `FALL_THROUGH` [`00bbe5dc`](#insn-00bbe5dc) → [`00bbe5e0`](#insn-00bbe5e0)
- ブロック [`00bbe5e0`](#insn-00bbe5e0) 範囲 `[['00bbe5e0', '00bbe5ef']]`
  - `CONDITIONAL_JUMP` [`00bbe5ec`](#insn-00bbe5ec) → [`00bbe61c`](#insn-00bbe61c)
  - `FALL_THROUGH` [`00bbe5ec`](#insn-00bbe5ec) → [`00bbe5f0`](#insn-00bbe5f0)
- ブロック [`00bbe5f0`](#insn-00bbe5f0) 範囲 `[['00bbe5f0', '00bbe5fb']]`
  - `CONDITIONAL_JUMP` [`00bbe5f8`](#insn-00bbe5f8) → [`00bbe610`](#insn-00bbe610)
  - `FALL_THROUGH` [`00bbe5f8`](#insn-00bbe5f8) → [`00bbe5fc`](#insn-00bbe5fc)
- ブロック [`00bbe5fc`](#insn-00bbe5fc) 範囲 `[['00bbe5fc', '00bbe607']]`
  - `CONDITIONAL_JUMP` [`00bbe604`](#insn-00bbe604) → [`00bbe61c`](#insn-00bbe61c)
  - `FALL_THROUGH` [`00bbe604`](#insn-00bbe604) → [`00bbe608`](#insn-00bbe608)
- ブロック [`00bbe608`](#insn-00bbe608) 範囲 `[['00bbe608', '00bbe60f']]`
  - `CONDITIONAL_JUMP` [`00bbe60c`](#insn-00bbe60c) → [`00bbe5fc`](#insn-00bbe5fc)
  - `FALL_THROUGH` [`00bbe60c`](#insn-00bbe60c) → [`00bbe610`](#insn-00bbe610)
- ブロック [`00bbe610`](#insn-00bbe610) 範囲 `[['00bbe610', '00bbe61b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe618`](#insn-00bbe618) → [`00bbe5fc`](#insn-00bbe5fc)
- ブロック [`00bbe61c`](#insn-00bbe61c) 範囲 `[['00bbe61c', '00bbe61f']]`
  - `FALL_THROUGH` [`00bbe61c`](#insn-00bbe61c) → [`00bbe620`](#insn-00bbe620)
- ブロック [`00bbe620`](#insn-00bbe620) 範囲 `[['00bbe620', '00bbe623']]`
  - `CONDITIONAL_JUMP` [`00bbe620`](#insn-00bbe620) → [`00bbe69c`](#insn-00bbe69c)
  - `FALL_THROUGH` [`00bbe620`](#insn-00bbe620) → [`00bbe624`](#insn-00bbe624)
- ブロック [`00bbe624`](#insn-00bbe624) 範囲 `[['00bbe624', '00bbe62b']]`
  - `FALL_THROUGH` [`00bbe628`](#insn-00bbe628) → [`00bbe62c`](#insn-00bbe62c)
- ブロック [`00bbe62c`](#insn-00bbe62c) 範囲 `[['00bbe62c', '00bbe63f']]`
  - `CONDITIONAL_JUMP` [`00bbe63c`](#insn-00bbe63c) → [`00bbe658`](#insn-00bbe658)
  - `FALL_THROUGH` [`00bbe63c`](#insn-00bbe63c) → [`00bbe640`](#insn-00bbe640)
- ブロック [`00bbe640`](#insn-00bbe640) 範囲 `[['00bbe640', '00bbe647']]`
  - `CONDITIONAL_JUMP` [`00bbe644`](#insn-00bbe644) → [`00bbe65c`](#insn-00bbe65c)
  - `FALL_THROUGH` [`00bbe644`](#insn-00bbe644) → [`00bbe648`](#insn-00bbe648)
- ブロック [`00bbe648`](#insn-00bbe648) 範囲 `[['00bbe648', '00bbe657']]`
  - `UNCONDITIONAL_JUMP` [`00bbe654`](#insn-00bbe654) → [`00bbe65c`](#insn-00bbe65c)
- ブロック [`00bbe658`](#insn-00bbe658) 範囲 `[['00bbe658', '00bbe65b']]`
  - `FALL_THROUGH` [`00bbe658`](#insn-00bbe658) → [`00bbe65c`](#insn-00bbe65c)
- ブロック [`00bbe65c`](#insn-00bbe65c) 範囲 `[['00bbe65c', '00bbe69b']]`
  - `CONDITIONAL_JUMP` [`00bbe698`](#insn-00bbe698) → [`00bbe62c`](#insn-00bbe62c)
  - `FALL_THROUGH` [`00bbe698`](#insn-00bbe698) → [`00bbe69c`](#insn-00bbe69c)
- ブロック [`00bbe69c`](#insn-00bbe69c) 範囲 `[['00bbe69c', '00bbe6af']]`
  - `CONDITIONAL_JUMP` [`00bbe6ac`](#insn-00bbe6ac) → [`00bbe6c8`](#insn-00bbe6c8)
  - `FALL_THROUGH` [`00bbe6ac`](#insn-00bbe6ac) → [`00bbe6b0`](#insn-00bbe6b0)
- ブロック [`00bbe6b0`](#insn-00bbe6b0) 範囲 `[['00bbe6b0', '00bbe6b7']]`
  - `CONDITIONAL_JUMP` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6cc`](#insn-00bbe6cc)
  - `FALL_THROUGH` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6b8`](#insn-00bbe6b8)
- ブロック [`00bbe6b8`](#insn-00bbe6b8) 範囲 `[['00bbe6b8', '00bbe6c7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe6cc`](#insn-00bbe6cc)
- ブロック [`00bbe6c8`](#insn-00bbe6c8) 範囲 `[['00bbe6c8', '00bbe6cb']]`
  - `FALL_THROUGH` [`00bbe6c8`](#insn-00bbe6c8) → [`00bbe6cc`](#insn-00bbe6cc)
- ブロック [`00bbe6cc`](#insn-00bbe6cc) 範囲 `[['00bbe6cc', '00bbe70b']]`
  - `CONDITIONAL_JUMP` [`00bbe708`](#insn-00bbe708) → [`00bbe814`](#insn-00bbe814)
  - `FALL_THROUGH` [`00bbe708`](#insn-00bbe708) → [`00bbe70c`](#insn-00bbe70c)
- ブロック [`00bbe70c`](#insn-00bbe70c) 範囲 `[['00bbe70c', '00bbe713']]`
  - `CONDITIONAL_JUMP` [`00bbe710`](#insn-00bbe710) → [`00bbe814`](#insn-00bbe814)
  - `FALL_THROUGH` [`00bbe710`](#insn-00bbe710) → [`00bbe714`](#insn-00bbe714)
- ブロック [`00bbe714`](#insn-00bbe714) 範囲 `[['00bbe714', '00bbe73f']]`
  - `CONDITIONAL_JUMP` [`00bbe73c`](#insn-00bbe73c) → [`00bbe754`](#insn-00bbe754)
  - `FALL_THROUGH` [`00bbe73c`](#insn-00bbe73c) → [`00bbe740`](#insn-00bbe740)
- ブロック [`00bbe740`](#insn-00bbe740) 範囲 `[['00bbe740', '00bbe753']]`
  - `UNCONDITIONAL_JUMP` [`00bbe750`](#insn-00bbe750) → [`00bbe798`](#insn-00bbe798)
- ブロック [`00bbe754`](#insn-00bbe754) 範囲 `[['00bbe754', '00bbe757']]`
  - `CONDITIONAL_JUMP` [`00bbe754`](#insn-00bbe754) → [`00bbe798`](#insn-00bbe798)
  - `FALL_THROUGH` [`00bbe754`](#insn-00bbe754) → [`00bbe758`](#insn-00bbe758)
- ブロック [`00bbe758`](#insn-00bbe758) 範囲 `[['00bbe758', '00bbe767']]`
  - `CONDITIONAL_JUMP` [`00bbe764`](#insn-00bbe764) → [`00bbe794`](#insn-00bbe794)
  - `FALL_THROUGH` [`00bbe764`](#insn-00bbe764) → [`00bbe768`](#insn-00bbe768)
- ブロック [`00bbe768`](#insn-00bbe768) 範囲 `[['00bbe768', '00bbe773']]`
  - `CONDITIONAL_JUMP` [`00bbe770`](#insn-00bbe770) → [`00bbe788`](#insn-00bbe788)
  - `FALL_THROUGH` [`00bbe770`](#insn-00bbe770) → [`00bbe774`](#insn-00bbe774)
- ブロック [`00bbe774`](#insn-00bbe774) 範囲 `[['00bbe774', '00bbe77f']]`
  - `CONDITIONAL_JUMP` [`00bbe77c`](#insn-00bbe77c) → [`00bbe794`](#insn-00bbe794)
  - `FALL_THROUGH` [`00bbe77c`](#insn-00bbe77c) → [`00bbe780`](#insn-00bbe780)
- ブロック [`00bbe780`](#insn-00bbe780) 範囲 `[['00bbe780', '00bbe787']]`
  - `CONDITIONAL_JUMP` [`00bbe784`](#insn-00bbe784) → [`00bbe774`](#insn-00bbe774)
  - `FALL_THROUGH` [`00bbe784`](#insn-00bbe784) → [`00bbe788`](#insn-00bbe788)
- ブロック [`00bbe788`](#insn-00bbe788) 範囲 `[['00bbe788', '00bbe793']]`
  - `UNCONDITIONAL_JUMP` [`00bbe790`](#insn-00bbe790) → [`00bbe774`](#insn-00bbe774)
- ブロック [`00bbe794`](#insn-00bbe794) 範囲 `[['00bbe794', '00bbe797']]`
  - `FALL_THROUGH` [`00bbe794`](#insn-00bbe794) → [`00bbe798`](#insn-00bbe798)
- ブロック [`00bbe798`](#insn-00bbe798) 範囲 `[['00bbe798', '00bbe79b']]`
  - `CONDITIONAL_JUMP` [`00bbe798`](#insn-00bbe798) → [`00bbe814`](#insn-00bbe814)
  - `FALL_THROUGH` [`00bbe798`](#insn-00bbe798) → [`00bbe79c`](#insn-00bbe79c)
- ブロック [`00bbe79c`](#insn-00bbe79c) 範囲 `[['00bbe79c', '00bbe7a3']]`
  - `FALL_THROUGH` [`00bbe7a0`](#insn-00bbe7a0) → [`00bbe7a4`](#insn-00bbe7a4)
- ブロック [`00bbe7a4`](#insn-00bbe7a4) 範囲 `[['00bbe7a4', '00bbe7b7']]`
  - `CONDITIONAL_JUMP` [`00bbe7b4`](#insn-00bbe7b4) → [`00bbe7d0`](#insn-00bbe7d0)
  - `FALL_THROUGH` [`00bbe7b4`](#insn-00bbe7b4) → [`00bbe7b8`](#insn-00bbe7b8)
- ブロック [`00bbe7b8`](#insn-00bbe7b8) 範囲 `[['00bbe7b8', '00bbe7bf']]`
  - `CONDITIONAL_JUMP` [`00bbe7bc`](#insn-00bbe7bc) → [`00bbe7d4`](#insn-00bbe7d4)
  - `FALL_THROUGH` [`00bbe7bc`](#insn-00bbe7bc) → [`00bbe7c0`](#insn-00bbe7c0)
- ブロック [`00bbe7c0`](#insn-00bbe7c0) 範囲 `[['00bbe7c0', '00bbe7cf']]`
  - `UNCONDITIONAL_JUMP` [`00bbe7cc`](#insn-00bbe7cc) → [`00bbe7d4`](#insn-00bbe7d4)
- ブロック [`00bbe7d0`](#insn-00bbe7d0) 範囲 `[['00bbe7d0', '00bbe7d3']]`
  - `FALL_THROUGH` [`00bbe7d0`](#insn-00bbe7d0) → [`00bbe7d4`](#insn-00bbe7d4)
- ブロック [`00bbe7d4`](#insn-00bbe7d4) 範囲 `[['00bbe7d4', '00bbe813']]`
  - `CONDITIONAL_JUMP` [`00bbe810`](#insn-00bbe810) → [`00bbe7a4`](#insn-00bbe7a4)
  - `FALL_THROUGH` [`00bbe810`](#insn-00bbe810) → [`00bbe814`](#insn-00bbe814)
- ブロック [`00bbe814`](#insn-00bbe814) 範囲 `[['00bbe814', '00bbe827']]`
  - `CONDITIONAL_JUMP` [`00bbe824`](#insn-00bbe824) → [`00bbe840`](#insn-00bbe840)
  - `FALL_THROUGH` [`00bbe824`](#insn-00bbe824) → [`00bbe828`](#insn-00bbe828)
- ブロック [`00bbe828`](#insn-00bbe828) 範囲 `[['00bbe828', '00bbe82f']]`
  - `CONDITIONAL_JUMP` [`00bbe82c`](#insn-00bbe82c) → [`00bbe844`](#insn-00bbe844)
  - `FALL_THROUGH` [`00bbe82c`](#insn-00bbe82c) → [`00bbe830`](#insn-00bbe830)
- ブロック [`00bbe830`](#insn-00bbe830) 範囲 `[['00bbe830', '00bbe83f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe83c`](#insn-00bbe83c) → [`00bbe844`](#insn-00bbe844)
- ブロック [`00bbe840`](#insn-00bbe840) 範囲 `[['00bbe840', '00bbe843']]`
  - `FALL_THROUGH` [`00bbe840`](#insn-00bbe840) → [`00bbe844`](#insn-00bbe844)
- ブロック [`00bbe844`](#insn-00bbe844) 範囲 `[['00bbe844', '00bbe867']]`
  - `FALL_THROUGH` [`00bbe864`](#insn-00bbe864) → [`00bbe868`](#insn-00bbe868)
- ブロック [`00bbe868`](#insn-00bbe868) 範囲 `[['00bbe868', '00bbe877']]`
  - `FALL_THROUGH` [`00bbe874`](#insn-00bbe874) → [`00bbe878`](#insn-00bbe878)
- ブロック [`00bbe878`](#insn-00bbe878) 範囲 `[['00bbe878', '00bbe88b']]`
  - `CONDITIONAL_JUMP` [`00bbe888`](#insn-00bbe888) → [`00bbe894`](#insn-00bbe894)
  - `FALL_THROUGH` [`00bbe888`](#insn-00bbe888) → [`00bbe88c`](#insn-00bbe88c)
- ブロック [`00bbe88c`](#insn-00bbe88c) 範囲 `[['00bbe88c', '00bbe893']]`
  - `FALL_THROUGH` [`00bbe890`](#insn-00bbe890) → [`00bbe894`](#insn-00bbe894)
- ブロック [`00bbe894`](#insn-00bbe894) 範囲 `[['00bbe894', '00bbe89b']]`
  - `CONDITIONAL_JUMP` [`00bbe898`](#insn-00bbe898) → [`00bbe8a4`](#insn-00bbe8a4)
  - `FALL_THROUGH` [`00bbe898`](#insn-00bbe898) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbe89c`](#insn-00bbe89c) 範囲 `[['00bbe89c', '00bbe8a3']]`
  - `FALL_THROUGH` [`00bbe8a0`](#insn-00bbe8a0) → [`00bbe8a4`](#insn-00bbe8a4)
- ブロック [`00bbe8a4`](#insn-00bbe8a4) 範囲 `[['00bbe8a4', '00bbe8c3']]`
  - `CONDITIONAL_JUMP` [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8e4`](#insn-00bbe8e4)
  - `FALL_THROUGH` [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8c4`](#insn-00bbe8c4)
- ブロック [`00bbe8c4`](#insn-00bbe8c4) 範囲 `[['00bbe8c4', '00bbe8e3']]`
- ブロック [`00bbe8e4`](#insn-00bbe8e4) 範囲 `[['00bbe8e4', '00bbe8e7']]`

## 命令位置別の参照

- [`00bbdae8`](#insn-00bbdae8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaec`](#insn-00bbdaec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaf0`](#insn-00bbdaf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaf4`](#insn-00bbdaf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaf8`](#insn-00bbdaf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdafc`](#insn-00bbdafc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb20`](#insn-00bbdb20) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb24`](#insn-00bbdb24) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb28`](#insn-00bbdb28) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb2c`](#insn-00bbdb2c) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb30`](#insn-00bbdb30) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb34`](#insn-00bbdb34) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb38`](#insn-00bbdb38) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb3c`](#insn-00bbdb3c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb40`](#insn-00bbdb40) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb44`](#insn-00bbdb44) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb48`](#insn-00bbdb48) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb4c`](#insn-00bbdb4c) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb50`](#insn-00bbdb50) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb54`](#insn-00bbdb54) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb58`](#insn-00bbdb58) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb5c`](#insn-00bbdb5c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb60`](#insn-00bbdb60) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb64`](#insn-00bbdb64) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb68`](#insn-00bbdb68) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb6c`](#insn-00bbdb6c) → `Stack[-0x230]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb70`](#insn-00bbdb70) → `Stack[-0x250]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb74`](#insn-00bbdb74) → `Stack[-0x270]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb78`](#insn-00bbdb78) → `Stack[-0x290]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb7c`](#insn-00bbdb7c) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb80`](#insn-00bbdb80) → `Stack[-0x2d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb84`](#insn-00bbdb84) → `Stack[-0x2f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb88`](#insn-00bbdb88) → `Stack[-0x300]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb8c`](#insn-00bbdb8c) → `Stack[-0x308]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbac`](#insn-00bbdbac) → [`00bbdbc4`](#insn-00bbdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbb4`](#insn-00bbdbb4) → [`00bbdbc4`](#insn-00bbdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbd8`](#insn-00bbdbd8) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdbdc`](#insn-00bbdbdc) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbec`](#insn-00bbdbec) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc00`](#insn-00bbdc00) → [`00bbdc1c`](#insn-00bbdc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc08`](#insn-00bbdc08) → [`00bbdc20`](#insn-00bbdc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc18`](#insn-00bbdc18) → [`00bbdc20`](#insn-00bbdc20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc30`](#insn-00bbdc30) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdc38`](#insn-00bbdc38) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc48`](#insn-00bbdc48) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc60`](#insn-00bbdc60) → [`00bbde08`](#insn-00bbde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc68`](#insn-00bbdc68) → [`00bbde08`](#insn-00bbde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc78`](#insn-00bbdc78) → [`00bbde08`](#insn-00bbde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc80`](#insn-00bbdc80) → [`00bbde08`](#insn-00bbde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc88`](#insn-00bbdc88) → `Stack[-0x340]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc98`](#insn-00bbdc98) → [`00bbdcac`](#insn-00bbdcac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdca8`](#insn-00bbdca8) → [`00bbddfc`](#insn-00bbddfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdce0`](#insn-00bbdce0) → [`00bbdd24`](#insn-00bbdd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdce8`](#insn-00bbdce8) → [`00bbdcf8`](#insn-00bbdcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd08`](#insn-00bbdd08) → [`00bbdd30`](#insn-00bbdd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd10`](#insn-00bbdd10) → [`00bbdd30`](#insn-00bbdd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd20`](#insn-00bbdd20) → [`00bbdd34`](#insn-00bbdd34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd28`](#insn-00bbdd28) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdd2c`](#insn-00bbdd2c) → [`00bbdd34`](#insn-00bbdd34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd44`](#insn-00bbdd44) → [`00c5b690`](../00c5b/00c5b690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b690` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd54`](#insn-00bbdd54) → [`0046d5e8`](../0046d/0046d5e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d5e8` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd60`](#insn-00bbdd60) → [`00bbddcc`](#insn-00bbddcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd68`](#insn-00bbdd68) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd6c`](#insn-00bbdd6c) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd70`](#insn-00bbdd70) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd74`](#insn-00bbdd74) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd78`](#insn-00bbdd78) → `Stack[-0x318]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd7c`](#insn-00bbdd7c) → `Stack[-0x320]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd98`](#insn-00bbdd98) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdda0`](#insn-00bbdda0) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdda4`](#insn-00bbdda4) → [`00bbddb4`](#insn-00bbddb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdda8`](#insn-00bbdda8) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddb0`](#insn-00bbddb0) → [`00bbddb8`](#insn-00bbddb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddb8`](#insn-00bbddb8) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddbc`](#insn-00bbddbc) → [`00c5b6b0`](../00c5b/00c5b6b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbddc0`](#insn-00bbddc0) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddc8`](#insn-00bbddc8) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddd4`](#insn-00bbddd4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde4`](#insn-00bbdde4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde8`](#insn-00bbdde8) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddec`](#insn-00bbddec) → [`00bbdc9c`](#insn-00bbdc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddf0`](#insn-00bbddf0) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddf4`](#insn-00bbddf4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbddf8`](#insn-00bbddf8) → [`00bbdc9c`](#insn-00bbdc9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddfc`](#insn-00bbddfc) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde14`](#insn-00bbde14) → [`00bbdedc`](#insn-00bbdedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde1c`](#insn-00bbde1c) → [`00bbdedc`](#insn-00bbdedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde2c`](#insn-00bbde2c) → [`00bbdedc`](#insn-00bbdedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde30`](#insn-00bbde30) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde34`](#insn-00bbde34) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde44`](#insn-00bbde44) → [`00bbde8c`](#insn-00bbde8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde48`](#insn-00bbde48) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde50`](#insn-00bbde50) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bbde68`](#insn-00bbde68) → [`00bbde78`](#insn-00bbde78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde74`](#insn-00bbde74) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde78`](#insn-00bbde78) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde7c`](#insn-00bbde7c) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde80`](#insn-00bbde80) → [`00bbde8c`](#insn-00bbde8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde88`](#insn-00bbde88) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeb4`](#insn-00bbdeb4) → `Stack[-0x328]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdec4`](#insn-00bbdec4) → `Stack[-0x330]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbded0`](#insn-00bbded0) → [`00c5d640`](../00c5d/00c5d640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d640` · 推定シンボル `None` · 推定型 `None`
- [`00bbdee8`](#insn-00bbdee8) → [`00bbdf04`](#insn-00bbdf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdef0`](#insn-00bbdef0) → [`00bbdf08`](#insn-00bbdf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf00`](#insn-00bbdf00) → [`00bbdf08`](#insn-00bbdf08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf18`](#insn-00bbdf18) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdf20`](#insn-00bbdf20) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf30`](#insn-00bbdf30) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf44`](#insn-00bbdf44) → [`00bbdf60`](#insn-00bbdf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf4c`](#insn-00bbdf4c) → [`00bbdf64`](#insn-00bbdf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf64`](#insn-00bbdf64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf74`](#insn-00bbdf74) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdf7c`](#insn-00bbdf7c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf8c`](#insn-00bbdf8c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfa4`](#insn-00bbdfa4) → [`00bbdfc0`](#insn-00bbdfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfac`](#insn-00bbdfac) → [`00bbdfc4`](#insn-00bbdfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfbc`](#insn-00bbdfbc) → [`00bbdfc4`](#insn-00bbdfc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfd0`](#insn-00bbdfd0) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdfd4`](#insn-00bbdfd4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfe4`](#insn-00bbdfe4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbdff8`](#insn-00bbdff8) → [`00bbe014`](#insn-00bbe014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe000`](#insn-00bbe000) → [`00bbe018`](#insn-00bbe018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe010`](#insn-00bbe010) → [`00bbe018`](#insn-00bbe018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe028`](#insn-00bbe028) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe030`](#insn-00bbe030) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe040`](#insn-00bbe040) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe054`](#insn-00bbe054) → [`00bbe090`](#insn-00bbe090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe05c`](#insn-00bbe05c) → [`00bbe06c`](#insn-00bbe06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe070`](#insn-00bbe070) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe074`](#insn-00bbe074) → [`00bbe09c`](#insn-00bbe09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe07c`](#insn-00bbe07c) → [`00bbe0a0`](#insn-00bbe0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe08c`](#insn-00bbe08c) → [`00bbe0a0`](#insn-00bbe0a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe094`](#insn-00bbe094) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe098`](#insn-00bbe098) → [`00bbe0a0`](#insn-00bbe0a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0ac`](#insn-00bbe0ac) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe0b0`](#insn-00bbe0b0) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0c0`](#insn-00bbe0c0) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0d4`](#insn-00bbe0d4) → [`00bbe0f0`](#insn-00bbe0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0dc`](#insn-00bbe0dc) → [`00bbe0f4`](#insn-00bbe0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0ec`](#insn-00bbe0ec) → [`00bbe0f4`](#insn-00bbe0f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe104`](#insn-00bbe104) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe10c`](#insn-00bbe10c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe11c`](#insn-00bbe11c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe130`](#insn-00bbe130) → [`00bbe14c`](#insn-00bbe14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe138`](#insn-00bbe138) → [`00bbe150`](#insn-00bbe150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe148`](#insn-00bbe148) → [`00bbe150`](#insn-00bbe150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe160`](#insn-00bbe160) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe168`](#insn-00bbe168) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe178`](#insn-00bbe178) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe18c`](#insn-00bbe18c) → [`00bbe1a8`](#insn-00bbe1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe194`](#insn-00bbe194) → [`00bbe1ac`](#insn-00bbe1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe1ac`](#insn-00bbe1ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1bc`](#insn-00bbe1bc) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe1c4`](#insn-00bbe1c4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1d4`](#insn-00bbe1d4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1e8`](#insn-00bbe1e8) → [`00bbe208`](#insn-00bbe208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1f0`](#insn-00bbe1f0) → [`00bbe1f8`](#insn-00bbe1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1f8`](#insn-00bbe1f8) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe200`](#insn-00bbe200) → [`00bbe21c`](#insn-00bbe21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe204`](#insn-00bbe204) → [`00bbe220`](#insn-00bbe220) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe20c`](#insn-00bbe20c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe210`](#insn-00bbe210) → [`00bbe270`](#insn-00bbe270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe218`](#insn-00bbe218) → [`00bbe220`](#insn-00bbe220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe224`](#insn-00bbe224) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe228`](#insn-00bbe228) → [`00bbe878`](#insn-00bbe878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe230`](#insn-00bbe230) → [`00bbe878`](#insn-00bbe878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe240`](#insn-00bbe240) → [`00bbe878`](#insn-00bbe878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe254`](#insn-00bbe254) → [`00bbe278`](#insn-00bbe278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe25c`](#insn-00bbe25c) → [`00bbe27c`](#insn-00bbe27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe26c`](#insn-00bbe26c) → [`00bbe27c`](#insn-00bbe27c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe270`](#insn-00bbe270) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe274`](#insn-00bbe274) → [`00bbe878`](#insn-00bbe878) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe288`](#insn-00bbe288) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe28c`](#insn-00bbe28c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe29c`](#insn-00bbe29c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2b0`](#insn-00bbe2b0) → [`00bbe2cc`](#insn-00bbe2cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2b8`](#insn-00bbe2b8) → [`00bbe2d0`](#insn-00bbe2d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2c8`](#insn-00bbe2c8) → [`00bbe2d0`](#insn-00bbe2d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2e0`](#insn-00bbe2e0) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe2e8`](#insn-00bbe2e8) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2f8`](#insn-00bbe2f8) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe30c`](#insn-00bbe30c) → [`00bbe328`](#insn-00bbe328) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe314`](#insn-00bbe314) → [`00bbe32c`](#insn-00bbe32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe324`](#insn-00bbe324) → [`00bbe32c`](#insn-00bbe32c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe33c`](#insn-00bbe33c) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe344`](#insn-00bbe344) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe354`](#insn-00bbe354) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe368`](#insn-00bbe368) → [`00bbe384`](#insn-00bbe384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe370`](#insn-00bbe370) → [`00bbe388`](#insn-00bbe388) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe380`](#insn-00bbe380) → [`00bbe388`](#insn-00bbe388) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe398`](#insn-00bbe398) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe3a0`](#insn-00bbe3a0) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3b0`](#insn-00bbe3b0) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3c4`](#insn-00bbe3c4) → [`00bbe3e0`](#insn-00bbe3e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3cc`](#insn-00bbe3cc) → [`00bbe3e4`](#insn-00bbe3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3dc`](#insn-00bbe3dc) → [`00bbe3e4`](#insn-00bbe3e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3f4`](#insn-00bbe3f4) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe3fc`](#insn-00bbe3fc) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe40c`](#insn-00bbe40c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe420`](#insn-00bbe420) → [`00bbe43c`](#insn-00bbe43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe428`](#insn-00bbe428) → [`00bbe440`](#insn-00bbe440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe438`](#insn-00bbe438) → [`00bbe440`](#insn-00bbe440) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe450`](#insn-00bbe450) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe458`](#insn-00bbe458) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe468`](#insn-00bbe468) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe47c`](#insn-00bbe47c) → [`00bbe498`](#insn-00bbe498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe484`](#insn-00bbe484) → [`00bbe49c`](#insn-00bbe49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe494`](#insn-00bbe494) → [`00bbe49c`](#insn-00bbe49c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4ac`](#insn-00bbe4ac) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe4b4`](#insn-00bbe4b4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4c4`](#insn-00bbe4c4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4d8`](#insn-00bbe4d8) → [`00bbe4f4`](#insn-00bbe4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4e0`](#insn-00bbe4e0) → [`00bbe4f8`](#insn-00bbe4f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4f0`](#insn-00bbe4f0) → [`00bbe4f8`](#insn-00bbe4f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe508`](#insn-00bbe508) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe510`](#insn-00bbe510) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe520`](#insn-00bbe520) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe534`](#insn-00bbe534) → [`00bbe550`](#insn-00bbe550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe53c`](#insn-00bbe53c) → [`00bbe554`](#insn-00bbe554) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe54c`](#insn-00bbe54c) → [`00bbe554`](#insn-00bbe554) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe564`](#insn-00bbe564) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe56c`](#insn-00bbe56c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe57c`](#insn-00bbe57c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe590`](#insn-00bbe590) → [`00bbe69c`](#insn-00bbe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe598`](#insn-00bbe598) → [`00bbe69c`](#insn-00bbe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5a4`](#insn-00bbe5a4) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5c4`](#insn-00bbe5c4) → [`00bbe5dc`](#insn-00bbe5dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5d4`](#insn-00bbe5d4) → [`00c5d630`](../00c5d/00c5d630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d630` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5d8`](#insn-00bbe5d8) → [`00bbe620`](#insn-00bbe620) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5dc`](#insn-00bbe5dc) → [`00bbe620`](#insn-00bbe620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5ec`](#insn-00bbe5ec) → [`00bbe61c`](#insn-00bbe61c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5f8`](#insn-00bbe5f8) → [`00bbe610`](#insn-00bbe610) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe604`](#insn-00bbe604) → [`00bbe61c`](#insn-00bbe61c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe60c`](#insn-00bbe60c) → [`00bbe5fc`](#insn-00bbe5fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe614`](#insn-00bbe614) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbe618`](#insn-00bbe618) → [`00bbe5fc`](#insn-00bbe5fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe61c`](#insn-00bbe61c) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe620`](#insn-00bbe620) → [`00bbe69c`](#insn-00bbe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe63c`](#insn-00bbe63c) → [`00bbe658`](#insn-00bbe658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe644`](#insn-00bbe644) → [`00bbe65c`](#insn-00bbe65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe654`](#insn-00bbe654) → [`00bbe65c`](#insn-00bbe65c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe668`](#insn-00bbe668) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe67c`](#insn-00bbe67c) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe68c`](#insn-00bbe68c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe698`](#insn-00bbe698) → [`00bbe62c`](#insn-00bbe62c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6ac`](#insn-00bbe6ac) → [`00bbe6c8`](#insn-00bbe6c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6cc`](#insn-00bbe6cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe6cc`](#insn-00bbe6cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6dc`](#insn-00bbe6dc) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe6e4`](#insn-00bbe6e4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f4`](#insn-00bbe6f4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe708`](#insn-00bbe708) → [`00bbe814`](#insn-00bbe814) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe710`](#insn-00bbe710) → [`00bbe814`](#insn-00bbe814) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe71c`](#insn-00bbe71c) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe73c`](#insn-00bbe73c) → [`00bbe754`](#insn-00bbe754) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe74c`](#insn-00bbe74c) → [`00c5d630`](../00c5d/00c5d630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d630` · 推定シンボル `None` · 推定型 `None`
- [`00bbe750`](#insn-00bbe750) → [`00bbe798`](#insn-00bbe798) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe754`](#insn-00bbe754) → [`00bbe798`](#insn-00bbe798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe764`](#insn-00bbe764) → [`00bbe794`](#insn-00bbe794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe770`](#insn-00bbe770) → [`00bbe788`](#insn-00bbe788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe77c`](#insn-00bbe77c) → [`00bbe794`](#insn-00bbe794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe784`](#insn-00bbe784) → [`00bbe774`](#insn-00bbe774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe78c`](#insn-00bbe78c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbe790`](#insn-00bbe790) → [`00bbe774`](#insn-00bbe774) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe794`](#insn-00bbe794) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe798`](#insn-00bbe798) → [`00bbe814`](#insn-00bbe814) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7b4`](#insn-00bbe7b4) → [`00bbe7d0`](#insn-00bbe7d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7bc`](#insn-00bbe7bc) → [`00bbe7d4`](#insn-00bbe7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7cc`](#insn-00bbe7cc) → [`00bbe7d4`](#insn-00bbe7d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7e0`](#insn-00bbe7e0) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7f4`](#insn-00bbe7f4) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe804`](#insn-00bbe804) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe810`](#insn-00bbe810) → [`00bbe7a4`](#insn-00bbe7a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe824`](#insn-00bbe824) → [`00bbe840`](#insn-00bbe840) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe82c`](#insn-00bbe82c) → [`00bbe844`](#insn-00bbe844) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe83c`](#insn-00bbe83c) → [`00bbe844`](#insn-00bbe844) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe850`](#insn-00bbe850) → `002a638e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe854`](#insn-00bbe854) → [`00c580b0`](../00c58/00c580b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe868`](#insn-00bbe868) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bbe870`](#insn-00bbe870) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe874`](#insn-00bbe874) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe884`](#insn-00bbe884) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe888`](#insn-00bbe888) → [`00bbe894`](#insn-00bbe894) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe88c`](#insn-00bbe88c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe890`](#insn-00bbe890) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe894`](#insn-00bbe894) → `Stack[-0x308]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe898`](#insn-00bbe898) → [`00bbe8a4`](#insn-00bbe8a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe89c`](#insn-00bbe89c) → `Stack[-0x2f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8a0`](#insn-00bbe8a0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8a8`](#insn-00bbe8a8) → [`00c5d3a0`](../00c5d/00c5d3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d3a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8b0`](#insn-00bbe8b0) → [`00c5d4c0`](../00c5d/00c5d4c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d4c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8b8`](#insn-00bbe8b8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8e4`](#insn-00bbe8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8c8`](#insn-00bbe8c8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8cc`](#insn-00bbe8cc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8d0`](#insn-00bbe8d0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8d4`](#insn-00bbe8d4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8d8`](#insn-00bbe8d8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8e4`](#insn-00bbe8e4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbdae8`](#insn-00bbdae8)

~~~json
{
  "source": "00bbdae8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaec`](#insn-00bbdaec)

~~~json
{
  "source": "00bbdaec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaf0`](#insn-00bbdaf0)

~~~json
{
  "source": "00bbdaf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaf4`](#insn-00bbdaf4)

~~~json
{
  "source": "00bbdaf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaf8`](#insn-00bbdaf8)

~~~json
{
  "source": "00bbdaf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdafc`](#insn-00bbdafc)

~~~json
{
  "source": "00bbdafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb20`](#insn-00bbdb20)

~~~json
{
  "source": "00bbdb20",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb24`](#insn-00bbdb24)

~~~json
{
  "source": "00bbdb24",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb28`](#insn-00bbdb28)

~~~json
{
  "source": "00bbdb28",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb2c`](#insn-00bbdb2c)

~~~json
{
  "source": "00bbdb2c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb30`](#insn-00bbdb30)

~~~json
{
  "source": "00bbdb30",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb34`](#insn-00bbdb34)

~~~json
{
  "source": "00bbdb34",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb38`](#insn-00bbdb38)

~~~json
{
  "source": "00bbdb38",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb3c`](#insn-00bbdb3c)

~~~json
{
  "source": "00bbdb3c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb40`](#insn-00bbdb40)

~~~json
{
  "source": "00bbdb40",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb44`](#insn-00bbdb44)

~~~json
{
  "source": "00bbdb44",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb48`](#insn-00bbdb48)

~~~json
{
  "source": "00bbdb48",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb4c`](#insn-00bbdb4c)

~~~json
{
  "source": "00bbdb4c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb50`](#insn-00bbdb50)

~~~json
{
  "source": "00bbdb50",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb54`](#insn-00bbdb54)

~~~json
{
  "source": "00bbdb54",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb58`](#insn-00bbdb58)

~~~json
{
  "source": "00bbdb58",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb5c`](#insn-00bbdb5c)

~~~json
{
  "source": "00bbdb5c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb60`](#insn-00bbdb60)

~~~json
{
  "source": "00bbdb60",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb64`](#insn-00bbdb64)

~~~json
{
  "source": "00bbdb64",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb68`](#insn-00bbdb68)

~~~json
{
  "source": "00bbdb68",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb6c`](#insn-00bbdb6c)

~~~json
{
  "source": "00bbdb6c",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb70`](#insn-00bbdb70)

~~~json
{
  "source": "00bbdb70",
  "target": "Stack[-0x250]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb74`](#insn-00bbdb74)

~~~json
{
  "source": "00bbdb74",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb78`](#insn-00bbdb78)

~~~json
{
  "source": "00bbdb78",
  "target": "Stack[-0x290]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb7c`](#insn-00bbdb7c)

~~~json
{
  "source": "00bbdb7c",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb80`](#insn-00bbdb80)

~~~json
{
  "source": "00bbdb80",
  "target": "Stack[-0x2d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb84`](#insn-00bbdb84)

~~~json
{
  "source": "00bbdb84",
  "target": "Stack[-0x2f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb88`](#insn-00bbdb88)

~~~json
{
  "source": "00bbdb88",
  "target": "Stack[-0x300]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb8c`](#insn-00bbdb8c)

~~~json
{
  "source": "00bbdb8c",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbac`](#insn-00bbdbac)

~~~json
{
  "source": "00bbdbac",
  "target": "00bbdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbb4`](#insn-00bbdbb4)

~~~json
{
  "source": "00bbdbb4",
  "target": "00bbdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbd8`](#insn-00bbdbd8)

~~~json
{
  "source": "00bbdbd8",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdbdc`](#insn-00bbdbdc)

~~~json
{
  "source": "00bbdbdc",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbec`](#insn-00bbdbec)

~~~json
{
  "source": "00bbdbec",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdc00`](#insn-00bbdc00)

~~~json
{
  "source": "00bbdc00",
  "target": "00bbdc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc08`](#insn-00bbdc08)

~~~json
{
  "source": "00bbdc08",
  "target": "00bbdc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc18`](#insn-00bbdc18)

~~~json
{
  "source": "00bbdc18",
  "target": "00bbdc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc30`](#insn-00bbdc30)

~~~json
{
  "source": "00bbdc30",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdc38`](#insn-00bbdc38)

~~~json
{
  "source": "00bbdc38",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdc48`](#insn-00bbdc48)

~~~json
{
  "source": "00bbdc48",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdc60`](#insn-00bbdc60)

~~~json
{
  "source": "00bbdc60",
  "target": "00bbde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc68`](#insn-00bbdc68)

~~~json
{
  "source": "00bbdc68",
  "target": "00bbde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc78`](#insn-00bbdc78)

~~~json
{
  "source": "00bbdc78",
  "target": "00bbde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc80`](#insn-00bbdc80)

~~~json
{
  "source": "00bbdc80",
  "target": "00bbde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc88`](#insn-00bbdc88)

~~~json
{
  "source": "00bbdc88",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc98`](#insn-00bbdc98)

~~~json
{
  "source": "00bbdc98",
  "target": "00bbdcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdca8`](#insn-00bbdca8)

~~~json
{
  "source": "00bbdca8",
  "target": "00bbddfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdce0`](#insn-00bbdce0)

~~~json
{
  "source": "00bbdce0",
  "target": "00bbdd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdce8`](#insn-00bbdce8)

~~~json
{
  "source": "00bbdce8",
  "target": "00bbdcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd08`](#insn-00bbdd08)

~~~json
{
  "source": "00bbdd08",
  "target": "00bbdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd10`](#insn-00bbdd10)

~~~json
{
  "source": "00bbdd10",
  "target": "00bbdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd20`](#insn-00bbdd20)

~~~json
{
  "source": "00bbdd20",
  "target": "00bbdd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd28`](#insn-00bbdd28)

~~~json
{
  "source": "00bbdd28",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdd2c`](#insn-00bbdd2c)

~~~json
{
  "source": "00bbdd2c",
  "target": "00bbdd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd44`](#insn-00bbdd44)

~~~json
{
  "source": "00bbdd44",
  "target": "00c5b690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd54`](#insn-00bbdd54)

~~~json
{
  "source": "00bbdd54",
  "target": "0046d5e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd60`](#insn-00bbdd60)

~~~json
{
  "source": "00bbdd60",
  "target": "00bbddcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd68`](#insn-00bbdd68)

~~~json
{
  "source": "00bbdd68",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd6c`](#insn-00bbdd6c)

~~~json
{
  "source": "00bbdd6c",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd70`](#insn-00bbdd70)

~~~json
{
  "source": "00bbdd70",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd74`](#insn-00bbdd74)

~~~json
{
  "source": "00bbdd74",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd78`](#insn-00bbdd78)

~~~json
{
  "source": "00bbdd78",
  "target": "Stack[-0x318]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd7c`](#insn-00bbdd7c)

~~~json
{
  "source": "00bbdd7c",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd98`](#insn-00bbdd98)

~~~json
{
  "source": "00bbdd98",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdda0`](#insn-00bbdda0)

~~~json
{
  "source": "00bbdda0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdda4`](#insn-00bbdda4)

~~~json
{
  "source": "00bbdda4",
  "target": "00bbddb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdda8`](#insn-00bbdda8)

~~~json
{
  "source": "00bbdda8",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddb0`](#insn-00bbddb0)

~~~json
{
  "source": "00bbddb0",
  "target": "00bbddb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddb8`](#insn-00bbddb8)

~~~json
{
  "source": "00bbddb8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddbc`](#insn-00bbddbc)

~~~json
{
  "source": "00bbddbc",
  "target": "00c5b6b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbddc0`](#insn-00bbddc0)

~~~json
{
  "source": "00bbddc0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddc8`](#insn-00bbddc8)

~~~json
{
  "source": "00bbddc8",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddd4`](#insn-00bbddd4)

~~~json
{
  "source": "00bbddd4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdde4`](#insn-00bbdde4)

~~~json
{
  "source": "00bbdde4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdde8`](#insn-00bbdde8)

~~~json
{
  "source": "00bbdde8",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddec`](#insn-00bbddec)

~~~json
{
  "source": "00bbddec",
  "target": "00bbdc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddf0`](#insn-00bbddf0)

~~~json
{
  "source": "00bbddf0",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddf4`](#insn-00bbddf4)

~~~json
{
  "source": "00bbddf4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbddf8`](#insn-00bbddf8)

~~~json
{
  "source": "00bbddf8",
  "target": "00bbdc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddfc`](#insn-00bbddfc)

~~~json
{
  "source": "00bbddfc",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde14`](#insn-00bbde14)

~~~json
{
  "source": "00bbde14",
  "target": "00bbdedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde1c`](#insn-00bbde1c)

~~~json
{
  "source": "00bbde1c",
  "target": "00bbdedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde2c`](#insn-00bbde2c)

~~~json
{
  "source": "00bbde2c",
  "target": "00bbdedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde30`](#insn-00bbde30)

~~~json
{
  "source": "00bbde30",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde34`](#insn-00bbde34)

~~~json
{
  "source": "00bbde34",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde44`](#insn-00bbde44)

~~~json
{
  "source": "00bbde44",
  "target": "00bbde8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde48`](#insn-00bbde48)

~~~json
{
  "source": "00bbde48",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde50`](#insn-00bbde50)

~~~json
{
  "source": "00bbde50",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde68`](#insn-00bbde68)

~~~json
{
  "source": "00bbde68",
  "target": "00bbde78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde74`](#insn-00bbde74)

~~~json
{
  "source": "00bbde74",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde78`](#insn-00bbde78)

~~~json
{
  "source": "00bbde78",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde7c`](#insn-00bbde7c)

~~~json
{
  "source": "00bbde7c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde80`](#insn-00bbde80)

~~~json
{
  "source": "00bbde80",
  "target": "00bbde8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde88`](#insn-00bbde88)

~~~json
{
  "source": "00bbde88",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdeb4`](#insn-00bbdeb4)

~~~json
{
  "source": "00bbdeb4",
  "target": "Stack[-0x328]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdec4`](#insn-00bbdec4)

~~~json
{
  "source": "00bbdec4",
  "target": "Stack[-0x330]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbded0`](#insn-00bbded0)

~~~json
{
  "source": "00bbded0",
  "target": "00c5d640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdee8`](#insn-00bbdee8)

~~~json
{
  "source": "00bbdee8",
  "target": "00bbdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdef0`](#insn-00bbdef0)

~~~json
{
  "source": "00bbdef0",
  "target": "00bbdf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf00`](#insn-00bbdf00)

~~~json
{
  "source": "00bbdf00",
  "target": "00bbdf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf18`](#insn-00bbdf18)

~~~json
{
  "source": "00bbdf18",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdf20`](#insn-00bbdf20)

~~~json
{
  "source": "00bbdf20",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf30`](#insn-00bbdf30)

~~~json
{
  "source": "00bbdf30",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf44`](#insn-00bbdf44)

~~~json
{
  "source": "00bbdf44",
  "target": "00bbdf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf4c`](#insn-00bbdf4c)

~~~json
{
  "source": "00bbdf4c",
  "target": "00bbdf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf5c`](#insn-00bbdf5c)

~~~json
{
  "source": "00bbdf5c",
  "target": "00bbdf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf74`](#insn-00bbdf74)

~~~json
{
  "source": "00bbdf74",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdf7c`](#insn-00bbdf7c)

~~~json
{
  "source": "00bbdf7c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf8c`](#insn-00bbdf8c)

~~~json
{
  "source": "00bbdf8c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfa4`](#insn-00bbdfa4)

~~~json
{
  "source": "00bbdfa4",
  "target": "00bbdfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfac`](#insn-00bbdfac)

~~~json
{
  "source": "00bbdfac",
  "target": "00bbdfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfbc`](#insn-00bbdfbc)

~~~json
{
  "source": "00bbdfbc",
  "target": "00bbdfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfd0`](#insn-00bbdfd0)

~~~json
{
  "source": "00bbdfd0",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdfd4`](#insn-00bbdfd4)

~~~json
{
  "source": "00bbdfd4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfe4`](#insn-00bbdfe4)

~~~json
{
  "source": "00bbdfe4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdff8`](#insn-00bbdff8)

~~~json
{
  "source": "00bbdff8",
  "target": "00bbe014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe000`](#insn-00bbe000)

~~~json
{
  "source": "00bbe000",
  "target": "00bbe018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe010`](#insn-00bbe010)

~~~json
{
  "source": "00bbe010",
  "target": "00bbe018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe028`](#insn-00bbe028)

~~~json
{
  "source": "00bbe028",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe030`](#insn-00bbe030)

~~~json
{
  "source": "00bbe030",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe040`](#insn-00bbe040)

~~~json
{
  "source": "00bbe040",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe054`](#insn-00bbe054)

~~~json
{
  "source": "00bbe054",
  "target": "00bbe090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe05c`](#insn-00bbe05c)

~~~json
{
  "source": "00bbe05c",
  "target": "00bbe06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe070`](#insn-00bbe070)

~~~json
{
  "source": "00bbe070",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe074`](#insn-00bbe074)

~~~json
{
  "source": "00bbe074",
  "target": "00bbe09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe07c`](#insn-00bbe07c)

~~~json
{
  "source": "00bbe07c",
  "target": "00bbe0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe08c`](#insn-00bbe08c)

~~~json
{
  "source": "00bbe08c",
  "target": "00bbe0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe094`](#insn-00bbe094)

~~~json
{
  "source": "00bbe094",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe098`](#insn-00bbe098)

~~~json
{
  "source": "00bbe098",
  "target": "00bbe0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0ac`](#insn-00bbe0ac)

~~~json
{
  "source": "00bbe0ac",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe0b0`](#insn-00bbe0b0)

~~~json
{
  "source": "00bbe0b0",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe0c0`](#insn-00bbe0c0)

~~~json
{
  "source": "00bbe0c0",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe0d4`](#insn-00bbe0d4)

~~~json
{
  "source": "00bbe0d4",
  "target": "00bbe0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0dc`](#insn-00bbe0dc)

~~~json
{
  "source": "00bbe0dc",
  "target": "00bbe0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0ec`](#insn-00bbe0ec)

~~~json
{
  "source": "00bbe0ec",
  "target": "00bbe0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe104`](#insn-00bbe104)

~~~json
{
  "source": "00bbe104",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe10c`](#insn-00bbe10c)

~~~json
{
  "source": "00bbe10c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe11c`](#insn-00bbe11c)

~~~json
{
  "source": "00bbe11c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe130`](#insn-00bbe130)

~~~json
{
  "source": "00bbe130",
  "target": "00bbe14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe138`](#insn-00bbe138)

~~~json
{
  "source": "00bbe138",
  "target": "00bbe150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe148`](#insn-00bbe148)

~~~json
{
  "source": "00bbe148",
  "target": "00bbe150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe160`](#insn-00bbe160)

~~~json
{
  "source": "00bbe160",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe168`](#insn-00bbe168)

~~~json
{
  "source": "00bbe168",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe178`](#insn-00bbe178)

~~~json
{
  "source": "00bbe178",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe18c`](#insn-00bbe18c)

~~~json
{
  "source": "00bbe18c",
  "target": "00bbe1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe194`](#insn-00bbe194)

~~~json
{
  "source": "00bbe194",
  "target": "00bbe1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1a4`](#insn-00bbe1a4)

~~~json
{
  "source": "00bbe1a4",
  "target": "00bbe1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1bc`](#insn-00bbe1bc)

~~~json
{
  "source": "00bbe1bc",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe1c4`](#insn-00bbe1c4)

~~~json
{
  "source": "00bbe1c4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe1d4`](#insn-00bbe1d4)

~~~json
{
  "source": "00bbe1d4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe1e8`](#insn-00bbe1e8)

~~~json
{
  "source": "00bbe1e8",
  "target": "00bbe208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1f0`](#insn-00bbe1f0)

~~~json
{
  "source": "00bbe1f0",
  "target": "00bbe1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1f8`](#insn-00bbe1f8)

~~~json
{
  "source": "00bbe1f8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe200`](#insn-00bbe200)

~~~json
{
  "source": "00bbe200",
  "target": "00bbe21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe204`](#insn-00bbe204)

~~~json
{
  "source": "00bbe204",
  "target": "00bbe220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe20c`](#insn-00bbe20c)

~~~json
{
  "source": "00bbe20c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe210`](#insn-00bbe210)

~~~json
{
  "source": "00bbe210",
  "target": "00bbe270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe218`](#insn-00bbe218)

~~~json
{
  "source": "00bbe218",
  "target": "00bbe220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe224`](#insn-00bbe224)

~~~json
{
  "source": "00bbe224",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe228`](#insn-00bbe228)

~~~json
{
  "source": "00bbe228",
  "target": "00bbe878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe230`](#insn-00bbe230)

~~~json
{
  "source": "00bbe230",
  "target": "00bbe878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe240`](#insn-00bbe240)

~~~json
{
  "source": "00bbe240",
  "target": "00bbe878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe254`](#insn-00bbe254)

~~~json
{
  "source": "00bbe254",
  "target": "00bbe278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe25c`](#insn-00bbe25c)

~~~json
{
  "source": "00bbe25c",
  "target": "00bbe27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe26c`](#insn-00bbe26c)

~~~json
{
  "source": "00bbe26c",
  "target": "00bbe27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe270`](#insn-00bbe270)

~~~json
{
  "source": "00bbe270",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe274`](#insn-00bbe274)

~~~json
{
  "source": "00bbe274",
  "target": "00bbe878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe288`](#insn-00bbe288)

~~~json
{
  "source": "00bbe288",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe28c`](#insn-00bbe28c)

~~~json
{
  "source": "00bbe28c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe29c`](#insn-00bbe29c)

~~~json
{
  "source": "00bbe29c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe2b0`](#insn-00bbe2b0)

~~~json
{
  "source": "00bbe2b0",
  "target": "00bbe2cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2b8`](#insn-00bbe2b8)

~~~json
{
  "source": "00bbe2b8",
  "target": "00bbe2d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2c8`](#insn-00bbe2c8)

~~~json
{
  "source": "00bbe2c8",
  "target": "00bbe2d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2e0`](#insn-00bbe2e0)

~~~json
{
  "source": "00bbe2e0",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe2e8`](#insn-00bbe2e8)

~~~json
{
  "source": "00bbe2e8",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe2f8`](#insn-00bbe2f8)

~~~json
{
  "source": "00bbe2f8",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe30c`](#insn-00bbe30c)

~~~json
{
  "source": "00bbe30c",
  "target": "00bbe328",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe314`](#insn-00bbe314)

~~~json
{
  "source": "00bbe314",
  "target": "00bbe32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe324`](#insn-00bbe324)

~~~json
{
  "source": "00bbe324",
  "target": "00bbe32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe33c`](#insn-00bbe33c)

~~~json
{
  "source": "00bbe33c",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe344`](#insn-00bbe344)

~~~json
{
  "source": "00bbe344",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe354`](#insn-00bbe354)

~~~json
{
  "source": "00bbe354",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe368`](#insn-00bbe368)

~~~json
{
  "source": "00bbe368",
  "target": "00bbe384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe370`](#insn-00bbe370)

~~~json
{
  "source": "00bbe370",
  "target": "00bbe388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe380`](#insn-00bbe380)

~~~json
{
  "source": "00bbe380",
  "target": "00bbe388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe398`](#insn-00bbe398)

~~~json
{
  "source": "00bbe398",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe3a0`](#insn-00bbe3a0)

~~~json
{
  "source": "00bbe3a0",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe3b0`](#insn-00bbe3b0)

~~~json
{
  "source": "00bbe3b0",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe3c4`](#insn-00bbe3c4)

~~~json
{
  "source": "00bbe3c4",
  "target": "00bbe3e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3cc`](#insn-00bbe3cc)

~~~json
{
  "source": "00bbe3cc",
  "target": "00bbe3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3dc`](#insn-00bbe3dc)

~~~json
{
  "source": "00bbe3dc",
  "target": "00bbe3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3f4`](#insn-00bbe3f4)

~~~json
{
  "source": "00bbe3f4",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe3fc`](#insn-00bbe3fc)

~~~json
{
  "source": "00bbe3fc",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe40c`](#insn-00bbe40c)

~~~json
{
  "source": "00bbe40c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe420`](#insn-00bbe420)

~~~json
{
  "source": "00bbe420",
  "target": "00bbe43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe428`](#insn-00bbe428)

~~~json
{
  "source": "00bbe428",
  "target": "00bbe440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe438`](#insn-00bbe438)

~~~json
{
  "source": "00bbe438",
  "target": "00bbe440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe450`](#insn-00bbe450)

~~~json
{
  "source": "00bbe450",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe458`](#insn-00bbe458)

~~~json
{
  "source": "00bbe458",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe468`](#insn-00bbe468)

~~~json
{
  "source": "00bbe468",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe47c`](#insn-00bbe47c)

~~~json
{
  "source": "00bbe47c",
  "target": "00bbe498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe484`](#insn-00bbe484)

~~~json
{
  "source": "00bbe484",
  "target": "00bbe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe494`](#insn-00bbe494)

~~~json
{
  "source": "00bbe494",
  "target": "00bbe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4ac`](#insn-00bbe4ac)

~~~json
{
  "source": "00bbe4ac",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe4b4`](#insn-00bbe4b4)

~~~json
{
  "source": "00bbe4b4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe4c4`](#insn-00bbe4c4)

~~~json
{
  "source": "00bbe4c4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe4d8`](#insn-00bbe4d8)

~~~json
{
  "source": "00bbe4d8",
  "target": "00bbe4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4e0`](#insn-00bbe4e0)

~~~json
{
  "source": "00bbe4e0",
  "target": "00bbe4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4f0`](#insn-00bbe4f0)

~~~json
{
  "source": "00bbe4f0",
  "target": "00bbe4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe508`](#insn-00bbe508)

~~~json
{
  "source": "00bbe508",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe510`](#insn-00bbe510)

~~~json
{
  "source": "00bbe510",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe520`](#insn-00bbe520)

~~~json
{
  "source": "00bbe520",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe534`](#insn-00bbe534)

~~~json
{
  "source": "00bbe534",
  "target": "00bbe550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe53c`](#insn-00bbe53c)

~~~json
{
  "source": "00bbe53c",
  "target": "00bbe554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe54c`](#insn-00bbe54c)

~~~json
{
  "source": "00bbe54c",
  "target": "00bbe554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe564`](#insn-00bbe564)

~~~json
{
  "source": "00bbe564",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe56c`](#insn-00bbe56c)

~~~json
{
  "source": "00bbe56c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe57c`](#insn-00bbe57c)

~~~json
{
  "source": "00bbe57c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe590`](#insn-00bbe590)

~~~json
{
  "source": "00bbe590",
  "target": "00bbe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe598`](#insn-00bbe598)

~~~json
{
  "source": "00bbe598",
  "target": "00bbe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5a4`](#insn-00bbe5a4)

~~~json
{
  "source": "00bbe5a4",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5c4`](#insn-00bbe5c4)

~~~json
{
  "source": "00bbe5c4",
  "target": "00bbe5dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5d4`](#insn-00bbe5d4)

~~~json
{
  "source": "00bbe5d4",
  "target": "00c5d630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe5d8`](#insn-00bbe5d8)

~~~json
{
  "source": "00bbe5d8",
  "target": "00bbe620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5dc`](#insn-00bbe5dc)

~~~json
{
  "source": "00bbe5dc",
  "target": "00bbe620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5ec`](#insn-00bbe5ec)

~~~json
{
  "source": "00bbe5ec",
  "target": "00bbe61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5f8`](#insn-00bbe5f8)

~~~json
{
  "source": "00bbe5f8",
  "target": "00bbe610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe604`](#insn-00bbe604)

~~~json
{
  "source": "00bbe604",
  "target": "00bbe61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe60c`](#insn-00bbe60c)

~~~json
{
  "source": "00bbe60c",
  "target": "00bbe5fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe614`](#insn-00bbe614)

~~~json
{
  "source": "00bbe614",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe618`](#insn-00bbe618)

~~~json
{
  "source": "00bbe618",
  "target": "00bbe5fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe61c`](#insn-00bbe61c)

~~~json
{
  "source": "00bbe61c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe620`](#insn-00bbe620)

~~~json
{
  "source": "00bbe620",
  "target": "00bbe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe63c`](#insn-00bbe63c)

~~~json
{
  "source": "00bbe63c",
  "target": "00bbe658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe644`](#insn-00bbe644)

~~~json
{
  "source": "00bbe644",
  "target": "00bbe65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe654`](#insn-00bbe654)

~~~json
{
  "source": "00bbe654",
  "target": "00bbe65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe668`](#insn-00bbe668)

~~~json
{
  "source": "00bbe668",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe67c`](#insn-00bbe67c)

~~~json
{
  "source": "00bbe67c",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe68c`](#insn-00bbe68c)

~~~json
{
  "source": "00bbe68c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe698`](#insn-00bbe698)

~~~json
{
  "source": "00bbe698",
  "target": "00bbe62c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6ac`](#insn-00bbe6ac)

~~~json
{
  "source": "00bbe6ac",
  "target": "00bbe6c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6b4`](#insn-00bbe6b4)

~~~json
{
  "source": "00bbe6b4",
  "target": "00bbe6cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6c4`](#insn-00bbe6c4)

~~~json
{
  "source": "00bbe6c4",
  "target": "00bbe6cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6dc`](#insn-00bbe6dc)

~~~json
{
  "source": "00bbe6dc",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe6e4`](#insn-00bbe6e4)

~~~json
{
  "source": "00bbe6e4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6f4`](#insn-00bbe6f4)

~~~json
{
  "source": "00bbe6f4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe708`](#insn-00bbe708)

~~~json
{
  "source": "00bbe708",
  "target": "00bbe814",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe710`](#insn-00bbe710)

~~~json
{
  "source": "00bbe710",
  "target": "00bbe814",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe71c`](#insn-00bbe71c)

~~~json
{
  "source": "00bbe71c",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe73c`](#insn-00bbe73c)

~~~json
{
  "source": "00bbe73c",
  "target": "00bbe754",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe74c`](#insn-00bbe74c)

~~~json
{
  "source": "00bbe74c",
  "target": "00c5d630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe750`](#insn-00bbe750)

~~~json
{
  "source": "00bbe750",
  "target": "00bbe798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe754`](#insn-00bbe754)

~~~json
{
  "source": "00bbe754",
  "target": "00bbe798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe764`](#insn-00bbe764)

~~~json
{
  "source": "00bbe764",
  "target": "00bbe794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe770`](#insn-00bbe770)

~~~json
{
  "source": "00bbe770",
  "target": "00bbe788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe77c`](#insn-00bbe77c)

~~~json
{
  "source": "00bbe77c",
  "target": "00bbe794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe784`](#insn-00bbe784)

~~~json
{
  "source": "00bbe784",
  "target": "00bbe774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe78c`](#insn-00bbe78c)

~~~json
{
  "source": "00bbe78c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe790`](#insn-00bbe790)

~~~json
{
  "source": "00bbe790",
  "target": "00bbe774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe794`](#insn-00bbe794)

~~~json
{
  "source": "00bbe794",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe798`](#insn-00bbe798)

~~~json
{
  "source": "00bbe798",
  "target": "00bbe814",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7b4`](#insn-00bbe7b4)

~~~json
{
  "source": "00bbe7b4",
  "target": "00bbe7d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7bc`](#insn-00bbe7bc)

~~~json
{
  "source": "00bbe7bc",
  "target": "00bbe7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7cc`](#insn-00bbe7cc)

~~~json
{
  "source": "00bbe7cc",
  "target": "00bbe7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7e0`](#insn-00bbe7e0)

~~~json
{
  "source": "00bbe7e0",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7f4`](#insn-00bbe7f4)

~~~json
{
  "source": "00bbe7f4",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe804`](#insn-00bbe804)

~~~json
{
  "source": "00bbe804",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe810`](#insn-00bbe810)

~~~json
{
  "source": "00bbe810",
  "target": "00bbe7a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe824`](#insn-00bbe824)

~~~json
{
  "source": "00bbe824",
  "target": "00bbe840",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe82c`](#insn-00bbe82c)

~~~json
{
  "source": "00bbe82c",
  "target": "00bbe844",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe83c`](#insn-00bbe83c)

~~~json
{
  "source": "00bbe83c",
  "target": "00bbe844",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe850`](#insn-00bbe850)

~~~json
{
  "source": "00bbe850",
  "target": "002a638e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a638e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a638e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe854`](#insn-00bbe854)

~~~json
{
  "source": "00bbe854",
  "target": "00c580b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe868`](#insn-00bbe868)

~~~json
{
  "source": "00bbe868",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe870`](#insn-00bbe870)

~~~json
{
  "source": "00bbe870",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe874`](#insn-00bbe874)

~~~json
{
  "source": "00bbe874",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe884`](#insn-00bbe884)

~~~json
{
  "source": "00bbe884",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe888`](#insn-00bbe888)

~~~json
{
  "source": "00bbe888",
  "target": "00bbe894",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe88c`](#insn-00bbe88c)

~~~json
{
  "source": "00bbe88c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe890`](#insn-00bbe890)

~~~json
{
  "source": "00bbe890",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe894`](#insn-00bbe894)

~~~json
{
  "source": "00bbe894",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe898`](#insn-00bbe898)

~~~json
{
  "source": "00bbe898",
  "target": "00bbe8a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe89c`](#insn-00bbe89c)

~~~json
{
  "source": "00bbe89c",
  "target": "Stack[-0x2f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8a0`](#insn-00bbe8a0)

~~~json
{
  "source": "00bbe8a0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8a8`](#insn-00bbe8a8)

~~~json
{
  "source": "00bbe8a8",
  "target": "00c5d3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8b0`](#insn-00bbe8b0)

~~~json
{
  "source": "00bbe8b0",
  "target": "00c5d4c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8b8`](#insn-00bbe8b8)

~~~json
{
  "source": "00bbe8b8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8c0`](#insn-00bbe8c0)

~~~json
{
  "source": "00bbe8c0",
  "target": "00bbe8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8c8`](#insn-00bbe8c8)

~~~json
{
  "source": "00bbe8c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8cc`](#insn-00bbe8cc)

~~~json
{
  "source": "00bbe8cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8d0`](#insn-00bbe8d0)

~~~json
{
  "source": "00bbe8d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8d4`](#insn-00bbe8d4)

~~~json
{
  "source": "00bbe8d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8d8`](#insn-00bbe8d8)

~~~json
{
  "source": "00bbe8d8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8e4`](#insn-00bbe8e4)

~~~json
{
  "source": "00bbe8e4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
