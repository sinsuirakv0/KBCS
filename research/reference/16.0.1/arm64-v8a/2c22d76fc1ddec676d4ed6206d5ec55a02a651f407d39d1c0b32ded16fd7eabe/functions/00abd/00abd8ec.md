# 00abd8ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00abd8ec",
  "name": "FUN_00abd8ec",
  "size": 1688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f506bb4e6039f3614d391a219f18da0723deba143d88c2a7671d27bd359b2727",
  "source_text_sha256": "f506bb4e6039f3614d391a219f18da0723deba143d88c2a7671d27bd359b2727"
}
~~~

## 呼び出し元

- [00b28f54](../00b28/00b28f54.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0044108c](../00441/0044108c.md)
- [00487e20](../00487/00487e20.md)
- [00488434](../00488/00488434.md)
- [00488658](../00488/00488658.md)
- [00596f2c](../00596/00596f2c.md)
- [00597608](../00597/00597608.md)
- [0086a1ec](../0086a/0086a1ec.md)
- [00abb92c](../00abb/00abb92c.md)
- [00abc814](../00abc/00abc814.md)
- [00ac0fd0](../00ac0/00ac0fd0.md)
- [00ac0fe4](../00ac0/00ac0fe4.md)
- [00ac0ff8](../00ac0/00ac0ff8.md)
- [00ac100c](../00ac1/00ac100c.md)
- [00b110ec](../00b11/00b110ec.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5a850](../00c5a/00c5a850.md)

## 関連文字列（未確認候補）

~~~text
"medallist.json"
"medalname.tsv"
~~~

## 疑似コード / UTF-8 13617 bytes

~~~c

void FUN_00abd8ec(long *param_1)

{
  bool bVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined *puVar8;
  ulong uVar9;
  long lVar10;
  undefined8 *puVar11;
  void *pvVar12;
  ulong uVar13;
  ulong uVar14;
  ulong uVar15;
  long *plVar16;
  undefined8 uVar17;
  void *pvVar18;
  ulong uVar19;
  undefined4 *puVar20;
  long *plVar21;
  undefined8 *puVar22;
  undefined1 auStack_200 [8];
  long *local_1f8;
  long local_1f0;
  long *local_1e8;
  byte local_1e0;
  undefined5 uStack_1df;
  char cStack_1da;
  char cStack_1d9;
  char cStack_1d8;
  char acStack_1d7 [5];
  char local_1d2;
  undefined1 local_1d1;
  void *local_1d0;
  undefined **local_1c8;
  void *local_1c0;
  void *local_1b8;
  byte local_1a8;
  void *local_198;
  long local_180;
  undefined *local_178 [8];
  byte local_138;
  void *local_128;
  undefined1 auStack_110 [160];
  long local_70;
  
  lVar7 = tpidr_el0;
                    /* try { // try from 00abd910 to 00bbd91b has its CatchHandler @ 00abdb04 */
  local_70 = *(long *)(lVar7 + 0x28);
  FUN_00487e20(&local_1c8);
                    /* try { // try from 00abd934 to 00bbd94f has its CatchHandler @ 00abdabc */
  local_1c8 = &PTR_FUN_00c64d38;
  local_1e0 = 0x1c;
  local_1d1 = 0;
                    /* try { // try from 00abd950 to 00bbd9af has its CatchHandler @ 00abd7ec */
  uStack_1df = (undefined5)s_medallist_json_002a1884._0_6_;
  cStack_1da = SUB61(s_medallist_json_002a1884._0_6_,5);
  cStack_1d9 = (char)s_medallist_json_002a1884._6_2_;
  cStack_1d8 = SUB21(s_medallist_json_002a1884._6_2_,1);
  acStack_1d7 = SUB65(s_medallist_json_002a1884._8_6_,0);
  local_1d2 = SUB61(s_medallist_json_002a1884._8_6_,5);
  uVar9 = FUN_00b110ec(&local_1c8,&local_1e0,0,0);
  if ((local_1e0 & 1) != 0) {
    _ZdlPv(local_1d0);
  }
  if ((uVar9 & 1) != 0) {
    FUN_00488434(&local_1e0,&local_1c8);
    thunk_FUN_0058adc8(auStack_200,&local_1e0);
    FUN_00596f2c(&local_1f0,auStack_200);
                    /* try { // try from 00abd9b0 to 00bbd9bb has its CatchHandler @ 00abdb08 */
    if ((local_1f8 != (long *)0x0) &&
       (lVar10 = FUN_00c53d00(0xffffffffffffffff,local_1f8 + 1), lVar10 == 0)) {
      (**(code **)(*local_1f8 + 0x10))(local_1f8);
                    /* try { // try from 00abd9d0 to 00bbd9e3 has its CatchHandler @ 00abda78 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_1f8);
    }
    if ((local_1e0 & 1) != 0) {
                    /* try { // try from 00abd9e4 to 00bbdb37 has its CatchHandler @ 00abd7ec */
      _ZdlPv(local_1d0);
    }
    plVar3 = (long *)*param_1;
    plVar16 = (long *)param_1[1];
    while (plVar16 != plVar3) {
      plVar16 = plVar16 + -1;
      lVar10 = *plVar16;
      *plVar16 = 0;
      if (lVar10 != 0) {
        FUN_0086a1ec(plVar16);
      }
    }
    plVar16 = param_1 + 3;
    uVar9 = 0;
    puVar20 = (undefined4 *)((ulong)&local_1e0 | 1);
    param_1[1] = (long)plVar3;
    param_1[4] = *plVar16;
    while( true ) {
      local_1e0 = 0xc;
      *puVar20 = 0x6e6f6369;
      *(undefined2 *)(puVar20 + 1) = 0x4449;
                    /* catch() { ... } // from try @ 00abd850 with catch @ 00abda74 */
      cStack_1d9 = 0;
                    /* catch() { ... } // from try @ 00abd9d0 with catch @ 00abda78 */
      lVar10 = FUN_0044108c(local_1f0 + 0x10,&local_1e0);
      lVar10 = *(long *)(lVar10 + 0x38);
      if (*(int *)(lVar10 + 8) != 6) {
        lVar10 = 0;
      }
      lVar4 = *(long *)(lVar10 + 0x10);
      lVar10 = *(long *)(lVar10 + 0x18);
      if ((local_1e0 & 1) != 0) {
        _ZdlPv(local_1d0);
      }
      puVar8 = PTR__ZSt7nothrow_00c9b520;
      if ((ulong)(lVar10 - lVar4 >> 3) <= uVar9) {
        lVar10 = param_1[3];
        lVar4 = param_1[4];
        uVar19 = lVar4 - lVar10 >> 3;
        uVar9 = uVar19;
        if (0 < (long)uVar19) goto LAB_00abdcfc;
        goto LAB_00abdd1c;
      }
                    /* catch() { ... } // from try @ 00abd934 with catch @ 00abdabc */
      puVar11 = (undefined8 *)_Znwm(0xb0);
      puVar5 = (undefined8 *)param_1[1];
      puVar6 = (undefined8 *)param_1[2];
      local_1e0 = (byte)puVar11;
      uStack_1df = (undefined5)((ulong)puVar11 >> 8);
      cStack_1da = (char)((ulong)puVar11 >> 0x30);
      cStack_1d9 = (char)((ulong)puVar11 >> 0x38);
      puVar11[3] = 0;
      puVar11[2] = 0;
      puVar11[5] = 0;
      puVar11[4] = 0;
      puVar11[7] = 0;
      puVar11[6] = 0;
      puVar11[9] = 0;
      puVar11[8] = 0;
      puVar11[0xb] = 0;
      puVar11[10] = 0;
      puVar11[0xd] = 0;
      puVar11[0xc] = 0;
      puVar11[0xf] = 0;
      puVar11[0xe] = 0;
      puVar11[0x11] = 0;
      puVar11[0x10] = 0;
      puVar11[0x13] = 0;
      puVar11[0x12] = 0;
      puVar11[0x15] = 0;
      puVar11[0x14] = 0;
      puVar11[1] = 0;
      *puVar11 = 0;
      if (puVar5 < puVar6) {
        local_1e0 = 0;
        uStack_1df = 0;
        cStack_1da = 0;
        cStack_1d9 = 0;
        puVar22 = puVar5 + 1;
        *puVar5 = puVar11;
      }
      else {
        pvVar18 = (void *)*param_1;
                    /* catch() { ... } // from try @ 00abd910 with catch @ 00abdb04 */
        lVar10 = (long)puVar5 - (long)pvVar18 >> 3;
                    /* catch() { ... } // from try @ 00abd9b0 with catch @ 00abdb08 */
        uVar19 = lVar10 + 1;
        if (uVar19 >> 0x3d != 0) goto LAB_00abdf34;
        uVar15 = (long)puVar6 - (long)pvVar18;
        uVar14 = (long)uVar15 >> 2;
        if (uVar14 <= uVar19) {
          uVar14 = uVar19;
        }
        if (0x7ffffffffffffff7 < uVar15) {
          uVar14 = 0x1fffffffffffffff;
        }
        if (uVar14 == 0) {
          pvVar12 = (void *)0x0;
        }
        else {
          if (uVar14 >> 0x3d != 0) {
            if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00440ec0();
            }
            goto LAB_00abe054;
          }
          pvVar12 = (void *)_Znwm(uVar14 << 3);
        }
        puVar6 = (undefined8 *)((long)pvVar12 + lVar10 * 8);
        local_1e0 = 0;
        uStack_1df = 0;
        cStack_1da = 0;
        cStack_1d9 = 0;
        puVar22 = puVar6 + 1;
        *puVar6 = puVar11;
        memcpy(pvVar12,pvVar18,(long)puVar5 - (long)pvVar18);
        *param_1 = (long)pvVar12;
        param_1[1] = (long)puVar22;
        param_1[2] = (long)((long)pvVar12 + uVar14 * 8);
        if (pvVar18 != (void *)0x0) {
          _ZdlPv(pvVar18);
        }
      }
      lVar10 = CONCAT17(cStack_1d9,CONCAT16(cStack_1da,CONCAT51(uStack_1df,local_1e0)));
      param_1[1] = (long)puVar22;
      local_1e0 = 0;
      uStack_1df._0_1_ = '\0';
      uStack_1df._1_1_ = '\0';
      uStack_1df._2_1_ = '\0';
      uStack_1df._3_1_ = '\0';
      uStack_1df._4_1_ = '\0';
      cStack_1da = '\0';
      cStack_1d9 = '\0';
      if (lVar10 != 0) {
        FUN_0086a1ec(&local_1e0);
        puVar22 = (undefined8 *)param_1[1];
      }
      if (puVar22 == (undefined8 *)*param_1) break;
      uVar17 = puVar22[-1];
      local_1e0 = 0xc;
      *puVar20 = 0x6e6f6369;
      *(undefined2 *)(puVar20 + 1) = 0x4449;
      cStack_1d9 = '\0';
      lVar10 = FUN_0044108c(local_1f0 + 0x10,&local_1e0);
      lVar10 = *(long *)(lVar10 + 0x38);
      if (*(int *)(lVar10 + 8) != 6) {
        lVar10 = 0;
      }
      lVar10 = *(long *)(*(long *)(lVar10 + 0x10) + uVar9 * 8);
      if (*(int *)(lVar10 + 8) != 7) {
        lVar10 = 0;
      }
      FUN_00abb92c(uVar17,lVar10);
      if ((local_1e0 & 1) != 0) {
        _ZdlPv(local_1d0);
      }
      if (param_1[1] == *param_1) goto LAB_00abdefc;
      plVar3 = (long *)param_1[4];
      uVar19 = (ulong)*(uint *)(*(long *)(param_1[1] + -8) + 0x44);
      if (plVar3 < (long *)param_1[5]) {
        plVar21 = plVar3 + 1;
                    /* catch() { ... } // from try @ 00abd874 with catch @ 00abda58 */
        *plVar3 = uVar9 + (uVar19 << 0x20);
      }
      else {
        pvVar18 = (void *)*plVar16;
        lVar10 = (long)plVar3 - (long)pvVar18 >> 3;
        uVar14 = lVar10 + 1;
        if (uVar14 >> 0x3d != 0) goto LAB_00abdf18;
        uVar13 = param_1[5] - (long)pvVar18;
        uVar15 = (long)uVar13 >> 2;
        if (uVar15 <= uVar14) {
          uVar15 = uVar14;
        }
        if (0x7ffffffffffffff7 < uVar13) {
          uVar15 = 0x1fffffffffffffff;
        }
        if (uVar15 == 0) {
          pvVar12 = (void *)0x0;
        }
        else {
          if (uVar15 >> 0x3d != 0) goto LAB_00abdf50;
          pvVar12 = (void *)_Znwm(uVar15 << 3);
        }
        plVar2 = (long *)((long)pvVar12 + lVar10 * 8);
        plVar21 = plVar2 + 1;
        *plVar2 = uVar9 + (uVar19 << 0x20);
        memcpy(pvVar12,pvVar18,(long)plVar3 - (long)pvVar18);
        param_1[3] = (long)pvVar12;
        param_1[4] = (long)plVar21;
        param_1[5] = (long)((long)pvVar12 + uVar15 * 8);
        if (pvVar18 != (void *)0x0) {
          _ZdlPv(pvVar18);
        }
      }
      param_1[4] = (long)plVar21;
      uVar9 = uVar9 + 1;
    }
    if (*(long *)(lVar7 + 0x28) != local_70) goto LAB_00abe054;
    FUN_00ac0fe4(param_1);
LAB_00abdefc:
    if (*(long *)(lVar7 + 0x28) == local_70) {
      FUN_00ac0fe4(param_1);
LAB_00abdf18:
      if (*(long *)(lVar7 + 0x28) == local_70) {
        FUN_00ac0ff8(plVar16);
LAB_00abdf34:
                    /* try { // try from 00abdf40 to 00bbdf53 has its CatchHandler @ 00abe04c */
        if (*(long *)(lVar7 + 0x28) == local_70) {
          FUN_00ac0fd0(param_1);
LAB_00abdf50:
                    /* try { // try from 00abdf54 to 00bbe07b has its CatchHandler @ 00abdd38 */
          if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
            FUN_00440ec0();
          }
        }
      }
    }
    goto LAB_00abe054;
  }
  goto LAB_00abdd94;
  while (bVar1 = 1 < uVar9, uVar9 = uVar9 >> 1, bVar1) {
LAB_00abdcfc:
    pvVar18 = (void *)_ZnwmRKSt9nothrow_t(uVar9 << 3,puVar8);
    if (pvVar18 != (void *)0x0) {
                    /* try { // try from 00abdd38 to 00bbdddf has its CatchHandler @ 00abdd38
                       catch() { ... } // from try @ 00abdd38 with catch @ 00abdd38
                       catch() { ... } // from try @ 00abdec8 with catch @ 00abdd38
                       catch() { ... } // from try @ 00abdf54 with catch @ 00abdd38 */
      FUN_00ac100c(lVar10,lVar4,uVar19,pvVar18,uVar9);
      _ZdlPv(pvVar18);
      goto LAB_00abdd5c;
    }
  }
LAB_00abdd1c:
  FUN_00ac100c(lVar10,lVar4,uVar19,0,0);
LAB_00abdd5c:
  FUN_00488658(&local_1c8);
  if ((local_1e8 != (long *)0x0) &&
     (lVar10 = FUN_00c53d00(0xffffffffffffffff,local_1e8 + 1), lVar10 == 0)) {
    (**(code **)(*local_1e8 + 0x10))(local_1e8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_1e8);
  }
LAB_00abdd94:
  local_1e0 = 0x1a;
  local_1d2 = '\0';
  uStack_1df._0_1_ = s_medalname_tsv_002a4c1f[0];
  uStack_1df._1_1_ = s_medalname_tsv_002a4c1f[1];
  uStack_1df._2_1_ = s_medalname_tsv_002a4c1f[2];
  uStack_1df._3_1_ = s_medalname_tsv_002a4c1f[3];
  uStack_1df._4_1_ = s_medalname_tsv_002a4c1f[4];
  cStack_1da = (char)s_medalname_tsv_002a4c1f._5_3_;
  cStack_1d9 = SUB31(s_medalname_tsv_002a4c1f._5_3_,1);
  cStack_1d8 = SUB31(s_medalname_tsv_002a4c1f._5_3_,2);
  acStack_1d7[0] = s_medalname_tsv_002a4c1f[8];
  acStack_1d7[1] = s_medalname_tsv_002a4c1f[9];
  acStack_1d7[2] = s_medalname_tsv_002a4c1f[10];
  acStack_1d7[3] = s_medalname_tsv_002a4c1f[0xb];
  acStack_1d7[4] = s_medalname_tsv_002a4c1f[0xc];
  uVar9 = FUN_00b110ec(&local_1c8,&local_1e0,0,0);
  if ((local_1e0 & 1) != 0) {
    _ZdlPv(local_1d0);
  }
                    /* try { // try from 00abdde0 to 00bbdde7 has its CatchHandler @ 00abdfe0 */
  if ((uVar9 & 1) != 0) {
    lVar10 = *param_1;
    if (param_1[1] != lVar10) {
      uVar9 = 0;
      do {
        FUN_00abc814(*(undefined8 *)(lVar10 + uVar9 * 8),&local_1c8);
        lVar10 = *param_1;
        uVar9 = uVar9 + 1;
      } while (uVar9 < (ulong)(param_1[1] - lVar10 >> 3));
    }
    FUN_00488658(&local_1c8);
  }
                    /* try { // try from 00abde1c to 00bbde27 has its CatchHandler @ 00abe038 */
  puVar8 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  local_180 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  local_1c8 = (undefined **)(PTR_DAT_00c9abb0 + 0x10);
  *(undefined8 *)((long)&local_180 + *(long *)(local_180 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x18);
                    /* try { // try from 00abde58 to 00bbde6b has its CatchHandler @ 00abdff4 */
  local_178[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  if ((local_138 & 1) != 0) {
    _ZdlPv(local_128);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_180,puVar8 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_110);
  if ((local_1a8 & 1) != 0) {
    _ZdlPv(local_198);
  }
                    /* try { // try from 00abde9c to 00bbdec7 has its CatchHandler @ 00abdff0 */
  if (local_1c0 != (void *)0x0) {
    local_1b8 = local_1c0;
    _ZdlPv(local_1c0);
  }
  if (*(long *)(lVar7 + 0x28) == local_70) {
                    /* try { // try from 00abdec8 to 00bbdf3f has its CatchHandler @ 00abdd38 */
    return;
  }
LAB_00abe054:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
