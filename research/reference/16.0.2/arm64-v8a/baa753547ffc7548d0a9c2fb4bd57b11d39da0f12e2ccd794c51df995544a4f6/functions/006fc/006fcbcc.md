# 006fcbcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `006fcb74`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0033.md#compare-198032dd00a5881c2ff8298daf3719e4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `006fcf7c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0034.md#compare-8d07a64905bda218cef776f7fa8a3a3b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fcbcc",
  "name": "FUN_006fcbcc",
  "size": 908,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0a50b17e8ac5f485e24a9845117021dcdda067a2422d76a3ad7fc450158d302",
  "source_text_sha256": "e0a50b17e8ac5f485e24a9845117021dcdda067a2422d76a3ad7fc450158d302",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fcbcc",
        "006fcf57"
      ]
    ],
    "bytes_sha256": "e574a43c509fc8ff21b4b580191ded4d273c9bb04dfd886973c152808c447f49",
    "instruction_count": 227,
    "instruction_bytes": 908,
    "body_bytes": 908,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006e542c](../006e5/006e542c.md)
- [006fcbcc](../006fc/006fcbcc.md)
- [006fcf58](../006fc/006fcf58.md)

## 呼び出し先

- [006e4b1c](../006e4/006e4b1c.md)
- [006fcbcc](../006fc/006fcbcc.md)
- [006fcf58](../006fc/006fcf58.md)
- [006fd2a8](../006fd/006fd2a8.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5825 bytes

~~~c

void FUN_006fcbcc(undefined4 *param_1,undefined4 *param_2,ulong param_3,undefined4 *param_4,
                 long param_5)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined4 *puVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  long lVar6;
  int iVar7;
  int iVar8;
  undefined8 uVar9;
  undefined4 *puVar10;
  undefined4 *puVar11;
  undefined4 *puVar12;
  undefined4 *puVar13;
  undefined4 *puVar14;
  ulong uVar15;
  ulong uVar16;
  ulong uVar17;
  ulong uVar18;
  long lVar19;
  undefined4 *puVar20;
  long lVar21;
  undefined8 uVar22;
  undefined8 uVar23;
  
  if (1 < param_3) {
    if (param_3 == 2) {
      uVar5 = param_2[-1];
      uVar4 = *param_1;
      uVar9 = FUN_00851550();
      iVar7 = FUN_006e4b1c(uVar9,uVar5,0x2c);
      uVar9 = FUN_00851550();
      iVar8 = FUN_006e4b1c(uVar9,uVar4,0x2c);
      if (iVar7 < iVar8) {
        uVar4 = *param_1;
        *param_1 = param_2[-1];
        param_2[-1] = uVar4;
      }
    }
    else if ((long)param_3 < 0x81) {
      if ((param_1 != param_2) && (param_1 + 1 != param_2)) {
        lVar19 = 0;
        puVar13 = param_1 + 1;
        puVar10 = param_1;
        do {
          puVar12 = puVar13;
          uVar4 = *puVar12;
          uVar5 = *puVar10;
          uVar9 = FUN_00851550();
          iVar7 = FUN_006e4b1c(uVar9,uVar4,0x2c);
          uVar9 = FUN_00851550();
          iVar8 = FUN_006e4b1c(uVar9,uVar5,0x2c);
          if (iVar7 < iVar8) {
            uVar4 = *puVar12;
            lVar6 = lVar19;
            do {
              lVar21 = lVar6;
              puVar13 = (undefined4 *)((long)param_1 + lVar21);
              puVar13[1] = *puVar13;
              puVar10 = param_1;
              if (lVar21 == 0) goto LAB_006fcc84;
              uVar5 = puVar13[-1];
              uVar9 = FUN_00851550();
              iVar7 = FUN_006e4b1c(uVar9,uVar4,0x2c);
              uVar9 = FUN_00851550();
              iVar8 = FUN_006e4b1c(uVar9,uVar5,0x2c);
              lVar6 = lVar21 + -4;
            } while (iVar7 < iVar8);
            puVar10 = (undefined4 *)((long)param_1 + lVar21);
LAB_006fcc84:
            *puVar10 = uVar4;
          }
          lVar19 = lVar19 + 4;
          puVar13 = puVar12 + 1;
          puVar10 = puVar12;
        } while (puVar12 + 1 != param_2);
      }
    }
    else {
      uVar18 = param_3 >> 1;
      puVar13 = param_1 + uVar18;
      lVar19 = param_3 - uVar18;
      if (param_5 < (long)param_3) {
        FUN_006fcbcc(param_1,puVar13,uVar18,param_4);
        FUN_006fcbcc(puVar13,param_2,lVar19,param_4,param_5);
        FUN_006fd2a8(param_1,puVar13,param_2,uVar18,lVar19,param_4,param_5);
        return;
      }
      FUN_006fcf58(param_1,puVar13,uVar18,param_4);
      puVar10 = param_4 + uVar18;
      FUN_006fcf58(puVar13,param_2,lVar19,puVar10);
      puVar13 = param_4 + param_3;
      puVar12 = puVar10;
      puVar14 = param_1;
      while (puVar11 = puVar12, puVar11 != puVar13) {
        uVar4 = *puVar11;
        uVar5 = *param_4;
        uVar9 = FUN_00851550();
        iVar7 = FUN_006e4b1c(uVar9,uVar4,0x2c);
        uVar9 = FUN_00851550();
        iVar8 = FUN_006e4b1c(uVar9,uVar5,0x2c);
        param_1 = param_1 + 1;
        uVar18 = (ulong)(iVar7 < iVar8);
        puVar3 = puVar11;
        if (iVar8 <= iVar7) {
          puVar3 = param_4;
        }
        param_4 = param_4 + (iVar8 <= iVar7);
        puVar12 = puVar11 + uVar18;
        puVar20 = puVar14 + 1;
        *puVar14 = *puVar3;
        puVar14 = puVar20;
        if (param_4 == puVar10) {
          if (puVar12 == puVar13) {
            return;
          }
          uVar15 = (long)puVar13 + (uVar18 * -4 - (long)puVar11) + -4;
          if ((0x2b < uVar15) && (0x1f < (long)param_1 + (uVar18 * -4 - (long)puVar11))) {
            lVar19 = 0;
            uVar15 = (uVar15 >> 2) + 1;
            uVar16 = uVar15 & 0x7ffffffffffffff8;
            uVar17 = uVar16;
            do {
              puVar1 = (undefined8 *)((long)puVar11 + lVar19 + uVar18 * 4);
              puVar2 = (undefined8 *)((long)puVar20 + lVar19);
              uVar17 = uVar17 - 8;
              uVar9 = *puVar1;
              uVar23 = puVar1[3];
              uVar22 = puVar1[2];
              lVar19 = lVar19 + 0x20;
              puVar2[1] = puVar1[1];
              *puVar2 = uVar9;
              puVar2[3] = uVar23;
              puVar2[2] = uVar22;
            } while (uVar17 != 0);
            puVar12 = puVar12 + uVar16;
            puVar20 = puVar20 + uVar16;
            if (uVar15 == uVar16) {
              return;
            }
          }
          do {
            puVar10 = puVar12 + 1;
            *puVar20 = *puVar12;
            puVar12 = puVar10;
            puVar20 = puVar20 + 1;
          } while (puVar10 != puVar13);
          return;
        }
      }
      if (param_4 == puVar10) {
        return;
      }
      uVar18 = (long)puVar10 + (-4 - (long)param_4);
      if ((0x1b < uVar18) && (0x1f < (ulong)((long)param_1 - (long)param_4))) {
        lVar19 = 0;
        uVar18 = (uVar18 >> 2) + 1;
        uVar17 = uVar18 & 0x7ffffffffffffff8;
        uVar15 = uVar17;
        do {
          puVar1 = (undefined8 *)((long)param_4 + lVar19);
          puVar2 = (undefined8 *)((long)puVar14 + lVar19);
          uVar15 = uVar15 - 8;
          uVar9 = *puVar1;
          uVar23 = puVar1[3];
          uVar22 = puVar1[2];
          lVar19 = lVar19 + 0x20;
          puVar2[1] = puVar1[1];
          *puVar2 = uVar9;
          puVar2[3] = uVar23;
          puVar2[2] = uVar22;
        } while (uVar15 != 0);
        param_4 = param_4 + uVar17;
        puVar14 = puVar14 + uVar17;
        if (uVar18 == uVar17) {
          return;
        }
      }
      do {
        puVar13 = param_4 + 1;
        *puVar14 = *param_4;
        param_4 = puVar13;
        puVar14 = puVar14 + 1;
      } while (puVar13 != puVar10);
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fcbcc"></a> `006fcbcc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-006fcbd0"></a> `006fcbd0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fcbd4"></a> `006fcbd4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fcbd8"></a> `006fcbd8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006fcbdc"></a> `006fcbdc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006fcbe0"></a> `006fcbe0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fcbe4"></a> `006fcbe4` | `5f 08 00 f1` | cmp x2,#0x2 | `FALL_THROUGH`
<a id="insn-006fcbe8"></a> `006fcbe8` | `e2 00 00 54` | b.cs 0x006fcc04 | `CONDITIONAL_JUMP`
<a id="insn-006fcbec"></a> `006fcbec` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006fcbf0"></a> `006fcbf0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006fcbf4"></a> `006fcbf4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fcbf8"></a> `006fcbf8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fcbfc"></a> `006fcbfc` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-006fcc00"></a> `006fcc00` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006fcc04"></a> `006fcc04` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-006fcc08"></a> `006fcc08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006fcc0c"></a> `006fcc0c` | `61 02 00 54` | b.ne 0x006fcc58 | `CONDITIONAL_JUMP`
<a id="insn-006fcc10"></a> `006fcc10` | `95 c2 5f b8` | ldur w21,[x20, #-0x4] | `FALL_THROUGH`
<a id="insn-006fcc14"></a> `006fcc14` | `76 02 40 b9` | ldr w22,[x19] | `FALL_THROUGH`
<a id="insn-006fcc18"></a> `006fcc18` | `4e 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fcc1c"></a> `006fcc1c` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006fcc20"></a> `006fcc20` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fcc24"></a> `006fcc24` | `be 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fcc28"></a> `006fcc28` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-006fcc2c"></a> `006fcc2c` | `49 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fcc30"></a> `006fcc30` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-006fcc34"></a> `006fcc34` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fcc38"></a> `006fcc38` | `b9 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fcc3c"></a> `006fcc3c` | `bf 02 00 6b` | cmp w21,w0 | `FALL_THROUGH`
<a id="insn-006fcc40"></a> `006fcc40` | `6a fd ff 54` | b.ge 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fcc44"></a> `006fcc44` | `88 c2 5f b8` | ldur w8,[x20, #-0x4] | `FALL_THROUGH`
<a id="insn-006fcc48"></a> `006fcc48` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-006fcc4c"></a> `006fcc4c` | `68 02 00 b9` | str w8,[x19] | `FALL_THROUGH`
<a id="insn-006fcc50"></a> `006fcc50` | `89 c2 1f b8` | stur w9,[x20, #-0x4] | `FALL_THROUGH`
<a id="insn-006fcc54"></a> `006fcc54` | `e6 ff ff 17` | b 0x006fcbec | `UNCONDITIONAL_JUMP`
<a id="insn-006fcc58"></a> `006fcc58` | `5f 00 02 f1` | cmp x2,#0x80 | `FALL_THROUGH`
<a id="insn-006fcc5c"></a> `006fcc5c` | `8c 06 00 54` | b.gt 0x006fcd2c | `CONDITIONAL_JUMP`
<a id="insn-006fcc60"></a> `006fcc60` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-006fcc64"></a> `006fcc64` | `40 fc ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fcc68"></a> `006fcc68` | `68 12 00 91` | add x8,x19,#0x4 | `FALL_THROUGH`
<a id="insn-006fcc6c"></a> `006fcc6c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-006fcc70"></a> `006fcc70` | `e0 fb ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fcc74"></a> `006fcc74` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-006fcc78"></a> `006fcc78` | `f9 03 13 aa` | mov x25,x19 | `FALL_THROUGH`
<a id="insn-006fcc7c"></a> `006fcc7c` | `07 00 00 14` | b 0x006fcc98 | `UNCONDITIONAL_JUMP`
<a id="insn-006fcc80"></a> `006fcc80` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-006fcc84"></a> `006fcc84` | `15 01 00 b9` | str w21,[x8] | `FALL_THROUGH`
<a id="insn-006fcc88"></a> `006fcc88` | `28 13 00 91` | add x8,x25,#0x4 | `FALL_THROUGH`
<a id="insn-006fcc8c"></a> `006fcc8c` | `18 13 00 91` | add x24,x24,#0x4 | `FALL_THROUGH`
<a id="insn-006fcc90"></a> `006fcc90` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-006fcc94"></a> `006fcc94` | `c0 fa ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fcc98"></a> `006fcc98` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-006fcc9c"></a> `006fcc9c` | `16 01 40 b9` | ldr w22,[x8] | `FALL_THROUGH`
<a id="insn-006fcca0"></a> `006fcca0` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-006fcca4"></a> `006fcca4` | `35 01 40 b9` | ldr w21,[x9] | `FALL_THROUGH`
<a id="insn-006fcca8"></a> `006fcca8` | `2a 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fccac"></a> `006fccac` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-006fccb0"></a> `006fccb0` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fccb4"></a> `006fccb4` | `9a 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fccb8"></a> `006fccb8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-006fccbc"></a> `006fccbc` | `25 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fccc0"></a> `006fccc0` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006fccc4"></a> `006fccc4` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fccc8"></a> `006fccc8` | `95 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fcccc"></a> `006fcccc` | `df 02 00 6b` | cmp w22,w0 | `FALL_THROUGH`
<a id="insn-006fccd0"></a> `006fccd0` | `ca fd ff 54` | b.ge 0x006fcc88 | `CONDITIONAL_JUMP`
<a id="insn-006fccd4"></a> `006fccd4` | `35 03 40 b9` | ldr w21,[x25] | `FALL_THROUGH`
<a id="insn-006fccd8"></a> `006fccd8` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-006fccdc"></a> `006fccdc` | `68 02 1a 8b` | add x8,x19,x26 | `FALL_THROUGH`
<a id="insn-006fcce0"></a> `006fcce0` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-006fcce4"></a> `006fcce4` | `09 05 00 b9` | str w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-006fcce8"></a> `006fcce8` | `da fc ff b4` | cbz x26,0x006fcc80 | `CONDITIONAL_JUMP`
<a id="insn-006fccec"></a> `006fccec` | `16 c1 5f b8` | ldur w22,[x8, #-0x4] | `FALL_THROUGH`
<a id="insn-006fccf0"></a> `006fccf0` | `18 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fccf4"></a> `006fccf4` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006fccf8"></a> `006fccf8` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fccfc"></a> `006fccfc` | `88 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fcd00"></a> `006fcd00` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006fcd04"></a> `006fcd04` | `13 52 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fcd08"></a> `006fcd08` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-006fcd0c"></a> `006fcd0c` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fcd10"></a> `006fcd10` | `83 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fcd14"></a> `006fcd14` | `ff 02 00 6b` | cmp w23,w0 | `FALL_THROUGH`
<a id="insn-006fcd18"></a> `006fcd18` | `5a 13 00 d1` | sub x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-006fcd1c"></a> `006fcd1c` | `0b fe ff 54` | b.lt 0x006fccdc | `CONDITIONAL_JUMP`
<a id="insn-006fcd20"></a> `006fcd20` | `68 02 1a 8b` | add x8,x19,x26 | `FALL_THROUGH`
<a id="insn-006fcd24"></a> `006fcd24` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-006fcd28"></a> `006fcd28` | `d7 ff ff 17` | b 0x006fcc84 | `UNCONDITIONAL_JUMP`
<a id="insn-006fcd2c"></a> `006fcd2c` | `56 fc 41 d3` | lsr x22,x2,#0x1 | `FALL_THROUGH`
<a id="insn-006fcd30"></a> `006fcd30` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-006fcd34"></a> `006fcd34` | `5f 00 04 eb` | cmp x2,x4 | `FALL_THROUGH`
<a id="insn-006fcd38"></a> `006fcd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006fcd3c"></a> `006fcd3c` | `77 0a 16 8b` | add x23,x19,x22, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006fcd40"></a> `006fcd40` | `58 00 16 cb` | sub x24,x2,x22 | `FALL_THROUGH`
<a id="insn-006fcd44"></a> `006fcd44` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-006fcd48"></a> `006fcd48` | `0d 03 00 54` | b.le 0x006fcda8 | `CONDITIONAL_JUMP`
<a id="insn-006fcd4c"></a> `006fcd4c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-006fcd50"></a> `006fcd50` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-006fcd54"></a> `006fcd54` | `f9 03 04 aa` | mov x25,x4 | `FALL_THROUGH`
<a id="insn-006fcd58"></a> `006fcd58` | `9d ff ff 97` | bl 0x006fcbcc | `UNCONDITIONAL_CALL`
<a id="insn-006fcd5c"></a> `006fcd5c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006fcd60"></a> `006fcd60` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006fcd64"></a> `006fcd64` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-006fcd68"></a> `006fcd68` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-006fcd6c"></a> `006fcd6c` | `e4 03 19 aa` | mov x4,x25 | `FALL_THROUGH`
<a id="insn-006fcd70"></a> `006fcd70` | `97 ff ff 97` | bl 0x006fcbcc | `UNCONDITIONAL_CALL`
<a id="insn-006fcd74"></a> `006fcd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006fcd78"></a> `006fcd78` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-006fcd7c"></a> `006fcd7c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-006fcd80"></a> `006fcd80` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-006fcd84"></a> `006fcd84` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-006fcd88"></a> `006fcd88` | `e5 03 15 aa` | mov x5,x21 | `FALL_THROUGH`
<a id="insn-006fcd8c"></a> `006fcd8c` | `e6 03 19 aa` | mov x6,x25 | `FALL_THROUGH`
<a id="insn-006fcd90"></a> `006fcd90` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006fcd94"></a> `006fcd94` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006fcd98"></a> `006fcd98` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fcd9c"></a> `006fcd9c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fcda0"></a> `006fcda0` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-006fcda4"></a> `006fcda4` | `41 01 00 14` | b 0x006fd2a8 | `CALL_TERMINATOR`
<a id="insn-006fcda8"></a> `006fcda8` | `f9 03 02 aa` | mov x25,x2 | `FALL_THROUGH`
<a id="insn-006fcdac"></a> `006fcdac` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-006fcdb0"></a> `006fcdb0` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-006fcdb4"></a> `006fcdb4` | `69 00 00 94` | bl 0x006fcf58 | `UNCONDITIONAL_CALL`
<a id="insn-006fcdb8"></a> `006fcdb8` | `b6 0a 16 8b` | add x22,x21,x22, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006fcdbc"></a> `006fcdbc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006fcdc0"></a> `006fcdc0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006fcdc4"></a> `006fcdc4` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-006fcdc8"></a> `006fcdc8` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-006fcdcc"></a> `006fcdcc` | `63 00 00 94` | bl 0x006fcf58 | `UNCONDITIONAL_CALL`
<a id="insn-006fcdd0"></a> `006fcdd0` | `b9 0a 19 8b` | add x25,x21,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006fcdd4"></a> `006fcdd4` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-006fcdd8"></a> `006fcdd8` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-006fcddc"></a> `006fcddc` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-006fcde0"></a> `006fcde0` | `80 07 00 54` | b.eq 0x006fced0 | `CONDITIONAL_JUMP`
<a id="insn-006fcde4"></a> `006fcde4` | `14 01 40 b9` | ldr w20,[x8] | `FALL_THROUGH`
<a id="insn-006fcde8"></a> `006fcde8` | `b7 02 40 b9` | ldr w23,[x21] | `FALL_THROUGH`
<a id="insn-006fcdec"></a> `006fcdec` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-006fcdf0"></a> `006fcdf0` | `d8 51 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fcdf4"></a> `006fcdf4` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-006fcdf8"></a> `006fcdf8` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fcdfc"></a> `006fcdfc` | `48 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fce00"></a> `006fce00` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-006fce04"></a> `006fce04` | `d3 51 05 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006fce08"></a> `006fce08` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-006fce0c"></a> `006fce0c` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006fce10"></a> `006fce10` | `43 9f ff 97` | bl 0x006e4b1c | `UNCONDITIONAL_CALL`
<a id="insn-006fce14"></a> `006fce14` | `9f 02 00 6b` | cmp w20,w0 | `FALL_THROUGH`
<a id="insn-006fce18"></a> `006fce18` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-006fce1c"></a> `006fce1c` | `e8 b7 9f 1a` | cset w8,ge | `FALL_THROUGH`
<a id="insn-006fce20"></a> `006fce20` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-006fce24"></a> `006fce24` | `4a b3 95 9a` | csel x10,x26,x21,lt | `FALL_THROUGH`
<a id="insn-006fce28"></a> `006fce28` | `b5 4a 28 8b` | add x21,x21,w8, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-006fce2c"></a> `006fce2c` | `29 7d 7e d3` | ubfiz x9,x9,#0x2,#0x20 | `FALL_THROUGH`
<a id="insn-006fce30"></a> `006fce30` | `4a 01 40 b9` | ldr w10,[x10] | `FALL_THROUGH`
<a id="insn-006fce34"></a> `006fce34` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006fce38"></a> `006fce38` | `48 03 09 8b` | add x8,x26,x9 | `FALL_THROUGH`
<a id="insn-006fce3c"></a> `006fce3c` | `0a 47 00 b8` | str w10,[x24], #0x4 | `FALL_THROUGH`
<a id="insn-006fce40"></a> `006fce40` | `e1 fc ff 54` | b.ne 0x006fcddc | `CONDITIONAL_JUMP`
<a id="insn-006fce44"></a> `006fce44` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-006fce48"></a> `006fce48` | `20 ed ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fce4c"></a> `006fce4c` | `2a 03 1a cb` | sub x10,x25,x26 | `FALL_THROUGH`
<a id="insn-006fce50"></a> `006fce50` | `4a 01 09 cb` | sub x10,x10,x9 | `FALL_THROUGH`
<a id="insn-006fce54"></a> `006fce54` | `4b 11 00 d1` | sub x11,x10,#0x4 | `FALL_THROUGH`
<a id="insn-006fce58"></a> `006fce58` | `7f b1 00 f1` | cmp x11,#0x2c | `FALL_THROUGH`
<a id="insn-006fce5c"></a> `006fce5c` | `03 03 00 54` | b.cc 0x006fcebc | `CONDITIONAL_JUMP`
<a id="insn-006fce60"></a> `006fce60` | `6a 02 1a cb` | sub x10,x19,x26 | `FALL_THROUGH`
<a id="insn-006fce64"></a> `006fce64` | `4a 01 09 cb` | sub x10,x10,x9 | `FALL_THROUGH`
<a id="insn-006fce68"></a> `006fce68` | `5f 81 00 f1` | cmp x10,#0x20 | `FALL_THROUGH`
<a id="insn-006fce6c"></a> `006fce6c` | `83 02 00 54` | b.cc 0x006fcebc | `CONDITIONAL_JUMP`
<a id="insn-006fce70"></a> `006fce70` | `6b fd 42 d3` | lsr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-006fce74"></a> `006fce74` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-006fce78"></a> `006fce78` | `49 03 09 8b` | add x9,x26,x9 | `FALL_THROUGH`
<a id="insn-006fce7c"></a> `006fce7c` | `6b 05 00 91` | add x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-006fce80"></a> `006fce80` | `6c ed 7d 92` | and x12,x11,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006fce84"></a> `006fce84` | `8d f5 7e d3` | lsl x13,x12,#0x2 | `FALL_THROUGH`
<a id="insn-006fce88"></a> `006fce88` | `ee 03 0c aa` | mov x14,x12 | `FALL_THROUGH`
<a id="insn-006fce8c"></a> `006fce8c` | `08 01 0d 8b` | add x8,x8,x13 | `FALL_THROUGH`
<a id="insn-006fce90"></a> `006fce90` | `0d 03 0d 8b` | add x13,x24,x13 | `FALL_THROUGH`
<a id="insn-006fce94"></a> `006fce94` | `2f 01 0a 8b` | add x15,x9,x10 | `FALL_THROUGH`
<a id="insn-006fce98"></a> `006fce98` | `10 03 0a 8b` | add x16,x24,x10 | `FALL_THROUGH`
<a id="insn-006fce9c"></a> `006fce9c` | `ce 21 00 f1` | subs x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-006fcea0"></a> `006fcea0` | `e0 05 40 ad` | ldp q0,q1,[x15] | `FALL_THROUGH`
<a id="insn-006fcea4"></a> `006fcea4` | `4a 81 00 91` | add x10,x10,#0x20 | `FALL_THROUGH`
<a id="insn-006fcea8"></a> `006fcea8` | `00 06 00 ad` | stp q0,q1,[x16] | `FALL_THROUGH`
<a id="insn-006fceac"></a> `006fceac` | `41 ff ff 54` | b.ne 0x006fce94 | `CONDITIONAL_JUMP`
<a id="insn-006fceb0"></a> `006fceb0` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-006fceb4"></a> `006fceb4` | `f8 03 0d aa` | mov x24,x13 | `FALL_THROUGH`
<a id="insn-006fceb8"></a> `006fceb8` | `a0 e9 ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fcebc"></a> `006fcebc` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-006fcec0"></a> `006fcec0` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-006fcec4"></a> `006fcec4` | `09 47 00 b8` | str w9,[x24], #0x4 | `FALL_THROUGH`
<a id="insn-006fcec8"></a> `006fcec8` | `a1 ff ff 54` | b.ne 0x006fcebc | `CONDITIONAL_JUMP`
<a id="insn-006fcecc"></a> `006fcecc` | `48 ff ff 17` | b 0x006fcbec | `UNCONDITIONAL_JUMP`
<a id="insn-006fced0"></a> `006fced0` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006fced4"></a> `006fced4` | `c0 e8 ff 54` | b.eq 0x006fcbec | `CONDITIONAL_JUMP`
<a id="insn-006fced8"></a> `006fced8` | `c8 02 15 cb` | sub x8,x22,x21 | `FALL_THROUGH`
<a id="insn-006fcedc"></a> `006fcedc` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-006fcee0"></a> `006fcee0` | `1f 71 00 f1` | cmp x8,#0x1c | `FALL_THROUGH`
<a id="insn-006fcee4"></a> `006fcee4` | `83 00 00 54` | b.cc 0x006fcef4 | `CONDITIONAL_JUMP`
<a id="insn-006fcee8"></a> `006fcee8` | `69 02 15 cb` | sub x9,x19,x21 | `FALL_THROUGH`
<a id="insn-006fceec"></a> `006fceec` | `3f 81 00 f1` | cmp x9,#0x20 | `FALL_THROUGH`
<a id="insn-006fcef0"></a> `006fcef0` | `02 01 00 54` | b.cs 0x006fcf10 | `CONDITIONAL_JUMP`
<a id="insn-006fcef4"></a> `006fcef4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-006fcef8"></a> `006fcef8` | `e9 03 18 aa` | mov x9,x24 | `FALL_THROUGH`
<a id="insn-006fcefc"></a> `006fcefc` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-006fcf00"></a> `006fcf00` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-006fcf04"></a> `006fcf04` | `2a 45 00 b8` | str w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-006fcf08"></a> `006fcf08` | `a1 ff ff 54` | b.ne 0x006fcefc | `CONDITIONAL_JUMP`
<a id="insn-006fcf0c"></a> `006fcf0c` | `38 ff ff 17` | b 0x006fcbec | `UNCONDITIONAL_JUMP`
<a id="insn-006fcf10"></a> `006fcf10` | `08 fd 42 d3` | lsr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006fcf14"></a> `006fcf14` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-006fcf18"></a> `006fcf18` | `0b 05 00 91` | add x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006fcf1c"></a> `006fcf1c` | `6c ed 7d 92` | and x12,x11,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006fcf20"></a> `006fcf20` | `89 f5 7e d3` | lsl x9,x12,#0x2 | `FALL_THROUGH`
<a id="insn-006fcf24"></a> `006fcf24` | `ed 03 0c aa` | mov x13,x12 | `FALL_THROUGH`
<a id="insn-006fcf28"></a> `006fcf28` | `a8 02 09 8b` | add x8,x21,x9 | `FALL_THROUGH`
<a id="insn-006fcf2c"></a> `006fcf2c` | `09 03 09 8b` | add x9,x24,x9 | `FALL_THROUGH`
<a id="insn-006fcf30"></a> `006fcf30` | `ae 02 0a 8b` | add x14,x21,x10 | `FALL_THROUGH`
<a id="insn-006fcf34"></a> `006fcf34` | `0f 03 0a 8b` | add x15,x24,x10 | `FALL_THROUGH`
<a id="insn-006fcf38"></a> `006fcf38` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-006fcf3c"></a> `006fcf3c` | `c0 05 40 ad` | ldp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-006fcf40"></a> `006fcf40` | `4a 81 00 91` | add x10,x10,#0x20 | `FALL_THROUGH`
<a id="insn-006fcf44"></a> `006fcf44` | `e0 05 00 ad` | stp q0,q1,[x15] | `FALL_THROUGH`
<a id="insn-006fcf48"></a> `006fcf48` | `41 ff ff 54` | b.ne 0x006fcf30 | `CONDITIONAL_JUMP`
<a id="insn-006fcf4c"></a> `006fcf4c` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-006fcf50"></a> `006fcf50` | `61 fd ff 54` | b.ne 0x006fcefc | `CONDITIONAL_JUMP`
<a id="insn-006fcf54"></a> `006fcf54` | `26 ff ff 17` | b 0x006fcbec | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`006fcbcc`](#insn-006fcbcc) 範囲 `[['006fcbcc', '006fcbeb']]`
  - `CONDITIONAL_JUMP` [`006fcbe8`](#insn-006fcbe8) → [`006fcc04`](#insn-006fcc04)
  - `FALL_THROUGH` [`006fcbe8`](#insn-006fcbe8) → [`006fcbec`](#insn-006fcbec)
- ブロック [`006fcbec`](#insn-006fcbec) 範囲 `[['006fcbec', '006fcc03']]`
- ブロック [`006fcc04`](#insn-006fcc04) 範囲 `[['006fcc04', '006fcc0f']]`
  - `CONDITIONAL_JUMP` [`006fcc0c`](#insn-006fcc0c) → [`006fcc58`](#insn-006fcc58)
  - `FALL_THROUGH` [`006fcc0c`](#insn-006fcc0c) → [`006fcc10`](#insn-006fcc10)
- ブロック [`006fcc10`](#insn-006fcc10) 範囲 `[['006fcc10', '006fcc43']]`
  - `CONDITIONAL_JUMP` [`006fcc40`](#insn-006fcc40) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fcc40`](#insn-006fcc40) → [`006fcc44`](#insn-006fcc44)
- ブロック [`006fcc44`](#insn-006fcc44) 範囲 `[['006fcc44', '006fcc57']]`
  - `UNCONDITIONAL_JUMP` [`006fcc54`](#insn-006fcc54) → [`006fcbec`](#insn-006fcbec)
- ブロック [`006fcc58`](#insn-006fcc58) 範囲 `[['006fcc58', '006fcc5f']]`
  - `CONDITIONAL_JUMP` [`006fcc5c`](#insn-006fcc5c) → [`006fcd2c`](#insn-006fcd2c)
  - `FALL_THROUGH` [`006fcc5c`](#insn-006fcc5c) → [`006fcc60`](#insn-006fcc60)
- ブロック [`006fcc60`](#insn-006fcc60) 範囲 `[['006fcc60', '006fcc67']]`
  - `CONDITIONAL_JUMP` [`006fcc64`](#insn-006fcc64) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fcc64`](#insn-006fcc64) → [`006fcc68`](#insn-006fcc68)
- ブロック [`006fcc68`](#insn-006fcc68) 範囲 `[['006fcc68', '006fcc73']]`
  - `CONDITIONAL_JUMP` [`006fcc70`](#insn-006fcc70) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fcc70`](#insn-006fcc70) → [`006fcc74`](#insn-006fcc74)
- ブロック [`006fcc74`](#insn-006fcc74) 範囲 `[['006fcc74', '006fcc7f']]`
  - `UNCONDITIONAL_JUMP` [`006fcc7c`](#insn-006fcc7c) → [`006fcc98`](#insn-006fcc98)
- ブロック [`006fcc80`](#insn-006fcc80) 範囲 `[['006fcc80', '006fcc83']]`
  - `FALL_THROUGH` [`006fcc80`](#insn-006fcc80) → [`006fcc84`](#insn-006fcc84)
- ブロック [`006fcc84`](#insn-006fcc84) 範囲 `[['006fcc84', '006fcc87']]`
  - `FALL_THROUGH` [`006fcc84`](#insn-006fcc84) → [`006fcc88`](#insn-006fcc88)
- ブロック [`006fcc88`](#insn-006fcc88) 範囲 `[['006fcc88', '006fcc97']]`
  - `CONDITIONAL_JUMP` [`006fcc94`](#insn-006fcc94) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fcc94`](#insn-006fcc94) → [`006fcc98`](#insn-006fcc98)
- ブロック [`006fcc98`](#insn-006fcc98) 範囲 `[['006fcc98', '006fccd3']]`
  - `CONDITIONAL_JUMP` [`006fccd0`](#insn-006fccd0) → [`006fcc88`](#insn-006fcc88)
  - `FALL_THROUGH` [`006fccd0`](#insn-006fccd0) → [`006fccd4`](#insn-006fccd4)
- ブロック [`006fccd4`](#insn-006fccd4) 範囲 `[['006fccd4', '006fccdb']]`
  - `FALL_THROUGH` [`006fccd8`](#insn-006fccd8) → [`006fccdc`](#insn-006fccdc)
- ブロック [`006fccdc`](#insn-006fccdc) 範囲 `[['006fccdc', '006fcceb']]`
  - `CONDITIONAL_JUMP` [`006fcce8`](#insn-006fcce8) → [`006fcc80`](#insn-006fcc80)
  - `FALL_THROUGH` [`006fcce8`](#insn-006fcce8) → [`006fccec`](#insn-006fccec)
- ブロック [`006fccec`](#insn-006fccec) 範囲 `[['006fccec', '006fcd1f']]`
  - `CONDITIONAL_JUMP` [`006fcd1c`](#insn-006fcd1c) → [`006fccdc`](#insn-006fccdc)
  - `FALL_THROUGH` [`006fcd1c`](#insn-006fcd1c) → [`006fcd20`](#insn-006fcd20)
- ブロック [`006fcd20`](#insn-006fcd20) 範囲 `[['006fcd20', '006fcd2b']]`
  - `UNCONDITIONAL_JUMP` [`006fcd28`](#insn-006fcd28) → [`006fcc84`](#insn-006fcc84)
- ブロック [`006fcd2c`](#insn-006fcd2c) 範囲 `[['006fcd2c', '006fcd4b']]`
  - `CONDITIONAL_JUMP` [`006fcd48`](#insn-006fcd48) → [`006fcda8`](#insn-006fcda8)
  - `FALL_THROUGH` [`006fcd48`](#insn-006fcd48) → [`006fcd4c`](#insn-006fcd4c)
- ブロック [`006fcd4c`](#insn-006fcd4c) 範囲 `[['006fcd4c', '006fcda7']]`
- ブロック [`006fcda8`](#insn-006fcda8) 範囲 `[['006fcda8', '006fcddb']]`
  - `FALL_THROUGH` [`006fcdd8`](#insn-006fcdd8) → [`006fcddc`](#insn-006fcddc)
- ブロック [`006fcddc`](#insn-006fcddc) 範囲 `[['006fcddc', '006fcde3']]`
  - `CONDITIONAL_JUMP` [`006fcde0`](#insn-006fcde0) → [`006fced0`](#insn-006fced0)
  - `FALL_THROUGH` [`006fcde0`](#insn-006fcde0) → [`006fcde4`](#insn-006fcde4)
- ブロック [`006fcde4`](#insn-006fcde4) 範囲 `[['006fcde4', '006fce43']]`
  - `CONDITIONAL_JUMP` [`006fce40`](#insn-006fce40) → [`006fcddc`](#insn-006fcddc)
  - `FALL_THROUGH` [`006fce40`](#insn-006fce40) → [`006fce44`](#insn-006fce44)
- ブロック [`006fce44`](#insn-006fce44) 範囲 `[['006fce44', '006fce4b']]`
  - `CONDITIONAL_JUMP` [`006fce48`](#insn-006fce48) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fce48`](#insn-006fce48) → [`006fce4c`](#insn-006fce4c)
- ブロック [`006fce4c`](#insn-006fce4c) 範囲 `[['006fce4c', '006fce5f']]`
  - `CONDITIONAL_JUMP` [`006fce5c`](#insn-006fce5c) → [`006fcebc`](#insn-006fcebc)
  - `FALL_THROUGH` [`006fce5c`](#insn-006fce5c) → [`006fce60`](#insn-006fce60)
- ブロック [`006fce60`](#insn-006fce60) 範囲 `[['006fce60', '006fce6f']]`
  - `CONDITIONAL_JUMP` [`006fce6c`](#insn-006fce6c) → [`006fcebc`](#insn-006fcebc)
  - `FALL_THROUGH` [`006fce6c`](#insn-006fce6c) → [`006fce70`](#insn-006fce70)
- ブロック [`006fce70`](#insn-006fce70) 範囲 `[['006fce70', '006fce93']]`
  - `FALL_THROUGH` [`006fce90`](#insn-006fce90) → [`006fce94`](#insn-006fce94)
- ブロック [`006fce94`](#insn-006fce94) 範囲 `[['006fce94', '006fceaf']]`
  - `CONDITIONAL_JUMP` [`006fceac`](#insn-006fceac) → [`006fce94`](#insn-006fce94)
  - `FALL_THROUGH` [`006fceac`](#insn-006fceac) → [`006fceb0`](#insn-006fceb0)
- ブロック [`006fceb0`](#insn-006fceb0) 範囲 `[['006fceb0', '006fcebb']]`
  - `CONDITIONAL_JUMP` [`006fceb8`](#insn-006fceb8) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fceb8`](#insn-006fceb8) → [`006fcebc`](#insn-006fcebc)
- ブロック [`006fcebc`](#insn-006fcebc) 範囲 `[['006fcebc', '006fcecb']]`
  - `CONDITIONAL_JUMP` [`006fcec8`](#insn-006fcec8) → [`006fcebc`](#insn-006fcebc)
  - `FALL_THROUGH` [`006fcec8`](#insn-006fcec8) → [`006fcecc`](#insn-006fcecc)
- ブロック [`006fcecc`](#insn-006fcecc) 範囲 `[['006fcecc', '006fcecf']]`
  - `UNCONDITIONAL_JUMP` [`006fcecc`](#insn-006fcecc) → [`006fcbec`](#insn-006fcbec)
- ブロック [`006fced0`](#insn-006fced0) 範囲 `[['006fced0', '006fced7']]`
  - `CONDITIONAL_JUMP` [`006fced4`](#insn-006fced4) → [`006fcbec`](#insn-006fcbec)
  - `FALL_THROUGH` [`006fced4`](#insn-006fced4) → [`006fced8`](#insn-006fced8)
- ブロック [`006fced8`](#insn-006fced8) 範囲 `[['006fced8', '006fcee7']]`
  - `CONDITIONAL_JUMP` [`006fcee4`](#insn-006fcee4) → [`006fcef4`](#insn-006fcef4)
  - `FALL_THROUGH` [`006fcee4`](#insn-006fcee4) → [`006fcee8`](#insn-006fcee8)
- ブロック [`006fcee8`](#insn-006fcee8) 範囲 `[['006fcee8', '006fcef3']]`
  - `CONDITIONAL_JUMP` [`006fcef0`](#insn-006fcef0) → [`006fcf10`](#insn-006fcf10)
  - `FALL_THROUGH` [`006fcef0`](#insn-006fcef0) → [`006fcef4`](#insn-006fcef4)
- ブロック [`006fcef4`](#insn-006fcef4) 範囲 `[['006fcef4', '006fcefb']]`
  - `FALL_THROUGH` [`006fcef8`](#insn-006fcef8) → [`006fcefc`](#insn-006fcefc)
- ブロック [`006fcefc`](#insn-006fcefc) 範囲 `[['006fcefc', '006fcf0b']]`
  - `CONDITIONAL_JUMP` [`006fcf08`](#insn-006fcf08) → [`006fcefc`](#insn-006fcefc)
  - `FALL_THROUGH` [`006fcf08`](#insn-006fcf08) → [`006fcf0c`](#insn-006fcf0c)
- ブロック [`006fcf0c`](#insn-006fcf0c) 範囲 `[['006fcf0c', '006fcf0f']]`
  - `UNCONDITIONAL_JUMP` [`006fcf0c`](#insn-006fcf0c) → [`006fcbec`](#insn-006fcbec)
- ブロック [`006fcf10`](#insn-006fcf10) 範囲 `[['006fcf10', '006fcf2f']]`
  - `FALL_THROUGH` [`006fcf2c`](#insn-006fcf2c) → [`006fcf30`](#insn-006fcf30)
- ブロック [`006fcf30`](#insn-006fcf30) 範囲 `[['006fcf30', '006fcf4b']]`
  - `CONDITIONAL_JUMP` [`006fcf48`](#insn-006fcf48) → [`006fcf30`](#insn-006fcf30)
  - `FALL_THROUGH` [`006fcf48`](#insn-006fcf48) → [`006fcf4c`](#insn-006fcf4c)
- ブロック [`006fcf4c`](#insn-006fcf4c) 範囲 `[['006fcf4c', '006fcf53']]`
  - `CONDITIONAL_JUMP` [`006fcf50`](#insn-006fcf50) → [`006fcefc`](#insn-006fcefc)
  - `FALL_THROUGH` [`006fcf50`](#insn-006fcf50) → [`006fcf54`](#insn-006fcf54)
- ブロック [`006fcf54`](#insn-006fcf54) 範囲 `[['006fcf54', '006fcf57']]`
  - `UNCONDITIONAL_JUMP` [`006fcf54`](#insn-006fcf54) → [`006fcbec`](#insn-006fcbec)

## 命令位置別の参照

- [`006fcbcc`](#insn-006fcbcc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbd0`](#insn-006fcbd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbd4`](#insn-006fcbd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbd8`](#insn-006fcbd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbdc`](#insn-006fcbdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbe8`](#insn-006fcbe8) → [`006fcc04`](#insn-006fcc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbec`](#insn-006fcbec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbf0`](#insn-006fcbf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbf4`](#insn-006fcbf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbf8`](#insn-006fcbf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcbfc`](#insn-006fcbfc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc0c`](#insn-006fcc0c) → [`006fcc58`](#insn-006fcc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc18`](#insn-006fcc18) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fcc24`](#insn-006fcc24) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fcc2c`](#insn-006fcc2c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fcc38`](#insn-006fcc38) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fcc40`](#insn-006fcc40) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc54`](#insn-006fcc54) → [`006fcbec`](#insn-006fcbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc5c`](#insn-006fcc5c) → [`006fcd2c`](#insn-006fcd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc64`](#insn-006fcc64) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc70`](#insn-006fcc70) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc7c`](#insn-006fcc7c) → [`006fcc98`](#insn-006fcc98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcc94`](#insn-006fcc94) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcca8`](#insn-006fcca8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fccb4`](#insn-006fccb4) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fccbc`](#insn-006fccbc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fccc8`](#insn-006fccc8) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fccd0`](#insn-006fccd0) → [`006fcc88`](#insn-006fcc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcce8`](#insn-006fcce8) → [`006fcc80`](#insn-006fcc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fccf0`](#insn-006fccf0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fccfc`](#insn-006fccfc) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fcd04`](#insn-006fcd04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fcd10`](#insn-006fcd10) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fcd1c`](#insn-006fcd1c) → [`006fccdc`](#insn-006fccdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd28`](#insn-006fcd28) → [`006fcc84`](#insn-006fcc84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd48`](#insn-006fcd48) → [`006fcda8`](#insn-006fcda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd58`](#insn-006fcd58) → [`006fcbcc`](#insn-006fcbcc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fcbcc` · 推定シンボル `None` · 推定型 `None`
- [`006fcd70`](#insn-006fcd70) → [`006fcbcc`](#insn-006fcbcc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fcbcc` · 推定シンボル `None` · 推定型 `None`
- [`006fcd90`](#insn-006fcd90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd94`](#insn-006fcd94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd98`](#insn-006fcd98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcd9c`](#insn-006fcd9c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcda0`](#insn-006fcda0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcda4`](#insn-006fcda4) → [`006fd2a8`](../006fd/006fd2a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fd2a8` · 推定シンボル `None` · 推定型 `None`
- [`006fcdb4`](#insn-006fcdb4) → [`006fcf58`](006fcf58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fcf58` · 推定シンボル `None` · 推定型 `None`
- [`006fcdcc`](#insn-006fcdcc) → [`006fcf58`](006fcf58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006fcf58` · 推定シンボル `None` · 推定型 `None`
- [`006fcde0`](#insn-006fcde0) → [`006fced0`](#insn-006fced0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcdf0`](#insn-006fcdf0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fcdfc`](#insn-006fcdfc) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fce04`](#insn-006fce04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006fce10`](#insn-006fce10) → [`006e4b1c`](../006e4/006e4b1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006e4b1c` · 推定シンボル `None` · 推定型 `None`
- [`006fce40`](#insn-006fce40) → [`006fcddc`](#insn-006fcddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fce48`](#insn-006fce48) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fce5c`](#insn-006fce5c) → [`006fcebc`](#insn-006fcebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fce6c`](#insn-006fce6c) → [`006fcebc`](#insn-006fcebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fceac`](#insn-006fceac) → [`006fce94`](#insn-006fce94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fceb8`](#insn-006fceb8) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcec8`](#insn-006fcec8) → [`006fcebc`](#insn-006fcebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcecc`](#insn-006fcecc) → [`006fcbec`](#insn-006fcbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fced4`](#insn-006fced4) → [`006fcbec`](#insn-006fcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcee4`](#insn-006fcee4) → [`006fcef4`](#insn-006fcef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcef0`](#insn-006fcef0) → [`006fcf10`](#insn-006fcf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcf08`](#insn-006fcf08) → [`006fcefc`](#insn-006fcefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcf0c`](#insn-006fcf0c) → [`006fcbec`](#insn-006fcbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcf48`](#insn-006fcf48) → [`006fcf30`](#insn-006fcf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcf50`](#insn-006fcf50) → [`006fcefc`](#insn-006fcefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fcf54`](#insn-006fcf54) → [`006fcbec`](#insn-006fcbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fcbcc`](#insn-006fcbcc)

~~~json
{
  "source": "006fcbcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbd0`](#insn-006fcbd0)

~~~json
{
  "source": "006fcbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbd4`](#insn-006fcbd4)

~~~json
{
  "source": "006fcbd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbd8`](#insn-006fcbd8)

~~~json
{
  "source": "006fcbd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbdc`](#insn-006fcbdc)

~~~json
{
  "source": "006fcbdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbe8`](#insn-006fcbe8)

~~~json
{
  "source": "006fcbe8",
  "target": "006fcc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbec`](#insn-006fcbec)

~~~json
{
  "source": "006fcbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbf0`](#insn-006fcbf0)

~~~json
{
  "source": "006fcbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbf4`](#insn-006fcbf4)

~~~json
{
  "source": "006fcbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbf8`](#insn-006fcbf8)

~~~json
{
  "source": "006fcbf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcbfc`](#insn-006fcbfc)

~~~json
{
  "source": "006fcbfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc0c`](#insn-006fcc0c)

~~~json
{
  "source": "006fcc0c",
  "target": "006fcc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc18`](#insn-006fcc18)

~~~json
{
  "source": "006fcc18",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcc24`](#insn-006fcc24)

~~~json
{
  "source": "006fcc24",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcc2c`](#insn-006fcc2c)

~~~json
{
  "source": "006fcc2c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcc38`](#insn-006fcc38)

~~~json
{
  "source": "006fcc38",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcc40`](#insn-006fcc40)

~~~json
{
  "source": "006fcc40",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc54`](#insn-006fcc54)

~~~json
{
  "source": "006fcc54",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc5c`](#insn-006fcc5c)

~~~json
{
  "source": "006fcc5c",
  "target": "006fcd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc64`](#insn-006fcc64)

~~~json
{
  "source": "006fcc64",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc70`](#insn-006fcc70)

~~~json
{
  "source": "006fcc70",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc7c`](#insn-006fcc7c)

~~~json
{
  "source": "006fcc7c",
  "target": "006fcc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcc94`](#insn-006fcc94)

~~~json
{
  "source": "006fcc94",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcca8`](#insn-006fcca8)

~~~json
{
  "source": "006fcca8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fccb4`](#insn-006fccb4)

~~~json
{
  "source": "006fccb4",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fccbc`](#insn-006fccbc)

~~~json
{
  "source": "006fccbc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fccc8`](#insn-006fccc8)

~~~json
{
  "source": "006fccc8",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fccd0`](#insn-006fccd0)

~~~json
{
  "source": "006fccd0",
  "target": "006fcc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcce8`](#insn-006fcce8)

~~~json
{
  "source": "006fcce8",
  "target": "006fcc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fccf0`](#insn-006fccf0)

~~~json
{
  "source": "006fccf0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fccfc`](#insn-006fccfc)

~~~json
{
  "source": "006fccfc",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcd04`](#insn-006fcd04)

~~~json
{
  "source": "006fcd04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcd10`](#insn-006fcd10)

~~~json
{
  "source": "006fcd10",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcd1c`](#insn-006fcd1c)

~~~json
{
  "source": "006fcd1c",
  "target": "006fccdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd28`](#insn-006fcd28)

~~~json
{
  "source": "006fcd28",
  "target": "006fcc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd48`](#insn-006fcd48)

~~~json
{
  "source": "006fcd48",
  "target": "006fcda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd58`](#insn-006fcd58)

~~~json
{
  "source": "006fcd58",
  "target": "006fcbcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcd70`](#insn-006fcd70)

~~~json
{
  "source": "006fcd70",
  "target": "006fcbcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcd90`](#insn-006fcd90)

~~~json
{
  "source": "006fcd90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd94`](#insn-006fcd94)

~~~json
{
  "source": "006fcd94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd98`](#insn-006fcd98)

~~~json
{
  "source": "006fcd98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcd9c`](#insn-006fcd9c)

~~~json
{
  "source": "006fcd9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcda0`](#insn-006fcda0)

~~~json
{
  "source": "006fcda0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcda4`](#insn-006fcda4)

~~~json
{
  "source": "006fcda4",
  "target": "006fd2a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcdb4`](#insn-006fcdb4)

~~~json
{
  "source": "006fcdb4",
  "target": "006fcf58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcdcc`](#insn-006fcdcc)

~~~json
{
  "source": "006fcdcc",
  "target": "006fcf58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcde0`](#insn-006fcde0)

~~~json
{
  "source": "006fcde0",
  "target": "006fced0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcdf0`](#insn-006fcdf0)

~~~json
{
  "source": "006fcdf0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fcdfc`](#insn-006fcdfc)

~~~json
{
  "source": "006fcdfc",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fce04`](#insn-006fce04)

~~~json
{
  "source": "006fce04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fce10`](#insn-006fce10)

~~~json
{
  "source": "006fce10",
  "target": "006e4b1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fce40`](#insn-006fce40)

~~~json
{
  "source": "006fce40",
  "target": "006fcddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fce48`](#insn-006fce48)

~~~json
{
  "source": "006fce48",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fce5c`](#insn-006fce5c)

~~~json
{
  "source": "006fce5c",
  "target": "006fcebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fce6c`](#insn-006fce6c)

~~~json
{
  "source": "006fce6c",
  "target": "006fcebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fceac`](#insn-006fceac)

~~~json
{
  "source": "006fceac",
  "target": "006fce94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fceb8`](#insn-006fceb8)

~~~json
{
  "source": "006fceb8",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcec8`](#insn-006fcec8)

~~~json
{
  "source": "006fcec8",
  "target": "006fcebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcecc`](#insn-006fcecc)

~~~json
{
  "source": "006fcecc",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fced4`](#insn-006fced4)

~~~json
{
  "source": "006fced4",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcee4`](#insn-006fcee4)

~~~json
{
  "source": "006fcee4",
  "target": "006fcef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcef0`](#insn-006fcef0)

~~~json
{
  "source": "006fcef0",
  "target": "006fcf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcf08`](#insn-006fcf08)

~~~json
{
  "source": "006fcf08",
  "target": "006fcefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcf0c`](#insn-006fcf0c)

~~~json
{
  "source": "006fcf0c",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcf48`](#insn-006fcf48)

~~~json
{
  "source": "006fcf48",
  "target": "006fcf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcf50`](#insn-006fcf50)

~~~json
{
  "source": "006fcf50",
  "target": "006fcefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fcf54`](#insn-006fcf54)

~~~json
{
  "source": "006fcf54",
  "target": "006fcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
