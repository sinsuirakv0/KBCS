# 008bdabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008bdabc",
  "name": "FUN_008bdabc",
  "size": 6112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d02706c765ae282051ac4c06e20ae83246727e6729ad4cfab68ddc92409c2e15",
  "source_text_sha256": "d02706c765ae282051ac4c06e20ae83246727e6729ad4cfab68ddc92409c2e15"
}
~~~

## 呼び出し元

- [008bc884](../008bc/008bc884.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00440e80](../00440/00440e80.md)
- [004428f0](../00442/004428f0.md)
- [00447eb4](../00447/00447eb4.md)
- [0046c984](../0046c/0046c984.md)
- [00470800](../00470/00470800.md)
- [0047e5cc](../0047e/0047e5cc.md)
- [004878ec](../00487/004878ec.md)
- [004878fc](../00487/004878fc.md)
- [00487de0](../00487/00487de0.md)
- [00488518](../00488/00488518.md)
- [005c175c](../005c1/005c175c.md)
- [005d8b88](../005d8/005d8b88.md)
- [00676a20](../00676/00676a20.md)
- [006b8c04](../006b8/006b8c04.md)
- [008514b8](../00851/008514b8.md)
- [008b6ecc](../008b6/008b6ecc.md)
- [008b6ed4](../008b6/008b6ed4.md)
- [008b6eec](../008b6/008b6eec.md)
- [008b6fa8](../008b6/008b6fa8.md)
- [008cb78c](../008cb/008cb78c.md)
- [008cb790](../008cb/008cb790.md)
- [008cba54](../008cb/008cba54.md)
- [008cbab4](../008cb/008cbab4.md)
- [008cbab8](../008cb/008cbab8.md)
- [008cbde0](../008cb/008cbde0.md)
- [008cbde4](../008cb/008cbde4.md)
- [008cc258](../008cc/008cc258.md)
- [008cc25c](../008cc/008cc25c.md)
- [00a4658c](../00a46/00a4658c.md)
- [00a466d0](../00a46/00a466d0.md)
- [00a46704](../00a46/00a46704.md)
- [00a46bf0](../00a46/00a46bf0.md)
- [00b10cc4](../00b10/00b10cc4.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57ba0](../00c57/00c57ba0.md)
- [00c57bb0](../00c57/00c57bb0.md)
- [00c57bc0](../00c57/00c57bc0.md)
- [00c57c00](../00c57/00c57c00.md)

## 関連文字列（未確認候補）

~~~text
"5.imgcut"
"ComboFiltering.tsv"
"Combo_name_%03d.png"
"img015.imgcut"
"img015.png"
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 40633 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_008bdabc(long param_1)

{
  undefined *puVar1;
  undefined4 *puVar2;
  uint uVar3;
  long lVar4;
  undefined8 uVar5;
  undefined *puVar6;
  undefined4 uVar7;
  bool bVar8;
  int iVar9;
  undefined4 uVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  long lVar14;
  ulong uVar15;
  void *pvVar16;
  uint *puVar17;
  undefined8 *puVar18;
  undefined8 *puVar19;
  undefined8 uVar20;
  undefined ***pppuVar21;
  undefined8 *puVar22;
  undefined8 *puVar23;
  undefined8 *puVar24;
  undefined8 *puVar25;
  ulong uVar26;
  long *plVar27;
  char *pcVar28;
  undefined8 *puVar29;
  undefined4 *puVar30;
  long *plVar31;
  long *plVar32;
  ulong uVar33;
  uint uVar34;
  long *plVar35;
  void *pvVar36;
  long *plVar37;
  long *plVar38;
  undefined4 *puVar39;
  uint *puVar40;
  size_t sVar41;
  int iVar42;
  undefined *puVar43;
  int local_32c;
  long *local_2f8 [2];
  void *local_2e8;
  long *local_2e0;
  long *plStack_2d8;
  undefined4 local_2d0;
  uint uStack_2cc;
  long local_2c0;
  long *plStack_2b8;
  byte local_2b0;
  undefined5 uStack_2af;
  undefined2 uStack_2aa;
  char cStack_2a8;
  char acStack_2a7 [5];
  char cStack_2a2;
  char cStack_2a1;
  char cStack_2a0;
  undefined2 uStack_29f;
  undefined1 uStack_29d;
  undefined4 uStack_29c;
  undefined8 local_298;
  char cStack_290;
  undefined2 uStack_28f;
  undefined1 uStack_28d;
  undefined4 uStack_28c;
  uint *local_288;
  uint *local_280;
  byte local_278;
  void *local_268;
  long local_250;
  undefined *local_248 [8];
  byte local_208;
  void *local_1f8;
  undefined1 auStack_1e0 [160];
  undefined **local_140;
  long lStack_138;
  undefined ***local_120;
  undefined **local_110;
  long lStack_108;
  undefined ***local_f0;
  undefined **local_e0;
  long lStack_d8;
  undefined ***local_c0;
  undefined **local_b0;
  long lStack_a8;
  ulong local_a0;
  undefined ***local_90;
  long local_80;
  
                    /* try { // try from 008bdadc to 009bdaf3 has its CatchHandler @ 008c72b0 */
  lVar4 = tpidr_el0;
  local_80 = *(long *)(lVar4 + 0x28);
  if (((DAT_00ca4b38 & 1) == 0) && (iVar11 = __cxa_guard_acquire(&DAT_00ca4b38), iVar11 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  uStack_28d = 0;
  uStack_28f = 0x676e;
  local_2b0 = 0x1a;
  local_298._0_4_ = CONCAT31((int3)s_img015_png_002b91cf._0_8_,0x14);
  local_298._4_4_ = SUB84(s_img015_png_002b91cf._0_8_,3);
  cStack_290 = SUB81(s_img015_png_002b91cf._0_8_,7);
                    /* try { // try from 008bdb30 to 009bdb47 has its CatchHandler @ 008c7020 */
  cStack_2a2 = '\0';
  uStack_2af = _DAT_002bdbcf;
  uStack_2aa = (undefined2)s_5_imgcut_002bdbd4._0_3_;
  cStack_2a8 = SUB31(s_5_imgcut_002bdbd4._0_3_,2);
  acStack_2a7[0] = s_5_imgcut_002bdbd4[3];
  acStack_2a7[1] = s_5_imgcut_002bdbd4[4];
  acStack_2a7[2] = s_5_imgcut_002bdbd4[5];
  acStack_2a7[3] = s_5_imgcut_002bdbd4[6];
  acStack_2a7[4] = s_5_imgcut_002bdbd4[7];
  FUN_0047e5cc(&local_2e0,&DAT_00ca4b00,&local_298,&local_2b0,0x2601);
  plVar38 = plStack_2d8;
  plVar31 = local_2e0;
  plVar35 = *(long **)(param_1 + 0x60);
  local_2e0 = (long *)0x0;
  plStack_2d8 = (long *)0x0;
  puVar24 = (undefined8 *)(param_1 + 0x58);
  *(long **)(param_1 + 0x60) = plVar38;
  *puVar24 = plVar31;
  plVar31 = plStack_2d8;
                    /* try { // try from 008bdb90 to 009bdb9b has its CatchHandler @ 008c700c */
  if ((plVar35 != (long *)0x0) &&
     (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar35 + 1), plVar31 = plStack_2d8, lVar14 == 0)) {
    (**(code **)(*plVar35 + 0x10))(plVar35);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar35);
    plVar31 = plStack_2d8;
  }
  plStack_2d8 = plVar31;
                    /* try { // try from 008bdb9c to 009be373 has its CatchHandler @ 008bda04 */
  if ((plVar31 != (long *)0x0) &&
     (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar31 + 1), lVar14 == 0)) {
    (**(code **)(*plVar31 + 0x10))(plVar31);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar31);
  }
  if ((local_2b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_29c,CONCAT13(uStack_29d,CONCAT21(uStack_29f,cStack_2a0))));
  }
  if (((uint)local_298 & 1) != 0) {
    _ZdlPv(local_288);
  }
  if (*(long *)(param_1 + 0x20) == 0) {
    FUN_00487de0(&local_298);
    local_298._0_4_ = 0xc64938;
    local_298._4_4_ = 0;
    local_2b0 = 0x24;
    uStack_29f = 0x7673;
    uStack_29d = 0;
    acStack_2a7 = SUB85(s_ComboFiltering_tsv_002b792b._8_8_,0);
    cStack_2a2 = SUB81(s_ComboFiltering_tsv_002b792b._8_8_,5);
    cStack_2a1 = SUB81(s_ComboFiltering_tsv_002b792b._8_8_,6);
    cStack_2a0 = SUB81(s_ComboFiltering_tsv_002b792b._8_8_,7);
    uStack_2af = (undefined5)s_ComboFiltering_tsv_002b792b._0_8_;
    uStack_2aa = SUB82(s_ComboFiltering_tsv_002b792b._0_8_,5);
    cStack_2a8 = SUB81(s_ComboFiltering_tsv_002b792b._0_8_,7);
    uVar15 = FUN_00b10cc4(&local_298,&local_2b0,0,0);
    if ((local_2b0 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_29c,CONCAT13(uStack_29d,CONCAT21(uStack_29f,cStack_2a0))));
    }
    if ((uVar15 & 1) != 0) {
      FUN_004878ec(&local_298);
      while (uVar15 = FUN_004878ec(&local_298), (uVar15 & 1) != 0) {
        for (iVar11 = 1; iVar9 = FUN_00488518(&local_298), iVar11 < iVar9; iVar11 = iVar11 + 1) {
          iVar9 = FUN_004878fc(&local_298,0);
          puVar25 = *(undefined8 **)(param_1 + 0x18);
          puVar22 = (undefined8 *)(param_1 + 0x18);
          while (puVar29 = puVar22, puVar25 != (undefined8 *)0x0) {
            while (puVar22 = puVar25, *(int *)(puVar22 + 4) <= iVar9) {
              if (iVar9 <= *(int *)(puVar22 + 4)) goto LAB_008bdd28;
              puVar25 = (undefined8 *)puVar22[1];
              if ((undefined8 *)puVar22[1] == (undefined8 *)0x0) {
                puVar29 = puVar22 + 1;
                goto LAB_008bdcd0;
              }
            }
            puVar25 = (undefined8 *)*puVar22;
          }
LAB_008bdcd0:
          puVar25 = (undefined8 *)_Znwm(0x40);
          *(int *)(puVar25 + 4) = iVar9;
          puVar25[6] = 0;
          puVar25[7] = 0;
          puVar25[5] = 0;
          *puVar25 = 0;
          puVar25[1] = 0;
          puVar25[2] = puVar22;
          *puVar29 = puVar25;
          puVar22 = puVar25;
          if (**(long **)(param_1 + 0x10) != 0) {
            *(long *)(param_1 + 0x10) = **(long **)(param_1 + 0x10);
            puVar22 = (undefined8 *)*puVar29;
          }
          FUN_0043bb64(*(undefined8 *)(param_1 + 0x18),puVar22);
          *(long *)(param_1 + 0x20) = *(long *)(param_1 + 0x20) + 1;
          puVar22 = puVar25;
LAB_008bdd28:
          uVar10 = FUN_004878fc(&local_298,iVar11);
          puVar30 = (undefined4 *)puVar22[6];
          if (puVar30 < (undefined4 *)puVar22[7]) {
            puVar39 = puVar30 + 1;
            *puVar30 = uVar10;
          }
          else {
            pvVar36 = (void *)puVar22[5];
            lVar14 = (long)puVar30 - (long)pvVar36 >> 2;
            uVar15 = lVar14 + 1;
            if (uVar15 >> 0x3e != 0) {
              if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
                FUN_00470800(puVar22 + 5);
              }
              goto LAB_008bf510;
            }
            uVar26 = (long)puVar22[7] - (long)pvVar36;
            uVar33 = (long)uVar26 >> 1;
            if (uVar33 <= uVar15) {
              uVar33 = uVar15;
            }
            if (0x7ffffffffffffffb < uVar26) {
              uVar33 = 0x3fffffffffffffff;
            }
            if (uVar33 == 0) {
              pvVar16 = (void *)0x0;
            }
            else {
              if (uVar33 >> 0x3e != 0) {
                if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
                  FUN_00440e80();
                }
                goto LAB_008bf510;
              }
              pvVar16 = (void *)_Znwm(uVar33 << 2);
            }
            puVar2 = (undefined4 *)((long)pvVar16 + lVar14 * 4);
            puVar39 = puVar2 + 1;
            *puVar2 = uVar10;
            memcpy(pvVar16,pvVar36,(long)puVar30 - (long)pvVar36);
            puVar22[5] = pvVar16;
            puVar22[6] = puVar39;
            puVar22[7] = (void *)((long)pvVar16 + uVar33 * 4);
            if (pvVar36 != (void *)0x0) {
              _ZdlPv(pvVar36);
            }
          }
          puVar22[6] = puVar39;
        }
      }
    }
    puVar6 = 
    PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9a7b8;
    local_250 = *(long *)
                 PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9a7b8
    ;
    local_298 = (long *)(PTR_DAT_00c9a7b0 + 0x10);
    *(undefined8 *)((long)&local_250 + *(long *)(local_250 + -0x18)) =
         *(undefined8 *)
          (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9a7b8
          + 0x18);
    local_248[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9a7c0
                   + 0x10;
    if ((local_208 & 1) != 0) {
      _ZdlPv(local_1f8);
    }
    _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_248);
    _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_250,puVar6 + 8);
    _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_1e0);
    if ((local_278 & 1) != 0) {
      _ZdlPv(local_268);
    }
    puVar17 = (uint *)CONCAT44(uStack_28c,CONCAT13(uStack_28d,CONCAT21(uStack_28f,cStack_290)));
    if (puVar17 != (uint *)0x0) {
      local_288 = puVar17;
      _ZdlPv(puVar17);
    }
  }
  puVar22 = (undefined8 *)(param_1 + 0x30);
  plVar35 = (long *)(param_1 + 0x28);
  FUN_00676a20(plVar35,*puVar22);
  plVar38 = *(long **)(param_1 + 0x10);
  plVar27 = (long *)(param_1 + 0x18);
  *puVar22 = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  *(undefined8 **)(param_1 + 0x28) = puVar22;
  plVar31 = local_298;
  while (plVar38 != plVar27) {
    pvVar36 = (void *)plVar38[5];
    pvVar16 = (void *)plVar38[6];
    local_298._0_4_ = (uint)plVar38[4];
    local_288 = (uint *)0x0;
    local_280 = (uint *)0x0;
    sVar41 = (long)pvVar16 - (long)pvVar36;
    cStack_290 = '\0';
    uStack_28f = 0;
    uStack_28d = 0;
    uStack_28c = 0;
    if (sVar41 != 0) {
      if ((long)sVar41 < 0) {
        if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
          FUN_00470800(&cStack_290);
        }
        goto LAB_008bf510;
      }
      puVar17 = (uint *)_Znwm(sVar41);
      puVar40 = (uint *)((long)puVar17 + sVar41);
      cStack_290 = (char)puVar17;
      uStack_28f = (undefined2)((ulong)puVar17 >> 8);
      uStack_28d = (undefined1)((ulong)puVar17 >> 0x18);
      uStack_28c = (undefined4)((ulong)puVar17 >> 0x20);
      local_280 = puVar40;
      memcpy(puVar17,pvVar36,sVar41);
      local_288 = puVar40;
      if (pvVar16 != pvVar36) {
        do {
          uVar3 = *puVar17;
          puVar25 = (undefined8 *)*puVar22;
          puVar29 = puVar22;
          while (puVar23 = puVar29, puVar18 = puVar29, puVar25 != (undefined8 *)0x0) {
            while (puVar29 = puVar25, *(int *)((long)puVar29 + 0x1c) <= (int)uVar3) {
              if ((int)uVar3 <= *(int *)((long)puVar29 + 0x1c)) goto LAB_008bdf18;
              puVar25 = (undefined8 *)puVar29[1];
              if ((undefined8 *)puVar29[1] == (undefined8 *)0x0) {
                puVar18 = puVar29 + 1;
                puVar23 = puVar29;
                goto LAB_008bdf68;
              }
            }
            puVar25 = (undefined8 *)*puVar29;
          }
LAB_008bdf68:
          puVar29 = (undefined8 *)_Znwm(0x28);
          *(uint *)((long)puVar29 + 0x1c) = uVar3;
          *(undefined1 *)(puVar29 + 4) = 0;
          *puVar29 = 0;
          puVar29[1] = 0;
          puVar29[2] = puVar23;
          *puVar18 = puVar29;
          puVar25 = puVar29;
          if (*(long *)*plVar35 != 0) {
            *plVar35 = *(long *)*plVar35;
            puVar25 = (undefined8 *)*puVar18;
          }
          FUN_0043bb64(*(undefined8 *)(param_1 + 0x30),puVar25);
          *(long *)(param_1 + 0x38) = *(long *)(param_1 + 0x38) + 1;
LAB_008bdf18:
          puVar17 = puVar17 + 1;
          *(undefined1 *)(puVar29 + 4) = 0;
        } while (puVar17 != puVar40);
        puVar40 = (uint *)CONCAT44(uStack_28c,CONCAT13(uStack_28d,CONCAT21(uStack_28f,cStack_290)));
        if (puVar40 == (uint *)0x0) goto LAB_008bdfc0;
      }
      _ZdlPv(puVar40);
    }
LAB_008bdfc0:
    plVar31 = (long *)CONCAT44(local_298._4_4_,(uint)local_298);
    plVar32 = (long *)plVar38[1];
    plVar37 = plVar38;
    if ((long *)plVar38[1] == (long *)0x0) {
      do {
        plVar38 = (long *)plVar37[2];
        bVar8 = (long *)*plVar38 != plVar37;
        plVar37 = plVar38;
      } while (bVar8);
    }
    else {
      do {
        plVar38 = plVar32;
        plVar32 = (long *)*plVar38;
      } while ((long *)*plVar38 != (long *)0x0);
    }
  }
  local_298 = plVar31;
  FUN_008514b8();
  iVar11 = FUN_0046c984();
  puVar25 = (undefined8 *)(param_1 + 0x48);
  plVar38 = (long *)(param_1 + 0x40);
  FUN_005c175c(plVar38,*puVar25);
  *(undefined8 *)(param_1 + 0x50) = 0;
  puVar43 = PTR_DAT_00c9af70;
  puVar6 = PTR_DAT_00c9af68;
  plVar31 = *(long **)(param_1 + 0x10);
  *(undefined8 **)(param_1 + 0x40) = puVar25;
  *(undefined8 *)(param_1 + 0x48) = 0;
  if (plVar31 == plVar27) {
    local_32c = 0x69;
  }
  else {
    pcVar28 = (char *)((ulong)&local_2e0 | 1);
    iVar9 = 0;
    puVar1 = puVar43 + 0x10;
    local_32c = 0x69;
    do {
      pvVar36 = (void *)plVar31[5];
      pvVar16 = (void *)plVar31[6];
      local_298._0_4_ = (uint)plVar31[4];
      local_288 = (uint *)0x0;
      local_280 = (uint *)0x0;
      sVar41 = (long)pvVar16 - (long)pvVar36;
      cStack_290 = '\0';
      uStack_28f = 0;
      uStack_28d = 0;
      uStack_28c = 0;
      if (sVar41 != 0) {
        if ((long)sVar41 < 0) {
          if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
            FUN_00470800(&cStack_290);
          }
          goto LAB_008bf510;
        }
        puVar17 = (uint *)_Znwm(sVar41);
        puVar40 = (uint *)((long)puVar17 + sVar41);
        cStack_290 = (char)puVar17;
        uStack_28f = (undefined2)((ulong)puVar17 >> 8);
        uStack_28d = (undefined1)((ulong)puVar17 >> 0x18);
        uStack_28c = (undefined4)((ulong)puVar17 >> 0x20);
        local_280 = puVar40;
        memcpy(puVar17,pvVar36,sVar41);
        local_288 = puVar40;
        if (pvVar16 != pvVar36) {
          uVar3 = 0;
LAB_008be148:
          uVar34 = uVar3;
          uVar3 = *puVar17;
          puVar29 = (undefined8 *)*puVar25;
          puVar18 = puVar25;
          while (puVar19 = puVar18, puVar23 = puVar18, puVar29 != (undefined8 *)0x0) {
            while (puVar18 = puVar29, *(int *)((long)puVar18 + 0x1c) <= (int)uVar3) {
              if ((int)uVar3 <= *(int *)((long)puVar18 + 0x1c)) goto LAB_008be1d8;
              puVar29 = (undefined8 *)puVar18[1];
              if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
                puVar23 = puVar18 + 1;
                puVar19 = puVar18;
                goto LAB_008be188;
              }
            }
            puVar29 = (undefined8 *)*puVar18;
          }
LAB_008be188:
          puVar18 = (undefined8 *)_Znwm(0x28);
          *(uint *)((long)puVar18 + 0x1c) = uVar3;
          *(undefined4 *)(puVar18 + 4) = 0;
          *puVar18 = 0;
          puVar18[1] = 0;
          puVar18[2] = puVar19;
          *puVar23 = puVar18;
          puVar29 = puVar18;
          if (*(long *)*plVar38 != 0) {
            *plVar38 = *(long *)*plVar38;
            puVar29 = (undefined8 *)*puVar23;
          }
          FUN_0043bb64(*(undefined8 *)(param_1 + 0x48),puVar29);
          *(long *)(param_1 + 0x50) = *(long *)(param_1 + 0x50) + 1;
LAB_008be1d8:
          *(int *)(puVar18 + 4) = iVar9 + 0x2bf;
          if (((DAT_00ca4b38 & 1) == 0) &&
             (iVar12 = __cxa_guard_acquire(&DAT_00ca4b38), iVar12 != 0)) {
            DAT_00ca4b08 = 0;
            DAT_00ca4b00 = &DAT_00ca4b08;
                    /* try { // try from 008be7a8 to 009be7ab has its CatchHandler @ 008c7578 */
                    /* try { // try from 008be7ac to 009be83b has its CatchHandler @ 008bda04 */
            DAT_00ca4b28 = 0;
            DAT_00ca4b30 = 0;
            DAT_00ca4b20 = 0;
            DAT_00ca4b10 = 0;
            DAT_00ca4b18 = &DAT_00ca4b20;
            __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
            __cxa_guard_release(&DAT_00ca4b38);
          }
          uVar5 = s_Combo_name__03d_png_002bdfe5._8_8_;
          uVar20 = s_Combo_name__03d_png_002bdfe5._0_8_;
          uStack_2cc = uStack_2cc & 0xffffff00;
          local_2e0 = (long *)CONCAT71(local_2e0._1_7_,0x26);
          pcVar28[0xf] = '.';
          pcVar28[0x10] = 'p';
          pcVar28[0x11] = 'n';
          pcVar28[0x12] = 'g';
          *(undefined8 *)(pcVar28 + 8) = uVar5;
          *(undefined8 *)pcVar28 = uVar20;
          FUN_00447eb4(&local_2b0,&local_2e0,0,(ulong)uVar3);
          local_2f8[0] = (long *)((ulong)local_2f8[0] & 0xffffffffffff0000);
          FUN_0047e5cc(&local_2c0,&DAT_00ca4b00,&local_2b0,local_2f8,0x2601);
          puVar29 = (undefined8 *)(param_1 + 0x70);
          while (puVar23 = (undefined8 *)*puVar29, puVar19 = puVar29, puVar18 = puVar29,
                (undefined8 *)*puVar29 != (undefined8 *)0x0) {
            while (puVar29 = puVar23, *(int *)(puVar29 + 4) <= (int)uVar3) {
              if ((int)uVar3 <= *(int *)(puVar29 + 4)) goto LAB_008be2d8;
              puVar23 = (undefined8 *)puVar29[1];
              if ((undefined8 *)puVar29[1] == (undefined8 *)0x0) {
                puVar18 = puVar29 + 1;
                puVar19 = puVar29;
                goto LAB_008be284;
              }
            }
          }
LAB_008be284:
          puVar29 = (undefined8 *)_Znwm(0x38);
          *(uint *)(puVar29 + 4) = uVar3;
          puVar29[5] = 0;
          puVar29[6] = 0;
          *puVar29 = 0;
          puVar29[1] = 0;
          puVar29[2] = puVar19;
          *puVar18 = puVar29;
          puVar23 = puVar29;
          if (**(long **)(param_1 + 0x68) != 0) {
            *(long *)(param_1 + 0x68) = **(long **)(param_1 + 0x68);
            puVar23 = (undefined8 *)*puVar18;
          }
          FUN_0043bb64(*(undefined8 *)(param_1 + 0x70),puVar23);
          *(long *)(param_1 + 0x78) = *(long *)(param_1 + 0x78) + 1;
LAB_008be2d8:
          plVar32 = plStack_2b8;
          lVar14 = local_2c0;
          plVar37 = (long *)puVar29[6];
          local_2c0 = 0;
          plStack_2b8 = (long *)0x0;
          puVar29[6] = plVar32;
          puVar29[5] = lVar14;
          plVar32 = plStack_2b8;
          if ((plVar37 != (long *)0x0) &&
             (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar37 + 1), plVar32 = plStack_2b8,
             lVar14 == 0)) {
            (**(code **)(*plVar37 + 0x10))(plVar37);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar37);
            plVar32 = plStack_2b8;
          }
          plStack_2b8 = plVar32;
          if ((plVar32 != (long *)0x0) &&
             (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar32 + 1), lVar14 == 0)) {
            (**(code **)(*plVar32 + 0x10))(plVar32);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar32);
          }
          if (((ulong)local_2f8[0] & 1) != 0) {
            _ZdlPv(local_2e8);
          }
          if ((local_2b0 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_29c,CONCAT13(uStack_29d,CONCAT21(uStack_29f,cStack_2a0)))
                  );
          }
          puVar29 = puVar22;
          if (((ulong)local_2e0 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_2cc,local_2d0));
          }
                    /* try { // try from 008be374 to 009be37b has its CatchHandler @ 008c75b0 */
                    /* try { // try from 008be37c to 009be42f has its CatchHandler @ 008bda04 */
          while (puVar18 = (undefined8 *)*puVar29, puVar23 = puVar29,
                (undefined8 *)*puVar29 != (undefined8 *)0x0) {
            while (puVar19 = puVar18, puVar29 = puVar19,
                  *(int *)((long)puVar19 + 0x1c) <= (int)uVar3) {
              if ((int)uVar3 <= *(int *)((long)puVar19 + 0x1c)) goto LAB_008be42c;
              puVar18 = (undefined8 *)puVar19[1];
              if ((undefined8 *)puVar19[1] == (undefined8 *)0x0) {
                puVar29 = puVar19 + 1;
                puVar23 = puVar19;
                goto LAB_008be3a4;
              }
            }
          }
LAB_008be3a4:
          puVar19 = (undefined8 *)_Znwm(0x28);
          *(uint *)((long)puVar19 + 0x1c) = uVar3;
          *(undefined1 *)(puVar19 + 4) = 0;
          *puVar19 = 0;
          puVar19[1] = 0;
          puVar19[2] = puVar23;
          *puVar29 = puVar19;
          puVar18 = puVar19;
          if (*(long *)*plVar35 != 0) {
            *plVar35 = *(long *)*plVar35;
            puVar18 = (undefined8 *)*puVar29;
          }
          FUN_0043bb64(*(undefined8 *)(param_1 + 0x30),puVar18);
          *(long *)(param_1 + 0x38) = *(long *)(param_1 + 0x38) + 1;
LAB_008be42c:
                    /* try { // try from 008be430 to 009be44f has its CatchHandler @ 008c7758 */
          iVar13 = (int)((double)(iVar11 + -0x3c0) * 0.5 + 224.0) + (uVar34 % 3) * 0xd3;
          iVar12 = (uVar34 / 3) * 0x41 + local_32c;
          FUN_00a46704(&local_2b0,puVar24,iVar13 + 0x69,iVar12 + 0x1b,*(byte *)(puVar19 + 4) ^ 1);
          plVar32 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
          (**(code **)(*plVar32 + 0x10))(plVar32,1);
          FUN_00a466d0(0x3f800000,0x3f800000);
          plVar32 = *(long **)(param_1 + 0x70);
          if (plVar32 != (long *)0x0) {
            uVar20 = CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
            do {
              if ((int)uVar3 < (int)plVar32[4]) {
                plVar32 = (long *)*plVar32;
              }
              else {
                if ((int)uVar3 <= (int)plVar32[4]) goto LAB_008be4d4;
                plVar32 = (long *)plVar32[1];
              }
              if (plVar32 == (long *)0x0) break;
            } while( true );
          }
          if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
            FUN_004428f0("map::at:  key not found");
          }
          goto LAB_008bf510;
        }
      }
      uVar34 = 0xffffffff;
LAB_008be7d0:
      FUN_008514b8();
      iVar13 = FUN_0046c984();
      uVar10 = (uint)local_298;
      iVar12 = ((int)uVar34 / 3) * 0x41;
      puVar30 = *(undefined4 **)(param_1 + 0xa0);
      iVar42 = (int)((double)(iVar13 + -0x3c0) * 0.5 + 75.0);
      iVar13 = iVar12 + 0x37;
      if (-1 < iVar12 + 0x36) {
        iVar13 = iVar12 + 0x36;
      }
      iVar13 = local_32c + (iVar13 >> 1);
      if (*(undefined4 **)(param_1 + 0xa8) <= puVar30) {
                    /* try { // try from 008be858 to 009be8a3 has its CatchHandler @ 008c7760 */
        pvVar36 = *(void **)(param_1 + 0x98);
        sVar41 = (long)puVar30 - (long)pvVar36;
        uVar15 = ((long)sVar41 >> 2) * -0x5555555555555555 + 1;
        if (uVar15 < 0x1555555555555556) {
          lVar14 = (long)*(undefined4 **)(param_1 + 0xa8) - (long)pvVar36 >> 2;
          uVar33 = lVar14 * 0x5555555555555556;
          if (uVar33 < uVar15 || uVar33 - uVar15 == 0) {
            uVar33 = uVar15;
          }
                    /* try { // try from 008be8a4 to 009bf463 has its CatchHandler @ 008bda04 */
          if (0xaaaaaaaaaaaaaa9 < (ulong)(lVar14 * -0x5555555555555555)) {
            uVar33 = 0x1555555555555555;
          }
          if (uVar33 == 0) {
            lVar14 = 0;
          }
          else {
            if (0x1555555555555555 < uVar33) {
              if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
                FUN_00440e80();
              }
              goto LAB_008bf510;
            }
            lVar14 = _Znwm(uVar33 * 0xc);
          }
          puVar30 = (undefined4 *)(lVar14 + ((long)sVar41 >> 2) * 4);
          puVar30[2] = iVar13;
          puVar39 = puVar30 + 3;
          *puVar30 = uVar10;
          puVar30[1] = iVar42;
          memcpy((void *)((long)puVar30 - sVar41),pvVar36,sVar41);
          *(void **)(param_1 + 0x98) = (void *)((long)puVar30 - sVar41);
          *(undefined4 **)(param_1 + 0xa0) = puVar39;
          *(ulong *)(param_1 + 0xa8) = lVar14 + uVar33 * 0xc;
          if (pvVar36 != (void *)0x0) {
            _ZdlPv(pvVar36);
          }
          goto LAB_008be924;
        }
        if (*(long *)(lVar4 + 0x28) == local_80) {
          FUN_008cba54(param_1 + 0x98);
LAB_008bf1f0:
          if (*(long *)(lVar4 + 0x28) == local_80) {
            FUN_006b8c04(param_1 + 0x80);
LAB_008bf210:
            if (*(long *)(lVar4 + 0x28) == local_80) {
                    /* WARNING: Subroutine does not return */
              FUN_00440e80();
            }
          }
        }
        goto LAB_008bf510;
      }
                    /* try { // try from 008be83c to 009be843 has its CatchHandler @ 008c7660 */
      *puVar30 = (uint)local_298;
      puVar30[1] = iVar42;
      puVar39 = puVar30 + 3;
      puVar30[2] = iVar13;
LAB_008be924:
      puVar43 = PTR_DAT_00c9af70;
      *(undefined4 **)(param_1 + 0xa0) = puVar39;
      FUN_008514b8();
      iVar13 = FUN_0046c984();
      puVar29 = *(undefined8 **)(param_1 + 0x88);
      iVar12 = local_32c + iVar12;
      local_32c = iVar12 + 0x4c;
      iVar12 = iVar12 + 0x3e;
      iVar13 = (int)((double)(iVar13 + -0x3c0) * 0.5 + 76.0);
      if (puVar29 < *(undefined8 **)(param_1 + 0x90)) {
        puVar23 = puVar29 + 1;
        *puVar29 = CONCAT44(iVar12,iVar13);
      }
      else {
        pvVar36 = *(void **)(param_1 + 0x80);
        lVar14 = (long)puVar29 - (long)pvVar36 >> 3;
        uVar15 = lVar14 + 1;
        if (uVar15 >> 0x3d != 0) goto LAB_008bf1f0;
        uVar26 = (long)*(undefined8 **)(param_1 + 0x90) - (long)pvVar36;
        uVar33 = (long)uVar26 >> 2;
        if (uVar33 <= uVar15) {
          uVar33 = uVar15;
        }
        if (0x7ffffffffffffff7 < uVar26) {
          uVar33 = 0x1fffffffffffffff;
        }
        if (uVar33 == 0) {
          pvVar16 = (void *)0x0;
        }
        else {
          if (uVar33 >> 0x3d != 0) goto LAB_008bf210;
          pvVar16 = (void *)_Znwm(uVar33 << 3);
        }
        puVar18 = (undefined8 *)((long)pvVar16 + lVar14 * 8);
        puVar23 = puVar18 + 1;
        *puVar18 = CONCAT44(iVar12,iVar13);
        memcpy(pvVar16,pvVar36,(long)puVar29 - (long)pvVar36);
        *(void **)(param_1 + 0x80) = pvVar16;
        *(undefined8 **)(param_1 + 0x88) = puVar23;
        *(void **)(param_1 + 0x90) = (void *)((long)pvVar16 + uVar33 * 8);
        if (pvVar36 != (void *)0x0) {
          _ZdlPv(pvVar36);
        }
      }
      pvVar36 = (void *)CONCAT44(uStack_28c,CONCAT13(uStack_28d,CONCAT21(uStack_28f,cStack_290)));
      *(undefined8 **)(param_1 + 0x88) = puVar23;
      if (pvVar36 != (void *)0x0) {
        _ZdlPv(pvVar36);
      }
      plVar32 = (long *)plVar31[1];
      plVar37 = plVar31;
      if ((long *)plVar31[1] == (long *)0x0) {
        do {
          plVar31 = (long *)plVar37[2];
          bVar8 = (long *)*plVar31 != plVar37;
          plVar37 = plVar31;
        } while (bVar8);
      }
      else {
        do {
          plVar31 = plVar32;
          plVar32 = (long *)*plVar31;
        } while ((long *)*plVar31 != (long *)0x0);
      }
    } while (plVar31 != plVar27);
  }
  *(undefined4 *)(param_1 + 4) = 0;
  *(int *)(param_1 + 0xc) = 0x230 - local_32c;
  *(long *)(param_1 + 0x88) = *(long *)(param_1 + 0x88) + -8;
  FUN_008514b8();
  iVar11 = FUN_0046c984();
  iVar11 = (int)((double)(iVar11 + -0x3c0) * 0.5 + 317.0);
  FUN_00a46704(&local_298,puVar24,iVar11 + 0xa5,0x24f,0x7d);
  (**(code **)(*local_298 + 0x10))(local_298,1);
  FUN_00a466d0(0x3faa3d71,0x3faa3d71);
  plVar38 = local_298;
  FUN_00a46704(&local_2e0,puVar24,0,0,0x7c);
  plVar31 = local_2e0;
  local_2e0 = (long *)0x0;
  local_2b0 = (byte)plVar31;
  uStack_2af = (undefined5)((ulong)plVar31 >> 8);
  uStack_2aa = (undefined2)((ulong)plVar31 >> 0x30);
  plVar31 = (long *)FUN_00a4658c(plVar38,&local_2b0);
  (**(code **)(*plVar31 + 0x10))(plVar31,1);
  FUN_00a466d0(0x3f800000,0x3f800000);
  plVar31 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar31 != (long *)0x0) {
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  plVar31 = local_2e0;
  local_2e0 = (long *)0x0;
  if (plVar31 != (long *)0x0) {
    plVar38 = (long *)plVar31[0x16];
    *plVar31 = (long)(puVar43 + 0x10);
    if (plVar38 != (long *)0x0) {
      lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar38 + 1);
      if (lVar14 == 0) {
        (**(code **)(*plVar38 + 0x10))(plVar38);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar38);
      }
    }
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  lVar14 = FUN_008514b8();
  plVar31 = local_298;
  local_c0 = &local_e0;
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  local_2b0 = (byte)plVar31;
  uStack_2af = (undefined5)((ulong)plVar31 >> 8);
  uStack_2aa = (undefined2)((ulong)plVar31 >> 0x30);
  local_e0 = &PTR_FUN_00c839e8;
  lStack_d8 = param_1;
  uVar20 = FUN_008b6fa8(lVar14 + 0x2f38,700,iVar11,0x22f,0x14a,0x40,&local_2b0,&local_e0);
  uVar20 = FUN_008b6ecc(uVar20,1);
  FUN_008b6ed4(uVar20,0);
  if (local_c0 == &local_e0) {
    lVar14 = 0x20;
    pppuVar21 = &local_e0;
LAB_008bec48:
    (**(code **)((long)*pppuVar21 + lVar14))();
  }
  else if (local_c0 != (undefined ***)0x0) {
    lVar14 = 0x28;
    pppuVar21 = local_c0;
    goto LAB_008bec48;
  }
  plVar31 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar31 != (long *)0x0) {
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  plVar31 = (long *)CONCAT44(local_298._4_4_,(uint)local_298);
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  if (plVar31 != (long *)0x0) {
    plVar38 = (long *)plVar31[0x16];
    *plVar31 = (long)(puVar43 + 0x10);
    if ((plVar38 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar38 + 1), lVar14 == 0)) {
      (**(code **)(*plVar38 + 0x10))(plVar38);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar38);
    }
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  FUN_008514b8();
  iVar11 = FUN_0046c984();
  iVar11 = (int)((double)(iVar11 + -0x3c0) * 0.5 + 765.0);
  FUN_00a46704(&local_298,puVar24,iVar11 + 0x49,0x24f,0x7b);
  (**(code **)(*(long *)CONCAT44(local_298._4_4_,(uint)local_298) + 0x10))
            ((long *)CONCAT44(local_298._4_4_,(uint)local_298),1);
  FUN_00a466d0(0x3faa3d71,0x3faa3d71);
  uVar20 = CONCAT44(local_298._4_4_,(uint)local_298);
  FUN_00a46704(&local_2e0,puVar24,0,0,0x22);
  plVar31 = local_2e0;
  local_2e0 = (long *)0x0;
  local_2b0 = (byte)plVar31;
  uStack_2af = (undefined5)((ulong)plVar31 >> 8);
  uStack_2aa = (undefined2)((ulong)plVar31 >> 0x30);
  plVar31 = (long *)FUN_00a4658c(uVar20,&local_2b0);
  (**(code **)(*plVar31 + 0x10))(plVar31,1);
  FUN_00a466d0(0x3f800000,0x3f800000);
  plVar31 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar31 != (long *)0x0) {
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  plVar31 = local_2e0;
  local_2e0 = (long *)0x0;
  if (plVar31 != (long *)0x0) {
    plVar38 = (long *)plVar31[0x16];
    *plVar31 = (long)(puVar43 + 0x10);
    if ((plVar38 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar38 + 1), lVar14 == 0)) {
      (**(code **)(*plVar38 + 0x10))(plVar38);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar38);
    }
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  lVar14 = FUN_008514b8();
  uVar7 = local_298._4_4_;
  uVar10 = (uint)local_298;
  uVar20 = CONCAT44(local_298._4_4_,(uint)local_298);
  local_f0 = &local_110;
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  local_2b0 = (byte)uVar10;
  uStack_2af = (undefined5)((ulong)uVar20 >> 8);
  uStack_2aa = (undefined2)((uint)uVar7 >> 0x10);
  local_110 = &PTR_FUN_00c83a68;
  lStack_108 = param_1;
  uVar20 = FUN_008b6fa8(lVar14 + 0x2f38,0x2bd,iVar11,0x22f,0x92,0x40,&local_2b0,&local_110);
  uVar20 = FUN_008b6ecc(uVar20,1);
  FUN_008b6ed4(uVar20,0);
  if (local_f0 == &local_110) {
    lVar14 = 0x20;
    pppuVar21 = &local_110;
LAB_008beeac:
    (**(code **)((long)*pppuVar21 + lVar14))();
  }
  else if (local_f0 != (undefined ***)0x0) {
    lVar14 = 0x28;
    pppuVar21 = local_f0;
    goto LAB_008beeac;
  }
  plVar31 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar31 != (long *)0x0) {
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  plVar31 = (long *)CONCAT44(local_298._4_4_,(uint)local_298);
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  if (plVar31 != (long *)0x0) {
    plVar38 = (long *)plVar31[0x16];
    *plVar31 = (long)(puVar43 + 0x10);
    if ((plVar38 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar38 + 1), lVar14 == 0)) {
      (**(code **)(*plVar38 + 0x10))(plVar38);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar38);
    }
    *plVar31 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  FUN_008514b8();
  iVar11 = FUN_0046c984();
  iVar11 = (int)((double)(iVar11 + -0x3c0) * 0.5 + 876.0);
  FUN_00a46704(&local_298,puVar24,iVar11 + 0x22,0x2c,0x7e);
  (**(code **)(*(long *)CONCAT44(local_298._4_4_,(uint)local_298) + 0x10))
            ((long *)CONCAT44(local_298._4_4_,(uint)local_298),1);
  FUN_00a466d0(0x3f800000,0x3f800000);
  lVar14 = FUN_008514b8();
  uVar7 = local_298._4_4_;
  uVar10 = (uint)local_298;
  uVar20 = CONCAT44(local_298._4_4_,(uint)local_298);
  local_120 = &local_140;
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  local_2b0 = (byte)uVar10;
  uStack_2af = (undefined5)((ulong)uVar20 >> 8);
  uStack_2aa = (undefined2)((uint)uVar7 >> 0x10);
  local_140 = &PTR_FUN_00c83ae8;
  lStack_138 = param_1;
  uVar20 = FUN_008b6fa8(lVar14 + 0x2f38,0x2be,iVar11,10,0x44,0x44,&local_2b0,&local_140);
  uVar20 = FUN_008b6ecc(uVar20,1);
  uVar20 = FUN_008b6ed4(uVar20,0);
  FUN_008b6eec(uVar20,1);
  puVar6 = PTR_DAT_00c9af68;
  if (local_120 == &local_140) {
    lVar14 = 0x20;
    pppuVar21 = &local_140;
  }
  else {
    if (local_120 == (undefined ***)0x0) goto LAB_008bf044;
    lVar14 = 0x28;
    pppuVar21 = local_120;
  }
  (**(code **)((long)*pppuVar21 + lVar14))();
LAB_008bf044:
  plVar31 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar31 != (long *)0x0) {
    *plVar31 = (long)(puVar6 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  plVar31 = (long *)CONCAT44(local_298._4_4_,(uint)local_298);
  local_298._0_4_ = 0;
  local_298._4_4_ = 0;
  if (plVar31 != (long *)0x0) {
    plVar38 = (long *)plVar31[0x16];
    *plVar31 = (long)(puVar43 + 0x10);
    if ((plVar38 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar38 + 1), lVar14 == 0)) {
      (**(code **)(*plVar38 + 0x10))(plVar38);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar38);
    }
    *plVar31 = (long)(puVar6 + 0x10);
    FUN_005d8b88(plVar31 + 10);
    _ZdlPv(plVar31);
  }
  if (*(long *)(lVar4 + 0x28) == local_80) {
    return;
  }
LAB_008bf510:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_008be4d4:
                    /* try { // try from 008be4e4 to 009be4e7 has its CatchHandler @ 008c7634 */
                    /* try { // try from 008be4e8 to 009be547 has its CatchHandler @ 008bda04 */
  FUN_00a46bf0(local_2f8,plVar32 + 5,0,0,0,0,0x99,0x26);
  local_2e0 = local_2f8[0];
  local_2f8[0] = (long *)0x0;
  plVar32 = (long *)FUN_00a4658c(uVar20,&local_2e0);
  (**(code **)(*plVar32 + 0x10))(plVar32,1);
  FUN_00a466d0(0x3f800000,0x3f800000);
  plVar32 = local_2e0;
  local_2e0 = (long *)0x0;
  if (plVar32 != (long *)0x0) {
                    /* try { // try from 008be548 to 009be567 has its CatchHandler @ 008c7764 */
    *plVar32 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar32 + 10);
    _ZdlPv(plVar32);
  }
  plVar32 = local_2f8[0];
  local_2f8[0] = (long *)0x0;
  if (plVar32 != (long *)0x0) {
    plVar37 = (long *)plVar32[0x16];
    *plVar32 = (long)(PTR_DAT_00c9af70 + 0x10);
    if ((plVar37 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar37 + 1), lVar14 == 0)) {
      (**(code **)(*plVar37 + 0x10))(plVar37);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar37);
    }
    *plVar32 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar32 + 10);
    _ZdlPv(plVar32);
  }
  lVar14 = FUN_008514b8();
  puVar29 = puVar25;
  while (puVar23 = (undefined8 *)*puVar29, puVar19 = puVar29, puVar18 = puVar29,
        (undefined8 *)*puVar29 != (undefined8 *)0x0) {
    while (puVar29 = puVar23, *(int *)((long)puVar29 + 0x1c) <= (int)uVar3) {
                    /* try { // try from 008be5f0 to 009be5f3 has its CatchHandler @ 008c7754 */
      if ((int)uVar3 <= *(int *)((long)puVar29 + 0x1c)) goto LAB_008be65c;
                    /* try { // try from 008be5f4 to 009be673 has its CatchHandler @ 008bda04 */
      puVar23 = (undefined8 *)puVar29[1];
      if ((undefined8 *)puVar29[1] == (undefined8 *)0x0) {
        puVar18 = puVar29 + 1;
        puVar19 = puVar29;
        goto LAB_008be600;
      }
    }
  }
LAB_008be600:
  puVar29 = (undefined8 *)_Znwm(0x28);
  *(uint *)((long)puVar29 + 0x1c) = uVar3;
  *(undefined4 *)(puVar29 + 4) = 0;
  *puVar29 = 0;
  puVar29[1] = 0;
  puVar29[2] = puVar19;
  *puVar18 = puVar29;
  puVar23 = puVar29;
  if (*(long *)*plVar38 != 0) {
    *plVar38 = *(long *)*plVar38;
    puVar23 = (undefined8 *)*puVar18;
  }
  FUN_0043bb64(*(undefined8 *)(param_1 + 0x48),puVar23);
  *(long *)(param_1 + 0x50) = *(long *)(param_1 + 0x50) + 1;
LAB_008be65c:
  local_2e0 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
                    /* try { // try from 008be674 to 009be67f has its CatchHandler @ 008c750c */
  local_b0 = &PTR_FUN_00c83968;
  local_90 = &local_b0;
  lStack_a8 = param_1;
  local_a0 = (ulong)uVar3;
                    /* try { // try from 008be6a0 to 009be6a7 has its CatchHandler @ 008c7578 */
  uVar20 = FUN_008b6fa8(lVar14 + 0x2f38,*(undefined4 *)(puVar29 + 4),iVar13,iVar12,0xd3,0x36,
                        &local_2e0,&local_b0);
  uVar20 = FUN_008b6ecc(uVar20,1);
  FUN_008b6ed4(uVar20,0);
  if (local_90 == &local_b0) {
    pppuVar21 = &local_b0;
    lVar14 = 0x20;
  }
  else {
    if (local_90 == (undefined ***)0x0) goto LAB_008be700;
    lVar14 = 0x28;
    pppuVar21 = local_90;
  }
  (**(code **)((long)*pppuVar21 + lVar14))();
LAB_008be700:
  plVar32 = local_2e0;
  local_2e0 = (long *)0x0;
  if (plVar32 != (long *)0x0) {
                    /* try { // try from 008be718 to 009be727 has its CatchHandler @ 008c7664 */
    *plVar32 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar32 + 10);
    _ZdlPv(plVar32);
  }
  plVar32 = (long *)CONCAT26(uStack_2aa,CONCAT51(uStack_2af,local_2b0));
  local_2b0 = 0;
  uStack_2af = 0;
  uStack_2aa = 0;
  if (plVar32 != (long *)0x0) {
    plVar37 = (long *)plVar32[0x16];
    *plVar32 = (long)puVar1;
    if ((plVar37 != (long *)0x0) &&
       (lVar14 = FUN_00c538e0(0xffffffffffffffff,plVar37 + 1), lVar14 == 0)) {
      (**(code **)(*plVar37 + 0x10))(plVar37);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar37);
    }
    *plVar32 = (long)(puVar6 + 0x10);
    FUN_005d8b88(plVar32 + 10);
    _ZdlPv(plVar32);
  }
  puVar17 = puVar17 + 1;
  iVar9 = iVar9 + 1;
  uVar3 = uVar34 + 1;
  if (puVar17 == puVar40) goto LAB_008be7d0;
  goto LAB_008be148;
}

~~~
