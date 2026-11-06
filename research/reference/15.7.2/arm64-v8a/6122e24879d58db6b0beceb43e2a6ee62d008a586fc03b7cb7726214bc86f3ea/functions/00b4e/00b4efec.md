# 00b4efec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_text_sha256": "b35b99da3eeb184bccbc25acb65d16970eee4988d50e25cf4819c5b213f05592"
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
