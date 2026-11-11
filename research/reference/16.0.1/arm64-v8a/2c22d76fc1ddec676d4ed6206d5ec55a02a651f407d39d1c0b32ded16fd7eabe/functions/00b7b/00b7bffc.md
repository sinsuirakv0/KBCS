# 00b7bffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b7bffc",
  "name": "_ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE",
  "size": 2636,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74e56a06d697692214c17c40c227a1a08bb1b6f79dff2b35b9e64fbd8974ac20",
  "source_text_sha256": "74e56a06d697692214c17c40c227a1a08bb1b6f79dff2b35b9e64fbd8974ac20"
}
~~~

## 呼び出し元

- [00c5c460](../00c5c/00c5c460.md)

## 呼び出し先

- [00b76d2c](../00b76/00b76d2c.md)
- [00b780bc](../00b78/00b780bc.md)
- [00b78960](../00b78/00b78960.md)
- [00b7d130](../00b7d/00b7d130.md)
- [00b7d688](../00b7d/00b7d688.md)
- [00b7de4c](../00b7d/00b7de4c.md)
- [00b7e490](../00b7e/00b7e490.md)
- [00b7e954](../00b7e/00b7e954.md)
- [00b7ee68](../00b7e/00b7ee68.md)
- [00b7f148](../00b7f/00b7f148.md)
- [00bab828](../00bab/00bab828.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c580b0](../00c58/00c580b0.md)
- [00c5a930](../00c5a/00c5a930.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5ba10](../00c5b/00c5ba10.md)
- [00c5be40](../00c5b/00c5be40.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5c1a0](../00c5c/00c5c1a0.md)
- [00c5c220](../00c5c/00c5c220.md)
- [00c5c230](../00c5c/00c5c230.md)
- [00c5c240](../00c5c/00c5c240.md)
- [00c5c250](../00c5c/00c5c250.md)
- [00c5c260](../00c5c/00c5c260.md)
- [00c5c270](../00c5c/00c5c270.md)
- [00c5c5c0](../00c5c/00c5c5c0.md)
- [00c5c6f0](../00c5c/00c5c6f0.md)
- [00c5c750](../00c5c/00c5c750.md)
- [00c5c770](../00c5c/00c5c770.md)

## 関連文字列（未確認候補）

~~~text
"Fixed-length array size is incorrect."
"error: "
~~~

## 疑似コード / UTF-8 22490 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE(char *param_1,long param_2,long param_3)

{
  uint uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined2 uVar4;
  bool bVar5;
  undefined4 *puVar6;
  void *__ptr;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  char cVar10;
  undefined1 *puVar11;
  byte bVar12;
  ulong uVar13;
  int iVar14;
  undefined8 uVar15;
  long lVar16;
  char *pcVar17;
  undefined4 *puVar18;
  undefined4 *puVar19;
  ulong uVar20;
  ulong uVar21;
  undefined4 **local_188;
  undefined4 *puStack_180;
  long local_178;
  ulong local_170;
  undefined8 uStack_168;
  char *local_160;
  undefined2 local_150;
  long *local_148;
  char local_140;
  undefined8 local_138;
  undefined4 local_130;
  undefined8 local_128;
  undefined8 uStack_120;
  uint local_118;
  void *local_110;
  undefined1 *local_108;
  int local_100;
  undefined2 uStack_fc;
  undefined2 uStack_fa;
  undefined6 uStack_f8;
  undefined8 local_f0;
  undefined2 local_e8;
  ulong local_e0;
  undefined2 local_d8;
  void *local_d0;
  undefined4 *local_c8;
  undefined4 *local_c0;
  undefined8 uStack_b8;
  byte local_b0;
  undefined1 uStack_af;
  undefined2 uStack_ae;
  undefined4 uStack_ac;
  void *local_a0;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined8 local_90;
  undefined8 uStack_88;
  ushort local_80;
  long local_78;
  
                    /* try { // try from 00b7c008 to 00c7c023 has its CatchHandler @ 00b7c094 */
  lVar2 = tpidr_el0;
                    /* try { // try from 00b7c024 to 00c7c127 has its CatchHandler @ 00b7becc */
  local_78 = *(long *)(lVar2 + 0x28);
  local_c0 = (undefined4 *)0x0;
  uStack_b8 = 0;
  local_c8 = (undefined4 *)0x0;
  local_148 = (long *)0x0;
  local_140 = '\0';
  local_138 = 0x400;
  local_130 = 0x7fffffff;
  uStack_120 = _UNK_002c3138;
  local_128 = _DAT_002c3130;
  local_118 = 0;
  local_e8 = 0;
  local_110 = (void *)0x0;
  local_108 = (undefined1 *)0x0;
  local_f0 = 0;
  local_100 = 0;
  uStack_fc = 0;
  uStack_fa = 0;
  uStack_f8 = 0;
  local_e0 = 1;
  local_d8 = 0x100;
  local_d0 = (void *)0x0;
  local_98 = *(undefined4 *)(param_3 + 4);
  uStack_88 = *(undefined8 *)(param_3 + 0x10);
  local_90 = *(undefined8 *)(param_3 + 8);
  local_80 = *(ushort *)(param_3 + 0x18);
  uVar20 = (ulong)local_80;
                    /* catch() { ... } // from try @ 00b7c008 with catch @ 00b7c094 */
  local_188 = &local_c8;
  uStack_94 = 0;
  puStack_180 = &local_98;
  local_178 = param_2;
  uVar15 = _ZN11flatbuffers6Parser6ExpectEi(&local_150,param_2,0x5b);
  uVar21 = 0;
  local_150 = CONCAT11(1,(char)local_150);
  if ((char)local_150 == '\0') {
    do {
      if (((uVar21 == 0) || (*(char *)(param_2 + 0x302) == '\0')) &&
         (uVar13 = uVar21, *(int *)(param_2 + 0x1c) == 0x5d)) {
LAB_00b7ca1c:
        uVar21 = uVar13;
        uVar15 = _ZN11flatbuffers6Parser4NextEv(&local_150,param_2);
        cVar10 = (char)local_150;
        bVar5 = true;
        local_150 = local_150 & 0xff;
        if (cVar10 == '\0') {
          bVar5 = false;
          local_150 = 0;
        }
        goto LAB_00b7c0d8;
      }
      uVar15 = FUN_00bab828(&local_150,&local_188);
      bVar5 = true;
      local_150 = CONCAT11(1,(char)local_150);
      if ((char)local_150 != '\0') goto LAB_00b7c0d8;
      uVar13 = uVar21 + 1;
      if (*(int *)(param_2 + 0x1c) == 0x5d) goto LAB_00b7ca1c;
      if (*(char *)(param_2 + 0x418) == '\0') {
        uVar15 = _ZN11flatbuffers6Parser6ExpectEi(&local_150,param_2,0x2c);
        if ((char)local_150 != '\0') goto code_r0x00b7c198;
      }
      local_150 = 0x100;
      uVar21 = uVar21 + 1;
    } while( true );
  }
  bVar5 = true;
LAB_00b7c0d8:
  *param_1 = bVar5;
  local_150 = CONCAT11(1,(char)local_150);
  param_1[1] = '\x01';
  __ptr = local_d0;
  if (!bVar5) {
    if (uVar21 == uVar20) {
      puVar18 = local_c0;
      if (local_c0 != local_c8) {
        do {
          puVar19 = puVar18 + -0x10;
          switch(*puVar19) {
          case 0:
          case 1:
          case 2:
          case 4:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            uVar15 = FUN_00b78960(param_1,lVar16,param_2,&local_b0);
            goto LAB_00b7c23c;
          case 3:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            uVar15 = FUN_00b7d130(param_1,lVar16,param_2,&local_b0);
LAB_00b7c23c:
            bVar12 = local_b0;
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            if (local_e0 == 0) {
              local_e0 = 1;
            }
            if ((int)local_108 == local_100) {
              uVar15 = _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,1);
            }
            local_118 = local_118 + 1;
            local_108[-1] = bVar12;
            local_108 = local_108 + -1;
            break;
          case 5:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            uVar15 = FUN_00b7d688(param_1,lVar16,param_2,&local_b0);
                    /* try { // try from 00b7c5b0 to 00c7c5cf has its CatchHandler @ 00b7d914 */
            goto LAB_00b7c5c8;
          case 6:
                    /* try { // try from 00b7c36c to 00c7c443 has its CatchHandler @ 00b7c36c
                       catch() { ... } // from try @ 00b7c36c with catch @ 00b7c36c
                       catch() { ... } // from try @ 00b7c450 with catch @ 00b7c36c */
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            uVar15 = FUN_00b76d2c(param_1,lVar16,param_2,&local_b0);
LAB_00b7c5c8:
            param_1[1] = '\x01';
                    /* try { // try from 00b7c5d0 to 00c7c62b has its CatchHandler @ 00b7c4f4 */
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            uVar4 = CONCAT11(uStack_af,local_b0);
            if (local_e0 < 2) {
              local_e0 = 2;
            }
            uVar21 = (ulong)local_118 & 1;
            if ((int)uVar21 != 0) {
              if ((uint)((int)local_108 - local_100) < uVar21) {
                uVar15 = _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
              }
              local_108 = local_108 + -uVar21;
              local_118 = local_118 + (int)uVar21;
                    /* try { // try from 00b7c62c to 00c7c637 has its CatchHandler @ 00b7d908 */
              *local_108 = 0;
            }
                    /* try { // try from 00b7c638 to 00c7c6f3 has its CatchHandler @ 00b7c4f4 */
            if (((int)local_108 - local_100 & 0xfffffffeU) == 0) {
              uVar15 = _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,2);
            }
            local_118 = local_118 + 2;
            *(undefined2 *)(local_108 + -2) = uVar4;
            local_108 = local_108 + -2;
            break;
          case 7:
          case 0x11:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b7de4c(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIijEET0_T_
                               (&local_148,CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0)));
            break;
          case 8:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b780bc(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 == '\0') {
              iVar14 = CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0));
              goto LAB_00b7c8b0;
            }
            goto joined_r0x00b7ca10;
          case 9:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b7e490(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIljEET0_T_
                               (&local_148,
                                CONCAT44(uStack_ac,CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0)))
                               );
            break;
          case 10:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b7e954(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 == '\0') {
              lVar16 = CONCAT44(uStack_ac,CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0)));
              goto LAB_00b7c7f4;
            }
            goto joined_r0x00b7ca10;
          case 0xb:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
                    /* try { // try from 00b7c4f4 to 00c7c5af has its CatchHandler @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c4f4 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c5d0 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c638 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c70c with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c774 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c84c with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7c9f8 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7cc20 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7cd88 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7ceb0 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7d31c with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7d4e0 with catch @ 00b7c4f4
                       catch() { ... } // from try @ 00b7d600 with catch @ 00b7c4f4 */
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b7ee68(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIfjEET0_T_
                               (CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0)),&local_148);
            break;
          case 0xc:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              lVar16 = (long)puVar18 + -0x1f;
            }
            else {
              lVar16 = *(long *)(puVar18 + -4);
            }
            FUN_00b7f148(param_1,lVar16,param_2,&local_b0);
            param_1[1] = '\x01';
            __ptr = local_d0;
            if (*param_1 != '\0') goto joined_r0x00b7ca10;
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIdjEET0_T_
                               (CONCAT44(uStack_ac,CONCAT22(uStack_ae,CONCAT11(uStack_af,local_b0)))
                                ,&local_148);
            break;
          case 0xd:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              pcVar17 = (char *)((long)puVar18 + -0x1f);
            }
            else {
              pcVar17 = *(char **)(puVar18 + -4);
            }
            iVar14 = atoi(pcVar17);
            param_1[0] = '\0';
            param_1[1] = '\x01';
            if (local_e0 < 4) {
              local_e0 = 4;
            }
            uVar1 = -local_118 & 3;
            uVar21 = (ulong)uVar1;
                    /* try { // try from 00b7c6f4 to 00c7c70b has its CatchHandler @ 00b7d904 */
            if (uVar1 != 0) {
              if ((uint)((int)local_108 - local_100) < uVar21) {
                    /* try { // try from 00b7c70c to 00c7c767 has its CatchHandler @ 00b7c4f4 */
                _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
              }
              local_108 = local_108 + -uVar21;
              local_118 = local_118 + uVar1;
              *local_108 = 0;
              if (uVar1 != 1) {
                uVar20 = 1;
                do {
                  local_108[uVar20] = 0;
                  uVar20 = uVar20 + 1;
                } while (uVar21 != uVar20);
              }
            }
            goto LAB_00b7c8a4;
          case 0xe:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              pcVar17 = (char *)((long)puVar18 + -0x1f);
            }
            else {
              pcVar17 = *(char **)(puVar18 + -4);
            }
            iVar14 = atoi(pcVar17);
            param_1[0] = '\0';
            param_1[1] = '\x01';
            if (local_e0 < 4) {
              local_e0 = 4;
            }
            uVar1 = -local_118 & 3;
            uVar21 = (ulong)uVar1;
            if (uVar1 != 0) {
                    /* catch() { ... } // from try @ 00b7c444 with catch @ 00b7c4a4 */
              if ((uint)((int)local_108 - local_100) < uVar21) {
                _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
              }
              local_108 = local_108 + -uVar21;
              local_118 = local_118 + uVar1;
              *local_108 = 0;
              if (uVar1 != 1) {
                uVar20 = 1;
                do {
                  local_108[uVar20] = 0;
                  uVar20 = uVar20 + 1;
                } while (uVar21 != uVar20);
              }
            }
            goto LAB_00b7c8a4;
          case 0xf:
            if (*(char *)(*(long *)(puVar18 + -0xe) + 0xd0) == '\0') {
              if ((*(byte *)(puVar18 + -8) & 1) == 0) {
                pcVar17 = (char *)((long)puVar18 + -0x1f);
              }
              else {
                pcVar17 = *(char **)(puVar18 + -4);
              }
              iVar14 = atoi(pcVar17);
              param_1[0] = '\0';
              param_1[1] = '\x01';
              if (local_e0 < 4) {
                    /* try { // try from 00b7c834 to 00c7c84b has its CatchHandler @ 00b7d8fc */
                local_e0 = 4;
              }
              uVar1 = -local_118 & 3;
              uVar21 = (ulong)uVar1;
              if (uVar1 != 0) {
                    /* try { // try from 00b7c84c to 00c7c9df has its CatchHandler @ 00b7c4f4 */
                if ((uint)((int)local_108 - local_100) < uVar21) {
                  _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
                }
                local_108 = local_108 + -uVar21;
                local_118 = local_118 + uVar1;
                *local_108 = 0;
                if (uVar1 != 1) {
                  uVar20 = 1;
                  do {
                    local_108[uVar20] = 0;
                    uVar20 = uVar20 + 1;
                  } while (uVar21 != uVar20);
                }
              }
              goto LAB_00b7c8a4;
            }
            uVar15 = _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE
                               (uVar15,&local_148,*(long *)(puVar18 + -0xe),puVar19);
            break;
          case 0x10:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              pcVar17 = (char *)((long)puVar18 + -0x1f);
            }
            else {
              pcVar17 = *(char **)(puVar18 + -4);
            }
            iVar14 = atoi(pcVar17);
            param_1[0] = '\0';
            param_1[1] = '\x01';
            if (local_e0 < 4) {
              local_e0 = 4;
            }
            uVar1 = -local_118 & 3;
            uVar21 = (ulong)uVar1;
            if (uVar1 != 0) {
              if ((uint)((int)local_108 - local_100) < uVar21) {
                _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
              }
              local_108 = local_108 + -uVar21;
              local_118 = local_118 + uVar1;
              *local_108 = 0;
              if (uVar1 != 1) {
                    /* try { // try from 00b7c444 to 00c7c44f has its CatchHandler @ 00b7c4a4 */
                uVar20 = 1;
                do {
                  local_108[uVar20] = 0;
                    /* try { // try from 00b7c450 to 00c7c4cb has its CatchHandler @ 00b7c36c */
                  uVar20 = uVar20 + 1;
                } while (uVar21 != uVar20);
              }
            }
LAB_00b7c8a4:
            iVar14 = (local_118 - iVar14) + 4;
LAB_00b7c8b0:
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
                               (&local_148,iVar14);
            break;
          case 0x12:
            if ((*(byte *)(puVar18 + -8) & 1) == 0) {
              pcVar17 = (char *)((long)puVar18 + -0x1f);
            }
            else {
              pcVar17 = *(char **)(puVar18 + -4);
            }
            iVar14 = atoi(pcVar17);
            param_1[0] = '\0';
            param_1[1] = '\x01';
                    /* try { // try from 00b7c768 to 00c7c773 has its CatchHandler @ 00b7d900 */
            if (local_e0 < 8) {
                    /* try { // try from 00b7c774 to 00c7c833 has its CatchHandler @ 00b7c4f4 */
              local_e0 = 8;
            }
            uVar1 = -local_118 & 7;
            uVar21 = (ulong)uVar1;
            if (uVar1 != 0) {
              if ((uint)((int)local_108 - local_100) < uVar21) {
                _ZN11flatbuffers15vector_downwardIjE10reallocateEm(&local_148,uVar21);
              }
              local_108 = local_108 + -uVar21;
              local_118 = local_118 + uVar1;
              *local_108 = 0;
              if (uVar1 != 1) {
                uVar20 = 1;
                do {
                  local_108[uVar20] = 0;
                  uVar20 = uVar20 + 1;
                } while (uVar21 != uVar20);
              }
            }
            lVar16 = ((ulong)local_118 - (long)iVar14) + 8;
LAB_00b7c7f4:
            uVar15 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementImjEET0_T_
                               (&local_148,lVar16);
          }
          puVar18 = puVar19;
        } while (puVar19 != local_c8);
      }
      puVar11 = local_108;
      uVar15 = _ZN11flatbuffers10InlineSizeERKNS_4TypeE(param_3);
                    /* try { // try from 00b7c9f8 to 00c7cbbb has its CatchHandler @ 00b7c4f4 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                (param_3 + 0x20,puVar11,uVar15);
      param_1[0] = '\0';
      param_1[1] = '\0';
      __ptr = local_d0;
    }
    else {
      local_160 = (char *)_Znwm(0x30);
      uStack_168 = _UNK_002c2618;
      local_170 = _DAT_002c2610;
      uVar9 = s_Fixed_length_array_size_is_incor_002a0c87._16_8_;
      uVar8 = s_Fixed_length_array_size_is_incor_002a0c87._8_8_;
      uVar7 = s_Fixed_length_array_size_is_incor_002a0c87._0_8_;
      uVar15 = CONCAT35(s_Fixed_length_array_size_is_incor_002a0c87._29_3_,
                        s_Fixed_length_array_size_is_incor_002a0c87._24_5_);
      uVar3 = CONCAT53(s_Fixed_length_array_size_is_incor_002a0c87._32_5_,
                       s_Fixed_length_array_size_is_incor_002a0c87._29_3_);
      local_160[0x25] = '\0';
      *(undefined8 *)(local_160 + 8) = uVar8;
      *(undefined8 *)local_160 = uVar7;
      *(undefined8 *)(local_160 + 0x18) = uVar15;
      *(undefined8 *)(local_160 + 0x10) = uVar9;
      *(undefined8 *)(local_160 + 0x1d) = uVar3;
      _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
                (&local_b0,"error: ",&local_170);
      _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
                (param_2,&local_b0);
      if ((local_b0 & 1) != 0) {
        _ZdlPv(local_a0);
      }
      param_1[0] = '\x01';
      param_1[1] = '\0';
      __ptr = local_d0;
      if ((local_170 & 1) != 0) {
        _ZdlPv(local_160);
                    /* try { // try from 00b7c9e0 to 00c7c9f7 has its CatchHandler @ 00b7d8f8 */
        __ptr = local_d0;
      }
    }
  }
joined_r0x00b7ca10:
  local_d0 = __ptr;
  if (__ptr != (void *)0x0) {
    _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_21FlatBufferBuilderImplILb0EE19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (__ptr,*(undefined8 *)((long)__ptr + 8));
    _ZdlPv(__ptr);
  }
  if (local_110 != (void *)0x0) {
    if (local_148 == (long *)0x0) {
      _ZdaPv(local_110);
    }
    else {
                    /* catch() { ... } // from try @ 00b7bfe4 with catch @ 00b7c118 */
      (**(code **)(*local_148 + 0x18))(local_148,local_110,uStack_120);
    }
  }
  local_110 = (void *)0x0;
  if ((local_140 != '\0') && (local_148 != (long *)0x0)) {
    (**(code **)(*local_148 + 8))();
  }
  puVar18 = local_c8;
  puVar19 = local_c0;
  if (local_c8 != (undefined4 *)0x0) {
    while (puVar6 = puVar19, puVar6 != puVar18) {
      puVar19 = puVar6 + -0x10;
      if ((*(byte *)(puVar6 + -8) & 1) != 0) {
        _ZdlPv(*(void **)(puVar6 + -4));
      }
    }
    local_c0 = puVar18;
    _ZdlPv(local_c8);
  }
  if (*(long *)(lVar2 + 0x28) == local_78) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
code_r0x00b7c198:
  bVar5 = true;
  local_150 = local_150 & 0xff;
  uVar21 = uVar21 + 1;
  goto LAB_00b7c0d8;
}

~~~
