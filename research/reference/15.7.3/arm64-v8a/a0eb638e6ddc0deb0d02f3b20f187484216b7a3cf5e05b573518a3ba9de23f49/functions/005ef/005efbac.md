# 005efbac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005efbac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ef/005efbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0004.md#compare-23980596f8a28e6c256541743bdb32a5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005efbac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005efbac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0004.md#compare-a1b36ee8c6e7637f2d15483b5873f609)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005efbac",
  "name": "FUN_005efbac",
  "size": 828,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b627be22636f9d7b57a80edbf65586e6b9231b17e095f0272279d0f9385c290",
  "source_text_sha256": "7b627be22636f9d7b57a80edbf65586e6b9231b17e095f0272279d0f9385c290",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005efbac",
        "005efee7"
      ]
    ],
    "bytes_sha256": "8b4c63deab7e442f579fa33d50a9c5a10e9569bbc09cbb953e9a3af8c0d0db2e",
    "instruction_count": 207,
    "instruction_bytes": 828,
    "body_bytes": 828,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)

## 呼び出し先

- [00444c18](../00444/00444c18.md)
- [00444c54](../00444/00444c54.md)
- [0044507c](../00445/0044507c.md)
- [004460b0](../00446/004460b0.md)
- [00448034](../00448/00448034.md)
- [00449aec](../00449/00449aec.md)
- [00467074](../00467/00467074.md)
- [0081f580](../0081f/0081f580.md)
- [00883bb8](../00883/00883bb8.md)
- [008847e4](../00884/008847e4.md)
- [00a0b03c](../00a0b/00a0b03c.md)
- [00a0b818](../00a0b/00a0b818.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5486 bytes

~~~c

void FUN_005efbac(long param_1,long param_2,undefined8 param_3)

{
  int *piVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  uint uVar6;
  undefined *puVar7;
  int iVar8;
  undefined4 uVar9;
  ulong uVar10;
  long lVar11;
  undefined8 uVar12;
  float local_8c;
  float fStack_88;
  long local_78;
  
  lVar5 = tpidr_el0;
                    /* try { // try from 005efbd4 to 006efbdb has its CatchHandler @ 005efcd4 */
  local_78 = *(long *)(lVar5 + 0x28);
  piVar1 = (int *)(param_1 + 0x83e38);
  if (0 < *piVar1) {
    uVar2 = *(uint *)(param_1 + 0x83e3c);
    uVar12 = *(undefined8 *)(param_2 + 0x410);
    if (0xb < uVar2) {
      uVar2 = 0xc;
    }
    if (*piVar1 != 1) {
      uVar2 = 0xc;
    }
    iVar8 = FUN_00449aec();
    puVar7 = PTR_DAT_00c1b6a0;
    if (iVar8 < 0) {
      iVar8 = iVar8 + 1;
    }
                    /* try { // try from 005efc3c to 006efc43 has its CatchHandler @ 005efcbc */
                    /* try { // try from 005efc48 to 006efc53 has its CatchHandler @ 005efcac */
    FUN_004460b0(param_3,uVar12,
                 ((iVar8 >> 1) - *(int *)(PTR_DAT_00c1b6a0 + (ulong)uVar2 * 4)) + -0xef,0xbe,0xc);
    if (1 < *piVar1) {
      uVar2 = *(uint *)(param_1 + 0x83e3c);
      if (0xb < uVar2) {
        uVar2 = 0xc;
      }
                    /* try { // try from 005efc70 to 006efc7b has its CatchHandler @ 005efca8 */
      if (*piVar1 != 2) {
        uVar2 = 0xc;
      }
      FUN_00444c18(param_3,2);
                    /* try { // try from 005efc7c to 006efd03 has its CatchHandler @ 005efb8c */
      FUN_00444c54(param_3,0x28,0x28,0x4d,0xff);
      iVar8 = *(int *)(puVar7 + (ulong)uVar2 * 4);
      uVar9 = FUN_00449aec(param_1);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc70 with catch @ 005efca8
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc48 with catch @ 005efcac
                        */
      FUN_0044507c(param_3,-iVar8,0x13b,uVar9,0x37);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efc3c with catch @ 005efcbc
                        */
      FUN_00444c18(param_3,0);
      uVar10 = FUN_00a0b03c(*(undefined8 *)(param_1 + 0x7e8));
      if ((uVar10 & 1) != 0) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005efbd4 with catch @ 005efcd4
                        */
        uVar12 = *(undefined8 *)(param_2 + 800);
        FUN_0081f580();
        iVar8 = FUN_00449aec();
        iVar4 = *(int *)(puVar7 + (ulong)uVar2 * 4);
        if (iVar8 < 0) {
          iVar8 = iVar8 + 1;
        }
        uVar9 = FUN_00a0b818(*(undefined8 *)(param_1 + 0x7e8));
                    /* catch() { ... } // from try @ 005efdac with catch @ 005efd04 */
        lVar11 = FUN_00467074(*(undefined8 *)(param_2 + 0x410),5);
        iVar3 = *(int *)(lVar11 + 8);
        lVar11 = FUN_00467074(*(undefined8 *)(param_2 + 0x410),4);
                    /* try { // try from 005efd4c to 006efd53 has its CatchHandler @ 005efe00 */
        FUN_00448034(&local_8c,(float)((iVar8 >> 1) - iVar4),0x43a08000,0xbf800000,param_3,uVar12,0,
                     uVar9,iVar3 + 0x14,*(int *)(lVar11 + 8) + 0x14,1,0);
        uVar12 = *(undefined8 *)(param_2 + 0x410);
        lVar11 = FUN_00467074(uVar12,0xb);
                    /* try { // try from 005efd90 to 006efd9f has its CatchHandler @ 005efde8 */
                    /* try { // try from 005efda0 to 006efdab has its CatchHandler @ 005efdd8 */
        FUN_004460b0(param_3,uVar12,(int)((local_8c - (float)*(int *)(lVar11 + 8)) + -20.0),0x144,
                     0xb);
                    /* try { // try from 005efdac to 006efe2f has its CatchHandler @ 005efd04 */
        FUN_004460b0(param_3,*(undefined8 *)(param_2 + 0x410),(int)(fStack_88 + 20.0),0x143,4);
        if (*piVar1 == 2) goto LAB_005efeb0;
                    /* catch() { ... } // from try @ 005efda0 with catch @ 005efdd8 */
        if (*(int *)(param_1 + 0x83e58) == 1) {
                    /* catch() { ... } // from try @ 005efd90 with catch @ 005efde8 */
          uVar12 = *(undefined8 *)(param_2 + 0x410);
                    /* catch() { ... } // from try @ 005efd4c with catch @ 005efe00 */
          lVar11 = FUN_00467074(uVar12,6);
          iVar8 = *(int *)(lVar11 + 8);
          uVar2 = *(uint *)(BYTE_ARRAY_003c3369 + param_1 + 3) & 3;
          if (iVar8 < 0) {
            iVar8 = iVar8 + 1;
          }
          uVar6 = -*(uint *)(BYTE_ARRAY_003c3369 + param_1 + 3);
                    /* catch() { ... } // from try @ 005f0028 with catch @ 005efe30 */
          if (-1 < (int)uVar6) {
            uVar2 = -(uVar6 & 3);
          }
          FUN_004460b0(param_3,uVar12,
                       (int)((local_8c + (fStack_88 - local_8c) * 0.5) - (float)(iVar8 >> 1)),300,
                       ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 6 &
                       0xff);
        }
      }
      if ((*piVar1 == 7) && ((*(byte *)((long)&DWORD_0032e038 + param_1) & 1) == 0)) {
        uVar12 = FUN_008847e4(param_1 + 0x2e48,200);
        FUN_00883bb8(uVar12,0,0);
        uVar12 = FUN_008847e4(param_1 + 0x2e48,0xc9);
                    /* try { // try from 005efea8 to 006efeaf has its CatchHandler @ 005f0068 */
        FUN_00883bb8(uVar12,0,0);
      }
    }
  }
LAB_005efeb0:
  if (*(long *)(lVar5 + 0x28) == local_78) {
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
<a id="insn-005efbac"></a> `005efbac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-005efbb0"></a> `005efbb0` | `e9 23 02 6d` | stp d9,d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005efbb4"></a> `005efbb4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005efbb8"></a> `005efbb8` | `fb 23 00 f9` | str x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005efbbc"></a> `005efbbc` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005efbc0"></a> `005efbc0` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005efbc4"></a> `005efbc4` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005efbc8"></a> `005efbc8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005efbcc"></a> `005efbcc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-005efbd0"></a> `005efbd0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005efbd4"></a> `005efbd4` | `09 0c 42 91` | add x9,x0,#0x83, LSL #12 | `FALL_THROUGH`
<a id="insn-005efbd8"></a> `005efbd8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-005efbdc"></a> `005efbdc` | `39 e1 38 91` | add x25,x9,#0xe38 | `FALL_THROUGH`
<a id="insn-005efbe0"></a> `005efbe0` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005efbe4"></a> `005efbe4` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-005efbe8"></a> `005efbe8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-005efbec"></a> `005efbec` | `2b 16 00 54` | b.lt 0x005efeb0 | `CONDITIONAL_JUMP`
<a id="insn-005efbf0"></a> `005efbf0` | `29 07 40 b9` | ldr w9,[x25, #0x4] | `FALL_THROUGH`
<a id="insn-005efbf4"></a> `005efbf4` | `9a 01 80 52` | mov w26,#0xc | `FALL_THROUGH`
<a id="insn-005efbf8"></a> `005efbf8` | `36 08 42 f9` | ldr x22,[x1, #0x410] | `FALL_THROUGH`
<a id="insn-005efbfc"></a> `005efbfc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-005efc00"></a> `005efc00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005efc04"></a> `005efc04` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-005efc08"></a> `005efc08` | `3f 31 00 71` | cmp w9,#0xc | `FALL_THROUGH`
<a id="insn-005efc0c"></a> `005efc0c` | `29 31 9a 1a` | csel w9,w9,w26,cc | `FALL_THROUGH`
<a id="insn-005efc10"></a> `005efc10` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-005efc14"></a> `005efc14` | `3b 01 9a 1a` | csel w27,w9,w26,eq | `FALL_THROUGH`
<a id="insn-005efc18"></a> `005efc18` | `b5 67 f9 97` | bl 0x00449aec | `UNCONDITIONAL_CALL`
<a id="insn-005efc1c"></a> `005efc1c` | `77 31 00 90` | adrp x23,0xc1b000 | `FALL_THROUGH`
<a id="insn-005efc20"></a> `005efc20` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-005efc24"></a> `005efc24` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-005efc28"></a> `005efc28` | `f7 52 43 f9` | ldr x23,[x23, #0x6a0] | `FALL_THROUGH`
<a id="insn-005efc2c"></a> `005efc2c` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-005efc30"></a> `005efc30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efc34"></a> `005efc34` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-005efc38"></a> `005efc38` | `c3 17 80 52` | mov w3,#0xbe | `FALL_THROUGH`
<a id="insn-005efc3c"></a> `005efc3c` | `84 01 80 52` | mov w4,#0xc | `FALL_THROUGH`
<a id="insn-005efc40"></a> `005efc40` | `e9 5a 7b b8` | ldr w9,[x23, w27, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-005efc44"></a> `005efc44` | `08 01 09 4b` | sub w8,w8,w9 | `FALL_THROUGH`
<a id="insn-005efc48"></a> `005efc48` | `02 bd 03 51` | sub w2,w8,#0xef | `FALL_THROUGH`
<a id="insn-005efc4c"></a> `005efc4c` | `19 59 f9 97` | bl 0x004460b0 | `UNCONDITIONAL_CALL`
<a id="insn-005efc50"></a> `005efc50` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-005efc54"></a> `005efc54` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-005efc58"></a> `005efc58` | `cb 12 00 54` | b.lt 0x005efeb0 | `CONDITIONAL_JUMP`
<a id="insn-005efc5c"></a> `005efc5c` | `29 07 40 b9` | ldr w9,[x25, #0x4] | `FALL_THROUGH`
<a id="insn-005efc60"></a> `005efc60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efc64"></a> `005efc64` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-005efc68"></a> `005efc68` | `3f 31 00 71` | cmp w9,#0xc | `FALL_THROUGH`
<a id="insn-005efc6c"></a> `005efc6c` | `29 31 9a 1a` | csel w9,w9,w26,cc | `FALL_THROUGH`
<a id="insn-005efc70"></a> `005efc70` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-005efc74"></a> `005efc74` | `3a 01 9a 1a` | csel w26,w9,w26,eq | `FALL_THROUGH`
<a id="insn-005efc78"></a> `005efc78` | `e8 53 f9 97` | bl 0x00444c18 | `UNCONDITIONAL_CALL`
<a id="insn-005efc7c"></a> `005efc7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efc80"></a> `005efc80` | `01 05 80 52` | mov w1,#0x28 | `FALL_THROUGH`
<a id="insn-005efc84"></a> `005efc84` | `02 05 80 52` | mov w2,#0x28 | `FALL_THROUGH`
<a id="insn-005efc88"></a> `005efc88` | `a3 09 80 52` | mov w3,#0x4d | `FALL_THROUGH`
<a id="insn-005efc8c"></a> `005efc8c` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-005efc90"></a> `005efc90` | `f1 53 f9 97` | bl 0x00444c54 | `UNCONDITIONAL_CALL`
<a id="insn-005efc94"></a> `005efc94` | `e8 5a 7a b8` | ldr w8,[x23, w26, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-005efc98"></a> `005efc98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005efc9c"></a> `005efc9c` | `f6 03 08 4b` | neg w22,w8 | `FALL_THROUGH`
<a id="insn-005efca0"></a> `005efca0` | `93 67 f9 97` | bl 0x00449aec | `UNCONDITIONAL_CALL`
<a id="insn-005efca4"></a> `005efca4` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-005efca8"></a> `005efca8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efcac"></a> `005efcac` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-005efcb0"></a> `005efcb0` | `62 27 80 52` | mov w2,#0x13b | `FALL_THROUGH`
<a id="insn-005efcb4"></a> `005efcb4` | `e4 06 80 52` | mov w4,#0x37 | `FALL_THROUGH`
<a id="insn-005efcb8"></a> `005efcb8` | `f1 54 f9 97` | bl 0x0044507c | `UNCONDITIONAL_CALL`
<a id="insn-005efcbc"></a> `005efcbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efcc0"></a> `005efcc0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-005efcc4"></a> `005efcc4` | `d5 53 f9 97` | bl 0x00444c18 | `UNCONDITIONAL_CALL`
<a id="insn-005efcc8"></a> `005efcc8` | `60 f6 43 f9` | ldr x0,[x19, #0x7e8] | `FALL_THROUGH`
<a id="insn-005efccc"></a> `005efccc` | `dc 6c 10 94` | bl 0x00a0b03c | `UNCONDITIONAL_CALL`
<a id="insn-005efcd0"></a> `005efcd0` | `80 0c 00 36` | tbz w0,#0x0,0x005efe60 | `CONDITIONAL_JUMP`
<a id="insn-005efcd4"></a> `005efcd4` | `b6 92 41 f9` | ldr x22,[x21, #0x320] | `FALL_THROUGH`
<a id="insn-005efcd8"></a> `005efcd8` | `2a be 08 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005efcdc"></a> `005efcdc` | `84 67 f9 97` | bl 0x00449aec | `UNCONDITIONAL_CALL`
<a id="insn-005efce0"></a> `005efce0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-005efce4"></a> `005efce4` | `e8 5a 7a b8` | ldr w8,[x23, w26, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-005efce8"></a> `005efce8` | `09 a4 80 1a` | cinc w9,w0,lt | `FALL_THROUGH`
<a id="insn-005efcec"></a> `005efcec` | `60 f6 43 f9` | ldr x0,[x19, #0x7e8] | `FALL_THROUGH`
<a id="insn-005efcf0"></a> `005efcf0` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-005efcf4"></a> `005efcf4` | `28 01 08 4b` | sub w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005efcf8"></a> `005efcf8` | `08 01 22 1e` | scvtf s8,w8 | `FALL_THROUGH`
<a id="insn-005efcfc"></a> `005efcfc` | `c7 6e 10 94` | bl 0x00a0b818 | `UNCONDITIONAL_CALL`
<a id="insn-005efd00"></a> `005efd00` | `a8 0a 42 f9` | ldr x8,[x21, #0x410] | `FALL_THROUGH`
<a id="insn-005efd04"></a> `005efd04` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-005efd08"></a> `005efd08` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-005efd0c"></a> `005efd0c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005efd10"></a> `005efd10` | `d9 dc f9 97` | bl 0x00467074 | `UNCONDITIONAL_CALL`
<a id="insn-005efd14"></a> `005efd14` | `a8 0a 42 f9` | ldr x8,[x21, #0x410] | `FALL_THROUGH`
<a id="insn-005efd18"></a> `005efd18` | `1a 08 40 b9` | ldr w26,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005efd1c"></a> `005efd1c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-005efd20"></a> `005efd20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005efd24"></a> `005efd24` | `d4 dc f9 97` | bl 0x00467074 | `UNCONDITIONAL_CALL`
<a id="insn-005efd28"></a> `005efd28` | `0a 00 90 52` | mov w10,#0x8000 | `FALL_THROUGH`
<a id="insn-005efd2c"></a> `005efd2c` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005efd30"></a> `005efd30` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005efd34"></a> `005efd34` | `0a 74 a8 72` | movk w10,#0x43a0, LSL #16 | `FALL_THROUGH`
<a id="insn-005efd38"></a> `005efd38` | `02 10 3e 1e` | fmov s2,0xbf800000 | `FALL_THROUGH`
<a id="insn-005efd3c"></a> `005efd3c` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-005efd40"></a> `005efd40` | `41 01 27 1e` | fmov s1,w10 | `FALL_THROUGH`
<a id="insn-005efd44"></a> `005efd44` | `44 53 00 11` | add w4,w26,#0x14 | `FALL_THROUGH`
<a id="insn-005efd48"></a> `005efd48` | `25 51 00 11` | add w5,w9,#0x14 | `FALL_THROUGH`
<a id="insn-005efd4c"></a> `005efd4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efd50"></a> `005efd50` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-005efd54"></a> `005efd54` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-005efd58"></a> `005efd58` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-005efd5c"></a> `005efd5c` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-005efd60"></a> `005efd60` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-005efd64"></a> `005efd64` | `b4 60 f9 97` | bl 0x00448034 | `UNCONDITIONAL_CALL`
<a id="insn-005efd68"></a> `005efd68` | `b6 0a 42 f9` | ldr x22,[x21, #0x410] | `FALL_THROUGH`
<a id="insn-005efd6c"></a> `005efd6c` | `e8 a7 40 2d` | ldp s8,s9,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-005efd70"></a> `005efd70` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-005efd74"></a> `005efd74` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-005efd78"></a> `005efd78` | `bf dc f9 97` | bl 0x00467074 | `UNCONDITIONAL_CALL`
<a id="insn-005efd7c"></a> `005efd7c` | `00 08 40 bd` | ldr s0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005efd80"></a> `005efd80` | `01 90 36 1e` | fmov s1,0xc1a00000 | `FALL_THROUGH`
<a id="insn-005efd84"></a> `005efd84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efd88"></a> `005efd88` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-005efd8c"></a> `005efd8c` | `83 28 80 52` | mov w3,#0x144 | `FALL_THROUGH`
<a id="insn-005efd90"></a> `005efd90` | `64 01 80 52` | mov w4,#0xb | `FALL_THROUGH`
<a id="insn-005efd94"></a> `005efd94` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-005efd98"></a> `005efd98` | `00 39 20 1e` | fsub s0,s8,s0 | `FALL_THROUGH`
<a id="insn-005efd9c"></a> `005efd9c` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005efda0"></a> `005efda0` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-005efda4"></a> `005efda4` | `c3 58 f9 97` | bl 0x004460b0 | `UNCONDITIONAL_CALL`
<a id="insn-005efda8"></a> `005efda8` | `00 90 26 1e` | fmov s0,0x41a00000 | `FALL_THROUGH`
<a id="insn-005efdac"></a> `005efdac` | `a1 0a 42 f9` | ldr x1,[x21, #0x410] | `FALL_THROUGH`
<a id="insn-005efdb0"></a> `005efdb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efdb4"></a> `005efdb4` | `63 28 80 52` | mov w3,#0x143 | `FALL_THROUGH`
<a id="insn-005efdb8"></a> `005efdb8` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-005efdbc"></a> `005efdbc` | `20 29 20 1e` | fadd s0,s9,s0 | `FALL_THROUGH`
<a id="insn-005efdc0"></a> `005efdc0` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-005efdc4"></a> `005efdc4` | `bb 58 f9 97` | bl 0x004460b0 | `UNCONDITIONAL_CALL`
<a id="insn-005efdc8"></a> `005efdc8` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-005efdcc"></a> `005efdcc` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-005efdd0"></a> `005efdd0` | `00 07 00 54` | b.eq 0x005efeb0 | `CONDITIONAL_JUMP`
<a id="insn-005efdd4"></a> `005efdd4` | `28 23 40 b9` | ldr w8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-005efdd8"></a> `005efdd8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-005efddc"></a> `005efddc` | `21 04 00 54` | b.ne 0x005efe60 | `CONDITIONAL_JUMP`
<a id="insn-005efde0"></a> `005efde0` | `20 39 28 1e` | fsub s0,s9,s8 | `FALL_THROUGH`
<a id="insn-005efde4"></a> `005efde4` | `01 10 2c 1e` | fmov s1,0x3f000000 | `FALL_THROUGH`
<a id="insn-005efde8"></a> `005efde8` | `b5 0a 42 f9` | ldr x21,[x21, #0x410] | `FALL_THROUGH`
<a id="insn-005efdec"></a> `005efdec` | `96 6d 86 52` | mov w22,#0x336c | `FALL_THROUGH`
<a id="insn-005efdf0"></a> `005efdf0` | `c1 00 80 52` | mov w1,#0x6 | `FALL_THROUGH`
<a id="insn-005efdf4"></a> `005efdf4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-005efdf8"></a> `005efdf8` | `96 07 a0 72` | movk w22,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-005efdfc"></a> `005efdfc` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005efe00"></a> `005efe00` | `08 29 20 1e` | fadd s8,s8,s0 | `FALL_THROUGH`
<a id="insn-005efe04"></a> `005efe04` | `9c dc f9 97` | bl 0x00467074 | `UNCONDITIONAL_CALL`
<a id="insn-005efe08"></a> `005efe08` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005efe0c"></a> `005efe0c` | `68 6a 76 b8` | ldr w8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005efe10"></a> `005efe10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005efe14"></a> `005efe14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-005efe18"></a> `005efe18` | `83 25 80 52` | mov w3,#0x12c | `FALL_THROUGH`
<a id="insn-005efe1c"></a> `005efe1c` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-005efe20"></a> `005efe20` | `0a 05 00 12` | and w10,w8,#0x3 | `FALL_THROUGH`
<a id="insn-005efe24"></a> `005efe24` | `29 a5 89 1a` | cinc w9,w9,lt | `FALL_THROUGH`
<a id="insn-005efe28"></a> `005efe28` | `e8 03 08 6b` | negs w8,w8 | `FALL_THROUGH`
<a id="insn-005efe2c"></a> `005efe2c` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-005efe30"></a> `005efe30` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-005efe34"></a> `005efe34` | `48 45 88 5a` | csneg w8,w10,w8,mi | `FALL_THROUGH`
<a id="insn-005efe38"></a> `005efe38` | `20 01 22 1e` | scvtf s0,w9 | `FALL_THROUGH`
<a id="insn-005efe3c"></a> `005efe3c` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-005efe40"></a> `005efe40` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-005efe44"></a> `005efe44` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-005efe48"></a> `005efe48` | `00 39 20 1e` | fsub s0,s8,s0 | `FALL_THROUGH`
<a id="insn-005efe4c"></a> `005efe4c` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-005efe50"></a> `005efe50` | `08 19 00 11` | add w8,w8,#0x6 | `FALL_THROUGH`
<a id="insn-005efe54"></a> `005efe54` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-005efe58"></a> `005efe58` | `04 1d 00 12` | and w4,w8,#0xff | `FALL_THROUGH`
<a id="insn-005efe5c"></a> `005efe5c` | `95 58 f9 97` | bl 0x004460b0 | `UNCONDITIONAL_CALL`
<a id="insn-005efe60"></a> `005efe60` | `28 03 40 b9` | ldr w8,[x25] | `FALL_THROUGH`
<a id="insn-005efe64"></a> `005efe64` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-005efe68"></a> `005efe68` | `41 02 00 54` | b.ne 0x005efeb0 | `CONDITIONAL_JUMP`
<a id="insn-005efe6c"></a> `005efe6c` | `08 07 9c 52` | mov w8,#0xe038 | `FALL_THROUGH`
<a id="insn-005efe70"></a> `005efe70` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-005efe74"></a> `005efe74` | `68 6a 68 38` | ldrb w8,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-005efe78"></a> `005efe78` | `c8 01 00 37` | tbnz w8,#0x0,0x005efeb0 | `CONDITIONAL_JUMP`
<a id="insn-005efe7c"></a> `005efe7c` | `14 c9 85 52` | mov w20,#0x2e48 | `FALL_THROUGH`
<a id="insn-005efe80"></a> `005efe80` | `01 19 80 52` | mov w1,#0xc8 | `FALL_THROUGH`
<a id="insn-005efe84"></a> `005efe84` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-005efe88"></a> `005efe88` | `57 52 0a 94` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-005efe8c"></a> `005efe8c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-005efe90"></a> `005efe90` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-005efe94"></a> `005efe94` | `49 4f 0a 94` | bl 0x00883bb8 | `UNCONDITIONAL_CALL`
<a id="insn-005efe98"></a> `005efe98` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-005efe9c"></a> `005efe9c` | `21 19 80 52` | mov w1,#0xc9 | `FALL_THROUGH`
<a id="insn-005efea0"></a> `005efea0` | `51 52 0a 94` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-005efea4"></a> `005efea4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-005efea8"></a> `005efea8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-005efeac"></a> `005efeac` | `43 4f 0a 94` | bl 0x00883bb8 | `UNCONDITIONAL_CALL`
<a id="insn-005efeb0"></a> `005efeb0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-005efeb4"></a> `005efeb4` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005efeb8"></a> `005efeb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005efebc"></a> `005efebc` | `41 01 00 54` | b.ne 0x005efee4 | `CONDITIONAL_JUMP`
<a id="insn-005efec0"></a> `005efec0` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005efec4"></a> `005efec4` | `fb 23 40 f9` | ldr x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005efec8"></a> `005efec8` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005efecc"></a> `005efecc` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005efed0"></a> `005efed0` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005efed4"></a> `005efed4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005efed8"></a> `005efed8` | `e9 23 42 6d` | ldp d9,d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005efedc"></a> `005efedc` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-005efee0"></a> `005efee0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005efee4"></a> `005efee4` | `57 ac 17 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005efbac`](#insn-005efbac) 範囲 `[['005efbac', '005efbd3']]`
  - `FALL_THROUGH` [`005efbd0`](#insn-005efbd0) → [`005efbd4`](#insn-005efbd4)
- ブロック [`005efbd4`](#insn-005efbd4) 範囲 `[['005efbd4', '005efbef']]`
  - `CONDITIONAL_JUMP` [`005efbec`](#insn-005efbec) → [`005efeb0`](#insn-005efeb0)
  - `FALL_THROUGH` [`005efbec`](#insn-005efbec) → [`005efbf0`](#insn-005efbf0)
- ブロック [`005efbf0`](#insn-005efbf0) 範囲 `[['005efbf0', '005efc3b']]`
  - `FALL_THROUGH` [`005efc38`](#insn-005efc38) → [`005efc3c`](#insn-005efc3c)
- ブロック [`005efc3c`](#insn-005efc3c) 範囲 `[['005efc3c', '005efc47']]`
  - `FALL_THROUGH` [`005efc44`](#insn-005efc44) → [`005efc48`](#insn-005efc48)
- ブロック [`005efc48`](#insn-005efc48) 範囲 `[['005efc48', '005efc5b']]`
  - `CONDITIONAL_JUMP` [`005efc58`](#insn-005efc58) → [`005efeb0`](#insn-005efeb0)
  - `FALL_THROUGH` [`005efc58`](#insn-005efc58) → [`005efc5c`](#insn-005efc5c)
- ブロック [`005efc5c`](#insn-005efc5c) 範囲 `[['005efc5c', '005efc6f']]`
  - `FALL_THROUGH` [`005efc6c`](#insn-005efc6c) → [`005efc70`](#insn-005efc70)
- ブロック [`005efc70`](#insn-005efc70) 範囲 `[['005efc70', '005efc7b']]`
  - `FALL_THROUGH` [`005efc78`](#insn-005efc78) → [`005efc7c`](#insn-005efc7c)
- ブロック [`005efc7c`](#insn-005efc7c) 範囲 `[['005efc7c', '005efca7']]`
  - `FALL_THROUGH` [`005efca4`](#insn-005efca4) → [`005efca8`](#insn-005efca8)
- ブロック [`005efca8`](#insn-005efca8) 範囲 `[['005efca8', '005efcab']]`
  - `FALL_THROUGH` [`005efca8`](#insn-005efca8) → [`005efcac`](#insn-005efcac)
- ブロック [`005efcac`](#insn-005efcac) 範囲 `[['005efcac', '005efcbb']]`
  - `FALL_THROUGH` [`005efcb8`](#insn-005efcb8) → [`005efcbc`](#insn-005efcbc)
- ブロック [`005efcbc`](#insn-005efcbc) 範囲 `[['005efcbc', '005efcd3']]`
  - `CONDITIONAL_JUMP` [`005efcd0`](#insn-005efcd0) → [`005efe60`](#insn-005efe60)
  - `FALL_THROUGH` [`005efcd0`](#insn-005efcd0) → [`005efcd4`](#insn-005efcd4)
- ブロック [`005efcd4`](#insn-005efcd4) 範囲 `[['005efcd4', '005efd03']]`
  - `FALL_THROUGH` [`005efd00`](#insn-005efd00) → [`005efd04`](#insn-005efd04)
- ブロック [`005efd04`](#insn-005efd04) 範囲 `[['005efd04', '005efd4b']]`
  - `FALL_THROUGH` [`005efd48`](#insn-005efd48) → [`005efd4c`](#insn-005efd4c)
- ブロック [`005efd4c`](#insn-005efd4c) 範囲 `[['005efd4c', '005efd8f']]`
  - `FALL_THROUGH` [`005efd8c`](#insn-005efd8c) → [`005efd90`](#insn-005efd90)
- ブロック [`005efd90`](#insn-005efd90) 範囲 `[['005efd90', '005efd9f']]`
  - `FALL_THROUGH` [`005efd9c`](#insn-005efd9c) → [`005efda0`](#insn-005efda0)
- ブロック [`005efda0`](#insn-005efda0) 範囲 `[['005efda0', '005efdab']]`
  - `FALL_THROUGH` [`005efda8`](#insn-005efda8) → [`005efdac`](#insn-005efdac)
- ブロック [`005efdac`](#insn-005efdac) 範囲 `[['005efdac', '005efdd3']]`
  - `CONDITIONAL_JUMP` [`005efdd0`](#insn-005efdd0) → [`005efeb0`](#insn-005efeb0)
  - `FALL_THROUGH` [`005efdd0`](#insn-005efdd0) → [`005efdd4`](#insn-005efdd4)
- ブロック [`005efdd4`](#insn-005efdd4) 範囲 `[['005efdd4', '005efdd7']]`
  - `FALL_THROUGH` [`005efdd4`](#insn-005efdd4) → [`005efdd8`](#insn-005efdd8)
- ブロック [`005efdd8`](#insn-005efdd8) 範囲 `[['005efdd8', '005efddf']]`
  - `CONDITIONAL_JUMP` [`005efddc`](#insn-005efddc) → [`005efe60`](#insn-005efe60)
  - `FALL_THROUGH` [`005efddc`](#insn-005efddc) → [`005efde0`](#insn-005efde0)
- ブロック [`005efde0`](#insn-005efde0) 範囲 `[['005efde0', '005efde7']]`
  - `FALL_THROUGH` [`005efde4`](#insn-005efde4) → [`005efde8`](#insn-005efde8)
- ブロック [`005efde8`](#insn-005efde8) 範囲 `[['005efde8', '005efdff']]`
  - `FALL_THROUGH` [`005efdfc`](#insn-005efdfc) → [`005efe00`](#insn-005efe00)
- ブロック [`005efe00`](#insn-005efe00) 範囲 `[['005efe00', '005efe2f']]`
  - `FALL_THROUGH` [`005efe2c`](#insn-005efe2c) → [`005efe30`](#insn-005efe30)
- ブロック [`005efe30`](#insn-005efe30) 範囲 `[['005efe30', '005efe5f']]`
  - `FALL_THROUGH` [`005efe5c`](#insn-005efe5c) → [`005efe60`](#insn-005efe60)
- ブロック [`005efe60`](#insn-005efe60) 範囲 `[['005efe60', '005efe6b']]`
  - `CONDITIONAL_JUMP` [`005efe68`](#insn-005efe68) → [`005efeb0`](#insn-005efeb0)
  - `FALL_THROUGH` [`005efe68`](#insn-005efe68) → [`005efe6c`](#insn-005efe6c)
- ブロック [`005efe6c`](#insn-005efe6c) 範囲 `[['005efe6c', '005efe7b']]`
  - `CONDITIONAL_JUMP` [`005efe78`](#insn-005efe78) → [`005efeb0`](#insn-005efeb0)
  - `FALL_THROUGH` [`005efe78`](#insn-005efe78) → [`005efe7c`](#insn-005efe7c)
- ブロック [`005efe7c`](#insn-005efe7c) 範囲 `[['005efe7c', '005efea7']]`
  - `FALL_THROUGH` [`005efea4`](#insn-005efea4) → [`005efea8`](#insn-005efea8)
- ブロック [`005efea8`](#insn-005efea8) 範囲 `[['005efea8', '005efeaf']]`
  - `FALL_THROUGH` [`005efeac`](#insn-005efeac) → [`005efeb0`](#insn-005efeb0)
- ブロック [`005efeb0`](#insn-005efeb0) 範囲 `[['005efeb0', '005efebf']]`
  - `CONDITIONAL_JUMP` [`005efebc`](#insn-005efebc) → [`005efee4`](#insn-005efee4)
  - `FALL_THROUGH` [`005efebc`](#insn-005efebc) → [`005efec0`](#insn-005efec0)
- ブロック [`005efec0`](#insn-005efec0) 範囲 `[['005efec0', '005efee3']]`
- ブロック [`005efee4`](#insn-005efee4) 範囲 `[['005efee4', '005efee7']]`

## 命令位置別の参照

- [`005efbb0`](#insn-005efbb0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbb4`](#insn-005efbb4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbb8`](#insn-005efbb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbbc`](#insn-005efbbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbc0`](#insn-005efbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbc4`](#insn-005efbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbc8`](#insn-005efbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbe0`](#insn-005efbe0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efbec`](#insn-005efbec) → [`005efeb0`](#insn-005efeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efc18`](#insn-005efc18) → [`00449aec`](../00449/00449aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449aec` · 推定シンボル `None` · 推定型 `None`
- [`005efc28`](#insn-005efc28) → `00c1b6a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`005efc40`](#insn-005efc40) → `00c24134`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`005efc4c`](#insn-005efc4c) → [`004460b0`](../00446/004460b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004460b0` · 推定シンボル `None` · 推定型 `None`
- [`005efc58`](#insn-005efc58) → [`005efeb0`](#insn-005efeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efc78`](#insn-005efc78) → [`00444c18`](../00444/00444c18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00444c18` · 推定シンボル `None` · 推定型 `None`
- [`005efc90`](#insn-005efc90) → [`00444c54`](../00444/00444c54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00444c54` · 推定シンボル `None` · 推定型 `None`
- [`005efc94`](#insn-005efc94) → `00c24134`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`005efca0`](#insn-005efca0) → [`00449aec`](../00449/00449aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449aec` · 推定シンボル `None` · 推定型 `None`
- [`005efcb8`](#insn-005efcb8) → [`0044507c`](../00445/0044507c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044507c` · 推定シンボル `None` · 推定型 `None`
- [`005efcc4`](#insn-005efcc4) → [`00444c18`](../00444/00444c18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00444c18` · 推定シンボル `None` · 推定型 `None`
- [`005efccc`](#insn-005efccc) → [`00a0b03c`](../00a0b/00a0b03c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a0b03c` · 推定シンボル `None` · 推定型 `None`
- [`005efcd0`](#insn-005efcd0) → [`005efe60`](#insn-005efe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efcd8`](#insn-005efcd8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005efcdc`](#insn-005efcdc) → [`00449aec`](../00449/00449aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449aec` · 推定シンボル `None` · 推定型 `None`
- [`005efce4`](#insn-005efce4) → `00c24134`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`005efcfc`](#insn-005efcfc) → [`00a0b818`](../00a0b/00a0b818.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a0b818` · 推定シンボル `None` · 推定型 `None`
- [`005efd10`](#insn-005efd10) → [`00467074`](../00467/00467074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467074` · 推定シンボル `None` · 推定型 `None`
- [`005efd24`](#insn-005efd24) → [`00467074`](../00467/00467074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467074` · 推定シンボル `None` · 推定型 `None`
- [`005efd64`](#insn-005efd64) → [`00448034`](../00448/00448034.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00448034` · 推定シンボル `None` · 推定型 `None`
- [`005efd6c`](#insn-005efd6c) → `Stack[-0x8c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efd78`](#insn-005efd78) → [`00467074`](../00467/00467074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467074` · 推定シンボル `None` · 推定型 `None`
- [`005efda4`](#insn-005efda4) → [`004460b0`](../00446/004460b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004460b0` · 推定シンボル `None` · 推定型 `None`
- [`005efdc4`](#insn-005efdc4) → [`004460b0`](../00446/004460b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004460b0` · 推定シンボル `None` · 推定型 `None`
- [`005efdd0`](#insn-005efdd0) → [`005efeb0`](#insn-005efeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efddc`](#insn-005efddc) → [`005efe60`](#insn-005efe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe04`](#insn-005efe04) → [`00467074`](../00467/00467074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467074` · 推定シンボル `None` · 推定型 `None`
- [`005efe0c`](#insn-005efe0c) → `003c336c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[47]`
- [`005efe5c`](#insn-005efe5c) → [`004460b0`](../00446/004460b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004460b0` · 推定シンボル `None` · 推定型 `None`
- [`005efe68`](#insn-005efe68) → [`005efeb0`](#insn-005efeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe74`](#insn-005efe74) → `0032e038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`005efe78`](#insn-005efe78) → [`005efeb0`](#insn-005efeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efe88`](#insn-005efe88) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`005efe94`](#insn-005efe94) → [`00883bb8`](../00883/00883bb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883bb8` · 推定シンボル `None` · 推定型 `None`
- [`005efea0`](#insn-005efea0) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`005efeac`](#insn-005efeac) → [`00883bb8`](../00883/00883bb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883bb8` · 推定シンボル `None` · 推定型 `None`
- [`005efeb4`](#insn-005efeb4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efebc`](#insn-005efebc) → [`005efee4`](#insn-005efee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efec0`](#insn-005efec0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efec4`](#insn-005efec4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efec8`](#insn-005efec8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efecc`](#insn-005efecc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed0`](#insn-005efed0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed4`](#insn-005efed4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efed8`](#insn-005efed8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005efee4`](#insn-005efee4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005efbb0`](#insn-005efbb0)

~~~json
{
  "source": "005efbb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbb4`](#insn-005efbb4)

~~~json
{
  "source": "005efbb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbb8`](#insn-005efbb8)

~~~json
{
  "source": "005efbb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbbc`](#insn-005efbbc)

~~~json
{
  "source": "005efbbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbc0`](#insn-005efbc0)

~~~json
{
  "source": "005efbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbc4`](#insn-005efbc4)

~~~json
{
  "source": "005efbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbc8`](#insn-005efbc8)

~~~json
{
  "source": "005efbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbe0`](#insn-005efbe0)

~~~json
{
  "source": "005efbe0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efbec`](#insn-005efbec)

~~~json
{
  "source": "005efbec",
  "target": "005efeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efc18`](#insn-005efc18)

~~~json
{
  "source": "005efc18",
  "target": "00449aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efc28`](#insn-005efc28)

~~~json
{
  "source": "005efc28",
  "target": "00c1b6a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b6a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005efc40`](#insn-005efc40)

~~~json
{
  "source": "005efc40",
  "target": "00c24134",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24134",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005efc4c`](#insn-005efc4c)

~~~json
{
  "source": "005efc4c",
  "target": "004460b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efc58`](#insn-005efc58)

~~~json
{
  "source": "005efc58",
  "target": "005efeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efc78`](#insn-005efc78)

~~~json
{
  "source": "005efc78",
  "target": "00444c18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efc90`](#insn-005efc90)

~~~json
{
  "source": "005efc90",
  "target": "00444c54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efc94`](#insn-005efc94)

~~~json
{
  "source": "005efc94",
  "target": "00c24134",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24134",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005efca0`](#insn-005efca0)

~~~json
{
  "source": "005efca0",
  "target": "00449aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efcb8`](#insn-005efcb8)

~~~json
{
  "source": "005efcb8",
  "target": "0044507c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efcc4`](#insn-005efcc4)

~~~json
{
  "source": "005efcc4",
  "target": "00444c18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efccc`](#insn-005efccc)

~~~json
{
  "source": "005efccc",
  "target": "00a0b03c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efcd0`](#insn-005efcd0)

~~~json
{
  "source": "005efcd0",
  "target": "005efe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efcd8`](#insn-005efcd8)

~~~json
{
  "source": "005efcd8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efcdc`](#insn-005efcdc)

~~~json
{
  "source": "005efcdc",
  "target": "00449aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efce4`](#insn-005efce4)

~~~json
{
  "source": "005efce4",
  "target": "00c24134",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24134",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005efcfc`](#insn-005efcfc)

~~~json
{
  "source": "005efcfc",
  "target": "00a0b818",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efd10`](#insn-005efd10)

~~~json
{
  "source": "005efd10",
  "target": "00467074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efd24`](#insn-005efd24)

~~~json
{
  "source": "005efd24",
  "target": "00467074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efd64`](#insn-005efd64)

~~~json
{
  "source": "005efd64",
  "target": "00448034",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efd6c`](#insn-005efd6c)

~~~json
{
  "source": "005efd6c",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efd78`](#insn-005efd78)

~~~json
{
  "source": "005efd78",
  "target": "00467074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efda4`](#insn-005efda4)

~~~json
{
  "source": "005efda4",
  "target": "004460b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efdc4`](#insn-005efdc4)

~~~json
{
  "source": "005efdc4",
  "target": "004460b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efdd0`](#insn-005efdd0)

~~~json
{
  "source": "005efdd0",
  "target": "005efeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efddc`](#insn-005efddc)

~~~json
{
  "source": "005efddc",
  "target": "005efe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe04`](#insn-005efe04)

~~~json
{
  "source": "005efe04",
  "target": "00467074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efe0c`](#insn-005efe0c)

~~~json
{
  "source": "005efe0c",
  "target": "003c336c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c3369",
  "offset": 3,
  "size": 47,
  "datatype": "byte[47]",
  "bytes": "442d440e40500c1d409302940495069608970a980c9e0e9d100a0334010c1f40",
  "capture_start": "003c3369",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`005efe5c`](#insn-005efe5c)

~~~json
{
  "source": "005efe5c",
  "target": "004460b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efe68`](#insn-005efe68)

~~~json
{
  "source": "005efe68",
  "target": "005efeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe74`](#insn-005efe74)

~~~json
{
  "source": "005efe74",
  "target": "0032e038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032e038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "402b0000",
  "capture_start": "0032e038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005efe78`](#insn-005efe78)

~~~json
{
  "source": "005efe78",
  "target": "005efeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efe88`](#insn-005efe88)

~~~json
{
  "source": "005efe88",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efe94`](#insn-005efe94)

~~~json
{
  "source": "005efe94",
  "target": "00883bb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efea0`](#insn-005efea0)

~~~json
{
  "source": "005efea0",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efeac`](#insn-005efeac)

~~~json
{
  "source": "005efeac",
  "target": "00883bb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005efeb4`](#insn-005efeb4)

~~~json
{
  "source": "005efeb4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efebc`](#insn-005efebc)

~~~json
{
  "source": "005efebc",
  "target": "005efee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efec0`](#insn-005efec0)

~~~json
{
  "source": "005efec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efec4`](#insn-005efec4)

~~~json
{
  "source": "005efec4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efec8`](#insn-005efec8)

~~~json
{
  "source": "005efec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efecc`](#insn-005efecc)

~~~json
{
  "source": "005efecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed0`](#insn-005efed0)

~~~json
{
  "source": "005efed0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed4`](#insn-005efed4)

~~~json
{
  "source": "005efed4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efed8`](#insn-005efed8)

~~~json
{
  "source": "005efed8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005efee4`](#insn-005efee4)

~~~json
{
  "source": "005efee4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
