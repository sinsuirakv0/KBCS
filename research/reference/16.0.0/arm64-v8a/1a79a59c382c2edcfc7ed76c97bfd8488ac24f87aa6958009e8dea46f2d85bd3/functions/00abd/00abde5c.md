# 00abde5c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5fea4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-e2fb6f9bf622d3c0f37c1f6e5c144038)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abe058`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe058.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-fed1cd6c07ceead1cf3e0fb424ee16a9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abde5c",
  "name": "FUN_00abde5c",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbcd21db6de30a07d00b8720eb7e552d1e78aaf258ea455ee6d4b8f4f90fbc5",
  "source_text_sha256": "5fbcd21db6de30a07d00b8720eb7e552d1e78aaf258ea455ee6d4b8f4f90fbc5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abde5c",
        "00abe0b3"
      ]
    ],
    "bytes_sha256": "af85ea27b05ec0fcd41e56e402ccb3054c10d6c1fa1bfd697c284dcd06fbd35b",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a26020](../00a26/00a26020.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [004800d8](../00480/004800d8.md)
- [00480138](../00480/00480138.md)
- [004802b8](../00480/004802b8.md)
- [004803b0](../00480/004803b0.md)
- [005c175c](../005c1/005c175c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5056 bytes

~~~c

void FUN_00abde5c(long param_1,undefined8 param_2)

{
  ulong uVar1;
  int *piVar2;
  int *piVar3;
  int iVar4;
  char cVar5;
  byte bVar6;
  short sVar7;
  short sVar8;
  undefined4 uVar9;
  undefined8 *puVar10;
  void *__dest;
  undefined8 *puVar11;
  long *plVar12;
  ulong uVar13;
  ulong uVar14;
  undefined8 *puVar15;
  long *plVar16;
  void *__src;
  undefined8 *puVar17;
  int iVar18;
  int *piVar19;
  long lVar20;
  undefined8 *puVar21;
  
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 0x60) = uVar9;
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 100) = uVar9;
                    /* catch() { ... } // from try @ 00abdc80 with catch @ 00abde9c */
  uVar9 = FUN_004803b0(param_2);
  *(undefined4 *)(param_1 + 0x68) = uVar9;
  sVar7 = FUN_00480138(param_2);
                    /* catch() { ... } // from try @ 00abdda4 with catch @ 00abdeb0 */
  iVar18 = (int)sVar7;
  puVar15 = (undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *puVar15;
  if (0 < iVar18) {
    do {
      sVar7 = FUN_00480138(param_2);
      piVar3 = *(int **)(param_1 + 0x38);
                    /* try { // try from 00abdfe0 to 00bbe09f has its CatchHandler @ 00abdee0 */
      if (piVar3 < *(int **)(param_1 + 0x40)) {
        piVar19 = piVar3 + 1;
        *piVar3 = (int)sVar7;
      }
      else {
        __src = (void *)*puVar15;
        lVar20 = (long)piVar3 - (long)__src >> 2;
        uVar1 = lVar20 + 1;
        if (uVar1 >> 0x3e != 0) {
                    /* try { // try from 00abe0a8 to 00bbe143 has its CatchHandler @ 00abdee0 */
                    /* WARNING: Subroutine does not return */
          FUN_00470800(puVar15);
        }
        uVar13 = (long)*(int **)(param_1 + 0x40) - (long)__src;
        uVar14 = (long)uVar13 >> 1;
        if (uVar14 <= uVar1) {
          uVar14 = uVar1;
        }
        if (0x7ffffffffffffffb < uVar13) {
          uVar14 = 0x3fffffffffffffff;
        }
        if (uVar14 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar14 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00440e80();
          }
          __dest = (void *)_Znwm(uVar14 << 2);
        }
        piVar2 = (int *)((long)__dest + lVar20 * 4);
        piVar19 = piVar2 + 1;
        *piVar2 = (int)sVar7;
        memcpy(__dest,__src,(long)piVar3 - (long)__src);
        *(void **)(param_1 + 0x30) = __dest;
        *(int **)(param_1 + 0x38) = piVar19;
        *(void **)(param_1 + 0x40) = (void *)((long)__dest + uVar14 * 4);
        if (__src != (void *)0x0) {
          _ZdlPv(__src);
        }
      }
      iVar18 = iVar18 + -1;
      *(int **)(param_1 + 0x38) = piVar19;
    } while (iVar18 != 0);
  }
  sVar7 = FUN_00480138(param_2);
  puVar15 = (undefined8 *)(param_1 + 0x50);
  plVar16 = (long *)(param_1 + 0x48);
                    /* try { // try from 00abdee0 to 00bbdfbb has its CatchHandler @ 00abdee0
                       catch() { ... } // from try @ 00abdee0 with catch @ 00abdee0
                       catch() { ... } // from try @ 00abdfe0 with catch @ 00abdee0
                       catch() { ... } // from try @ 00abe0a8 with catch @ 00abdee0 */
  FUN_005c175c(plVar16,*puVar15);
  *puVar15 = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 **)(param_1 + 0x48) = puVar15;
  if (0 < sVar7) {
    iVar18 = 0;
    do {
      sVar8 = FUN_00480138(param_2);
      iVar4 = (int)sVar8;
      cVar5 = FUN_004800d8(param_2);
      puVar11 = (undefined8 *)*puVar15;
      puVar17 = puVar15;
      puVar21 = puVar15;
      if ((undefined8 *)*puVar15 != (undefined8 *)0x0) {
        do {
          while (puVar10 = puVar11, puVar17 = puVar10, iVar4 < *(int *)((long)puVar10 + 0x1c)) {
            puVar11 = (undefined8 *)*puVar10;
            puVar21 = puVar10;
            if ((undefined8 *)*puVar10 == (undefined8 *)0x0) goto LAB_00abdf88;
          }
          if (iVar4 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00abdf18;
          puVar11 = (undefined8 *)puVar10[1];
        } while ((undefined8 *)puVar10[1] != (undefined8 *)0x0);
        puVar21 = puVar10 + 1;
      }
LAB_00abdf88:
      puVar10 = (undefined8 *)_Znwm(0x28);
      *puVar10 = 0;
      puVar10[1] = 0;
      puVar10[2] = puVar17;
      *puVar21 = puVar10;
      plVar12 = (long *)*plVar16;
      *(int *)((long)puVar10 + 0x1c) = iVar4;
      *(undefined4 *)(puVar10 + 4) = 0;
      puVar11 = puVar10;
      if (*plVar12 != 0) {
        *plVar16 = *plVar12;
                    /* try { // try from 00abdfbc to 00bbdfdf has its CatchHandler @ 00abe0f4 */
        puVar11 = (undefined8 *)*puVar21;
      }
      FUN_0043bb64(*(undefined8 *)(param_1 + 0x50),puVar11);
      *(long *)(param_1 + 0x58) = *(long *)(param_1 + 0x58) + 1;
LAB_00abdf18:
      iVar18 = iVar18 + 1;
      *(int *)(puVar10 + 4) = (int)cVar5;
    } while (iVar18 != sVar7);
  }
  bVar6 = FUN_004802b8(param_2);
  *(byte *)(param_1 + 0x6c) = bVar6 & 1;
                    /* try { // try from 00abe0a0 to 00bbe0a7 has its CatchHandler @ 00abe0d8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abde5c"></a> `00abde5c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abde60"></a> `00abde60` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abde64"></a> `00abde64` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abde68"></a> `00abde68` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abde6c"></a> `00abde6c` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abde70"></a> `00abde70` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abde74"></a> `00abde74` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abde78"></a> `00abde78` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abde7c"></a> `00abde7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abde80"></a> `00abde80` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00abde84"></a> `00abde84` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00abde88"></a> `00abde88` | `4a 09 e7 97` | bl 0x004803b0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde8c"></a> `00abde8c` | `60 62 00 b9` | str w0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00abde90"></a> `00abde90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abde94"></a> `00abde94` | `47 09 e7 97` | bl 0x004803b0 | `UNCONDITIONAL_CALL`
<a id="insn-00abde98"></a> `00abde98` | `60 66 00 b9` | str w0,[x19, #0x64] | `FALL_THROUGH`
<a id="insn-00abde9c"></a> `00abde9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdea0"></a> `00abdea0` | `44 09 e7 97` | bl 0x004803b0 | `UNCONDITIONAL_CALL`
<a id="insn-00abdea4"></a> `00abdea4` | `60 6a 00 b9` | str w0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abdea8"></a> `00abdea8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdeac"></a> `00abdeac` | `a3 08 e7 97` | bl 0x00480138 | `UNCONDITIONAL_CALL`
<a id="insn-00abdeb0"></a> `00abdeb0` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00abdeb4"></a> `00abdeb4` | `19 3c 00 13` | sxth w25,w0 | `FALL_THROUGH`
<a id="insn-00abdeb8"></a> `00abdeb8` | `a8 0e 43 f8` | ldr x8,[x21, #0x30]! | `FALL_THROUGH`
<a id="insn-00abdebc"></a> `00abdebc` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00abdec0"></a> `00abdec0` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00abdec4"></a> `00abdec4` | `8a 08 00 54` | b.ge 0x00abdfd4 | `CONDITIONAL_JUMP`
<a id="insn-00abdec8"></a> `00abdec8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdecc"></a> `00abdecc` | `9b 08 e7 97` | bl 0x00480138 | `UNCONDITIONAL_CALL`
<a id="insn-00abded0"></a> `00abded0` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00abded4"></a> `00abded4` | `16 3c 00 13` | sxth w22,w0 | `FALL_THROUGH`
<a id="insn-00abded8"></a> `00abded8` | `01 0f 45 f8` | ldr x1,[x24, #0x50]! | `FALL_THROUGH`
<a id="insn-00abdedc"></a> `00abdedc` | `15 23 00 d1` | sub x21,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00abdee0"></a> `00abdee0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abdee4"></a> `00abdee4` | `1e 0e ec 97` | bl 0x005c175c | `UNCONDITIONAL_CALL`
<a id="insn-00abdee8"></a> `00abdee8` | `df 06 00 71` | cmp w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abdeec"></a> `00abdeec` | `1f 7f 00 a9` | stp xzr,xzr,[x24] | `FALL_THROUGH`
<a id="insn-00abdef0"></a> `00abdef0` | `b6 c3 1f b8` | stur w22,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00abdef4"></a> `00abdef4` | `18 83 1f f8` | stur x24,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00abdef8"></a> `00abdef8` | `0b 0c 00 54` | b.lt 0x00abe078 | `CONDITIONAL_JUMP`
<a id="insn-00abdefc"></a> `00abdefc` | `fa 03 1f 2a` | mov w26,wzr | `FALL_THROUGH`
<a id="insn-00abdf00"></a> `00abdf00` | `0c 00 00 14` | b 0x00abdf30 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdf04"></a> `00abdf04` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00abdf08"></a> `00abdf08` | `17 f7 e5 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf0c"></a> `00abdf0c` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abdf10"></a> `00abdf10` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abdf14"></a> `00abdf14` | `68 2e 00 f9` | str x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abdf18"></a> `00abdf18` | `a9 c3 5f b8` | ldur w9,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00abdf1c"></a> `00abdf1c` | `c8 1e 00 13` | sxtb w8,w22 | `FALL_THROUGH`
<a id="insn-00abdf20"></a> `00abdf20` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00abdf24"></a> `00abdf24` | `5f 03 09 6b` | cmp w26,w9 | `FALL_THROUGH`
<a id="insn-00abdf28"></a> `00abdf28` | `e8 22 00 b9` | str w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00abdf2c"></a> `00abdf2c` | `60 0a 00 54` | b.eq 0x00abe078 | `CONDITIONAL_JUMP`
<a id="insn-00abdf30"></a> `00abdf30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdf34"></a> `00abdf34` | `81 08 e7 97` | bl 0x00480138 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf38"></a> `00abdf38` | `1b 3c 00 13` | sxth w27,w0 | `FALL_THROUGH`
<a id="insn-00abdf3c"></a> `00abdf3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdf40"></a> `00abdf40` | `66 08 e7 97` | bl 0x004800d8 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf44"></a> `00abdf44` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00abdf48"></a> `00abdf48` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00abdf4c"></a> `00abdf4c` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00abdf50"></a> `00abdf50` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00abdf54"></a> `00abdf54` | `a8 00 00 b5` | cbnz x8,0x00abdf68 | `CONDITIONAL_JUMP`
<a id="insn-00abdf58"></a> `00abdf58` | `0c 00 00 14` | b 0x00abdf88 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdf5c"></a> `00abdf5c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abdf60"></a> `00abdf60` | `fc 03 17 aa` | mov x28,x23 | `FALL_THROUGH`
<a id="insn-00abdf64"></a> `00abdf64` | `28 01 00 b4` | cbz x8,0x00abdf88 | `CONDITIONAL_JUMP`
<a id="insn-00abdf68"></a> `00abdf68` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abdf6c"></a> `00abdf6c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abdf70"></a> `00abdf70` | `1f 01 1b 6b` | cmp w8,w27 | `FALL_THROUGH`
<a id="insn-00abdf74"></a> `00abdf74` | `4c ff ff 54` | b.gt 0x00abdf5c | `CONDITIONAL_JUMP`
<a id="insn-00abdf78"></a> `00abdf78` | `0a fd ff 54` | b.ge 0x00abdf18 | `CONDITIONAL_JUMP`
<a id="insn-00abdf7c"></a> `00abdf7c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00abdf80"></a> `00abdf80` | `48 ff ff b5` | cbnz x8,0x00abdf68 | `CONDITIONAL_JUMP`
<a id="insn-00abdf84"></a> `00abdf84` | `fc 22 00 91` | add x28,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abdf88"></a> `00abdf88` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abdf8c"></a> `00abdf8c` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00abdf90"></a> `00abdf90` | `c0 66 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abdf94"></a> `00abdf94` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abdf98"></a> `00abdf98` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abdf9c"></a> `00abdf9c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abdfa0"></a> `00abdfa0` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abdfa4"></a> `00abdfa4` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00abdfa8"></a> `00abdfa8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abdfac"></a> `00abdfac` | `1b fc 03 29` | stp w27,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abdfb0"></a> `00abdfb0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abdfb4"></a> `00abdfb4` | `88 fa ff b4` | cbz x8,0x00abdf04 | `CONDITIONAL_JUMP`
<a id="insn-00abdfb8"></a> `00abdfb8` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00abdfbc"></a> `00abdfbc` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00abdfc0"></a> `00abdfc0` | `d1 ff ff 17` | b 0x00abdf04 | `UNCONDITIONAL_JUMP`
<a id="insn-00abdfc4"></a> `00abdfc4` | `5c 47 00 b8` | str w28,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00abdfc8"></a> `00abdfc8` | `39 07 00 71` | subs w25,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00abdfcc"></a> `00abdfcc` | `7a 1e 00 f9` | str x26,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abdfd0"></a> `00abdfd0` | `c0 f7 ff 54` | b.eq 0x00abdec8 | `CONDITIONAL_JUMP`
<a id="insn-00abdfd4"></a> `00abdfd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abdfd8"></a> `00abdfd8` | `58 08 e7 97` | bl 0x00480138 | `UNCONDITIONAL_CALL`
<a id="insn-00abdfdc"></a> `00abdfdc` | `7a a2 43 a9` | ldp x26,x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abdfe0"></a> `00abdfe0` | `1c 3c 00 13` | sxth w28,w0 | `FALL_THROUGH`
<a id="insn-00abdfe4"></a> `00abdfe4` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00abdfe8"></a> `00abdfe8` | `e3 fe ff 54` | b.cc 0x00abdfc4 | `CONDITIONAL_JUMP`
<a id="insn-00abdfec"></a> `00abdfec` | `b6 02 40 f9` | ldr x22,[x21] | `FALL_THROUGH`
<a id="insn-00abdff0"></a> `00abdff0` | `57 03 16 cb` | sub x23,x26,x22 | `FALL_THROUGH`
<a id="insn-00abdff4"></a> `00abdff4` | `fa fe 42 93` | asr x26,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00abdff8"></a> `00abdff8` | `49 07 00 91` | add x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00abdffc"></a> `00abdffc` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00abe000"></a> `00abe000` | `4a 05 00 b5` | cbnz x10,0x00abe0a8 | `CONDITIONAL_JUMP`
<a id="insn-00abe004"></a> `00abe004` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00abe008"></a> `00abe008` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abe00c"></a> `00abe00c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00abe010"></a> `00abe010` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00abe014"></a> `00abe014` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00abe018"></a> `00abe018` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abe01c"></a> `00abe01c` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abe020"></a> `00abe020` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00abe024"></a> `00abe024` | `fb 00 00 b4` | cbz x27,0x00abe040 | `CONDITIONAL_JUMP`
<a id="insn-00abe028"></a> `00abe028` | `68 ff 7e d3` | lsr x8,x27,#0x3e | `FALL_THROUGH`
<a id="insn-00abe02c"></a> `00abe02c` | `28 04 00 b5` | cbnz x8,0x00abe0b0 | `CONDITIONAL_JUMP`
<a id="insn-00abe030"></a> `00abe030` | `60 f7 7e d3` | lsl x0,x27,#0x2 | `FALL_THROUGH`
<a id="insn-00abe034"></a> `00abe034` | `97 66 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abe038"></a> `00abe038` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00abe03c"></a> `00abe03c` | `02 00 00 14` | b 0x00abe044 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe040"></a> `00abe040` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00abe044"></a> `00abe044` | `1a 0b 1a 8b` | add x26,x24,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abe048"></a> `00abe048` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abe04c"></a> `00abe04c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00abe050"></a> `00abe050` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00abe054"></a> `00abe054` | `1b 0b 1b 8b` | add x27,x24,x27, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abe058"></a> `00abe058` | `5c 47 00 b8` | str w28,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00abe05c"></a> `00abe05c` | `e9 66 06 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00abe060"></a> `00abe060` | `78 6a 03 a9` | stp x24,x26,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00abe064"></a> `00abe064` | `7b 22 00 f9` | str x27,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00abe068"></a> `00abe068` | `16 fb ff b4` | cbz x22,0x00abdfc8 | `CONDITIONAL_JUMP`
<a id="insn-00abe06c"></a> `00abe06c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abe070"></a> `00abe070` | `90 66 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe074"></a> `00abe074` | `d5 ff ff 17` | b 0x00abdfc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe078"></a> `00abe078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abe07c"></a> `00abe07c` | `8f 08 e7 97` | bl 0x004802b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe080"></a> `00abe080` | `08 00 00 12` | and w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abe084"></a> `00abe084` | `68 b2 01 39` | strb w8,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abe088"></a> `00abe088` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abe08c"></a> `00abe08c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abe090"></a> `00abe090` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abe094"></a> `00abe094` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abe098"></a> `00abe098` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abe09c"></a> `00abe09c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abe0a0"></a> `00abe0a0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abe0a4"></a> `00abe0a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abe0a8"></a> `00abe0a8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abe0ac"></a> `00abe0ac` | `d5 c9 e6 97` | bl 0x00470800 | `CALL_TERMINATOR`
<a id="insn-00abe0b0"></a> `00abe0b0` | `74 0b e6 97` | bl 0x00440e80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abde5c`](#insn-00abde5c) 範囲 `[['00abde5c', '00abde9b']]`
  - `FALL_THROUGH` [`00abde98`](#insn-00abde98) → [`00abde9c`](#insn-00abde9c)
- ブロック [`00abde9c`](#insn-00abde9c) 範囲 `[['00abde9c', '00abdeaf']]`
  - `FALL_THROUGH` [`00abdeac`](#insn-00abdeac) → [`00abdeb0`](#insn-00abdeb0)
- ブロック [`00abdeb0`](#insn-00abdeb0) 範囲 `[['00abdeb0', '00abdec7']]`
  - `CONDITIONAL_JUMP` [`00abdec4`](#insn-00abdec4) → [`00abdfd4`](#insn-00abdfd4)
  - `FALL_THROUGH` [`00abdec4`](#insn-00abdec4) → [`00abdec8`](#insn-00abdec8)
- ブロック [`00abdec8`](#insn-00abdec8) 範囲 `[['00abdec8', '00abdedf']]`
  - `FALL_THROUGH` [`00abdedc`](#insn-00abdedc) → [`00abdee0`](#insn-00abdee0)
- ブロック [`00abdee0`](#insn-00abdee0) 範囲 `[['00abdee0', '00abdefb']]`
  - `CONDITIONAL_JUMP` [`00abdef8`](#insn-00abdef8) → [`00abe078`](#insn-00abe078)
  - `FALL_THROUGH` [`00abdef8`](#insn-00abdef8) → [`00abdefc`](#insn-00abdefc)
- ブロック [`00abdefc`](#insn-00abdefc) 範囲 `[['00abdefc', '00abdf03']]`
  - `UNCONDITIONAL_JUMP` [`00abdf00`](#insn-00abdf00) → [`00abdf30`](#insn-00abdf30)
- ブロック [`00abdf04`](#insn-00abdf04) 範囲 `[['00abdf04', '00abdf17']]`
  - `FALL_THROUGH` [`00abdf14`](#insn-00abdf14) → [`00abdf18`](#insn-00abdf18)
- ブロック [`00abdf18`](#insn-00abdf18) 範囲 `[['00abdf18', '00abdf2f']]`
  - `CONDITIONAL_JUMP` [`00abdf2c`](#insn-00abdf2c) → [`00abe078`](#insn-00abe078)
  - `FALL_THROUGH` [`00abdf2c`](#insn-00abdf2c) → [`00abdf30`](#insn-00abdf30)
- ブロック [`00abdf30`](#insn-00abdf30) 範囲 `[['00abdf30', '00abdf57']]`
  - `CONDITIONAL_JUMP` [`00abdf54`](#insn-00abdf54) → [`00abdf68`](#insn-00abdf68)
  - `FALL_THROUGH` [`00abdf54`](#insn-00abdf54) → [`00abdf58`](#insn-00abdf58)
- ブロック [`00abdf58`](#insn-00abdf58) 範囲 `[['00abdf58', '00abdf5b']]`
  - `UNCONDITIONAL_JUMP` [`00abdf58`](#insn-00abdf58) → [`00abdf88`](#insn-00abdf88)
- ブロック [`00abdf5c`](#insn-00abdf5c) 範囲 `[['00abdf5c', '00abdf67']]`
  - `CONDITIONAL_JUMP` [`00abdf64`](#insn-00abdf64) → [`00abdf88`](#insn-00abdf88)
  - `FALL_THROUGH` [`00abdf64`](#insn-00abdf64) → [`00abdf68`](#insn-00abdf68)
- ブロック [`00abdf68`](#insn-00abdf68) 範囲 `[['00abdf68', '00abdf77']]`
  - `CONDITIONAL_JUMP` [`00abdf74`](#insn-00abdf74) → [`00abdf5c`](#insn-00abdf5c)
  - `FALL_THROUGH` [`00abdf74`](#insn-00abdf74) → [`00abdf78`](#insn-00abdf78)
- ブロック [`00abdf78`](#insn-00abdf78) 範囲 `[['00abdf78', '00abdf7b']]`
  - `CONDITIONAL_JUMP` [`00abdf78`](#insn-00abdf78) → [`00abdf18`](#insn-00abdf18)
  - `FALL_THROUGH` [`00abdf78`](#insn-00abdf78) → [`00abdf7c`](#insn-00abdf7c)
- ブロック [`00abdf7c`](#insn-00abdf7c) 範囲 `[['00abdf7c', '00abdf83']]`
  - `CONDITIONAL_JUMP` [`00abdf80`](#insn-00abdf80) → [`00abdf68`](#insn-00abdf68)
  - `FALL_THROUGH` [`00abdf80`](#insn-00abdf80) → [`00abdf84`](#insn-00abdf84)
- ブロック [`00abdf84`](#insn-00abdf84) 範囲 `[['00abdf84', '00abdf87']]`
  - `FALL_THROUGH` [`00abdf84`](#insn-00abdf84) → [`00abdf88`](#insn-00abdf88)
- ブロック [`00abdf88`](#insn-00abdf88) 範囲 `[['00abdf88', '00abdfb7']]`
  - `CONDITIONAL_JUMP` [`00abdfb4`](#insn-00abdfb4) → [`00abdf04`](#insn-00abdf04)
  - `FALL_THROUGH` [`00abdfb4`](#insn-00abdfb4) → [`00abdfb8`](#insn-00abdfb8)
- ブロック [`00abdfb8`](#insn-00abdfb8) 範囲 `[['00abdfb8', '00abdfbb']]`
  - `FALL_THROUGH` [`00abdfb8`](#insn-00abdfb8) → [`00abdfbc`](#insn-00abdfbc)
- ブロック [`00abdfbc`](#insn-00abdfbc) 範囲 `[['00abdfbc', '00abdfc3']]`
  - `UNCONDITIONAL_JUMP` [`00abdfc0`](#insn-00abdfc0) → [`00abdf04`](#insn-00abdf04)
- ブロック [`00abdfc4`](#insn-00abdfc4) 範囲 `[['00abdfc4', '00abdfc7']]`
  - `FALL_THROUGH` [`00abdfc4`](#insn-00abdfc4) → [`00abdfc8`](#insn-00abdfc8)
- ブロック [`00abdfc8`](#insn-00abdfc8) 範囲 `[['00abdfc8', '00abdfd3']]`
  - `CONDITIONAL_JUMP` [`00abdfd0`](#insn-00abdfd0) → [`00abdec8`](#insn-00abdec8)
  - `FALL_THROUGH` [`00abdfd0`](#insn-00abdfd0) → [`00abdfd4`](#insn-00abdfd4)
- ブロック [`00abdfd4`](#insn-00abdfd4) 範囲 `[['00abdfd4', '00abdfdf']]`
  - `FALL_THROUGH` [`00abdfdc`](#insn-00abdfdc) → [`00abdfe0`](#insn-00abdfe0)
- ブロック [`00abdfe0`](#insn-00abdfe0) 範囲 `[['00abdfe0', '00abdfeb']]`
  - `CONDITIONAL_JUMP` [`00abdfe8`](#insn-00abdfe8) → [`00abdfc4`](#insn-00abdfc4)
  - `FALL_THROUGH` [`00abdfe8`](#insn-00abdfe8) → [`00abdfec`](#insn-00abdfec)
- ブロック [`00abdfec`](#insn-00abdfec) 範囲 `[['00abdfec', '00abe003']]`
  - `CONDITIONAL_JUMP` [`00abe000`](#insn-00abe000) → [`00abe0a8`](#insn-00abe0a8)
  - `FALL_THROUGH` [`00abe000`](#insn-00abe000) → [`00abe004`](#insn-00abe004)
- ブロック [`00abe004`](#insn-00abe004) 範囲 `[['00abe004', '00abe027']]`
  - `CONDITIONAL_JUMP` [`00abe024`](#insn-00abe024) → [`00abe040`](#insn-00abe040)
  - `FALL_THROUGH` [`00abe024`](#insn-00abe024) → [`00abe028`](#insn-00abe028)
- ブロック [`00abe028`](#insn-00abe028) 範囲 `[['00abe028', '00abe02f']]`
  - `CONDITIONAL_JUMP` [`00abe02c`](#insn-00abe02c) → [`00abe0b0`](#insn-00abe0b0)
  - `FALL_THROUGH` [`00abe02c`](#insn-00abe02c) → [`00abe030`](#insn-00abe030)
- ブロック [`00abe030`](#insn-00abe030) 範囲 `[['00abe030', '00abe03f']]`
  - `UNCONDITIONAL_JUMP` [`00abe03c`](#insn-00abe03c) → [`00abe044`](#insn-00abe044)
- ブロック [`00abe040`](#insn-00abe040) 範囲 `[['00abe040', '00abe043']]`
  - `FALL_THROUGH` [`00abe040`](#insn-00abe040) → [`00abe044`](#insn-00abe044)
- ブロック [`00abe044`](#insn-00abe044) 範囲 `[['00abe044', '00abe06b']]`
  - `CONDITIONAL_JUMP` [`00abe068`](#insn-00abe068) → [`00abdfc8`](#insn-00abdfc8)
  - `FALL_THROUGH` [`00abe068`](#insn-00abe068) → [`00abe06c`](#insn-00abe06c)
- ブロック [`00abe06c`](#insn-00abe06c) 範囲 `[['00abe06c', '00abe077']]`
  - `UNCONDITIONAL_JUMP` [`00abe074`](#insn-00abe074) → [`00abdfc8`](#insn-00abdfc8)
- ブロック [`00abe078`](#insn-00abe078) 範囲 `[['00abe078', '00abe09f']]`
  - `FALL_THROUGH` [`00abe09c`](#insn-00abe09c) → [`00abe0a0`](#insn-00abe0a0)
- ブロック [`00abe0a0`](#insn-00abe0a0) 範囲 `[['00abe0a0', '00abe0a7']]`
- ブロック [`00abe0a8`](#insn-00abe0a8) 範囲 `[['00abe0a8', '00abe0af']]`
- ブロック [`00abe0b0`](#insn-00abe0b0) 範囲 `[['00abe0b0', '00abe0b3']]`

## 命令位置別の参照

- [`00abde60`](#insn-00abde60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde64`](#insn-00abde64) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde68`](#insn-00abde68) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde6c`](#insn-00abde6c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde70`](#insn-00abde70) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde74`](#insn-00abde74) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abde88`](#insn-00abde88) → [`004803b0`](../00480/004803b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803b0` · 推定シンボル `None` · 推定型 `None`
- [`00abde94`](#insn-00abde94) → [`004803b0`](../00480/004803b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803b0` · 推定シンボル `None` · 推定型 `None`
- [`00abdea0`](#insn-00abdea0) → [`004803b0`](../00480/004803b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004803b0` · 推定シンボル `None` · 推定型 `None`
- [`00abdeac`](#insn-00abdeac) → [`00480138`](../00480/00480138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480138` · 推定シンボル `None` · 推定型 `None`
- [`00abdec4`](#insn-00abdec4) → [`00abdfd4`](#insn-00abdfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdecc`](#insn-00abdecc) → [`00480138`](../00480/00480138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480138` · 推定シンボル `None` · 推定型 `None`
- [`00abdee4`](#insn-00abdee4) → [`005c175c`](../005c1/005c175c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c175c` · 推定シンボル `None` · 推定型 `None`
- [`00abdef0`](#insn-00abdef0) → `Stack[-0x64]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdef8`](#insn-00abdef8) → [`00abe078`](#insn-00abe078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf00`](#insn-00abdf00) → [`00abdf30`](#insn-00abdf30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf08`](#insn-00abdf08) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00abdf18`](#insn-00abdf18) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf2c`](#insn-00abdf2c) → [`00abe078`](#insn-00abe078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf34`](#insn-00abdf34) → [`00480138`](../00480/00480138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480138` · 推定シンボル `None` · 推定型 `None`
- [`00abdf40`](#insn-00abdf40) → [`004800d8`](../00480/004800d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004800d8` · 推定シンボル `None` · 推定型 `None`
- [`00abdf54`](#insn-00abdf54) → [`00abdf68`](#insn-00abdf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf58`](#insn-00abdf58) → [`00abdf88`](#insn-00abdf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf64`](#insn-00abdf64) → [`00abdf88`](#insn-00abdf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf74`](#insn-00abdf74) → [`00abdf5c`](#insn-00abdf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf78`](#insn-00abdf78) → [`00abdf18`](#insn-00abdf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf80`](#insn-00abdf80) → [`00abdf68`](#insn-00abdf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdf90`](#insn-00abdf90) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abdfb4`](#insn-00abdfb4) → [`00abdf04`](#insn-00abdf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdfc0`](#insn-00abdfc0) → [`00abdf04`](#insn-00abdf04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdfd0`](#insn-00abdfd0) → [`00abdec8`](#insn-00abdec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abdfd8`](#insn-00abdfd8) → [`00480138`](../00480/00480138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480138` · 推定シンボル `None` · 推定型 `None`
- [`00abdfe8`](#insn-00abdfe8) → [`00abdfc4`](#insn-00abdfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe000`](#insn-00abe000) → [`00abe0a8`](#insn-00abe0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe024`](#insn-00abe024) → [`00abe040`](#insn-00abe040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe02c`](#insn-00abe02c) → [`00abe0b0`](#insn-00abe0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe034`](#insn-00abe034) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abe03c`](#insn-00abe03c) → [`00abe044`](#insn-00abe044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe05c`](#insn-00abe05c) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00abe068`](#insn-00abe068) → [`00abdfc8`](#insn-00abdfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe070`](#insn-00abe070) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abe074`](#insn-00abe074) → [`00abdfc8`](#insn-00abdfc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe07c`](#insn-00abe07c) → [`004802b8`](../00480/004802b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004802b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe088`](#insn-00abe088) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe08c`](#insn-00abe08c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe090`](#insn-00abe090) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe094`](#insn-00abe094) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe098`](#insn-00abe098) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe09c`](#insn-00abe09c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe0ac`](#insn-00abe0ac) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`
- [`00abe0b0`](#insn-00abe0b0) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abde60`](#insn-00abde60)

~~~json
{
  "source": "00abde60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde64`](#insn-00abde64)

~~~json
{
  "source": "00abde64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde68`](#insn-00abde68)

~~~json
{
  "source": "00abde68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde6c`](#insn-00abde6c)

~~~json
{
  "source": "00abde6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde70`](#insn-00abde70)

~~~json
{
  "source": "00abde70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde74`](#insn-00abde74)

~~~json
{
  "source": "00abde74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abde88`](#insn-00abde88)

~~~json
{
  "source": "00abde88",
  "target": "004803b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abde94`](#insn-00abde94)

~~~json
{
  "source": "00abde94",
  "target": "004803b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdea0`](#insn-00abdea0)

~~~json
{
  "source": "00abdea0",
  "target": "004803b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdeac`](#insn-00abdeac)

~~~json
{
  "source": "00abdeac",
  "target": "00480138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdec4`](#insn-00abdec4)

~~~json
{
  "source": "00abdec4",
  "target": "00abdfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdecc`](#insn-00abdecc)

~~~json
{
  "source": "00abdecc",
  "target": "00480138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdee4`](#insn-00abdee4)

~~~json
{
  "source": "00abdee4",
  "target": "005c175c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdef0`](#insn-00abdef0)

~~~json
{
  "source": "00abdef0",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdef8`](#insn-00abdef8)

~~~json
{
  "source": "00abdef8",
  "target": "00abe078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf00`](#insn-00abdf00)

~~~json
{
  "source": "00abdf00",
  "target": "00abdf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf08`](#insn-00abdf08)

~~~json
{
  "source": "00abdf08",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf18`](#insn-00abdf18)

~~~json
{
  "source": "00abdf18",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf2c`](#insn-00abdf2c)

~~~json
{
  "source": "00abdf2c",
  "target": "00abe078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf34`](#insn-00abdf34)

~~~json
{
  "source": "00abdf34",
  "target": "00480138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf40`](#insn-00abdf40)

~~~json
{
  "source": "00abdf40",
  "target": "004800d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdf54`](#insn-00abdf54)

~~~json
{
  "source": "00abdf54",
  "target": "00abdf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf58`](#insn-00abdf58)

~~~json
{
  "source": "00abdf58",
  "target": "00abdf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf64`](#insn-00abdf64)

~~~json
{
  "source": "00abdf64",
  "target": "00abdf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf74`](#insn-00abdf74)

~~~json
{
  "source": "00abdf74",
  "target": "00abdf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf78`](#insn-00abdf78)

~~~json
{
  "source": "00abdf78",
  "target": "00abdf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf80`](#insn-00abdf80)

~~~json
{
  "source": "00abdf80",
  "target": "00abdf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdf90`](#insn-00abdf90)

~~~json
{
  "source": "00abdf90",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdfb4`](#insn-00abdfb4)

~~~json
{
  "source": "00abdfb4",
  "target": "00abdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdfc0`](#insn-00abdfc0)

~~~json
{
  "source": "00abdfc0",
  "target": "00abdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdfd0`](#insn-00abdfd0)

~~~json
{
  "source": "00abdfd0",
  "target": "00abdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abdfd8`](#insn-00abdfd8)

~~~json
{
  "source": "00abdfd8",
  "target": "00480138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abdfe8`](#insn-00abdfe8)

~~~json
{
  "source": "00abdfe8",
  "target": "00abdfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe000`](#insn-00abe000)

~~~json
{
  "source": "00abe000",
  "target": "00abe0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe024`](#insn-00abe024)

~~~json
{
  "source": "00abe024",
  "target": "00abe040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe02c`](#insn-00abe02c)

~~~json
{
  "source": "00abe02c",
  "target": "00abe0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe034`](#insn-00abe034)

~~~json
{
  "source": "00abe034",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe03c`](#insn-00abe03c)

~~~json
{
  "source": "00abe03c",
  "target": "00abe044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe05c`](#insn-00abe05c)

~~~json
{
  "source": "00abe05c",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe068`](#insn-00abe068)

~~~json
{
  "source": "00abe068",
  "target": "00abdfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe070`](#insn-00abe070)

~~~json
{
  "source": "00abe070",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe074`](#insn-00abe074)

~~~json
{
  "source": "00abe074",
  "target": "00abdfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe07c`](#insn-00abe07c)

~~~json
{
  "source": "00abe07c",
  "target": "004802b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe088`](#insn-00abe088)

~~~json
{
  "source": "00abe088",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe08c`](#insn-00abe08c)

~~~json
{
  "source": "00abe08c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe090`](#insn-00abe090)

~~~json
{
  "source": "00abe090",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe094`](#insn-00abe094)

~~~json
{
  "source": "00abe094",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe098`](#insn-00abe098)

~~~json
{
  "source": "00abe098",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe09c`](#insn-00abe09c)

~~~json
{
  "source": "00abe09c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe0ac`](#insn-00abe0ac)

~~~json
{
  "source": "00abe0ac",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe0b0`](#insn-00abe0b0)

~~~json
{
  "source": "00abe0b0",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
