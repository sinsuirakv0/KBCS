# 00a9fbcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9fb88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-28abb97a8d39b73255f87e10e4cf906c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0088.md#review-e3f27bd2162558288a2f690cb2e1c9da)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9fbcc",
  "name": "FUN_00a9fbcc",
  "size": 1860,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77f3d477a7a18621dc130344feeb1f80fd25711033b0c8c3c9c2e6d9ded8d973",
  "source_text_sha256": "77f3d477a7a18621dc130344feeb1f80fd25711033b0c8c3c9c2e6d9ded8d973",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9fbcc",
        "00aa030f"
      ]
    ],
    "bytes_sha256": "bf2f80b7ca05ad1b9020ffd33ab28bd833441ce450800503b37149818d7d41e7",
    "instruction_count": 465,
    "instruction_bytes": 1860,
    "body_bytes": 1860,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006e4aec](../006e4/006e4aec.md)
- [009f1ea8](../009f1/009f1ea8.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0066398c](../00663/0066398c.md)
- [0078aefc](../0078a/0078aefc.md)
- [0078af80](../0078a/0078af80.md)
- [007bd9d0](../007bd/007bd9d0.md)
- [007cebc8](../007ce/007cebc8.md)
- [007cf4b0](../007cf/007cf4b0.md)
- [007cf950](../007cf/007cf950.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [0088f9e4](../0088f/0088f9e4.md)
- [00a06cfc](../00a06/00a06cfc.md)
- [00a5b0c8](../00a5b/00a5b0c8.md)
- [00a5b31c](../00a5b/00a5b31c.md)
- [00a9f124](../00a9f/00a9f124.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 10016 bytes

~~~c

ulong FUN_00a9fbcc(int param_1,int param_2,int param_3,uint param_4,int param_5,int param_6,
                  uint param_7,uint param_8)

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
  char *pcVar10;
  
                    /* catch() { ... } // from try @ 00a9f574 with catch @ 00a9fbcc */
                    /* catch() { ... } // from try @ 00a9f4bc with catch @ 00a9fbd4 */
                    /* catch() { ... } // from try @ 00a9ef28 with catch @ 00a9fbdc */
  lVar6 = FUN_0081f580();
  uVar7 = FUN_005c2710(lVar6 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar7 & 1) != 0) {
    if ((int)param_4 < 1) {
      uVar7 = 0;
    }
    else {
      lVar6 = FUN_0081f580();
      lVar6 = (long)*(int *)(lVar6 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc +
                             (long)*(int *)(&DAT_002f48d0 + (long)param_6 * 4) * 4 + 0x9ee88) * 100;
      if (param_4 != 1) {
                    /* try { // try from 00a9fe4c to 00b9feb3 has its CatchHandler @ 00a9fe4c
                       catch() { ... } // from try @ 00a9fe4c with catch @ 00a9fe4c
                       catch() { ... } // from try @ 00a9fec4 with catch @ 00a9fe4c
                       catch() { ... } // from try @ 00aa019c with catch @ 00a9fe4c
                       catch() { ... } // from try @ 00aa02a4 with catch @ 00a9fe4c
                       catch() { ... } // from try @ 00aa0884 with catch @ 00a9fe4c
                       catch() { ... } // from try @ 00aa18c4 with catch @ 00a9fe4c */
        uVar13 = 1;
        do {
          FUN_0081f580();
          if (uVar13 < 200) {
            lVar8 = FUN_0081f580();
            iVar4 = *(int *)(lVar8 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc +
                             (long)*(int *)(&DAT_002f48d0 + (long)param_6 * 4) * 4 + 0x9ee88);
                    /* try { // try from 00a9feb4 to 00b9fec3 has its CatchHandler @ 00aa1b10 */
            lVar8 = FUN_0081f580();
                    /* try { // try from 00a9fec4 to 00b9ff63 has its CatchHandler @ 00a9fe4c */
            lVar6 = lVar6 + (long)*(int *)(lVar8 + (long)param_2 * 0x50 +
                                           (ulong)((uVar13 & 0xff) / 10) * 4 + 0x44fcc4) *
                            (long)iVar4;
          }
          uVar13 = uVar13 + 1;
        } while (param_4 != uVar13);
      }
      uVar7 = (lVar6 + 0x32) / 100;
    }
    if ((param_7 & 1) != 0) goto LAB_00aa02ec;
    lVar6 = FUN_0081f580();
    iVar4 = FUN_00a5b0c8("ScoreBonusMap.json" + lVar6 + 0xb,10);
    lVar6 = FUN_0081f580();
    iVar5 = FUN_0088f9e4(lVar6 + 0x448e70,0,param_2);
    uVar7 = (long)(((long)(uVar7 * (long)iVar4) / 100 + uVar7) * (long)(iVar5 + 100)) / 100;
    iVar4 = FUN_00a9f124(param_1,param_2,param_3,0x1f,0);
    if (1 < param_3) {
      iVar5 = FUN_007cf4b0(0);
      if (iVar5 == 0) {
LAB_00a9fe40:
        uVar11 = 9;
      }
      else {
        FUN_0081f580();
        uVar9 = FUN_0078aefc();
        if ((uVar9 & 1) != 0) goto LAB_00a9fe40;
        iVar5 = FUN_007cf4b0(0);
        if (iVar5 != -9) {
          FUN_0081f580();
          uVar9 = FUN_0078af80();
          if ((uVar9 & 1) == 0) {
            FUN_0081f580();
            uVar9 = FUN_007bd9d0();
            if ((uVar9 & 1) == 0) goto LAB_00aa0290;
          }
        }
        uVar11 = 0x10;
      }
      lVar6 = FUN_0081f580();
                    /* try { // try from 00aa027c to 00ba028f has its CatchHandler @ 00aa1ab8 */
      iVar5 = FUN_0066398c(lVar6 + 0x1560,param_2,uVar11,1,0);
      iVar4 = iVar5 + iVar4;
    }
LAB_00aa0290:
                    /* try { // try from 00aa0290 to 00ba02a3 has its CatchHandler @ 00aa1aa8 */
    if (0 < iVar4) {
                    /* try { // try from 00aa02a4 to 00ba02ff has its CatchHandler @ 00a9fe4c */
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    iVar4 = FUN_00a9f124(param_1,param_2,param_3,0x46,0);
    if (0 < iVar4) {
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    goto LAB_00aa02ec;
  }
  lVar6 = FUN_0081f580();
  if ((*(int *)(BYTE_ARRAY_0032f921 + lVar6 + 0x13) < 3) &&
     (lVar6 = FUN_0081f580(), (BYTE_ARRAY_00334045[lVar6 + 3] & 1) == 0)) {
    lVar8 = FUN_0081f580();
    lVar6 = (long)param_2 + 2;
    iVar4 = *(int *)((long)__DT_JMPREL +
                    lVar8 + lVar6 * 0x1c4 + (long)*(int *)(&DAT_002f48dc + (long)param_6 * 4) * 4 +
                    0xa370);
    lVar8 = FUN_0081f580();
                    /* try { // try from 00a9ff64 to 00b9ff73 has its CatchHandler @ 00aa1ad4 */
    lVar8 = ((long)*(int *)(PTR_DAT_00c1b870 +
                           (long)*(int *)(BYTE_ARRAY_0032f921 + lVar8 + 0x13) * 4) + 10) *
            (long)iVar4 + 5;
                    /* try { // try from 00a9ff74 to 00b9ff87 has its CatchHandler @ 00aa1ad0 */
    lVar12 = SUB168(SEXT816(lVar8) * SEXT816(0x6666666666666667),8);
    lVar8 = lVar8 / 10 + (lVar8 >> 0x3f);
LAB_00a9ff84:
    uVar7 = lVar8 - (lVar12 >> 0x3f);
  }
  else {
    lVar6 = FUN_0081f580();
    iVar4 = *(int *)(BYTE_ARRAY_0032f921 + lVar6 + 0x13);
    lVar8 = FUN_0081f580();
    lVar6 = (long)param_2 + 2;
    iVar5 = *(int *)((long)__DT_JMPREL +
                    lVar8 + lVar6 * 0x1c4 + (long)*(int *)(&DAT_002f48dc + (long)param_6 * 4) * 4 +
                    0xa370);
    lVar8 = FUN_0081f580();
    iVar1 = FUN_00a06cfc(*(long *)(lVar8 + 0x9ee70) + (long)param_5 * 0x38);
    uVar7 = ((long)iVar5 * (long)iVar1 + 0x32) / 100;
    if (iVar4 == 3) {
      if ((param_8 & 1) == 0) {
        lVar8 = FUN_0081f580();
        uVar2 = FUN_007cf950(0);
        uVar3 = FUN_007cfcd8();
        iVar4 = FUN_007cebc8(lVar8 + 0x333288,uVar2,uVar3);
        lVar8 = (long)iVar4;
      }
      else {
        lVar8 = 100;
      }
      lVar8 = lVar8 * uVar7;
      lVar12 = SUB168(SEXT816(lVar8) * ZEXT816(0xa3d70a3d70a3d70b),8);
      lVar8 = lVar8 / 100 + (lVar8 >> 0x3f);
      goto LAB_00a9ff84;
    }
  }
  lVar8 = FUN_0081f580();
  uVar9 = FUN_005c2710(lVar8 + 0x2868);
  lVar8 = FUN_0081f580();
  if ((uVar9 & 1) == 0) {
                    /* try { // try from 00a9ffa8 to 00b9ffbb has its CatchHandler @ 00aa1b48 */
    if (*(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa3b8) == 0) goto LAB_00aa0038;
LAB_00a9ffd8:
    lVar8 = FUN_0081f580();
    uVar9 = FUN_005c2710(lVar8 + 0x2868);
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_0081f580(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa484) != 0))
    goto LAB_00aa0038;
    lVar6 = FUN_0081f580();
                    /* try { // try from 00aa0018 to 00ba001f has its CatchHandler @ 00aa1b48 */
    iVar4 = FUN_00a5b31c("ScoreBonusMap.json" + lVar6 + 0xb,0x10);
                    /* try { // try from 00aa0020 to 00ba00ab has its CatchHandler @ 00aa1b2c */
    lVar6 = FUN_0081f580();
    pcVar10 = "ScoreBonusMap.json" + lVar6 + 0xb;
    uVar11 = 0x10;
  }
  else {
                    /* try { // try from 00a9ffc8 to 00ba0013 has its CatchHandler @ 00aa1b0c */
    if (*(int *)(lVar8 + lVar6 * 0x770 + 0x9eedc) != 0) goto LAB_00a9ffd8;
    FUN_0081f580();
LAB_00aa0038:
    lVar8 = FUN_0081f580();
    uVar9 = FUN_005c2710(lVar8 + 0x2868);
    lVar8 = FUN_0081f580();
    if ((uVar9 & 1) == 0) {
      if (*(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa3b8) != 0) {
LAB_00aa0088:
        lVar8 = FUN_0081f580();
        uVar9 = FUN_005c2710(lVar8 + 0x2868);
        if (((uVar9 & 1) == 0) &&
           (lVar8 = FUN_0081f580(),
           *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa484) == 1)) {
          lVar6 = FUN_0081f580();
          iVar4 = FUN_00a5b31c("ScoreBonusMap.json" + lVar6 + 0xb,0x12);
          lVar6 = FUN_0081f580();
          pcVar10 = "ScoreBonusMap.json" + lVar6 + 0xb;
          uVar11 = 0x12;
          goto LAB_00aa0208;
        }
      }
    }
    else {
      if (*(int *)(lVar8 + lVar6 * 0x770 + 0x9eedc) != 0) goto LAB_00aa0088;
      FUN_0081f580();
    }
    lVar8 = FUN_0081f580();
    uVar9 = FUN_005c2710(lVar8 + 0x2868);
                    /* try { // try from 00aa0108 to 00ba010f has its CatchHandler @ 00aa1b3c */
                    /* try { // try from 00aa0114 to 00ba019b has its CatchHandler @ 00aa1b50 */
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_0081f580(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa484) == 2))
    {
      lVar6 = FUN_0081f580();
      iVar4 = FUN_00a5b31c("ScoreBonusMap.json" + lVar6 + 0xb,0x16);
      lVar6 = FUN_0081f580();
      pcVar10 = "ScoreBonusMap.json" + lVar6 + 0xb;
      uVar11 = 0x16;
    }
    else {
      lVar8 = FUN_0081f580();
      uVar9 = FUN_005c2710(lVar8 + 0x2868);
      if (((uVar9 & 1) == 0) &&
         (lVar8 = FUN_0081f580(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa484) == 3)
         ) {
        lVar6 = FUN_0081f580();
        iVar4 = FUN_00a5b31c("ScoreBonusMap.json" + lVar6 + 0xb,0x17);
                    /* try { // try from 00aa019c to 00ba0223 has its CatchHandler @ 00a9fe4c */
        lVar6 = FUN_0081f580();
        pcVar10 = "ScoreBonusMap.json" + lVar6 + 0xb;
        uVar11 = 0x17;
      }
      else {
        lVar8 = FUN_0081f580();
        uVar9 = FUN_005c2710(lVar8 + 0x2868);
        if (((uVar9 & 1) != 0) ||
           (lVar8 = FUN_0081f580(),
           *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0xa484) != 4)) goto LAB_00aa02ec;
        lVar6 = FUN_0081f580();
        iVar4 = FUN_00a5b31c("ScoreBonusMap.json" + lVar6 + 0xb,0x18);
        lVar6 = FUN_0081f580();
        pcVar10 = "ScoreBonusMap.json" + lVar6 + 0xb;
        uVar11 = 0x18;
      }
    }
  }
LAB_00aa0208:
  iVar5 = FUN_00a5b0c8(pcVar10,uVar11);
                    /* try { // try from 00aa0224 to 00ba022b has its CatchHandler @ 00aa1b48 */
  uVar7 = (long)(uVar7 * (long)(iVar4 - iVar5)) / 100 + uVar7;
LAB_00aa02ec:
                    /* try { // try from 00aa0300 to 00ba0313 has its CatchHandler @ 00aa1af0 */
  return uVar7 & 0xffffffff;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9fbcc"></a> `00a9fbcc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a9fbd0"></a> `00a9fbd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9fbd4"></a> `00a9fbd4` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9fbd8"></a> `00a9fbd8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9fbdc"></a> `00a9fbdc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a9fbe0"></a> `00a9fbe0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a9fbe4"></a> `00a9fbe4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a9fbe8"></a> `00a9fbe8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a9fbec"></a> `00a9fbec` | `f9 03 07 2a` | mov w25,w7 | `FALL_THROUGH`
<a id="insn-00a9fbf0"></a> `00a9fbf0` | `f7 03 06 2a` | mov w23,w6 | `FALL_THROUGH`
<a id="insn-00a9fbf4"></a> `00a9fbf4` | `f3 03 05 2a` | mov w19,w5 | `FALL_THROUGH`
<a id="insn-00a9fbf8"></a> `00a9fbf8` | `fa 03 04 2a` | mov w26,w4 | `FALL_THROUGH`
<a id="insn-00a9fbfc"></a> `00a9fbfc` | `f8 03 03 2a` | mov w24,w3 | `FALL_THROUGH`
<a id="insn-00a9fc00"></a> `00a9fc00` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00a9fc04"></a> `00a9fc04` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00a9fc08"></a> `00a9fc08` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00a9fc0c"></a> `00a9fc0c` | `5d fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc10"></a> `00a9fc10` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00a9fc14"></a> `00a9fc14` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00a9fc18"></a> `00a9fc18` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9fc1c"></a> `00a9fc1c` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00a9fc20"></a> `00a9fc20` | `bc 8a ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc24"></a> `00a9fc24` | `60 06 00 37` | tbnz w0,#0x0,0x00a9fcf0 | `CONDITIONAL_JUMP`
<a id="insn-00a9fc28"></a> `00a9fc28` | `56 fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc2c"></a> `00a9fc2c` | `88 26 9f 52` | mov w8,#0xf934 | `FALL_THROUGH`
<a id="insn-00a9fc30"></a> `00a9fc30` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fc34"></a> `00a9fc34` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fc38"></a> `00a9fc38` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9fc3c"></a> `00a9fc3c` | `cc 00 00 54` | b.gt 0x00a9fc54 | `CONDITIONAL_JUMP`
<a id="insn-00a9fc40"></a> `00a9fc40` | `50 fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc44"></a> `00a9fc44` | `08 09 88 52` | mov w8,#0x4048 | `FALL_THROUGH`
<a id="insn-00a9fc48"></a> `00a9fc48` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fc4c"></a> `00a9fc4c` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a9fc50"></a> `00a9fc50` | `48 16 00 36` | tbz w8,#0x0,0x00a9ff18 | `CONDITIONAL_JUMP`
<a id="insn-00a9fc54"></a> `00a9fc54` | `4b fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc58"></a> `00a9fc58` | `88 26 9f 52` | mov w8,#0xf934 | `FALL_THROUGH`
<a id="insn-00a9fc5c"></a> `00a9fc5c` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fc60"></a> `00a9fc60` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fc64"></a> `00a9fc64` | `47 fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc68"></a> `00a9fc68` | `a8 7e 40 93` | sxtw x8,w21 | `FALL_THROUGH`
<a id="insn-00a9fc6c"></a> `00a9fc6c` | `a9 c2 ff b0` | adrp x9,0x2f4000 | `FALL_THROUGH`
<a id="insn-00a9fc70"></a> `00a9fc70` | `29 71 23 91` | add x9,x9,#0x8dc | `FALL_THROUGH`
<a id="insn-00a9fc74"></a> `00a9fc74` | `29 d9 b3 b8` | ldrsw x9,[x9, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00a9fc78"></a> `00a9fc78` | `16 09 00 91` | add x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9fc7c"></a> `00a9fc7c` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00a9fc80"></a> `00a9fc80` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9fc84"></a> `00a9fc84` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a9fc88"></a> `00a9fc88` | `09 b5 93 52` | mov w9,#0x9da8 | `FALL_THROUGH`
<a id="insn-00a9fc8c"></a> `00a9fc8c` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fc90"></a> `00a9fc90` | `13 69 a9 b8` | ldrsw x19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fc94"></a> `00a9fc94` | `3b fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fc98"></a> `00a9fc98` | `08 ce 9d 52` | mov w8,#0xee70 | `FALL_THROUGH`
<a id="insn-00a9fc9c"></a> `00a9fc9c` | `09 07 80 52` | mov w9,#0x38 | `FALL_THROUGH`
<a id="insn-00a9fca0"></a> `00a9fca0` | `28 01 a0 72` | movk w8,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fca4"></a> `00a9fca4` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fca8"></a> `00a9fca8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00a9fcac"></a> `00a9fcac` | `40 23 29 9b` | smaddl x0,w26,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9fcb0"></a> `00a9fcb0` | `13 9c fd 97` | bl 0x00a06cfc | `UNCONDITIONAL_CALL`
<a id="insn-00a9fcb4"></a> `00a9fcb4` | `77 e1 9a d2` | mov x23,#0xd70b | `FALL_THROUGH`
<a id="insn-00a9fcb8"></a> `00a9fcb8` | `68 7e 20 9b` | smull x8,w19,w0 | `FALL_THROUGH`
<a id="insn-00a9fcbc"></a> `00a9fcbc` | `9f 0e 00 71` | cmp w20,#0x3 | `FALL_THROUGH`
<a id="insn-00a9fcc0"></a> `00a9fcc0` | `77 14 ae f2` | movk x23,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fcc4"></a> `00a9fcc4` | `b7 47 c1 f2` | movk x23,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00a9fcc8"></a> `00a9fcc8` | `f7 7a f4 f2` | movk x23,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00a9fccc"></a> `00a9fccc` | `08 c9 00 91` | add x8,x8,#0x32 | `FALL_THROUGH`
<a id="insn-00a9fcd0"></a> `00a9fcd0` | `09 7d 57 9b` | smulh x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00a9fcd4"></a> `00a9fcd4` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00a9fcd8"></a> `00a9fcd8` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00a9fcdc"></a> `00a9fcdc` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00a9fce0"></a> `00a9fce0` | `41 15 00 54` | b.ne 0x00a9ff88 | `CONDITIONAL_JUMP`
<a id="insn-00a9fce4"></a> `00a9fce4` | `99 0f 00 36` | tbz w25,#0x0,0x00a9fed4 | `CONDITIONAL_JUMP`
<a id="insn-00a9fce8"></a> `00a9fce8` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00a9fcec"></a> `00a9fcec` | `86 00 00 14` | b 0x00a9ff04 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9fcf0"></a> `00a9fcf0` | `79 e1 9a d2` | mov x25,#0xd70b | `FALL_THROUGH`
<a id="insn-00a9fcf4"></a> `00a9fcf4` | `1f 07 00 71` | cmp w24,#0x1 | `FALL_THROUGH`
<a id="insn-00a9fcf8"></a> `00a9fcf8` | `79 14 ae f2` | movk x25,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fcfc"></a> `00a9fcfc` | `b9 47 c1 f2` | movk x25,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00a9fd00"></a> `00a9fd00` | `f9 7a f4 f2` | movk x25,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00a9fd04"></a> `00a9fd04` | `cb 04 00 54` | b.lt 0x00a9fd9c | `CONDITIONAL_JUMP`
<a id="insn-00a9fd08"></a> `00a9fd08` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-00a9fd0c"></a> `00a9fd0c` | `f7 5b 01 29` | stp w23,w22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a9fd10"></a> `00a9fd10` | `1a 7d 40 93` | sxtw x26,w8 | `FALL_THROUGH`
<a id="insn-00a9fd14"></a> `00a9fd14` | `b5 83 1f f8` | stur x21,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9fd18"></a> `00a9fd18` | `b5 c2 ff b0` | adrp x21,0x2f4000 | `FALL_THROUGH`
<a id="insn-00a9fd1c"></a> `00a9fd1c` | `b5 42 23 91` | add x21,x21,#0x8d0 | `FALL_THROUGH`
<a id="insn-00a9fd20"></a> `00a9fd20` | `5b 0b 00 91` | add x27,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00a9fd24"></a> `00a9fd24` | `17 fe f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fd28"></a> `00a9fd28` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00a9fd2c"></a> `00a9fd2c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00a9fd30"></a> `00a9fd30` | `1f 07 00 71` | cmp w24,#0x1 | `FALL_THROUGH`
<a id="insn-00a9fd34"></a> `00a9fd34` | `68 03 08 9b` | madd x8,x27,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9fd38"></a> `00a9fd38` | `f4 0b 00 f9` | str x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9fd3c"></a> `00a9fd3c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00a9fd40"></a> `00a9fd40` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9fd44"></a> `00a9fd44` | `a9 da b3 b8` | ldrsw x9,[x21, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00a9fd48"></a> `00a9fd48` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a9fd4c"></a> `00a9fd4c` | `09 d1 9d 52` | mov w9,#0xee88 | `FALL_THROUGH`
<a id="insn-00a9fd50"></a> `00a9fd50` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fd54"></a> `00a9fd54` | `08 69 a9 b8` | ldrsw x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fd58"></a> `00a9fd58` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00a9fd5c"></a> `00a9fd5c` | `19 7d 29 9b` | smull x25,w8,w9 | `FALL_THROUGH`
<a id="insn-00a9fd60"></a> `00a9fd60` | `41 07 00 54` | b.ne 0x00a9fe48 | `CONDITIONAL_JUMP`
<a id="insn-00a9fd64"></a> `00a9fd64` | `28 cb 00 91` | add x8,x25,#0x32 | `FALL_THROUGH`
<a id="insn-00a9fd68"></a> `00a9fd68` | `79 e1 9a d2` | mov x25,#0xd70b | `FALL_THROUGH`
<a id="insn-00a9fd6c"></a> `00a9fd6c` | `b5 83 5f f8` | ldur x21,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9fd70"></a> `00a9fd70` | `79 14 ae f2` | movk x25,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fd74"></a> `00a9fd74` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9fd78"></a> `00a9fd78` | `b9 47 c1 f2` | movk x25,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00a9fd7c"></a> `00a9fd7c` | `f9 7a f4 f2` | movk x25,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00a9fd80"></a> `00a9fd80` | `09 7d 59 9b` | smulh x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00a9fd84"></a> `00a9fd84` | `f7 5b 41 29` | ldp w23,w22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a9fd88"></a> `00a9fd88` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00a9fd8c"></a> `00a9fd8c` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00a9fd90"></a> `00a9fd90` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00a9fd94"></a> `00a9fd94` | `97 00 00 36` | tbz w23,#0x0,0x00a9fda4 | `CONDITIONAL_JUMP`
<a id="insn-00a9fd98"></a> `00a9fd98` | `55 01 00 14` | b 0x00aa02ec | `UNCONDITIONAL_JUMP`
<a id="insn-00a9fd9c"></a> `00a9fd9c` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00a9fda0"></a> `00a9fda0` | `77 2a 00 37` | tbnz w23,#0x0,0x00aa02ec | `CONDITIONAL_JUMP`
<a id="insn-00a9fda4"></a> `00a9fda4` | `f7 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fda8"></a> `00a9fda8` | `08 5c 4a 91` | add x8,x0,#0x297, LSL #12 | `FALL_THROUGH`
<a id="insn-00a9fdac"></a> `00a9fdac` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00a9fdb0"></a> `00a9fdb0` | `00 e1 07 91` | add x0,x8,#0x1f8 | `FALL_THROUGH`
<a id="insn-00a9fdb4"></a> `00a9fdb4` | `c5 ec fe 97` | bl 0x00a5b0c8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fdb8"></a> `00a9fdb8` | `08 7c 40 93` | sxtw x8,w0 | `FALL_THROUGH`
<a id="insn-00a9fdbc"></a> `00a9fdbc` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00a9fdc0"></a> `00a9fdc0` | `09 7d 59 9b` | smulh x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00a9fdc4"></a> `00a9fdc4` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00a9fdc8"></a> `00a9fdc8` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00a9fdcc"></a> `00a9fdcc` | `28 fd 48 8b` | add x8,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00a9fdd0"></a> `00a9fdd0` | `13 01 13 8b` | add x19,x8,x19 | `FALL_THROUGH`
<a id="insn-00a9fdd4"></a> `00a9fdd4` | `eb fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fdd8"></a> `00a9fdd8` | `08 20 51 91` | add x8,x0,#0x448, LSL #12 | `FALL_THROUGH`
<a id="insn-00a9fddc"></a> `00a9fddc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a9fde0"></a> `00a9fde0` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00a9fde4"></a> `00a9fde4` | `00 c1 39 91` | add x0,x8,#0xe70 | `FALL_THROUGH`
<a id="insn-00a9fde8"></a> `00a9fde8` | `ff be f7 97` | bl 0x0088f9e4 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fdec"></a> `00a9fdec` | `08 90 01 11` | add w8,w0,#0x64 | `FALL_THROUGH`
<a id="insn-00a9fdf0"></a> `00a9fdf0` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00a9fdf4"></a> `00a9fdf4` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00a9fdf8"></a> `00a9fdf8` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00a9fdfc"></a> `00a9fdfc` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00a9fe00"></a> `00a9fe00` | `e3 03 80 52` | mov w3,#0x1f | `FALL_THROUGH`
<a id="insn-00a9fe04"></a> `00a9fe04` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00a9fe08"></a> `00a9fe08` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00a9fe0c"></a> `00a9fe0c` | `09 7d 59 9b` | smulh x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00a9fe10"></a> `00a9fe10` | `38 01 08 8b` | add x24,x9,x8 | `FALL_THROUGH`
<a id="insn-00a9fe14"></a> `00a9fe14` | `1a ff 46 93` | asr x26,x24,#0x6 | `FALL_THROUGH`
<a id="insn-00a9fe18"></a> `00a9fe18` | `c3 fc ff 97` | bl 0x00a9f124 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe1c"></a> `00a9fe1c` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00a9fe20"></a> `00a9fe20` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00a9fe24"></a> `00a9fe24` | `6d 23 00 54` | b.le 0x00aa0290 | `CONDITIONAL_JUMP`
<a id="insn-00a9fe28"></a> `00a9fe28` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9fe2c"></a> `00a9fe2c` | `a1 bd f4 97` | bl 0x007cf4b0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe30"></a> `00a9fe30` | `80 00 00 34` | cbz w0,0x00a9fe40 | `CONDITIONAL_JUMP`
<a id="insn-00a9fe34"></a> `00a9fe34` | `d3 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe38"></a> `00a9fe38` | `31 ac f3 97` | bl 0x0078aefc | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe3c"></a> `00a9fe3c` | `20 20 00 36` | tbz w0,#0x0,0x00aa0240 | `CONDITIONAL_JUMP`
<a id="insn-00a9fe40"></a> `00a9fe40` | `33 01 80 52` | mov w19,#0x9 | `FALL_THROUGH`
<a id="insn-00a9fe44"></a> `00a9fe44` | `0a 01 00 14` | b 0x00aa026c | `UNCONDITIONAL_JUMP`
<a id="insn-00a9fe48"></a> `00a9fe48` | `95 7e 40 93` | sxtw x21,w20 | `FALL_THROUGH`
<a id="insn-00a9fe4c"></a> `00a9fe4c` | `9c 98 9f 52` | mov w28,#0xfcc4 | `FALL_THROUGH`
<a id="insn-00a9fe50"></a> `00a9fe50` | `34 00 80 52` | mov w20,#0x1 | `FALL_THROUGH`
<a id="insn-00a9fe54"></a> `00a9fe54` | `9c 08 a0 72` | movk w28,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9fe58"></a> `00a9fe58` | `04 00 00 14` | b 0x00a9fe68 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9fe5c"></a> `00a9fe5c` | `94 06 00 11` | add w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00a9fe60"></a> `00a9fe60` | `1f 03 14 6b` | cmp w24,w20 | `FALL_THROUGH`
<a id="insn-00a9fe64"></a> `00a9fe64` | `00 f8 ff 54` | b.eq 0x00a9fd64 | `CONDITIONAL_JUMP`
<a id="insn-00a9fe68"></a> `00a9fe68` | `c6 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe6c"></a> `00a9fe6c` | `9f 1e 03 71` | cmp w20,#0xc7 | `FALL_THROUGH`
<a id="insn-00a9fe70"></a> `00a9fe70` | `68 ff ff 54` | b.hi 0x00a9fe5c | `CONDITIONAL_JUMP`
<a id="insn-00a9fe74"></a> `00a9fe74` | `88 1e 00 12` | and w8,w20,#0xff | `FALL_THROUGH`
<a id="insn-00a9fe78"></a> `00a9fe78` | `a9 19 80 52` | mov w9,#0xcd | `FALL_THROUGH`
<a id="insn-00a9fe7c"></a> `00a9fe7c` | `08 7d 09 1b` | mul w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00a9fe80"></a> `00a9fe80` | `16 7d 0b 53` | lsr w22,w8,#0xb | `FALL_THROUGH`
<a id="insn-00a9fe84"></a> `00a9fe84` | `bf fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fe88"></a> `00a9fe88` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00a9fe8c"></a> `00a9fe8c` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00a9fe90"></a> `00a9fe90` | `68 03 08 9b` | madd x8,x27,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9fe94"></a> `00a9fe94` | `a8 22 29 9b` | smaddl x8,w21,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9fe98"></a> `00a9fe98` | `a9 c2 ff b0` | adrp x9,0x2f4000 | `FALL_THROUGH`
<a id="insn-00a9fe9c"></a> `00a9fe9c` | `29 41 23 91` | add x9,x9,#0x8d0 | `FALL_THROUGH`
<a id="insn-00a9fea0"></a> `00a9fea0` | `29 d9 b3 b8` | ldrsw x9,[x9, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00a9fea4"></a> `00a9fea4` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a9fea8"></a> `00a9fea8` | `09 d1 9d 52` | mov w9,#0xee88 | `FALL_THROUGH`
<a id="insn-00a9feac"></a> `00a9feac` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9feb0"></a> `00a9feb0` | `17 69 a9 b8` | ldrsw x23,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9feb4"></a> `00a9feb4` | `b3 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9feb8"></a> `00a9feb8` | `08 0a 80 52` | mov w8,#0x50 | `FALL_THROUGH`
<a id="insn-00a9febc"></a> `00a9febc` | `48 03 28 9b` | smaddl x8,w26,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9fec0"></a> `00a9fec0` | `08 49 36 8b` | add x8,x8,w22, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00a9fec4"></a> `00a9fec4` | `08 69 bc b8` | ldrsw x8,[x8, x28, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9fec8"></a> `00a9fec8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00a9fecc"></a> `00a9fecc` | `19 65 37 9b` | smaddl x25,w8,w23,x25 | `FALL_THROUGH`
<a id="insn-00a9fed0"></a> `00a9fed0` | `e3 ff ff 17` | b 0x00a9fe5c | `UNCONDITIONAL_JUMP`
<a id="insn-00a9fed4"></a> `00a9fed4` | `ab fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fed8"></a> `00a9fed8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a9fedc"></a> `00a9fedc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9fee0"></a> `00a9fee0` | `9c be f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fee4"></a> `00a9fee4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00a9fee8"></a> `00a9fee8` | `7c bf f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9feec"></a> `00a9feec` | `88 ce 4c 91` | add x8,x20,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00a9fef0"></a> `00a9fef0` | `e2 03 00 2a` | mov w2,w0 | `FALL_THROUGH`
<a id="insn-00a9fef4"></a> `00a9fef4` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00a9fef8"></a> `00a9fef8` | `00 21 0a 91` | add x0,x8,#0x288 | `FALL_THROUGH`
<a id="insn-00a9fefc"></a> `00a9fefc` | `33 bb f4 97` | bl 0x007cebc8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ff00"></a> `00a9ff00` | `08 7c 40 93` | sxtw x8,w0 | `FALL_THROUGH`
<a id="insn-00a9ff04"></a> `00a9ff04` | `08 7d 13 9b` | mul x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00a9ff08"></a> `00a9ff08` | `09 7d 57 9b` | smulh x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00a9ff0c"></a> `00a9ff0c` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00a9ff10"></a> `00a9ff10` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00a9ff14"></a> `00a9ff14` | `1c 00 00 14` | b 0x00a9ff84 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ff18"></a> `00a9ff18` | `9a fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ff1c"></a> `00a9ff1c` | `e8 03 15 2a` | mov w8,w21 | `FALL_THROUGH`
<a id="insn-00a9ff20"></a> `00a9ff20` | `a9 c2 ff b0` | adrp x9,0x2f4000 | `FALL_THROUGH`
<a id="insn-00a9ff24"></a> `00a9ff24` | `29 71 23 91` | add x9,x9,#0x8dc | `FALL_THROUGH`
<a id="insn-00a9ff28"></a> `00a9ff28` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00a9ff2c"></a> `00a9ff2c` | `29 d9 b3 b8` | ldrsw x9,[x9, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00a9ff30"></a> `00a9ff30` | `16 09 00 91` | add x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9ff34"></a> `00a9ff34` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00a9ff38"></a> `00a9ff38` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9ff3c"></a> `00a9ff3c` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a9ff40"></a> `00a9ff40` | `09 b5 93 52` | mov w9,#0x9da8 | `FALL_THROUGH`
<a id="insn-00a9ff44"></a> `00a9ff44` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ff48"></a> `00a9ff48` | `13 69 a9 b8` | ldrsw x19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ff4c"></a> `00a9ff4c` | `8d fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ff50"></a> `00a9ff50` | `88 26 9f 52` | mov w8,#0xf934 | `FALL_THROUGH`
<a id="insn-00a9ff54"></a> `00a9ff54` | `e9 0b 00 90` | adrp x9,0xc1b000 | `FALL_THROUGH`
<a id="insn-00a9ff58"></a> `00a9ff58` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ff5c"></a> `00a9ff5c` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ff60"></a> `00a9ff60` | `29 39 44 f9` | ldr x9,[x9, #0x870] | `FALL_THROUGH`
<a id="insn-00a9ff64"></a> `00a9ff64` | `28 79 a8 b8` | ldrsw x8,[x9, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00a9ff68"></a> `00a9ff68` | `a9 00 80 d2` | mov x9,#0x5 | `FALL_THROUGH`
<a id="insn-00a9ff6c"></a> `00a9ff6c` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00a9ff70"></a> `00a9ff70` | `08 25 13 9b` | madd x8,x8,x19,x9 | `FALL_THROUGH`
<a id="insn-00a9ff74"></a> `00a9ff74` | `e9 e7 03 b2` | orr x9,xzr,#0x6666666666666666 | `FALL_THROUGH`
<a id="insn-00a9ff78"></a> `00a9ff78` | `e9 cc 8c f2` | movk x9,#0x6667 | `FALL_THROUGH`
<a id="insn-00a9ff7c"></a> `00a9ff7c` | `08 7d 49 9b` | smulh x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00a9ff80"></a> `00a9ff80` | `09 fd 42 93` | asr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9ff84"></a> `00a9ff84` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00a9ff88"></a> `00a9ff88` | `7e fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ff8c"></a> `00a9ff8c` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00a9ff90"></a> `00a9ff90` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00a9ff94"></a> `00a9ff94` | `df 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ff98"></a> `00a9ff98` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9ff9c"></a> `00a9ff9c` | `79 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ffa0"></a> `00a9ffa0` | `14 01 00 37` | tbnz w20,#0x0,0x00a9ffc0 | `CONDITIONAL_JUMP`
<a id="insn-00a9ffa4"></a> `00a9ffa4` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00a9ffa8"></a> `00a9ffa8` | `09 be 93 52` | mov w9,#0x9df0 | `FALL_THROUGH`
<a id="insn-00a9ffac"></a> `00a9ffac` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9ffb0"></a> `00a9ffb0` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ffb4"></a> `00a9ffb4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ffb8"></a> `00a9ffb8` | `08 01 00 35` | cbnz w8,0x00a9ffd8 | `CONDITIONAL_JUMP`
<a id="insn-00a9ffbc"></a> `00a9ffbc` | `1f 00 00 14` | b 0x00aa0038 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ffc0"></a> `00a9ffc0` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00a9ffc4"></a> `00a9ffc4` | `89 db 9d 52` | mov w9,#0xeedc | `FALL_THROUGH`
<a id="insn-00a9ffc8"></a> `00a9ffc8` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9ffcc"></a> `00a9ffcc` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ffd0"></a> `00a9ffd0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9ffd4"></a> `00a9ffd4` | `08 03 00 34` | cbz w8,0x00aa0034 | `CONDITIONAL_JUMP`
<a id="insn-00a9ffd8"></a> `00a9ffd8` | `6a fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ffdc"></a> `00a9ffdc` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00a9ffe0"></a> `00a9ffe0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00a9ffe4"></a> `00a9ffe4` | `cb 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ffe8"></a> `00a9ffe8` | `00 01 00 37` | tbnz w0,#0x0,0x00aa0008 | `CONDITIONAL_JUMP`
<a id="insn-00a9ffec"></a> `00a9ffec` | `65 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9fff0"></a> `00a9fff0` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00a9fff4"></a> `00a9fff4` | `89 d7 93 52` | mov w9,#0x9ebc | `FALL_THROUGH`
<a id="insn-00a9fff8"></a> `00a9fff8` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00a9fffc"></a> `00a9fffc` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0000"></a> `00aa0000` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa0004"></a> `00aa0004` | `a8 01 00 35` | cbnz w8,0x00aa0038 | `CONDITIONAL_JUMP`
<a id="insn-00aa0008"></a> `00aa0008` | `5e fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa000c"></a> `00aa000c` | `15 3f 8e 52` | mov w21,#0x71f8 | `FALL_THROUGH`
<a id="insn-00aa0010"></a> `00aa0010` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-00aa0014"></a> `00aa0014` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0018"></a> `00aa0018` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa001c"></a> `00aa001c` | `c0 ec fe 97` | bl 0x00a5b31c | `UNCONDITIONAL_CALL`
<a id="insn-00aa0020"></a> `00aa0020` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa0024"></a> `00aa0024` | `57 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0028"></a> `00aa0028` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa002c"></a> `00aa002c` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-00aa0030"></a> `00aa0030` | `76 00 00 14` | b 0x00aa0208 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa0034"></a> `00aa0034` | `53 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0038"></a> `00aa0038` | `52 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa003c"></a> `00aa003c` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00aa0040"></a> `00aa0040` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa0044"></a> `00aa0044` | `b3 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0048"></a> `00aa0048` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa004c"></a> `00aa004c` | `4d fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0050"></a> `00aa0050` | `14 01 00 37` | tbnz w20,#0x0,0x00aa0070 | `CONDITIONAL_JUMP`
<a id="insn-00aa0054"></a> `00aa0054` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa0058"></a> `00aa0058` | `09 be 93 52` | mov w9,#0x9df0 | `FALL_THROUGH`
<a id="insn-00aa005c"></a> `00aa005c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa0060"></a> `00aa0060` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0064"></a> `00aa0064` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa0068"></a> `00aa0068` | `08 01 00 35` | cbnz w8,0x00aa0088 | `CONDITIONAL_JUMP`
<a id="insn-00aa006c"></a> `00aa006c` | `20 00 00 14` | b 0x00aa00ec | `UNCONDITIONAL_JUMP`
<a id="insn-00aa0070"></a> `00aa0070` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00aa0074"></a> `00aa0074` | `89 db 9d 52` | mov w9,#0xeedc | `FALL_THROUGH`
<a id="insn-00aa0078"></a> `00aa0078` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa007c"></a> `00aa007c` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0080"></a> `00aa0080` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa0084"></a> `00aa0084` | `28 03 00 34` | cbz w8,0x00aa00e8 | `CONDITIONAL_JUMP`
<a id="insn-00aa0088"></a> `00aa0088` | `3e fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa008c"></a> `00aa008c` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00aa0090"></a> `00aa0090` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa0094"></a> `00aa0094` | `9f 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0098"></a> `00aa0098` | `a0 02 00 37` | tbnz w0,#0x0,0x00aa00ec | `CONDITIONAL_JUMP`
<a id="insn-00aa009c"></a> `00aa009c` | `39 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00a0"></a> `00aa00a0` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa00a4"></a> `00aa00a4` | `89 d7 93 52` | mov w9,#0x9ebc | `FALL_THROUGH`
<a id="insn-00aa00a8"></a> `00aa00a8` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa00ac"></a> `00aa00ac` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa00b0"></a> `00aa00b0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa00b4"></a> `00aa00b4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa00b8"></a> `00aa00b8` | `a1 01 00 54` | b.ne 0x00aa00ec | `CONDITIONAL_JUMP`
<a id="insn-00aa00bc"></a> `00aa00bc` | `31 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00c0"></a> `00aa00c0` | `15 3f 8e 52` | mov w21,#0x71f8 | `FALL_THROUGH`
<a id="insn-00aa00c4"></a> `00aa00c4` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00aa00c8"></a> `00aa00c8` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa00cc"></a> `00aa00cc` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa00d0"></a> `00aa00d0` | `93 ec fe 97` | bl 0x00a5b31c | `UNCONDITIONAL_CALL`
<a id="insn-00aa00d4"></a> `00aa00d4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa00d8"></a> `00aa00d8` | `2a fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00dc"></a> `00aa00dc` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa00e0"></a> `00aa00e0` | `41 02 80 52` | mov w1,#0x12 | `FALL_THROUGH`
<a id="insn-00aa00e4"></a> `00aa00e4` | `49 00 00 14` | b 0x00aa0208 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa00e8"></a> `00aa00e8` | `26 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00ec"></a> `00aa00ec` | `25 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00f0"></a> `00aa00f0` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00aa00f4"></a> `00aa00f4` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa00f8"></a> `00aa00f8` | `86 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa00fc"></a> `00aa00fc` | `80 02 00 37` | tbnz w0,#0x0,0x00aa014c | `CONDITIONAL_JUMP`
<a id="insn-00aa0100"></a> `00aa0100` | `20 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0104"></a> `00aa0104` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa0108"></a> `00aa0108` | `89 d7 93 52` | mov w9,#0x9ebc | `FALL_THROUGH`
<a id="insn-00aa010c"></a> `00aa010c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa0110"></a> `00aa0110` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0114"></a> `00aa0114` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa0118"></a> `00aa0118` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aa011c"></a> `00aa011c` | `81 01 00 54` | b.ne 0x00aa014c | `CONDITIONAL_JUMP`
<a id="insn-00aa0120"></a> `00aa0120` | `18 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0124"></a> `00aa0124` | `15 3f 8e 52` | mov w21,#0x71f8 | `FALL_THROUGH`
<a id="insn-00aa0128"></a> `00aa0128` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00aa012c"></a> `00aa012c` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0130"></a> `00aa0130` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa0134"></a> `00aa0134` | `7a ec fe 97` | bl 0x00a5b31c | `UNCONDITIONAL_CALL`
<a id="insn-00aa0138"></a> `00aa0138` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa013c"></a> `00aa013c` | `11 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0140"></a> `00aa0140` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa0144"></a> `00aa0144` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00aa0148"></a> `00aa0148` | `30 00 00 14` | b 0x00aa0208 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa014c"></a> `00aa014c` | `0d fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0150"></a> `00aa0150` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00aa0154"></a> `00aa0154` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa0158"></a> `00aa0158` | `6e 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa015c"></a> `00aa015c` | `80 02 00 37` | tbnz w0,#0x0,0x00aa01ac | `CONDITIONAL_JUMP`
<a id="insn-00aa0160"></a> `00aa0160` | `08 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0164"></a> `00aa0164` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa0168"></a> `00aa0168` | `89 d7 93 52` | mov w9,#0x9ebc | `FALL_THROUGH`
<a id="insn-00aa016c"></a> `00aa016c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa0170"></a> `00aa0170` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0174"></a> `00aa0174` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa0178"></a> `00aa0178` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aa017c"></a> `00aa017c` | `81 01 00 54` | b.ne 0x00aa01ac | `CONDITIONAL_JUMP`
<a id="insn-00aa0180"></a> `00aa0180` | `00 fd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0184"></a> `00aa0184` | `15 3f 8e 52` | mov w21,#0x71f8 | `FALL_THROUGH`
<a id="insn-00aa0188"></a> `00aa0188` | `e1 02 80 52` | mov w1,#0x17 | `FALL_THROUGH`
<a id="insn-00aa018c"></a> `00aa018c` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa0190"></a> `00aa0190` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa0194"></a> `00aa0194` | `62 ec fe 97` | bl 0x00a5b31c | `UNCONDITIONAL_CALL`
<a id="insn-00aa0198"></a> `00aa0198` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa019c"></a> `00aa019c` | `f9 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa01a0"></a> `00aa01a0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa01a4"></a> `00aa01a4` | `e1 02 80 52` | mov w1,#0x17 | `FALL_THROUGH`
<a id="insn-00aa01a8"></a> `00aa01a8` | `18 00 00 14` | b 0x00aa0208 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa01ac"></a> `00aa01ac` | `f5 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa01b0"></a> `00aa01b0` | `08 0d 85 52` | mov w8,#0x2868 | `FALL_THROUGH`
<a id="insn-00aa01b4"></a> `00aa01b4` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa01b8"></a> `00aa01b8` | `56 89 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa01bc"></a> `00aa01bc` | `80 09 00 37` | tbnz w0,#0x0,0x00aa02ec | `CONDITIONAL_JUMP`
<a id="insn-00aa01c0"></a> `00aa01c0` | `f0 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa01c4"></a> `00aa01c4` | `88 38 80 52` | mov w8,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aa01c8"></a> `00aa01c8` | `89 d7 93 52` | mov w9,#0x9ebc | `FALL_THROUGH`
<a id="insn-00aa01cc"></a> `00aa01cc` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00aa01d0"></a> `00aa01d0` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa01d4"></a> `00aa01d4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa01d8"></a> `00aa01d8` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aa01dc"></a> `00aa01dc` | `81 08 00 54` | b.ne 0x00aa02ec | `CONDITIONAL_JUMP`
<a id="insn-00aa01e0"></a> `00aa01e0` | `e8 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa01e4"></a> `00aa01e4` | `15 3f 8e 52` | mov w21,#0x71f8 | `FALL_THROUGH`
<a id="insn-00aa01e8"></a> `00aa01e8` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00aa01ec"></a> `00aa01ec` | `35 05 a0 72` | movk w21,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa01f0"></a> `00aa01f0` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa01f4"></a> `00aa01f4` | `4a ec fe 97` | bl 0x00a5b31c | `UNCONDITIONAL_CALL`
<a id="insn-00aa01f8"></a> `00aa01f8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aa01fc"></a> `00aa01fc` | `e1 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0200"></a> `00aa0200` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-00aa0204"></a> `00aa0204` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00aa0208"></a> `00aa0208` | `b0 eb fe 97` | bl 0x00a5b0c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa020c"></a> `00aa020c` | `88 02 00 4b` | sub w8,w20,w0 | `FALL_THROUGH`
<a id="insn-00aa0210"></a> `00aa0210` | `69 e1 9a d2` | mov x9,#0xd70b | `FALL_THROUGH`
<a id="insn-00aa0214"></a> `00aa0214` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00aa0218"></a> `00aa0218` | `69 14 ae f2` | movk x9,#0x70a3, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa021c"></a> `00aa021c` | `a9 47 c1 f2` | movk x9,#0xa3d, LSL #32 | `FALL_THROUGH`
<a id="insn-00aa0220"></a> `00aa0220` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00aa0224"></a> `00aa0224` | `e9 7a f4 f2` | movk x9,#0xa3d7, LSL #48 | `FALL_THROUGH`
<a id="insn-00aa0228"></a> `00aa0228` | `09 7d 49 9b` | smulh x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa022c"></a> `00aa022c` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00aa0230"></a> `00aa0230` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00aa0234"></a> `00aa0234` | `28 fd 48 8b` | add x8,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00aa0238"></a> `00aa0238` | `13 01 13 8b` | add x19,x8,x19 | `FALL_THROUGH`
<a id="insn-00aa023c"></a> `00aa023c` | `2c 00 00 14` | b 0x00aa02ec | `UNCONDITIONAL_JUMP`
<a id="insn-00aa0240"></a> `00aa0240` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa0244"></a> `00aa0244` | `9b bc f4 97` | bl 0x007cf4b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0248"></a> `00aa0248` | `1f 24 00 31` | cmn w0,#0x9 | `FALL_THROUGH`
<a id="insn-00aa024c"></a> `00aa024c` | `e0 00 00 54` | b.eq 0x00aa0268 | `CONDITIONAL_JUMP`
<a id="insn-00aa0250"></a> `00aa0250` | `cc fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0254"></a> `00aa0254` | `4b ab f3 97` | bl 0x0078af80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0258"></a> `00aa0258` | `80 00 00 37` | tbnz w0,#0x0,0x00aa0268 | `CONDITIONAL_JUMP`
<a id="insn-00aa025c"></a> `00aa025c` | `c9 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0260"></a> `00aa0260` | `dc 75 f4 97` | bl 0x007bd9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0264"></a> `00aa0264` | `60 01 00 36` | tbz w0,#0x0,0x00aa0290 | `CONDITIONAL_JUMP`
<a id="insn-00aa0268"></a> `00aa0268` | `13 02 80 52` | mov w19,#0x10 | `FALL_THROUGH`
<a id="insn-00aa026c"></a> `00aa026c` | `c5 fc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa0270"></a> `00aa0270` | `08 ac 82 52` | mov w8,#0x1560 | `FALL_THROUGH`
<a id="insn-00aa0274"></a> `00aa0274` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00aa0278"></a> `00aa0278` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa027c"></a> `00aa027c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aa0280"></a> `00aa0280` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aa0284"></a> `00aa0284` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aa0288"></a> `00aa0288` | `c1 0d ef 97` | bl 0x0066398c | `UNCONDITIONAL_CALL`
<a id="insn-00aa028c"></a> `00aa028c` | `17 00 17 0b` | add w23,w0,w23 | `FALL_THROUGH`
<a id="insn-00aa0290"></a> `00aa0290` | `53 ff 58 8b` | add x19,x26,x24, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00aa0294"></a> `00aa0294` | `ff 06 00 71` | cmp w23,#0x1 | `FALL_THROUGH`
<a id="insn-00aa0298"></a> `00aa0298` | `eb 00 00 54` | b.lt 0x00aa02b4 | `CONDITIONAL_JUMP`
<a id="insn-00aa029c"></a> `00aa029c` | `e8 92 01 11` | add w8,w23,#0x64 | `FALL_THROUGH`
<a id="insn-00aa02a0"></a> `00aa02a0` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00aa02a4"></a> `00aa02a4` | `09 7d 59 9b` | smulh x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aa02a8"></a> `00aa02a8` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00aa02ac"></a> `00aa02ac` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00aa02b0"></a> `00aa02b0` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00aa02b4"></a> `00aa02b4` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aa02b8"></a> `00aa02b8` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00aa02bc"></a> `00aa02bc` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00aa02c0"></a> `00aa02c0` | `c3 08 80 52` | mov w3,#0x46 | `FALL_THROUGH`
<a id="insn-00aa02c4"></a> `00aa02c4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aa02c8"></a> `00aa02c8` | `97 fb ff 97` | bl 0x00a9f124 | `UNCONDITIONAL_CALL`
<a id="insn-00aa02cc"></a> `00aa02cc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa02d0"></a> `00aa02d0` | `eb 00 00 54` | b.lt 0x00aa02ec | `CONDITIONAL_JUMP`
<a id="insn-00aa02d4"></a> `00aa02d4` | `08 90 01 11` | add w8,w0,#0x64 | `FALL_THROUGH`
<a id="insn-00aa02d8"></a> `00aa02d8` | `68 7e 08 9b` | mul x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00aa02dc"></a> `00aa02dc` | `09 7d 59 9b` | smulh x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aa02e0"></a> `00aa02e0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00aa02e4"></a> `00aa02e4` | `09 fd 46 93` | asr x9,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00aa02e8"></a> `00aa02e8` | `33 fd 48 8b` | add x19,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00aa02ec"></a> `00aa02ec` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00aa02f0"></a> `00aa02f0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa02f4"></a> `00aa02f4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa02f8"></a> `00aa02f8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa02fc"></a> `00aa02fc` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa0300"></a> `00aa0300` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa0304"></a> `00aa0304` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa0308"></a> `00aa0308` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00aa030c"></a> `00aa030c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9fbcc`](#insn-00a9fbcc) 範囲 `[['00a9fbcc', '00a9fbd3']]`
  - `FALL_THROUGH` [`00a9fbd0`](#insn-00a9fbd0) → [`00a9fbd4`](#insn-00a9fbd4)
- ブロック [`00a9fbd4`](#insn-00a9fbd4) 範囲 `[['00a9fbd4', '00a9fbdb']]`
  - `FALL_THROUGH` [`00a9fbd8`](#insn-00a9fbd8) → [`00a9fbdc`](#insn-00a9fbdc)
- ブロック [`00a9fbdc`](#insn-00a9fbdc) 範囲 `[['00a9fbdc', '00a9fc27']]`
  - `CONDITIONAL_JUMP` [`00a9fc24`](#insn-00a9fc24) → [`00a9fcf0`](#insn-00a9fcf0)
  - `FALL_THROUGH` [`00a9fc24`](#insn-00a9fc24) → [`00a9fc28`](#insn-00a9fc28)
- ブロック [`00a9fc28`](#insn-00a9fc28) 範囲 `[['00a9fc28', '00a9fc3f']]`
  - `CONDITIONAL_JUMP` [`00a9fc3c`](#insn-00a9fc3c) → [`00a9fc54`](#insn-00a9fc54)
  - `FALL_THROUGH` [`00a9fc3c`](#insn-00a9fc3c) → [`00a9fc40`](#insn-00a9fc40)
- ブロック [`00a9fc40`](#insn-00a9fc40) 範囲 `[['00a9fc40', '00a9fc53']]`
  - `CONDITIONAL_JUMP` [`00a9fc50`](#insn-00a9fc50) → [`00a9ff18`](#insn-00a9ff18)
  - `FALL_THROUGH` [`00a9fc50`](#insn-00a9fc50) → [`00a9fc54`](#insn-00a9fc54)
- ブロック [`00a9fc54`](#insn-00a9fc54) 範囲 `[['00a9fc54', '00a9fce3']]`
  - `CONDITIONAL_JUMP` [`00a9fce0`](#insn-00a9fce0) → [`00a9ff88`](#insn-00a9ff88)
  - `FALL_THROUGH` [`00a9fce0`](#insn-00a9fce0) → [`00a9fce4`](#insn-00a9fce4)
- ブロック [`00a9fce4`](#insn-00a9fce4) 範囲 `[['00a9fce4', '00a9fce7']]`
  - `CONDITIONAL_JUMP` [`00a9fce4`](#insn-00a9fce4) → [`00a9fed4`](#insn-00a9fed4)
  - `FALL_THROUGH` [`00a9fce4`](#insn-00a9fce4) → [`00a9fce8`](#insn-00a9fce8)
- ブロック [`00a9fce8`](#insn-00a9fce8) 範囲 `[['00a9fce8', '00a9fcef']]`
  - `UNCONDITIONAL_JUMP` [`00a9fcec`](#insn-00a9fcec) → [`00a9ff04`](#insn-00a9ff04)
- ブロック [`00a9fcf0`](#insn-00a9fcf0) 範囲 `[['00a9fcf0', '00a9fd07']]`
  - `CONDITIONAL_JUMP` [`00a9fd04`](#insn-00a9fd04) → [`00a9fd9c`](#insn-00a9fd9c)
  - `FALL_THROUGH` [`00a9fd04`](#insn-00a9fd04) → [`00a9fd08`](#insn-00a9fd08)
- ブロック [`00a9fd08`](#insn-00a9fd08) 範囲 `[['00a9fd08', '00a9fd63']]`
  - `CONDITIONAL_JUMP` [`00a9fd60`](#insn-00a9fd60) → [`00a9fe48`](#insn-00a9fe48)
  - `FALL_THROUGH` [`00a9fd60`](#insn-00a9fd60) → [`00a9fd64`](#insn-00a9fd64)
- ブロック [`00a9fd64`](#insn-00a9fd64) 範囲 `[['00a9fd64', '00a9fd97']]`
  - `CONDITIONAL_JUMP` [`00a9fd94`](#insn-00a9fd94) → [`00a9fda4`](#insn-00a9fda4)
  - `FALL_THROUGH` [`00a9fd94`](#insn-00a9fd94) → [`00a9fd98`](#insn-00a9fd98)
- ブロック [`00a9fd98`](#insn-00a9fd98) 範囲 `[['00a9fd98', '00a9fd9b']]`
  - `UNCONDITIONAL_JUMP` [`00a9fd98`](#insn-00a9fd98) → [`00aa02ec`](#insn-00aa02ec)
- ブロック [`00a9fd9c`](#insn-00a9fd9c) 範囲 `[['00a9fd9c', '00a9fda3']]`
  - `CONDITIONAL_JUMP` [`00a9fda0`](#insn-00a9fda0) → [`00aa02ec`](#insn-00aa02ec)
  - `FALL_THROUGH` [`00a9fda0`](#insn-00a9fda0) → [`00a9fda4`](#insn-00a9fda4)
- ブロック [`00a9fda4`](#insn-00a9fda4) 範囲 `[['00a9fda4', '00a9fe27']]`
  - `CONDITIONAL_JUMP` [`00a9fe24`](#insn-00a9fe24) → [`00aa0290`](#insn-00aa0290)
  - `FALL_THROUGH` [`00a9fe24`](#insn-00a9fe24) → [`00a9fe28`](#insn-00a9fe28)
- ブロック [`00a9fe28`](#insn-00a9fe28) 範囲 `[['00a9fe28', '00a9fe33']]`
  - `CONDITIONAL_JUMP` [`00a9fe30`](#insn-00a9fe30) → [`00a9fe40`](#insn-00a9fe40)
  - `FALL_THROUGH` [`00a9fe30`](#insn-00a9fe30) → [`00a9fe34`](#insn-00a9fe34)
- ブロック [`00a9fe34`](#insn-00a9fe34) 範囲 `[['00a9fe34', '00a9fe3f']]`
  - `CONDITIONAL_JUMP` [`00a9fe3c`](#insn-00a9fe3c) → [`00aa0240`](#insn-00aa0240)
  - `FALL_THROUGH` [`00a9fe3c`](#insn-00a9fe3c) → [`00a9fe40`](#insn-00a9fe40)
- ブロック [`00a9fe40`](#insn-00a9fe40) 範囲 `[['00a9fe40', '00a9fe47']]`
  - `UNCONDITIONAL_JUMP` [`00a9fe44`](#insn-00a9fe44) → [`00aa026c`](#insn-00aa026c)
- ブロック [`00a9fe48`](#insn-00a9fe48) 範囲 `[['00a9fe48', '00a9fe4b']]`
  - `FALL_THROUGH` [`00a9fe48`](#insn-00a9fe48) → [`00a9fe4c`](#insn-00a9fe4c)
- ブロック [`00a9fe4c`](#insn-00a9fe4c) 範囲 `[['00a9fe4c', '00a9fe5b']]`
  - `UNCONDITIONAL_JUMP` [`00a9fe58`](#insn-00a9fe58) → [`00a9fe68`](#insn-00a9fe68)
- ブロック [`00a9fe5c`](#insn-00a9fe5c) 範囲 `[['00a9fe5c', '00a9fe67']]`
  - `CONDITIONAL_JUMP` [`00a9fe64`](#insn-00a9fe64) → [`00a9fd64`](#insn-00a9fd64)
  - `FALL_THROUGH` [`00a9fe64`](#insn-00a9fe64) → [`00a9fe68`](#insn-00a9fe68)
- ブロック [`00a9fe68`](#insn-00a9fe68) 範囲 `[['00a9fe68', '00a9fe73']]`
  - `CONDITIONAL_JUMP` [`00a9fe70`](#insn-00a9fe70) → [`00a9fe5c`](#insn-00a9fe5c)
  - `FALL_THROUGH` [`00a9fe70`](#insn-00a9fe70) → [`00a9fe74`](#insn-00a9fe74)
- ブロック [`00a9fe74`](#insn-00a9fe74) 範囲 `[['00a9fe74', '00a9feb3']]`
  - `FALL_THROUGH` [`00a9feb0`](#insn-00a9feb0) → [`00a9feb4`](#insn-00a9feb4)
- ブロック [`00a9feb4`](#insn-00a9feb4) 範囲 `[['00a9feb4', '00a9fec3']]`
  - `FALL_THROUGH` [`00a9fec0`](#insn-00a9fec0) → [`00a9fec4`](#insn-00a9fec4)
- ブロック [`00a9fec4`](#insn-00a9fec4) 範囲 `[['00a9fec4', '00a9fed3']]`
  - `UNCONDITIONAL_JUMP` [`00a9fed0`](#insn-00a9fed0) → [`00a9fe5c`](#insn-00a9fe5c)
- ブロック [`00a9fed4`](#insn-00a9fed4) 範囲 `[['00a9fed4', '00a9ff03']]`
  - `FALL_THROUGH` [`00a9ff00`](#insn-00a9ff00) → [`00a9ff04`](#insn-00a9ff04)
- ブロック [`00a9ff04`](#insn-00a9ff04) 範囲 `[['00a9ff04', '00a9ff17']]`
  - `UNCONDITIONAL_JUMP` [`00a9ff14`](#insn-00a9ff14) → [`00a9ff84`](#insn-00a9ff84)
- ブロック [`00a9ff18`](#insn-00a9ff18) 範囲 `[['00a9ff18', '00a9ff63']]`
  - `FALL_THROUGH` [`00a9ff60`](#insn-00a9ff60) → [`00a9ff64`](#insn-00a9ff64)
- ブロック [`00a9ff64`](#insn-00a9ff64) 範囲 `[['00a9ff64', '00a9ff73']]`
  - `FALL_THROUGH` [`00a9ff70`](#insn-00a9ff70) → [`00a9ff74`](#insn-00a9ff74)
- ブロック [`00a9ff74`](#insn-00a9ff74) 範囲 `[['00a9ff74', '00a9ff83']]`
  - `FALL_THROUGH` [`00a9ff80`](#insn-00a9ff80) → [`00a9ff84`](#insn-00a9ff84)
- ブロック [`00a9ff84`](#insn-00a9ff84) 範囲 `[['00a9ff84', '00a9ff87']]`
  - `FALL_THROUGH` [`00a9ff84`](#insn-00a9ff84) → [`00a9ff88`](#insn-00a9ff88)
- ブロック [`00a9ff88`](#insn-00a9ff88) 範囲 `[['00a9ff88', '00a9ffa3']]`
  - `CONDITIONAL_JUMP` [`00a9ffa0`](#insn-00a9ffa0) → [`00a9ffc0`](#insn-00a9ffc0)
  - `FALL_THROUGH` [`00a9ffa0`](#insn-00a9ffa0) → [`00a9ffa4`](#insn-00a9ffa4)
- ブロック [`00a9ffa4`](#insn-00a9ffa4) 範囲 `[['00a9ffa4', '00a9ffa7']]`
  - `FALL_THROUGH` [`00a9ffa4`](#insn-00a9ffa4) → [`00a9ffa8`](#insn-00a9ffa8)
- ブロック [`00a9ffa8`](#insn-00a9ffa8) 範囲 `[['00a9ffa8', '00a9ffbb']]`
  - `CONDITIONAL_JUMP` [`00a9ffb8`](#insn-00a9ffb8) → [`00a9ffd8`](#insn-00a9ffd8)
  - `FALL_THROUGH` [`00a9ffb8`](#insn-00a9ffb8) → [`00a9ffbc`](#insn-00a9ffbc)
- ブロック [`00a9ffbc`](#insn-00a9ffbc) 範囲 `[['00a9ffbc', '00a9ffbf']]`
  - `UNCONDITIONAL_JUMP` [`00a9ffbc`](#insn-00a9ffbc) → [`00aa0038`](#insn-00aa0038)
- ブロック [`00a9ffc0`](#insn-00a9ffc0) 範囲 `[['00a9ffc0', '00a9ffc7']]`
  - `FALL_THROUGH` [`00a9ffc4`](#insn-00a9ffc4) → [`00a9ffc8`](#insn-00a9ffc8)
- ブロック [`00a9ffc8`](#insn-00a9ffc8) 範囲 `[['00a9ffc8', '00a9ffd7']]`
  - `CONDITIONAL_JUMP` [`00a9ffd4`](#insn-00a9ffd4) → [`00aa0034`](#insn-00aa0034)
  - `FALL_THROUGH` [`00a9ffd4`](#insn-00a9ffd4) → [`00a9ffd8`](#insn-00a9ffd8)
- ブロック [`00a9ffd8`](#insn-00a9ffd8) 範囲 `[['00a9ffd8', '00a9ffeb']]`
  - `CONDITIONAL_JUMP` [`00a9ffe8`](#insn-00a9ffe8) → [`00aa0008`](#insn-00aa0008)
  - `FALL_THROUGH` [`00a9ffe8`](#insn-00a9ffe8) → [`00a9ffec`](#insn-00a9ffec)
- ブロック [`00a9ffec`](#insn-00a9ffec) 範囲 `[['00a9ffec', '00aa0007']]`
  - `CONDITIONAL_JUMP` [`00aa0004`](#insn-00aa0004) → [`00aa0038`](#insn-00aa0038)
  - `FALL_THROUGH` [`00aa0004`](#insn-00aa0004) → [`00aa0008`](#insn-00aa0008)
- ブロック [`00aa0008`](#insn-00aa0008) 範囲 `[['00aa0008', '00aa0017']]`
  - `FALL_THROUGH` [`00aa0014`](#insn-00aa0014) → [`00aa0018`](#insn-00aa0018)
- ブロック [`00aa0018`](#insn-00aa0018) 範囲 `[['00aa0018', '00aa001f']]`
  - `FALL_THROUGH` [`00aa001c`](#insn-00aa001c) → [`00aa0020`](#insn-00aa0020)
- ブロック [`00aa0020`](#insn-00aa0020) 範囲 `[['00aa0020', '00aa0033']]`
  - `UNCONDITIONAL_JUMP` [`00aa0030`](#insn-00aa0030) → [`00aa0208`](#insn-00aa0208)
- ブロック [`00aa0034`](#insn-00aa0034) 範囲 `[['00aa0034', '00aa0037']]`
  - `FALL_THROUGH` [`00aa0034`](#insn-00aa0034) → [`00aa0038`](#insn-00aa0038)
- ブロック [`00aa0038`](#insn-00aa0038) 範囲 `[['00aa0038', '00aa0053']]`
  - `CONDITIONAL_JUMP` [`00aa0050`](#insn-00aa0050) → [`00aa0070`](#insn-00aa0070)
  - `FALL_THROUGH` [`00aa0050`](#insn-00aa0050) → [`00aa0054`](#insn-00aa0054)
- ブロック [`00aa0054`](#insn-00aa0054) 範囲 `[['00aa0054', '00aa006b']]`
  - `CONDITIONAL_JUMP` [`00aa0068`](#insn-00aa0068) → [`00aa0088`](#insn-00aa0088)
  - `FALL_THROUGH` [`00aa0068`](#insn-00aa0068) → [`00aa006c`](#insn-00aa006c)
- ブロック [`00aa006c`](#insn-00aa006c) 範囲 `[['00aa006c', '00aa006f']]`
  - `UNCONDITIONAL_JUMP` [`00aa006c`](#insn-00aa006c) → [`00aa00ec`](#insn-00aa00ec)
- ブロック [`00aa0070`](#insn-00aa0070) 範囲 `[['00aa0070', '00aa0087']]`
  - `CONDITIONAL_JUMP` [`00aa0084`](#insn-00aa0084) → [`00aa00e8`](#insn-00aa00e8)
  - `FALL_THROUGH` [`00aa0084`](#insn-00aa0084) → [`00aa0088`](#insn-00aa0088)
- ブロック [`00aa0088`](#insn-00aa0088) 範囲 `[['00aa0088', '00aa009b']]`
  - `CONDITIONAL_JUMP` [`00aa0098`](#insn-00aa0098) → [`00aa00ec`](#insn-00aa00ec)
  - `FALL_THROUGH` [`00aa0098`](#insn-00aa0098) → [`00aa009c`](#insn-00aa009c)
- ブロック [`00aa009c`](#insn-00aa009c) 範囲 `[['00aa009c', '00aa00bb']]`
  - `CONDITIONAL_JUMP` [`00aa00b8`](#insn-00aa00b8) → [`00aa00ec`](#insn-00aa00ec)
  - `FALL_THROUGH` [`00aa00b8`](#insn-00aa00b8) → [`00aa00bc`](#insn-00aa00bc)
- ブロック [`00aa00bc`](#insn-00aa00bc) 範囲 `[['00aa00bc', '00aa00e7']]`
  - `UNCONDITIONAL_JUMP` [`00aa00e4`](#insn-00aa00e4) → [`00aa0208`](#insn-00aa0208)
- ブロック [`00aa00e8`](#insn-00aa00e8) 範囲 `[['00aa00e8', '00aa00eb']]`
  - `FALL_THROUGH` [`00aa00e8`](#insn-00aa00e8) → [`00aa00ec`](#insn-00aa00ec)
- ブロック [`00aa00ec`](#insn-00aa00ec) 範囲 `[['00aa00ec', '00aa00ff']]`
  - `CONDITIONAL_JUMP` [`00aa00fc`](#insn-00aa00fc) → [`00aa014c`](#insn-00aa014c)
  - `FALL_THROUGH` [`00aa00fc`](#insn-00aa00fc) → [`00aa0100`](#insn-00aa0100)
- ブロック [`00aa0100`](#insn-00aa0100) 範囲 `[['00aa0100', '00aa0107']]`
  - `FALL_THROUGH` [`00aa0104`](#insn-00aa0104) → [`00aa0108`](#insn-00aa0108)
- ブロック [`00aa0108`](#insn-00aa0108) 範囲 `[['00aa0108', '00aa0113']]`
  - `FALL_THROUGH` [`00aa0110`](#insn-00aa0110) → [`00aa0114`](#insn-00aa0114)
- ブロック [`00aa0114`](#insn-00aa0114) 範囲 `[['00aa0114', '00aa011f']]`
  - `CONDITIONAL_JUMP` [`00aa011c`](#insn-00aa011c) → [`00aa014c`](#insn-00aa014c)
  - `FALL_THROUGH` [`00aa011c`](#insn-00aa011c) → [`00aa0120`](#insn-00aa0120)
- ブロック [`00aa0120`](#insn-00aa0120) 範囲 `[['00aa0120', '00aa014b']]`
  - `UNCONDITIONAL_JUMP` [`00aa0148`](#insn-00aa0148) → [`00aa0208`](#insn-00aa0208)
- ブロック [`00aa014c`](#insn-00aa014c) 範囲 `[['00aa014c', '00aa015f']]`
  - `CONDITIONAL_JUMP` [`00aa015c`](#insn-00aa015c) → [`00aa01ac`](#insn-00aa01ac)
  - `FALL_THROUGH` [`00aa015c`](#insn-00aa015c) → [`00aa0160`](#insn-00aa0160)
- ブロック [`00aa0160`](#insn-00aa0160) 範囲 `[['00aa0160', '00aa017f']]`
  - `CONDITIONAL_JUMP` [`00aa017c`](#insn-00aa017c) → [`00aa01ac`](#insn-00aa01ac)
  - `FALL_THROUGH` [`00aa017c`](#insn-00aa017c) → [`00aa0180`](#insn-00aa0180)
- ブロック [`00aa0180`](#insn-00aa0180) 範囲 `[['00aa0180', '00aa019b']]`
  - `FALL_THROUGH` [`00aa0198`](#insn-00aa0198) → [`00aa019c`](#insn-00aa019c)
- ブロック [`00aa019c`](#insn-00aa019c) 範囲 `[['00aa019c', '00aa01ab']]`
  - `UNCONDITIONAL_JUMP` [`00aa01a8`](#insn-00aa01a8) → [`00aa0208`](#insn-00aa0208)
- ブロック [`00aa01ac`](#insn-00aa01ac) 範囲 `[['00aa01ac', '00aa01bf']]`
  - `CONDITIONAL_JUMP` [`00aa01bc`](#insn-00aa01bc) → [`00aa02ec`](#insn-00aa02ec)
  - `FALL_THROUGH` [`00aa01bc`](#insn-00aa01bc) → [`00aa01c0`](#insn-00aa01c0)
- ブロック [`00aa01c0`](#insn-00aa01c0) 範囲 `[['00aa01c0', '00aa01df']]`
  - `CONDITIONAL_JUMP` [`00aa01dc`](#insn-00aa01dc) → [`00aa02ec`](#insn-00aa02ec)
  - `FALL_THROUGH` [`00aa01dc`](#insn-00aa01dc) → [`00aa01e0`](#insn-00aa01e0)
- ブロック [`00aa01e0`](#insn-00aa01e0) 範囲 `[['00aa01e0', '00aa0207']]`
  - `FALL_THROUGH` [`00aa0204`](#insn-00aa0204) → [`00aa0208`](#insn-00aa0208)
- ブロック [`00aa0208`](#insn-00aa0208) 範囲 `[['00aa0208', '00aa0223']]`
  - `FALL_THROUGH` [`00aa0220`](#insn-00aa0220) → [`00aa0224`](#insn-00aa0224)
- ブロック [`00aa0224`](#insn-00aa0224) 範囲 `[['00aa0224', '00aa023f']]`
  - `UNCONDITIONAL_JUMP` [`00aa023c`](#insn-00aa023c) → [`00aa02ec`](#insn-00aa02ec)
- ブロック [`00aa0240`](#insn-00aa0240) 範囲 `[['00aa0240', '00aa024f']]`
  - `CONDITIONAL_JUMP` [`00aa024c`](#insn-00aa024c) → [`00aa0268`](#insn-00aa0268)
  - `FALL_THROUGH` [`00aa024c`](#insn-00aa024c) → [`00aa0250`](#insn-00aa0250)
- ブロック [`00aa0250`](#insn-00aa0250) 範囲 `[['00aa0250', '00aa025b']]`
  - `CONDITIONAL_JUMP` [`00aa0258`](#insn-00aa0258) → [`00aa0268`](#insn-00aa0268)
  - `FALL_THROUGH` [`00aa0258`](#insn-00aa0258) → [`00aa025c`](#insn-00aa025c)
- ブロック [`00aa025c`](#insn-00aa025c) 範囲 `[['00aa025c', '00aa0267']]`
  - `CONDITIONAL_JUMP` [`00aa0264`](#insn-00aa0264) → [`00aa0290`](#insn-00aa0290)
  - `FALL_THROUGH` [`00aa0264`](#insn-00aa0264) → [`00aa0268`](#insn-00aa0268)
- ブロック [`00aa0268`](#insn-00aa0268) 範囲 `[['00aa0268', '00aa026b']]`
  - `FALL_THROUGH` [`00aa0268`](#insn-00aa0268) → [`00aa026c`](#insn-00aa026c)
- ブロック [`00aa026c`](#insn-00aa026c) 範囲 `[['00aa026c', '00aa027b']]`
  - `FALL_THROUGH` [`00aa0278`](#insn-00aa0278) → [`00aa027c`](#insn-00aa027c)
- ブロック [`00aa027c`](#insn-00aa027c) 範囲 `[['00aa027c', '00aa028f']]`
  - `FALL_THROUGH` [`00aa028c`](#insn-00aa028c) → [`00aa0290`](#insn-00aa0290)
- ブロック [`00aa0290`](#insn-00aa0290) 範囲 `[['00aa0290', '00aa029b']]`
  - `CONDITIONAL_JUMP` [`00aa0298`](#insn-00aa0298) → [`00aa02b4`](#insn-00aa02b4)
  - `FALL_THROUGH` [`00aa0298`](#insn-00aa0298) → [`00aa029c`](#insn-00aa029c)
- ブロック [`00aa029c`](#insn-00aa029c) 範囲 `[['00aa029c', '00aa02a3']]`
  - `FALL_THROUGH` [`00aa02a0`](#insn-00aa02a0) → [`00aa02a4`](#insn-00aa02a4)
- ブロック [`00aa02a4`](#insn-00aa02a4) 範囲 `[['00aa02a4', '00aa02b3']]`
  - `FALL_THROUGH` [`00aa02b0`](#insn-00aa02b0) → [`00aa02b4`](#insn-00aa02b4)
- ブロック [`00aa02b4`](#insn-00aa02b4) 範囲 `[['00aa02b4', '00aa02d3']]`
  - `CONDITIONAL_JUMP` [`00aa02d0`](#insn-00aa02d0) → [`00aa02ec`](#insn-00aa02ec)
  - `FALL_THROUGH` [`00aa02d0`](#insn-00aa02d0) → [`00aa02d4`](#insn-00aa02d4)
- ブロック [`00aa02d4`](#insn-00aa02d4) 範囲 `[['00aa02d4', '00aa02eb']]`
  - `FALL_THROUGH` [`00aa02e8`](#insn-00aa02e8) → [`00aa02ec`](#insn-00aa02ec)
- ブロック [`00aa02ec`](#insn-00aa02ec) 範囲 `[['00aa02ec', '00aa02ff']]`
  - `FALL_THROUGH` [`00aa02fc`](#insn-00aa02fc) → [`00aa0300`](#insn-00aa0300)
- ブロック [`00aa0300`](#insn-00aa0300) 範囲 `[['00aa0300', '00aa030f']]`

## 命令位置別の参照

- [`00a9fbd0`](#insn-00a9fbd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fbd4`](#insn-00a9fbd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fbd8`](#insn-00a9fbd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fbdc`](#insn-00a9fbdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fbe0`](#insn-00a9fbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fbe4`](#insn-00a9fbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc0c`](#insn-00a9fc0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc20`](#insn-00a9fc20) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc24`](#insn-00a9fc24) → [`00a9fcf0`](#insn-00a9fcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc28`](#insn-00a9fc28) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc34`](#insn-00a9fc34) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a9fc3c`](#insn-00a9fc3c) → [`00a9fc54`](#insn-00a9fc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc40`](#insn-00a9fc40) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc4c`](#insn-00a9fc4c) → `00334048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a9fc50`](#insn-00a9fc50) → [`00a9ff18`](#insn-00a9ff18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc54`](#insn-00a9fc54) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc60`](#insn-00a9fc60) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a9fc64`](#insn-00a9fc64) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc74`](#insn-00a9fc74) → `002f48dc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fc90`](#insn-00a9fc90) → `00239da8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00a9fc94`](#insn-00a9fc94) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fcb0`](#insn-00a9fcb0) → [`00a06cfc`](../00a06/00a06cfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a06cfc` · 推定シンボル `None` · 推定型 `None`
- [`00a9fce0`](#insn-00a9fce0) → [`00a9ff88`](#insn-00a9ff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fce4`](#insn-00a9fce4) → [`00a9fed4`](#insn-00a9fed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fcec`](#insn-00a9fcec) → [`00a9ff04`](#insn-00a9ff04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd04`](#insn-00a9fd04) → [`00a9fd9c`](#insn-00a9fd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd0c`](#insn-00a9fd0c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd14`](#insn-00a9fd14) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd24`](#insn-00a9fd24) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd38`](#insn-00a9fd38) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd44`](#insn-00a9fd44) → `002f48d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd60`](#insn-00a9fd60) → [`00a9fe48`](#insn-00a9fe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd6c`](#insn-00a9fd6c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd74`](#insn-00a9fd74) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd84`](#insn-00a9fd84) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd94`](#insn-00a9fd94) → [`00a9fda4`](#insn-00a9fda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fd98`](#insn-00a9fd98) → [`00aa02ec`](#insn-00aa02ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fda0`](#insn-00a9fda0) → [`00aa02ec`](#insn-00aa02ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fda4`](#insn-00a9fda4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fdb4`](#insn-00a9fdb4) → [`00a5b0c8`](../00a5b/00a5b0c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b0c8` · 推定シンボル `None` · 推定型 `None`
- [`00a9fdd4`](#insn-00a9fdd4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fde8`](#insn-00a9fde8) → [`0088f9e4`](../0088f/0088f9e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0088f9e4` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe18`](#insn-00a9fe18) → [`00a9f124`](00a9f124.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a9f124` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe24`](#insn-00a9fe24) → [`00aa0290`](#insn-00aa0290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe2c`](#insn-00a9fe2c) → [`007cf4b0`](../007cf/007cf4b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf4b0` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe30`](#insn-00a9fe30) → [`00a9fe40`](#insn-00a9fe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe34`](#insn-00a9fe34) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe38`](#insn-00a9fe38) → [`0078aefc`](../0078a/0078aefc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078aefc` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe3c`](#insn-00a9fe3c) → [`00aa0240`](#insn-00aa0240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe44`](#insn-00a9fe44) → [`00aa026c`](#insn-00aa026c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe58`](#insn-00a9fe58) → [`00a9fe68`](#insn-00a9fe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe64`](#insn-00a9fe64) → [`00a9fd64`](#insn-00a9fd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe68`](#insn-00a9fe68) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe70`](#insn-00a9fe70) → [`00a9fe5c`](#insn-00a9fe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fe84`](#insn-00a9fe84) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fea0`](#insn-00a9fea0) → `002f48d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9feb4`](#insn-00a9feb4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fed0`](#insn-00a9fed0) → [`00a9fe5c`](#insn-00a9fe5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9fed4`](#insn-00a9fed4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9fee0`](#insn-00a9fee0) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00a9fee8`](#insn-00a9fee8) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00a9fefc`](#insn-00a9fefc) → [`007cebc8`](../007ce/007cebc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cebc8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff14`](#insn-00a9ff14) → [`00a9ff84`](#insn-00a9ff84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff18`](#insn-00a9ff18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff2c`](#insn-00a9ff2c) → `002f48dc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff48`](#insn-00a9ff48) → `00239da8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00a9ff4c`](#insn-00a9ff4c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff5c`](#insn-00a9ff5c) → `0032f934`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00a9ff60`](#insn-00a9ff60) → `00c1b870`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a9ff64`](#insn-00a9ff64) → `00c24654`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff88`](#insn-00a9ff88) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff94`](#insn-00a9ff94) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9ff9c`](#insn-00a9ff9c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffa0`](#insn-00a9ffa0) → [`00a9ffc0`](#insn-00a9ffc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffb4`](#insn-00a9ffb4) → `00239df0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00a9ffb8`](#insn-00a9ffb8) → [`00a9ffd8`](#insn-00a9ffd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffbc`](#insn-00a9ffbc) → [`00aa0038`](#insn-00aa0038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffd4`](#insn-00a9ffd4) → [`00aa0034`](#insn-00aa0034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffd8`](#insn-00a9ffd8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffe4`](#insn-00a9ffe4) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffe8`](#insn-00a9ffe8) → [`00aa0008`](#insn-00aa0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ffec`](#insn-00a9ffec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0000`](#insn-00aa0000) → `00239ebc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa0004`](#insn-00aa0004) → [`00aa0038`](#insn-00aa0038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0008`](#insn-00aa0008) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa001c`](#insn-00aa001c) → [`00a5b31c`](../00a5b/00a5b31c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b31c` · 推定シンボル `None` · 推定型 `None`
- [`00aa0024`](#insn-00aa0024) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0030`](#insn-00aa0030) → [`00aa0208`](#insn-00aa0208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0034`](#insn-00aa0034) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0038`](#insn-00aa0038) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0044`](#insn-00aa0044) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa004c`](#insn-00aa004c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0050`](#insn-00aa0050) → [`00aa0070`](#insn-00aa0070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0064`](#insn-00aa0064) → `00239df0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa0068`](#insn-00aa0068) → [`00aa0088`](#insn-00aa0088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa006c`](#insn-00aa006c) → [`00aa00ec`](#insn-00aa00ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0084`](#insn-00aa0084) → [`00aa00e8`](#insn-00aa00e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0088`](#insn-00aa0088) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0094`](#insn-00aa0094) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa0098`](#insn-00aa0098) → [`00aa00ec`](#insn-00aa00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa009c`](#insn-00aa009c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa00b0`](#insn-00aa00b0) → `00239ebc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa00b8`](#insn-00aa00b8) → [`00aa00ec`](#insn-00aa00ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa00bc`](#insn-00aa00bc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa00d0`](#insn-00aa00d0) → [`00a5b31c`](../00a5b/00a5b31c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b31c` · 推定シンボル `None` · 推定型 `None`
- [`00aa00d8`](#insn-00aa00d8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa00e4`](#insn-00aa00e4) → [`00aa0208`](#insn-00aa0208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa00e8`](#insn-00aa00e8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa00ec`](#insn-00aa00ec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa00f8`](#insn-00aa00f8) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa00fc`](#insn-00aa00fc) → [`00aa014c`](#insn-00aa014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0100`](#insn-00aa0100) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0114`](#insn-00aa0114) → `00239ebc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa011c`](#insn-00aa011c) → [`00aa014c`](#insn-00aa014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0120`](#insn-00aa0120) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0134`](#insn-00aa0134) → [`00a5b31c`](../00a5b/00a5b31c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b31c` · 推定シンボル `None` · 推定型 `None`
- [`00aa013c`](#insn-00aa013c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0148`](#insn-00aa0148) → [`00aa0208`](#insn-00aa0208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa014c`](#insn-00aa014c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0158`](#insn-00aa0158) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa015c`](#insn-00aa015c) → [`00aa01ac`](#insn-00aa01ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0160`](#insn-00aa0160) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0174`](#insn-00aa0174) → `00239ebc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa017c`](#insn-00aa017c) → [`00aa01ac`](#insn-00aa01ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0180`](#insn-00aa0180) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0194`](#insn-00aa0194) → [`00a5b31c`](../00a5b/00a5b31c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b31c` · 推定シンボル `None` · 推定型 `None`
- [`00aa019c`](#insn-00aa019c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa01a8`](#insn-00aa01a8) → [`00aa0208`](#insn-00aa0208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa01ac`](#insn-00aa01ac) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa01b8`](#insn-00aa01b8) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa01bc`](#insn-00aa01bc) → [`00aa02ec`](#insn-00aa02ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa01c0`](#insn-00aa01c0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa01d4`](#insn-00aa01d4) → `00239ebc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1792]`
- [`00aa01dc`](#insn-00aa01dc) → [`00aa02ec`](#insn-00aa02ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa01e0`](#insn-00aa01e0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa01f4`](#insn-00aa01f4) → [`00a5b31c`](../00a5b/00a5b31c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b31c` · 推定シンボル `None` · 推定型 `None`
- [`00aa01fc`](#insn-00aa01fc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0208`](#insn-00aa0208) → [`00a5b0c8`](../00a5b/00a5b0c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a5b0c8` · 推定シンボル `None` · 推定型 `None`
- [`00aa023c`](#insn-00aa023c) → [`00aa02ec`](#insn-00aa02ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0244`](#insn-00aa0244) → [`007cf4b0`](../007cf/007cf4b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf4b0` · 推定シンボル `None` · 推定型 `None`
- [`00aa024c`](#insn-00aa024c) → [`00aa0268`](#insn-00aa0268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0250`](#insn-00aa0250) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0254`](#insn-00aa0254) → [`0078af80`](../0078a/0078af80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078af80` · 推定シンボル `None` · 推定型 `None`
- [`00aa0258`](#insn-00aa0258) → [`00aa0268`](#insn-00aa0268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa025c`](#insn-00aa025c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0260`](#insn-00aa0260) → [`007bd9d0`](../007bd/007bd9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bd9d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa0264`](#insn-00aa0264) → [`00aa0290`](#insn-00aa0290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa026c`](#insn-00aa026c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa0288`](#insn-00aa0288) → [`0066398c`](../00663/0066398c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066398c` · 推定シンボル `None` · 推定型 `None`
- [`00aa0298`](#insn-00aa0298) → [`00aa02b4`](#insn-00aa02b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa02c8`](#insn-00aa02c8) → [`00a9f124`](00a9f124.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a9f124` · 推定シンボル `None` · 推定型 `None`
- [`00aa02d0`](#insn-00aa02d0) → [`00aa02ec`](#insn-00aa02ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa02f0`](#insn-00aa02f0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa02f4`](#insn-00aa02f4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa02f8`](#insn-00aa02f8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa02fc`](#insn-00aa02fc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0300`](#insn-00aa0300) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0304`](#insn-00aa0304) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9fbd0`](#insn-00a9fbd0)

~~~json
{
  "source": "00a9fbd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fbd4`](#insn-00a9fbd4)

~~~json
{
  "source": "00a9fbd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fbd8`](#insn-00a9fbd8)

~~~json
{
  "source": "00a9fbd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fbdc`](#insn-00a9fbdc)

~~~json
{
  "source": "00a9fbdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fbe0`](#insn-00a9fbe0)

~~~json
{
  "source": "00a9fbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fbe4`](#insn-00a9fbe4)

~~~json
{
  "source": "00a9fbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fc0c`](#insn-00a9fc0c)

~~~json
{
  "source": "00a9fc0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc20`](#insn-00a9fc20)

~~~json
{
  "source": "00a9fc20",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc24`](#insn-00a9fc24)

~~~json
{
  "source": "00a9fc24",
  "target": "00a9fcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fc28`](#insn-00a9fc28)

~~~json
{
  "source": "00a9fc28",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc34`](#insn-00a9fc34)

~~~json
{
  "source": "00a9fc34",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9fc3c`](#insn-00a9fc3c)

~~~json
{
  "source": "00a9fc3c",
  "target": "00a9fc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fc40`](#insn-00a9fc40)

~~~json
{
  "source": "00a9fc40",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc4c`](#insn-00a9fc4c)

~~~json
{
  "source": "00a9fc4c",
  "target": "00334048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334045",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e20480c1d2093049e069d08580c1f20480e00d3dedd",
  "capture_start": "00334045",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9fc50`](#insn-00a9fc50)

~~~json
{
  "source": "00a9fc50",
  "target": "00a9ff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fc54`](#insn-00a9fc54)

~~~json
{
  "source": "00a9fc54",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc60`](#insn-00a9fc60)

~~~json
{
  "source": "00a9fc60",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9fc64`](#insn-00a9fc64)

~~~json
{
  "source": "00a9fc64",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fc74`](#insn-00a9fc74)

~~~json
{
  "source": "00a9fc74",
  "target": "002f48dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fc90`](#insn-00a9fc90)

~~~json
{
  "source": "00a9fc90",
  "target": "00239da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 41840,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00a9fc94`](#insn-00a9fc94)

~~~json
{
  "source": "00a9fc94",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fcb0`](#insn-00a9fcb0)

~~~json
{
  "source": "00a9fcb0",
  "target": "00a06cfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fce0`](#insn-00a9fce0)

~~~json
{
  "source": "00a9fce0",
  "target": "00a9ff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fce4`](#insn-00a9fce4)

~~~json
{
  "source": "00a9fce4",
  "target": "00a9fed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fcec`](#insn-00a9fcec)

~~~json
{
  "source": "00a9fcec",
  "target": "00a9ff04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd04`](#insn-00a9fd04)

~~~json
{
  "source": "00a9fd04",
  "target": "00a9fd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd0c`](#insn-00a9fd0c)

~~~json
{
  "source": "00a9fd0c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd14`](#insn-00a9fd14)

~~~json
{
  "source": "00a9fd14",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd24`](#insn-00a9fd24)

~~~json
{
  "source": "00a9fd24",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fd38`](#insn-00a9fd38)

~~~json
{
  "source": "00a9fd38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd44`](#insn-00a9fd44)

~~~json
{
  "source": "00a9fd44",
  "target": "002f48d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd60`](#insn-00a9fd60)

~~~json
{
  "source": "00a9fd60",
  "target": "00a9fe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd6c`](#insn-00a9fd6c)

~~~json
{
  "source": "00a9fd6c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd74`](#insn-00a9fd74)

~~~json
{
  "source": "00a9fd74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd84`](#insn-00a9fd84)

~~~json
{
  "source": "00a9fd84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd94`](#insn-00a9fd94)

~~~json
{
  "source": "00a9fd94",
  "target": "00a9fda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fd98`](#insn-00a9fd98)

~~~json
{
  "source": "00a9fd98",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fda0`](#insn-00a9fda0)

~~~json
{
  "source": "00a9fda0",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fda4`](#insn-00a9fda4)

~~~json
{
  "source": "00a9fda4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fdb4`](#insn-00a9fdb4)

~~~json
{
  "source": "00a9fdb4",
  "target": "00a5b0c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fdd4`](#insn-00a9fdd4)

~~~json
{
  "source": "00a9fdd4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fde8`](#insn-00a9fde8)

~~~json
{
  "source": "00a9fde8",
  "target": "0088f9e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe18`](#insn-00a9fe18)

~~~json
{
  "source": "00a9fe18",
  "target": "00a9f124",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe24`](#insn-00a9fe24)

~~~json
{
  "source": "00a9fe24",
  "target": "00aa0290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe2c`](#insn-00a9fe2c)

~~~json
{
  "source": "00a9fe2c",
  "target": "007cf4b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe30`](#insn-00a9fe30)

~~~json
{
  "source": "00a9fe30",
  "target": "00a9fe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe34`](#insn-00a9fe34)

~~~json
{
  "source": "00a9fe34",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe38`](#insn-00a9fe38)

~~~json
{
  "source": "00a9fe38",
  "target": "0078aefc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe3c`](#insn-00a9fe3c)

~~~json
{
  "source": "00a9fe3c",
  "target": "00aa0240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe44`](#insn-00a9fe44)

~~~json
{
  "source": "00a9fe44",
  "target": "00aa026c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe58`](#insn-00a9fe58)

~~~json
{
  "source": "00a9fe58",
  "target": "00a9fe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe64`](#insn-00a9fe64)

~~~json
{
  "source": "00a9fe64",
  "target": "00a9fd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe68`](#insn-00a9fe68)

~~~json
{
  "source": "00a9fe68",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fe70`](#insn-00a9fe70)

~~~json
{
  "source": "00a9fe70",
  "target": "00a9fe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fe84`](#insn-00a9fe84)

~~~json
{
  "source": "00a9fe84",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fea0`](#insn-00a9fea0)

~~~json
{
  "source": "00a9fea0",
  "target": "002f48d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9feb4`](#insn-00a9feb4)

~~~json
{
  "source": "00a9feb4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fed0`](#insn-00a9fed0)

~~~json
{
  "source": "00a9fed0",
  "target": "00a9fe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9fed4`](#insn-00a9fed4)

~~~json
{
  "source": "00a9fed4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fee0`](#insn-00a9fee0)

~~~json
{
  "source": "00a9fee0",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fee8`](#insn-00a9fee8)

~~~json
{
  "source": "00a9fee8",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9fefc`](#insn-00a9fefc)

~~~json
{
  "source": "00a9fefc",
  "target": "007cebc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ff14`](#insn-00a9ff14)

~~~json
{
  "source": "00a9ff14",
  "target": "00a9ff84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ff18`](#insn-00a9ff18)

~~~json
{
  "source": "00a9ff18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ff2c`](#insn-00a9ff2c)

~~~json
{
  "source": "00a9ff2c",
  "target": "002f48dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ff48`](#insn-00a9ff48)

~~~json
{
  "source": "00a9ff48",
  "target": "00239da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 41840,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00a9ff4c`](#insn-00a9ff4c)

~~~json
{
  "source": "00a9ff4c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ff5c`](#insn-00a9ff5c)

~~~json
{
  "source": "00a9ff5c",
  "target": "0032f934",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f921",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d040a640c1f10440e00dedd440b",
  "capture_start": "0032f921",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9ff60`](#insn-00a9ff60)

~~~json
{
  "source": "00a9ff60",
  "target": "00c1b870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b870",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a9ff64`](#insn-00a9ff64)

~~~json
{
  "source": "00a9ff64",
  "target": "00c24654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ff88`](#insn-00a9ff88)

~~~json
{
  "source": "00a9ff88",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ff94`](#insn-00a9ff94)

~~~json
{
  "source": "00a9ff94",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ff9c`](#insn-00a9ff9c)

~~~json
{
  "source": "00a9ff9c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ffa0`](#insn-00a9ffa0)

~~~json
{
  "source": "00a9ffa0",
  "target": "00a9ffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ffb4`](#insn-00a9ffb4)

~~~json
{
  "source": "00a9ffb4",
  "target": "00239df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 41912,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00a9ffb8`](#insn-00a9ffb8)

~~~json
{
  "source": "00a9ffb8",
  "target": "00a9ffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ffbc`](#insn-00a9ffbc)

~~~json
{
  "source": "00a9ffbc",
  "target": "00aa0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ffd4`](#insn-00a9ffd4)

~~~json
{
  "source": "00a9ffd4",
  "target": "00aa0034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ffd8`](#insn-00a9ffd8)

~~~json
{
  "source": "00a9ffd8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ffe4`](#insn-00a9ffe4)

~~~json
{
  "source": "00a9ffe4",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ffe8`](#insn-00a9ffe8)

~~~json
{
  "source": "00a9ffe8",
  "target": "00aa0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ffec`](#insn-00a9ffec)

~~~json
{
  "source": "00a9ffec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0000`](#insn-00aa0000)

~~~json
{
  "source": "00aa0000",
  "target": "00239ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42116,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa0004`](#insn-00aa0004)

~~~json
{
  "source": "00aa0004",
  "target": "00aa0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0008`](#insn-00aa0008)

~~~json
{
  "source": "00aa0008",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa001c`](#insn-00aa001c)

~~~json
{
  "source": "00aa001c",
  "target": "00a5b31c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0024`](#insn-00aa0024)

~~~json
{
  "source": "00aa0024",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0030`](#insn-00aa0030)

~~~json
{
  "source": "00aa0030",
  "target": "00aa0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0034`](#insn-00aa0034)

~~~json
{
  "source": "00aa0034",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0038`](#insn-00aa0038)

~~~json
{
  "source": "00aa0038",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0044`](#insn-00aa0044)

~~~json
{
  "source": "00aa0044",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa004c`](#insn-00aa004c)

~~~json
{
  "source": "00aa004c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0050`](#insn-00aa0050)

~~~json
{
  "source": "00aa0050",
  "target": "00aa0070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0064`](#insn-00aa0064)

~~~json
{
  "source": "00aa0064",
  "target": "00239df0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 41912,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa0068`](#insn-00aa0068)

~~~json
{
  "source": "00aa0068",
  "target": "00aa0088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa006c`](#insn-00aa006c)

~~~json
{
  "source": "00aa006c",
  "target": "00aa00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0084`](#insn-00aa0084)

~~~json
{
  "source": "00aa0084",
  "target": "00aa00e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0088`](#insn-00aa0088)

~~~json
{
  "source": "00aa0088",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0094`](#insn-00aa0094)

~~~json
{
  "source": "00aa0094",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0098`](#insn-00aa0098)

~~~json
{
  "source": "00aa0098",
  "target": "00aa00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa009c`](#insn-00aa009c)

~~~json
{
  "source": "00aa009c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00b0`](#insn-00aa00b0)

~~~json
{
  "source": "00aa00b0",
  "target": "00239ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42116,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa00b8`](#insn-00aa00b8)

~~~json
{
  "source": "00aa00b8",
  "target": "00aa00ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa00bc`](#insn-00aa00bc)

~~~json
{
  "source": "00aa00bc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00d0`](#insn-00aa00d0)

~~~json
{
  "source": "00aa00d0",
  "target": "00a5b31c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00d8`](#insn-00aa00d8)

~~~json
{
  "source": "00aa00d8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00e4`](#insn-00aa00e4)

~~~json
{
  "source": "00aa00e4",
  "target": "00aa0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa00e8`](#insn-00aa00e8)

~~~json
{
  "source": "00aa00e8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00ec`](#insn-00aa00ec)

~~~json
{
  "source": "00aa00ec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00f8`](#insn-00aa00f8)

~~~json
{
  "source": "00aa00f8",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa00fc`](#insn-00aa00fc)

~~~json
{
  "source": "00aa00fc",
  "target": "00aa014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0100`](#insn-00aa0100)

~~~json
{
  "source": "00aa0100",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0114`](#insn-00aa0114)

~~~json
{
  "source": "00aa0114",
  "target": "00239ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42116,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa011c`](#insn-00aa011c)

~~~json
{
  "source": "00aa011c",
  "target": "00aa014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0120`](#insn-00aa0120)

~~~json
{
  "source": "00aa0120",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0134`](#insn-00aa0134)

~~~json
{
  "source": "00aa0134",
  "target": "00a5b31c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa013c`](#insn-00aa013c)

~~~json
{
  "source": "00aa013c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0148`](#insn-00aa0148)

~~~json
{
  "source": "00aa0148",
  "target": "00aa0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa014c`](#insn-00aa014c)

~~~json
{
  "source": "00aa014c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0158`](#insn-00aa0158)

~~~json
{
  "source": "00aa0158",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa015c`](#insn-00aa015c)

~~~json
{
  "source": "00aa015c",
  "target": "00aa01ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0160`](#insn-00aa0160)

~~~json
{
  "source": "00aa0160",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0174`](#insn-00aa0174)

~~~json
{
  "source": "00aa0174",
  "target": "00239ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42116,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa017c`](#insn-00aa017c)

~~~json
{
  "source": "00aa017c",
  "target": "00aa01ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0180`](#insn-00aa0180)

~~~json
{
  "source": "00aa0180",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0194`](#insn-00aa0194)

~~~json
{
  "source": "00aa0194",
  "target": "00a5b31c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa019c`](#insn-00aa019c)

~~~json
{
  "source": "00aa019c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01a8`](#insn-00aa01a8)

~~~json
{
  "source": "00aa01a8",
  "target": "00aa0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa01ac`](#insn-00aa01ac)

~~~json
{
  "source": "00aa01ac",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01b8`](#insn-00aa01b8)

~~~json
{
  "source": "00aa01b8",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01bc`](#insn-00aa01bc)

~~~json
{
  "source": "00aa01bc",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa01c0`](#insn-00aa01c0)

~~~json
{
  "source": "00aa01c0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01d4`](#insn-00aa01d4)

~~~json
{
  "source": "00aa01d4",
  "target": "00239ebc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0022fa38",
  "offset": 42116,
  "size": 43008,
  "datatype": "Elf64_Rela[1792]",
  "bytes": "a0c0b1000000000002040000010000000000000000000000a8c0b10000000000",
  "capture_start": "0022fa38",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aa01dc`](#insn-00aa01dc)

~~~json
{
  "source": "00aa01dc",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa01e0`](#insn-00aa01e0)

~~~json
{
  "source": "00aa01e0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01f4`](#insn-00aa01f4)

~~~json
{
  "source": "00aa01f4",
  "target": "00a5b31c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa01fc`](#insn-00aa01fc)

~~~json
{
  "source": "00aa01fc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0208`](#insn-00aa0208)

~~~json
{
  "source": "00aa0208",
  "target": "00a5b0c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa023c`](#insn-00aa023c)

~~~json
{
  "source": "00aa023c",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0244`](#insn-00aa0244)

~~~json
{
  "source": "00aa0244",
  "target": "007cf4b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa024c`](#insn-00aa024c)

~~~json
{
  "source": "00aa024c",
  "target": "00aa0268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0250`](#insn-00aa0250)

~~~json
{
  "source": "00aa0250",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0254`](#insn-00aa0254)

~~~json
{
  "source": "00aa0254",
  "target": "0078af80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0258`](#insn-00aa0258)

~~~json
{
  "source": "00aa0258",
  "target": "00aa0268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa025c`](#insn-00aa025c)

~~~json
{
  "source": "00aa025c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0260`](#insn-00aa0260)

~~~json
{
  "source": "00aa0260",
  "target": "007bd9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0264`](#insn-00aa0264)

~~~json
{
  "source": "00aa0264",
  "target": "00aa0290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa026c`](#insn-00aa026c)

~~~json
{
  "source": "00aa026c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0288`](#insn-00aa0288)

~~~json
{
  "source": "00aa0288",
  "target": "0066398c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa0298`](#insn-00aa0298)

~~~json
{
  "source": "00aa0298",
  "target": "00aa02b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa02c8`](#insn-00aa02c8)

~~~json
{
  "source": "00aa02c8",
  "target": "00a9f124",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa02d0`](#insn-00aa02d0)

~~~json
{
  "source": "00aa02d0",
  "target": "00aa02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa02f0`](#insn-00aa02f0)

~~~json
{
  "source": "00aa02f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa02f4`](#insn-00aa02f4)

~~~json
{
  "source": "00aa02f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa02f8`](#insn-00aa02f8)

~~~json
{
  "source": "00aa02f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa02fc`](#insn-00aa02fc)

~~~json
{
  "source": "00aa02fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0300`](#insn-00aa0300)

~~~json
{
  "source": "00aa0300",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0304`](#insn-00aa0304)

~~~json
{
  "source": "00aa0304",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
