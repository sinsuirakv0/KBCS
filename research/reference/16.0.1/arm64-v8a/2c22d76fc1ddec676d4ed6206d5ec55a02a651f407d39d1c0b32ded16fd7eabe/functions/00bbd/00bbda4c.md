# 00bbda4c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbd624`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-89f948e4a5a59da1fd028b61524b2ca6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbdae8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbdae8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-4ac594f18f4fe61e92243c74c76710b9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbda4c",
  "name": "_ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE",
  "size": 3584,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b63e4c90bbd5ef845a087abd6b23840ea53d32c68a2dfab94a84e0e1cfb324c6",
  "source_text_sha256": "b63e4c90bbd5ef845a087abd6b23840ea53d32c68a2dfab94a84e0e1cfb324c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbda4c",
        "00bbe84b"
      ]
    ],
    "bytes_sha256": "8cb6b145fc0cb8278402f5fc7cf7a3a8776b0bfbb8039bec1ee590204c9c054e",
    "instruction_count": 896,
    "instruction_bytes": 3584,
    "body_bytes": 3584,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5d540](../00c5d/00c5d540.md)

## 呼び出し先

- [0046d5a8](../0046d/0046d5a8.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)
- [00c5b5e0](../00c5b/00c5b5e0.md)
- [00c5d2d0](../00c5d/00c5d2d0.md)
- [00c5d3f0](../00c5d/00c5d3f0.md)
- [00c5d560](../00c5d/00c5d560.md)
- [00c5d570](../00c5d/00c5d570.md)

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
  
  lVar5 = tpidr_el0;
  local_78 = *(long *)(lVar5 + 0x28);
                    /* try { // try from 00bbda78 to 00cbda83 has its CatchHandler @ 00bbe008 */
  local_178 = &local_170;
  local_170 = 0;
  local_168 = 0;
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
                    /* try { // try from 00bbdab8 to 00cbdabf has its CatchHandler @ 00bbe004 */
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
    lVar16 = 0;
    if (uVar17 != 0) {
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
                    /* try { // try from 00bbdb44 to 00cbdb47 has its CatchHandler @ 00bbdfc8 */
                    /* try { // try from 00bbdb48 to 00cbdbd3 has its CatchHandler @ 00bbd8ec */
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
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_1a8,pcVar14,sVar12);
  uVar17 = (ulong)(int)*param_2;
  lVar16 = -uVar17;
                    /* try { // try from 00bbdbd4 to 00cbdc0b has its CatchHandler @ 00bbe014 */
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
                    /* try { // try from 00bbdc88 to 00cbdc8b has its CatchHandler @ 00bbdfd4 */
        lVar16 = 0;
                    /* try { // try from 00bbdc8c to 00cbdd5b has its CatchHandler @ 00bbd8ec */
        pcVar14 = "";
      }
      else {
        lVar16 = 0;
        if ((ulong)puVar20[2] != 0) {
          puVar18 = (uint *)((long)piVar1 + (ulong)puVar20[2]);
          lVar16 = (long)puVar18 + (ulong)*puVar18;
        }
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
      puVar13 = (undefined8 *)FUN_0046d5a8(&local_178,&local_80,&local_320);
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
      sVar12 = strlen(__s_00);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (puVar23 + 7,__s_00,sVar12);
      if ((local_320 & 1) != 0) {
        _ZdlPv(local_310);
                    /* try { // try from 00bbdd5c to 00cbdd63 has its CatchHandler @ 00bbdf80 */
      }
      uVar17 = (ulong)*param_2;
      uVar21 = uVar21 + 4;
    } while ((ulong)uVar2 * 4 - uVar21 != 0);
                    /* try { // try from 00bbdd64 to 00cbddb7 has its CatchHandler @ 00bbd8ec */
    lVar16 = -(long)(int)*param_2;
  }
  lVar10 = lStack_158;
  pvVar9 = local_160;
  if (((0xc < *(ushort *)((long)param_2 + lVar16)) &&
      (uVar17 = (ulong)((ushort *)((long)param_2 + lVar16))[6], uVar17 != 0)) &&
     (puVar18 = (uint *)((long)param_2 + uVar17),
     puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18), puVar18 != (uint *)0x0)) {
    uVar17 = (ulong)*puVar18;
    if ((ulong)(local_150 - (long)local_160) < uVar17) {
      __dest = (void *)_Znwm(uVar17);
                    /* try { // try from 00bbddb8 to 00cbddcb has its CatchHandler @ 00bbdfac */
      sVar12 = lVar10 - (long)pvVar9;
      if (0 < (long)sVar12) {
        memcpy(__dest,pvVar9,sVar12);
      }
      local_160 = __dest;
      lStack_158 = (long)__dest + sVar12;
      local_150 = (long)__dest + uVar17;
      if (pvVar9 != (void *)0x0) {
        _ZdlPv(pvVar9);
      }
    }
                    /* try { // try from 00bbddf8 to 00cbddff has its CatchHandler @ 00bbdfd8 */
    uVar4 = *(ushort *)((long)param_2 + (0xc - (long)(int)*param_2));
    puVar18 = (uint *)((long)param_2 + (ulong)uVar4);
    puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18);
    local_328 = (uint *)0x0;
    if (uVar4 != 0) {
      local_328 = puVar18;
    }
                    /* try { // try from 00bbde14 to 00cbde1b has its CatchHandler @ 00bbdf84 */
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
  pcVar14 = __s;
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
  sVar12 = strlen(pcVar14);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_130,pcVar14,sVar12);
                    /* try { // try from 00bbdef4 to 00cbdefb has its CatchHandler @ 00bbe000 */
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x17) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xb];
                    /* try { // try from 00bbdf10 to 00cbdf33 has its CatchHandler @ 00bbe00c */
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
                    /* try { // try from 00bbdf48 to 00cbdf4f has its CatchHandler @ 00bbdfe0 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_f8,pcVar14,sVar12);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x19) {
    lVar16 = 0;
  }
  else {
    uVar17 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xc];
                    /* try { // try from 00bbdf64 to 00cbdf67 has its CatchHandler @ 00bbe00c */
    lVar16 = 0;
    if (uVar17 != 0) {
      puVar18 = (uint *)((long)param_2 + uVar17);
      lVar16 = (long)puVar18 + (ulong)*puVar18;
    }
  }
                    /* try { // try from 00bbdf7c to 00cbdf7f has its CatchHandler @ 00bbdfe0 */
                    /* catch() { ... } // from try @ 00bbdd5c with catch @ 00bbdf80
                       try { // try from 00bbdf80 to 00cbe057 has its CatchHandler @ 00bbd8ec */
  pcVar14 = __s;
                    /* catch() { ... } // from try @ 00bbde14 with catch @ 00bbdf84 */
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
                    /* catch() { ... } // from try @ 00bbd99c with catch @ 00bbdf88 */
  sVar12 = strlen(pcVar14);
                    /* catch() { ... } // from try @ 00bbd990 with catch @ 00bbdf98 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_e0,pcVar14,sVar12);
                    /* catch() { ... } // from try @ 00bbd984 with catch @ 00bbdfa8 */
                    /* catch() { ... } // from try @ 00bbddb8 with catch @ 00bbdfac */
  puVar20 = (ushort *)((long)param_2 - (long)(int)*param_2);
                    /* catch() { ... } // from try @ 00bbd958 with catch @ 00bbdfb0 */
  if (*puVar20 < 0x1d) {
    lVar16 = 0;
    local_c0 = false;
  }
  else {
    local_c0 = false;
    if ((ulong)puVar20[0xe] != 0) {
                    /* catch() { ... } // from try @ 00bbdb44 with catch @ 00bbdfc8 */
      local_c0 = *(char *)((long)param_2 + (ulong)puVar20[0xe]) != '\0';
    }
                    /* catch() { ... } // from try @ 00bbdc88 with catch @ 00bbdfd4 */
                    /* catch() { ... } // from try @ 00bbddf8 with catch @ 00bbdfd8 */
    if (*puVar20 < 0x1f) {
                    /* catch() { ... } // from try @ 00bbdef4 with catch @ 00bbe000 */
      lVar16 = 0;
    }
    else {
                    /* catch() { ... } // from try @ 00bbdf48 with catch @ 00bbdfe0
                       catch() { ... } // from try @ 00bbdf7c with catch @ 00bbdfe0 */
      lVar16 = 0;
      if ((ulong)puVar20[0xf] != 0) {
        puVar18 = (uint *)((long)param_2 + (ulong)puVar20[0xf]);
        lVar16 = (long)puVar18 + (ulong)*puVar18;
      }
    }
  }
                    /* catch() { ... } // from try @ 00bbdab8 with catch @ 00bbe004 */
                    /* catch() { ... } // from try @ 00bbda78 with catch @ 00bbe008 */
  pcVar14 = __s;
                    /* catch() { ... } // from try @ 00bbdf10 with catch @ 00bbe00c
                       catch() { ... } // from try @ 00bbdf64 with catch @ 00bbe00c */
  if (lVar16 != 0) {
    pcVar14 = (char *)(lVar16 + 4);
  }
                    /* catch() { ... } // from try @ 00bbdbd4 with catch @ 00bbe014 */
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
      goto LAB_00bbe7dc;
    }
    uVar17 = (ulong)puVar20[10];
    local_100 = 0;
    if (uVar17 != 0) goto LAB_00bbe180;
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
LAB_00bbe180:
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
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (&local_308,__s,sVar12);
    local_c8 = SUB81(&local_2f0,0);
    uStack_c7 = (undefined7)((ulong)&local_2f0 >> 8);
    local_1d0 = &local_308;
  }
LAB_00bbe7dc:
  (*(code *)*param_1)(&local_1c0,param_1[1]);
  if (CONCAT71(uStack_c7,local_c8) != 0) {
    *(undefined8 *)(CONCAT71(uStack_c7,local_c8) + 0x120) = 0;
    local_c8 = 0;
    uStack_c7 = 0;
  }
                    /* try { // try from 00bbe7f8 to 00cbeb17 has its CatchHandler @ 00bbe7f8
                       catch() { ... } // from try @ 00bbe7f8 with catch @ 00bbe7f8
                       catch() { ... } // from try @ 00bbeb68 with catch @ 00bbe7f8
                       catch() { ... } // from try @ 00bbec88 with catch @ 00bbe7f8
                       catch() { ... } // from try @ 00bbed50 with catch @ 00bbe7f8
                       catch() { ... } // from try @ 00bbf14c with catch @ 00bbe7f8
                       catch() { ... } // from try @ 00bbf3a0 with catch @ 00bbe7f8 */
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
<a id="insn-00bbda4c"></a> `00bbda4c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbda50"></a> `00bbda50` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbda54"></a> `00bbda54` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbda58"></a> `00bbda58` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbda5c"></a> `00bbda5c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbda60"></a> `00bbda60` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbda64"></a> `00bbda64` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbda68"></a> `00bbda68` | `ff 83 0b d1` | sub sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbda6c"></a> `00bbda6c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbda70"></a> `00bbda70` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbda74"></a> `00bbda74` | `fc 03 06 91` | add x28,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbda78"></a> `00bbda78` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbda7c"></a> `00bbda7c` | `89 43 01 91` | add x9,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00bbda80"></a> `00bbda80` | `95 23 04 91` | add x21,x28,#0x108 | `FALL_THROUGH`
<a id="insn-00bbda84"></a> `00bbda84` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbda88"></a> `00bbda88` | `ff 7f 1d a9` | stp xzr,xzr,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbda8c"></a> `00bbda8c` | `e0 03 0c ad` | stp q0,q0,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00bbda90"></a> `00bbda90` | `e0 03 0d ad` | stp q0,q0,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bbda94"></a> `00bbda94` | `ff 27 1c a9` | stp xzr,x9,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bbda98"></a> `00bbda98` | `e0 03 0f ad` | stp q0,q0,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbda9c"></a> `00bbda9c` | `e0 03 10 ad` | stp q0,q0,[sp, #0x200] | `FALL_THROUGH`
<a id="insn-00bbdaa0"></a> `00bbdaa0` | `e0 03 11 ad` | stp q0,q0,[sp, #0x220] | `FALL_THROUGH`
<a id="insn-00bbdaa4"></a> `00bbdaa4` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbdaa8"></a> `00bbdaa8` | `80 83 8c 3c` | stur q0,[x28, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbdaac"></a> `00bbdaac` | `80 83 8d 3c` | stur q0,[x28, #0xd8] | `FALL_THROUGH`
<a id="insn-00bbdab0"></a> `00bbdab0` | `80 83 8e 3c` | stur q0,[x28, #0xe8] | `FALL_THROUGH`
<a id="insn-00bbdab4"></a> `00bbdab4` | `80 13 8f 3c` | stur q0,[x28, #0xf1] | `FALL_THROUGH`
<a id="insn-00bbdab8"></a> `00bbdab8` | `bf 1a 00 f9` | str xzr,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdabc"></a> `00bbdabc` | `a0 82 00 ad` | stp q0,q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdac0"></a> `00bbdac0` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bbdac4"></a> `00bbdac4` | `ff bb 00 f9` | str xzr,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbdac8"></a> `00bbdac8` | `e0 83 0a ad` | stp q0,q0,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbdacc"></a> `00bbdacc` | `e0 83 09 ad` | stp q0,q0,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbdad0"></a> `00bbdad0` | `e0 83 08 ad` | stp q0,q0,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bbdad4"></a> `00bbdad4` | `e0 83 07 ad` | stp q0,q0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bbdad8"></a> `00bbdad8` | `e0 83 06 ad` | stp q0,q0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bbdadc"></a> `00bbdadc` | `e0 83 05 ad` | stp q0,q0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbdae0"></a> `00bbdae0` | `e0 83 04 ad` | stp q0,q0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbdae4"></a> `00bbdae4` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbdae8"></a> `00bbdae8` | `e0 83 02 ad` | stp q0,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbdaec"></a> `00bbdaec` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbdaf0"></a> `00bbdaf0` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbdaf4"></a> `00bbdaf4` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbdaf8"></a> `00bbdaf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbdafc"></a> `00bbdafc` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bbdb00"></a> `00bbdb00` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00bbdb04"></a> `00bbdb04` | `28 01 40 79` | ldrh w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbdb08"></a> `00bbdb08` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbdb0c"></a> `00bbdb0c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdb10"></a> `00bbdb10` | `c3 00 00 54` | b.cc 0x00bbdb28 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb14"></a> `00bbdb14` | `28 09 40 79` | ldrh w8,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbdb18"></a> `00bbdb18` | `88 00 00 b4` | cbz x8,0x00bbdb28 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb1c"></a> `00bbdb1c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdb20"></a> `00bbdb20` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdb24"></a> `00bbdb24` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdb28"></a> `00bbdb28` | `5b b7 ff b0` | adrp x27,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbdb2c"></a> `00bbdb2c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdb30"></a> `00bbdb30` | `7b ab 0f 91` | add x27,x27,#0x3ea | `FALL_THROUGH`
<a id="insn-00bbdb34"></a> `00bbdb34` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdb38"></a> `00bbdb38` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdb3c"></a> `00bbdb3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdb40"></a> `00bbdb40` | `28 69 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb44"></a> `00bbdb44` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdb48"></a> `00bbdb48` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdb4c"></a> `00bbdb4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdb50"></a> `00bbdb50` | `58 75 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb54"></a> `00bbdb54` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdb58"></a> `00bbdb58` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdb5c"></a> `00bbdb5c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdb60"></a> `00bbdb60` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbdb64"></a> `00bbdb64` | `e3 00 00 54` | b.cc 0x00bbdb80 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb68"></a> `00bbdb68` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbdb6c"></a> `00bbdb6c` | `c8 00 00 b4` | cbz x8,0x00bbdb84 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb70"></a> `00bbdb70` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdb74"></a> `00bbdb74` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdb78"></a> `00bbdb78` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdb7c"></a> `00bbdb7c` | `02 00 00 14` | b 0x00bbdb84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdb80"></a> `00bbdb80` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdb84"></a> `00bbdb84` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdb88"></a> `00bbdb88` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdb8c"></a> `00bbdb8c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdb90"></a> `00bbdb90` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdb94"></a> `00bbdb94` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdb98"></a> `00bbdb98` | `17 61 00 91` | add x23,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbdb9c"></a> `00bbdb9c` | `11 69 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdba0"></a> `00bbdba0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdba4"></a> `00bbdba4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdba8"></a> `00bbdba8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdbac"></a> `00bbdbac` | `41 75 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdbb0"></a> `00bbdbb0` | `89 02 80 b9` | ldrsw x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbdbb4"></a> `00bbdbb4` | `8a 02 09 cb` | sub x10,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbdbb8"></a> `00bbdbb8` | `48 01 40 79` | ldrh w8,[x10] | `FALL_THROUGH`
<a id="insn-00bbdbbc"></a> `00bbdbbc` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bbdbc0"></a> `00bbdbc0` | `e8 03 09 cb` | neg x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdbc4"></a> `00bbdbc4` | `43 0d 00 54` | b.cc 0x00bbdd6c | `CONDITIONAL_JUMP`
<a id="insn-00bbdbc8"></a> `00bbdbc8` | `4a 15 40 79` | ldrh w10,[x10, #0xa] | `FALL_THROUGH`
<a id="insn-00bbdbcc"></a> `00bbdbcc` | `0a 0d 00 b4` | cbz x10,0x00bbdd6c | `CONDITIONAL_JUMP`
<a id="insn-00bbdbd0"></a> `00bbdbd0` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00bbdbd4"></a> `00bbdbd4` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdbd8"></a> `00bbdbd8` | `4a 01 0b ab` | adds x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbdbdc"></a> `00bbdbdc` | `80 0c 00 54` | b.eq 0x00bbdd6c | `CONDITIONAL_JUMP`
<a id="insn-00bbdbe0"></a> `00bbdbe0` | `4a 01 40 b9` | ldr w10,[x10] | `FALL_THROUGH`
<a id="insn-00bbdbe4"></a> `00bbdbe4` | `4a 0c 00 34` | cbz w10,0x00bbdd6c | `CONDITIONAL_JUMP`
<a id="insn-00bbdbe8"></a> `00bbdbe8` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdbec"></a> `00bbdbec` | `fa 67 00 a9` | stp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbdbf0"></a> `00bbdbf0` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bbdbf4"></a> `00bbdbf4` | `16 21 01 91` | add x22,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbdbf8"></a> `00bbdbf8` | `53 f5 7e d3` | lsl x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbdbfc"></a> `00bbdbfc` | `05 00 00 14` | b 0x00bbdc10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdc00"></a> `00bbdc00` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bbdc04"></a> `00bbdc04` | `5a 13 00 91` | add x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdc08"></a> `00bbdc08` | `7f 02 1a eb` | cmp x19,x26 | `FALL_THROUGH`
<a id="insn-00bbdc0c"></a> `00bbdc0c` | `a0 0a 00 54` | b.eq 0x00bbdd60 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc10"></a> `00bbdc10` | `88 c2 29 cb` | sub x8,x20,w9, SXTW  | `FALL_THROUGH`
<a id="insn-00bbdc14"></a> `00bbdc14` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbdc18"></a> `00bbdc18` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdc1c"></a> `00bbdc1c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdc20"></a> `00bbdc20` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc24"></a> `00bbdc24` | `49 77 7e 92` | and x9,x26,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00bbdc28"></a> `00bbdc28` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc2c"></a> `00bbdc2c` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbdc30"></a> `00bbdc30` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc34"></a> `00bbdc34` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdc38"></a> `00bbdc38` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc3c"></a> `00bbdc3c` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbdc40"></a> `00bbdc40` | `5f 15 00 71` | cmp w10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbdc44"></a> `00bbdc44` | `23 02 00 54` | b.cc 0x00bbdc88 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc48"></a> `00bbdc48` | `2b 09 40 79` | ldrh w11,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bbdc4c"></a> `00bbdc4c` | `8b 00 00 b4` | cbz x11,0x00bbdc5c | `CONDITIONAL_JUMP`
<a id="insn-00bbdc50"></a> `00bbdc50` | `0b 01 0b 8b` | add x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbdc54"></a> `00bbdc54` | `6c 01 40 b9` | ldr w12,[x11] | `FALL_THROUGH`
<a id="insn-00bbdc58"></a> `00bbdc58` | `6b 01 0c 8b` | add x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00bbdc5c"></a> `00bbdc5c` | `6c 11 00 91` | add x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdc60"></a> `00bbdc60` | `7f 01 00 f1` | cmp x11,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdc64"></a> `00bbdc64` | `61 03 8c 9a` | csel x1,x27,x12,eq | `FALL_THROUGH`
<a id="insn-00bbdc68"></a> `00bbdc68` | `5f 1d 00 71` | cmp w10,#0x7 | `FALL_THROUGH`
<a id="insn-00bbdc6c"></a> `00bbdc6c` | `43 01 00 54` | b.cc 0x00bbdc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc70"></a> `00bbdc70` | `29 0d 40 79` | ldrh w9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bbdc74"></a> `00bbdc74` | `09 01 00 b4` | cbz x9,0x00bbdc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbdc78"></a> `00bbdc78` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc7c"></a> `00bbdc7c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdc80"></a> `00bbdc80` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdc84"></a> `00bbdc84` | `05 00 00 14` | b 0x00bbdc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdc88"></a> `00bbdc88` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdc8c"></a> `00bbdc8c` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00bbdc90"></a> `00bbdc90` | `02 00 00 14` | b 0x00bbdc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdc94"></a> `00bbdc94` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdc98"></a> `00bbdc98` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdc9c"></a> `00bbdc9c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdca0"></a> `00bbdca0` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdca4"></a> `00bbdca4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdca8"></a> `00bbdca8` | `46 76 02 94` | bl 0x00c5b5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdcac"></a> `00bbdcac` | `a1 c3 01 d1` | sub x1,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bbdcb0"></a> `00bbdcb0` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdcb4"></a> `00bbdcb4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdcb8"></a> `00bbdcb8` | `3c be e2 97` | bl 0x0046d5a8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdcbc"></a> `00bbdcbc` | `18 00 40 f9` | ldr x24,[x0] | `FALL_THROUGH`
<a id="insn-00bbdcc0"></a> `00bbdcc0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bbdcc4"></a> `00bbdcc4` | `78 03 00 b5` | cbnz x24,0x00bbdd30 | `CONDITIONAL_JUMP`
<a id="insn-00bbdcc8"></a> `00bbdcc8` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bbdccc"></a> `00bbdccc` | `71 68 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdcd0"></a> `00bbdcd0` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdcd4"></a> `00bbdcd4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdcd8"></a> `00bbdcd8` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbdcdc"></a> `00bbdcdc` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbdce0"></a> `00bbdce0` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdce4"></a> `00bbdce4` | `1f 7c 04 a9` | stp xzr,xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bbdce8"></a> `00bbdce8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbdcec"></a> `00bbdcec` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdcf0"></a> `00bbdcf0` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdcf4"></a> `00bbdcf4` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdcf8"></a> `00bbdcf8` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00bbdcfc"></a> `00bbdcfc` | `e8 e7 40 f9` | ldr x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbdd00"></a> `00bbdd00` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbdd04"></a> `00bbdd04` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd08"></a> `00bbdd08` | `88 00 00 b4` | cbz x8,0x00bbdd18 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd0c"></a> `00bbdd0c` | `e8 e7 00 f9` | str x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00bbdd10"></a> `00bbdd10` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00bbdd14"></a> `00bbdd14` | `02 00 00 14` | b 0x00bbdd1c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdd18"></a> `00bbdd18` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bbdd1c"></a> `00bbdd1c` | `e0 eb 40 f9` | ldr x0,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bbdd20"></a> `00bbdd20` | `30 76 02 94` | bl 0x00c5b5e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd24"></a> `00bbdd24` | `e8 ef 40 f9` | ldr x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbdd28"></a> `00bbdd28` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdd2c"></a> `00bbdd2c` | `e8 ef 00 f9` | str x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00bbdd30"></a> `00bbdd30` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdd34"></a> `00bbdd34` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-00bbdd38"></a> `00bbdd38` | `aa 68 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd3c"></a> `00bbdd3c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdd40"></a> `00bbdd40` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbdd44"></a> `00bbdd44` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbdd48"></a> `00bbdd48` | `da 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd4c"></a> `00bbdd4c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdd50"></a> `00bbdd50` | `88 f5 07 36` | tbz w8,#0x0,0x00bbdc00 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd54"></a> `00bbdd54` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdd58"></a> `00bbdd58` | `56 68 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdd5c"></a> `00bbdd5c` | `a9 ff ff 17` | b 0x00bbdc00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdd60"></a> `00bbdd60` | `fa 67 40 a9` | ldp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00bbdd64"></a> `00bbdd64` | `28 7d 40 93` | sxtw x8,w9 | `FALL_THROUGH`
<a id="insn-00bbdd68"></a> `00bbdd68` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbdd6c"></a> `00bbdd6c` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdd70"></a> `00bbdd70` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbdd74"></a> `00bbdd74` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00bbdd78"></a> `00bbdd78` | `43 06 00 54` | b.cc 0x00bbde40 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd7c"></a> `00bbdd7c` | `29 19 40 79` | ldrh w9,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00bbdd80"></a> `00bbdd80` | `09 06 00 b4` | cbz x9,0x00bbde40 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd84"></a> `00bbdd84` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00bbdd88"></a> `00bbdd88` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbdd8c"></a> `00bbdd8c` | `29 01 0a ab` | adds x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdd90"></a> `00bbdd90` | `80 05 00 54` | b.eq 0x00bbde40 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd94"></a> `00bbdd94` | `e8 fb 40 f9` | ldr x8,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbdd98"></a> `00bbdd98` | `f6 f3 40 f9` | ldr x22,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbdd9c"></a> `00bbdd9c` | `37 01 40 b9` | ldr w23,[x9] | `FALL_THROUGH`
<a id="insn-00bbdda0"></a> `00bbdda0` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00bbdda4"></a> `00bbdda4` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bbdda8"></a> `00bbdda8` | `42 02 00 54` | b.cs 0x00bbddf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbddac"></a> `00bbddac` | `f3 f7 40 f9` | ldr x19,[sp, #0x1e8] | `FALL_THROUGH`
<a id="insn-00bbddb0"></a> `00bbddb0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbddb4"></a> `00bbddb4` | `37 68 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddb8"></a> `00bbddb8` | `62 02 16 cb` | sub x2,x19,x22 | `FALL_THROUGH`
<a id="insn-00bbddbc"></a> `00bbddbc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbddc0"></a> `00bbddc0` | `13 00 02 8b` | add x19,x0,x2 | `FALL_THROUGH`
<a id="insn-00bbddc4"></a> `00bbddc4` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-00bbddc8"></a> `00bbddc8` | `17 00 17 8b` | add x23,x0,x23 | `FALL_THROUGH`
<a id="insn-00bbddcc"></a> `00bbddcc` | `8b 00 00 54` | b.lt 0x00bbdddc | `CONDITIONAL_JUMP`
<a id="insn-00bbddd0"></a> `00bbddd0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbddd4"></a> `00bbddd4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbddd8"></a> `00bbddd8` | `8a 68 02 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdddc"></a> `00bbdddc` | `f8 4f 1e a9` | stp x24,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bbdde0"></a> `00bbdde0` | `f7 fb 00 f9` | str x23,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bbdde4"></a> `00bbdde4` | `76 00 00 b4` | cbz x22,0x00bbddf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdde8"></a> `00bbdde8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbddec"></a> `00bbddec` | `31 68 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbddf0"></a> `00bbddf0` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbddf4"></a> `00bbddf4` | `80 83 01 91` | add x0,x28,#0x60 | `FALL_THROUGH`
<a id="insn-00bbddf8"></a> `00bbddf8` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbddfc"></a> `00bbddfc` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbde00"></a> `00bbde00` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbde04"></a> `00bbde04` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbde08"></a> `00bbde08` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbde0c"></a> `00bbde0c` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bbde10"></a> `00bbde10` | `e8 03 89 9a` | csel x8,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-00bbde14"></a> `00bbde14` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbde18"></a> `00bbde18` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbde1c"></a> `00bbde1c` | `28 01 40 b9` | ldr w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbde20"></a> `00bbde20` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbde24"></a> `00bbde24` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbde28"></a> `00bbde28` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbde2c"></a> `00bbde2c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbde30"></a> `00bbde30` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbde34"></a> `00bbde34` | `cf 7d 02 94` | bl 0x00c5d570 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde38"></a> `00bbde38` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbde3c"></a> `00bbde3c` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00bbde40"></a> `00bbde40` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbde44"></a> `00bbde44` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbde48"></a> `00bbde48` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbde4c"></a> `00bbde4c` | `e3 00 00 54` | b.cc 0x00bbde68 | `CONDITIONAL_JUMP`
<a id="insn-00bbde50"></a> `00bbde50` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbde54"></a> `00bbde54` | `c8 00 00 b4` | cbz x8,0x00bbde6c | `CONDITIONAL_JUMP`
<a id="insn-00bbde58"></a> `00bbde58` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbde5c"></a> `00bbde5c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbde60"></a> `00bbde60` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbde64"></a> `00bbde64` | `02 00 00 14` | b 0x00bbde6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbde68"></a> `00bbde68` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbde6c"></a> `00bbde6c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbde70"></a> `00bbde70` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbde74"></a> `00bbde74` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbde78"></a> `00bbde78` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbde7c"></a> `00bbde7c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbde80"></a> `00bbde80` | `17 e1 01 91` | add x23,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbde84"></a> `00bbde84` | `57 68 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde88"></a> `00bbde88` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbde8c"></a> `00bbde8c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbde90"></a> `00bbde90` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbde94"></a> `00bbde94` | `87 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbde98"></a> `00bbde98` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbde9c"></a> `00bbde9c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdea0"></a> `00bbdea0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdea4"></a> `00bbdea4` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbdea8"></a> `00bbdea8` | `e3 00 00 54` | b.cc 0x00bbdec4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdeac"></a> `00bbdeac` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdeb0"></a> `00bbdeb0` | `c8 00 00 b4` | cbz x8,0x00bbdec8 | `CONDITIONAL_JUMP`
<a id="insn-00bbdeb4"></a> `00bbdeb4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdeb8"></a> `00bbdeb8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdebc"></a> `00bbdebc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdec0"></a> `00bbdec0` | `02 00 00 14` | b 0x00bbdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdec4"></a> `00bbdec4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdec8"></a> `00bbdec8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdecc"></a> `00bbdecc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbded0"></a> `00bbded0` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbded4"></a> `00bbded4` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbded8"></a> `00bbded8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdedc"></a> `00bbdedc` | `17 41 02 91` | add x23,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbdee0"></a> `00bbdee0` | `40 68 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdee4"></a> `00bbdee4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdee8"></a> `00bbdee8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdeec"></a> `00bbdeec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdef0"></a> `00bbdef0` | `70 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdef4"></a> `00bbdef4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdef8"></a> `00bbdef8` | `96 23 03 91` | add x22,x28,#0xc8 | `FALL_THROUGH`
<a id="insn-00bbdefc"></a> `00bbdefc` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf00"></a> `00bbdf00` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf04"></a> `00bbdf04` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbdf08"></a> `00bbdf08` | `e3 00 00 54` | b.cc 0x00bbdf24 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf0c"></a> `00bbdf0c` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbdf10"></a> `00bbdf10` | `c8 00 00 b4` | cbz x8,0x00bbdf28 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf14"></a> `00bbdf14` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf18"></a> `00bbdf18` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf1c"></a> `00bbdf1c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdf20"></a> `00bbdf20` | `02 00 00 14` | b 0x00bbdf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdf24"></a> `00bbdf24` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdf28"></a> `00bbdf28` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdf2c"></a> `00bbdf2c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdf30"></a> `00bbdf30` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf34"></a> `00bbdf34` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdf38"></a> `00bbdf38` | `2a 68 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf3c"></a> `00bbdf3c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdf40"></a> `00bbdf40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdf44"></a> `00bbdf44` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbdf48"></a> `00bbdf48` | `5a 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf4c"></a> `00bbdf4c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdf50"></a> `00bbdf50` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf54"></a> `00bbdf54` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf58"></a> `00bbdf58` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbdf5c"></a> `00bbdf5c` | `e3 00 00 54` | b.cc 0x00bbdf78 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf60"></a> `00bbdf60` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdf64"></a> `00bbdf64` | `c8 00 00 b4` | cbz x8,0x00bbdf7c | `CONDITIONAL_JUMP`
<a id="insn-00bbdf68"></a> `00bbdf68` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdf6c"></a> `00bbdf6c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdf70"></a> `00bbdf70` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdf74"></a> `00bbdf74` | `02 00 00 14` | b 0x00bbdf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdf78"></a> `00bbdf78` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdf7c"></a> `00bbdf7c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbdf80"></a> `00bbdf80` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdf84"></a> `00bbdf84` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbdf88"></a> `00bbdf88` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbdf8c"></a> `00bbdf8c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdf90"></a> `00bbdf90` | `17 81 03 91` | add x23,x8,#0xe0 | `FALL_THROUGH`
<a id="insn-00bbdf94"></a> `00bbdf94` | `13 68 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf98"></a> `00bbdf98` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbdf9c"></a> `00bbdf9c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdfa0"></a> `00bbdfa0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbdfa4"></a> `00bbdfa4` | `43 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdfa8"></a> `00bbdfa8` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbdfac"></a> `00bbdfac` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdfb0"></a> `00bbdfb0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdfb4"></a> `00bbdfb4` | `3f 71 00 71` | cmp w9,#0x1c | `FALL_THROUGH`
<a id="insn-00bbdfb8"></a> `00bbdfb8` | `e9 01 00 54` | b.ls 0x00bbdff4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfbc"></a> `00bbdfbc` | `0a 39 40 79` | ldrh w10,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbdfc0"></a> `00bbdfc0` | `8a 00 00 b4` | cbz x10,0x00bbdfd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfc4"></a> `00bbdfc4` | `8a 6a 6a 38` | ldrb w10,[x20, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00bbdfc8"></a> `00bbdfc8` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00bbdfcc"></a> `00bbdfcc` | `ea 07 9f 1a` | cset w10,ne | `FALL_THROUGH`
<a id="insn-00bbdfd0"></a> `00bbdfd0` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00bbdfd4"></a> `00bbdfd4` | `ea 03 0a 39` | strb w10,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbdfd8"></a> `00bbdfd8` | `43 01 00 54` | b.cc 0x00bbe000 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfdc"></a> `00bbdfdc` | `08 3d 40 79` | ldrh w8,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00bbdfe0"></a> `00bbdfe0` | `28 01 00 b4` | cbz x8,0x00bbe004 | `CONDITIONAL_JUMP`
<a id="insn-00bbdfe4"></a> `00bbdfe4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdfe8"></a> `00bbdfe8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbdfec"></a> `00bbdfec` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdff0"></a> `00bbdff0` | `05 00 00 14` | b 0x00bbe004 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdff4"></a> `00bbdff4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdff8"></a> `00bbdff8` | `ff 03 0a 39` | strb wzr,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00bbdffc"></a> `00bbdffc` | `02 00 00 14` | b 0x00bbe004 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe000"></a> `00bbe000` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe004"></a> `00bbe004` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe008"></a> `00bbe008` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe00c"></a> `00bbe00c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe010"></a> `00bbe010` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe014"></a> `00bbe014` | `f3 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe018"></a> `00bbe018` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe01c"></a> `00bbe01c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe020"></a> `00bbe020` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbe024"></a> `00bbe024` | `23 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe028"></a> `00bbe028` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe02c"></a> `00bbe02c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe030"></a> `00bbe030` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe034"></a> `00bbe034` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbe038"></a> `00bbe038` | `e3 00 00 54` | b.cc 0x00bbe054 | `CONDITIONAL_JUMP`
<a id="insn-00bbe03c"></a> `00bbe03c` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe040"></a> `00bbe040` | `c8 00 00 b4` | cbz x8,0x00bbe058 | `CONDITIONAL_JUMP`
<a id="insn-00bbe044"></a> `00bbe044` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe048"></a> `00bbe048` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe04c"></a> `00bbe04c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe050"></a> `00bbe050` | `02 00 00 14` | b 0x00bbe058 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe054"></a> `00bbe054` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe058"></a> `00bbe058` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe05c"></a> `00bbe05c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe060"></a> `00bbe060` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe064"></a> `00bbe064` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe068"></a> `00bbe068` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe06c"></a> `00bbe06c` | `16 c1 00 91` | add x22,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe070"></a> `00bbe070` | `dc 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe074"></a> `00bbe074` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe078"></a> `00bbe078` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe07c"></a> `00bbe07c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe080"></a> `00bbe080` | `0c 74 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe084"></a> `00bbe084` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe088"></a> `00bbe088` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe08c"></a> `00bbe08c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe090"></a> `00bbe090` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbe094"></a> `00bbe094` | `e3 00 00 54` | b.cc 0x00bbe0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe098"></a> `00bbe098` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbe09c"></a> `00bbe09c` | `c8 00 00 b4` | cbz x8,0x00bbe0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe0a0"></a> `00bbe0a0` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe0a4"></a> `00bbe0a4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe0a8"></a> `00bbe0a8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe0ac"></a> `00bbe0ac` | `02 00 00 14` | b 0x00bbe0b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe0b0"></a> `00bbe0b0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe0b4"></a> `00bbe0b4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe0b8"></a> `00bbe0b8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe0bc"></a> `00bbe0bc` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe0c0"></a> `00bbe0c0` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe0c4"></a> `00bbe0c4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe0c8"></a> `00bbe0c8` | `16 a1 02 91` | add x22,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbe0cc"></a> `00bbe0cc` | `c5 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe0d0"></a> `00bbe0d0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe0d4"></a> `00bbe0d4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe0d8"></a> `00bbe0d8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe0dc"></a> `00bbe0dc` | `f5 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe0e0"></a> `00bbe0e0` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe0e4"></a> `00bbe0e4` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe0e8"></a> `00bbe0e8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe0ec"></a> `00bbe0ec` | `3f 8d 00 71` | cmp w9,#0x23 | `FALL_THROUGH`
<a id="insn-00bbe0f0"></a> `00bbe0f0` | `e3 00 00 54` | b.cc 0x00bbe10c | `CONDITIONAL_JUMP`
<a id="insn-00bbe0f4"></a> `00bbe0f4` | `08 45 40 79` | ldrh w8,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00bbe0f8"></a> `00bbe0f8` | `c8 00 00 b4` | cbz x8,0x00bbe110 | `CONDITIONAL_JUMP`
<a id="insn-00bbe0fc"></a> `00bbe0fc` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe100"></a> `00bbe100` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe104"></a> `00bbe104` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe108"></a> `00bbe108` | `02 00 00 14` | b 0x00bbe110 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe10c"></a> `00bbe10c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe110"></a> `00bbe110` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe114"></a> `00bbe114` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe118"></a> `00bbe118` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe11c"></a> `00bbe11c` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe120"></a> `00bbe120` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe124"></a> `00bbe124` | `16 81 04 91` | add x22,x8,#0x120 | `FALL_THROUGH`
<a id="insn-00bbe128"></a> `00bbe128` | `ae 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe12c"></a> `00bbe12c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe130"></a> `00bbe130` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe134"></a> `00bbe134` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe138"></a> `00bbe138` | `de 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe13c"></a> `00bbe13c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbe140"></a> `00bbe140` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe144"></a> `00bbe144` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe148"></a> `00bbe148` | `3f 85 00 71` | cmp w9,#0x21 | `FALL_THROUGH`
<a id="insn-00bbe14c"></a> `00bbe14c` | `03 01 00 54` | b.cc 0x00bbe16c | `CONDITIONAL_JUMP`
<a id="insn-00bbe150"></a> `00bbe150` | `0a 41 40 79` | ldrh w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe154"></a> `00bbe154` | `4a 00 00 b4` | cbz x10,0x00bbe15c | `CONDITIONAL_JUMP`
<a id="insn-00bbe158"></a> `00bbe158` | `8a 6a 6a f8` | ldr x10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe15c"></a> `00bbe15c` | `ea 5f 01 f9` | str x10,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbe160"></a> `00bbe160` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe164"></a> `00bbe164` | `ea 00 00 b5` | cbnz x10,0x00bbe180 | `CONDITIONAL_JUMP`
<a id="insn-00bbe168"></a> `00bbe168` | `07 00 00 14` | b 0x00bbe184 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe16c"></a> `00bbe16c` | `3f 51 00 71` | cmp w9,#0x14 | `FALL_THROUGH`
<a id="insn-00bbe170"></a> `00bbe170` | `ff 5f 01 f9` | str xzr,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00bbe174"></a> `00bbe174` | `09 03 00 54` | b.ls 0x00bbe1d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe178"></a> `00bbe178` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe17c"></a> `00bbe17c` | `4a 00 00 b4` | cbz x10,0x00bbe184 | `CONDITIONAL_JUMP`
<a id="insn-00bbe180"></a> `00bbe180` | `8a 6a 6a b8` | ldr w10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe184"></a> `00bbe184` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe188"></a> `00bbe188` | `ea 43 02 b9` | str w10,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbe18c"></a> `00bbe18c` | `83 32 00 54` | b.cc 0x00bbe7dc | `CONDITIONAL_JUMP`
<a id="insn-00bbe190"></a> `00bbe190` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe194"></a> `00bbe194` | `48 32 00 b4` | cbz x8,0x00bbe7dc | `CONDITIONAL_JUMP`
<a id="insn-00bbe198"></a> `00bbe198` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe19c"></a> `00bbe19c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe1a0"></a> `00bbe1a0` | `16 01 09 ab` | adds x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe1a4"></a> `00bbe1a4` | `c0 31 00 54` | b.eq 0x00bbe7dc | `CONDITIONAL_JUMP`
<a id="insn-00bbe1a8"></a> `00bbe1a8` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe1ac"></a> `00bbe1ac` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe1b0"></a> `00bbe1b0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe1b4"></a> `00bbe1b4` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bbe1b8"></a> `00bbe1b8` | `23 01 00 54` | b.cc 0x00bbe1dc | `CONDITIONAL_JUMP`
<a id="insn-00bbe1bc"></a> `00bbe1bc` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbe1c0"></a> `00bbe1c0` | `08 01 00 b4` | cbz x8,0x00bbe1e0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe1c4"></a> `00bbe1c4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe1c8"></a> `00bbe1c8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe1cc"></a> `00bbe1cc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe1d0"></a> `00bbe1d0` | `04 00 00 14` | b 0x00bbe1e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe1d4"></a> `00bbe1d4` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00bbe1d8"></a> `00bbe1d8` | `81 01 00 14` | b 0x00bbe7dc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe1dc"></a> `00bbe1dc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe1e0"></a> `00bbe1e0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe1e4"></a> `00bbe1e4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe1e8"></a> `00bbe1e8` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe1ec"></a> `00bbe1ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe1f0"></a> `00bbe1f0` | `7c 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe1f4"></a> `00bbe1f4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe1f8"></a> `00bbe1f8` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe1fc"></a> `00bbe1fc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe200"></a> `00bbe200` | `ac 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe204"></a> `00bbe204` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe208"></a> `00bbe208` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe20c"></a> `00bbe20c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe210"></a> `00bbe210` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbe214"></a> `00bbe214` | `e3 00 00 54` | b.cc 0x00bbe230 | `CONDITIONAL_JUMP`
<a id="insn-00bbe218"></a> `00bbe218` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00bbe21c"></a> `00bbe21c` | `c8 00 00 b4` | cbz x8,0x00bbe234 | `CONDITIONAL_JUMP`
<a id="insn-00bbe220"></a> `00bbe220` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe224"></a> `00bbe224` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe228"></a> `00bbe228` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe22c"></a> `00bbe22c` | `02 00 00 14` | b 0x00bbe234 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe230"></a> `00bbe230` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe234"></a> `00bbe234` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe238"></a> `00bbe238` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe23c"></a> `00bbe23c` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe240"></a> `00bbe240` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe244"></a> `00bbe244` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe248"></a> `00bbe248` | `15 61 00 91` | add x21,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe24c"></a> `00bbe24c` | `65 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe250"></a> `00bbe250` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe254"></a> `00bbe254` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe258"></a> `00bbe258` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe25c"></a> `00bbe25c` | `95 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe260"></a> `00bbe260` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe264"></a> `00bbe264` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe268"></a> `00bbe268` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe26c"></a> `00bbe26c` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00bbe270"></a> `00bbe270` | `e3 00 00 54` | b.cc 0x00bbe28c | `CONDITIONAL_JUMP`
<a id="insn-00bbe274"></a> `00bbe274` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe278"></a> `00bbe278` | `c8 00 00 b4` | cbz x8,0x00bbe290 | `CONDITIONAL_JUMP`
<a id="insn-00bbe27c"></a> `00bbe27c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe280"></a> `00bbe280` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe284"></a> `00bbe284` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe288"></a> `00bbe288` | `02 00 00 14` | b 0x00bbe290 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe28c"></a> `00bbe28c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe290"></a> `00bbe290` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe294"></a> `00bbe294` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe298"></a> `00bbe298` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe29c"></a> `00bbe29c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe2a0"></a> `00bbe2a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe2a4"></a> `00bbe2a4` | `15 c1 00 91` | add x21,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe2a8"></a> `00bbe2a8` | `4e 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2ac"></a> `00bbe2ac` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe2b0"></a> `00bbe2b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe2b4"></a> `00bbe2b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe2b8"></a> `00bbe2b8` | `7e 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2bc"></a> `00bbe2bc` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe2c0"></a> `00bbe2c0` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe2c4"></a> `00bbe2c4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe2c8"></a> `00bbe2c8` | `3f 2d 00 71` | cmp w9,#0xb | `FALL_THROUGH`
<a id="insn-00bbe2cc"></a> `00bbe2cc` | `e3 00 00 54` | b.cc 0x00bbe2e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe2d0"></a> `00bbe2d0` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bbe2d4"></a> `00bbe2d4` | `c8 00 00 b4` | cbz x8,0x00bbe2ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe2d8"></a> `00bbe2d8` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe2dc"></a> `00bbe2dc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe2e0"></a> `00bbe2e0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe2e4"></a> `00bbe2e4` | `02 00 00 14` | b 0x00bbe2ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe2e8"></a> `00bbe2e8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe2ec"></a> `00bbe2ec` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe2f0"></a> `00bbe2f0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe2f4"></a> `00bbe2f4` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe2f8"></a> `00bbe2f8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe2fc"></a> `00bbe2fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe300"></a> `00bbe300` | `15 21 01 91` | add x21,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbe304"></a> `00bbe304` | `37 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe308"></a> `00bbe308` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe30c"></a> `00bbe30c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe310"></a> `00bbe310` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe314"></a> `00bbe314` | `67 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe318"></a> `00bbe318` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe31c"></a> `00bbe31c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe320"></a> `00bbe320` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe324"></a> `00bbe324` | `3f 35 00 71` | cmp w9,#0xd | `FALL_THROUGH`
<a id="insn-00bbe328"></a> `00bbe328` | `e3 00 00 54` | b.cc 0x00bbe344 | `CONDITIONAL_JUMP`
<a id="insn-00bbe32c"></a> `00bbe32c` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00bbe330"></a> `00bbe330` | `c8 00 00 b4` | cbz x8,0x00bbe348 | `CONDITIONAL_JUMP`
<a id="insn-00bbe334"></a> `00bbe334` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe338"></a> `00bbe338` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe33c"></a> `00bbe33c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe340"></a> `00bbe340` | `02 00 00 14` | b 0x00bbe348 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe344"></a> `00bbe344` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe348"></a> `00bbe348` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe34c"></a> `00bbe34c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe350"></a> `00bbe350` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe354"></a> `00bbe354` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe358"></a> `00bbe358` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe35c"></a> `00bbe35c` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbe360"></a> `00bbe360` | `20 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe364"></a> `00bbe364` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe368"></a> `00bbe368` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe36c"></a> `00bbe36c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe370"></a> `00bbe370` | `50 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe374"></a> `00bbe374` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe378"></a> `00bbe378` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe37c"></a> `00bbe37c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe380"></a> `00bbe380` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00bbe384"></a> `00bbe384` | `e3 00 00 54` | b.cc 0x00bbe3a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe388"></a> `00bbe388` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00bbe38c"></a> `00bbe38c` | `c8 00 00 b4` | cbz x8,0x00bbe3a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe390"></a> `00bbe390` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe394"></a> `00bbe394` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe398"></a> `00bbe398` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe39c"></a> `00bbe39c` | `02 00 00 14` | b 0x00bbe3a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe3a0"></a> `00bbe3a0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe3a4"></a> `00bbe3a4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe3a8"></a> `00bbe3a8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe3ac"></a> `00bbe3ac` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe3b0"></a> `00bbe3b0` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe3b4"></a> `00bbe3b4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe3b8"></a> `00bbe3b8` | `15 e1 01 91` | add x21,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00bbe3bc"></a> `00bbe3bc` | `09 67 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe3c0"></a> `00bbe3c0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe3c4"></a> `00bbe3c4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe3c8"></a> `00bbe3c8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe3cc"></a> `00bbe3cc` | `39 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe3d0"></a> `00bbe3d0` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe3d4"></a> `00bbe3d4` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe3d8"></a> `00bbe3d8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe3dc"></a> `00bbe3dc` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00bbe3e0"></a> `00bbe3e0` | `e3 00 00 54` | b.cc 0x00bbe3fc | `CONDITIONAL_JUMP`
<a id="insn-00bbe3e4"></a> `00bbe3e4` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe3e8"></a> `00bbe3e8` | `c8 00 00 b4` | cbz x8,0x00bbe400 | `CONDITIONAL_JUMP`
<a id="insn-00bbe3ec"></a> `00bbe3ec` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe3f0"></a> `00bbe3f0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe3f4"></a> `00bbe3f4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe3f8"></a> `00bbe3f8` | `02 00 00 14` | b 0x00bbe400 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe3fc"></a> `00bbe3fc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe400"></a> `00bbe400` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe404"></a> `00bbe404` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe408"></a> `00bbe408` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe40c"></a> `00bbe40c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe410"></a> `00bbe410` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe414"></a> `00bbe414` | `15 41 02 91` | add x21,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00bbe418"></a> `00bbe418` | `f2 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe41c"></a> `00bbe41c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe420"></a> `00bbe420` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe424"></a> `00bbe424` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe428"></a> `00bbe428` | `22 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe42c"></a> `00bbe42c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe430"></a> `00bbe430` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe434"></a> `00bbe434` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe438"></a> `00bbe438` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00bbe43c"></a> `00bbe43c` | `e3 00 00 54` | b.cc 0x00bbe458 | `CONDITIONAL_JUMP`
<a id="insn-00bbe440"></a> `00bbe440` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00bbe444"></a> `00bbe444` | `c8 00 00 b4` | cbz x8,0x00bbe45c | `CONDITIONAL_JUMP`
<a id="insn-00bbe448"></a> `00bbe448` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe44c"></a> `00bbe44c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe450"></a> `00bbe450` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe454"></a> `00bbe454` | `02 00 00 14` | b 0x00bbe45c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe458"></a> `00bbe458` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe45c"></a> `00bbe45c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe460"></a> `00bbe460` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe464"></a> `00bbe464` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe468"></a> `00bbe468` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe46c"></a> `00bbe46c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe470"></a> `00bbe470` | `15 a1 02 91` | add x21,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00bbe474"></a> `00bbe474` | `db 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe478"></a> `00bbe478` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe47c"></a> `00bbe47c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe480"></a> `00bbe480` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe484"></a> `00bbe484` | `0b 73 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe488"></a> `00bbe488` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe48c"></a> `00bbe48c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe490"></a> `00bbe490` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe494"></a> `00bbe494` | `3f 55 00 71` | cmp w9,#0x15 | `FALL_THROUGH`
<a id="insn-00bbe498"></a> `00bbe498` | `e3 00 00 54` | b.cc 0x00bbe4b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe49c"></a> `00bbe49c` | `08 29 40 79` | ldrh w8,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00bbe4a0"></a> `00bbe4a0` | `c8 00 00 b4` | cbz x8,0x00bbe4b8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4a4"></a> `00bbe4a4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe4a8"></a> `00bbe4a8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe4ac"></a> `00bbe4ac` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe4b0"></a> `00bbe4b0` | `02 00 00 14` | b 0x00bbe4b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe4b4"></a> `00bbe4b4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe4b8"></a> `00bbe4b8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe4bc"></a> `00bbe4bc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe4c0"></a> `00bbe4c0` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe4c4"></a> `00bbe4c4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe4c8"></a> `00bbe4c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe4cc"></a> `00bbe4cc` | `15 01 03 91` | add x21,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bbe4d0"></a> `00bbe4d0` | `c4 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe4d4"></a> `00bbe4d4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe4d8"></a> `00bbe4d8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe4dc"></a> `00bbe4dc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe4e0"></a> `00bbe4e0` | `f4 72 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe4e4"></a> `00bbe4e4` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe4e8"></a> `00bbe4e8` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe4ec"></a> `00bbe4ec` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe4f0"></a> `00bbe4f0` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbe4f4"></a> `00bbe4f4` | `63 08 00 54` | b.cc 0x00bbe600 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4f8"></a> `00bbe4f8` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbe4fc"></a> `00bbe4fc` | `28 08 00 b4` | cbz x8,0x00bbe600 | `CONDITIONAL_JUMP`
<a id="insn-00bbe500"></a> `00bbe500` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe504"></a> `00bbe504` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbe508"></a> `00bbe508` | `e9 a3 52 a9` | ldp x9,x8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe50c"></a> `00bbe50c` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe510"></a> `00bbe510` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe514"></a> `00bbe514` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbe518"></a> `00bbe518` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe51c"></a> `00bbe51c` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbe520"></a> `00bbe520` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbe524"></a> `00bbe524` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbe528"></a> `00bbe528` | `c2 00 00 54` | b.cs 0x00bbe540 | `CONDITIONAL_JUMP`
<a id="insn-00bbe52c"></a> `00bbe52c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe530"></a> `00bbe530` | `00 61 03 91` | add x0,x8,#0xd8 | `FALL_THROUGH`
<a id="insn-00bbe534"></a> `00bbe534` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbe538"></a> `00bbe538` | `0a 7c 02 94` | bl 0x00c5d560 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe53c"></a> `00bbe53c` | `12 00 00 14` | b 0x00bbe584 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe540"></a> `00bbe540` | `29 02 00 54` | b.ls 0x00bbe584 | `CONDITIONAL_JUMP`
<a id="insn-00bbe544"></a> `00bbe544` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe548"></a> `00bbe548` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbe54c"></a> `00bbe54c` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe550"></a> `00bbe550` | `80 01 00 54` | b.eq 0x00bbe580 | `CONDITIONAL_JUMP`
<a id="insn-00bbe554"></a> `00bbe554` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbe558"></a> `00bbe558` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe55c"></a> `00bbe55c` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbe574 | `CONDITIONAL_JUMP`
<a id="insn-00bbe560"></a> `00bbe560` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbe564"></a> `00bbe564` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbe568"></a> `00bbe568` | `c0 00 00 54` | b.eq 0x00bbe580 | `CONDITIONAL_JUMP`
<a id="insn-00bbe56c"></a> `00bbe56c` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe570"></a> `00bbe570` | `89 ff 07 36` | tbz w9,#0x0,0x00bbe560 | `CONDITIONAL_JUMP`
<a id="insn-00bbe574"></a> `00bbe574` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbe578"></a> `00bbe578` | `4e 66 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe57c"></a> `00bbe57c` | `f9 ff ff 17` | b 0x00bbe560 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe580"></a> `00bbe580` | `f4 9b 00 f9` | str x20,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbe584"></a> `00bbe584` | `f3 03 00 34` | cbz w19,0x00bbe600 | `CONDITIONAL_JUMP`
<a id="insn-00bbe588"></a> `00bbe588` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbe58c"></a> `00bbe58c` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe590"></a> `00bbe590` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe594"></a> `00bbe594` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe598"></a> `00bbe598` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe59c"></a> `00bbe59c` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00bbe5a0"></a> `00bbe5a0` | `e3 00 00 54` | b.cc 0x00bbe5bc | `CONDITIONAL_JUMP`
<a id="insn-00bbe5a4"></a> `00bbe5a4` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00bbe5a8"></a> `00bbe5a8` | `c8 00 00 b4` | cbz x8,0x00bbe5c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe5ac"></a> `00bbe5ac` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe5b0"></a> `00bbe5b0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe5b4"></a> `00bbe5b4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe5b8"></a> `00bbe5b8` | `02 00 00 14` | b 0x00bbe5c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe5bc"></a> `00bbe5bc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe5c0"></a> `00bbe5c0` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe5c4"></a> `00bbe5c4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe5c8"></a> `00bbe5c8` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbe5cc"></a> `00bbe5cc` | `ea 97 40 f9` | ldr x10,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe5d0"></a> `00bbe5d0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe5d4"></a> `00bbe5d4` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe5d8"></a> `00bbe5d8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe5dc"></a> `00bbe5dc` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbe5e0"></a> `00bbe5e0` | `80 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe5e4"></a> `00bbe5e4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe5e8"></a> `00bbe5e8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe5ec"></a> `00bbe5ec` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe5f0"></a> `00bbe5f0` | `b0 72 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe5f4"></a> `00bbe5f4` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe5f8"></a> `00bbe5f8` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbe5fc"></a> `00bbe5fc` | `a1 fc ff 54` | b.ne 0x00bbe590 | `CONDITIONAL_JUMP`
<a id="insn-00bbe600"></a> `00bbe600` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe604"></a> `00bbe604` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe608"></a> `00bbe608` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe60c"></a> `00bbe60c` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00bbe610"></a> `00bbe610` | `e3 00 00 54` | b.cc 0x00bbe62c | `CONDITIONAL_JUMP`
<a id="insn-00bbe614"></a> `00bbe614` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe618"></a> `00bbe618` | `c8 00 00 b4` | cbz x8,0x00bbe630 | `CONDITIONAL_JUMP`
<a id="insn-00bbe61c"></a> `00bbe61c` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe620"></a> `00bbe620` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe624"></a> `00bbe624` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe628"></a> `00bbe628` | `02 00 00 14` | b 0x00bbe630 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe62c"></a> `00bbe62c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe630"></a> `00bbe630` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe634"></a> `00bbe634` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe638"></a> `00bbe638` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe63c"></a> `00bbe63c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe640"></a> `00bbe640` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe644"></a> `00bbe644` | `15 c1 03 91` | add x21,x8,#0xf0 | `FALL_THROUGH`
<a id="insn-00bbe648"></a> `00bbe648` | `66 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe64c"></a> `00bbe64c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe650"></a> `00bbe650` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe654"></a> `00bbe654` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe658"></a> `00bbe658` | `96 72 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe65c"></a> `00bbe65c` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe660"></a> `00bbe660` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe664"></a> `00bbe664` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe668"></a> `00bbe668` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe66c"></a> `00bbe66c` | `63 08 00 54` | b.cc 0x00bbe778 | `CONDITIONAL_JUMP`
<a id="insn-00bbe670"></a> `00bbe670` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe674"></a> `00bbe674` | `28 08 00 b4` | cbz x8,0x00bbe778 | `CONDITIONAL_JUMP`
<a id="insn-00bbe678"></a> `00bbe678` | `ca 02 08 8b` | add x10,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe67c"></a> `00bbe67c` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbe680"></a> `00bbe680` | `e9 a3 55 a9` | ldp x9,x8,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbe684"></a> `00bbe684` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbe688"></a> `00bbe688` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe68c"></a> `00bbe68c` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bbe690"></a> `00bbe690` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe694"></a> `00bbe694` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bbe698"></a> `00bbe698` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbe69c"></a> `00bbe69c` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bbe6a0"></a> `00bbe6a0` | `c2 00 00 54` | b.cs 0x00bbe6b8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6a4"></a> `00bbe6a4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe6a8"></a> `00bbe6a8` | `00 21 04 91` | add x0,x8,#0x108 | `FALL_THROUGH`
<a id="insn-00bbe6ac"></a> `00bbe6ac` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00bbe6b0"></a> `00bbe6b0` | `ac 7b 02 94` | bl 0x00c5d560 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6b4"></a> `00bbe6b4` | `12 00 00 14` | b 0x00bbe6fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6b8"></a> `00bbe6b8` | `29 02 00 54` | b.ls 0x00bbe6fc | `CONDITIONAL_JUMP`
<a id="insn-00bbe6bc"></a> `00bbe6bc` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe6c0"></a> `00bbe6c0` | `74 26 0a 9b` | madd x20,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00bbe6c4"></a> `00bbe6c4` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe6c8"></a> `00bbe6c8` | `80 01 00 54` | b.eq 0x00bbe6f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6cc"></a> `00bbe6cc` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbe6d0"></a> `00bbe6d0` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe6d4"></a> `00bbe6d4` | `c9 00 00 37` | tbnz w9,#0x0,0x00bbe6ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe6d8"></a> `00bbe6d8` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00bbe6dc"></a> `00bbe6dc` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbe6e0"></a> `00bbe6e0` | `c0 00 00 54` | b.eq 0x00bbe6f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6e4"></a> `00bbe6e4` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bbe6e8"></a> `00bbe6e8` | `89 ff 07 36` | tbz w9,#0x0,0x00bbe6d8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6ec"></a> `00bbe6ec` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bbe6f0"></a> `00bbe6f0` | `f0 65 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6f4"></a> `00bbe6f4` | `f9 ff ff 17` | b 0x00bbe6d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6f8"></a> `00bbe6f8` | `f4 b3 00 f9` | str x20,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bbe6fc"></a> `00bbe6fc` | `f3 03 00 34` | cbz w19,0x00bbe778 | `CONDITIONAL_JUMP`
<a id="insn-00bbe700"></a> `00bbe700` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bbe704"></a> `00bbe704` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe708"></a> `00bbe708` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe70c"></a> `00bbe70c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe710"></a> `00bbe710` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe714"></a> `00bbe714` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00bbe718"></a> `00bbe718` | `e3 00 00 54` | b.cc 0x00bbe734 | `CONDITIONAL_JUMP`
<a id="insn-00bbe71c"></a> `00bbe71c` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00bbe720"></a> `00bbe720` | `c8 00 00 b4` | cbz x8,0x00bbe738 | `CONDITIONAL_JUMP`
<a id="insn-00bbe724"></a> `00bbe724` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe728"></a> `00bbe728` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe72c"></a> `00bbe72c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe730"></a> `00bbe730` | `02 00 00 14` | b 0x00bbe738 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe734"></a> `00bbe734` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe738"></a> `00bbe738` | `e9 76 1e 53` | lsl w9,w23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe73c"></a> `00bbe73c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe740"></a> `00bbe740` | `09 4d 40 b8` | ldr w9,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bbe744"></a> `00bbe744` | `ea af 40 f9` | ldr x10,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00bbe748"></a> `00bbe748` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe74c"></a> `00bbe74c` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe750"></a> `00bbe750` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe754"></a> `00bbe754` | `f5 2a 18 9b` | madd x21,x23,x24,x10 | `FALL_THROUGH`
<a id="insn-00bbe758"></a> `00bbe758` | `22 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe75c"></a> `00bbe75c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe760"></a> `00bbe760` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe764"></a> `00bbe764` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe768"></a> `00bbe768` | `52 72 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe76c"></a> `00bbe76c` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe770"></a> `00bbe770` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00bbe774"></a> `00bbe774` | `a1 fc ff 54` | b.ne 0x00bbe708 | `CONDITIONAL_JUMP`
<a id="insn-00bbe778"></a> `00bbe778` | `c8 02 80 b9` | ldrsw x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbe77c"></a> `00bbe77c` | `c8 02 08 cb` | sub x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe780"></a> `00bbe780` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe784"></a> `00bbe784` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bbe788"></a> `00bbe788` | `e3 00 00 54` | b.cc 0x00bbe7a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe78c"></a> `00bbe78c` | `08 39 40 79` | ldrh w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00bbe790"></a> `00bbe790` | `c8 00 00 b4` | cbz x8,0x00bbe7a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe794"></a> `00bbe794` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe798"></a> `00bbe798` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe79c"></a> `00bbe79c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe7a0"></a> `00bbe7a0` | `02 00 00 14` | b 0x00bbe7a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe7a4"></a> `00bbe7a4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe7a8"></a> `00bbe7a8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbe7ac"></a> `00bbe7ac` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bbe7b0"></a> `00bbe7b0` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00bbe7b4"></a> `00bbe7b4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe7b8"></a> `00bbe7b8` | `0a 66 02 94` | bl 0x00c57fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe7bc"></a> `00bbe7bc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbe7c0"></a> `00bbe7c0` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbe7c4"></a> `00bbe7c4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbe7c8"></a> `00bbe7c8` | `f3 e3 00 91` | add x19,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbe7cc"></a> `00bbe7cc` | `39 72 02 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe7d0"></a> `00bbe7d0` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe7d4"></a> `00bbe7d4` | `f3 bb 00 f9` | str x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bbe7d8"></a> `00bbe7d8` | `e8 3f 01 f9` | str x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe7dc"></a> `00bbe7dc` | `48 07 40 a9` | ldp x8,x1,[x26] | `FALL_THROUGH`
<a id="insn-00bbe7e0"></a> `00bbe7e0` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe7e4"></a> `00bbe7e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbe7e8"></a> `00bbe7e8` | `e8 3f 41 f9` | ldr x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe7ec"></a> `00bbe7ec` | `68 00 00 b4` | cbz x8,0x00bbe7f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7f0"></a> `00bbe7f0` | `1f 91 00 f9` | str xzr,[x8, #0x120] | `FALL_THROUGH`
<a id="insn-00bbe7f4"></a> `00bbe7f4` | `ff 3f 01 f9` | str xzr,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00bbe7f8"></a> `00bbe7f8` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbe7fc"></a> `00bbe7fc` | `68 00 00 36` | tbz w8,#0x0,0x00bbe808 | `CONDITIONAL_JUMP`
<a id="insn-00bbe800"></a> `00bbe800` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbe804"></a> `00bbe804` | `ab 65 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe808"></a> `00bbe808` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbe80c"></a> `00bbe80c` | `b1 7a 02 94` | bl 0x00c5d2d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe810"></a> `00bbe810` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bbe814"></a> `00bbe814` | `f7 7a 02 94` | bl 0x00c5d3f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe818"></a> `00bbe818` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbe81c"></a> `00bbe81c` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbe820"></a> `00bbe820` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe824"></a> `00bbe824` | `21 01 00 54` | b.ne 0x00bbe848 | `CONDITIONAL_JUMP`
<a id="insn-00bbe828"></a> `00bbe828` | `ff 83 0b 91` | add sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00bbe82c"></a> `00bbe82c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbe830"></a> `00bbe830` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbe834"></a> `00bbe834` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbe838"></a> `00bbe838` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe83c"></a> `00bbe83c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe840"></a> `00bbe840` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bbe844"></a> `00bbe844` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbe848"></a> `00bbe848` | `a6 65 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbda4c`](#insn-00bbda4c) 範囲 `[['00bbda4c', '00bbda77']]`
  - `FALL_THROUGH` [`00bbda74`](#insn-00bbda74) → [`00bbda78`](#insn-00bbda78)
- ブロック [`00bbda78`](#insn-00bbda78) 範囲 `[['00bbda78', '00bbdab7']]`
  - `FALL_THROUGH` [`00bbdab4`](#insn-00bbdab4) → [`00bbdab8`](#insn-00bbdab8)
- ブロック [`00bbdab8`](#insn-00bbdab8) 範囲 `[['00bbdab8', '00bbdb13']]`
  - `CONDITIONAL_JUMP` [`00bbdb10`](#insn-00bbdb10) → [`00bbdb28`](#insn-00bbdb28)
  - `FALL_THROUGH` [`00bbdb10`](#insn-00bbdb10) → [`00bbdb14`](#insn-00bbdb14)
- ブロック [`00bbdb14`](#insn-00bbdb14) 範囲 `[['00bbdb14', '00bbdb1b']]`
  - `CONDITIONAL_JUMP` [`00bbdb18`](#insn-00bbdb18) → [`00bbdb28`](#insn-00bbdb28)
  - `FALL_THROUGH` [`00bbdb18`](#insn-00bbdb18) → [`00bbdb1c`](#insn-00bbdb1c)
- ブロック [`00bbdb1c`](#insn-00bbdb1c) 範囲 `[['00bbdb1c', '00bbdb27']]`
  - `FALL_THROUGH` [`00bbdb24`](#insn-00bbdb24) → [`00bbdb28`](#insn-00bbdb28)
- ブロック [`00bbdb28`](#insn-00bbdb28) 範囲 `[['00bbdb28', '00bbdb43']]`
  - `FALL_THROUGH` [`00bbdb40`](#insn-00bbdb40) → [`00bbdb44`](#insn-00bbdb44)
- ブロック [`00bbdb44`](#insn-00bbdb44) 範囲 `[['00bbdb44', '00bbdb47']]`
  - `FALL_THROUGH` [`00bbdb44`](#insn-00bbdb44) → [`00bbdb48`](#insn-00bbdb48)
- ブロック [`00bbdb48`](#insn-00bbdb48) 範囲 `[['00bbdb48', '00bbdb67']]`
  - `CONDITIONAL_JUMP` [`00bbdb64`](#insn-00bbdb64) → [`00bbdb80`](#insn-00bbdb80)
  - `FALL_THROUGH` [`00bbdb64`](#insn-00bbdb64) → [`00bbdb68`](#insn-00bbdb68)
- ブロック [`00bbdb68`](#insn-00bbdb68) 範囲 `[['00bbdb68', '00bbdb6f']]`
  - `CONDITIONAL_JUMP` [`00bbdb6c`](#insn-00bbdb6c) → [`00bbdb84`](#insn-00bbdb84)
  - `FALL_THROUGH` [`00bbdb6c`](#insn-00bbdb6c) → [`00bbdb70`](#insn-00bbdb70)
- ブロック [`00bbdb70`](#insn-00bbdb70) 範囲 `[['00bbdb70', '00bbdb7f']]`
  - `UNCONDITIONAL_JUMP` [`00bbdb7c`](#insn-00bbdb7c) → [`00bbdb84`](#insn-00bbdb84)
- ブロック [`00bbdb80`](#insn-00bbdb80) 範囲 `[['00bbdb80', '00bbdb83']]`
  - `FALL_THROUGH` [`00bbdb80`](#insn-00bbdb80) → [`00bbdb84`](#insn-00bbdb84)
- ブロック [`00bbdb84`](#insn-00bbdb84) 範囲 `[['00bbdb84', '00bbdbc7']]`
  - `CONDITIONAL_JUMP` [`00bbdbc4`](#insn-00bbdbc4) → [`00bbdd6c`](#insn-00bbdd6c)
  - `FALL_THROUGH` [`00bbdbc4`](#insn-00bbdbc4) → [`00bbdbc8`](#insn-00bbdbc8)
- ブロック [`00bbdbc8`](#insn-00bbdbc8) 範囲 `[['00bbdbc8', '00bbdbcf']]`
  - `CONDITIONAL_JUMP` [`00bbdbcc`](#insn-00bbdbcc) → [`00bbdd6c`](#insn-00bbdd6c)
  - `FALL_THROUGH` [`00bbdbcc`](#insn-00bbdbcc) → [`00bbdbd0`](#insn-00bbdbd0)
- ブロック [`00bbdbd0`](#insn-00bbdbd0) 範囲 `[['00bbdbd0', '00bbdbd3']]`
  - `FALL_THROUGH` [`00bbdbd0`](#insn-00bbdbd0) → [`00bbdbd4`](#insn-00bbdbd4)
- ブロック [`00bbdbd4`](#insn-00bbdbd4) 範囲 `[['00bbdbd4', '00bbdbdf']]`
  - `CONDITIONAL_JUMP` [`00bbdbdc`](#insn-00bbdbdc) → [`00bbdd6c`](#insn-00bbdd6c)
  - `FALL_THROUGH` [`00bbdbdc`](#insn-00bbdbdc) → [`00bbdbe0`](#insn-00bbdbe0)
- ブロック [`00bbdbe0`](#insn-00bbdbe0) 範囲 `[['00bbdbe0', '00bbdbe7']]`
  - `CONDITIONAL_JUMP` [`00bbdbe4`](#insn-00bbdbe4) → [`00bbdd6c`](#insn-00bbdd6c)
  - `FALL_THROUGH` [`00bbdbe4`](#insn-00bbdbe4) → [`00bbdbe8`](#insn-00bbdbe8)
- ブロック [`00bbdbe8`](#insn-00bbdbe8) 範囲 `[['00bbdbe8', '00bbdbff']]`
  - `UNCONDITIONAL_JUMP` [`00bbdbfc`](#insn-00bbdbfc) → [`00bbdc10`](#insn-00bbdc10)
- ブロック [`00bbdc00`](#insn-00bbdc00) 範囲 `[['00bbdc00', '00bbdc0f']]`
  - `CONDITIONAL_JUMP` [`00bbdc0c`](#insn-00bbdc0c) → [`00bbdd60`](#insn-00bbdd60)
  - `FALL_THROUGH` [`00bbdc0c`](#insn-00bbdc0c) → [`00bbdc10`](#insn-00bbdc10)
- ブロック [`00bbdc10`](#insn-00bbdc10) 範囲 `[['00bbdc10', '00bbdc47']]`
  - `CONDITIONAL_JUMP` [`00bbdc44`](#insn-00bbdc44) → [`00bbdc88`](#insn-00bbdc88)
  - `FALL_THROUGH` [`00bbdc44`](#insn-00bbdc44) → [`00bbdc48`](#insn-00bbdc48)
- ブロック [`00bbdc48`](#insn-00bbdc48) 範囲 `[['00bbdc48', '00bbdc4f']]`
  - `CONDITIONAL_JUMP` [`00bbdc4c`](#insn-00bbdc4c) → [`00bbdc5c`](#insn-00bbdc5c)
  - `FALL_THROUGH` [`00bbdc4c`](#insn-00bbdc4c) → [`00bbdc50`](#insn-00bbdc50)
- ブロック [`00bbdc50`](#insn-00bbdc50) 範囲 `[['00bbdc50', '00bbdc5b']]`
  - `FALL_THROUGH` [`00bbdc58`](#insn-00bbdc58) → [`00bbdc5c`](#insn-00bbdc5c)
- ブロック [`00bbdc5c`](#insn-00bbdc5c) 範囲 `[['00bbdc5c', '00bbdc6f']]`
  - `CONDITIONAL_JUMP` [`00bbdc6c`](#insn-00bbdc6c) → [`00bbdc94`](#insn-00bbdc94)
  - `FALL_THROUGH` [`00bbdc6c`](#insn-00bbdc6c) → [`00bbdc70`](#insn-00bbdc70)
- ブロック [`00bbdc70`](#insn-00bbdc70) 範囲 `[['00bbdc70', '00bbdc77']]`
  - `CONDITIONAL_JUMP` [`00bbdc74`](#insn-00bbdc74) → [`00bbdc94`](#insn-00bbdc94)
  - `FALL_THROUGH` [`00bbdc74`](#insn-00bbdc74) → [`00bbdc78`](#insn-00bbdc78)
- ブロック [`00bbdc78`](#insn-00bbdc78) 範囲 `[['00bbdc78', '00bbdc87']]`
  - `UNCONDITIONAL_JUMP` [`00bbdc84`](#insn-00bbdc84) → [`00bbdc98`](#insn-00bbdc98)
- ブロック [`00bbdc88`](#insn-00bbdc88) 範囲 `[['00bbdc88', '00bbdc8b']]`
  - `FALL_THROUGH` [`00bbdc88`](#insn-00bbdc88) → [`00bbdc8c`](#insn-00bbdc8c)
- ブロック [`00bbdc8c`](#insn-00bbdc8c) 範囲 `[['00bbdc8c', '00bbdc93']]`
  - `UNCONDITIONAL_JUMP` [`00bbdc90`](#insn-00bbdc90) → [`00bbdc98`](#insn-00bbdc98)
- ブロック [`00bbdc94`](#insn-00bbdc94) 範囲 `[['00bbdc94', '00bbdc97']]`
  - `FALL_THROUGH` [`00bbdc94`](#insn-00bbdc94) → [`00bbdc98`](#insn-00bbdc98)
- ブロック [`00bbdc98`](#insn-00bbdc98) 範囲 `[['00bbdc98', '00bbdcc7']]`
  - `CONDITIONAL_JUMP` [`00bbdcc4`](#insn-00bbdcc4) → [`00bbdd30`](#insn-00bbdd30)
  - `FALL_THROUGH` [`00bbdcc4`](#insn-00bbdcc4) → [`00bbdcc8`](#insn-00bbdcc8)
- ブロック [`00bbdcc8`](#insn-00bbdcc8) 範囲 `[['00bbdcc8', '00bbdd0b']]`
  - `CONDITIONAL_JUMP` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd18`](#insn-00bbdd18)
  - `FALL_THROUGH` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd0c`](#insn-00bbdd0c)
- ブロック [`00bbdd0c`](#insn-00bbdd0c) 範囲 `[['00bbdd0c', '00bbdd17']]`
  - `UNCONDITIONAL_JUMP` [`00bbdd14`](#insn-00bbdd14) → [`00bbdd1c`](#insn-00bbdd1c)
- ブロック [`00bbdd18`](#insn-00bbdd18) 範囲 `[['00bbdd18', '00bbdd1b']]`
  - `FALL_THROUGH` [`00bbdd18`](#insn-00bbdd18) → [`00bbdd1c`](#insn-00bbdd1c)
- ブロック [`00bbdd1c`](#insn-00bbdd1c) 範囲 `[['00bbdd1c', '00bbdd2f']]`
  - `FALL_THROUGH` [`00bbdd2c`](#insn-00bbdd2c) → [`00bbdd30`](#insn-00bbdd30)
- ブロック [`00bbdd30`](#insn-00bbdd30) 範囲 `[['00bbdd30', '00bbdd53']]`
  - `CONDITIONAL_JUMP` [`00bbdd50`](#insn-00bbdd50) → [`00bbdc00`](#insn-00bbdc00)
  - `FALL_THROUGH` [`00bbdd50`](#insn-00bbdd50) → [`00bbdd54`](#insn-00bbdd54)
- ブロック [`00bbdd54`](#insn-00bbdd54) 範囲 `[['00bbdd54', '00bbdd5b']]`
  - `FALL_THROUGH` [`00bbdd58`](#insn-00bbdd58) → [`00bbdd5c`](#insn-00bbdd5c)
- ブロック [`00bbdd5c`](#insn-00bbdd5c) 範囲 `[['00bbdd5c', '00bbdd5f']]`
  - `UNCONDITIONAL_JUMP` [`00bbdd5c`](#insn-00bbdd5c) → [`00bbdc00`](#insn-00bbdc00)
- ブロック [`00bbdd60`](#insn-00bbdd60) 範囲 `[['00bbdd60', '00bbdd63']]`
  - `FALL_THROUGH` [`00bbdd60`](#insn-00bbdd60) → [`00bbdd64`](#insn-00bbdd64)
- ブロック [`00bbdd64`](#insn-00bbdd64) 範囲 `[['00bbdd64', '00bbdd6b']]`
  - `FALL_THROUGH` [`00bbdd68`](#insn-00bbdd68) → [`00bbdd6c`](#insn-00bbdd6c)
- ブロック [`00bbdd6c`](#insn-00bbdd6c) 範囲 `[['00bbdd6c', '00bbdd7b']]`
  - `CONDITIONAL_JUMP` [`00bbdd78`](#insn-00bbdd78) → [`00bbde40`](#insn-00bbde40)
  - `FALL_THROUGH` [`00bbdd78`](#insn-00bbdd78) → [`00bbdd7c`](#insn-00bbdd7c)
- ブロック [`00bbdd7c`](#insn-00bbdd7c) 範囲 `[['00bbdd7c', '00bbdd83']]`
  - `CONDITIONAL_JUMP` [`00bbdd80`](#insn-00bbdd80) → [`00bbde40`](#insn-00bbde40)
  - `FALL_THROUGH` [`00bbdd80`](#insn-00bbdd80) → [`00bbdd84`](#insn-00bbdd84)
- ブロック [`00bbdd84`](#insn-00bbdd84) 範囲 `[['00bbdd84', '00bbdd93']]`
  - `CONDITIONAL_JUMP` [`00bbdd90`](#insn-00bbdd90) → [`00bbde40`](#insn-00bbde40)
  - `FALL_THROUGH` [`00bbdd90`](#insn-00bbdd90) → [`00bbdd94`](#insn-00bbdd94)
- ブロック [`00bbdd94`](#insn-00bbdd94) 範囲 `[['00bbdd94', '00bbddab']]`
  - `CONDITIONAL_JUMP` [`00bbdda8`](#insn-00bbdda8) → [`00bbddf0`](#insn-00bbddf0)
  - `FALL_THROUGH` [`00bbdda8`](#insn-00bbdda8) → [`00bbddac`](#insn-00bbddac)
- ブロック [`00bbddac`](#insn-00bbddac) 範囲 `[['00bbddac', '00bbddb7']]`
  - `FALL_THROUGH` [`00bbddb4`](#insn-00bbddb4) → [`00bbddb8`](#insn-00bbddb8)
- ブロック [`00bbddb8`](#insn-00bbddb8) 範囲 `[['00bbddb8', '00bbddcf']]`
  - `CONDITIONAL_JUMP` [`00bbddcc`](#insn-00bbddcc) → [`00bbdddc`](#insn-00bbdddc)
  - `FALL_THROUGH` [`00bbddcc`](#insn-00bbddcc) → [`00bbddd0`](#insn-00bbddd0)
- ブロック [`00bbddd0`](#insn-00bbddd0) 範囲 `[['00bbddd0', '00bbdddb']]`
  - `FALL_THROUGH` [`00bbddd8`](#insn-00bbddd8) → [`00bbdddc`](#insn-00bbdddc)
- ブロック [`00bbdddc`](#insn-00bbdddc) 範囲 `[['00bbdddc', '00bbdde7']]`
  - `CONDITIONAL_JUMP` [`00bbdde4`](#insn-00bbdde4) → [`00bbddf0`](#insn-00bbddf0)
  - `FALL_THROUGH` [`00bbdde4`](#insn-00bbdde4) → [`00bbdde8`](#insn-00bbdde8)
- ブロック [`00bbdde8`](#insn-00bbdde8) 範囲 `[['00bbdde8', '00bbddef']]`
  - `FALL_THROUGH` [`00bbddec`](#insn-00bbddec) → [`00bbddf0`](#insn-00bbddf0)
- ブロック [`00bbddf0`](#insn-00bbddf0) 範囲 `[['00bbddf0', '00bbddf7']]`
  - `FALL_THROUGH` [`00bbddf4`](#insn-00bbddf4) → [`00bbddf8`](#insn-00bbddf8)
- ブロック [`00bbddf8`](#insn-00bbddf8) 範囲 `[['00bbddf8', '00bbde13']]`
  - `FALL_THROUGH` [`00bbde10`](#insn-00bbde10) → [`00bbde14`](#insn-00bbde14)
- ブロック [`00bbde14`](#insn-00bbde14) 範囲 `[['00bbde14', '00bbde3f']]`
  - `FALL_THROUGH` [`00bbde3c`](#insn-00bbde3c) → [`00bbde40`](#insn-00bbde40)
- ブロック [`00bbde40`](#insn-00bbde40) 範囲 `[['00bbde40', '00bbde4f']]`
  - `CONDITIONAL_JUMP` [`00bbde4c`](#insn-00bbde4c) → [`00bbde68`](#insn-00bbde68)
  - `FALL_THROUGH` [`00bbde4c`](#insn-00bbde4c) → [`00bbde50`](#insn-00bbde50)
- ブロック [`00bbde50`](#insn-00bbde50) 範囲 `[['00bbde50', '00bbde57']]`
  - `CONDITIONAL_JUMP` [`00bbde54`](#insn-00bbde54) → [`00bbde6c`](#insn-00bbde6c)
  - `FALL_THROUGH` [`00bbde54`](#insn-00bbde54) → [`00bbde58`](#insn-00bbde58)
- ブロック [`00bbde58`](#insn-00bbde58) 範囲 `[['00bbde58', '00bbde67']]`
  - `UNCONDITIONAL_JUMP` [`00bbde64`](#insn-00bbde64) → [`00bbde6c`](#insn-00bbde6c)
- ブロック [`00bbde68`](#insn-00bbde68) 範囲 `[['00bbde68', '00bbde6b']]`
  - `FALL_THROUGH` [`00bbde68`](#insn-00bbde68) → [`00bbde6c`](#insn-00bbde6c)
- ブロック [`00bbde6c`](#insn-00bbde6c) 範囲 `[['00bbde6c', '00bbdeab']]`
  - `CONDITIONAL_JUMP` [`00bbdea8`](#insn-00bbdea8) → [`00bbdec4`](#insn-00bbdec4)
  - `FALL_THROUGH` [`00bbdea8`](#insn-00bbdea8) → [`00bbdeac`](#insn-00bbdeac)
- ブロック [`00bbdeac`](#insn-00bbdeac) 範囲 `[['00bbdeac', '00bbdeb3']]`
  - `CONDITIONAL_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdec8`](#insn-00bbdec8)
  - `FALL_THROUGH` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdeb4`](#insn-00bbdeb4)
- ブロック [`00bbdeb4`](#insn-00bbdeb4) 範囲 `[['00bbdeb4', '00bbdec3']]`
  - `UNCONDITIONAL_JUMP` [`00bbdec0`](#insn-00bbdec0) → [`00bbdec8`](#insn-00bbdec8)
- ブロック [`00bbdec4`](#insn-00bbdec4) 範囲 `[['00bbdec4', '00bbdec7']]`
  - `FALL_THROUGH` [`00bbdec4`](#insn-00bbdec4) → [`00bbdec8`](#insn-00bbdec8)
- ブロック [`00bbdec8`](#insn-00bbdec8) 範囲 `[['00bbdec8', '00bbdef3']]`
  - `FALL_THROUGH` [`00bbdef0`](#insn-00bbdef0) → [`00bbdef4`](#insn-00bbdef4)
- ブロック [`00bbdef4`](#insn-00bbdef4) 範囲 `[['00bbdef4', '00bbdf0b']]`
  - `CONDITIONAL_JUMP` [`00bbdf08`](#insn-00bbdf08) → [`00bbdf24`](#insn-00bbdf24)
  - `FALL_THROUGH` [`00bbdf08`](#insn-00bbdf08) → [`00bbdf0c`](#insn-00bbdf0c)
- ブロック [`00bbdf0c`](#insn-00bbdf0c) 範囲 `[['00bbdf0c', '00bbdf0f']]`
  - `FALL_THROUGH` [`00bbdf0c`](#insn-00bbdf0c) → [`00bbdf10`](#insn-00bbdf10)
- ブロック [`00bbdf10`](#insn-00bbdf10) 範囲 `[['00bbdf10', '00bbdf13']]`
  - `CONDITIONAL_JUMP` [`00bbdf10`](#insn-00bbdf10) → [`00bbdf28`](#insn-00bbdf28)
  - `FALL_THROUGH` [`00bbdf10`](#insn-00bbdf10) → [`00bbdf14`](#insn-00bbdf14)
- ブロック [`00bbdf14`](#insn-00bbdf14) 範囲 `[['00bbdf14', '00bbdf23']]`
  - `UNCONDITIONAL_JUMP` [`00bbdf20`](#insn-00bbdf20) → [`00bbdf28`](#insn-00bbdf28)
- ブロック [`00bbdf24`](#insn-00bbdf24) 範囲 `[['00bbdf24', '00bbdf27']]`
  - `FALL_THROUGH` [`00bbdf24`](#insn-00bbdf24) → [`00bbdf28`](#insn-00bbdf28)
- ブロック [`00bbdf28`](#insn-00bbdf28) 範囲 `[['00bbdf28', '00bbdf47']]`
  - `FALL_THROUGH` [`00bbdf44`](#insn-00bbdf44) → [`00bbdf48`](#insn-00bbdf48)
- ブロック [`00bbdf48`](#insn-00bbdf48) 範囲 `[['00bbdf48', '00bbdf5f']]`
  - `CONDITIONAL_JUMP` [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf78`](#insn-00bbdf78)
  - `FALL_THROUGH` [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf60`](#insn-00bbdf60)
- ブロック [`00bbdf60`](#insn-00bbdf60) 範囲 `[['00bbdf60', '00bbdf63']]`
  - `FALL_THROUGH` [`00bbdf60`](#insn-00bbdf60) → [`00bbdf64`](#insn-00bbdf64)
- ブロック [`00bbdf64`](#insn-00bbdf64) 範囲 `[['00bbdf64', '00bbdf67']]`
  - `CONDITIONAL_JUMP` [`00bbdf64`](#insn-00bbdf64) → [`00bbdf7c`](#insn-00bbdf7c)
  - `FALL_THROUGH` [`00bbdf64`](#insn-00bbdf64) → [`00bbdf68`](#insn-00bbdf68)
- ブロック [`00bbdf68`](#insn-00bbdf68) 範囲 `[['00bbdf68', '00bbdf77']]`
  - `UNCONDITIONAL_JUMP` [`00bbdf74`](#insn-00bbdf74) → [`00bbdf7c`](#insn-00bbdf7c)
- ブロック [`00bbdf78`](#insn-00bbdf78) 範囲 `[['00bbdf78', '00bbdf7b']]`
  - `FALL_THROUGH` [`00bbdf78`](#insn-00bbdf78) → [`00bbdf7c`](#insn-00bbdf7c)
- ブロック [`00bbdf7c`](#insn-00bbdf7c) 範囲 `[['00bbdf7c', '00bbdf7f']]`
  - `FALL_THROUGH` [`00bbdf7c`](#insn-00bbdf7c) → [`00bbdf80`](#insn-00bbdf80)
- ブロック [`00bbdf80`](#insn-00bbdf80) 範囲 `[['00bbdf80', '00bbdf83']]`
  - `FALL_THROUGH` [`00bbdf80`](#insn-00bbdf80) → [`00bbdf84`](#insn-00bbdf84)
- ブロック [`00bbdf84`](#insn-00bbdf84) 範囲 `[['00bbdf84', '00bbdf87']]`
  - `FALL_THROUGH` [`00bbdf84`](#insn-00bbdf84) → [`00bbdf88`](#insn-00bbdf88)
- ブロック [`00bbdf88`](#insn-00bbdf88) 範囲 `[['00bbdf88', '00bbdf97']]`
  - `FALL_THROUGH` [`00bbdf94`](#insn-00bbdf94) → [`00bbdf98`](#insn-00bbdf98)
- ブロック [`00bbdf98`](#insn-00bbdf98) 範囲 `[['00bbdf98', '00bbdfa7']]`
  - `FALL_THROUGH` [`00bbdfa4`](#insn-00bbdfa4) → [`00bbdfa8`](#insn-00bbdfa8)
- ブロック [`00bbdfa8`](#insn-00bbdfa8) 範囲 `[['00bbdfa8', '00bbdfab']]`
  - `FALL_THROUGH` [`00bbdfa8`](#insn-00bbdfa8) → [`00bbdfac`](#insn-00bbdfac)
- ブロック [`00bbdfac`](#insn-00bbdfac) 範囲 `[['00bbdfac', '00bbdfaf']]`
  - `FALL_THROUGH` [`00bbdfac`](#insn-00bbdfac) → [`00bbdfb0`](#insn-00bbdfb0)
- ブロック [`00bbdfb0`](#insn-00bbdfb0) 範囲 `[['00bbdfb0', '00bbdfbb']]`
  - `CONDITIONAL_JUMP` [`00bbdfb8`](#insn-00bbdfb8) → [`00bbdff4`](#insn-00bbdff4)
  - `FALL_THROUGH` [`00bbdfb8`](#insn-00bbdfb8) → [`00bbdfbc`](#insn-00bbdfbc)
- ブロック [`00bbdfbc`](#insn-00bbdfbc) 範囲 `[['00bbdfbc', '00bbdfc3']]`
  - `CONDITIONAL_JUMP` [`00bbdfc0`](#insn-00bbdfc0) → [`00bbdfd0`](#insn-00bbdfd0)
  - `FALL_THROUGH` [`00bbdfc0`](#insn-00bbdfc0) → [`00bbdfc4`](#insn-00bbdfc4)
- ブロック [`00bbdfc4`](#insn-00bbdfc4) 範囲 `[['00bbdfc4', '00bbdfc7']]`
  - `FALL_THROUGH` [`00bbdfc4`](#insn-00bbdfc4) → [`00bbdfc8`](#insn-00bbdfc8)
- ブロック [`00bbdfc8`](#insn-00bbdfc8) 範囲 `[['00bbdfc8', '00bbdfcf']]`
  - `FALL_THROUGH` [`00bbdfcc`](#insn-00bbdfcc) → [`00bbdfd0`](#insn-00bbdfd0)
- ブロック [`00bbdfd0`](#insn-00bbdfd0) 範囲 `[['00bbdfd0', '00bbdfd3']]`
  - `FALL_THROUGH` [`00bbdfd0`](#insn-00bbdfd0) → [`00bbdfd4`](#insn-00bbdfd4)
- ブロック [`00bbdfd4`](#insn-00bbdfd4) 範囲 `[['00bbdfd4', '00bbdfd7']]`
  - `FALL_THROUGH` [`00bbdfd4`](#insn-00bbdfd4) → [`00bbdfd8`](#insn-00bbdfd8)
- ブロック [`00bbdfd8`](#insn-00bbdfd8) 範囲 `[['00bbdfd8', '00bbdfdb']]`
  - `CONDITIONAL_JUMP` [`00bbdfd8`](#insn-00bbdfd8) → [`00bbe000`](#insn-00bbe000)
  - `FALL_THROUGH` [`00bbdfd8`](#insn-00bbdfd8) → [`00bbdfdc`](#insn-00bbdfdc)
- ブロック [`00bbdfdc`](#insn-00bbdfdc) 範囲 `[['00bbdfdc', '00bbdfdf']]`
  - `FALL_THROUGH` [`00bbdfdc`](#insn-00bbdfdc) → [`00bbdfe0`](#insn-00bbdfe0)
- ブロック [`00bbdfe0`](#insn-00bbdfe0) 範囲 `[['00bbdfe0', '00bbdfe3']]`
  - `CONDITIONAL_JUMP` [`00bbdfe0`](#insn-00bbdfe0) → [`00bbe004`](#insn-00bbe004)
  - `FALL_THROUGH` [`00bbdfe0`](#insn-00bbdfe0) → [`00bbdfe4`](#insn-00bbdfe4)
- ブロック [`00bbdfe4`](#insn-00bbdfe4) 範囲 `[['00bbdfe4', '00bbdff3']]`
  - `UNCONDITIONAL_JUMP` [`00bbdff0`](#insn-00bbdff0) → [`00bbe004`](#insn-00bbe004)
- ブロック [`00bbdff4`](#insn-00bbdff4) 範囲 `[['00bbdff4', '00bbdfff']]`
  - `UNCONDITIONAL_JUMP` [`00bbdffc`](#insn-00bbdffc) → [`00bbe004`](#insn-00bbe004)
- ブロック [`00bbe000`](#insn-00bbe000) 範囲 `[['00bbe000', '00bbe003']]`
  - `FALL_THROUGH` [`00bbe000`](#insn-00bbe000) → [`00bbe004`](#insn-00bbe004)
- ブロック [`00bbe004`](#insn-00bbe004) 範囲 `[['00bbe004', '00bbe007']]`
  - `FALL_THROUGH` [`00bbe004`](#insn-00bbe004) → [`00bbe008`](#insn-00bbe008)
- ブロック [`00bbe008`](#insn-00bbe008) 範囲 `[['00bbe008', '00bbe00b']]`
  - `FALL_THROUGH` [`00bbe008`](#insn-00bbe008) → [`00bbe00c`](#insn-00bbe00c)
- ブロック [`00bbe00c`](#insn-00bbe00c) 範囲 `[['00bbe00c', '00bbe013']]`
  - `FALL_THROUGH` [`00bbe010`](#insn-00bbe010) → [`00bbe014`](#insn-00bbe014)
- ブロック [`00bbe014`](#insn-00bbe014) 範囲 `[['00bbe014', '00bbe03b']]`
  - `CONDITIONAL_JUMP` [`00bbe038`](#insn-00bbe038) → [`00bbe054`](#insn-00bbe054)
  - `FALL_THROUGH` [`00bbe038`](#insn-00bbe038) → [`00bbe03c`](#insn-00bbe03c)
- ブロック [`00bbe03c`](#insn-00bbe03c) 範囲 `[['00bbe03c', '00bbe043']]`
  - `CONDITIONAL_JUMP` [`00bbe040`](#insn-00bbe040) → [`00bbe058`](#insn-00bbe058)
  - `FALL_THROUGH` [`00bbe040`](#insn-00bbe040) → [`00bbe044`](#insn-00bbe044)
- ブロック [`00bbe044`](#insn-00bbe044) 範囲 `[['00bbe044', '00bbe053']]`
  - `UNCONDITIONAL_JUMP` [`00bbe050`](#insn-00bbe050) → [`00bbe058`](#insn-00bbe058)
- ブロック [`00bbe054`](#insn-00bbe054) 範囲 `[['00bbe054', '00bbe057']]`
  - `FALL_THROUGH` [`00bbe054`](#insn-00bbe054) → [`00bbe058`](#insn-00bbe058)
- ブロック [`00bbe058`](#insn-00bbe058) 範囲 `[['00bbe058', '00bbe097']]`
  - `CONDITIONAL_JUMP` [`00bbe094`](#insn-00bbe094) → [`00bbe0b0`](#insn-00bbe0b0)
  - `FALL_THROUGH` [`00bbe094`](#insn-00bbe094) → [`00bbe098`](#insn-00bbe098)
- ブロック [`00bbe098`](#insn-00bbe098) 範囲 `[['00bbe098', '00bbe09f']]`
  - `CONDITIONAL_JUMP` [`00bbe09c`](#insn-00bbe09c) → [`00bbe0b4`](#insn-00bbe0b4)
  - `FALL_THROUGH` [`00bbe09c`](#insn-00bbe09c) → [`00bbe0a0`](#insn-00bbe0a0)
- ブロック [`00bbe0a0`](#insn-00bbe0a0) 範囲 `[['00bbe0a0', '00bbe0af']]`
  - `UNCONDITIONAL_JUMP` [`00bbe0ac`](#insn-00bbe0ac) → [`00bbe0b4`](#insn-00bbe0b4)
- ブロック [`00bbe0b0`](#insn-00bbe0b0) 範囲 `[['00bbe0b0', '00bbe0b3']]`
  - `FALL_THROUGH` [`00bbe0b0`](#insn-00bbe0b0) → [`00bbe0b4`](#insn-00bbe0b4)
- ブロック [`00bbe0b4`](#insn-00bbe0b4) 範囲 `[['00bbe0b4', '00bbe0f3']]`
  - `CONDITIONAL_JUMP` [`00bbe0f0`](#insn-00bbe0f0) → [`00bbe10c`](#insn-00bbe10c)
  - `FALL_THROUGH` [`00bbe0f0`](#insn-00bbe0f0) → [`00bbe0f4`](#insn-00bbe0f4)
- ブロック [`00bbe0f4`](#insn-00bbe0f4) 範囲 `[['00bbe0f4', '00bbe0fb']]`
  - `CONDITIONAL_JUMP` [`00bbe0f8`](#insn-00bbe0f8) → [`00bbe110`](#insn-00bbe110)
  - `FALL_THROUGH` [`00bbe0f8`](#insn-00bbe0f8) → [`00bbe0fc`](#insn-00bbe0fc)
- ブロック [`00bbe0fc`](#insn-00bbe0fc) 範囲 `[['00bbe0fc', '00bbe10b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe108`](#insn-00bbe108) → [`00bbe110`](#insn-00bbe110)
- ブロック [`00bbe10c`](#insn-00bbe10c) 範囲 `[['00bbe10c', '00bbe10f']]`
  - `FALL_THROUGH` [`00bbe10c`](#insn-00bbe10c) → [`00bbe110`](#insn-00bbe110)
- ブロック [`00bbe110`](#insn-00bbe110) 範囲 `[['00bbe110', '00bbe14f']]`
  - `CONDITIONAL_JUMP` [`00bbe14c`](#insn-00bbe14c) → [`00bbe16c`](#insn-00bbe16c)
  - `FALL_THROUGH` [`00bbe14c`](#insn-00bbe14c) → [`00bbe150`](#insn-00bbe150)
- ブロック [`00bbe150`](#insn-00bbe150) 範囲 `[['00bbe150', '00bbe157']]`
  - `CONDITIONAL_JUMP` [`00bbe154`](#insn-00bbe154) → [`00bbe15c`](#insn-00bbe15c)
  - `FALL_THROUGH` [`00bbe154`](#insn-00bbe154) → [`00bbe158`](#insn-00bbe158)
- ブロック [`00bbe158`](#insn-00bbe158) 範囲 `[['00bbe158', '00bbe15b']]`
  - `FALL_THROUGH` [`00bbe158`](#insn-00bbe158) → [`00bbe15c`](#insn-00bbe15c)
- ブロック [`00bbe15c`](#insn-00bbe15c) 範囲 `[['00bbe15c', '00bbe167']]`
  - `CONDITIONAL_JUMP` [`00bbe164`](#insn-00bbe164) → [`00bbe180`](#insn-00bbe180)
  - `FALL_THROUGH` [`00bbe164`](#insn-00bbe164) → [`00bbe168`](#insn-00bbe168)
- ブロック [`00bbe168`](#insn-00bbe168) 範囲 `[['00bbe168', '00bbe16b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe168`](#insn-00bbe168) → [`00bbe184`](#insn-00bbe184)
- ブロック [`00bbe16c`](#insn-00bbe16c) 範囲 `[['00bbe16c', '00bbe177']]`
  - `CONDITIONAL_JUMP` [`00bbe174`](#insn-00bbe174) → [`00bbe1d4`](#insn-00bbe1d4)
  - `FALL_THROUGH` [`00bbe174`](#insn-00bbe174) → [`00bbe178`](#insn-00bbe178)
- ブロック [`00bbe178`](#insn-00bbe178) 範囲 `[['00bbe178', '00bbe17f']]`
  - `CONDITIONAL_JUMP` [`00bbe17c`](#insn-00bbe17c) → [`00bbe184`](#insn-00bbe184)
  - `FALL_THROUGH` [`00bbe17c`](#insn-00bbe17c) → [`00bbe180`](#insn-00bbe180)
- ブロック [`00bbe180`](#insn-00bbe180) 範囲 `[['00bbe180', '00bbe183']]`
  - `FALL_THROUGH` [`00bbe180`](#insn-00bbe180) → [`00bbe184`](#insn-00bbe184)
- ブロック [`00bbe184`](#insn-00bbe184) 範囲 `[['00bbe184', '00bbe18f']]`
  - `CONDITIONAL_JUMP` [`00bbe18c`](#insn-00bbe18c) → [`00bbe7dc`](#insn-00bbe7dc)
  - `FALL_THROUGH` [`00bbe18c`](#insn-00bbe18c) → [`00bbe190`](#insn-00bbe190)
- ブロック [`00bbe190`](#insn-00bbe190) 範囲 `[['00bbe190', '00bbe197']]`
  - `CONDITIONAL_JUMP` [`00bbe194`](#insn-00bbe194) → [`00bbe7dc`](#insn-00bbe7dc)
  - `FALL_THROUGH` [`00bbe194`](#insn-00bbe194) → [`00bbe198`](#insn-00bbe198)
- ブロック [`00bbe198`](#insn-00bbe198) 範囲 `[['00bbe198', '00bbe1a7']]`
  - `CONDITIONAL_JUMP` [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe7dc`](#insn-00bbe7dc)
  - `FALL_THROUGH` [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe1a8`](#insn-00bbe1a8)
- ブロック [`00bbe1a8`](#insn-00bbe1a8) 範囲 `[['00bbe1a8', '00bbe1bb']]`
  - `CONDITIONAL_JUMP` [`00bbe1b8`](#insn-00bbe1b8) → [`00bbe1dc`](#insn-00bbe1dc)
  - `FALL_THROUGH` [`00bbe1b8`](#insn-00bbe1b8) → [`00bbe1bc`](#insn-00bbe1bc)
- ブロック [`00bbe1bc`](#insn-00bbe1bc) 範囲 `[['00bbe1bc', '00bbe1c3']]`
  - `CONDITIONAL_JUMP` [`00bbe1c0`](#insn-00bbe1c0) → [`00bbe1e0`](#insn-00bbe1e0)
  - `FALL_THROUGH` [`00bbe1c0`](#insn-00bbe1c0) → [`00bbe1c4`](#insn-00bbe1c4)
- ブロック [`00bbe1c4`](#insn-00bbe1c4) 範囲 `[['00bbe1c4', '00bbe1d3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe1d0`](#insn-00bbe1d0) → [`00bbe1e0`](#insn-00bbe1e0)
- ブロック [`00bbe1d4`](#insn-00bbe1d4) 範囲 `[['00bbe1d4', '00bbe1db']]`
  - `UNCONDITIONAL_JUMP` [`00bbe1d8`](#insn-00bbe1d8) → [`00bbe7dc`](#insn-00bbe7dc)
- ブロック [`00bbe1dc`](#insn-00bbe1dc) 範囲 `[['00bbe1dc', '00bbe1df']]`
  - `FALL_THROUGH` [`00bbe1dc`](#insn-00bbe1dc) → [`00bbe1e0`](#insn-00bbe1e0)
- ブロック [`00bbe1e0`](#insn-00bbe1e0) 範囲 `[['00bbe1e0', '00bbe217']]`
  - `CONDITIONAL_JUMP` [`00bbe214`](#insn-00bbe214) → [`00bbe230`](#insn-00bbe230)
  - `FALL_THROUGH` [`00bbe214`](#insn-00bbe214) → [`00bbe218`](#insn-00bbe218)
- ブロック [`00bbe218`](#insn-00bbe218) 範囲 `[['00bbe218', '00bbe21f']]`
  - `CONDITIONAL_JUMP` [`00bbe21c`](#insn-00bbe21c) → [`00bbe234`](#insn-00bbe234)
  - `FALL_THROUGH` [`00bbe21c`](#insn-00bbe21c) → [`00bbe220`](#insn-00bbe220)
- ブロック [`00bbe220`](#insn-00bbe220) 範囲 `[['00bbe220', '00bbe22f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe22c`](#insn-00bbe22c) → [`00bbe234`](#insn-00bbe234)
- ブロック [`00bbe230`](#insn-00bbe230) 範囲 `[['00bbe230', '00bbe233']]`
  - `FALL_THROUGH` [`00bbe230`](#insn-00bbe230) → [`00bbe234`](#insn-00bbe234)
- ブロック [`00bbe234`](#insn-00bbe234) 範囲 `[['00bbe234', '00bbe273']]`
  - `CONDITIONAL_JUMP` [`00bbe270`](#insn-00bbe270) → [`00bbe28c`](#insn-00bbe28c)
  - `FALL_THROUGH` [`00bbe270`](#insn-00bbe270) → [`00bbe274`](#insn-00bbe274)
- ブロック [`00bbe274`](#insn-00bbe274) 範囲 `[['00bbe274', '00bbe27b']]`
  - `CONDITIONAL_JUMP` [`00bbe278`](#insn-00bbe278) → [`00bbe290`](#insn-00bbe290)
  - `FALL_THROUGH` [`00bbe278`](#insn-00bbe278) → [`00bbe27c`](#insn-00bbe27c)
- ブロック [`00bbe27c`](#insn-00bbe27c) 範囲 `[['00bbe27c', '00bbe28b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe288`](#insn-00bbe288) → [`00bbe290`](#insn-00bbe290)
- ブロック [`00bbe28c`](#insn-00bbe28c) 範囲 `[['00bbe28c', '00bbe28f']]`
  - `FALL_THROUGH` [`00bbe28c`](#insn-00bbe28c) → [`00bbe290`](#insn-00bbe290)
- ブロック [`00bbe290`](#insn-00bbe290) 範囲 `[['00bbe290', '00bbe2cf']]`
  - `CONDITIONAL_JUMP` [`00bbe2cc`](#insn-00bbe2cc) → [`00bbe2e8`](#insn-00bbe2e8)
  - `FALL_THROUGH` [`00bbe2cc`](#insn-00bbe2cc) → [`00bbe2d0`](#insn-00bbe2d0)
- ブロック [`00bbe2d0`](#insn-00bbe2d0) 範囲 `[['00bbe2d0', '00bbe2d7']]`
  - `CONDITIONAL_JUMP` [`00bbe2d4`](#insn-00bbe2d4) → [`00bbe2ec`](#insn-00bbe2ec)
  - `FALL_THROUGH` [`00bbe2d4`](#insn-00bbe2d4) → [`00bbe2d8`](#insn-00bbe2d8)
- ブロック [`00bbe2d8`](#insn-00bbe2d8) 範囲 `[['00bbe2d8', '00bbe2e7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe2e4`](#insn-00bbe2e4) → [`00bbe2ec`](#insn-00bbe2ec)
- ブロック [`00bbe2e8`](#insn-00bbe2e8) 範囲 `[['00bbe2e8', '00bbe2eb']]`
  - `FALL_THROUGH` [`00bbe2e8`](#insn-00bbe2e8) → [`00bbe2ec`](#insn-00bbe2ec)
- ブロック [`00bbe2ec`](#insn-00bbe2ec) 範囲 `[['00bbe2ec', '00bbe32b']]`
  - `CONDITIONAL_JUMP` [`00bbe328`](#insn-00bbe328) → [`00bbe344`](#insn-00bbe344)
  - `FALL_THROUGH` [`00bbe328`](#insn-00bbe328) → [`00bbe32c`](#insn-00bbe32c)
- ブロック [`00bbe32c`](#insn-00bbe32c) 範囲 `[['00bbe32c', '00bbe333']]`
  - `CONDITIONAL_JUMP` [`00bbe330`](#insn-00bbe330) → [`00bbe348`](#insn-00bbe348)
  - `FALL_THROUGH` [`00bbe330`](#insn-00bbe330) → [`00bbe334`](#insn-00bbe334)
- ブロック [`00bbe334`](#insn-00bbe334) 範囲 `[['00bbe334', '00bbe343']]`
  - `UNCONDITIONAL_JUMP` [`00bbe340`](#insn-00bbe340) → [`00bbe348`](#insn-00bbe348)
- ブロック [`00bbe344`](#insn-00bbe344) 範囲 `[['00bbe344', '00bbe347']]`
  - `FALL_THROUGH` [`00bbe344`](#insn-00bbe344) → [`00bbe348`](#insn-00bbe348)
- ブロック [`00bbe348`](#insn-00bbe348) 範囲 `[['00bbe348', '00bbe387']]`
  - `CONDITIONAL_JUMP` [`00bbe384`](#insn-00bbe384) → [`00bbe3a0`](#insn-00bbe3a0)
  - `FALL_THROUGH` [`00bbe384`](#insn-00bbe384) → [`00bbe388`](#insn-00bbe388)
- ブロック [`00bbe388`](#insn-00bbe388) 範囲 `[['00bbe388', '00bbe38f']]`
  - `CONDITIONAL_JUMP` [`00bbe38c`](#insn-00bbe38c) → [`00bbe3a4`](#insn-00bbe3a4)
  - `FALL_THROUGH` [`00bbe38c`](#insn-00bbe38c) → [`00bbe390`](#insn-00bbe390)
- ブロック [`00bbe390`](#insn-00bbe390) 範囲 `[['00bbe390', '00bbe39f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe39c`](#insn-00bbe39c) → [`00bbe3a4`](#insn-00bbe3a4)
- ブロック [`00bbe3a0`](#insn-00bbe3a0) 範囲 `[['00bbe3a0', '00bbe3a3']]`
  - `FALL_THROUGH` [`00bbe3a0`](#insn-00bbe3a0) → [`00bbe3a4`](#insn-00bbe3a4)
- ブロック [`00bbe3a4`](#insn-00bbe3a4) 範囲 `[['00bbe3a4', '00bbe3e3']]`
  - `CONDITIONAL_JUMP` [`00bbe3e0`](#insn-00bbe3e0) → [`00bbe3fc`](#insn-00bbe3fc)
  - `FALL_THROUGH` [`00bbe3e0`](#insn-00bbe3e0) → [`00bbe3e4`](#insn-00bbe3e4)
- ブロック [`00bbe3e4`](#insn-00bbe3e4) 範囲 `[['00bbe3e4', '00bbe3eb']]`
  - `CONDITIONAL_JUMP` [`00bbe3e8`](#insn-00bbe3e8) → [`00bbe400`](#insn-00bbe400)
  - `FALL_THROUGH` [`00bbe3e8`](#insn-00bbe3e8) → [`00bbe3ec`](#insn-00bbe3ec)
- ブロック [`00bbe3ec`](#insn-00bbe3ec) 範囲 `[['00bbe3ec', '00bbe3fb']]`
  - `UNCONDITIONAL_JUMP` [`00bbe3f8`](#insn-00bbe3f8) → [`00bbe400`](#insn-00bbe400)
- ブロック [`00bbe3fc`](#insn-00bbe3fc) 範囲 `[['00bbe3fc', '00bbe3ff']]`
  - `FALL_THROUGH` [`00bbe3fc`](#insn-00bbe3fc) → [`00bbe400`](#insn-00bbe400)
- ブロック [`00bbe400`](#insn-00bbe400) 範囲 `[['00bbe400', '00bbe43f']]`
  - `CONDITIONAL_JUMP` [`00bbe43c`](#insn-00bbe43c) → [`00bbe458`](#insn-00bbe458)
  - `FALL_THROUGH` [`00bbe43c`](#insn-00bbe43c) → [`00bbe440`](#insn-00bbe440)
- ブロック [`00bbe440`](#insn-00bbe440) 範囲 `[['00bbe440', '00bbe447']]`
  - `CONDITIONAL_JUMP` [`00bbe444`](#insn-00bbe444) → [`00bbe45c`](#insn-00bbe45c)
  - `FALL_THROUGH` [`00bbe444`](#insn-00bbe444) → [`00bbe448`](#insn-00bbe448)
- ブロック [`00bbe448`](#insn-00bbe448) 範囲 `[['00bbe448', '00bbe457']]`
  - `UNCONDITIONAL_JUMP` [`00bbe454`](#insn-00bbe454) → [`00bbe45c`](#insn-00bbe45c)
- ブロック [`00bbe458`](#insn-00bbe458) 範囲 `[['00bbe458', '00bbe45b']]`
  - `FALL_THROUGH` [`00bbe458`](#insn-00bbe458) → [`00bbe45c`](#insn-00bbe45c)
- ブロック [`00bbe45c`](#insn-00bbe45c) 範囲 `[['00bbe45c', '00bbe49b']]`
  - `CONDITIONAL_JUMP` [`00bbe498`](#insn-00bbe498) → [`00bbe4b4`](#insn-00bbe4b4)
  - `FALL_THROUGH` [`00bbe498`](#insn-00bbe498) → [`00bbe49c`](#insn-00bbe49c)
- ブロック [`00bbe49c`](#insn-00bbe49c) 範囲 `[['00bbe49c', '00bbe4a3']]`
  - `CONDITIONAL_JUMP` [`00bbe4a0`](#insn-00bbe4a0) → [`00bbe4b8`](#insn-00bbe4b8)
  - `FALL_THROUGH` [`00bbe4a0`](#insn-00bbe4a0) → [`00bbe4a4`](#insn-00bbe4a4)
- ブロック [`00bbe4a4`](#insn-00bbe4a4) 範囲 `[['00bbe4a4', '00bbe4b3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe4b0`](#insn-00bbe4b0) → [`00bbe4b8`](#insn-00bbe4b8)
- ブロック [`00bbe4b4`](#insn-00bbe4b4) 範囲 `[['00bbe4b4', '00bbe4b7']]`
  - `FALL_THROUGH` [`00bbe4b4`](#insn-00bbe4b4) → [`00bbe4b8`](#insn-00bbe4b8)
- ブロック [`00bbe4b8`](#insn-00bbe4b8) 範囲 `[['00bbe4b8', '00bbe4f7']]`
  - `CONDITIONAL_JUMP` [`00bbe4f4`](#insn-00bbe4f4) → [`00bbe600`](#insn-00bbe600)
  - `FALL_THROUGH` [`00bbe4f4`](#insn-00bbe4f4) → [`00bbe4f8`](#insn-00bbe4f8)
- ブロック [`00bbe4f8`](#insn-00bbe4f8) 範囲 `[['00bbe4f8', '00bbe4ff']]`
  - `CONDITIONAL_JUMP` [`00bbe4fc`](#insn-00bbe4fc) → [`00bbe600`](#insn-00bbe600)
  - `FALL_THROUGH` [`00bbe4fc`](#insn-00bbe4fc) → [`00bbe500`](#insn-00bbe500)
- ブロック [`00bbe500`](#insn-00bbe500) 範囲 `[['00bbe500', '00bbe52b']]`
  - `CONDITIONAL_JUMP` [`00bbe528`](#insn-00bbe528) → [`00bbe540`](#insn-00bbe540)
  - `FALL_THROUGH` [`00bbe528`](#insn-00bbe528) → [`00bbe52c`](#insn-00bbe52c)
- ブロック [`00bbe52c`](#insn-00bbe52c) 範囲 `[['00bbe52c', '00bbe53f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe53c`](#insn-00bbe53c) → [`00bbe584`](#insn-00bbe584)
- ブロック [`00bbe540`](#insn-00bbe540) 範囲 `[['00bbe540', '00bbe543']]`
  - `CONDITIONAL_JUMP` [`00bbe540`](#insn-00bbe540) → [`00bbe584`](#insn-00bbe584)
  - `FALL_THROUGH` [`00bbe540`](#insn-00bbe540) → [`00bbe544`](#insn-00bbe544)
- ブロック [`00bbe544`](#insn-00bbe544) 範囲 `[['00bbe544', '00bbe553']]`
  - `CONDITIONAL_JUMP` [`00bbe550`](#insn-00bbe550) → [`00bbe580`](#insn-00bbe580)
  - `FALL_THROUGH` [`00bbe550`](#insn-00bbe550) → [`00bbe554`](#insn-00bbe554)
- ブロック [`00bbe554`](#insn-00bbe554) 範囲 `[['00bbe554', '00bbe55f']]`
  - `CONDITIONAL_JUMP` [`00bbe55c`](#insn-00bbe55c) → [`00bbe574`](#insn-00bbe574)
  - `FALL_THROUGH` [`00bbe55c`](#insn-00bbe55c) → [`00bbe560`](#insn-00bbe560)
- ブロック [`00bbe560`](#insn-00bbe560) 範囲 `[['00bbe560', '00bbe56b']]`
  - `CONDITIONAL_JUMP` [`00bbe568`](#insn-00bbe568) → [`00bbe580`](#insn-00bbe580)
  - `FALL_THROUGH` [`00bbe568`](#insn-00bbe568) → [`00bbe56c`](#insn-00bbe56c)
- ブロック [`00bbe56c`](#insn-00bbe56c) 範囲 `[['00bbe56c', '00bbe573']]`
  - `CONDITIONAL_JUMP` [`00bbe570`](#insn-00bbe570) → [`00bbe560`](#insn-00bbe560)
  - `FALL_THROUGH` [`00bbe570`](#insn-00bbe570) → [`00bbe574`](#insn-00bbe574)
- ブロック [`00bbe574`](#insn-00bbe574) 範囲 `[['00bbe574', '00bbe57f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe57c`](#insn-00bbe57c) → [`00bbe560`](#insn-00bbe560)
- ブロック [`00bbe580`](#insn-00bbe580) 範囲 `[['00bbe580', '00bbe583']]`
  - `FALL_THROUGH` [`00bbe580`](#insn-00bbe580) → [`00bbe584`](#insn-00bbe584)
- ブロック [`00bbe584`](#insn-00bbe584) 範囲 `[['00bbe584', '00bbe587']]`
  - `CONDITIONAL_JUMP` [`00bbe584`](#insn-00bbe584) → [`00bbe600`](#insn-00bbe600)
  - `FALL_THROUGH` [`00bbe584`](#insn-00bbe584) → [`00bbe588`](#insn-00bbe588)
- ブロック [`00bbe588`](#insn-00bbe588) 範囲 `[['00bbe588', '00bbe58f']]`
  - `FALL_THROUGH` [`00bbe58c`](#insn-00bbe58c) → [`00bbe590`](#insn-00bbe590)
- ブロック [`00bbe590`](#insn-00bbe590) 範囲 `[['00bbe590', '00bbe5a3']]`
  - `CONDITIONAL_JUMP` [`00bbe5a0`](#insn-00bbe5a0) → [`00bbe5bc`](#insn-00bbe5bc)
  - `FALL_THROUGH` [`00bbe5a0`](#insn-00bbe5a0) → [`00bbe5a4`](#insn-00bbe5a4)
- ブロック [`00bbe5a4`](#insn-00bbe5a4) 範囲 `[['00bbe5a4', '00bbe5ab']]`
  - `CONDITIONAL_JUMP` [`00bbe5a8`](#insn-00bbe5a8) → [`00bbe5c0`](#insn-00bbe5c0)
  - `FALL_THROUGH` [`00bbe5a8`](#insn-00bbe5a8) → [`00bbe5ac`](#insn-00bbe5ac)
- ブロック [`00bbe5ac`](#insn-00bbe5ac) 範囲 `[['00bbe5ac', '00bbe5bb']]`
  - `UNCONDITIONAL_JUMP` [`00bbe5b8`](#insn-00bbe5b8) → [`00bbe5c0`](#insn-00bbe5c0)
- ブロック [`00bbe5bc`](#insn-00bbe5bc) 範囲 `[['00bbe5bc', '00bbe5bf']]`
  - `FALL_THROUGH` [`00bbe5bc`](#insn-00bbe5bc) → [`00bbe5c0`](#insn-00bbe5c0)
- ブロック [`00bbe5c0`](#insn-00bbe5c0) 範囲 `[['00bbe5c0', '00bbe5ff']]`
  - `CONDITIONAL_JUMP` [`00bbe5fc`](#insn-00bbe5fc) → [`00bbe590`](#insn-00bbe590)
  - `FALL_THROUGH` [`00bbe5fc`](#insn-00bbe5fc) → [`00bbe600`](#insn-00bbe600)
- ブロック [`00bbe600`](#insn-00bbe600) 範囲 `[['00bbe600', '00bbe613']]`
  - `CONDITIONAL_JUMP` [`00bbe610`](#insn-00bbe610) → [`00bbe62c`](#insn-00bbe62c)
  - `FALL_THROUGH` [`00bbe610`](#insn-00bbe610) → [`00bbe614`](#insn-00bbe614)
- ブロック [`00bbe614`](#insn-00bbe614) 範囲 `[['00bbe614', '00bbe61b']]`
  - `CONDITIONAL_JUMP` [`00bbe618`](#insn-00bbe618) → [`00bbe630`](#insn-00bbe630)
  - `FALL_THROUGH` [`00bbe618`](#insn-00bbe618) → [`00bbe61c`](#insn-00bbe61c)
- ブロック [`00bbe61c`](#insn-00bbe61c) 範囲 `[['00bbe61c', '00bbe62b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe628`](#insn-00bbe628) → [`00bbe630`](#insn-00bbe630)
- ブロック [`00bbe62c`](#insn-00bbe62c) 範囲 `[['00bbe62c', '00bbe62f']]`
  - `FALL_THROUGH` [`00bbe62c`](#insn-00bbe62c) → [`00bbe630`](#insn-00bbe630)
- ブロック [`00bbe630`](#insn-00bbe630) 範囲 `[['00bbe630', '00bbe66f']]`
  - `CONDITIONAL_JUMP` [`00bbe66c`](#insn-00bbe66c) → [`00bbe778`](#insn-00bbe778)
  - `FALL_THROUGH` [`00bbe66c`](#insn-00bbe66c) → [`00bbe670`](#insn-00bbe670)
- ブロック [`00bbe670`](#insn-00bbe670) 範囲 `[['00bbe670', '00bbe677']]`
  - `CONDITIONAL_JUMP` [`00bbe674`](#insn-00bbe674) → [`00bbe778`](#insn-00bbe778)
  - `FALL_THROUGH` [`00bbe674`](#insn-00bbe674) → [`00bbe678`](#insn-00bbe678)
- ブロック [`00bbe678`](#insn-00bbe678) 範囲 `[['00bbe678', '00bbe6a3']]`
  - `CONDITIONAL_JUMP` [`00bbe6a0`](#insn-00bbe6a0) → [`00bbe6b8`](#insn-00bbe6b8)
  - `FALL_THROUGH` [`00bbe6a0`](#insn-00bbe6a0) → [`00bbe6a4`](#insn-00bbe6a4)
- ブロック [`00bbe6a4`](#insn-00bbe6a4) 範囲 `[['00bbe6a4', '00bbe6b7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6fc`](#insn-00bbe6fc)
- ブロック [`00bbe6b8`](#insn-00bbe6b8) 範囲 `[['00bbe6b8', '00bbe6bb']]`
  - `CONDITIONAL_JUMP` [`00bbe6b8`](#insn-00bbe6b8) → [`00bbe6fc`](#insn-00bbe6fc)
  - `FALL_THROUGH` [`00bbe6b8`](#insn-00bbe6b8) → [`00bbe6bc`](#insn-00bbe6bc)
- ブロック [`00bbe6bc`](#insn-00bbe6bc) 範囲 `[['00bbe6bc', '00bbe6cb']]`
  - `CONDITIONAL_JUMP` [`00bbe6c8`](#insn-00bbe6c8) → [`00bbe6f8`](#insn-00bbe6f8)
  - `FALL_THROUGH` [`00bbe6c8`](#insn-00bbe6c8) → [`00bbe6cc`](#insn-00bbe6cc)
- ブロック [`00bbe6cc`](#insn-00bbe6cc) 範囲 `[['00bbe6cc', '00bbe6d7']]`
  - `CONDITIONAL_JUMP` [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe6ec`](#insn-00bbe6ec)
  - `FALL_THROUGH` [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe6d8`](#insn-00bbe6d8)
- ブロック [`00bbe6d8`](#insn-00bbe6d8) 範囲 `[['00bbe6d8', '00bbe6e3']]`
  - `CONDITIONAL_JUMP` [`00bbe6e0`](#insn-00bbe6e0) → [`00bbe6f8`](#insn-00bbe6f8)
  - `FALL_THROUGH` [`00bbe6e0`](#insn-00bbe6e0) → [`00bbe6e4`](#insn-00bbe6e4)
- ブロック [`00bbe6e4`](#insn-00bbe6e4) 範囲 `[['00bbe6e4', '00bbe6eb']]`
  - `CONDITIONAL_JUMP` [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe6d8`](#insn-00bbe6d8)
  - `FALL_THROUGH` [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe6ec`](#insn-00bbe6ec)
- ブロック [`00bbe6ec`](#insn-00bbe6ec) 範囲 `[['00bbe6ec', '00bbe6f7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6f4`](#insn-00bbe6f4) → [`00bbe6d8`](#insn-00bbe6d8)
- ブロック [`00bbe6f8`](#insn-00bbe6f8) 範囲 `[['00bbe6f8', '00bbe6fb']]`
  - `FALL_THROUGH` [`00bbe6f8`](#insn-00bbe6f8) → [`00bbe6fc`](#insn-00bbe6fc)
- ブロック [`00bbe6fc`](#insn-00bbe6fc) 範囲 `[['00bbe6fc', '00bbe6ff']]`
  - `CONDITIONAL_JUMP` [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe778`](#insn-00bbe778)
  - `FALL_THROUGH` [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe700`](#insn-00bbe700)
- ブロック [`00bbe700`](#insn-00bbe700) 範囲 `[['00bbe700', '00bbe707']]`
  - `FALL_THROUGH` [`00bbe704`](#insn-00bbe704) → [`00bbe708`](#insn-00bbe708)
- ブロック [`00bbe708`](#insn-00bbe708) 範囲 `[['00bbe708', '00bbe71b']]`
  - `CONDITIONAL_JUMP` [`00bbe718`](#insn-00bbe718) → [`00bbe734`](#insn-00bbe734)
  - `FALL_THROUGH` [`00bbe718`](#insn-00bbe718) → [`00bbe71c`](#insn-00bbe71c)
- ブロック [`00bbe71c`](#insn-00bbe71c) 範囲 `[['00bbe71c', '00bbe723']]`
  - `CONDITIONAL_JUMP` [`00bbe720`](#insn-00bbe720) → [`00bbe738`](#insn-00bbe738)
  - `FALL_THROUGH` [`00bbe720`](#insn-00bbe720) → [`00bbe724`](#insn-00bbe724)
- ブロック [`00bbe724`](#insn-00bbe724) 範囲 `[['00bbe724', '00bbe733']]`
  - `UNCONDITIONAL_JUMP` [`00bbe730`](#insn-00bbe730) → [`00bbe738`](#insn-00bbe738)
- ブロック [`00bbe734`](#insn-00bbe734) 範囲 `[['00bbe734', '00bbe737']]`
  - `FALL_THROUGH` [`00bbe734`](#insn-00bbe734) → [`00bbe738`](#insn-00bbe738)
- ブロック [`00bbe738`](#insn-00bbe738) 範囲 `[['00bbe738', '00bbe777']]`
  - `CONDITIONAL_JUMP` [`00bbe774`](#insn-00bbe774) → [`00bbe708`](#insn-00bbe708)
  - `FALL_THROUGH` [`00bbe774`](#insn-00bbe774) → [`00bbe778`](#insn-00bbe778)
- ブロック [`00bbe778`](#insn-00bbe778) 範囲 `[['00bbe778', '00bbe78b']]`
  - `CONDITIONAL_JUMP` [`00bbe788`](#insn-00bbe788) → [`00bbe7a4`](#insn-00bbe7a4)
  - `FALL_THROUGH` [`00bbe788`](#insn-00bbe788) → [`00bbe78c`](#insn-00bbe78c)
- ブロック [`00bbe78c`](#insn-00bbe78c) 範囲 `[['00bbe78c', '00bbe793']]`
  - `CONDITIONAL_JUMP` [`00bbe790`](#insn-00bbe790) → [`00bbe7a8`](#insn-00bbe7a8)
  - `FALL_THROUGH` [`00bbe790`](#insn-00bbe790) → [`00bbe794`](#insn-00bbe794)
- ブロック [`00bbe794`](#insn-00bbe794) 範囲 `[['00bbe794', '00bbe7a3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe7a0`](#insn-00bbe7a0) → [`00bbe7a8`](#insn-00bbe7a8)
- ブロック [`00bbe7a4`](#insn-00bbe7a4) 範囲 `[['00bbe7a4', '00bbe7a7']]`
  - `FALL_THROUGH` [`00bbe7a4`](#insn-00bbe7a4) → [`00bbe7a8`](#insn-00bbe7a8)
- ブロック [`00bbe7a8`](#insn-00bbe7a8) 範囲 `[['00bbe7a8', '00bbe7db']]`
  - `FALL_THROUGH` [`00bbe7d8`](#insn-00bbe7d8) → [`00bbe7dc`](#insn-00bbe7dc)
- ブロック [`00bbe7dc`](#insn-00bbe7dc) 範囲 `[['00bbe7dc', '00bbe7ef']]`
  - `CONDITIONAL_JUMP` [`00bbe7ec`](#insn-00bbe7ec) → [`00bbe7f8`](#insn-00bbe7f8)
  - `FALL_THROUGH` [`00bbe7ec`](#insn-00bbe7ec) → [`00bbe7f0`](#insn-00bbe7f0)
- ブロック [`00bbe7f0`](#insn-00bbe7f0) 範囲 `[['00bbe7f0', '00bbe7f7']]`
  - `FALL_THROUGH` [`00bbe7f4`](#insn-00bbe7f4) → [`00bbe7f8`](#insn-00bbe7f8)
- ブロック [`00bbe7f8`](#insn-00bbe7f8) 範囲 `[['00bbe7f8', '00bbe7ff']]`
  - `CONDITIONAL_JUMP` [`00bbe7fc`](#insn-00bbe7fc) → [`00bbe808`](#insn-00bbe808)
  - `FALL_THROUGH` [`00bbe7fc`](#insn-00bbe7fc) → [`00bbe800`](#insn-00bbe800)
- ブロック [`00bbe800`](#insn-00bbe800) 範囲 `[['00bbe800', '00bbe807']]`
  - `FALL_THROUGH` [`00bbe804`](#insn-00bbe804) → [`00bbe808`](#insn-00bbe808)
- ブロック [`00bbe808`](#insn-00bbe808) 範囲 `[['00bbe808', '00bbe827']]`
  - `CONDITIONAL_JUMP` [`00bbe824`](#insn-00bbe824) → [`00bbe848`](#insn-00bbe848)
  - `FALL_THROUGH` [`00bbe824`](#insn-00bbe824) → [`00bbe828`](#insn-00bbe828)
- ブロック [`00bbe828`](#insn-00bbe828) 範囲 `[['00bbe828', '00bbe847']]`
- ブロック [`00bbe848`](#insn-00bbe848) 範囲 `[['00bbe848', '00bbe84b']]`

## 命令位置別の参照

- [`00bbda4c`](#insn-00bbda4c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda50`](#insn-00bbda50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda54`](#insn-00bbda54) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda58`](#insn-00bbda58) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda5c`](#insn-00bbda5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda60`](#insn-00bbda60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda84`](#insn-00bbda84) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda88`](#insn-00bbda88) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda8c`](#insn-00bbda8c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda90`](#insn-00bbda90) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda94`](#insn-00bbda94) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda98`](#insn-00bbda98) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda9c`](#insn-00bbda9c) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaa0`](#insn-00bbdaa0) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaa4`](#insn-00bbdaa4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaa8`](#insn-00bbdaa8) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaac`](#insn-00bbdaac) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdab0`](#insn-00bbdab0) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdab4`](#insn-00bbdab4) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdab8`](#insn-00bbdab8) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdabc`](#insn-00bbdabc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdac0`](#insn-00bbdac0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdac4`](#insn-00bbdac4) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdac8`](#insn-00bbdac8) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdacc`](#insn-00bbdacc) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdad0`](#insn-00bbdad0) → `Stack[-0x230]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdad4`](#insn-00bbdad4) → `Stack[-0x250]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdad8`](#insn-00bbdad8) → `Stack[-0x270]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdadc`](#insn-00bbdadc) → `Stack[-0x290]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdae0`](#insn-00bbdae0) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdae4`](#insn-00bbdae4) → `Stack[-0x2d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdae8`](#insn-00bbdae8) → `Stack[-0x2f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaec`](#insn-00bbdaec) → `Stack[-0x300]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaf0`](#insn-00bbdaf0) → `Stack[-0x308]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb10`](#insn-00bbdb10) → [`00bbdb28`](#insn-00bbdb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb18`](#insn-00bbdb18) → [`00bbdb28`](#insn-00bbdb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb3c`](#insn-00bbdb3c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdb40`](#insn-00bbdb40) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb50`](#insn-00bbdb50) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb64`](#insn-00bbdb64) → [`00bbdb80`](#insn-00bbdb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb6c`](#insn-00bbdb6c) → [`00bbdb84`](#insn-00bbdb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb7c`](#insn-00bbdb7c) → [`00bbdb84`](#insn-00bbdb84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb94`](#insn-00bbdb94) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdb9c`](#insn-00bbdb9c) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbac`](#insn-00bbdbac) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbc4`](#insn-00bbdbc4) → [`00bbdd6c`](#insn-00bbdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbcc`](#insn-00bbdbcc) → [`00bbdd6c`](#insn-00bbdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbdc`](#insn-00bbdbdc) → [`00bbdd6c`](#insn-00bbdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbe4`](#insn-00bbdbe4) → [`00bbdd6c`](#insn-00bbdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbec`](#insn-00bbdbec) → `Stack[-0x340]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbfc`](#insn-00bbdbfc) → [`00bbdc10`](#insn-00bbdc10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc0c`](#insn-00bbdc0c) → [`00bbdd60`](#insn-00bbdd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc44`](#insn-00bbdc44) → [`00bbdc88`](#insn-00bbdc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc4c`](#insn-00bbdc4c) → [`00bbdc5c`](#insn-00bbdc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc6c`](#insn-00bbdc6c) → [`00bbdc94`](#insn-00bbdc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc74`](#insn-00bbdc74) → [`00bbdc94`](#insn-00bbdc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc84`](#insn-00bbdc84) → [`00bbdc98`](#insn-00bbdc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdc8c`](#insn-00bbdc8c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdc90`](#insn-00bbdc90) → [`00bbdc98`](#insn-00bbdc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdca8`](#insn-00bbdca8) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcb8`](#insn-00bbdcb8) → [`0046d5a8`](../0046d/0046d5a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d5a8` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcc4`](#insn-00bbdcc4) → [`00bbdd30`](#insn-00bbdd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdccc`](#insn-00bbdccc) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcd0`](#insn-00bbdcd0) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcd4`](#insn-00bbdcd4) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcd8`](#insn-00bbdcd8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcdc`](#insn-00bbdcdc) → `Stack[-0x318]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdce0`](#insn-00bbdce0) → `Stack[-0x320]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcfc`](#insn-00bbdcfc) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd04`](#insn-00bbdd04) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd08`](#insn-00bbdd08) → [`00bbdd18`](#insn-00bbdd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd0c`](#insn-00bbdd0c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd14`](#insn-00bbdd14) → [`00bbdd1c`](#insn-00bbdd1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd1c`](#insn-00bbdd1c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd20`](#insn-00bbdd20) → [`00c5b5e0`](../00c5b/00c5b5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd24`](#insn-00bbdd24) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd2c`](#insn-00bbdd2c) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd38`](#insn-00bbdd38) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd48`](#insn-00bbdd48) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd4c`](#insn-00bbdd4c) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd50`](#insn-00bbdd50) → [`00bbdc00`](#insn-00bbdc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd54`](#insn-00bbdd54) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd58`](#insn-00bbdd58) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd5c`](#insn-00bbdd5c) → [`00bbdc00`](#insn-00bbdc00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd60`](#insn-00bbdd60) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd78`](#insn-00bbdd78) → [`00bbde40`](#insn-00bbde40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd80`](#insn-00bbdd80) → [`00bbde40`](#insn-00bbde40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd90`](#insn-00bbdd90) → [`00bbde40`](#insn-00bbde40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd94`](#insn-00bbdd94) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd98`](#insn-00bbdd98) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdda8`](#insn-00bbdda8) → [`00bbddf0`](#insn-00bbddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddac`](#insn-00bbddac) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddb4`](#insn-00bbddb4) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bbddcc`](#insn-00bbddcc) → [`00bbdddc`](#insn-00bbdddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddd8`](#insn-00bbddd8) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00bbdddc`](#insn-00bbdddc) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde0`](#insn-00bbdde0) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdde4`](#insn-00bbdde4) → [`00bbddf0`](#insn-00bbddf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbddec`](#insn-00bbddec) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde18`](#insn-00bbde18) → `Stack[-0x328]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde28`](#insn-00bbde28) → `Stack[-0x330]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde34`](#insn-00bbde34) → [`00c5d570`](../00c5d/00c5d570.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d570` · 推定シンボル `None` · 推定型 `None`
- [`00bbde4c`](#insn-00bbde4c) → [`00bbde68`](#insn-00bbde68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde54`](#insn-00bbde54) → [`00bbde6c`](#insn-00bbde6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde64`](#insn-00bbde64) → [`00bbde6c`](#insn-00bbde6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde7c`](#insn-00bbde7c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbde84`](#insn-00bbde84) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbde94`](#insn-00bbde94) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdea8`](#insn-00bbdea8) → [`00bbdec4`](#insn-00bbdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdec8`](#insn-00bbdec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdec0`](#insn-00bbdec0) → [`00bbdec8`](#insn-00bbdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbded8`](#insn-00bbded8) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdee0`](#insn-00bbdee0) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdef0`](#insn-00bbdef0) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf08`](#insn-00bbdf08) → [`00bbdf24`](#insn-00bbdf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf10`](#insn-00bbdf10) → [`00bbdf28`](#insn-00bbdf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf20`](#insn-00bbdf20) → [`00bbdf28`](#insn-00bbdf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf34`](#insn-00bbdf34) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdf38`](#insn-00bbdf38) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf48`](#insn-00bbdf48) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf5c`](#insn-00bbdf5c) → [`00bbdf78`](#insn-00bbdf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf64`](#insn-00bbdf64) → [`00bbdf7c`](#insn-00bbdf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf74`](#insn-00bbdf74) → [`00bbdf7c`](#insn-00bbdf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf8c`](#insn-00bbdf8c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbdf94`](#insn-00bbdf94) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfa4`](#insn-00bbdfa4) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfb8`](#insn-00bbdfb8) → [`00bbdff4`](#insn-00bbdff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfc0`](#insn-00bbdfc0) → [`00bbdfd0`](#insn-00bbdfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfd4`](#insn-00bbdfd4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfd8`](#insn-00bbdfd8) → [`00bbe000`](#insn-00bbe000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfe0`](#insn-00bbdfe0) → [`00bbe004`](#insn-00bbe004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdff0`](#insn-00bbdff0) → [`00bbe004`](#insn-00bbe004) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdff8`](#insn-00bbdff8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdffc`](#insn-00bbdffc) → [`00bbe004`](#insn-00bbe004) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe010`](#insn-00bbe010) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe014`](#insn-00bbe014) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe024`](#insn-00bbe024) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe038`](#insn-00bbe038) → [`00bbe054`](#insn-00bbe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe040`](#insn-00bbe040) → [`00bbe058`](#insn-00bbe058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe050`](#insn-00bbe050) → [`00bbe058`](#insn-00bbe058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe068`](#insn-00bbe068) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe070`](#insn-00bbe070) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe080`](#insn-00bbe080) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe094`](#insn-00bbe094) → [`00bbe0b0`](#insn-00bbe0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe09c`](#insn-00bbe09c) → [`00bbe0b4`](#insn-00bbe0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0ac`](#insn-00bbe0ac) → [`00bbe0b4`](#insn-00bbe0b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0c4`](#insn-00bbe0c4) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe0cc`](#insn-00bbe0cc) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0dc`](#insn-00bbe0dc) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0f0`](#insn-00bbe0f0) → [`00bbe10c`](#insn-00bbe10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0f8`](#insn-00bbe0f8) → [`00bbe110`](#insn-00bbe110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe108`](#insn-00bbe108) → [`00bbe110`](#insn-00bbe110) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe120`](#insn-00bbe120) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe128`](#insn-00bbe128) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe138`](#insn-00bbe138) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe14c`](#insn-00bbe14c) → [`00bbe16c`](#insn-00bbe16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe154`](#insn-00bbe154) → [`00bbe15c`](#insn-00bbe15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe15c`](#insn-00bbe15c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe164`](#insn-00bbe164) → [`00bbe180`](#insn-00bbe180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe168`](#insn-00bbe168) → [`00bbe184`](#insn-00bbe184) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe170`](#insn-00bbe170) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe174`](#insn-00bbe174) → [`00bbe1d4`](#insn-00bbe1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe17c`](#insn-00bbe17c) → [`00bbe184`](#insn-00bbe184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe188`](#insn-00bbe188) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe18c`](#insn-00bbe18c) → [`00bbe7dc`](#insn-00bbe7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe194`](#insn-00bbe194) → [`00bbe7dc`](#insn-00bbe7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe7dc`](#insn-00bbe7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1b8`](#insn-00bbe1b8) → [`00bbe1dc`](#insn-00bbe1dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1c0`](#insn-00bbe1c0) → [`00bbe1e0`](#insn-00bbe1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1d0`](#insn-00bbe1d0) → [`00bbe1e0`](#insn-00bbe1e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1d4`](#insn-00bbe1d4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1d8`](#insn-00bbe1d8) → [`00bbe7dc`](#insn-00bbe7dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1ec`](#insn-00bbe1ec) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe1f0`](#insn-00bbe1f0) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe200`](#insn-00bbe200) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe214`](#insn-00bbe214) → [`00bbe230`](#insn-00bbe230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe21c`](#insn-00bbe21c) → [`00bbe234`](#insn-00bbe234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe22c`](#insn-00bbe22c) → [`00bbe234`](#insn-00bbe234) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe244`](#insn-00bbe244) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe24c`](#insn-00bbe24c) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe25c`](#insn-00bbe25c) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe270`](#insn-00bbe270) → [`00bbe28c`](#insn-00bbe28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe278`](#insn-00bbe278) → [`00bbe290`](#insn-00bbe290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe288`](#insn-00bbe288) → [`00bbe290`](#insn-00bbe290) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2a0`](#insn-00bbe2a0) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe2a8`](#insn-00bbe2a8) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2b8`](#insn-00bbe2b8) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2cc`](#insn-00bbe2cc) → [`00bbe2e8`](#insn-00bbe2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2d4`](#insn-00bbe2d4) → [`00bbe2ec`](#insn-00bbe2ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2e4`](#insn-00bbe2e4) → [`00bbe2ec`](#insn-00bbe2ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2fc`](#insn-00bbe2fc) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe304`](#insn-00bbe304) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe314`](#insn-00bbe314) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe328`](#insn-00bbe328) → [`00bbe344`](#insn-00bbe344) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe330`](#insn-00bbe330) → [`00bbe348`](#insn-00bbe348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe340`](#insn-00bbe340) → [`00bbe348`](#insn-00bbe348) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe358`](#insn-00bbe358) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe360`](#insn-00bbe360) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe370`](#insn-00bbe370) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe384`](#insn-00bbe384) → [`00bbe3a0`](#insn-00bbe3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe38c`](#insn-00bbe38c) → [`00bbe3a4`](#insn-00bbe3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe39c`](#insn-00bbe39c) → [`00bbe3a4`](#insn-00bbe3a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3b4`](#insn-00bbe3b4) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe3bc`](#insn-00bbe3bc) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3cc`](#insn-00bbe3cc) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3e0`](#insn-00bbe3e0) → [`00bbe3fc`](#insn-00bbe3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3e8`](#insn-00bbe3e8) → [`00bbe400`](#insn-00bbe400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3f8`](#insn-00bbe3f8) → [`00bbe400`](#insn-00bbe400) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe410`](#insn-00bbe410) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe418`](#insn-00bbe418) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe428`](#insn-00bbe428) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe43c`](#insn-00bbe43c) → [`00bbe458`](#insn-00bbe458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe444`](#insn-00bbe444) → [`00bbe45c`](#insn-00bbe45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe454`](#insn-00bbe454) → [`00bbe45c`](#insn-00bbe45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe46c`](#insn-00bbe46c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe474`](#insn-00bbe474) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe484`](#insn-00bbe484) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe498`](#insn-00bbe498) → [`00bbe4b4`](#insn-00bbe4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4a0`](#insn-00bbe4a0) → [`00bbe4b8`](#insn-00bbe4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4b0`](#insn-00bbe4b0) → [`00bbe4b8`](#insn-00bbe4b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4c8`](#insn-00bbe4c8) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe4d0`](#insn-00bbe4d0) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4e0`](#insn-00bbe4e0) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4f4`](#insn-00bbe4f4) → [`00bbe600`](#insn-00bbe600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4fc`](#insn-00bbe4fc) → [`00bbe600`](#insn-00bbe600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe508`](#insn-00bbe508) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe528`](#insn-00bbe528) → [`00bbe540`](#insn-00bbe540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe538`](#insn-00bbe538) → [`00c5d560`](../00c5d/00c5d560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d560` · 推定シンボル `None` · 推定型 `None`
- [`00bbe53c`](#insn-00bbe53c) → [`00bbe584`](#insn-00bbe584) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe540`](#insn-00bbe540) → [`00bbe584`](#insn-00bbe584) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe550`](#insn-00bbe550) → [`00bbe580`](#insn-00bbe580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe55c`](#insn-00bbe55c) → [`00bbe574`](#insn-00bbe574) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe568`](#insn-00bbe568) → [`00bbe580`](#insn-00bbe580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe570`](#insn-00bbe570) → [`00bbe560`](#insn-00bbe560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe578`](#insn-00bbe578) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe57c`](#insn-00bbe57c) → [`00bbe560`](#insn-00bbe560) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe580`](#insn-00bbe580) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe584`](#insn-00bbe584) → [`00bbe600`](#insn-00bbe600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5a0`](#insn-00bbe5a0) → [`00bbe5bc`](#insn-00bbe5bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5a8`](#insn-00bbe5a8) → [`00bbe5c0`](#insn-00bbe5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5b8`](#insn-00bbe5b8) → [`00bbe5c0`](#insn-00bbe5c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5cc`](#insn-00bbe5cc) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5e0`](#insn-00bbe5e0) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5f0`](#insn-00bbe5f0) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5fc`](#insn-00bbe5fc) → [`00bbe590`](#insn-00bbe590) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe610`](#insn-00bbe610) → [`00bbe62c`](#insn-00bbe62c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe618`](#insn-00bbe618) → [`00bbe630`](#insn-00bbe630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe628`](#insn-00bbe628) → [`00bbe630`](#insn-00bbe630) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe640`](#insn-00bbe640) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe648`](#insn-00bbe648) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe658`](#insn-00bbe658) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe66c`](#insn-00bbe66c) → [`00bbe778`](#insn-00bbe778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe674`](#insn-00bbe674) → [`00bbe778`](#insn-00bbe778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe680`](#insn-00bbe680) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6a0`](#insn-00bbe6a0) → [`00bbe6b8`](#insn-00bbe6b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b0`](#insn-00bbe6b0) → [`00c5d560`](../00c5d/00c5d560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d560` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6fc`](#insn-00bbe6fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b8`](#insn-00bbe6b8) → [`00bbe6fc`](#insn-00bbe6fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6c8`](#insn-00bbe6c8) → [`00bbe6f8`](#insn-00bbe6f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6d4`](#insn-00bbe6d4) → [`00bbe6ec`](#insn-00bbe6ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6e0`](#insn-00bbe6e0) → [`00bbe6f8`](#insn-00bbe6f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6e8`](#insn-00bbe6e8) → [`00bbe6d8`](#insn-00bbe6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f0`](#insn-00bbe6f0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f4`](#insn-00bbe6f4) → [`00bbe6d8`](#insn-00bbe6d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6f8`](#insn-00bbe6f8) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe778`](#insn-00bbe778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe718`](#insn-00bbe718) → [`00bbe734`](#insn-00bbe734) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe720`](#insn-00bbe720) → [`00bbe738`](#insn-00bbe738) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe730`](#insn-00bbe730) → [`00bbe738`](#insn-00bbe738) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe744`](#insn-00bbe744) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe758`](#insn-00bbe758) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe768`](#insn-00bbe768) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe774`](#insn-00bbe774) → [`00bbe708`](#insn-00bbe708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe788`](#insn-00bbe788) → [`00bbe7a4`](#insn-00bbe7a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe790`](#insn-00bbe790) → [`00bbe7a8`](#insn-00bbe7a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7a0`](#insn-00bbe7a0) → [`00bbe7a8`](#insn-00bbe7a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7b4`](#insn-00bbe7b4) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbe7b8`](#insn-00bbe7b8) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7cc`](#insn-00bbe7cc) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7d4`](#insn-00bbe7d4) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7d8`](#insn-00bbe7d8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7e8`](#insn-00bbe7e8) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7ec`](#insn-00bbe7ec) → [`00bbe7f8`](#insn-00bbe7f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7f0`](#insn-00bbe7f0) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7f4`](#insn-00bbe7f4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7f8`](#insn-00bbe7f8) → `Stack[-0x308]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7fc`](#insn-00bbe7fc) → [`00bbe808`](#insn-00bbe808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe800`](#insn-00bbe800) → `Stack[-0x2f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe804`](#insn-00bbe804) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe80c`](#insn-00bbe80c) → [`00c5d2d0`](../00c5d/00c5d2d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d2d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe814`](#insn-00bbe814) → [`00c5d3f0`](../00c5d/00c5d3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d3f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe81c`](#insn-00bbe81c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe824`](#insn-00bbe824) → [`00bbe848`](#insn-00bbe848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe82c`](#insn-00bbe82c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe830`](#insn-00bbe830) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe834`](#insn-00bbe834) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe838`](#insn-00bbe838) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe83c`](#insn-00bbe83c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe848`](#insn-00bbe848) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbda4c`](#insn-00bbda4c)

~~~json
{
  "source": "00bbda4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda50`](#insn-00bbda50)

~~~json
{
  "source": "00bbda50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda54`](#insn-00bbda54)

~~~json
{
  "source": "00bbda54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda58`](#insn-00bbda58)

~~~json
{
  "source": "00bbda58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda5c`](#insn-00bbda5c)

~~~json
{
  "source": "00bbda5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda60`](#insn-00bbda60)

~~~json
{
  "source": "00bbda60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda84`](#insn-00bbda84)

~~~json
{
  "source": "00bbda84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda88`](#insn-00bbda88)

~~~json
{
  "source": "00bbda88",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda8c`](#insn-00bbda8c)

~~~json
{
  "source": "00bbda8c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda90`](#insn-00bbda90)

~~~json
{
  "source": "00bbda90",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda94`](#insn-00bbda94)

~~~json
{
  "source": "00bbda94",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda98`](#insn-00bbda98)

~~~json
{
  "source": "00bbda98",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda9c`](#insn-00bbda9c)

~~~json
{
  "source": "00bbda9c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaa0`](#insn-00bbdaa0)

~~~json
{
  "source": "00bbdaa0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaa4`](#insn-00bbdaa4)

~~~json
{
  "source": "00bbdaa4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaa8`](#insn-00bbdaa8)

~~~json
{
  "source": "00bbdaa8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaac`](#insn-00bbdaac)

~~~json
{
  "source": "00bbdaac",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdab0`](#insn-00bbdab0)

~~~json
{
  "source": "00bbdab0",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdab4`](#insn-00bbdab4)

~~~json
{
  "source": "00bbdab4",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdab8`](#insn-00bbdab8)

~~~json
{
  "source": "00bbdab8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdabc`](#insn-00bbdabc)

~~~json
{
  "source": "00bbdabc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdac0`](#insn-00bbdac0)

~~~json
{
  "source": "00bbdac0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdac4`](#insn-00bbdac4)

~~~json
{
  "source": "00bbdac4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdac8`](#insn-00bbdac8)

~~~json
{
  "source": "00bbdac8",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdacc`](#insn-00bbdacc)

~~~json
{
  "source": "00bbdacc",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdad0`](#insn-00bbdad0)

~~~json
{
  "source": "00bbdad0",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdad4`](#insn-00bbdad4)

~~~json
{
  "source": "00bbdad4",
  "target": "Stack[-0x250]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdad8`](#insn-00bbdad8)

~~~json
{
  "source": "00bbdad8",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdadc`](#insn-00bbdadc)

~~~json
{
  "source": "00bbdadc",
  "target": "Stack[-0x290]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdae0`](#insn-00bbdae0)

~~~json
{
  "source": "00bbdae0",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdae4`](#insn-00bbdae4)

~~~json
{
  "source": "00bbdae4",
  "target": "Stack[-0x2d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdae8`](#insn-00bbdae8)

~~~json
{
  "source": "00bbdae8",
  "target": "Stack[-0x2f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaec`](#insn-00bbdaec)

~~~json
{
  "source": "00bbdaec",
  "target": "Stack[-0x300]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaf0`](#insn-00bbdaf0)

~~~json
{
  "source": "00bbdaf0",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb10`](#insn-00bbdb10)

~~~json
{
  "source": "00bbdb10",
  "target": "00bbdb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb18`](#insn-00bbdb18)

~~~json
{
  "source": "00bbdb18",
  "target": "00bbdb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb3c`](#insn-00bbdb3c)

~~~json
{
  "source": "00bbdb3c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdb40`](#insn-00bbdb40)

~~~json
{
  "source": "00bbdb40",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb50`](#insn-00bbdb50)

~~~json
{
  "source": "00bbdb50",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb64`](#insn-00bbdb64)

~~~json
{
  "source": "00bbdb64",
  "target": "00bbdb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb6c`](#insn-00bbdb6c)

~~~json
{
  "source": "00bbdb6c",
  "target": "00bbdb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb7c`](#insn-00bbdb7c)

~~~json
{
  "source": "00bbdb7c",
  "target": "00bbdb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb94`](#insn-00bbdb94)

~~~json
{
  "source": "00bbdb94",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdb9c`](#insn-00bbdb9c)

~~~json
{
  "source": "00bbdb9c",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbac`](#insn-00bbdbac)

~~~json
{
  "source": "00bbdbac",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbc4`](#insn-00bbdbc4)

~~~json
{
  "source": "00bbdbc4",
  "target": "00bbdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbcc`](#insn-00bbdbcc)

~~~json
{
  "source": "00bbdbcc",
  "target": "00bbdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbdc`](#insn-00bbdbdc)

~~~json
{
  "source": "00bbdbdc",
  "target": "00bbdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbe4`](#insn-00bbdbe4)

~~~json
{
  "source": "00bbdbe4",
  "target": "00bbdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbec`](#insn-00bbdbec)

~~~json
{
  "source": "00bbdbec",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdbfc`](#insn-00bbdbfc)

~~~json
{
  "source": "00bbdbfc",
  "target": "00bbdc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc0c`](#insn-00bbdc0c)

~~~json
{
  "source": "00bbdc0c",
  "target": "00bbdd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc44`](#insn-00bbdc44)

~~~json
{
  "source": "00bbdc44",
  "target": "00bbdc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc4c`](#insn-00bbdc4c)

~~~json
{
  "source": "00bbdc4c",
  "target": "00bbdc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc6c`](#insn-00bbdc6c)

~~~json
{
  "source": "00bbdc6c",
  "target": "00bbdc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc74`](#insn-00bbdc74)

~~~json
{
  "source": "00bbdc74",
  "target": "00bbdc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc84`](#insn-00bbdc84)

~~~json
{
  "source": "00bbdc84",
  "target": "00bbdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdc8c`](#insn-00bbdc8c)

~~~json
{
  "source": "00bbdc8c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdc90`](#insn-00bbdc90)

~~~json
{
  "source": "00bbdc90",
  "target": "00bbdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdca8`](#insn-00bbdca8)

~~~json
{
  "source": "00bbdca8",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdcb8`](#insn-00bbdcb8)

~~~json
{
  "source": "00bbdcb8",
  "target": "0046d5a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdcc4`](#insn-00bbdcc4)

~~~json
{
  "source": "00bbdcc4",
  "target": "00bbdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdccc`](#insn-00bbdccc)

~~~json
{
  "source": "00bbdccc",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdcd0`](#insn-00bbdcd0)

~~~json
{
  "source": "00bbdcd0",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcd4`](#insn-00bbdcd4)

~~~json
{
  "source": "00bbdcd4",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcd8`](#insn-00bbdcd8)

~~~json
{
  "source": "00bbdcd8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcdc`](#insn-00bbdcdc)

~~~json
{
  "source": "00bbdcdc",
  "target": "Stack[-0x318]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdce0`](#insn-00bbdce0)

~~~json
{
  "source": "00bbdce0",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcfc`](#insn-00bbdcfc)

~~~json
{
  "source": "00bbdcfc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd04`](#insn-00bbdd04)

~~~json
{
  "source": "00bbdd04",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd08`](#insn-00bbdd08)

~~~json
{
  "source": "00bbdd08",
  "target": "00bbdd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd0c`](#insn-00bbdd0c)

~~~json
{
  "source": "00bbdd0c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd14`](#insn-00bbdd14)

~~~json
{
  "source": "00bbdd14",
  "target": "00bbdd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd1c`](#insn-00bbdd1c)

~~~json
{
  "source": "00bbdd1c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd20`](#insn-00bbdd20)

~~~json
{
  "source": "00bbdd20",
  "target": "00c5b5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd24`](#insn-00bbdd24)

~~~json
{
  "source": "00bbdd24",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd2c`](#insn-00bbdd2c)

~~~json
{
  "source": "00bbdd2c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd38`](#insn-00bbdd38)

~~~json
{
  "source": "00bbdd38",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd48`](#insn-00bbdd48)

~~~json
{
  "source": "00bbdd48",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd4c`](#insn-00bbdd4c)

~~~json
{
  "source": "00bbdd4c",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd50`](#insn-00bbdd50)

~~~json
{
  "source": "00bbdd50",
  "target": "00bbdc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd54`](#insn-00bbdd54)

~~~json
{
  "source": "00bbdd54",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd58`](#insn-00bbdd58)

~~~json
{
  "source": "00bbdd58",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdd5c`](#insn-00bbdd5c)

~~~json
{
  "source": "00bbdd5c",
  "target": "00bbdc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd60`](#insn-00bbdd60)

~~~json
{
  "source": "00bbdd60",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd78`](#insn-00bbdd78)

~~~json
{
  "source": "00bbdd78",
  "target": "00bbde40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd80`](#insn-00bbdd80)

~~~json
{
  "source": "00bbdd80",
  "target": "00bbde40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd90`](#insn-00bbdd90)

~~~json
{
  "source": "00bbdd90",
  "target": "00bbde40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd94`](#insn-00bbdd94)

~~~json
{
  "source": "00bbdd94",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd98`](#insn-00bbdd98)

~~~json
{
  "source": "00bbdd98",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdda8`](#insn-00bbdda8)

~~~json
{
  "source": "00bbdda8",
  "target": "00bbddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddac`](#insn-00bbddac)

~~~json
{
  "source": "00bbddac",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddb4`](#insn-00bbddb4)

~~~json
{
  "source": "00bbddb4",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbddcc`](#insn-00bbddcc)

~~~json
{
  "source": "00bbddcc",
  "target": "00bbdddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddd8`](#insn-00bbddd8)

~~~json
{
  "source": "00bbddd8",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdddc`](#insn-00bbdddc)

~~~json
{
  "source": "00bbdddc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdde0`](#insn-00bbdde0)

~~~json
{
  "source": "00bbdde0",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdde4`](#insn-00bbdde4)

~~~json
{
  "source": "00bbdde4",
  "target": "00bbddf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbddec`](#insn-00bbddec)

~~~json
{
  "source": "00bbddec",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde18`](#insn-00bbde18)

~~~json
{
  "source": "00bbde18",
  "target": "Stack[-0x328]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde28`](#insn-00bbde28)

~~~json
{
  "source": "00bbde28",
  "target": "Stack[-0x330]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde34`](#insn-00bbde34)

~~~json
{
  "source": "00bbde34",
  "target": "00c5d570",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde4c`](#insn-00bbde4c)

~~~json
{
  "source": "00bbde4c",
  "target": "00bbde68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde54`](#insn-00bbde54)

~~~json
{
  "source": "00bbde54",
  "target": "00bbde6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde64`](#insn-00bbde64)

~~~json
{
  "source": "00bbde64",
  "target": "00bbde6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde7c`](#insn-00bbde7c)

~~~json
{
  "source": "00bbde7c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbde84`](#insn-00bbde84)

~~~json
{
  "source": "00bbde84",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbde94`](#insn-00bbde94)

~~~json
{
  "source": "00bbde94",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdea8`](#insn-00bbdea8)

~~~json
{
  "source": "00bbdea8",
  "target": "00bbdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdec0`](#insn-00bbdec0)

~~~json
{
  "source": "00bbdec0",
  "target": "00bbdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbded8`](#insn-00bbded8)

~~~json
{
  "source": "00bbded8",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdee0`](#insn-00bbdee0)

~~~json
{
  "source": "00bbdee0",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdef0`](#insn-00bbdef0)

~~~json
{
  "source": "00bbdef0",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf08`](#insn-00bbdf08)

~~~json
{
  "source": "00bbdf08",
  "target": "00bbdf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf10`](#insn-00bbdf10)

~~~json
{
  "source": "00bbdf10",
  "target": "00bbdf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf20`](#insn-00bbdf20)

~~~json
{
  "source": "00bbdf20",
  "target": "00bbdf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf34`](#insn-00bbdf34)

~~~json
{
  "source": "00bbdf34",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdf38`](#insn-00bbdf38)

~~~json
{
  "source": "00bbdf38",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf48`](#insn-00bbdf48)

~~~json
{
  "source": "00bbdf48",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf5c`](#insn-00bbdf5c)

~~~json
{
  "source": "00bbdf5c",
  "target": "00bbdf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf64`](#insn-00bbdf64)

~~~json
{
  "source": "00bbdf64",
  "target": "00bbdf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf74`](#insn-00bbdf74)

~~~json
{
  "source": "00bbdf74",
  "target": "00bbdf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf8c`](#insn-00bbdf8c)

~~~json
{
  "source": "00bbdf8c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdf94`](#insn-00bbdf94)

~~~json
{
  "source": "00bbdf94",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfa4`](#insn-00bbdfa4)

~~~json
{
  "source": "00bbdfa4",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdfb8`](#insn-00bbdfb8)

~~~json
{
  "source": "00bbdfb8",
  "target": "00bbdff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfc0`](#insn-00bbdfc0)

~~~json
{
  "source": "00bbdfc0",
  "target": "00bbdfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfd4`](#insn-00bbdfd4)

~~~json
{
  "source": "00bbdfd4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfd8`](#insn-00bbdfd8)

~~~json
{
  "source": "00bbdfd8",
  "target": "00bbe000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfe0`](#insn-00bbdfe0)

~~~json
{
  "source": "00bbdfe0",
  "target": "00bbe004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdff0`](#insn-00bbdff0)

~~~json
{
  "source": "00bbdff0",
  "target": "00bbe004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdff8`](#insn-00bbdff8)

~~~json
{
  "source": "00bbdff8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdffc`](#insn-00bbdffc)

~~~json
{
  "source": "00bbdffc",
  "target": "00bbe004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe010`](#insn-00bbe010)

~~~json
{
  "source": "00bbe010",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe014`](#insn-00bbe014)

~~~json
{
  "source": "00bbe014",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe024`](#insn-00bbe024)

~~~json
{
  "source": "00bbe024",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe038`](#insn-00bbe038)

~~~json
{
  "source": "00bbe038",
  "target": "00bbe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe040`](#insn-00bbe040)

~~~json
{
  "source": "00bbe040",
  "target": "00bbe058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe050`](#insn-00bbe050)

~~~json
{
  "source": "00bbe050",
  "target": "00bbe058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe068`](#insn-00bbe068)

~~~json
{
  "source": "00bbe068",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe070`](#insn-00bbe070)

~~~json
{
  "source": "00bbe070",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe080`](#insn-00bbe080)

~~~json
{
  "source": "00bbe080",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe094`](#insn-00bbe094)

~~~json
{
  "source": "00bbe094",
  "target": "00bbe0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe09c`](#insn-00bbe09c)

~~~json
{
  "source": "00bbe09c",
  "target": "00bbe0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0ac`](#insn-00bbe0ac)

~~~json
{
  "source": "00bbe0ac",
  "target": "00bbe0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0c4`](#insn-00bbe0c4)

~~~json
{
  "source": "00bbe0c4",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe0cc`](#insn-00bbe0cc)

~~~json
{
  "source": "00bbe0cc",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe0dc`](#insn-00bbe0dc)

~~~json
{
  "source": "00bbe0dc",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe0f0`](#insn-00bbe0f0)

~~~json
{
  "source": "00bbe0f0",
  "target": "00bbe10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0f8`](#insn-00bbe0f8)

~~~json
{
  "source": "00bbe0f8",
  "target": "00bbe110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe108`](#insn-00bbe108)

~~~json
{
  "source": "00bbe108",
  "target": "00bbe110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe120`](#insn-00bbe120)

~~~json
{
  "source": "00bbe120",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe128`](#insn-00bbe128)

~~~json
{
  "source": "00bbe128",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe138`](#insn-00bbe138)

~~~json
{
  "source": "00bbe138",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe14c`](#insn-00bbe14c)

~~~json
{
  "source": "00bbe14c",
  "target": "00bbe16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe154`](#insn-00bbe154)

~~~json
{
  "source": "00bbe154",
  "target": "00bbe15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe15c`](#insn-00bbe15c)

~~~json
{
  "source": "00bbe15c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe164`](#insn-00bbe164)

~~~json
{
  "source": "00bbe164",
  "target": "00bbe180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe168`](#insn-00bbe168)

~~~json
{
  "source": "00bbe168",
  "target": "00bbe184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe170`](#insn-00bbe170)

~~~json
{
  "source": "00bbe170",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe174`](#insn-00bbe174)

~~~json
{
  "source": "00bbe174",
  "target": "00bbe1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe17c`](#insn-00bbe17c)

~~~json
{
  "source": "00bbe17c",
  "target": "00bbe184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe188`](#insn-00bbe188)

~~~json
{
  "source": "00bbe188",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe18c`](#insn-00bbe18c)

~~~json
{
  "source": "00bbe18c",
  "target": "00bbe7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe194`](#insn-00bbe194)

~~~json
{
  "source": "00bbe194",
  "target": "00bbe7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1a4`](#insn-00bbe1a4)

~~~json
{
  "source": "00bbe1a4",
  "target": "00bbe7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1b8`](#insn-00bbe1b8)

~~~json
{
  "source": "00bbe1b8",
  "target": "00bbe1dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1c0`](#insn-00bbe1c0)

~~~json
{
  "source": "00bbe1c0",
  "target": "00bbe1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1d0`](#insn-00bbe1d0)

~~~json
{
  "source": "00bbe1d0",
  "target": "00bbe1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1d4`](#insn-00bbe1d4)

~~~json
{
  "source": "00bbe1d4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1d8`](#insn-00bbe1d8)

~~~json
{
  "source": "00bbe1d8",
  "target": "00bbe7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1ec`](#insn-00bbe1ec)

~~~json
{
  "source": "00bbe1ec",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe1f0`](#insn-00bbe1f0)

~~~json
{
  "source": "00bbe1f0",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe200`](#insn-00bbe200)

~~~json
{
  "source": "00bbe200",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe214`](#insn-00bbe214)

~~~json
{
  "source": "00bbe214",
  "target": "00bbe230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe21c`](#insn-00bbe21c)

~~~json
{
  "source": "00bbe21c",
  "target": "00bbe234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe22c`](#insn-00bbe22c)

~~~json
{
  "source": "00bbe22c",
  "target": "00bbe234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe244`](#insn-00bbe244)

~~~json
{
  "source": "00bbe244",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe24c`](#insn-00bbe24c)

~~~json
{
  "source": "00bbe24c",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe25c`](#insn-00bbe25c)

~~~json
{
  "source": "00bbe25c",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe270`](#insn-00bbe270)

~~~json
{
  "source": "00bbe270",
  "target": "00bbe28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe278`](#insn-00bbe278)

~~~json
{
  "source": "00bbe278",
  "target": "00bbe290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe288`](#insn-00bbe288)

~~~json
{
  "source": "00bbe288",
  "target": "00bbe290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2a0`](#insn-00bbe2a0)

~~~json
{
  "source": "00bbe2a0",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe2a8`](#insn-00bbe2a8)

~~~json
{
  "source": "00bbe2a8",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe2b8`](#insn-00bbe2b8)

~~~json
{
  "source": "00bbe2b8",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe2cc`](#insn-00bbe2cc)

~~~json
{
  "source": "00bbe2cc",
  "target": "00bbe2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2d4`](#insn-00bbe2d4)

~~~json
{
  "source": "00bbe2d4",
  "target": "00bbe2ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2e4`](#insn-00bbe2e4)

~~~json
{
  "source": "00bbe2e4",
  "target": "00bbe2ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2fc`](#insn-00bbe2fc)

~~~json
{
  "source": "00bbe2fc",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe304`](#insn-00bbe304)

~~~json
{
  "source": "00bbe304",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe314`](#insn-00bbe314)

~~~json
{
  "source": "00bbe314",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe328`](#insn-00bbe328)

~~~json
{
  "source": "00bbe328",
  "target": "00bbe344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe330`](#insn-00bbe330)

~~~json
{
  "source": "00bbe330",
  "target": "00bbe348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe340`](#insn-00bbe340)

~~~json
{
  "source": "00bbe340",
  "target": "00bbe348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe358`](#insn-00bbe358)

~~~json
{
  "source": "00bbe358",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe360`](#insn-00bbe360)

~~~json
{
  "source": "00bbe360",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe370`](#insn-00bbe370)

~~~json
{
  "source": "00bbe370",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe384`](#insn-00bbe384)

~~~json
{
  "source": "00bbe384",
  "target": "00bbe3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe38c`](#insn-00bbe38c)

~~~json
{
  "source": "00bbe38c",
  "target": "00bbe3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe39c`](#insn-00bbe39c)

~~~json
{
  "source": "00bbe39c",
  "target": "00bbe3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3b4`](#insn-00bbe3b4)

~~~json
{
  "source": "00bbe3b4",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe3bc`](#insn-00bbe3bc)

~~~json
{
  "source": "00bbe3bc",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe3cc`](#insn-00bbe3cc)

~~~json
{
  "source": "00bbe3cc",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe3e0`](#insn-00bbe3e0)

~~~json
{
  "source": "00bbe3e0",
  "target": "00bbe3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3e8`](#insn-00bbe3e8)

~~~json
{
  "source": "00bbe3e8",
  "target": "00bbe400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3f8`](#insn-00bbe3f8)

~~~json
{
  "source": "00bbe3f8",
  "target": "00bbe400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe410`](#insn-00bbe410)

~~~json
{
  "source": "00bbe410",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe418`](#insn-00bbe418)

~~~json
{
  "source": "00bbe418",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe428`](#insn-00bbe428)

~~~json
{
  "source": "00bbe428",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe43c`](#insn-00bbe43c)

~~~json
{
  "source": "00bbe43c",
  "target": "00bbe458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe444`](#insn-00bbe444)

~~~json
{
  "source": "00bbe444",
  "target": "00bbe45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe454`](#insn-00bbe454)

~~~json
{
  "source": "00bbe454",
  "target": "00bbe45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe46c`](#insn-00bbe46c)

~~~json
{
  "source": "00bbe46c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe474`](#insn-00bbe474)

~~~json
{
  "source": "00bbe474",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe484`](#insn-00bbe484)

~~~json
{
  "source": "00bbe484",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe498`](#insn-00bbe498)

~~~json
{
  "source": "00bbe498",
  "target": "00bbe4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4a0`](#insn-00bbe4a0)

~~~json
{
  "source": "00bbe4a0",
  "target": "00bbe4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4b0`](#insn-00bbe4b0)

~~~json
{
  "source": "00bbe4b0",
  "target": "00bbe4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4c8`](#insn-00bbe4c8)

~~~json
{
  "source": "00bbe4c8",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe4d0`](#insn-00bbe4d0)

~~~json
{
  "source": "00bbe4d0",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe4e0`](#insn-00bbe4e0)

~~~json
{
  "source": "00bbe4e0",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe4f4`](#insn-00bbe4f4)

~~~json
{
  "source": "00bbe4f4",
  "target": "00bbe600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4fc`](#insn-00bbe4fc)

~~~json
{
  "source": "00bbe4fc",
  "target": "00bbe600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe508`](#insn-00bbe508)

~~~json
{
  "source": "00bbe508",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe528`](#insn-00bbe528)

~~~json
{
  "source": "00bbe528",
  "target": "00bbe540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe538`](#insn-00bbe538)

~~~json
{
  "source": "00bbe538",
  "target": "00c5d560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe53c`](#insn-00bbe53c)

~~~json
{
  "source": "00bbe53c",
  "target": "00bbe584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe540`](#insn-00bbe540)

~~~json
{
  "source": "00bbe540",
  "target": "00bbe584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe550`](#insn-00bbe550)

~~~json
{
  "source": "00bbe550",
  "target": "00bbe580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe55c`](#insn-00bbe55c)

~~~json
{
  "source": "00bbe55c",
  "target": "00bbe574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe568`](#insn-00bbe568)

~~~json
{
  "source": "00bbe568",
  "target": "00bbe580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe570`](#insn-00bbe570)

~~~json
{
  "source": "00bbe570",
  "target": "00bbe560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe578`](#insn-00bbe578)

~~~json
{
  "source": "00bbe578",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe57c`](#insn-00bbe57c)

~~~json
{
  "source": "00bbe57c",
  "target": "00bbe560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe580`](#insn-00bbe580)

~~~json
{
  "source": "00bbe580",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe584`](#insn-00bbe584)

~~~json
{
  "source": "00bbe584",
  "target": "00bbe600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5a0`](#insn-00bbe5a0)

~~~json
{
  "source": "00bbe5a0",
  "target": "00bbe5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5a8`](#insn-00bbe5a8)

~~~json
{
  "source": "00bbe5a8",
  "target": "00bbe5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5b8`](#insn-00bbe5b8)

~~~json
{
  "source": "00bbe5b8",
  "target": "00bbe5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5cc`](#insn-00bbe5cc)

~~~json
{
  "source": "00bbe5cc",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5e0`](#insn-00bbe5e0)

~~~json
{
  "source": "00bbe5e0",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe5f0`](#insn-00bbe5f0)

~~~json
{
  "source": "00bbe5f0",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe5fc`](#insn-00bbe5fc)

~~~json
{
  "source": "00bbe5fc",
  "target": "00bbe590",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe610`](#insn-00bbe610)

~~~json
{
  "source": "00bbe610",
  "target": "00bbe62c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe618`](#insn-00bbe618)

~~~json
{
  "source": "00bbe618",
  "target": "00bbe630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe628`](#insn-00bbe628)

~~~json
{
  "source": "00bbe628",
  "target": "00bbe630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe640`](#insn-00bbe640)

~~~json
{
  "source": "00bbe640",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe648`](#insn-00bbe648)

~~~json
{
  "source": "00bbe648",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe658`](#insn-00bbe658)

~~~json
{
  "source": "00bbe658",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe66c`](#insn-00bbe66c)

~~~json
{
  "source": "00bbe66c",
  "target": "00bbe778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe674`](#insn-00bbe674)

~~~json
{
  "source": "00bbe674",
  "target": "00bbe778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe680`](#insn-00bbe680)

~~~json
{
  "source": "00bbe680",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6a0`](#insn-00bbe6a0)

~~~json
{
  "source": "00bbe6a0",
  "target": "00bbe6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6b0`](#insn-00bbe6b0)

~~~json
{
  "source": "00bbe6b0",
  "target": "00c5d560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6b4`](#insn-00bbe6b4)

~~~json
{
  "source": "00bbe6b4",
  "target": "00bbe6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6b8`](#insn-00bbe6b8)

~~~json
{
  "source": "00bbe6b8",
  "target": "00bbe6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6c8`](#insn-00bbe6c8)

~~~json
{
  "source": "00bbe6c8",
  "target": "00bbe6f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6d4`](#insn-00bbe6d4)

~~~json
{
  "source": "00bbe6d4",
  "target": "00bbe6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6e0`](#insn-00bbe6e0)

~~~json
{
  "source": "00bbe6e0",
  "target": "00bbe6f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6e8`](#insn-00bbe6e8)

~~~json
{
  "source": "00bbe6e8",
  "target": "00bbe6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6f0`](#insn-00bbe6f0)

~~~json
{
  "source": "00bbe6f0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6f4`](#insn-00bbe6f4)

~~~json
{
  "source": "00bbe6f4",
  "target": "00bbe6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6f8`](#insn-00bbe6f8)

~~~json
{
  "source": "00bbe6f8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6fc`](#insn-00bbe6fc)

~~~json
{
  "source": "00bbe6fc",
  "target": "00bbe778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe718`](#insn-00bbe718)

~~~json
{
  "source": "00bbe718",
  "target": "00bbe734",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe720`](#insn-00bbe720)

~~~json
{
  "source": "00bbe720",
  "target": "00bbe738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe730`](#insn-00bbe730)

~~~json
{
  "source": "00bbe730",
  "target": "00bbe738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe744`](#insn-00bbe744)

~~~json
{
  "source": "00bbe744",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe758`](#insn-00bbe758)

~~~json
{
  "source": "00bbe758",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe768`](#insn-00bbe768)

~~~json
{
  "source": "00bbe768",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe774`](#insn-00bbe774)

~~~json
{
  "source": "00bbe774",
  "target": "00bbe708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe788`](#insn-00bbe788)

~~~json
{
  "source": "00bbe788",
  "target": "00bbe7a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe790`](#insn-00bbe790)

~~~json
{
  "source": "00bbe790",
  "target": "00bbe7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7a0`](#insn-00bbe7a0)

~~~json
{
  "source": "00bbe7a0",
  "target": "00bbe7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7b4`](#insn-00bbe7b4)

~~~json
{
  "source": "00bbe7b4",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe7b8`](#insn-00bbe7b8)

~~~json
{
  "source": "00bbe7b8",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe7cc`](#insn-00bbe7cc)

~~~json
{
  "source": "00bbe7cc",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe7d4`](#insn-00bbe7d4)

~~~json
{
  "source": "00bbe7d4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7d8`](#insn-00bbe7d8)

~~~json
{
  "source": "00bbe7d8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7e8`](#insn-00bbe7e8)

~~~json
{
  "source": "00bbe7e8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7ec`](#insn-00bbe7ec)

~~~json
{
  "source": "00bbe7ec",
  "target": "00bbe7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7f0`](#insn-00bbe7f0)

~~~json
{
  "source": "00bbe7f0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7f4`](#insn-00bbe7f4)

~~~json
{
  "source": "00bbe7f4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7f8`](#insn-00bbe7f8)

~~~json
{
  "source": "00bbe7f8",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7fc`](#insn-00bbe7fc)

~~~json
{
  "source": "00bbe7fc",
  "target": "00bbe808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe800`](#insn-00bbe800)

~~~json
{
  "source": "00bbe800",
  "target": "Stack[-0x2f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe804`](#insn-00bbe804)

~~~json
{
  "source": "00bbe804",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe80c`](#insn-00bbe80c)

~~~json
{
  "source": "00bbe80c",
  "target": "00c5d2d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe814`](#insn-00bbe814)

~~~json
{
  "source": "00bbe814",
  "target": "00c5d3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe81c`](#insn-00bbe81c)

~~~json
{
  "source": "00bbe81c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe824`](#insn-00bbe824)

~~~json
{
  "source": "00bbe824",
  "target": "00bbe848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe82c`](#insn-00bbe82c)

~~~json
{
  "source": "00bbe82c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe830`](#insn-00bbe830)

~~~json
{
  "source": "00bbe830",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe834`](#insn-00bbe834)

~~~json
{
  "source": "00bbe834",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe838`](#insn-00bbe838)

~~~json
{
  "source": "00bbe838",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe83c`](#insn-00bbe83c)

~~~json
{
  "source": "00bbe83c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe848`](#insn-00bbe848)

~~~json
{
  "source": "00bbe848",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
