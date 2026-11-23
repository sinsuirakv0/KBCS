# 00b4efec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4f0b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4f0b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0067.md#compare-9c9bccaf7f6ce70b0dc0ba9f05611cae)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4efec",
  "name": "_ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE",
  "size": 3656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b35b99da3eeb184bccbc25acb65d16970eee4988d50e25cf4819c5b213f05592",
  "source_text_sha256": "b35b99da3eeb184bccbc25acb65d16970eee4988d50e25cf4819c5b213f05592",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4efec",
        "00b4fe33"
      ]
    ],
    "bytes_sha256": "49fce85c0fbc3e3eebfa1d3e87dc5c0df967535f7bcc217640de7677202c28a5",
    "instruction_count": 914,
    "instruction_bytes": 3656,
    "body_bytes": 3656,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00be0450](../00be0/00be0450.md)

## 呼び出し先

- [0044a6d0](../0044a/0044a6d0.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde130](../00bde/00bde130.md)
- [00bde640](../00bde/00bde640.md)
- [00bde660](../00bde/00bde660.md)
- [00be0260](../00be0/00be0260.md)
- [00be0320](../00be0/00be0320.md)
- [00be0470](../00be0/00be0470.md)
- [00be0480](../00be0/00be0480.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 34786 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE
               (undefined8 *param_1,uint *param_2)

{
  char *__s;
  uint *puVar1;
  int *piVar2;
  long lVar3;
  char *__s_00;
  uint uVar4;
  byte bVar5;
  ushort uVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  undefined8 uVar10;
  void *pvVar11;
  byte *pbVar12;
  size_t sVar13;
  undefined8 *puVar14;
  void *__dest;
  char *pcVar15;
  undefined8 *puVar16;
  long lVar17;
  ulong uVar18;
  ushort *puVar19;
  ulong uVar20;
  ulong uVar21;
  long lVar22;
  ulong uVar23;
  long lVar24;
  byte *pbVar25;
  undefined8 *puVar26;
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
  
                    /* try { // try from 00b4f00c to 00c4f017 has its CatchHandler @ 00b4f27c */
  lVar7 = tpidr_el0;
  local_78 = *(long *)(lVar7 + 0x28);
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
                    /* try { // try from 00b4f03c to 00c4f053 has its CatchHandler @ 00b4f264 */
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
                    /* try { // try from 00b4f054 to 00c4f05f has its CatchHandler @ 00b4f24c */
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
                    /* try { // try from 00b4f078 to 00c4f083 has its CatchHandler @ 00b4f234 */
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
                    /* try { // try from 00b4f0a0 to 00c4f0ab has its CatchHandler @ 00b4f228 */
  lVar17 = 0;
  if (4 < *(ushort *)((long)param_2 - (long)(int)*param_2)) {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[2];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
                    /* try { // try from 00b4f0c4 to 00c4f0cf has its CatchHandler @ 00b4f224 */
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  __s = "";
                    /* try { // try from 00b4f0d4 to 00c4f0df has its CatchHandler @ 00b4f21c */
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_1c0,pcVar15,sVar13);
                    /* try { // try from 00b4f0f4 to 00c4f0ff has its CatchHandler @ 00b4f208 */
                    /* try { // try from 00b4f100 to 00c4f10b has its CatchHandler @ 00b4f204 */
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 7) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[3];
                    /* try { // try from 00b4f10c to 00c4f117 has its CatchHandler @ 00b4f200 */
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
                    /* try { // try from 00b4f138 to 00c4f143 has its CatchHandler @ 00b4f1fc */
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_1a8,pcVar15,sVar13);
  uVar18 = (ulong)(int)*param_2;
                    /* try { // try from 00b4f154 to 00c4f173 has its CatchHandler @ 00b4f2f8 */
  lVar17 = -uVar18;
                    /* try { // try from 00b4f174 to 00c4f1bf has its CatchHandler @ 00b4f430 */
  if ((((10 < *(ushort *)((long)param_2 - uVar18)) &&
       (uVar20 = (ulong)((ushort *)((long)param_2 - uVar18))[5], uVar20 != 0)) &&
      (puVar1 = (uint *)((long)param_2 + uVar20), puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1),
      puVar1 != (uint *)0x0)) && (uVar4 = *puVar1, uVar4 != 0)) {
    lVar17 = 0;
    do {
      uVar18 = (ulong)*(ushort *)((long)param_2 + (10 - (long)(int)uVar18));
      uVar20 = (ulong)*(uint *)((long)param_2 + uVar18);
                    /* try { // try from 00b4f1c0 to 00c4f437 has its CatchHandler @ 00b4ec40 */
      uVar21 = (ulong)*(uint *)((long)param_2 + lVar17 + uVar18 + uVar20 + 4);
      lVar24 = uVar18 + uVar20 + uVar21;
      lVar22 = (long)*(int *)((long)param_2 + lVar17 + lVar24 + 4);
      lVar24 = lVar17 + (lVar24 - lVar22);
      uVar6 = *(ushort *)((long)param_2 + lVar24 + 4);
      if (uVar6 < 5) {
        lVar24 = 0;
                    /* catch() { ... } // from try @ 00b4f00c with catch @ 00b4f27c */
        pcVar15 = "";
                    /* catch() { ... } // from try @ 00b4efe8 with catch @ 00b4f280 */
      }
      else {
        uVar23 = (ulong)*(ushort *)((long)param_2 + lVar24 + 8);
        lVar24 = 0;
        if (uVar23 != 0) {
                    /* catch() { ... } // from try @ 00b4f138 with catch @ 00b4f1fc */
                    /* catch() { ... } // from try @ 00b4f10c with catch @ 00b4f200 */
                    /* catch() { ... } // from try @ 00b4f100 with catch @ 00b4f204 */
          lVar24 = uVar18 + uVar20 + uVar21 + uVar23;
                    /* catch() { ... } // from try @ 00b4f0f4 with catch @ 00b4f208 */
                    /* catch() { ... } // from try @ 00b4f0d4 with catch @ 00b4f21c */
          lVar24 = (long)param_2 +
                   lVar17 + lVar24 + (ulong)*(uint *)((long)param_2 + lVar17 + lVar24 + 4) + 4;
        }
                    /* catch() { ... } // from try @ 00b4f0c4 with catch @ 00b4f224 */
                    /* catch() { ... } // from try @ 00b4f0a0 with catch @ 00b4f228 */
        pcVar15 = __s;
        if (lVar24 != 0) {
          pcVar15 = (char *)(lVar24 + 4);
        }
                    /* catch() { ... } // from try @ 00b4f078 with catch @ 00b4f234 */
        if (6 < uVar6) {
          lVar24 = uVar18 + uVar20 + uVar21;
                    /* catch() { ... } // from try @ 00b4f054 with catch @ 00b4f24c */
          uVar18 = (ulong)*(ushort *)((long)param_2 + lVar17 + (lVar24 - lVar22) + 10);
          if (uVar18 != 0) {
            lVar24 = lVar24 + uVar18;
                    /* catch() { ... } // from try @ 00b4f03c with catch @ 00b4f264 */
            lVar24 = (long)param_2 +
                     lVar17 + lVar24 + (ulong)*(uint *)((long)param_2 + lVar17 + lVar24 + 4) + 4;
            goto LAB_00b4f288;
          }
        }
        lVar24 = 0;
      }
LAB_00b4f288:
                    /* catch() { ... } // from try @ 00b4efc0 with catch @ 00b4f28c */
      __s_00 = __s;
      if (lVar24 != 0) {
        __s_00 = (char *)(lVar24 + 4);
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                (&local_320,pcVar15);
      puVar14 = (undefined8 *)FUN_0044a6d0(&local_178,&local_80,&local_320);
      puVar26 = (undefined8 *)*puVar14;
      if (puVar26 == (undefined8 *)0x0) {
        puVar26 = (undefined8 *)_Znwm(0x50);
        pvVar11 = local_310;
        uVar10 = uStack_318;
        uVar18 = local_320;
        uStack_318 = 0;
        local_310 = (void *)0x0;
        local_320 = 0;
        puVar26[8] = 0;
        puVar26[9] = 0;
                    /* catch() { ... } // from try @ 00b4ef9c with catch @ 00b4f2d8 */
        *puVar26 = 0;
        puVar26[1] = 0;
        puVar26[5] = uVar10;
        puVar26[4] = uVar18;
        puVar26[6] = pvVar11;
        puVar26[7] = 0;
        puVar26[2] = local_80;
                    /* catch() { ... } // from try @ 00b4ef90 with catch @ 00b4f2e8 */
        *puVar14 = puVar26;
                    /* catch() { ... } // from try @ 00b4ef7c with catch @ 00b4f2f0 */
                    /* catch() { ... } // from try @ 00b4ef58 with catch @ 00b4f2f4 */
                    /* catch() { ... } // from try @ 00b4f154 with catch @ 00b4f2f8 */
        puVar16 = puVar26;
        if ((undefined8 *)*local_178 != (undefined8 *)0x0) {
                    /* catch() { ... } // from try @ 00b4ee80 with catch @ 00b4f2fc */
                    /* catch() { ... } // from try @ 00b4ee74 with catch @ 00b4f300 */
          puVar16 = (undefined8 *)*puVar14;
          local_178 = (undefined8 *)*local_178;
                    /* catch() { ... } // from try @ 00b4ee68 with catch @ 00b4f304 */
        }
        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                  (local_170,puVar16);
        local_168 = local_168 + 1;
                    /* catch() { ... } // from try @ 00b4ee3c with catch @ 00b4f31c */
      }
                    /* catch() { ... } // from try @ 00b4ee2c with catch @ 00b4f324 */
                    /* catch() { ... } // from try @ 00b4ee08 with catch @ 00b4f328 */
      sVar13 = strlen(__s_00);
                    /* catch() { ... } // from try @ 00b4eddc with catch @ 00b4f334 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (puVar26 + 7,__s_00,sVar13);
      if ((local_320 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4edbc with catch @ 00b4f348 */
        _ZdlPv(local_310);
      }
      uVar18 = (ulong)*param_2;
      lVar17 = lVar17 + 4;
    } while ((ulong)uVar4 * 4 - lVar17 != 0);
                    /* catch() { ... } // from try @ 00b4edac with catch @ 00b4f350 */
                    /* catch() { ... } // from try @ 00b4ed88 with catch @ 00b4f354 */
    lVar17 = -(long)(int)*param_2;
  }
  lVar24 = lStack_158;
  pvVar11 = local_160;
                    /* catch() { ... } // from try @ 00b4ed60 with catch @ 00b4f360 */
  if (((0xc < *(ushort *)((long)param_2 + lVar17)) &&
      (uVar18 = (ulong)((ushort *)((long)param_2 + lVar17))[6], uVar18 != 0)) &&
     (puVar1 = (uint *)((long)param_2 + uVar18), puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1),
     puVar1 != (uint *)0x0)) {
                    /* catch() { ... } // from try @ 00b4ed3c with catch @ 00b4f388 */
    uVar18 = (ulong)*puVar1;
                    /* catch() { ... } // from try @ 00b4ed30 with catch @ 00b4f398 */
    if ((ulong)(local_150 - (long)local_160) < uVar18) {
      __dest = (void *)_Znwm(uVar18);
      sVar13 = lVar24 - (long)pvVar11;
                    /* catch() { ... } // from try @ 00b4ed1c with catch @ 00b4f3b8 */
                    /* catch() { ... } // from try @ 00b4ecf8 with catch @ 00b4f3bc */
      if (0 < (long)sVar13) {
        memcpy(__dest,pvVar11,sVar13);
      }
                    /* catch() { ... } // from try @ 00b4ee9c with catch @ 00b4f3cc */
      local_160 = __dest;
      lStack_158 = (long)__dest + sVar13;
      local_150 = (long)__dest + uVar18;
      if (pvVar11 != (void *)0x0) {
        _ZdlPv(pvVar11);
      }
    }
    uVar6 = *(ushort *)((long)param_2 + (0xc - (long)(int)*param_2));
    puVar1 = (uint *)((long)param_2 + (ulong)uVar6);
    puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
    local_328 = (uint *)0x0;
    if (uVar6 != 0) {
      local_328 = puVar1;
    }
    local_328 = local_328 + 1;
    local_330 = (long)puVar1 + (ulong)*puVar1 + 4;
    _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS9_E9referenceEEE5valueEvE4typeES9_S9_
              (&local_160,&local_328,&local_330);
    lVar17 = -(long)(int)*param_2;
  }
                    /* catch() { ... } // from try @ 00b4f174 with catch @ 00b4f430 */
                    /* catch() { ... } // from try @ 00b4eeb8 with catch @ 00b4f434 */
                    /* try { // try from 00b4f438 to 00c4f49f has its CatchHandler @ 00b4f438
                       catch() { ... } // from try @ 00b4f438 with catch @ 00b4f438
                       catch() { ... } // from try @ 00b4fb2c with catch @ 00b4f438 */
  if (*(ushort *)((long)param_2 + lVar17) < 0xf) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 + lVar17))[7];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_148,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x11) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[8];
                    /* try { // try from 00b4f4a0 to 00c4f4ab has its CatchHandler @ 00b4fc64 */
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
                    /* try { // try from 00b4f4b8 to 00c4f4bf has its CatchHandler @ 00b4fc5c */
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_130,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x17) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xb];
    lVar17 = 0;
    if (uVar18 != 0) {
                    /* try { // try from 00b4f504 to 00c4f50f has its CatchHandler @ 00b4fc38 */
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
                    /* try { // try from 00b4f510 to 00c4f51f has its CatchHandler @ 00b4fc04 */
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_f8,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x19) {
    lVar17 = 0;
  }
  else {
                    /* try { // try from 00b4f550 to 00c4f563 has its CatchHandler @ 00b4fc6c */
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0xc];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
                    /* try { // try from 00b4f57c to 00c4f583 has its CatchHandler @ 00b4fca4 */
  sVar13 = strlen(pcVar15);
                    /* try { // try from 00b4f588 to 00c4f597 has its CatchHandler @ 00b4fca0 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_e0,pcVar15,sVar13);
                    /* try { // try from 00b4f598 to 00c4f5a7 has its CatchHandler @ 00b4fc90 */
  puVar19 = (ushort *)((long)param_2 - (long)(int)*param_2);
  if (*puVar19 < 0x1d) {
    lVar17 = 0;
    local_c0 = false;
  }
  else {
    local_c0 = false;
    if ((ulong)puVar19[0xe] != 0) {
      local_c0 = *(char *)((long)param_2 + (ulong)puVar19[0xe]) != '\0';
    }
    if (*puVar19 < 0x1f) {
      lVar17 = 0;
    }
    else {
      lVar17 = 0;
      if ((ulong)puVar19[0xf] != 0) {
        puVar1 = (uint *)((long)param_2 + (ulong)puVar19[0xf]);
        lVar17 = (long)puVar1 + (ulong)*puVar1;
      }
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&local_b8,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 9) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[4];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_190,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x13) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[9];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
                    /* try { // try from 00b4f698 to 00c4f6a3 has its CatchHandler @ 00b4fc70 */
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_118,pcVar15,sVar13);
  if (*(ushort *)((long)param_2 - (long)(int)*param_2) < 0x23) {
    lVar17 = 0;
  }
  else {
    uVar18 = (ulong)((ushort *)((long)param_2 - (long)(int)*param_2))[0x11];
    lVar17 = 0;
    if (uVar18 != 0) {
      puVar1 = (uint *)((long)param_2 + uVar18);
      lVar17 = (long)puVar1 + (ulong)*puVar1;
    }
  }
  pcVar15 = __s;
  if (lVar17 != 0) {
    pcVar15 = (char *)(lVar17 + 4);
  }
  sVar13 = strlen(pcVar15);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
            (&uStack_a0,pcVar15,sVar13);
  puVar19 = (ushort *)((long)param_2 - (long)(int)*param_2);
  uVar6 = *puVar19;
  if (uVar6 < 0x21) {
    local_88 = 0;
    if (uVar6 < 0x15) {
      local_100 = 0;
      goto LAB_00b4fdc0;
    }
    uVar18 = (ulong)puVar19[10];
    local_100 = 0;
    if (uVar18 != 0) goto LAB_00b4f770;
  }
  else {
    local_88 = 0;
    if ((ulong)puVar19[0x10] != 0) {
      local_88 = *(undefined8 *)((long)param_2 + (ulong)puVar19[0x10]);
    }
    uVar18 = (ulong)puVar19[10];
    if (uVar18 == 0) {
      local_100 = 0;
    }
    else {
LAB_00b4f770:
      local_100 = *(undefined4 *)((long)param_2 + uVar18);
    }
  }
                    /* try { // try from 00b4f784 to 00c4f78b has its CatchHandler @ 00b4fc6c */
  if ((0x1a < uVar6) && (uVar18 = (ulong)puVar19[0xd], uVar18 != 0)) {
    uVar20 = (ulong)*(uint *)((long)param_2 + uVar18);
    piVar2 = (int *)((long)((long)param_2 + uVar18) + uVar20);
    if (piVar2 != (int *)0x0) {
                    /* try { // try from 00b4f7a0 to 00c4f7a7 has its CatchHandler @ 00b4fc00 */
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 5) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[2];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_2f0,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 7) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[3];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_2d8,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 9) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[4];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
                    /* try { // try from 00b4f878 to 00c4f87f has its CatchHandler @ 00b4fbc8 */
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_2c0,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0xb) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[5];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_2a8,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0xd) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[6];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
                    /* try { // try from 00b4f948 to 00c4f953 has its CatchHandler @ 00b4fcac */
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_290,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0xf) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[7];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
                    /* try { // try from 00b4f9a0 to 00c4f9a7 has its CatchHandler @ 00b4fbb8 */
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
                    /* try { // try from 00b4f9b8 to 00c4f9bf has its CatchHandler @ 00b4fba8 */
                    /* try { // try from 00b4f9c0 to 00c4f9cb has its CatchHandler @ 00b4fbcc */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_278,pcVar15,sVar13);
                    /* try { // try from 00b4f9cc to 00c4f9e3 has its CatchHandler @ 00b4fb6c */
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0x11) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[8];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_260,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0x13) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[9];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_248,pcVar15,sVar13);
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0x15) {
        lVar17 = 0;
      }
      else {
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[10];
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_230,pcVar15,sVar13);
      if ((0x16 < *(ushort *)((long)piVar2 - (long)*piVar2)) &&
         (uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[0xb], uVar21 != 0)) {
        puVar1 = (uint *)((long)piVar2 + uVar21);
        uVar4 = *(uint *)((long)puVar1 + (ulong)*puVar1);
        uVar23 = (ulong)uVar4;
        lVar17 = (long)local_210 - local_218 >> 3;
        uVar21 = lVar17 * -0x5555555555555555;
        if (uVar21 < uVar23) {
                    /* try { // try from 00b4fb24 to 00c4fb2b has its CatchHandler @ 00b4fcac */
                    /* try { // try from 00b4fb2c to 00c4fd13 has its CatchHandler @ 00b4f438 */
          _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                    (&local_218,uVar23 + lVar17 * 0x5555555555555555);
          pbVar25 = local_210;
        }
        else {
          pbVar25 = local_210;
          if ((uVar21 - uVar23 != 0) &&
             (pbVar25 = (byte *)(local_218 + uVar23 * 0x18), pbVar25 != local_210)) {
            bVar5 = local_210[-0x18];
            pbVar12 = local_210 + -0x18;
            pbVar9 = local_210;
            while( true ) {
              pbVar8 = pbVar12;
              if ((bVar5 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4f9cc with catch @ 00b4fb6c */
                _ZdlPv(*(void **)(pbVar9 + -8));
              }
              if (pbVar25 == pbVar8) break;
              bVar5 = pbVar8[-0x18];
              pbVar12 = pbVar8 + -0x18;
              pbVar9 = pbVar8;
            }
          }
        }
        local_210 = pbVar25;
        if (uVar4 != 0) {
          lVar17 = 0;
          lVar24 = uVar20 + uVar18 + (long)param_2;
          do {
            lVar24 = lVar24 + 4;
            uVar21 = (ulong)*(ushort *)((long)piVar2 + (0x16 - (long)*piVar2));
                    /* catch() { ... } // from try @ 00b4f9b8 with catch @ 00b4fba8 */
            lVar22 = local_218 + lVar17;
            lVar3 = uVar21 + *(uint *)((long)piVar2 + uVar21);
                    /* catch() { ... } // from try @ 00b4f9a0 with catch @ 00b4fbb8 */
            pcVar15 = (char *)(lVar24 + lVar3 + (ulong)*(uint *)(lVar24 + lVar3) + 4);
                    /* catch() { ... } // from try @ 00b4f878 with catch @ 00b4fbc8 */
            sVar13 = strlen(pcVar15);
                    /* catch() { ... } // from try @ 00b4f9c0 with catch @ 00b4fbcc */
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (lVar22,pcVar15,sVar13);
            lVar17 = lVar17 + 0x18;
          } while (uVar23 * 0x18 - lVar17 != 0);
        }
      }
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0x19) {
        lVar17 = 0;
      }
      else {
                    /* catch() { ... } // from try @ 00b4f7a0 with catch @ 00b4fc00 */
        uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[0xc];
                    /* catch() { ... } // from try @ 00b4f510 with catch @ 00b4fc04 */
        lVar17 = 0;
        if (uVar21 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar21);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      pcVar15 = __s;
      if (lVar17 != 0) {
        pcVar15 = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(pcVar15);
                    /* catch() { ... } // from try @ 00b4f504 with catch @ 00b4fc38 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&uStack_200,pcVar15,sVar13);
                    /* catch() { ... } // from try @ 00b4f4b8 with catch @ 00b4fc5c */
      if ((0x1a < *(ushort *)((long)piVar2 - (long)*piVar2)) &&
         (uVar21 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[0xd], uVar21 != 0)) {
                    /* catch() { ... } // from try @ 00b4f4a0 with catch @ 00b4fc64 */
        puVar1 = (uint *)((long)piVar2 + uVar21);
                    /* catch() { ... } // from try @ 00b4f550 with catch @ 00b4fc6c
                       catch() { ... } // from try @ 00b4f784 with catch @ 00b4fc6c */
                    /* catch() { ... } // from try @ 00b4f698 with catch @ 00b4fc70 */
        uVar4 = *(uint *)((long)puVar1 + (ulong)*puVar1);
        uVar23 = (ulong)uVar4;
        lVar17 = (long)local_1e0 - lStack_1e8 >> 3;
        uVar21 = lVar17 * -0x5555555555555555;
        if (uVar21 < uVar23) {
                    /* catch() { ... } // from try @ 00b4f598 with catch @ 00b4fc90 */
          _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                    (&lStack_1e8,uVar23 + lVar17 * 0x5555555555555555);
          pbVar25 = local_1e0;
                    /* catch() { ... } // from try @ 00b4f588 with catch @ 00b4fca0 */
        }
        else {
          pbVar25 = local_1e0;
                    /* catch() { ... } // from try @ 00b4f57c with catch @ 00b4fca4 */
                    /* catch() { ... } // from try @ 00b4f948 with catch @ 00b4fcac
                       catch() { ... } // from try @ 00b4fb24 with catch @ 00b4fcac */
          if ((uVar21 - uVar23 != 0) &&
             (pbVar25 = (byte *)(lStack_1e8 + uVar23 * 0x18), pbVar25 != local_1e0)) {
            bVar5 = local_1e0[-0x18];
            pbVar12 = local_1e0 + -0x18;
            pbVar9 = local_1e0;
            while( true ) {
              pbVar8 = pbVar12;
              if ((bVar5 & 1) != 0) {
                _ZdlPv(*(void **)(pbVar9 + -8));
              }
              if (pbVar25 == pbVar8) break;
              bVar5 = pbVar8[-0x18];
              pbVar12 = pbVar8 + -0x18;
              pbVar9 = pbVar8;
            }
          }
        }
        local_1e0 = pbVar25;
        if (uVar4 != 0) {
          lVar17 = 0;
          lVar24 = uVar20 + uVar18 + (long)param_2;
          do {
            lVar24 = lVar24 + 4;
            uVar18 = (ulong)*(ushort *)((long)piVar2 + (0x1a - (long)*piVar2));
            lVar22 = lStack_1e8 + lVar17;
            lVar3 = uVar18 + *(uint *)((long)piVar2 + uVar18);
            pcVar15 = (char *)(lVar24 + lVar3 + (ulong)*(uint *)(lVar24 + lVar3) + 4);
            sVar13 = strlen(pcVar15);
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (lVar22,pcVar15,sVar13);
            lVar17 = lVar17 + 0x18;
          } while (uVar23 * 0x18 - lVar17 != 0);
        }
      }
      if (*(ushort *)((long)piVar2 - (long)*piVar2) < 0x1d) {
        lVar17 = 0;
      }
      else {
        uVar18 = (ulong)((ushort *)((long)piVar2 - (long)*piVar2))[0xe];
        lVar17 = 0;
        if (uVar18 != 0) {
          puVar1 = (uint *)((long)piVar2 + uVar18);
          lVar17 = (long)puVar1 + (ulong)*puVar1;
        }
      }
      if (lVar17 != 0) {
        __s = (char *)(lVar17 + 4);
      }
      sVar13 = strlen(__s);
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (&local_308,__s,sVar13);
      local_c8 = SUB81(&local_2f0,0);
      uStack_c7 = (undefined7)((ulong)&local_2f0 >> 8);
      local_1d0 = &local_308;
    }
  }
LAB_00b4fdc0:
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
  if (*(long *)(lVar7 + 0x28) == local_78) {
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
<a id="insn-00b4efec"></a> `00b4efec` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00b4eff0"></a> `00b4eff0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4eff4"></a> `00b4eff4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4eff8"></a> `00b4eff8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4effc"></a> `00b4effc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4f000"></a> `00b4f000` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4f004"></a> `00b4f004` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f008"></a> `00b4f008` | `ff 83 0b d1` | sub sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00b4f00c"></a> `00b4f00c` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b4f010"></a> `00b4f010` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b4f014"></a> `00b4f014` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b4f018"></a> `00b4f018` | `fc 03 06 91` | add x28,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f01c"></a> `00b4f01c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f020"></a> `00b4f020` | `89 43 01 91` | add x9,x28,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f024"></a> `00b4f024` | `95 23 04 91` | add x21,x28,#0x108 | `FALL_THROUGH`
<a id="insn-00b4f028"></a> `00b4f028` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b4f02c"></a> `00b4f02c` | `ff 7f 1d a9` | stp xzr,xzr,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00b4f030"></a> `00b4f030` | `e0 03 0c ad` | stp q0,q0,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00b4f034"></a> `00b4f034` | `e0 03 0d ad` | stp q0,q0,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00b4f038"></a> `00b4f038` | `ff 27 1c a9` | stp xzr,x9,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00b4f03c"></a> `00b4f03c` | `e0 03 0f ad` | stp q0,q0,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00b4f040"></a> `00b4f040` | `e0 03 10 ad` | stp q0,q0,[sp, #0x200] | `FALL_THROUGH`
<a id="insn-00b4f044"></a> `00b4f044` | `e0 03 11 ad` | stp q0,q0,[sp, #0x220] | `FALL_THROUGH`
<a id="insn-00b4f048"></a> `00b4f048` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00b4f04c"></a> `00b4f04c` | `80 83 8c 3c` | stur q0,[x28, #0xc8] | `FALL_THROUGH`
<a id="insn-00b4f050"></a> `00b4f050` | `80 83 8d 3c` | stur q0,[x28, #0xd8] | `FALL_THROUGH`
<a id="insn-00b4f054"></a> `00b4f054` | `80 83 8e 3c` | stur q0,[x28, #0xe8] | `FALL_THROUGH`
<a id="insn-00b4f058"></a> `00b4f058` | `80 13 8f 3c` | stur q0,[x28, #0xf1] | `FALL_THROUGH`
<a id="insn-00b4f05c"></a> `00b4f05c` | `bf 1a 00 f9` | str xzr,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00b4f060"></a> `00b4f060` | `a0 82 00 ad` | stp q0,q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f064"></a> `00b4f064` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00b4f068"></a> `00b4f068` | `ff bb 00 f9` | str xzr,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00b4f06c"></a> `00b4f06c` | `e0 83 0a ad` | stp q0,q0,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b4f070"></a> `00b4f070` | `e0 83 09 ad` | stp q0,q0,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b4f074"></a> `00b4f074` | `e0 83 08 ad` | stp q0,q0,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b4f078"></a> `00b4f078` | `e0 83 07 ad` | stp q0,q0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b4f07c"></a> `00b4f07c` | `e0 83 06 ad` | stp q0,q0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b4f080"></a> `00b4f080` | `e0 83 05 ad` | stp q0,q0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4f084"></a> `00b4f084` | `e0 83 04 ad` | stp q0,q0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b4f088"></a> `00b4f088` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4f08c"></a> `00b4f08c` | `e0 83 02 ad` | stp q0,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4f090"></a> `00b4f090` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4f094"></a> `00b4f094` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b4f098"></a> `00b4f098` | `28 00 80 b9` | ldrsw x8,[x1] | `FALL_THROUGH`
<a id="insn-00b4f09c"></a> `00b4f09c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b4f0a0"></a> `00b4f0a0` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00b4f0a4"></a> `00b4f0a4` | `28 01 40 79` | ldrh w8,[x9] | `FALL_THROUGH`
<a id="insn-00b4f0a8"></a> `00b4f0a8` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00b4f0ac"></a> `00b4f0ac` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f0b0"></a> `00b4f0b0` | `c3 00 00 54` | b.cc 0x00b4f0c8 | `CONDITIONAL_JUMP`
<a id="insn-00b4f0b4"></a> `00b4f0b4` | `28 09 40 79` | ldrh w8,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f0b8"></a> `00b4f0b8` | `88 00 00 b4` | cbz x8,0x00b4f0c8 | `CONDITIONAL_JUMP`
<a id="insn-00b4f0bc"></a> `00b4f0bc` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f0c0"></a> `00b4f0c0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f0c4"></a> `00b4f0c4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f0c8"></a> `00b4f0c8` | `3b ba ff f0` | adrp x27,0x296000 | `FALL_THROUGH`
<a id="insn-00b4f0cc"></a> `00b4f0cc` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f0d0"></a> `00b4f0d0` | `7b 67 1f 91` | add x27,x27,#0x7d9 | `FALL_THROUGH`
<a id="insn-00b4f0d4"></a> `00b4f0d4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f0d8"></a> `00b4f0d8` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f0dc"></a> `00b4f0dc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f0e0"></a> `00b4f0e0` | `ec 2f 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f0e4"></a> `00b4f0e4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f0e8"></a> `00b4f0e8` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f0ec"></a> `00b4f0ec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f0f0"></a> `00b4f0f0` | `10 3c 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f0f4"></a> `00b4f0f4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f0f8"></a> `00b4f0f8` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f0fc"></a> `00b4f0fc` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f100"></a> `00b4f100` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00b4f104"></a> `00b4f104` | `e3 00 00 54` | b.cc 0x00b4f120 | `CONDITIONAL_JUMP`
<a id="insn-00b4f108"></a> `00b4f108` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00b4f10c"></a> `00b4f10c` | `c8 00 00 b4` | cbz x8,0x00b4f124 | `CONDITIONAL_JUMP`
<a id="insn-00b4f110"></a> `00b4f110` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f114"></a> `00b4f114` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f118"></a> `00b4f118` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f11c"></a> `00b4f11c` | `02 00 00 14` | b 0x00b4f124 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f120"></a> `00b4f120` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f124"></a> `00b4f124` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f128"></a> `00b4f128` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f12c"></a> `00b4f12c` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f130"></a> `00b4f130` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f134"></a> `00b4f134` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f138"></a> `00b4f138` | `17 61 00 91` | add x23,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b4f13c"></a> `00b4f13c` | `d5 2f 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f140"></a> `00b4f140` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f144"></a> `00b4f144` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f148"></a> `00b4f148` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f14c"></a> `00b4f14c` | `f9 3b 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f150"></a> `00b4f150` | `89 02 80 b9` | ldrsw x9,[x20] | `FALL_THROUGH`
<a id="insn-00b4f154"></a> `00b4f154` | `8a 02 09 cb` | sub x10,x20,x9 | `FALL_THROUGH`
<a id="insn-00b4f158"></a> `00b4f158` | `48 01 40 79` | ldrh w8,[x10] | `FALL_THROUGH`
<a id="insn-00b4f15c"></a> `00b4f15c` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00b4f160"></a> `00b4f160` | `e8 03 09 cb` | neg x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f164"></a> `00b4f164` | `c3 0f 00 54` | b.cc 0x00b4f35c | `CONDITIONAL_JUMP`
<a id="insn-00b4f168"></a> `00b4f168` | `4a 15 40 79` | ldrh w10,[x10, #0xa] | `FALL_THROUGH`
<a id="insn-00b4f16c"></a> `00b4f16c` | `8a 0f 00 b4` | cbz x10,0x00b4f35c | `CONDITIONAL_JUMP`
<a id="insn-00b4f170"></a> `00b4f170` | `8a 02 0a 8b` | add x10,x20,x10 | `FALL_THROUGH`
<a id="insn-00b4f174"></a> `00b4f174` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00b4f178"></a> `00b4f178` | `4a 01 0b ab` | adds x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b4f17c"></a> `00b4f17c` | `00 0f 00 54` | b.eq 0x00b4f35c | `CONDITIONAL_JUMP`
<a id="insn-00b4f180"></a> `00b4f180` | `4a 01 40 b9` | ldr w10,[x10] | `FALL_THROUGH`
<a id="insn-00b4f184"></a> `00b4f184` | `ca 0e 00 34` | cbz w10,0x00b4f35c | `CONDITIONAL_JUMP`
<a id="insn-00b4f188"></a> `00b4f188` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f18c"></a> `00b4f18c` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00b4f190"></a> `00b4f190` | `16 21 01 91` | add x22,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00b4f194"></a> `00b4f194` | `53 f5 7e d3` | lsl x19,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00b4f198"></a> `00b4f198` | `f9 03 00 f9` | str x25,[sp] | `FALL_THROUGH`
<a id="insn-00b4f19c"></a> `00b4f19c` | `05 00 00 14` | b 0x00b4f1b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f1a0"></a> `00b4f1a0` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00b4f1a4"></a> `00b4f1a4` | `5a 13 00 91` | add x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f1a8"></a> `00b4f1a8` | `7f 02 1a eb` | cmp x19,x26 | `FALL_THROUGH`
<a id="insn-00b4f1ac"></a> `00b4f1ac` | `20 0d 00 54` | b.eq 0x00b4f350 | `CONDITIONAL_JUMP`
<a id="insn-00b4f1b0"></a> `00b4f1b0` | `88 c2 29 cb` | sub x8,x20,w9, SXTW  | `FALL_THROUGH`
<a id="insn-00b4f1b4"></a> `00b4f1b4` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00b4f1b8"></a> `00b4f1b8` | `89 6a 68 b8` | ldr w9,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4f1bc"></a> `00b4f1bc` | `0b 01 09 8b` | add x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f1c0"></a> `00b4f1c0` | `8a 02 0b 8b` | add x10,x20,x11 | `FALL_THROUGH`
<a id="insn-00b4f1c4"></a> `00b4f1c4` | `4a 01 1a 8b` | add x10,x10,x26 | `FALL_THROUGH`
<a id="insn-00b4f1c8"></a> `00b4f1c8` | `4a 05 40 b9` | ldr w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f1cc"></a> `00b4f1cc` | `6c 01 0a 8b` | add x12,x11,x10 | `FALL_THROUGH`
<a id="insn-00b4f1d0"></a> `00b4f1d0` | `8b 02 0c 8b` | add x11,x20,x12 | `FALL_THROUGH`
<a id="insn-00b4f1d4"></a> `00b4f1d4` | `6b 01 1a 8b` | add x11,x11,x26 | `FALL_THROUGH`
<a id="insn-00b4f1d8"></a> `00b4f1d8` | `6b 05 80 b9` | ldrsw x11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f1dc"></a> `00b4f1dc` | `8c 01 0b cb` | sub x12,x12,x11 | `FALL_THROUGH`
<a id="insn-00b4f1e0"></a> `00b4f1e0` | `4c 03 0c 8b` | add x12,x26,x12 | `FALL_THROUGH`
<a id="insn-00b4f1e4"></a> `00b4f1e4` | `8d 02 0c 8b` | add x13,x20,x12 | `FALL_THROUGH`
<a id="insn-00b4f1e8"></a> `00b4f1e8` | `ac 09 40 79` | ldrh w12,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f1ec"></a> `00b4f1ec` | `9f 15 00 71` | cmp w12,#0x5 | `FALL_THROUGH`
<a id="insn-00b4f1f0"></a> `00b4f1f0` | `43 04 00 54` | b.cc 0x00b4f278 | `CONDITIONAL_JUMP`
<a id="insn-00b4f1f4"></a> `00b4f1f4` | `ad 11 40 79` | ldrh w13,[x13, #0x8] | `FALL_THROUGH`
<a id="insn-00b4f1f8"></a> `00b4f1f8` | `6d 01 00 b4` | cbz x13,0x00b4f224 | `CONDITIONAL_JUMP`
<a id="insn-00b4f1fc"></a> `00b4f1fc` | `0e 01 09 8b` | add x14,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f200"></a> `00b4f200` | `ce 01 0a 8b` | add x14,x14,x10 | `FALL_THROUGH`
<a id="insn-00b4f204"></a> `00b4f204` | `cd 01 0d 8b` | add x13,x14,x13 | `FALL_THROUGH`
<a id="insn-00b4f208"></a> `00b4f208` | `8e 02 0d 8b` | add x14,x20,x13 | `FALL_THROUGH`
<a id="insn-00b4f20c"></a> `00b4f20c` | `ce 01 1a 8b` | add x14,x14,x26 | `FALL_THROUGH`
<a id="insn-00b4f210"></a> `00b4f210` | `ce 05 40 b9` | ldr w14,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f214"></a> `00b4f214` | `ad 01 0e 8b` | add x13,x13,x14 | `FALL_THROUGH`
<a id="insn-00b4f218"></a> `00b4f218` | `4d 03 0d 8b` | add x13,x26,x13 | `FALL_THROUGH`
<a id="insn-00b4f21c"></a> `00b4f21c` | `8d 02 0d 8b` | add x13,x20,x13 | `FALL_THROUGH`
<a id="insn-00b4f220"></a> `00b4f220` | `ad 11 00 91` | add x13,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f224"></a> `00b4f224` | `ae 11 00 91` | add x14,x13,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f228"></a> `00b4f228` | `bf 01 00 f1` | cmp x13,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f22c"></a> `00b4f22c` | `61 03 8e 9a` | csel x1,x27,x14,eq | `FALL_THROUGH`
<a id="insn-00b4f230"></a> `00b4f230` | `9f 1d 00 71` | cmp w12,#0x7 | `FALL_THROUGH`
<a id="insn-00b4f234"></a> `00b4f234` | `83 02 00 54` | b.cc 0x00b4f284 | `CONDITIONAL_JUMP`
<a id="insn-00b4f238"></a> `00b4f238` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f23c"></a> `00b4f23c` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b4f240"></a> `00b4f240` | `09 01 0b cb` | sub x9,x8,x11 | `FALL_THROUGH`
<a id="insn-00b4f244"></a> `00b4f244` | `49 03 09 8b` | add x9,x26,x9 | `FALL_THROUGH`
<a id="insn-00b4f248"></a> `00b4f248` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00b4f24c"></a> `00b4f24c` | `29 15 40 79` | ldrh w9,[x9, #0xa] | `FALL_THROUGH`
<a id="insn-00b4f250"></a> `00b4f250` | `a9 01 00 b4` | cbz x9,0x00b4f284 | `CONDITIONAL_JUMP`
<a id="insn-00b4f254"></a> `00b4f254` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f258"></a> `00b4f258` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f25c"></a> `00b4f25c` | `29 01 1a 8b` | add x9,x9,x26 | `FALL_THROUGH`
<a id="insn-00b4f260"></a> `00b4f260` | `29 05 40 b9` | ldr w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f264"></a> `00b4f264` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f268"></a> `00b4f268` | `48 03 08 8b` | add x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00b4f26c"></a> `00b4f26c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f270"></a> `00b4f270` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f274"></a> `00b4f274` | `05 00 00 14` | b 0x00b4f288 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f278"></a> `00b4f278` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f27c"></a> `00b4f27c` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00b4f280"></a> `00b4f280` | `02 00 00 14` | b 0x00b4f288 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f284"></a> `00b4f284` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f288"></a> `00b4f288` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f28c"></a> `00b4f28c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f290"></a> `00b4f290` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f294"></a> `00b4f294` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4f298"></a> `00b4f298` | `ea 3c 02 94` | bl 0x00bde640 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f29c"></a> `00b4f29c` | `a1 c3 01 d1` | sub x1,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00b4f2a0"></a> `00b4f2a0` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4f2a4"></a> `00b4f2a4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f2a8"></a> `00b4f2a8` | `0a ed e3 97` | bl 0x0044a6d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f2ac"></a> `00b4f2ac` | `18 00 40 f9` | ldr x24,[x0] | `FALL_THROUGH`
<a id="insn-00b4f2b0"></a> `00b4f2b0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00b4f2b4"></a> `00b4f2b4` | `78 03 00 b5` | cbnz x24,0x00b4f320 | `CONDITIONAL_JUMP`
<a id="insn-00b4f2b8"></a> `00b4f2b8` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f2bc"></a> `00b4f2bc` | `21 2f 02 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f2c0"></a> `00b4f2c0` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4f2c4"></a> `00b4f2c4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4f2c8"></a> `00b4f2c8` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b4f2cc"></a> `00b4f2cc` | `ff ff 02 a9` | stp xzr,xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b4f2d0"></a> `00b4f2d0` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4f2d4"></a> `00b4f2d4` | `1f 7c 04 a9` | stp xzr,xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00b4f2d8"></a> `00b4f2d8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b4f2dc"></a> `00b4f2dc` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b4f2e0"></a> `00b4f2e0` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00b4f2e4"></a> `00b4f2e4` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f2e8"></a> `00b4f2e8` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00b4f2ec"></a> `00b4f2ec` | `e8 e7 40 f9` | ldr x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00b4f2f0"></a> `00b4f2f0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b4f2f4"></a> `00b4f2f4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b4f2f8"></a> `00b4f2f8` | `88 00 00 b4` | cbz x8,0x00b4f308 | `CONDITIONAL_JUMP`
<a id="insn-00b4f2fc"></a> `00b4f2fc` | `e8 e7 00 f9` | str x8,[sp, #0x1c8] | `FALL_THROUGH`
<a id="insn-00b4f300"></a> `00b4f300` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00b4f304"></a> `00b4f304` | `02 00 00 14` | b 0x00b4f30c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f308"></a> `00b4f308` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00b4f30c"></a> `00b4f30c` | `e0 eb 40 f9` | ldr x0,[sp, #0x1d0] | `FALL_THROUGH`
<a id="insn-00b4f310"></a> `00b4f310` | `d4 3c 02 94` | bl 0x00bde660 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f314"></a> `00b4f314` | `e8 ef 40 f9` | ldr x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00b4f318"></a> `00b4f318` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4f31c"></a> `00b4f31c` | `e8 ef 00 f9` | str x8,[sp, #0x1d8] | `FALL_THROUGH`
<a id="insn-00b4f320"></a> `00b4f320` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f324"></a> `00b4f324` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-00b4f328"></a> `00b4f328` | `5a 2f 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f32c"></a> `00b4f32c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f330"></a> `00b4f330` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b4f334"></a> `00b4f334` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b4f338"></a> `00b4f338` | `7e 3b 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f33c"></a> `00b4f33c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4f340"></a> `00b4f340` | `08 f3 07 36` | tbz w8,#0x0,0x00b4f1a0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f344"></a> `00b4f344` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4f348"></a> `00b4f348` | `06 2f 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f34c"></a> `00b4f34c` | `95 ff ff 17` | b 0x00b4f1a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f350"></a> `00b4f350` | `f9 03 40 f9` | ldr x25,[sp] | `FALL_THROUGH`
<a id="insn-00b4f354"></a> `00b4f354` | `28 7d 40 93` | sxtw x8,w9 | `FALL_THROUGH`
<a id="insn-00b4f358"></a> `00b4f358` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b4f35c"></a> `00b4f35c` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f360"></a> `00b4f360` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00b4f364"></a> `00b4f364` | `5f 35 00 71` | cmp w10,#0xd | `FALL_THROUGH`
<a id="insn-00b4f368"></a> `00b4f368` | `43 06 00 54` | b.cc 0x00b4f430 | `CONDITIONAL_JUMP`
<a id="insn-00b4f36c"></a> `00b4f36c` | `29 19 40 79` | ldrh w9,[x9, #0xc] | `FALL_THROUGH`
<a id="insn-00b4f370"></a> `00b4f370` | `09 06 00 b4` | cbz x9,0x00b4f430 | `CONDITIONAL_JUMP`
<a id="insn-00b4f374"></a> `00b4f374` | `89 02 09 8b` | add x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00b4f378"></a> `00b4f378` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b4f37c"></a> `00b4f37c` | `29 01 0a ab` | adds x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00b4f380"></a> `00b4f380` | `80 05 00 54` | b.eq 0x00b4f430 | `CONDITIONAL_JUMP`
<a id="insn-00b4f384"></a> `00b4f384` | `e8 fb 40 f9` | ldr x8,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00b4f388"></a> `00b4f388` | `f6 f3 40 f9` | ldr x22,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00b4f38c"></a> `00b4f38c` | `37 01 40 b9` | ldr w23,[x9] | `FALL_THROUGH`
<a id="insn-00b4f390"></a> `00b4f390` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00b4f394"></a> `00b4f394` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00b4f398"></a> `00b4f398` | `42 02 00 54` | b.cs 0x00b4f3e0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f39c"></a> `00b4f39c` | `f3 f7 40 f9` | ldr x19,[sp, #0x1e8] | `FALL_THROUGH`
<a id="insn-00b4f3a0"></a> `00b4f3a0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f3a4"></a> `00b4f3a4` | `e7 2e 02 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f3a8"></a> `00b4f3a8` | `62 02 16 cb` | sub x2,x19,x22 | `FALL_THROUGH`
<a id="insn-00b4f3ac"></a> `00b4f3ac` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00b4f3b0"></a> `00b4f3b0` | `13 00 02 8b` | add x19,x0,x2 | `FALL_THROUGH`
<a id="insn-00b4f3b4"></a> `00b4f3b4` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-00b4f3b8"></a> `00b4f3b8` | `17 00 17 8b` | add x23,x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f3bc"></a> `00b4f3bc` | `8b 00 00 54` | b.lt 0x00b4f3cc | `CONDITIONAL_JUMP`
<a id="insn-00b4f3c0"></a> `00b4f3c0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b4f3c4"></a> `00b4f3c4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f3c8"></a> `00b4f3c8` | `3a 2f 02 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f3cc"></a> `00b4f3cc` | `f8 4f 1e a9` | stp x24,x19,[sp, #0x1e0] | `FALL_THROUGH`
<a id="insn-00b4f3d0"></a> `00b4f3d0` | `f7 fb 00 f9` | str x23,[sp, #0x1f0] | `FALL_THROUGH`
<a id="insn-00b4f3d4"></a> `00b4f3d4` | `76 00 00 b4` | cbz x22,0x00b4f3e0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f3d8"></a> `00b4f3d8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f3dc"></a> `00b4f3dc` | `e1 2e 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f3e0"></a> `00b4f3e0` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f3e4"></a> `00b4f3e4` | `80 83 01 91` | add x0,x28,#0x60 | `FALL_THROUGH`
<a id="insn-00b4f3e8"></a> `00b4f3e8` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f3ec"></a> `00b4f3ec` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00b4f3f0"></a> `00b4f3f0` | `89 02 08 8b` | add x9,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f3f4"></a> `00b4f3f4` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00b4f3f8"></a> `00b4f3f8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f3fc"></a> `00b4f3fc` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00b4f400"></a> `00b4f400` | `e8 03 89 9a` | csel x8,xzr,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f404"></a> `00b4f404` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f408"></a> `00b4f408` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b4f40c"></a> `00b4f40c` | `28 01 40 b9` | ldr w8,[x9] | `FALL_THROUGH`
<a id="insn-00b4f410"></a> `00b4f410` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00b4f414"></a> `00b4f414` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f418"></a> `00b4f418` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f41c"></a> `00b4f41c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4f420"></a> `00b4f420` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4f424"></a> `00b4f424` | `17 44 02 94` | bl 0x00be0480 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f428"></a> `00b4f428` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f42c"></a> `00b4f42c` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-00b4f430"></a> `00b4f430` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f434"></a> `00b4f434` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f438"></a> `00b4f438` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00b4f43c"></a> `00b4f43c` | `e3 00 00 54` | b.cc 0x00b4f458 | `CONDITIONAL_JUMP`
<a id="insn-00b4f440"></a> `00b4f440` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00b4f444"></a> `00b4f444` | `c8 00 00 b4` | cbz x8,0x00b4f45c | `CONDITIONAL_JUMP`
<a id="insn-00b4f448"></a> `00b4f448` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f44c"></a> `00b4f44c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f450"></a> `00b4f450` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f454"></a> `00b4f454` | `02 00 00 14` | b 0x00b4f45c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f458"></a> `00b4f458` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f45c"></a> `00b4f45c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f460"></a> `00b4f460` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f464"></a> `00b4f464` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f468"></a> `00b4f468` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f46c"></a> `00b4f46c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f470"></a> `00b4f470` | `17 e1 01 91` | add x23,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00b4f474"></a> `00b4f474` | `07 2f 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f478"></a> `00b4f478` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f47c"></a> `00b4f47c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f480"></a> `00b4f480` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f484"></a> `00b4f484` | `2b 3b 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f488"></a> `00b4f488` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f48c"></a> `00b4f48c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f490"></a> `00b4f490` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f494"></a> `00b4f494` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00b4f498"></a> `00b4f498` | `e3 00 00 54` | b.cc 0x00b4f4b4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f49c"></a> `00b4f49c` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f4a0"></a> `00b4f4a0` | `c8 00 00 b4` | cbz x8,0x00b4f4b8 | `CONDITIONAL_JUMP`
<a id="insn-00b4f4a4"></a> `00b4f4a4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f4a8"></a> `00b4f4a8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f4ac"></a> `00b4f4ac` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f4b0"></a> `00b4f4b0` | `02 00 00 14` | b 0x00b4f4b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f4b4"></a> `00b4f4b4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f4b8"></a> `00b4f4b8` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f4bc"></a> `00b4f4bc` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f4c0"></a> `00b4f4c0` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f4c4"></a> `00b4f4c4` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f4c8"></a> `00b4f4c8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f4cc"></a> `00b4f4cc` | `17 41 02 91` | add x23,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00b4f4d0"></a> `00b4f4d0` | `f0 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f4d4"></a> `00b4f4d4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f4d8"></a> `00b4f4d8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f4dc"></a> `00b4f4dc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f4e0"></a> `00b4f4e0` | `14 3b 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f4e4"></a> `00b4f4e4` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f4e8"></a> `00b4f4e8` | `96 23 03 91` | add x22,x28,#0xc8 | `FALL_THROUGH`
<a id="insn-00b4f4ec"></a> `00b4f4ec` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f4f0"></a> `00b4f4f0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f4f4"></a> `00b4f4f4` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00b4f4f8"></a> `00b4f4f8` | `e3 00 00 54` | b.cc 0x00b4f514 | `CONDITIONAL_JUMP`
<a id="insn-00b4f4fc"></a> `00b4f4fc` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00b4f500"></a> `00b4f500` | `c8 00 00 b4` | cbz x8,0x00b4f518 | `CONDITIONAL_JUMP`
<a id="insn-00b4f504"></a> `00b4f504` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f508"></a> `00b4f508` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f50c"></a> `00b4f50c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f510"></a> `00b4f510` | `02 00 00 14` | b 0x00b4f518 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f514"></a> `00b4f514` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f518"></a> `00b4f518` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f51c"></a> `00b4f51c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f520"></a> `00b4f520` | `77 03 89 9a` | csel x23,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f524"></a> `00b4f524` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f528"></a> `00b4f528` | `da 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f52c"></a> `00b4f52c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f530"></a> `00b4f530` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f534"></a> `00b4f534` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b4f538"></a> `00b4f538` | `fe 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f53c"></a> `00b4f53c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f540"></a> `00b4f540` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f544"></a> `00b4f544` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f548"></a> `00b4f548` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00b4f54c"></a> `00b4f54c` | `e3 00 00 54` | b.cc 0x00b4f568 | `CONDITIONAL_JUMP`
<a id="insn-00b4f550"></a> `00b4f550` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b4f554"></a> `00b4f554` | `c8 00 00 b4` | cbz x8,0x00b4f56c | `CONDITIONAL_JUMP`
<a id="insn-00b4f558"></a> `00b4f558` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f55c"></a> `00b4f55c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f560"></a> `00b4f560` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f564"></a> `00b4f564` | `02 00 00 14` | b 0x00b4f56c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f568"></a> `00b4f568` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f56c"></a> `00b4f56c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f570"></a> `00b4f570` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f574"></a> `00b4f574` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f578"></a> `00b4f578` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f57c"></a> `00b4f57c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f580"></a> `00b4f580` | `17 81 03 91` | add x23,x8,#0xe0 | `FALL_THROUGH`
<a id="insn-00b4f584"></a> `00b4f584` | `c3 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f588"></a> `00b4f588` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f58c"></a> `00b4f58c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b4f590"></a> `00b4f590` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f594"></a> `00b4f594` | `e7 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f598"></a> `00b4f598` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f59c"></a> `00b4f59c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f5a0"></a> `00b4f5a0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f5a4"></a> `00b4f5a4` | `3f 71 00 71` | cmp w9,#0x1c | `FALL_THROUGH`
<a id="insn-00b4f5a8"></a> `00b4f5a8` | `e9 01 00 54` | b.ls 0x00b4f5e4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f5ac"></a> `00b4f5ac` | `0a 39 40 79` | ldrh w10,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00b4f5b0"></a> `00b4f5b0` | `8a 00 00 b4` | cbz x10,0x00b4f5c0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f5b4"></a> `00b4f5b4` | `8a 6a 6a 38` | ldrb w10,[x20, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00b4f5b8"></a> `00b4f5b8` | `5f 01 00 71` | cmp w10,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f5bc"></a> `00b4f5bc` | `ea 07 9f 1a` | cset w10,ne | `FALL_THROUGH`
<a id="insn-00b4f5c0"></a> `00b4f5c0` | `3f 7d 00 71` | cmp w9,#0x1f | `FALL_THROUGH`
<a id="insn-00b4f5c4"></a> `00b4f5c4` | `ea 03 0a 39` | strb w10,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00b4f5c8"></a> `00b4f5c8` | `43 01 00 54` | b.cc 0x00b4f5f0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f5cc"></a> `00b4f5cc` | `08 3d 40 79` | ldrh w8,[x8, #0x1e] | `FALL_THROUGH`
<a id="insn-00b4f5d0"></a> `00b4f5d0` | `28 01 00 b4` | cbz x8,0x00b4f5f4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f5d4"></a> `00b4f5d4` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f5d8"></a> `00b4f5d8` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f5dc"></a> `00b4f5dc` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f5e0"></a> `00b4f5e0` | `05 00 00 14` | b 0x00b4f5f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f5e4"></a> `00b4f5e4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f5e8"></a> `00b4f5e8` | `ff 03 0a 39` | strb wzr,[sp, #0x280] | `FALL_THROUGH`
<a id="insn-00b4f5ec"></a> `00b4f5ec` | `02 00 00 14` | b 0x00b4f5f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f5f0"></a> `00b4f5f0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f5f4"></a> `00b4f5f4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f5f8"></a> `00b4f5f8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f5fc"></a> `00b4f5fc` | `76 03 89 9a` | csel x22,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f600"></a> `00b4f600` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f604"></a> `00b4f604` | `a3 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f608"></a> `00b4f608` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f60c"></a> `00b4f60c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f610"></a> `00b4f610` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4f614"></a> `00b4f614` | `c7 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f618"></a> `00b4f618` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f61c"></a> `00b4f61c` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f620"></a> `00b4f620` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f624"></a> `00b4f624` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00b4f628"></a> `00b4f628` | `e3 00 00 54` | b.cc 0x00b4f644 | `CONDITIONAL_JUMP`
<a id="insn-00b4f62c"></a> `00b4f62c` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b4f630"></a> `00b4f630` | `c8 00 00 b4` | cbz x8,0x00b4f648 | `CONDITIONAL_JUMP`
<a id="insn-00b4f634"></a> `00b4f634` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f638"></a> `00b4f638` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f63c"></a> `00b4f63c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f640"></a> `00b4f640` | `02 00 00 14` | b 0x00b4f648 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f644"></a> `00b4f644` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f648"></a> `00b4f648` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f64c"></a> `00b4f64c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f650"></a> `00b4f650` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f654"></a> `00b4f654` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f658"></a> `00b4f658` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f65c"></a> `00b4f65c` | `16 c1 00 91` | add x22,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00b4f660"></a> `00b4f660` | `8c 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f664"></a> `00b4f664` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f668"></a> `00b4f668` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f66c"></a> `00b4f66c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f670"></a> `00b4f670` | `b0 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f674"></a> `00b4f674` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f678"></a> `00b4f678` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f67c"></a> `00b4f67c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f680"></a> `00b4f680` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00b4f684"></a> `00b4f684` | `e3 00 00 54` | b.cc 0x00b4f6a0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f688"></a> `00b4f688` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00b4f68c"></a> `00b4f68c` | `c8 00 00 b4` | cbz x8,0x00b4f6a4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f690"></a> `00b4f690` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f694"></a> `00b4f694` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f698"></a> `00b4f698` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f69c"></a> `00b4f69c` | `02 00 00 14` | b 0x00b4f6a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f6a0"></a> `00b4f6a0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f6a4"></a> `00b4f6a4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f6a8"></a> `00b4f6a8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f6ac"></a> `00b4f6ac` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f6b0"></a> `00b4f6b0` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f6b4"></a> `00b4f6b4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f6b8"></a> `00b4f6b8` | `16 a1 02 91` | add x22,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00b4f6bc"></a> `00b4f6bc` | `75 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f6c0"></a> `00b4f6c0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f6c4"></a> `00b4f6c4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f6c8"></a> `00b4f6c8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f6cc"></a> `00b4f6cc` | `99 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f6d0"></a> `00b4f6d0` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f6d4"></a> `00b4f6d4` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f6d8"></a> `00b4f6d8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f6dc"></a> `00b4f6dc` | `3f 8d 00 71` | cmp w9,#0x23 | `FALL_THROUGH`
<a id="insn-00b4f6e0"></a> `00b4f6e0` | `e3 00 00 54` | b.cc 0x00b4f6fc | `CONDITIONAL_JUMP`
<a id="insn-00b4f6e4"></a> `00b4f6e4` | `08 45 40 79` | ldrh w8,[x8, #0x22] | `FALL_THROUGH`
<a id="insn-00b4f6e8"></a> `00b4f6e8` | `c8 00 00 b4` | cbz x8,0x00b4f700 | `CONDITIONAL_JUMP`
<a id="insn-00b4f6ec"></a> `00b4f6ec` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f6f0"></a> `00b4f6f0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f6f4"></a> `00b4f6f4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f6f8"></a> `00b4f6f8` | `02 00 00 14` | b 0x00b4f700 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f6fc"></a> `00b4f6fc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f700"></a> `00b4f700` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f704"></a> `00b4f704` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f708"></a> `00b4f708` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f70c"></a> `00b4f70c` | `e8 03 06 91` | add x8,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4f710"></a> `00b4f710` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f714"></a> `00b4f714` | `16 81 04 91` | add x22,x8,#0x120 | `FALL_THROUGH`
<a id="insn-00b4f718"></a> `00b4f718` | `5e 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f71c"></a> `00b4f71c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f720"></a> `00b4f720` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f724"></a> `00b4f724` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f728"></a> `00b4f728` | `82 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f72c"></a> `00b4f72c` | `88 02 80 b9` | ldrsw x8,[x20] | `FALL_THROUGH`
<a id="insn-00b4f730"></a> `00b4f730` | `88 02 08 cb` | sub x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b4f734"></a> `00b4f734` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f738"></a> `00b4f738` | `3f 85 00 71` | cmp w9,#0x21 | `FALL_THROUGH`
<a id="insn-00b4f73c"></a> `00b4f73c` | `03 01 00 54` | b.cc 0x00b4f75c | `CONDITIONAL_JUMP`
<a id="insn-00b4f740"></a> `00b4f740` | `0a 41 40 79` | ldrh w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b4f744"></a> `00b4f744` | `4a 00 00 b4` | cbz x10,0x00b4f74c | `CONDITIONAL_JUMP`
<a id="insn-00b4f748"></a> `00b4f748` | `8a 6a 6a f8` | ldr x10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4f74c"></a> `00b4f74c` | `ea 5f 01 f9` | str x10,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00b4f750"></a> `00b4f750` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00b4f754"></a> `00b4f754` | `ea 00 00 b5` | cbnz x10,0x00b4f770 | `CONDITIONAL_JUMP`
<a id="insn-00b4f758"></a> `00b4f758` | `07 00 00 14` | b 0x00b4f774 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f75c"></a> `00b4f75c` | `3f 51 00 71` | cmp w9,#0x14 | `FALL_THROUGH`
<a id="insn-00b4f760"></a> `00b4f760` | `ff 5f 01 f9` | str xzr,[sp, #0x2b8] | `FALL_THROUGH`
<a id="insn-00b4f764"></a> `00b4f764` | `29 03 00 54` | b.ls 0x00b4f7c8 | `CONDITIONAL_JUMP`
<a id="insn-00b4f768"></a> `00b4f768` | `0a 29 40 79` | ldrh w10,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00b4f76c"></a> `00b4f76c` | `4a 00 00 b4` | cbz x10,0x00b4f774 | `CONDITIONAL_JUMP`
<a id="insn-00b4f770"></a> `00b4f770` | `8a 6a 6a b8` | ldr w10,[x20, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4f774"></a> `00b4f774` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00b4f778"></a> `00b4f778` | `ea 43 02 b9` | str w10,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00b4f77c"></a> `00b4f77c` | `23 32 00 54` | b.cc 0x00b4fdc0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f780"></a> `00b4f780` | `18 35 40 79` | ldrh w24,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00b4f784"></a> `00b4f784` | `f8 31 00 b4` | cbz x24,0x00b4fdc0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f788"></a> `00b4f788` | `88 02 18 8b` | add x8,x20,x24 | `FALL_THROUGH`
<a id="insn-00b4f78c"></a> `00b4f78c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b4f790"></a> `00b4f790` | `17 01 0a ab` | adds x23,x8,x10 | `FALL_THROUGH`
<a id="insn-00b4f794"></a> `00b4f794` | `60 31 00 54` | b.eq 0x00b4fdc0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f798"></a> `00b4f798` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f79c"></a> `00b4f79c` | `ea 03 00 f9` | str x10,[sp] | `FALL_THROUGH`
<a id="insn-00b4f7a0"></a> `00b4f7a0` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f7a4"></a> `00b4f7a4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f7a8"></a> `00b4f7a8` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-00b4f7ac"></a> `00b4f7ac` | `23 01 00 54` | b.cc 0x00b4f7d0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f7b0"></a> `00b4f7b0` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f7b4"></a> `00b4f7b4` | `08 01 00 b4` | cbz x8,0x00b4f7d4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f7b8"></a> `00b4f7b8` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f7bc"></a> `00b4f7bc` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f7c0"></a> `00b4f7c0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f7c4"></a> `00b4f7c4` | `04 00 00 14` | b 0x00b4f7d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f7c8"></a> `00b4f7c8` | `ff 43 02 b9` | str wzr,[sp, #0x240] | `FALL_THROUGH`
<a id="insn-00b4f7cc"></a> `00b4f7cc` | `7d 01 00 14` | b 0x00b4fdc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f7d0"></a> `00b4f7d0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f7d4"></a> `00b4f7d4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f7d8"></a> `00b4f7d8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f7dc"></a> `00b4f7dc` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f7e0"></a> `00b4f7e0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f7e4"></a> `00b4f7e4` | `2b 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f7e8"></a> `00b4f7e8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f7ec"></a> `00b4f7ec` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f7f0"></a> `00b4f7f0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f7f4"></a> `00b4f7f4` | `4f 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f7f8"></a> `00b4f7f8` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f7fc"></a> `00b4f7fc` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f800"></a> `00b4f800` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f804"></a> `00b4f804` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00b4f808"></a> `00b4f808` | `e3 00 00 54` | b.cc 0x00b4f824 | `CONDITIONAL_JUMP`
<a id="insn-00b4f80c"></a> `00b4f80c` | `08 0d 40 79` | ldrh w8,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00b4f810"></a> `00b4f810` | `c8 00 00 b4` | cbz x8,0x00b4f828 | `CONDITIONAL_JUMP`
<a id="insn-00b4f814"></a> `00b4f814` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f818"></a> `00b4f818` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f81c"></a> `00b4f81c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f820"></a> `00b4f820` | `02 00 00 14` | b 0x00b4f828 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f824"></a> `00b4f824` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f828"></a> `00b4f828` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f82c"></a> `00b4f82c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f830"></a> `00b4f830` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f834"></a> `00b4f834` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f838"></a> `00b4f838` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f83c"></a> `00b4f83c` | `16 61 00 91` | add x22,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b4f840"></a> `00b4f840` | `14 2e 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f844"></a> `00b4f844` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f848"></a> `00b4f848` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f84c"></a> `00b4f84c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f850"></a> `00b4f850` | `38 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f854"></a> `00b4f854` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f858"></a> `00b4f858` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f85c"></a> `00b4f85c` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f860"></a> `00b4f860` | `3f 25 00 71` | cmp w9,#0x9 | `FALL_THROUGH`
<a id="insn-00b4f864"></a> `00b4f864` | `e3 00 00 54` | b.cc 0x00b4f880 | `CONDITIONAL_JUMP`
<a id="insn-00b4f868"></a> `00b4f868` | `08 11 40 79` | ldrh w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b4f86c"></a> `00b4f86c` | `c8 00 00 b4` | cbz x8,0x00b4f884 | `CONDITIONAL_JUMP`
<a id="insn-00b4f870"></a> `00b4f870` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f874"></a> `00b4f874` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f878"></a> `00b4f878` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f87c"></a> `00b4f87c` | `02 00 00 14` | b 0x00b4f884 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f880"></a> `00b4f880` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f884"></a> `00b4f884` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f888"></a> `00b4f888` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f88c"></a> `00b4f88c` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f890"></a> `00b4f890` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f894"></a> `00b4f894` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f898"></a> `00b4f898` | `16 c1 00 91` | add x22,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00b4f89c"></a> `00b4f89c` | `fd 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f8a0"></a> `00b4f8a0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f8a4"></a> `00b4f8a4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f8a8"></a> `00b4f8a8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f8ac"></a> `00b4f8ac` | `21 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f8b0"></a> `00b4f8b0` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f8b4"></a> `00b4f8b4` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f8b8"></a> `00b4f8b8` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f8bc"></a> `00b4f8bc` | `3f 2d 00 71` | cmp w9,#0xb | `FALL_THROUGH`
<a id="insn-00b4f8c0"></a> `00b4f8c0` | `e3 00 00 54` | b.cc 0x00b4f8dc | `CONDITIONAL_JUMP`
<a id="insn-00b4f8c4"></a> `00b4f8c4` | `08 15 40 79` | ldrh w8,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00b4f8c8"></a> `00b4f8c8` | `c8 00 00 b4` | cbz x8,0x00b4f8e0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f8cc"></a> `00b4f8cc` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f8d0"></a> `00b4f8d0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f8d4"></a> `00b4f8d4` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f8d8"></a> `00b4f8d8` | `02 00 00 14` | b 0x00b4f8e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f8dc"></a> `00b4f8dc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f8e0"></a> `00b4f8e0` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f8e4"></a> `00b4f8e4` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f8e8"></a> `00b4f8e8` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f8ec"></a> `00b4f8ec` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f8f0"></a> `00b4f8f0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f8f4"></a> `00b4f8f4` | `16 21 01 91` | add x22,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00b4f8f8"></a> `00b4f8f8` | `e6 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f8fc"></a> `00b4f8fc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f900"></a> `00b4f900` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f904"></a> `00b4f904` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f908"></a> `00b4f908` | `0a 3a 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f90c"></a> `00b4f90c` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f910"></a> `00b4f910` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f914"></a> `00b4f914` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f918"></a> `00b4f918` | `3f 35 00 71` | cmp w9,#0xd | `FALL_THROUGH`
<a id="insn-00b4f91c"></a> `00b4f91c` | `e3 00 00 54` | b.cc 0x00b4f938 | `CONDITIONAL_JUMP`
<a id="insn-00b4f920"></a> `00b4f920` | `08 19 40 79` | ldrh w8,[x8, #0xc] | `FALL_THROUGH`
<a id="insn-00b4f924"></a> `00b4f924` | `c8 00 00 b4` | cbz x8,0x00b4f93c | `CONDITIONAL_JUMP`
<a id="insn-00b4f928"></a> `00b4f928` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f92c"></a> `00b4f92c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f930"></a> `00b4f930` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f934"></a> `00b4f934` | `02 00 00 14` | b 0x00b4f93c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f938"></a> `00b4f938` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f93c"></a> `00b4f93c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f940"></a> `00b4f940` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f944"></a> `00b4f944` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f948"></a> `00b4f948` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f94c"></a> `00b4f94c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f950"></a> `00b4f950` | `16 81 01 91` | add x22,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00b4f954"></a> `00b4f954` | `cf 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f958"></a> `00b4f958` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f95c"></a> `00b4f95c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f960"></a> `00b4f960` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f964"></a> `00b4f964` | `f3 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f968"></a> `00b4f968` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f96c"></a> `00b4f96c` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f970"></a> `00b4f970` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f974"></a> `00b4f974` | `3f 3d 00 71` | cmp w9,#0xf | `FALL_THROUGH`
<a id="insn-00b4f978"></a> `00b4f978` | `e3 00 00 54` | b.cc 0x00b4f994 | `CONDITIONAL_JUMP`
<a id="insn-00b4f97c"></a> `00b4f97c` | `08 1d 40 79` | ldrh w8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00b4f980"></a> `00b4f980` | `c8 00 00 b4` | cbz x8,0x00b4f998 | `CONDITIONAL_JUMP`
<a id="insn-00b4f984"></a> `00b4f984` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f988"></a> `00b4f988` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f98c"></a> `00b4f98c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f990"></a> `00b4f990` | `02 00 00 14` | b 0x00b4f998 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f994"></a> `00b4f994` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f998"></a> `00b4f998` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f99c"></a> `00b4f99c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f9a0"></a> `00b4f9a0` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4f9a4"></a> `00b4f9a4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4f9a8"></a> `00b4f9a8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4f9ac"></a> `00b4f9ac` | `16 e1 01 91` | add x22,x8,#0x78 | `FALL_THROUGH`
<a id="insn-00b4f9b0"></a> `00b4f9b0` | `b8 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f9b4"></a> `00b4f9b4` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4f9b8"></a> `00b4f9b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4f9bc"></a> `00b4f9bc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4f9c0"></a> `00b4f9c0` | `dc 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f9c4"></a> `00b4f9c4` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4f9c8"></a> `00b4f9c8` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f9cc"></a> `00b4f9cc` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f9d0"></a> `00b4f9d0` | `3f 45 00 71` | cmp w9,#0x11 | `FALL_THROUGH`
<a id="insn-00b4f9d4"></a> `00b4f9d4` | `e3 00 00 54` | b.cc 0x00b4f9f0 | `CONDITIONAL_JUMP`
<a id="insn-00b4f9d8"></a> `00b4f9d8` | `08 21 40 79` | ldrh w8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f9dc"></a> `00b4f9dc` | `c8 00 00 b4` | cbz x8,0x00b4f9f4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f9e0"></a> `00b4f9e0` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4f9e4"></a> `00b4f9e4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f9e8"></a> `00b4f9e8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f9ec"></a> `00b4f9ec` | `02 00 00 14` | b 0x00b4f9f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f9f0"></a> `00b4f9f0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f9f4"></a> `00b4f9f4` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f9f8"></a> `00b4f9f8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f9fc"></a> `00b4f9fc` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4fa00"></a> `00b4fa00` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fa04"></a> `00b4fa04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fa08"></a> `00b4fa08` | `16 41 02 91` | add x22,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00b4fa0c"></a> `00b4fa0c` | `a1 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fa10"></a> `00b4fa10` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fa14"></a> `00b4fa14` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4fa18"></a> `00b4fa18` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4fa1c"></a> `00b4fa1c` | `c5 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fa20"></a> `00b4fa20` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fa24"></a> `00b4fa24` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fa28"></a> `00b4fa28` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fa2c"></a> `00b4fa2c` | `3f 4d 00 71` | cmp w9,#0x13 | `FALL_THROUGH`
<a id="insn-00b4fa30"></a> `00b4fa30` | `e3 00 00 54` | b.cc 0x00b4fa4c | `CONDITIONAL_JUMP`
<a id="insn-00b4fa34"></a> `00b4fa34` | `08 25 40 79` | ldrh w8,[x8, #0x12] | `FALL_THROUGH`
<a id="insn-00b4fa38"></a> `00b4fa38` | `c8 00 00 b4` | cbz x8,0x00b4fa50 | `CONDITIONAL_JUMP`
<a id="insn-00b4fa3c"></a> `00b4fa3c` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fa40"></a> `00b4fa40` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fa44"></a> `00b4fa44` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fa48"></a> `00b4fa48` | `02 00 00 14` | b 0x00b4fa50 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fa4c"></a> `00b4fa4c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4fa50"></a> `00b4fa50` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fa54"></a> `00b4fa54` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4fa58"></a> `00b4fa58` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4fa5c"></a> `00b4fa5c` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fa60"></a> `00b4fa60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fa64"></a> `00b4fa64` | `16 a1 02 91` | add x22,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00b4fa68"></a> `00b4fa68` | `8a 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fa6c"></a> `00b4fa6c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fa70"></a> `00b4fa70` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4fa74"></a> `00b4fa74` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4fa78"></a> `00b4fa78` | `ae 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fa7c"></a> `00b4fa7c` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fa80"></a> `00b4fa80` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fa84"></a> `00b4fa84` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fa88"></a> `00b4fa88` | `3f 55 00 71` | cmp w9,#0x15 | `FALL_THROUGH`
<a id="insn-00b4fa8c"></a> `00b4fa8c` | `e3 00 00 54` | b.cc 0x00b4faa8 | `CONDITIONAL_JUMP`
<a id="insn-00b4fa90"></a> `00b4fa90` | `08 29 40 79` | ldrh w8,[x8, #0x14] | `FALL_THROUGH`
<a id="insn-00b4fa94"></a> `00b4fa94` | `c8 00 00 b4` | cbz x8,0x00b4faac | `CONDITIONAL_JUMP`
<a id="insn-00b4fa98"></a> `00b4fa98` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fa9c"></a> `00b4fa9c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4faa0"></a> `00b4faa0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4faa4"></a> `00b4faa4` | `02 00 00 14` | b 0x00b4faac | `UNCONDITIONAL_JUMP`
<a id="insn-00b4faa8"></a> `00b4faa8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4faac"></a> `00b4faac` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fab0"></a> `00b4fab0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4fab4"></a> `00b4fab4` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4fab8"></a> `00b4fab8` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fabc"></a> `00b4fabc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fac0"></a> `00b4fac0` | `16 01 03 91` | add x22,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-00b4fac4"></a> `00b4fac4` | `73 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fac8"></a> `00b4fac8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4facc"></a> `00b4facc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4fad0"></a> `00b4fad0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4fad4"></a> `00b4fad4` | `97 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fad8"></a> `00b4fad8` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fadc"></a> `00b4fadc` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fae0"></a> `00b4fae0` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fae4"></a> `00b4fae4` | `3f 5d 00 71` | cmp w9,#0x17 | `FALL_THROUGH`
<a id="insn-00b4fae8"></a> `00b4fae8` | `23 08 00 54` | b.cc 0x00b4fbec | `CONDITIONAL_JUMP`
<a id="insn-00b4faec"></a> `00b4faec` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00b4faf0"></a> `00b4faf0` | `e8 07 00 b4` | cbz x8,0x00b4fbec | `CONDITIONAL_JUMP`
<a id="insn-00b4faf4"></a> `00b4faf4` | `ea 02 08 8b` | add x10,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4faf8"></a> `00b4faf8` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00b4fafc"></a> `00b4fafc` | `e9 a3 52 a9` | ldp x9,x8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00b4fb00"></a> `00b4fb00` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fb04"></a> `00b4fb04` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fb08"></a> `00b4fb08` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b4fb0c"></a> `00b4fb0c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b4fb10"></a> `00b4fb10` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00b4fb14"></a> `00b4fb14` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b4fb18"></a> `00b4fb18` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00b4fb1c"></a> `00b4fb1c` | `c2 00 00 54` | b.cs 0x00b4fb34 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb20"></a> `00b4fb20` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fb24"></a> `00b4fb24` | `00 61 03 91` | add x0,x8,#0xd8 | `FALL_THROUGH`
<a id="insn-00b4fb28"></a> `00b4fb28` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00b4fb2c"></a> `00b4fb2c` | `51 42 02 94` | bl 0x00be0470 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fb30"></a> `00b4fb30` | `12 00 00 14` | b 0x00b4fb78 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fb34"></a> `00b4fb34` | `29 02 00 54` | b.ls 0x00b4fb78 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb38"></a> `00b4fb38` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00b4fb3c"></a> `00b4fb3c` | `75 26 0a 9b` | madd x21,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00b4fb40"></a> `00b4fb40` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b4fb44"></a> `00b4fb44` | `80 01 00 54` | b.eq 0x00b4fb74 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb48"></a> `00b4fb48` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b4fb4c"></a> `00b4fb4c` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b4fb50"></a> `00b4fb50` | `c9 00 00 37` | tbnz w9,#0x0,0x00b4fb68 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb54"></a> `00b4fb54` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00b4fb58"></a> `00b4fb58` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b4fb5c"></a> `00b4fb5c` | `c0 00 00 54` | b.eq 0x00b4fb74 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb60"></a> `00b4fb60` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b4fb64"></a> `00b4fb64` | `89 ff 07 36` | tbz w9,#0x0,0x00b4fb54 | `CONDITIONAL_JUMP`
<a id="insn-00b4fb68"></a> `00b4fb68` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b4fb6c"></a> `00b4fb6c` | `fd 2c 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fb70"></a> `00b4fb70` | `f9 ff ff 17` | b 0x00b4fb54 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fb74"></a> `00b4fb74` | `f5 9b 00 f9` | str x21,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b4fb78"></a> `00b4fb78` | `b3 03 00 34` | cbz w19,0x00b4fbec | `CONDITIONAL_JUMP`
<a id="insn-00b4fb7c"></a> `00b4fb7c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00b4fb80"></a> `00b4fb80` | `69 06 13 8b` | add x9,x19,x19, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00b4fb84"></a> `00b4fb84` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00b4fb88"></a> `00b4fb88` | `3c f1 7d d3` | lsl x28,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00b4fb8c"></a> `00b4fb8c` | `08 01 18 8b` | add x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b4fb90"></a> `00b4fb90` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00b4fb94"></a> `00b4fb94` | `13 11 00 91` | add x19,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fb98"></a> `00b4fb98` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fb9c"></a> `00b4fb9c` | `ea 97 40 f9` | ldr x10,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00b4fba0"></a> `00b4fba0` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fba4"></a> `00b4fba4` | `08 2d 40 79` | ldrh w8,[x8, #0x16] | `FALL_THROUGH`
<a id="insn-00b4fba8"></a> `00b4fba8` | `56 01 1a 8b` | add x22,x10,x26 | `FALL_THROUGH`
<a id="insn-00b4fbac"></a> `00b4fbac` | `e9 6a 68 b8` | ldr w9,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fbb0"></a> `00b4fbb0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fbb4"></a> `00b4fbb4` | `69 6a 68 b8` | ldr w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fbb8"></a> `00b4fbb8` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fbbc"></a> `00b4fbbc` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b4fbc0"></a> `00b4fbc0` | `15 11 00 91` | add x21,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fbc4"></a> `00b4fbc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fbc8"></a> `00b4fbc8` | `32 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fbcc"></a> `00b4fbcc` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fbd0"></a> `00b4fbd0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4fbd4"></a> `00b4fbd4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4fbd8"></a> `00b4fbd8` | `56 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fbdc"></a> `00b4fbdc` | `5a 63 00 91` | add x26,x26,#0x18 | `FALL_THROUGH`
<a id="insn-00b4fbe0"></a> `00b4fbe0` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00b4fbe4"></a> `00b4fbe4` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fbe8"></a> `00b4fbe8` | `81 fd ff 54` | b.ne 0x00b4fb98 | `CONDITIONAL_JUMP`
<a id="insn-00b4fbec"></a> `00b4fbec` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fbf0"></a> `00b4fbf0` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fbf4"></a> `00b4fbf4` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fbf8"></a> `00b4fbf8` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-00b4fbfc"></a> `00b4fbfc` | `e3 00 00 54` | b.cc 0x00b4fc18 | `CONDITIONAL_JUMP`
<a id="insn-00b4fc00"></a> `00b4fc00` | `08 31 40 79` | ldrh w8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b4fc04"></a> `00b4fc04` | `c8 00 00 b4` | cbz x8,0x00b4fc1c | `CONDITIONAL_JUMP`
<a id="insn-00b4fc08"></a> `00b4fc08` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fc0c"></a> `00b4fc0c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fc10"></a> `00b4fc10` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fc14"></a> `00b4fc14` | `02 00 00 14` | b 0x00b4fc1c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fc18"></a> `00b4fc18` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4fc1c"></a> `00b4fc1c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fc20"></a> `00b4fc20` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4fc24"></a> `00b4fc24` | `75 03 89 9a` | csel x21,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4fc28"></a> `00b4fc28` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fc2c"></a> `00b4fc2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fc30"></a> `00b4fc30` | `16 c1 03 91` | add x22,x8,#0xf0 | `FALL_THROUGH`
<a id="insn-00b4fc34"></a> `00b4fc34` | `17 2d 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fc38"></a> `00b4fc38` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fc3c"></a> `00b4fc3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4fc40"></a> `00b4fc40` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4fc44"></a> `00b4fc44` | `3b 39 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fc48"></a> `00b4fc48` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fc4c"></a> `00b4fc4c` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fc50"></a> `00b4fc50` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fc54"></a> `00b4fc54` | `3f 6d 00 71` | cmp w9,#0x1b | `FALL_THROUGH`
<a id="insn-00b4fc58"></a> `00b4fc58` | `23 08 00 54` | b.cc 0x00b4fd5c | `CONDITIONAL_JUMP`
<a id="insn-00b4fc5c"></a> `00b4fc5c` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00b4fc60"></a> `00b4fc60` | `e8 07 00 b4` | cbz x8,0x00b4fd5c | `CONDITIONAL_JUMP`
<a id="insn-00b4fc64"></a> `00b4fc64` | `ea 02 08 8b` | add x10,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fc68"></a> `00b4fc68` | `4b 01 40 b9` | ldr w11,[x10] | `FALL_THROUGH`
<a id="insn-00b4fc6c"></a> `00b4fc6c` | `e9 a3 55 a9` | ldp x9,x8,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00b4fc70"></a> `00b4fc70` | `53 69 6b b8` | ldr w19,[x10, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fc74"></a> `00b4fc74` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fc78"></a> `00b4fc78` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b4fc7c"></a> `00b4fc7c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b4fc80"></a> `00b4fc80` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00b4fc84"></a> `00b4fc84` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b4fc88"></a> `00b4fc88` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00b4fc8c"></a> `00b4fc8c` | `c2 00 00 54` | b.cs 0x00b4fca4 | `CONDITIONAL_JUMP`
<a id="insn-00b4fc90"></a> `00b4fc90` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fc94"></a> `00b4fc94` | `00 21 04 91` | add x0,x8,#0x108 | `FALL_THROUGH`
<a id="insn-00b4fc98"></a> `00b4fc98` | `61 02 0a cb` | sub x1,x19,x10 | `FALL_THROUGH`
<a id="insn-00b4fc9c"></a> `00b4fc9c` | `f5 41 02 94` | bl 0x00be0470 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fca0"></a> `00b4fca0` | `12 00 00 14` | b 0x00b4fce8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fca4"></a> `00b4fca4` | `29 02 00 54` | b.ls 0x00b4fce8 | `CONDITIONAL_JUMP`
<a id="insn-00b4fca8"></a> `00b4fca8` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00b4fcac"></a> `00b4fcac` | `75 26 0a 9b` | madd x21,x19,x10,x9 | `FALL_THROUGH`
<a id="insn-00b4fcb0"></a> `00b4fcb0` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b4fcb4"></a> `00b4fcb4` | `80 01 00 54` | b.eq 0x00b4fce4 | `CONDITIONAL_JUMP`
<a id="insn-00b4fcb8"></a> `00b4fcb8` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b4fcbc"></a> `00b4fcbc` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b4fcc0"></a> `00b4fcc0` | `c9 00 00 37` | tbnz w9,#0x0,0x00b4fcd8 | `CONDITIONAL_JUMP`
<a id="insn-00b4fcc4"></a> `00b4fcc4` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00b4fcc8"></a> `00b4fcc8` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b4fccc"></a> `00b4fccc` | `c0 00 00 54` | b.eq 0x00b4fce4 | `CONDITIONAL_JUMP`
<a id="insn-00b4fcd0"></a> `00b4fcd0` | `c9 8e 5e 38` | ldrb w9,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b4fcd4"></a> `00b4fcd4` | `89 ff 07 36` | tbz w9,#0x0,0x00b4fcc4 | `CONDITIONAL_JUMP`
<a id="insn-00b4fcd8"></a> `00b4fcd8` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b4fcdc"></a> `00b4fcdc` | `a1 2c 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fce0"></a> `00b4fce0` | `f9 ff ff 17` | b 0x00b4fcc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fce4"></a> `00b4fce4` | `f5 b3 00 f9` | str x21,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00b4fce8"></a> `00b4fce8` | `b3 03 00 34` | cbz w19,0x00b4fd5c | `CONDITIONAL_JUMP`
<a id="insn-00b4fcec"></a> `00b4fcec` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00b4fcf0"></a> `00b4fcf0` | `69 06 13 8b` | add x9,x19,x19, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00b4fcf4"></a> `00b4fcf4` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00b4fcf8"></a> `00b4fcf8` | `08 01 18 8b` | add x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b4fcfc"></a> `00b4fcfc` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00b4fd00"></a> `00b4fd00` | `13 11 00 91` | add x19,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fd04"></a> `00b4fd04` | `38 f1 7d d3` | lsl x24,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00b4fd08"></a> `00b4fd08` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fd0c"></a> `00b4fd0c` | `ea af 40 f9` | ldr x10,[sp, #0x158] | `FALL_THROUGH`
<a id="insn-00b4fd10"></a> `00b4fd10` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fd14"></a> `00b4fd14` | `08 35 40 79` | ldrh w8,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00b4fd18"></a> `00b4fd18` | `55 01 16 8b` | add x21,x10,x22 | `FALL_THROUGH`
<a id="insn-00b4fd1c"></a> `00b4fd1c` | `e9 6a 68 b8` | ldr w9,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fd20"></a> `00b4fd20` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fd24"></a> `00b4fd24` | `69 6a 68 b8` | ldr w9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b4fd28"></a> `00b4fd28` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fd2c"></a> `00b4fd2c` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b4fd30"></a> `00b4fd30` | `14 11 00 91` | add x20,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fd34"></a> `00b4fd34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4fd38"></a> `00b4fd38` | `d6 2c 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fd3c"></a> `00b4fd3c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fd40"></a> `00b4fd40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b4fd44"></a> `00b4fd44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b4fd48"></a> `00b4fd48` | `fa 38 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fd4c"></a> `00b4fd4c` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00b4fd50"></a> `00b4fd50` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00b4fd54"></a> `00b4fd54` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fd58"></a> `00b4fd58` | `81 fd ff 54` | b.ne 0x00b4fd08 | `CONDITIONAL_JUMP`
<a id="insn-00b4fd5c"></a> `00b4fd5c` | `e8 02 80 b9` | ldrsw x8,[x23] | `FALL_THROUGH`
<a id="insn-00b4fd60"></a> `00b4fd60` | `e8 02 08 cb` | sub x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fd64"></a> `00b4fd64` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fd68"></a> `00b4fd68` | `3f 75 00 71` | cmp w9,#0x1d | `FALL_THROUGH`
<a id="insn-00b4fd6c"></a> `00b4fd6c` | `e3 00 00 54` | b.cc 0x00b4fd88 | `CONDITIONAL_JUMP`
<a id="insn-00b4fd70"></a> `00b4fd70` | `08 39 40 79` | ldrh w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00b4fd74"></a> `00b4fd74` | `c8 00 00 b4` | cbz x8,0x00b4fd8c | `CONDITIONAL_JUMP`
<a id="insn-00b4fd78"></a> `00b4fd78` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00b4fd7c"></a> `00b4fd7c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4fd80"></a> `00b4fd80` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fd84"></a> `00b4fd84` | `02 00 00 14` | b 0x00b4fd8c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4fd88"></a> `00b4fd88` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4fd8c"></a> `00b4fd8c` | `09 11 00 91` | add x9,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4fd90"></a> `00b4fd90` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4fd94"></a> `00b4fd94` | `74 03 89 9a` | csel x20,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b4fd98"></a> `00b4fd98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4fd9c"></a> `00b4fd9c` | `bd 2c 02 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fda0"></a> `00b4fda0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00b4fda4"></a> `00b4fda4` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00b4fda8"></a> `00b4fda8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b4fdac"></a> `00b4fdac` | `f3 e3 00 91` | add x19,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00b4fdb0"></a> `00b4fdb0` | `e0 38 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fdb4"></a> `00b4fdb4` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fdb8"></a> `00b4fdb8` | `f3 bb 00 f9` | str x19,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00b4fdbc"></a> `00b4fdbc` | `e8 3f 01 f9` | str x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00b4fdc0"></a> `00b4fdc0` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b4fdc4"></a> `00b4fdc4` | `28 05 40 a9` | ldp x8,x1,[x9] | `FALL_THROUGH`
<a id="insn-00b4fdc8"></a> `00b4fdc8` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4fdcc"></a> `00b4fdcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4fdd0"></a> `00b4fdd0` | `e8 3f 41 f9` | ldr x8,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00b4fdd4"></a> `00b4fdd4` | `68 00 00 b4` | cbz x8,0x00b4fde0 | `CONDITIONAL_JUMP`
<a id="insn-00b4fdd8"></a> `00b4fdd8` | `1f 91 00 f9` | str xzr,[x8, #0x120] | `FALL_THROUGH`
<a id="insn-00b4fddc"></a> `00b4fddc` | `ff 3f 01 f9` | str xzr,[sp, #0x278] | `FALL_THROUGH`
<a id="insn-00b4fde0"></a> `00b4fde0` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b4fde4"></a> `00b4fde4` | `68 00 00 36` | tbz w8,#0x0,0x00b4fdf0 | `CONDITIONAL_JUMP`
<a id="insn-00b4fde8"></a> `00b4fde8` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b4fdec"></a> `00b4fdec` | `5d 2c 02 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fdf0"></a> `00b4fdf0` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b4fdf4"></a> `00b4fdf4` | `1b 41 02 94` | bl 0x00be0260 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fdf8"></a> `00b4fdf8` | `e0 03 06 91` | add x0,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00b4fdfc"></a> `00b4fdfc` | `49 41 02 94` | bl 0x00be0320 | `UNCONDITIONAL_CALL`
<a id="insn-00b4fe00"></a> `00b4fe00` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00b4fe04"></a> `00b4fe04` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b4fe08"></a> `00b4fe08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b4fe0c"></a> `00b4fe0c` | `21 01 00 54` | b.ne 0x00b4fe30 | `CONDITIONAL_JUMP`
<a id="insn-00b4fe10"></a> `00b4fe10` | `ff 83 0b 91` | add sp,sp,#0x2e0 | `FALL_THROUGH`
<a id="insn-00b4fe14"></a> `00b4fe14` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4fe18"></a> `00b4fe18` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4fe1c"></a> `00b4fe1c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4fe20"></a> `00b4fe20` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4fe24"></a> `00b4fe24` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4fe28"></a> `00b4fe28` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00b4fe2c"></a> `00b4fe2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b4fe30"></a> `00b4fe30` | `58 2c 02 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4efec`](#insn-00b4efec) 範囲 `[['00b4efec', '00b4f00b']]`
  - `FALL_THROUGH` [`00b4f008`](#insn-00b4f008) → [`00b4f00c`](#insn-00b4f00c)
- ブロック [`00b4f00c`](#insn-00b4f00c) 範囲 `[['00b4f00c', '00b4f03b']]`
  - `FALL_THROUGH` [`00b4f038`](#insn-00b4f038) → [`00b4f03c`](#insn-00b4f03c)
- ブロック [`00b4f03c`](#insn-00b4f03c) 範囲 `[['00b4f03c', '00b4f053']]`
  - `FALL_THROUGH` [`00b4f050`](#insn-00b4f050) → [`00b4f054`](#insn-00b4f054)
- ブロック [`00b4f054`](#insn-00b4f054) 範囲 `[['00b4f054', '00b4f077']]`
  - `FALL_THROUGH` [`00b4f074`](#insn-00b4f074) → [`00b4f078`](#insn-00b4f078)
- ブロック [`00b4f078`](#insn-00b4f078) 範囲 `[['00b4f078', '00b4f09f']]`
  - `FALL_THROUGH` [`00b4f09c`](#insn-00b4f09c) → [`00b4f0a0`](#insn-00b4f0a0)
- ブロック [`00b4f0a0`](#insn-00b4f0a0) 範囲 `[['00b4f0a0', '00b4f0b3']]`
  - `CONDITIONAL_JUMP` [`00b4f0b0`](#insn-00b4f0b0) → [`00b4f0c8`](#insn-00b4f0c8)
  - `FALL_THROUGH` [`00b4f0b0`](#insn-00b4f0b0) → [`00b4f0b4`](#insn-00b4f0b4)
- ブロック [`00b4f0b4`](#insn-00b4f0b4) 範囲 `[['00b4f0b4', '00b4f0bb']]`
  - `CONDITIONAL_JUMP` [`00b4f0b8`](#insn-00b4f0b8) → [`00b4f0c8`](#insn-00b4f0c8)
  - `FALL_THROUGH` [`00b4f0b8`](#insn-00b4f0b8) → [`00b4f0bc`](#insn-00b4f0bc)
- ブロック [`00b4f0bc`](#insn-00b4f0bc) 範囲 `[['00b4f0bc', '00b4f0c3']]`
  - `FALL_THROUGH` [`00b4f0c0`](#insn-00b4f0c0) → [`00b4f0c4`](#insn-00b4f0c4)
- ブロック [`00b4f0c4`](#insn-00b4f0c4) 範囲 `[['00b4f0c4', '00b4f0c7']]`
  - `FALL_THROUGH` [`00b4f0c4`](#insn-00b4f0c4) → [`00b4f0c8`](#insn-00b4f0c8)
- ブロック [`00b4f0c8`](#insn-00b4f0c8) 範囲 `[['00b4f0c8', '00b4f0d3']]`
  - `FALL_THROUGH` [`00b4f0d0`](#insn-00b4f0d0) → [`00b4f0d4`](#insn-00b4f0d4)
- ブロック [`00b4f0d4`](#insn-00b4f0d4) 範囲 `[['00b4f0d4', '00b4f0f3']]`
  - `FALL_THROUGH` [`00b4f0f0`](#insn-00b4f0f0) → [`00b4f0f4`](#insn-00b4f0f4)
- ブロック [`00b4f0f4`](#insn-00b4f0f4) 範囲 `[['00b4f0f4', '00b4f0ff']]`
  - `FALL_THROUGH` [`00b4f0fc`](#insn-00b4f0fc) → [`00b4f100`](#insn-00b4f100)
- ブロック [`00b4f100`](#insn-00b4f100) 範囲 `[['00b4f100', '00b4f107']]`
  - `CONDITIONAL_JUMP` [`00b4f104`](#insn-00b4f104) → [`00b4f120`](#insn-00b4f120)
  - `FALL_THROUGH` [`00b4f104`](#insn-00b4f104) → [`00b4f108`](#insn-00b4f108)
- ブロック [`00b4f108`](#insn-00b4f108) 範囲 `[['00b4f108', '00b4f10b']]`
  - `FALL_THROUGH` [`00b4f108`](#insn-00b4f108) → [`00b4f10c`](#insn-00b4f10c)
- ブロック [`00b4f10c`](#insn-00b4f10c) 範囲 `[['00b4f10c', '00b4f10f']]`
  - `CONDITIONAL_JUMP` [`00b4f10c`](#insn-00b4f10c) → [`00b4f124`](#insn-00b4f124)
  - `FALL_THROUGH` [`00b4f10c`](#insn-00b4f10c) → [`00b4f110`](#insn-00b4f110)
- ブロック [`00b4f110`](#insn-00b4f110) 範囲 `[['00b4f110', '00b4f11f']]`
  - `UNCONDITIONAL_JUMP` [`00b4f11c`](#insn-00b4f11c) → [`00b4f124`](#insn-00b4f124)
- ブロック [`00b4f120`](#insn-00b4f120) 範囲 `[['00b4f120', '00b4f123']]`
  - `FALL_THROUGH` [`00b4f120`](#insn-00b4f120) → [`00b4f124`](#insn-00b4f124)
- ブロック [`00b4f124`](#insn-00b4f124) 範囲 `[['00b4f124', '00b4f137']]`
  - `FALL_THROUGH` [`00b4f134`](#insn-00b4f134) → [`00b4f138`](#insn-00b4f138)
- ブロック [`00b4f138`](#insn-00b4f138) 範囲 `[['00b4f138', '00b4f153']]`
  - `FALL_THROUGH` [`00b4f150`](#insn-00b4f150) → [`00b4f154`](#insn-00b4f154)
- ブロック [`00b4f154`](#insn-00b4f154) 範囲 `[['00b4f154', '00b4f167']]`
  - `CONDITIONAL_JUMP` [`00b4f164`](#insn-00b4f164) → [`00b4f35c`](#insn-00b4f35c)
  - `FALL_THROUGH` [`00b4f164`](#insn-00b4f164) → [`00b4f168`](#insn-00b4f168)
- ブロック [`00b4f168`](#insn-00b4f168) 範囲 `[['00b4f168', '00b4f16f']]`
  - `CONDITIONAL_JUMP` [`00b4f16c`](#insn-00b4f16c) → [`00b4f35c`](#insn-00b4f35c)
  - `FALL_THROUGH` [`00b4f16c`](#insn-00b4f16c) → [`00b4f170`](#insn-00b4f170)
- ブロック [`00b4f170`](#insn-00b4f170) 範囲 `[['00b4f170', '00b4f173']]`
  - `FALL_THROUGH` [`00b4f170`](#insn-00b4f170) → [`00b4f174`](#insn-00b4f174)
- ブロック [`00b4f174`](#insn-00b4f174) 範囲 `[['00b4f174', '00b4f17f']]`
  - `CONDITIONAL_JUMP` [`00b4f17c`](#insn-00b4f17c) → [`00b4f35c`](#insn-00b4f35c)
  - `FALL_THROUGH` [`00b4f17c`](#insn-00b4f17c) → [`00b4f180`](#insn-00b4f180)
- ブロック [`00b4f180`](#insn-00b4f180) 範囲 `[['00b4f180', '00b4f187']]`
  - `CONDITIONAL_JUMP` [`00b4f184`](#insn-00b4f184) → [`00b4f35c`](#insn-00b4f35c)
  - `FALL_THROUGH` [`00b4f184`](#insn-00b4f184) → [`00b4f188`](#insn-00b4f188)
- ブロック [`00b4f188`](#insn-00b4f188) 範囲 `[['00b4f188', '00b4f19f']]`
  - `UNCONDITIONAL_JUMP` [`00b4f19c`](#insn-00b4f19c) → [`00b4f1b0`](#insn-00b4f1b0)
- ブロック [`00b4f1a0`](#insn-00b4f1a0) 範囲 `[['00b4f1a0', '00b4f1af']]`
  - `CONDITIONAL_JUMP` [`00b4f1ac`](#insn-00b4f1ac) → [`00b4f350`](#insn-00b4f350)
  - `FALL_THROUGH` [`00b4f1ac`](#insn-00b4f1ac) → [`00b4f1b0`](#insn-00b4f1b0)
- ブロック [`00b4f1b0`](#insn-00b4f1b0) 範囲 `[['00b4f1b0', '00b4f1bf']]`
  - `FALL_THROUGH` [`00b4f1bc`](#insn-00b4f1bc) → [`00b4f1c0`](#insn-00b4f1c0)
- ブロック [`00b4f1c0`](#insn-00b4f1c0) 範囲 `[['00b4f1c0', '00b4f1f3']]`
  - `CONDITIONAL_JUMP` [`00b4f1f0`](#insn-00b4f1f0) → [`00b4f278`](#insn-00b4f278)
  - `FALL_THROUGH` [`00b4f1f0`](#insn-00b4f1f0) → [`00b4f1f4`](#insn-00b4f1f4)
- ブロック [`00b4f1f4`](#insn-00b4f1f4) 範囲 `[['00b4f1f4', '00b4f1fb']]`
  - `CONDITIONAL_JUMP` [`00b4f1f8`](#insn-00b4f1f8) → [`00b4f224`](#insn-00b4f224)
  - `FALL_THROUGH` [`00b4f1f8`](#insn-00b4f1f8) → [`00b4f1fc`](#insn-00b4f1fc)
- ブロック [`00b4f1fc`](#insn-00b4f1fc) 範囲 `[['00b4f1fc', '00b4f1ff']]`
  - `FALL_THROUGH` [`00b4f1fc`](#insn-00b4f1fc) → [`00b4f200`](#insn-00b4f200)
- ブロック [`00b4f200`](#insn-00b4f200) 範囲 `[['00b4f200', '00b4f203']]`
  - `FALL_THROUGH` [`00b4f200`](#insn-00b4f200) → [`00b4f204`](#insn-00b4f204)
- ブロック [`00b4f204`](#insn-00b4f204) 範囲 `[['00b4f204', '00b4f207']]`
  - `FALL_THROUGH` [`00b4f204`](#insn-00b4f204) → [`00b4f208`](#insn-00b4f208)
- ブロック [`00b4f208`](#insn-00b4f208) 範囲 `[['00b4f208', '00b4f21b']]`
  - `FALL_THROUGH` [`00b4f218`](#insn-00b4f218) → [`00b4f21c`](#insn-00b4f21c)
- ブロック [`00b4f21c`](#insn-00b4f21c) 範囲 `[['00b4f21c', '00b4f223']]`
  - `FALL_THROUGH` [`00b4f220`](#insn-00b4f220) → [`00b4f224`](#insn-00b4f224)
- ブロック [`00b4f224`](#insn-00b4f224) 範囲 `[['00b4f224', '00b4f227']]`
  - `FALL_THROUGH` [`00b4f224`](#insn-00b4f224) → [`00b4f228`](#insn-00b4f228)
- ブロック [`00b4f228`](#insn-00b4f228) 範囲 `[['00b4f228', '00b4f233']]`
  - `FALL_THROUGH` [`00b4f230`](#insn-00b4f230) → [`00b4f234`](#insn-00b4f234)
- ブロック [`00b4f234`](#insn-00b4f234) 範囲 `[['00b4f234', '00b4f237']]`
  - `CONDITIONAL_JUMP` [`00b4f234`](#insn-00b4f234) → [`00b4f284`](#insn-00b4f284)
  - `FALL_THROUGH` [`00b4f234`](#insn-00b4f234) → [`00b4f238`](#insn-00b4f238)
- ブロック [`00b4f238`](#insn-00b4f238) 範囲 `[['00b4f238', '00b4f24b']]`
  - `FALL_THROUGH` [`00b4f248`](#insn-00b4f248) → [`00b4f24c`](#insn-00b4f24c)
- ブロック [`00b4f24c`](#insn-00b4f24c) 範囲 `[['00b4f24c', '00b4f253']]`
  - `CONDITIONAL_JUMP` [`00b4f250`](#insn-00b4f250) → [`00b4f284`](#insn-00b4f284)
  - `FALL_THROUGH` [`00b4f250`](#insn-00b4f250) → [`00b4f254`](#insn-00b4f254)
- ブロック [`00b4f254`](#insn-00b4f254) 範囲 `[['00b4f254', '00b4f263']]`
  - `FALL_THROUGH` [`00b4f260`](#insn-00b4f260) → [`00b4f264`](#insn-00b4f264)
- ブロック [`00b4f264`](#insn-00b4f264) 範囲 `[['00b4f264', '00b4f277']]`
  - `UNCONDITIONAL_JUMP` [`00b4f274`](#insn-00b4f274) → [`00b4f288`](#insn-00b4f288)
- ブロック [`00b4f278`](#insn-00b4f278) 範囲 `[['00b4f278', '00b4f27b']]`
  - `FALL_THROUGH` [`00b4f278`](#insn-00b4f278) → [`00b4f27c`](#insn-00b4f27c)
- ブロック [`00b4f27c`](#insn-00b4f27c) 範囲 `[['00b4f27c', '00b4f27f']]`
  - `FALL_THROUGH` [`00b4f27c`](#insn-00b4f27c) → [`00b4f280`](#insn-00b4f280)
- ブロック [`00b4f280`](#insn-00b4f280) 範囲 `[['00b4f280', '00b4f283']]`
  - `UNCONDITIONAL_JUMP` [`00b4f280`](#insn-00b4f280) → [`00b4f288`](#insn-00b4f288)
- ブロック [`00b4f284`](#insn-00b4f284) 範囲 `[['00b4f284', '00b4f287']]`
  - `FALL_THROUGH` [`00b4f284`](#insn-00b4f284) → [`00b4f288`](#insn-00b4f288)
- ブロック [`00b4f288`](#insn-00b4f288) 範囲 `[['00b4f288', '00b4f28b']]`
  - `FALL_THROUGH` [`00b4f288`](#insn-00b4f288) → [`00b4f28c`](#insn-00b4f28c)
- ブロック [`00b4f28c`](#insn-00b4f28c) 範囲 `[['00b4f28c', '00b4f2b7']]`
  - `CONDITIONAL_JUMP` [`00b4f2b4`](#insn-00b4f2b4) → [`00b4f320`](#insn-00b4f320)
  - `FALL_THROUGH` [`00b4f2b4`](#insn-00b4f2b4) → [`00b4f2b8`](#insn-00b4f2b8)
- ブロック [`00b4f2b8`](#insn-00b4f2b8) 範囲 `[['00b4f2b8', '00b4f2d7']]`
  - `FALL_THROUGH` [`00b4f2d4`](#insn-00b4f2d4) → [`00b4f2d8`](#insn-00b4f2d8)
- ブロック [`00b4f2d8`](#insn-00b4f2d8) 範囲 `[['00b4f2d8', '00b4f2e7']]`
  - `FALL_THROUGH` [`00b4f2e4`](#insn-00b4f2e4) → [`00b4f2e8`](#insn-00b4f2e8)
- ブロック [`00b4f2e8`](#insn-00b4f2e8) 範囲 `[['00b4f2e8', '00b4f2ef']]`
  - `FALL_THROUGH` [`00b4f2ec`](#insn-00b4f2ec) → [`00b4f2f0`](#insn-00b4f2f0)
- ブロック [`00b4f2f0`](#insn-00b4f2f0) 範囲 `[['00b4f2f0', '00b4f2f3']]`
  - `FALL_THROUGH` [`00b4f2f0`](#insn-00b4f2f0) → [`00b4f2f4`](#insn-00b4f2f4)
- ブロック [`00b4f2f4`](#insn-00b4f2f4) 範囲 `[['00b4f2f4', '00b4f2f7']]`
  - `FALL_THROUGH` [`00b4f2f4`](#insn-00b4f2f4) → [`00b4f2f8`](#insn-00b4f2f8)
- ブロック [`00b4f2f8`](#insn-00b4f2f8) 範囲 `[['00b4f2f8', '00b4f2fb']]`
  - `CONDITIONAL_JUMP` [`00b4f2f8`](#insn-00b4f2f8) → [`00b4f308`](#insn-00b4f308)
  - `FALL_THROUGH` [`00b4f2f8`](#insn-00b4f2f8) → [`00b4f2fc`](#insn-00b4f2fc)
- ブロック [`00b4f2fc`](#insn-00b4f2fc) 範囲 `[['00b4f2fc', '00b4f2ff']]`
  - `FALL_THROUGH` [`00b4f2fc`](#insn-00b4f2fc) → [`00b4f300`](#insn-00b4f300)
- ブロック [`00b4f300`](#insn-00b4f300) 範囲 `[['00b4f300', '00b4f303']]`
  - `FALL_THROUGH` [`00b4f300`](#insn-00b4f300) → [`00b4f304`](#insn-00b4f304)
- ブロック [`00b4f304`](#insn-00b4f304) 範囲 `[['00b4f304', '00b4f307']]`
  - `UNCONDITIONAL_JUMP` [`00b4f304`](#insn-00b4f304) → [`00b4f30c`](#insn-00b4f30c)
- ブロック [`00b4f308`](#insn-00b4f308) 範囲 `[['00b4f308', '00b4f30b']]`
  - `FALL_THROUGH` [`00b4f308`](#insn-00b4f308) → [`00b4f30c`](#insn-00b4f30c)
- ブロック [`00b4f30c`](#insn-00b4f30c) 範囲 `[['00b4f30c', '00b4f31b']]`
  - `FALL_THROUGH` [`00b4f318`](#insn-00b4f318) → [`00b4f31c`](#insn-00b4f31c)
- ブロック [`00b4f31c`](#insn-00b4f31c) 範囲 `[['00b4f31c', '00b4f31f']]`
  - `FALL_THROUGH` [`00b4f31c`](#insn-00b4f31c) → [`00b4f320`](#insn-00b4f320)
- ブロック [`00b4f320`](#insn-00b4f320) 範囲 `[['00b4f320', '00b4f323']]`
  - `FALL_THROUGH` [`00b4f320`](#insn-00b4f320) → [`00b4f324`](#insn-00b4f324)
- ブロック [`00b4f324`](#insn-00b4f324) 範囲 `[['00b4f324', '00b4f327']]`
  - `FALL_THROUGH` [`00b4f324`](#insn-00b4f324) → [`00b4f328`](#insn-00b4f328)
- ブロック [`00b4f328`](#insn-00b4f328) 範囲 `[['00b4f328', '00b4f333']]`
  - `FALL_THROUGH` [`00b4f330`](#insn-00b4f330) → [`00b4f334`](#insn-00b4f334)
- ブロック [`00b4f334`](#insn-00b4f334) 範囲 `[['00b4f334', '00b4f343']]`
  - `CONDITIONAL_JUMP` [`00b4f340`](#insn-00b4f340) → [`00b4f1a0`](#insn-00b4f1a0)
  - `FALL_THROUGH` [`00b4f340`](#insn-00b4f340) → [`00b4f344`](#insn-00b4f344)
- ブロック [`00b4f344`](#insn-00b4f344) 範囲 `[['00b4f344', '00b4f347']]`
  - `FALL_THROUGH` [`00b4f344`](#insn-00b4f344) → [`00b4f348`](#insn-00b4f348)
- ブロック [`00b4f348`](#insn-00b4f348) 範囲 `[['00b4f348', '00b4f34f']]`
  - `UNCONDITIONAL_JUMP` [`00b4f34c`](#insn-00b4f34c) → [`00b4f1a0`](#insn-00b4f1a0)
- ブロック [`00b4f350`](#insn-00b4f350) 範囲 `[['00b4f350', '00b4f353']]`
  - `FALL_THROUGH` [`00b4f350`](#insn-00b4f350) → [`00b4f354`](#insn-00b4f354)
- ブロック [`00b4f354`](#insn-00b4f354) 範囲 `[['00b4f354', '00b4f35b']]`
  - `FALL_THROUGH` [`00b4f358`](#insn-00b4f358) → [`00b4f35c`](#insn-00b4f35c)
- ブロック [`00b4f35c`](#insn-00b4f35c) 範囲 `[['00b4f35c', '00b4f35f']]`
  - `FALL_THROUGH` [`00b4f35c`](#insn-00b4f35c) → [`00b4f360`](#insn-00b4f360)
- ブロック [`00b4f360`](#insn-00b4f360) 範囲 `[['00b4f360', '00b4f36b']]`
  - `CONDITIONAL_JUMP` [`00b4f368`](#insn-00b4f368) → [`00b4f430`](#insn-00b4f430)
  - `FALL_THROUGH` [`00b4f368`](#insn-00b4f368) → [`00b4f36c`](#insn-00b4f36c)
- ブロック [`00b4f36c`](#insn-00b4f36c) 範囲 `[['00b4f36c', '00b4f373']]`
  - `CONDITIONAL_JUMP` [`00b4f370`](#insn-00b4f370) → [`00b4f430`](#insn-00b4f430)
  - `FALL_THROUGH` [`00b4f370`](#insn-00b4f370) → [`00b4f374`](#insn-00b4f374)
- ブロック [`00b4f374`](#insn-00b4f374) 範囲 `[['00b4f374', '00b4f383']]`
  - `CONDITIONAL_JUMP` [`00b4f380`](#insn-00b4f380) → [`00b4f430`](#insn-00b4f430)
  - `FALL_THROUGH` [`00b4f380`](#insn-00b4f380) → [`00b4f384`](#insn-00b4f384)
- ブロック [`00b4f384`](#insn-00b4f384) 範囲 `[['00b4f384', '00b4f387']]`
  - `FALL_THROUGH` [`00b4f384`](#insn-00b4f384) → [`00b4f388`](#insn-00b4f388)
- ブロック [`00b4f388`](#insn-00b4f388) 範囲 `[['00b4f388', '00b4f397']]`
  - `FALL_THROUGH` [`00b4f394`](#insn-00b4f394) → [`00b4f398`](#insn-00b4f398)
- ブロック [`00b4f398`](#insn-00b4f398) 範囲 `[['00b4f398', '00b4f39b']]`
  - `CONDITIONAL_JUMP` [`00b4f398`](#insn-00b4f398) → [`00b4f3e0`](#insn-00b4f3e0)
  - `FALL_THROUGH` [`00b4f398`](#insn-00b4f398) → [`00b4f39c`](#insn-00b4f39c)
- ブロック [`00b4f39c`](#insn-00b4f39c) 範囲 `[['00b4f39c', '00b4f3b7']]`
  - `FALL_THROUGH` [`00b4f3b4`](#insn-00b4f3b4) → [`00b4f3b8`](#insn-00b4f3b8)
- ブロック [`00b4f3b8`](#insn-00b4f3b8) 範囲 `[['00b4f3b8', '00b4f3bb']]`
  - `FALL_THROUGH` [`00b4f3b8`](#insn-00b4f3b8) → [`00b4f3bc`](#insn-00b4f3bc)
- ブロック [`00b4f3bc`](#insn-00b4f3bc) 範囲 `[['00b4f3bc', '00b4f3bf']]`
  - `CONDITIONAL_JUMP` [`00b4f3bc`](#insn-00b4f3bc) → [`00b4f3cc`](#insn-00b4f3cc)
  - `FALL_THROUGH` [`00b4f3bc`](#insn-00b4f3bc) → [`00b4f3c0`](#insn-00b4f3c0)
- ブロック [`00b4f3c0`](#insn-00b4f3c0) 範囲 `[['00b4f3c0', '00b4f3cb']]`
  - `FALL_THROUGH` [`00b4f3c8`](#insn-00b4f3c8) → [`00b4f3cc`](#insn-00b4f3cc)
- ブロック [`00b4f3cc`](#insn-00b4f3cc) 範囲 `[['00b4f3cc', '00b4f3d7']]`
  - `CONDITIONAL_JUMP` [`00b4f3d4`](#insn-00b4f3d4) → [`00b4f3e0`](#insn-00b4f3e0)
  - `FALL_THROUGH` [`00b4f3d4`](#insn-00b4f3d4) → [`00b4f3d8`](#insn-00b4f3d8)
- ブロック [`00b4f3d8`](#insn-00b4f3d8) 範囲 `[['00b4f3d8', '00b4f3df']]`
  - `FALL_THROUGH` [`00b4f3dc`](#insn-00b4f3dc) → [`00b4f3e0`](#insn-00b4f3e0)
- ブロック [`00b4f3e0`](#insn-00b4f3e0) 範囲 `[['00b4f3e0', '00b4f42f']]`
  - `FALL_THROUGH` [`00b4f42c`](#insn-00b4f42c) → [`00b4f430`](#insn-00b4f430)
- ブロック [`00b4f430`](#insn-00b4f430) 範囲 `[['00b4f430', '00b4f433']]`
  - `FALL_THROUGH` [`00b4f430`](#insn-00b4f430) → [`00b4f434`](#insn-00b4f434)
- ブロック [`00b4f434`](#insn-00b4f434) 範囲 `[['00b4f434', '00b4f437']]`
  - `FALL_THROUGH` [`00b4f434`](#insn-00b4f434) → [`00b4f438`](#insn-00b4f438)
- ブロック [`00b4f438`](#insn-00b4f438) 範囲 `[['00b4f438', '00b4f43f']]`
  - `CONDITIONAL_JUMP` [`00b4f43c`](#insn-00b4f43c) → [`00b4f458`](#insn-00b4f458)
  - `FALL_THROUGH` [`00b4f43c`](#insn-00b4f43c) → [`00b4f440`](#insn-00b4f440)
- ブロック [`00b4f440`](#insn-00b4f440) 範囲 `[['00b4f440', '00b4f447']]`
  - `CONDITIONAL_JUMP` [`00b4f444`](#insn-00b4f444) → [`00b4f45c`](#insn-00b4f45c)
  - `FALL_THROUGH` [`00b4f444`](#insn-00b4f444) → [`00b4f448`](#insn-00b4f448)
- ブロック [`00b4f448`](#insn-00b4f448) 範囲 `[['00b4f448', '00b4f457']]`
  - `UNCONDITIONAL_JUMP` [`00b4f454`](#insn-00b4f454) → [`00b4f45c`](#insn-00b4f45c)
- ブロック [`00b4f458`](#insn-00b4f458) 範囲 `[['00b4f458', '00b4f45b']]`
  - `FALL_THROUGH` [`00b4f458`](#insn-00b4f458) → [`00b4f45c`](#insn-00b4f45c)
- ブロック [`00b4f45c`](#insn-00b4f45c) 範囲 `[['00b4f45c', '00b4f49b']]`
  - `CONDITIONAL_JUMP` [`00b4f498`](#insn-00b4f498) → [`00b4f4b4`](#insn-00b4f4b4)
  - `FALL_THROUGH` [`00b4f498`](#insn-00b4f498) → [`00b4f49c`](#insn-00b4f49c)
- ブロック [`00b4f49c`](#insn-00b4f49c) 範囲 `[['00b4f49c', '00b4f49f']]`
  - `FALL_THROUGH` [`00b4f49c`](#insn-00b4f49c) → [`00b4f4a0`](#insn-00b4f4a0)
- ブロック [`00b4f4a0`](#insn-00b4f4a0) 範囲 `[['00b4f4a0', '00b4f4a3']]`
  - `CONDITIONAL_JUMP` [`00b4f4a0`](#insn-00b4f4a0) → [`00b4f4b8`](#insn-00b4f4b8)
  - `FALL_THROUGH` [`00b4f4a0`](#insn-00b4f4a0) → [`00b4f4a4`](#insn-00b4f4a4)
- ブロック [`00b4f4a4`](#insn-00b4f4a4) 範囲 `[['00b4f4a4', '00b4f4b3']]`
  - `UNCONDITIONAL_JUMP` [`00b4f4b0`](#insn-00b4f4b0) → [`00b4f4b8`](#insn-00b4f4b8)
- ブロック [`00b4f4b4`](#insn-00b4f4b4) 範囲 `[['00b4f4b4', '00b4f4b7']]`
  - `FALL_THROUGH` [`00b4f4b4`](#insn-00b4f4b4) → [`00b4f4b8`](#insn-00b4f4b8)
- ブロック [`00b4f4b8`](#insn-00b4f4b8) 範囲 `[['00b4f4b8', '00b4f4fb']]`
  - `CONDITIONAL_JUMP` [`00b4f4f8`](#insn-00b4f4f8) → [`00b4f514`](#insn-00b4f514)
  - `FALL_THROUGH` [`00b4f4f8`](#insn-00b4f4f8) → [`00b4f4fc`](#insn-00b4f4fc)
- ブロック [`00b4f4fc`](#insn-00b4f4fc) 範囲 `[['00b4f4fc', '00b4f503']]`
  - `CONDITIONAL_JUMP` [`00b4f500`](#insn-00b4f500) → [`00b4f518`](#insn-00b4f518)
  - `FALL_THROUGH` [`00b4f500`](#insn-00b4f500) → [`00b4f504`](#insn-00b4f504)
- ブロック [`00b4f504`](#insn-00b4f504) 範囲 `[['00b4f504', '00b4f50f']]`
  - `FALL_THROUGH` [`00b4f50c`](#insn-00b4f50c) → [`00b4f510`](#insn-00b4f510)
- ブロック [`00b4f510`](#insn-00b4f510) 範囲 `[['00b4f510', '00b4f513']]`
  - `UNCONDITIONAL_JUMP` [`00b4f510`](#insn-00b4f510) → [`00b4f518`](#insn-00b4f518)
- ブロック [`00b4f514`](#insn-00b4f514) 範囲 `[['00b4f514', '00b4f517']]`
  - `FALL_THROUGH` [`00b4f514`](#insn-00b4f514) → [`00b4f518`](#insn-00b4f518)
- ブロック [`00b4f518`](#insn-00b4f518) 範囲 `[['00b4f518', '00b4f54f']]`
  - `CONDITIONAL_JUMP` [`00b4f54c`](#insn-00b4f54c) → [`00b4f568`](#insn-00b4f568)
  - `FALL_THROUGH` [`00b4f54c`](#insn-00b4f54c) → [`00b4f550`](#insn-00b4f550)
- ブロック [`00b4f550`](#insn-00b4f550) 範囲 `[['00b4f550', '00b4f557']]`
  - `CONDITIONAL_JUMP` [`00b4f554`](#insn-00b4f554) → [`00b4f56c`](#insn-00b4f56c)
  - `FALL_THROUGH` [`00b4f554`](#insn-00b4f554) → [`00b4f558`](#insn-00b4f558)
- ブロック [`00b4f558`](#insn-00b4f558) 範囲 `[['00b4f558', '00b4f567']]`
  - `UNCONDITIONAL_JUMP` [`00b4f564`](#insn-00b4f564) → [`00b4f56c`](#insn-00b4f56c)
- ブロック [`00b4f568`](#insn-00b4f568) 範囲 `[['00b4f568', '00b4f56b']]`
  - `FALL_THROUGH` [`00b4f568`](#insn-00b4f568) → [`00b4f56c`](#insn-00b4f56c)
- ブロック [`00b4f56c`](#insn-00b4f56c) 範囲 `[['00b4f56c', '00b4f57b']]`
  - `FALL_THROUGH` [`00b4f578`](#insn-00b4f578) → [`00b4f57c`](#insn-00b4f57c)
- ブロック [`00b4f57c`](#insn-00b4f57c) 範囲 `[['00b4f57c', '00b4f587']]`
  - `FALL_THROUGH` [`00b4f584`](#insn-00b4f584) → [`00b4f588`](#insn-00b4f588)
- ブロック [`00b4f588`](#insn-00b4f588) 範囲 `[['00b4f588', '00b4f597']]`
  - `FALL_THROUGH` [`00b4f594`](#insn-00b4f594) → [`00b4f598`](#insn-00b4f598)
- ブロック [`00b4f598`](#insn-00b4f598) 範囲 `[['00b4f598', '00b4f5ab']]`
  - `CONDITIONAL_JUMP` [`00b4f5a8`](#insn-00b4f5a8) → [`00b4f5e4`](#insn-00b4f5e4)
  - `FALL_THROUGH` [`00b4f5a8`](#insn-00b4f5a8) → [`00b4f5ac`](#insn-00b4f5ac)
- ブロック [`00b4f5ac`](#insn-00b4f5ac) 範囲 `[['00b4f5ac', '00b4f5b3']]`
  - `CONDITIONAL_JUMP` [`00b4f5b0`](#insn-00b4f5b0) → [`00b4f5c0`](#insn-00b4f5c0)
  - `FALL_THROUGH` [`00b4f5b0`](#insn-00b4f5b0) → [`00b4f5b4`](#insn-00b4f5b4)
- ブロック [`00b4f5b4`](#insn-00b4f5b4) 範囲 `[['00b4f5b4', '00b4f5bf']]`
  - `FALL_THROUGH` [`00b4f5bc`](#insn-00b4f5bc) → [`00b4f5c0`](#insn-00b4f5c0)
- ブロック [`00b4f5c0`](#insn-00b4f5c0) 範囲 `[['00b4f5c0', '00b4f5cb']]`
  - `CONDITIONAL_JUMP` [`00b4f5c8`](#insn-00b4f5c8) → [`00b4f5f0`](#insn-00b4f5f0)
  - `FALL_THROUGH` [`00b4f5c8`](#insn-00b4f5c8) → [`00b4f5cc`](#insn-00b4f5cc)
- ブロック [`00b4f5cc`](#insn-00b4f5cc) 範囲 `[['00b4f5cc', '00b4f5d3']]`
  - `CONDITIONAL_JUMP` [`00b4f5d0`](#insn-00b4f5d0) → [`00b4f5f4`](#insn-00b4f5f4)
  - `FALL_THROUGH` [`00b4f5d0`](#insn-00b4f5d0) → [`00b4f5d4`](#insn-00b4f5d4)
- ブロック [`00b4f5d4`](#insn-00b4f5d4) 範囲 `[['00b4f5d4', '00b4f5e3']]`
  - `UNCONDITIONAL_JUMP` [`00b4f5e0`](#insn-00b4f5e0) → [`00b4f5f4`](#insn-00b4f5f4)
- ブロック [`00b4f5e4`](#insn-00b4f5e4) 範囲 `[['00b4f5e4', '00b4f5ef']]`
  - `UNCONDITIONAL_JUMP` [`00b4f5ec`](#insn-00b4f5ec) → [`00b4f5f4`](#insn-00b4f5f4)
- ブロック [`00b4f5f0`](#insn-00b4f5f0) 範囲 `[['00b4f5f0', '00b4f5f3']]`
  - `FALL_THROUGH` [`00b4f5f0`](#insn-00b4f5f0) → [`00b4f5f4`](#insn-00b4f5f4)
- ブロック [`00b4f5f4`](#insn-00b4f5f4) 範囲 `[['00b4f5f4', '00b4f62b']]`
  - `CONDITIONAL_JUMP` [`00b4f628`](#insn-00b4f628) → [`00b4f644`](#insn-00b4f644)
  - `FALL_THROUGH` [`00b4f628`](#insn-00b4f628) → [`00b4f62c`](#insn-00b4f62c)
- ブロック [`00b4f62c`](#insn-00b4f62c) 範囲 `[['00b4f62c', '00b4f633']]`
  - `CONDITIONAL_JUMP` [`00b4f630`](#insn-00b4f630) → [`00b4f648`](#insn-00b4f648)
  - `FALL_THROUGH` [`00b4f630`](#insn-00b4f630) → [`00b4f634`](#insn-00b4f634)
- ブロック [`00b4f634`](#insn-00b4f634) 範囲 `[['00b4f634', '00b4f643']]`
  - `UNCONDITIONAL_JUMP` [`00b4f640`](#insn-00b4f640) → [`00b4f648`](#insn-00b4f648)
- ブロック [`00b4f644`](#insn-00b4f644) 範囲 `[['00b4f644', '00b4f647']]`
  - `FALL_THROUGH` [`00b4f644`](#insn-00b4f644) → [`00b4f648`](#insn-00b4f648)
- ブロック [`00b4f648`](#insn-00b4f648) 範囲 `[['00b4f648', '00b4f687']]`
  - `CONDITIONAL_JUMP` [`00b4f684`](#insn-00b4f684) → [`00b4f6a0`](#insn-00b4f6a0)
  - `FALL_THROUGH` [`00b4f684`](#insn-00b4f684) → [`00b4f688`](#insn-00b4f688)
- ブロック [`00b4f688`](#insn-00b4f688) 範囲 `[['00b4f688', '00b4f68f']]`
  - `CONDITIONAL_JUMP` [`00b4f68c`](#insn-00b4f68c) → [`00b4f6a4`](#insn-00b4f6a4)
  - `FALL_THROUGH` [`00b4f68c`](#insn-00b4f68c) → [`00b4f690`](#insn-00b4f690)
- ブロック [`00b4f690`](#insn-00b4f690) 範囲 `[['00b4f690', '00b4f697']]`
  - `FALL_THROUGH` [`00b4f694`](#insn-00b4f694) → [`00b4f698`](#insn-00b4f698)
- ブロック [`00b4f698`](#insn-00b4f698) 範囲 `[['00b4f698', '00b4f69f']]`
  - `UNCONDITIONAL_JUMP` [`00b4f69c`](#insn-00b4f69c) → [`00b4f6a4`](#insn-00b4f6a4)
- ブロック [`00b4f6a0`](#insn-00b4f6a0) 範囲 `[['00b4f6a0', '00b4f6a3']]`
  - `FALL_THROUGH` [`00b4f6a0`](#insn-00b4f6a0) → [`00b4f6a4`](#insn-00b4f6a4)
- ブロック [`00b4f6a4`](#insn-00b4f6a4) 範囲 `[['00b4f6a4', '00b4f6e3']]`
  - `CONDITIONAL_JUMP` [`00b4f6e0`](#insn-00b4f6e0) → [`00b4f6fc`](#insn-00b4f6fc)
  - `FALL_THROUGH` [`00b4f6e0`](#insn-00b4f6e0) → [`00b4f6e4`](#insn-00b4f6e4)
- ブロック [`00b4f6e4`](#insn-00b4f6e4) 範囲 `[['00b4f6e4', '00b4f6eb']]`
  - `CONDITIONAL_JUMP` [`00b4f6e8`](#insn-00b4f6e8) → [`00b4f700`](#insn-00b4f700)
  - `FALL_THROUGH` [`00b4f6e8`](#insn-00b4f6e8) → [`00b4f6ec`](#insn-00b4f6ec)
- ブロック [`00b4f6ec`](#insn-00b4f6ec) 範囲 `[['00b4f6ec', '00b4f6fb']]`
  - `UNCONDITIONAL_JUMP` [`00b4f6f8`](#insn-00b4f6f8) → [`00b4f700`](#insn-00b4f700)
- ブロック [`00b4f6fc`](#insn-00b4f6fc) 範囲 `[['00b4f6fc', '00b4f6ff']]`
  - `FALL_THROUGH` [`00b4f6fc`](#insn-00b4f6fc) → [`00b4f700`](#insn-00b4f700)
- ブロック [`00b4f700`](#insn-00b4f700) 範囲 `[['00b4f700', '00b4f73f']]`
  - `CONDITIONAL_JUMP` [`00b4f73c`](#insn-00b4f73c) → [`00b4f75c`](#insn-00b4f75c)
  - `FALL_THROUGH` [`00b4f73c`](#insn-00b4f73c) → [`00b4f740`](#insn-00b4f740)
- ブロック [`00b4f740`](#insn-00b4f740) 範囲 `[['00b4f740', '00b4f747']]`
  - `CONDITIONAL_JUMP` [`00b4f744`](#insn-00b4f744) → [`00b4f74c`](#insn-00b4f74c)
  - `FALL_THROUGH` [`00b4f744`](#insn-00b4f744) → [`00b4f748`](#insn-00b4f748)
- ブロック [`00b4f748`](#insn-00b4f748) 範囲 `[['00b4f748', '00b4f74b']]`
  - `FALL_THROUGH` [`00b4f748`](#insn-00b4f748) → [`00b4f74c`](#insn-00b4f74c)
- ブロック [`00b4f74c`](#insn-00b4f74c) 範囲 `[['00b4f74c', '00b4f757']]`
  - `CONDITIONAL_JUMP` [`00b4f754`](#insn-00b4f754) → [`00b4f770`](#insn-00b4f770)
  - `FALL_THROUGH` [`00b4f754`](#insn-00b4f754) → [`00b4f758`](#insn-00b4f758)
- ブロック [`00b4f758`](#insn-00b4f758) 範囲 `[['00b4f758', '00b4f75b']]`
  - `UNCONDITIONAL_JUMP` [`00b4f758`](#insn-00b4f758) → [`00b4f774`](#insn-00b4f774)
- ブロック [`00b4f75c`](#insn-00b4f75c) 範囲 `[['00b4f75c', '00b4f767']]`
  - `CONDITIONAL_JUMP` [`00b4f764`](#insn-00b4f764) → [`00b4f7c8`](#insn-00b4f7c8)
  - `FALL_THROUGH` [`00b4f764`](#insn-00b4f764) → [`00b4f768`](#insn-00b4f768)
- ブロック [`00b4f768`](#insn-00b4f768) 範囲 `[['00b4f768', '00b4f76f']]`
  - `CONDITIONAL_JUMP` [`00b4f76c`](#insn-00b4f76c) → [`00b4f774`](#insn-00b4f774)
  - `FALL_THROUGH` [`00b4f76c`](#insn-00b4f76c) → [`00b4f770`](#insn-00b4f770)
- ブロック [`00b4f770`](#insn-00b4f770) 範囲 `[['00b4f770', '00b4f773']]`
  - `FALL_THROUGH` [`00b4f770`](#insn-00b4f770) → [`00b4f774`](#insn-00b4f774)
- ブロック [`00b4f774`](#insn-00b4f774) 範囲 `[['00b4f774', '00b4f77f']]`
  - `CONDITIONAL_JUMP` [`00b4f77c`](#insn-00b4f77c) → [`00b4fdc0`](#insn-00b4fdc0)
  - `FALL_THROUGH` [`00b4f77c`](#insn-00b4f77c) → [`00b4f780`](#insn-00b4f780)
- ブロック [`00b4f780`](#insn-00b4f780) 範囲 `[['00b4f780', '00b4f783']]`
  - `FALL_THROUGH` [`00b4f780`](#insn-00b4f780) → [`00b4f784`](#insn-00b4f784)
- ブロック [`00b4f784`](#insn-00b4f784) 範囲 `[['00b4f784', '00b4f787']]`
  - `CONDITIONAL_JUMP` [`00b4f784`](#insn-00b4f784) → [`00b4fdc0`](#insn-00b4fdc0)
  - `FALL_THROUGH` [`00b4f784`](#insn-00b4f784) → [`00b4f788`](#insn-00b4f788)
- ブロック [`00b4f788`](#insn-00b4f788) 範囲 `[['00b4f788', '00b4f797']]`
  - `CONDITIONAL_JUMP` [`00b4f794`](#insn-00b4f794) → [`00b4fdc0`](#insn-00b4fdc0)
  - `FALL_THROUGH` [`00b4f794`](#insn-00b4f794) → [`00b4f798`](#insn-00b4f798)
- ブロック [`00b4f798`](#insn-00b4f798) 範囲 `[['00b4f798', '00b4f79f']]`
  - `FALL_THROUGH` [`00b4f79c`](#insn-00b4f79c) → [`00b4f7a0`](#insn-00b4f7a0)
- ブロック [`00b4f7a0`](#insn-00b4f7a0) 範囲 `[['00b4f7a0', '00b4f7af']]`
  - `CONDITIONAL_JUMP` [`00b4f7ac`](#insn-00b4f7ac) → [`00b4f7d0`](#insn-00b4f7d0)
  - `FALL_THROUGH` [`00b4f7ac`](#insn-00b4f7ac) → [`00b4f7b0`](#insn-00b4f7b0)
- ブロック [`00b4f7b0`](#insn-00b4f7b0) 範囲 `[['00b4f7b0', '00b4f7b7']]`
  - `CONDITIONAL_JUMP` [`00b4f7b4`](#insn-00b4f7b4) → [`00b4f7d4`](#insn-00b4f7d4)
  - `FALL_THROUGH` [`00b4f7b4`](#insn-00b4f7b4) → [`00b4f7b8`](#insn-00b4f7b8)
- ブロック [`00b4f7b8`](#insn-00b4f7b8) 範囲 `[['00b4f7b8', '00b4f7c7']]`
  - `UNCONDITIONAL_JUMP` [`00b4f7c4`](#insn-00b4f7c4) → [`00b4f7d4`](#insn-00b4f7d4)
- ブロック [`00b4f7c8`](#insn-00b4f7c8) 範囲 `[['00b4f7c8', '00b4f7cf']]`
  - `UNCONDITIONAL_JUMP` [`00b4f7cc`](#insn-00b4f7cc) → [`00b4fdc0`](#insn-00b4fdc0)
- ブロック [`00b4f7d0`](#insn-00b4f7d0) 範囲 `[['00b4f7d0', '00b4f7d3']]`
  - `FALL_THROUGH` [`00b4f7d0`](#insn-00b4f7d0) → [`00b4f7d4`](#insn-00b4f7d4)
- ブロック [`00b4f7d4`](#insn-00b4f7d4) 範囲 `[['00b4f7d4', '00b4f80b']]`
  - `CONDITIONAL_JUMP` [`00b4f808`](#insn-00b4f808) → [`00b4f824`](#insn-00b4f824)
  - `FALL_THROUGH` [`00b4f808`](#insn-00b4f808) → [`00b4f80c`](#insn-00b4f80c)
- ブロック [`00b4f80c`](#insn-00b4f80c) 範囲 `[['00b4f80c', '00b4f813']]`
  - `CONDITIONAL_JUMP` [`00b4f810`](#insn-00b4f810) → [`00b4f828`](#insn-00b4f828)
  - `FALL_THROUGH` [`00b4f810`](#insn-00b4f810) → [`00b4f814`](#insn-00b4f814)
- ブロック [`00b4f814`](#insn-00b4f814) 範囲 `[['00b4f814', '00b4f823']]`
  - `UNCONDITIONAL_JUMP` [`00b4f820`](#insn-00b4f820) → [`00b4f828`](#insn-00b4f828)
- ブロック [`00b4f824`](#insn-00b4f824) 範囲 `[['00b4f824', '00b4f827']]`
  - `FALL_THROUGH` [`00b4f824`](#insn-00b4f824) → [`00b4f828`](#insn-00b4f828)
- ブロック [`00b4f828`](#insn-00b4f828) 範囲 `[['00b4f828', '00b4f867']]`
  - `CONDITIONAL_JUMP` [`00b4f864`](#insn-00b4f864) → [`00b4f880`](#insn-00b4f880)
  - `FALL_THROUGH` [`00b4f864`](#insn-00b4f864) → [`00b4f868`](#insn-00b4f868)
- ブロック [`00b4f868`](#insn-00b4f868) 範囲 `[['00b4f868', '00b4f86f']]`
  - `CONDITIONAL_JUMP` [`00b4f86c`](#insn-00b4f86c) → [`00b4f884`](#insn-00b4f884)
  - `FALL_THROUGH` [`00b4f86c`](#insn-00b4f86c) → [`00b4f870`](#insn-00b4f870)
- ブロック [`00b4f870`](#insn-00b4f870) 範囲 `[['00b4f870', '00b4f877']]`
  - `FALL_THROUGH` [`00b4f874`](#insn-00b4f874) → [`00b4f878`](#insn-00b4f878)
- ブロック [`00b4f878`](#insn-00b4f878) 範囲 `[['00b4f878', '00b4f87f']]`
  - `UNCONDITIONAL_JUMP` [`00b4f87c`](#insn-00b4f87c) → [`00b4f884`](#insn-00b4f884)
- ブロック [`00b4f880`](#insn-00b4f880) 範囲 `[['00b4f880', '00b4f883']]`
  - `FALL_THROUGH` [`00b4f880`](#insn-00b4f880) → [`00b4f884`](#insn-00b4f884)
- ブロック [`00b4f884`](#insn-00b4f884) 範囲 `[['00b4f884', '00b4f8c3']]`
  - `CONDITIONAL_JUMP` [`00b4f8c0`](#insn-00b4f8c0) → [`00b4f8dc`](#insn-00b4f8dc)
  - `FALL_THROUGH` [`00b4f8c0`](#insn-00b4f8c0) → [`00b4f8c4`](#insn-00b4f8c4)
- ブロック [`00b4f8c4`](#insn-00b4f8c4) 範囲 `[['00b4f8c4', '00b4f8cb']]`
  - `CONDITIONAL_JUMP` [`00b4f8c8`](#insn-00b4f8c8) → [`00b4f8e0`](#insn-00b4f8e0)
  - `FALL_THROUGH` [`00b4f8c8`](#insn-00b4f8c8) → [`00b4f8cc`](#insn-00b4f8cc)
- ブロック [`00b4f8cc`](#insn-00b4f8cc) 範囲 `[['00b4f8cc', '00b4f8db']]`
  - `UNCONDITIONAL_JUMP` [`00b4f8d8`](#insn-00b4f8d8) → [`00b4f8e0`](#insn-00b4f8e0)
- ブロック [`00b4f8dc`](#insn-00b4f8dc) 範囲 `[['00b4f8dc', '00b4f8df']]`
  - `FALL_THROUGH` [`00b4f8dc`](#insn-00b4f8dc) → [`00b4f8e0`](#insn-00b4f8e0)
- ブロック [`00b4f8e0`](#insn-00b4f8e0) 範囲 `[['00b4f8e0', '00b4f91f']]`
  - `CONDITIONAL_JUMP` [`00b4f91c`](#insn-00b4f91c) → [`00b4f938`](#insn-00b4f938)
  - `FALL_THROUGH` [`00b4f91c`](#insn-00b4f91c) → [`00b4f920`](#insn-00b4f920)
- ブロック [`00b4f920`](#insn-00b4f920) 範囲 `[['00b4f920', '00b4f927']]`
  - `CONDITIONAL_JUMP` [`00b4f924`](#insn-00b4f924) → [`00b4f93c`](#insn-00b4f93c)
  - `FALL_THROUGH` [`00b4f924`](#insn-00b4f924) → [`00b4f928`](#insn-00b4f928)
- ブロック [`00b4f928`](#insn-00b4f928) 範囲 `[['00b4f928', '00b4f937']]`
  - `UNCONDITIONAL_JUMP` [`00b4f934`](#insn-00b4f934) → [`00b4f93c`](#insn-00b4f93c)
- ブロック [`00b4f938`](#insn-00b4f938) 範囲 `[['00b4f938', '00b4f93b']]`
  - `FALL_THROUGH` [`00b4f938`](#insn-00b4f938) → [`00b4f93c`](#insn-00b4f93c)
- ブロック [`00b4f93c`](#insn-00b4f93c) 範囲 `[['00b4f93c', '00b4f947']]`
  - `FALL_THROUGH` [`00b4f944`](#insn-00b4f944) → [`00b4f948`](#insn-00b4f948)
- ブロック [`00b4f948`](#insn-00b4f948) 範囲 `[['00b4f948', '00b4f97b']]`
  - `CONDITIONAL_JUMP` [`00b4f978`](#insn-00b4f978) → [`00b4f994`](#insn-00b4f994)
  - `FALL_THROUGH` [`00b4f978`](#insn-00b4f978) → [`00b4f97c`](#insn-00b4f97c)
- ブロック [`00b4f97c`](#insn-00b4f97c) 範囲 `[['00b4f97c', '00b4f983']]`
  - `CONDITIONAL_JUMP` [`00b4f980`](#insn-00b4f980) → [`00b4f998`](#insn-00b4f998)
  - `FALL_THROUGH` [`00b4f980`](#insn-00b4f980) → [`00b4f984`](#insn-00b4f984)
- ブロック [`00b4f984`](#insn-00b4f984) 範囲 `[['00b4f984', '00b4f993']]`
  - `UNCONDITIONAL_JUMP` [`00b4f990`](#insn-00b4f990) → [`00b4f998`](#insn-00b4f998)
- ブロック [`00b4f994`](#insn-00b4f994) 範囲 `[['00b4f994', '00b4f997']]`
  - `FALL_THROUGH` [`00b4f994`](#insn-00b4f994) → [`00b4f998`](#insn-00b4f998)
- ブロック [`00b4f998`](#insn-00b4f998) 範囲 `[['00b4f998', '00b4f99f']]`
  - `FALL_THROUGH` [`00b4f99c`](#insn-00b4f99c) → [`00b4f9a0`](#insn-00b4f9a0)
- ブロック [`00b4f9a0`](#insn-00b4f9a0) 範囲 `[['00b4f9a0', '00b4f9b7']]`
  - `FALL_THROUGH` [`00b4f9b4`](#insn-00b4f9b4) → [`00b4f9b8`](#insn-00b4f9b8)
- ブロック [`00b4f9b8`](#insn-00b4f9b8) 範囲 `[['00b4f9b8', '00b4f9bf']]`
  - `FALL_THROUGH` [`00b4f9bc`](#insn-00b4f9bc) → [`00b4f9c0`](#insn-00b4f9c0)
- ブロック [`00b4f9c0`](#insn-00b4f9c0) 範囲 `[['00b4f9c0', '00b4f9cb']]`
  - `FALL_THROUGH` [`00b4f9c8`](#insn-00b4f9c8) → [`00b4f9cc`](#insn-00b4f9cc)
- ブロック [`00b4f9cc`](#insn-00b4f9cc) 範囲 `[['00b4f9cc', '00b4f9d7']]`
  - `CONDITIONAL_JUMP` [`00b4f9d4`](#insn-00b4f9d4) → [`00b4f9f0`](#insn-00b4f9f0)
  - `FALL_THROUGH` [`00b4f9d4`](#insn-00b4f9d4) → [`00b4f9d8`](#insn-00b4f9d8)
- ブロック [`00b4f9d8`](#insn-00b4f9d8) 範囲 `[['00b4f9d8', '00b4f9df']]`
  - `CONDITIONAL_JUMP` [`00b4f9dc`](#insn-00b4f9dc) → [`00b4f9f4`](#insn-00b4f9f4)
  - `FALL_THROUGH` [`00b4f9dc`](#insn-00b4f9dc) → [`00b4f9e0`](#insn-00b4f9e0)
- ブロック [`00b4f9e0`](#insn-00b4f9e0) 範囲 `[['00b4f9e0', '00b4f9ef']]`
  - `UNCONDITIONAL_JUMP` [`00b4f9ec`](#insn-00b4f9ec) → [`00b4f9f4`](#insn-00b4f9f4)
- ブロック [`00b4f9f0`](#insn-00b4f9f0) 範囲 `[['00b4f9f0', '00b4f9f3']]`
  - `FALL_THROUGH` [`00b4f9f0`](#insn-00b4f9f0) → [`00b4f9f4`](#insn-00b4f9f4)
- ブロック [`00b4f9f4`](#insn-00b4f9f4) 範囲 `[['00b4f9f4', '00b4fa33']]`
  - `CONDITIONAL_JUMP` [`00b4fa30`](#insn-00b4fa30) → [`00b4fa4c`](#insn-00b4fa4c)
  - `FALL_THROUGH` [`00b4fa30`](#insn-00b4fa30) → [`00b4fa34`](#insn-00b4fa34)
- ブロック [`00b4fa34`](#insn-00b4fa34) 範囲 `[['00b4fa34', '00b4fa3b']]`
  - `CONDITIONAL_JUMP` [`00b4fa38`](#insn-00b4fa38) → [`00b4fa50`](#insn-00b4fa50)
  - `FALL_THROUGH` [`00b4fa38`](#insn-00b4fa38) → [`00b4fa3c`](#insn-00b4fa3c)
- ブロック [`00b4fa3c`](#insn-00b4fa3c) 範囲 `[['00b4fa3c', '00b4fa4b']]`
  - `UNCONDITIONAL_JUMP` [`00b4fa48`](#insn-00b4fa48) → [`00b4fa50`](#insn-00b4fa50)
- ブロック [`00b4fa4c`](#insn-00b4fa4c) 範囲 `[['00b4fa4c', '00b4fa4f']]`
  - `FALL_THROUGH` [`00b4fa4c`](#insn-00b4fa4c) → [`00b4fa50`](#insn-00b4fa50)
- ブロック [`00b4fa50`](#insn-00b4fa50) 範囲 `[['00b4fa50', '00b4fa8f']]`
  - `CONDITIONAL_JUMP` [`00b4fa8c`](#insn-00b4fa8c) → [`00b4faa8`](#insn-00b4faa8)
  - `FALL_THROUGH` [`00b4fa8c`](#insn-00b4fa8c) → [`00b4fa90`](#insn-00b4fa90)
- ブロック [`00b4fa90`](#insn-00b4fa90) 範囲 `[['00b4fa90', '00b4fa97']]`
  - `CONDITIONAL_JUMP` [`00b4fa94`](#insn-00b4fa94) → [`00b4faac`](#insn-00b4faac)
  - `FALL_THROUGH` [`00b4fa94`](#insn-00b4fa94) → [`00b4fa98`](#insn-00b4fa98)
- ブロック [`00b4fa98`](#insn-00b4fa98) 範囲 `[['00b4fa98', '00b4faa7']]`
  - `UNCONDITIONAL_JUMP` [`00b4faa4`](#insn-00b4faa4) → [`00b4faac`](#insn-00b4faac)
- ブロック [`00b4faa8`](#insn-00b4faa8) 範囲 `[['00b4faa8', '00b4faab']]`
  - `FALL_THROUGH` [`00b4faa8`](#insn-00b4faa8) → [`00b4faac`](#insn-00b4faac)
- ブロック [`00b4faac`](#insn-00b4faac) 範囲 `[['00b4faac', '00b4faeb']]`
  - `CONDITIONAL_JUMP` [`00b4fae8`](#insn-00b4fae8) → [`00b4fbec`](#insn-00b4fbec)
  - `FALL_THROUGH` [`00b4fae8`](#insn-00b4fae8) → [`00b4faec`](#insn-00b4faec)
- ブロック [`00b4faec`](#insn-00b4faec) 範囲 `[['00b4faec', '00b4faf3']]`
  - `CONDITIONAL_JUMP` [`00b4faf0`](#insn-00b4faf0) → [`00b4fbec`](#insn-00b4fbec)
  - `FALL_THROUGH` [`00b4faf0`](#insn-00b4faf0) → [`00b4faf4`](#insn-00b4faf4)
- ブロック [`00b4faf4`](#insn-00b4faf4) 範囲 `[['00b4faf4', '00b4fb1f']]`
  - `CONDITIONAL_JUMP` [`00b4fb1c`](#insn-00b4fb1c) → [`00b4fb34`](#insn-00b4fb34)
  - `FALL_THROUGH` [`00b4fb1c`](#insn-00b4fb1c) → [`00b4fb20`](#insn-00b4fb20)
- ブロック [`00b4fb20`](#insn-00b4fb20) 範囲 `[['00b4fb20', '00b4fb23']]`
  - `FALL_THROUGH` [`00b4fb20`](#insn-00b4fb20) → [`00b4fb24`](#insn-00b4fb24)
- ブロック [`00b4fb24`](#insn-00b4fb24) 範囲 `[['00b4fb24', '00b4fb2b']]`
  - `FALL_THROUGH` [`00b4fb28`](#insn-00b4fb28) → [`00b4fb2c`](#insn-00b4fb2c)
- ブロック [`00b4fb2c`](#insn-00b4fb2c) 範囲 `[['00b4fb2c', '00b4fb33']]`
  - `UNCONDITIONAL_JUMP` [`00b4fb30`](#insn-00b4fb30) → [`00b4fb78`](#insn-00b4fb78)
- ブロック [`00b4fb34`](#insn-00b4fb34) 範囲 `[['00b4fb34', '00b4fb37']]`
  - `CONDITIONAL_JUMP` [`00b4fb34`](#insn-00b4fb34) → [`00b4fb78`](#insn-00b4fb78)
  - `FALL_THROUGH` [`00b4fb34`](#insn-00b4fb34) → [`00b4fb38`](#insn-00b4fb38)
- ブロック [`00b4fb38`](#insn-00b4fb38) 範囲 `[['00b4fb38', '00b4fb47']]`
  - `CONDITIONAL_JUMP` [`00b4fb44`](#insn-00b4fb44) → [`00b4fb74`](#insn-00b4fb74)
  - `FALL_THROUGH` [`00b4fb44`](#insn-00b4fb44) → [`00b4fb48`](#insn-00b4fb48)
- ブロック [`00b4fb48`](#insn-00b4fb48) 範囲 `[['00b4fb48', '00b4fb53']]`
  - `CONDITIONAL_JUMP` [`00b4fb50`](#insn-00b4fb50) → [`00b4fb68`](#insn-00b4fb68)
  - `FALL_THROUGH` [`00b4fb50`](#insn-00b4fb50) → [`00b4fb54`](#insn-00b4fb54)
- ブロック [`00b4fb54`](#insn-00b4fb54) 範囲 `[['00b4fb54', '00b4fb5f']]`
  - `CONDITIONAL_JUMP` [`00b4fb5c`](#insn-00b4fb5c) → [`00b4fb74`](#insn-00b4fb74)
  - `FALL_THROUGH` [`00b4fb5c`](#insn-00b4fb5c) → [`00b4fb60`](#insn-00b4fb60)
- ブロック [`00b4fb60`](#insn-00b4fb60) 範囲 `[['00b4fb60', '00b4fb67']]`
  - `CONDITIONAL_JUMP` [`00b4fb64`](#insn-00b4fb64) → [`00b4fb54`](#insn-00b4fb54)
  - `FALL_THROUGH` [`00b4fb64`](#insn-00b4fb64) → [`00b4fb68`](#insn-00b4fb68)
- ブロック [`00b4fb68`](#insn-00b4fb68) 範囲 `[['00b4fb68', '00b4fb6b']]`
  - `FALL_THROUGH` [`00b4fb68`](#insn-00b4fb68) → [`00b4fb6c`](#insn-00b4fb6c)
- ブロック [`00b4fb6c`](#insn-00b4fb6c) 範囲 `[['00b4fb6c', '00b4fb73']]`
  - `UNCONDITIONAL_JUMP` [`00b4fb70`](#insn-00b4fb70) → [`00b4fb54`](#insn-00b4fb54)
- ブロック [`00b4fb74`](#insn-00b4fb74) 範囲 `[['00b4fb74', '00b4fb77']]`
  - `FALL_THROUGH` [`00b4fb74`](#insn-00b4fb74) → [`00b4fb78`](#insn-00b4fb78)
- ブロック [`00b4fb78`](#insn-00b4fb78) 範囲 `[['00b4fb78', '00b4fb7b']]`
  - `CONDITIONAL_JUMP` [`00b4fb78`](#insn-00b4fb78) → [`00b4fbec`](#insn-00b4fbec)
  - `FALL_THROUGH` [`00b4fb78`](#insn-00b4fb78) → [`00b4fb7c`](#insn-00b4fb7c)
- ブロック [`00b4fb7c`](#insn-00b4fb7c) 範囲 `[['00b4fb7c', '00b4fb97']]`
  - `FALL_THROUGH` [`00b4fb94`](#insn-00b4fb94) → [`00b4fb98`](#insn-00b4fb98)
- ブロック [`00b4fb98`](#insn-00b4fb98) 範囲 `[['00b4fb98', '00b4fba7']]`
  - `FALL_THROUGH` [`00b4fba4`](#insn-00b4fba4) → [`00b4fba8`](#insn-00b4fba8)
- ブロック [`00b4fba8`](#insn-00b4fba8) 範囲 `[['00b4fba8', '00b4fbb7']]`
  - `FALL_THROUGH` [`00b4fbb4`](#insn-00b4fbb4) → [`00b4fbb8`](#insn-00b4fbb8)
- ブロック [`00b4fbb8`](#insn-00b4fbb8) 範囲 `[['00b4fbb8', '00b4fbc7']]`
  - `FALL_THROUGH` [`00b4fbc4`](#insn-00b4fbc4) → [`00b4fbc8`](#insn-00b4fbc8)
- ブロック [`00b4fbc8`](#insn-00b4fbc8) 範囲 `[['00b4fbc8', '00b4fbcb']]`
  - `FALL_THROUGH` [`00b4fbc8`](#insn-00b4fbc8) → [`00b4fbcc`](#insn-00b4fbcc)
- ブロック [`00b4fbcc`](#insn-00b4fbcc) 範囲 `[['00b4fbcc', '00b4fbeb']]`
  - `CONDITIONAL_JUMP` [`00b4fbe8`](#insn-00b4fbe8) → [`00b4fb98`](#insn-00b4fb98)
  - `FALL_THROUGH` [`00b4fbe8`](#insn-00b4fbe8) → [`00b4fbec`](#insn-00b4fbec)
- ブロック [`00b4fbec`](#insn-00b4fbec) 範囲 `[['00b4fbec', '00b4fbff']]`
  - `CONDITIONAL_JUMP` [`00b4fbfc`](#insn-00b4fbfc) → [`00b4fc18`](#insn-00b4fc18)
  - `FALL_THROUGH` [`00b4fbfc`](#insn-00b4fbfc) → [`00b4fc00`](#insn-00b4fc00)
- ブロック [`00b4fc00`](#insn-00b4fc00) 範囲 `[['00b4fc00', '00b4fc03']]`
  - `FALL_THROUGH` [`00b4fc00`](#insn-00b4fc00) → [`00b4fc04`](#insn-00b4fc04)
- ブロック [`00b4fc04`](#insn-00b4fc04) 範囲 `[['00b4fc04', '00b4fc07']]`
  - `CONDITIONAL_JUMP` [`00b4fc04`](#insn-00b4fc04) → [`00b4fc1c`](#insn-00b4fc1c)
  - `FALL_THROUGH` [`00b4fc04`](#insn-00b4fc04) → [`00b4fc08`](#insn-00b4fc08)
- ブロック [`00b4fc08`](#insn-00b4fc08) 範囲 `[['00b4fc08', '00b4fc17']]`
  - `UNCONDITIONAL_JUMP` [`00b4fc14`](#insn-00b4fc14) → [`00b4fc1c`](#insn-00b4fc1c)
- ブロック [`00b4fc18`](#insn-00b4fc18) 範囲 `[['00b4fc18', '00b4fc1b']]`
  - `FALL_THROUGH` [`00b4fc18`](#insn-00b4fc18) → [`00b4fc1c`](#insn-00b4fc1c)
- ブロック [`00b4fc1c`](#insn-00b4fc1c) 範囲 `[['00b4fc1c', '00b4fc37']]`
  - `FALL_THROUGH` [`00b4fc34`](#insn-00b4fc34) → [`00b4fc38`](#insn-00b4fc38)
- ブロック [`00b4fc38`](#insn-00b4fc38) 範囲 `[['00b4fc38', '00b4fc5b']]`
  - `CONDITIONAL_JUMP` [`00b4fc58`](#insn-00b4fc58) → [`00b4fd5c`](#insn-00b4fd5c)
  - `FALL_THROUGH` [`00b4fc58`](#insn-00b4fc58) → [`00b4fc5c`](#insn-00b4fc5c)
- ブロック [`00b4fc5c`](#insn-00b4fc5c) 範囲 `[['00b4fc5c', '00b4fc63']]`
  - `CONDITIONAL_JUMP` [`00b4fc60`](#insn-00b4fc60) → [`00b4fd5c`](#insn-00b4fd5c)
  - `FALL_THROUGH` [`00b4fc60`](#insn-00b4fc60) → [`00b4fc64`](#insn-00b4fc64)
- ブロック [`00b4fc64`](#insn-00b4fc64) 範囲 `[['00b4fc64', '00b4fc6b']]`
  - `FALL_THROUGH` [`00b4fc68`](#insn-00b4fc68) → [`00b4fc6c`](#insn-00b4fc6c)
- ブロック [`00b4fc6c`](#insn-00b4fc6c) 範囲 `[['00b4fc6c', '00b4fc6f']]`
  - `FALL_THROUGH` [`00b4fc6c`](#insn-00b4fc6c) → [`00b4fc70`](#insn-00b4fc70)
- ブロック [`00b4fc70`](#insn-00b4fc70) 範囲 `[['00b4fc70', '00b4fc8f']]`
  - `CONDITIONAL_JUMP` [`00b4fc8c`](#insn-00b4fc8c) → [`00b4fca4`](#insn-00b4fca4)
  - `FALL_THROUGH` [`00b4fc8c`](#insn-00b4fc8c) → [`00b4fc90`](#insn-00b4fc90)
- ブロック [`00b4fc90`](#insn-00b4fc90) 範囲 `[['00b4fc90', '00b4fc9f']]`
  - `FALL_THROUGH` [`00b4fc9c`](#insn-00b4fc9c) → [`00b4fca0`](#insn-00b4fca0)
- ブロック [`00b4fca0`](#insn-00b4fca0) 範囲 `[['00b4fca0', '00b4fca3']]`
  - `UNCONDITIONAL_JUMP` [`00b4fca0`](#insn-00b4fca0) → [`00b4fce8`](#insn-00b4fce8)
- ブロック [`00b4fca4`](#insn-00b4fca4) 範囲 `[['00b4fca4', '00b4fca7']]`
  - `CONDITIONAL_JUMP` [`00b4fca4`](#insn-00b4fca4) → [`00b4fce8`](#insn-00b4fce8)
  - `FALL_THROUGH` [`00b4fca4`](#insn-00b4fca4) → [`00b4fca8`](#insn-00b4fca8)
- ブロック [`00b4fca8`](#insn-00b4fca8) 範囲 `[['00b4fca8', '00b4fcab']]`
  - `FALL_THROUGH` [`00b4fca8`](#insn-00b4fca8) → [`00b4fcac`](#insn-00b4fcac)
- ブロック [`00b4fcac`](#insn-00b4fcac) 範囲 `[['00b4fcac', '00b4fcb7']]`
  - `CONDITIONAL_JUMP` [`00b4fcb4`](#insn-00b4fcb4) → [`00b4fce4`](#insn-00b4fce4)
  - `FALL_THROUGH` [`00b4fcb4`](#insn-00b4fcb4) → [`00b4fcb8`](#insn-00b4fcb8)
- ブロック [`00b4fcb8`](#insn-00b4fcb8) 範囲 `[['00b4fcb8', '00b4fcc3']]`
  - `CONDITIONAL_JUMP` [`00b4fcc0`](#insn-00b4fcc0) → [`00b4fcd8`](#insn-00b4fcd8)
  - `FALL_THROUGH` [`00b4fcc0`](#insn-00b4fcc0) → [`00b4fcc4`](#insn-00b4fcc4)
- ブロック [`00b4fcc4`](#insn-00b4fcc4) 範囲 `[['00b4fcc4', '00b4fccf']]`
  - `CONDITIONAL_JUMP` [`00b4fccc`](#insn-00b4fccc) → [`00b4fce4`](#insn-00b4fce4)
  - `FALL_THROUGH` [`00b4fccc`](#insn-00b4fccc) → [`00b4fcd0`](#insn-00b4fcd0)
- ブロック [`00b4fcd0`](#insn-00b4fcd0) 範囲 `[['00b4fcd0', '00b4fcd7']]`
  - `CONDITIONAL_JUMP` [`00b4fcd4`](#insn-00b4fcd4) → [`00b4fcc4`](#insn-00b4fcc4)
  - `FALL_THROUGH` [`00b4fcd4`](#insn-00b4fcd4) → [`00b4fcd8`](#insn-00b4fcd8)
- ブロック [`00b4fcd8`](#insn-00b4fcd8) 範囲 `[['00b4fcd8', '00b4fce3']]`
  - `UNCONDITIONAL_JUMP` [`00b4fce0`](#insn-00b4fce0) → [`00b4fcc4`](#insn-00b4fcc4)
- ブロック [`00b4fce4`](#insn-00b4fce4) 範囲 `[['00b4fce4', '00b4fce7']]`
  - `FALL_THROUGH` [`00b4fce4`](#insn-00b4fce4) → [`00b4fce8`](#insn-00b4fce8)
- ブロック [`00b4fce8`](#insn-00b4fce8) 範囲 `[['00b4fce8', '00b4fceb']]`
  - `CONDITIONAL_JUMP` [`00b4fce8`](#insn-00b4fce8) → [`00b4fd5c`](#insn-00b4fd5c)
  - `FALL_THROUGH` [`00b4fce8`](#insn-00b4fce8) → [`00b4fcec`](#insn-00b4fcec)
- ブロック [`00b4fcec`](#insn-00b4fcec) 範囲 `[['00b4fcec', '00b4fd07']]`
  - `FALL_THROUGH` [`00b4fd04`](#insn-00b4fd04) → [`00b4fd08`](#insn-00b4fd08)
- ブロック [`00b4fd08`](#insn-00b4fd08) 範囲 `[['00b4fd08', '00b4fd5b']]`
  - `CONDITIONAL_JUMP` [`00b4fd58`](#insn-00b4fd58) → [`00b4fd08`](#insn-00b4fd08)
  - `FALL_THROUGH` [`00b4fd58`](#insn-00b4fd58) → [`00b4fd5c`](#insn-00b4fd5c)
- ブロック [`00b4fd5c`](#insn-00b4fd5c) 範囲 `[['00b4fd5c', '00b4fd6f']]`
  - `CONDITIONAL_JUMP` [`00b4fd6c`](#insn-00b4fd6c) → [`00b4fd88`](#insn-00b4fd88)
  - `FALL_THROUGH` [`00b4fd6c`](#insn-00b4fd6c) → [`00b4fd70`](#insn-00b4fd70)
- ブロック [`00b4fd70`](#insn-00b4fd70) 範囲 `[['00b4fd70', '00b4fd77']]`
  - `CONDITIONAL_JUMP` [`00b4fd74`](#insn-00b4fd74) → [`00b4fd8c`](#insn-00b4fd8c)
  - `FALL_THROUGH` [`00b4fd74`](#insn-00b4fd74) → [`00b4fd78`](#insn-00b4fd78)
- ブロック [`00b4fd78`](#insn-00b4fd78) 範囲 `[['00b4fd78', '00b4fd87']]`
  - `UNCONDITIONAL_JUMP` [`00b4fd84`](#insn-00b4fd84) → [`00b4fd8c`](#insn-00b4fd8c)
- ブロック [`00b4fd88`](#insn-00b4fd88) 範囲 `[['00b4fd88', '00b4fd8b']]`
  - `FALL_THROUGH` [`00b4fd88`](#insn-00b4fd88) → [`00b4fd8c`](#insn-00b4fd8c)
- ブロック [`00b4fd8c`](#insn-00b4fd8c) 範囲 `[['00b4fd8c', '00b4fdbf']]`
  - `FALL_THROUGH` [`00b4fdbc`](#insn-00b4fdbc) → [`00b4fdc0`](#insn-00b4fdc0)
- ブロック [`00b4fdc0`](#insn-00b4fdc0) 範囲 `[['00b4fdc0', '00b4fdd7']]`
  - `CONDITIONAL_JUMP` [`00b4fdd4`](#insn-00b4fdd4) → [`00b4fde0`](#insn-00b4fde0)
  - `FALL_THROUGH` [`00b4fdd4`](#insn-00b4fdd4) → [`00b4fdd8`](#insn-00b4fdd8)
- ブロック [`00b4fdd8`](#insn-00b4fdd8) 範囲 `[['00b4fdd8', '00b4fddf']]`
  - `FALL_THROUGH` [`00b4fddc`](#insn-00b4fddc) → [`00b4fde0`](#insn-00b4fde0)
- ブロック [`00b4fde0`](#insn-00b4fde0) 範囲 `[['00b4fde0', '00b4fde7']]`
  - `CONDITIONAL_JUMP` [`00b4fde4`](#insn-00b4fde4) → [`00b4fdf0`](#insn-00b4fdf0)
  - `FALL_THROUGH` [`00b4fde4`](#insn-00b4fde4) → [`00b4fde8`](#insn-00b4fde8)
- ブロック [`00b4fde8`](#insn-00b4fde8) 範囲 `[['00b4fde8', '00b4fdef']]`
  - `FALL_THROUGH` [`00b4fdec`](#insn-00b4fdec) → [`00b4fdf0`](#insn-00b4fdf0)
- ブロック [`00b4fdf0`](#insn-00b4fdf0) 範囲 `[['00b4fdf0', '00b4fe0f']]`
  - `CONDITIONAL_JUMP` [`00b4fe0c`](#insn-00b4fe0c) → [`00b4fe30`](#insn-00b4fe30)
  - `FALL_THROUGH` [`00b4fe0c`](#insn-00b4fe0c) → [`00b4fe10`](#insn-00b4fe10)
- ブロック [`00b4fe10`](#insn-00b4fe10) 範囲 `[['00b4fe10', '00b4fe2f']]`
- ブロック [`00b4fe30`](#insn-00b4fe30) 範囲 `[['00b4fe30', '00b4fe33']]`

## 命令位置別の参照

- [`00b4efec`](#insn-00b4efec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eff0`](#insn-00b4eff0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eff4`](#insn-00b4eff4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eff8`](#insn-00b4eff8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4effc`](#insn-00b4effc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f000`](#insn-00b4f000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f00c`](#insn-00b4f00c) → `Stack[-0x338]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f028`](#insn-00b4f028) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f02c`](#insn-00b4f02c) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f030`](#insn-00b4f030) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f034`](#insn-00b4f034) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f038`](#insn-00b4f038) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f03c`](#insn-00b4f03c) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f040`](#insn-00b4f040) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f044`](#insn-00b4f044) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f048`](#insn-00b4f048) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f04c`](#insn-00b4f04c) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f050`](#insn-00b4f050) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f054`](#insn-00b4f054) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f058`](#insn-00b4f058) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f05c`](#insn-00b4f05c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f060`](#insn-00b4f060) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f064`](#insn-00b4f064) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f068`](#insn-00b4f068) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f06c`](#insn-00b4f06c) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f070`](#insn-00b4f070) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f074`](#insn-00b4f074) → `Stack[-0x230]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f078`](#insn-00b4f078) → `Stack[-0x250]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f07c`](#insn-00b4f07c) → `Stack[-0x270]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f080`](#insn-00b4f080) → `Stack[-0x290]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f084`](#insn-00b4f084) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f088`](#insn-00b4f088) → `Stack[-0x2d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f08c`](#insn-00b4f08c) → `Stack[-0x2f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f090`](#insn-00b4f090) → `Stack[-0x300]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f094`](#insn-00b4f094) → `Stack[-0x308]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0b0`](#insn-00b4f0b0) → [`00b4f0c8`](#insn-00b4f0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0b8`](#insn-00b4f0b8) → [`00b4f0c8`](#insn-00b4f0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0dc`](#insn-00b4f0dc) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f0e0`](#insn-00b4f0e0) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0f0`](#insn-00b4f0f0) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f104`](#insn-00b4f104) → [`00b4f120`](#insn-00b4f120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f10c`](#insn-00b4f10c) → [`00b4f124`](#insn-00b4f124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f11c`](#insn-00b4f11c) → [`00b4f124`](#insn-00b4f124) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f134`](#insn-00b4f134) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f13c`](#insn-00b4f13c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f14c`](#insn-00b4f14c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f164`](#insn-00b4f164) → [`00b4f35c`](#insn-00b4f35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f16c`](#insn-00b4f16c) → [`00b4f35c`](#insn-00b4f35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f17c`](#insn-00b4f17c) → [`00b4f35c`](#insn-00b4f35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f184`](#insn-00b4f184) → [`00b4f35c`](#insn-00b4f35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f198`](#insn-00b4f198) → `Stack[-0x340]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f19c`](#insn-00b4f19c) → [`00b4f1b0`](#insn-00b4f1b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f1ac`](#insn-00b4f1ac) → [`00b4f350`](#insn-00b4f350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f1f0`](#insn-00b4f1f0) → [`00b4f278`](#insn-00b4f278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f1f8`](#insn-00b4f1f8) → [`00b4f224`](#insn-00b4f224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f234`](#insn-00b4f234) → [`00b4f284`](#insn-00b4f284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f250`](#insn-00b4f250) → [`00b4f284`](#insn-00b4f284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f274`](#insn-00b4f274) → [`00b4f288`](#insn-00b4f288) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f27c`](#insn-00b4f27c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f280`](#insn-00b4f280) → [`00b4f288`](#insn-00b4f288) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f298`](#insn-00b4f298) → [`00bde640`](../00bde/00bde640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde640` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2a8`](#insn-00b4f2a8) → [`0044a6d0`](../0044a/0044a6d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044a6d0` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2b4`](#insn-00b4f2b4) → [`00b4f320`](#insn-00b4f320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2bc`](#insn-00b4f2bc) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2c0`](#insn-00b4f2c0) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2c4`](#insn-00b4f2c4) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2c8`](#insn-00b4f2c8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2cc`](#insn-00b4f2cc) → `Stack[-0x318]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2d0`](#insn-00b4f2d0) → `Stack[-0x320]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2ec`](#insn-00b4f2ec) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2f4`](#insn-00b4f2f4) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2f8`](#insn-00b4f2f8) → [`00b4f308`](#insn-00b4f308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f2fc`](#insn-00b4f2fc) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f304`](#insn-00b4f304) → [`00b4f30c`](#insn-00b4f30c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f30c`](#insn-00b4f30c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f310`](#insn-00b4f310) → [`00bde660`](../00bde/00bde660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde660` · 推定シンボル `None` · 推定型 `None`
- [`00b4f314`](#insn-00b4f314) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f31c`](#insn-00b4f31c) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f328`](#insn-00b4f328) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f338`](#insn-00b4f338) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f33c`](#insn-00b4f33c) → `Stack[-0x320]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f340`](#insn-00b4f340) → [`00b4f1a0`](#insn-00b4f1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f344`](#insn-00b4f344) → `Stack[-0x310]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f348`](#insn-00b4f348) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b4f34c`](#insn-00b4f34c) → [`00b4f1a0`](#insn-00b4f1a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f350`](#insn-00b4f350) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f368`](#insn-00b4f368) → [`00b4f430`](#insn-00b4f430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f370`](#insn-00b4f370) → [`00b4f430`](#insn-00b4f430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f380`](#insn-00b4f380) → [`00b4f430`](#insn-00b4f430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f384`](#insn-00b4f384) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f388`](#insn-00b4f388) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f398`](#insn-00b4f398) → [`00b4f3e0`](#insn-00b4f3e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f39c`](#insn-00b4f39c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3a4`](#insn-00b4f3a4) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3bc`](#insn-00b4f3bc) → [`00b4f3cc`](#insn-00b4f3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3c8`](#insn-00b4f3c8) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3cc`](#insn-00b4f3cc) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3d0`](#insn-00b4f3d0) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3d4`](#insn-00b4f3d4) → [`00b4f3e0`](#insn-00b4f3e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f3dc`](#insn-00b4f3dc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b4f408`](#insn-00b4f408) → `Stack[-0x328]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f418`](#insn-00b4f418) → `Stack[-0x330]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f424`](#insn-00b4f424) → [`00be0480`](../00be0/00be0480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0480` · 推定シンボル `None` · 推定型 `None`
- [`00b4f43c`](#insn-00b4f43c) → [`00b4f458`](#insn-00b4f458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f444`](#insn-00b4f444) → [`00b4f45c`](#insn-00b4f45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f454`](#insn-00b4f454) → [`00b4f45c`](#insn-00b4f45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f46c`](#insn-00b4f46c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f474`](#insn-00b4f474) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f484`](#insn-00b4f484) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f498`](#insn-00b4f498) → [`00b4f4b4`](#insn-00b4f4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f4a0`](#insn-00b4f4a0) → [`00b4f4b8`](#insn-00b4f4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f4b0`](#insn-00b4f4b0) → [`00b4f4b8`](#insn-00b4f4b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f4c8`](#insn-00b4f4c8) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f4d0`](#insn-00b4f4d0) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f4e0`](#insn-00b4f4e0) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f4f8`](#insn-00b4f4f8) → [`00b4f514`](#insn-00b4f514) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f500`](#insn-00b4f500) → [`00b4f518`](#insn-00b4f518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f510`](#insn-00b4f510) → [`00b4f518`](#insn-00b4f518) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f524`](#insn-00b4f524) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f528`](#insn-00b4f528) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f538`](#insn-00b4f538) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f54c`](#insn-00b4f54c) → [`00b4f568`](#insn-00b4f568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f554`](#insn-00b4f554) → [`00b4f56c`](#insn-00b4f56c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f564`](#insn-00b4f564) → [`00b4f56c`](#insn-00b4f56c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f57c`](#insn-00b4f57c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f584`](#insn-00b4f584) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f594`](#insn-00b4f594) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5a8`](#insn-00b4f5a8) → [`00b4f5e4`](#insn-00b4f5e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5b0`](#insn-00b4f5b0) → [`00b4f5c0`](#insn-00b4f5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5c4`](#insn-00b4f5c4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5c8`](#insn-00b4f5c8) → [`00b4f5f0`](#insn-00b4f5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5d0`](#insn-00b4f5d0) → [`00b4f5f4`](#insn-00b4f5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5e0`](#insn-00b4f5e0) → [`00b4f5f4`](#insn-00b4f5f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5e8`](#insn-00b4f5e8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f5ec`](#insn-00b4f5ec) → [`00b4f5f4`](#insn-00b4f5f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f600`](#insn-00b4f600) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f604`](#insn-00b4f604) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f614`](#insn-00b4f614) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f628`](#insn-00b4f628) → [`00b4f644`](#insn-00b4f644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f630`](#insn-00b4f630) → [`00b4f648`](#insn-00b4f648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f640`](#insn-00b4f640) → [`00b4f648`](#insn-00b4f648) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f658`](#insn-00b4f658) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f660`](#insn-00b4f660) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f670`](#insn-00b4f670) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f684`](#insn-00b4f684) → [`00b4f6a0`](#insn-00b4f6a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f68c`](#insn-00b4f68c) → [`00b4f6a4`](#insn-00b4f6a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f69c`](#insn-00b4f69c) → [`00b4f6a4`](#insn-00b4f6a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f6b4`](#insn-00b4f6b4) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f6bc`](#insn-00b4f6bc) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f6cc`](#insn-00b4f6cc) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f6e0`](#insn-00b4f6e0) → [`00b4f6fc`](#insn-00b4f6fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f6e8`](#insn-00b4f6e8) → [`00b4f700`](#insn-00b4f700) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f6f8`](#insn-00b4f6f8) → [`00b4f700`](#insn-00b4f700) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f710`](#insn-00b4f710) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f718`](#insn-00b4f718) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f728`](#insn-00b4f728) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f73c`](#insn-00b4f73c) → [`00b4f75c`](#insn-00b4f75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f744`](#insn-00b4f744) → [`00b4f74c`](#insn-00b4f74c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f74c`](#insn-00b4f74c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f754`](#insn-00b4f754) → [`00b4f770`](#insn-00b4f770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f758`](#insn-00b4f758) → [`00b4f774`](#insn-00b4f774) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f760`](#insn-00b4f760) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f764`](#insn-00b4f764) → [`00b4f7c8`](#insn-00b4f7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f76c`](#insn-00b4f76c) → [`00b4f774`](#insn-00b4f774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f778`](#insn-00b4f778) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f77c`](#insn-00b4f77c) → [`00b4fdc0`](#insn-00b4fdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f784`](#insn-00b4f784) → [`00b4fdc0`](#insn-00b4fdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f794`](#insn-00b4f794) → [`00b4fdc0`](#insn-00b4fdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f79c`](#insn-00b4f79c) → `Stack[-0x340]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7ac`](#insn-00b4f7ac) → [`00b4f7d0`](#insn-00b4f7d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7b4`](#insn-00b4f7b4) → [`00b4f7d4`](#insn-00b4f7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7c4`](#insn-00b4f7c4) → [`00b4f7d4`](#insn-00b4f7d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7c8`](#insn-00b4f7c8) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7cc`](#insn-00b4f7cc) → [`00b4fdc0`](#insn-00b4fdc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7e0`](#insn-00b4f7e0) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f7e4`](#insn-00b4f7e4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f7f4`](#insn-00b4f7f4) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f808`](#insn-00b4f808) → [`00b4f824`](#insn-00b4f824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f810`](#insn-00b4f810) → [`00b4f828`](#insn-00b4f828) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f820`](#insn-00b4f820) → [`00b4f828`](#insn-00b4f828) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f838`](#insn-00b4f838) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f840`](#insn-00b4f840) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f850`](#insn-00b4f850) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f864`](#insn-00b4f864) → [`00b4f880`](#insn-00b4f880) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f86c`](#insn-00b4f86c) → [`00b4f884`](#insn-00b4f884) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f87c`](#insn-00b4f87c) → [`00b4f884`](#insn-00b4f884) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f894`](#insn-00b4f894) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f89c`](#insn-00b4f89c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f8ac`](#insn-00b4f8ac) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f8c0`](#insn-00b4f8c0) → [`00b4f8dc`](#insn-00b4f8dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f8c8`](#insn-00b4f8c8) → [`00b4f8e0`](#insn-00b4f8e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f8d8`](#insn-00b4f8d8) → [`00b4f8e0`](#insn-00b4f8e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f8f0`](#insn-00b4f8f0) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f8f8`](#insn-00b4f8f8) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f908`](#insn-00b4f908) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f91c`](#insn-00b4f91c) → [`00b4f938`](#insn-00b4f938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f924`](#insn-00b4f924) → [`00b4f93c`](#insn-00b4f93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f934`](#insn-00b4f934) → [`00b4f93c`](#insn-00b4f93c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f94c`](#insn-00b4f94c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f954`](#insn-00b4f954) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f964`](#insn-00b4f964) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f978`](#insn-00b4f978) → [`00b4f994`](#insn-00b4f994) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f980`](#insn-00b4f980) → [`00b4f998`](#insn-00b4f998) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f990`](#insn-00b4f990) → [`00b4f998`](#insn-00b4f998) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f9a8`](#insn-00b4f9a8) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f9b0`](#insn-00b4f9b0) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4f9c0`](#insn-00b4f9c0) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4f9d4`](#insn-00b4f9d4) → [`00b4f9f0`](#insn-00b4f9f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f9dc`](#insn-00b4f9dc) → [`00b4f9f4`](#insn-00b4f9f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f9ec`](#insn-00b4f9ec) → [`00b4f9f4`](#insn-00b4f9f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa04`](#insn-00b4fa04) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4fa0c`](#insn-00b4fa0c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa1c`](#insn-00b4fa1c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa30`](#insn-00b4fa30) → [`00b4fa4c`](#insn-00b4fa4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa38`](#insn-00b4fa38) → [`00b4fa50`](#insn-00b4fa50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa48`](#insn-00b4fa48) → [`00b4fa50`](#insn-00b4fa50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa60`](#insn-00b4fa60) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4fa68`](#insn-00b4fa68) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa78`](#insn-00b4fa78) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa8c`](#insn-00b4fa8c) → [`00b4faa8`](#insn-00b4faa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fa94`](#insn-00b4fa94) → [`00b4faac`](#insn-00b4faac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4faa4`](#insn-00b4faa4) → [`00b4faac`](#insn-00b4faac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fabc`](#insn-00b4fabc) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4fac4`](#insn-00b4fac4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fad4`](#insn-00b4fad4) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fae8`](#insn-00b4fae8) → [`00b4fbec`](#insn-00b4fbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4faf0`](#insn-00b4faf0) → [`00b4fbec`](#insn-00b4fbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fafc`](#insn-00b4fafc) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb1c`](#insn-00b4fb1c) → [`00b4fb34`](#insn-00b4fb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb2c`](#insn-00b4fb2c) → [`00be0470`](../00be0/00be0470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0470` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb30`](#insn-00b4fb30) → [`00b4fb78`](#insn-00b4fb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb34`](#insn-00b4fb34) → [`00b4fb78`](#insn-00b4fb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb44`](#insn-00b4fb44) → [`00b4fb74`](#insn-00b4fb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb50`](#insn-00b4fb50) → [`00b4fb68`](#insn-00b4fb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb5c`](#insn-00b4fb5c) → [`00b4fb74`](#insn-00b4fb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb64`](#insn-00b4fb64) → [`00b4fb54`](#insn-00b4fb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb6c`](#insn-00b4fb6c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb70`](#insn-00b4fb70) → [`00b4fb54`](#insn-00b4fb54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb74`](#insn-00b4fb74) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb78`](#insn-00b4fb78) → [`00b4fbec`](#insn-00b4fbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb7c`](#insn-00b4fb7c) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fb9c`](#insn-00b4fb9c) → `Stack[-0x218]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fbc8`](#insn-00b4fbc8) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fbd8`](#insn-00b4fbd8) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fbe8`](#insn-00b4fbe8) → [`00b4fb98`](#insn-00b4fb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fbfc`](#insn-00b4fbfc) → [`00b4fc18`](#insn-00b4fc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc04`](#insn-00b4fc04) → [`00b4fc1c`](#insn-00b4fc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc14`](#insn-00b4fc14) → [`00b4fc1c`](#insn-00b4fc1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc2c`](#insn-00b4fc2c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4fc34`](#insn-00b4fc34) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc44`](#insn-00b4fc44) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc58`](#insn-00b4fc58) → [`00b4fd5c`](#insn-00b4fd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc60`](#insn-00b4fc60) → [`00b4fd5c`](#insn-00b4fd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc6c`](#insn-00b4fc6c) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc8c`](#insn-00b4fc8c) → [`00b4fca4`](#insn-00b4fca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fc9c`](#insn-00b4fc9c) → [`00be0470`](../00be0/00be0470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0470` · 推定シンボル `None` · 推定型 `None`
- [`00b4fca0`](#insn-00b4fca0) → [`00b4fce8`](#insn-00b4fce8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fca4`](#insn-00b4fca4) → [`00b4fce8`](#insn-00b4fce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fcb4`](#insn-00b4fcb4) → [`00b4fce4`](#insn-00b4fce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fcc0`](#insn-00b4fcc0) → [`00b4fcd8`](#insn-00b4fcd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fccc`](#insn-00b4fccc) → [`00b4fce4`](#insn-00b4fce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fcd4`](#insn-00b4fcd4) → [`00b4fcc4`](#insn-00b4fcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fcdc`](#insn-00b4fcdc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b4fce0`](#insn-00b4fce0) → [`00b4fcc4`](#insn-00b4fcc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fce4`](#insn-00b4fce4) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fce8`](#insn-00b4fce8) → [`00b4fd5c`](#insn-00b4fd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fcec`](#insn-00b4fcec) → `Stack[-0x340]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd0c`](#insn-00b4fd0c) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd38`](#insn-00b4fd38) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd48`](#insn-00b4fd48) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd58`](#insn-00b4fd58) → [`00b4fd08`](#insn-00b4fd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd6c`](#insn-00b4fd6c) → [`00b4fd88`](#insn-00b4fd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd74`](#insn-00b4fd74) → [`00b4fd8c`](#insn-00b4fd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd84`](#insn-00b4fd84) → [`00b4fd8c`](#insn-00b4fd8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fd98`](#insn-00b4fd98) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4fd9c`](#insn-00b4fd9c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdb0`](#insn-00b4fdb0) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdb8`](#insn-00b4fdb8) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdbc`](#insn-00b4fdbc) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdc0`](#insn-00b4fdc0) → `Stack[-0x338]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdd0`](#insn-00b4fdd0) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdd4`](#insn-00b4fdd4) → [`00b4fde0`](#insn-00b4fde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdd8`](#insn-00b4fdd8) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fddc`](#insn-00b4fddc) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fde0`](#insn-00b4fde0) → `Stack[-0x308]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fde4`](#insn-00b4fde4) → [`00b4fdf0`](#insn-00b4fdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fde8`](#insn-00b4fde8) → `Stack[-0x2f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdec`](#insn-00b4fdec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdf4`](#insn-00b4fdf4) → [`00be0260`](../00be0/00be0260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0260` · 推定シンボル `None` · 推定型 `None`
- [`00b4fdfc`](#insn-00b4fdfc) → [`00be0320`](../00be0/00be0320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0320` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe04`](#insn-00b4fe04) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe0c`](#insn-00b4fe0c) → [`00b4fe30`](#insn-00b4fe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe14`](#insn-00b4fe14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe18`](#insn-00b4fe18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe1c`](#insn-00b4fe1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe20`](#insn-00b4fe20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe24`](#insn-00b4fe24) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4fe30`](#insn-00b4fe30) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4efec`](#insn-00b4efec)

~~~json
{
  "source": "00b4efec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eff0`](#insn-00b4eff0)

~~~json
{
  "source": "00b4eff0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eff4`](#insn-00b4eff4)

~~~json
{
  "source": "00b4eff4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eff8`](#insn-00b4eff8)

~~~json
{
  "source": "00b4eff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4effc`](#insn-00b4effc)

~~~json
{
  "source": "00b4effc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f000`](#insn-00b4f000)

~~~json
{
  "source": "00b4f000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f00c`](#insn-00b4f00c)

~~~json
{
  "source": "00b4f00c",
  "target": "Stack[-0x338]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f028`](#insn-00b4f028)

~~~json
{
  "source": "00b4f028",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f02c`](#insn-00b4f02c)

~~~json
{
  "source": "00b4f02c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f030`](#insn-00b4f030)

~~~json
{
  "source": "00b4f030",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f034`](#insn-00b4f034)

~~~json
{
  "source": "00b4f034",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f038`](#insn-00b4f038)

~~~json
{
  "source": "00b4f038",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f03c`](#insn-00b4f03c)

~~~json
{
  "source": "00b4f03c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f040`](#insn-00b4f040)

~~~json
{
  "source": "00b4f040",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f044`](#insn-00b4f044)

~~~json
{
  "source": "00b4f044",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f048`](#insn-00b4f048)

~~~json
{
  "source": "00b4f048",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f04c`](#insn-00b4f04c)

~~~json
{
  "source": "00b4f04c",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f050`](#insn-00b4f050)

~~~json
{
  "source": "00b4f050",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f054`](#insn-00b4f054)

~~~json
{
  "source": "00b4f054",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f058`](#insn-00b4f058)

~~~json
{
  "source": "00b4f058",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f05c`](#insn-00b4f05c)

~~~json
{
  "source": "00b4f05c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f060`](#insn-00b4f060)

~~~json
{
  "source": "00b4f060",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f064`](#insn-00b4f064)

~~~json
{
  "source": "00b4f064",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f068`](#insn-00b4f068)

~~~json
{
  "source": "00b4f068",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f06c`](#insn-00b4f06c)

~~~json
{
  "source": "00b4f06c",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f070`](#insn-00b4f070)

~~~json
{
  "source": "00b4f070",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f074`](#insn-00b4f074)

~~~json
{
  "source": "00b4f074",
  "target": "Stack[-0x230]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f078`](#insn-00b4f078)

~~~json
{
  "source": "00b4f078",
  "target": "Stack[-0x250]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f07c`](#insn-00b4f07c)

~~~json
{
  "source": "00b4f07c",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f080`](#insn-00b4f080)

~~~json
{
  "source": "00b4f080",
  "target": "Stack[-0x290]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f084`](#insn-00b4f084)

~~~json
{
  "source": "00b4f084",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f088`](#insn-00b4f088)

~~~json
{
  "source": "00b4f088",
  "target": "Stack[-0x2d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f08c`](#insn-00b4f08c)

~~~json
{
  "source": "00b4f08c",
  "target": "Stack[-0x2f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f090`](#insn-00b4f090)

~~~json
{
  "source": "00b4f090",
  "target": "Stack[-0x300]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f094`](#insn-00b4f094)

~~~json
{
  "source": "00b4f094",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0b0`](#insn-00b4f0b0)

~~~json
{
  "source": "00b4f0b0",
  "target": "00b4f0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0b8`](#insn-00b4f0b8)

~~~json
{
  "source": "00b4f0b8",
  "target": "00b4f0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0dc`](#insn-00b4f0dc)

~~~json
{
  "source": "00b4f0dc",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f0e0`](#insn-00b4f0e0)

~~~json
{
  "source": "00b4f0e0",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f0f0`](#insn-00b4f0f0)

~~~json
{
  "source": "00b4f0f0",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f104`](#insn-00b4f104)

~~~json
{
  "source": "00b4f104",
  "target": "00b4f120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f10c`](#insn-00b4f10c)

~~~json
{
  "source": "00b4f10c",
  "target": "00b4f124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f11c`](#insn-00b4f11c)

~~~json
{
  "source": "00b4f11c",
  "target": "00b4f124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f134`](#insn-00b4f134)

~~~json
{
  "source": "00b4f134",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f13c`](#insn-00b4f13c)

~~~json
{
  "source": "00b4f13c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f14c`](#insn-00b4f14c)

~~~json
{
  "source": "00b4f14c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f164`](#insn-00b4f164)

~~~json
{
  "source": "00b4f164",
  "target": "00b4f35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f16c`](#insn-00b4f16c)

~~~json
{
  "source": "00b4f16c",
  "target": "00b4f35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f17c`](#insn-00b4f17c)

~~~json
{
  "source": "00b4f17c",
  "target": "00b4f35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f184`](#insn-00b4f184)

~~~json
{
  "source": "00b4f184",
  "target": "00b4f35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f198`](#insn-00b4f198)

~~~json
{
  "source": "00b4f198",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f19c`](#insn-00b4f19c)

~~~json
{
  "source": "00b4f19c",
  "target": "00b4f1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f1ac`](#insn-00b4f1ac)

~~~json
{
  "source": "00b4f1ac",
  "target": "00b4f350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f1f0`](#insn-00b4f1f0)

~~~json
{
  "source": "00b4f1f0",
  "target": "00b4f278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f1f8`](#insn-00b4f1f8)

~~~json
{
  "source": "00b4f1f8",
  "target": "00b4f224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f234`](#insn-00b4f234)

~~~json
{
  "source": "00b4f234",
  "target": "00b4f284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f250`](#insn-00b4f250)

~~~json
{
  "source": "00b4f250",
  "target": "00b4f284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f274`](#insn-00b4f274)

~~~json
{
  "source": "00b4f274",
  "target": "00b4f288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f27c`](#insn-00b4f27c)

~~~json
{
  "source": "00b4f27c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f280`](#insn-00b4f280)

~~~json
{
  "source": "00b4f280",
  "target": "00b4f288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f298`](#insn-00b4f298)

~~~json
{
  "source": "00b4f298",
  "target": "00bde640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f2a8`](#insn-00b4f2a8)

~~~json
{
  "source": "00b4f2a8",
  "target": "0044a6d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f2b4`](#insn-00b4f2b4)

~~~json
{
  "source": "00b4f2b4",
  "target": "00b4f320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2bc`](#insn-00b4f2bc)

~~~json
{
  "source": "00b4f2bc",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f2c0`](#insn-00b4f2c0)

~~~json
{
  "source": "00b4f2c0",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2c4`](#insn-00b4f2c4)

~~~json
{
  "source": "00b4f2c4",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2c8`](#insn-00b4f2c8)

~~~json
{
  "source": "00b4f2c8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2cc`](#insn-00b4f2cc)

~~~json
{
  "source": "00b4f2cc",
  "target": "Stack[-0x318]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2d0`](#insn-00b4f2d0)

~~~json
{
  "source": "00b4f2d0",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2ec`](#insn-00b4f2ec)

~~~json
{
  "source": "00b4f2ec",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2f4`](#insn-00b4f2f4)

~~~json
{
  "source": "00b4f2f4",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2f8`](#insn-00b4f2f8)

~~~json
{
  "source": "00b4f2f8",
  "target": "00b4f308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f2fc`](#insn-00b4f2fc)

~~~json
{
  "source": "00b4f2fc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f304`](#insn-00b4f304)

~~~json
{
  "source": "00b4f304",
  "target": "00b4f30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f30c`](#insn-00b4f30c)

~~~json
{
  "source": "00b4f30c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f310`](#insn-00b4f310)

~~~json
{
  "source": "00b4f310",
  "target": "00bde660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f314`](#insn-00b4f314)

~~~json
{
  "source": "00b4f314",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f31c`](#insn-00b4f31c)

~~~json
{
  "source": "00b4f31c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f328`](#insn-00b4f328)

~~~json
{
  "source": "00b4f328",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f338`](#insn-00b4f338)

~~~json
{
  "source": "00b4f338",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f33c`](#insn-00b4f33c)

~~~json
{
  "source": "00b4f33c",
  "target": "Stack[-0x320]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f340`](#insn-00b4f340)

~~~json
{
  "source": "00b4f340",
  "target": "00b4f1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f344`](#insn-00b4f344)

~~~json
{
  "source": "00b4f344",
  "target": "Stack[-0x310]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f348`](#insn-00b4f348)

~~~json
{
  "source": "00b4f348",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f34c`](#insn-00b4f34c)

~~~json
{
  "source": "00b4f34c",
  "target": "00b4f1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f350`](#insn-00b4f350)

~~~json
{
  "source": "00b4f350",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f368`](#insn-00b4f368)

~~~json
{
  "source": "00b4f368",
  "target": "00b4f430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f370`](#insn-00b4f370)

~~~json
{
  "source": "00b4f370",
  "target": "00b4f430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f380`](#insn-00b4f380)

~~~json
{
  "source": "00b4f380",
  "target": "00b4f430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f384`](#insn-00b4f384)

~~~json
{
  "source": "00b4f384",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f388`](#insn-00b4f388)

~~~json
{
  "source": "00b4f388",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f398`](#insn-00b4f398)

~~~json
{
  "source": "00b4f398",
  "target": "00b4f3e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f39c`](#insn-00b4f39c)

~~~json
{
  "source": "00b4f39c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f3a4`](#insn-00b4f3a4)

~~~json
{
  "source": "00b4f3a4",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f3bc`](#insn-00b4f3bc)

~~~json
{
  "source": "00b4f3bc",
  "target": "00b4f3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f3c8`](#insn-00b4f3c8)

~~~json
{
  "source": "00b4f3c8",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f3cc`](#insn-00b4f3cc)

~~~json
{
  "source": "00b4f3cc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f3d0`](#insn-00b4f3d0)

~~~json
{
  "source": "00b4f3d0",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f3d4`](#insn-00b4f3d4)

~~~json
{
  "source": "00b4f3d4",
  "target": "00b4f3e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f3dc`](#insn-00b4f3dc)

~~~json
{
  "source": "00b4f3dc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f408`](#insn-00b4f408)

~~~json
{
  "source": "00b4f408",
  "target": "Stack[-0x328]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f418`](#insn-00b4f418)

~~~json
{
  "source": "00b4f418",
  "target": "Stack[-0x330]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f424`](#insn-00b4f424)

~~~json
{
  "source": "00b4f424",
  "target": "00be0480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f43c`](#insn-00b4f43c)

~~~json
{
  "source": "00b4f43c",
  "target": "00b4f458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f444`](#insn-00b4f444)

~~~json
{
  "source": "00b4f444",
  "target": "00b4f45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f454`](#insn-00b4f454)

~~~json
{
  "source": "00b4f454",
  "target": "00b4f45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f46c`](#insn-00b4f46c)

~~~json
{
  "source": "00b4f46c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f474`](#insn-00b4f474)

~~~json
{
  "source": "00b4f474",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f484`](#insn-00b4f484)

~~~json
{
  "source": "00b4f484",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f498`](#insn-00b4f498)

~~~json
{
  "source": "00b4f498",
  "target": "00b4f4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f4a0`](#insn-00b4f4a0)

~~~json
{
  "source": "00b4f4a0",
  "target": "00b4f4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f4b0`](#insn-00b4f4b0)

~~~json
{
  "source": "00b4f4b0",
  "target": "00b4f4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f4c8`](#insn-00b4f4c8)

~~~json
{
  "source": "00b4f4c8",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f4d0`](#insn-00b4f4d0)

~~~json
{
  "source": "00b4f4d0",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f4e0`](#insn-00b4f4e0)

~~~json
{
  "source": "00b4f4e0",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f4f8`](#insn-00b4f4f8)

~~~json
{
  "source": "00b4f4f8",
  "target": "00b4f514",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f500`](#insn-00b4f500)

~~~json
{
  "source": "00b4f500",
  "target": "00b4f518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f510`](#insn-00b4f510)

~~~json
{
  "source": "00b4f510",
  "target": "00b4f518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f524`](#insn-00b4f524)

~~~json
{
  "source": "00b4f524",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f528`](#insn-00b4f528)

~~~json
{
  "source": "00b4f528",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f538`](#insn-00b4f538)

~~~json
{
  "source": "00b4f538",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f54c`](#insn-00b4f54c)

~~~json
{
  "source": "00b4f54c",
  "target": "00b4f568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f554`](#insn-00b4f554)

~~~json
{
  "source": "00b4f554",
  "target": "00b4f56c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f564`](#insn-00b4f564)

~~~json
{
  "source": "00b4f564",
  "target": "00b4f56c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f57c`](#insn-00b4f57c)

~~~json
{
  "source": "00b4f57c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f584`](#insn-00b4f584)

~~~json
{
  "source": "00b4f584",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f594`](#insn-00b4f594)

~~~json
{
  "source": "00b4f594",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f5a8`](#insn-00b4f5a8)

~~~json
{
  "source": "00b4f5a8",
  "target": "00b4f5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5b0`](#insn-00b4f5b0)

~~~json
{
  "source": "00b4f5b0",
  "target": "00b4f5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5c4`](#insn-00b4f5c4)

~~~json
{
  "source": "00b4f5c4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5c8`](#insn-00b4f5c8)

~~~json
{
  "source": "00b4f5c8",
  "target": "00b4f5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5d0`](#insn-00b4f5d0)

~~~json
{
  "source": "00b4f5d0",
  "target": "00b4f5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5e0`](#insn-00b4f5e0)

~~~json
{
  "source": "00b4f5e0",
  "target": "00b4f5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5e8`](#insn-00b4f5e8)

~~~json
{
  "source": "00b4f5e8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f5ec`](#insn-00b4f5ec)

~~~json
{
  "source": "00b4f5ec",
  "target": "00b4f5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f600`](#insn-00b4f600)

~~~json
{
  "source": "00b4f600",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f604`](#insn-00b4f604)

~~~json
{
  "source": "00b4f604",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f614`](#insn-00b4f614)

~~~json
{
  "source": "00b4f614",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f628`](#insn-00b4f628)

~~~json
{
  "source": "00b4f628",
  "target": "00b4f644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f630`](#insn-00b4f630)

~~~json
{
  "source": "00b4f630",
  "target": "00b4f648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f640`](#insn-00b4f640)

~~~json
{
  "source": "00b4f640",
  "target": "00b4f648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f658`](#insn-00b4f658)

~~~json
{
  "source": "00b4f658",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f660`](#insn-00b4f660)

~~~json
{
  "source": "00b4f660",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f670`](#insn-00b4f670)

~~~json
{
  "source": "00b4f670",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f684`](#insn-00b4f684)

~~~json
{
  "source": "00b4f684",
  "target": "00b4f6a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f68c`](#insn-00b4f68c)

~~~json
{
  "source": "00b4f68c",
  "target": "00b4f6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f69c`](#insn-00b4f69c)

~~~json
{
  "source": "00b4f69c",
  "target": "00b4f6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f6b4`](#insn-00b4f6b4)

~~~json
{
  "source": "00b4f6b4",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f6bc`](#insn-00b4f6bc)

~~~json
{
  "source": "00b4f6bc",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f6cc`](#insn-00b4f6cc)

~~~json
{
  "source": "00b4f6cc",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f6e0`](#insn-00b4f6e0)

~~~json
{
  "source": "00b4f6e0",
  "target": "00b4f6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f6e8`](#insn-00b4f6e8)

~~~json
{
  "source": "00b4f6e8",
  "target": "00b4f700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f6f8`](#insn-00b4f6f8)

~~~json
{
  "source": "00b4f6f8",
  "target": "00b4f700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f710`](#insn-00b4f710)

~~~json
{
  "source": "00b4f710",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f718`](#insn-00b4f718)

~~~json
{
  "source": "00b4f718",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f728`](#insn-00b4f728)

~~~json
{
  "source": "00b4f728",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f73c`](#insn-00b4f73c)

~~~json
{
  "source": "00b4f73c",
  "target": "00b4f75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f744`](#insn-00b4f744)

~~~json
{
  "source": "00b4f744",
  "target": "00b4f74c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f74c`](#insn-00b4f74c)

~~~json
{
  "source": "00b4f74c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f754`](#insn-00b4f754)

~~~json
{
  "source": "00b4f754",
  "target": "00b4f770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f758`](#insn-00b4f758)

~~~json
{
  "source": "00b4f758",
  "target": "00b4f774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f760`](#insn-00b4f760)

~~~json
{
  "source": "00b4f760",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f764`](#insn-00b4f764)

~~~json
{
  "source": "00b4f764",
  "target": "00b4f7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f76c`](#insn-00b4f76c)

~~~json
{
  "source": "00b4f76c",
  "target": "00b4f774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f778`](#insn-00b4f778)

~~~json
{
  "source": "00b4f778",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f77c`](#insn-00b4f77c)

~~~json
{
  "source": "00b4f77c",
  "target": "00b4fdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f784`](#insn-00b4f784)

~~~json
{
  "source": "00b4f784",
  "target": "00b4fdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f794`](#insn-00b4f794)

~~~json
{
  "source": "00b4f794",
  "target": "00b4fdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f79c`](#insn-00b4f79c)

~~~json
{
  "source": "00b4f79c",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7ac`](#insn-00b4f7ac)

~~~json
{
  "source": "00b4f7ac",
  "target": "00b4f7d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7b4`](#insn-00b4f7b4)

~~~json
{
  "source": "00b4f7b4",
  "target": "00b4f7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7c4`](#insn-00b4f7c4)

~~~json
{
  "source": "00b4f7c4",
  "target": "00b4f7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7c8`](#insn-00b4f7c8)

~~~json
{
  "source": "00b4f7c8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7cc`](#insn-00b4f7cc)

~~~json
{
  "source": "00b4f7cc",
  "target": "00b4fdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f7e0`](#insn-00b4f7e0)

~~~json
{
  "source": "00b4f7e0",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f7e4`](#insn-00b4f7e4)

~~~json
{
  "source": "00b4f7e4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f7f4`](#insn-00b4f7f4)

~~~json
{
  "source": "00b4f7f4",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f808`](#insn-00b4f808)

~~~json
{
  "source": "00b4f808",
  "target": "00b4f824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f810`](#insn-00b4f810)

~~~json
{
  "source": "00b4f810",
  "target": "00b4f828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f820`](#insn-00b4f820)

~~~json
{
  "source": "00b4f820",
  "target": "00b4f828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f838`](#insn-00b4f838)

~~~json
{
  "source": "00b4f838",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f840`](#insn-00b4f840)

~~~json
{
  "source": "00b4f840",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f850`](#insn-00b4f850)

~~~json
{
  "source": "00b4f850",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f864`](#insn-00b4f864)

~~~json
{
  "source": "00b4f864",
  "target": "00b4f880",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f86c`](#insn-00b4f86c)

~~~json
{
  "source": "00b4f86c",
  "target": "00b4f884",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f87c`](#insn-00b4f87c)

~~~json
{
  "source": "00b4f87c",
  "target": "00b4f884",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f894`](#insn-00b4f894)

~~~json
{
  "source": "00b4f894",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f89c`](#insn-00b4f89c)

~~~json
{
  "source": "00b4f89c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f8ac`](#insn-00b4f8ac)

~~~json
{
  "source": "00b4f8ac",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f8c0`](#insn-00b4f8c0)

~~~json
{
  "source": "00b4f8c0",
  "target": "00b4f8dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f8c8`](#insn-00b4f8c8)

~~~json
{
  "source": "00b4f8c8",
  "target": "00b4f8e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f8d8`](#insn-00b4f8d8)

~~~json
{
  "source": "00b4f8d8",
  "target": "00b4f8e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f8f0`](#insn-00b4f8f0)

~~~json
{
  "source": "00b4f8f0",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f8f8`](#insn-00b4f8f8)

~~~json
{
  "source": "00b4f8f8",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f908`](#insn-00b4f908)

~~~json
{
  "source": "00b4f908",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f91c`](#insn-00b4f91c)

~~~json
{
  "source": "00b4f91c",
  "target": "00b4f938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f924`](#insn-00b4f924)

~~~json
{
  "source": "00b4f924",
  "target": "00b4f93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f934`](#insn-00b4f934)

~~~json
{
  "source": "00b4f934",
  "target": "00b4f93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f94c`](#insn-00b4f94c)

~~~json
{
  "source": "00b4f94c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f954`](#insn-00b4f954)

~~~json
{
  "source": "00b4f954",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f964`](#insn-00b4f964)

~~~json
{
  "source": "00b4f964",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f978`](#insn-00b4f978)

~~~json
{
  "source": "00b4f978",
  "target": "00b4f994",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f980`](#insn-00b4f980)

~~~json
{
  "source": "00b4f980",
  "target": "00b4f998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f990`](#insn-00b4f990)

~~~json
{
  "source": "00b4f990",
  "target": "00b4f998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f9a8`](#insn-00b4f9a8)

~~~json
{
  "source": "00b4f9a8",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f9b0`](#insn-00b4f9b0)

~~~json
{
  "source": "00b4f9b0",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f9c0`](#insn-00b4f9c0)

~~~json
{
  "source": "00b4f9c0",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f9d4`](#insn-00b4f9d4)

~~~json
{
  "source": "00b4f9d4",
  "target": "00b4f9f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f9dc`](#insn-00b4f9dc)

~~~json
{
  "source": "00b4f9dc",
  "target": "00b4f9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f9ec`](#insn-00b4f9ec)

~~~json
{
  "source": "00b4f9ec",
  "target": "00b4f9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fa04`](#insn-00b4fa04)

~~~json
{
  "source": "00b4fa04",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4fa0c`](#insn-00b4fa0c)

~~~json
{
  "source": "00b4fa0c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fa1c`](#insn-00b4fa1c)

~~~json
{
  "source": "00b4fa1c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fa30`](#insn-00b4fa30)

~~~json
{
  "source": "00b4fa30",
  "target": "00b4fa4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fa38`](#insn-00b4fa38)

~~~json
{
  "source": "00b4fa38",
  "target": "00b4fa50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fa48`](#insn-00b4fa48)

~~~json
{
  "source": "00b4fa48",
  "target": "00b4fa50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fa60`](#insn-00b4fa60)

~~~json
{
  "source": "00b4fa60",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4fa68`](#insn-00b4fa68)

~~~json
{
  "source": "00b4fa68",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fa78`](#insn-00b4fa78)

~~~json
{
  "source": "00b4fa78",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fa8c`](#insn-00b4fa8c)

~~~json
{
  "source": "00b4fa8c",
  "target": "00b4faa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fa94`](#insn-00b4fa94)

~~~json
{
  "source": "00b4fa94",
  "target": "00b4faac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4faa4`](#insn-00b4faa4)

~~~json
{
  "source": "00b4faa4",
  "target": "00b4faac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fabc`](#insn-00b4fabc)

~~~json
{
  "source": "00b4fabc",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4fac4`](#insn-00b4fac4)

~~~json
{
  "source": "00b4fac4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fad4`](#insn-00b4fad4)

~~~json
{
  "source": "00b4fad4",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fae8`](#insn-00b4fae8)

~~~json
{
  "source": "00b4fae8",
  "target": "00b4fbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4faf0`](#insn-00b4faf0)

~~~json
{
  "source": "00b4faf0",
  "target": "00b4fbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fafc`](#insn-00b4fafc)

~~~json
{
  "source": "00b4fafc",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb1c`](#insn-00b4fb1c)

~~~json
{
  "source": "00b4fb1c",
  "target": "00b4fb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb2c`](#insn-00b4fb2c)

~~~json
{
  "source": "00b4fb2c",
  "target": "00be0470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fb30`](#insn-00b4fb30)

~~~json
{
  "source": "00b4fb30",
  "target": "00b4fb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb34`](#insn-00b4fb34)

~~~json
{
  "source": "00b4fb34",
  "target": "00b4fb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb44`](#insn-00b4fb44)

~~~json
{
  "source": "00b4fb44",
  "target": "00b4fb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb50`](#insn-00b4fb50)

~~~json
{
  "source": "00b4fb50",
  "target": "00b4fb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb5c`](#insn-00b4fb5c)

~~~json
{
  "source": "00b4fb5c",
  "target": "00b4fb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb64`](#insn-00b4fb64)

~~~json
{
  "source": "00b4fb64",
  "target": "00b4fb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb6c`](#insn-00b4fb6c)

~~~json
{
  "source": "00b4fb6c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fb70`](#insn-00b4fb70)

~~~json
{
  "source": "00b4fb70",
  "target": "00b4fb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb74`](#insn-00b4fb74)

~~~json
{
  "source": "00b4fb74",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb78`](#insn-00b4fb78)

~~~json
{
  "source": "00b4fb78",
  "target": "00b4fbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb7c`](#insn-00b4fb7c)

~~~json
{
  "source": "00b4fb7c",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fb9c`](#insn-00b4fb9c)

~~~json
{
  "source": "00b4fb9c",
  "target": "Stack[-0x218]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fbc8`](#insn-00b4fbc8)

~~~json
{
  "source": "00b4fbc8",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fbd8`](#insn-00b4fbd8)

~~~json
{
  "source": "00b4fbd8",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fbe8`](#insn-00b4fbe8)

~~~json
{
  "source": "00b4fbe8",
  "target": "00b4fb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fbfc`](#insn-00b4fbfc)

~~~json
{
  "source": "00b4fbfc",
  "target": "00b4fc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc04`](#insn-00b4fc04)

~~~json
{
  "source": "00b4fc04",
  "target": "00b4fc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc14`](#insn-00b4fc14)

~~~json
{
  "source": "00b4fc14",
  "target": "00b4fc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc2c`](#insn-00b4fc2c)

~~~json
{
  "source": "00b4fc2c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4fc34`](#insn-00b4fc34)

~~~json
{
  "source": "00b4fc34",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fc44`](#insn-00b4fc44)

~~~json
{
  "source": "00b4fc44",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fc58`](#insn-00b4fc58)

~~~json
{
  "source": "00b4fc58",
  "target": "00b4fd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc60`](#insn-00b4fc60)

~~~json
{
  "source": "00b4fc60",
  "target": "00b4fd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc6c`](#insn-00b4fc6c)

~~~json
{
  "source": "00b4fc6c",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc8c`](#insn-00b4fc8c)

~~~json
{
  "source": "00b4fc8c",
  "target": "00b4fca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fc9c`](#insn-00b4fc9c)

~~~json
{
  "source": "00b4fc9c",
  "target": "00be0470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fca0`](#insn-00b4fca0)

~~~json
{
  "source": "00b4fca0",
  "target": "00b4fce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fca4`](#insn-00b4fca4)

~~~json
{
  "source": "00b4fca4",
  "target": "00b4fce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fcb4`](#insn-00b4fcb4)

~~~json
{
  "source": "00b4fcb4",
  "target": "00b4fce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fcc0`](#insn-00b4fcc0)

~~~json
{
  "source": "00b4fcc0",
  "target": "00b4fcd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fccc`](#insn-00b4fccc)

~~~json
{
  "source": "00b4fccc",
  "target": "00b4fce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fcd4`](#insn-00b4fcd4)

~~~json
{
  "source": "00b4fcd4",
  "target": "00b4fcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fcdc`](#insn-00b4fcdc)

~~~json
{
  "source": "00b4fcdc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fce0`](#insn-00b4fce0)

~~~json
{
  "source": "00b4fce0",
  "target": "00b4fcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fce4`](#insn-00b4fce4)

~~~json
{
  "source": "00b4fce4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fce8`](#insn-00b4fce8)

~~~json
{
  "source": "00b4fce8",
  "target": "00b4fd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fcec`](#insn-00b4fcec)

~~~json
{
  "source": "00b4fcec",
  "target": "Stack[-0x340]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd0c`](#insn-00b4fd0c)

~~~json
{
  "source": "00b4fd0c",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd38`](#insn-00b4fd38)

~~~json
{
  "source": "00b4fd38",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fd48`](#insn-00b4fd48)

~~~json
{
  "source": "00b4fd48",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fd58`](#insn-00b4fd58)

~~~json
{
  "source": "00b4fd58",
  "target": "00b4fd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd6c`](#insn-00b4fd6c)

~~~json
{
  "source": "00b4fd6c",
  "target": "00b4fd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd74`](#insn-00b4fd74)

~~~json
{
  "source": "00b4fd74",
  "target": "00b4fd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd84`](#insn-00b4fd84)

~~~json
{
  "source": "00b4fd84",
  "target": "00b4fd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fd98`](#insn-00b4fd98)

~~~json
{
  "source": "00b4fd98",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4fd9c`](#insn-00b4fd9c)

~~~json
{
  "source": "00b4fd9c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fdb0`](#insn-00b4fdb0)

~~~json
{
  "source": "00b4fdb0",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fdb8`](#insn-00b4fdb8)

~~~json
{
  "source": "00b4fdb8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdbc`](#insn-00b4fdbc)

~~~json
{
  "source": "00b4fdbc",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdc0`](#insn-00b4fdc0)

~~~json
{
  "source": "00b4fdc0",
  "target": "Stack[-0x338]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdd0`](#insn-00b4fdd0)

~~~json
{
  "source": "00b4fdd0",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdd4`](#insn-00b4fdd4)

~~~json
{
  "source": "00b4fdd4",
  "target": "00b4fde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdd8`](#insn-00b4fdd8)

~~~json
{
  "source": "00b4fdd8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fddc`](#insn-00b4fddc)

~~~json
{
  "source": "00b4fddc",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fde0`](#insn-00b4fde0)

~~~json
{
  "source": "00b4fde0",
  "target": "Stack[-0x308]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fde4`](#insn-00b4fde4)

~~~json
{
  "source": "00b4fde4",
  "target": "00b4fdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fde8`](#insn-00b4fde8)

~~~json
{
  "source": "00b4fde8",
  "target": "Stack[-0x2f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fdec`](#insn-00b4fdec)

~~~json
{
  "source": "00b4fdec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fdf4`](#insn-00b4fdf4)

~~~json
{
  "source": "00b4fdf4",
  "target": "00be0260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fdfc`](#insn-00b4fdfc)

~~~json
{
  "source": "00b4fdfc",
  "target": "00be0320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4fe04`](#insn-00b4fe04)

~~~json
{
  "source": "00b4fe04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe0c`](#insn-00b4fe0c)

~~~json
{
  "source": "00b4fe0c",
  "target": "00b4fe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe14`](#insn-00b4fe14)

~~~json
{
  "source": "00b4fe14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe18`](#insn-00b4fe18)

~~~json
{
  "source": "00b4fe18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe1c`](#insn-00b4fe1c)

~~~json
{
  "source": "00b4fe1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe20`](#insn-00b4fe20)

~~~json
{
  "source": "00b4fe20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe24`](#insn-00b4fe24)

~~~json
{
  "source": "00b4fe24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4fe30`](#insn-00b4fe30)

~~~json
{
  "source": "00b4fe30",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
