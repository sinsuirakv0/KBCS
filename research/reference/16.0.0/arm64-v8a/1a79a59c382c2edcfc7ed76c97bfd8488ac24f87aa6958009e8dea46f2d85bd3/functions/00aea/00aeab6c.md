# 00aeab6c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeab6c",
  "name": "FUN_00aeab6c",
  "size": 2380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc9598e93d895d7585c7320c6f6bbd3aadd8455bb6addc1411f1dabebae04014",
  "source_text_sha256": "fc9598e93d895d7585c7320c6f6bbd3aadd8455bb6addc1411f1dabebae04014"
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [006623ac](../00662/006623ac.md)
- [00662450](../00662/00662450.md)
- [006624f4](../00662/006624f4.md)
- [006dfafc](../006df/006dfafc.md)
- [00802678](../00802/00802678.md)
- [009e0e24](../009e0/009e0e24.md)
- [00a32c10](../00a32/00a32c10.md)
- [00ace960](../00ace/00ace960.md)
- [00aeb4b8](../00aeb/00aeb4b8.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57b40](../00c57/00c57b40.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 22385 bytes

~~~c

void FUN_00aeab6c(long param_1)

{
  short sVar1;
  uint uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  char cVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  byte bVar12;
  byte bVar13;
  char cVar14;
  byte bVar15;
  byte bVar16;
  char cVar17;
  byte bVar18;
  byte bVar19;
  byte bVar20;
  char cVar21;
  byte bVar22;
  char cVar23;
  char cVar24;
  byte bVar25;
  byte bVar26;
  char cVar27;
  byte bVar28;
  byte bVar29;
  byte bVar30;
  byte bVar31;
  char cVar32;
  char cVar33;
  char cVar34;
  size_t __n;
  long lVar35;
  short sVar36;
  short sVar37;
  short sVar38;
  short sVar39;
  short sVar40;
  short sVar41;
  short sVar42;
  short sVar43;
  short sVar44;
  short sVar45;
  bool bVar46;
  undefined1 uVar47;
  int iVar48;
  wchar_t __c;
  ulong uVar49;
  undefined8 *puVar50;
  wchar_t *pwVar51;
  wchar_t *pwVar52;
  undefined8 *puVar53;
  undefined8 *puVar54;
  void *__dest;
  undefined8 uVar55;
  undefined8 *puVar56;
  undefined8 *puVar57;
  long *plVar58;
  ulong uVar59;
  ulong uVar60;
  void *__src;
  wchar_t *pwVar61;
  int iVar62;
  undefined8 *puVar63;
  long lVar64;
  int iVar65;
  undefined8 uVar66;
  undefined8 uVar67;
  undefined8 uVar68;
  undefined8 uVar69;
  wchar_t local_a8;
  undefined2 local_a4;
  char local_a2;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  char local_88;
  undefined1 uStack_87;
  short local_86;
  char local_84;
  undefined1 uStack_83;
  short local_82;
  char cStack_80;
  undefined1 uStack_7f;
  short sStack_7e;
  char cStack_7c;
  undefined1 uStack_7b;
  undefined8 uStack_7a;
  long local_70;
  
                    /* try { // try from 00aeab78 to 00beab7f has its CatchHandler @ 00aead28 */
  lVar35 = tpidr_el0;
  local_70 = *(long *)(lVar35 + 0x28);
  iVar48 = FUN_00802678(0);
  uVar2 = iVar48 + 0x19;
                    /* try { // try from 00aeabc4 to 00beabcf has its CatchHandler @ 00aead30 */
  if (((0x13 < uVar2) ||
      (((1 << (ulong)(uVar2 & 0x1f) & 0x87c11U) == 0 &&
       ((uVar2 != 0x11 || (uVar49 = FUN_00a32c10(param_1 + 0x530), (uVar49 & 1) != 0)))))) &&
     (uVar49 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff), (uVar49 & 1) == 0)) {
    uVar47 = FUN_006623ac(param_1 + 0x22c8);
    local_a4 = CONCAT11(local_a4._1_1_,uVar47);
    uVar47 = FUN_00662450(param_1 + 0x22c8);
    local_a4 = CONCAT11(uVar47,(undefined1)local_a4);
    local_a2 = FUN_006624f4(param_1 + 0x22c8);
    bVar3 = *(byte *)(param_1 + 0xc97c);
    bVar4 = *(byte *)(param_1 + 0xc97d);
    bVar5 = *(byte *)(param_1 + 0xc954);
    bVar6 = *(byte *)(param_1 + 0xc955);
    bVar7 = *(byte *)(param_1 + 0xc958);
    cVar8 = *(char *)((long)&fde_table_entry_003339b8.initial_loc + param_1);
    bVar9 = *(byte *)(param_1 + 0xc978);
    bVar10 = *(byte *)(param_1 + 0xc959);
    bVar11 = *(byte *)(param_1 + 0xc95c);
    bVar12 = *(byte *)(param_1 + 0xc95d);
    bVar13 = *(byte *)(param_1 + 0xc960);
    cVar14 = *(char *)((long)&fde_table_entry_003339b8.data_loc + param_1);
    bVar15 = *(byte *)(param_1 + 0xc964);
    bVar16 = *(byte *)(param_1 + 0xc961);
    cVar17 = *(char *)((long)&fde_table_entry_003339c0.initial_loc + param_1);
    bVar18 = *(byte *)(param_1 + 0xc965);
    bVar19 = *(byte *)(param_1 + 0xc968);
                    /* try { // try from 00aeacfc to 00beacff has its CatchHandler @ 00aead80 */
    bVar20 = *(byte *)(param_1 + 0xc969);
    cVar21 = *(char *)((long)&fde_table_entry_003339c0.data_loc + param_1);
                    /* try { // try from 00aead10 to 00bead13 has its CatchHandler @ 00aead38 */
    bVar22 = *(byte *)(param_1 + 0xc96c);
                    /* try { // try from 00aead24 to 00bead27 has its CatchHandler @ 00aead30 */
                    /* catch() { ... } // from try @ 00aeab78 with catch @ 00aead28
                       try { // try from 00aead28 to 00beade7 has its CatchHandler @ 00aea7d8 */
                    /* catch() { ... } // from try @ 00aeab0c with catch @ 00aead2c */
    cVar23 = *(char *)((long)&fde_table_entry_003339c8.data_loc + param_1);
                    /* catch() { ... } // from try @ 00aeabc4 with catch @ 00aead30
                       catch() { ... } // from try @ 00aead24 with catch @ 00aead30 */
    cVar24 = *(char *)((long)&fde_table_entry_003339c8.initial_loc + param_1);
                    /* catch() { ... } // from try @ 00aea924 with catch @ 00aead34 */
                    /* catch() { ... } // from try @ 00aeab58 with catch @ 00aead38
                       catch() { ... } // from try @ 00aead10 with catch @ 00aead38 */
    bVar25 = *(byte *)(param_1 + 0xc96d);
    bVar26 = *(byte *)(param_1 + 0xc974);
                    /* catch() { ... } // from try @ 00aea8ec with catch @ 00aead50 */
                    /* catch() { ... } // from try @ 00aea8a0 with catch @ 00aead54 */
    cVar27 = *(char *)((long)&fde_table_entry_003339d0.initial_loc + param_1);
    bVar28 = *(byte *)(param_1 + 0xc975);
                    /* catch() { ... } // from try @ 00aea894 with catch @ 00aead64 */
    bVar29 = *(byte *)(param_1 + 0xc970);
    bVar30 = *(byte *)(param_1 + 0xc971);
                    /* catch() { ... } // from try @ 00aeaa9c with catch @ 00aead74 */
                    /* catch() { ... } // from try @ 00aea884 with catch @ 00aead78 */
                    /* catch() { ... } // from try @ 00aeaae8 with catch @ 00aead80
                       catch() { ... } // from try @ 00aeacfc with catch @ 00aead80 */
                    /* catch() { ... } // from try @ 00aea858 with catch @ 00aead84 */
    bVar31 = *(byte *)(param_1 + 0xc979);
    cVar32 = *(char *)((long)&fde_table_entry_003339d0.data_loc + param_1);
                    /* catch() { ... } // from try @ 00aea824 with catch @ 00aeada0 */
    cVar33 = *(char *)((long)&fde_table_entry_003339d8.initial_loc + param_1);
    cVar34 = *(char *)((long)&fde_table_entry_003339d8.data_loc + param_1);
                    /* catch() { ... } // from try @ 00aea9f4 with catch @ 00aeadac */
                    /* catch() { ... } // from try @ 00aeaa54 with catch @ 00aeadb0 */
                    /* catch() { ... } // from try @ 00aea984 with catch @ 00aeadb4 */
    __c = FUN_00ace960(param_1);
    puVar63 = *(undefined8 **)(param_1 + 0x33c0);
    puVar56 = (undefined8 *)(param_1 + 0x33c8);
    local_a8 = __c;
    while (puVar63 != puVar56) {
      pwVar52 = (wchar_t *)puVar63[6];
      pwVar51 = wmemchr((wchar_t *)puVar63[5],__c,(long)pwVar52 - (long)puVar63[5] >> 2);
      pwVar61 = (wchar_t *)puVar63[6];
      if (pwVar51 != (wchar_t *)0x0) {
        pwVar52 = pwVar51;
      }
      if (pwVar52 != pwVar61) {
        pwVar52 = wmemchr((wchar_t *)puVar63[5],__c,(long)pwVar61 - (long)puVar63[5] >> 2);
        if (pwVar52 != (wchar_t *)0x0) {
          pwVar61 = pwVar52;
        }
        __n = puVar63[6] - (long)(pwVar61 + 1);
                    /* try { // try from 00aeaf8c to 00beaf93 has its CatchHandler @ 00aebe74 */
        if (__n != 0) {
          memmove(pwVar61,pwVar61 + 1,__n);
        }
        puVar63[6] = (long)pwVar61 + __n;
      }
      puVar57 = (undefined8 *)puVar63[1];
      puVar53 = puVar63;
      if ((undefined8 *)puVar63[1] == (undefined8 *)0x0) {
        do {
          puVar63 = (undefined8 *)puVar53[2];
          bVar46 = (undefined8 *)*puVar63 != puVar53;
          puVar53 = puVar63;
        } while (bVar46);
      }
      else {
        do {
          puVar63 = puVar57;
          puVar57 = (undefined8 *)*puVar63;
        } while ((undefined8 *)*puVar63 != (undefined8 *)0x0);
      }
    }
                    /* catch() { ... } // from try @ 00aeb08c with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb198 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb36c with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb3fc with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb490 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb520 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb6f4 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb73c with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeb9d4 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aeba70 with catch @ 00aeade8
                       catch() { ... } // from try @ 00aebc6c with catch @ 00aeade8 */
    sVar36 = CONCAT11(bVar4 ^ bVar6,bVar3 ^ bVar5);
    sVar38 = CONCAT11(bVar4 ^ bVar10,bVar3 ^ bVar7);
    sVar39 = CONCAT11(bVar4 ^ bVar12,bVar3 ^ bVar11);
    sVar40 = CONCAT11(bVar4 ^ bVar18,bVar3 ^ bVar15);
    sVar41 = CONCAT11(bVar4 ^ bVar16,bVar3 ^ bVar13);
    puVar63 = (undefined8 *)(param_1 + 0x33b0);
    sVar42 = CONCAT11(bVar4 ^ bVar25,bVar3 ^ bVar22);
    sVar43 = CONCAT11(bVar4 ^ bVar20,bVar3 ^ bVar19);
    puVar57 = *(undefined8 **)(param_1 + 0x33a8);
    sVar37 = CONCAT11(bVar4 ^ bVar30,bVar3 ^ bVar29);
    sVar44 = CONCAT11(bVar4 ^ bVar28,bVar3 ^ bVar26);
    sVar45 = CONCAT11(bVar4 ^ bVar31,bVar3 ^ bVar9);
                    /* try { // try from 00aeae40 to 00beae47 has its CatchHandler @ 00aebe90 */
    while (puVar57 != puVar63) {
      uVar67 = *(undefined8 *)((long)puVar57 + 0x22);
      uVar55 = *(undefined8 *)((long)puVar57 + 0x1a);
      uVar66 = *(undefined8 *)((long)puVar57 + 0x32);
      uVar69 = *(undefined8 *)((long)puVar57 + 0x2a);
      local_88 = (char)uVar66;
      uStack_87 = (undefined1)((ulong)uVar66 >> 8);
      local_86 = (short)((ulong)uVar66 >> 0x10);
      local_84 = (char)((ulong)uVar66 >> 0x20);
      uStack_83 = (undefined1)((ulong)uVar66 >> 0x28);
      uVar68 = puVar57[8];
      uVar66 = puVar57[7];
      local_a0._2_2_ = (short)((ulong)uVar55 >> 0x10);
      local_82 = (short)uVar66;
      cStack_80 = (char)((ulong)uVar66 >> 0x10);
      uStack_7f = (undefined1)((ulong)uVar66 >> 0x18);
      sStack_7e = (short)((ulong)uVar66 >> 0x20);
      cStack_7c = (char)((ulong)uVar66 >> 0x30);
      uStack_7b = (undefined1)((ulong)uVar66 >> 0x38);
      local_a0 = uVar55;
      uStack_98 = uVar67;
      local_90 = uVar69;
      uStack_7a = uVar68;
                    /* try { // try from 00aeb064 to 00beb08b has its CatchHandler @ 00aebe60 */
                    /* try { // try from 00aeb08c to 00beb107 has its CatchHandler @ 00aeade8 */
      if ((((((local_a0._2_2_ == sVar36) &&
             (local_a0._4_1_ = (char)((ulong)uVar55 >> 0x20), local_a0._4_1_ == cVar8)) &&
            (local_a0._6_2_ = (short)((ulong)uVar55 >> 0x30), local_a0._6_2_ == sVar38)) &&
           ((uStack_98._0_1_ = (char)uVar67, (char)uStack_98 == cVar14 &&
            (uStack_98._2_2_ = (short)((ulong)uVar67 >> 0x10), uStack_98._2_2_ == sVar39)))) &&
          (((uStack_98._4_1_ = (char)((ulong)uVar67 >> 0x20), uStack_98._4_1_ == cVar17 &&
            ((uStack_98._6_2_ = (short)((ulong)uVar67 >> 0x30), uStack_98._6_2_ == sVar41 &&
             (local_90._0_1_ = (char)uVar69, (char)local_90 == cVar21)))) &&
           (local_90._2_2_ = (short)((ulong)uVar69 >> 0x10), local_90._2_2_ == sVar40)))) &&
         (((((local_90._4_1_ = (char)((ulong)uVar69 >> 0x20), local_90._4_1_ == cVar24 &&
             (local_90._6_2_ = (short)((ulong)uVar69 >> 0x30), local_90._6_2_ == sVar43)) &&
            (local_88 == cVar23)) &&
           (((local_86 == sVar42 && (local_84 == cVar27)) &&
            ((local_82 == sVar37 && ((cStack_80 == cVar32 && (sStack_7e == sVar44)))))))) &&
          ((cStack_7c == cVar33 &&
           ((uStack_7a._0_2_ = (short)uVar68, (short)uStack_7a == sVar45 &&
            (uStack_7a._2_1_ = (char)((ulong)uVar68 >> 0x10), uStack_7a._2_1_ == cVar34)))))))) {
        uStack_7a._4_2_ = (short)((ulong)uVar68 >> 0x20);
                    /* try { // try from 00aeb108 to 00beb10f has its CatchHandler @ 00aebe54 */
        uStack_7a._6_1_ = (char)((ulong)uVar68 >> 0x30);
        if (uStack_7a._4_2_ == local_a4 && uStack_7a._6_1_ == local_a2) {
                    /* try { // try from 00aeb478 to 00beb48f has its CatchHandler @ 00aebd64 */
          uVar55 = FUN_00aeb4b8(param_1 + 0x33c0,&local_a0);
          FUN_006dfafc(uVar55,&local_a8);
          goto LAB_00aeabc8;
        }
      }
      puVar53 = puVar57;
      puVar54 = (undefined8 *)puVar57[1];
      if ((undefined8 *)puVar57[1] == (undefined8 *)0x0) {
        do {
          puVar57 = (undefined8 *)puVar53[2];
          bVar46 = (undefined8 *)*puVar57 != puVar53;
          puVar53 = puVar57;
        } while (bVar46);
      }
      else {
        do {
          puVar57 = puVar54;
          puVar54 = (undefined8 *)*puVar57;
        } while ((undefined8 *)*puVar57 != (undefined8 *)0x0);
      }
    }
    iVar48 = *(int *)(param_1 + 0x33d0);
    iVar65 = iVar48;
    if (0 < iVar48) {
      iVar62 = 0;
      do {
                    /* try { // try from 00aeae84 to 00beaed3 has its CatchHandler @ 00aebe9c */
        sVar1 = (short)iVar62;
        puVar57 = (undefined8 *)*puVar56;
        puVar53 = puVar56;
        puVar54 = puVar56;
        if ((undefined8 *)*puVar56 != (undefined8 *)0x0) {
          do {
            while (puVar50 = puVar57, puVar53 = puVar50, sVar1 < *(short *)(puVar50 + 4)) {
              puVar57 = (undefined8 *)*puVar50;
              puVar54 = puVar50;
              if ((undefined8 *)*puVar50 == (undefined8 *)0x0) goto LAB_00aeaebc;
            }
            if (sVar1 <= *(short *)(puVar50 + 4)) goto LAB_00aeaf14;
            puVar57 = (undefined8 *)puVar50[1];
          } while ((undefined8 *)puVar50[1] != (undefined8 *)0x0);
          puVar54 = puVar50 + 1;
        }
LAB_00aeaebc:
        puVar50 = (undefined8 *)_Znwm(0x40);
        puVar50[6] = 0;
        puVar50[7] = 0;
        puVar50[5] = 0;
        *puVar50 = 0;
        puVar50[1] = 0;
        puVar50[2] = puVar53;
        *puVar54 = puVar50;
        plVar58 = *(long **)(param_1 + 0x33c0);
        *(short *)(puVar50 + 4) = sVar1;
        puVar57 = puVar50;
        if (*plVar58 != 0) {
          *(long *)(param_1 + 0x33c0) = *plVar58;
          puVar57 = (undefined8 *)*puVar54;
        }
        FUN_0043bb64(*(undefined8 *)(param_1 + 0x33c8),puVar57);
        *(long *)(param_1 + 0x33d0) = *(long *)(param_1 + 0x33d0) + 1;
LAB_00aeaf14:
        iVar65 = iVar62;
      } while ((puVar50[5] != puVar50[6]) &&
              (iVar62 = iVar62 + 1, iVar65 = iVar48, iVar62 != iVar48
                    /* try { // try from 00aeaf24 to 00beaf47 has its CatchHandler @ 00aebe80 */));
    }
    puVar57 = (undefined8 *)*puVar63;
    sVar1 = (short)iVar65;
    puVar53 = puVar57;
    puVar54 = puVar63;
    puVar50 = puVar63;
    if (puVar57 != (undefined8 *)0x0) {
      do {
        while (puVar54 = puVar53, sVar1 < *(short *)((long)puVar54 + 0x1a)) {
          puVar53 = (undefined8 *)*puVar54;
          puVar50 = puVar54;
          if ((undefined8 *)*puVar54 == (undefined8 *)0x0) goto LAB_00aeb198;
        }
        puVar53 = puVar54;
        if (sVar1 <= *(short *)((long)puVar54 + 0x1a)) goto LAB_00aeb1fc;
        puVar53 = (undefined8 *)puVar54[1];
      } while ((undefined8 *)puVar54[1] != (undefined8 *)0x0);
      puVar50 = puVar54 + 1;
    }
LAB_00aeb198:
                    /* try { // try from 00aeb198 to 00beb1eb has its CatchHandler @ 00aeade8 */
    puVar53 = (undefined8 *)_Znwm(0x48);
    *puVar53 = 0;
    puVar53[1] = 0;
    puVar53[2] = puVar54;
    *(short *)((long)puVar53 + 0x1a) = sVar1;
    *(undefined8 *)((long)puVar53 + 0x24) = 0;
    *(undefined8 *)((long)puVar53 + 0x1c) = 0;
    *(undefined8 *)((long)puVar53 + 0x34) = 0;
    *(undefined8 *)((long)puVar53 + 0x2c) = 0;
    *(undefined8 *)((long)puVar53 + 0x3f) = 0;
    *(undefined8 *)((long)puVar53 + 0x37) = 0;
    *puVar50 = puVar53;
    puVar57 = puVar53;
    if (**(long **)(param_1 + 0x33a8) != 0) {
      *(long *)(param_1 + 0x33a8) = **(long **)(param_1 + 0x33a8);
      puVar57 = (undefined8 *)*puVar50;
    }
    FUN_0043bb64(*(undefined8 *)(param_1 + 0x33b0),puVar57);
                    /* try { // try from 00aeb1ec to 00beb213 has its CatchHandler @ 00aebe50 */
    puVar57 = *(undefined8 **)(param_1 + 0x33b0);
    *(long *)(param_1 + 0x33b8) = *(long *)(param_1 + 0x33b8) + 1;
LAB_00aeb1fc:
    *(short *)((long)puVar53 + 0x1c) = sVar36;
    *(char *)((long)puVar53 + 0x1e) = cVar8;
    *(short *)(puVar53 + 4) = sVar38;
    *(char *)((long)puVar53 + 0x22) = cVar14;
    *(short *)((long)puVar53 + 0x24) = sVar39;
    *(char *)((long)puVar53 + 0x26) = cVar17;
    *(short *)(puVar53 + 5) = sVar41;
    *(char *)((long)puVar53 + 0x2a) = cVar21;
    *(short *)((long)puVar53 + 0x2c) = sVar40;
    *(char *)((long)puVar53 + 0x2e) = cVar24;
    *(short *)(puVar53 + 6) = sVar43;
    *(char *)((long)puVar53 + 0x32) = cVar23;
    *(short *)((long)puVar53 + 0x34) = sVar42;
    *(char *)((long)puVar53 + 0x36) = cVar27;
    *(short *)(puVar53 + 7) = sVar37;
                    /* try { // try from 00aeb274 to 00beb27b has its CatchHandler @ 00aebe48 */
    *(char *)((long)puVar53 + 0x3a) = cVar32;
    *(short *)((long)puVar53 + 0x3c) = sVar44;
    *(char *)((long)puVar53 + 0x3e) = cVar33;
    *(short *)(puVar53 + 8) = sVar45;
    *(char *)((long)puVar53 + 0x42) = cVar34;
    puVar53 = puVar63;
    if (puVar57 != (undefined8 *)0x0) {
      do {
                    /* try { // try from 00aeb2b8 to 00beb31f has its CatchHandler @ 00aebe5c */
        while (puVar54 = puVar57, puVar63 = puVar54, sVar1 < *(short *)((long)puVar54 + 0x1a)) {
          puVar57 = (undefined8 *)*puVar54;
          puVar53 = puVar54;
          if ((undefined8 *)*puVar54 == (undefined8 *)0x0) goto LAB_00aeb2d0;
        }
        if (sVar1 <= *(short *)((long)puVar54 + 0x1a)) goto LAB_00aeb32c;
        puVar57 = (undefined8 *)puVar54[1];
      } while ((undefined8 *)puVar54[1] != (undefined8 *)0x0);
      puVar53 = puVar54 + 1;
    }
LAB_00aeb2d0:
    puVar54 = (undefined8 *)_Znwm(0x48);
    *puVar54 = 0;
    puVar54[1] = 0;
    puVar54[2] = puVar63;
    *(short *)((long)puVar54 + 0x1a) = sVar1;
    *(undefined8 *)((long)puVar54 + 0x24) = 0;
    *(undefined8 *)((long)puVar54 + 0x1c) = 0;
    *(undefined8 *)((long)puVar54 + 0x34) = 0;
    *(undefined8 *)((long)puVar54 + 0x2c) = 0;
    *(undefined8 *)((long)puVar54 + 0x3f) = 0;
    *(undefined8 *)((long)puVar54 + 0x37) = 0;
    *puVar53 = puVar54;
    puVar63 = puVar54;
    if (**(long **)(param_1 + 0x33a8) != 0) {
      *(long *)(param_1 + 0x33a8) = **(long **)(param_1 + 0x33a8);
      puVar63 = (undefined8 *)*puVar53;
    }
    FUN_0043bb64(*(undefined8 *)(param_1 + 0x33b0),puVar63);
    *(long *)(param_1 + 0x33b8) = *(long *)(param_1 + 0x33b8) + 1;
LAB_00aeb32c:
    *(short *)((long)puVar54 + 0x44) = local_a4;
    *(char *)((long)puVar54 + 0x46) = local_a2;
    puVar63 = (undefined8 *)*puVar56;
    puVar57 = puVar56;
    if ((undefined8 *)*puVar56 != (undefined8 *)0x0) {
      do {
        while (puVar53 = puVar63, puVar56 = puVar53, sVar1 < *(short *)(puVar53 + 4)) {
          puVar63 = (undefined8 *)*puVar53;
          puVar57 = puVar53;
          if ((undefined8 *)*puVar53 == (undefined8 *)0x0) goto LAB_00aeb378;
        }
        if (sVar1 <= *(short *)(puVar53 + 4)) goto LAB_00aeb3cc;
                    /* try { // try from 00aeb36c to 00beb3c3 has its CatchHandler @ 00aeade8 */
        puVar63 = (undefined8 *)puVar53[1];
      } while ((undefined8 *)puVar53[1] != (undefined8 *)0x0);
      puVar57 = puVar53 + 1;
    }
LAB_00aeb378:
    puVar53 = (undefined8 *)_Znwm(0x40);
    puVar53[6] = 0;
    puVar53[7] = 0;
    puVar53[5] = 0;
    *puVar53 = 0;
    puVar53[1] = 0;
    puVar53[2] = puVar56;
    *puVar57 = puVar53;
    plVar58 = *(long **)(param_1 + 0x33c0);
    *(short *)(puVar53 + 4) = sVar1;
    puVar56 = puVar53;
    if (*plVar58 != 0) {
      *(long *)(param_1 + 0x33c0) = *plVar58;
      puVar56 = (undefined8 *)*puVar57;
    }
    FUN_0043bb64(*(undefined8 *)(param_1 + 0x33c8),puVar56);
                    /* try { // try from 00aeb3c4 to 00beb3d3 has its CatchHandler @ 00aebe04 */
    *(long *)(param_1 + 0x33d0) = *(long *)(param_1 + 0x33d0) + 1;
LAB_00aeb3cc:
    pwVar52 = (wchar_t *)puVar53[6];
                    /* try { // try from 00aeb3d4 to 00beb3e3 has its CatchHandler @ 00aebdc4 */
    if (pwVar52 < (wchar_t *)puVar53[7]) {
      pwVar51 = pwVar52 + 1;
      *pwVar52 = __c;
    }
    else {
      __src = (void *)puVar53[5];
                    /* try { // try from 00aeb3e4 to 00beb3fb has its CatchHandler @ 00aebd7c */
      lVar64 = (long)pwVar52 - (long)__src >> 2;
      uVar49 = lVar64 + 1;
      if (uVar49 >> 0x3e != 0) {
                    /* try { // try from 00aeb490 to 00beb4eb has its CatchHandler @ 00aeade8 */
        if (*(long *)(lVar35 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
          FUN_00470800(puVar53 + 5);
        }
        goto LAB_00aeb4b4;
      }
      uVar59 = (long)puVar53[7] - (long)__src;
                    /* try { // try from 00aeb3fc to 00beb457 has its CatchHandler @ 00aeade8 */
      uVar60 = (long)uVar59 >> 1;
      if (uVar60 <= uVar49) {
        uVar60 = uVar49;
      }
      if (0x7ffffffffffffffb < uVar59) {
        uVar60 = 0x3fffffffffffffff;
      }
      if (uVar60 == 0) {
        __dest = (void *)0x0;
      }
      else {
        if (uVar60 >> 0x3e != 0) {
          if (*(long *)(lVar35 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
            FUN_00440e80();
          }
          goto LAB_00aeb4b4;
        }
        __dest = (void *)_Znwm(uVar60 << 2);
      }
      pwVar61 = (wchar_t *)((long)__dest + lVar64 * 4);
      pwVar51 = pwVar61 + 1;
      *pwVar61 = __c;
      memcpy(__dest,__src,(long)pwVar52 - (long)__src);
      puVar53[5] = __dest;
      puVar53[6] = pwVar51;
                    /* try { // try from 00aeb458 to 00beb467 has its CatchHandler @ 00aebdf4 */
      puVar53[7] = (void *)((long)__dest + uVar60 * 4);
      if (__src != (void *)0x0) {
        _ZdlPv(__src);
      }
    }
                    /* try { // try from 00aeb468 to 00beb477 has its CatchHandler @ 00aebdac */
    puVar53[6] = pwVar51;
  }
LAB_00aeabc8:
                    /* try { // try from 00aeabd0 to 00beacfb has its CatchHandler @ 00aea7d8 */
  if (*(long *)(lVar35 + 0x28) == local_70) {
    return;
  }
LAB_00aeb4b4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
