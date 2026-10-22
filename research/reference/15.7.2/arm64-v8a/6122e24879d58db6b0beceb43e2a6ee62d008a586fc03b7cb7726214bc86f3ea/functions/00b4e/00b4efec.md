# 00b4efec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b4efec.md)

## 関数情報

~~~json
{
  "address": "00b4efec",
  "name": "firebase::messaging::internal::MessageReader::ConsumeMessage",
  "size": 3656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f312b9d4e136077c7f7f0261ce5d1cc286fba597d3746fb13a842386e6c2a56b",
  "source_text_sha256": "f312b9d4e136077c7f7f0261ce5d1cc286fba597d3746fb13a842386e6c2a56b"
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

## 疑似コード 1/2 / UTF-8 24555 bytes

~~~c

/* firebase::messaging::internal::MessageReader::ConsumeMessage(com::google::firebase::messaging::cpp::SerializedMessage
   const*) const */

void __thiscall
firebase::messaging::internal::MessageReader::ConsumeMessage
          (MessageReader *this,SerializedMessage *param_1)

{
  long lVar1;
  long lVar2;
  long lVar3;
  basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *pbVar4;
  SerializedMessage *pSVar5;
  uint uVar6;
  byte bVar7;
  ushort uVar8;
  long lVar9;
  byte *pbVar10;
  byte *pbVar11;
  undefined8 uVar12;
  void *pvVar13;
  byte *pbVar14;
  size_t sVar15;
  undefined8 *puVar16;
  void *__dest;
  __tree_node_base *p_Var17;
  SerializedMessage *pSVar18;
  ulong uVar19;
  long lVar20;
  ulong uVar21;
  ulong uVar22;
  ulong uVar23;
  SerializedMessage *pSVar24;
  byte *pbVar25;
  __tree_node_base *p_Var26;
  SerializedMessage *local_330;
  SerializedMessage *local_328;
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
  __tree_node_base *local_178;
  __tree_node_base *local_170;
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
  lVar9 = tpidr_el0;
  local_78 = *(long *)(lVar9 + 0x28);
  local_178 = (__tree_node_base *)&local_170;
  local_170 = (__tree_node_base *)0x0;
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
  pSVar18 = (SerializedMessage *)0x0;
  if (4 < *(ushort *)(param_1 + -(long)*(int *)param_1)) {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 4);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
                    /* try { // try from 00b4f0c4 to 00c4f0cf has its CatchHandler @ 00b4f224 */
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
                    /* try { // try from 00b4f0d4 to 00c4f0df has its CatchHandler @ 00b4f21c */
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &local_1c0,(char *)pSVar24,sVar15);
                    /* try { // try from 00b4f0f4 to 00c4f0ff has its CatchHandler @ 00b4f208 */
                    /* try { // try from 00b4f100 to 00c4f10b has its CatchHandler @ 00b4f204 */
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 7) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 6);
                    /* try { // try from 00b4f10c to 00c4f117 has its CatchHandler @ 00b4f200 */
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
                    /* try { // try from 00b4f138 to 00c4f143 has its CatchHandler @ 00b4f1fc */
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_1a8,(char *)pSVar24,sVar15);
  uVar19 = (ulong)*(int *)param_1;
                    /* try { // try from 00b4f154 to 00c4f173 has its CatchHandler @ 00b4f2f8 */
  lVar20 = -uVar19;
                    /* try { // try from 00b4f174 to 00c4f1bf has its CatchHandler @ 00b4f430 */
  if ((((10 < *(ushort *)(param_1 + -uVar19)) &&
       (uVar21 = (ulong)*(ushort *)(param_1 + -uVar19 + 10), uVar21 != 0)) &&
      (pSVar18 = param_1 + uVar21, pSVar18 + *(uint *)pSVar18 != (SerializedMessage *)0x0)) &&
     (uVar6 = *(uint *)(pSVar18 + *(uint *)pSVar18), uVar6 != 0)) {
    lVar20 = 0;
    do {
      uVar19 = (ulong)*(ushort *)(param_1 + (10 - (long)(int)uVar19));
      uVar21 = (ulong)*(uint *)(param_1 + uVar19);
                    /* try { // try from 00b4f1c0 to 00c4f437 has its CatchHandler @ 00b4ec40 */
      uVar22 = (ulong)*(uint *)(param_1 + lVar20 + uVar19 + uVar21 + 4);
      lVar1 = uVar19 + uVar21 + uVar22;
      lVar2 = lVar20 + (lVar1 - *(int *)(param_1 + lVar20 + lVar1 + 4));
      if (*(ushort *)(param_1 + lVar2 + 4) < 5) {
        pSVar18 = (SerializedMessage *)0x0;
                    /* catch() { ... } // from try @ 00b4f00c with catch @ 00b4f27c */
        pSVar24 = (SerializedMessage *)&DAT_002967d9;
                    /* catch() { ... } // from try @ 00b4efe8 with catch @ 00b4f280 */
      }
      else {
        pSVar18 = (SerializedMessage *)0x0;
        if ((ulong)*(ushort *)(param_1 + lVar2 + 8) != 0) {
                    /* catch() { ... } // from try @ 00b4f138 with catch @ 00b4f1fc */
                    /* catch() { ... } // from try @ 00b4f10c with catch @ 00b4f200 */
                    /* catch() { ... } // from try @ 00b4f100 with catch @ 00b4f204 */
          lVar3 = uVar19 + uVar21 + uVar22 + (ulong)*(ushort *)(param_1 + lVar2 + 8);
                    /* catch() { ... } // from try @ 00b4f0f4 with catch @ 00b4f208 */
                    /* catch() { ... } // from try @ 00b4f0d4 with catch @ 00b4f21c */
          pSVar18 = param_1 + lVar20 + lVar3 + (ulong)*(uint *)(param_1 + lVar20 + lVar3 + 4) + 4;
        }
                    /* catch() { ... } // from try @ 00b4f0c4 with catch @ 00b4f224 */
                    /* catch() { ... } // from try @ 00b4f0a0 with catch @ 00b4f228 */
        pSVar24 = (SerializedMessage *)&DAT_002967d9;
        if (pSVar18 != (SerializedMessage *)0x0) {
          pSVar24 = pSVar18 + 4;
        }
                    /* catch() { ... } // from try @ 00b4f078 with catch @ 00b4f234 */
        if (6 < *(ushort *)(param_1 + lVar2 + 4)) {
          lVar2 = uVar19 + uVar21 + uVar22;
                    /* catch() { ... } // from try @ 00b4f054 with catch @ 00b4f24c */
          if ((ulong)*(ushort *)
                      (param_1 + lVar20 + (lVar2 - *(int *)(param_1 + lVar20 + lVar1 + 4)) + 10) !=
              0) {
            lVar2 = lVar2 + (ulong)*(ushort *)
                                    (param_1 +
                                    lVar20 + (lVar2 - *(int *)(param_1 + lVar20 + lVar1 + 4)) + 10);
                    /* catch() { ... } // from try @ 00b4f03c with catch @ 00b4f264 */
            pSVar18 = param_1 + lVar20 + lVar2 + (ulong)*(uint *)(param_1 + lVar20 + lVar2 + 4) + 4;
            goto LAB_00b4f288;
          }
        }
        pSVar18 = (SerializedMessage *)0x0;
      }
LAB_00b4f288:
                    /* catch() { ... } // from try @ 00b4efc0 with catch @ 00b4f28c */
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar18 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar18 + 4;
      }
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      basic_string<decltype(nullptr)>
                ((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
                 &local_320,(char *)pSVar24);
      puVar16 = (undefined8 *)FUN_0044a6d0(&local_178,&local_80,&local_320);
      p_Var26 = (__tree_node_base *)*puVar16;
      if (p_Var26 == (__tree_node_base *)0x0) {
        p_Var26 = operator_new(0x50);
        pvVar13 = local_310;
        uVar12 = uStack_318;
        uVar19 = local_320;
        uStack_318 = 0;
        local_310 = (void *)0x0;
        local_320 = 0;
        *(undefined8 *)(p_Var26 + 0x40) = 0;
        *(undefined8 *)(p_Var26 + 0x48) = 0;
                    /* catch() { ... } // from try @ 00b4ef9c with catch @ 00b4f2d8 */
        *(undefined8 *)p_Var26 = 0;
        *(undefined8 *)(p_Var26 + 8) = 0;
        *(undefined8 *)(p_Var26 + 0x28) = uVar12;
        *(ulong *)(p_Var26 + 0x20) = uVar19;
        *(void **)(p_Var26 + 0x30) = pvVar13;
        *(undefined8 *)(p_Var26 + 0x38) = 0;
        *(undefined8 *)(p_Var26 + 0x10) = local_80;
                    /* catch() { ... } // from try @ 00b4ef90 with catch @ 00b4f2e8 */
        *puVar16 = p_Var26;
                    /* catch() { ... } // from try @ 00b4ef7c with catch @ 00b4f2f0 */
                    /* catch() { ... } // from try @ 00b4ef58 with catch @ 00b4f2f4 */
                    /* catch() { ... } // from try @ 00b4f154 with catch @ 00b4f2f8 */
        p_Var17 = p_Var26;
        if (*(__tree_node_base **)local_178 != (__tree_node_base *)0x0) {
                    /* catch() { ... } // from try @ 00b4ee80 with catch @ 00b4f2fc */
                    /* catch() { ... } // from try @ 00b4ee74 with catch @ 00b4f300 */
          p_Var17 = (__tree_node_base *)*puVar16;
          local_178 = *(__tree_node_base **)local_178;
                    /* catch() { ... } // from try @ 00b4ee68 with catch @ 00b4f304 */
        }
        std::__ndk1::__tree_balance_after_insert<std::__ndk1::__tree_node_base<void*>*>
                  (local_170,p_Var17);
        local_168 = local_168 + 1;
                    /* catch() { ... } // from try @ 00b4ee3c with catch @ 00b4f31c */
      }
                    /* catch() { ... } // from try @ 00b4ee2c with catch @ 00b4f324 */
                    /* catch() { ... } // from try @ 00b4ee08 with catch @ 00b4f328 */
      sVar15 = strlen((char *)pSVar5);
                    /* catch() { ... } // from try @ 00b4eddc with catch @ 00b4f334 */
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             (p_Var26 + 0x38),(char *)pSVar5,sVar15);
      if ((local_320 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4edbc with catch @ 00b4f348 */
        operator_delete(local_310);
      }
      uVar19 = (ulong)*(uint *)param_1;
      lVar20 = lVar20 + 4;
    } while ((ulong)uVar6 * 4 - lVar20 != 0);
                    /* catch() { ... } // from try @ 00b4edac with catch @ 00b4f350 */
                    /* catch() { ... } // from try @ 00b4ed88 with catch @ 00b4f354 */
    lVar20 = -(long)(int)*(uint *)param_1;
  }
  lVar1 = lStack_158;
  pvVar13 = local_160;
                    /* catch() { ... } // from try @ 00b4ed60 with catch @ 00b4f360 */
  if (((0xc < *(ushort *)(param_1 + lVar20)) &&
      (uVar19 = (ulong)*(ushort *)(param_1 + lVar20 + 0xc), uVar19 != 0)) &&
     (pSVar18 = param_1 + uVar19, pSVar18 + *(uint *)pSVar18 != (SerializedMessage *)0x0)) {
                    /* catch() { ... } // from try @ 00b4ed3c with catch @ 00b4f388 */
    uVar19 = (ulong)*(uint *)(pSVar18 + *(uint *)pSVar18);
                    /* catch() { ... } // from try @ 00b4ed30 with catch @ 00b4f398 */
    if ((ulong)(local_150 - (long)local_160) < uVar19) {
      __dest = operator_new(uVar19);
      sVar15 = lVar1 - (long)pvVar13;
                    /* catch() { ... } // from try @ 00b4ed1c with catch @ 00b4f3b8 */
                    /* catch() { ... } // from try @ 00b4ecf8 with catch @ 00b4f3bc */
      if (0 < (long)sVar15) {
        memcpy(__dest,pvVar13,sVar15);
      }
                    /* catch() { ... } // from try @ 00b4ee9c with catch @ 00b4f3cc */
      local_160 = __dest;
      lStack_158 = (long)__dest + sVar15;
      local_150 = (long)__dest + uVar19;
      if (pvVar13 != (void *)0x0) {
        operator_delete(pvVar13);
      }
    }
    local_330 = param_1 + *(ushort *)(param_1 + (0xc - (long)*(int *)param_1)) +
                *(uint *)(param_1 + *(ushort *)(param_1 + (0xc - (long)*(int *)param_1)));
    local_328 = (SerializedMessage *)0x0;
    if (*(ushort *)(param_1 + (0xc - (long)*(int *)param_1)) != 0) {
      local_328 = local_330;
    }
    local_328 = local_328 + 4;
    local_330 = local_330 + (ulong)*(uint *)local_330 + 4;
    std::__ndk1::vector<unsigned_char,std::__ndk1::allocator<unsigned_char>>::
    assign<flatbuffers::VectorIterator<unsigned_char,unsigned_char>>
              ((vector<unsigned_char,std::__ndk1::allocator<unsigned_char>> *)&local_160,&local_328,
               &local_330);
    lVar20 = -(long)*(int *)param_1;
  }
                    /* catch() { ... } // from try @ 00b4f174 with catch @ 00b4f430 */
                    /* catch() { ... } // from try @ 00b4eeb8 with catch @ 00b4f434 */
                    /* try { // try from 00b4f438 to 00c4f49f has its CatchHandler @ 00b4f438
                       catch() { ... } // from try @ 00b4f438 with catch @ 00b4f438
                       catch() { ... } // from try @ 00b4fb2c with catch @ 00b4f438 */
  if (*(ushort *)(param_1 + lVar20) < 0xf) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + lVar20 + 0xe);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_148,(char *)pSVar24,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 0x11) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 0x10);
                    /* try { // try from 00b4f4a0 to 00c4f4ab has its CatchHandler @ 00b4fc64 */
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
                    /* try { // try from 00b4f4b8 to 00c4f4bf has its CatchHandler @ 00b4fc5c */
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_130,(char *)pSVar24,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 0x17) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 0x16);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
                    /* try { // try from 00b4f504 to 00c4f50f has its CatchHandler @ 00b4fc38 */
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
                    /* try { // try from 00b4f510 to 00c4f51f has its CatchHandler @ 00b4fc04 */
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)&local_f8
         ,(char *)pSVar24,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 0x19) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
                    /* try { // try from 00b4f550 to 00c4f563 has its CatchHandler @ 00b4fc6c */
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 0x18);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
                    /* try { // try from 00b4f57c to 00c4f583 has its CatchHandler @ 00b4fca4 */
  sVar15 = strlen((char *)pSVar24);
                    /* try { // try from 00b4f588 to 00c4f597 has its CatchHandler @ 00b4fca0 */
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_e0,(char *)pSVar24,sVar15);
                    /* try { // try from 00b4f598 to 00c4f5a7 has its CatchHandler @ 00b4fc90 */
  pSVar18 = param_1 + -(long)*(int *)param_1;
  if (*(ushort *)pSVar18 < 0x1d) {
    pSVar24 = (SerializedMessage *)0x0;
    local_c0 = false;
  }
  else {
    local_c0 = false;
    if ((ulong)*(ushort *)(pSVar18 + 0x1c) != 0) {
      local_c0 = param_1[*(ushort *)(pSVar18 + 0x1c)] != (SerializedMessage)0x0;
    }
    if (*(ushort *)pSVar18 < 0x1f) {
      pSVar24 = (SerializedMessage *)0x0;
    }
    else {
      pSVar24 = (SerializedMessage *)0x0;
      if ((ulong)*(ushort *)(pSVar18 + 0x1e) != 0) {
        pSVar24 = param_1 + *(ushort *)(pSVar18 + 0x1e) +
                  *(uint *)(param_1 + *(ushort *)(pSVar18 + 0x1e));
      }
    }
  }
  pSVar18 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar24 != (SerializedMessage *)0x0) {
    pSVar18 = pSVar24 + 4;
  }
  sVar15 = strlen((char *)pSVar18);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)&local_b8
         ,(char *)pSVar18,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 9) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 8);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_190,(char *)pSVar24,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 0x13) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 0x12);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
                    /* try { // try from 00b4f698 to 00c4f6a3 has its CatchHandler @ 00b4fc70 */
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_118,(char *)pSVar24,sVar15);
  if (*(ushort *)(param_1 + -(long)*(int *)param_1) < 0x23) {
    pSVar18 = (SerializedMessage *)0x0;
  }
  else {
    uVar19 = (ulong)*(ushort *)(param_1 + -(long)*(int *)param_1 + 0x22);
    pSVar18 = (SerializedMessage *)0x0;
    if (uVar19 != 0) {
      pSVar18 = param_1 + uVar19 + *(uint *)(param_1 + uVar19);
    }
  }
  pSVar24 = (SerializedMessage *)&DAT_002967d9;
  if (pSVar18 != (SerializedMessage *)0x0) {
    pSVar24 = pSVar18 + 4;
  }
  sVar15 = strlen((char *)pSVar24);
  std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
         &uStack_a0,(char *)pSVar24,sVar15);
  pSVar18 = param_1 + -(long)*(int *)param_1;
  uVar8 = *(ushort *)pSVar18;
  if (uVar8 < 0x21) {
    local_88 = 0;
    if (uVar8 < 0x15) {
      local_100 = 0;
      goto LAB_00b4fdc0;
    }
    uVar19 = (ulong)*(ushort *)(pSVar18 + 0x14);
    local_100 = 0;
    if (uVar19 != 0) goto LAB_00b4f770;
  }
  else {
    local_88 = 0;
    if ((ulong)*(ushort *)(pSVar18 + 0x20) != 0) {
      local_88 = *(undefined8 *)(param_1 + *(ushort *)(pSVar18 + 0x20));
    }
    uVar19 = (ulong)*(ushort *)(pSVar18 + 0x14);
    if (uVar19 == 0) {
      local_100 = 0;
    }
    else {
LAB_00b4f770:
      local_100 = *(undefined4 *)(param_1 + uVar19);
    }
  }
                    /* try { // try from 00b4f784 to 00c4f78b has its CatchHandler @ 00b4fc6c */
~~~
## 疑似コード 2/2 / UTF-8 17595 bytes

~~~c
  if ((0x1a < uVar8) && (uVar19 = (ulong)*(ushort *)(pSVar18 + 0x1a), uVar19 != 0)) {
    uVar21 = (ulong)*(uint *)(param_1 + uVar19);
    pSVar18 = param_1 + uVar19 + uVar21;
    if (pSVar18 != (SerializedMessage *)0x0) {
                    /* try { // try from 00b4f7a0 to 00c4f7a7 has its CatchHandler @ 00b4fc00 */
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 5) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 4);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &local_2f0,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 7) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 6);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_2d8,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 9) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 8);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
                    /* try { // try from 00b4f878 to 00c4f87f has its CatchHandler @ 00b4fbc8 */
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_2c0,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0xb) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 10);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_2a8,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0xd) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0xc);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
                    /* try { // try from 00b4f948 to 00c4f953 has its CatchHandler @ 00b4fcac */
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &local_290,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0xf) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0xe);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
                    /* try { // try from 00b4f9a0 to 00c4f9a7 has its CatchHandler @ 00b4fbb8 */
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
                    /* try { // try from 00b4f9b8 to 00c4f9bf has its CatchHandler @ 00b4fba8 */
                    /* try { // try from 00b4f9c0 to 00c4f9cb has its CatchHandler @ 00b4fbcc */
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_278,(char *)pSVar5,sVar15);
                    /* try { // try from 00b4f9cc to 00c4f9e3 has its CatchHandler @ 00b4fb6c */
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0x11) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x10);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_260,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0x13) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x12);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_248,(char *)pSVar5,sVar15);
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0x15) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x14);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &local_230,(char *)pSVar5,sVar15);
      if ((0x16 < *(ushort *)(pSVar18 + -(long)*(int *)pSVar18)) &&
         (uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x16), uVar22 != 0)) {
        uVar6 = *(uint *)(pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22));
        uVar23 = (ulong)uVar6;
        lVar20 = (long)local_210 - local_218 >> 3;
        uVar22 = lVar20 * -0x5555555555555555;
        if (uVar22 < uVar23) {
                    /* try { // try from 00b4fb24 to 00c4fb2b has its CatchHandler @ 00b4fcac */
                    /* try { // try from 00b4fb2c to 00c4fd13 has its CatchHandler @ 00b4f438 */
          std::__ndk1::
          vector<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::allocator<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>>
          ::__append((vector<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::allocator<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>>
                      *)&local_218,uVar23 + lVar20 * 0x5555555555555555);
          pbVar25 = local_210;
        }
        else {
          pbVar25 = local_210;
          if ((uVar22 - uVar23 != 0) &&
             (pbVar25 = (byte *)(local_218 + uVar23 * 0x18), pbVar25 != local_210)) {
            bVar7 = local_210[-0x18];
            pbVar14 = local_210 + -0x18;
            pbVar11 = local_210;
            while( true ) {
              pbVar10 = pbVar14;
              if ((bVar7 & 1) != 0) {
                    /* catch() { ... } // from try @ 00b4f9cc with catch @ 00b4fb6c */
                operator_delete(*(void **)(pbVar11 + -8));
              }
              if (pbVar25 == pbVar10) break;
              bVar7 = pbVar10[-0x18];
              pbVar14 = pbVar10 + -0x18;
              pbVar11 = pbVar10;
            }
          }
        }
        local_210 = pbVar25;
        if (uVar6 != 0) {
          lVar20 = 0;
          pSVar24 = param_1 + uVar21 + uVar19;
          do {
            pSVar24 = pSVar24 + 4;
                    /* catch() { ... } // from try @ 00b4f9b8 with catch @ 00b4fba8 */
            pbVar4 = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
                      *)(local_218 + lVar20);
            lVar1 = (ulong)*(ushort *)(pSVar18 + (0x16 - (long)*(int *)pSVar18)) +
                    (ulong)*(uint *)(pSVar18 + *(ushort *)(pSVar18 + (0x16 - (long)*(int *)pSVar18))
                                    );
            uVar6 = *(uint *)(pSVar24 + lVar1);
                    /* catch() { ... } // from try @ 00b4f9a0 with catch @ 00b4fbb8 */
                    /* catch() { ... } // from try @ 00b4f878 with catch @ 00b4fbc8 */
            sVar15 = strlen((char *)(pSVar24 + lVar1 + (ulong)uVar6 + 4));
                    /* catch() { ... } // from try @ 00b4f9c0 with catch @ 00b4fbcc */
            std::__ndk1::
            basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::assign
                      (pbVar4,(char *)(pSVar24 + lVar1 + (ulong)uVar6 + 4),sVar15);
            lVar20 = lVar20 + 0x18;
          } while (uVar23 * 0x18 - lVar20 != 0);
        }
      }
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0x19) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
                    /* catch() { ... } // from try @ 00b4f7a0 with catch @ 00b4fc00 */
        uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x18);
                    /* catch() { ... } // from try @ 00b4f510 with catch @ 00b4fc04 */
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar22 != 0) {
          pSVar24 = pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22);
        }
      }
      pSVar5 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar5 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar5);
                    /* catch() { ... } // from try @ 00b4f504 with catch @ 00b4fc38 */
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &uStack_200,(char *)pSVar5,sVar15);
                    /* catch() { ... } // from try @ 00b4f4b8 with catch @ 00b4fc5c */
      if ((0x1a < *(ushort *)(pSVar18 + -(long)*(int *)pSVar18)) &&
         (uVar22 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x1a), uVar22 != 0)) {
                    /* catch() { ... } // from try @ 00b4f4a0 with catch @ 00b4fc64 */
                    /* catch() { ... } // from try @ 00b4f550 with catch @ 00b4fc6c
                       catch() { ... } // from try @ 00b4f784 with catch @ 00b4fc6c */
                    /* catch() { ... } // from try @ 00b4f698 with catch @ 00b4fc70 */
        uVar6 = *(uint *)(pSVar18 + uVar22 + *(uint *)(pSVar18 + uVar22));
        uVar23 = (ulong)uVar6;
        lVar20 = (long)local_1e0 - lStack_1e8 >> 3;
        uVar22 = lVar20 * -0x5555555555555555;
        if (uVar22 < uVar23) {
                    /* catch() { ... } // from try @ 00b4f598 with catch @ 00b4fc90 */
          std::__ndk1::
          vector<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::allocator<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>>
          ::__append((vector<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::allocator<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>>
                      *)&lStack_1e8,uVar23 + lVar20 * 0x5555555555555555);
          pbVar25 = local_1e0;
                    /* catch() { ... } // from try @ 00b4f588 with catch @ 00b4fca0 */
        }
        else {
          pbVar25 = local_1e0;
                    /* catch() { ... } // from try @ 00b4f57c with catch @ 00b4fca4 */
                    /* catch() { ... } // from try @ 00b4f948 with catch @ 00b4fcac
                       catch() { ... } // from try @ 00b4fb24 with catch @ 00b4fcac */
          if ((uVar22 - uVar23 != 0) &&
             (pbVar25 = (byte *)(lStack_1e8 + uVar23 * 0x18), pbVar25 != local_1e0)) {
            bVar7 = local_1e0[-0x18];
            pbVar14 = local_1e0 + -0x18;
            pbVar11 = local_1e0;
            while( true ) {
              pbVar10 = pbVar14;
              if ((bVar7 & 1) != 0) {
                operator_delete(*(void **)(pbVar11 + -8));
              }
              if (pbVar25 == pbVar10) break;
              bVar7 = pbVar10[-0x18];
              pbVar14 = pbVar10 + -0x18;
              pbVar11 = pbVar10;
            }
          }
        }
        local_1e0 = pbVar25;
        if (uVar6 != 0) {
          lVar20 = 0;
          pSVar24 = param_1 + uVar21 + uVar19;
          do {
            pSVar24 = pSVar24 + 4;
            pbVar4 = (basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>
                      *)(lStack_1e8 + lVar20);
            lVar1 = (ulong)*(ushort *)(pSVar18 + (0x1a - (long)*(int *)pSVar18)) +
                    (ulong)*(uint *)(pSVar18 + *(ushort *)(pSVar18 + (0x1a - (long)*(int *)pSVar18))
                                    );
            uVar6 = *(uint *)(pSVar24 + lVar1);
            sVar15 = strlen((char *)(pSVar24 + lVar1 + (ulong)uVar6 + 4));
            std::__ndk1::
            basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::assign
                      (pbVar4,(char *)(pSVar24 + lVar1 + (ulong)uVar6 + 4),sVar15);
            lVar20 = lVar20 + 0x18;
          } while (uVar23 * 0x18 - lVar20 != 0);
        }
      }
      if (*(ushort *)(pSVar18 + -(long)*(int *)pSVar18) < 0x1d) {
        pSVar24 = (SerializedMessage *)0x0;
      }
      else {
        uVar19 = (ulong)*(ushort *)(pSVar18 + -(long)*(int *)pSVar18 + 0x1c);
        pSVar24 = (SerializedMessage *)0x0;
        if (uVar19 != 0) {
          pSVar24 = pSVar18 + uVar19 + *(uint *)(pSVar18 + uVar19);
        }
      }
      pSVar18 = (SerializedMessage *)&DAT_002967d9;
      if (pSVar24 != (SerializedMessage *)0x0) {
        pSVar18 = pSVar24 + 4;
      }
      sVar15 = strlen((char *)pSVar18);
      std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
      assign((basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>> *)
             &local_308,(char *)pSVar18,sVar15);
      local_c8 = SUB81(&local_2f0,0);
      uStack_c7 = (undefined7)((ulong)&local_2f0 >> 8);
      local_1d0 = &local_308;
    }
  }
LAB_00b4fdc0:
  (**(code **)this)(&local_1c0,*(undefined8 *)(this + 8));
  if (CONCAT71(uStack_c7,local_c8) != 0) {
    *(undefined8 *)(CONCAT71(uStack_c7,local_c8) + 0x120) = 0;
    local_c8 = 0;
    uStack_c7 = 0;
  }
  if ((local_308 & 1) != 0) {
    operator_delete(local_2f8);
  }
  Notification::~Notification((Notification *)&local_2f0);
  Message::~Message((Message *)&local_1c0);
  if (*(long *)(lVar9 + 0x28) == local_78) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
