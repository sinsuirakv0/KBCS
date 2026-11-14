# 00bbeadc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "be38e3f143a57876a89ea966a07798c6331dce0bb9a6859ac24faf08d4208d7f"
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
