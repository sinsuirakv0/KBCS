# 00ad7aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ad6af8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-f2af87c11f349f040e76625f5833727f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad7aec",
  "name": "FUN_00ad7aec",
  "size": 1220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "082e43f754b2f05681b462dc4418a371c11e2b0ae4e6e89a43fd4e15428b950e",
  "source_text_sha256": "082e43f754b2f05681b462dc4418a371c11e2b0ae4e6e89a43fd4e15428b950e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad7aec",
        "00ad7faf"
      ]
    ],
    "bytes_sha256": "f4aa1ff85f412a046942590f13f49ae0b1d51f436b3400251c598e3d7adc5af3",
    "instruction_count": 305,
    "instruction_bytes": 1220,
    "body_bytes": 1220,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad19bc](../00ad1/00ad19bc.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)
- [00ae1ccc](../00ae1/00ae1ccc.md)
- [00aed9f0](../00aed/00aed9f0.md)
- [00af1198](../00af1/00af1198.md)
- [00b0d2e4](../00b0d/00b0d2e4.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [005c08e0](../005c0/005c08e0.md)
- [00615d00](../00615/00615d00.md)
- [00676b3c](../00676/00676b3c.md)
- [00744198](../00744/00744198.md)
- [00744334](../00744/00744334.md)
- [00744610](../00744/00744610.md)
- [007bcd04](../007bc/007bcd04.md)
- [007df5b8](../007df/007df5b8.md)
- [007df630](../007df/007df630.md)
- [008011a8](../00801/008011a8.md)
- [00803674](../00803/00803674.md)
- [00803b14](../00803/00803b14.md)
- [00803c64](../00803/00803c64.md)
- [008621ec](../00862/008621ec.md)
- [00a33a4c](../00a33/00a33a4c.md)
- [00a33ee0](../00a33/00a33ee0.md)
- [00a43078](../00a43/00a43078.md)
- [00a43104](../00a43/00a43104.md)
- [00a43aec](../00a43/00a43aec.md)
- [00b0a6ec](../00b0a/00b0a6ec.md)
- [00b0bda4](../00b0b/00b0bda4.md)
- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 12177 bytes

~~~c

undefined8 FUN_00ad7aec(long param_1)

{
  char cVar1;
  uint uVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  ulong uVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 uVar12;
  undefined8 *puVar13;
  long *plVar14;
  long lVar15;
  long *plVar16;
  byte *pbVar17;
  long lVar18;
  ulong uVar19;
  undefined8 *puVar20;
  long lVar21;
  char *pcVar22;
  
                    /* try { // try from 00ad7af4 to 00bd7b03 has its CatchHandler @ 00ad8904 */
                    /* try { // try from 00ad7b08 to 00bd7b1b has its CatchHandler @ 00ad8900 */
  plVar16 = (long *)((long)&fde_table_entry_003380b8.initial_loc + param_1);
  cVar1 = *(char *)((long)&fde_table_entry_003380e8.initial_loc + param_1 + 1);
                    /* try { // try from 00ad7b1c to 00bd7b2f has its CatchHandler @ 00ad88fc */
  *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
  if (cVar1 != '\0') {
    iVar3 = *(int *)((long)&fde_table_entry_00333970.data_loc + param_1);
    puVar11 = (undefined8 *)((long)&fde_table_entry_003380c0.initial_loc + param_1);
    puVar13 = (undefined8 *)*puVar11;
    while (puVar20 = puVar11, puVar13 != (undefined8 *)0x0) {
      while (puVar7 = puVar13, puVar11 = puVar7, *(int *)(puVar7 + 4) <= iVar3) {
                    /* try { // try from 00ad7b5c to 00bd7b6f has its CatchHandler @ 00ad88b8 */
        if (iVar3 <= *(int *)(puVar7 + 4)) goto LAB_00ad7bc8;
        puVar13 = (undefined8 *)puVar7[1];
        if ((undefined8 *)puVar7[1] == (undefined8 *)0x0) {
          puVar20 = puVar7 + 1;
          goto LAB_00ad7b6c;
        }
      }
      puVar13 = (undefined8 *)*puVar7;
                    /* try { // try from 00ad7b44 to 00bd7b53 has its CatchHandler @ 00ad88bc */
    }
LAB_00ad7b6c:
                    /* try { // try from 00ad7b70 to 00bd7b83 has its CatchHandler @ 00ad88b4 */
    puVar7 = (undefined8 *)_Znwm(0x40);
    puVar7[7] = 0;
    puVar7[6] = 0;
                    /* try { // try from 00ad7b8c to 00bd7b93 has its CatchHandler @ 00ad89f0 */
    puVar7[5] = puVar7 + 6;
    *puVar7 = 0;
    puVar7[1] = 0;
    puVar7[2] = puVar11;
    *puVar20 = puVar7;
                    /* try { // try from 00ad7b9c to 00bd7bab has its CatchHandler @ 00ad88b0 */
    plVar14 = (long *)*plVar16;
    *(int *)(puVar7 + 4) = iVar3;
    lVar15 = *plVar14;
    puVar11 = puVar7;
    if (lVar15 != 0) {
      *plVar16 = lVar15;
                    /* try { // try from 00ad7bb0 to 00bd7bc3 has its CatchHandler @ 00ad88ac */
      puVar11 = (undefined8 *)*puVar20;
    }
    FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380c0.initial_loc + param_1),puVar11);
                    /* try { // try from 00ad7bc4 to 00bd7bd7 has its CatchHandler @ 00ad88a8 */
    *(long *)((long)&fde_table_entry_003380c8.initial_loc + param_1) =
         *(long *)((long)&fde_table_entry_003380c8.initial_loc + param_1) + 1;
LAB_00ad7bc8:
    iVar3 = FUN_00803c64();
    puVar13 = (undefined8 *)puVar7[6];
    puVar11 = puVar7 + 6;
    while (puVar20 = puVar11, puVar13 != (undefined8 *)0x0) {
                    /* try { // try from 00ad7bf4 to 00bd7c07 has its CatchHandler @ 00ad88dc */
      while (puVar8 = puVar13, puVar11 = puVar8, *(int *)((long)puVar8 + 0x1c) <= iVar3) {
        if (iVar3 <= *(int *)((long)puVar8 + 0x1c)) goto LAB_00ad7c64;
                    /* try { // try from 00ad7c08 to 00bd7c1b has its CatchHandler @ 00ad88c8 */
        puVar13 = (undefined8 *)puVar8[1];
        if ((undefined8 *)puVar8[1] == (undefined8 *)0x0) {
          puVar20 = puVar8 + 1;
          goto LAB_00ad7c14;
        }
      }
      puVar13 = (undefined8 *)*puVar8;
    }
LAB_00ad7c14:
    puVar8 = (undefined8 *)_Znwm(0x28);
                    /* try { // try from 00ad7c20 to 00bd7c2f has its CatchHandler @ 00ad88ec */
    *puVar8 = 0;
    puVar8[1] = 0;
    puVar8[2] = puVar11;
    *puVar20 = puVar8;
    plVar16 = (long *)puVar7[5];
                    /* try { // try from 00ad7c38 to 00bd7c4b has its CatchHandler @ 00ad88d8 */
    *(int *)((long)puVar8 + 0x1c) = iVar3;
    *(undefined1 *)(puVar8 + 4) = 0;
    puVar11 = puVar8;
    if (*plVar16 != 0) {
      puVar7[5] = *plVar16;
                    /* try { // try from 00ad7c4c to 00bd7c5f has its CatchHandler @ 00ad88c4 */
      puVar11 = (undefined8 *)*puVar20;
    }
    FUN_0043bf04(puVar7[6],puVar11);
    puVar7[7] = puVar7[7] + 1;
LAB_00ad7c64:
                    /* try { // try from 00ad7c64 to 00bd7c73 has its CatchHandler @ 00ad88e8 */
    if (*(char *)(puVar8 + 4) != '\0') {
      *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 1;
    }
  }
  uVar5 = *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + param_1);
                    /* try { // try from 00ad7c7c to 00bd7c8f has its CatchHandler @ 00ad88d4 */
  *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
  uVar9 = FUN_007df5b8(param_1,uVar5);
                    /* try { // try from 00ad7c90 to 00bd7ca3 has its CatchHandler @ 00ad88c0 */
  if (((uVar9 & 1) != 0) &&
     (cVar1 = *(char *)((long)&fde_table_entry_003380f8.initial_loc + param_1),
     iVar3 = FUN_00803c64(), iVar3 == cVar1)) {
    *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 1;
  }
  uVar5 = *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + param_1);
                    /* try { // try from 00ad7ca8 to 00bd7caf has its CatchHandler @ 00ad89f0 */
  *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 3) = 0;
  uVar9 = FUN_007df630(param_1,uVar5);
                    /* try { // try from 00ad7cb8 to 00bd7cc7 has its CatchHandler @ 00ad88a4 */
  if (((uVar9 & 1) != 0) &&
     (cVar1 = *(char *)((long)&fde_table_entry_003380f8.initial_loc + param_1),
     iVar3 = FUN_00803c64(), iVar3 == cVar1)) {
    *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 3) = 1;
  }
                    /* try { // try from 00ad7cd0 to 00bd7ce3 has its CatchHandler @ 00ad88a0 */
  uVar4 = FUN_00803b14(0);
  uVar5 = FUN_00803c64();
                    /* try { // try from 00ad7ce4 to 00bd7cf7 has its CatchHandler @ 00ad889c */
  uVar9 = FUN_00676b3c(param_1 + 0x13d8,1);
  if ((uVar9 & 1) == 0) {
    uVar9 = FUN_007bcd04(param_1,1);
                    /* try { // try from 00ad7d0c to 00bd7d1b has its CatchHandler @ 00ad8898 */
    if ((uVar9 & 1) == 0) {
                    /* try { // try from 00ad7f6c to 00bd7f7b has its CatchHandler @ 00ad8868 */
      uVar9 = FUN_00a33a4c(param_1 + 0x530,0xffffffff,0xffffffff);
      if ((uVar9 & 1) != 0) {
        uVar4 = FUN_00a33ee0(param_1 + 0x530,uVar4);
                    /* try { // try from 00ad7f84 to 00bd7f97 has its CatchHandler @ 00ad8864 */
      }
      goto LAB_00ad7d24;
    }
    uVar12 = 0x44;
  }
  else {
    uVar12 = 0x2a;
                    /* try { // try from 00ad7cfc to 00bd7d03 has its CatchHandler @ 00ad89f0 */
  }
  uVar4 = FUN_008011a8(0xfffffff8,uVar12);
  uVar5 = 0;
LAB_00ad7d24:
                    /* try { // try from 00ad7d24 to 00bd7d37 has its CatchHandler @ 00ad8894 */
  uVar6 = FUN_008621ec(param_1);
                    /* try { // try from 00ad7d38 to 00bd7d4b has its CatchHandler @ 00ad8890 */
  uVar9 = FUN_00615d00(param_1,uVar4,uVar5,uVar6);
  if ((((uVar9 & 1) == 0) && (uVar9 = FUN_00744610(param_1 + 0xbe0), (uVar9 & 1) == 0)) &&
     (iVar3 = FUN_00803674(0), iVar3 != -0x18)) {
    uVar12 = 0;
    *(undefined2 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
    *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
  }
  else {
    *(undefined2 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
                    /* try { // try from 00ad7d6c to 00bd7d73 has its CatchHandler @ 00ad89f0 */
    *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
                    /* try { // try from 00ad7d74 to 00bd7dff has its CatchHandler @ 00ad8970 */
    pcVar22 = (char *)(param_1 + 0x46f91);
    lVar15 = param_1 + 0xc5bb;
    lVar21 = 10;
    do {
      iVar3 = *(int *)((long)&QWORD_0039b978 + param_1 + 4);
      lVar18 = param_1 + 0xc5b8 + (long)iVar3 * 0x2c;
      pbVar17 = (byte *)(lVar15 + (long)iVar3 * 0x2c);
      uVar2 = (uint)(*(byte *)(lVar18 + 0x2a) ^ pbVar17[-1]) << 0x10 |
              (uint)(*(byte *)(lVar18 + 0x2b) ^ *pbVar17) << 0x18 |
              (uint)(*(byte *)(lVar18 + 0x29) ^ pbVar17[-2]) << 8 |
              (uint)(*(byte *)(lVar18 + 0x28) ^ pbVar17[-3]);
      iVar3 = uVar2 - 2;
                    /* try { // try from 00ad7e10 to 00bd7e17 has its CatchHandler @ 00ad8974 */
                    /* try { // try from 00ad7e1c to 00bd7e3f has its CatchHandler @ 00ad89b0 */
      if (((int)uVar2 < 2) ||
         (((uVar9 = FUN_00744610(param_1 + 0xbe0), (uVar9 & 1) == 0 ||
           ((uVar9 = FUN_00744198(param_1 + 0xbe0,iVar3), (uVar9 & 1) != 0 &&
            (uVar9 = FUN_00744334(param_1 + 0xbe0,iVar3), (uVar9 & 1) == 0)))) &&
          (uVar9 = FUN_005c08e0(param_1 + 0x4a0,*(undefined4 *)((long)&QWORD_0039b978 + param_1 + 4)
                                ,iVar3), (uVar9 & 1) == 0)))) {
                    /* try { // try from 00ad7e44 to 00bd7e5b has its CatchHandler @ 00ad89f0 */
        if ((*(uint *)(param_1 + 0x3398) & 0xfffffffe) == 2) {
          uVar5 = FUN_00a43078(param_1 + 0x347348);
                    /* try { // try from 00ad7e64 to 00bd7e73 has its CatchHandler @ 00ad888c */
          uVar9 = FUN_00a43104(param_1 + 0x347348,uVar5);
          uVar9 = uVar9 & 0xffffffff;
        }
        else {
                    /* try { // try from 00ad7e78 to 00bd7e8b has its CatchHandler @ 00ad8888 */
          uVar9 = 0;
        }
        uVar19 = 0;
                    /* try { // try from 00ad7e8c to 00bd7e9f has its CatchHandler @ 00ad8884 */
                    /* try { // try from 00ad7eac to 00bd7eb3 has its CatchHandler @ 00ad89f0 */
                    /* try { // try from 00ad7ebc to 00bd7ecb has its CatchHandler @ 00ad8880 */
                    /* try { // try from 00ad7ed4 to 00bd7ee7 has its CatchHandler @ 00ad887c */
                    /* try { // try from 00ad7ee8 to 00bd7efb has its CatchHandler @ 00ad8878 */
                    /* try { // try from 00ad7f04 to 00bd7f0b has its CatchHandler @ 00ad89f0 */
                    /* try { // try from 00ad7f14 to 00bd7f23 has its CatchHandler @ 00ad8874 */
                    /* try { // try from 00ad7f28 to 00bd7f3b has its CatchHandler @ 00ad8870 */
                    /* try { // try from 00ad7f3c to 00bd7f4f has its CatchHandler @ 00ad886c */
        while ((((((*(char *)(param_1 + 0x47d72) == pcVar22[1] &&
                   *(char *)(param_1 + 0x47d73) == pcVar22[2]) &&
                  *(char *)(param_1 + 0x47d71) == *pcVar22) &&
                  *(char *)(param_1 + 0x47d70) == pcVar22[-1] ||
                 ((uVar10 = FUN_00744610(param_1 + 0xbe0), (uVar10 & 1) != 0 &&
                  ((uVar10 = FUN_00744198(param_1 + 0xbe0,uVar19 & 0xffffffff), (uVar10 & 1) == 0 ||
                   (uVar10 = FUN_00744334(param_1 + 0xbe0,uVar19 & 0xffffffff), (uVar10 & 1) != 0)))
                  ))) || ((uVar10 = FUN_00b0a6ec(param_1 + 0x3d8), (uVar10 & 1) != 0 &&
                          (uVar10 = FUN_00b0bda4(param_1 + 0x3d8,uVar19 & 0xffffffff),
                          (uVar10 & 1) == 0)))) ||
               ((uVar10 = FUN_005c08e0(param_1 + 0x4a0,
                                       *(undefined4 *)((long)&QWORD_0039b978 + param_1 + 4),
                                       uVar19 & 0xffffffff), (uVar10 & 1) != 0 ||
                (((uVar9 & 1) != 0 &&
                 (uVar10 = FUN_00a43aec(param_1 + 0x347348,uVar19 & 0xffffffff), (uVar10 & 1) == 0))
                ))))) {
          uVar19 = uVar19 + 1;
          pcVar22 = pcVar22 + 4;
          if (uVar19 == 0x378) {
            return 2;
          }
        }
        return 3;
      }
      lVar21 = lVar21 + -1;
      lVar15 = lVar15 + 4;
    } while (lVar21 != 0);
    uVar12 = 1;
  }
                    /* try { // try from 00ad7f98 to 00bd7fab has its CatchHandler @ 00ad8860 */
  return uVar12;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad7aec"></a> `00ad7aec` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ad7af0"></a> `00ad7af0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7af4"></a> `00ad7af4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7af8"></a> `00ad7af8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7afc"></a> `00ad7afc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7b00"></a> `00ad7b00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ad7b04"></a> `00ad7b04` | `08 e0 4c 91` | add x8,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00ad7b08"></a> `00ad7b08` | `98 2e 87 52` | mov w24,#0x3974 | `FALL_THROUGH`
<a id="insn-00ad7b0c"></a> `00ad7b0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad7b10"></a> `00ad7b10` | `17 e1 02 91` | add x23,x8,#0xb8 | `FALL_THROUGH`
<a id="insn-00ad7b14"></a> `00ad7b14` | `78 06 a0 72` | movk w24,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad7b18"></a> `00ad7b18` | `e8 c6 40 39` | ldrb w8,[x23, #0x31] | `FALL_THROUGH`
<a id="insn-00ad7b1c"></a> `00ad7b1c` | `ff c2 00 39` | strb wzr,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7b20"></a> `00ad7b20` | `a8 0a 00 34` | cbz w8,0x00ad7c74 | `CONDITIONAL_JUMP`
<a id="insn-00ad7b24"></a> `00ad7b24` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00ad7b28"></a> `00ad7b28` | `75 6a 78 b8` | ldr w21,[x19, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7b2c"></a> `00ad7b2c` | `c8 8e 40 f8` | ldr x8,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00ad7b30"></a> `00ad7b30` | `c8 00 00 b5` | cbnz x8,0x00ad7b48 | `CONDITIONAL_JUMP`
<a id="insn-00ad7b34"></a> `00ad7b34` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00ad7b38"></a> `00ad7b38` | `0d 00 00 14` | b 0x00ad7b6c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7b3c"></a> `00ad7b3c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ad7b40"></a> `00ad7b40` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00ad7b44"></a> `00ad7b44` | `48 01 00 b4` | cbz x8,0x00ad7b6c | `CONDITIONAL_JUMP`
<a id="insn-00ad7b48"></a> `00ad7b48` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00ad7b4c"></a> `00ad7b4c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7b50"></a> `00ad7b50` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00ad7b54"></a> `00ad7b54` | `4b ff ff 54` | b.lt 0x00ad7b3c | `CONDITIONAL_JUMP`
<a id="insn-00ad7b58"></a> `00ad7b58` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00ad7b5c"></a> `00ad7b5c` | `6a 03 00 54` | b.ge 0x00ad7bc8 | `CONDITIONAL_JUMP`
<a id="insn-00ad7b60"></a> `00ad7b60` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00ad7b64"></a> `00ad7b64` | `28 ff ff b5` | cbnz x8,0x00ad7b48 | `CONDITIONAL_JUMP`
<a id="insn-00ad7b68"></a> `00ad7b68` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ad7b6c"></a> `00ad7b6c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ad7b70"></a> `00ad7b70` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00ad7b74"></a> `00ad7b74` | `ef 04 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7b78"></a> `00ad7b78` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ad7b7c"></a> `00ad7b7c` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ad7b80"></a> `00ad7b80` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ad7b84"></a> `00ad7b84` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ad7b88"></a> `00ad7b88` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ad7b8c"></a> `00ad7b8c` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ad7b90"></a> `00ad7b90` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ad7b94"></a> `00ad7b94` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7b98"></a> `00ad7b98` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00ad7b9c"></a> `00ad7b9c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00ad7ba0"></a> `00ad7ba0` | `15 20 00 b9` | str w21,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7ba4"></a> `00ad7ba4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ad7ba8"></a> `00ad7ba8` | `68 00 00 b4` | cbz x8,0x00ad7bb4 | `CONDITIONAL_JUMP`
<a id="insn-00ad7bac"></a> `00ad7bac` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00ad7bb0"></a> `00ad7bb0` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00ad7bb4"></a> `00ad7bb4` | `e0 06 40 f9` | ldr x0,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ad7bb8"></a> `00ad7bb8` | `d3 90 e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7bbc"></a> `00ad7bbc` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7bc0"></a> `00ad7bc0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7bc4"></a> `00ad7bc4` | `e8 0a 00 f9` | str x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7bc8"></a> `00ad7bc8` | `27 b0 f4 97` | bl 0x00803c64 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7bcc"></a> `00ad7bcc` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00ad7bd0"></a> `00ad7bd0` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00ad7bd4"></a> `00ad7bd4` | `28 0f 43 f8` | ldr x8,[x25, #0x30]! | `FALL_THROUGH`
<a id="insn-00ad7bd8"></a> `00ad7bd8` | `c8 00 00 b5` | cbnz x8,0x00ad7bf0 | `CONDITIONAL_JUMP`
<a id="insn-00ad7bdc"></a> `00ad7bdc` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-00ad7be0"></a> `00ad7be0` | `0d 00 00 14` | b 0x00ad7c14 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7be4"></a> `00ad7be4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ad7be8"></a> `00ad7be8` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00ad7bec"></a> `00ad7bec` | `48 01 00 b4` | cbz x8,0x00ad7c14 | `CONDITIONAL_JUMP`
<a id="insn-00ad7bf0"></a> `00ad7bf0` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00ad7bf4"></a> `00ad7bf4` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ad7bf8"></a> `00ad7bf8` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00ad7bfc"></a> `00ad7bfc` | `4b ff ff 54` | b.lt 0x00ad7be4 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c00"></a> `00ad7c00` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00ad7c04"></a> `00ad7c04` | `0a 03 00 54` | b.ge 0x00ad7c64 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c08"></a> `00ad7c08` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ad7c0c"></a> `00ad7c0c` | `28 ff ff b5` | cbnz x8,0x00ad7bf0 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c10"></a> `00ad7c10` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ad7c14"></a> `00ad7c14` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ad7c18"></a> `00ad7c18` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00ad7c1c"></a> `00ad7c1c` | `c5 04 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7c20"></a> `00ad7c20` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ad7c24"></a> `00ad7c24` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ad7c28"></a> `00ad7c28` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ad7c2c"></a> `00ad7c2c` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7c30"></a> `00ad7c30` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00ad7c34"></a> `00ad7c34` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad7c38"></a> `00ad7c38` | `16 1c 00 b9` | str w22,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ad7c3c"></a> `00ad7c3c` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7c40"></a> `00ad7c40` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ad7c44"></a> `00ad7c44` | `68 00 00 b4` | cbz x8,0x00ad7c50 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c48"></a> `00ad7c48` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad7c4c"></a> `00ad7c4c` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00ad7c50"></a> `00ad7c50` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7c54"></a> `00ad7c54` | `ac 90 e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7c58"></a> `00ad7c58` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ad7c5c"></a> `00ad7c5c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7c60"></a> `00ad7c60` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ad7c64"></a> `00ad7c64` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7c68"></a> `00ad7c68` | `68 00 00 34` | cbz w8,0x00ad7c74 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c6c"></a> `00ad7c6c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7c70"></a> `00ad7c70` | `e8 c2 00 39` | strb w8,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7c74"></a> `00ad7c74` | `61 6a 78 b8` | ldr w1,[x19, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7c78"></a> `00ad7c78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad7c7c"></a> `00ad7c7c` | `ff fa 00 39` | strb wzr,[x23, #0x3e] | `FALL_THROUGH`
<a id="insn-00ad7c80"></a> `00ad7c80` | `4e 1e f4 97` | bl 0x007df5b8 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7c84"></a> `00ad7c84` | `e0 00 00 36` | tbz w0,#0x0,0x00ad7ca0 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c88"></a> `00ad7c88` | `f4 02 c1 39` | ldrsb w20,[x23, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7c8c"></a> `00ad7c8c` | `f6 af f4 97` | bl 0x00803c64 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7c90"></a> `00ad7c90` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00ad7c94"></a> `00ad7c94` | `61 00 00 54` | b.ne 0x00ad7ca0 | `CONDITIONAL_JUMP`
<a id="insn-00ad7c98"></a> `00ad7c98` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7c9c"></a> `00ad7c9c` | `e8 fa 00 39` | strb w8,[x23, #0x3e] | `FALL_THROUGH`
<a id="insn-00ad7ca0"></a> `00ad7ca0` | `61 6a 78 b8` | ldr w1,[x19, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7ca4"></a> `00ad7ca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad7ca8"></a> `00ad7ca8` | `ff fe 00 39` | strb wzr,[x23, #0x3f] | `FALL_THROUGH`
<a id="insn-00ad7cac"></a> `00ad7cac` | `61 1e f4 97` | bl 0x007df630 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7cb0"></a> `00ad7cb0` | `e0 00 00 36` | tbz w0,#0x0,0x00ad7ccc | `CONDITIONAL_JUMP`
<a id="insn-00ad7cb4"></a> `00ad7cb4` | `f4 02 c1 39` | ldrsb w20,[x23, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7cb8"></a> `00ad7cb8` | `eb af f4 97` | bl 0x00803c64 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7cbc"></a> `00ad7cbc` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00ad7cc0"></a> `00ad7cc0` | `61 00 00 54` | b.ne 0x00ad7ccc | `CONDITIONAL_JUMP`
<a id="insn-00ad7cc4"></a> `00ad7cc4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7cc8"></a> `00ad7cc8` | `e8 fe 00 39` | strb w8,[x23, #0x3f] | `FALL_THROUGH`
<a id="insn-00ad7ccc"></a> `00ad7ccc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ad7cd0"></a> `00ad7cd0` | `91 af f4 97` | bl 0x00803b14 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7cd4"></a> `00ad7cd4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ad7cd8"></a> `00ad7cd8` | `e3 af f4 97` | bl 0x00803c64 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7cdc"></a> `00ad7cdc` | `08 7b 82 52` | mov w8,#0x13d8 | `FALL_THROUGH`
<a id="insn-00ad7ce0"></a> `00ad7ce0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00ad7ce4"></a> `00ad7ce4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7ce8"></a> `00ad7ce8` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00ad7cec"></a> `00ad7cec` | `94 7b ee 97` | bl 0x00676b3c | `UNCONDITIONAL_CALL`
<a id="insn-00ad7cf0"></a> `00ad7cf0` | `80 00 00 36` | tbz w0,#0x0,0x00ad7d00 | `CONDITIONAL_JUMP`
<a id="insn-00ad7cf4"></a> `00ad7cf4` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00ad7cf8"></a> `00ad7cf8` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-00ad7cfc"></a> `00ad7cfc` | `07 00 00 14` | b 0x00ad7d18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7d00"></a> `00ad7d00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad7d04"></a> `00ad7d04` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7d08"></a> `00ad7d08` | `ff 93 f3 97` | bl 0x007bcd04 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d0c"></a> `00ad7d0c` | `c0 12 00 36` | tbz w0,#0x0,0x00ad7f64 | `CONDITIONAL_JUMP`
<a id="insn-00ad7d10"></a> `00ad7d10` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00ad7d14"></a> `00ad7d14` | `81 08 80 52` | mov w1,#0x44 | `FALL_THROUGH`
<a id="insn-00ad7d18"></a> `00ad7d18` | `24 a5 f4 97` | bl 0x008011a8 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d1c"></a> `00ad7d1c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ad7d20"></a> `00ad7d20` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00ad7d24"></a> `00ad7d24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad7d28"></a> `00ad7d28` | `31 29 f6 97` | bl 0x008621ec | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d2c"></a> `00ad7d2c` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00ad7d30"></a> `00ad7d30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad7d34"></a> `00ad7d34` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ad7d38"></a> `00ad7d38` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00ad7d3c"></a> `00ad7d3c` | `f1 f7 ec 97` | bl 0x00615d00 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d40"></a> `00ad7d40` | `00 01 00 37` | tbnz w0,#0x0,0x00ad7d60 | `CONDITIONAL_JUMP`
<a id="insn-00ad7d44"></a> `00ad7d44` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7d48"></a> `00ad7d48` | `32 b2 f1 97` | bl 0x00744610 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d4c"></a> `00ad7d4c` | `a0 00 00 37` | tbnz w0,#0x0,0x00ad7d60 | `CONDITIONAL_JUMP`
<a id="insn-00ad7d50"></a> `00ad7d50` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ad7d54"></a> `00ad7d54` | `48 ae f4 97` | bl 0x00803674 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7d58"></a> `00ad7d58` | `1f 60 00 31` | cmn w0,#0x18 | `FALL_THROUGH`
<a id="insn-00ad7d5c"></a> `00ad7d5c` | `81 11 00 54` | b.ne 0x00ad7f8c | `CONDITIONAL_JUMP`
<a id="insn-00ad7d60"></a> `00ad7d60` | `68 1a 41 91` | add x8,x19,#0x46, LSL #12 | `FALL_THROUGH`
<a id="insn-00ad7d64"></a> `00ad7d64` | `96 2f 97 52` | mov w22,#0xb97c | `FALL_THROUGH`
<a id="insn-00ad7d68"></a> `00ad7d68` | `ff 7e 00 79` | strh wzr,[x23, #0x3e] | `FALL_THROUGH`
<a id="insn-00ad7d6c"></a> `00ad7d6c` | `09 b7 98 52` | mov w9,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00ad7d70"></a> `00ad7d70` | `ff c2 00 39` | strb wzr,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7d74"></a> `00ad7d74` | `17 45 3e 91` | add x23,x8,#0xf91 | `FALL_THROUGH`
<a id="insn-00ad7d78"></a> `00ad7d78` | `68 b7 98 52` | mov w8,#0xc5bb | `FALL_THROUGH`
<a id="insn-00ad7d7c"></a> `00ad7d7c` | `36 07 a0 72` | movk w22,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad7d80"></a> `00ad7d80` | `75 02 09 8b` | add x21,x19,x9 | `FALL_THROUGH`
<a id="insn-00ad7d84"></a> `00ad7d84` | `78 02 08 8b` | add x24,x19,x8 | `FALL_THROUGH`
<a id="insn-00ad7d88"></a> `00ad7d88` | `59 01 80 52` | mov w25,#0xa | `FALL_THROUGH`
<a id="insn-00ad7d8c"></a> `00ad7d8c` | `9a 05 80 52` | mov w26,#0x2c | `FALL_THROUGH`
<a id="insn-00ad7d90"></a> `00ad7d90` | `09 00 00 14` | b 0x00ad7db4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7d94"></a> `00ad7d94` | `61 6a 76 b8` | ldr w1,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7d98"></a> `00ad7d98` | `60 82 12 91` | add x0,x19,#0x4a0 | `FALL_THROUGH`
<a id="insn-00ad7d9c"></a> `00ad7d9c` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00ad7da0"></a> `00ad7da0` | `d0 a2 eb 97` | bl 0x005c08e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7da4"></a> `00ad7da4` | `c0 04 00 36` | tbz w0,#0x0,0x00ad7e3c | `CONDITIONAL_JUMP`
<a id="insn-00ad7da8"></a> `00ad7da8` | `39 07 00 f1` | subs x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7dac"></a> `00ad7dac` | `18 13 00 91` | add x24,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00ad7db0"></a> `00ad7db0` | `00 06 00 54` | b.eq 0x00ad7e70 | `CONDITIONAL_JUMP`
<a id="insn-00ad7db4"></a> `00ad7db4` | `68 6a b6 b8` | ldrsw x8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7db8"></a> `00ad7db8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ad7dbc"></a> `00ad7dbc` | `09 55 3a 9b` | smaddl x9,w8,w26,x21 | `FALL_THROUGH`
<a id="insn-00ad7dc0"></a> `00ad7dc0` | `08 61 3a 9b` | smaddl x8,w8,w26,x24 | `FALL_THROUGH`
<a id="insn-00ad7dc4"></a> `00ad7dc4` | `2b a9 40 39` | ldrb w11,[x9, #0x2a] | `FALL_THROUGH`
<a id="insn-00ad7dc8"></a> `00ad7dc8` | `2c ad 40 39` | ldrb w12,[x9, #0x2b] | `FALL_THROUGH`
<a id="insn-00ad7dcc"></a> `00ad7dcc` | `0a f1 5f 38` | ldurb w10,[x8, #-0x1] | `FALL_THROUGH`
<a id="insn-00ad7dd0"></a> `00ad7dd0` | `0d e1 5f 38` | ldurb w13,[x8, #-0x2] | `FALL_THROUGH`
<a id="insn-00ad7dd4"></a> `00ad7dd4` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00ad7dd8"></a> `00ad7dd8` | `0b 01 40 39` | ldrb w11,[x8] | `FALL_THROUGH`
<a id="insn-00ad7ddc"></a> `00ad7ddc` | `08 d1 5f 38` | ldurb w8,[x8, #-0x3] | `FALL_THROUGH`
<a id="insn-00ad7de0"></a> `00ad7de0` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00ad7de4"></a> `00ad7de4` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00ad7de8"></a> `00ad7de8` | `2c a5 40 39` | ldrb w12,[x9, #0x29] | `FALL_THROUGH`
<a id="insn-00ad7dec"></a> `00ad7dec` | `29 a1 40 39` | ldrb w9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00ad7df0"></a> `00ad7df0` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ad7df4"></a> `00ad7df4` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00ad7df8"></a> `00ad7df8` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00ad7dfc"></a> `00ad7dfc` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ad7e00"></a> `00ad7e00` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00ad7e04"></a> `00ad7e04` | `14 09 00 71` | subs w20,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00ad7e08"></a> `00ad7e08` | `ab 01 00 54` | b.lt 0x00ad7e3c | `CONDITIONAL_JUMP`
<a id="insn-00ad7e0c"></a> `00ad7e0c` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7e10"></a> `00ad7e10` | `00 b2 f1 97` | bl 0x00744610 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7e14"></a> `00ad7e14` | `00 fc 07 36` | tbz w0,#0x0,0x00ad7d94 | `CONDITIONAL_JUMP`
<a id="insn-00ad7e18"></a> `00ad7e18` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7e1c"></a> `00ad7e1c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ad7e20"></a> `00ad7e20` | `de b0 f1 97` | bl 0x00744198 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7e24"></a> `00ad7e24` | `20 fc 07 36` | tbz w0,#0x0,0x00ad7da8 | `CONDITIONAL_JUMP`
<a id="insn-00ad7e28"></a> `00ad7e28` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7e2c"></a> `00ad7e2c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ad7e30"></a> `00ad7e30` | `41 b1 f1 97` | bl 0x00744334 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7e34"></a> `00ad7e34` | `00 fb 07 36` | tbz w0,#0x0,0x00ad7d94 | `CONDITIONAL_JUMP`
<a id="insn-00ad7e38"></a> `00ad7e38` | `dc ff ff 17` | b 0x00ad7da8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7e3c"></a> `00ad7e3c` | `68 9a 73 b9` | ldr w8,[x19, #0x3398] | `FALL_THROUGH`
<a id="insn-00ad7e40"></a> `00ad7e40` | `08 79 1f 12` | and w8,w8,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00ad7e44"></a> `00ad7e44` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00ad7e48"></a> `00ad7e48` | `81 01 00 54` | b.ne 0x00ad7e78 | `CONDITIONAL_JUMP`
<a id="insn-00ad7e4c"></a> `00ad7e4c` | `14 69 8e 52` | mov w20,#0x7348 | `FALL_THROUGH`
<a id="insn-00ad7e50"></a> `00ad7e50` | `94 06 a0 72` | movk w20,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad7e54"></a> `00ad7e54` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00ad7e58"></a> `00ad7e58` | `88 ac fd 97` | bl 0x00a43078 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7e5c"></a> `00ad7e5c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00ad7e60"></a> `00ad7e60` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00ad7e64"></a> `00ad7e64` | `a8 ac fd 97` | bl 0x00a43104 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7e68"></a> `00ad7e68` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ad7e6c"></a> `00ad7e6c` | `04 00 00 14` | b 0x00ad7e7c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7e70"></a> `00ad7e70` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7e74"></a> `00ad7e74` | `49 00 00 14` | b 0x00ad7f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7e78"></a> `00ad7e78` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00ad7e7c"></a> `00ad7e7c` | `18 69 8e 52` | mov w24,#0x7348 | `FALL_THROUGH`
<a id="insn-00ad7e80"></a> `00ad7e80` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00ad7e84"></a> `00ad7e84` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00ad7e88"></a> `00ad7e88` | `98 06 a0 72` | movk w24,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ad7e8c"></a> `00ad7e8c` | `05 00 00 14` | b 0x00ad7ea0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7e90"></a> `00ad7e90` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad7e94"></a> `00ad7e94` | `39 13 00 91` | add x25,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00ad7e98"></a> `00ad7e98` | `bf e2 0d f1` | cmp x21,#0x378 | `FALL_THROUGH`
<a id="insn-00ad7e9c"></a> `00ad7e9c` | `00 06 00 54` | b.eq 0x00ad7f5c | `CONDITIONAL_JUMP`
<a id="insn-00ad7ea0"></a> `00ad7ea0` | `28 07 40 39` | ldrb w8,[x25, #0x1] | `FALL_THROUGH`
<a id="insn-00ad7ea4"></a> `00ad7ea4` | `e9 86 77 39` | ldrb w9,[x23, #0xde1] | `FALL_THROUGH`
<a id="insn-00ad7ea8"></a> `00ad7ea8` | `ea 8a 77 39` | ldrb w10,[x23, #0xde2] | `FALL_THROUGH`
<a id="insn-00ad7eac"></a> `00ad7eac` | `2b 03 40 39` | ldrb w11,[x25] | `FALL_THROUGH`
<a id="insn-00ad7eb0"></a> `00ad7eb0` | `ec 82 77 39` | ldrb w12,[x23, #0xde0] | `FALL_THROUGH`
<a id="insn-00ad7eb4"></a> `00ad7eb4` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00ad7eb8"></a> `00ad7eb8` | `29 0b 40 39` | ldrb w9,[x25, #0x2] | `FALL_THROUGH`
<a id="insn-00ad7ebc"></a> `00ad7ebc` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00ad7ec0"></a> `00ad7ec0` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00ad7ec4"></a> `00ad7ec4` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00ad7ec8"></a> `00ad7ec8` | `ea 7e 77 39` | ldrb w10,[x23, #0xddf] | `FALL_THROUGH`
<a id="insn-00ad7ecc"></a> `00ad7ecc` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ad7ed0"></a> `00ad7ed0` | `29 f3 5f 38` | ldurb w9,[x25, #-0x1] | `FALL_THROUGH`
<a id="insn-00ad7ed4"></a> `00ad7ed4` | `08 21 0b 2a` | orr w8,w8,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ad7ed8"></a> `00ad7ed8` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00ad7edc"></a> `00ad7edc` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00ad7ee0"></a> `00ad7ee0` | `88 fd ff 34` | cbz w8,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7ee4"></a> `00ad7ee4` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7ee8"></a> `00ad7ee8` | `ca b1 f1 97` | bl 0x00744610 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7eec"></a> `00ad7eec` | `20 01 00 36` | tbz w0,#0x0,0x00ad7f10 | `CONDITIONAL_JUMP`
<a id="insn-00ad7ef0"></a> `00ad7ef0` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7ef4"></a> `00ad7ef4` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00ad7ef8"></a> `00ad7ef8` | `a8 b0 f1 97` | bl 0x00744198 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7efc"></a> `00ad7efc` | `a0 fc 07 36` | tbz w0,#0x0,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f00"></a> `00ad7f00` | `60 82 2f 91` | add x0,x19,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ad7f04"></a> `00ad7f04` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00ad7f08"></a> `00ad7f08` | `0b b1 f1 97` | bl 0x00744334 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f0c"></a> `00ad7f0c` | `20 fc 07 37` | tbnz w0,#0x0,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f10"></a> `00ad7f10` | `60 62 0f 91` | add x0,x19,#0x3d8 | `FALL_THROUGH`
<a id="insn-00ad7f14"></a> `00ad7f14` | `f6 c9 00 94` | bl 0x00b0a6ec | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f18"></a> `00ad7f18` | `a0 00 00 36` | tbz w0,#0x0,0x00ad7f2c | `CONDITIONAL_JUMP`
<a id="insn-00ad7f1c"></a> `00ad7f1c` | `60 62 0f 91` | add x0,x19,#0x3d8 | `FALL_THROUGH`
<a id="insn-00ad7f20"></a> `00ad7f20` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00ad7f24"></a> `00ad7f24` | `a0 cf 00 94` | bl 0x00b0bda4 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f28"></a> `00ad7f28` | `40 fb 07 36` | tbz w0,#0x0,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f2c"></a> `00ad7f2c` | `61 6a 76 b8` | ldr w1,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad7f30"></a> `00ad7f30` | `60 82 12 91` | add x0,x19,#0x4a0 | `FALL_THROUGH`
<a id="insn-00ad7f34"></a> `00ad7f34` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00ad7f38"></a> `00ad7f38` | `6a a2 eb 97` | bl 0x005c08e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f3c"></a> `00ad7f3c` | `a0 fa 07 37` | tbnz w0,#0x0,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f40"></a> `00ad7f40` | `b4 00 00 36` | tbz w20,#0x0,0x00ad7f54 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f44"></a> `00ad7f44` | `60 02 18 8b` | add x0,x19,x24 | `FALL_THROUGH`
<a id="insn-00ad7f48"></a> `00ad7f48` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00ad7f4c"></a> `00ad7f4c` | `e8 ae fd 97` | bl 0x00a43aec | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f50"></a> `00ad7f50` | `00 fa 07 36` | tbz w0,#0x0,0x00ad7e90 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f54"></a> `00ad7f54` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00ad7f58"></a> `00ad7f58` | `10 00 00 14` | b 0x00ad7f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7f5c"></a> `00ad7f5c` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00ad7f60"></a> `00ad7f60` | `0e 00 00 14` | b 0x00ad7f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7f64"></a> `00ad7f64` | `60 c2 14 91` | add x0,x19,#0x530 | `FALL_THROUGH`
<a id="insn-00ad7f68"></a> `00ad7f68` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad7f6c"></a> `00ad7f6c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ad7f70"></a> `00ad7f70` | `b7 6e fd 97` | bl 0x00a33a4c | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f74"></a> `00ad7f74` | `80 ed 07 36` | tbz w0,#0x0,0x00ad7d24 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f78"></a> `00ad7f78` | `60 c2 14 91` | add x0,x19,#0x530 | `FALL_THROUGH`
<a id="insn-00ad7f7c"></a> `00ad7f7c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ad7f80"></a> `00ad7f80` | `d8 6f fd 97` | bl 0x00a33ee0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f84"></a> `00ad7f84` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ad7f88"></a> `00ad7f88` | `67 ff ff 17` | b 0x00ad7d24 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7f8c"></a> `00ad7f8c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ad7f90"></a> `00ad7f90` | `ff 7e 00 79` | strh wzr,[x23, #0x3e] | `FALL_THROUGH`
<a id="insn-00ad7f94"></a> `00ad7f94` | `ff c2 00 39` | strb wzr,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7f98"></a> `00ad7f98` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7f9c"></a> `00ad7f9c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7fa0"></a> `00ad7fa0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7fa4"></a> `00ad7fa4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7fa8"></a> `00ad7fa8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ad7fac"></a> `00ad7fac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad7aec`](#insn-00ad7aec) 範囲 `[['00ad7aec', '00ad7af3']]`
  - `FALL_THROUGH` [`00ad7af0`](#insn-00ad7af0) → [`00ad7af4`](#insn-00ad7af4)
- ブロック [`00ad7af4`](#insn-00ad7af4) 範囲 `[['00ad7af4', '00ad7b07']]`
  - `FALL_THROUGH` [`00ad7b04`](#insn-00ad7b04) → [`00ad7b08`](#insn-00ad7b08)
- ブロック [`00ad7b08`](#insn-00ad7b08) 範囲 `[['00ad7b08', '00ad7b1b']]`
  - `FALL_THROUGH` [`00ad7b18`](#insn-00ad7b18) → [`00ad7b1c`](#insn-00ad7b1c)
- ブロック [`00ad7b1c`](#insn-00ad7b1c) 範囲 `[['00ad7b1c', '00ad7b23']]`
  - `CONDITIONAL_JUMP` [`00ad7b20`](#insn-00ad7b20) → [`00ad7c74`](#insn-00ad7c74)
  - `FALL_THROUGH` [`00ad7b20`](#insn-00ad7b20) → [`00ad7b24`](#insn-00ad7b24)
- ブロック [`00ad7b24`](#insn-00ad7b24) 範囲 `[['00ad7b24', '00ad7b33']]`
  - `CONDITIONAL_JUMP` [`00ad7b30`](#insn-00ad7b30) → [`00ad7b48`](#insn-00ad7b48)
  - `FALL_THROUGH` [`00ad7b30`](#insn-00ad7b30) → [`00ad7b34`](#insn-00ad7b34)
- ブロック [`00ad7b34`](#insn-00ad7b34) 範囲 `[['00ad7b34', '00ad7b3b']]`
  - `UNCONDITIONAL_JUMP` [`00ad7b38`](#insn-00ad7b38) → [`00ad7b6c`](#insn-00ad7b6c)
- ブロック [`00ad7b3c`](#insn-00ad7b3c) 範囲 `[['00ad7b3c', '00ad7b43']]`
  - `FALL_THROUGH` [`00ad7b40`](#insn-00ad7b40) → [`00ad7b44`](#insn-00ad7b44)
- ブロック [`00ad7b44`](#insn-00ad7b44) 範囲 `[['00ad7b44', '00ad7b47']]`
  - `CONDITIONAL_JUMP` [`00ad7b44`](#insn-00ad7b44) → [`00ad7b6c`](#insn-00ad7b6c)
  - `FALL_THROUGH` [`00ad7b44`](#insn-00ad7b44) → [`00ad7b48`](#insn-00ad7b48)
- ブロック [`00ad7b48`](#insn-00ad7b48) 範囲 `[['00ad7b48', '00ad7b57']]`
  - `CONDITIONAL_JUMP` [`00ad7b54`](#insn-00ad7b54) → [`00ad7b3c`](#insn-00ad7b3c)
  - `FALL_THROUGH` [`00ad7b54`](#insn-00ad7b54) → [`00ad7b58`](#insn-00ad7b58)
- ブロック [`00ad7b58`](#insn-00ad7b58) 範囲 `[['00ad7b58', '00ad7b5b']]`
  - `FALL_THROUGH` [`00ad7b58`](#insn-00ad7b58) → [`00ad7b5c`](#insn-00ad7b5c)
- ブロック [`00ad7b5c`](#insn-00ad7b5c) 範囲 `[['00ad7b5c', '00ad7b5f']]`
  - `CONDITIONAL_JUMP` [`00ad7b5c`](#insn-00ad7b5c) → [`00ad7bc8`](#insn-00ad7bc8)
  - `FALL_THROUGH` [`00ad7b5c`](#insn-00ad7b5c) → [`00ad7b60`](#insn-00ad7b60)
- ブロック [`00ad7b60`](#insn-00ad7b60) 範囲 `[['00ad7b60', '00ad7b67']]`
  - `CONDITIONAL_JUMP` [`00ad7b64`](#insn-00ad7b64) → [`00ad7b48`](#insn-00ad7b48)
  - `FALL_THROUGH` [`00ad7b64`](#insn-00ad7b64) → [`00ad7b68`](#insn-00ad7b68)
- ブロック [`00ad7b68`](#insn-00ad7b68) 範囲 `[['00ad7b68', '00ad7b6b']]`
  - `FALL_THROUGH` [`00ad7b68`](#insn-00ad7b68) → [`00ad7b6c`](#insn-00ad7b6c)
- ブロック [`00ad7b6c`](#insn-00ad7b6c) 範囲 `[['00ad7b6c', '00ad7b6f']]`
  - `FALL_THROUGH` [`00ad7b6c`](#insn-00ad7b6c) → [`00ad7b70`](#insn-00ad7b70)
- ブロック [`00ad7b70`](#insn-00ad7b70) 範囲 `[['00ad7b70', '00ad7b8b']]`
  - `FALL_THROUGH` [`00ad7b88`](#insn-00ad7b88) → [`00ad7b8c`](#insn-00ad7b8c)
- ブロック [`00ad7b8c`](#insn-00ad7b8c) 範囲 `[['00ad7b8c', '00ad7b9b']]`
  - `FALL_THROUGH` [`00ad7b98`](#insn-00ad7b98) → [`00ad7b9c`](#insn-00ad7b9c)
- ブロック [`00ad7b9c`](#insn-00ad7b9c) 範囲 `[['00ad7b9c', '00ad7bab']]`
  - `CONDITIONAL_JUMP` [`00ad7ba8`](#insn-00ad7ba8) → [`00ad7bb4`](#insn-00ad7bb4)
  - `FALL_THROUGH` [`00ad7ba8`](#insn-00ad7ba8) → [`00ad7bac`](#insn-00ad7bac)
- ブロック [`00ad7bac`](#insn-00ad7bac) 範囲 `[['00ad7bac', '00ad7baf']]`
  - `FALL_THROUGH` [`00ad7bac`](#insn-00ad7bac) → [`00ad7bb0`](#insn-00ad7bb0)
- ブロック [`00ad7bb0`](#insn-00ad7bb0) 範囲 `[['00ad7bb0', '00ad7bb3']]`
  - `FALL_THROUGH` [`00ad7bb0`](#insn-00ad7bb0) → [`00ad7bb4`](#insn-00ad7bb4)
- ブロック [`00ad7bb4`](#insn-00ad7bb4) 範囲 `[['00ad7bb4', '00ad7bc3']]`
  - `FALL_THROUGH` [`00ad7bc0`](#insn-00ad7bc0) → [`00ad7bc4`](#insn-00ad7bc4)
- ブロック [`00ad7bc4`](#insn-00ad7bc4) 範囲 `[['00ad7bc4', '00ad7bc7']]`
  - `FALL_THROUGH` [`00ad7bc4`](#insn-00ad7bc4) → [`00ad7bc8`](#insn-00ad7bc8)
- ブロック [`00ad7bc8`](#insn-00ad7bc8) 範囲 `[['00ad7bc8', '00ad7bdb']]`
  - `CONDITIONAL_JUMP` [`00ad7bd8`](#insn-00ad7bd8) → [`00ad7bf0`](#insn-00ad7bf0)
  - `FALL_THROUGH` [`00ad7bd8`](#insn-00ad7bd8) → [`00ad7bdc`](#insn-00ad7bdc)
- ブロック [`00ad7bdc`](#insn-00ad7bdc) 範囲 `[['00ad7bdc', '00ad7be3']]`
  - `UNCONDITIONAL_JUMP` [`00ad7be0`](#insn-00ad7be0) → [`00ad7c14`](#insn-00ad7c14)
- ブロック [`00ad7be4`](#insn-00ad7be4) 範囲 `[['00ad7be4', '00ad7bef']]`
  - `CONDITIONAL_JUMP` [`00ad7bec`](#insn-00ad7bec) → [`00ad7c14`](#insn-00ad7c14)
  - `FALL_THROUGH` [`00ad7bec`](#insn-00ad7bec) → [`00ad7bf0`](#insn-00ad7bf0)
- ブロック [`00ad7bf0`](#insn-00ad7bf0) 範囲 `[['00ad7bf0', '00ad7bf3']]`
  - `FALL_THROUGH` [`00ad7bf0`](#insn-00ad7bf0) → [`00ad7bf4`](#insn-00ad7bf4)
- ブロック [`00ad7bf4`](#insn-00ad7bf4) 範囲 `[['00ad7bf4', '00ad7bff']]`
  - `CONDITIONAL_JUMP` [`00ad7bfc`](#insn-00ad7bfc) → [`00ad7be4`](#insn-00ad7be4)
  - `FALL_THROUGH` [`00ad7bfc`](#insn-00ad7bfc) → [`00ad7c00`](#insn-00ad7c00)
- ブロック [`00ad7c00`](#insn-00ad7c00) 範囲 `[['00ad7c00', '00ad7c07']]`
  - `CONDITIONAL_JUMP` [`00ad7c04`](#insn-00ad7c04) → [`00ad7c64`](#insn-00ad7c64)
  - `FALL_THROUGH` [`00ad7c04`](#insn-00ad7c04) → [`00ad7c08`](#insn-00ad7c08)
- ブロック [`00ad7c08`](#insn-00ad7c08) 範囲 `[['00ad7c08', '00ad7c0f']]`
  - `CONDITIONAL_JUMP` [`00ad7c0c`](#insn-00ad7c0c) → [`00ad7bf0`](#insn-00ad7bf0)
  - `FALL_THROUGH` [`00ad7c0c`](#insn-00ad7c0c) → [`00ad7c10`](#insn-00ad7c10)
- ブロック [`00ad7c10`](#insn-00ad7c10) 範囲 `[['00ad7c10', '00ad7c13']]`
  - `FALL_THROUGH` [`00ad7c10`](#insn-00ad7c10) → [`00ad7c14`](#insn-00ad7c14)
- ブロック [`00ad7c14`](#insn-00ad7c14) 範囲 `[['00ad7c14', '00ad7c1f']]`
  - `FALL_THROUGH` [`00ad7c1c`](#insn-00ad7c1c) → [`00ad7c20`](#insn-00ad7c20)
- ブロック [`00ad7c20`](#insn-00ad7c20) 範囲 `[['00ad7c20', '00ad7c37']]`
  - `FALL_THROUGH` [`00ad7c34`](#insn-00ad7c34) → [`00ad7c38`](#insn-00ad7c38)
- ブロック [`00ad7c38`](#insn-00ad7c38) 範囲 `[['00ad7c38', '00ad7c47']]`
  - `CONDITIONAL_JUMP` [`00ad7c44`](#insn-00ad7c44) → [`00ad7c50`](#insn-00ad7c50)
  - `FALL_THROUGH` [`00ad7c44`](#insn-00ad7c44) → [`00ad7c48`](#insn-00ad7c48)
- ブロック [`00ad7c48`](#insn-00ad7c48) 範囲 `[['00ad7c48', '00ad7c4b']]`
  - `FALL_THROUGH` [`00ad7c48`](#insn-00ad7c48) → [`00ad7c4c`](#insn-00ad7c4c)
- ブロック [`00ad7c4c`](#insn-00ad7c4c) 範囲 `[['00ad7c4c', '00ad7c4f']]`
  - `FALL_THROUGH` [`00ad7c4c`](#insn-00ad7c4c) → [`00ad7c50`](#insn-00ad7c50)
- ブロック [`00ad7c50`](#insn-00ad7c50) 範囲 `[['00ad7c50', '00ad7c63']]`
  - `FALL_THROUGH` [`00ad7c60`](#insn-00ad7c60) → [`00ad7c64`](#insn-00ad7c64)
- ブロック [`00ad7c64`](#insn-00ad7c64) 範囲 `[['00ad7c64', '00ad7c6b']]`
  - `CONDITIONAL_JUMP` [`00ad7c68`](#insn-00ad7c68) → [`00ad7c74`](#insn-00ad7c74)
  - `FALL_THROUGH` [`00ad7c68`](#insn-00ad7c68) → [`00ad7c6c`](#insn-00ad7c6c)
- ブロック [`00ad7c6c`](#insn-00ad7c6c) 範囲 `[['00ad7c6c', '00ad7c73']]`
  - `FALL_THROUGH` [`00ad7c70`](#insn-00ad7c70) → [`00ad7c74`](#insn-00ad7c74)
- ブロック [`00ad7c74`](#insn-00ad7c74) 範囲 `[['00ad7c74', '00ad7c7b']]`
  - `FALL_THROUGH` [`00ad7c78`](#insn-00ad7c78) → [`00ad7c7c`](#insn-00ad7c7c)
- ブロック [`00ad7c7c`](#insn-00ad7c7c) 範囲 `[['00ad7c7c', '00ad7c87']]`
  - `CONDITIONAL_JUMP` [`00ad7c84`](#insn-00ad7c84) → [`00ad7ca0`](#insn-00ad7ca0)
  - `FALL_THROUGH` [`00ad7c84`](#insn-00ad7c84) → [`00ad7c88`](#insn-00ad7c88)
- ブロック [`00ad7c88`](#insn-00ad7c88) 範囲 `[['00ad7c88', '00ad7c8f']]`
  - `FALL_THROUGH` [`00ad7c8c`](#insn-00ad7c8c) → [`00ad7c90`](#insn-00ad7c90)
- ブロック [`00ad7c90`](#insn-00ad7c90) 範囲 `[['00ad7c90', '00ad7c97']]`
  - `CONDITIONAL_JUMP` [`00ad7c94`](#insn-00ad7c94) → [`00ad7ca0`](#insn-00ad7ca0)
  - `FALL_THROUGH` [`00ad7c94`](#insn-00ad7c94) → [`00ad7c98`](#insn-00ad7c98)
- ブロック [`00ad7c98`](#insn-00ad7c98) 範囲 `[['00ad7c98', '00ad7c9f']]`
  - `FALL_THROUGH` [`00ad7c9c`](#insn-00ad7c9c) → [`00ad7ca0`](#insn-00ad7ca0)
- ブロック [`00ad7ca0`](#insn-00ad7ca0) 範囲 `[['00ad7ca0', '00ad7ca7']]`
  - `FALL_THROUGH` [`00ad7ca4`](#insn-00ad7ca4) → [`00ad7ca8`](#insn-00ad7ca8)
- ブロック [`00ad7ca8`](#insn-00ad7ca8) 範囲 `[['00ad7ca8', '00ad7cb3']]`
  - `CONDITIONAL_JUMP` [`00ad7cb0`](#insn-00ad7cb0) → [`00ad7ccc`](#insn-00ad7ccc)
  - `FALL_THROUGH` [`00ad7cb0`](#insn-00ad7cb0) → [`00ad7cb4`](#insn-00ad7cb4)
- ブロック [`00ad7cb4`](#insn-00ad7cb4) 範囲 `[['00ad7cb4', '00ad7cb7']]`
  - `FALL_THROUGH` [`00ad7cb4`](#insn-00ad7cb4) → [`00ad7cb8`](#insn-00ad7cb8)
- ブロック [`00ad7cb8`](#insn-00ad7cb8) 範囲 `[['00ad7cb8', '00ad7cc3']]`
  - `CONDITIONAL_JUMP` [`00ad7cc0`](#insn-00ad7cc0) → [`00ad7ccc`](#insn-00ad7ccc)
  - `FALL_THROUGH` [`00ad7cc0`](#insn-00ad7cc0) → [`00ad7cc4`](#insn-00ad7cc4)
- ブロック [`00ad7cc4`](#insn-00ad7cc4) 範囲 `[['00ad7cc4', '00ad7ccb']]`
  - `FALL_THROUGH` [`00ad7cc8`](#insn-00ad7cc8) → [`00ad7ccc`](#insn-00ad7ccc)
- ブロック [`00ad7ccc`](#insn-00ad7ccc) 範囲 `[['00ad7ccc', '00ad7ccf']]`
  - `FALL_THROUGH` [`00ad7ccc`](#insn-00ad7ccc) → [`00ad7cd0`](#insn-00ad7cd0)
- ブロック [`00ad7cd0`](#insn-00ad7cd0) 範囲 `[['00ad7cd0', '00ad7ce3']]`
  - `FALL_THROUGH` [`00ad7ce0`](#insn-00ad7ce0) → [`00ad7ce4`](#insn-00ad7ce4)
- ブロック [`00ad7ce4`](#insn-00ad7ce4) 範囲 `[['00ad7ce4', '00ad7cf3']]`
  - `CONDITIONAL_JUMP` [`00ad7cf0`](#insn-00ad7cf0) → [`00ad7d00`](#insn-00ad7d00)
  - `FALL_THROUGH` [`00ad7cf0`](#insn-00ad7cf0) → [`00ad7cf4`](#insn-00ad7cf4)
- ブロック [`00ad7cf4`](#insn-00ad7cf4) 範囲 `[['00ad7cf4', '00ad7cfb']]`
  - `FALL_THROUGH` [`00ad7cf8`](#insn-00ad7cf8) → [`00ad7cfc`](#insn-00ad7cfc)
- ブロック [`00ad7cfc`](#insn-00ad7cfc) 範囲 `[['00ad7cfc', '00ad7cff']]`
  - `UNCONDITIONAL_JUMP` [`00ad7cfc`](#insn-00ad7cfc) → [`00ad7d18`](#insn-00ad7d18)
- ブロック [`00ad7d00`](#insn-00ad7d00) 範囲 `[['00ad7d00', '00ad7d0b']]`
  - `FALL_THROUGH` [`00ad7d08`](#insn-00ad7d08) → [`00ad7d0c`](#insn-00ad7d0c)
- ブロック [`00ad7d0c`](#insn-00ad7d0c) 範囲 `[['00ad7d0c', '00ad7d0f']]`
  - `CONDITIONAL_JUMP` [`00ad7d0c`](#insn-00ad7d0c) → [`00ad7f64`](#insn-00ad7f64)
  - `FALL_THROUGH` [`00ad7d0c`](#insn-00ad7d0c) → [`00ad7d10`](#insn-00ad7d10)
- ブロック [`00ad7d10`](#insn-00ad7d10) 範囲 `[['00ad7d10', '00ad7d17']]`
  - `FALL_THROUGH` [`00ad7d14`](#insn-00ad7d14) → [`00ad7d18`](#insn-00ad7d18)
- ブロック [`00ad7d18`](#insn-00ad7d18) 範囲 `[['00ad7d18', '00ad7d23']]`
  - `FALL_THROUGH` [`00ad7d20`](#insn-00ad7d20) → [`00ad7d24`](#insn-00ad7d24)
- ブロック [`00ad7d24`](#insn-00ad7d24) 範囲 `[['00ad7d24', '00ad7d37']]`
  - `FALL_THROUGH` [`00ad7d34`](#insn-00ad7d34) → [`00ad7d38`](#insn-00ad7d38)
- ブロック [`00ad7d38`](#insn-00ad7d38) 範囲 `[['00ad7d38', '00ad7d43']]`
  - `CONDITIONAL_JUMP` [`00ad7d40`](#insn-00ad7d40) → [`00ad7d60`](#insn-00ad7d60)
  - `FALL_THROUGH` [`00ad7d40`](#insn-00ad7d40) → [`00ad7d44`](#insn-00ad7d44)
- ブロック [`00ad7d44`](#insn-00ad7d44) 範囲 `[['00ad7d44', '00ad7d4f']]`
  - `CONDITIONAL_JUMP` [`00ad7d4c`](#insn-00ad7d4c) → [`00ad7d60`](#insn-00ad7d60)
  - `FALL_THROUGH` [`00ad7d4c`](#insn-00ad7d4c) → [`00ad7d50`](#insn-00ad7d50)
- ブロック [`00ad7d50`](#insn-00ad7d50) 範囲 `[['00ad7d50', '00ad7d5f']]`
  - `CONDITIONAL_JUMP` [`00ad7d5c`](#insn-00ad7d5c) → [`00ad7f8c`](#insn-00ad7f8c)
  - `FALL_THROUGH` [`00ad7d5c`](#insn-00ad7d5c) → [`00ad7d60`](#insn-00ad7d60)
- ブロック [`00ad7d60`](#insn-00ad7d60) 範囲 `[['00ad7d60', '00ad7d6b']]`
  - `FALL_THROUGH` [`00ad7d68`](#insn-00ad7d68) → [`00ad7d6c`](#insn-00ad7d6c)
- ブロック [`00ad7d6c`](#insn-00ad7d6c) 範囲 `[['00ad7d6c', '00ad7d73']]`
  - `FALL_THROUGH` [`00ad7d70`](#insn-00ad7d70) → [`00ad7d74`](#insn-00ad7d74)
- ブロック [`00ad7d74`](#insn-00ad7d74) 範囲 `[['00ad7d74', '00ad7d93']]`
  - `UNCONDITIONAL_JUMP` [`00ad7d90`](#insn-00ad7d90) → [`00ad7db4`](#insn-00ad7db4)
- ブロック [`00ad7d94`](#insn-00ad7d94) 範囲 `[['00ad7d94', '00ad7da7']]`
  - `CONDITIONAL_JUMP` [`00ad7da4`](#insn-00ad7da4) → [`00ad7e3c`](#insn-00ad7e3c)
  - `FALL_THROUGH` [`00ad7da4`](#insn-00ad7da4) → [`00ad7da8`](#insn-00ad7da8)
- ブロック [`00ad7da8`](#insn-00ad7da8) 範囲 `[['00ad7da8', '00ad7db3']]`
  - `CONDITIONAL_JUMP` [`00ad7db0`](#insn-00ad7db0) → [`00ad7e70`](#insn-00ad7e70)
  - `FALL_THROUGH` [`00ad7db0`](#insn-00ad7db0) → [`00ad7db4`](#insn-00ad7db4)
- ブロック [`00ad7db4`](#insn-00ad7db4) 範囲 `[['00ad7db4', '00ad7e0b']]`
  - `CONDITIONAL_JUMP` [`00ad7e08`](#insn-00ad7e08) → [`00ad7e3c`](#insn-00ad7e3c)
  - `FALL_THROUGH` [`00ad7e08`](#insn-00ad7e08) → [`00ad7e0c`](#insn-00ad7e0c)
- ブロック [`00ad7e0c`](#insn-00ad7e0c) 範囲 `[['00ad7e0c', '00ad7e0f']]`
  - `FALL_THROUGH` [`00ad7e0c`](#insn-00ad7e0c) → [`00ad7e10`](#insn-00ad7e10)
- ブロック [`00ad7e10`](#insn-00ad7e10) 範囲 `[['00ad7e10', '00ad7e17']]`
  - `CONDITIONAL_JUMP` [`00ad7e14`](#insn-00ad7e14) → [`00ad7d94`](#insn-00ad7d94)
  - `FALL_THROUGH` [`00ad7e14`](#insn-00ad7e14) → [`00ad7e18`](#insn-00ad7e18)
- ブロック [`00ad7e18`](#insn-00ad7e18) 範囲 `[['00ad7e18', '00ad7e1b']]`
  - `FALL_THROUGH` [`00ad7e18`](#insn-00ad7e18) → [`00ad7e1c`](#insn-00ad7e1c)
- ブロック [`00ad7e1c`](#insn-00ad7e1c) 範囲 `[['00ad7e1c', '00ad7e27']]`
  - `CONDITIONAL_JUMP` [`00ad7e24`](#insn-00ad7e24) → [`00ad7da8`](#insn-00ad7da8)
  - `FALL_THROUGH` [`00ad7e24`](#insn-00ad7e24) → [`00ad7e28`](#insn-00ad7e28)
- ブロック [`00ad7e28`](#insn-00ad7e28) 範囲 `[['00ad7e28', '00ad7e37']]`
  - `CONDITIONAL_JUMP` [`00ad7e34`](#insn-00ad7e34) → [`00ad7d94`](#insn-00ad7d94)
  - `FALL_THROUGH` [`00ad7e34`](#insn-00ad7e34) → [`00ad7e38`](#insn-00ad7e38)
- ブロック [`00ad7e38`](#insn-00ad7e38) 範囲 `[['00ad7e38', '00ad7e3b']]`
  - `UNCONDITIONAL_JUMP` [`00ad7e38`](#insn-00ad7e38) → [`00ad7da8`](#insn-00ad7da8)
- ブロック [`00ad7e3c`](#insn-00ad7e3c) 範囲 `[['00ad7e3c', '00ad7e43']]`
  - `FALL_THROUGH` [`00ad7e40`](#insn-00ad7e40) → [`00ad7e44`](#insn-00ad7e44)
- ブロック [`00ad7e44`](#insn-00ad7e44) 範囲 `[['00ad7e44', '00ad7e4b']]`
  - `CONDITIONAL_JUMP` [`00ad7e48`](#insn-00ad7e48) → [`00ad7e78`](#insn-00ad7e78)
  - `FALL_THROUGH` [`00ad7e48`](#insn-00ad7e48) → [`00ad7e4c`](#insn-00ad7e4c)
- ブロック [`00ad7e4c`](#insn-00ad7e4c) 範囲 `[['00ad7e4c', '00ad7e63']]`
  - `FALL_THROUGH` [`00ad7e60`](#insn-00ad7e60) → [`00ad7e64`](#insn-00ad7e64)
- ブロック [`00ad7e64`](#insn-00ad7e64) 範囲 `[['00ad7e64', '00ad7e6f']]`
  - `UNCONDITIONAL_JUMP` [`00ad7e6c`](#insn-00ad7e6c) → [`00ad7e7c`](#insn-00ad7e7c)
- ブロック [`00ad7e70`](#insn-00ad7e70) 範囲 `[['00ad7e70', '00ad7e77']]`
  - `UNCONDITIONAL_JUMP` [`00ad7e74`](#insn-00ad7e74) → [`00ad7f98`](#insn-00ad7f98)
- ブロック [`00ad7e78`](#insn-00ad7e78) 範囲 `[['00ad7e78', '00ad7e7b']]`
  - `FALL_THROUGH` [`00ad7e78`](#insn-00ad7e78) → [`00ad7e7c`](#insn-00ad7e7c)
- ブロック [`00ad7e7c`](#insn-00ad7e7c) 範囲 `[['00ad7e7c', '00ad7e8b']]`
  - `FALL_THROUGH` [`00ad7e88`](#insn-00ad7e88) → [`00ad7e8c`](#insn-00ad7e8c)
- ブロック [`00ad7e8c`](#insn-00ad7e8c) 範囲 `[['00ad7e8c', '00ad7e8f']]`
  - `UNCONDITIONAL_JUMP` [`00ad7e8c`](#insn-00ad7e8c) → [`00ad7ea0`](#insn-00ad7ea0)
- ブロック [`00ad7e90`](#insn-00ad7e90) 範囲 `[['00ad7e90', '00ad7e9f']]`
  - `CONDITIONAL_JUMP` [`00ad7e9c`](#insn-00ad7e9c) → [`00ad7f5c`](#insn-00ad7f5c)
  - `FALL_THROUGH` [`00ad7e9c`](#insn-00ad7e9c) → [`00ad7ea0`](#insn-00ad7ea0)
- ブロック [`00ad7ea0`](#insn-00ad7ea0) 範囲 `[['00ad7ea0', '00ad7eab']]`
  - `FALL_THROUGH` [`00ad7ea8`](#insn-00ad7ea8) → [`00ad7eac`](#insn-00ad7eac)
- ブロック [`00ad7eac`](#insn-00ad7eac) 範囲 `[['00ad7eac', '00ad7ebb']]`
  - `FALL_THROUGH` [`00ad7eb8`](#insn-00ad7eb8) → [`00ad7ebc`](#insn-00ad7ebc)
- ブロック [`00ad7ebc`](#insn-00ad7ebc) 範囲 `[['00ad7ebc', '00ad7ed3']]`
  - `FALL_THROUGH` [`00ad7ed0`](#insn-00ad7ed0) → [`00ad7ed4`](#insn-00ad7ed4)
- ブロック [`00ad7ed4`](#insn-00ad7ed4) 範囲 `[['00ad7ed4', '00ad7ee3']]`
  - `CONDITIONAL_JUMP` [`00ad7ee0`](#insn-00ad7ee0) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7ee0`](#insn-00ad7ee0) → [`00ad7ee4`](#insn-00ad7ee4)
- ブロック [`00ad7ee4`](#insn-00ad7ee4) 範囲 `[['00ad7ee4', '00ad7ee7']]`
  - `FALL_THROUGH` [`00ad7ee4`](#insn-00ad7ee4) → [`00ad7ee8`](#insn-00ad7ee8)
- ブロック [`00ad7ee8`](#insn-00ad7ee8) 範囲 `[['00ad7ee8', '00ad7eef']]`
  - `CONDITIONAL_JUMP` [`00ad7eec`](#insn-00ad7eec) → [`00ad7f10`](#insn-00ad7f10)
  - `FALL_THROUGH` [`00ad7eec`](#insn-00ad7eec) → [`00ad7ef0`](#insn-00ad7ef0)
- ブロック [`00ad7ef0`](#insn-00ad7ef0) 範囲 `[['00ad7ef0', '00ad7eff']]`
  - `CONDITIONAL_JUMP` [`00ad7efc`](#insn-00ad7efc) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7efc`](#insn-00ad7efc) → [`00ad7f00`](#insn-00ad7f00)
- ブロック [`00ad7f00`](#insn-00ad7f00) 範囲 `[['00ad7f00', '00ad7f03']]`
  - `FALL_THROUGH` [`00ad7f00`](#insn-00ad7f00) → [`00ad7f04`](#insn-00ad7f04)
- ブロック [`00ad7f04`](#insn-00ad7f04) 範囲 `[['00ad7f04', '00ad7f0f']]`
  - `CONDITIONAL_JUMP` [`00ad7f0c`](#insn-00ad7f0c) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7f0c`](#insn-00ad7f0c) → [`00ad7f10`](#insn-00ad7f10)
- ブロック [`00ad7f10`](#insn-00ad7f10) 範囲 `[['00ad7f10', '00ad7f13']]`
  - `FALL_THROUGH` [`00ad7f10`](#insn-00ad7f10) → [`00ad7f14`](#insn-00ad7f14)
- ブロック [`00ad7f14`](#insn-00ad7f14) 範囲 `[['00ad7f14', '00ad7f1b']]`
  - `CONDITIONAL_JUMP` [`00ad7f18`](#insn-00ad7f18) → [`00ad7f2c`](#insn-00ad7f2c)
  - `FALL_THROUGH` [`00ad7f18`](#insn-00ad7f18) → [`00ad7f1c`](#insn-00ad7f1c)
- ブロック [`00ad7f1c`](#insn-00ad7f1c) 範囲 `[['00ad7f1c', '00ad7f27']]`
  - `FALL_THROUGH` [`00ad7f24`](#insn-00ad7f24) → [`00ad7f28`](#insn-00ad7f28)
- ブロック [`00ad7f28`](#insn-00ad7f28) 範囲 `[['00ad7f28', '00ad7f2b']]`
  - `CONDITIONAL_JUMP` [`00ad7f28`](#insn-00ad7f28) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7f28`](#insn-00ad7f28) → [`00ad7f2c`](#insn-00ad7f2c)
- ブロック [`00ad7f2c`](#insn-00ad7f2c) 範囲 `[['00ad7f2c', '00ad7f3b']]`
  - `FALL_THROUGH` [`00ad7f38`](#insn-00ad7f38) → [`00ad7f3c`](#insn-00ad7f3c)
- ブロック [`00ad7f3c`](#insn-00ad7f3c) 範囲 `[['00ad7f3c', '00ad7f3f']]`
  - `CONDITIONAL_JUMP` [`00ad7f3c`](#insn-00ad7f3c) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7f3c`](#insn-00ad7f3c) → [`00ad7f40`](#insn-00ad7f40)
- ブロック [`00ad7f40`](#insn-00ad7f40) 範囲 `[['00ad7f40', '00ad7f43']]`
  - `CONDITIONAL_JUMP` [`00ad7f40`](#insn-00ad7f40) → [`00ad7f54`](#insn-00ad7f54)
  - `FALL_THROUGH` [`00ad7f40`](#insn-00ad7f40) → [`00ad7f44`](#insn-00ad7f44)
- ブロック [`00ad7f44`](#insn-00ad7f44) 範囲 `[['00ad7f44', '00ad7f53']]`
  - `CONDITIONAL_JUMP` [`00ad7f50`](#insn-00ad7f50) → [`00ad7e90`](#insn-00ad7e90)
  - `FALL_THROUGH` [`00ad7f50`](#insn-00ad7f50) → [`00ad7f54`](#insn-00ad7f54)
- ブロック [`00ad7f54`](#insn-00ad7f54) 範囲 `[['00ad7f54', '00ad7f5b']]`
  - `UNCONDITIONAL_JUMP` [`00ad7f58`](#insn-00ad7f58) → [`00ad7f98`](#insn-00ad7f98)
- ブロック [`00ad7f5c`](#insn-00ad7f5c) 範囲 `[['00ad7f5c', '00ad7f63']]`
  - `UNCONDITIONAL_JUMP` [`00ad7f60`](#insn-00ad7f60) → [`00ad7f98`](#insn-00ad7f98)
- ブロック [`00ad7f64`](#insn-00ad7f64) 範囲 `[['00ad7f64', '00ad7f6b']]`
  - `FALL_THROUGH` [`00ad7f68`](#insn-00ad7f68) → [`00ad7f6c`](#insn-00ad7f6c)
- ブロック [`00ad7f6c`](#insn-00ad7f6c) 範囲 `[['00ad7f6c', '00ad7f77']]`
  - `CONDITIONAL_JUMP` [`00ad7f74`](#insn-00ad7f74) → [`00ad7d24`](#insn-00ad7d24)
  - `FALL_THROUGH` [`00ad7f74`](#insn-00ad7f74) → [`00ad7f78`](#insn-00ad7f78)
- ブロック [`00ad7f78`](#insn-00ad7f78) 範囲 `[['00ad7f78', '00ad7f83']]`
  - `FALL_THROUGH` [`00ad7f80`](#insn-00ad7f80) → [`00ad7f84`](#insn-00ad7f84)
- ブロック [`00ad7f84`](#insn-00ad7f84) 範囲 `[['00ad7f84', '00ad7f8b']]`
  - `UNCONDITIONAL_JUMP` [`00ad7f88`](#insn-00ad7f88) → [`00ad7d24`](#insn-00ad7d24)
- ブロック [`00ad7f8c`](#insn-00ad7f8c) 範囲 `[['00ad7f8c', '00ad7f97']]`
  - `FALL_THROUGH` [`00ad7f94`](#insn-00ad7f94) → [`00ad7f98`](#insn-00ad7f98)
- ブロック [`00ad7f98`](#insn-00ad7f98) 範囲 `[['00ad7f98', '00ad7faf']]`

## 命令位置別の参照

- [`00ad7aec`](#insn-00ad7aec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7af0`](#insn-00ad7af0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7af4`](#insn-00ad7af4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7af8`](#insn-00ad7af8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7afc`](#insn-00ad7afc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b18`](#insn-00ad7b18) → `003380e9`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7b1c`](#insn-00ad7b1c) → `003380e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7b20`](#insn-00ad7b20) → [`00ad7c74`](#insn-00ad7c74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b28`](#insn-00ad7b28) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7b2c`](#insn-00ad7b2c) → `003380c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7b30`](#insn-00ad7b30) → [`00ad7b48`](#insn-00ad7b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b38`](#insn-00ad7b38) → [`00ad7b6c`](#insn-00ad7b6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b44`](#insn-00ad7b44) → [`00ad7b6c`](#insn-00ad7b6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b54`](#insn-00ad7b54) → [`00ad7b3c`](#insn-00ad7b3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b5c`](#insn-00ad7b5c) → [`00ad7bc8`](#insn-00ad7bc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b64`](#insn-00ad7b64) → [`00ad7b48`](#insn-00ad7b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b74`](#insn-00ad7b74) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00ad7b98`](#insn-00ad7b98) → `003380c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7b9c`](#insn-00ad7b9c) → `003380b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7ba8`](#insn-00ad7ba8) → [`00ad7bb4`](#insn-00ad7bb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7bac`](#insn-00ad7bac) → `003380b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7bb0`](#insn-00ad7bb0) → `003380c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7bb4`](#insn-00ad7bb4) → `003380c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7bb8`](#insn-00ad7bb8) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00ad7bbc`](#insn-00ad7bbc) → `003380c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7bc4`](#insn-00ad7bc4) → `003380c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7bc8`](#insn-00ad7bc8) → [`00803c64`](../00803/00803c64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803c64` · 推定シンボル `None` · 推定型 `None`
- [`00ad7bd8`](#insn-00ad7bd8) → [`00ad7bf0`](#insn-00ad7bf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7be0`](#insn-00ad7be0) → [`00ad7c14`](#insn-00ad7c14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7bec`](#insn-00ad7bec) → [`00ad7c14`](#insn-00ad7c14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7bfc`](#insn-00ad7bfc) → [`00ad7be4`](#insn-00ad7be4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c04`](#insn-00ad7c04) → [`00ad7c64`](#insn-00ad7c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c0c`](#insn-00ad7c0c) → [`00ad7bf0`](#insn-00ad7bf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c1c`](#insn-00ad7c1c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c44`](#insn-00ad7c44) → [`00ad7c50`](#insn-00ad7c50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c54`](#insn-00ad7c54) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c68`](#insn-00ad7c68) → [`00ad7c74`](#insn-00ad7c74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c70`](#insn-00ad7c70) → `003380e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7c74`](#insn-00ad7c74) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7c7c`](#insn-00ad7c7c) → `003380f6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7c80`](#insn-00ad7c80) → [`007df5b8`](../007df/007df5b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007df5b8` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c84`](#insn-00ad7c84) → [`00ad7ca0`](#insn-00ad7ca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c88`](#insn-00ad7c88) → `003380f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7c8c`](#insn-00ad7c8c) → [`00803c64`](../00803/00803c64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803c64` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c94`](#insn-00ad7c94) → [`00ad7ca0`](#insn-00ad7ca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7c9c`](#insn-00ad7c9c) → `003380f6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7ca0`](#insn-00ad7ca0) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7ca8`](#insn-00ad7ca8) → `003380f7`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7cac`](#insn-00ad7cac) → [`007df630`](../007df/007df630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007df630` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cb0`](#insn-00ad7cb0) → [`00ad7ccc`](#insn-00ad7ccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cb4`](#insn-00ad7cb4) → `003380f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7cb8`](#insn-00ad7cb8) → [`00803c64`](../00803/00803c64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803c64` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cc0`](#insn-00ad7cc0) → [`00ad7ccc`](#insn-00ad7ccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cc8`](#insn-00ad7cc8) → `003380f7`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7cd0`](#insn-00ad7cd0) → [`00803b14`](../00803/00803b14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803b14` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cd8`](#insn-00ad7cd8) → [`00803c64`](../00803/00803c64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803c64` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cec`](#insn-00ad7cec) → [`00676b3c`](../00676/00676b3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00676b3c` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cf0`](#insn-00ad7cf0) → [`00ad7d00`](#insn-00ad7d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7cfc`](#insn-00ad7cfc) → [`00ad7d18`](#insn-00ad7d18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d08`](#insn-00ad7d08) → [`007bcd04`](../007bc/007bcd04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bcd04` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d0c`](#insn-00ad7d0c) → [`00ad7f64`](#insn-00ad7f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d18`](#insn-00ad7d18) → [`008011a8`](../00801/008011a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008011a8` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d28`](#insn-00ad7d28) → [`008621ec`](../00862/008621ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008621ec` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d3c`](#insn-00ad7d3c) → [`00615d00`](../00615/00615d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00615d00` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d40`](#insn-00ad7d40) → [`00ad7d60`](#insn-00ad7d60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d48`](#insn-00ad7d48) → [`00744610`](../00744/00744610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744610` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d4c`](#insn-00ad7d4c) → [`00ad7d60`](#insn-00ad7d60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d54`](#insn-00ad7d54) → [`00803674`](../00803/00803674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803674` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d5c`](#insn-00ad7d5c) → [`00ad7f8c`](#insn-00ad7f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d68`](#insn-00ad7d68) → `003380f6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7d70`](#insn-00ad7d70) → `003380e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7d90`](#insn-00ad7d90) → [`00ad7db4`](#insn-00ad7db4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7d94`](#insn-00ad7d94) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ad7da0`](#insn-00ad7da0) → [`005c08e0`](../005c0/005c08e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c08e0` · 推定シンボル `None` · 推定型 `None`
- [`00ad7da4`](#insn-00ad7da4) → [`00ad7e3c`](#insn-00ad7e3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7db0`](#insn-00ad7db0) → [`00ad7e70`](#insn-00ad7e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7db4`](#insn-00ad7db4) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ad7e08`](#insn-00ad7e08) → [`00ad7e3c`](#insn-00ad7e3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e10`](#insn-00ad7e10) → [`00744610`](../00744/00744610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744610` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e14`](#insn-00ad7e14) → [`00ad7d94`](#insn-00ad7d94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e20`](#insn-00ad7e20) → [`00744198`](../00744/00744198.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744198` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e24`](#insn-00ad7e24) → [`00ad7da8`](#insn-00ad7da8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e30`](#insn-00ad7e30) → [`00744334`](../00744/00744334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744334` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e34`](#insn-00ad7e34) → [`00ad7d94`](#insn-00ad7d94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e38`](#insn-00ad7e38) → [`00ad7da8`](#insn-00ad7da8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e48`](#insn-00ad7e48) → [`00ad7e78`](#insn-00ad7e78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e58`](#insn-00ad7e58) → [`00a43078`](../00a43/00a43078.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a43078` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e64`](#insn-00ad7e64) → [`00a43104`](../00a43/00a43104.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a43104` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e6c`](#insn-00ad7e6c) → [`00ad7e7c`](#insn-00ad7e7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e74`](#insn-00ad7e74) → [`00ad7f98`](#insn-00ad7f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e8c`](#insn-00ad7e8c) → [`00ad7ea0`](#insn-00ad7ea0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7e9c`](#insn-00ad7e9c) → [`00ad7f5c`](#insn-00ad7f5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ee0`](#insn-00ad7ee0) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ee8`](#insn-00ad7ee8) → [`00744610`](../00744/00744610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744610` · 推定シンボル `None` · 推定型 `None`
- [`00ad7eec`](#insn-00ad7eec) → [`00ad7f10`](#insn-00ad7f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ef8`](#insn-00ad7ef8) → [`00744198`](../00744/00744198.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744198` · 推定シンボル `None` · 推定型 `None`
- [`00ad7efc`](#insn-00ad7efc) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f08`](#insn-00ad7f08) → [`00744334`](../00744/00744334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744334` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f0c`](#insn-00ad7f0c) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f14`](#insn-00ad7f14) → [`00b0a6ec`](../00b0a/00b0a6ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0a6ec` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f18`](#insn-00ad7f18) → [`00ad7f2c`](#insn-00ad7f2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f24`](#insn-00ad7f24) → [`00b0bda4`](../00b0b/00b0bda4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0bda4` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f28`](#insn-00ad7f28) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f2c`](#insn-00ad7f2c) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ad7f38`](#insn-00ad7f38) → [`005c08e0`](../005c0/005c08e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c08e0` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f3c`](#insn-00ad7f3c) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f40`](#insn-00ad7f40) → [`00ad7f54`](#insn-00ad7f54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f4c`](#insn-00ad7f4c) → [`00a43aec`](../00a43/00a43aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a43aec` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f50`](#insn-00ad7f50) → [`00ad7e90`](#insn-00ad7e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f58`](#insn-00ad7f58) → [`00ad7f98`](#insn-00ad7f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f60`](#insn-00ad7f60) → [`00ad7f98`](#insn-00ad7f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f70`](#insn-00ad7f70) → [`00a33a4c`](../00a33/00a33a4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a33a4c` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f74`](#insn-00ad7f74) → [`00ad7d24`](#insn-00ad7d24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f80`](#insn-00ad7f80) → [`00a33ee0`](../00a33/00a33ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a33ee0` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f88`](#insn-00ad7f88) → [`00ad7d24`](#insn-00ad7d24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f90`](#insn-00ad7f90) → `003380f6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7f94`](#insn-00ad7f94) → `003380e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ad7f98`](#insn-00ad7f98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f9c`](#insn-00ad7f9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fa0`](#insn-00ad7fa0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fa4`](#insn-00ad7fa4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fa8`](#insn-00ad7fa8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad7aec`](#insn-00ad7aec)

~~~json
{
  "source": "00ad7aec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7af0`](#insn-00ad7af0)

~~~json
{
  "source": "00ad7af0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7af4`](#insn-00ad7af4)

~~~json
{
  "source": "00ad7af4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7af8`](#insn-00ad7af8)

~~~json
{
  "source": "00ad7af8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7afc`](#insn-00ad7afc)

~~~json
{
  "source": "00ad7afc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b18`](#insn-00ad7b18)

~~~json
{
  "source": "00ad7b18",
  "target": "003380e9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c97d009c6f0a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7b1c`](#insn-00ad7b1c)

~~~json
{
  "source": "00ad7b1c",
  "target": "003380e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c97d009c6f0a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7b20`](#insn-00ad7b20)

~~~json
{
  "source": "00ad7b20",
  "target": "00ad7c74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b28`](#insn-00ad7b28)

~~~json
{
  "source": "00ad7b28",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4a06a00a0760900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7b2c`](#insn-00ad7b2c)

~~~json
{
  "source": "00ad7b2c",
  "target": "003380c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20c97d00106f0a00",
  "capture_start": "003380c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7b30`](#insn-00ad7b30)

~~~json
{
  "source": "00ad7b30",
  "target": "00ad7b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b38`](#insn-00ad7b38)

~~~json
{
  "source": "00ad7b38",
  "target": "00ad7b6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b44`](#insn-00ad7b44)

~~~json
{
  "source": "00ad7b44",
  "target": "00ad7b6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b54`](#insn-00ad7b54)

~~~json
{
  "source": "00ad7b54",
  "target": "00ad7b3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b5c`](#insn-00ad7b5c)

~~~json
{
  "source": "00ad7b5c",
  "target": "00ad7bc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b64`](#insn-00ad7b64)

~~~json
{
  "source": "00ad7b64",
  "target": "00ad7b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7b74`](#insn-00ad7b74)

~~~json
{
  "source": "00ad7b74",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7b98`](#insn-00ad7b98)

~~~json
{
  "source": "00ad7b98",
  "target": "003380c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20c97d00106f0a00",
  "capture_start": "003380c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7b9c`](#insn-00ad7b9c)

~~~json
{
  "source": "00ad7b9c",
  "target": "003380b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380b8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1cc97d00fc6e0a00",
  "capture_start": "003380b8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7ba8`](#insn-00ad7ba8)

~~~json
{
  "source": "00ad7ba8",
  "target": "00ad7bb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7bac`](#insn-00ad7bac)

~~~json
{
  "source": "00ad7bac",
  "target": "003380b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380b8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1cc97d00fc6e0a00",
  "capture_start": "003380b8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7bb0`](#insn-00ad7bb0)

~~~json
{
  "source": "00ad7bb0",
  "target": "003380c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20c97d00106f0a00",
  "capture_start": "003380c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7bb4`](#insn-00ad7bb4)

~~~json
{
  "source": "00ad7bb4",
  "target": "003380c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "20c97d00106f0a00",
  "capture_start": "003380c0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7bb8`](#insn-00ad7bb8)

~~~json
{
  "source": "00ad7bb8",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7bbc`](#insn-00ad7bbc)

~~~json
{
  "source": "00ad7bbc",
  "target": "003380c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "50c97d00386f0a00",
  "capture_start": "003380c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7bc4`](#insn-00ad7bc4)

~~~json
{
  "source": "00ad7bc4",
  "target": "003380c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380c8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "50c97d00386f0a00",
  "capture_start": "003380c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7bc8`](#insn-00ad7bc8)

~~~json
{
  "source": "00ad7bc8",
  "target": "00803c64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7bd8`](#insn-00ad7bd8)

~~~json
{
  "source": "00ad7bd8",
  "target": "00ad7bf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7be0`](#insn-00ad7be0)

~~~json
{
  "source": "00ad7be0",
  "target": "00ad7c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7bec`](#insn-00ad7bec)

~~~json
{
  "source": "00ad7bec",
  "target": "00ad7c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7bfc`](#insn-00ad7bfc)

~~~json
{
  "source": "00ad7bfc",
  "target": "00ad7be4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c04`](#insn-00ad7c04)

~~~json
{
  "source": "00ad7c04",
  "target": "00ad7c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c0c`](#insn-00ad7c0c)

~~~json
{
  "source": "00ad7c0c",
  "target": "00ad7bf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c1c`](#insn-00ad7c1c)

~~~json
{
  "source": "00ad7c1c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7c44`](#insn-00ad7c44)

~~~json
{
  "source": "00ad7c44",
  "target": "00ad7c50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c54`](#insn-00ad7c54)

~~~json
{
  "source": "00ad7c54",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7c68`](#insn-00ad7c68)

~~~json
{
  "source": "00ad7c68",
  "target": "00ad7c74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c70`](#insn-00ad7c70)

~~~json
{
  "source": "00ad7c70",
  "target": "003380e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c97d009c6f0a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7c74`](#insn-00ad7c74)

~~~json
{
  "source": "00ad7c74",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4a06a00a0760900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7c7c`](#insn-00ad7c7c)

~~~json
{
  "source": "00ad7c7c",
  "target": "003380f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7c80`](#insn-00ad7c80)

~~~json
{
  "source": "00ad7c80",
  "target": "007df5b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7c84`](#insn-00ad7c84)

~~~json
{
  "source": "00ad7c84",
  "target": "00ad7ca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c88`](#insn-00ad7c88)

~~~json
{
  "source": "00ad7c88",
  "target": "003380f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c8c97d00c46f0a00",
  "capture_start": "003380f8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7c8c`](#insn-00ad7c8c)

~~~json
{
  "source": "00ad7c8c",
  "target": "00803c64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7c94`](#insn-00ad7c94)

~~~json
{
  "source": "00ad7c94",
  "target": "00ad7ca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7c9c`](#insn-00ad7c9c)

~~~json
{
  "source": "00ad7c9c",
  "target": "003380f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7ca0`](#insn-00ad7ca0)

~~~json
{
  "source": "00ad7ca0",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4a06a00a0760900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7ca8`](#insn-00ad7ca8)

~~~json
{
  "source": "00ad7ca8",
  "target": "003380f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 7,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7cac`](#insn-00ad7cac)

~~~json
{
  "source": "00ad7cac",
  "target": "007df630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7cb0`](#insn-00ad7cb0)

~~~json
{
  "source": "00ad7cb0",
  "target": "00ad7ccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7cb4`](#insn-00ad7cb4)

~~~json
{
  "source": "00ad7cb4",
  "target": "003380f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c8c97d00c46f0a00",
  "capture_start": "003380f8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7cb8`](#insn-00ad7cb8)

~~~json
{
  "source": "00ad7cb8",
  "target": "00803c64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7cc0`](#insn-00ad7cc0)

~~~json
{
  "source": "00ad7cc0",
  "target": "00ad7ccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7cc8`](#insn-00ad7cc8)

~~~json
{
  "source": "00ad7cc8",
  "target": "003380f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 7,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7cd0`](#insn-00ad7cd0)

~~~json
{
  "source": "00ad7cd0",
  "target": "00803b14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7cd8`](#insn-00ad7cd8)

~~~json
{
  "source": "00ad7cd8",
  "target": "00803c64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7cec`](#insn-00ad7cec)

~~~json
{
  "source": "00ad7cec",
  "target": "00676b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7cf0`](#insn-00ad7cf0)

~~~json
{
  "source": "00ad7cf0",
  "target": "00ad7d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7cfc`](#insn-00ad7cfc)

~~~json
{
  "source": "00ad7cfc",
  "target": "00ad7d18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d08`](#insn-00ad7d08)

~~~json
{
  "source": "00ad7d08",
  "target": "007bcd04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d0c`](#insn-00ad7d0c)

~~~json
{
  "source": "00ad7d0c",
  "target": "00ad7f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d18`](#insn-00ad7d18)

~~~json
{
  "source": "00ad7d18",
  "target": "008011a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d28`](#insn-00ad7d28)

~~~json
{
  "source": "00ad7d28",
  "target": "008621ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d3c`](#insn-00ad7d3c)

~~~json
{
  "source": "00ad7d3c",
  "target": "00615d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d40`](#insn-00ad7d40)

~~~json
{
  "source": "00ad7d40",
  "target": "00ad7d60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d48`](#insn-00ad7d48)

~~~json
{
  "source": "00ad7d48",
  "target": "00744610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d4c`](#insn-00ad7d4c)

~~~json
{
  "source": "00ad7d4c",
  "target": "00ad7d60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d54`](#insn-00ad7d54)

~~~json
{
  "source": "00ad7d54",
  "target": "00803674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7d5c`](#insn-00ad7d5c)

~~~json
{
  "source": "00ad7d5c",
  "target": "00ad7f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d68`](#insn-00ad7d68)

~~~json
{
  "source": "00ad7d68",
  "target": "003380f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7d70`](#insn-00ad7d70)

~~~json
{
  "source": "00ad7d70",
  "target": "003380e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c97d009c6f0a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7d90`](#insn-00ad7d90)

~~~json
{
  "source": "00ad7d90",
  "target": "00ad7db4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7d94`](#insn-00ad7d94)

~~~json
{
  "source": "00ad7d94",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7da0`](#insn-00ad7da0)

~~~json
{
  "source": "00ad7da0",
  "target": "005c08e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7da4`](#insn-00ad7da4)

~~~json
{
  "source": "00ad7da4",
  "target": "00ad7e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7db0`](#insn-00ad7db0)

~~~json
{
  "source": "00ad7db0",
  "target": "00ad7e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7db4`](#insn-00ad7db4)

~~~json
{
  "source": "00ad7db4",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7e08`](#insn-00ad7e08)

~~~json
{
  "source": "00ad7e08",
  "target": "00ad7e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e10`](#insn-00ad7e10)

~~~json
{
  "source": "00ad7e10",
  "target": "00744610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7e14`](#insn-00ad7e14)

~~~json
{
  "source": "00ad7e14",
  "target": "00ad7d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e20`](#insn-00ad7e20)

~~~json
{
  "source": "00ad7e20",
  "target": "00744198",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7e24`](#insn-00ad7e24)

~~~json
{
  "source": "00ad7e24",
  "target": "00ad7da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e30`](#insn-00ad7e30)

~~~json
{
  "source": "00ad7e30",
  "target": "00744334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7e34`](#insn-00ad7e34)

~~~json
{
  "source": "00ad7e34",
  "target": "00ad7d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e38`](#insn-00ad7e38)

~~~json
{
  "source": "00ad7e38",
  "target": "00ad7da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e48`](#insn-00ad7e48)

~~~json
{
  "source": "00ad7e48",
  "target": "00ad7e78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e58`](#insn-00ad7e58)

~~~json
{
  "source": "00ad7e58",
  "target": "00a43078",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7e64`](#insn-00ad7e64)

~~~json
{
  "source": "00ad7e64",
  "target": "00a43104",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7e6c`](#insn-00ad7e6c)

~~~json
{
  "source": "00ad7e6c",
  "target": "00ad7e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e74`](#insn-00ad7e74)

~~~json
{
  "source": "00ad7e74",
  "target": "00ad7f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e8c`](#insn-00ad7e8c)

~~~json
{
  "source": "00ad7e8c",
  "target": "00ad7ea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7e9c`](#insn-00ad7e9c)

~~~json
{
  "source": "00ad7e9c",
  "target": "00ad7f5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ee0`](#insn-00ad7ee0)

~~~json
{
  "source": "00ad7ee0",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ee8`](#insn-00ad7ee8)

~~~json
{
  "source": "00ad7ee8",
  "target": "00744610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7eec`](#insn-00ad7eec)

~~~json
{
  "source": "00ad7eec",
  "target": "00ad7f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ef8`](#insn-00ad7ef8)

~~~json
{
  "source": "00ad7ef8",
  "target": "00744198",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7efc`](#insn-00ad7efc)

~~~json
{
  "source": "00ad7efc",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f08`](#insn-00ad7f08)

~~~json
{
  "source": "00ad7f08",
  "target": "00744334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f0c`](#insn-00ad7f0c)

~~~json
{
  "source": "00ad7f0c",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f14`](#insn-00ad7f14)

~~~json
{
  "source": "00ad7f14",
  "target": "00b0a6ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f18`](#insn-00ad7f18)

~~~json
{
  "source": "00ad7f18",
  "target": "00ad7f2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f24`](#insn-00ad7f24)

~~~json
{
  "source": "00ad7f24",
  "target": "00b0bda4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f28`](#insn-00ad7f28)

~~~json
{
  "source": "00ad7f28",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f2c`](#insn-00ad7f2c)

~~~json
{
  "source": "00ad7f2c",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b978",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "0039b978",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f38`](#insn-00ad7f38)

~~~json
{
  "source": "00ad7f38",
  "target": "005c08e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f3c`](#insn-00ad7f3c)

~~~json
{
  "source": "00ad7f3c",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f40`](#insn-00ad7f40)

~~~json
{
  "source": "00ad7f40",
  "target": "00ad7f54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f4c`](#insn-00ad7f4c)

~~~json
{
  "source": "00ad7f4c",
  "target": "00a43aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f50`](#insn-00ad7f50)

~~~json
{
  "source": "00ad7f50",
  "target": "00ad7e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f58`](#insn-00ad7f58)

~~~json
{
  "source": "00ad7f58",
  "target": "00ad7f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f60`](#insn-00ad7f60)

~~~json
{
  "source": "00ad7f60",
  "target": "00ad7f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f70`](#insn-00ad7f70)

~~~json
{
  "source": "00ad7f70",
  "target": "00a33a4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f74`](#insn-00ad7f74)

~~~json
{
  "source": "00ad7f74",
  "target": "00ad7d24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f80`](#insn-00ad7f80)

~~~json
{
  "source": "00ad7f80",
  "target": "00a33ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f88`](#insn-00ad7f88)

~~~json
{
  "source": "00ad7f88",
  "target": "00ad7d24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f90`](#insn-00ad7f90)

~~~json
{
  "source": "00ad7f90",
  "target": "003380f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380f0",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c4c97d00b06f0a00",
  "capture_start": "003380f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f94`](#insn-00ad7f94)

~~~json
{
  "source": "00ad7f94",
  "target": "003380e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "b0c97d009c6f0a00",
  "capture_start": "003380e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f98`](#insn-00ad7f98)

~~~json
{
  "source": "00ad7f98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f9c`](#insn-00ad7f9c)

~~~json
{
  "source": "00ad7f9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fa0`](#insn-00ad7fa0)

~~~json
{
  "source": "00ad7fa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fa4`](#insn-00ad7fa4)

~~~json
{
  "source": "00ad7fa4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fa8`](#insn-00ad7fa8)

~~~json
{
  "source": "00ad7fa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
