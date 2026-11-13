# 00aec9fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aec9fc",
  "name": "FUN_00aec9fc",
  "size": 2372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c0b06b66a9667d9b078056e642a89f246d9f0c1c59d6249aa660069dc3102c2",
  "source_text_sha256": "0c0b06b66a9667d9b078056e642a89f246d9f0c1c59d6249aa660069dc3102c2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [0047e64c](../0047e/0047e64c.md)
- [0048ce94](../0048c/0048ce94.md)
- [005c1390](../005c1/005c1390.md)
- [00665da4](../00665/00665da4.md)
- [00851550](../00851/00851550.md)
- [008b6f98](../008b6/008b6f98.md)
- [008b7a20](../008b7/008b7a20.md)
- [008b91d0](../008b9/008b91d0.md)
- [009df688](../009df/009df688.md)
- [009e1014](../009e1/009e1014.md)
- [009e2fe8](../009e2/009e2fe8.md)
- [00acebcc](../00ace/00acebcc.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)
- [00acf868](../00acf/00acf868.md)
- [00acfd30](../00acf/00acfd30.md)
- [00ad6af8](../00ad6/00ad6af8.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58520](../00c58/00c58520.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"uni.imgcut"
~~~

## 疑似コード / UTF-8 16844 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00aec9fc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  byte *pbVar1;
  wchar_t *pwVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  char cVar10;
  short sVar11;
  byte bVar12;
  wchar_t __c;
  long lVar13;
  long *plVar14;
  undefined4 uVar15;
  int iVar16;
  undefined8 uVar17;
  long lVar18;
  long lVar19;
  long lVar20;
  ulong uVar21;
  wchar_t *pwVar22;
  long lVar23;
  int *piVar24;
  char *pcVar25;
  undefined4 *puVar26;
  undefined8 uVar27;
  long *plVar28;
  long lVar29;
  long *plVar30;
  long local_138;
  byte local_f8 [11];
  undefined1 local_ed;
  void *local_e8;
  byte local_e0 [16];
  void *local_d0;
  byte local_c8 [8];
  undefined1 local_c0;
  void *local_b8;
  long local_b0;
  long *plStack_a8;
  undefined8 local_a0;
  long *plStack_98;
  void *local_90;
  long local_70;
  
  lVar13 = tpidr_el0;
  local_70 = *(long *)(lVar13 + 0x28);
                    /* try { // try from 00aeca2c to 00beca3f has its CatchHandler @ 00aece30 */
  if ((*param_3 == 2) && (iVar16 = *param_4, iVar16 != -1)) {
    lVar29 = *(long *)(param_1 + 8);
    uVar27 = *param_2;
    uVar17 = FUN_0047ad34();
    FUN_0047ce14(uVar17,0xb,0);
                    /* try { // try from 00aeca58 to 00beca63 has its CatchHandler @ 00aece24 */
    FUN_008b91d0(uVar27);
    if (iVar16 == 0) {
                    /* try { // try from 00aeca64 to 00beca6f has its CatchHandler @ 00aece0c */
                    /* try { // try from 00aeca78 to 00beca7f has its CatchHandler @ 00aecde0 */
      if (DAT_00ca4a78 == 0) {
        local_138 = 0;
      }
      else {
                    /* try { // try from 00aeca80 to 00beca8b has its CatchHandler @ 00aecdd0 */
        local_138 = __dynamic_cast(DAT_00ca4a78,
                                   &PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                                   &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
      }
                    /* try { // try from 00aecaa0 to 00becaa7 has its CatchHandler @ 00aece1c */
      lVar18 = FUN_00851550();
      if ((*(byte *)(lVar18 + 0x33a5) & 1) == 0) {
        lVar18 = 0;
        do {
          lVar23 = FUN_00851550();
          lVar19 = FUN_00851550();
          lVar23 = lVar23 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) * 0x2c;
          lVar19 = FUN_00851550();
          pbVar1 = (byte *)(lVar23 + 0xc5b8 + lVar18);
          uVar15 = *(undefined4 *)((long)&fde_table_entry_00333b98.data_loc + lVar19 + lVar18);
          *pbVar1 = *(byte *)(lVar23 + 0xc5e0) ^ (byte)uVar15;
          pbVar1[1] = *(byte *)(lVar23 + 0xc5e1) ^ (byte)((uint)uVar15 >> 8);
                    /* try { // try from 00aecdb4 to 00becdb7 has its CatchHandler @ 00aece2c */
          pbVar1[2] = *(byte *)(lVar23 + 0xc5e2) ^ (byte)((uint)uVar15 >> 0x10);
                    /* try { // try from 00aecdc8 to 00becdcb has its CatchHandler @ 00aecdf0 */
          pbVar1[3] = *(byte *)(lVar23 + 0xc5e3) ^ (byte)((uint)uVar15 >> 0x18);
                    /* catch() { ... } // from try @ 00aecc34 with catch @ 00aecdcc
                       try { // try from 00aecdcc to 00bece87 has its CatchHandler @ 00aec9b0 */
                    /* catch() { ... } // from try @ 00aeca80 with catch @ 00aecdd0 */
          pwVar22 = *(wchar_t **)((long)&fde_table_entry_00333bc8.initial_loc + lVar29);
          pwVar2 = *(wchar_t **)((long)&fde_table_entry_00333bd0.initial_loc + lVar29);
          uVar15 = *(undefined4 *)(BYTE_ARRAY_0039b979 + lVar29 + 3);
          __c = *(int *)(lVar29 + 0x333b9c + lVar18) + L'\xfffffffe';
                    /* catch() { ... } // from try @ 00aeca78 with catch @ 00aecde0 */
          pwVar22 = wmemchr(pwVar22,__c,(long)pwVar2 - (long)pwVar22 >> 2);
                    /* catch() { ... } // from try @ 00aecc80 with catch @ 00aecdf0
                       catch() { ... } // from try @ 00aecdc8 with catch @ 00aecdf0 */
          if (pwVar22 != (wchar_t *)0x0) {
            pwVar2 = pwVar22;
          }
                    /* catch() { ... } // from try @ 00aecb54 with catch @ 00aece08 */
                    /* catch() { ... } // from try @ 00aeca64 with catch @ 00aece0c */
                    /* catch() { ... } // from try @ 00aecaa0 with catch @ 00aece1c */
          FUN_005c1390(lVar29 + 0x4a0,uVar15,__c,
                       pwVar2 != *(wchar_t **)((long)&fde_table_entry_00333bd0.initial_loc + lVar29)
                      );
          lVar18 = lVar18 + 4;
                    /* catch() { ... } // from try @ 00aeca58 with catch @ 00aece24 */
        } while (lVar18 != 0x28);
                    /* catch() { ... } // from try @ 00aecaec with catch @ 00aece2c
                       catch() { ... } // from try @ 00aecdb4 with catch @ 00aece2c */
                    /* catch() { ... } // from try @ 00aeca2c with catch @ 00aece30 */
        lVar18 = lVar29 + 0x4347f8;
        lVar23 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aec9f8 with catch @ 00aece48 */
        *(undefined1 *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3) =
             *(undefined1 *)((long)&fde_table_entry_00333bc0.data_loc + lVar23);
                    /* catch() { ... } // from try @ 00aecbfc with catch @ 00aece50 */
        lVar23 = FUN_00851550();
                    /* catch() { ... } // from try @ 00aecb84 with catch @ 00aece54 */
                    /* catch() { ... } // from try @ 00aecb90 with catch @ 00aece58 */
        *(undefined1 *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3 + 1) =
             *(undefined1 *)((long)&fde_table_entry_00333bc0.data_loc + lVar23 + 1);
        lVar23 = FUN_00851550();
        *(undefined1 *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3 + 2) =
             *(undefined1 *)((long)&fde_table_entry_00333bc0.data_loc + lVar23 + 2);
      }
      else {
        FUN_00851550();
        uVar15 = FUN_00acebcc();
        FUN_00acee90(&local_a0,lVar29,uVar15);
        uVar15 = FUN_00acf228(lVar29,uVar15);
        FUN_00851550();
                    /* try { // try from 00aecaec to 00becaf7 has its CatchHandler @ 00aece2c */
        FUN_00851550();
                    /* try { // try from 00aecaf8 to 00becb53 has its CatchHandler @ 00aec9b0 */
        lVar18 = 0;
        lVar23 = lVar29 + 0xc5b8;
        do {
          lVar19 = FUN_00851550();
          lVar20 = FUN_00851550();
          sVar11 = *(short *)((long)&local_a0 + lVar18);
          lVar19 = lVar19 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar20 + 3) * 0x2c;
          pbVar1 = (byte *)(lVar19 + lVar18 + 0xc5b9);
          pbVar1[-1] = *(byte *)(lVar19 + 0xc5e0) ^ (byte)sVar11;
          *pbVar1 = *(byte *)(lVar19 + 0xc5e1) ^ (byte)((ushort)sVar11 >> 8);
          pbVar1[1] = *(byte *)(lVar19 + 0xc5e2) ^ (byte)((uint)(int)sVar11 >> 0xf);
          pbVar1[2] = *(byte *)(lVar19 + 0xc5e3) ^ (byte)(sVar11 >> 0xf);
          lVar19 = FUN_00851550();
                    /* try { // try from 00aecbfc to 00becc07 has its CatchHandler @ 00aece50 */
          lVar20 = FUN_00851550();
          lVar19 = lVar19 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar20 + 3) * 0x2c;
          pbVar1 = (byte *)(lVar19 + lVar18 + 0xc5b9);
                    /* try { // try from 00aecc34 to 00becc3b has its CatchHandler @ 00aecdcc */
          if (((uint)(*(byte *)(lVar19 + 0xc5e2) ^ pbVar1[1]) << 0x10 |
               (uint)(*(byte *)(lVar19 + 0xc5e3) ^ pbVar1[2]) << 0x18 |
               (uint)(*(byte *)(lVar19 + 0xc5e1) ^ *pbVar1) << 8 |
              (uint)(*(byte *)(lVar19 + 0xc5e0) ^ pbVar1[-1])) != 0xffffffff) {
            lVar19 = FUN_00851550();
            cVar10 = *(char *)((long)&local_a0 + lVar18 + 2);
                    /* try { // try from 00aecc80 to 00becc8b has its CatchHandler @ 00aecdf0 */
            lVar20 = lVar23 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) * 0x2c;
            pbVar1 = (byte *)(lVar23 + lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) *
                                                0x2c);
                    /* try { // try from 00aecc8c to 00becdb3 has its CatchHandler @ 00aec9b0 */
            iVar16 = CONCAT13(*(byte *)(lVar20 + 0x2b) ^ pbVar1[3],
                              CONCAT12(*(byte *)(lVar20 + 0x2a) ^ pbVar1[2],
                                       CONCAT11(*(byte *)(lVar20 + 0x29) ^ pbVar1[1],
                                                *(byte *)(lVar20 + 0x28) ^ *pbVar1))) + -2;
            uVar21 = FUN_009e1014(lVar29 + 0x50,0xffffffff,0xffffffff);
            if ((uVar21 & 1) == 0) {
              piVar24 = (int *)(lVar29 + 0x49934 + (long)iVar16 * 4);
            }
            else {
              lVar19 = FUN_009e2fe8(lVar29 + 0x50,0xffffffff,0xffffffff);
              if ((lVar19 == 0) || (lVar19 = FUN_009df688(lVar19,iVar16), lVar19 == 0))
              goto LAB_00aecb28;
              piVar24 = (int *)(lVar19 + 4);
            }
            *piVar24 = (int)cVar10;
          }
LAB_00aecb28:
          iVar16 = *(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3);
          lVar19 = lVar23 + (long)iVar16 * 0x2c;
          pbVar1 = (byte *)(lVar23 + lVar18 + (long)iVar16 * 0x2c);
                    /* try { // try from 00aecb54 to 00becb5b has its CatchHandler @ 00aece08 */
                    /* try { // try from 00aecb84 to 00becb8b has its CatchHandler @ 00aece54 */
          FUN_005c1390(lVar29 + 0x4a0,(long)iVar16,
                       CONCAT13(*(byte *)(lVar19 + 0x2b) ^ pbVar1[3],
                                CONCAT12(*(byte *)(lVar19 + 0x2a) ^ pbVar1[2],
                                         CONCAT11(*(byte *)(lVar19 + 0x29) ^ pbVar1[1],
                                                  *(byte *)(lVar19 + 0x28) ^ *pbVar1))) + -2,0);
                    /* try { // try from 00aecb90 to 00becbab has its CatchHandler @ 00aece58 */
          FUN_00851550();
          FUN_00851550();
          lVar18 = lVar18 + 4;
        } while (lVar18 != 0x28);
        lVar18 = lVar29 + 0x4347f8;
        *(char *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3) = (char)uVar15;
        *(char *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3 + 1) =
             (char)((uint)uVar15 >> 8);
        *(char *)(lVar18 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar29 + 3) * 3 + 2) =
             (char)((uint)uVar15 >> 0x10);
        FUN_00acfd30(lVar29,1);
      }
      pcVar25 = (char *)((ulong)local_f8 | 1);
      lVar18 = 0;
      plVar28 = (long *)(local_138 + 0x348);
      do {
        lVar23 = FUN_00851550();
        lVar19 = FUN_00851550();
        lVar23 = lVar23 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) * 0x2c;
        pbVar1 = (byte *)(lVar23 + lVar18 + 0xc5b9);
        if (((uint)(*(byte *)(lVar23 + 0xc5e2) ^ pbVar1[1]) << 0x10 |
             (uint)(*(byte *)(lVar23 + 0xc5e3) ^ pbVar1[2]) << 0x18 |
             (uint)(*(byte *)(lVar23 + 0xc5e1) ^ *pbVar1) << 8 |
            (uint)(*(byte *)(lVar23 + 0xc5e0) ^ pbVar1[-1])) == 0xffffffff) {
          if (((DAT_00ca5038 & 1) == 0) &&
             (iVar16 = __cxa_guard_acquire(&DAT_00ca5038), iVar16 != 0)) {
            DAT_00ca5008 = 0;
            DAT_00ca5000 = &DAT_00ca5008;
                    /* try { // try from 00aed2ac to 00bed2cf has its CatchHandler @ 00aed5b0 */
            DAT_00ca5028 = 0;
            DAT_00ca5030 = 0;
            DAT_00ca5020 = 0;
            DAT_00ca5010 = 0;
            DAT_00ca5018 = &DAT_00ca5020;
            __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
            __cxa_guard_release(&DAT_00ca5038);
          }
          local_c0 = 0;
          local_c8[0] = 0xe;
          *(undefined4 *)((ulong)local_c8 | 1) = 0x2e696e75;
          *(undefined4 *)((long)((ulong)local_c8 | 1) + 3) = 0x676e702e;
          FUN_0048ce94(&local_a0,local_c8);
          uVar17 = s_uni_imgcut_002cab54._0_8_;
          local_f8[0] = 0x14;
                    /* catch() { ... } // from try @ 00aed3f4 with catch @ 00aed16c
                       catch() { ... } // from try @ 00aed5a4 with catch @ 00aed16c */
          pcVar25[8] = 'u';
          pcVar25[9] = 't';
          local_ed = 0;
          *(undefined8 *)pcVar25 = uVar17;
          FUN_0048ce94(local_e0,local_f8);
          FUN_0047e64c(&local_b0,&DAT_00ca5000,&local_a0,local_e0,0x2601);
          plVar14 = plStack_a8;
          lVar23 = local_b0;
          local_b0 = 0;
          plStack_a8 = (long *)0x0;
          plVar30 = (long *)*plVar28;
          *plVar28 = (long)plVar14;
          plVar28[-1] = lVar23;
          plVar14 = plStack_a8;
          if ((plVar30 != (long *)0x0) &&
             (lVar23 = FUN_00c53da0(0xffffffffffffffff,plVar30 + 1), plVar14 = plStack_a8,
             lVar23 == 0)) {
            (**(code **)(*plVar30 + 0x10))(plVar30);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar30);
            plVar14 = plStack_a8;
                    /* try { // try from 00aed210 to 00bed25f has its CatchHandler @ 00aed5cc */
          }
          plStack_a8 = plVar14;
                    /* try { // try from 00aed1cc to 00bed1d3 has its CatchHandler @ 00aed5c0 */
          if ((plVar14 != (long *)0x0) &&
             (lVar23 = FUN_00c53da0(0xffffffffffffffff,plVar14 + 1), lVar23 == 0)) {
            (**(code **)(*plVar14 + 0x10))(plVar14);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
          }
          if ((local_e0[0] & 1) != 0) {
            _ZdlPv(local_d0);
          }
          if ((local_f8[0] & 1) != 0) {
            _ZdlPv(local_e8);
          }
          if ((local_a0 & 1) != 0) {
            _ZdlPv(local_90);
          }
          if ((local_c8[0] & 1) != 0) {
            _ZdlPv(local_b8);
          }
        }
        else {
          lVar23 = FUN_00851550();
          lVar19 = FUN_00851550();
          lVar23 = lVar23 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) * 0x2c;
          pbVar1 = (byte *)(lVar23 + lVar18 + 0xc5b9);
          bVar12 = pbVar1[-1];
          bVar3 = *pbVar1;
          bVar4 = pbVar1[1];
          bVar5 = pbVar1[2];
          bVar6 = *(byte *)(lVar23 + 0xc5e2);
          bVar7 = *(byte *)(lVar23 + 0xc5e0);
          bVar8 = *(byte *)(lVar23 + 0xc5e1);
          bVar9 = *(byte *)(lVar23 + 0xc5e3);
          lVar23 = FUN_00851550();
          lVar19 = FUN_00851550();
          lVar23 = lVar23 + (long)*(int *)(BYTE_ARRAY_0039b979 + lVar19 + 3) * 0x2c;
          pbVar1 = (byte *)(lVar23 + lVar18 + 0xc5b9);
          iVar16 = CONCAT13(*(byte *)(lVar23 + 0xc5e3) ^ pbVar1[2],
                            CONCAT12(*(byte *)(lVar23 + 0xc5e2) ^ pbVar1[1],
                                     CONCAT11(*(byte *)(lVar23 + 0xc5e1) ^ *pbVar1,
                                              *(byte *)(lVar23 + 0xc5e0) ^ pbVar1[-1]))) + -2;
          uVar21 = FUN_009e1014(lVar29 + 0x50,0xffffffff,0xffffffff);
          if ((((uVar21 & 1) == 0) ||
              (lVar23 = FUN_009e2fe8(lVar29 + 0x50,0xffffffff,0xffffffff), lVar23 == 0)) ||
             (lVar23 = FUN_009df688(lVar23,iVar16), lVar23 == 0)) {
            puVar26 = (undefined4 *)(lVar29 + 0x49934 + (long)iVar16 * 4);
          }
          else {
            puVar26 = (undefined4 *)(lVar23 + 4);
          }
          FUN_00665da4(&local_a0,
                       CONCAT13(bVar9 ^ bVar5,
                                CONCAT12(bVar6 ^ bVar4,CONCAT11(bVar8 ^ bVar3,bVar7 ^ bVar12))) + -2
                       ,*puVar26,0);
          plVar14 = plStack_98;
          uVar21 = local_a0;
          local_a0 = 0;
          plStack_98 = (long *)0x0;
          plVar30 = (long *)*plVar28;
          *plVar28 = (long)plVar14;
          plVar28[-1] = uVar21;
          if ((plVar30 != (long *)0x0) &&
             (lVar23 = FUN_00c53da0(0xffffffffffffffff,plVar30 + 1), lVar23 == 0)) {
            (**(code **)(*plVar30 + 0x10))(plVar30);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar30);
          }
          plVar14 = plStack_98;
          if ((plStack_98 != (long *)0x0) &&
             (lVar23 = FUN_00c53da0(0xffffffffffffffff,plStack_98 + 1), lVar23 == 0)) {
            (**(code **)(*plVar14 + 0x10))(plVar14);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
          }
        }
        lVar18 = lVar18 + 4;
        plVar28 = plVar28 + 2;
      } while (lVar18 != 0x28);
      FUN_00acf868(local_138);
      uVar17 = FUN_008b7a20(lVar29 + 0x2f38,0x324);
      iVar16 = FUN_00ad6af8(lVar29);
      FUN_008b6f98(uVar17,iVar16 == 3);
    }
  }
                    /* try { // try from 00aed310 to 00bed317 has its CatchHandler @ 00aed5a8 */
  if (*(long *)(lVar13 + 0x28) == local_70) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
