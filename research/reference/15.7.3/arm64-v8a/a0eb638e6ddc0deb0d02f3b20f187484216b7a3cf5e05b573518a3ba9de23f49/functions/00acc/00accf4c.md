# 00accf4c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acce84`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-632930dd500322c1d1b54f899090413f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00accf90`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-245370318a2a26f098bb307efb7d28a6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00accf4c",
  "name": "FUN_00accf4c",
  "size": 960,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ce9589541f198062e6d4f732841e78860609ec36ea49f90d20024a21a1ce77d",
  "source_text_sha256": "6ce9589541f198062e6d4f732841e78860609ec36ea49f90d20024a21a1ce77d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00accf4c",
        "00acd307"
      ],
      [
        "00acd344",
        "00acd347"
      ]
    ],
    "bytes_sha256": "3796e0e77071ba6cbd465968c6b380e3ec97711db74a9af54638e575cc382181",
    "instruction_count": 240,
    "instruction_bytes": 960,
    "body_bytes": 960,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [004183ec](../00418/004183ec.md)
- [0041876c](../00418/0041876c.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041c8e4](../0041c/0041c8e4.md)
- [0041c8ec](../0041c/0041c8ec.md)
- [0041c8f8](../0041c/0041c8f8.md)
- [00449b7c](../00449/00449b7c.md)
- [00449c14](../00449/00449c14.md)
- [00469e20](../00469/00469e20.md)
- [0046f694](../0046f/0046f694.md)
- [005377dc](../00537/005377dc.md)
- [005377ec](../00537/005377ec.md)
- [00558f34](../00558/00558f34.md)
- [00565f94](../00565/00565f94.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [0081f580](../0081f/0081f580.md)
- [00821cb4](../00821/00821cb4.md)
- [00acbd60](../00acb/00acbd60.md)
- [00acbecc](../00acb/00acbecc.md)
- [00acc038](../00acc/00acc038.md)
- [00acc1a0](../00acc/00acc1a0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"getScreenWindowRatio"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5755 bytes

~~~c

void FUN_00accf4c(void)

{
  byte *pbVar1;
  long lVar2;
  long lVar3;
  undefined *puVar4;
  char cVar5;
  int iVar6;
  int iVar7;
  long *plVar8;
  undefined8 uVar9;
  long lVar10;
  ulong uVar11;
  long lVar12;
  undefined4 uVar13;
  float fVar14;
  int iVar15;
  int iVar16;
  float fVar17;
  int iVar18;
  byte local_78 [16];
  void *local_68;
  byte local_60;
  char local_5f [8];
  undefined7 uStack_57;
  char cStack_50;
  undefined4 uStack_4f;
  undefined1 uStack_4b;
  undefined2 uStack_4a;
  long local_48;
  
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  plVar8 = (long *)FUN_00565f94();
  uVar9 = FUN_00566284();
  local_60 = 0x28;
  local_78[0] = 6;
  uStack_4b = 0;
  uStack_4f = 0x6f697461;
  uStack_57 = (undefined7)s_getScreenWindowRatio_0029964e._8_8_;
  cStack_50 = SUB81(s_getScreenWindowRatio_0029964e._8_8_,7);
  local_5f[0] = s_getScreenWindowRatio_0029964e[0];
  local_5f[1] = s_getScreenWindowRatio_0029964e[1];
  local_5f[2] = s_getScreenWindowRatio_0029964e[2];
  local_5f[3] = s_getScreenWindowRatio_0029964e[3];
  local_5f[4] = s_getScreenWindowRatio_0029964e[4];
  local_5f[5] = s_getScreenWindowRatio_0029964e[5];
  local_5f[6] = s_getScreenWindowRatio_0029964e[6];
  local_5f[7] = s_getScreenWindowRatio_0029964e[7];
  local_78[1] = 0x28;
  local_78[2] = 0x29;
  local_78[3] = 0x46;
  local_78[4] = 0;
  lVar10 = FUN_00566448(uVar9,&local_60,local_78,plVar8);
  if ((local_78[0] & 1) != 0) {
    _ZdlPv(local_68);
  }
  if ((local_60 & 1) != 0) {
    _ZdlPv((void *)CONCAT26(uStack_4a,CONCAT15(uStack_4b,CONCAT41(uStack_4f,cStack_50))));
  }
  FUN_00566284();
  uVar9 = FUN_00566978();
  if (lVar10 == 0) {
    uVar13 = 0;
  }
  else {
    uVar13 = FUN_00558f34(plVar8,uVar9,lVar10);
    cVar5 = (**(code **)(*plVar8 + 0x720))(plVar8);
    if (cVar5 != '\0') {
      (**(code **)(*plVar8 + 0x80))(plVar8);
      (**(code **)(*plVar8 + 0x88))(plVar8);
    }
  }
  puVar4 = PTR_DAT_00c1ad28;
  *(undefined4 *)(PTR_DAT_00c1ad28 + 0x28) = uVar13;
  *(undefined4 *)(puVar4 + 0x24) = 0x3f800000;
  uVar13 = FUN_005377ec();
  *(undefined4 *)(puVar4 + 8) = uVar13;
  iVar6 = FUN_005377dc();
  *(int *)(puVar4 + 0x14) = iVar6;
  fVar14 = (float)iVar6 * 960.0;
  *(int *)(puVar4 + 0xc) = iVar6;
  *(int *)(puVar4 + 0x10) = *(int *)(puVar4 + 8);
  fVar17 = (float)*(int *)(puVar4 + 8);
  if (fVar14 / 640.0 <= fVar17) {
    *(int *)(puVar4 + 0x18) = (int)(long)((fVar17 * 640.0) / (float)iVar6);
    *(undefined8 *)(puVar4 + 0x1c) = 0x28000000280;
    iVar6 = FUN_00acc1a0();
    iVar7 = FUN_00acc038();
    if (iVar6 <= iVar7) {
      iVar6 = iVar7;
    }
    *(int *)(puVar4 + 0x34) = iVar6;
    uVar13 = FUN_00acbd60();
    *(undefined4 *)(puVar4 + 0x38) = uVar13;
    *(undefined4 *)(puVar4 + 0x3c) = *(undefined4 *)(puVar4 + 0x34);
    uVar13 = FUN_00acbecc();
    *(undefined4 *)(puVar4 + 0x40) = uVar13;
    uVar11 = FUN_00449b7c(puVar4);
    if ((uVar11 & 1) == 0) {
      iVar6 = *(int *)(puVar4 + 0x18);
      iVar7 = *(int *)(puVar4 + 0x1c);
    }
    else {
      iVar7 = *(int *)(puVar4 + 0x18);
      iVar15 = *(int *)(puVar4 + 0xc);
      iVar6 = FUN_00449c14(puVar4);
      iVar16 = *(int *)(puVar4 + 0x1c);
      iVar18 = *(int *)(puVar4 + 0xc);
      *(int *)(puVar4 + 0x18) = (int)(long)(((float)iVar7 * (float)iVar15) / (float)iVar6);
      iVar7 = FUN_00449c14(puVar4);
      iVar6 = *(int *)(puVar4 + 0x18);
      iVar7 = (int)(long)(((float)iVar16 * (float)iVar18) / (float)iVar7);
      *(int *)(puVar4 + 0x1c) = iVar7;
      if (0x51c < iVar6) {
        iVar15 = *(int *)(puVar4 + 0x34) +
                 (int)(long)(((float)(iVar6 + -0x51c) / 2.0) * *(float *)(puVar4 + 0x28));
        *(int *)(puVar4 + 0x34) = iVar15;
        *(int *)(puVar4 + 0x3c) = iVar15;
      }
    }
  }
  else {
    iVar6 = 0x3c0;
    *(undefined4 *)(puVar4 + 0x18) = 0x3c0;
    iVar7 = (int)(long)(fVar14 / fVar17);
    *(int *)(puVar4 + 0x1c) = iVar7;
    *(int *)(puVar4 + 0x20) = iVar7;
  }
  iVar15 = 0;
  if (iVar6 != 0) {
    iVar15 = (*(int *)(puVar4 + 8) * iVar7) / iVar6;
  }
  if (*(int *)(puVar4 + 0xc) < iVar15) {
    fVar14 = (float)(long)(((float)iVar6 * (float)*(int *)(puVar4 + 0xc)) / (float)iVar7);
  }
  else {
    fVar14 = (float)*(int *)(puVar4 + 8);
  }
  iVar7 = *(int *)(puVar4 + 0x20);
  *(float *)(puVar4 + 0x24) = (fVar14 + fVar14) / (float)iVar6;
  lVar10 = FUN_0081f580();
  *(int *)(BYTE_ARRAY_0032f999 + lVar10 + 0xf) = (int)(long)((float)(iVar7 + -0x280) / 2.0);
  lVar10 = FUN_0081f580();
  if (*(int *)(BYTE_ARRAY_0032f999 + lVar10 + 0xf) < 1) {
    uVar13 = 0;
  }
  else {
    iVar6 = *(int *)(puVar4 + 0x20);
    lVar10 = FUN_0081f580();
    if (iVar6 < 0x2d0) {
      uVar13 = 0;
      goto LAB_00acd288;
    }
    lVar12 = (long)(((float)*(int *)(puVar4 + 0x18) * (float)*(int *)(puVar4 + 0xc)) /
                   (float)*(int *)(puVar4 + 8));
    lVar2 = lVar12 + -0x2cf;
    if (0x2cf < lVar12) {
      lVar2 = lVar12 + -0x2d0;
    }
    pbVar1 = BYTE_ARRAY_0032f999 + lVar10 + 0xf;
    pbVar1[0] = 0x28;
    pbVar1[1] = 0;
    pbVar1[2] = 0;
    pbVar1[3] = 0;
    uVar13 = (undefined4)(long)(double)(lVar2 >> 1);
  }
  lVar10 = FUN_0081f580();
LAB_00acd288:
  *(undefined4 *)(BYTE_ARRAY_0032f999 + lVar10 + 0x13) = uVar13;
  FUN_0041be0c();
  FUN_0041c8e4(*(undefined4 *)(puVar4 + 0x28));
  FUN_0081f580();
  iVar6 = FUN_00821cb4();
  if (iVar6 == 100) {
    lVar10 = FUN_0081f580();
    iVar6 = *(int *)(BYTE_ARRAY_0032fef1 + lVar10 + 0x1b);
    FUN_0081f580();
    if (iVar6 == 0) {
      FUN_0041be0c();
      FUN_0041c8f8();
      FUN_0041be0c();
      FUN_0041c8ec();
    }
  }
  FUN_00469e20();
  FUN_0046f694();
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00accf4c"></a> `00accf4c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00accf50"></a> `00accf50` | `e8 23 00 fd` | str d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accf54"></a> `00accf54` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accf58"></a> `00accf58` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00accf5c"></a> `00accf5c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00accf60"></a> `00accf60` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00accf64"></a> `00accf64` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00accf68"></a> `00accf68` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00accf6c"></a> `00accf6c` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00accf70"></a> `00accf70` | `09 64 ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00accf74"></a> `00accf74` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00accf78"></a> `00accf78` | `c3 64 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00accf7c"></a> `00accf7c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00accf80"></a> `00accf80` | `69 be ff b0` | adrp x9,0x299000 | `FALL_THROUGH`
<a id="insn-00accf84"></a> `00accf84` | `29 39 19 91` | add x9,x9,#0x64e | `FALL_THROUGH`
<a id="insn-00accf88"></a> `00accf88` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accf8c"></a> `00accf8c` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00accf90"></a> `00accf90` | `2a 8c 8e 52` | mov w10,#0x7461 | `FALL_THROUGH`
<a id="insn-00accf94"></a> `00accf94` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00accf98"></a> `00accf98` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00accf9c"></a> `00accf9c` | `08 25 85 52` | mov w8,#0x2928 | `FALL_THROUGH`
<a id="insn-00accfa0"></a> `00accfa0` | `2a ed ad 72` | movk w10,#0x6f69, LSL #16 | `FALL_THROUGH`
<a id="insn-00accfa4"></a> `00accfa4` | `c8 08 a0 72` | movk w8,#0x46, LSL #16 | `FALL_THROUGH`
<a id="insn-00accfa8"></a> `00accfa8` | `ff d7 00 39` | strb wzr,[sp, #0x35] | `FALL_THROUGH`
<a id="insn-00accfac"></a> `00accfac` | `ea 13 03 b8` | stur w10,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00accfb0"></a> `00accfb0` | `e0 13 82 3c` | stur q0,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00accfb4"></a> `00accfb4` | `e8 93 00 b8` | stur w8,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00accfb8"></a> `00accfb8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00accfbc"></a> `00accfbc` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00accfc0"></a> `00accfc0` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00accfc4"></a> `00accfc4` | `21 65 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00accfc8"></a> `00accfc8` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00accfcc"></a> `00accfcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00accfd0"></a> `00accfd0` | `68 00 00 36` | tbz w8,#0x0,0x00accfdc | `CONDITIONAL_JUMP`
<a id="insn-00accfd4"></a> `00accfd4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00accfd8"></a> `00accfd8` | `0e 38 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00accfdc"></a> `00accfdc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accfe0"></a> `00accfe0` | `68 00 00 36` | tbz w8,#0x0,0x00accfec | `CONDITIONAL_JUMP`
<a id="insn-00accfe4"></a> `00accfe4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00accfe8"></a> `00accfe8` | `0a 38 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00accfec"></a> `00accfec` | `a6 64 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00accff0"></a> `00accff0` | `62 66 ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00accff4"></a> `00accff4` | `b4 02 00 b4` | cbz x20,0x00acd048 | `CONDITIONAL_JUMP`
<a id="insn-00accff8"></a> `00accff8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00accffc"></a> `00accffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd000"></a> `00acd000` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00acd004"></a> `00acd004` | `cc 2f ea 97` | bl 0x00558f34 | `UNCONDITIONAL_CALL`
<a id="insn-00acd008"></a> `00acd008` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acd00c"></a> `00acd00c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd010"></a> `00acd010` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-00acd014"></a> `00acd014` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00acd018"></a> `00acd018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd01c"></a> `00acd01c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00acd020"></a> `00acd020` | `60 01 00 54` | b.eq 0x00acd04c | `CONDITIONAL_JUMP`
<a id="insn-00acd024"></a> `00acd024` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acd028"></a> `00acd028` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd02c"></a> `00acd02c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00acd030"></a> `00acd030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd034"></a> `00acd034` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acd038"></a> `00acd038` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd03c"></a> `00acd03c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00acd040"></a> `00acd040` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acd044"></a> `00acd044` | `02 00 00 14` | b 0x00acd04c | `UNCONDITIONAL_JUMP`
<a id="insn-00acd048"></a> `00acd048` | `08 e4 00 2f` | movi d8,#0x0 | `FALL_THROUGH`
<a id="insn-00acd04c"></a> `00acd04c` | `73 0a 00 b0` | adrp x19,0xc1a000 | `FALL_THROUGH`
<a id="insn-00acd050"></a> `00acd050` | `08 f0 a7 52` | mov w8,#0x3f800000 | `FALL_THROUGH`
<a id="insn-00acd054"></a> `00acd054` | `73 96 46 f9` | ldr x19,[x19, #0xd28] | `FALL_THROUGH`
<a id="insn-00acd058"></a> `00acd058` | `68 2a 00 bd` | str s8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00acd05c"></a> `00acd05c` | `68 26 00 b9` | str w8,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00acd060"></a> `00acd060` | `e3 a9 e9 97` | bl 0x005377ec | `UNCONDITIONAL_CALL`
<a id="insn-00acd064"></a> `00acd064` | `60 0a 00 b9` | str w0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acd068"></a> `00acd068` | `dd a9 e9 97` | bl 0x005377dc | `UNCONDITIONAL_CALL`
<a id="insn-00acd06c"></a> `00acd06c` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acd070"></a> `00acd070` | `08 8e a8 52` | mov w8,#0x44700000 | `FALL_THROUGH`
<a id="insn-00acd074"></a> `00acd074` | `60 16 00 b9` | str w0,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00acd078"></a> `00acd078` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00acd07c"></a> `00acd07c` | `08 84 a8 52` | mov w8,#0x44200000 | `FALL_THROUGH`
<a id="insn-00acd080"></a> `00acd080` | `02 01 27 1e` | fmov s2,w8 | `FALL_THROUGH`
<a id="insn-00acd084"></a> `00acd084` | `68 0a 40 b9` | ldr w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acd088"></a> `00acd088` | `01 08 21 1e` | fmul s1,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd08c"></a> `00acd08c` | `60 a2 01 29` | stp w0,w8,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00acd090"></a> `00acd090` | `23 18 22 1e` | fdiv s3,s1,s2 | `FALL_THROUGH`
<a id="insn-00acd094"></a> `00acd094` | `02 01 22 1e` | scvtf s2,w8 | `FALL_THROUGH`
<a id="insn-00acd098"></a> `00acd098` | `60 20 22 1e` | fcmp s3,s2 | `FALL_THROUGH`
<a id="insn-00acd09c"></a> `00acd09c` | `e9 00 00 54` | b.ls 0x00acd0b8 | `CONDITIONAL_JUMP`
<a id="insn-00acd0a0"></a> `00acd0a0` | `20 18 22 1e` | fdiv s0,s1,s2 | `FALL_THROUGH`
<a id="insn-00acd0a4"></a> `00acd0a4` | `08 78 80 52` | mov w8,#0x3c0 | `FALL_THROUGH`
<a id="insn-00acd0a8"></a> `00acd0a8` | `68 1a 00 b9` | str w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd0ac"></a> `00acd0ac` | `09 00 24 9e` | fcvtas x9,s0 | `FALL_THROUGH`
<a id="insn-00acd0b0"></a> `00acd0b0` | `69 a6 03 29` | stp w9,w9,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00acd0b4"></a> `00acd0b4` | `3c 00 00 14` | b 0x00acd1a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd0b8"></a> `00acd0b8` | `08 84 a8 52` | mov w8,#0x44200000 | `FALL_THROUGH`
<a id="insn-00acd0bc"></a> `00acd0bc` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00acd0c0"></a> `00acd0c0` | `08 50 80 52` | mov w8,#0x280 | `FALL_THROUGH`
<a id="insn-00acd0c4"></a> `00acd0c4` | `41 08 21 1e` | fmul s1,s2,s1 | `FALL_THROUGH`
<a id="insn-00acd0c8"></a> `00acd0c8` | `20 18 20 1e` | fdiv s0,s1,s0 | `FALL_THROUGH`
<a id="insn-00acd0cc"></a> `00acd0cc` | `09 00 24 9e` | fcvtas x9,s0 | `FALL_THROUGH`
<a id="insn-00acd0d0"></a> `00acd0d0` | `00 0d 04 0e` | dup v0.2S,w8 | `FALL_THROUGH`
<a id="insn-00acd0d4"></a> `00acd0d4` | `69 1a 00 b9` | str w9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd0d8"></a> `00acd0d8` | `60 c2 01 fc` | stur d0,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00acd0dc"></a> `00acd0dc` | `31 fc ff 97` | bl 0x00acc1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00acd0e0"></a> `00acd0e0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acd0e4"></a> `00acd0e4` | `d5 fb ff 97` | bl 0x00acc038 | `UNCONDITIONAL_CALL`
<a id="insn-00acd0e8"></a> `00acd0e8` | `9f 02 00 6b` | cmp w20,w0 | `FALL_THROUGH`
<a id="insn-00acd0ec"></a> `00acd0ec` | `88 c2 80 1a` | csel w8,w20,w0,gt | `FALL_THROUGH`
<a id="insn-00acd0f0"></a> `00acd0f0` | `68 36 00 b9` | str w8,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00acd0f4"></a> `00acd0f4` | `1b fb ff 97` | bl 0x00acbd60 | `UNCONDITIONAL_CALL`
<a id="insn-00acd0f8"></a> `00acd0f8` | `68 36 40 b9` | ldr w8,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00acd0fc"></a> `00acd0fc` | `60 22 07 29` | stp w0,w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00acd100"></a> `00acd100` | `73 fb ff 97` | bl 0x00acbecc | `UNCONDITIONAL_CALL`
<a id="insn-00acd104"></a> `00acd104` | `60 42 00 b9` | str w0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00acd108"></a> `00acd108` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd10c"></a> `00acd10c` | `9c f2 e5 97` | bl 0x00449b7c | `UNCONDITIONAL_CALL`
<a id="insn-00acd110"></a> `00acd110` | `80 04 00 36` | tbz w0,#0x0,0x00acd1a0 | `CONDITIONAL_JUMP`
<a id="insn-00acd114"></a> `00acd114` | `60 1a 40 bd` | ldr s0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd118"></a> `00acd118` | `61 0e 40 bd` | ldr s1,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00acd11c"></a> `00acd11c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd120"></a> `00acd120` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acd124"></a> `00acd124` | `21 d8 21 5e` | scvtf s1,s1 | `FALL_THROUGH`
<a id="insn-00acd128"></a> `00acd128` | `08 08 21 1e` | fmul s8,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd12c"></a> `00acd12c` | `ba f2 e5 97` | bl 0x00449c14 | `UNCONDITIONAL_CALL`
<a id="insn-00acd130"></a> `00acd130` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acd134"></a> `00acd134` | `61 1e 40 bd` | ldr s1,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00acd138"></a> `00acd138` | `62 0e 40 bd` | ldr s2,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00acd13c"></a> `00acd13c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd140"></a> `00acd140` | `21 d8 21 5e` | scvtf s1,s1 | `FALL_THROUGH`
<a id="insn-00acd144"></a> `00acd144` | `42 d8 21 5e` | scvtf s2,s2 | `FALL_THROUGH`
<a id="insn-00acd148"></a> `00acd148` | `00 19 20 1e` | fdiv s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acd14c"></a> `00acd14c` | `28 08 22 1e` | fmul s8,s1,s2 | `FALL_THROUGH`
<a id="insn-00acd150"></a> `00acd150` | `08 00 24 9e` | fcvtas x8,s0 | `FALL_THROUGH`
<a id="insn-00acd154"></a> `00acd154` | `68 1a 00 b9` | str w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd158"></a> `00acd158` | `af f2 e5 97` | bl 0x00449c14 | `UNCONDITIONAL_CALL`
<a id="insn-00acd15c"></a> `00acd15c` | `00 00 22 1e` | scvtf s0,w0 | `FALL_THROUGH`
<a id="insn-00acd160"></a> `00acd160` | `68 1a 40 b9` | ldr w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd164"></a> `00acd164` | `1f 75 14 71` | cmp w8,#0x51d | `FALL_THROUGH`
<a id="insn-00acd168"></a> `00acd168` | `00 19 20 1e` | fdiv s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acd16c"></a> `00acd16c` | `09 00 24 9e` | fcvtas x9,s0 | `FALL_THROUGH`
<a id="insn-00acd170"></a> `00acd170` | `69 1e 00 b9` | str w9,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00acd174"></a> `00acd174` | `8b 01 00 54` | b.lt 0x00acd1a4 | `CONDITIONAL_JUMP`
<a id="insn-00acd178"></a> `00acd178` | `0a 71 14 51` | sub w10,w8,#0x51c | `FALL_THROUGH`
<a id="insn-00acd17c"></a> `00acd17c` | `61 2a 40 bd` | ldr s1,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00acd180"></a> `00acd180` | `6b 36 40 b9` | ldr w11,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00acd184"></a> `00acd184` | `40 fd 02 1e` | scvtf s0,w10,#0x1 | `FALL_THROUGH`
<a id="insn-00acd188"></a> `00acd188` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd18c"></a> `00acd18c` | `0a 00 24 9e` | fcvtas x10,s0 | `FALL_THROUGH`
<a id="insn-00acd190"></a> `00acd190` | `6a 01 0a 0b` | add w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00acd194"></a> `00acd194` | `6a 36 00 b9` | str w10,[x19, #0x34] | `FALL_THROUGH`
<a id="insn-00acd198"></a> `00acd198` | `6a 3e 00 b9` | str w10,[x19, #0x3c] | `FALL_THROUGH`
<a id="insn-00acd19c"></a> `00acd19c` | `02 00 00 14` | b 0x00acd1a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd1a0"></a> `00acd1a0` | `68 26 43 29` | ldp w8,w9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd1a4"></a> `00acd1a4` | `6a 2e 41 29` | ldp w10,w11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acd1a8"></a> `00acd1a8` | `4c 7d 09 1b` | mul w12,w10,w9 | `FALL_THROUGH`
<a id="insn-00acd1ac"></a> `00acd1ac` | `8c 0d c8 1a` | sdiv w12,w12,w8 | `FALL_THROUGH`
<a id="insn-00acd1b0"></a> `00acd1b0` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00acd1b4"></a> `00acd1b4` | `2d 01 00 54` | b.le 0x00acd1d8 | `CONDITIONAL_JUMP`
<a id="insn-00acd1b8"></a> `00acd1b8` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acd1bc"></a> `00acd1bc` | `61 01 22 1e` | scvtf s1,w11 | `FALL_THROUGH`
<a id="insn-00acd1c0"></a> `00acd1c0` | `22 01 22 1e` | scvtf s2,w9 | `FALL_THROUGH`
<a id="insn-00acd1c4"></a> `00acd1c4` | `01 08 21 1e` | fmul s1,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd1c8"></a> `00acd1c8` | `21 18 22 1e` | fdiv s1,s1,s2 | `FALL_THROUGH`
<a id="insn-00acd1cc"></a> `00acd1cc` | `28 00 24 9e` | fcvtas x8,s1 | `FALL_THROUGH`
<a id="insn-00acd1d0"></a> `00acd1d0` | `01 01 22 9e` | scvtf s1,x8 | `FALL_THROUGH`
<a id="insn-00acd1d4"></a> `00acd1d4` | `03 00 00 14` | b 0x00acd1e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd1d8"></a> `00acd1d8` | `41 01 22 1e` | scvtf s1,w10 | `FALL_THROUGH`
<a id="insn-00acd1dc"></a> `00acd1dc` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00acd1e0"></a> `00acd1e0` | `21 28 21 1e` | fadd s1,s1,s1 | `FALL_THROUGH`
<a id="insn-00acd1e4"></a> `00acd1e4` | `68 22 40 b9` | ldr w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acd1e8"></a> `00acd1e8` | `08 01 0a 51` | sub w8,w8,#0x280 | `FALL_THROUGH`
<a id="insn-00acd1ec"></a> `00acd1ec` | `20 18 20 1e` | fdiv s0,s1,s0 | `FALL_THROUGH`
<a id="insn-00acd1f0"></a> `00acd1f0` | `01 fd 02 1e` | scvtf s1,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acd1f4"></a> `00acd1f4` | `34 00 24 9e` | fcvtas x20,s1 | `FALL_THROUGH`
<a id="insn-00acd1f8"></a> `00acd1f8` | `60 26 00 bd` | str s0,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00acd1fc"></a> `00acd1fc` | `e1 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd200"></a> `00acd200` | `16 35 9f 52` | mov w22,#0xf9a8 | `FALL_THROUGH`
<a id="insn-00acd204"></a> `00acd204` | `56 06 a0 72` | movk w22,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00acd208"></a> `00acd208` | `14 68 36 b8` | str w20,[x0, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd20c"></a> `00acd20c` | `dd 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd210"></a> `00acd210` | `08 68 76 b8` | ldr w8,[x0, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd214"></a> `00acd214` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acd218"></a> `00acd218` | `0b 03 00 54` | b.lt 0x00acd278 | `CONDITIONAL_JUMP`
<a id="insn-00acd21c"></a> `00acd21c` | `74 22 40 b9` | ldr w20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acd220"></a> `00acd220` | `d8 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd224"></a> `00acd224` | `9f 42 0b 71` | cmp w20,#0x2d0 | `FALL_THROUGH`
<a id="insn-00acd228"></a> `00acd228` | `eb 02 00 54` | b.lt 0x00acd284 | `CONDITIONAL_JUMP`
<a id="insn-00acd22c"></a> `00acd22c` | `62 06 41 2d` | ldp s2,s1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acd230"></a> `00acd230` | `60 1a 40 bd` | ldr s0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00acd234"></a> `00acd234` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-00acd238"></a> `00acd238` | `21 d8 21 5e` | scvtf s1,s1 | `FALL_THROUGH`
<a id="insn-00acd23c"></a> `00acd23c` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd240"></a> `00acd240` | `41 d8 21 5e` | scvtf s1,s2 | `FALL_THROUGH`
<a id="insn-00acd244"></a> `00acd244` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00acd248"></a> `00acd248` | `08 00 24 9e` | fcvtas x8,s0 | `FALL_THROUGH`
<a id="insn-00acd24c"></a> `00acd24c` | `09 41 0b f1` | subs x9,x8,#0x2d0 | `FALL_THROUGH`
<a id="insn-00acd250"></a> `00acd250` | `08 3d 0b d1` | sub x8,x8,#0x2cf | `FALL_THROUGH`
<a id="insn-00acd254"></a> `00acd254` | `08 b1 89 9a` | csel x8,x8,x9,lt | `FALL_THROUGH`
<a id="insn-00acd258"></a> `00acd258` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00acd25c"></a> `00acd25c` | `08 fd 41 93` | asr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acd260"></a> `00acd260` | `00 01 62 9e` | scvtf d0,x8 | `FALL_THROUGH`
<a id="insn-00acd264"></a> `00acd264` | `08 35 9f 52` | mov w8,#0xf9a8 | `FALL_THROUGH`
<a id="insn-00acd268"></a> `00acd268` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00acd26c"></a> `00acd26c` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd270"></a> `00acd270` | `14 00 64 9e` | fcvtas x20,d0 | `FALL_THROUGH`
<a id="insn-00acd274"></a> `00acd274` | `02 00 00 14` | b 0x00acd27c | `UNCONDITIONAL_JUMP`
<a id="insn-00acd278"></a> `00acd278` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00acd27c"></a> `00acd27c` | `c1 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd280"></a> `00acd280` | `02 00 00 14` | b 0x00acd288 | `UNCONDITIONAL_JUMP`
<a id="insn-00acd284"></a> `00acd284` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00acd288"></a> `00acd288` | `88 35 9f 52` | mov w8,#0xf9ac | `FALL_THROUGH`
<a id="insn-00acd28c"></a> `00acd28c` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00acd290"></a> `00acd290` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd294"></a> `00acd294` | `de 3a e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00acd298"></a> `00acd298` | `60 2a 40 bd` | ldr s0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00acd29c"></a> `00acd29c` | `92 3d e5 97` | bl 0x0041c8e4 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2a0"></a> `00acd2a0` | `b8 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2a4"></a> `00acd2a4` | `84 52 f5 97` | bl 0x00821cb4 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2a8"></a> `00acd2a8` | `1f 90 01 71` | cmp w0,#0x64 | `FALL_THROUGH`
<a id="insn-00acd2ac"></a> `00acd2ac` | `61 01 00 54` | b.ne 0x00acd2d8 | `CONDITIONAL_JUMP`
<a id="insn-00acd2b0"></a> `00acd2b0` | `b4 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2b4"></a> `00acd2b4` | `88 e1 9f 52` | mov w8,#0xff0c | `FALL_THROUGH`
<a id="insn-00acd2b8"></a> `00acd2b8` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00acd2bc"></a> `00acd2bc` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acd2c0"></a> `00acd2c0` | `b0 48 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2c4"></a> `00acd2c4` | `b3 00 00 35` | cbnz w19,0x00acd2d8 | `CONDITIONAL_JUMP`
<a id="insn-00acd2c8"></a> `00acd2c8` | `d1 3a e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00acd2cc"></a> `00acd2cc` | `8b 3d e5 97` | bl 0x0041c8f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2d0"></a> `00acd2d0` | `cf 3a e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00acd2d4"></a> `00acd2d4` | `86 3d e5 97` | bl 0x0041c8ec | `UNCONDITIONAL_CALL`
<a id="insn-00acd2d8"></a> `00acd2d8` | `d2 72 e6 97` | bl 0x00469e20 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2dc"></a> `00acd2dc` | `ee 88 e6 97` | bl 0x0046f694 | `UNCONDITIONAL_CALL`
<a id="insn-00acd2e0"></a> `00acd2e0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acd2e4"></a> `00acd2e4` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acd2e8"></a> `00acd2e8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acd2ec"></a> `00acd2ec` | `c1 02 00 54` | b.ne 0x00acd344 | `CONDITIONAL_JUMP`
<a id="insn-00acd2f0"></a> `00acd2f0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acd2f4"></a> `00acd2f4` | `e8 23 40 fd` | ldr d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acd2f8"></a> `00acd2f8` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acd2fc"></a> `00acd2fc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acd300"></a> `00acd300` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acd304"></a> `00acd304` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acd344"></a> `00acd344` | `3f 37 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00accf4c`](#insn-00accf4c) 範囲 `[['00accf4c', '00accfd3']]`
  - `CONDITIONAL_JUMP` [`00accfd0`](#insn-00accfd0) → [`00accfdc`](#insn-00accfdc)
  - `FALL_THROUGH` [`00accfd0`](#insn-00accfd0) → [`00accfd4`](#insn-00accfd4)
- ブロック [`00accfd4`](#insn-00accfd4) 範囲 `[['00accfd4', '00accfdb']]`
  - `FALL_THROUGH` [`00accfd8`](#insn-00accfd8) → [`00accfdc`](#insn-00accfdc)
- ブロック [`00accfdc`](#insn-00accfdc) 範囲 `[['00accfdc', '00accfe3']]`
  - `CONDITIONAL_JUMP` [`00accfe0`](#insn-00accfe0) → [`00accfec`](#insn-00accfec)
  - `FALL_THROUGH` [`00accfe0`](#insn-00accfe0) → [`00accfe4`](#insn-00accfe4)
- ブロック [`00accfe4`](#insn-00accfe4) 範囲 `[['00accfe4', '00accfeb']]`
  - `FALL_THROUGH` [`00accfe8`](#insn-00accfe8) → [`00accfec`](#insn-00accfec)
- ブロック [`00accfec`](#insn-00accfec) 範囲 `[['00accfec', '00accff7']]`
  - `CONDITIONAL_JUMP` [`00accff4`](#insn-00accff4) → [`00acd048`](#insn-00acd048)
  - `FALL_THROUGH` [`00accff4`](#insn-00accff4) → [`00accff8`](#insn-00accff8)
- ブロック [`00accff8`](#insn-00accff8) 範囲 `[['00accff8', '00acd023']]`
  - `CONDITIONAL_JUMP` [`00acd020`](#insn-00acd020) → [`00acd04c`](#insn-00acd04c)
  - `FALL_THROUGH` [`00acd020`](#insn-00acd020) → [`00acd024`](#insn-00acd024)
- ブロック [`00acd024`](#insn-00acd024) 範囲 `[['00acd024', '00acd047']]`
  - `UNCONDITIONAL_JUMP` [`00acd044`](#insn-00acd044) → [`00acd04c`](#insn-00acd04c)
- ブロック [`00acd048`](#insn-00acd048) 範囲 `[['00acd048', '00acd04b']]`
  - `FALL_THROUGH` [`00acd048`](#insn-00acd048) → [`00acd04c`](#insn-00acd04c)
- ブロック [`00acd04c`](#insn-00acd04c) 範囲 `[['00acd04c', '00acd09f']]`
  - `CONDITIONAL_JUMP` [`00acd09c`](#insn-00acd09c) → [`00acd0b8`](#insn-00acd0b8)
  - `FALL_THROUGH` [`00acd09c`](#insn-00acd09c) → [`00acd0a0`](#insn-00acd0a0)
- ブロック [`00acd0a0`](#insn-00acd0a0) 範囲 `[['00acd0a0', '00acd0b7']]`
  - `UNCONDITIONAL_JUMP` [`00acd0b4`](#insn-00acd0b4) → [`00acd1a4`](#insn-00acd1a4)
- ブロック [`00acd0b8`](#insn-00acd0b8) 範囲 `[['00acd0b8', '00acd113']]`
  - `CONDITIONAL_JUMP` [`00acd110`](#insn-00acd110) → [`00acd1a0`](#insn-00acd1a0)
  - `FALL_THROUGH` [`00acd110`](#insn-00acd110) → [`00acd114`](#insn-00acd114)
- ブロック [`00acd114`](#insn-00acd114) 範囲 `[['00acd114', '00acd177']]`
  - `CONDITIONAL_JUMP` [`00acd174`](#insn-00acd174) → [`00acd1a4`](#insn-00acd1a4)
  - `FALL_THROUGH` [`00acd174`](#insn-00acd174) → [`00acd178`](#insn-00acd178)
- ブロック [`00acd178`](#insn-00acd178) 範囲 `[['00acd178', '00acd19f']]`
  - `UNCONDITIONAL_JUMP` [`00acd19c`](#insn-00acd19c) → [`00acd1a4`](#insn-00acd1a4)
- ブロック [`00acd1a0`](#insn-00acd1a0) 範囲 `[['00acd1a0', '00acd1a3']]`
  - `FALL_THROUGH` [`00acd1a0`](#insn-00acd1a0) → [`00acd1a4`](#insn-00acd1a4)
- ブロック [`00acd1a4`](#insn-00acd1a4) 範囲 `[['00acd1a4', '00acd1b7']]`
  - `CONDITIONAL_JUMP` [`00acd1b4`](#insn-00acd1b4) → [`00acd1d8`](#insn-00acd1d8)
  - `FALL_THROUGH` [`00acd1b4`](#insn-00acd1b4) → [`00acd1b8`](#insn-00acd1b8)
- ブロック [`00acd1b8`](#insn-00acd1b8) 範囲 `[['00acd1b8', '00acd1d7']]`
  - `UNCONDITIONAL_JUMP` [`00acd1d4`](#insn-00acd1d4) → [`00acd1e0`](#insn-00acd1e0)
- ブロック [`00acd1d8`](#insn-00acd1d8) 範囲 `[['00acd1d8', '00acd1df']]`
  - `FALL_THROUGH` [`00acd1dc`](#insn-00acd1dc) → [`00acd1e0`](#insn-00acd1e0)
- ブロック [`00acd1e0`](#insn-00acd1e0) 範囲 `[['00acd1e0', '00acd21b']]`
  - `CONDITIONAL_JUMP` [`00acd218`](#insn-00acd218) → [`00acd278`](#insn-00acd278)
  - `FALL_THROUGH` [`00acd218`](#insn-00acd218) → [`00acd21c`](#insn-00acd21c)
- ブロック [`00acd21c`](#insn-00acd21c) 範囲 `[['00acd21c', '00acd22b']]`
  - `CONDITIONAL_JUMP` [`00acd228`](#insn-00acd228) → [`00acd284`](#insn-00acd284)
  - `FALL_THROUGH` [`00acd228`](#insn-00acd228) → [`00acd22c`](#insn-00acd22c)
- ブロック [`00acd22c`](#insn-00acd22c) 範囲 `[['00acd22c', '00acd277']]`
  - `UNCONDITIONAL_JUMP` [`00acd274`](#insn-00acd274) → [`00acd27c`](#insn-00acd27c)
- ブロック [`00acd278`](#insn-00acd278) 範囲 `[['00acd278', '00acd27b']]`
  - `FALL_THROUGH` [`00acd278`](#insn-00acd278) → [`00acd27c`](#insn-00acd27c)
- ブロック [`00acd27c`](#insn-00acd27c) 範囲 `[['00acd27c', '00acd283']]`
  - `UNCONDITIONAL_JUMP` [`00acd280`](#insn-00acd280) → [`00acd288`](#insn-00acd288)
- ブロック [`00acd284`](#insn-00acd284) 範囲 `[['00acd284', '00acd287']]`
  - `FALL_THROUGH` [`00acd284`](#insn-00acd284) → [`00acd288`](#insn-00acd288)
- ブロック [`00acd288`](#insn-00acd288) 範囲 `[['00acd288', '00acd2af']]`
  - `CONDITIONAL_JUMP` [`00acd2ac`](#insn-00acd2ac) → [`00acd2d8`](#insn-00acd2d8)
  - `FALL_THROUGH` [`00acd2ac`](#insn-00acd2ac) → [`00acd2b0`](#insn-00acd2b0)
- ブロック [`00acd2b0`](#insn-00acd2b0) 範囲 `[['00acd2b0', '00acd2c7']]`
  - `CONDITIONAL_JUMP` [`00acd2c4`](#insn-00acd2c4) → [`00acd2d8`](#insn-00acd2d8)
  - `FALL_THROUGH` [`00acd2c4`](#insn-00acd2c4) → [`00acd2c8`](#insn-00acd2c8)
- ブロック [`00acd2c8`](#insn-00acd2c8) 範囲 `[['00acd2c8', '00acd2d7']]`
  - `FALL_THROUGH` [`00acd2d4`](#insn-00acd2d4) → [`00acd2d8`](#insn-00acd2d8)
- ブロック [`00acd2d8`](#insn-00acd2d8) 範囲 `[['00acd2d8', '00acd2ef']]`
  - `CONDITIONAL_JUMP` [`00acd2ec`](#insn-00acd2ec) → [`00acd344`](#insn-00acd344)
  - `FALL_THROUGH` [`00acd2ec`](#insn-00acd2ec) → [`00acd2f0`](#insn-00acd2f0)
- ブロック [`00acd2f0`](#insn-00acd2f0) 範囲 `[['00acd2f0', '00acd307']]`
- ブロック [`00acd344`](#insn-00acd344) 範囲 `[['00acd344', '00acd347']]`

## 命令位置別の参照

- [`00accf50`](#insn-00accf50) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf54`](#insn-00accf54) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf58`](#insn-00accf58) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf5c`](#insn-00accf5c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf6c`](#insn-00accf6c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf70`](#insn-00accf70) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00accf78`](#insn-00accf78) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00accf88`](#insn-00accf88) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf94`](#insn-00accf94) → `0029964e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00accf98`](#insn-00accf98) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfa8`](#insn-00accfa8) → `Stack[-0x4b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfac`](#insn-00accfac) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfb0`](#insn-00accfb0) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfb4`](#insn-00accfb4) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfc4`](#insn-00accfc4) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00accfc8`](#insn-00accfc8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfd0`](#insn-00accfd0) → [`00accfdc`](#insn-00accfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfd4`](#insn-00accfd4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfd8`](#insn-00accfd8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00accfdc`](#insn-00accfdc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfe0`](#insn-00accfe0) → [`00accfec`](#insn-00accfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfe4`](#insn-00accfe4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accfe8`](#insn-00accfe8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00accfec`](#insn-00accfec) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00accff0`](#insn-00accff0) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00accff4`](#insn-00accff4) → [`00acd048`](#insn-00acd048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd004`](#insn-00acd004) → [`00558f34`](../00558/00558f34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00558f34` · 推定シンボル `None` · 推定型 `None`
- [`00acd020`](#insn-00acd020) → [`00acd04c`](#insn-00acd04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd044`](#insn-00acd044) → [`00acd04c`](#insn-00acd04c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd054`](#insn-00acd054) → `00c1ad28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acd058`](#insn-00acd058) → `00c24d98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd05c`](#insn-00acd05c) → `00c24d94`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd060`](#insn-00acd060) → [`005377ec`](../00537/005377ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005377ec` · 推定シンボル `None` · 推定型 `None`
- [`00acd064`](#insn-00acd064) → `00c24d78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd068`](#insn-00acd068) → [`005377dc`](../00537/005377dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005377dc` · 推定シンボル `None` · 推定型 `None`
- [`00acd074`](#insn-00acd074) → `00c24d84`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd084`](#insn-00acd084) → `00c24d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd08c`](#insn-00acd08c) → `00c24d7c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd08c`](#insn-00acd08c) → `00c24d80`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd09c`](#insn-00acd09c) → [`00acd0b8`](#insn-00acd0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd0a8`](#insn-00acd0a8) → `00c24d88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0b0`](#insn-00acd0b0) → `00c24d8c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0b0`](#insn-00acd0b0) → `00c24d90`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0b4`](#insn-00acd0b4) → [`00acd1a4`](#insn-00acd1a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd0d4`](#insn-00acd0d4) → `00c24d88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0d8`](#insn-00acd0d8) → `00c24d8c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0dc`](#insn-00acd0dc) → [`00acc1a0`](00acc1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acc1a0` · 推定シンボル `None` · 推定型 `None`
- [`00acd0e4`](#insn-00acd0e4) → [`00acc038`](00acc038.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acc038` · 推定シンボル `None` · 推定型 `None`
- [`00acd0f0`](#insn-00acd0f0) → `00c24da4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0f4`](#insn-00acd0f4) → [`00acbd60`](../00acb/00acbd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acbd60` · 推定シンボル `None` · 推定型 `None`
- [`00acd0f8`](#insn-00acd0f8) → `00c24da4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0fc`](#insn-00acd0fc) → `00c24da8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd0fc`](#insn-00acd0fc) → `00c24dac`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd100`](#insn-00acd100) → [`00acbecc`](../00acb/00acbecc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acbecc` · 推定シンボル `None` · 推定型 `None`
- [`00acd104`](#insn-00acd104) → `00c24db0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd108`](#insn-00acd108) → `00c24d70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acd10c`](#insn-00acd10c) → [`00449b7c`](../00449/00449b7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449b7c` · 推定シンボル `None` · 推定型 `None`
- [`00acd110`](#insn-00acd110) → [`00acd1a0`](#insn-00acd1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd114`](#insn-00acd114) → `00c24d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd118`](#insn-00acd118) → `00c24d7c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd11c`](#insn-00acd11c) → `00c24d70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acd12c`](#insn-00acd12c) → [`00449c14`](../00449/00449c14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449c14` · 推定シンボル `None` · 推定型 `None`
- [`00acd134`](#insn-00acd134) → `00c24d8c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd138`](#insn-00acd138) → `00c24d7c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd13c`](#insn-00acd13c) → `00c24d70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acd154`](#insn-00acd154) → `00c24d88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd158`](#insn-00acd158) → [`00449c14`](../00449/00449c14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449c14` · 推定シンボル `None` · 推定型 `None`
- [`00acd160`](#insn-00acd160) → `00c24d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd170`](#insn-00acd170) → `00c24d8c`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd174`](#insn-00acd174) → [`00acd1a4`](#insn-00acd1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd17c`](#insn-00acd17c) → `00c24d98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd180`](#insn-00acd180) → `00c24da4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd194`](#insn-00acd194) → `00c24da4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd198`](#insn-00acd198) → `00c24dac`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd19c`](#insn-00acd19c) → [`00acd1a4`](#insn-00acd1a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd1a0`](#insn-00acd1a0) → `00c24d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1a0`](#insn-00acd1a0) → `00c24d8c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1a4`](#insn-00acd1a4) → `00c24d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1a4`](#insn-00acd1a4) → `00c24d7c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1b4`](#insn-00acd1b4) → [`00acd1d8`](#insn-00acd1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd1d4`](#insn-00acd1d4) → [`00acd1e0`](#insn-00acd1e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd1e4`](#insn-00acd1e4) → `00c24d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1f8`](#insn-00acd1f8) → `00c24d94`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd1fc`](#insn-00acd1fc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd208`](#insn-00acd208) → `0032f9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00acd20c`](#insn-00acd20c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd210`](#insn-00acd210) → `0032f9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00acd218`](#insn-00acd218) → [`00acd278`](#insn-00acd278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd21c`](#insn-00acd21c) → `00c24d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd220`](#insn-00acd220) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd228`](#insn-00acd228) → [`00acd284`](#insn-00acd284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd22c`](#insn-00acd22c) → `00c24d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd22c`](#insn-00acd22c) → `00c24d7c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd230`](#insn-00acd230) → `00c24d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd26c`](#insn-00acd26c) → `0032f9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00acd274`](#insn-00acd274) → [`00acd27c`](#insn-00acd27c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd27c`](#insn-00acd27c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd280`](#insn-00acd280) → [`00acd288`](#insn-00acd288) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd290`](#insn-00acd290) → `0032f9ac`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00acd294`](#insn-00acd294) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00acd298`](#insn-00acd298) → `00c24d98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00acd29c`](#insn-00acd29c) → [`0041c8e4`](../0041c/0041c8e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041c8e4` · 推定シンボル `None` · 推定型 `None`
- [`00acd2a0`](#insn-00acd2a0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd2a4`](#insn-00acd2a4) → [`00821cb4`](../00821/00821cb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00821cb4` · 推定シンボル `None` · 推定型 `None`
- [`00acd2ac`](#insn-00acd2ac) → [`00acd2d8`](#insn-00acd2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2b0`](#insn-00acd2b0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd2bc`](#insn-00acd2bc) → `0032ff0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[35]`
- [`00acd2c0`](#insn-00acd2c0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acd2c4`](#insn-00acd2c4) → [`00acd2d8`](#insn-00acd2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2c8`](#insn-00acd2c8) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00acd2cc`](#insn-00acd2cc) → [`0041c8f8`](../0041c/0041c8f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041c8f8` · 推定シンボル `None` · 推定型 `None`
- [`00acd2d0`](#insn-00acd2d0) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00acd2d4`](#insn-00acd2d4) → [`0041c8ec`](../0041c/0041c8ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041c8ec` · 推定シンボル `None` · 推定型 `None`
- [`00acd2d8`](#insn-00acd2d8) → [`00469e20`](../00469/00469e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469e20` · 推定シンボル `None` · 推定型 `None`
- [`00acd2dc`](#insn-00acd2dc) → [`0046f694`](../0046f/0046f694.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046f694` · 推定シンボル `None` · 推定型 `None`
- [`00acd2e4`](#insn-00acd2e4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2ec`](#insn-00acd2ec) → [`00acd344`](#insn-00acd344) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2f0`](#insn-00acd2f0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2f4`](#insn-00acd2f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2f8`](#insn-00acd2f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd2fc`](#insn-00acd2fc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd344`](#insn-00acd344) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00accf50`](#insn-00accf50)

~~~json
{
  "source": "00accf50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf54`](#insn-00accf54)

~~~json
{
  "source": "00accf54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf58`](#insn-00accf58)

~~~json
{
  "source": "00accf58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf5c`](#insn-00accf5c)

~~~json
{
  "source": "00accf5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf6c`](#insn-00accf6c)

~~~json
{
  "source": "00accf6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf70`](#insn-00accf70)

~~~json
{
  "source": "00accf70",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accf78`](#insn-00accf78)

~~~json
{
  "source": "00accf78",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accf88`](#insn-00accf88)

~~~json
{
  "source": "00accf88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf94`](#insn-00accf94)

~~~json
{
  "source": "00accf94",
  "target": "0029964e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029964e",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "67657453637265656e57696e646f77526174696f00",
  "capture_start": "0029964e",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00accf98`](#insn-00accf98)

~~~json
{
  "source": "00accf98",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfa8`](#insn-00accfa8)

~~~json
{
  "source": "00accfa8",
  "target": "Stack[-0x4b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfac`](#insn-00accfac)

~~~json
{
  "source": "00accfac",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfb0`](#insn-00accfb0)

~~~json
{
  "source": "00accfb0",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfb4`](#insn-00accfb4)

~~~json
{
  "source": "00accfb4",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfc4`](#insn-00accfc4)

~~~json
{
  "source": "00accfc4",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accfc8`](#insn-00accfc8)

~~~json
{
  "source": "00accfc8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfd0`](#insn-00accfd0)

~~~json
{
  "source": "00accfd0",
  "target": "00accfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfd4`](#insn-00accfd4)

~~~json
{
  "source": "00accfd4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfd8`](#insn-00accfd8)

~~~json
{
  "source": "00accfd8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accfdc`](#insn-00accfdc)

~~~json
{
  "source": "00accfdc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfe0`](#insn-00accfe0)

~~~json
{
  "source": "00accfe0",
  "target": "00accfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfe4`](#insn-00accfe4)

~~~json
{
  "source": "00accfe4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accfe8`](#insn-00accfe8)

~~~json
{
  "source": "00accfe8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accfec`](#insn-00accfec)

~~~json
{
  "source": "00accfec",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accff0`](#insn-00accff0)

~~~json
{
  "source": "00accff0",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00accff4`](#insn-00accff4)

~~~json
{
  "source": "00accff4",
  "target": "00acd048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd004`](#insn-00acd004)

~~~json
{
  "source": "00acd004",
  "target": "00558f34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd020`](#insn-00acd020)

~~~json
{
  "source": "00acd020",
  "target": "00acd04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd044`](#insn-00acd044)

~~~json
{
  "source": "00acd044",
  "target": "00acd04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd054`](#insn-00acd054)

~~~json
{
  "source": "00acd054",
  "target": "00c1ad28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ad28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acd058`](#insn-00acd058)

~~~json
{
  "source": "00acd058",
  "target": "00c24d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d98",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd05c`](#insn-00acd05c)

~~~json
{
  "source": "00acd05c",
  "target": "00c24d94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d94",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd060`](#insn-00acd060)

~~~json
{
  "source": "00acd060",
  "target": "005377ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd064`](#insn-00acd064)

~~~json
{
  "source": "00acd064",
  "target": "00c24d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d78",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd068`](#insn-00acd068)

~~~json
{
  "source": "00acd068",
  "target": "005377dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd074`](#insn-00acd074)

~~~json
{
  "source": "00acd074",
  "target": "00c24d84",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d84",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd084`](#insn-00acd084)

~~~json
{
  "source": "00acd084",
  "target": "00c24d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d78",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd08c`](#insn-00acd08c)

~~~json
{
  "source": "00acd08c",
  "target": "00c24d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d7c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd08c`](#insn-00acd08c)

~~~json
{
  "source": "00acd08c",
  "target": "00c24d80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d80",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd09c`](#insn-00acd09c)

~~~json
{
  "source": "00acd09c",
  "target": "00acd0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd0a8`](#insn-00acd0a8)

~~~json
{
  "source": "00acd0a8",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0b0`](#insn-00acd0b0)

~~~json
{
  "source": "00acd0b0",
  "target": "00c24d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0b0`](#insn-00acd0b0)

~~~json
{
  "source": "00acd0b0",
  "target": "00c24d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d90",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0b4`](#insn-00acd0b4)

~~~json
{
  "source": "00acd0b4",
  "target": "00acd1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd0d4`](#insn-00acd0d4)

~~~json
{
  "source": "00acd0d4",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0d8`](#insn-00acd0d8)

~~~json
{
  "source": "00acd0d8",
  "target": "00c24d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0dc`](#insn-00acd0dc)

~~~json
{
  "source": "00acd0dc",
  "target": "00acc1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd0e4`](#insn-00acd0e4)

~~~json
{
  "source": "00acd0e4",
  "target": "00acc038",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd0f0`](#insn-00acd0f0)

~~~json
{
  "source": "00acd0f0",
  "target": "00c24da4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24da4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0f4`](#insn-00acd0f4)

~~~json
{
  "source": "00acd0f4",
  "target": "00acbd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd0f8`](#insn-00acd0f8)

~~~json
{
  "source": "00acd0f8",
  "target": "00c24da4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24da4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0fc`](#insn-00acd0fc)

~~~json
{
  "source": "00acd0fc",
  "target": "00c24da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24da8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd0fc`](#insn-00acd0fc)

~~~json
{
  "source": "00acd0fc",
  "target": "00c24dac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24dac",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd100`](#insn-00acd100)

~~~json
{
  "source": "00acd100",
  "target": "00acbecc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd104`](#insn-00acd104)

~~~json
{
  "source": "00acd104",
  "target": "00c24db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24db0",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd108`](#insn-00acd108)

~~~json
{
  "source": "00acd108",
  "target": "00c24d70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd10c`](#insn-00acd10c)

~~~json
{
  "source": "00acd10c",
  "target": "00449b7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd110`](#insn-00acd110)

~~~json
{
  "source": "00acd110",
  "target": "00acd1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd114`](#insn-00acd114)

~~~json
{
  "source": "00acd114",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd118`](#insn-00acd118)

~~~json
{
  "source": "00acd118",
  "target": "00c24d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d7c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd11c`](#insn-00acd11c)

~~~json
{
  "source": "00acd11c",
  "target": "00c24d70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd12c`](#insn-00acd12c)

~~~json
{
  "source": "00acd12c",
  "target": "00449c14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd134`](#insn-00acd134)

~~~json
{
  "source": "00acd134",
  "target": "00c24d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd138`](#insn-00acd138)

~~~json
{
  "source": "00acd138",
  "target": "00c24d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d7c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd13c`](#insn-00acd13c)

~~~json
{
  "source": "00acd13c",
  "target": "00c24d70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd154`](#insn-00acd154)

~~~json
{
  "source": "00acd154",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd158`](#insn-00acd158)

~~~json
{
  "source": "00acd158",
  "target": "00449c14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd160`](#insn-00acd160)

~~~json
{
  "source": "00acd160",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd170`](#insn-00acd170)

~~~json
{
  "source": "00acd170",
  "target": "00c24d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd174`](#insn-00acd174)

~~~json
{
  "source": "00acd174",
  "target": "00acd1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd17c`](#insn-00acd17c)

~~~json
{
  "source": "00acd17c",
  "target": "00c24d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d98",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd180`](#insn-00acd180)

~~~json
{
  "source": "00acd180",
  "target": "00c24da4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24da4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd194`](#insn-00acd194)

~~~json
{
  "source": "00acd194",
  "target": "00c24da4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24da4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd198`](#insn-00acd198)

~~~json
{
  "source": "00acd198",
  "target": "00c24dac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24dac",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd19c`](#insn-00acd19c)

~~~json
{
  "source": "00acd19c",
  "target": "00acd1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd1a0`](#insn-00acd1a0)

~~~json
{
  "source": "00acd1a0",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1a0`](#insn-00acd1a0)

~~~json
{
  "source": "00acd1a0",
  "target": "00c24d8c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d8c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1a4`](#insn-00acd1a4)

~~~json
{
  "source": "00acd1a4",
  "target": "00c24d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d78",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1a4`](#insn-00acd1a4)

~~~json
{
  "source": "00acd1a4",
  "target": "00c24d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d7c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1b4`](#insn-00acd1b4)

~~~json
{
  "source": "00acd1b4",
  "target": "00acd1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd1d4`](#insn-00acd1d4)

~~~json
{
  "source": "00acd1d4",
  "target": "00acd1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd1e4`](#insn-00acd1e4)

~~~json
{
  "source": "00acd1e4",
  "target": "00c24d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d90",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1f8`](#insn-00acd1f8)

~~~json
{
  "source": "00acd1f8",
  "target": "00c24d94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d94",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd1fc`](#insn-00acd1fc)

~~~json
{
  "source": "00acd1fc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd208`](#insn-00acd208)

~~~json
{
  "source": "00acd208",
  "target": "0032f9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acd20c`](#insn-00acd20c)

~~~json
{
  "source": "00acd20c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd210`](#insn-00acd210)

~~~json
{
  "source": "00acd210",
  "target": "0032f9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acd218`](#insn-00acd218)

~~~json
{
  "source": "00acd218",
  "target": "00acd278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd21c`](#insn-00acd21c)

~~~json
{
  "source": "00acd21c",
  "target": "00c24d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d90",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd220`](#insn-00acd220)

~~~json
{
  "source": "00acd220",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd228`](#insn-00acd228)

~~~json
{
  "source": "00acd228",
  "target": "00acd284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd22c`](#insn-00acd22c)

~~~json
{
  "source": "00acd22c",
  "target": "00c24d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d78",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd22c`](#insn-00acd22c)

~~~json
{
  "source": "00acd22c",
  "target": "00c24d7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d7c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd230`](#insn-00acd230)

~~~json
{
  "source": "00acd230",
  "target": "00c24d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d88",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd26c`](#insn-00acd26c)

~~~json
{
  "source": "00acd26c",
  "target": "0032f9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acd274`](#insn-00acd274)

~~~json
{
  "source": "00acd274",
  "target": "00acd27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd27c`](#insn-00acd27c)

~~~json
{
  "source": "00acd27c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd280`](#insn-00acd280)

~~~json
{
  "source": "00acd280",
  "target": "00acd288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd290`](#insn-00acd290)

~~~json
{
  "source": "00acd290",
  "target": "0032f9ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acd294`](#insn-00acd294)

~~~json
{
  "source": "00acd294",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd298`](#insn-00acd298)

~~~json
{
  "source": "00acd298",
  "target": "00c24d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24d98",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acd29c`](#insn-00acd29c)

~~~json
{
  "source": "00acd29c",
  "target": "0041c8e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2a0`](#insn-00acd2a0)

~~~json
{
  "source": "00acd2a0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2a4`](#insn-00acd2a4)

~~~json
{
  "source": "00acd2a4",
  "target": "00821cb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2ac`](#insn-00acd2ac)

~~~json
{
  "source": "00acd2ac",
  "target": "00acd2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2b0`](#insn-00acd2b0)

~~~json
{
  "source": "00acd2b0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2bc`](#insn-00acd2bc)

~~~json
{
  "source": "00acd2bc",
  "target": "0032ff0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fef1",
  "offset": 27,
  "size": 35,
  "datatype": "byte[35]",
  "bytes": "440e304c0c1d2093049e069d0805480a05490c02500c1f304c0e00d3dedd0648",
  "capture_start": "0032fef1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acd2c0`](#insn-00acd2c0)

~~~json
{
  "source": "00acd2c0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2c4`](#insn-00acd2c4)

~~~json
{
  "source": "00acd2c4",
  "target": "00acd2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2c8`](#insn-00acd2c8)

~~~json
{
  "source": "00acd2c8",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2cc`](#insn-00acd2cc)

~~~json
{
  "source": "00acd2cc",
  "target": "0041c8f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2d0`](#insn-00acd2d0)

~~~json
{
  "source": "00acd2d0",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2d4`](#insn-00acd2d4)

~~~json
{
  "source": "00acd2d4",
  "target": "0041c8ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2d8`](#insn-00acd2d8)

~~~json
{
  "source": "00acd2d8",
  "target": "00469e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2dc`](#insn-00acd2dc)

~~~json
{
  "source": "00acd2dc",
  "target": "0046f694",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd2e4`](#insn-00acd2e4)

~~~json
{
  "source": "00acd2e4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2ec`](#insn-00acd2ec)

~~~json
{
  "source": "00acd2ec",
  "target": "00acd344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2f0`](#insn-00acd2f0)

~~~json
{
  "source": "00acd2f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2f4`](#insn-00acd2f4)

~~~json
{
  "source": "00acd2f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2f8`](#insn-00acd2f8)

~~~json
{
  "source": "00acd2f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd2fc`](#insn-00acd2fc)

~~~json
{
  "source": "00acd2fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd344`](#insn-00acd344)

~~~json
{
  "source": "00acd344",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
