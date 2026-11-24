# 00afdfe4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-f700e68163cb0fac4a5a630213d51d15)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0044.md#review-f700e68163cb0fac4a5a630213d51d15)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdfe4",
  "name": "FUN_00afdfe4",
  "size": 1756,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d568da2dd08dc66494d2b86f87d2dd7062cdbf8af16e6470f11eb27758ea22d6",
  "source_text_sha256": "d568da2dd08dc66494d2b86f87d2dd7062cdbf8af16e6470f11eb27758ea22d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdfe4",
        "00afe6bf"
      ]
    ],
    "bytes_sha256": "f343c392c5b31c8d74bf720be83767bc07ab900324ade947c2bc34dff01f14ad",
    "instruction_count": 439,
    "instruction_bytes": 1756,
    "body_bytes": 1756,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005bc78c](../005bc/005bc78c.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [00689c7c](../00689/00689c7c.md)
- [007bbbec](../007bb/007bbbec.md)
- [007bbc70](../007bb/007bbc70.md)
- [007efb3c](../007ef/007efb3c.md)
- [00801d4c](../00801/00801d4c.md)
- [00802678](../00802/00802678.md)
- [00802b18](../00802/00802b18.md)
- [00802ea0](../00802/00802ea0.md)
- [008514b8](../00851/008514b8.md)
- [008c2ce0](../008c2/008c2ce0.md)
- [00a64340](../00a64/00a64340.md)
- [00ab9080](../00ab9/00ab9080.md)
- [00ab92d4](../00ab9/00ab92d4.md)
- [00afe6c0](../00afe/00afe6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6987 bytes

~~~c

ulong FUN_00afdfe4(int param_1,int param_2,int param_3,uint param_4,int param_5)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  ulong uVar7;
  long lVar8;
  ulong uVar9;
  undefined8 uVar11;
  long lVar12;
  uint uVar13;
  uleb128 *puVar10;
  
  lVar6 = FUN_008514b8();
  uVar7 = FUN_005e73e0(lVar6 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar7 & 1) != 0) {
    if ((int)param_4 < 1) {
      lVar6 = 0;
    }
    else {
      lVar6 = FUN_008514b8();
      lVar6 = (long)*(int *)(lVar6 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6d0)
              * 100;
      if (param_4 != 1) {
        uVar13 = 1;
        do {
          FUN_008514b8();
          if (uVar13 < 200) {
            lVar8 = FUN_008514b8();
            iVar4 = *(int *)(lVar8 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6d0);
            lVar8 = FUN_008514b8();
            lVar6 = lVar6 + (long)*(int *)(&DAT_00454bb4 +
                                          lVar8 + (long)param_2 * 0x50 +
                                          (ulong)((uVar13 & 0xff) / 10) * 4) * (long)iVar4;
          }
          uVar13 = uVar13 + 1;
        } while (param_4 != uVar13);
      }
      lVar6 = (lVar6 + 0x32) / 100;
    }
    lVar8 = FUN_008514b8();
    iVar4 = FUN_00ab9080(&uleb128_0029a6e0 + lVar8,9);
    lVar8 = FUN_008514b8();
    iVar5 = FUN_008c2ce0(&DAT_0044dd00 + lVar8,1,param_2);
    uVar7 = (((lVar6 * iVar4) / 100 + lVar6) * (long)(iVar5 + 100)) / 100;
    iVar4 = FUN_00afe6c0(param_1,param_2,param_3,0x20,0);
    if (1 < param_3) {
      iVar5 = FUN_00802678(0);
      if (iVar5 == 0) {
LAB_00afe25c:
        uVar11 = 9;
      }
      else {
        FUN_008514b8();
        uVar9 = FUN_007bbbec();
        if ((uVar9 & 1) != 0) goto LAB_00afe25c;
        iVar5 = FUN_00802678(0);
        if (iVar5 != -9) {
          FUN_008514b8();
          uVar9 = FUN_007bbc70();
          if ((uVar9 & 1) == 0) {
            FUN_008514b8();
            uVar9 = FUN_007efb3c();
            if ((uVar9 & 1) == 0) goto LAB_00afe640;
          }
        }
        uVar11 = 0x10;
      }
      lVar6 = FUN_008514b8();
      iVar5 = FUN_00689c7c(lVar6 + 0x1648,param_2,uVar11,0,0);
      iVar4 = iVar5 + iVar4;
    }
LAB_00afe640:
    if (0 < iVar4) {
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    iVar4 = FUN_00afe6c0(param_1,param_2,param_3,0x47,0);
    if (0 < iVar4) {
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    goto LAB_00afe69c;
  }
  lVar6 = FUN_008514b8();
  if ((*(int *)((long)&fde_table_entry_00333970.data_loc + lVar6) < 3) &&
     (lVar6 = FUN_008514b8(),
     (*(byte *)((long)&fde_table_entry_003380e8.initial_loc + lVar6) & 1) == 0)) {
    lVar8 = FUN_008514b8();
    lVar6 = (long)param_2 + 2;
    iVar4 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x17f8);
    lVar8 = FUN_008514b8();
    lVar12 = ((long)*(int *)(PTR_DAT_00c9b270 +
                            (long)*(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) * 4) +
             10) * (long)iVar4 + 5;
    lVar8 = SUB168(SEXT816(lVar12) * SEXT816(0x6666666666666667),8);
    lVar12 = lVar12 / 10 + (lVar12 >> 0x3f);
LAB_00afe33c:
    uVar7 = lVar12 - (lVar8 >> 0x3f);
  }
  else {
    lVar6 = FUN_008514b8();
    iVar4 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar6);
    lVar8 = FUN_008514b8();
    lVar6 = (long)param_2 + 2;
    iVar5 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x17f8);
    lVar8 = FUN_008514b8();
    iVar1 = FUN_00a64340(*(long *)(lVar8 + 0x9f6b8) + (long)param_5 * 0x38);
    uVar7 = ((long)iVar5 * (long)iVar1 + 0x32) / 100;
    if (iVar4 == 3) {
      lVar8 = FUN_008514b8();
      uVar2 = FUN_00802b18(0);
      uVar3 = FUN_00802ea0();
      iVar4 = FUN_00801d4c((long)&fde_table_entry_00337310.initial_loc + lVar8,uVar2,uVar3);
      lVar12 = uVar7 * (long)iVar4;
      lVar8 = SUB168(SEXT816(lVar12) * ZEXT816(0xa3d70a3d70a3d70b),8);
      lVar12 = lVar12 / 100 + (lVar12 >> 0x3f);
      goto LAB_00afe33c;
    }
  }
  lVar8 = FUN_008514b8();
  uVar9 = FUN_005e73e0(lVar8 + 0x2958);
  lVar8 = FUN_008514b8();
  if ((uVar9 & 1) == 0) {
    if (*(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x1840) == 0) goto LAB_00afe3c0;
LAB_00afe390:
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) != 0))
    goto LAB_00afe3c0;
    lVar6 = FUN_008514b8();
    iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x10);
    lVar6 = FUN_008514b8();
    puVar10 = &uleb128_0029a6e0 + lVar6;
    uVar11 = 0x10;
  }
  else {
    if (*(int *)(lVar8 + lVar6 * 0x770 + 0x9f724) != 0) goto LAB_00afe390;
LAB_00afe3c0:
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    lVar8 = FUN_008514b8();
    if ((uVar9 & 1) == 0) {
      iVar4 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x1840);
    }
    else {
      iVar4 = *(int *)(lVar8 + lVar6 * 0x770 + 0x9f724);
    }
    if (iVar4 != 0) {
      lVar8 = FUN_008514b8();
      uVar9 = FUN_005e73e0(lVar8 + 0x2958);
      if (((uVar9 & 1) == 0) &&
         (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 1)
         ) {
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x12);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x12;
        goto LAB_00afe5b8;
      }
    }
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 2))
    {
      lVar6 = FUN_008514b8();
      iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x16);
      lVar6 = FUN_008514b8();
      puVar10 = &uleb128_0029a6e0 + lVar6;
      uVar11 = 0x16;
    }
    else {
      lVar8 = FUN_008514b8();
      uVar9 = FUN_005e73e0(lVar8 + 0x2958);
      if (((uVar9 & 1) == 0) &&
         (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 3)
         ) {
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x17);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x17;
      }
      else {
        lVar8 = FUN_008514b8();
        uVar9 = FUN_005e73e0(lVar8 + 0x2958);
        if (((uVar9 & 1) != 0) ||
           (lVar8 = FUN_008514b8(),
           *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) != 4)) goto LAB_00afe69c;
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x18);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x18;
      }
    }
  }
LAB_00afe5b8:
  iVar5 = FUN_00ab9080(puVar10,uVar11);
  uVar7 = (long)(uVar7 * (long)(iVar4 - iVar5)) / 100 + uVar7;
LAB_00afe69c:
  return uVar7 & 0xffffffff;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdfe4"></a> `00afdfe4` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afdfe8"></a> `00afdfe8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdfec"></a> `00afdfec` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdff0"></a> `00afdff0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdff4"></a> `00afdff4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdff8"></a> `00afdff8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afdffc"></a> `00afdffc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afe000"></a> `00afe000` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afe004"></a> `00afe004` | `f7 03 04 2a` | mov w23,w4 | `FALL_THROUGH`
<a id="insn-00afe008"></a> `00afe008` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00afe00c"></a> `00afe00c` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afe010"></a> `00afe010` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00afe014"></a> `00afe014` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00afe018"></a> `00afe018` | `28 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe01c"></a> `00afe01c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afe020"></a> `00afe020` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afe024"></a> `00afe024` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe028"></a> `00afe028` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe02c"></a> `00afe02c` | `ed a4 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe030"></a> `00afe030` | `a0 07 00 37` | tbnz w0,#0x0,0x00afe124 | `CONDITIONAL_JUMP`
<a id="insn-00afe034"></a> `00afe034` | `21 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe038"></a> `00afe038` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00afe03c"></a> `00afe03c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe040"></a> `00afe040` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe044"></a> `00afe044` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00afe048"></a> `00afe048` | `cc 00 00 54` | b.gt 0x00afe060 | `CONDITIONAL_JUMP`
<a id="insn-00afe04c"></a> `00afe04c` | `1b 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe050"></a> `00afe050` | `08 1d 90 52` | mov w8,#0x80e8 | `FALL_THROUGH`
<a id="insn-00afe054"></a> `00afe054` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe058"></a> `00afe058` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00afe05c"></a> `00afe05c` | `28 14 00 36` | tbz w8,#0x0,0x00afe2e0 | `CONDITIONAL_JUMP`
<a id="insn-00afe060"></a> `00afe060` | `16 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe064"></a> `00afe064` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00afe068"></a> `00afe068` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe06c"></a> `00afe06c` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe070"></a> `00afe070` | `12 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe074"></a> `00afe074` | `a8 7e 40 93` | sxtw x8,w21 | `FALL_THROUGH`
<a id="insn-00afe078"></a> `00afe078` | `09 52 9a 52` | mov w9,#0xd290 | `FALL_THROUGH`
<a id="insn-00afe07c"></a> `00afe07c` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe080"></a> `00afe080` | `16 09 00 91` | add x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00afe084"></a> `00afe084` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe088"></a> `00afe088` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe08c"></a> `00afe08c` | `13 69 a9 b8` | ldrsw x19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe090"></a> `00afe090` | `0a 4d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe094"></a> `00afe094` | `08 d7 9e 52` | mov w8,#0xf6b8 | `FALL_THROUGH`
<a id="insn-00afe098"></a> `00afe098` | `09 07 80 52` | mov w9,#0x38 | `FALL_THROUGH`
<a id="insn-00afe09c"></a> `00afe09c` | `28 01 a0 72` | movk w8,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe0a0"></a> `00afe0a0` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe0a4"></a> `00afe0a4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afe0a8"></a> `00afe0a8` | `e0 22 29 9b` | smaddl x0,w23,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe0ac"></a> `00afe0ac` | `a5 98 fd 97` | bl 0x00a64340 | `UNCONDITIONAL_CALL`
<a id="insn-00afe0b0"></a> `00afe0b0` | `77 e1 9a d2` | mov x23,#0xd70b | `FALL_THROUGH`
<a id="insn-00afe0b4"></a> `00afe0b4` | `68 7e 20 9b` | smull x8,w19,w0 | `FALL_THROUGH`
<a id="insn-00afe0b8"></a> `00afe0b8` | `9f 0e 00 71` | cmp w20,#0x3 | `FALL_THROUGH`
<a id="insn-00afe0bc"></a> `00afe0bc` | `77 14 ae f2` | movk x23,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe0c0"></a> `00afe0c0` | `b7 47 c1 f2` | movk x23,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00afe0c4"></a> `00afe0c4` | `f7 7a f4 f2` | movk x23,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00afe0c8"></a> `00afe0c8` | `08 c9 00 91` | add x8,x8,#0x32 | `FALL_THROUGH`
<a id="insn-00afe0cc"></a> `00afe0cc` | `09 7d 57 9b` | smulh x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00afe0d0"></a> `00afe0d0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe0d4"></a> `00afe0d4` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe0d8"></a> `00afe0d8` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe0dc"></a> `00afe0dc` | `21 13 00 54` | b.ne 0x00afe340 | `CONDITIONAL_JUMP`
<a id="insn-00afe0e0"></a> `00afe0e0` | `f6 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe0e4"></a> `00afe0e4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afe0e8"></a> `00afe0e8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afe0ec"></a> `00afe0ec` | `8b 12 f4 97` | bl 0x00802b18 | `UNCONDITIONAL_CALL`
<a id="insn-00afe0f0"></a> `00afe0f0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afe0f4"></a> `00afe0f4` | `6b 13 f4 97` | bl 0x00802ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe0f8"></a> `00afe0f8` | `88 de 4c 91` | add x8,x20,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-00afe0fc"></a> `00afe0fc` | `e2 03 00 2a` | mov w2,w0 | `FALL_THROUGH`
<a id="insn-00afe100"></a> `00afe100` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afe104"></a> `00afe104` | `00 41 0c 91` | add x0,x8,#0x310 | `FALL_THROUGH`
<a id="insn-00afe108"></a> `00afe108` | `11 0f f4 97` | bl 0x00801d4c | `UNCONDITIONAL_CALL`
<a id="insn-00afe10c"></a> `00afe10c` | `08 7c 40 93` | sxtw x8,w0 | `FALL_THROUGH`
<a id="insn-00afe110"></a> `00afe110` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe114"></a> `00afe114` | `09 7d 57 9b` | smulh x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00afe118"></a> `00afe118` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe11c"></a> `00afe11c` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe120"></a> `00afe120` | `87 00 00 14` | b 0x00afe33c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe124"></a> `00afe124` | `78 e1 9a d2` | mov x24,#0xd70b | `FALL_THROUGH`
<a id="insn-00afe128"></a> `00afe128` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00afe12c"></a> `00afe12c` | `78 14 ae f2` | movk x24,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe130"></a> `00afe130` | `b8 47 c1 f2` | movk x24,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00afe134"></a> `00afe134` | `f8 7a f4 f2` | movk x24,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00afe138"></a> `00afe138` | `2b 04 00 54` | b.lt 0x00afe1bc | `CONDITIONAL_JUMP`
<a id="insn-00afe13c"></a> `00afe13c` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-00afe140"></a> `00afe140` | `f6 0f 00 b9` | str w22,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00afe144"></a> `00afe144` | `17 7d 40 93` | sxtw x23,w8 | `FALL_THROUGH`
<a id="insn-00afe148"></a> `00afe148` | `b5 83 1f f8` | stur x21,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afe14c"></a> `00afe14c` | `f9 0a 00 91` | add x25,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00afe150"></a> `00afe150` | `da 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe154"></a> `00afe154` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00afe158"></a> `00afe158` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00afe15c"></a> `00afe15c` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00afe160"></a> `00afe160` | `28 03 08 9b` | madd x8,x25,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe164"></a> `00afe164` | `f4 0b 00 f9` | str x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe168"></a> `00afe168` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afe16c"></a> `00afe16c` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe170"></a> `00afe170` | `09 da 9e 52` | mov w9,#0xf6d0 | `FALL_THROUGH`
<a id="insn-00afe174"></a> `00afe174` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe178"></a> `00afe178` | `08 69 a9 b8` | ldrsw x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe17c"></a> `00afe17c` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00afe180"></a> `00afe180` | `1a 7d 29 9b` | smull x26,w8,w9 | `FALL_THROUGH`
<a id="insn-00afe184"></a> `00afe184` | `01 07 00 54` | b.ne 0x00afe264 | `CONDITIONAL_JUMP`
<a id="insn-00afe188"></a> `00afe188` | `78 e1 9a d2` | mov x24,#0xd70b | `FALL_THROUGH`
<a id="insn-00afe18c"></a> `00afe18c` | `48 cb 00 91` | add x8,x26,#0x32 | `FALL_THROUGH`
<a id="insn-00afe190"></a> `00afe190` | `b5 83 5f f8` | ldur x21,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afe194"></a> `00afe194` | `78 14 ae f2` | movk x24,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe198"></a> `00afe198` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe19c"></a> `00afe19c` | `f6 0f 40 b9` | ldr w22,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00afe1a0"></a> `00afe1a0` | `b8 47 c1 f2` | movk x24,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00afe1a4"></a> `00afe1a4` | `f8 7a f4 f2` | movk x24,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00afe1a8"></a> `00afe1a8` | `09 7d 58 9b` | smulh x9,x8,x24 | `FALL_THROUGH`
<a id="insn-00afe1ac"></a> `00afe1ac` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe1b0"></a> `00afe1b0` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe1b4"></a> `00afe1b4` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe1b8"></a> `00afe1b8` | `02 00 00 14` | b 0x00afe1c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe1bc"></a> `00afe1bc` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00afe1c0"></a> `00afe1c0` | `be 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe1c4"></a> `00afe1c4` | `08 68 4a 91` | add x8,x0,#0x29a, LSL #12 | `FALL_THROUGH`
<a id="insn-00afe1c8"></a> `00afe1c8` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-00afe1cc"></a> `00afe1cc` | `00 81 1b 91` | add x0,x8,#0x6e0 | `FALL_THROUGH`
<a id="insn-00afe1d0"></a> `00afe1d0` | `ac eb fe 97` | bl 0x00ab9080 | `UNCONDITIONAL_CALL`
<a id="insn-00afe1d4"></a> `00afe1d4` | `08 7c 40 93` | sxtw x8,w0 | `FALL_THROUGH`
<a id="insn-00afe1d8"></a> `00afe1d8` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe1dc"></a> `00afe1dc` | `09 7d 58 9b` | smulh x9,x8,x24 | `FALL_THROUGH`
<a id="insn-00afe1e0"></a> `00afe1e0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe1e4"></a> `00afe1e4` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe1e8"></a> `00afe1e8` | `28 fd 48 8b` | add x8,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe1ec"></a> `00afe1ec` | `13 01 13 8b` | add x19,x8,x19 | `FALL_THROUGH`
<a id="insn-00afe1f0"></a> `00afe1f0` | `b2 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe1f4"></a> `00afe1f4` | `08 34 51 91` | add x8,x0,#0x44d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afe1f8"></a> `00afe1f8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afe1fc"></a> `00afe1fc` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00afe200"></a> `00afe200` | `00 01 34 91` | add x0,x8,#0xd00 | `FALL_THROUGH`
<a id="insn-00afe204"></a> `00afe204` | `b7 12 f7 97` | bl 0x008c2ce0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe208"></a> `00afe208` | `08 90 01 11` | add w8,w0,#0x64 | `FALL_THROUGH`
<a id="insn-00afe20c"></a> `00afe20c` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00afe210"></a> `00afe210` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afe214"></a> `00afe214` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00afe218"></a> `00afe218` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00afe21c"></a> `00afe21c` | `03 04 80 52` | mov w3,#0x20 | `FALL_THROUGH`
<a id="insn-00afe220"></a> `00afe220` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00afe224"></a> `00afe224` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe228"></a> `00afe228` | `09 7d 58 9b` | smulh x9,x8,x24 | `FALL_THROUGH`
<a id="insn-00afe22c"></a> `00afe22c` | `39 01 08 8b` | add x25,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe230"></a> `00afe230` | `3a ff 46 93` | asr x26,x25,#0x6 | `FALL_THROUGH`
<a id="insn-00afe234"></a> `00afe234` | `23 01 00 94` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe238"></a> `00afe238` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afe23c"></a> `00afe23c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00afe240"></a> `00afe240` | `0d 20 00 54` | b.le 0x00afe640 | `CONDITIONAL_JUMP`
<a id="insn-00afe244"></a> `00afe244` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afe248"></a> `00afe248` | `0c 11 f4 97` | bl 0x00802678 | `UNCONDITIONAL_CALL`
<a id="insn-00afe24c"></a> `00afe24c` | `80 00 00 34` | cbz w0,0x00afe25c | `CONDITIONAL_JUMP`
<a id="insn-00afe250"></a> `00afe250` | `9a 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe254"></a> `00afe254` | `66 f6 f2 97` | bl 0x007bbbec | `UNCONDITIONAL_CALL`
<a id="insn-00afe258"></a> `00afe258` | `c0 1c 00 36` | tbz w0,#0x0,0x00afe5f0 | `CONDITIONAL_JUMP`
<a id="insn-00afe25c"></a> `00afe25c` | `33 01 80 52` | mov w19,#0x9 | `FALL_THROUGH`
<a id="insn-00afe260"></a> `00afe260` | `ef 00 00 14` | b 0x00afe61c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe264"></a> `00afe264` | `9b 7e 40 93` | sxtw x27,w20 | `FALL_THROUGH`
<a id="insn-00afe268"></a> `00afe268` | `95 76 89 52` | mov w21,#0x4bb4 | `FALL_THROUGH`
<a id="insn-00afe26c"></a> `00afe26c` | `3c 00 80 52` | mov w28,#0x1 | `FALL_THROUGH`
<a id="insn-00afe270"></a> `00afe270` | `18 0a 80 52` | mov w24,#0x50 | `FALL_THROUGH`
<a id="insn-00afe274"></a> `00afe274` | `b5 08 a0 72` | movk w21,#0x45, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe278"></a> `00afe278` | `04 00 00 14` | b 0x00afe288 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe27c"></a> `00afe27c` | `9c 07 00 11` | add w28,w28,#0x1 | `FALL_THROUGH`
<a id="insn-00afe280"></a> `00afe280` | `7f 02 1c 6b` | cmp w19,w28 | `FALL_THROUGH`
<a id="insn-00afe284"></a> `00afe284` | `20 f8 ff 54` | b.eq 0x00afe188 | `CONDITIONAL_JUMP`
<a id="insn-00afe288"></a> `00afe288` | `8c 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe28c"></a> `00afe28c` | `9f 1f 03 71` | cmp w28,#0xc7 | `FALL_THROUGH`
<a id="insn-00afe290"></a> `00afe290` | `68 ff ff 54` | b.hi 0x00afe27c | `CONDITIONAL_JUMP`
<a id="insn-00afe294"></a> `00afe294` | `88 1f 00 12` | and w8,w28,#0xff | `FALL_THROUGH`
<a id="insn-00afe298"></a> `00afe298` | `a9 19 80 52` | mov w9,#0xcd | `FALL_THROUGH`
<a id="insn-00afe29c"></a> `00afe29c` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00afe2a0"></a> `00afe2a0` | `16 7d 0b 53` | lsr w22,w8,#0xb | `FALL_THROUGH`
<a id="insn-00afe2a4"></a> `00afe2a4` | `85 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe2a8"></a> `00afe2a8` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00afe2ac"></a> `00afe2ac` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00afe2b0"></a> `00afe2b0` | `28 03 08 9b` | madd x8,x25,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe2b4"></a> `00afe2b4` | `68 23 29 9b` | smaddl x8,w27,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe2b8"></a> `00afe2b8` | `09 da 9e 52` | mov w9,#0xf6d0 | `FALL_THROUGH`
<a id="insn-00afe2bc"></a> `00afe2bc` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe2c0"></a> `00afe2c0` | `14 69 a9 b8` | ldrsw x20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe2c4"></a> `00afe2c4` | `7d 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe2c8"></a> `00afe2c8` | `e8 02 38 9b` | smaddl x8,w23,w24,x0 | `FALL_THROUGH`
<a id="insn-00afe2cc"></a> `00afe2cc` | `08 49 36 8b` | add x8,x8,w22, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00afe2d0"></a> `00afe2d0` | `08 69 b5 b8` | ldrsw x8,[x8, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe2d4"></a> `00afe2d4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afe2d8"></a> `00afe2d8` | `1a 69 34 9b` | smaddl x26,w8,w20,x26 | `FALL_THROUGH`
<a id="insn-00afe2dc"></a> `00afe2dc` | `e8 ff ff 17` | b 0x00afe27c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe2e0"></a> `00afe2e0` | `76 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe2e4"></a> `00afe2e4` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-00afe2e8"></a> `00afe2e8` | `09 52 9a 52` | mov w9,#0xd290 | `FALL_THROUGH`
<a id="insn-00afe2ec"></a> `00afe2ec` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00afe2f0"></a> `00afe2f0` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe2f4"></a> `00afe2f4` | `16 09 00 91` | add x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00afe2f8"></a> `00afe2f8` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe2fc"></a> `00afe2fc` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe300"></a> `00afe300` | `13 69 a9 b8` | ldrsw x19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe304"></a> `00afe304` | `6d 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe308"></a> `00afe308` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00afe30c"></a> `00afe30c` | `e9 0c 00 b0` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-00afe310"></a> `00afe310` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe314"></a> `00afe314` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe318"></a> `00afe318` | `29 39 41 f9` | ldr x9,[x9, #0x270] | `FALL_THROUGH`
<a id="insn-00afe31c"></a> `00afe31c` | `28 79 a8 b8` | ldrsw x8,[x9, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00afe320"></a> `00afe320` | `a9 00 80 d2` | mov x9,#0x5 | `FALL_THROUGH`
<a id="insn-00afe324"></a> `00afe324` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00afe328"></a> `00afe328` | `08 25 13 9b` | madd x8,x8,x19,x9 | `FALL_THROUGH`
<a id="insn-00afe32c"></a> `00afe32c` | `e9 e7 03 b2` | orr x9,xzr,#0x6666666666666666 | `FALL_THROUGH`
<a id="insn-00afe330"></a> `00afe330` | `e9 cc 8c f2` | movk x9,#0x6667 | `FALL_THROUGH`
<a id="insn-00afe334"></a> `00afe334` | `08 7d 49 9b` | smulh x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe338"></a> `00afe338` | `09 fd 42 93` | asr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00afe33c"></a> `00afe33c` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe340"></a> `00afe340` | `5e 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe344"></a> `00afe344` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe348"></a> `00afe348` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe34c"></a> `00afe34c` | `25 a4 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe350"></a> `00afe350` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe354"></a> `00afe354` | `59 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe358"></a> `00afe358` | `14 01 00 37` | tbnz w20,#0x0,0x00afe378 | `CONDITIONAL_JUMP`
<a id="insn-00afe35c"></a> `00afe35c` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe360"></a> `00afe360` | `09 5b 9a 52` | mov w9,#0xd2d8 | `FALL_THROUGH`
<a id="insn-00afe364"></a> `00afe364` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe368"></a> `00afe368` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe36c"></a> `00afe36c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe370"></a> `00afe370` | `08 01 00 35` | cbnz w8,0x00afe390 | `CONDITIONAL_JUMP`
<a id="insn-00afe374"></a> `00afe374` | `13 00 00 14` | b 0x00afe3c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe378"></a> `00afe378` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00afe37c"></a> `00afe37c` | `89 e4 9e 52` | mov w9,#0xf724 | `FALL_THROUGH`
<a id="insn-00afe380"></a> `00afe380` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe384"></a> `00afe384` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe388"></a> `00afe388` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe38c"></a> `00afe38c` | `a8 01 00 34` | cbz w8,0x00afe3c0 | `CONDITIONAL_JUMP`
<a id="insn-00afe390"></a> `00afe390` | `4a 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe394"></a> `00afe394` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe398"></a> `00afe398` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe39c"></a> `00afe39c` | `11 a4 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3a0"></a> `00afe3a0` | `c0 02 00 37` | tbnz w0,#0x0,0x00afe3f8 | `CONDITIONAL_JUMP`
<a id="insn-00afe3a4"></a> `00afe3a4` | `45 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3a8"></a> `00afe3a8` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe3ac"></a> `00afe3ac` | `89 74 9a 52` | mov w9,#0xd3a4 | `FALL_THROUGH`
<a id="insn-00afe3b0"></a> `00afe3b0` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe3b4"></a> `00afe3b4` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe3b8"></a> `00afe3b8` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe3bc"></a> `00afe3bc` | `e8 01 00 34` | cbz w8,0x00afe3f8 | `CONDITIONAL_JUMP`
<a id="insn-00afe3c0"></a> `00afe3c0` | `3e 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3c4"></a> `00afe3c4` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe3c8"></a> `00afe3c8` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe3cc"></a> `00afe3cc` | `05 a4 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3d0"></a> `00afe3d0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe3d4"></a> `00afe3d4` | `39 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3d8"></a> `00afe3d8` | `74 02 00 37` | tbnz w20,#0x0,0x00afe424 | `CONDITIONAL_JUMP`
<a id="insn-00afe3dc"></a> `00afe3dc` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe3e0"></a> `00afe3e0` | `09 5b 9a 52` | mov w9,#0xd2d8 | `FALL_THROUGH`
<a id="insn-00afe3e4"></a> `00afe3e4` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe3e8"></a> `00afe3e8` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe3ec"></a> `00afe3ec` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe3f0"></a> `00afe3f0` | `68 02 00 35` | cbnz w8,0x00afe43c | `CONDITIONAL_JUMP`
<a id="insn-00afe3f4"></a> `00afe3f4` | `2a 00 00 14` | b 0x00afe49c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe3f8"></a> `00afe3f8` | `30 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe3fc"></a> `00afe3fc` | `15 dc 94 52` | mov w21,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00afe400"></a> `00afe400` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-00afe404"></a> `00afe404` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe408"></a> `00afe408` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe40c"></a> `00afe40c` | `b2 eb fe 97` | bl 0x00ab92d4 | `UNCONDITIONAL_CALL`
<a id="insn-00afe410"></a> `00afe410` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe414"></a> `00afe414` | `29 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe418"></a> `00afe418` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe41c"></a> `00afe41c` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-00afe420"></a> `00afe420` | `66 00 00 14` | b 0x00afe5b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe424"></a> `00afe424` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00afe428"></a> `00afe428` | `89 e4 9e 52` | mov w9,#0xf724 | `FALL_THROUGH`
<a id="insn-00afe42c"></a> `00afe42c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe430"></a> `00afe430` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe434"></a> `00afe434` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe438"></a> `00afe438` | `28 03 00 34` | cbz w8,0x00afe49c | `CONDITIONAL_JUMP`
<a id="insn-00afe43c"></a> `00afe43c` | `1f 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe440"></a> `00afe440` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe444"></a> `00afe444` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe448"></a> `00afe448` | `e6 a3 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe44c"></a> `00afe44c` | `80 02 00 37` | tbnz w0,#0x0,0x00afe49c | `CONDITIONAL_JUMP`
<a id="insn-00afe450"></a> `00afe450` | `1a 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe454"></a> `00afe454` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe458"></a> `00afe458` | `89 74 9a 52` | mov w9,#0xd3a4 | `FALL_THROUGH`
<a id="insn-00afe45c"></a> `00afe45c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe460"></a> `00afe460` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe464"></a> `00afe464` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe468"></a> `00afe468` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afe46c"></a> `00afe46c` | `81 01 00 54` | b.ne 0x00afe49c | `CONDITIONAL_JUMP`
<a id="insn-00afe470"></a> `00afe470` | `12 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe474"></a> `00afe474` | `15 dc 94 52` | mov w21,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00afe478"></a> `00afe478` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00afe47c"></a> `00afe47c` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe480"></a> `00afe480` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe484"></a> `00afe484` | `94 eb fe 97` | bl 0x00ab92d4 | `UNCONDITIONAL_CALL`
<a id="insn-00afe488"></a> `00afe488` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe48c"></a> `00afe48c` | `0b 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe490"></a> `00afe490` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe494"></a> `00afe494` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00afe498"></a> `00afe498` | `48 00 00 14` | b 0x00afe5b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe49c"></a> `00afe49c` | `07 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4a0"></a> `00afe4a0` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe4a4"></a> `00afe4a4` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe4a8"></a> `00afe4a8` | `ce a3 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4ac"></a> `00afe4ac` | `80 02 00 37` | tbnz w0,#0x0,0x00afe4fc | `CONDITIONAL_JUMP`
<a id="insn-00afe4b0"></a> `00afe4b0` | `02 4c f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4b4"></a> `00afe4b4` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe4b8"></a> `00afe4b8` | `89 74 9a 52` | mov w9,#0xd3a4 | `FALL_THROUGH`
<a id="insn-00afe4bc"></a> `00afe4bc` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe4c0"></a> `00afe4c0` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe4c4"></a> `00afe4c4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe4c8"></a> `00afe4c8` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00afe4cc"></a> `00afe4cc` | `81 01 00 54` | b.ne 0x00afe4fc | `CONDITIONAL_JUMP`
<a id="insn-00afe4d0"></a> `00afe4d0` | `fa 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4d4"></a> `00afe4d4` | `15 dc 94 52` | mov w21,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00afe4d8"></a> `00afe4d8` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00afe4dc"></a> `00afe4dc` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe4e0"></a> `00afe4e0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe4e4"></a> `00afe4e4` | `7c eb fe 97` | bl 0x00ab92d4 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4e8"></a> `00afe4e8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe4ec"></a> `00afe4ec` | `f3 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe4f0"></a> `00afe4f0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe4f4"></a> `00afe4f4` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00afe4f8"></a> `00afe4f8` | `30 00 00 14` | b 0x00afe5b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe4fc"></a> `00afe4fc` | `ef 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe500"></a> `00afe500` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe504"></a> `00afe504` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe508"></a> `00afe508` | `b6 a3 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe50c"></a> `00afe50c` | `80 02 00 37` | tbnz w0,#0x0,0x00afe55c | `CONDITIONAL_JUMP`
<a id="insn-00afe510"></a> `00afe510` | `ea 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe514"></a> `00afe514` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe518"></a> `00afe518` | `89 74 9a 52` | mov w9,#0xd3a4 | `FALL_THROUGH`
<a id="insn-00afe51c"></a> `00afe51c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe520"></a> `00afe520` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe524"></a> `00afe524` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe528"></a> `00afe528` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00afe52c"></a> `00afe52c` | `81 01 00 54` | b.ne 0x00afe55c | `CONDITIONAL_JUMP`
<a id="insn-00afe530"></a> `00afe530` | `e2 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe534"></a> `00afe534` | `15 dc 94 52` | mov w21,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00afe538"></a> `00afe538` | `e1 02 80 52` | mov w1,#0x17 | `FALL_THROUGH`
<a id="insn-00afe53c"></a> `00afe53c` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe540"></a> `00afe540` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe544"></a> `00afe544` | `64 eb fe 97` | bl 0x00ab92d4 | `UNCONDITIONAL_CALL`
<a id="insn-00afe548"></a> `00afe548` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe54c"></a> `00afe54c` | `db 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe550"></a> `00afe550` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe554"></a> `00afe554` | `e1 02 80 52` | mov w1,#0x17 | `FALL_THROUGH`
<a id="insn-00afe558"></a> `00afe558` | `18 00 00 14` | b 0x00afe5b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe55c"></a> `00afe55c` | `d7 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe560"></a> `00afe560` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00afe564"></a> `00afe564` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe568"></a> `00afe568` | `9e a3 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe56c"></a> `00afe56c` | `80 09 00 37` | tbnz w0,#0x0,0x00afe69c | `CONDITIONAL_JUMP`
<a id="insn-00afe570"></a> `00afe570` | `d2 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe574"></a> `00afe574` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00afe578"></a> `00afe578` | `89 74 9a 52` | mov w9,#0xd3a4 | `FALL_THROUGH`
<a id="insn-00afe57c"></a> `00afe57c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00afe580"></a> `00afe580` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe584"></a> `00afe584` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe588"></a> `00afe588` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00afe58c"></a> `00afe58c` | `81 08 00 54` | b.ne 0x00afe69c | `CONDITIONAL_JUMP`
<a id="insn-00afe590"></a> `00afe590` | `ca 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe594"></a> `00afe594` | `15 dc 94 52` | mov w21,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00afe598"></a> `00afe598` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00afe59c"></a> `00afe59c` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe5a0"></a> `00afe5a0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe5a4"></a> `00afe5a4` | `4c eb fe 97` | bl 0x00ab92d4 | `UNCONDITIONAL_CALL`
<a id="insn-00afe5a8"></a> `00afe5a8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afe5ac"></a> `00afe5ac` | `c3 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe5b0"></a> `00afe5b0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00afe5b4"></a> `00afe5b4` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00afe5b8"></a> `00afe5b8` | `b2 ea fe 97` | bl 0x00ab9080 | `UNCONDITIONAL_CALL`
<a id="insn-00afe5bc"></a> `00afe5bc` | `88 02 00 4b` | sub w8,w20,w0 | `FALL_THROUGH`
<a id="insn-00afe5c0"></a> `00afe5c0` | `69 e1 9a d2` | mov x9,#0xd70b | `FALL_THROUGH`
<a id="insn-00afe5c4"></a> `00afe5c4` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00afe5c8"></a> `00afe5c8` | `69 14 ae f2` | movk x9,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe5cc"></a> `00afe5cc` | `a9 47 c1 f2` | movk x9,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00afe5d0"></a> `00afe5d0` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe5d4"></a> `00afe5d4` | `e9 7a f4 f2` | movk x9,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00afe5d8"></a> `00afe5d8` | `09 7d 49 9b` | smulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe5dc"></a> `00afe5dc` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe5e0"></a> `00afe5e0` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe5e4"></a> `00afe5e4` | `28 fd 48 8b` | add x8,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe5e8"></a> `00afe5e8` | `13 01 13 8b` | add x19,x8,x19 | `FALL_THROUGH`
<a id="insn-00afe5ec"></a> `00afe5ec` | `2c 00 00 14` | b 0x00afe69c | `UNCONDITIONAL_JUMP`
<a id="insn-00afe5f0"></a> `00afe5f0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afe5f4"></a> `00afe5f4` | `21 10 f4 97` | bl 0x00802678 | `UNCONDITIONAL_CALL`
<a id="insn-00afe5f8"></a> `00afe5f8` | `1f 24 00 31` | cmn w0,#0x9 | `FALL_THROUGH`
<a id="insn-00afe5fc"></a> `00afe5fc` | `e0 00 00 54` | b.eq 0x00afe618 | `CONDITIONAL_JUMP`
<a id="insn-00afe600"></a> `00afe600` | `ae 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe604"></a> `00afe604` | `9b f5 f2 97` | bl 0x007bbc70 | `UNCONDITIONAL_CALL`
<a id="insn-00afe608"></a> `00afe608` | `80 00 00 37` | tbnz w0,#0x0,0x00afe618 | `CONDITIONAL_JUMP`
<a id="insn-00afe60c"></a> `00afe60c` | `ab 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe610"></a> `00afe610` | `4b c5 f3 97` | bl 0x007efb3c | `UNCONDITIONAL_CALL`
<a id="insn-00afe614"></a> `00afe614` | `60 01 00 36` | tbz w0,#0x0,0x00afe640 | `CONDITIONAL_JUMP`
<a id="insn-00afe618"></a> `00afe618` | `13 02 80 52` | mov w19,#0x10 | `FALL_THROUGH`
<a id="insn-00afe61c"></a> `00afe61c` | `a7 4b f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afe620"></a> `00afe620` | `08 c9 82 52` | mov w8,#0x1648 | `FALL_THROUGH`
<a id="insn-00afe624"></a> `00afe624` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afe628"></a> `00afe628` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00afe62c"></a> `00afe62c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00afe630"></a> `00afe630` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00afe634"></a> `00afe634` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00afe638"></a> `00afe638` | `91 2d ee 97` | bl 0x00689c7c | `UNCONDITIONAL_CALL`
<a id="insn-00afe63c"></a> `00afe63c` | `17 00 17 0b` | add w23,w0,w23 | `FALL_THROUGH`
<a id="insn-00afe640"></a> `00afe640` | `53 ff 59 8b` | add x19,x26,x25, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe644"></a> `00afe644` | `ff 06 00 71` | cmp w23,#0x1 | `FALL_THROUGH`
<a id="insn-00afe648"></a> `00afe648` | `eb 00 00 54` | b.lt 0x00afe664 | `CONDITIONAL_JUMP`
<a id="insn-00afe64c"></a> `00afe64c` | `e8 92 01 11` | add w8,w23,#0x64 | `FALL_THROUGH`
<a id="insn-00afe650"></a> `00afe650` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe654"></a> `00afe654` | `09 7d 58 9b` | smulh x9,x8,x24 | `FALL_THROUGH`
<a id="insn-00afe658"></a> `00afe658` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe65c"></a> `00afe65c` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe660"></a> `00afe660` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe664"></a> `00afe664` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00afe668"></a> `00afe668` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00afe66c"></a> `00afe66c` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00afe670"></a> `00afe670` | `e3 08 80 52` | mov w3,#0x47 | `FALL_THROUGH`
<a id="insn-00afe674"></a> `00afe674` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00afe678"></a> `00afe678` | `12 00 00 94` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00afe67c"></a> `00afe67c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afe680"></a> `00afe680` | `eb 00 00 54` | b.lt 0x00afe69c | `CONDITIONAL_JUMP`
<a id="insn-00afe684"></a> `00afe684` | `08 90 01 11` | add w8,w0,#0x64 | `FALL_THROUGH`
<a id="insn-00afe688"></a> `00afe688` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00afe68c"></a> `00afe68c` | `09 7d 58 9b` | smulh x9,x8,x24 | `FALL_THROUGH`
<a id="insn-00afe690"></a> `00afe690` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00afe694"></a> `00afe694` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00afe698"></a> `00afe698` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00afe69c"></a> `00afe69c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00afe6a0"></a> `00afe6a0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afe6a4"></a> `00afe6a4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afe6a8"></a> `00afe6a8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afe6ac"></a> `00afe6ac` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afe6b0"></a> `00afe6b0` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afe6b4"></a> `00afe6b4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afe6b8"></a> `00afe6b8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afe6bc"></a> `00afe6bc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdfe4`](#insn-00afdfe4) 範囲 `[['00afdfe4', '00afe033']]`
  - `CONDITIONAL_JUMP` [`00afe030`](#insn-00afe030) → [`00afe124`](#insn-00afe124)
  - `FALL_THROUGH` [`00afe030`](#insn-00afe030) → [`00afe034`](#insn-00afe034)
- ブロック [`00afe034`](#insn-00afe034) 範囲 `[['00afe034', '00afe04b']]`
  - `CONDITIONAL_JUMP` [`00afe048`](#insn-00afe048) → [`00afe060`](#insn-00afe060)
  - `FALL_THROUGH` [`00afe048`](#insn-00afe048) → [`00afe04c`](#insn-00afe04c)
- ブロック [`00afe04c`](#insn-00afe04c) 範囲 `[['00afe04c', '00afe05f']]`
  - `CONDITIONAL_JUMP` [`00afe05c`](#insn-00afe05c) → [`00afe2e0`](#insn-00afe2e0)
  - `FALL_THROUGH` [`00afe05c`](#insn-00afe05c) → [`00afe060`](#insn-00afe060)
- ブロック [`00afe060`](#insn-00afe060) 範囲 `[['00afe060', '00afe0df']]`
  - `CONDITIONAL_JUMP` [`00afe0dc`](#insn-00afe0dc) → [`00afe340`](#insn-00afe340)
  - `FALL_THROUGH` [`00afe0dc`](#insn-00afe0dc) → [`00afe0e0`](#insn-00afe0e0)
- ブロック [`00afe0e0`](#insn-00afe0e0) 範囲 `[['00afe0e0', '00afe123']]`
  - `UNCONDITIONAL_JUMP` [`00afe120`](#insn-00afe120) → [`00afe33c`](#insn-00afe33c)
- ブロック [`00afe124`](#insn-00afe124) 範囲 `[['00afe124', '00afe13b']]`
  - `CONDITIONAL_JUMP` [`00afe138`](#insn-00afe138) → [`00afe1bc`](#insn-00afe1bc)
  - `FALL_THROUGH` [`00afe138`](#insn-00afe138) → [`00afe13c`](#insn-00afe13c)
- ブロック [`00afe13c`](#insn-00afe13c) 範囲 `[['00afe13c', '00afe187']]`
  - `CONDITIONAL_JUMP` [`00afe184`](#insn-00afe184) → [`00afe264`](#insn-00afe264)
  - `FALL_THROUGH` [`00afe184`](#insn-00afe184) → [`00afe188`](#insn-00afe188)
- ブロック [`00afe188`](#insn-00afe188) 範囲 `[['00afe188', '00afe1bb']]`
  - `UNCONDITIONAL_JUMP` [`00afe1b8`](#insn-00afe1b8) → [`00afe1c0`](#insn-00afe1c0)
- ブロック [`00afe1bc`](#insn-00afe1bc) 範囲 `[['00afe1bc', '00afe1bf']]`
  - `FALL_THROUGH` [`00afe1bc`](#insn-00afe1bc) → [`00afe1c0`](#insn-00afe1c0)
- ブロック [`00afe1c0`](#insn-00afe1c0) 範囲 `[['00afe1c0', '00afe243']]`
  - `CONDITIONAL_JUMP` [`00afe240`](#insn-00afe240) → [`00afe640`](#insn-00afe640)
  - `FALL_THROUGH` [`00afe240`](#insn-00afe240) → [`00afe244`](#insn-00afe244)
- ブロック [`00afe244`](#insn-00afe244) 範囲 `[['00afe244', '00afe24f']]`
  - `CONDITIONAL_JUMP` [`00afe24c`](#insn-00afe24c) → [`00afe25c`](#insn-00afe25c)
  - `FALL_THROUGH` [`00afe24c`](#insn-00afe24c) → [`00afe250`](#insn-00afe250)
- ブロック [`00afe250`](#insn-00afe250) 範囲 `[['00afe250', '00afe25b']]`
  - `CONDITIONAL_JUMP` [`00afe258`](#insn-00afe258) → [`00afe5f0`](#insn-00afe5f0)
  - `FALL_THROUGH` [`00afe258`](#insn-00afe258) → [`00afe25c`](#insn-00afe25c)
- ブロック [`00afe25c`](#insn-00afe25c) 範囲 `[['00afe25c', '00afe263']]`
  - `UNCONDITIONAL_JUMP` [`00afe260`](#insn-00afe260) → [`00afe61c`](#insn-00afe61c)
- ブロック [`00afe264`](#insn-00afe264) 範囲 `[['00afe264', '00afe27b']]`
  - `UNCONDITIONAL_JUMP` [`00afe278`](#insn-00afe278) → [`00afe288`](#insn-00afe288)
- ブロック [`00afe27c`](#insn-00afe27c) 範囲 `[['00afe27c', '00afe287']]`
  - `CONDITIONAL_JUMP` [`00afe284`](#insn-00afe284) → [`00afe188`](#insn-00afe188)
  - `FALL_THROUGH` [`00afe284`](#insn-00afe284) → [`00afe288`](#insn-00afe288)
- ブロック [`00afe288`](#insn-00afe288) 範囲 `[['00afe288', '00afe293']]`
  - `CONDITIONAL_JUMP` [`00afe290`](#insn-00afe290) → [`00afe27c`](#insn-00afe27c)
  - `FALL_THROUGH` [`00afe290`](#insn-00afe290) → [`00afe294`](#insn-00afe294)
- ブロック [`00afe294`](#insn-00afe294) 範囲 `[['00afe294', '00afe2df']]`
  - `UNCONDITIONAL_JUMP` [`00afe2dc`](#insn-00afe2dc) → [`00afe27c`](#insn-00afe27c)
- ブロック [`00afe2e0`](#insn-00afe2e0) 範囲 `[['00afe2e0', '00afe33b']]`
  - `FALL_THROUGH` [`00afe338`](#insn-00afe338) → [`00afe33c`](#insn-00afe33c)
- ブロック [`00afe33c`](#insn-00afe33c) 範囲 `[['00afe33c', '00afe33f']]`
  - `FALL_THROUGH` [`00afe33c`](#insn-00afe33c) → [`00afe340`](#insn-00afe340)
- ブロック [`00afe340`](#insn-00afe340) 範囲 `[['00afe340', '00afe35b']]`
  - `CONDITIONAL_JUMP` [`00afe358`](#insn-00afe358) → [`00afe378`](#insn-00afe378)
  - `FALL_THROUGH` [`00afe358`](#insn-00afe358) → [`00afe35c`](#insn-00afe35c)
- ブロック [`00afe35c`](#insn-00afe35c) 範囲 `[['00afe35c', '00afe373']]`
  - `CONDITIONAL_JUMP` [`00afe370`](#insn-00afe370) → [`00afe390`](#insn-00afe390)
  - `FALL_THROUGH` [`00afe370`](#insn-00afe370) → [`00afe374`](#insn-00afe374)
- ブロック [`00afe374`](#insn-00afe374) 範囲 `[['00afe374', '00afe377']]`
  - `UNCONDITIONAL_JUMP` [`00afe374`](#insn-00afe374) → [`00afe3c0`](#insn-00afe3c0)
- ブロック [`00afe378`](#insn-00afe378) 範囲 `[['00afe378', '00afe38f']]`
  - `CONDITIONAL_JUMP` [`00afe38c`](#insn-00afe38c) → [`00afe3c0`](#insn-00afe3c0)
  - `FALL_THROUGH` [`00afe38c`](#insn-00afe38c) → [`00afe390`](#insn-00afe390)
- ブロック [`00afe390`](#insn-00afe390) 範囲 `[['00afe390', '00afe3a3']]`
  - `CONDITIONAL_JUMP` [`00afe3a0`](#insn-00afe3a0) → [`00afe3f8`](#insn-00afe3f8)
  - `FALL_THROUGH` [`00afe3a0`](#insn-00afe3a0) → [`00afe3a4`](#insn-00afe3a4)
- ブロック [`00afe3a4`](#insn-00afe3a4) 範囲 `[['00afe3a4', '00afe3bf']]`
  - `CONDITIONAL_JUMP` [`00afe3bc`](#insn-00afe3bc) → [`00afe3f8`](#insn-00afe3f8)
  - `FALL_THROUGH` [`00afe3bc`](#insn-00afe3bc) → [`00afe3c0`](#insn-00afe3c0)
- ブロック [`00afe3c0`](#insn-00afe3c0) 範囲 `[['00afe3c0', '00afe3db']]`
  - `CONDITIONAL_JUMP` [`00afe3d8`](#insn-00afe3d8) → [`00afe424`](#insn-00afe424)
  - `FALL_THROUGH` [`00afe3d8`](#insn-00afe3d8) → [`00afe3dc`](#insn-00afe3dc)
- ブロック [`00afe3dc`](#insn-00afe3dc) 範囲 `[['00afe3dc', '00afe3f3']]`
  - `CONDITIONAL_JUMP` [`00afe3f0`](#insn-00afe3f0) → [`00afe43c`](#insn-00afe43c)
  - `FALL_THROUGH` [`00afe3f0`](#insn-00afe3f0) → [`00afe3f4`](#insn-00afe3f4)
- ブロック [`00afe3f4`](#insn-00afe3f4) 範囲 `[['00afe3f4', '00afe3f7']]`
  - `UNCONDITIONAL_JUMP` [`00afe3f4`](#insn-00afe3f4) → [`00afe49c`](#insn-00afe49c)
- ブロック [`00afe3f8`](#insn-00afe3f8) 範囲 `[['00afe3f8', '00afe423']]`
  - `UNCONDITIONAL_JUMP` [`00afe420`](#insn-00afe420) → [`00afe5b8`](#insn-00afe5b8)
- ブロック [`00afe424`](#insn-00afe424) 範囲 `[['00afe424', '00afe43b']]`
  - `CONDITIONAL_JUMP` [`00afe438`](#insn-00afe438) → [`00afe49c`](#insn-00afe49c)
  - `FALL_THROUGH` [`00afe438`](#insn-00afe438) → [`00afe43c`](#insn-00afe43c)
- ブロック [`00afe43c`](#insn-00afe43c) 範囲 `[['00afe43c', '00afe44f']]`
  - `CONDITIONAL_JUMP` [`00afe44c`](#insn-00afe44c) → [`00afe49c`](#insn-00afe49c)
  - `FALL_THROUGH` [`00afe44c`](#insn-00afe44c) → [`00afe450`](#insn-00afe450)
- ブロック [`00afe450`](#insn-00afe450) 範囲 `[['00afe450', '00afe46f']]`
  - `CONDITIONAL_JUMP` [`00afe46c`](#insn-00afe46c) → [`00afe49c`](#insn-00afe49c)
  - `FALL_THROUGH` [`00afe46c`](#insn-00afe46c) → [`00afe470`](#insn-00afe470)
- ブロック [`00afe470`](#insn-00afe470) 範囲 `[['00afe470', '00afe49b']]`
  - `UNCONDITIONAL_JUMP` [`00afe498`](#insn-00afe498) → [`00afe5b8`](#insn-00afe5b8)
- ブロック [`00afe49c`](#insn-00afe49c) 範囲 `[['00afe49c', '00afe4af']]`
  - `CONDITIONAL_JUMP` [`00afe4ac`](#insn-00afe4ac) → [`00afe4fc`](#insn-00afe4fc)
  - `FALL_THROUGH` [`00afe4ac`](#insn-00afe4ac) → [`00afe4b0`](#insn-00afe4b0)
- ブロック [`00afe4b0`](#insn-00afe4b0) 範囲 `[['00afe4b0', '00afe4cf']]`
  - `CONDITIONAL_JUMP` [`00afe4cc`](#insn-00afe4cc) → [`00afe4fc`](#insn-00afe4fc)
  - `FALL_THROUGH` [`00afe4cc`](#insn-00afe4cc) → [`00afe4d0`](#insn-00afe4d0)
- ブロック [`00afe4d0`](#insn-00afe4d0) 範囲 `[['00afe4d0', '00afe4fb']]`
  - `UNCONDITIONAL_JUMP` [`00afe4f8`](#insn-00afe4f8) → [`00afe5b8`](#insn-00afe5b8)
- ブロック [`00afe4fc`](#insn-00afe4fc) 範囲 `[['00afe4fc', '00afe50f']]`
  - `CONDITIONAL_JUMP` [`00afe50c`](#insn-00afe50c) → [`00afe55c`](#insn-00afe55c)
  - `FALL_THROUGH` [`00afe50c`](#insn-00afe50c) → [`00afe510`](#insn-00afe510)
- ブロック [`00afe510`](#insn-00afe510) 範囲 `[['00afe510', '00afe52f']]`
  - `CONDITIONAL_JUMP` [`00afe52c`](#insn-00afe52c) → [`00afe55c`](#insn-00afe55c)
  - `FALL_THROUGH` [`00afe52c`](#insn-00afe52c) → [`00afe530`](#insn-00afe530)
- ブロック [`00afe530`](#insn-00afe530) 範囲 `[['00afe530', '00afe55b']]`
  - `UNCONDITIONAL_JUMP` [`00afe558`](#insn-00afe558) → [`00afe5b8`](#insn-00afe5b8)
- ブロック [`00afe55c`](#insn-00afe55c) 範囲 `[['00afe55c', '00afe56f']]`
  - `CONDITIONAL_JUMP` [`00afe56c`](#insn-00afe56c) → [`00afe69c`](#insn-00afe69c)
  - `FALL_THROUGH` [`00afe56c`](#insn-00afe56c) → [`00afe570`](#insn-00afe570)
- ブロック [`00afe570`](#insn-00afe570) 範囲 `[['00afe570', '00afe58f']]`
  - `CONDITIONAL_JUMP` [`00afe58c`](#insn-00afe58c) → [`00afe69c`](#insn-00afe69c)
  - `FALL_THROUGH` [`00afe58c`](#insn-00afe58c) → [`00afe590`](#insn-00afe590)
- ブロック [`00afe590`](#insn-00afe590) 範囲 `[['00afe590', '00afe5b7']]`
  - `FALL_THROUGH` [`00afe5b4`](#insn-00afe5b4) → [`00afe5b8`](#insn-00afe5b8)
- ブロック [`00afe5b8`](#insn-00afe5b8) 範囲 `[['00afe5b8', '00afe5ef']]`
  - `UNCONDITIONAL_JUMP` [`00afe5ec`](#insn-00afe5ec) → [`00afe69c`](#insn-00afe69c)
- ブロック [`00afe5f0`](#insn-00afe5f0) 範囲 `[['00afe5f0', '00afe5ff']]`
  - `CONDITIONAL_JUMP` [`00afe5fc`](#insn-00afe5fc) → [`00afe618`](#insn-00afe618)
  - `FALL_THROUGH` [`00afe5fc`](#insn-00afe5fc) → [`00afe600`](#insn-00afe600)
- ブロック [`00afe600`](#insn-00afe600) 範囲 `[['00afe600', '00afe60b']]`
  - `CONDITIONAL_JUMP` [`00afe608`](#insn-00afe608) → [`00afe618`](#insn-00afe618)
  - `FALL_THROUGH` [`00afe608`](#insn-00afe608) → [`00afe60c`](#insn-00afe60c)
- ブロック [`00afe60c`](#insn-00afe60c) 範囲 `[['00afe60c', '00afe617']]`
  - `CONDITIONAL_JUMP` [`00afe614`](#insn-00afe614) → [`00afe640`](#insn-00afe640)
  - `FALL_THROUGH` [`00afe614`](#insn-00afe614) → [`00afe618`](#insn-00afe618)
- ブロック [`00afe618`](#insn-00afe618) 範囲 `[['00afe618', '00afe61b']]`
  - `FALL_THROUGH` [`00afe618`](#insn-00afe618) → [`00afe61c`](#insn-00afe61c)
- ブロック [`00afe61c`](#insn-00afe61c) 範囲 `[['00afe61c', '00afe63f']]`
  - `FALL_THROUGH` [`00afe63c`](#insn-00afe63c) → [`00afe640`](#insn-00afe640)
- ブロック [`00afe640`](#insn-00afe640) 範囲 `[['00afe640', '00afe64b']]`
  - `CONDITIONAL_JUMP` [`00afe648`](#insn-00afe648) → [`00afe664`](#insn-00afe664)
  - `FALL_THROUGH` [`00afe648`](#insn-00afe648) → [`00afe64c`](#insn-00afe64c)
- ブロック [`00afe64c`](#insn-00afe64c) 範囲 `[['00afe64c', '00afe663']]`
  - `FALL_THROUGH` [`00afe660`](#insn-00afe660) → [`00afe664`](#insn-00afe664)
- ブロック [`00afe664`](#insn-00afe664) 範囲 `[['00afe664', '00afe683']]`
  - `CONDITIONAL_JUMP` [`00afe680`](#insn-00afe680) → [`00afe69c`](#insn-00afe69c)
  - `FALL_THROUGH` [`00afe680`](#insn-00afe680) → [`00afe684`](#insn-00afe684)
- ブロック [`00afe684`](#insn-00afe684) 範囲 `[['00afe684', '00afe69b']]`
  - `FALL_THROUGH` [`00afe698`](#insn-00afe698) → [`00afe69c`](#insn-00afe69c)
- ブロック [`00afe69c`](#insn-00afe69c) 範囲 `[['00afe69c', '00afe6bf']]`

## 命令位置別の参照

- [`00afdfe8`](#insn-00afdfe8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfec`](#insn-00afdfec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff0`](#insn-00afdff0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff4`](#insn-00afdff4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdff8`](#insn-00afdff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdffc`](#insn-00afdffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe018`](#insn-00afe018) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe02c`](#insn-00afe02c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe030`](#insn-00afe030) → [`00afe124`](#insn-00afe124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe034`](#insn-00afe034) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe040`](#insn-00afe040) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00afe048`](#insn-00afe048) → [`00afe060`](#insn-00afe060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe04c`](#insn-00afe04c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe058`](#insn-00afe058) → `003380e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00afe05c`](#insn-00afe05c) → [`00afe2e0`](#insn-00afe2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe060`](#insn-00afe060) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe06c`](#insn-00afe06c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00afe070`](#insn-00afe070) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe08c`](#insn-00afe08c) → `0023d290`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe090`](#insn-00afe090) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe0ac`](#insn-00afe0ac) → [`00a64340`](../00a64/00a64340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a64340` · 推定シンボル `None` · 推定型 `None`
- [`00afe0dc`](#insn-00afe0dc) → [`00afe340`](#insn-00afe340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe0e0`](#insn-00afe0e0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe0ec`](#insn-00afe0ec) → [`00802b18`](../00802/00802b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b18` · 推定シンボル `None` · 推定型 `None`
- [`00afe0f4`](#insn-00afe0f4) → [`00802ea0`](../00802/00802ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802ea0` · 推定シンボル `None` · 推定型 `None`
- [`00afe108`](#insn-00afe108) → [`00801d4c`](../00801/00801d4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00801d4c` · 推定シンボル `None` · 推定型 `None`
- [`00afe120`](#insn-00afe120) → [`00afe33c`](#insn-00afe33c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe138`](#insn-00afe138) → [`00afe1bc`](#insn-00afe1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe140`](#insn-00afe140) → `Stack[-0x74]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe148`](#insn-00afe148) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe150`](#insn-00afe150) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe164`](#insn-00afe164) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe184`](#insn-00afe184) → [`00afe264`](#insn-00afe264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe190`](#insn-00afe190) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe198`](#insn-00afe198) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe19c`](#insn-00afe19c) → `Stack[-0x74]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe1b8`](#insn-00afe1b8) → [`00afe1c0`](#insn-00afe1c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe1c0`](#insn-00afe1c0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe1d0`](#insn-00afe1d0) → [`00ab9080`](../00ab9/00ab9080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab9080` · 推定シンボル `None` · 推定型 `None`
- [`00afe1f0`](#insn-00afe1f0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe204`](#insn-00afe204) → [`008c2ce0`](../008c2/008c2ce0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c2ce0` · 推定シンボル `None` · 推定型 `None`
- [`00afe234`](#insn-00afe234) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00afe240`](#insn-00afe240) → [`00afe640`](#insn-00afe640) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe248`](#insn-00afe248) → [`00802678`](../00802/00802678.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802678` · 推定シンボル `None` · 推定型 `None`
- [`00afe24c`](#insn-00afe24c) → [`00afe25c`](#insn-00afe25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe250`](#insn-00afe250) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe254`](#insn-00afe254) → [`007bbbec`](../007bb/007bbbec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bbbec` · 推定シンボル `None` · 推定型 `None`
- [`00afe258`](#insn-00afe258) → [`00afe5f0`](#insn-00afe5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe260`](#insn-00afe260) → [`00afe61c`](#insn-00afe61c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe278`](#insn-00afe278) → [`00afe288`](#insn-00afe288) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe284`](#insn-00afe284) → [`00afe188`](#insn-00afe188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe288`](#insn-00afe288) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe290`](#insn-00afe290) → [`00afe27c`](#insn-00afe27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe2a4`](#insn-00afe2a4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe2c4`](#insn-00afe2c4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe2d0`](#insn-00afe2d0) → `00454bb4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe2dc`](#insn-00afe2dc) → [`00afe27c`](#insn-00afe27c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe2e0`](#insn-00afe2e0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe300`](#insn-00afe300) → `0023d290`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe304`](#insn-00afe304) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe314`](#insn-00afe314) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00afe318`](#insn-00afe318) → `00c9b270`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afe31c`](#insn-00afe31c) → `00ca413c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe340`](#insn-00afe340) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe34c`](#insn-00afe34c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe354`](#insn-00afe354) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe358`](#insn-00afe358) → [`00afe378`](#insn-00afe378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe36c`](#insn-00afe36c) → `0023d2d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe370`](#insn-00afe370) → [`00afe390`](#insn-00afe390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe374`](#insn-00afe374) → [`00afe3c0`](#insn-00afe3c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe38c`](#insn-00afe38c) → [`00afe3c0`](#insn-00afe3c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe390`](#insn-00afe390) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe39c`](#insn-00afe39c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe3a0`](#insn-00afe3a0) → [`00afe3f8`](#insn-00afe3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe3a4`](#insn-00afe3a4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe3b8`](#insn-00afe3b8) → `0023d3a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe3bc`](#insn-00afe3bc) → [`00afe3f8`](#insn-00afe3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe3c0`](#insn-00afe3c0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe3cc`](#insn-00afe3cc) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe3d4`](#insn-00afe3d4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe3d8`](#insn-00afe3d8) → [`00afe424`](#insn-00afe424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe3ec`](#insn-00afe3ec) → `0023d2d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe3f0`](#insn-00afe3f0) → [`00afe43c`](#insn-00afe43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe3f4`](#insn-00afe3f4) → [`00afe49c`](#insn-00afe49c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe3f8`](#insn-00afe3f8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe40c`](#insn-00afe40c) → [`00ab92d4`](../00ab9/00ab92d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab92d4` · 推定シンボル `None` · 推定型 `None`
- [`00afe414`](#insn-00afe414) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe420`](#insn-00afe420) → [`00afe5b8`](#insn-00afe5b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe438`](#insn-00afe438) → [`00afe49c`](#insn-00afe49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe43c`](#insn-00afe43c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe448`](#insn-00afe448) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe44c`](#insn-00afe44c) → [`00afe49c`](#insn-00afe49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe450`](#insn-00afe450) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe464`](#insn-00afe464) → `0023d3a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe46c`](#insn-00afe46c) → [`00afe49c`](#insn-00afe49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe470`](#insn-00afe470) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe484`](#insn-00afe484) → [`00ab92d4`](../00ab9/00ab92d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab92d4` · 推定シンボル `None` · 推定型 `None`
- [`00afe48c`](#insn-00afe48c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe498`](#insn-00afe498) → [`00afe5b8`](#insn-00afe5b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe49c`](#insn-00afe49c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe4a8`](#insn-00afe4a8) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe4ac`](#insn-00afe4ac) → [`00afe4fc`](#insn-00afe4fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe4b0`](#insn-00afe4b0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe4c4`](#insn-00afe4c4) → `0023d3a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe4cc`](#insn-00afe4cc) → [`00afe4fc`](#insn-00afe4fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe4d0`](#insn-00afe4d0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe4e4`](#insn-00afe4e4) → [`00ab92d4`](../00ab9/00ab92d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab92d4` · 推定シンボル `None` · 推定型 `None`
- [`00afe4ec`](#insn-00afe4ec) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe4f8`](#insn-00afe4f8) → [`00afe5b8`](#insn-00afe5b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe4fc`](#insn-00afe4fc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe508`](#insn-00afe508) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe50c`](#insn-00afe50c) → [`00afe55c`](#insn-00afe55c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe510`](#insn-00afe510) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe524`](#insn-00afe524) → `0023d3a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe52c`](#insn-00afe52c) → [`00afe55c`](#insn-00afe55c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe530`](#insn-00afe530) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe544`](#insn-00afe544) → [`00ab92d4`](../00ab9/00ab92d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab92d4` · 推定シンボル `None` · 推定型 `None`
- [`00afe54c`](#insn-00afe54c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe558`](#insn-00afe558) → [`00afe5b8`](#insn-00afe5b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe55c`](#insn-00afe55c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe568`](#insn-00afe568) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afe56c`](#insn-00afe56c) → [`00afe69c`](#insn-00afe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe570`](#insn-00afe570) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe584`](#insn-00afe584) → `0023d3a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afe58c`](#insn-00afe58c) → [`00afe69c`](#insn-00afe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe590`](#insn-00afe590) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe5a4`](#insn-00afe5a4) → [`00ab92d4`](../00ab9/00ab92d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab92d4` · 推定シンボル `None` · 推定型 `None`
- [`00afe5ac`](#insn-00afe5ac) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe5b8`](#insn-00afe5b8) → [`00ab9080`](../00ab9/00ab9080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab9080` · 推定シンボル `None` · 推定型 `None`
- [`00afe5ec`](#insn-00afe5ec) → [`00afe69c`](#insn-00afe69c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe5f4`](#insn-00afe5f4) → [`00802678`](../00802/00802678.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802678` · 推定シンボル `None` · 推定型 `None`
- [`00afe5fc`](#insn-00afe5fc) → [`00afe618`](#insn-00afe618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe600`](#insn-00afe600) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe604`](#insn-00afe604) → [`007bbc70`](../007bb/007bbc70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bbc70` · 推定シンボル `None` · 推定型 `None`
- [`00afe608`](#insn-00afe608) → [`00afe618`](#insn-00afe618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe60c`](#insn-00afe60c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe610`](#insn-00afe610) → [`007efb3c`](../007ef/007efb3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007efb3c` · 推定シンボル `None` · 推定型 `None`
- [`00afe614`](#insn-00afe614) → [`00afe640`](#insn-00afe640) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe61c`](#insn-00afe61c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afe638`](#insn-00afe638) → [`00689c7c`](../00689/00689c7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00689c7c` · 推定シンボル `None` · 推定型 `None`
- [`00afe648`](#insn-00afe648) → [`00afe664`](#insn-00afe664) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe678`](#insn-00afe678) → [`00afe6c0`](../00afe/00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00afe680`](#insn-00afe680) → [`00afe69c`](#insn-00afe69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6a0`](#insn-00afe6a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6a4`](#insn-00afe6a4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6a8`](#insn-00afe6a8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6ac`](#insn-00afe6ac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6b0`](#insn-00afe6b0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6b4`](#insn-00afe6b4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdfe8`](#insn-00afdfe8)

~~~json
{
  "source": "00afdfe8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfec`](#insn-00afdfec)

~~~json
{
  "source": "00afdfec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff0`](#insn-00afdff0)

~~~json
{
  "source": "00afdff0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff4`](#insn-00afdff4)

~~~json
{
  "source": "00afdff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdff8`](#insn-00afdff8)

~~~json
{
  "source": "00afdff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdffc`](#insn-00afdffc)

~~~json
{
  "source": "00afdffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe018`](#insn-00afe018)

~~~json
{
  "source": "00afe018",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe02c`](#insn-00afe02c)

~~~json
{
  "source": "00afe02c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe030`](#insn-00afe030)

~~~json
{
  "source": "00afe030",
  "target": "00afe124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe034`](#insn-00afe034)

~~~json
{
  "source": "00afe034",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe040`](#insn-00afe040)

~~~json
{
  "source": "00afe040",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c06a0040780900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00afe048`](#insn-00afe048)

~~~json
{
  "source": "00afe048",
  "target": "00afe060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe04c`](#insn-00afe04c)

~~~json
{
  "source": "00afe04c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe058`](#insn-00afe058)

~~~json
{
  "source": "00afe058",
  "target": "003380e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "5cc17d0054710a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00afe05c`](#insn-00afe05c)

~~~json
{
  "source": "00afe05c",
  "target": "00afe2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe060`](#insn-00afe060)

~~~json
{
  "source": "00afe060",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe06c`](#insn-00afe06c)

~~~json
{
  "source": "00afe06c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c06a0040780900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00afe070`](#insn-00afe070)

~~~json
{
  "source": "00afe070",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe08c`](#insn-00afe08c)

~~~json
{
  "source": "00afe08c",
  "target": "0023d290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6136,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe090`](#insn-00afe090)

~~~json
{
  "source": "00afe090",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0ac`](#insn-00afe0ac)

~~~json
{
  "source": "00afe0ac",
  "target": "00a64340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0dc`](#insn-00afe0dc)

~~~json
{
  "source": "00afe0dc",
  "target": "00afe340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe0e0`](#insn-00afe0e0)

~~~json
{
  "source": "00afe0e0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0ec`](#insn-00afe0ec)

~~~json
{
  "source": "00afe0ec",
  "target": "00802b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0f4`](#insn-00afe0f4)

~~~json
{
  "source": "00afe0f4",
  "target": "00802ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe108`](#insn-00afe108)

~~~json
{
  "source": "00afe108",
  "target": "00801d4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe120`](#insn-00afe120)

~~~json
{
  "source": "00afe120",
  "target": "00afe33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe138`](#insn-00afe138)

~~~json
{
  "source": "00afe138",
  "target": "00afe1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe140`](#insn-00afe140)

~~~json
{
  "source": "00afe140",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe148`](#insn-00afe148)

~~~json
{
  "source": "00afe148",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe150`](#insn-00afe150)

~~~json
{
  "source": "00afe150",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe164`](#insn-00afe164)

~~~json
{
  "source": "00afe164",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe184`](#insn-00afe184)

~~~json
{
  "source": "00afe184",
  "target": "00afe264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe190`](#insn-00afe190)

~~~json
{
  "source": "00afe190",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe198`](#insn-00afe198)

~~~json
{
  "source": "00afe198",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe19c`](#insn-00afe19c)

~~~json
{
  "source": "00afe19c",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe1b8`](#insn-00afe1b8)

~~~json
{
  "source": "00afe1b8",
  "target": "00afe1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe1c0`](#insn-00afe1c0)

~~~json
{
  "source": "00afe1c0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe1d0`](#insn-00afe1d0)

~~~json
{
  "source": "00afe1d0",
  "target": "00ab9080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe1f0`](#insn-00afe1f0)

~~~json
{
  "source": "00afe1f0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe204`](#insn-00afe204)

~~~json
{
  "source": "00afe204",
  "target": "008c2ce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe234`](#insn-00afe234)

~~~json
{
  "source": "00afe234",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe240`](#insn-00afe240)

~~~json
{
  "source": "00afe240",
  "target": "00afe640",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe248`](#insn-00afe248)

~~~json
{
  "source": "00afe248",
  "target": "00802678",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe24c`](#insn-00afe24c)

~~~json
{
  "source": "00afe24c",
  "target": "00afe25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe250`](#insn-00afe250)

~~~json
{
  "source": "00afe250",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe254`](#insn-00afe254)

~~~json
{
  "source": "00afe254",
  "target": "007bbbec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe258`](#insn-00afe258)

~~~json
{
  "source": "00afe258",
  "target": "00afe5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe260`](#insn-00afe260)

~~~json
{
  "source": "00afe260",
  "target": "00afe61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe278`](#insn-00afe278)

~~~json
{
  "source": "00afe278",
  "target": "00afe288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe284`](#insn-00afe284)

~~~json
{
  "source": "00afe284",
  "target": "00afe188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe288`](#insn-00afe288)

~~~json
{
  "source": "00afe288",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe290`](#insn-00afe290)

~~~json
{
  "source": "00afe290",
  "target": "00afe27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe2a4`](#insn-00afe2a4)

~~~json
{
  "source": "00afe2a4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe2c4`](#insn-00afe2c4)

~~~json
{
  "source": "00afe2c4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe2d0`](#insn-00afe2d0)

~~~json
{
  "source": "00afe2d0",
  "target": "00454bb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe2dc`](#insn-00afe2dc)

~~~json
{
  "source": "00afe2dc",
  "target": "00afe27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe2e0`](#insn-00afe2e0)

~~~json
{
  "source": "00afe2e0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe300`](#insn-00afe300)

~~~json
{
  "source": "00afe300",
  "target": "0023d290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6136,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe304`](#insn-00afe304)

~~~json
{
  "source": "00afe304",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe314`](#insn-00afe314)

~~~json
{
  "source": "00afe314",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c06a0040780900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00afe318`](#insn-00afe318)

~~~json
{
  "source": "00afe318",
  "target": "00c9b270",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b270",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afe31c`](#insn-00afe31c)

~~~json
{
  "source": "00afe31c",
  "target": "00ca413c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe340`](#insn-00afe340)

~~~json
{
  "source": "00afe340",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe34c`](#insn-00afe34c)

~~~json
{
  "source": "00afe34c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe354`](#insn-00afe354)

~~~json
{
  "source": "00afe354",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe358`](#insn-00afe358)

~~~json
{
  "source": "00afe358",
  "target": "00afe378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe36c`](#insn-00afe36c)

~~~json
{
  "source": "00afe36c",
  "target": "0023d2d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6208,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe370`](#insn-00afe370)

~~~json
{
  "source": "00afe370",
  "target": "00afe390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe374`](#insn-00afe374)

~~~json
{
  "source": "00afe374",
  "target": "00afe3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe38c`](#insn-00afe38c)

~~~json
{
  "source": "00afe38c",
  "target": "00afe3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe390`](#insn-00afe390)

~~~json
{
  "source": "00afe390",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe39c`](#insn-00afe39c)

~~~json
{
  "source": "00afe39c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe3a0`](#insn-00afe3a0)

~~~json
{
  "source": "00afe3a0",
  "target": "00afe3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe3a4`](#insn-00afe3a4)

~~~json
{
  "source": "00afe3a4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe3b8`](#insn-00afe3b8)

~~~json
{
  "source": "00afe3b8",
  "target": "0023d3a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6412,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe3bc`](#insn-00afe3bc)

~~~json
{
  "source": "00afe3bc",
  "target": "00afe3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe3c0`](#insn-00afe3c0)

~~~json
{
  "source": "00afe3c0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe3cc`](#insn-00afe3cc)

~~~json
{
  "source": "00afe3cc",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe3d4`](#insn-00afe3d4)

~~~json
{
  "source": "00afe3d4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe3d8`](#insn-00afe3d8)

~~~json
{
  "source": "00afe3d8",
  "target": "00afe424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe3ec`](#insn-00afe3ec)

~~~json
{
  "source": "00afe3ec",
  "target": "0023d2d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6208,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe3f0`](#insn-00afe3f0)

~~~json
{
  "source": "00afe3f0",
  "target": "00afe43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe3f4`](#insn-00afe3f4)

~~~json
{
  "source": "00afe3f4",
  "target": "00afe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe3f8`](#insn-00afe3f8)

~~~json
{
  "source": "00afe3f8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe40c`](#insn-00afe40c)

~~~json
{
  "source": "00afe40c",
  "target": "00ab92d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe414`](#insn-00afe414)

~~~json
{
  "source": "00afe414",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe420`](#insn-00afe420)

~~~json
{
  "source": "00afe420",
  "target": "00afe5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe438`](#insn-00afe438)

~~~json
{
  "source": "00afe438",
  "target": "00afe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe43c`](#insn-00afe43c)

~~~json
{
  "source": "00afe43c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe448`](#insn-00afe448)

~~~json
{
  "source": "00afe448",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe44c`](#insn-00afe44c)

~~~json
{
  "source": "00afe44c",
  "target": "00afe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe450`](#insn-00afe450)

~~~json
{
  "source": "00afe450",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe464`](#insn-00afe464)

~~~json
{
  "source": "00afe464",
  "target": "0023d3a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6412,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe46c`](#insn-00afe46c)

~~~json
{
  "source": "00afe46c",
  "target": "00afe49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe470`](#insn-00afe470)

~~~json
{
  "source": "00afe470",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe484`](#insn-00afe484)

~~~json
{
  "source": "00afe484",
  "target": "00ab92d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe48c`](#insn-00afe48c)

~~~json
{
  "source": "00afe48c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe498`](#insn-00afe498)

~~~json
{
  "source": "00afe498",
  "target": "00afe5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe49c`](#insn-00afe49c)

~~~json
{
  "source": "00afe49c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4a8`](#insn-00afe4a8)

~~~json
{
  "source": "00afe4a8",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4ac`](#insn-00afe4ac)

~~~json
{
  "source": "00afe4ac",
  "target": "00afe4fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe4b0`](#insn-00afe4b0)

~~~json
{
  "source": "00afe4b0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4c4`](#insn-00afe4c4)

~~~json
{
  "source": "00afe4c4",
  "target": "0023d3a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6412,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe4cc`](#insn-00afe4cc)

~~~json
{
  "source": "00afe4cc",
  "target": "00afe4fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe4d0`](#insn-00afe4d0)

~~~json
{
  "source": "00afe4d0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4e4`](#insn-00afe4e4)

~~~json
{
  "source": "00afe4e4",
  "target": "00ab92d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4ec`](#insn-00afe4ec)

~~~json
{
  "source": "00afe4ec",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe4f8`](#insn-00afe4f8)

~~~json
{
  "source": "00afe4f8",
  "target": "00afe5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe4fc`](#insn-00afe4fc)

~~~json
{
  "source": "00afe4fc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe508`](#insn-00afe508)

~~~json
{
  "source": "00afe508",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe50c`](#insn-00afe50c)

~~~json
{
  "source": "00afe50c",
  "target": "00afe55c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe510`](#insn-00afe510)

~~~json
{
  "source": "00afe510",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe524`](#insn-00afe524)

~~~json
{
  "source": "00afe524",
  "target": "0023d3a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6412,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe52c`](#insn-00afe52c)

~~~json
{
  "source": "00afe52c",
  "target": "00afe55c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe530`](#insn-00afe530)

~~~json
{
  "source": "00afe530",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe544`](#insn-00afe544)

~~~json
{
  "source": "00afe544",
  "target": "00ab92d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe54c`](#insn-00afe54c)

~~~json
{
  "source": "00afe54c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe558`](#insn-00afe558)

~~~json
{
  "source": "00afe558",
  "target": "00afe5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe55c`](#insn-00afe55c)

~~~json
{
  "source": "00afe55c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe568`](#insn-00afe568)

~~~json
{
  "source": "00afe568",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe56c`](#insn-00afe56c)

~~~json
{
  "source": "00afe56c",
  "target": "00afe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe570`](#insn-00afe570)

~~~json
{
  "source": "00afe570",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe584`](#insn-00afe584)

~~~json
{
  "source": "00afe584",
  "target": "0023d3a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6412,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afe58c`](#insn-00afe58c)

~~~json
{
  "source": "00afe58c",
  "target": "00afe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe590`](#insn-00afe590)

~~~json
{
  "source": "00afe590",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe5a4`](#insn-00afe5a4)

~~~json
{
  "source": "00afe5a4",
  "target": "00ab92d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe5ac`](#insn-00afe5ac)

~~~json
{
  "source": "00afe5ac",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe5b8`](#insn-00afe5b8)

~~~json
{
  "source": "00afe5b8",
  "target": "00ab9080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe5ec`](#insn-00afe5ec)

~~~json
{
  "source": "00afe5ec",
  "target": "00afe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe5f4`](#insn-00afe5f4)

~~~json
{
  "source": "00afe5f4",
  "target": "00802678",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe5fc`](#insn-00afe5fc)

~~~json
{
  "source": "00afe5fc",
  "target": "00afe618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe600`](#insn-00afe600)

~~~json
{
  "source": "00afe600",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe604`](#insn-00afe604)

~~~json
{
  "source": "00afe604",
  "target": "007bbc70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe608`](#insn-00afe608)

~~~json
{
  "source": "00afe608",
  "target": "00afe618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe60c`](#insn-00afe60c)

~~~json
{
  "source": "00afe60c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe610`](#insn-00afe610)

~~~json
{
  "source": "00afe610",
  "target": "007efb3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe614`](#insn-00afe614)

~~~json
{
  "source": "00afe614",
  "target": "00afe640",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe61c`](#insn-00afe61c)

~~~json
{
  "source": "00afe61c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe638`](#insn-00afe638)

~~~json
{
  "source": "00afe638",
  "target": "00689c7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe648`](#insn-00afe648)

~~~json
{
  "source": "00afe648",
  "target": "00afe664",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe678`](#insn-00afe678)

~~~json
{
  "source": "00afe678",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe680`](#insn-00afe680)

~~~json
{
  "source": "00afe680",
  "target": "00afe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6a0`](#insn-00afe6a0)

~~~json
{
  "source": "00afe6a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6a4`](#insn-00afe6a4)

~~~json
{
  "source": "00afe6a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6a8`](#insn-00afe6a8)

~~~json
{
  "source": "00afe6a8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6ac`](#insn-00afe6ac)

~~~json
{
  "source": "00afe6ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6b0`](#insn-00afe6b0)

~~~json
{
  "source": "00afe6b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6b4`](#insn-00afe6b4)

~~~json
{
  "source": "00afe6b4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
