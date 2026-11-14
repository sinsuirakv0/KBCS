# 00bbaaa4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "c0db4de9f59bfaf291ebcee4a2c21ea2a636f1dc526e256ae6a2f90451f44cc0"
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
