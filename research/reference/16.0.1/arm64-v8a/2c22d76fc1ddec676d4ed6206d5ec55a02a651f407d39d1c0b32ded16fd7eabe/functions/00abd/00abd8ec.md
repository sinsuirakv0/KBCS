# 00abd8ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abd6f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-6ab7e250d6217821246406903ca901bf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abd95c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abd/00abd95c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-59dd3625ec2fe14508a39f7476dbc727)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "f506bb4e6039f3614d391a219f18da0723deba143d88c2a7671d27bd359b2727",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abd8ec",
        "00abdf7f"
      ],
      [
        "00abe054",
        "00abe057"
      ]
    ],
    "bytes_sha256": "d9bdcfc962077825679f426a2e12b7d3f3dcd336d6e6e07651659e791c8f0025",
    "instruction_count": 422,
    "instruction_bytes": 1688,
    "body_bytes": 1688,
    "indirect": 2,
    "unresolved": 2
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abd8ec"></a> `00abd8ec` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00abd8f0"></a> `00abd8f0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd8f4"></a> `00abd8f4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd8f8"></a> `00abd8f8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abd8fc"></a> `00abd8fc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abd900"></a> `00abd900` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abd904"></a> `00abd904` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abd908"></a> `00abd908` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00abd90c"></a> `00abd90c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abd910"></a> `00abd910` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abd914"></a> `00abd914` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abd918"></a> `00abd918` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00abd91c"></a> `00abd91c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abd920"></a> `00abd920` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd924"></a> `00abd924` | `3f 29 e7 97` | bl 0x00487e20 | `UNCONDITIONAL_CALL`
<a id="insn-00abd928"></a> `00abd928` | `28 0d 00 f0` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-00abd92c"></a> `00abd92c` | `08 e1 34 91` | add x8,x8,#0xd38 | `FALL_THROUGH`
<a id="insn-00abd930"></a> `00abd930` | `29 bf ff 90` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abd934"></a> `00abd934` | `29 11 22 91` | add x9,x9,#0x884 | `FALL_THROUGH`
<a id="insn-00abd938"></a> `00abd938` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abd93c"></a> `00abd93c` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-00abd940"></a> `00abd940` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abd944"></a> `00abd944` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abd948"></a> `00abd948` | `28 61 40 f8` | ldur x8,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00abd94c"></a> `00abd94c` | `ff ff 00 39` | strb wzr,[sp, #0x3f] | `FALL_THROUGH`
<a id="insn-00abd950"></a> `00abd950` | `ea 13 03 f8` | stur x10,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abd954"></a> `00abd954` | `e8 73 03 f8` | stur x8,[sp, #0x37] | `FALL_THROUGH`
<a id="insn-00abd958"></a> `00abd958` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abd95c"></a> `00abd95c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abd960"></a> `00abd960` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abd964"></a> `00abd964` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abd968"></a> `00abd968` | `e1 4d 01 94` | bl 0x00b110ec | `UNCONDITIONAL_CALL`
<a id="insn-00abd96c"></a> `00abd96c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abd970"></a> `00abd970` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abd974"></a> `00abd974` | `68 00 00 36` | tbz w8,#0x0,0x00abd980 | `CONDITIONAL_JUMP`
<a id="insn-00abd978"></a> `00abd978` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abd97c"></a> `00abd97c` | `4d 69 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd980"></a> `00abd980` | `b4 20 00 36` | tbz w20,#0x0,0x00abdd94 | `CONDITIONAL_JUMP`
<a id="insn-00abd984"></a> `00abd984` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abd988"></a> `00abd988` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abd98c"></a> `00abd98c` | `aa 2a e7 97` | bl 0x00488434 | `UNCONDITIONAL_CALL`
<a id="insn-00abd990"></a> `00abd990` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abd994"></a> `00abd994` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abd998"></a> `00abd998` | `1c 67 eb 97` | bl 0x00597608 | `UNCONDITIONAL_CALL`
<a id="insn-00abd99c"></a> `00abd99c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abd9a0"></a> `00abd9a0` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abd9a4"></a> `00abd9a4` | `62 65 eb 97` | bl 0x00596f2c | `UNCONDITIONAL_CALL`
<a id="insn-00abd9a8"></a> `00abd9a8` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abd9ac"></a> `00abd9ac` | `74 01 00 b4` | cbz x20,0x00abd9d8 | `CONDITIONAL_JUMP`
<a id="insn-00abd9b0"></a> `00abd9b0` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abd9b4"></a> `00abd9b4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abd9b8"></a> `00abd9b8` | `d2 58 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abd9bc"></a> `00abd9bc` | `e0 00 00 b5` | cbnz x0,0x00abd9d8 | `CONDITIONAL_JUMP`
<a id="insn-00abd9c0"></a> `00abd9c0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abd9c4"></a> `00abd9c4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abd9c8"></a> `00abd9c8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abd9cc"></a> `00abd9cc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abd9d0"></a> `00abd9d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abd9d4"></a> `00abd9d4` | `2b 69 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abd9d8"></a> `00abd9d8` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abd9dc"></a> `00abd9dc` | `68 00 00 36` | tbz w8,#0x0,0x00abd9e8 | `CONDITIONAL_JUMP`
<a id="insn-00abd9e0"></a> `00abd9e0` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abd9e4"></a> `00abd9e4` | `33 69 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd9e8"></a> `00abd9e8` | `75 22 40 a9` | ldp x21,x8,[x19] | `FALL_THROUGH`
<a id="insn-00abd9ec"></a> `00abd9ec` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00abd9f0"></a> `00abd9f0` | `80 01 00 54` | b.eq 0x00abda20 | `CONDITIONAL_JUMP`
<a id="insn-00abd9f4"></a> `00abd9f4` | `14 21 00 d1` | sub x20,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00abd9f8"></a> `00abd9f8` | `04 00 00 14` | b 0x00abda08 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd9fc"></a> `00abd9fc` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00abda00"></a> `00abda00` | `94 22 00 d1` | sub x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abda04"></a> `00abda04` | `e0 00 00 54` | b.eq 0x00abda20 | `CONDITIONAL_JUMP`
<a id="insn-00abda08"></a> `00abda08` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00abda0c"></a> `00abda0c` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00abda10"></a> `00abda10` | `61 ff ff b4` | cbz x1,0x00abd9fc | `CONDITIONAL_JUMP`
<a id="insn-00abda14"></a> `00abda14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abda18"></a> `00abda18` | `f5 b1 f6 97` | bl 0x0086a1ec | `UNCONDITIONAL_CALL`
<a id="insn-00abda1c"></a> `00abda1c` | `f8 ff ff 17` | b 0x00abd9fc | `UNCONDITIONAL_JUMP`
<a id="insn-00abda20"></a> `00abda20` | `ea 03 13 aa` | mov x10,x19 | `FALL_THROUGH`
<a id="insn-00abda24"></a> `00abda24` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abda28"></a> `00abda28` | `3c 6d 8c 52` | mov w28,#0x6369 | `FALL_THROUGH`
<a id="insn-00abda2c"></a> `00abda2c` | `48 8d 41 f8` | ldr x8,[x10, #0x18]! | `FALL_THROUGH`
<a id="insn-00abda30"></a> `00abda30` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00abda34"></a> `00abda34` | `97 01 80 52` | mov w23,#0xc | `FALL_THROUGH`
<a id="insn-00abda38"></a> `00abda38` | `fc cd ad 72` | movk w28,#0x6e6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00abda3c"></a> `00abda3c` | `39 01 40 b2` | orr x25,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00abda40"></a> `00abda40` | `34 89 88 52` | mov w20,#0x4449 | `FALL_THROUGH`
<a id="insn-00abda44"></a> `00abda44` | `55 01 1f f8` | stur x21,[x10, #-0x10] | `FALL_THROUGH`
<a id="insn-00abda48"></a> `00abda48` | `ea 07 00 f9` | str x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abda4c"></a> `00abda4c` | `48 05 00 f9` | str x8,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00abda50"></a> `00abda50` | `05 00 00 14` | b 0x00abda64 | `UNCONDITIONAL_JUMP`
<a id="insn-00abda54"></a> `00abda54` | `48 83 18 8b` | add x8,x26,x24, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00abda58"></a> `00abda58` | `68 87 00 f8` | str x8,[x27], #0x8 | `FALL_THROUGH`
<a id="insn-00abda5c"></a> `00abda5c` | `7b 12 00 f9` | str x27,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00abda60"></a> `00abda60` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00abda64"></a> `00abda64` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abda68"></a> `00abda68` | `f7 c3 00 39` | strb w23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abda6c"></a> `00abda6c` | `3c 03 00 b9` | str w28,[x25] | `FALL_THROUGH`
<a id="insn-00abda70"></a> `00abda70` | `34 0b 00 79` | strh w20,[x25, #0x4] | `FALL_THROUGH`
<a id="insn-00abda74"></a> `00abda74` | `ff df 00 39` | strb wzr,[sp, #0x37] | `FALL_THROUGH`
<a id="insn-00abda78"></a> `00abda78` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abda7c"></a> `00abda7c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abda80"></a> `00abda80` | `83 0d e6 97` | bl 0x0044108c | `UNCONDITIONAL_CALL`
<a id="insn-00abda84"></a> `00abda84` | `08 1c 40 f9` | ldr x8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abda88"></a> `00abda88` | `09 09 40 b9` | ldr w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abda8c"></a> `00abda8c` | `3f 19 00 71` | cmp w9,#0x6 | `FALL_THROUGH`
<a id="insn-00abda90"></a> `00abda90` | `e9 c3 40 39` | ldrb w9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abda94"></a> `00abda94` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00abda98"></a> `00abda98` | `16 55 41 a9` | ldp x22,x21,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abda9c"></a> `00abda9c` | `69 00 00 36` | tbz w9,#0x0,0x00abdaa8 | `CONDITIONAL_JUMP`
<a id="insn-00abdaa0"></a> `00abdaa0` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abdaa4"></a> `00abdaa4` | `03 69 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdaa8"></a> `00abdaa8` | `a8 02 16 cb` | sub x8,x21,x22 | `FALL_THROUGH`
<a id="insn-00abdaac"></a> `00abdaac` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00abdab0"></a> `00abdab0` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00abdab4"></a> `00abdab4` | `49 11 00 54` | b.ls 0x00abdcdc | `CONDITIONAL_JUMP`
<a id="insn-00abdab8"></a> `00abdab8` | `00 16 80 52` | mov w0,#0xb0 | `FALL_THROUGH`
<a id="insn-00abdabc"></a> `00abdabc` | `f5 68 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abdac0"></a> `00abdac0` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00abdac4"></a> `00abdac4` | `7b a2 40 a9` | ldp x27,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abdac8"></a> `00abdac8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abdacc"></a> `00abdacc` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdad0"></a> `00abdad0` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00abdad4"></a> `00abdad4` | `00 80 00 ad` | stp q0,q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abdad8"></a> `00abdad8` | `00 80 01 ad` | stp q0,q0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00abdadc"></a> `00abdadc` | `00 80 02 ad` | stp q0,q0,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00abdae0"></a> `00abdae0` | `00 80 03 ad` | stp q0,q0,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00abdae4"></a> `00abdae4` | `00 80 04 ad` | stp q0,q0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00abdae8"></a> `00abdae8` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00abdaec"></a> `00abdaec` | `82 00 00 54` | b.cs 0x00abdafc | `CONDITIONAL_JUMP`
<a id="insn-00abdaf0"></a> `00abdaf0` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdaf4"></a> `00abdaf4` | `75 87 00 f8` | str x21,[x27], #0x8 | `FALL_THROUGH`
<a id="insn-00abdaf8"></a> `00abdaf8` | `27 00 00 14` | b 0x00abdb94 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdafc"></a> `00abdafc` | `76 02 40 f9` | ldr x22,[x19] | `FALL_THROUGH`
<a id="insn-00abdb00"></a> `00abdb00` | `77 03 16 cb` | sub x23,x27,x22 | `FALL_THROUGH`
<a id="insn-00abdb04"></a> `00abdb04` | `fb fe 43 93` | asr x27,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00abdb08"></a> `00abdb08` | `69 07 00 91` | add x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00abdb0c"></a> `00abdb0c` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00abdb10"></a> `00abdb10` | `2a 21 00 b5` | cbnz x10,0x00abdf34 | `CONDITIONAL_JUMP`
<a id="insn-00abdb14"></a> `00abdb14` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00abdb18"></a> `00abdb18` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abdb1c"></a> `00abdb1c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00abdb20"></a> `00abdb20` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00abdb24"></a> `00abdb24` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00abdb28"></a> `00abdb28` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abdb2c"></a> `00abdb2c` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abdb30"></a> `00abdb30` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00abdb34"></a> `00abdb34` | `fc 00 00 b4` | cbz x28,0x00abdb50 | `CONDITIONAL_JUMP`
<a id="insn-00abdb38"></a> `00abdb38` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-00abdb3c"></a> `00abdb3c` | `68 21 00 b5` | cbnz x8,0x00abdf68 | `CONDITIONAL_JUMP`
<a id="insn-00abdb40"></a> `00abdb40` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-00abdb44"></a> `00abdb44` | `d3 68 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abdb48"></a> `00abdb48` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00abdb4c"></a> `00abdb4c` | `02 00 00 14` | b 0x00abdb54 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdb50"></a> `00abdb50` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00abdb54"></a> `00abdb54` | `1b 0f 1b 8b` | add x27,x24,x27, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00abdb58"></a> `00abdb58` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abdb5c"></a> `00abdb5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00abdb60"></a> `00abdb60` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00abdb64"></a> `00abdb64` | `1c 0f 1c 8b` | add x28,x24,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00abdb68"></a> `00abdb68` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdb6c"></a> `00abdb6c` | `75 87 00 f8` | str x21,[x27], #0x8 | `FALL_THROUGH`
<a id="insn-00abdb70"></a> `00abdb70` | `24 69 06 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00abdb74"></a> `00abdb74` | `78 6e 00 a9` | stp x24,x27,[x19] | `FALL_THROUGH`
<a id="insn-00abdb78"></a> `00abdb78` | `7c 0a 00 f9` | str x28,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00abdb7c"></a> `00abdb7c` | `76 00 00 b4` | cbz x22,0x00abdb88 | `CONDITIONAL_JUMP`
<a id="insn-00abdb80"></a> `00abdb80` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abdb84"></a> `00abdb84` | `cb 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdb88"></a> `00abdb88` | `3c 6d 8c 52` | mov w28,#0x6369 | `FALL_THROUGH`
<a id="insn-00abdb8c"></a> `00abdb8c` | `97 01 80 52` | mov w23,#0xc | `FALL_THROUGH`
<a id="insn-00abdb90"></a> `00abdb90` | `fc cd ad 72` | movk w28,#0x6e6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00abdb94"></a> `00abdb94` | `e1 1b 40 f9` | ldr x1,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdb98"></a> `00abdb98` | `7b 06 00 f9` | str x27,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abdb9c"></a> `00abdb9c` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdba0"></a> `00abdba0` | `81 00 00 b4` | cbz x1,0x00abdbb0 | `CONDITIONAL_JUMP`
<a id="insn-00abdba4"></a> `00abdba4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abdba8"></a> `00abdba8` | `91 b1 f6 97` | bl 0x0086a1ec | `UNCONDITIONAL_CALL`
<a id="insn-00abdbac"></a> `00abdbac` | `7b 06 40 f9` | ldr x27,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abdbb0"></a> `00abdbb0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00abdbb4"></a> `00abdbb4` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00abdbb8"></a> `00abdbb8` | `40 19 00 54` | b.eq 0x00abdee0 | `CONDITIONAL_JUMP`
<a id="insn-00abdbbc"></a> `00abdbbc` | `75 83 5f f8` | ldur x21,[x27, #-0x8] | `FALL_THROUGH`
<a id="insn-00abdbc0"></a> `00abdbc0` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abdbc4"></a> `00abdbc4` | `f7 c3 00 39` | strb w23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdbc8"></a> `00abdbc8` | `3c 03 00 b9` | str w28,[x25] | `FALL_THROUGH`
<a id="insn-00abdbcc"></a> `00abdbcc` | `34 0b 00 79` | strh w20,[x25, #0x4] | `FALL_THROUGH`
<a id="insn-00abdbd0"></a> `00abdbd0` | `ff df 00 39` | strb wzr,[sp, #0x37] | `FALL_THROUGH`
<a id="insn-00abdbd4"></a> `00abdbd4` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abdbd8"></a> `00abdbd8` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abdbdc"></a> `00abdbdc` | `2c 0d e6 97` | bl 0x0044108c | `UNCONDITIONAL_CALL`
<a id="insn-00abdbe0"></a> `00abdbe0` | `08 1c 40 f9` | ldr x8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abdbe4"></a> `00abdbe4` | `09 09 40 b9` | ldr w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abdbe8"></a> `00abdbe8` | `3f 19 00 71` | cmp w9,#0x6 | `FALL_THROUGH`
<a id="insn-00abdbec"></a> `00abdbec` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00abdbf0"></a> `00abdbf0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abdbf4"></a> `00abdbf4` | `08 79 7a f8` | ldr x8,[x8, x26, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abdbf8"></a> `00abdbf8` | `09 09 40 b9` | ldr w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abdbfc"></a> `00abdbfc` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-00abdc00"></a> `00abdc00` | `01 01 9f 9a` | csel x1,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00abdc04"></a> `00abdc04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abdc08"></a> `00abdc08` | `49 f7 ff 97` | bl 0x00abb92c | `UNCONDITIONAL_CALL`
<a id="insn-00abdc0c"></a> `00abdc0c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abdc10"></a> `00abdc10` | `68 00 00 36` | tbz w8,#0x0,0x00abdc1c | `CONDITIONAL_JUMP`
<a id="insn-00abdc14"></a> `00abdc14` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abdc18"></a> `00abdc18` | `a6 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdc1c"></a> `00abdc1c` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00abdc20"></a> `00abdc20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdc24"></a> `00abdc24` | `c0 16 00 54` | b.eq 0x00abdefc | `CONDITIONAL_JUMP`
<a id="insn-00abdc28"></a> `00abdc28` | `09 81 5f f8` | ldur x9,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00abdc2c"></a> `00abdc2c` | `7b 22 42 a9` | ldp x27,x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00abdc30"></a> `00abdc30` | `38 45 40 b9` | ldr w24,[x9, #0x44] | `FALL_THROUGH`
<a id="insn-00abdc34"></a> `00abdc34` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00abdc38"></a> `00abdc38` | `e3 f0 ff 54` | b.cc 0x00abda54 | `CONDITIONAL_JUMP`
<a id="insn-00abdc3c"></a> `00abdc3c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abdc40"></a> `00abdc40` | `35 01 40 f9` | ldr x21,[x9] | `FALL_THROUGH`
<a id="insn-00abdc44"></a> `00abdc44` | `76 03 15 cb` | sub x22,x27,x21 | `FALL_THROUGH`
<a id="insn-00abdc48"></a> `00abdc48` | `db fe 43 93` | asr x27,x22,#0x3 | `FALL_THROUGH`
<a id="insn-00abdc4c"></a> `00abdc4c` | `69 07 00 91` | add x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00abdc50"></a> `00abdc50` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00abdc54"></a> `00abdc54` | `2a 16 00 b5` | cbnz x10,0x00abdf18 | `CONDITIONAL_JUMP`
<a id="insn-00abdc58"></a> `00abdc58` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00abdc5c"></a> `00abdc5c` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abdc60"></a> `00abdc60` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00abdc64"></a> `00abdc64` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00abdc68"></a> `00abdc68` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00abdc6c"></a> `00abdc6c` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abdc70"></a> `00abdc70` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abdc74"></a> `00abdc74` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00abdc78"></a> `00abdc78` | `fc 00 00 b4` | cbz x28,0x00abdc94 | `CONDITIONAL_JUMP`
<a id="insn-00abdc7c"></a> `00abdc7c` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-00abdc80"></a> `00abdc80` | `88 16 00 b5` | cbnz x8,0x00abdf50 | `CONDITIONAL_JUMP`
<a id="insn-00abdc84"></a> `00abdc84` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-00abdc88"></a> `00abdc88` | `82 68 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abdc8c"></a> `00abdc8c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abdc90"></a> `00abdc90` | `02 00 00 14` | b 0x00abdc98 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdc94"></a> `00abdc94` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00abdc98"></a> `00abdc98` | `fb 0e 1b 8b` | add x27,x23,x27, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00abdc9c"></a> `00abdc9c` | `48 83 18 8b` | add x8,x26,x24, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00abdca0"></a> `00abdca0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abdca4"></a> `00abdca4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00abdca8"></a> `00abdca8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00abdcac"></a> `00abdcac` | `f8 0e 1c 8b` | add x24,x23,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00abdcb0"></a> `00abdcb0` | `68 87 00 f8` | str x8,[x27], #0x8 | `FALL_THROUGH`
<a id="insn-00abdcb4"></a> `00abdcb4` | `d3 68 06 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00abdcb8"></a> `00abdcb8` | `77 ee 01 a9` | stp x23,x27,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00abdcbc"></a> `00abdcbc` | `78 16 00 f9` | str x24,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00abdcc0"></a> `00abdcc0` | `75 00 00 b4` | cbz x21,0x00abdccc | `CONDITIONAL_JUMP`
<a id="insn-00abdcc4"></a> `00abdcc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abdcc8"></a> `00abdcc8` | `7a 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdccc"></a> `00abdccc` | `3c 6d 8c 52` | mov w28,#0x6369 | `FALL_THROUGH`
<a id="insn-00abdcd0"></a> `00abdcd0` | `97 01 80 52` | mov w23,#0xc | `FALL_THROUGH`
<a id="insn-00abdcd4"></a> `00abdcd4` | `fc cd ad 72` | movk w28,#0x6e6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00abdcd8"></a> `00abdcd8` | `61 ff ff 17` | b 0x00abda5c | `UNCONDITIONAL_JUMP`
<a id="insn-00abdcdc"></a> `00abdcdc` | `74 d6 41 a9` | ldp x20,x21,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00abdce0"></a> `00abdce0` | `a8 02 14 cb` | sub x8,x21,x20 | `FALL_THROUGH`
<a id="insn-00abdce4"></a> `00abdce4` | `16 fd 43 93` | asr x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00abdce8"></a> `00abdce8` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00abdcec"></a> `00abdcec` | `8b 01 00 54` | b.lt 0x00abdd1c | `CONDITIONAL_JUMP`
<a id="insn-00abdcf0"></a> `00abdcf0` | `f8 0e 00 d0` | adrp x24,0xc9b000 | `FALL_THROUGH`
<a id="insn-00abdcf4"></a> `00abdcf4` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00abdcf8"></a> `00abdcf8` | `18 93 42 f9` | ldr x24,[x24, #0x520] | `FALL_THROUGH`
<a id="insn-00abdcfc"></a> `00abdcfc` | `e0 f2 7d d3` | lsl x0,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00abdd00"></a> `00abdd00` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00abdd04"></a> `00abdd04` | `d3 72 06 94` | bl 0x00c5a850 | `UNCONDITIONAL_CALL`
<a id="insn-00abdd08"></a> `00abdd08` | `80 01 00 b5` | cbnz x0,0x00abdd38 | `CONDITIONAL_JUMP`
<a id="insn-00abdd0c"></a> `00abdd0c` | `e8 fe 41 d3` | lsr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00abdd10"></a> `00abdd10` | `ff 06 00 f1` | cmp x23,#0x1 | `FALL_THROUGH`
<a id="insn-00abdd14"></a> `00abdd14` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abdd18"></a> `00abdd18` | `28 ff ff 54` | b.hi 0x00abdcfc | `CONDITIONAL_JUMP`
<a id="insn-00abdd1c"></a> `00abdd1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdd20"></a> `00abdd20` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00abdd24"></a> `00abdd24` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00abdd28"></a> `00abdd28` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00abdd2c"></a> `00abdd2c` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00abdd30"></a> `00abdd30` | `b7 0c 00 94` | bl 0x00ac100c | `UNCONDITIONAL_CALL`
<a id="insn-00abdd34"></a> `00abdd34` | `0a 00 00 14` | b 0x00abdd5c | `UNCONDITIONAL_JUMP`
<a id="insn-00abdd38"></a> `00abdd38` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00abdd3c"></a> `00abdd3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdd40"></a> `00abdd40` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00abdd44"></a> `00abdd44` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00abdd48"></a> `00abdd48` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00abdd4c"></a> `00abdd4c` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00abdd50"></a> `00abdd50` | `af 0c 00 94` | bl 0x00ac100c | `UNCONDITIONAL_CALL`
<a id="insn-00abdd54"></a> `00abdd54` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abdd58"></a> `00abdd58` | `56 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdd5c"></a> `00abdd5c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abdd60"></a> `00abdd60` | `3e 2a e7 97` | bl 0x00488658 | `UNCONDITIONAL_CALL`
<a id="insn-00abdd64"></a> `00abdd64` | `f4 17 40 f9` | ldr x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abdd68"></a> `00abdd68` | `74 01 00 b4` | cbz x20,0x00abdd94 | `CONDITIONAL_JUMP`
<a id="insn-00abdd6c"></a> `00abdd6c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abdd70"></a> `00abdd70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abdd74"></a> `00abdd74` | `e3 57 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abdd78"></a> `00abdd78` | `e0 00 00 b5` | cbnz x0,0x00abdd94 | `CONDITIONAL_JUMP`
<a id="insn-00abdd7c"></a> `00abdd7c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abdd80"></a> `00abdd80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdd84"></a> `00abdd84` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abdd88"></a> `00abdd88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abdd8c"></a> `00abdd8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdd90"></a> `00abdd90` | `3c 68 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abdd94"></a> `00abdd94` | `29 bf ff f0` | adrp x9,0x2a4000 | `FALL_THROUGH`
<a id="insn-00abdd98"></a> `00abdd98` | `29 7d 30 91` | add x9,x9,#0xc1f | `FALL_THROUGH`
<a id="insn-00abdd9c"></a> `00abdd9c` | `48 03 80 52` | mov w8,#0x1a | `FALL_THROUGH`
<a id="insn-00abdda0"></a> `00abdda0` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abdda4"></a> `00abdda4` | `29 51 40 f8` | ldur x9,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-00abdda8"></a> `00abdda8` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abddac"></a> `00abddac` | `ff fb 00 39` | strb wzr,[sp, #0x3e] | `FALL_THROUGH`
<a id="insn-00abddb0"></a> `00abddb0` | `ea 13 03 f8` | stur x10,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abddb4"></a> `00abddb4` | `e9 63 03 f8` | stur x9,[sp, #0x36] | `FALL_THROUGH`
<a id="insn-00abddb8"></a> `00abddb8` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abddbc"></a> `00abddbc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abddc0"></a> `00abddc0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00abddc4"></a> `00abddc4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abddc8"></a> `00abddc8` | `c9 4c 01 94` | bl 0x00b110ec | `UNCONDITIONAL_CALL`
<a id="insn-00abddcc"></a> `00abddcc` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abddd0"></a> `00abddd0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abddd4"></a> `00abddd4` | `68 00 00 36` | tbz w8,#0x0,0x00abdde0 | `CONDITIONAL_JUMP`
<a id="insn-00abddd8"></a> `00abddd8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abdddc"></a> `00abdddc` | `35 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdde0"></a> `00abdde0` | `f4 01 00 36` | tbz w20,#0x0,0x00abde1c | `CONDITIONAL_JUMP`
<a id="insn-00abdde4"></a> `00abdde4` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00abdde8"></a> `00abdde8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abddec"></a> `00abddec` | `40 01 00 54` | b.eq 0x00abde14 | `CONDITIONAL_JUMP`
<a id="insn-00abddf0"></a> `00abddf0` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00abddf4"></a> `00abddf4` | `00 79 74 f8` | ldr x0,[x8, x20, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abddf8"></a> `00abddf8` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abddfc"></a> `00abddfc` | `86 fa ff 97` | bl 0x00abc814 | `UNCONDITIONAL_CALL`
<a id="insn-00abde00"></a> `00abde00` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00abde04"></a> `00abde04` | `94 06 00 91` | add x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00abde08"></a> `00abde08` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abde0c"></a> `00abde0c` | `9f 0e 89 eb` | cmp x20,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abde10"></a> `00abde10` | `23 ff ff 54` | b.cc 0x00abddf4 | `CONDITIONAL_JUMP`
<a id="insn-00abde14"></a> `00abde14` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abde18"></a> `00abde18` | `10 2a e7 97` | bl 0x00488658 | `UNCONDITIONAL_CALL`
<a id="insn-00abde1c"></a> `00abde1c` | `e8 0e 00 b0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abde20"></a> `00abde20` | `f5 0e 00 b0` | adrp x21,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abde24"></a> `00abde24` | `f4 23 01 91` | add x20,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00abde28"></a> `00abde28` | `08 d9 45 f9` | ldr x8,[x8, #0xbb0] | `FALL_THROUGH`
<a id="insn-00abde2c"></a> `00abde2c` | `b5 de 45 f9` | ldr x21,[x21, #0xbb8] | `FALL_THROUGH`
<a id="insn-00abde30"></a> `00abde30` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00abde34"></a> `00abde34` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00abde38"></a> `00abde38` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abde3c"></a> `00abde3c` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abde40"></a> `00abde40` | `e9 4b 00 f9` | str x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abde44"></a> `00abde44` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00abde48"></a> `00abde48` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00abde4c"></a> `00abde4c` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abde50"></a> `00abde50` | `e8 0e 00 b0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abde54"></a> `00abde54` | `08 e1 45 f9` | ldr x8,[x8, #0xbc0] | `FALL_THROUGH`
<a id="insn-00abde58"></a> `00abde58` | `e9 63 43 39` | ldrb w9,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00abde5c"></a> `00abde5c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abde60"></a> `00abde60` | `e8 4f 00 f9` | str x8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00abde64"></a> `00abde64` | `69 00 00 36` | tbz w9,#0x0,0x00abde70 | `CONDITIONAL_JUMP`
<a id="insn-00abde68"></a> `00abde68` | `e0 77 40 f9` | ldr x0,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00abde6c"></a> `00abde6c` | `11 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde70"></a> `00abde70` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00abde74"></a> `00abde74` | `4b 68 06 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde78"></a> `00abde78` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abde7c"></a> `00abde7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abde80"></a> `00abde80` | `4c 68 06 94` | bl 0x00c57fb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde84"></a> `00abde84` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-00abde88"></a> `00abde88` | `4e 68 06 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde8c"></a> `00abde8c` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00abde90"></a> `00abde90` | `68 00 00 36` | tbz w8,#0x0,0x00abde9c | `CONDITIONAL_JUMP`
<a id="insn-00abde94"></a> `00abde94` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00abde98"></a> `00abde98` | `06 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde9c"></a> `00abde9c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abdea0"></a> `00abdea0` | `60 00 00 b4` | cbz x0,0x00abdeac | `CONDITIONAL_JUMP`
<a id="insn-00abdea4"></a> `00abdea4` | `e0 2f 00 f9` | str x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abdea8"></a> `00abdea8` | `02 68 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdeac"></a> `00abdeac` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdeb0"></a> `00abdeb0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdeb4"></a> `00abdeb4` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdeb8"></a> `00abdeb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdebc"></a> `00abdebc` | `c1 0c 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdec0"></a> `00abdec0` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00abdec4"></a> `00abdec4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abdec8"></a> `00abdec8` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abdecc"></a> `00abdecc` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abded0"></a> `00abded0` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abded4"></a> `00abded4` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abded8"></a> `00abded8` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00abdedc"></a> `00abdedc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abdee0"></a> `00abdee0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdee4"></a> `00abdee4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdee8"></a> `00abdee8` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdeec"></a> `00abdeec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdef0"></a> `00abdef0` | `21 0b 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdef4"></a> `00abdef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abdef8"></a> `00abdef8` | `3b 0c 00 94` | bl 0x00ac0fe4 | `UNCONDITIONAL_CALL`
<a id="insn-00abdefc"></a> `00abdefc` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdf00"></a> `00abdf00` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdf04"></a> `00abdf04` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdf08"></a> `00abdf08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdf0c"></a> `00abdf0c` | `41 0a 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdf10"></a> `00abdf10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abdf14"></a> `00abdf14` | `34 0c 00 94` | bl 0x00ac0fe4 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf18"></a> `00abdf18` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdf1c"></a> `00abdf1c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdf20"></a> `00abdf20` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdf24"></a> `00abdf24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdf28"></a> `00abdf28` | `61 09 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdf2c"></a> `00abdf2c` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abdf30"></a> `00abdf30` | `32 0c 00 94` | bl 0x00ac0ff8 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf34"></a> `00abdf34` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdf38"></a> `00abdf38` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdf3c"></a> `00abdf3c` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdf40"></a> `00abdf40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdf44"></a> `00abdf44` | `81 08 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdf48"></a> `00abdf48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abdf4c"></a> `00abdf4c` | `21 0c 00 94` | bl 0x00ac0fd0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf50"></a> `00abdf50` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdf54"></a> `00abdf54` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdf58"></a> `00abdf58` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdf5c"></a> `00abdf5c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdf60"></a> `00abdf60` | `a1 07 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdf64"></a> `00abdf64` | `d7 0b e6 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-00abdf68"></a> `00abdf68` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00abdf6c"></a> `00abdf6c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abdf70"></a> `00abdf70` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abdf74"></a> `00abdf74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abdf78"></a> `00abdf78` | `e1 06 00 54` | b.ne 0x00abe054 | `CONDITIONAL_JUMP`
<a id="insn-00abdf7c"></a> `00abdf7c` | `d1 0b e6 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-00abe054"></a> `00abe054` | `a3 67 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abd8ec`](#insn-00abd8ec) 範囲 `[['00abd8ec', '00abd90f']]`
  - `FALL_THROUGH` [`00abd90c`](#insn-00abd90c) → [`00abd910`](#insn-00abd910)
- ブロック [`00abd910`](#insn-00abd910) 範囲 `[['00abd910', '00abd933']]`
  - `FALL_THROUGH` [`00abd930`](#insn-00abd930) → [`00abd934`](#insn-00abd934)
- ブロック [`00abd934`](#insn-00abd934) 範囲 `[['00abd934', '00abd94f']]`
  - `FALL_THROUGH` [`00abd94c`](#insn-00abd94c) → [`00abd950`](#insn-00abd950)
- ブロック [`00abd950`](#insn-00abd950) 範囲 `[['00abd950', '00abd977']]`
  - `CONDITIONAL_JUMP` [`00abd974`](#insn-00abd974) → [`00abd980`](#insn-00abd980)
  - `FALL_THROUGH` [`00abd974`](#insn-00abd974) → [`00abd978`](#insn-00abd978)
- ブロック [`00abd978`](#insn-00abd978) 範囲 `[['00abd978', '00abd97f']]`
  - `FALL_THROUGH` [`00abd97c`](#insn-00abd97c) → [`00abd980`](#insn-00abd980)
- ブロック [`00abd980`](#insn-00abd980) 範囲 `[['00abd980', '00abd983']]`
  - `CONDITIONAL_JUMP` [`00abd980`](#insn-00abd980) → [`00abdd94`](#insn-00abdd94)
  - `FALL_THROUGH` [`00abd980`](#insn-00abd980) → [`00abd984`](#insn-00abd984)
- ブロック [`00abd984`](#insn-00abd984) 範囲 `[['00abd984', '00abd9af']]`
  - `CONDITIONAL_JUMP` [`00abd9ac`](#insn-00abd9ac) → [`00abd9d8`](#insn-00abd9d8)
  - `FALL_THROUGH` [`00abd9ac`](#insn-00abd9ac) → [`00abd9b0`](#insn-00abd9b0)
- ブロック [`00abd9b0`](#insn-00abd9b0) 範囲 `[['00abd9b0', '00abd9bf']]`
  - `CONDITIONAL_JUMP` [`00abd9bc`](#insn-00abd9bc) → [`00abd9d8`](#insn-00abd9d8)
  - `FALL_THROUGH` [`00abd9bc`](#insn-00abd9bc) → [`00abd9c0`](#insn-00abd9c0)
- ブロック [`00abd9c0`](#insn-00abd9c0) 範囲 `[['00abd9c0', '00abd9cf']]`
  - `FALL_THROUGH` [`00abd9cc`](#insn-00abd9cc) → [`00abd9d0`](#insn-00abd9d0)
- ブロック [`00abd9d0`](#insn-00abd9d0) 範囲 `[['00abd9d0', '00abd9d7']]`
  - `FALL_THROUGH` [`00abd9d4`](#insn-00abd9d4) → [`00abd9d8`](#insn-00abd9d8)
- ブロック [`00abd9d8`](#insn-00abd9d8) 範囲 `[['00abd9d8', '00abd9df']]`
  - `CONDITIONAL_JUMP` [`00abd9dc`](#insn-00abd9dc) → [`00abd9e8`](#insn-00abd9e8)
  - `FALL_THROUGH` [`00abd9dc`](#insn-00abd9dc) → [`00abd9e0`](#insn-00abd9e0)
- ブロック [`00abd9e0`](#insn-00abd9e0) 範囲 `[['00abd9e0', '00abd9e3']]`
  - `FALL_THROUGH` [`00abd9e0`](#insn-00abd9e0) → [`00abd9e4`](#insn-00abd9e4)
- ブロック [`00abd9e4`](#insn-00abd9e4) 範囲 `[['00abd9e4', '00abd9e7']]`
  - `FALL_THROUGH` [`00abd9e4`](#insn-00abd9e4) → [`00abd9e8`](#insn-00abd9e8)
- ブロック [`00abd9e8`](#insn-00abd9e8) 範囲 `[['00abd9e8', '00abd9f3']]`
  - `CONDITIONAL_JUMP` [`00abd9f0`](#insn-00abd9f0) → [`00abda20`](#insn-00abda20)
  - `FALL_THROUGH` [`00abd9f0`](#insn-00abd9f0) → [`00abd9f4`](#insn-00abd9f4)
- ブロック [`00abd9f4`](#insn-00abd9f4) 範囲 `[['00abd9f4', '00abd9fb']]`
  - `UNCONDITIONAL_JUMP` [`00abd9f8`](#insn-00abd9f8) → [`00abda08`](#insn-00abda08)
- ブロック [`00abd9fc`](#insn-00abd9fc) 範囲 `[['00abd9fc', '00abda07']]`
  - `CONDITIONAL_JUMP` [`00abda04`](#insn-00abda04) → [`00abda20`](#insn-00abda20)
  - `FALL_THROUGH` [`00abda04`](#insn-00abda04) → [`00abda08`](#insn-00abda08)
- ブロック [`00abda08`](#insn-00abda08) 範囲 `[['00abda08', '00abda13']]`
  - `CONDITIONAL_JUMP` [`00abda10`](#insn-00abda10) → [`00abd9fc`](#insn-00abd9fc)
  - `FALL_THROUGH` [`00abda10`](#insn-00abda10) → [`00abda14`](#insn-00abda14)
- ブロック [`00abda14`](#insn-00abda14) 範囲 `[['00abda14', '00abda1f']]`
  - `UNCONDITIONAL_JUMP` [`00abda1c`](#insn-00abda1c) → [`00abd9fc`](#insn-00abd9fc)
- ブロック [`00abda20`](#insn-00abda20) 範囲 `[['00abda20', '00abda53']]`
  - `UNCONDITIONAL_JUMP` [`00abda50`](#insn-00abda50) → [`00abda64`](#insn-00abda64)
- ブロック [`00abda54`](#insn-00abda54) 範囲 `[['00abda54', '00abda57']]`
  - `FALL_THROUGH` [`00abda54`](#insn-00abda54) → [`00abda58`](#insn-00abda58)
- ブロック [`00abda58`](#insn-00abda58) 範囲 `[['00abda58', '00abda5b']]`
  - `FALL_THROUGH` [`00abda58`](#insn-00abda58) → [`00abda5c`](#insn-00abda5c)
- ブロック [`00abda5c`](#insn-00abda5c) 範囲 `[['00abda5c', '00abda63']]`
  - `FALL_THROUGH` [`00abda60`](#insn-00abda60) → [`00abda64`](#insn-00abda64)
- ブロック [`00abda64`](#insn-00abda64) 範囲 `[['00abda64', '00abda73']]`
  - `FALL_THROUGH` [`00abda70`](#insn-00abda70) → [`00abda74`](#insn-00abda74)
- ブロック [`00abda74`](#insn-00abda74) 範囲 `[['00abda74', '00abda77']]`
  - `FALL_THROUGH` [`00abda74`](#insn-00abda74) → [`00abda78`](#insn-00abda78)
- ブロック [`00abda78`](#insn-00abda78) 範囲 `[['00abda78', '00abda9f']]`
  - `CONDITIONAL_JUMP` [`00abda9c`](#insn-00abda9c) → [`00abdaa8`](#insn-00abdaa8)
  - `FALL_THROUGH` [`00abda9c`](#insn-00abda9c) → [`00abdaa0`](#insn-00abdaa0)
- ブロック [`00abdaa0`](#insn-00abdaa0) 範囲 `[['00abdaa0', '00abdaa7']]`
  - `FALL_THROUGH` [`00abdaa4`](#insn-00abdaa4) → [`00abdaa8`](#insn-00abdaa8)
- ブロック [`00abdaa8`](#insn-00abdaa8) 範囲 `[['00abdaa8', '00abdab7']]`
  - `CONDITIONAL_JUMP` [`00abdab4`](#insn-00abdab4) → [`00abdcdc`](#insn-00abdcdc)
  - `FALL_THROUGH` [`00abdab4`](#insn-00abdab4) → [`00abdab8`](#insn-00abdab8)
- ブロック [`00abdab8`](#insn-00abdab8) 範囲 `[['00abdab8', '00abdabb']]`
  - `FALL_THROUGH` [`00abdab8`](#insn-00abdab8) → [`00abdabc`](#insn-00abdabc)
- ブロック [`00abdabc`](#insn-00abdabc) 範囲 `[['00abdabc', '00abdaef']]`
  - `CONDITIONAL_JUMP` [`00abdaec`](#insn-00abdaec) → [`00abdafc`](#insn-00abdafc)
  - `FALL_THROUGH` [`00abdaec`](#insn-00abdaec) → [`00abdaf0`](#insn-00abdaf0)
- ブロック [`00abdaf0`](#insn-00abdaf0) 範囲 `[['00abdaf0', '00abdafb']]`
  - `UNCONDITIONAL_JUMP` [`00abdaf8`](#insn-00abdaf8) → [`00abdb94`](#insn-00abdb94)
- ブロック [`00abdafc`](#insn-00abdafc) 範囲 `[['00abdafc', '00abdb03']]`
  - `FALL_THROUGH` [`00abdb00`](#insn-00abdb00) → [`00abdb04`](#insn-00abdb04)
- ブロック [`00abdb04`](#insn-00abdb04) 範囲 `[['00abdb04', '00abdb07']]`
  - `FALL_THROUGH` [`00abdb04`](#insn-00abdb04) → [`00abdb08`](#insn-00abdb08)
- ブロック [`00abdb08`](#insn-00abdb08) 範囲 `[['00abdb08', '00abdb13']]`
  - `CONDITIONAL_JUMP` [`00abdb10`](#insn-00abdb10) → [`00abdf34`](#insn-00abdf34)
  - `FALL_THROUGH` [`00abdb10`](#insn-00abdb10) → [`00abdb14`](#insn-00abdb14)
- ブロック [`00abdb14`](#insn-00abdb14) 範囲 `[['00abdb14', '00abdb37']]`
  - `CONDITIONAL_JUMP` [`00abdb34`](#insn-00abdb34) → [`00abdb50`](#insn-00abdb50)
  - `FALL_THROUGH` [`00abdb34`](#insn-00abdb34) → [`00abdb38`](#insn-00abdb38)
- ブロック [`00abdb38`](#insn-00abdb38) 範囲 `[['00abdb38', '00abdb3f']]`
  - `CONDITIONAL_JUMP` [`00abdb3c`](#insn-00abdb3c) → [`00abdf68`](#insn-00abdf68)
  - `FALL_THROUGH` [`00abdb3c`](#insn-00abdb3c) → [`00abdb40`](#insn-00abdb40)
- ブロック [`00abdb40`](#insn-00abdb40) 範囲 `[['00abdb40', '00abdb4f']]`
  - `UNCONDITIONAL_JUMP` [`00abdb4c`](#insn-00abdb4c) → [`00abdb54`](#insn-00abdb54)
- ブロック [`00abdb50`](#insn-00abdb50) 範囲 `[['00abdb50', '00abdb53']]`
  - `FALL_THROUGH` [`00abdb50`](#insn-00abdb50) → [`00abdb54`](#insn-00abdb54)
- ブロック [`00abdb54`](#insn-00abdb54) 範囲 `[['00abdb54', '00abdb7f']]`
  - `CONDITIONAL_JUMP` [`00abdb7c`](#insn-00abdb7c) → [`00abdb88`](#insn-00abdb88)
  - `FALL_THROUGH` [`00abdb7c`](#insn-00abdb7c) → [`00abdb80`](#insn-00abdb80)
- ブロック [`00abdb80`](#insn-00abdb80) 範囲 `[['00abdb80', '00abdb87']]`
  - `FALL_THROUGH` [`00abdb84`](#insn-00abdb84) → [`00abdb88`](#insn-00abdb88)
- ブロック [`00abdb88`](#insn-00abdb88) 範囲 `[['00abdb88', '00abdb93']]`
  - `FALL_THROUGH` [`00abdb90`](#insn-00abdb90) → [`00abdb94`](#insn-00abdb94)
- ブロック [`00abdb94`](#insn-00abdb94) 範囲 `[['00abdb94', '00abdba3']]`
  - `CONDITIONAL_JUMP` [`00abdba0`](#insn-00abdba0) → [`00abdbb0`](#insn-00abdbb0)
  - `FALL_THROUGH` [`00abdba0`](#insn-00abdba0) → [`00abdba4`](#insn-00abdba4)
- ブロック [`00abdba4`](#insn-00abdba4) 範囲 `[['00abdba4', '00abdbaf']]`
  - `FALL_THROUGH` [`00abdbac`](#insn-00abdbac) → [`00abdbb0`](#insn-00abdbb0)
- ブロック [`00abdbb0`](#insn-00abdbb0) 範囲 `[['00abdbb0', '00abdbbb']]`
  - `CONDITIONAL_JUMP` [`00abdbb8`](#insn-00abdbb8) → [`00abdee0`](#insn-00abdee0)
  - `FALL_THROUGH` [`00abdbb8`](#insn-00abdbb8) → [`00abdbbc`](#insn-00abdbbc)
- ブロック [`00abdbbc`](#insn-00abdbbc) 範囲 `[['00abdbbc', '00abdc13']]`
  - `CONDITIONAL_JUMP` [`00abdc10`](#insn-00abdc10) → [`00abdc1c`](#insn-00abdc1c)
  - `FALL_THROUGH` [`00abdc10`](#insn-00abdc10) → [`00abdc14`](#insn-00abdc14)
- ブロック [`00abdc14`](#insn-00abdc14) 範囲 `[['00abdc14', '00abdc1b']]`
  - `FALL_THROUGH` [`00abdc18`](#insn-00abdc18) → [`00abdc1c`](#insn-00abdc1c)
- ブロック [`00abdc1c`](#insn-00abdc1c) 範囲 `[['00abdc1c', '00abdc27']]`
  - `CONDITIONAL_JUMP` [`00abdc24`](#insn-00abdc24) → [`00abdefc`](#insn-00abdefc)
  - `FALL_THROUGH` [`00abdc24`](#insn-00abdc24) → [`00abdc28`](#insn-00abdc28)
- ブロック [`00abdc28`](#insn-00abdc28) 範囲 `[['00abdc28', '00abdc3b']]`
  - `CONDITIONAL_JUMP` [`00abdc38`](#insn-00abdc38) → [`00abda54`](#insn-00abda54)
  - `FALL_THROUGH` [`00abdc38`](#insn-00abdc38) → [`00abdc3c`](#insn-00abdc3c)
- ブロック [`00abdc3c`](#insn-00abdc3c) 範囲 `[['00abdc3c', '00abdc57']]`
  - `CONDITIONAL_JUMP` [`00abdc54`](#insn-00abdc54) → [`00abdf18`](#insn-00abdf18)
  - `FALL_THROUGH` [`00abdc54`](#insn-00abdc54) → [`00abdc58`](#insn-00abdc58)
- ブロック [`00abdc58`](#insn-00abdc58) 範囲 `[['00abdc58', '00abdc7b']]`
  - `CONDITIONAL_JUMP` [`00abdc78`](#insn-00abdc78) → [`00abdc94`](#insn-00abdc94)
  - `FALL_THROUGH` [`00abdc78`](#insn-00abdc78) → [`00abdc7c`](#insn-00abdc7c)
- ブロック [`00abdc7c`](#insn-00abdc7c) 範囲 `[['00abdc7c', '00abdc83']]`
  - `CONDITIONAL_JUMP` [`00abdc80`](#insn-00abdc80) → [`00abdf50`](#insn-00abdf50)
  - `FALL_THROUGH` [`00abdc80`](#insn-00abdc80) → [`00abdc84`](#insn-00abdc84)
- ブロック [`00abdc84`](#insn-00abdc84) 範囲 `[['00abdc84', '00abdc93']]`
  - `UNCONDITIONAL_JUMP` [`00abdc90`](#insn-00abdc90) → [`00abdc98`](#insn-00abdc98)
- ブロック [`00abdc94`](#insn-00abdc94) 範囲 `[['00abdc94', '00abdc97']]`
  - `FALL_THROUGH` [`00abdc94`](#insn-00abdc94) → [`00abdc98`](#insn-00abdc98)
- ブロック [`00abdc98`](#insn-00abdc98) 範囲 `[['00abdc98', '00abdcc3']]`
  - `CONDITIONAL_JUMP` [`00abdcc0`](#insn-00abdcc0) → [`00abdccc`](#insn-00abdccc)
  - `FALL_THROUGH` [`00abdcc0`](#insn-00abdcc0) → [`00abdcc4`](#insn-00abdcc4)
- ブロック [`00abdcc4`](#insn-00abdcc4) 範囲 `[['00abdcc4', '00abdccb']]`
  - `FALL_THROUGH` [`00abdcc8`](#insn-00abdcc8) → [`00abdccc`](#insn-00abdccc)
- ブロック [`00abdccc`](#insn-00abdccc) 範囲 `[['00abdccc', '00abdcdb']]`
  - `UNCONDITIONAL_JUMP` [`00abdcd8`](#insn-00abdcd8) → [`00abda5c`](#insn-00abda5c)
- ブロック [`00abdcdc`](#insn-00abdcdc) 範囲 `[['00abdcdc', '00abdcef']]`
  - `CONDITIONAL_JUMP` [`00abdcec`](#insn-00abdcec) → [`00abdd1c`](#insn-00abdd1c)
  - `FALL_THROUGH` [`00abdcec`](#insn-00abdcec) → [`00abdcf0`](#insn-00abdcf0)
- ブロック [`00abdcf0`](#insn-00abdcf0) 範囲 `[['00abdcf0', '00abdcfb']]`
  - `FALL_THROUGH` [`00abdcf8`](#insn-00abdcf8) → [`00abdcfc`](#insn-00abdcfc)
- ブロック [`00abdcfc`](#insn-00abdcfc) 範囲 `[['00abdcfc', '00abdd0b']]`
  - `CONDITIONAL_JUMP` [`00abdd08`](#insn-00abdd08) → [`00abdd38`](#insn-00abdd38)
  - `FALL_THROUGH` [`00abdd08`](#insn-00abdd08) → [`00abdd0c`](#insn-00abdd0c)
- ブロック [`00abdd0c`](#insn-00abdd0c) 範囲 `[['00abdd0c', '00abdd1b']]`
  - `CONDITIONAL_JUMP` [`00abdd18`](#insn-00abdd18) → [`00abdcfc`](#insn-00abdcfc)
  - `FALL_THROUGH` [`00abdd18`](#insn-00abdd18) → [`00abdd1c`](#insn-00abdd1c)
- ブロック [`00abdd1c`](#insn-00abdd1c) 範囲 `[['00abdd1c', '00abdd37']]`
  - `UNCONDITIONAL_JUMP` [`00abdd34`](#insn-00abdd34) → [`00abdd5c`](#insn-00abdd5c)
- ブロック [`00abdd38`](#insn-00abdd38) 範囲 `[['00abdd38', '00abdd5b']]`
  - `FALL_THROUGH` [`00abdd58`](#insn-00abdd58) → [`00abdd5c`](#insn-00abdd5c)
- ブロック [`00abdd5c`](#insn-00abdd5c) 範囲 `[['00abdd5c', '00abdd6b']]`
  - `CONDITIONAL_JUMP` [`00abdd68`](#insn-00abdd68) → [`00abdd94`](#insn-00abdd94)
  - `FALL_THROUGH` [`00abdd68`](#insn-00abdd68) → [`00abdd6c`](#insn-00abdd6c)
- ブロック [`00abdd6c`](#insn-00abdd6c) 範囲 `[['00abdd6c', '00abdd7b']]`
  - `CONDITIONAL_JUMP` [`00abdd78`](#insn-00abdd78) → [`00abdd94`](#insn-00abdd94)
  - `FALL_THROUGH` [`00abdd78`](#insn-00abdd78) → [`00abdd7c`](#insn-00abdd7c)
- ブロック [`00abdd7c`](#insn-00abdd7c) 範囲 `[['00abdd7c', '00abdd93']]`
  - `FALL_THROUGH` [`00abdd90`](#insn-00abdd90) → [`00abdd94`](#insn-00abdd94)
- ブロック [`00abdd94`](#insn-00abdd94) 範囲 `[['00abdd94', '00abddd7']]`
  - `CONDITIONAL_JUMP` [`00abddd4`](#insn-00abddd4) → [`00abdde0`](#insn-00abdde0)
  - `FALL_THROUGH` [`00abddd4`](#insn-00abddd4) → [`00abddd8`](#insn-00abddd8)
- ブロック [`00abddd8`](#insn-00abddd8) 範囲 `[['00abddd8', '00abdddf']]`
  - `FALL_THROUGH` [`00abdddc`](#insn-00abdddc) → [`00abdde0`](#insn-00abdde0)
- ブロック [`00abdde0`](#insn-00abdde0) 範囲 `[['00abdde0', '00abdde3']]`
  - `CONDITIONAL_JUMP` [`00abdde0`](#insn-00abdde0) → [`00abde1c`](#insn-00abde1c)
  - `FALL_THROUGH` [`00abdde0`](#insn-00abdde0) → [`00abdde4`](#insn-00abdde4)
- ブロック [`00abdde4`](#insn-00abdde4) 範囲 `[['00abdde4', '00abddef']]`
  - `CONDITIONAL_JUMP` [`00abddec`](#insn-00abddec) → [`00abde14`](#insn-00abde14)
  - `FALL_THROUGH` [`00abddec`](#insn-00abddec) → [`00abddf0`](#insn-00abddf0)
- ブロック [`00abddf0`](#insn-00abddf0) 範囲 `[['00abddf0', '00abddf3']]`
  - `FALL_THROUGH` [`00abddf0`](#insn-00abddf0) → [`00abddf4`](#insn-00abddf4)
- ブロック [`00abddf4`](#insn-00abddf4) 範囲 `[['00abddf4', '00abde13']]`
  - `CONDITIONAL_JUMP` [`00abde10`](#insn-00abde10) → [`00abddf4`](#insn-00abddf4)
  - `FALL_THROUGH` [`00abde10`](#insn-00abde10) → [`00abde14`](#insn-00abde14)
- ブロック [`00abde14`](#insn-00abde14) 範囲 `[['00abde14', '00abde1b']]`
  - `FALL_THROUGH` [`00abde18`](#insn-00abde18) → [`00abde1c`](#insn-00abde1c)
- ブロック [`00abde1c`](#insn-00abde1c) 範囲 `[['00abde1c', '00abde57']]`
  - `FALL_THROUGH` [`00abde54`](#insn-00abde54) → [`00abde58`](#insn-00abde58)
- ブロック [`00abde58`](#insn-00abde58) 範囲 `[['00abde58', '00abde67']]`
  - `CONDITIONAL_JUMP` [`00abde64`](#insn-00abde64) → [`00abde70`](#insn-00abde70)
  - `FALL_THROUGH` [`00abde64`](#insn-00abde64) → [`00abde68`](#insn-00abde68)
- ブロック [`00abde68`](#insn-00abde68) 範囲 `[['00abde68', '00abde6f']]`
  - `FALL_THROUGH` [`00abde6c`](#insn-00abde6c) → [`00abde70`](#insn-00abde70)
- ブロック [`00abde70`](#insn-00abde70) 範囲 `[['00abde70', '00abde93']]`
  - `CONDITIONAL_JUMP` [`00abde90`](#insn-00abde90) → [`00abde9c`](#insn-00abde9c)
  - `FALL_THROUGH` [`00abde90`](#insn-00abde90) → [`00abde94`](#insn-00abde94)
- ブロック [`00abde94`](#insn-00abde94) 範囲 `[['00abde94', '00abde9b']]`
  - `FALL_THROUGH` [`00abde98`](#insn-00abde98) → [`00abde9c`](#insn-00abde9c)
- ブロック [`00abde9c`](#insn-00abde9c) 範囲 `[['00abde9c', '00abdea3']]`
  - `CONDITIONAL_JUMP` [`00abdea0`](#insn-00abdea0) → [`00abdeac`](#insn-00abdeac)
  - `FALL_THROUGH` [`00abdea0`](#insn-00abdea0) → [`00abdea4`](#insn-00abdea4)
- ブロック [`00abdea4`](#insn-00abdea4) 範囲 `[['00abdea4', '00abdeab']]`
  - `FALL_THROUGH` [`00abdea8`](#insn-00abdea8) → [`00abdeac`](#insn-00abdeac)
- ブロック [`00abdeac`](#insn-00abdeac) 範囲 `[['00abdeac', '00abdebf']]`
  - `CONDITIONAL_JUMP` [`00abdebc`](#insn-00abdebc) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdebc`](#insn-00abdebc) → [`00abdec0`](#insn-00abdec0)
- ブロック [`00abdec0`](#insn-00abdec0) 範囲 `[['00abdec0', '00abdec7']]`
  - `FALL_THROUGH` [`00abdec4`](#insn-00abdec4) → [`00abdec8`](#insn-00abdec8)
- ブロック [`00abdec8`](#insn-00abdec8) 範囲 `[['00abdec8', '00abdedf']]`
- ブロック [`00abdee0`](#insn-00abdee0) 範囲 `[['00abdee0', '00abdef3']]`
  - `CONDITIONAL_JUMP` [`00abdef0`](#insn-00abdef0) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdef0`](#insn-00abdef0) → [`00abdef4`](#insn-00abdef4)
- ブロック [`00abdef4`](#insn-00abdef4) 範囲 `[['00abdef4', '00abdefb']]`
  - `FALL_THROUGH` [`00abdef8`](#insn-00abdef8) → [`00abdefc`](#insn-00abdefc)
- ブロック [`00abdefc`](#insn-00abdefc) 範囲 `[['00abdefc', '00abdf0f']]`
  - `CONDITIONAL_JUMP` [`00abdf0c`](#insn-00abdf0c) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdf0c`](#insn-00abdf0c) → [`00abdf10`](#insn-00abdf10)
- ブロック [`00abdf10`](#insn-00abdf10) 範囲 `[['00abdf10', '00abdf17']]`
  - `FALL_THROUGH` [`00abdf14`](#insn-00abdf14) → [`00abdf18`](#insn-00abdf18)
- ブロック [`00abdf18`](#insn-00abdf18) 範囲 `[['00abdf18', '00abdf2b']]`
  - `CONDITIONAL_JUMP` [`00abdf28`](#insn-00abdf28) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdf28`](#insn-00abdf28) → [`00abdf2c`](#insn-00abdf2c)
- ブロック [`00abdf2c`](#insn-00abdf2c) 範囲 `[['00abdf2c', '00abdf33']]`
  - `FALL_THROUGH` [`00abdf30`](#insn-00abdf30) → [`00abdf34`](#insn-00abdf34)
- ブロック [`00abdf34`](#insn-00abdf34) 範囲 `[['00abdf34', '00abdf3f']]`
  - `FALL_THROUGH` [`00abdf3c`](#insn-00abdf3c) → [`00abdf40`](#insn-00abdf40)
- ブロック [`00abdf40`](#insn-00abdf40) 範囲 `[['00abdf40', '00abdf47']]`
  - `CONDITIONAL_JUMP` [`00abdf44`](#insn-00abdf44) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdf44`](#insn-00abdf44) → [`00abdf48`](#insn-00abdf48)
- ブロック [`00abdf48`](#insn-00abdf48) 範囲 `[['00abdf48', '00abdf4f']]`
  - `FALL_THROUGH` [`00abdf4c`](#insn-00abdf4c) → [`00abdf50`](#insn-00abdf50)
- ブロック [`00abdf50`](#insn-00abdf50) 範囲 `[['00abdf50', '00abdf53']]`
  - `FALL_THROUGH` [`00abdf50`](#insn-00abdf50) → [`00abdf54`](#insn-00abdf54)
- ブロック [`00abdf54`](#insn-00abdf54) 範囲 `[['00abdf54', '00abdf63']]`
  - `CONDITIONAL_JUMP` [`00abdf60`](#insn-00abdf60) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdf60`](#insn-00abdf60) → [`00abdf64`](#insn-00abdf64)
- ブロック [`00abdf64`](#insn-00abdf64) 範囲 `[['00abdf64', '00abdf67']]`
- ブロック [`00abdf68`](#insn-00abdf68) 範囲 `[['00abdf68', '00abdf7b']]`
  - `CONDITIONAL_JUMP` [`00abdf78`](#insn-00abdf78) → [`00abe054`](#insn-00abe054)
  - `FALL_THROUGH` [`00abdf78`](#insn-00abdf78) → [`00abdf7c`](#insn-00abdf7c)
- ブロック [`00abdf7c`](#insn-00abdf7c) 範囲 `[['00abdf7c', '00abdf7f']]`
- ブロック [`00abe054`](#insn-00abe054) 範囲 `[['00abe054', '00abe057']]`

## 命令位置別の参照

- [`00abd8ec`](#insn-00abd8ec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8f0`](#insn-00abd8f0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8f4`](#insn-00abd8f4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8f8`](#insn-00abd8f8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8fc`](#insn-00abd8fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd900`](#insn-00abd900) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd918`](#insn-00abd918) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd920`](#insn-00abd920) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd924`](#insn-00abd924) → [`00487e20`](../00487/00487e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e20` · 推定シンボル `None` · 推定型 `None`
- [`00abd938`](#insn-00abd938) → `00c64d38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abd938`](#insn-00abd938) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd940`](#insn-00abd940) → `002a1884`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abd944`](#insn-00abd944) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd948`](#insn-00abd948) → `002a188a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abd94c`](#insn-00abd94c) → `Stack[-0x1d1]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd950`](#insn-00abd950) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd954`](#insn-00abd954) → `Stack[-0x1d9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd968`](#insn-00abd968) → [`00b110ec`](../00b11/00b110ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b110ec` · 推定シンボル `None` · 推定型 `None`
- [`00abd96c`](#insn-00abd96c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd974`](#insn-00abd974) → [`00abd980`](#insn-00abd980) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd978`](#insn-00abd978) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd97c`](#insn-00abd97c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd980`](#insn-00abd980) → [`00abdd94`](#insn-00abdd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd98c`](#insn-00abd98c) → [`00488434`](../00488/00488434.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488434` · 推定シンボル `None` · 推定型 `None`
- [`00abd998`](#insn-00abd998) → [`00597608`](../00597/00597608.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00597608` · 推定シンボル `None` · 推定型 `None`
- [`00abd9a4`](#insn-00abd9a4) → [`00596f2c`](../00596/00596f2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00596f2c` · 推定シンボル `None` · 推定型 `None`
- [`00abd9a8`](#insn-00abd9a8) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9ac`](#insn-00abd9ac) → [`00abd9d8`](#insn-00abd9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9b8`](#insn-00abd9b8) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abd9bc`](#insn-00abd9bc) → [`00abd9d8`](#insn-00abd9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9d4`](#insn-00abd9d4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abd9d8`](#insn-00abd9d8) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9dc`](#insn-00abd9dc) → [`00abd9e8`](#insn-00abd9e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9e0`](#insn-00abd9e0) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9e4`](#insn-00abd9e4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd9f0`](#insn-00abd9f0) → [`00abda20`](#insn-00abda20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd9f8`](#insn-00abd9f8) → [`00abda08`](#insn-00abda08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda04`](#insn-00abda04) → [`00abda20`](#insn-00abda20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda10`](#insn-00abda10) → [`00abd9fc`](#insn-00abd9fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda18`](#insn-00abda18) → [`0086a1ec`](../0086a/0086a1ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086a1ec` · 推定シンボル `None` · 推定型 `None`
- [`00abda1c`](#insn-00abda1c) → [`00abd9fc`](#insn-00abd9fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda48`](#insn-00abda48) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda50`](#insn-00abda50) → [`00abda64`](#insn-00abda64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda64`](#insn-00abda64) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda68`](#insn-00abda68) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda74`](#insn-00abda74) → `Stack[-0x1d9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda80`](#insn-00abda80) → [`0044108c`](../00441/0044108c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044108c` · 推定シンボル `None` · 推定型 `None`
- [`00abda90`](#insn-00abda90) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abda9c`](#insn-00abda9c) → [`00abdaa8`](#insn-00abdaa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdaa0`](#insn-00abdaa0) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdaa4`](#insn-00abdaa4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdab4`](#insn-00abdab4) → [`00abdcdc`](#insn-00abdcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdabc`](#insn-00abdabc) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abdacc`](#insn-00abdacc) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdaec`](#insn-00abdaec) → [`00abdafc`](#insn-00abdafc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdaf0`](#insn-00abdaf0) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdaf8`](#insn-00abdaf8) → [`00abdb94`](#insn-00abdb94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb10`](#insn-00abdb10) → [`00abdf34`](#insn-00abdf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb34`](#insn-00abdb34) → [`00abdb50`](#insn-00abdb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb3c`](#insn-00abdb3c) → [`00abdf68`](#insn-00abdf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb44`](#insn-00abdb44) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abdb4c`](#insn-00abdb4c) → [`00abdb54`](#insn-00abdb54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb68`](#insn-00abdb68) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb70`](#insn-00abdb70) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00abdb7c`](#insn-00abdb7c) → [`00abdb88`](#insn-00abdb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb84`](#insn-00abdb84) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdb94`](#insn-00abdb94) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdb9c`](#insn-00abdb9c) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdba0`](#insn-00abdba0) → [`00abdbb0`](#insn-00abdbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdba8`](#insn-00abdba8) → [`0086a1ec`](../0086a/0086a1ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086a1ec` · 推定シンボル `None` · 推定型 `None`
- [`00abdbb8`](#insn-00abdbb8) → [`00abdee0`](#insn-00abdee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdbc0`](#insn-00abdbc0) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdbc4`](#insn-00abdbc4) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdbd0`](#insn-00abdbd0) → `Stack[-0x1d9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdbdc`](#insn-00abdbdc) → [`0044108c`](../00441/0044108c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044108c` · 推定シンボル `None` · 推定型 `None`
- [`00abdc08`](#insn-00abdc08) → [`00abb92c`](../00abb/00abb92c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abb92c` · 推定シンボル `None` · 推定型 `None`
- [`00abdc0c`](#insn-00abdc0c) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc10`](#insn-00abdc10) → [`00abdc1c`](#insn-00abdc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc14`](#insn-00abdc14) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc18`](#insn-00abdc18) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdc24`](#insn-00abdc24) → [`00abdefc`](#insn-00abdefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc38`](#insn-00abdc38) → [`00abda54`](#insn-00abda54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc3c`](#insn-00abdc3c) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc54`](#insn-00abdc54) → [`00abdf18`](#insn-00abdf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc78`](#insn-00abdc78) → [`00abdc94`](#insn-00abdc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc80`](#insn-00abdc80) → [`00abdf50`](#insn-00abdf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdc88`](#insn-00abdc88) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abdc90`](#insn-00abdc90) → [`00abdc98`](#insn-00abdc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdcb4`](#insn-00abdcb4) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00abdcc0`](#insn-00abdcc0) → [`00abdccc`](#insn-00abdccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdcc8`](#insn-00abdcc8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdcd8`](#insn-00abdcd8) → [`00abda5c`](#insn-00abda5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdcec`](#insn-00abdcec) → [`00abdd1c`](#insn-00abdd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdcf8`](#insn-00abdcf8) → `00c9b520`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abdd00`](#insn-00abdd00) → `003104a1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZSt7nothrow` · 推定型 `undefined1`
- [`00abdd04`](#insn-00abdd04) → [`00c5a850`](../00c5a/00c5a850.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a850` · 推定シンボル `None` · 推定型 `None`
- [`00abdd08`](#insn-00abdd08) → [`00abdd38`](#insn-00abdd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd18`](#insn-00abdd18) → [`00abdcfc`](#insn-00abdcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd30`](#insn-00abdd30) → [`00ac100c`](../00ac1/00ac100c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac100c` · 推定シンボル `None` · 推定型 `None`
- [`00abdd34`](#insn-00abdd34) → [`00abdd5c`](#insn-00abdd5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd50`](#insn-00abdd50) → [`00ac100c`](../00ac1/00ac100c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac100c` · 推定シンボル `None` · 推定型 `None`
- [`00abdd58`](#insn-00abdd58) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdd60`](#insn-00abdd60) → [`00488658`](../00488/00488658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488658` · 推定シンボル `None` · 推定型 `None`
- [`00abdd64`](#insn-00abdd64) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd68`](#insn-00abdd68) → [`00abdd94`](#insn-00abdd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd74`](#insn-00abdd74) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abdd78`](#insn-00abdd78) → [`00abdd94`](#insn-00abdd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdd90`](#insn-00abdd90) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abdda0`](#insn-00abdda0) → `002a4c1f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abdda4`](#insn-00abdda4) → `002a4c24`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abdda8`](#insn-00abdda8) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddac`](#insn-00abddac) → `Stack[-0x1d2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddb0`](#insn-00abddb0) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddb4`](#insn-00abddb4) → `Stack[-0x1da]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddc8`](#insn-00abddc8) → [`00b110ec`](../00b11/00b110ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b110ec` · 推定シンボル `None` · 推定型 `None`
- [`00abddcc`](#insn-00abddcc) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddd4`](#insn-00abddd4) → [`00abdde0`](#insn-00abdde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddd8`](#insn-00abddd8) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdddc`](#insn-00abdddc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdde0`](#insn-00abdde0) → [`00abde1c`](#insn-00abde1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddec`](#insn-00abddec) → [`00abde14`](#insn-00abde14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abddfc`](#insn-00abddfc) → [`00abc814`](../00abc/00abc814.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abc814` · 推定シンボル `None` · 推定型 `None`
- [`00abde10`](#insn-00abde10) → [`00abddf4`](#insn-00abddf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde18`](#insn-00abde18) → [`00488658`](../00488/00488658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488658` · 推定シンボル `None` · 推定型 `None`
- [`00abde28`](#insn-00abde28) → `00c9abb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abde2c`](#insn-00abde2c) → `00c9abb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abde34`](#insn-00abde34) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00abde3c`](#insn-00abde3c) → `00c65818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abde3c`](#insn-00abde3c) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde40`](#insn-00abde40) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abde40`](#insn-00abde40) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde44`](#insn-00abde44) → `00c90ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00abde48`](#insn-00abde48) → `00c93218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00abde4c`](#insn-00abde4c) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abde54`](#insn-00abde54) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abde58`](#insn-00abde58) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde60`](#insn-00abde60) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00abde60`](#insn-00abde60) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde64`](#insn-00abde64) → [`00abde70`](#insn-00abde70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde68`](#insn-00abde68) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde6c`](#insn-00abde6c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abde74`](#insn-00abde74) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`00abde78`](#insn-00abde78) → `00c93208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00abde80`](#insn-00abde80) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`00abde88`](#insn-00abde88) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`00abde8c`](#insn-00abde8c) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde90`](#insn-00abde90) → [`00abde9c`](#insn-00abde9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde94`](#insn-00abde94) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde98`](#insn-00abde98) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abde9c`](#insn-00abde9c) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdea0`](#insn-00abdea0) → [`00abdeac`](#insn-00abdeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdea4`](#insn-00abdea4) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdea8`](#insn-00abdea8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abdeac`](#insn-00abdeac) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdeb4`](#insn-00abdeb4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdebc`](#insn-00abdebc) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdec4`](#insn-00abdec4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdec8`](#insn-00abdec8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdecc`](#insn-00abdecc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abded0`](#insn-00abded0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abded4`](#insn-00abded4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abded8`](#insn-00abded8) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdee0`](#insn-00abdee0) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdee8`](#insn-00abdee8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdef0`](#insn-00abdef0) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdef8`](#insn-00abdef8) → [`00ac0fe4`](../00ac0/00ac0fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0fe4` · 推定シンボル `None` · 推定型 `None`
- [`00abdefc`](#insn-00abdefc) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf04`](#insn-00abdf04) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf0c`](#insn-00abdf0c) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf14`](#insn-00abdf14) → [`00ac0fe4`](../00ac0/00ac0fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0fe4` · 推定シンボル `None` · 推定型 `None`
- [`00abdf18`](#insn-00abdf18) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf20`](#insn-00abdf20) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf28`](#insn-00abdf28) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf2c`](#insn-00abdf2c) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf30`](#insn-00abdf30) → [`00ac0ff8`](../00ac0/00ac0ff8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0ff8` · 推定シンボル `None` · 推定型 `None`
- [`00abdf34`](#insn-00abdf34) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf3c`](#insn-00abdf3c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf44`](#insn-00abdf44) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf4c`](#insn-00abdf4c) → [`00ac0fd0`](../00ac0/00ac0fd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0fd0` · 推定シンボル `None` · 推定型 `None`
- [`00abdf50`](#insn-00abdf50) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf58`](#insn-00abdf58) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf60`](#insn-00abdf60) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf64`](#insn-00abdf64) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`00abdf68`](#insn-00abdf68) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf70`](#insn-00abdf70) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf78`](#insn-00abdf78) → [`00abe054`](#insn-00abe054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf7c`](#insn-00abdf7c) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`00abe054`](#insn-00abe054) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abd8ec`](#insn-00abd8ec)

~~~json
{
  "source": "00abd8ec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8f0`](#insn-00abd8f0)

~~~json
{
  "source": "00abd8f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8f4`](#insn-00abd8f4)

~~~json
{
  "source": "00abd8f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8f8`](#insn-00abd8f8)

~~~json
{
  "source": "00abd8f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8fc`](#insn-00abd8fc)

~~~json
{
  "source": "00abd8fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd900`](#insn-00abd900)

~~~json
{
  "source": "00abd900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd918`](#insn-00abd918)

~~~json
{
  "source": "00abd918",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd920`](#insn-00abd920)

~~~json
{
  "source": "00abd920",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd924`](#insn-00abd924)

~~~json
{
  "source": "00abd924",
  "target": "00487e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd938`](#insn-00abd938)

~~~json
{
  "source": "00abd938",
  "target": "00c64d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abd938`](#insn-00abd938)

~~~json
{
  "source": "00abd938",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd940`](#insn-00abd940)

~~~json
{
  "source": "00abd940",
  "target": "002a1884",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1884",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c6c6973742e6a736f6e00",
  "capture_start": "002a1884",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abd944`](#insn-00abd944)

~~~json
{
  "source": "00abd944",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd948`](#insn-00abd948)

~~~json
{
  "source": "00abd948",
  "target": "002a188a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1884",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c6c6973742e6a736f6e00",
  "capture_start": "002a1884",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abd94c`](#insn-00abd94c)

~~~json
{
  "source": "00abd94c",
  "target": "Stack[-0x1d1]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd950`](#insn-00abd950)

~~~json
{
  "source": "00abd950",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd954`](#insn-00abd954)

~~~json
{
  "source": "00abd954",
  "target": "Stack[-0x1d9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd968`](#insn-00abd968)

~~~json
{
  "source": "00abd968",
  "target": "00b110ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd96c`](#insn-00abd96c)

~~~json
{
  "source": "00abd96c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd974`](#insn-00abd974)

~~~json
{
  "source": "00abd974",
  "target": "00abd980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd978`](#insn-00abd978)

~~~json
{
  "source": "00abd978",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd97c`](#insn-00abd97c)

~~~json
{
  "source": "00abd97c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd980`](#insn-00abd980)

~~~json
{
  "source": "00abd980",
  "target": "00abdd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd98c`](#insn-00abd98c)

~~~json
{
  "source": "00abd98c",
  "target": "00488434",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd998`](#insn-00abd998)

~~~json
{
  "source": "00abd998",
  "target": "00597608",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd9a4`](#insn-00abd9a4)

~~~json
{
  "source": "00abd9a4",
  "target": "00596f2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd9a8`](#insn-00abd9a8)

~~~json
{
  "source": "00abd9a8",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9ac`](#insn-00abd9ac)

~~~json
{
  "source": "00abd9ac",
  "target": "00abd9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9b8`](#insn-00abd9b8)

~~~json
{
  "source": "00abd9b8",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd9bc`](#insn-00abd9bc)

~~~json
{
  "source": "00abd9bc",
  "target": "00abd9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9d4`](#insn-00abd9d4)

~~~json
{
  "source": "00abd9d4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd9d8`](#insn-00abd9d8)

~~~json
{
  "source": "00abd9d8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9dc`](#insn-00abd9dc)

~~~json
{
  "source": "00abd9dc",
  "target": "00abd9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9e0`](#insn-00abd9e0)

~~~json
{
  "source": "00abd9e0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9e4`](#insn-00abd9e4)

~~~json
{
  "source": "00abd9e4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd9f0`](#insn-00abd9f0)

~~~json
{
  "source": "00abd9f0",
  "target": "00abda20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd9f8`](#insn-00abd9f8)

~~~json
{
  "source": "00abd9f8",
  "target": "00abda08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda04`](#insn-00abda04)

~~~json
{
  "source": "00abda04",
  "target": "00abda20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda10`](#insn-00abda10)

~~~json
{
  "source": "00abda10",
  "target": "00abd9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda18`](#insn-00abda18)

~~~json
{
  "source": "00abda18",
  "target": "0086a1ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abda1c`](#insn-00abda1c)

~~~json
{
  "source": "00abda1c",
  "target": "00abd9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda48`](#insn-00abda48)

~~~json
{
  "source": "00abda48",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda50`](#insn-00abda50)

~~~json
{
  "source": "00abda50",
  "target": "00abda64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda64`](#insn-00abda64)

~~~json
{
  "source": "00abda64",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda68`](#insn-00abda68)

~~~json
{
  "source": "00abda68",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda74`](#insn-00abda74)

~~~json
{
  "source": "00abda74",
  "target": "Stack[-0x1d9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda80`](#insn-00abda80)

~~~json
{
  "source": "00abda80",
  "target": "0044108c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abda90`](#insn-00abda90)

~~~json
{
  "source": "00abda90",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abda9c`](#insn-00abda9c)

~~~json
{
  "source": "00abda9c",
  "target": "00abdaa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdaa0`](#insn-00abdaa0)

~~~json
{
  "source": "00abdaa0",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdaa4`](#insn-00abdaa4)

~~~json
{
  "source": "00abdaa4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdab4`](#insn-00abdab4)

~~~json
{
  "source": "00abdab4",
  "target": "00abdcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdabc`](#insn-00abdabc)

~~~json
{
  "source": "00abdabc",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdacc`](#insn-00abdacc)

~~~json
{
  "source": "00abdacc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdaec`](#insn-00abdaec)

~~~json
{
  "source": "00abdaec",
  "target": "00abdafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdaf0`](#insn-00abdaf0)

~~~json
{
  "source": "00abdaf0",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdaf8`](#insn-00abdaf8)

~~~json
{
  "source": "00abdaf8",
  "target": "00abdb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb10`](#insn-00abdb10)

~~~json
{
  "source": "00abdb10",
  "target": "00abdf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb34`](#insn-00abdb34)

~~~json
{
  "source": "00abdb34",
  "target": "00abdb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb3c`](#insn-00abdb3c)

~~~json
{
  "source": "00abdb3c",
  "target": "00abdf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb44`](#insn-00abdb44)

~~~json
{
  "source": "00abdb44",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdb4c`](#insn-00abdb4c)

~~~json
{
  "source": "00abdb4c",
  "target": "00abdb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb68`](#insn-00abdb68)

~~~json
{
  "source": "00abdb68",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb70`](#insn-00abdb70)

~~~json
{
  "source": "00abdb70",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdb7c`](#insn-00abdb7c)

~~~json
{
  "source": "00abdb7c",
  "target": "00abdb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb84`](#insn-00abdb84)

~~~json
{
  "source": "00abdb84",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdb94`](#insn-00abdb94)

~~~json
{
  "source": "00abdb94",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdb9c`](#insn-00abdb9c)

~~~json
{
  "source": "00abdb9c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdba0`](#insn-00abdba0)

~~~json
{
  "source": "00abdba0",
  "target": "00abdbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdba8`](#insn-00abdba8)

~~~json
{
  "source": "00abdba8",
  "target": "0086a1ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdbb8`](#insn-00abdbb8)

~~~json
{
  "source": "00abdbb8",
  "target": "00abdee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdbc0`](#insn-00abdbc0)

~~~json
{
  "source": "00abdbc0",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdbc4`](#insn-00abdbc4)

~~~json
{
  "source": "00abdbc4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdbd0`](#insn-00abdbd0)

~~~json
{
  "source": "00abdbd0",
  "target": "Stack[-0x1d9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdbdc`](#insn-00abdbdc)

~~~json
{
  "source": "00abdbdc",
  "target": "0044108c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdc08`](#insn-00abdc08)

~~~json
{
  "source": "00abdc08",
  "target": "00abb92c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdc0c`](#insn-00abdc0c)

~~~json
{
  "source": "00abdc0c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc10`](#insn-00abdc10)

~~~json
{
  "source": "00abdc10",
  "target": "00abdc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc14`](#insn-00abdc14)

~~~json
{
  "source": "00abdc14",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc18`](#insn-00abdc18)

~~~json
{
  "source": "00abdc18",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdc24`](#insn-00abdc24)

~~~json
{
  "source": "00abdc24",
  "target": "00abdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc38`](#insn-00abdc38)

~~~json
{
  "source": "00abdc38",
  "target": "00abda54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc3c`](#insn-00abdc3c)

~~~json
{
  "source": "00abdc3c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc54`](#insn-00abdc54)

~~~json
{
  "source": "00abdc54",
  "target": "00abdf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc78`](#insn-00abdc78)

~~~json
{
  "source": "00abdc78",
  "target": "00abdc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc80`](#insn-00abdc80)

~~~json
{
  "source": "00abdc80",
  "target": "00abdf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdc88`](#insn-00abdc88)

~~~json
{
  "source": "00abdc88",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdc90`](#insn-00abdc90)

~~~json
{
  "source": "00abdc90",
  "target": "00abdc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdcb4`](#insn-00abdcb4)

~~~json
{
  "source": "00abdcb4",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdcc0`](#insn-00abdcc0)

~~~json
{
  "source": "00abdcc0",
  "target": "00abdccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdcc8`](#insn-00abdcc8)

~~~json
{
  "source": "00abdcc8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdcd8`](#insn-00abdcd8)

~~~json
{
  "source": "00abdcd8",
  "target": "00abda5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdcec`](#insn-00abdcec)

~~~json
{
  "source": "00abdcec",
  "target": "00abdd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdcf8`](#insn-00abdcf8)

~~~json
{
  "source": "00abdcf8",
  "target": "00c9b520",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b520",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abdd00`](#insn-00abdd00)

~~~json
{
  "source": "00abdd00",
  "target": "003104a1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003104a1",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "003104a1",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abdd04`](#insn-00abdd04)

~~~json
{
  "source": "00abdd04",
  "target": "00c5a850",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd08`](#insn-00abdd08)

~~~json
{
  "source": "00abdd08",
  "target": "00abdd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd18`](#insn-00abdd18)

~~~json
{
  "source": "00abdd18",
  "target": "00abdcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd30`](#insn-00abdd30)

~~~json
{
  "source": "00abdd30",
  "target": "00ac100c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd34`](#insn-00abdd34)

~~~json
{
  "source": "00abdd34",
  "target": "00abdd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd50`](#insn-00abdd50)

~~~json
{
  "source": "00abdd50",
  "target": "00ac100c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd58`](#insn-00abdd58)

~~~json
{
  "source": "00abdd58",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd60`](#insn-00abdd60)

~~~json
{
  "source": "00abdd60",
  "target": "00488658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd64`](#insn-00abdd64)

~~~json
{
  "source": "00abdd64",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd68`](#insn-00abdd68)

~~~json
{
  "source": "00abdd68",
  "target": "00abdd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd74`](#insn-00abdd74)

~~~json
{
  "source": "00abdd74",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdd78`](#insn-00abdd78)

~~~json
{
  "source": "00abdd78",
  "target": "00abdd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdd90`](#insn-00abdd90)

~~~json
{
  "source": "00abdd90",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdda0`](#insn-00abdda0)

~~~json
{
  "source": "00abdda0",
  "target": "002a4c1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4c1f",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6d6564616c6e616d652e74737600",
  "capture_start": "002a4c1f",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abdda4`](#insn-00abdda4)

~~~json
{
  "source": "00abdda4",
  "target": "002a4c24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4c1f",
  "offset": 5,
  "size": 14,
  "datatype": "string",
  "bytes": "6d6564616c6e616d652e74737600",
  "capture_start": "002a4c1f",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abdda8`](#insn-00abdda8)

~~~json
{
  "source": "00abdda8",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddac`](#insn-00abddac)

~~~json
{
  "source": "00abddac",
  "target": "Stack[-0x1d2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddb0`](#insn-00abddb0)

~~~json
{
  "source": "00abddb0",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddb4`](#insn-00abddb4)

~~~json
{
  "source": "00abddb4",
  "target": "Stack[-0x1da]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddc8`](#insn-00abddc8)

~~~json
{
  "source": "00abddc8",
  "target": "00b110ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abddcc`](#insn-00abddcc)

~~~json
{
  "source": "00abddcc",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddd4`](#insn-00abddd4)

~~~json
{
  "source": "00abddd4",
  "target": "00abdde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddd8`](#insn-00abddd8)

~~~json
{
  "source": "00abddd8",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdddc`](#insn-00abdddc)

~~~json
{
  "source": "00abdddc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdde0`](#insn-00abdde0)

~~~json
{
  "source": "00abdde0",
  "target": "00abde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddec`](#insn-00abddec)

~~~json
{
  "source": "00abddec",
  "target": "00abde14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abddfc`](#insn-00abddfc)

~~~json
{
  "source": "00abddfc",
  "target": "00abc814",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde10`](#insn-00abde10)

~~~json
{
  "source": "00abde10",
  "target": "00abddf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde18`](#insn-00abde18)

~~~json
{
  "source": "00abde18",
  "target": "00488658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde28`](#insn-00abde28)

~~~json
{
  "source": "00abde28",
  "target": "00c9abb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde2c`](#insn-00abde2c)

~~~json
{
  "source": "00abde2c",
  "target": "00c9abb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde34`](#insn-00abde34)

~~~json
{
  "source": "00abde34",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde3c`](#insn-00abde3c)

~~~json
{
  "source": "00abde3c",
  "target": "00c65818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde3c`](#insn-00abde3c)

~~~json
{
  "source": "00abde3c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde40`](#insn-00abde40)

~~~json
{
  "source": "00abde40",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde40`](#insn-00abde40)

~~~json
{
  "source": "00abde40",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde44`](#insn-00abde44)

~~~json
{
  "source": "00abde44",
  "target": "00c90ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c90ff8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abde48`](#insn-00abde48)

~~~json
{
  "source": "00abde48",
  "target": "00c93218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93218",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde4c`](#insn-00abde4c)

~~~json
{
  "source": "00abde4c",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde54`](#insn-00abde54)

~~~json
{
  "source": "00abde54",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde58`](#insn-00abde58)

~~~json
{
  "source": "00abde58",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde60`](#insn-00abde60)

~~~json
{
  "source": "00abde60",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00abde60`](#insn-00abde60)

~~~json
{
  "source": "00abde60",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde64`](#insn-00abde64)

~~~json
{
  "source": "00abde64",
  "target": "00abde70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde68`](#insn-00abde68)

~~~json
{
  "source": "00abde68",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde6c`](#insn-00abde6c)

~~~json
{
  "source": "00abde6c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde74`](#insn-00abde74)

~~~json
{
  "source": "00abde74",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde78`](#insn-00abde78)

~~~json
{
  "source": "00abde78",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abde80`](#insn-00abde80)

~~~json
{
  "source": "00abde80",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde88`](#insn-00abde88)

~~~json
{
  "source": "00abde88",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde8c`](#insn-00abde8c)

~~~json
{
  "source": "00abde8c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde90`](#insn-00abde90)

~~~json
{
  "source": "00abde90",
  "target": "00abde9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde94`](#insn-00abde94)

~~~json
{
  "source": "00abde94",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde98`](#insn-00abde98)

~~~json
{
  "source": "00abde98",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde9c`](#insn-00abde9c)

~~~json
{
  "source": "00abde9c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdea0`](#insn-00abdea0)

~~~json
{
  "source": "00abdea0",
  "target": "00abdeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdea4`](#insn-00abdea4)

~~~json
{
  "source": "00abdea4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdea8`](#insn-00abdea8)

~~~json
{
  "source": "00abdea8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdeac`](#insn-00abdeac)

~~~json
{
  "source": "00abdeac",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdeb4`](#insn-00abdeb4)

~~~json
{
  "source": "00abdeb4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdebc`](#insn-00abdebc)

~~~json
{
  "source": "00abdebc",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdec4`](#insn-00abdec4)

~~~json
{
  "source": "00abdec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdec8`](#insn-00abdec8)

~~~json
{
  "source": "00abdec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdecc`](#insn-00abdecc)

~~~json
{
  "source": "00abdecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abded0`](#insn-00abded0)

~~~json
{
  "source": "00abded0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abded4`](#insn-00abded4)

~~~json
{
  "source": "00abded4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abded8`](#insn-00abded8)

~~~json
{
  "source": "00abded8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdee0`](#insn-00abdee0)

~~~json
{
  "source": "00abdee0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdee8`](#insn-00abdee8)

~~~json
{
  "source": "00abdee8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdef0`](#insn-00abdef0)

~~~json
{
  "source": "00abdef0",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdef8`](#insn-00abdef8)

~~~json
{
  "source": "00abdef8",
  "target": "00ac0fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdefc`](#insn-00abdefc)

~~~json
{
  "source": "00abdefc",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf04`](#insn-00abdf04)

~~~json
{
  "source": "00abdf04",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf0c`](#insn-00abdf0c)

~~~json
{
  "source": "00abdf0c",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf14`](#insn-00abdf14)

~~~json
{
  "source": "00abdf14",
  "target": "00ac0fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf18`](#insn-00abdf18)

~~~json
{
  "source": "00abdf18",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf20`](#insn-00abdf20)

~~~json
{
  "source": "00abdf20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf28`](#insn-00abdf28)

~~~json
{
  "source": "00abdf28",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf2c`](#insn-00abdf2c)

~~~json
{
  "source": "00abdf2c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf30`](#insn-00abdf30)

~~~json
{
  "source": "00abdf30",
  "target": "00ac0ff8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf34`](#insn-00abdf34)

~~~json
{
  "source": "00abdf34",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf3c`](#insn-00abdf3c)

~~~json
{
  "source": "00abdf3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf44`](#insn-00abdf44)

~~~json
{
  "source": "00abdf44",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf4c`](#insn-00abdf4c)

~~~json
{
  "source": "00abdf4c",
  "target": "00ac0fd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf50`](#insn-00abdf50)

~~~json
{
  "source": "00abdf50",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf58`](#insn-00abdf58)

~~~json
{
  "source": "00abdf58",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf60`](#insn-00abdf60)

~~~json
{
  "source": "00abdf60",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf64`](#insn-00abdf64)

~~~json
{
  "source": "00abdf64",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf68`](#insn-00abdf68)

~~~json
{
  "source": "00abdf68",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf70`](#insn-00abdf70)

~~~json
{
  "source": "00abdf70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf78`](#insn-00abdf78)

~~~json
{
  "source": "00abdf78",
  "target": "00abe054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf7c`](#insn-00abdf7c)

~~~json
{
  "source": "00abdf7c",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe054`](#insn-00abe054)

~~~json
{
  "source": "00abe054",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
