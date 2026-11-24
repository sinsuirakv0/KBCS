# 00bbaaa4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb9ab0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-2153be00d6d6c304b1a957aaf0efba9a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaaa4",
  "name": "_ZN8firebase9messaging15ProcessMessagesEv",
  "size": 2800,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0db4de9f59bfaf291ebcee4a2c21ea2a636f1dc526e256ae6a2f90451f44cc0",
  "source_text_sha256": "c0db4de9f59bfaf291ebcee4a2c21ea2a636f1dc526e256ae6a2f90451f44cc0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaaa4",
        "00bbb593"
      ]
    ],
    "bytes_sha256": "f46104d53aaab2ce4db22dfbc907c29c15b590bb20c09932dba291cd916a4137",
    "instruction_count": 700,
    "instruction_bytes": 2800,
    "body_bytes": 2800,
    "indirect": 21,
    "unresolved": 21
  }
}
~~~

## 呼び出し元

- [00c5e640](../00c5e/00c5e640.md)

## 呼び出し先

- [0046d908](../0046d/0046d908.md)
- [00497b94](../00497/00497b94.md)
- [00497da8](../00497/00497da8.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5b0a0](../00c5b/00c5b0a0.md)
- [00c5b0f0](../00c5b/00c5b0f0.md)
- [00c5b100](../00c5b/00c5b100.md)
- [00c5b120](../00c5b/00c5b120.md)
- [00c5b130](../00c5b/00c5b130.md)
- [00c5b300](../00c5b/00c5b300.md)
- [00c5b310](../00c5b/00c5b310.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c030](../00c5c/00c5c030.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c390](../00c5c/00c5c390.md)
- [00c5c430](../00c5c/00c5c430.md)
- [00c5c5a0](../00c5c/00c5c5a0.md)
- [00c5c5d0](../00c5c/00c5c5d0.md)
- [00c5c5f0](../00c5c/00c5c5f0.md)
- [00c5c600](../00c5c/00c5c600.md)
- [00c5c660](../00c5c/00c5c660.md)
- [00c5c680](../00c5c/00c5c680.md)
- [00c5c8f0](../00c5c/00c5c8f0.md)
- [00c5cce0](../00c5c/00c5cce0.md)
- [00c5cf10](../00c5c/00c5cf10.md)
- [00c5e1d0](../00c5e/00c5e1d0.md)
- [00c5e340](../00c5e/00c5e340.md)
- [00c5e440](../00c5e/00c5e440.md)
- [00c5e490](../00c5e/00c5e490.md)
- [00c5e5f0](../00c5e/00c5e5f0.md)
- [00c5e620](../00c5e/00c5e620.md)

## 関連文字列（未確認候補）

~~~text
"LoadFile(g_local_storage_file_path->c_str(), &buffer)"
"collapse_key"
"from"
"gcm."
"google."
"google.message_id"
"google.to"
"message_id"
"message_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 20752 bytes

~~~c

void _ZN8firebase9messaging15ProcessMessagesEv(void)

{
  bool bVar1;
  code *pcVar2;
  long lVar3;
  code *__ptr;
  void *pvVar4;
  char cVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  long *plVar9;
  ulong uVar10;
  undefined8 uVar11;
  long lVar12;
  long lVar13;
  undefined8 uVar14;
  char *__s1;
  size_t sVar15;
  undefined8 uVar16;
  undefined8 *puVar17;
  FILE *pFVar18;
  byte *pbVar19;
  undefined8 *puVar20;
  byte *pbVar21;
  undefined8 uVar22;
  undefined8 *puVar23;
  code *local_1f0;
  code *pcStack_1e8;
  code *local_1e0;
  code *local_1d8;
  code *pcStack_1d0;
  code *pcStack_1c8;
  code *local_1c0;
  code *pcStack_1b8;
  code *local_1b0;
  undefined8 *local_1a8;
  undefined8 local_1a0;
  long local_198;
  undefined8 local_190;
  undefined8 uStack_188;
  undefined8 uStack_180;
  code *local_178;
  code *pcStack_170;
  code *pcStack_168;
  code *local_160;
  code *pcStack_158;
  code *local_150;
  undefined8 uStack_148;
  undefined8 uStack_140;
  undefined8 uStack_138;
  undefined4 local_130;
  undefined8 local_128;
  undefined8 uStack_120;
  undefined8 local_118;
  undefined8 uStack_110;
  undefined8 local_108;
  undefined1 uStack_100;
  undefined7 uStack_ff;
  undefined1 uStack_f8;
  undefined8 uStack_f7;
  code *local_e8;
  code *pcStack_e0;
  code *local_d8;
  undefined8 uStack_d0;
  undefined8 uStack_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  ulong local_b0;
  undefined8 uStack_a8;
  void *local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  code *pcStack_88;
  code *local_80;
  long local_78;
  
  lVar3 = tpidr_el0;
  local_78 = *(long *)(lVar3 + 0x28);
  _ZN8firebase5Mutex7AcquireEv(&DAT_01127318);
  if (DAT_01127420 == (undefined8 *)0x0) {
    plVar9 = (long *)0x0;
  }
  else {
    plVar9 = (long *)_ZNK8firebase3App9GetJNIEnvEv();
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01127318);
  uVar10 = _ZN8firebase9messaging11HasListenerEv();
  if ((plVar9 == (long *)0x0) || ((uVar10 & 1) == 0)) goto LAB_00bbb560;
  uVar22 = 0x1127000;
  if (((DAT_01127448 & 1) == 0) &&
     (uVar10 = _ZN8firebase9messaging11HasListenerEv(), (uVar10 & 1) != 0)) {
                    /* try { // try from 00bbab30 to 00cbab37 has its CatchHandler @ 00bbaba0 */
    DAT_01127448 = 1;
    _ZN8firebase5Mutex7AcquireEv(&DAT_01127318);
                    /* try { // try from 00bbab38 to 00cbab97 has its CatchHandler @ 00bbaa94 */
    bVar1 = DAT_01127420 != (undefined8 *)0x0;
    if (bVar1) {
      uVar22 = (**(code **)(*plVar9 + 200))(plVar9,*DAT_01127420);
    }
    _ZN8firebase5Mutex7ReleaseEv(&DAT_01127318);
    if (bVar1) {
      uVar11 = _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE(3);
      lVar12 = FUN_00497b94(plVar9,uVar22,uVar11);
                    /* try { // try from 00bbab98 to 00cbab9f has its CatchHandler @ 00bbaba4 */
                    /* catch() { ... } // from try @ 00bbab30 with catch @ 00bbaba0
                       try { // try from 00bbaba0 to 00cbabdb has its CatchHandler @ 00bbaa94 */
      (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
                    /* catch() { ... } // from try @ 00bbab98 with catch @ 00bbaba4 */
      if (lVar12 != 0) {
        uVar22 = _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE(2);
        lVar13 = FUN_00497b94(plVar9,lVar12,uVar22);
        if (lVar13 != 0) {
          local_1a8 = &local_1a0;
                    /* catch() { ... } // from try @ 00bbadb8 with catch @ 00bbabdc */
          local_1a0 = 0;
          local_198 = 0;
          local_130 = 0;
          pcStack_1e8 = (code *)0x0;
          local_1f0 = (code *)0x0;
          local_1d8 = (code *)0x0;
          local_1e0 = (code *)0x0;
          pcStack_1c8 = (code *)0x0;
          pcStack_1d0 = (code *)0x0;
          pcStack_1b8 = (code *)0x0;
          local_1c0 = (code *)0x0;
          uStack_188 = 0;
          local_190 = 0;
          local_178 = (code *)0x0;
          uStack_180 = 0;
          pcStack_168 = (code *)0x0;
          pcStack_170 = (code *)0x0;
          pcStack_158 = (code *)0x0;
          local_160 = (code *)0x0;
          uStack_148 = 0;
          local_150 = (code *)0x0;
          uStack_138 = 0;
          uStack_140 = 0;
          local_1b0 = (code *)0x0;
          uStack_120 = 0;
          local_128 = 0;
          uStack_110 = 0;
          local_118 = 0;
          uStack_100 = 0;
          local_108 = 0;
          uStack_f7 = 0;
          uStack_ff = 0;
          uStack_f8 = 0;
          local_b8 = 0;
          uStack_d0 = 0;
          local_d8 = (code *)0x0;
          uStack_c0 = 0;
          uStack_c8 = 0;
          pcStack_e0 = (code *)0x0;
          local_e8 = (code *)0x0;
          uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,"google.message_id");
          uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
          uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
          (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
          if (((ulong)local_178 & 1) != 0) {
            *pcStack_168 = (code)0x0;
            pcStack_170 = (code *)0x0;
            if (((ulong)local_178 & 1) != 0) {
              _ZdlPv(pcStack_168);
            }
          }
          pcStack_168 = local_80;
          pcStack_170 = pcStack_88;
          local_178 = local_90;
          pcVar2 = (code *)((ulong)local_90 >> 1 & 0x7f);
          if (((ulong)local_90 & 1) != 0) {
            pcVar2 = pcStack_88;
          }
          if (pcVar2 == (code *)0x0) {
            uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,"message_id");
            uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
            uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
                    /* try { // try from 00bbad30 to 00cbadb7 has its CatchHandler @ 00bbae9c */
            (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
            if (((ulong)local_178 & 1) != 0) {
              *pcStack_168 = (code)0x0;
              pcStack_170 = (code *)0x0;
              if (((ulong)local_178 & 1) != 0) {
                _ZdlPv(pcStack_168);
              }
            }
          }
          local_178 = local_90;
          pcStack_170 = pcStack_88;
          uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,&DAT_0030e8ea);
          uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
          uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
                    /* try { // try from 00bbadb8 to 00cbaf6b has its CatchHandler @ 00bbabdc */
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
          (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
          if (((ulong)local_1f0 & 1) != 0) {
            *local_1e0 = (code)0x0;
            pcStack_1e8 = (code *)0x0;
            if (((ulong)local_1f0 & 1) != 0) {
              _ZdlPv(local_1e0);
            }
          }
          pcVar2 = (code *)((ulong)local_178 >> 1 & 0x7f);
          if (((ulong)local_178 & 1) != 0) {
            pcVar2 = pcStack_170;
          }
          pcStack_1e8 = pcStack_88;
          local_1f0 = local_90;
          local_1e0 = local_80;
          if (pcVar2 != (code *)0x0) {
            pcVar2 = (code *)((ulong)local_90 >> 1 & 0x7f);
            if (((ulong)local_90 & 1) != 0) {
              pcVar2 = pcStack_88;
            }
            if (pcVar2 != (code *)0x0) {
              uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,"google.to");
              uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
              uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
              _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
                    /* catch() { ... } // from try @ 00bbad30 with catch @ 00bbae9c */
              (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
              if (((ulong)local_1d8 & 1) != 0) {
                *pcStack_1c8 = (code)0x0;
                pcStack_1d0 = (code *)0x0;
                if (((ulong)local_1d8 & 1) != 0) {
                  _ZdlPv(pcStack_1c8);
                }
              }
              pcStack_1c8 = local_80;
              pcStack_1d0 = pcStack_88;
              local_1d8 = local_90;
              uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,"message_type");
              uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
              uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
              _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
              (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
              if (((ulong)local_160 & 1) != 0) {
                *local_150 = (code)0x0;
                pcStack_158 = (code *)0x0;
                if (((ulong)local_160 & 1) != 0) {
                  _ZdlPv(local_150);
                }
              }
                    /* try { // try from 00bbaf80 to 00cbafeb has its CatchHandler @ 00bbaf80
                       catch() { ... } // from try @ 00bbaf80 with catch @ 00bbaf80
                       catch() { ... } // from try @ 00bbb03c with catch @ 00bbaf80
                       catch() { ... } // from try @ 00bbb40c with catch @ 00bbaf80 */
              local_150 = local_80;
              pcStack_158 = pcStack_88;
              local_160 = local_90;
              uVar22 = (**(code **)(*plVar9 + 0x538))(plVar9,"collapse_key");
              uVar11 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
              uVar11 = FUN_00497b94(plVar9,lVar13,uVar11,uVar22);
              _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar11);
              (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
                    /* try { // try from 00bbafec to 00cbafff has its CatchHandler @ 00bbb58c */
              if (((ulong)local_1c0 & 1) != 0) {
                *local_1b0 = (code)0x0;
                pcStack_1b8 = (code *)0x0;
                if (((ulong)local_1c0 & 1) != 0) {
                    /* try { // try from 00bbb018 to 00cbb023 has its CatchHandler @ 00bbb538 */
                  _ZdlPv(local_1b0);
                }
              }
                    /* try { // try from 00bbb024 to 00cbb02f has its CatchHandler @ 00bbb528 */
              local_1b0 = local_80;
              pcStack_1b8 = pcStack_88;
              local_1c0 = local_90;
                    /* try { // try from 00bbb030 to 00cbb03b has its CatchHandler @ 00bbb518 */
              uVar22 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(2);
                    /* try { // try from 00bbb03c to 00cbb09f has its CatchHandler @ 00bbaf80 */
              uVar22 = FUN_00497b94(plVar9,lVar13,uVar22);
              uVar11 = _ZN8firebase4util3set11GetMethodIdENS1_6MethodE(0);
              uVar11 = FUN_00497b94(plVar9,uVar22,uVar11);
              uVar14 = _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(0);
              cVar5 = FUN_00497da8(plVar9,uVar11,uVar14);
              if (cVar5 != '\0') {
                    /* try { // try from 00bbb0a0 to 00cbb0c7 has its CatchHandler @ 00bbb54c */
                do {
                  uVar14 = _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(1);
                  uVar14 = FUN_00497b94(plVar9,uVar11,uVar14);
                  __s1 = (char *)(**(code **)(*plVar9 + 0x548))(plVar9,uVar14,0);
                  sVar15 = __strlen_chk("google.",8);
                  iVar6 = strncmp(__s1,"google.",sVar15);
                  if (iVar6 != 0) {
                    sVar15 = __strlen_chk(&DAT_0030e91b,5);
                    iVar6 = strncmp(__s1,"gcm.",sVar15);
                    /* try { // try from 00bbb128 to 00cbb14f has its CatchHandler @ 00bbb548 */
                    if ((((iVar6 != 0) && (iVar6 = strcmp(__s1,"from"), iVar6 != 0)) &&
                        (iVar6 = strcmp(__s1,"message_type"), iVar6 != 0)) &&
                       (iVar6 = strcmp(__s1,"collapse_key"), iVar6 != 0)) {
                      uVar16 = _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE(1);
                      uVar16 = FUN_00497b94(plVar9,lVar13,uVar16,uVar14);
                      _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject
                                (&local_90,plVar9,uVar16);
                      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                                (&local_b0,__s1);
                    /* try { // try from 00bbb19c to 00cbb1a3 has its CatchHandler @ 00bbb50c */
                      puVar17 = (undefined8 *)FUN_0046d908(&local_1a8,&uStack_98,&local_b0);
                      puVar23 = (undefined8 *)*puVar17;
                      if (puVar23 == (undefined8 *)0x0) {
                        puVar23 = (undefined8 *)_Znwm(0x50);
                        pvVar4 = local_a0;
                        uVar16 = uStack_a8;
                        uVar10 = local_b0;
                        uStack_a8 = 0;
                        local_a0 = (void *)0x0;
                        local_b0 = 0;
                        puVar23[8] = 0;
                        puVar23[9] = 0;
                        *puVar23 = 0;
                        puVar23[1] = 0;
                        puVar23[5] = uVar16;
                        puVar23[4] = uVar10;
                        puVar23[6] = pvVar4;
                        puVar23[7] = 0;
                        puVar23[2] = uStack_98;
                        *puVar17 = puVar23;
                        puVar20 = puVar23;
                        if ((undefined8 *)*local_1a8 != (undefined8 *)0x0) {
                          puVar20 = (undefined8 *)*puVar17;
                          local_1a8 = (undefined8 *)*local_1a8;
                        }
                        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                                  (local_1a0,puVar20);
                        local_198 = local_198 + 1;
                      }
                      pbVar21 = (byte *)(puVar23 + 7);
                      if ((*pbVar21 & 1) == 0) {
                    /* try { // try from 00bbb21c to 00cbb243 has its CatchHandler @ 00bbb544 */
                        pbVar21[0] = 0;
                        pbVar21[1] = 0;
                      }
                      else {
                        *(undefined1 *)puVar23[9] = 0;
                        puVar23[8] = 0;
                        if ((*(byte *)(puVar23 + 7) & 1) != 0) {
                          _ZdlPv((void *)puVar23[9]);
                          puVar23[7] = 0;
                        }
                      }
                      puVar23[9] = local_80;
                      puVar23[8] = pcStack_88;
                      *(code **)pbVar21 = local_90;
                      pcStack_88 = (code *)0x0;
                      local_80 = (code *)0x0;
                      local_90 = (code *)0x0;
                      if (((local_b0 & 1) != 0) && (_ZdlPv(local_a0), ((ulong)local_90 & 1) != 0)) {
                        _ZdlPv(local_80);
                      }
                    }
                  }
                  (**(code **)(*plVar9 + 0x550))(plVar9,uVar14,__s1);
                    /* try { // try from 00bbb294 to 00cbb29b has its CatchHandler @ 00bbb508 */
                  (**(code **)(*plVar9 + 0xb8))(plVar9,uVar14);
                  uVar14 = _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(0);
                  cVar5 = FUN_00497da8(plVar9,uVar11,uVar14);
                } while (cVar5 != '\0');
              }
              (**(code **)(*plVar9 + 0xb8))(plVar9,uVar11);
              (**(code **)(*plVar9 + 0xb8))(plVar9,uVar22);
              uStack_f7 = CONCAT17(1,(undefined7)uStack_f7);
              uVar22 = _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE(4);
              uVar22 = FUN_00497b94(plVar9,lVar12,uVar22);
              _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar9);
                    /* try { // try from 00bbb324 to 00cbb34b has its CatchHandler @ 00bbb540 */
              _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(&local_90,plVar9,uVar22);
              if (((ulong)local_e8 & 1) != 0) {
                *local_d8 = (code)0x0;
                pcStack_e0 = (code *)0x0;
                if (((ulong)local_e8 & 1) != 0) {
                  _ZdlPv(local_d8);
                }
              }
              local_d8 = local_80;
              pcStack_e0 = pcStack_88;
              local_e8 = local_90;
              _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE(&local_1f0);
            }
          }
          (**(code **)(*plVar9 + 0xb8))(plVar9,lVar13);
          _ZN8firebase9messaging7MessageD2Ev(&local_1f0);
        }
                    /* try { // try from 00bbb398 to 00cbb39f has its CatchHandler @ 00bbb504 */
        (**(code **)(*plVar9 + 0xb8))(plVar9,lVar12);
      }
    }
  }
  pcStack_88 = (code *)0x0;
  local_80 = (code *)0x0;
  local_90 = (code *)0x0;
  if ((*DAT_01127450 & 1) == 0) {
    pbVar21 = DAT_01127450 + 1;
  }
  else {
    pbVar21 = *(byte **)(DAT_01127450 + 0x10);
  }
  iVar6 = _ZN8firebase9messaging10FileLocker11AcquireLockEPKc(pbVar21);
  if ((*DAT_01127428 & 1) == 0) {
    pbVar19 = DAT_01127428 + 1;
  }
  else {
    pbVar19 = *(byte **)(DAT_01127428 + 0x10);
  }
  pFVar18 = fopen((char *)pbVar19,"rb");
  if (pFVar18 == (FILE *)0x0) {
LAB_00bbb490:
    _ZN8firebase9LogAssertEPKcz("LoadFile(g_local_storage_file_path->c_str(), &buffer)");
    bVar1 = true;
  }
  else {
                    /* try { // try from 00bbb404 to 00cbb40b has its CatchHandler @ 00bbb510 */
                    /* try { // try from 00bbb40c to 00cbb5a3 has its CatchHandler @ 00bbaf80 */
    fseek(pFVar18,0,2);
    lVar12 = ftell(pFVar18);
    if (lVar12 == 0) {
      local_90 = (code *)((ulong)local_90 & 0xffffffffffff0000);
    }
    else {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
                (&local_90,lVar12,0);
    }
    fseek(pFVar18,0,0);
    pcVar2 = pcStack_88;
    __ptr = local_80;
    if (((ulong)local_90 & 1) == 0) {
      pcVar2 = (code *)((ulong)local_90 >> 1 & 0x7f);
      __ptr = (code *)((long)&local_90 + 1);
    }
    fread(__ptr,(size_t)pcVar2,1,pFVar18);
    iVar7 = ferror(pFVar18);
    iVar8 = fclose(pFVar18);
    if (iVar8 != 0 || iVar7 != 0) goto LAB_00bbb490;
    pcVar2 = (code *)((ulong)local_90 >> 1 & 0x7f);
    if (((ulong)local_90 & 1) != 0) {
      pcVar2 = pcStack_88;
    }
    if (pcVar2 != (code *)0x0) {
      if ((*DAT_01127428 & 1) == 0) {
        pbVar19 = DAT_01127428 + 1;
      }
      else {
        pbVar19 = *(byte **)(DAT_01127428 + 0x10);
      }
      pFVar18 = fopen((char *)pbVar19,"w");
      fclose(pFVar18);
    }
    bVar1 = false;
  }
  if (-1 < iVar6) {
    remove((char *)pbVar21);
    close(iVar6);
                    /* catch() { ... } // from try @ 00bbb398 with catch @ 00bbb504 */
                    /* catch() { ... } // from try @ 00bbb294 with catch @ 00bbb508 */
    if (DAT_01127418 != 0) {
                    /* catch() { ... } // from try @ 00bbb19c with catch @ 00bbb50c */
      _ZN8firebase5Mutex7ReleaseEv();
    }
  }
                    /* catch() { ... } // from try @ 00bbb404 with catch @ 00bbb510 */
  if (!bVar1) {
                    /* catch() { ... } // from try @ 00bbb030 with catch @ 00bbb518 */
                    /* catch() { ... } // from try @ 00bbb024 with catch @ 00bbb528 */
    local_1f0 = _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE;
    pcStack_1e8 = (code *)0x0;
                    /* catch() { ... } // from try @ 00bbb018 with catch @ 00bbb538 */
    local_1e0 = FUN_00bbe1e8;
    local_1d8 = (code *)0x0;
    pcStack_1d0 = FUN_00bbe398;
    pcStack_1c8 = (code *)0x0;
                    /* catch() { ... } // from try @ 00bbb324 with catch @ 00bbb540 */
    local_1c0 = _ZN8firebase9messaging38NotifyListenerOnUnregistrationReceivedEPKc;
    pcStack_1b8 = (code *)0x0;
                    /* catch() { ... } // from try @ 00bbb21c with catch @ 00bbb544 */
                    /* catch() { ... } // from try @ 00bbb128 with catch @ 00bbb548 */
                    /* catch() { ... } // from try @ 00bbb0a0 with catch @ 00bbb54c */
    _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
              (&local_1f0,&local_90);
  }
  if (((ulong)local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
LAB_00bbb560:
  if (*(long *)(lVar3 + 0x28) != local_78) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00bbafec with catch @ 00bbb58c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaaa4"></a> `00bbaaa4` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbaaa8"></a> `00bbaaa8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaaac"></a> `00bbaaac` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbaab0"></a> `00bbaab0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbaab4"></a> `00bbaab4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbaab8"></a> `00bbaab8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbaabc"></a> `00bbaabc` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbaac0"></a> `00bbaac0` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00bbaac4"></a> `00bbaac4` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbaac8"></a> `00bbaac8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbaacc"></a> `00bbaacc` | `60 2b 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbaad0"></a> `00bbaad0` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbaad4"></a> `00bbaad4` | `a8 83 19 f8` | stur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbaad8"></a> `00bbaad8` | `f2 83 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaadc"></a> `00bbaadc` | `74 2b 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbaae0"></a> `00bbaae0` | `80 12 42 f9` | ldr x0,[x20, #0x420] | `FALL_THROUGH`
<a id="insn-00bbaae4"></a> `00bbaae4` | `80 00 00 b4` | cbz x0,0x00bbaaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbaae8"></a> `00bbaae8` | `8e 85 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaaec"></a> `00bbaaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaaf0"></a> `00bbaaf0` | `02 00 00 14` | b 0x00bbaaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbaaf4"></a> `00bbaaf4` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bbaaf8"></a> `00bbaaf8` | `60 2b 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbaafc"></a> `00bbaafc` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbab00"></a> `00bbab00` | `ec 83 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab04"></a> `00bbab04` | `0f 8e 02 94` | bl 0x00c5e340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab08"></a> `00bbab08` | `d3 52 00 b4` | cbz x19,0x00bbb560 | `CONDITIONAL_JUMP`
<a id="insn-00bbab0c"></a> `00bbab0c` | `a0 52 00 36` | tbz w0,#0x0,0x00bbb560 | `CONDITIONAL_JUMP`
<a id="insn-00bbab10"></a> `00bbab10` | `75 2b 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbab14"></a> `00bbab14` | `a8 22 51 39` | ldrb w8,[x21, #0x448] | `FALL_THROUGH`
<a id="insn-00bbab18"></a> `00bbab18` | `88 44 00 37` | tbnz w8,#0x0,0x00bbb3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbab1c"></a> `00bbab1c` | `09 8e 02 94` | bl 0x00c5e340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab20"></a> `00bbab20` | `40 44 00 36` | tbz w0,#0x0,0x00bbb3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbab24"></a> `00bbab24` | `60 2b 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbab28"></a> `00bbab28` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbab2c"></a> `00bbab2c` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbab30"></a> `00bbab30` | `a8 22 11 39` | strb w8,[x21, #0x448] | `FALL_THROUGH`
<a id="insn-00bbab34"></a> `00bbab34` | `db 83 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab38"></a> `00bbab38` | `88 12 42 f9` | ldr x8,[x20, #0x420] | `FALL_THROUGH`
<a id="insn-00bbab3c"></a> `00bbab3c` | `28 01 00 b4` | cbz x8,0x00bbab60 | `CONDITIONAL_JUMP`
<a id="insn-00bbab40"></a> `00bbab40` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbab44"></a> `00bbab44` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bbab48"></a> `00bbab48` | `28 65 40 f9` | ldr x8,[x9, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbab4c"></a> `00bbab4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbab50"></a> `00bbab50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbab54"></a> `00bbab54` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbab58"></a> `00bbab58` | `34 00 80 52` | mov w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bbab5c"></a> `00bbab5c` | `02 00 00 14` | b 0x00bbab64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbab60"></a> `00bbab60` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00bbab64"></a> `00bbab64` | `60 2b 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbab68"></a> `00bbab68` | `00 60 0c 91` | add x0,x0,#0x318 | `FALL_THROUGH`
<a id="insn-00bbab6c"></a> `00bbab6c` | `d1 83 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab70"></a> `00bbab70` | `d4 41 00 34` | cbz w20,0x00bbb3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbab74"></a> `00bbab74` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bbab78"></a> `00bbab78` | `9e 86 02 94` | bl 0x00c5c5f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab7c"></a> `00bbab7c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbab80"></a> `00bbab80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbab84"></a> `00bbab84` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbab88"></a> `00bbab88` | `03 74 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbab8c"></a> `00bbab8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbab90"></a> `00bbab90` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbab94"></a> `00bbab94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbab98"></a> `00bbab98` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbab9c"></a> `00bbab9c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbaba0"></a> `00bbaba0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbaba4"></a> `00bbaba4` | `34 40 00 b4` | cbz x20,0x00bbb3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbaba8"></a> `00bbaba8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bbabac"></a> `00bbabac` | `89 86 02 94` | bl 0x00c5c5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbabb0"></a> `00bbabb0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbabb4"></a> `00bbabb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbabb8"></a> `00bbabb8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbabbc"></a> `00bbabbc` | `f4 0f 00 f9` | str x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbabc0"></a> `00bbabc0` | `f5 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbabc4"></a> `00bbabc4` | `80 3e 00 b4` | cbz x0,0x00bbb394 | `CONDITIONAL_JUMP`
<a id="insn-00bbabc8"></a> `00bbabc8` | `e9 83 00 91` | add x9,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbabcc"></a> `00bbabcc` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbabd0"></a> `00bbabd0` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbabd4"></a> `00bbabd4` | `2a 41 01 91` | add x10,x9,#0x50 | `FALL_THROUGH`
<a id="insn-00bbabd8"></a> `00bbabd8` | `29 21 04 91` | add x9,x9,#0x108 | `FALL_THROUGH`
<a id="insn-00bbabdc"></a> `00bbabdc` | `ff 7f 07 a9` | stp xzr,xzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbabe0"></a> `00bbabe0` | `ff e3 00 b9` | str wzr,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bbabe4"></a> `00bbabe4` | `e0 03 01 ad` | stp q0,q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbabe8"></a> `00bbabe8` | `e0 03 02 ad` | stp q0,q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbabec"></a> `00bbabec` | `e0 03 04 ad` | stp q0,q0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbabf0"></a> `00bbabf0` | `e0 03 05 ad` | stp q0,q0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbabf4"></a> `00bbabf4` | `e0 03 06 ad` | stp q0,q0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bbabf8"></a> `00bbabf8` | `ff 2b 06 a9` | stp xzr,x10,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbabfc"></a> `00bbabfc` | `00 81 8c 3c` | stur q0,[x8, #0xc8] | `FALL_THROUGH`
<a id="insn-00bbac00"></a> `00bbac00` | `00 81 8d 3c` | stur q0,[x8, #0xd8] | `FALL_THROUGH`
<a id="insn-00bbac04"></a> `00bbac04` | `00 81 8e 3c` | stur q0,[x8, #0xe8] | `FALL_THROUGH`
<a id="insn-00bbac08"></a> `00bbac08` | `00 11 8f 3c` | stur q0,[x8, #0xf1] | `FALL_THROUGH`
<a id="insn-00bbac0c"></a> `00bbac0c` | `3f 19 00 f9` | str xzr,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00bbac10"></a> `00bbac10` | `20 81 00 ad` | stp q0,q0,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bbac14"></a> `00bbac14` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00bbac18"></a> `00bbac18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac1c"></a> `00bbac1c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbac20"></a> `00bbac20` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbac24"></a> `00bbac24` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbac28"></a> `00bbac28` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbac2c"></a> `00bbac2c` | `21 34 23 91` | add x1,x1,#0x8cd | `FALL_THROUGH`
<a id="insn-00bbac30"></a> `00bbac30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac34"></a> `00bbac34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac38"></a> `00bbac38` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbac3c"></a> `00bbac3c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbac40"></a> `00bbac40` | `fc 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac44"></a> `00bbac44` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbac48"></a> `00bbac48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac4c"></a> `00bbac4c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbac50"></a> `00bbac50` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbac54"></a> `00bbac54` | `d0 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac58"></a> `00bbac58` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbac5c"></a> `00bbac5c` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbac60"></a> `00bbac60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac64"></a> `00bbac64` | `f3 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac68"></a> `00bbac68` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac6c"></a> `00bbac6c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbac70"></a> `00bbac70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac74"></a> `00bbac74` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbac78"></a> `00bbac78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac7c"></a> `00bbac7c` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbac80"></a> `00bbac80` | `e9 83 00 91` | add x9,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbac84"></a> `00bbac84` | `34 e1 01 91` | add x20,x9,#0x78 | `FALL_THROUGH`
<a id="insn-00bbac88"></a> `00bbac88` | `68 00 00 37` | tbnz w8,#0x0,0x00bbac94 | `CONDITIONAL_JUMP`
<a id="insn-00bbac8c"></a> `00bbac8c` | `ff 33 01 79` | strh wzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbac90"></a> `00bbac90` | `09 00 00 14` | b 0x00bbacb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbac94"></a> `00bbac94` | `e8 57 40 f9` | ldr x8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bbac98"></a> `00bbac98` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbac9c"></a> `00bbac9c` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbaca0"></a> `00bbaca0` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbaca4"></a> `00bbaca4` | `88 00 00 36` | tbz w8,#0x0,0x00bbacb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbaca8"></a> `00bbaca8` | `e0 57 40 f9` | ldr x0,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bbacac"></a> `00bbacac` | `a9 78 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacb0"></a> `00bbacb0` | `ff 4f 00 f9` | str xzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbacb4"></a> `00bbacb4` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbacb8"></a> `00bbacb8` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbacbc"></a> `00bbacbc` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbacc0"></a> `00bbacc0` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbacc4"></a> `00bbacc4` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbacc8"></a> `00bbacc8` | `e9 53 40 f9` | ldr x9,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbaccc"></a> `00bbaccc` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbacd0"></a> `00bbacd0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbacd4"></a> `00bbacd4` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbacd8"></a> `00bbacd8` | `08 05 00 b5` | cbnz x8,0x00bbad78 | `CONDITIONAL_JUMP`
<a id="insn-00bbacdc"></a> `00bbacdc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbace0"></a> `00bbace0` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbace8"></a> `00bbace8` | `21 7c 23 91` | add x1,x1,#0x8df | `FALL_THROUGH`
<a id="insn-00bbacec"></a> `00bbacec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbacf0"></a> `00bbacf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbacf4"></a> `00bbacf4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbacf8"></a> `00bbacf8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbacfc"></a> `00bbacfc` | `cd 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad00"></a> `00bbad00` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbad04"></a> `00bbad04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbad08"></a> `00bbad08` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbad0c"></a> `00bbad0c` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbad10"></a> `00bbad10` | `a1 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad14"></a> `00bbad14` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbad18"></a> `00bbad18` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbad1c"></a> `00bbad1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbad20"></a> `00bbad20` | `c4 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad24"></a> `00bbad24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbad28"></a> `00bbad28` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbad2c"></a> `00bbad2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbad30"></a> `00bbad30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbad34"></a> `00bbad34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbad38"></a> `00bbad38` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbad3c"></a> `00bbad3c` | `68 00 00 37` | tbnz w8,#0x0,0x00bbad48 | `CONDITIONAL_JUMP`
<a id="insn-00bbad40"></a> `00bbad40` | `ff 33 01 79` | strh wzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbad44"></a> `00bbad44` | `09 00 00 14` | b 0x00bbad68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbad48"></a> `00bbad48` | `e8 57 40 f9` | ldr x8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bbad4c"></a> `00bbad4c` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbad50"></a> `00bbad50` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbad54"></a> `00bbad54` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbad58"></a> `00bbad58` | `88 00 00 36` | tbz w8,#0x0,0x00bbad68 | `CONDITIONAL_JUMP`
<a id="insn-00bbad5c"></a> `00bbad5c` | `e0 57 40 f9` | ldr x0,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bbad60"></a> `00bbad60` | `7c 78 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad64"></a> `00bbad64` | `ff 4f 00 f9` | str xzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbad68"></a> `00bbad68` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbad6c"></a> `00bbad6c` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbad70"></a> `00bbad70` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbad74"></a> `00bbad74` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbad78"></a> `00bbad78` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbad7c"></a> `00bbad7c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbad80"></a> `00bbad80` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbad84"></a> `00bbad84` | `21 a8 23 91` | add x1,x1,#0x8ea | `FALL_THROUGH`
<a id="insn-00bbad88"></a> `00bbad88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbad8c"></a> `00bbad8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbad90"></a> `00bbad90` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbad94"></a> `00bbad94` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbad98"></a> `00bbad98` | `a6 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbad9c"></a> `00bbad9c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbada0"></a> `00bbada0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbada4"></a> `00bbada4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbada8"></a> `00bbada8` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbadac"></a> `00bbadac` | `7a 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadb0"></a> `00bbadb0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbadb4"></a> `00bbadb4` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbadb8"></a> `00bbadb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbadbc"></a> `00bbadbc` | `9d 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbadc0"></a> `00bbadc0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbadc4"></a> `00bbadc4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbadc8"></a> `00bbadc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbadcc"></a> `00bbadcc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbadd0"></a> `00bbadd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbadd4"></a> `00bbadd4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbadd8"></a> `00bbadd8` | `68 00 00 37` | tbnz w8,#0x0,0x00bbade4 | `CONDITIONAL_JUMP`
<a id="insn-00bbaddc"></a> `00bbaddc` | `ff 43 00 79` | strh wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbade0"></a> `00bbade0` | `09 00 00 14` | b 0x00bbae04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbade4"></a> `00bbade4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbade8"></a> `00bbade8` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbadf4"></a> `00bbadf4` | `88 00 00 36` | tbz w8,#0x0,0x00bbae04 | `CONDITIONAL_JUMP`
<a id="insn-00bbadf8"></a> `00bbadf8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbadfc"></a> `00bbadfc` | `55 78 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae00"></a> `00bbae00` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbae04"></a> `00bbae04` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bbae08"></a> `00bbae08` | `ea 53 40 f9` | ldr x10,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbae0c"></a> `00bbae0c` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbae10"></a> `00bbae10` | `a9 03 59 f8` | ldur x9,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbae14"></a> `00bbae14` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae18"></a> `00bbae18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae1c"></a> `00bbae1c` | `68 01 8a 9a` | csel x8,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bbae20"></a> `00bbae20` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbae24"></a> `00bbae24` | `e9 1b 00 f9` | str x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbae28"></a> `00bbae28` | `88 2a 00 b4` | cbz x8,0x00bbb378 | `CONDITIONAL_JUMP`
<a id="insn-00bbae2c"></a> `00bbae2c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbae30"></a> `00bbae30` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbae34"></a> `00bbae34` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae38"></a> `00bbae38` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae3c"></a> `00bbae3c` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbae40"></a> `00bbae40` | `c8 29 00 b4` | cbz x8,0x00bbb378 | `CONDITIONAL_JUMP`
<a id="insn-00bbae44"></a> `00bbae44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbae48"></a> `00bbae48` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbae4c"></a> `00bbae4c` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbae50"></a> `00bbae50` | `21 bc 23 91` | add x1,x1,#0x8ef | `FALL_THROUGH`
<a id="insn-00bbae54"></a> `00bbae54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbae58"></a> `00bbae58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbae5c"></a> `00bbae5c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbae60"></a> `00bbae60` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae64"></a> `00bbae64` | `73 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae68"></a> `00bbae68` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbae6c"></a> `00bbae6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbae70"></a> `00bbae70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbae74"></a> `00bbae74` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbae78"></a> `00bbae78` | `47 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae7c"></a> `00bbae7c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbae80"></a> `00bbae80` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbae84"></a> `00bbae84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbae88"></a> `00bbae88` | `6a 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae8c"></a> `00bbae8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbae90"></a> `00bbae90` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbae94"></a> `00bbae94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbae98"></a> `00bbae98` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbae9c"></a> `00bbae9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbaea0"></a> `00bbaea0` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbaea4"></a> `00bbaea4` | `e9 83 00 91` | add x9,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbaea8"></a> `00bbaea8` | `34 61 00 91` | add x20,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00bbaeac"></a> `00bbaeac` | `68 00 00 37` | tbnz w8,#0x0,0x00bbaeb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbaeb0"></a> `00bbaeb0` | `ff 73 00 79` | strh wzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbaeb4"></a> `00bbaeb4` | `09 00 00 14` | b 0x00bbaed8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbaeb8"></a> `00bbaeb8` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbaebc"></a> `00bbaebc` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbaec0"></a> `00bbaec0` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbaec4"></a> `00bbaec4` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbaec8"></a> `00bbaec8` | `88 00 00 36` | tbz w8,#0x0,0x00bbaed8 | `CONDITIONAL_JUMP`
<a id="insn-00bbaecc"></a> `00bbaecc` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbaed0"></a> `00bbaed0` | `20 78 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaed4"></a> `00bbaed4` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbaed8"></a> `00bbaed8` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbaedc"></a> `00bbaedc` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbaee0"></a> `00bbaee0` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaee4"></a> `00bbaee4` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbaee8"></a> `00bbaee8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbaeec"></a> `00bbaeec` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbaef0"></a> `00bbaef0` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbaef4"></a> `00bbaef4` | `21 e4 23 91` | add x1,x1,#0x8f9 | `FALL_THROUGH`
<a id="insn-00bbaef8"></a> `00bbaef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaefc"></a> `00bbaefc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbaf00"></a> `00bbaf00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbaf04"></a> `00bbaf04` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbaf08"></a> `00bbaf08` | `4a 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf0c"></a> `00bbaf0c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbaf10"></a> `00bbaf10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf14"></a> `00bbaf14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbaf18"></a> `00bbaf18` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbaf1c"></a> `00bbaf1c` | `1e 73 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf20"></a> `00bbaf20` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbaf24"></a> `00bbaf24` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbaf28"></a> `00bbaf28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf2c"></a> `00bbaf2c` | `41 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf30"></a> `00bbaf30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbaf34"></a> `00bbaf34` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbaf38"></a> `00bbaf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf3c"></a> `00bbaf3c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbaf40"></a> `00bbaf40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbaf44"></a> `00bbaf44` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbaf48"></a> `00bbaf48` | `e9 83 00 91` | add x9,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbaf4c"></a> `00bbaf4c` | `34 41 02 91` | add x20,x9,#0x90 | `FALL_THROUGH`
<a id="insn-00bbaf50"></a> `00bbaf50` | `68 00 00 37` | tbnz w8,#0x0,0x00bbaf5c | `CONDITIONAL_JUMP`
<a id="insn-00bbaf54"></a> `00bbaf54` | `ff 63 01 79` | strh wzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbaf58"></a> `00bbaf58` | `09 00 00 14` | b 0x00bbaf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbaf5c"></a> `00bbaf5c` | `e8 63 40 f9` | ldr x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bbaf60"></a> `00bbaf60` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbaf64"></a> `00bbaf64` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbaf68"></a> `00bbaf68` | `ff 5f 00 f9` | str xzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbaf6c"></a> `00bbaf6c` | `88 00 00 36` | tbz w8,#0x0,0x00bbaf7c | `CONDITIONAL_JUMP`
<a id="insn-00bbaf70"></a> `00bbaf70` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bbaf74"></a> `00bbaf74` | `f7 77 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf78"></a> `00bbaf78` | `ff 5b 00 f9` | str xzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbaf7c"></a> `00bbaf7c` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbaf80"></a> `00bbaf80` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbaf84"></a> `00bbaf84` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf88"></a> `00bbaf88` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbaf8c"></a> `00bbaf8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbaf90"></a> `00bbaf90` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bbaf94"></a> `00bbaf94` | `a1 ba ff 90` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbaf98"></a> `00bbaf98` | `21 18 24 91` | add x1,x1,#0x906 | `FALL_THROUGH`
<a id="insn-00bbaf9c"></a> `00bbaf9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafa0"></a> `00bbafa0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbafa4"></a> `00bbafa4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbafa8"></a> `00bbafa8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbafac"></a> `00bbafac` | `21 84 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafb0"></a> `00bbafb0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbafb4"></a> `00bbafb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafb8"></a> `00bbafb8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbafbc"></a> `00bbafbc` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbafc0"></a> `00bbafc0` | `f5 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafc4"></a> `00bbafc4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbafc8"></a> `00bbafc8` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbafcc"></a> `00bbafcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafd0"></a> `00bbafd0` | `18 85 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafd4"></a> `00bbafd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbafd8"></a> `00bbafd8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbafdc"></a> `00bbafdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafe0"></a> `00bbafe0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbafe4"></a> `00bbafe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbafe8"></a> `00bbafe8` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbafec"></a> `00bbafec` | `e9 83 00 91` | add x9,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbaff0"></a> `00bbaff0` | `34 c1 00 91` | add x20,x9,#0x30 | `FALL_THROUGH`
<a id="insn-00bbaff4"></a> `00bbaff4` | `68 00 00 37` | tbnz w8,#0x0,0x00bbb000 | `CONDITIONAL_JUMP`
<a id="insn-00bbaff8"></a> `00bbaff8` | `ff a3 00 79` | strh wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbaffc"></a> `00bbaffc` | `09 00 00 14` | b 0x00bbb020 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb000"></a> `00bbb000` | `e8 33 40 f9` | ldr x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb004"></a> `00bbb004` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbb008"></a> `00bbb008` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb00c"></a> `00bbb00c` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbb010"></a> `00bbb010` | `88 00 00 36` | tbz w8,#0x0,0x00bbb020 | `CONDITIONAL_JUMP`
<a id="insn-00bbb014"></a> `00bbb014` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb018"></a> `00bbb018` | `ce 77 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb01c"></a> `00bbb01c` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb020"></a> `00bbb020` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbb024"></a> `00bbb024` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb028"></a> `00bbb028` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb02c"></a> `00bbb02c` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bbb030"></a> `00bbb030` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb034"></a> `00bbb034` | `ff 83 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb038"></a> `00bbb038` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb03c"></a> `00bbb03c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb040"></a> `00bbb040` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb044"></a> `00bbb044` | `d4 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb048"></a> `00bbb048` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb04c"></a> `00bbb04c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbb050"></a> `00bbb050` | `54 85 02 94` | bl 0x00c5c5a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb054"></a> `00bbb054` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb058"></a> `00bbb058` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb05c"></a> `00bbb05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb060"></a> `00bbb060` | `cd 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb064"></a> `00bbb064` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbb068"></a> `00bbb068` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbb06c"></a> `00bbb06c` | `65 85 02 94` | bl 0x00c5c600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb070"></a> `00bbb070` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb074"></a> `00bbb074` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb078"></a> `00bbb078` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbb07c"></a> `00bbb07c` | `4b 73 e3 97` | bl 0x00497da8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb080"></a> `00bbb080` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbb084"></a> `00bbb084` | `20 12 00 54` | b.eq 0x00bbb2c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb088"></a> `00bbb088` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbb08c"></a> `00bbb08c` | `98 ba ff f0` | adrp x24,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb090"></a> `00bbb090` | `94 ba ff f0` | adrp x20,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb094"></a> `00bbb094` | `18 4f 24 91` | add x24,x24,#0x913 | `FALL_THROUGH`
<a id="insn-00bbb098"></a> `00bbb098` | `94 6e 24 91` | add x20,x20,#0x91b | `FALL_THROUGH`
<a id="insn-00bbb09c"></a> `00bbb09c` | `08 21 01 91` | add x8,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb0a0"></a> `00bbb0a0` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bbb0a4"></a> `00bbb0a4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb0a8"></a> `00bbb0a8` | `56 85 02 94` | bl 0x00c5c600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0ac"></a> `00bbb0ac` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb0b0"></a> `00bbb0b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb0b4"></a> `00bbb0b4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbb0b8"></a> `00bbb0b8` | `b7 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0bc"></a> `00bbb0bc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb0c0"></a> `00bbb0c0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbb0c4"></a> `00bbb0c4` | `08 a5 42 f9` | ldr x8,[x8, #0x548] | `FALL_THROUGH`
<a id="insn-00bbb0c8"></a> `00bbb0c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb0cc"></a> `00bbb0cc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb0d0"></a> `00bbb0d0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbb0d4"></a> `00bbb0d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb0d8"></a> `00bbb0d8` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00bbb0dc"></a> `00bbb0dc` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-00bbb0e0"></a> `00bbb0e0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbb0e4"></a> `00bbb0e4` | `ff 86 02 94` | bl 0x00c5cce0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0e8"></a> `00bbb0e8` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb0ec"></a> `00bbb0ec` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bbb0f0"></a> `00bbb0f0` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bbb0f4"></a> `00bbb0f4` | `37 8c 02 94` | bl 0x00c5e1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0f8"></a> `00bbb0f8` | `20 0c 00 34` | cbz w0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb0fc"></a> `00bbb0fc` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00bbb100"></a> `00bbb100` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb104"></a> `00bbb104` | `f7 86 02 94` | bl 0x00c5cce0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb108"></a> `00bbb108` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb10c"></a> `00bbb10c` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bbb110"></a> `00bbb110` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbb114"></a> `00bbb114` | `2f 8c 02 94` | bl 0x00c5e1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb118"></a> `00bbb118` | `20 0b 00 34` | cbz w0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb11c"></a> `00bbb11c` | `81 ba ff f0` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb120"></a> `00bbb120` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bbb124"></a> `00bbb124` | `21 a8 23 91` | add x1,x1,#0x8ea | `FALL_THROUGH`
<a id="insn-00bbb128"></a> `00bbb128` | `f2 85 02 94` | bl 0x00c5c8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb12c"></a> `00bbb12c` | `80 0a 00 34` | cbz w0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb130"></a> `00bbb130` | `81 ba ff f0` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb134"></a> `00bbb134` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bbb138"></a> `00bbb138` | `21 e4 23 91` | add x1,x1,#0x8f9 | `FALL_THROUGH`
<a id="insn-00bbb13c"></a> `00bbb13c` | `ed 85 02 94` | bl 0x00c5c8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb140"></a> `00bbb140` | `e0 09 00 34` | cbz w0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb144"></a> `00bbb144` | `81 ba ff f0` | adrp x1,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb148"></a> `00bbb148` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00bbb14c"></a> `00bbb14c` | `21 18 24 91` | add x1,x1,#0x906 | `FALL_THROUGH`
<a id="insn-00bbb150"></a> `00bbb150` | `e8 85 02 94` | bl 0x00c5c8f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb154"></a> `00bbb154` | `40 09 00 34` | cbz w0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb158"></a> `00bbb158` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb15c"></a> `00bbb15c` | `b5 83 02 94` | bl 0x00c5c030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb160"></a> `00bbb160` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb164"></a> `00bbb164` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb168"></a> `00bbb168` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb16c"></a> `00bbb16c` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bbb170"></a> `00bbb170` | `89 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb174"></a> `00bbb174` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbb178"></a> `00bbb178` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb17c"></a> `00bbb17c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb180"></a> `00bbb180` | `ac 84 02 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb184"></a> `00bbb184` | `a0 83 02 d1` | sub x0,x29,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbb188"></a> `00bbb188` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bbb18c"></a> `00bbb18c` | `35 85 02 94` | bl 0x00c5c660 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb190"></a> `00bbb190` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00bbb194"></a> `00bbb194` | `a1 23 02 d1` | sub x1,x29,#0x88 | `FALL_THROUGH`
<a id="insn-00bbb198"></a> `00bbb198` | `a2 83 02 d1` | sub x2,x29,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbb19c"></a> `00bbb19c` | `db c9 e2 97` | bl 0x0046d908 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb1a0"></a> `00bbb1a0` | `1b 00 40 f9` | ldr x27,[x0] | `FALL_THROUGH`
<a id="insn-00bbb1a4"></a> `00bbb1a4` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bbb1a8"></a> `00bbb1a8` | `5b 03 00 b5` | cbnz x27,0x00bbb210 | `CONDITIONAL_JUMP`
<a id="insn-00bbb1ac"></a> `00bbb1ac` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bbb1b0"></a> `00bbb1b0` | `60 77 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb1b4"></a> `00bbb1b4` | `a0 03 d6 3c` | ldur q0,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00bbb1b8"></a> `00bbb1b8` | `a8 27 77 a9` | ldp x8,x9,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00bbb1bc"></a> `00bbb1bc` | `bf ff 36 a9` | stp xzr,xzr,[x29, #-0x98] | `FALL_THROUGH`
<a id="insn-00bbb1c0"></a> `00bbb1c0` | `bf 03 16 f8` | stur xzr,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00bbb1c4"></a> `00bbb1c4` | `1f 7c 04 a9` | stp xzr,xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb1c8"></a> `00bbb1c8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbb1cc"></a> `00bbb1cc` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb1d0"></a> `00bbb1d0` | `08 7c 03 a9` | stp x8,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb1d4"></a> `00bbb1d4` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb1d8"></a> `00bbb1d8` | `40 03 00 f9` | str x0,[x26] | `FALL_THROUGH`
<a id="insn-00bbb1dc"></a> `00bbb1dc` | `e8 37 40 f9` | ldr x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bbb1e0"></a> `00bbb1e0` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bbb1e4"></a> `00bbb1e4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbb1e8"></a> `00bbb1e8` | `88 00 00 b4` | cbz x8,0x00bbb1f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb1ec"></a> `00bbb1ec` | `e8 37 00 f9` | str x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bbb1f0"></a> `00bbb1f0` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00bbb1f4"></a> `00bbb1f4` | `02 00 00 14` | b 0x00bbb1fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb1f8"></a> `00bbb1f8` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00bbb1fc"></a> `00bbb1fc` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb200"></a> `00bbb200` | `20 85 02 94` | bl 0x00c5c680 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb204"></a> `00bbb204` | `e8 3f 40 f9` | ldr x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bbb208"></a> `00bbb208` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb20c"></a> `00bbb20c` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bbb210"></a> `00bbb210` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00bbb214"></a> `00bbb214` | `48 8f 43 38` | ldrb w8,[x26, #0x38]! | `FALL_THROUGH`
<a id="insn-00bbb218"></a> `00bbb218` | `68 00 00 37` | tbnz w8,#0x0,0x00bbb224 | `CONDITIONAL_JUMP`
<a id="insn-00bbb21c"></a> `00bbb21c` | `5f 03 00 79` | strh wzr,[x26] | `FALL_THROUGH`
<a id="insn-00bbb220"></a> `00bbb220` | `09 00 00 14` | b 0x00bbb244 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb224"></a> `00bbb224` | `68 27 40 f9` | ldr x8,[x27, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb228"></a> `00bbb228` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbb22c"></a> `00bbb22c` | `68 e3 40 39` | ldrb w8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb230"></a> `00bbb230` | `7f 23 00 f9` | str xzr,[x27, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb234"></a> `00bbb234` | `88 00 00 36` | tbz w8,#0x0,0x00bbb244 | `CONDITIONAL_JUMP`
<a id="insn-00bbb238"></a> `00bbb238` | `60 27 40 f9` | ldr x0,[x27, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb23c"></a> `00bbb23c` | `45 77 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb240"></a> `00bbb240` | `7f 1f 00 f9` | str xzr,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb244"></a> `00bbb244` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbb248"></a> `00bbb248` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb24c"></a> `00bbb24c` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb250"></a> `00bbb250` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00bbb254"></a> `00bbb254` | `a8 03 56 38` | ldurb w8,[x29, #-0xa0] | `FALL_THROUGH`
<a id="insn-00bbb258"></a> `00bbb258` | `bf ff 38 a9` | stp xzr,xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00bbb25c"></a> `00bbb25c` | `bf 03 18 f8` | stur xzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb260"></a> `00bbb260` | `e8 00 00 36` | tbz w8,#0x0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb264"></a> `00bbb264` | `a0 03 57 f8` | ldur x0,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00bbb268"></a> `00bbb268` | `3a 77 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb26c"></a> `00bbb26c` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb270"></a> `00bbb270` | `68 00 00 36` | tbz w8,#0x0,0x00bbb27c | `CONDITIONAL_JUMP`
<a id="insn-00bbb274"></a> `00bbb274` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbb278"></a> `00bbb278` | `36 77 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb27c"></a> `00bbb27c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb280"></a> `00bbb280` | `08 a9 42 f9` | ldr x8,[x8, #0x550] | `FALL_THROUGH`
<a id="insn-00bbb284"></a> `00bbb284` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb288"></a> `00bbb288` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb28c"></a> `00bbb28c` | `e2 03 1c aa` | mov x2,x28 | `FALL_THROUGH`
<a id="insn-00bbb290"></a> `00bbb290` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb294"></a> `00bbb294` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb298"></a> `00bbb298` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbb29c"></a> `00bbb29c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb2a0"></a> `00bbb2a0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb2a4"></a> `00bbb2a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb2a8"></a> `00bbb2a8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbb2ac"></a> `00bbb2ac` | `d5 84 02 94` | bl 0x00c5c600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb2b0"></a> `00bbb2b0` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb2b4"></a> `00bbb2b4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb2b8"></a> `00bbb2b8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbb2bc"></a> `00bbb2bc` | `bb 72 e3 97` | bl 0x00497da8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb2c0"></a> `00bbb2c0` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbb2c4"></a> `00bbb2c4` | `01 ef ff 54` | b.ne 0x00bbb0a4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb2c8"></a> `00bbb2c8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb2cc"></a> `00bbb2cc` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbb2d0"></a> `00bbb2d0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb2d4"></a> `00bbb2d4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbb2d8"></a> `00bbb2d8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb2dc"></a> `00bbb2dc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb2e0"></a> `00bbb2e0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbb2e4"></a> `00bbb2e4` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb2e8"></a> `00bbb2e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb2ec"></a> `00bbb2ec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb2f0"></a> `00bbb2f0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb2f4"></a> `00bbb2f4` | `e8 83 04 39` | strb w8,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbb2f8"></a> `00bbb2f8` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bbb2fc"></a> `00bbb2fc` | `b5 84 02 94` | bl 0x00c5c5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb300"></a> `00bbb300` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bbb304"></a> `00bbb304` | `e1 0f 40 f9` | ldr x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb308"></a> `00bbb308` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb30c"></a> `00bbb30c` | `22 72 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb310"></a> `00bbb310` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbb314"></a> `00bbb314` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb318"></a> `00bbb318` | `3a 83 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb31c"></a> `00bbb31c` | `a8 03 02 d1` | sub x8,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb320"></a> `00bbb320` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb324"></a> `00bbb324` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb328"></a> `00bbb328` | `1a 84 02 94` | bl 0x00c5c390 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb32c"></a> `00bbb32c` | `e8 a3 44 39` | ldrb w8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbb330"></a> `00bbb330` | `68 00 00 37` | tbnz w8,#0x0,0x00bbb33c | `CONDITIONAL_JUMP`
<a id="insn-00bbb334"></a> `00bbb334` | `ff 53 02 79` | strh wzr,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbb338"></a> `00bbb338` | `09 00 00 14` | b 0x00bbb35c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb33c"></a> `00bbb33c` | `e8 9f 40 f9` | ldr x8,[sp, #0x138] | `FALL_THROUGH`
<a id="insn-00bbb340"></a> `00bbb340` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbb344"></a> `00bbb344` | `e8 a3 44 39` | ldrb w8,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbb348"></a> `00bbb348` | `ff 9b 00 f9` | str xzr,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbb34c"></a> `00bbb34c` | `88 00 00 36` | tbz w8,#0x0,0x00bbb35c | `CONDITIONAL_JUMP`
<a id="insn-00bbb350"></a> `00bbb350` | `e0 9f 40 f9` | ldr x0,[sp, #0x138] | `FALL_THROUGH`
<a id="insn-00bbb354"></a> `00bbb354` | `ff 76 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb358"></a> `00bbb358` | `ff 97 00 f9` | str xzr,[sp, #0x128] | `FALL_THROUGH`
<a id="insn-00bbb35c"></a> `00bbb35c` | `a8 03 59 f8` | ldur x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbb360"></a> `00bbb360` | `a0 03 d8 3c` | ldur q0,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb364"></a> `00bbb364` | `e9 0b 40 f9` | ldr x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb368"></a> `00bbb368` | `28 09 00 f9` | str x8,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb36c"></a> `00bbb36c` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00bbb370"></a> `00bbb370` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbb374"></a> `00bbb374` | `33 8c 02 94` | bl 0x00c5e440 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb378"></a> `00bbb378` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb37c"></a> `00bbb37c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbb380"></a> `00bbb380` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb384"></a> `00bbb384` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb388"></a> `00bbb388` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb38c"></a> `00bbb38c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbb390"></a> `00bbb390` | `40 8c 02 94` | bl 0x00c5e490 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb394"></a> `00bbb394` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbb398"></a> `00bbb398` | `e1 0f 40 f9` | ldr x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb39c"></a> `00bbb39c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb3a0"></a> `00bbb3a0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbb3a4"></a> `00bbb3a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb3a8"></a> `00bbb3a8` | `68 2b 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbb3ac"></a> `00bbb3ac` | `08 29 42 f9` | ldr x8,[x8, #0x450] | `FALL_THROUGH`
<a id="insn-00bbb3b0"></a> `00bbb3b0` | `bf ff 38 a9` | stp xzr,xzr,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00bbb3b4"></a> `00bbb3b4` | `bf 03 18 f8` | stur xzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb3b8"></a> `00bbb3b8` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbb3bc"></a> `00bbb3bc` | `69 00 00 37` | tbnz w9,#0x0,0x00bbb3c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb3c0"></a> `00bbb3c0` | `14 05 00 91` | add x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb3c4"></a> `00bbb3c4` | `02 00 00 14` | b 0x00bbb3cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb3c8"></a> `00bbb3c8` | `14 09 40 f9` | ldr x20,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb3cc"></a> `00bbb3cc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb3d0"></a> `00bbb3d0` | `94 8c 02 94` | bl 0x00c5e620 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb3d4"></a> `00bbb3d4` | `77 2b 00 90` | adrp x23,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbb3d8"></a> `00bbb3d8` | `e8 16 42 f9` | ldr x8,[x23, #0x428] | `FALL_THROUGH`
<a id="insn-00bbb3dc"></a> `00bbb3dc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00bbb3e0"></a> `00bbb3e0` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbb3e4"></a> `00bbb3e4` | `69 00 00 37` | tbnz w9,#0x0,0x00bbb3f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbb3e8"></a> `00bbb3e8` | `00 05 00 91` | add x0,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb3ec"></a> `00bbb3ec` | `02 00 00 14` | b 0x00bbb3f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb3f0"></a> `00bbb3f0` | `00 09 40 f9` | ldr x0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb3f4"></a> `00bbb3f4` | `a1 b7 ff b0` | adrp x1,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbb3f8"></a> `00bbb3f8` | `21 bc 1f 91` | add x1,x1,#0x7ef | `FALL_THROUGH`
<a id="insn-00bbb3fc"></a> `00bbb3fc` | `4d 7f 02 94` | bl 0x00c5b130 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb400"></a> `00bbb400` | `80 04 00 b4` | cbz x0,0x00bbb490 | `CONDITIONAL_JUMP`
<a id="insn-00bbb404"></a> `00bbb404` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb408"></a> `00bbb408` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbb40c"></a> `00bbb40c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbb410"></a> `00bbb410` | `3c 7f 02 94` | bl 0x00c5b100 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb414"></a> `00bbb414` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb418"></a> `00bbb418` | `36 7f 02 94` | bl 0x00c5b0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb41c"></a> `00bbb41c` | `e0 00 00 b4` | cbz x0,0x00bbb438 | `CONDITIONAL_JUMP`
<a id="insn-00bbb420"></a> `00bbb420` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bbb424"></a> `00bbb424` | `a0 03 02 d1` | sub x0,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb428"></a> `00bbb428` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bbb42c"></a> `00bbb42c` | `b9 86 02 94` | bl 0x00c5cf10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb430"></a> `00bbb430` | `b6 03 02 d1` | sub x22,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb434"></a> `00bbb434` | `03 00 00 14` | b 0x00bbb440 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb438"></a> `00bbb438` | `b6 03 02 d1` | sub x22,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb43c"></a> `00bbb43c` | `bf 03 18 78` | sturh wzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb440"></a> `00bbb440` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb444"></a> `00bbb444` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbb448"></a> `00bbb448` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bbb44c"></a> `00bbb44c` | `2d 7f 02 94` | bl 0x00c5b100 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb450"></a> `00bbb450` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb454"></a> `00bbb454` | `aa a7 78 a9` | ldp x10,x9,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00bbb458"></a> `00bbb458` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb45c"></a> `00bbb45c` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bbb460"></a> `00bbb460` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb464"></a> `00bbb464` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb468"></a> `00bbb468` | `20 15 96 9a` | csinc x0,x9,x22,ne | `FALL_THROUGH`
<a id="insn-00bbb46c"></a> `00bbb46c` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bbb470"></a> `00bbb470` | `2c 7f 02 94` | bl 0x00c5b120 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb474"></a> `00bbb474` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb478"></a> `00bbb478` | `a6 7f 02 94` | bl 0x00c5b310 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb47c"></a> `00bbb47c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bbb480"></a> `00bbb480` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb484"></a> `00bbb484` | `07 7f 02 94` | bl 0x00c5b0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb488"></a> `00bbb488` | `08 00 16 2a` | orr w8,w0,w22 | `FALL_THROUGH`
<a id="insn-00bbb48c"></a> `00bbb48c` | `e8 00 00 34` | cbz w8,0x00bbb4a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb490"></a> `00bbb490` | `00 b8 ff f0` | adrp x0,0x2be000 | `FALL_THROUGH`
<a id="insn-00bbb494"></a> `00bbb494` | `00 3c 24 91` | add x0,x0,#0x90f | `FALL_THROUGH`
<a id="insn-00bbb498"></a> `00bbb498` | `02 83 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb49c"></a> `00bbb49c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb4a0"></a> `00bbb4a0` | `95 02 f8 36` | tbz w21,#0x1f,0x00bbb4f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbb4a4"></a> `00bbb4a4` | `1b 00 00 14` | b 0x00bbb510 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb4a8"></a> `00bbb4a8` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb4ac"></a> `00bbb4ac` | `a9 83 58 f8` | ldur x9,[x29, #-0x78] | `FALL_THROUGH`
<a id="insn-00bbb4b0"></a> `00bbb4b0` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb4b4"></a> `00bbb4b4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb4b8"></a> `00bbb4b8` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbb4bc"></a> `00bbb4bc` | `68 01 00 b4` | cbz x8,0x00bbb4e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb4c0"></a> `00bbb4c0` | `e8 16 42 f9` | ldr x8,[x23, #0x428] | `FALL_THROUGH`
<a id="insn-00bbb4c4"></a> `00bbb4c4` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbb4c8"></a> `00bbb4c8` | `69 00 00 37` | tbnz w9,#0x0,0x00bbb4d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb4cc"></a> `00bbb4cc` | `00 05 00 91` | add x0,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb4d0"></a> `00bbb4d0` | `02 00 00 14` | b 0x00bbb4d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb4d4"></a> `00bbb4d4` | `00 09 40 f9` | ldr x0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb4d8"></a> `00bbb4d8` | `01 b8 ff b0` | adrp x1,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bbb4dc"></a> `00bbb4dc` | `21 b4 1f 91` | add x1,x1,#0x7ed | `FALL_THROUGH`
<a id="insn-00bbb4e0"></a> `00bbb4e0` | `14 7f 02 94` | bl 0x00c5b130 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4e4"></a> `00bbb4e4` | `ef 7e 02 94` | bl 0x00c5b0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4e8"></a> `00bbb4e8` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00bbb4ec"></a> `00bbb4ec` | `35 01 f8 37` | tbnz w21,#0x1f,0x00bbb510 | `CONDITIONAL_JUMP`
<a id="insn-00bbb4f0"></a> `00bbb4f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb4f4"></a> `00bbb4f4` | `83 7f 02 94` | bl 0x00c5b300 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb4f8"></a> `00bbb4f8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00bbb4fc"></a> `00bbb4fc` | `dd 7c 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb500"></a> `00bbb500` | `68 2b 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbb504"></a> `00bbb504` | `00 0d 42 f9` | ldr x0,[x8, #0x418] | `FALL_THROUGH`
<a id="insn-00bbb508"></a> `00bbb508` | `40 00 00 b4` | cbz x0,0x00bbb510 | `CONDITIONAL_JUMP`
<a id="insn-00bbb50c"></a> `00bbb50c` | `69 81 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb510"></a> `00bbb510` | `13 02 00 35` | cbnz w19,0x00bbb550 | `CONDITIONAL_JUMP`
<a id="insn-00bbb514"></a> `00bbb514` | `08 00 00 f0` | adrp x8,0xbbe000 | `FALL_THROUGH`
<a id="insn-00bbb518"></a> `00bbb518` | `09 00 00 f0` | adrp x9,0xbbe000 | `FALL_THROUGH`
<a id="insn-00bbb51c"></a> `00bbb51c` | `0a 00 00 f0` | adrp x10,0xbbe000 | `FALL_THROUGH`
<a id="insn-00bbb520"></a> `00bbb520` | `0b 00 00 f0` | adrp x11,0xbbe000 | `FALL_THROUGH`
<a id="insn-00bbb524"></a> `00bbb524` | `08 91 07 91` | add x8,x8,#0x1e4 | `FALL_THROUGH`
<a id="insn-00bbb528"></a> `00bbb528` | `29 a1 07 91` | add x9,x9,#0x1e8 | `FALL_THROUGH`
<a id="insn-00bbb52c"></a> `00bbb52c` | `4a 61 0e 91` | add x10,x10,#0x398 | `FALL_THROUGH`
<a id="insn-00bbb530"></a> `00bbb530` | `6b 01 10 91` | add x11,x11,#0x400 | `FALL_THROUGH`
<a id="insn-00bbb534"></a> `00bbb534` | `e8 7f 02 a9` | stp x8,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb538"></a> `00bbb538` | `e9 7f 03 a9` | stp x9,xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb53c"></a> `00bbb53c` | `ea 7f 04 a9` | stp x10,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb540"></a> `00bbb540` | `eb 7f 05 a9` | stp x11,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb544"></a> `00bbb544` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbb548"></a> `00bbb548` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00bbb54c"></a> `00bbb54c` | `29 8c 02 94` | bl 0x00c5e5f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb550"></a> `00bbb550` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00bbb554"></a> `00bbb554` | `68 00 00 36` | tbz w8,#0x0,0x00bbb560 | `CONDITIONAL_JUMP`
<a id="insn-00bbb558"></a> `00bbb558` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00bbb55c"></a> `00bbb55c` | `7d 76 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb560"></a> `00bbb560` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb564"></a> `00bbb564` | `a9 83 59 f8` | ldur x9,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00bbb568"></a> `00bbb568` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbb56c"></a> `00bbb56c` | `21 01 00 54` | b.ne 0x00bbb590 | `CONDITIONAL_JUMP`
<a id="insn-00bbb570"></a> `00bbb570` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00bbb574"></a> `00bbb574` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb578"></a> `00bbb578` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb57c"></a> `00bbb57c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb580"></a> `00bbb580` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb584"></a> `00bbb584` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb588"></a> `00bbb588` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bbb58c"></a> `00bbb58c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb590"></a> `00bbb590` | `7c 76 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaaa4`](#insn-00bbaaa4) 範囲 `[['00bbaaa4', '00bbaae7']]`
  - `CONDITIONAL_JUMP` [`00bbaae4`](#insn-00bbaae4) → [`00bbaaf4`](#insn-00bbaaf4)
  - `FALL_THROUGH` [`00bbaae4`](#insn-00bbaae4) → [`00bbaae8`](#insn-00bbaae8)
- ブロック [`00bbaae8`](#insn-00bbaae8) 範囲 `[['00bbaae8', '00bbaaf3']]`
  - `UNCONDITIONAL_JUMP` [`00bbaaf0`](#insn-00bbaaf0) → [`00bbaaf8`](#insn-00bbaaf8)
- ブロック [`00bbaaf4`](#insn-00bbaaf4) 範囲 `[['00bbaaf4', '00bbaaf7']]`
  - `FALL_THROUGH` [`00bbaaf4`](#insn-00bbaaf4) → [`00bbaaf8`](#insn-00bbaaf8)
- ブロック [`00bbaaf8`](#insn-00bbaaf8) 範囲 `[['00bbaaf8', '00bbab0b']]`
  - `CONDITIONAL_JUMP` [`00bbab08`](#insn-00bbab08) → [`00bbb560`](#insn-00bbb560)
  - `FALL_THROUGH` [`00bbab08`](#insn-00bbab08) → [`00bbab0c`](#insn-00bbab0c)
- ブロック [`00bbab0c`](#insn-00bbab0c) 範囲 `[['00bbab0c', '00bbab0f']]`
  - `CONDITIONAL_JUMP` [`00bbab0c`](#insn-00bbab0c) → [`00bbb560`](#insn-00bbb560)
  - `FALL_THROUGH` [`00bbab0c`](#insn-00bbab0c) → [`00bbab10`](#insn-00bbab10)
- ブロック [`00bbab10`](#insn-00bbab10) 範囲 `[['00bbab10', '00bbab1b']]`
  - `CONDITIONAL_JUMP` [`00bbab18`](#insn-00bbab18) → [`00bbb3a8`](#insn-00bbb3a8)
  - `FALL_THROUGH` [`00bbab18`](#insn-00bbab18) → [`00bbab1c`](#insn-00bbab1c)
- ブロック [`00bbab1c`](#insn-00bbab1c) 範囲 `[['00bbab1c', '00bbab23']]`
  - `CONDITIONAL_JUMP` [`00bbab20`](#insn-00bbab20) → [`00bbb3a8`](#insn-00bbb3a8)
  - `FALL_THROUGH` [`00bbab20`](#insn-00bbab20) → [`00bbab24`](#insn-00bbab24)
- ブロック [`00bbab24`](#insn-00bbab24) 範囲 `[['00bbab24', '00bbab2f']]`
  - `FALL_THROUGH` [`00bbab2c`](#insn-00bbab2c) → [`00bbab30`](#insn-00bbab30)
- ブロック [`00bbab30`](#insn-00bbab30) 範囲 `[['00bbab30', '00bbab37']]`
  - `FALL_THROUGH` [`00bbab34`](#insn-00bbab34) → [`00bbab38`](#insn-00bbab38)
- ブロック [`00bbab38`](#insn-00bbab38) 範囲 `[['00bbab38', '00bbab3f']]`
  - `CONDITIONAL_JUMP` [`00bbab3c`](#insn-00bbab3c) → [`00bbab60`](#insn-00bbab60)
  - `FALL_THROUGH` [`00bbab3c`](#insn-00bbab3c) → [`00bbab40`](#insn-00bbab40)
- ブロック [`00bbab40`](#insn-00bbab40) 範囲 `[['00bbab40', '00bbab5f']]`
  - `UNCONDITIONAL_JUMP` [`00bbab5c`](#insn-00bbab5c) → [`00bbab64`](#insn-00bbab64)
- ブロック [`00bbab60`](#insn-00bbab60) 範囲 `[['00bbab60', '00bbab63']]`
  - `FALL_THROUGH` [`00bbab60`](#insn-00bbab60) → [`00bbab64`](#insn-00bbab64)
- ブロック [`00bbab64`](#insn-00bbab64) 範囲 `[['00bbab64', '00bbab73']]`
  - `CONDITIONAL_JUMP` [`00bbab70`](#insn-00bbab70) → [`00bbb3a8`](#insn-00bbb3a8)
  - `FALL_THROUGH` [`00bbab70`](#insn-00bbab70) → [`00bbab74`](#insn-00bbab74)
- ブロック [`00bbab74`](#insn-00bbab74) 範囲 `[['00bbab74', '00bbab97']]`
  - `FALL_THROUGH` [`00bbab94`](#insn-00bbab94) → [`00bbab98`](#insn-00bbab98)
- ブロック [`00bbab98`](#insn-00bbab98) 範囲 `[['00bbab98', '00bbab9f']]`
  - `FALL_THROUGH` [`00bbab9c`](#insn-00bbab9c) → [`00bbaba0`](#insn-00bbaba0)
- ブロック [`00bbaba0`](#insn-00bbaba0) 範囲 `[['00bbaba0', '00bbaba3']]`
  - `FALL_THROUGH` [`00bbaba0`](#insn-00bbaba0) → [`00bbaba4`](#insn-00bbaba4)
- ブロック [`00bbaba4`](#insn-00bbaba4) 範囲 `[['00bbaba4', '00bbaba7']]`
  - `CONDITIONAL_JUMP` [`00bbaba4`](#insn-00bbaba4) → [`00bbb3a8`](#insn-00bbb3a8)
  - `FALL_THROUGH` [`00bbaba4`](#insn-00bbaba4) → [`00bbaba8`](#insn-00bbaba8)
- ブロック [`00bbaba8`](#insn-00bbaba8) 範囲 `[['00bbaba8', '00bbabc7']]`
  - `CONDITIONAL_JUMP` [`00bbabc4`](#insn-00bbabc4) → [`00bbb394`](#insn-00bbb394)
  - `FALL_THROUGH` [`00bbabc4`](#insn-00bbabc4) → [`00bbabc8`](#insn-00bbabc8)
- ブロック [`00bbabc8`](#insn-00bbabc8) 範囲 `[['00bbabc8', '00bbabdb']]`
  - `FALL_THROUGH` [`00bbabd8`](#insn-00bbabd8) → [`00bbabdc`](#insn-00bbabdc)
- ブロック [`00bbabdc`](#insn-00bbabdc) 範囲 `[['00bbabdc', '00bbac8b']]`
  - `CONDITIONAL_JUMP` [`00bbac88`](#insn-00bbac88) → [`00bbac94`](#insn-00bbac94)
  - `FALL_THROUGH` [`00bbac88`](#insn-00bbac88) → [`00bbac8c`](#insn-00bbac8c)
- ブロック [`00bbac8c`](#insn-00bbac8c) 範囲 `[['00bbac8c', '00bbac93']]`
  - `UNCONDITIONAL_JUMP` [`00bbac90`](#insn-00bbac90) → [`00bbacb4`](#insn-00bbacb4)
- ブロック [`00bbac94`](#insn-00bbac94) 範囲 `[['00bbac94', '00bbaca7']]`
  - `CONDITIONAL_JUMP` [`00bbaca4`](#insn-00bbaca4) → [`00bbacb4`](#insn-00bbacb4)
  - `FALL_THROUGH` [`00bbaca4`](#insn-00bbaca4) → [`00bbaca8`](#insn-00bbaca8)
- ブロック [`00bbaca8`](#insn-00bbaca8) 範囲 `[['00bbaca8', '00bbacb3']]`
  - `FALL_THROUGH` [`00bbacb0`](#insn-00bbacb0) → [`00bbacb4`](#insn-00bbacb4)
- ブロック [`00bbacb4`](#insn-00bbacb4) 範囲 `[['00bbacb4', '00bbacdb']]`
  - `CONDITIONAL_JUMP` [`00bbacd8`](#insn-00bbacd8) → [`00bbad78`](#insn-00bbad78)
  - `FALL_THROUGH` [`00bbacd8`](#insn-00bbacd8) → [`00bbacdc`](#insn-00bbacdc)
- ブロック [`00bbacdc`](#insn-00bbacdc) 範囲 `[['00bbacdc', '00bbad2f']]`
  - `FALL_THROUGH` [`00bbad2c`](#insn-00bbad2c) → [`00bbad30`](#insn-00bbad30)
- ブロック [`00bbad30`](#insn-00bbad30) 範囲 `[['00bbad30', '00bbad3f']]`
  - `CONDITIONAL_JUMP` [`00bbad3c`](#insn-00bbad3c) → [`00bbad48`](#insn-00bbad48)
  - `FALL_THROUGH` [`00bbad3c`](#insn-00bbad3c) → [`00bbad40`](#insn-00bbad40)
- ブロック [`00bbad40`](#insn-00bbad40) 範囲 `[['00bbad40', '00bbad47']]`
  - `UNCONDITIONAL_JUMP` [`00bbad44`](#insn-00bbad44) → [`00bbad68`](#insn-00bbad68)
- ブロック [`00bbad48`](#insn-00bbad48) 範囲 `[['00bbad48', '00bbad5b']]`
  - `CONDITIONAL_JUMP` [`00bbad58`](#insn-00bbad58) → [`00bbad68`](#insn-00bbad68)
  - `FALL_THROUGH` [`00bbad58`](#insn-00bbad58) → [`00bbad5c`](#insn-00bbad5c)
- ブロック [`00bbad5c`](#insn-00bbad5c) 範囲 `[['00bbad5c', '00bbad67']]`
  - `FALL_THROUGH` [`00bbad64`](#insn-00bbad64) → [`00bbad68`](#insn-00bbad68)
- ブロック [`00bbad68`](#insn-00bbad68) 範囲 `[['00bbad68', '00bbad77']]`
  - `FALL_THROUGH` [`00bbad74`](#insn-00bbad74) → [`00bbad78`](#insn-00bbad78)
- ブロック [`00bbad78`](#insn-00bbad78) 範囲 `[['00bbad78', '00bbadb7']]`
  - `FALL_THROUGH` [`00bbadb4`](#insn-00bbadb4) → [`00bbadb8`](#insn-00bbadb8)
- ブロック [`00bbadb8`](#insn-00bbadb8) 範囲 `[['00bbadb8', '00bbaddb']]`
  - `CONDITIONAL_JUMP` [`00bbadd8`](#insn-00bbadd8) → [`00bbade4`](#insn-00bbade4)
  - `FALL_THROUGH` [`00bbadd8`](#insn-00bbadd8) → [`00bbaddc`](#insn-00bbaddc)
- ブロック [`00bbaddc`](#insn-00bbaddc) 範囲 `[['00bbaddc', '00bbade3']]`
  - `UNCONDITIONAL_JUMP` [`00bbade0`](#insn-00bbade0) → [`00bbae04`](#insn-00bbae04)
- ブロック [`00bbade4`](#insn-00bbade4) 範囲 `[['00bbade4', '00bbadf7']]`
  - `CONDITIONAL_JUMP` [`00bbadf4`](#insn-00bbadf4) → [`00bbae04`](#insn-00bbae04)
  - `FALL_THROUGH` [`00bbadf4`](#insn-00bbadf4) → [`00bbadf8`](#insn-00bbadf8)
- ブロック [`00bbadf8`](#insn-00bbadf8) 範囲 `[['00bbadf8', '00bbae03']]`
  - `FALL_THROUGH` [`00bbae00`](#insn-00bbae00) → [`00bbae04`](#insn-00bbae04)
- ブロック [`00bbae04`](#insn-00bbae04) 範囲 `[['00bbae04', '00bbae2b']]`
  - `CONDITIONAL_JUMP` [`00bbae28`](#insn-00bbae28) → [`00bbb378`](#insn-00bbb378)
  - `FALL_THROUGH` [`00bbae28`](#insn-00bbae28) → [`00bbae2c`](#insn-00bbae2c)
- ブロック [`00bbae2c`](#insn-00bbae2c) 範囲 `[['00bbae2c', '00bbae43']]`
  - `CONDITIONAL_JUMP` [`00bbae40`](#insn-00bbae40) → [`00bbb378`](#insn-00bbb378)
  - `FALL_THROUGH` [`00bbae40`](#insn-00bbae40) → [`00bbae44`](#insn-00bbae44)
- ブロック [`00bbae44`](#insn-00bbae44) 範囲 `[['00bbae44', '00bbae9b']]`
  - `FALL_THROUGH` [`00bbae98`](#insn-00bbae98) → [`00bbae9c`](#insn-00bbae9c)
- ブロック [`00bbae9c`](#insn-00bbae9c) 範囲 `[['00bbae9c', '00bbaeaf']]`
  - `CONDITIONAL_JUMP` [`00bbaeac`](#insn-00bbaeac) → [`00bbaeb8`](#insn-00bbaeb8)
  - `FALL_THROUGH` [`00bbaeac`](#insn-00bbaeac) → [`00bbaeb0`](#insn-00bbaeb0)
- ブロック [`00bbaeb0`](#insn-00bbaeb0) 範囲 `[['00bbaeb0', '00bbaeb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbaeb4`](#insn-00bbaeb4) → [`00bbaed8`](#insn-00bbaed8)
- ブロック [`00bbaeb8`](#insn-00bbaeb8) 範囲 `[['00bbaeb8', '00bbaecb']]`
  - `CONDITIONAL_JUMP` [`00bbaec8`](#insn-00bbaec8) → [`00bbaed8`](#insn-00bbaed8)
  - `FALL_THROUGH` [`00bbaec8`](#insn-00bbaec8) → [`00bbaecc`](#insn-00bbaecc)
- ブロック [`00bbaecc`](#insn-00bbaecc) 範囲 `[['00bbaecc', '00bbaed7']]`
  - `FALL_THROUGH` [`00bbaed4`](#insn-00bbaed4) → [`00bbaed8`](#insn-00bbaed8)
- ブロック [`00bbaed8`](#insn-00bbaed8) 範囲 `[['00bbaed8', '00bbaf53']]`
  - `CONDITIONAL_JUMP` [`00bbaf50`](#insn-00bbaf50) → [`00bbaf5c`](#insn-00bbaf5c)
  - `FALL_THROUGH` [`00bbaf50`](#insn-00bbaf50) → [`00bbaf54`](#insn-00bbaf54)
- ブロック [`00bbaf54`](#insn-00bbaf54) 範囲 `[['00bbaf54', '00bbaf5b']]`
  - `UNCONDITIONAL_JUMP` [`00bbaf58`](#insn-00bbaf58) → [`00bbaf7c`](#insn-00bbaf7c)
- ブロック [`00bbaf5c`](#insn-00bbaf5c) 範囲 `[['00bbaf5c', '00bbaf6f']]`
  - `CONDITIONAL_JUMP` [`00bbaf6c`](#insn-00bbaf6c) → [`00bbaf7c`](#insn-00bbaf7c)
  - `FALL_THROUGH` [`00bbaf6c`](#insn-00bbaf6c) → [`00bbaf70`](#insn-00bbaf70)
- ブロック [`00bbaf70`](#insn-00bbaf70) 範囲 `[['00bbaf70', '00bbaf7b']]`
  - `FALL_THROUGH` [`00bbaf78`](#insn-00bbaf78) → [`00bbaf7c`](#insn-00bbaf7c)
- ブロック [`00bbaf7c`](#insn-00bbaf7c) 範囲 `[['00bbaf7c', '00bbaf7f']]`
  - `FALL_THROUGH` [`00bbaf7c`](#insn-00bbaf7c) → [`00bbaf80`](#insn-00bbaf80)
- ブロック [`00bbaf80`](#insn-00bbaf80) 範囲 `[['00bbaf80', '00bbafeb']]`
  - `FALL_THROUGH` [`00bbafe8`](#insn-00bbafe8) → [`00bbafec`](#insn-00bbafec)
- ブロック [`00bbafec`](#insn-00bbafec) 範囲 `[['00bbafec', '00bbaff7']]`
  - `CONDITIONAL_JUMP` [`00bbaff4`](#insn-00bbaff4) → [`00bbb000`](#insn-00bbb000)
  - `FALL_THROUGH` [`00bbaff4`](#insn-00bbaff4) → [`00bbaff8`](#insn-00bbaff8)
- ブロック [`00bbaff8`](#insn-00bbaff8) 範囲 `[['00bbaff8', '00bbafff']]`
  - `UNCONDITIONAL_JUMP` [`00bbaffc`](#insn-00bbaffc) → [`00bbb020`](#insn-00bbb020)
- ブロック [`00bbb000`](#insn-00bbb000) 範囲 `[['00bbb000', '00bbb013']]`
  - `CONDITIONAL_JUMP` [`00bbb010`](#insn-00bbb010) → [`00bbb020`](#insn-00bbb020)
  - `FALL_THROUGH` [`00bbb010`](#insn-00bbb010) → [`00bbb014`](#insn-00bbb014)
- ブロック [`00bbb014`](#insn-00bbb014) 範囲 `[['00bbb014', '00bbb017']]`
  - `FALL_THROUGH` [`00bbb014`](#insn-00bbb014) → [`00bbb018`](#insn-00bbb018)
- ブロック [`00bbb018`](#insn-00bbb018) 範囲 `[['00bbb018', '00bbb01f']]`
  - `FALL_THROUGH` [`00bbb01c`](#insn-00bbb01c) → [`00bbb020`](#insn-00bbb020)
- ブロック [`00bbb020`](#insn-00bbb020) 範囲 `[['00bbb020', '00bbb023']]`
  - `FALL_THROUGH` [`00bbb020`](#insn-00bbb020) → [`00bbb024`](#insn-00bbb024)
- ブロック [`00bbb024`](#insn-00bbb024) 範囲 `[['00bbb024', '00bbb02f']]`
  - `FALL_THROUGH` [`00bbb02c`](#insn-00bbb02c) → [`00bbb030`](#insn-00bbb030)
- ブロック [`00bbb030`](#insn-00bbb030) 範囲 `[['00bbb030', '00bbb03b']]`
  - `FALL_THROUGH` [`00bbb038`](#insn-00bbb038) → [`00bbb03c`](#insn-00bbb03c)
- ブロック [`00bbb03c`](#insn-00bbb03c) 範囲 `[['00bbb03c', '00bbb087']]`
  - `CONDITIONAL_JUMP` [`00bbb084`](#insn-00bbb084) → [`00bbb2c8`](#insn-00bbb2c8)
  - `FALL_THROUGH` [`00bbb084`](#insn-00bbb084) → [`00bbb088`](#insn-00bbb088)
- ブロック [`00bbb088`](#insn-00bbb088) 範囲 `[['00bbb088', '00bbb09f']]`
  - `FALL_THROUGH` [`00bbb09c`](#insn-00bbb09c) → [`00bbb0a0`](#insn-00bbb0a0)
- ブロック [`00bbb0a0`](#insn-00bbb0a0) 範囲 `[['00bbb0a0', '00bbb0a3']]`
  - `FALL_THROUGH` [`00bbb0a0`](#insn-00bbb0a0) → [`00bbb0a4`](#insn-00bbb0a4)
- ブロック [`00bbb0a4`](#insn-00bbb0a4) 範囲 `[['00bbb0a4', '00bbb0fb']]`
  - `CONDITIONAL_JUMP` [`00bbb0f8`](#insn-00bbb0f8) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb0f8`](#insn-00bbb0f8) → [`00bbb0fc`](#insn-00bbb0fc)
- ブロック [`00bbb0fc`](#insn-00bbb0fc) 範囲 `[['00bbb0fc', '00bbb11b']]`
  - `CONDITIONAL_JUMP` [`00bbb118`](#insn-00bbb118) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb118`](#insn-00bbb118) → [`00bbb11c`](#insn-00bbb11c)
- ブロック [`00bbb11c`](#insn-00bbb11c) 範囲 `[['00bbb11c', '00bbb127']]`
  - `FALL_THROUGH` [`00bbb124`](#insn-00bbb124) → [`00bbb128`](#insn-00bbb128)
- ブロック [`00bbb128`](#insn-00bbb128) 範囲 `[['00bbb128', '00bbb12f']]`
  - `CONDITIONAL_JUMP` [`00bbb12c`](#insn-00bbb12c) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb12c`](#insn-00bbb12c) → [`00bbb130`](#insn-00bbb130)
- ブロック [`00bbb130`](#insn-00bbb130) 範囲 `[['00bbb130', '00bbb143']]`
  - `CONDITIONAL_JUMP` [`00bbb140`](#insn-00bbb140) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb140`](#insn-00bbb140) → [`00bbb144`](#insn-00bbb144)
- ブロック [`00bbb144`](#insn-00bbb144) 範囲 `[['00bbb144', '00bbb157']]`
  - `CONDITIONAL_JUMP` [`00bbb154`](#insn-00bbb154) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb154`](#insn-00bbb154) → [`00bbb158`](#insn-00bbb158)
- ブロック [`00bbb158`](#insn-00bbb158) 範囲 `[['00bbb158', '00bbb19b']]`
  - `FALL_THROUGH` [`00bbb198`](#insn-00bbb198) → [`00bbb19c`](#insn-00bbb19c)
- ブロック [`00bbb19c`](#insn-00bbb19c) 範囲 `[['00bbb19c', '00bbb1ab']]`
  - `CONDITIONAL_JUMP` [`00bbb1a8`](#insn-00bbb1a8) → [`00bbb210`](#insn-00bbb210)
  - `FALL_THROUGH` [`00bbb1a8`](#insn-00bbb1a8) → [`00bbb1ac`](#insn-00bbb1ac)
- ブロック [`00bbb1ac`](#insn-00bbb1ac) 範囲 `[['00bbb1ac', '00bbb1eb']]`
  - `CONDITIONAL_JUMP` [`00bbb1e8`](#insn-00bbb1e8) → [`00bbb1f8`](#insn-00bbb1f8)
  - `FALL_THROUGH` [`00bbb1e8`](#insn-00bbb1e8) → [`00bbb1ec`](#insn-00bbb1ec)
- ブロック [`00bbb1ec`](#insn-00bbb1ec) 範囲 `[['00bbb1ec', '00bbb1f7']]`
  - `UNCONDITIONAL_JUMP` [`00bbb1f4`](#insn-00bbb1f4) → [`00bbb1fc`](#insn-00bbb1fc)
- ブロック [`00bbb1f8`](#insn-00bbb1f8) 範囲 `[['00bbb1f8', '00bbb1fb']]`
  - `FALL_THROUGH` [`00bbb1f8`](#insn-00bbb1f8) → [`00bbb1fc`](#insn-00bbb1fc)
- ブロック [`00bbb1fc`](#insn-00bbb1fc) 範囲 `[['00bbb1fc', '00bbb20f']]`
  - `FALL_THROUGH` [`00bbb20c`](#insn-00bbb20c) → [`00bbb210`](#insn-00bbb210)
- ブロック [`00bbb210`](#insn-00bbb210) 範囲 `[['00bbb210', '00bbb21b']]`
  - `CONDITIONAL_JUMP` [`00bbb218`](#insn-00bbb218) → [`00bbb224`](#insn-00bbb224)
  - `FALL_THROUGH` [`00bbb218`](#insn-00bbb218) → [`00bbb21c`](#insn-00bbb21c)
- ブロック [`00bbb21c`](#insn-00bbb21c) 範囲 `[['00bbb21c', '00bbb223']]`
  - `UNCONDITIONAL_JUMP` [`00bbb220`](#insn-00bbb220) → [`00bbb244`](#insn-00bbb244)
- ブロック [`00bbb224`](#insn-00bbb224) 範囲 `[['00bbb224', '00bbb237']]`
  - `CONDITIONAL_JUMP` [`00bbb234`](#insn-00bbb234) → [`00bbb244`](#insn-00bbb244)
  - `FALL_THROUGH` [`00bbb234`](#insn-00bbb234) → [`00bbb238`](#insn-00bbb238)
- ブロック [`00bbb238`](#insn-00bbb238) 範囲 `[['00bbb238', '00bbb243']]`
  - `FALL_THROUGH` [`00bbb240`](#insn-00bbb240) → [`00bbb244`](#insn-00bbb244)
- ブロック [`00bbb244`](#insn-00bbb244) 範囲 `[['00bbb244', '00bbb263']]`
  - `CONDITIONAL_JUMP` [`00bbb260`](#insn-00bbb260) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb260`](#insn-00bbb260) → [`00bbb264`](#insn-00bbb264)
- ブロック [`00bbb264`](#insn-00bbb264) 範囲 `[['00bbb264', '00bbb273']]`
  - `CONDITIONAL_JUMP` [`00bbb270`](#insn-00bbb270) → [`00bbb27c`](#insn-00bbb27c)
  - `FALL_THROUGH` [`00bbb270`](#insn-00bbb270) → [`00bbb274`](#insn-00bbb274)
- ブロック [`00bbb274`](#insn-00bbb274) 範囲 `[['00bbb274', '00bbb27b']]`
  - `FALL_THROUGH` [`00bbb278`](#insn-00bbb278) → [`00bbb27c`](#insn-00bbb27c)
- ブロック [`00bbb27c`](#insn-00bbb27c) 範囲 `[['00bbb27c', '00bbb293']]`
  - `FALL_THROUGH` [`00bbb290`](#insn-00bbb290) → [`00bbb294`](#insn-00bbb294)
- ブロック [`00bbb294`](#insn-00bbb294) 範囲 `[['00bbb294', '00bbb2c7']]`
  - `CONDITIONAL_JUMP` [`00bbb2c4`](#insn-00bbb2c4) → [`00bbb0a4`](#insn-00bbb0a4)
  - `FALL_THROUGH` [`00bbb2c4`](#insn-00bbb2c4) → [`00bbb2c8`](#insn-00bbb2c8)
- ブロック [`00bbb2c8`](#insn-00bbb2c8) 範囲 `[['00bbb2c8', '00bbb323']]`
  - `FALL_THROUGH` [`00bbb320`](#insn-00bbb320) → [`00bbb324`](#insn-00bbb324)
- ブロック [`00bbb324`](#insn-00bbb324) 範囲 `[['00bbb324', '00bbb333']]`
  - `CONDITIONAL_JUMP` [`00bbb330`](#insn-00bbb330) → [`00bbb33c`](#insn-00bbb33c)
  - `FALL_THROUGH` [`00bbb330`](#insn-00bbb330) → [`00bbb334`](#insn-00bbb334)
- ブロック [`00bbb334`](#insn-00bbb334) 範囲 `[['00bbb334', '00bbb33b']]`
  - `UNCONDITIONAL_JUMP` [`00bbb338`](#insn-00bbb338) → [`00bbb35c`](#insn-00bbb35c)
- ブロック [`00bbb33c`](#insn-00bbb33c) 範囲 `[['00bbb33c', '00bbb34f']]`
  - `CONDITIONAL_JUMP` [`00bbb34c`](#insn-00bbb34c) → [`00bbb35c`](#insn-00bbb35c)
  - `FALL_THROUGH` [`00bbb34c`](#insn-00bbb34c) → [`00bbb350`](#insn-00bbb350)
- ブロック [`00bbb350`](#insn-00bbb350) 範囲 `[['00bbb350', '00bbb35b']]`
  - `FALL_THROUGH` [`00bbb358`](#insn-00bbb358) → [`00bbb35c`](#insn-00bbb35c)
- ブロック [`00bbb35c`](#insn-00bbb35c) 範囲 `[['00bbb35c', '00bbb377']]`
  - `FALL_THROUGH` [`00bbb374`](#insn-00bbb374) → [`00bbb378`](#insn-00bbb378)
- ブロック [`00bbb378`](#insn-00bbb378) 範囲 `[['00bbb378', '00bbb393']]`
  - `FALL_THROUGH` [`00bbb390`](#insn-00bbb390) → [`00bbb394`](#insn-00bbb394)
- ブロック [`00bbb394`](#insn-00bbb394) 範囲 `[['00bbb394', '00bbb397']]`
  - `FALL_THROUGH` [`00bbb394`](#insn-00bbb394) → [`00bbb398`](#insn-00bbb398)
- ブロック [`00bbb398`](#insn-00bbb398) 範囲 `[['00bbb398', '00bbb3a7']]`
  - `FALL_THROUGH` [`00bbb3a4`](#insn-00bbb3a4) → [`00bbb3a8`](#insn-00bbb3a8)
- ブロック [`00bbb3a8`](#insn-00bbb3a8) 範囲 `[['00bbb3a8', '00bbb3bf']]`
  - `CONDITIONAL_JUMP` [`00bbb3bc`](#insn-00bbb3bc) → [`00bbb3c8`](#insn-00bbb3c8)
  - `FALL_THROUGH` [`00bbb3bc`](#insn-00bbb3bc) → [`00bbb3c0`](#insn-00bbb3c0)
- ブロック [`00bbb3c0`](#insn-00bbb3c0) 範囲 `[['00bbb3c0', '00bbb3c7']]`
  - `UNCONDITIONAL_JUMP` [`00bbb3c4`](#insn-00bbb3c4) → [`00bbb3cc`](#insn-00bbb3cc)
- ブロック [`00bbb3c8`](#insn-00bbb3c8) 範囲 `[['00bbb3c8', '00bbb3cb']]`
  - `FALL_THROUGH` [`00bbb3c8`](#insn-00bbb3c8) → [`00bbb3cc`](#insn-00bbb3cc)
- ブロック [`00bbb3cc`](#insn-00bbb3cc) 範囲 `[['00bbb3cc', '00bbb3e7']]`
  - `CONDITIONAL_JUMP` [`00bbb3e4`](#insn-00bbb3e4) → [`00bbb3f0`](#insn-00bbb3f0)
  - `FALL_THROUGH` [`00bbb3e4`](#insn-00bbb3e4) → [`00bbb3e8`](#insn-00bbb3e8)
- ブロック [`00bbb3e8`](#insn-00bbb3e8) 範囲 `[['00bbb3e8', '00bbb3ef']]`
  - `UNCONDITIONAL_JUMP` [`00bbb3ec`](#insn-00bbb3ec) → [`00bbb3f4`](#insn-00bbb3f4)
- ブロック [`00bbb3f0`](#insn-00bbb3f0) 範囲 `[['00bbb3f0', '00bbb3f3']]`
  - `FALL_THROUGH` [`00bbb3f0`](#insn-00bbb3f0) → [`00bbb3f4`](#insn-00bbb3f4)
- ブロック [`00bbb3f4`](#insn-00bbb3f4) 範囲 `[['00bbb3f4', '00bbb403']]`
  - `CONDITIONAL_JUMP` [`00bbb400`](#insn-00bbb400) → [`00bbb490`](#insn-00bbb490)
  - `FALL_THROUGH` [`00bbb400`](#insn-00bbb400) → [`00bbb404`](#insn-00bbb404)
- ブロック [`00bbb404`](#insn-00bbb404) 範囲 `[['00bbb404', '00bbb40b']]`
  - `FALL_THROUGH` [`00bbb408`](#insn-00bbb408) → [`00bbb40c`](#insn-00bbb40c)
- ブロック [`00bbb40c`](#insn-00bbb40c) 範囲 `[['00bbb40c', '00bbb41f']]`
  - `CONDITIONAL_JUMP` [`00bbb41c`](#insn-00bbb41c) → [`00bbb438`](#insn-00bbb438)
  - `FALL_THROUGH` [`00bbb41c`](#insn-00bbb41c) → [`00bbb420`](#insn-00bbb420)
- ブロック [`00bbb420`](#insn-00bbb420) 範囲 `[['00bbb420', '00bbb437']]`
  - `UNCONDITIONAL_JUMP` [`00bbb434`](#insn-00bbb434) → [`00bbb440`](#insn-00bbb440)
- ブロック [`00bbb438`](#insn-00bbb438) 範囲 `[['00bbb438', '00bbb43f']]`
  - `FALL_THROUGH` [`00bbb43c`](#insn-00bbb43c) → [`00bbb440`](#insn-00bbb440)
- ブロック [`00bbb440`](#insn-00bbb440) 範囲 `[['00bbb440', '00bbb48f']]`
  - `CONDITIONAL_JUMP` [`00bbb48c`](#insn-00bbb48c) → [`00bbb4a8`](#insn-00bbb4a8)
  - `FALL_THROUGH` [`00bbb48c`](#insn-00bbb48c) → [`00bbb490`](#insn-00bbb490)
- ブロック [`00bbb490`](#insn-00bbb490) 範囲 `[['00bbb490', '00bbb4a3']]`
  - `CONDITIONAL_JUMP` [`00bbb4a0`](#insn-00bbb4a0) → [`00bbb4f0`](#insn-00bbb4f0)
  - `FALL_THROUGH` [`00bbb4a0`](#insn-00bbb4a0) → [`00bbb4a4`](#insn-00bbb4a4)
- ブロック [`00bbb4a4`](#insn-00bbb4a4) 範囲 `[['00bbb4a4', '00bbb4a7']]`
  - `UNCONDITIONAL_JUMP` [`00bbb4a4`](#insn-00bbb4a4) → [`00bbb510`](#insn-00bbb510)
- ブロック [`00bbb4a8`](#insn-00bbb4a8) 範囲 `[['00bbb4a8', '00bbb4bf']]`
  - `CONDITIONAL_JUMP` [`00bbb4bc`](#insn-00bbb4bc) → [`00bbb4e8`](#insn-00bbb4e8)
  - `FALL_THROUGH` [`00bbb4bc`](#insn-00bbb4bc) → [`00bbb4c0`](#insn-00bbb4c0)
- ブロック [`00bbb4c0`](#insn-00bbb4c0) 範囲 `[['00bbb4c0', '00bbb4cb']]`
  - `CONDITIONAL_JUMP` [`00bbb4c8`](#insn-00bbb4c8) → [`00bbb4d4`](#insn-00bbb4d4)
  - `FALL_THROUGH` [`00bbb4c8`](#insn-00bbb4c8) → [`00bbb4cc`](#insn-00bbb4cc)
- ブロック [`00bbb4cc`](#insn-00bbb4cc) 範囲 `[['00bbb4cc', '00bbb4d3']]`
  - `UNCONDITIONAL_JUMP` [`00bbb4d0`](#insn-00bbb4d0) → [`00bbb4d8`](#insn-00bbb4d8)
- ブロック [`00bbb4d4`](#insn-00bbb4d4) 範囲 `[['00bbb4d4', '00bbb4d7']]`
  - `FALL_THROUGH` [`00bbb4d4`](#insn-00bbb4d4) → [`00bbb4d8`](#insn-00bbb4d8)
- ブロック [`00bbb4d8`](#insn-00bbb4d8) 範囲 `[['00bbb4d8', '00bbb4e7']]`
  - `FALL_THROUGH` [`00bbb4e4`](#insn-00bbb4e4) → [`00bbb4e8`](#insn-00bbb4e8)
- ブロック [`00bbb4e8`](#insn-00bbb4e8) 範囲 `[['00bbb4e8', '00bbb4ef']]`
  - `CONDITIONAL_JUMP` [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb510`](#insn-00bbb510)
  - `FALL_THROUGH` [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb4f0`](#insn-00bbb4f0)
- ブロック [`00bbb4f0`](#insn-00bbb4f0) 範囲 `[['00bbb4f0', '00bbb503']]`
  - `FALL_THROUGH` [`00bbb500`](#insn-00bbb500) → [`00bbb504`](#insn-00bbb504)
- ブロック [`00bbb504`](#insn-00bbb504) 範囲 `[['00bbb504', '00bbb507']]`
  - `FALL_THROUGH` [`00bbb504`](#insn-00bbb504) → [`00bbb508`](#insn-00bbb508)
- ブロック [`00bbb508`](#insn-00bbb508) 範囲 `[['00bbb508', '00bbb50b']]`
  - `CONDITIONAL_JUMP` [`00bbb508`](#insn-00bbb508) → [`00bbb510`](#insn-00bbb510)
  - `FALL_THROUGH` [`00bbb508`](#insn-00bbb508) → [`00bbb50c`](#insn-00bbb50c)
- ブロック [`00bbb50c`](#insn-00bbb50c) 範囲 `[['00bbb50c', '00bbb50f']]`
  - `FALL_THROUGH` [`00bbb50c`](#insn-00bbb50c) → [`00bbb510`](#insn-00bbb510)
- ブロック [`00bbb510`](#insn-00bbb510) 範囲 `[['00bbb510', '00bbb513']]`
  - `CONDITIONAL_JUMP` [`00bbb510`](#insn-00bbb510) → [`00bbb550`](#insn-00bbb550)
  - `FALL_THROUGH` [`00bbb510`](#insn-00bbb510) → [`00bbb514`](#insn-00bbb514)
- ブロック [`00bbb514`](#insn-00bbb514) 範囲 `[['00bbb514', '00bbb517']]`
  - `FALL_THROUGH` [`00bbb514`](#insn-00bbb514) → [`00bbb518`](#insn-00bbb518)
- ブロック [`00bbb518`](#insn-00bbb518) 範囲 `[['00bbb518', '00bbb527']]`
  - `FALL_THROUGH` [`00bbb524`](#insn-00bbb524) → [`00bbb528`](#insn-00bbb528)
- ブロック [`00bbb528`](#insn-00bbb528) 範囲 `[['00bbb528', '00bbb537']]`
  - `FALL_THROUGH` [`00bbb534`](#insn-00bbb534) → [`00bbb538`](#insn-00bbb538)
- ブロック [`00bbb538`](#insn-00bbb538) 範囲 `[['00bbb538', '00bbb53f']]`
  - `FALL_THROUGH` [`00bbb53c`](#insn-00bbb53c) → [`00bbb540`](#insn-00bbb540)
- ブロック [`00bbb540`](#insn-00bbb540) 範囲 `[['00bbb540', '00bbb543']]`
  - `FALL_THROUGH` [`00bbb540`](#insn-00bbb540) → [`00bbb544`](#insn-00bbb544)
- ブロック [`00bbb544`](#insn-00bbb544) 範囲 `[['00bbb544', '00bbb547']]`
  - `FALL_THROUGH` [`00bbb544`](#insn-00bbb544) → [`00bbb548`](#insn-00bbb548)
- ブロック [`00bbb548`](#insn-00bbb548) 範囲 `[['00bbb548', '00bbb54b']]`
  - `FALL_THROUGH` [`00bbb548`](#insn-00bbb548) → [`00bbb54c`](#insn-00bbb54c)
- ブロック [`00bbb54c`](#insn-00bbb54c) 範囲 `[['00bbb54c', '00bbb54f']]`
  - `FALL_THROUGH` [`00bbb54c`](#insn-00bbb54c) → [`00bbb550`](#insn-00bbb550)
- ブロック [`00bbb550`](#insn-00bbb550) 範囲 `[['00bbb550', '00bbb557']]`
  - `CONDITIONAL_JUMP` [`00bbb554`](#insn-00bbb554) → [`00bbb560`](#insn-00bbb560)
  - `FALL_THROUGH` [`00bbb554`](#insn-00bbb554) → [`00bbb558`](#insn-00bbb558)
- ブロック [`00bbb558`](#insn-00bbb558) 範囲 `[['00bbb558', '00bbb55f']]`
  - `FALL_THROUGH` [`00bbb55c`](#insn-00bbb55c) → [`00bbb560`](#insn-00bbb560)
- ブロック [`00bbb560`](#insn-00bbb560) 範囲 `[['00bbb560', '00bbb56f']]`
  - `CONDITIONAL_JUMP` [`00bbb56c`](#insn-00bbb56c) → [`00bbb590`](#insn-00bbb590)
  - `FALL_THROUGH` [`00bbb56c`](#insn-00bbb56c) → [`00bbb570`](#insn-00bbb570)
- ブロック [`00bbb570`](#insn-00bbb570) 範囲 `[['00bbb570', '00bbb58b']]`
  - `FALL_THROUGH` [`00bbb588`](#insn-00bbb588) → [`00bbb58c`](#insn-00bbb58c)
- ブロック [`00bbb58c`](#insn-00bbb58c) 範囲 `[['00bbb58c', '00bbb58f']]`
- ブロック [`00bbb590`](#insn-00bbb590) 範囲 `[['00bbb590', '00bbb593']]`

## 命令位置別の参照

- [`00bbaaa4`](#insn-00bbaaa4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaa8`](#insn-00bbaaa8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaac`](#insn-00bbaaac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaab0`](#insn-00bbaab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaab4`](#insn-00bbaab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaab8`](#insn-00bbaab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaad0`](#insn-00bbaad0) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaad4`](#insn-00bbaad4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaad8`](#insn-00bbaad8) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaae0`](#insn-00bbaae0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbaae4`](#insn-00bbaae4) → [`00bbaaf4`](#insn-00bbaaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaae8`](#insn-00bbaae8) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bbaaf0`](#insn-00bbaaf0) → [`00bbaaf8`](#insn-00bbaaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaafc`](#insn-00bbaafc) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab00`](#insn-00bbab00) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab04`](#insn-00bbab04) → [`00c5e340`](../00c5e/00c5e340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e340` · 推定シンボル `None` · 推定型 `None`
- [`00bbab08`](#insn-00bbab08) → [`00bbb560`](#insn-00bbb560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab0c`](#insn-00bbab0c) → [`00bbb560`](#insn-00bbb560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab14`](#insn-00bbab14) → `01127448`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbab18`](#insn-00bbab18) → [`00bbb3a8`](#insn-00bbb3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab1c`](#insn-00bbab1c) → [`00c5e340`](../00c5e/00c5e340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e340` · 推定シンボル `None` · 推定型 `None`
- [`00bbab20`](#insn-00bbab20) → [`00bbb3a8`](#insn-00bbb3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab2c`](#insn-00bbab2c) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab30`](#insn-00bbab30) → `01127448`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbab34`](#insn-00bbab34) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab38`](#insn-00bbab38) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbab3c`](#insn-00bbab3c) → [`00bbab60`](#insn-00bbab60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab5c`](#insn-00bbab5c) → [`00bbab64`](#insn-00bbab64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab68`](#insn-00bbab68) → `01127318`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab6c`](#insn-00bbab6c) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab70`](#insn-00bbab70) → [`00bbb3a8`](#insn-00bbb3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbab78`](#insn-00bbab78) → [`00c5c5f0`](../00c5c/00c5c5f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbab88`](#insn-00bbab88) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbaba4`](#insn-00bbaba4) → [`00bbb3a8`](#insn-00bbb3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabac`](#insn-00bbabac) → [`00c5c5d0`](../00c5c/00c5c5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbabbc`](#insn-00bbabbc) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc0`](#insn-00bbabc0) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc4`](#insn-00bbabc4) → [`00bbb394`](#insn-00bbb394) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabdc`](#insn-00bbabdc) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabe0`](#insn-00bbabe0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabe4`](#insn-00bbabe4) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabe8`](#insn-00bbabe8) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabec`](#insn-00bbabec) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf0`](#insn-00bbabf0) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf4`](#insn-00bbabf4) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf8`](#insn-00bbabf8) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabfc`](#insn-00bbabfc) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac00`](#insn-00bbac00) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac04`](#insn-00bbac04) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac08`](#insn-00bbac08) → `Stack[-0xff]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac0c`](#insn-00bbac0c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac10`](#insn-00bbac10) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac14`](#insn-00bbac14) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac20`](#insn-00bbac20) → `Stack[-0x200]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac2c`](#insn-00bbac2c) → `0030e8cd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbac40`](#insn-00bbac40) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbac54`](#insn-00bbac54) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbac64`](#insn-00bbac64) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbac7c`](#insn-00bbac7c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac88`](#insn-00bbac88) → [`00bbac94`](#insn-00bbac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac8c`](#insn-00bbac8c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac90`](#insn-00bbac90) → [`00bbacb4`](#insn-00bbacb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac94`](#insn-00bbac94) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac9c`](#insn-00bbac9c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaca0`](#insn-00bbaca0) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaca4`](#insn-00bbaca4) → [`00bbacb4`](#insn-00bbacb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaca8`](#insn-00bbaca8) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacac`](#insn-00bbacac) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb0`](#insn-00bbacb0) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb4`](#insn-00bbacb4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb8`](#insn-00bbacb8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacbc`](#insn-00bbacbc) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc0`](#insn-00bbacc0) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc4`](#insn-00bbacc4) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc8`](#insn-00bbacc8) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd8`](#insn-00bbacd8) → [`00bbad78`](#insn-00bbad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbace8`](#insn-00bbace8) → `0030e8df`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbacfc`](#insn-00bbacfc) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbad10`](#insn-00bbad10) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbad20`](#insn-00bbad20) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbad38`](#insn-00bbad38) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad3c`](#insn-00bbad3c) → [`00bbad48`](#insn-00bbad48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad40`](#insn-00bbad40) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad44`](#insn-00bbad44) → [`00bbad68`](#insn-00bbad68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad48`](#insn-00bbad48) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad50`](#insn-00bbad50) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad54`](#insn-00bbad54) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad58`](#insn-00bbad58) → [`00bbad68`](#insn-00bbad68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad5c`](#insn-00bbad5c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad60`](#insn-00bbad60) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbad64`](#insn-00bbad64) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad68`](#insn-00bbad68) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad6c`](#insn-00bbad6c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad70`](#insn-00bbad70) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad74`](#insn-00bbad74) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad84`](#insn-00bbad84) → `0030e8ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbad98`](#insn-00bbad98) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbadac`](#insn-00bbadac) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbadbc`](#insn-00bbadbc) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbadd4`](#insn-00bbadd4) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadd8`](#insn-00bbadd8) → [`00bbade4`](#insn-00bbade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaddc`](#insn-00bbaddc) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade0`](#insn-00bbade0) → [`00bbae04`](#insn-00bbae04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade4`](#insn-00bbade4) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadec`](#insn-00bbadec) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf0`](#insn-00bbadf0) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf4`](#insn-00bbadf4) → [`00bbae04`](#insn-00bbae04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf8`](#insn-00bbadf8) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadfc`](#insn-00bbadfc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbae00`](#insn-00bbae00) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae04`](#insn-00bbae04) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae08`](#insn-00bbae08) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae0c`](#insn-00bbae0c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae10`](#insn-00bbae10) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae20`](#insn-00bbae20) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae24`](#insn-00bbae24) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae28`](#insn-00bbae28) → [`00bbb378`](#insn-00bbb378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae2c`](#insn-00bbae2c) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae30`](#insn-00bbae30) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae40`](#insn-00bbae40) → [`00bbb378`](#insn-00bbb378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae50`](#insn-00bbae50) → `0030e8ef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbae64`](#insn-00bbae64) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbae78`](#insn-00bbae78) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbae88`](#insn-00bbae88) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbaea0`](#insn-00bbaea0) → `Stack[-0x1d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeac`](#insn-00bbaeac) → [`00bbaeb8`](#insn-00bbaeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeb0`](#insn-00bbaeb0) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeb4`](#insn-00bbaeb4) → [`00bbaed8`](#insn-00bbaed8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaeb8`](#insn-00bbaeb8) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaec0`](#insn-00bbaec0) → `Stack[-0x1d8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaec4`](#insn-00bbaec4) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaec8`](#insn-00bbaec8) → [`00bbaed8`](#insn-00bbaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaecc`](#insn-00bbaecc) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed0`](#insn-00bbaed0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed4`](#insn-00bbaed4) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed8`](#insn-00bbaed8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaedc`](#insn-00bbaedc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee0`](#insn-00bbaee0) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee4`](#insn-00bbaee4) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef4`](#insn-00bbaef4) → `0030e8f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbaf08`](#insn-00bbaf08) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf1c`](#insn-00bbaf1c) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf2c`](#insn-00bbaf2c) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf44`](#insn-00bbaf44) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf50`](#insn-00bbaf50) → [`00bbaf5c`](#insn-00bbaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf54`](#insn-00bbaf54) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf58`](#insn-00bbaf58) → [`00bbaf7c`](#insn-00bbaf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf5c`](#insn-00bbaf5c) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf64`](#insn-00bbaf64) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf68`](#insn-00bbaf68) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf6c`](#insn-00bbaf6c) → [`00bbaf7c`](#insn-00bbaf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf70`](#insn-00bbaf70) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf74`](#insn-00bbaf74) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf78`](#insn-00bbaf78) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf7c`](#insn-00bbaf7c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf80`](#insn-00bbaf80) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf84`](#insn-00bbaf84) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf88`](#insn-00bbaf88) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf98`](#insn-00bbaf98) → `0030e906`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbafac`](#insn-00bbafac) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbafc0`](#insn-00bbafc0) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbafd0`](#insn-00bbafd0) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbafe8`](#insn-00bbafe8) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff4`](#insn-00bbaff4) → [`00bbb000`](#insn-00bbb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff8`](#insn-00bbaff8) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaffc`](#insn-00bbaffc) → [`00bbb020`](#insn-00bbb020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb000`](#insn-00bbb000) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb008`](#insn-00bbb008) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb00c`](#insn-00bbb00c) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb010`](#insn-00bbb010) → [`00bbb020`](#insn-00bbb020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb014`](#insn-00bbb014) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb018`](#insn-00bbb018) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb01c`](#insn-00bbb01c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb020`](#insn-00bbb020) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb024`](#insn-00bbb024) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb028`](#insn-00bbb028) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb02c`](#insn-00bbb02c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb034`](#insn-00bbb034) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbb044`](#insn-00bbb044) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbb048`](#insn-00bbb048) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb050`](#insn-00bbb050) → [`00c5c5a0`](../00c5c/00c5c5a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb058`](#insn-00bbb058) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb060`](#insn-00bbb060) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbb06c`](#insn-00bbb06c) → [`00c5c600`](../00c5c/00c5c600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c600` · 推定シンボル `None` · 推定型 `None`
- [`00bbb07c`](#insn-00bbb07c) → [`00497da8`](../00497/00497da8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497da8` · 推定シンボル `None` · 推定型 `None`
- [`00bbb084`](#insn-00bbb084) → [`00bbb2c8`](#insn-00bbb2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0a0`](#insn-00bbb0a0) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0a8`](#insn-00bbb0a8) → [`00c5c600`](../00c5c/00c5c600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c600` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0b8`](#insn-00bbb0b8) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0e0`](#insn-00bbb0e0) → `0030e913`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb0e4`](#insn-00bbb0e4) → [`00c5cce0`](../00c5c/00c5cce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cce0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0f0`](#insn-00bbb0f0) → `0030e913`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb0f4`](#insn-00bbb0f4) → [`00c5e1d0`](../00c5e/00c5e1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0f8`](#insn-00bbb0f8) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb100`](#insn-00bbb100) → `0030e91b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb104`](#insn-00bbb104) → [`00c5cce0`](../00c5c/00c5cce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cce0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb110`](#insn-00bbb110) → `0030e91b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb114`](#insn-00bbb114) → [`00c5e1d0`](../00c5e/00c5e1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb118`](#insn-00bbb118) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb124`](#insn-00bbb124) → `0030e8ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb128`](#insn-00bbb128) → [`00c5c8f0`](../00c5c/00c5c8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c8f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb12c`](#insn-00bbb12c) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb138`](#insn-00bbb138) → `0030e8f9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb13c`](#insn-00bbb13c) → [`00c5c8f0`](../00c5c/00c5c8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c8f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb140`](#insn-00bbb140) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb14c`](#insn-00bbb14c) → `0030e906`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb150`](#insn-00bbb150) → [`00c5c8f0`](../00c5c/00c5c8f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c8f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb154`](#insn-00bbb154) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb15c`](#insn-00bbb15c) → [`00c5c030`](../00c5c/00c5c030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c030` · 推定シンボル `None` · 推定型 `None`
- [`00bbb170`](#insn-00bbb170) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbb180`](#insn-00bbb180) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bbb18c`](#insn-00bbb18c) → [`00c5c660`](../00c5c/00c5c660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c660` · 推定シンボル `None` · 推定型 `None`
- [`00bbb190`](#insn-00bbb190) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb19c`](#insn-00bbb19c) → [`0046d908`](../0046d/0046d908.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d908` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1a8`](#insn-00bbb1a8) → [`00bbb210`](#insn-00bbb210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b0`](#insn-00bbb1b0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b4`](#insn-00bbb1b4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b8`](#insn-00bbb1b8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1bc`](#insn-00bbb1bc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1c0`](#insn-00bbb1c0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1dc`](#insn-00bbb1dc) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1e4`](#insn-00bbb1e4) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1e8`](#insn-00bbb1e8) → [`00bbb1f8`](#insn-00bbb1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1ec`](#insn-00bbb1ec) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1f4`](#insn-00bbb1f4) → [`00bbb1fc`](#insn-00bbb1fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1fc`](#insn-00bbb1fc) → `Stack[-0x1a0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb200`](#insn-00bbb200) → [`00c5c680`](../00c5c/00c5c680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c680` · 推定シンボル `None` · 推定型 `None`
- [`00bbb204`](#insn-00bbb204) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb20c`](#insn-00bbb20c) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb218`](#insn-00bbb218) → [`00bbb224`](#insn-00bbb224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb220`](#insn-00bbb220) → [`00bbb244`](#insn-00bbb244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb234`](#insn-00bbb234) → [`00bbb244`](#insn-00bbb244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb23c`](#insn-00bbb23c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb244`](#insn-00bbb244) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb248`](#insn-00bbb248) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb254`](#insn-00bbb254) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb258`](#insn-00bbb258) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb25c`](#insn-00bbb25c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb260`](#insn-00bbb260) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb264`](#insn-00bbb264) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb268`](#insn-00bbb268) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb26c`](#insn-00bbb26c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb270`](#insn-00bbb270) → [`00bbb27c`](#insn-00bbb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb274`](#insn-00bbb274) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb278`](#insn-00bbb278) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2ac`](#insn-00bbb2ac) → [`00c5c600`](../00c5c/00c5c600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c600` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2bc`](#insn-00bbb2bc) → [`00497da8`](../00497/00497da8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497da8` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2c4`](#insn-00bbb2c4) → [`00bbb0a4`](#insn-00bbb0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2e4`](#insn-00bbb2e4) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2f4`](#insn-00bbb2f4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2fc`](#insn-00bbb2fc) → [`00c5c5d0`](../00c5c/00c5c5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb304`](#insn-00bbb304) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb30c`](#insn-00bbb30c) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bbb318`](#insn-00bbb318) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bbb328`](#insn-00bbb328) → [`00c5c390`](../00c5c/00c5c390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c390` · 推定シンボル `None` · 推定型 `None`
- [`00bbb32c`](#insn-00bbb32c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb330`](#insn-00bbb330) → [`00bbb33c`](#insn-00bbb33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb334`](#insn-00bbb334) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb338`](#insn-00bbb338) → [`00bbb35c`](#insn-00bbb35c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb33c`](#insn-00bbb33c) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb344`](#insn-00bbb344) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb348`](#insn-00bbb348) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb34c`](#insn-00bbb34c) → [`00bbb35c`](#insn-00bbb35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb350`](#insn-00bbb350) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb354`](#insn-00bbb354) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb358`](#insn-00bbb358) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb35c`](#insn-00bbb35c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb360`](#insn-00bbb360) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb364`](#insn-00bbb364) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb368`](#insn-00bbb368) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb36c`](#insn-00bbb36c) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb374`](#insn-00bbb374) → [`00c5e440`](../00c5e/00c5e440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e440` · 推定シンボル `None` · 推定型 `None`
- [`00bbb390`](#insn-00bbb390) → [`00c5e490`](../00c5e/00c5e490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e490` · 推定シンボル `None` · 推定型 `None`
- [`00bbb398`](#insn-00bbb398) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3ac`](#insn-00bbb3ac) → `01127450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb3b0`](#insn-00bbb3b0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3b4`](#insn-00bbb3b4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3bc`](#insn-00bbb3bc) → [`00bbb3c8`](#insn-00bbb3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3c4`](#insn-00bbb3c4) → [`00bbb3cc`](#insn-00bbb3cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3d0`](#insn-00bbb3d0) → [`00c5e620`](../00c5e/00c5e620.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e620` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3d8`](#insn-00bbb3d8) → `01127428`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb3e4`](#insn-00bbb3e4) → [`00bbb3f0`](#insn-00bbb3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3ec`](#insn-00bbb3ec) → [`00bbb3f4`](#insn-00bbb3f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3f8`](#insn-00bbb3f8) → `002b07ef`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3fc`](#insn-00bbb3fc) → [`00c5b130`](../00c5b/00c5b130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b130` · 推定シンボル `None` · 推定型 `None`
- [`00bbb400`](#insn-00bbb400) → [`00bbb490`](#insn-00bbb490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb410`](#insn-00bbb410) → [`00c5b100`](../00c5b/00c5b100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b100` · 推定シンボル `None` · 推定型 `None`
- [`00bbb418`](#insn-00bbb418) → [`00c5b0f0`](../00c5b/00c5b0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb41c`](#insn-00bbb41c) → [`00bbb438`](#insn-00bbb438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb42c`](#insn-00bbb42c) → [`00c5cf10`](../00c5c/00c5cf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cf10` · 推定シンボル `None` · 推定型 `None`
- [`00bbb434`](#insn-00bbb434) → [`00bbb440`](#insn-00bbb440) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb43c`](#insn-00bbb43c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb44c`](#insn-00bbb44c) → [`00c5b100`](../00c5b/00c5b100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b100` · 推定シンボル `None` · 推定型 `None`
- [`00bbb450`](#insn-00bbb450) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb454`](#insn-00bbb454) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb470`](#insn-00bbb470) → [`00c5b120`](../00c5b/00c5b120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b120` · 推定シンボル `None` · 推定型 `None`
- [`00bbb478`](#insn-00bbb478) → [`00c5b310`](../00c5b/00c5b310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b310` · 推定シンボル `None` · 推定型 `None`
- [`00bbb484`](#insn-00bbb484) → [`00c5b0a0`](../00c5b/00c5b0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb48c`](#insn-00bbb48c) → [`00bbb4a8`](#insn-00bbb4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb494`](#insn-00bbb494) → `002be90f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb498`](#insn-00bbb498) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4a0`](#insn-00bbb4a0) → [`00bbb4f0`](#insn-00bbb4f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4a4`](#insn-00bbb4a4) → [`00bbb510`](#insn-00bbb510) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4a8`](#insn-00bbb4a8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4ac`](#insn-00bbb4ac) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4bc`](#insn-00bbb4bc) → [`00bbb4e8`](#insn-00bbb4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4c0`](#insn-00bbb4c0) → `01127428`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb4c8`](#insn-00bbb4c8) → [`00bbb4d4`](#insn-00bbb4d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4d0`](#insn-00bbb4d0) → [`00bbb4d8`](#insn-00bbb4d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4dc`](#insn-00bbb4dc) → `002bc7ed`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4e0`](#insn-00bbb4e0) → [`00c5b130`](../00c5b/00c5b130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b130` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4e4`](#insn-00bbb4e4) → [`00c5b0a0`](../00c5b/00c5b0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4ec`](#insn-00bbb4ec) → [`00bbb510`](#insn-00bbb510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4f4`](#insn-00bbb4f4) → [`00c5b300`](../00c5b/00c5b300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b300` · 推定シンボル `None` · 推定型 `None`
- [`00bbb4fc`](#insn-00bbb4fc) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bbb504`](#insn-00bbb504) → `01127418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb508`](#insn-00bbb508) → [`00bbb510`](#insn-00bbb510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb50c`](#insn-00bbb50c) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb510`](#insn-00bbb510) → [`00bbb550`](#insn-00bbb550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb534`](#insn-00bbb534) → [`00bbe1e4`](../00bbe/00bbe1e4.md) · `DATA` · `ANALYSIS` · 関数 `00bbe1e4` · 推定シンボル `None` · 推定型 `None`
- [`00bbb534`](#insn-00bbb534) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb538`](#insn-00bbb538) → [`00bbe1e8`](../00bbe/00bbe1e8.md) · `DATA` · `ANALYSIS` · 関数 `00bbe1e8` · 推定シンボル `None` · 推定型 `None`
- [`00bbb538`](#insn-00bbb538) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb53c`](#insn-00bbb53c) → [`00bbe398`](../00bbe/00bbe398.md) · `DATA` · `ANALYSIS` · 関数 `00bbe398` · 推定シンボル `None` · 推定型 `None`
- [`00bbb53c`](#insn-00bbb53c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb540`](#insn-00bbb540) → [`00bbe400`](../00bbe/00bbe400.md) · `DATA` · `ANALYSIS` · 関数 `00bbe400` · 推定シンボル `None` · 推定型 `None`
- [`00bbb540`](#insn-00bbb540) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb54c`](#insn-00bbb54c) → [`00c5e5f0`](../00c5e/00c5e5f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb550`](#insn-00bbb550) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb554`](#insn-00bbb554) → [`00bbb560`](#insn-00bbb560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb558`](#insn-00bbb558) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb55c`](#insn-00bbb55c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bbb564`](#insn-00bbb564) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb56c`](#insn-00bbb56c) → [`00bbb590`](#insn-00bbb590) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb574`](#insn-00bbb574) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb578`](#insn-00bbb578) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb57c`](#insn-00bbb57c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb580`](#insn-00bbb580) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb584`](#insn-00bbb584) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb590`](#insn-00bbb590) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaaa4`](#insn-00bbaaa4)

~~~json
{
  "source": "00bbaaa4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaaa8`](#insn-00bbaaa8)

~~~json
{
  "source": "00bbaaa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaaac`](#insn-00bbaaac)

~~~json
{
  "source": "00bbaaac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaab0`](#insn-00bbaab0)

~~~json
{
  "source": "00bbaab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaab4`](#insn-00bbaab4)

~~~json
{
  "source": "00bbaab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaab8`](#insn-00bbaab8)

~~~json
{
  "source": "00bbaab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaad0`](#insn-00bbaad0)

~~~json
{
  "source": "00bbaad0",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaad4`](#insn-00bbaad4)

~~~json
{
  "source": "00bbaad4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaad8`](#insn-00bbaad8)

~~~json
{
  "source": "00bbaad8",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaae0`](#insn-00bbaae0)

~~~json
{
  "source": "00bbaae0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbaae4`](#insn-00bbaae4)

~~~json
{
  "source": "00bbaae4",
  "target": "00bbaaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaae8`](#insn-00bbaae8)

~~~json
{
  "source": "00bbaae8",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaaf0`](#insn-00bbaaf0)

~~~json
{
  "source": "00bbaaf0",
  "target": "00bbaaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaafc`](#insn-00bbaafc)

~~~json
{
  "source": "00bbaafc",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab00`](#insn-00bbab00)

~~~json
{
  "source": "00bbab00",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab04`](#insn-00bbab04)

~~~json
{
  "source": "00bbab04",
  "target": "00c5e340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab08`](#insn-00bbab08)

~~~json
{
  "source": "00bbab08",
  "target": "00bbb560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab0c`](#insn-00bbab0c)

~~~json
{
  "source": "00bbab0c",
  "target": "00bbb560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab14`](#insn-00bbab14)

~~~json
{
  "source": "00bbab14",
  "target": "01127448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127448",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab18`](#insn-00bbab18)

~~~json
{
  "source": "00bbab18",
  "target": "00bbb3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab1c`](#insn-00bbab1c)

~~~json
{
  "source": "00bbab1c",
  "target": "00c5e340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab20`](#insn-00bbab20)

~~~json
{
  "source": "00bbab20",
  "target": "00bbb3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab2c`](#insn-00bbab2c)

~~~json
{
  "source": "00bbab2c",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab30`](#insn-00bbab30)

~~~json
{
  "source": "00bbab30",
  "target": "01127448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127448",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab34`](#insn-00bbab34)

~~~json
{
  "source": "00bbab34",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab38`](#insn-00bbab38)

~~~json
{
  "source": "00bbab38",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbab3c`](#insn-00bbab3c)

~~~json
{
  "source": "00bbab3c",
  "target": "00bbab60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab5c`](#insn-00bbab5c)

~~~json
{
  "source": "00bbab5c",
  "target": "00bbab64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab68`](#insn-00bbab68)

~~~json
{
  "source": "00bbab68",
  "target": "01127318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab6c`](#insn-00bbab6c)

~~~json
{
  "source": "00bbab6c",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab70`](#insn-00bbab70)

~~~json
{
  "source": "00bbab70",
  "target": "00bbb3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbab78`](#insn-00bbab78)

~~~json
{
  "source": "00bbab78",
  "target": "00c5c5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbab88`](#insn-00bbab88)

~~~json
{
  "source": "00bbab88",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaba4`](#insn-00bbaba4)

~~~json
{
  "source": "00bbaba4",
  "target": "00bbb3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabac`](#insn-00bbabac)

~~~json
{
  "source": "00bbabac",
  "target": "00c5c5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbabbc`](#insn-00bbabbc)

~~~json
{
  "source": "00bbabbc",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabc0`](#insn-00bbabc0)

~~~json
{
  "source": "00bbabc0",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbabc4`](#insn-00bbabc4)

~~~json
{
  "source": "00bbabc4",
  "target": "00bbb394",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabdc`](#insn-00bbabdc)

~~~json
{
  "source": "00bbabdc",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabe0`](#insn-00bbabe0)

~~~json
{
  "source": "00bbabe0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabe4`](#insn-00bbabe4)

~~~json
{
  "source": "00bbabe4",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabe8`](#insn-00bbabe8)

~~~json
{
  "source": "00bbabe8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabec`](#insn-00bbabec)

~~~json
{
  "source": "00bbabec",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf0`](#insn-00bbabf0)

~~~json
{
  "source": "00bbabf0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf4`](#insn-00bbabf4)

~~~json
{
  "source": "00bbabf4",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf8`](#insn-00bbabf8)

~~~json
{
  "source": "00bbabf8",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabfc`](#insn-00bbabfc)

~~~json
{
  "source": "00bbabfc",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac00`](#insn-00bbac00)

~~~json
{
  "source": "00bbac00",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac04`](#insn-00bbac04)

~~~json
{
  "source": "00bbac04",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac08`](#insn-00bbac08)

~~~json
{
  "source": "00bbac08",
  "target": "Stack[-0xff]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac0c`](#insn-00bbac0c)

~~~json
{
  "source": "00bbac0c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac10`](#insn-00bbac10)

~~~json
{
  "source": "00bbac10",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac14`](#insn-00bbac14)

~~~json
{
  "source": "00bbac14",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac20`](#insn-00bbac20)

~~~json
{
  "source": "00bbac20",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac2c`](#insn-00bbac2c)

~~~json
{
  "source": "00bbac2c",
  "target": "0030e8cd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8cd",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "676f6f676c652e6d6573736167655f696400",
  "capture_start": "0030e8cd",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbac40`](#insn-00bbac40)

~~~json
{
  "source": "00bbac40",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac54`](#insn-00bbac54)

~~~json
{
  "source": "00bbac54",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac64`](#insn-00bbac64)

~~~json
{
  "source": "00bbac64",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac7c`](#insn-00bbac7c)

~~~json
{
  "source": "00bbac7c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac88`](#insn-00bbac88)

~~~json
{
  "source": "00bbac88",
  "target": "00bbac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac8c`](#insn-00bbac8c)

~~~json
{
  "source": "00bbac8c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac90`](#insn-00bbac90)

~~~json
{
  "source": "00bbac90",
  "target": "00bbacb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac94`](#insn-00bbac94)

~~~json
{
  "source": "00bbac94",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac9c`](#insn-00bbac9c)

~~~json
{
  "source": "00bbac9c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaca0`](#insn-00bbaca0)

~~~json
{
  "source": "00bbaca0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaca4`](#insn-00bbaca4)

~~~json
{
  "source": "00bbaca4",
  "target": "00bbacb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaca8`](#insn-00bbaca8)

~~~json
{
  "source": "00bbaca8",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacac`](#insn-00bbacac)

~~~json
{
  "source": "00bbacac",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb4`](#insn-00bbacb4)

~~~json
{
  "source": "00bbacb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb8`](#insn-00bbacb8)

~~~json
{
  "source": "00bbacb8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacbc`](#insn-00bbacbc)

~~~json
{
  "source": "00bbacbc",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc0`](#insn-00bbacc0)

~~~json
{
  "source": "00bbacc0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc4`](#insn-00bbacc4)

~~~json
{
  "source": "00bbacc4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc8`](#insn-00bbacc8)

~~~json
{
  "source": "00bbacc8",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacd8`](#insn-00bbacd8)

~~~json
{
  "source": "00bbacd8",
  "target": "00bbad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbace8`](#insn-00bbace8)

~~~json
{
  "source": "00bbace8",
  "target": "0030e8df",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8df",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6d6573736167655f696400",
  "capture_start": "0030e8df",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbacfc`](#insn-00bbacfc)

~~~json
{
  "source": "00bbacfc",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad10`](#insn-00bbad10)

~~~json
{
  "source": "00bbad10",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad20`](#insn-00bbad20)

~~~json
{
  "source": "00bbad20",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad38`](#insn-00bbad38)

~~~json
{
  "source": "00bbad38",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad3c`](#insn-00bbad3c)

~~~json
{
  "source": "00bbad3c",
  "target": "00bbad48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad40`](#insn-00bbad40)

~~~json
{
  "source": "00bbad40",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad44`](#insn-00bbad44)

~~~json
{
  "source": "00bbad44",
  "target": "00bbad68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad48`](#insn-00bbad48)

~~~json
{
  "source": "00bbad48",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad50`](#insn-00bbad50)

~~~json
{
  "source": "00bbad50",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad54`](#insn-00bbad54)

~~~json
{
  "source": "00bbad54",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad58`](#insn-00bbad58)

~~~json
{
  "source": "00bbad58",
  "target": "00bbad68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad5c`](#insn-00bbad5c)

~~~json
{
  "source": "00bbad5c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad60`](#insn-00bbad60)

~~~json
{
  "source": "00bbad60",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbad64`](#insn-00bbad64)

~~~json
{
  "source": "00bbad64",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad68`](#insn-00bbad68)

~~~json
{
  "source": "00bbad68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad6c`](#insn-00bbad6c)

~~~json
{
  "source": "00bbad6c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad70`](#insn-00bbad70)

~~~json
{
  "source": "00bbad70",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad74`](#insn-00bbad74)

~~~json
{
  "source": "00bbad74",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad84`](#insn-00bbad84)

~~~json
{
  "source": "00bbad84",
  "target": "0030e8ea",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbad98`](#insn-00bbad98)

~~~json
{
  "source": "00bbad98",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadac`](#insn-00bbadac)

~~~json
{
  "source": "00bbadac",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadbc`](#insn-00bbadbc)

~~~json
{
  "source": "00bbadbc",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbadd4`](#insn-00bbadd4)

~~~json
{
  "source": "00bbadd4",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadd8`](#insn-00bbadd8)

~~~json
{
  "source": "00bbadd8",
  "target": "00bbade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaddc`](#insn-00bbaddc)

~~~json
{
  "source": "00bbaddc",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade0`](#insn-00bbade0)

~~~json
{
  "source": "00bbade0",
  "target": "00bbae04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade4`](#insn-00bbade4)

~~~json
{
  "source": "00bbade4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadec`](#insn-00bbadec)

~~~json
{
  "source": "00bbadec",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf0`](#insn-00bbadf0)

~~~json
{
  "source": "00bbadf0",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf4`](#insn-00bbadf4)

~~~json
{
  "source": "00bbadf4",
  "target": "00bbae04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf8`](#insn-00bbadf8)

~~~json
{
  "source": "00bbadf8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadfc`](#insn-00bbadfc)

~~~json
{
  "source": "00bbadfc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae00`](#insn-00bbae00)

~~~json
{
  "source": "00bbae00",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae04`](#insn-00bbae04)

~~~json
{
  "source": "00bbae04",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae08`](#insn-00bbae08)

~~~json
{
  "source": "00bbae08",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae0c`](#insn-00bbae0c)

~~~json
{
  "source": "00bbae0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae10`](#insn-00bbae10)

~~~json
{
  "source": "00bbae10",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae20`](#insn-00bbae20)

~~~json
{
  "source": "00bbae20",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae24`](#insn-00bbae24)

~~~json
{
  "source": "00bbae24",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae28`](#insn-00bbae28)

~~~json
{
  "source": "00bbae28",
  "target": "00bbb378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae2c`](#insn-00bbae2c)

~~~json
{
  "source": "00bbae2c",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae30`](#insn-00bbae30)

~~~json
{
  "source": "00bbae30",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae40`](#insn-00bbae40)

~~~json
{
  "source": "00bbae40",
  "target": "00bbb378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae50`](#insn-00bbae50)

~~~json
{
  "source": "00bbae50",
  "target": "0030e8ef",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8ef",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "676f6f676c652e746f00",
  "capture_start": "0030e8ef",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbae64`](#insn-00bbae64)

~~~json
{
  "source": "00bbae64",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae78`](#insn-00bbae78)

~~~json
{
  "source": "00bbae78",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae88`](#insn-00bbae88)

~~~json
{
  "source": "00bbae88",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaea0`](#insn-00bbaea0)

~~~json
{
  "source": "00bbaea0",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeac`](#insn-00bbaeac)

~~~json
{
  "source": "00bbaeac",
  "target": "00bbaeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeb0`](#insn-00bbaeb0)

~~~json
{
  "source": "00bbaeb0",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeb4`](#insn-00bbaeb4)

~~~json
{
  "source": "00bbaeb4",
  "target": "00bbaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaeb8`](#insn-00bbaeb8)

~~~json
{
  "source": "00bbaeb8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaec0`](#insn-00bbaec0)

~~~json
{
  "source": "00bbaec0",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaec4`](#insn-00bbaec4)

~~~json
{
  "source": "00bbaec4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaec8`](#insn-00bbaec8)

~~~json
{
  "source": "00bbaec8",
  "target": "00bbaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaecc`](#insn-00bbaecc)

~~~json
{
  "source": "00bbaecc",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaed0`](#insn-00bbaed0)

~~~json
{
  "source": "00bbaed0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaed4`](#insn-00bbaed4)

~~~json
{
  "source": "00bbaed4",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaed8`](#insn-00bbaed8)

~~~json
{
  "source": "00bbaed8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaedc`](#insn-00bbaedc)

~~~json
{
  "source": "00bbaedc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee0`](#insn-00bbaee0)

~~~json
{
  "source": "00bbaee0",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee4`](#insn-00bbaee4)

~~~json
{
  "source": "00bbaee4",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaef4`](#insn-00bbaef4)

~~~json
{
  "source": "00bbaef4",
  "target": "0030e8f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8f9",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "6d6573736167655f7479706500",
  "capture_start": "0030e8f9",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbaf08`](#insn-00bbaf08)

~~~json
{
  "source": "00bbaf08",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf1c`](#insn-00bbaf1c)

~~~json
{
  "source": "00bbaf1c",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf2c`](#insn-00bbaf2c)

~~~json
{
  "source": "00bbaf2c",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf44`](#insn-00bbaf44)

~~~json
{
  "source": "00bbaf44",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf50`](#insn-00bbaf50)

~~~json
{
  "source": "00bbaf50",
  "target": "00bbaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf54`](#insn-00bbaf54)

~~~json
{
  "source": "00bbaf54",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf58`](#insn-00bbaf58)

~~~json
{
  "source": "00bbaf58",
  "target": "00bbaf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf5c`](#insn-00bbaf5c)

~~~json
{
  "source": "00bbaf5c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf64`](#insn-00bbaf64)

~~~json
{
  "source": "00bbaf64",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf68`](#insn-00bbaf68)

~~~json
{
  "source": "00bbaf68",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf6c`](#insn-00bbaf6c)

~~~json
{
  "source": "00bbaf6c",
  "target": "00bbaf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf70`](#insn-00bbaf70)

~~~json
{
  "source": "00bbaf70",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf74`](#insn-00bbaf74)

~~~json
{
  "source": "00bbaf74",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf78`](#insn-00bbaf78)

~~~json
{
  "source": "00bbaf78",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf7c`](#insn-00bbaf7c)

~~~json
{
  "source": "00bbaf7c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf80`](#insn-00bbaf80)

~~~json
{
  "source": "00bbaf80",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf84`](#insn-00bbaf84)

~~~json
{
  "source": "00bbaf84",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf88`](#insn-00bbaf88)

~~~json
{
  "source": "00bbaf88",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf98`](#insn-00bbaf98)

~~~json
{
  "source": "00bbaf98",
  "target": "0030e906",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e906",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "636f6c6c617073655f6b657900",
  "capture_start": "0030e906",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbafac`](#insn-00bbafac)

~~~json
{
  "source": "00bbafac",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbafc0`](#insn-00bbafc0)

~~~json
{
  "source": "00bbafc0",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbafd0`](#insn-00bbafd0)

~~~json
{
  "source": "00bbafd0",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbafe8`](#insn-00bbafe8)

~~~json
{
  "source": "00bbafe8",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaff4`](#insn-00bbaff4)

~~~json
{
  "source": "00bbaff4",
  "target": "00bbb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaff8`](#insn-00bbaff8)

~~~json
{
  "source": "00bbaff8",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaffc`](#insn-00bbaffc)

~~~json
{
  "source": "00bbaffc",
  "target": "00bbb020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb000`](#insn-00bbb000)

~~~json
{
  "source": "00bbb000",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb008`](#insn-00bbb008)

~~~json
{
  "source": "00bbb008",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb00c`](#insn-00bbb00c)

~~~json
{
  "source": "00bbb00c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb010`](#insn-00bbb010)

~~~json
{
  "source": "00bbb010",
  "target": "00bbb020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb014`](#insn-00bbb014)

~~~json
{
  "source": "00bbb014",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb018`](#insn-00bbb018)

~~~json
{
  "source": "00bbb018",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb01c`](#insn-00bbb01c)

~~~json
{
  "source": "00bbb01c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb020`](#insn-00bbb020)

~~~json
{
  "source": "00bbb020",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb024`](#insn-00bbb024)

~~~json
{
  "source": "00bbb024",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb028`](#insn-00bbb028)

~~~json
{
  "source": "00bbb028",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb02c`](#insn-00bbb02c)

~~~json
{
  "source": "00bbb02c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb034`](#insn-00bbb034)

~~~json
{
  "source": "00bbb034",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb044`](#insn-00bbb044)

~~~json
{
  "source": "00bbb044",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb048`](#insn-00bbb048)

~~~json
{
  "source": "00bbb048",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb050`](#insn-00bbb050)

~~~json
{
  "source": "00bbb050",
  "target": "00c5c5a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb058`](#insn-00bbb058)

~~~json
{
  "source": "00bbb058",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb060`](#insn-00bbb060)

~~~json
{
  "source": "00bbb060",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb06c`](#insn-00bbb06c)

~~~json
{
  "source": "00bbb06c",
  "target": "00c5c600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb07c`](#insn-00bbb07c)

~~~json
{
  "source": "00bbb07c",
  "target": "00497da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb084`](#insn-00bbb084)

~~~json
{
  "source": "00bbb084",
  "target": "00bbb2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0a0`](#insn-00bbb0a0)

~~~json
{
  "source": "00bbb0a0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0a8`](#insn-00bbb0a8)

~~~json
{
  "source": "00bbb0a8",
  "target": "00c5c600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0b8`](#insn-00bbb0b8)

~~~json
{
  "source": "00bbb0b8",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0e0`](#insn-00bbb0e0)

~~~json
{
  "source": "00bbb0e0",
  "target": "0030e913",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e913",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "676f6f676c652e00",
  "capture_start": "0030e913",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb0e4`](#insn-00bbb0e4)

~~~json
{
  "source": "00bbb0e4",
  "target": "00c5cce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0f0`](#insn-00bbb0f0)

~~~json
{
  "source": "00bbb0f0",
  "target": "0030e913",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e913",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "676f6f676c652e00",
  "capture_start": "0030e913",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb0f4`](#insn-00bbb0f4)

~~~json
{
  "source": "00bbb0f4",
  "target": "00c5e1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0f8`](#insn-00bbb0f8)

~~~json
{
  "source": "00bbb0f8",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb100`](#insn-00bbb100)

~~~json
{
  "source": "00bbb100",
  "target": "0030e91b",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb104`](#insn-00bbb104)

~~~json
{
  "source": "00bbb104",
  "target": "00c5cce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb110`](#insn-00bbb110)

~~~json
{
  "source": "00bbb110",
  "target": "0030e91b",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb114`](#insn-00bbb114)

~~~json
{
  "source": "00bbb114",
  "target": "00c5e1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb118`](#insn-00bbb118)

~~~json
{
  "source": "00bbb118",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb124`](#insn-00bbb124)

~~~json
{
  "source": "00bbb124",
  "target": "0030e8ea",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb128`](#insn-00bbb128)

~~~json
{
  "source": "00bbb128",
  "target": "00c5c8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb12c`](#insn-00bbb12c)

~~~json
{
  "source": "00bbb12c",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb138`](#insn-00bbb138)

~~~json
{
  "source": "00bbb138",
  "target": "0030e8f9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8f9",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "6d6573736167655f7479706500",
  "capture_start": "0030e8f9",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb13c`](#insn-00bbb13c)

~~~json
{
  "source": "00bbb13c",
  "target": "00c5c8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb140`](#insn-00bbb140)

~~~json
{
  "source": "00bbb140",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb14c`](#insn-00bbb14c)

~~~json
{
  "source": "00bbb14c",
  "target": "0030e906",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e906",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "636f6c6c617073655f6b657900",
  "capture_start": "0030e906",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb150`](#insn-00bbb150)

~~~json
{
  "source": "00bbb150",
  "target": "00c5c8f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb154`](#insn-00bbb154)

~~~json
{
  "source": "00bbb154",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb15c`](#insn-00bbb15c)

~~~json
{
  "source": "00bbb15c",
  "target": "00c5c030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb170`](#insn-00bbb170)

~~~json
{
  "source": "00bbb170",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb180`](#insn-00bbb180)

~~~json
{
  "source": "00bbb180",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb18c`](#insn-00bbb18c)

~~~json
{
  "source": "00bbb18c",
  "target": "00c5c660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb190`](#insn-00bbb190)

~~~json
{
  "source": "00bbb190",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb19c`](#insn-00bbb19c)

~~~json
{
  "source": "00bbb19c",
  "target": "0046d908",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb1a8`](#insn-00bbb1a8)

~~~json
{
  "source": "00bbb1a8",
  "target": "00bbb210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1b0`](#insn-00bbb1b0)

~~~json
{
  "source": "00bbb1b0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb1b4`](#insn-00bbb1b4)

~~~json
{
  "source": "00bbb1b4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1b8`](#insn-00bbb1b8)

~~~json
{
  "source": "00bbb1b8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1bc`](#insn-00bbb1bc)

~~~json
{
  "source": "00bbb1bc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1c0`](#insn-00bbb1c0)

~~~json
{
  "source": "00bbb1c0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1dc`](#insn-00bbb1dc)

~~~json
{
  "source": "00bbb1dc",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1e4`](#insn-00bbb1e4)

~~~json
{
  "source": "00bbb1e4",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1e8`](#insn-00bbb1e8)

~~~json
{
  "source": "00bbb1e8",
  "target": "00bbb1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1ec`](#insn-00bbb1ec)

~~~json
{
  "source": "00bbb1ec",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1f4`](#insn-00bbb1f4)

~~~json
{
  "source": "00bbb1f4",
  "target": "00bbb1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1fc`](#insn-00bbb1fc)

~~~json
{
  "source": "00bbb1fc",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb200`](#insn-00bbb200)

~~~json
{
  "source": "00bbb200",
  "target": "00c5c680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb204`](#insn-00bbb204)

~~~json
{
  "source": "00bbb204",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb20c`](#insn-00bbb20c)

~~~json
{
  "source": "00bbb20c",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb218`](#insn-00bbb218)

~~~json
{
  "source": "00bbb218",
  "target": "00bbb224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb220`](#insn-00bbb220)

~~~json
{
  "source": "00bbb220",
  "target": "00bbb244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb234`](#insn-00bbb234)

~~~json
{
  "source": "00bbb234",
  "target": "00bbb244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb23c`](#insn-00bbb23c)

~~~json
{
  "source": "00bbb23c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb244`](#insn-00bbb244)

~~~json
{
  "source": "00bbb244",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb248`](#insn-00bbb248)

~~~json
{
  "source": "00bbb248",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb254`](#insn-00bbb254)

~~~json
{
  "source": "00bbb254",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb258`](#insn-00bbb258)

~~~json
{
  "source": "00bbb258",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb25c`](#insn-00bbb25c)

~~~json
{
  "source": "00bbb25c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb260`](#insn-00bbb260)

~~~json
{
  "source": "00bbb260",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb264`](#insn-00bbb264)

~~~json
{
  "source": "00bbb264",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb268`](#insn-00bbb268)

~~~json
{
  "source": "00bbb268",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb26c`](#insn-00bbb26c)

~~~json
{
  "source": "00bbb26c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb270`](#insn-00bbb270)

~~~json
{
  "source": "00bbb270",
  "target": "00bbb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb274`](#insn-00bbb274)

~~~json
{
  "source": "00bbb274",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb278`](#insn-00bbb278)

~~~json
{
  "source": "00bbb278",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb2ac`](#insn-00bbb2ac)

~~~json
{
  "source": "00bbb2ac",
  "target": "00c5c600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb2bc`](#insn-00bbb2bc)

~~~json
{
  "source": "00bbb2bc",
  "target": "00497da8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb2c4`](#insn-00bbb2c4)

~~~json
{
  "source": "00bbb2c4",
  "target": "00bbb0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2e4`](#insn-00bbb2e4)

~~~json
{
  "source": "00bbb2e4",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2f4`](#insn-00bbb2f4)

~~~json
{
  "source": "00bbb2f4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2fc`](#insn-00bbb2fc)

~~~json
{
  "source": "00bbb2fc",
  "target": "00c5c5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb304`](#insn-00bbb304)

~~~json
{
  "source": "00bbb304",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb30c`](#insn-00bbb30c)

~~~json
{
  "source": "00bbb30c",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb318`](#insn-00bbb318)

~~~json
{
  "source": "00bbb318",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb328`](#insn-00bbb328)

~~~json
{
  "source": "00bbb328",
  "target": "00c5c390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb32c`](#insn-00bbb32c)

~~~json
{
  "source": "00bbb32c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb330`](#insn-00bbb330)

~~~json
{
  "source": "00bbb330",
  "target": "00bbb33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb334`](#insn-00bbb334)

~~~json
{
  "source": "00bbb334",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb338`](#insn-00bbb338)

~~~json
{
  "source": "00bbb338",
  "target": "00bbb35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb33c`](#insn-00bbb33c)

~~~json
{
  "source": "00bbb33c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb344`](#insn-00bbb344)

~~~json
{
  "source": "00bbb344",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb348`](#insn-00bbb348)

~~~json
{
  "source": "00bbb348",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb34c`](#insn-00bbb34c)

~~~json
{
  "source": "00bbb34c",
  "target": "00bbb35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb350`](#insn-00bbb350)

~~~json
{
  "source": "00bbb350",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb354`](#insn-00bbb354)

~~~json
{
  "source": "00bbb354",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb358`](#insn-00bbb358)

~~~json
{
  "source": "00bbb358",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb35c`](#insn-00bbb35c)

~~~json
{
  "source": "00bbb35c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb360`](#insn-00bbb360)

~~~json
{
  "source": "00bbb360",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb364`](#insn-00bbb364)

~~~json
{
  "source": "00bbb364",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb368`](#insn-00bbb368)

~~~json
{
  "source": "00bbb368",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb36c`](#insn-00bbb36c)

~~~json
{
  "source": "00bbb36c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb374`](#insn-00bbb374)

~~~json
{
  "source": "00bbb374",
  "target": "00c5e440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb390`](#insn-00bbb390)

~~~json
{
  "source": "00bbb390",
  "target": "00c5e490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb398`](#insn-00bbb398)

~~~json
{
  "source": "00bbb398",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3ac`](#insn-00bbb3ac)

~~~json
{
  "source": "00bbb3ac",
  "target": "01127450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127450",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb3b0`](#insn-00bbb3b0)

~~~json
{
  "source": "00bbb3b0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3b4`](#insn-00bbb3b4)

~~~json
{
  "source": "00bbb3b4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3bc`](#insn-00bbb3bc)

~~~json
{
  "source": "00bbb3bc",
  "target": "00bbb3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3c4`](#insn-00bbb3c4)

~~~json
{
  "source": "00bbb3c4",
  "target": "00bbb3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3d0`](#insn-00bbb3d0)

~~~json
{
  "source": "00bbb3d0",
  "target": "00c5e620",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb3d8`](#insn-00bbb3d8)

~~~json
{
  "source": "00bbb3d8",
  "target": "01127428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb3e4`](#insn-00bbb3e4)

~~~json
{
  "source": "00bbb3e4",
  "target": "00bbb3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3ec`](#insn-00bbb3ec)

~~~json
{
  "source": "00bbb3ec",
  "target": "00bbb3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3f8`](#insn-00bbb3f8)

~~~json
{
  "source": "00bbb3f8",
  "target": "002b07ef",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3fc`](#insn-00bbb3fc)

~~~json
{
  "source": "00bbb3fc",
  "target": "00c5b130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb400`](#insn-00bbb400)

~~~json
{
  "source": "00bbb400",
  "target": "00bbb490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb410`](#insn-00bbb410)

~~~json
{
  "source": "00bbb410",
  "target": "00c5b100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb418`](#insn-00bbb418)

~~~json
{
  "source": "00bbb418",
  "target": "00c5b0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb41c`](#insn-00bbb41c)

~~~json
{
  "source": "00bbb41c",
  "target": "00bbb438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb42c`](#insn-00bbb42c)

~~~json
{
  "source": "00bbb42c",
  "target": "00c5cf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb434`](#insn-00bbb434)

~~~json
{
  "source": "00bbb434",
  "target": "00bbb440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb43c`](#insn-00bbb43c)

~~~json
{
  "source": "00bbb43c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb44c`](#insn-00bbb44c)

~~~json
{
  "source": "00bbb44c",
  "target": "00c5b100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb450`](#insn-00bbb450)

~~~json
{
  "source": "00bbb450",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb454`](#insn-00bbb454)

~~~json
{
  "source": "00bbb454",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb470`](#insn-00bbb470)

~~~json
{
  "source": "00bbb470",
  "target": "00c5b120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb478`](#insn-00bbb478)

~~~json
{
  "source": "00bbb478",
  "target": "00c5b310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb484`](#insn-00bbb484)

~~~json
{
  "source": "00bbb484",
  "target": "00c5b0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb48c`](#insn-00bbb48c)

~~~json
{
  "source": "00bbb48c",
  "target": "00bbb4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb494`](#insn-00bbb494)

~~~json
{
  "source": "00bbb494",
  "target": "002be90f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be90f",
  "offset": 0,
  "size": 54,
  "datatype": "string",
  "bytes": "4c6f616446696c6528675f6c6f63616c5f73746f726167655f66696c655f7061",
  "capture_start": "002be90f",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbb498`](#insn-00bbb498)

~~~json
{
  "source": "00bbb498",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4a0`](#insn-00bbb4a0)

~~~json
{
  "source": "00bbb4a0",
  "target": "00bbb4f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4a4`](#insn-00bbb4a4)

~~~json
{
  "source": "00bbb4a4",
  "target": "00bbb510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4a8`](#insn-00bbb4a8)

~~~json
{
  "source": "00bbb4a8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4ac`](#insn-00bbb4ac)

~~~json
{
  "source": "00bbb4ac",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4bc`](#insn-00bbb4bc)

~~~json
{
  "source": "00bbb4bc",
  "target": "00bbb4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4c0`](#insn-00bbb4c0)

~~~json
{
  "source": "00bbb4c0",
  "target": "01127428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb4c8`](#insn-00bbb4c8)

~~~json
{
  "source": "00bbb4c8",
  "target": "00bbb4d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4d0`](#insn-00bbb4d0)

~~~json
{
  "source": "00bbb4d0",
  "target": "00bbb4d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4dc`](#insn-00bbb4dc)

~~~json
{
  "source": "00bbb4dc",
  "target": "002bc7ed",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4e0`](#insn-00bbb4e0)

~~~json
{
  "source": "00bbb4e0",
  "target": "00c5b130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4e4`](#insn-00bbb4e4)

~~~json
{
  "source": "00bbb4e4",
  "target": "00c5b0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4ec`](#insn-00bbb4ec)

~~~json
{
  "source": "00bbb4ec",
  "target": "00bbb510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb4f4`](#insn-00bbb4f4)

~~~json
{
  "source": "00bbb4f4",
  "target": "00c5b300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb4fc`](#insn-00bbb4fc)

~~~json
{
  "source": "00bbb4fc",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb504`](#insn-00bbb504)

~~~json
{
  "source": "00bbb504",
  "target": "01127418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb508`](#insn-00bbb508)

~~~json
{
  "source": "00bbb508",
  "target": "00bbb510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb50c`](#insn-00bbb50c)

~~~json
{
  "source": "00bbb50c",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb510`](#insn-00bbb510)

~~~json
{
  "source": "00bbb510",
  "target": "00bbb550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb534`](#insn-00bbb534)

~~~json
{
  "source": "00bbb534",
  "target": "00bbe1e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb534`](#insn-00bbb534)

~~~json
{
  "source": "00bbb534",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb538`](#insn-00bbb538)

~~~json
{
  "source": "00bbb538",
  "target": "00bbe1e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb538`](#insn-00bbb538)

~~~json
{
  "source": "00bbb538",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb53c`](#insn-00bbb53c)

~~~json
{
  "source": "00bbb53c",
  "target": "00bbe398",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb53c`](#insn-00bbb53c)

~~~json
{
  "source": "00bbb53c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb540`](#insn-00bbb540)

~~~json
{
  "source": "00bbb540",
  "target": "00bbe400",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb540`](#insn-00bbb540)

~~~json
{
  "source": "00bbb540",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb54c`](#insn-00bbb54c)

~~~json
{
  "source": "00bbb54c",
  "target": "00c5e5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb550`](#insn-00bbb550)

~~~json
{
  "source": "00bbb550",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb554`](#insn-00bbb554)

~~~json
{
  "source": "00bbb554",
  "target": "00bbb560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb558`](#insn-00bbb558)

~~~json
{
  "source": "00bbb558",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb55c`](#insn-00bbb55c)

~~~json
{
  "source": "00bbb55c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb564`](#insn-00bbb564)

~~~json
{
  "source": "00bbb564",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb56c`](#insn-00bbb56c)

~~~json
{
  "source": "00bbb56c",
  "target": "00bbb590",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb574`](#insn-00bbb574)

~~~json
{
  "source": "00bbb574",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb578`](#insn-00bbb578)

~~~json
{
  "source": "00bbb578",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb57c`](#insn-00bbb57c)

~~~json
{
  "source": "00bbb57c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb580`](#insn-00bbb580)

~~~json
{
  "source": "00bbb580",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb584`](#insn-00bbb584)

~~~json
{
  "source": "00bbb584",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb590`](#insn-00bbb590)

~~~json
{
  "source": "00bbb590",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
