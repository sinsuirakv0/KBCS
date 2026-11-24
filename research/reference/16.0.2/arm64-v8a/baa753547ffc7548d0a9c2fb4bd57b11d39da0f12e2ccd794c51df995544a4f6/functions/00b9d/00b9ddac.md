# 00b9ddac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b9dd10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9d/00b9dd10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-bfc3fd90b7909d4c7805771c3f229448)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b9eda0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9e/00b9eda0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0034.md#compare-944aa2e8d34f43895111ad8e83b479bc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b9ddac",
  "name": "FUN_00b9ddac",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbfd29adf95e806802edb7ba00615a9128da9b346b1f96f51ae6418d5fb9b62",
  "source_text_sha256": "5fbfd29adf95e806802edb7ba00615a9128da9b346b1f96f51ae6418d5fb9b62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b9ddac",
        "00b9df73"
      ]
    ],
    "bytes_sha256": "1a06c797c8f1227d7b186c88b743b4d01355854e200c21527ee4844154d01ce9",
    "instruction_count": 114,
    "instruction_bytes": 456,
    "body_bytes": 456,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b9d3b8](../00b9d/00b9d3b8.md)

## 呼び出し先

- [00c58010](../00c58/00c58010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3750 bytes

~~~c

undefined4 * FUN_00b9ddac(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3)

{
  ulong uVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined4 uVar4;
  size_t sVar5;
  long lVar6;
  ulong uVar7;
  undefined4 *puVar8;
  long lVar9;
  undefined4 *puVar10;
  long lVar11;
  long lVar12;
  ulong uVar13;
  long lVar14;
  undefined4 *puVar15;
  undefined4 *puVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  undefined8 uVar21;
  undefined8 uVar22;
  undefined8 uVar23;
  
  if (param_1 + 1 == param_2) {
    uVar4 = *param_1;
    sVar5 = (long)param_3 - (long)param_2;
    if (sVar5 != 0) {
      memmove(param_1,param_2,sVar5);
    }
    param_1[(long)sVar5 >> 2] = uVar4;
    param_3 = param_1 + ((long)sVar5 >> 2);
  }
  else if (param_2 + 1 == param_3) {
    uVar4 = param_3[-1];
    sVar5 = (long)(param_3 + -1) - (long)param_1;
    if (sVar5 != 0) {
      param_3 = (undefined4 *)((long)param_3 - sVar5);
      memmove(param_3,param_1,sVar5);
    }
    *param_1 = uVar4;
  }
  else {
    lVar9 = (long)param_2 - (long)param_1 >> 2;
    lVar6 = (long)param_3 - (long)param_2 >> 2;
    lVar14 = lVar9;
    lVar12 = lVar6;
    if (lVar9 == lVar6) {
      param_3 = param_1;
      if (param_1 != param_2) {
        uVar7 = ((long)param_2 - (long)param_1) - 4;
        uVar1 = (uVar7 >> 2) + 1;
        puVar8 = param_2;
        if ((7 < uVar1) &&
           ((lVar14 = (uVar7 & 0xfffffffffffffffc) + 4,
            (undefined4 *)((long)param_2 + lVar14) <= param_1 ||
            ((undefined4 *)((long)param_1 + lVar14) <= param_2)))) {
          uVar13 = uVar1 & 0x7ffffffffffffff8;
          lVar14 = 0;
          uVar7 = uVar13;
          do {
            puVar2 = (undefined8 *)((long)param_1 + lVar14);
            puVar3 = (undefined8 *)((long)param_2 + lVar14);
            uVar17 = *puVar3;
            uVar19 = puVar3[3];
            uVar18 = puVar3[2];
            uVar21 = puVar2[1];
            uVar20 = *puVar2;
            uVar23 = puVar2[3];
            uVar22 = puVar2[2];
            uVar7 = uVar7 - 8;
            lVar14 = lVar14 + 0x20;
            puVar2[1] = puVar3[1];
            *puVar2 = uVar17;
            puVar2[3] = uVar19;
            puVar2[2] = uVar18;
            puVar3[1] = uVar21;
            *puVar3 = uVar20;
            puVar3[3] = uVar23;
            puVar3[2] = uVar22;
          } while (uVar7 != 0);
          puVar8 = param_2 + uVar13;
          param_1 = param_1 + uVar13;
          if (uVar1 == uVar13) {
            return param_2;
          }
        }
        do {
          uVar4 = *param_1;
          puVar10 = param_1 + 1;
          *param_1 = *puVar8;
          *puVar8 = uVar4;
          puVar8 = puVar8 + 1;
          param_1 = puVar10;
          param_3 = param_2;
        } while (param_2 != puVar10);
      }
    }
    else {
      do {
        lVar11 = lVar12;
        lVar12 = 0;
        if (lVar11 != 0) {
          lVar12 = lVar14 / lVar11;
        }
        lVar12 = lVar14 - lVar12 * lVar11;
        lVar14 = lVar11;
      } while (lVar12 != 0);
      if (lVar11 != 0) {
        puVar8 = param_1 + lVar11;
        do {
          puVar8 = puVar8 + -1;
          uVar4 = *puVar8;
          puVar15 = puVar8;
          puVar10 = puVar8 + lVar9;
          do {
            puVar16 = puVar10;
            lVar14 = (long)param_3 - (long)puVar16 >> 2;
            puVar10 = puVar16 + lVar9;
            if (lVar14 <= lVar9) {
              puVar10 = param_1 + (lVar9 - lVar14);
            }
            *puVar15 = *puVar16;
            puVar15 = puVar16;
          } while (puVar10 != puVar8);
          *puVar16 = uVar4;
        } while (puVar8 != param_1);
      }
      param_3 = param_1 + lVar6;
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b9ddac"></a> `00b9ddac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b9ddb0"></a> `00b9ddb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b9ddb4"></a> `00b9ddb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b9ddb8"></a> `00b9ddb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b9ddbc"></a> `00b9ddbc` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00b9ddc0"></a> `00b9ddc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b9ddc4"></a> `00b9ddc4` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00b9ddc8"></a> `00b9ddc8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b9ddcc"></a> `00b9ddcc` | `60 04 00 54` | b.eq 0x00b9de58 | `CONDITIONAL_JUMP`
<a id="insn-00b9ddd0"></a> `00b9ddd0` | `28 10 00 91` | add x8,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00b9ddd4"></a> `00b9ddd4` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00b9ddd8"></a> `00b9ddd8` | `20 05 00 54` | b.eq 0x00b9de7c | `CONDITIONAL_JUMP`
<a id="insn-00b9dddc"></a> `00b9dddc` | `2a 00 13 cb` | sub x10,x1,x19 | `FALL_THROUGH`
<a id="insn-00b9dde0"></a> `00b9dde0` | `88 02 01 cb` | sub x8,x20,x1 | `FALL_THROUGH`
<a id="insn-00b9dde4"></a> `00b9dde4` | `49 fd 42 93` | asr x9,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00b9dde8"></a> `00b9dde8` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00b9ddec"></a> `00b9ddec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b9ddf0"></a> `00b9ddf0` | `c1 05 00 54` | b.ne 0x00b9dea8 | `CONDITIONAL_JUMP`
<a id="insn-00b9ddf4"></a> `00b9ddf4` | `7f 02 01 eb` | cmp x19,x1 | `FALL_THROUGH`
<a id="insn-00b9ddf8"></a> `00b9ddf8` | `00 09 00 54` | b.eq 0x00b9df18 | `CONDITIONAL_JUMP`
<a id="insn-00b9ddfc"></a> `00b9ddfc` | `48 11 00 d1` | sub x8,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00b9de00"></a> `00b9de00` | `09 fd 42 d3` | lsr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00b9de04"></a> `00b9de04` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b9de08"></a> `00b9de08` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-00b9de0c"></a> `00b9de0c` | `23 01 00 54` | b.cc 0x00b9de30 | `CONDITIONAL_JUMP`
<a id="insn-00b9de10"></a> `00b9de10` | `08 f5 7e 92` | and x8,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00b9de14"></a> `00b9de14` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b9de18"></a> `00b9de18` | `29 00 08 8b` | add x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00b9de1c"></a> `00b9de1c` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00b9de20"></a> `00b9de20` | `69 08 00 54` | b.ls 0x00b9df2c | `CONDITIONAL_JUMP`
<a id="insn-00b9de24"></a> `00b9de24` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00b9de28"></a> `00b9de28` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00b9de2c"></a> `00b9de2c` | `09 08 00 54` | b.ls 0x00b9df2c | `CONDITIONAL_JUMP`
<a id="insn-00b9de30"></a> `00b9de30` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b9de34"></a> `00b9de34` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-00b9de38"></a> `00b9de38` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b9de3c"></a> `00b9de3c` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b9de40"></a> `00b9de40` | `2a 45 00 b8` | str w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00b9de44"></a> `00b9de44` | `3f 00 09 eb` | cmp x1,x9 | `FALL_THROUGH`
<a id="insn-00b9de48"></a> `00b9de48` | `0b 45 00 b8` | str w11,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00b9de4c"></a> `00b9de4c` | `61 ff ff 54` | b.ne 0x00b9de38 | `CONDITIONAL_JUMP`
<a id="insn-00b9de50"></a> `00b9de50` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b9de54"></a> `00b9de54` | `31 00 00 14` | b 0x00b9df18 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9de58"></a> `00b9de58` | `75 02 40 b9` | ldr w21,[x19] | `FALL_THROUGH`
<a id="insn-00b9de5c"></a> `00b9de5c` | `82 02 01 eb` | subs x2,x20,x1 | `FALL_THROUGH`
<a id="insn-00b9de60"></a> `00b9de60` | `54 fc 42 93` | asr x20,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00b9de64"></a> `00b9de64` | `60 00 00 54` | b.eq 0x00b9de70 | `CONDITIONAL_JUMP`
<a id="insn-00b9de68"></a> `00b9de68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b9de6c"></a> `00b9de6c` | `69 e8 02 94` | bl 0x00c58010 | `UNCONDITIONAL_CALL`
<a id="insn-00b9de70"></a> `00b9de70` | `73 0a 14 8b` | add x19,x19,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9de74"></a> `00b9de74` | `75 02 00 b9` | str w21,[x19] | `FALL_THROUGH`
<a id="insn-00b9de78"></a> `00b9de78` | `28 00 00 14` | b 0x00b9df18 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9de7c"></a> `00b9de7c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b9de80"></a> `00b9de80` | `15 cd 5f b8` | ldr w21,[x8, #-0x4]! | `FALL_THROUGH`
<a id="insn-00b9de84"></a> `00b9de84` | `02 01 13 eb` | subs x2,x8,x19 | `FALL_THROUGH`
<a id="insn-00b9de88"></a> `00b9de88` | `a0 00 00 54` | b.eq 0x00b9de9c | `CONDITIONAL_JUMP`
<a id="insn-00b9de8c"></a> `00b9de8c` | `94 02 02 cb` | sub x20,x20,x2 | `FALL_THROUGH`
<a id="insn-00b9de90"></a> `00b9de90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b9de94"></a> `00b9de94` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b9de98"></a> `00b9de98` | `5e e8 02 94` | bl 0x00c58010 | `UNCONDITIONAL_CALL`
<a id="insn-00b9de9c"></a> `00b9de9c` | `75 02 00 b9` | str w21,[x19] | `FALL_THROUGH`
<a id="insn-00b9dea0"></a> `00b9dea0` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00b9dea4"></a> `00b9dea4` | `1d 00 00 14` | b 0x00b9df18 | `UNCONDITIONAL_JUMP`
<a id="insn-00b9dea8"></a> `00b9dea8` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00b9deac"></a> `00b9deac` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00b9deb0"></a> `00b9deb0` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00b9deb4"></a> `00b9deb4` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00b9deb8"></a> `00b9deb8` | `8b 0d cb 9a` | sdiv x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00b9debc"></a> `00b9debc` | `6b b1 0a 9b` | msub x11,x11,x10,x12 | `FALL_THROUGH`
<a id="insn-00b9dec0"></a> `00b9dec0` | `8b ff ff b5` | cbnz x11,0x00b9deb0 | `CONDITIONAL_JUMP`
<a id="insn-00b9dec4"></a> `00b9dec4` | `8a 02 00 b4` | cbz x10,0x00b9df14 | `CONDITIONAL_JUMP`
<a id="insn-00b9dec8"></a> `00b9dec8` | `6a 0a 0a 8b` | add x10,x19,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9decc"></a> `00b9decc` | `4b cd 5f b8` | ldr w11,[x10, #-0x4]! | `FALL_THROUGH`
<a id="insn-00b9ded0"></a> `00b9ded0` | `4e 09 09 8b` | add x14,x10,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9ded4"></a> `00b9ded4` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00b9ded8"></a> `00b9ded8` | `ec 03 0e aa` | mov x12,x14 | `FALL_THROUGH`
<a id="insn-00b9dedc"></a> `00b9dedc` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00b9dee0"></a> `00b9dee0` | `8e 02 0e cb` | sub x14,x20,x14 | `FALL_THROUGH`
<a id="insn-00b9dee4"></a> `00b9dee4` | `ce fd 42 93` | asr x14,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00b9dee8"></a> `00b9dee8` | `2e 01 0e eb` | subs x14,x9,x14 | `FALL_THROUGH`
<a id="insn-00b9deec"></a> `00b9deec` | `90 09 09 8b` | add x16,x12,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9def0"></a> `00b9def0` | `6e 0a 0e 8b` | add x14,x19,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9def4"></a> `00b9def4` | `0e b2 8e 9a` | csel x14,x16,x14,lt | `FALL_THROUGH`
<a id="insn-00b9def8"></a> `00b9def8` | `df 01 0a eb` | cmp x14,x10 | `FALL_THROUGH`
<a id="insn-00b9defc"></a> `00b9defc` | `af 01 00 b9` | str w15,[x13] | `FALL_THROUGH`
<a id="insn-00b9df00"></a> `00b9df00` | `ed 03 0c aa` | mov x13,x12 | `FALL_THROUGH`
<a id="insn-00b9df04"></a> `00b9df04` | `a1 fe ff 54` | b.ne 0x00b9ded8 | `CONDITIONAL_JUMP`
<a id="insn-00b9df08"></a> `00b9df08` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00b9df0c"></a> `00b9df0c` | `8b 01 00 b9` | str w11,[x12] | `FALL_THROUGH`
<a id="insn-00b9df10"></a> `00b9df10` | `e1 fd ff 54` | b.ne 0x00b9decc | `CONDITIONAL_JUMP`
<a id="insn-00b9df14"></a> `00b9df14` | `73 0a 08 8b` | add x19,x19,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00b9df18"></a> `00b9df18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b9df1c"></a> `00b9df1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b9df20"></a> `00b9df20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b9df24"></a> `00b9df24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b9df28"></a> `00b9df28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b9df2c"></a> `00b9df2c` | `4b ed 7d 92` | and x11,x10,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00b9df30"></a> `00b9df30` | `69 f5 7e d3` | lsl x9,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b9df34"></a> `00b9df34` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00b9df38"></a> `00b9df38` | `28 00 09 8b` | add x8,x1,x9 | `FALL_THROUGH`
<a id="insn-00b9df3c"></a> `00b9df3c` | `69 02 09 8b` | add x9,x19,x9 | `FALL_THROUGH`
<a id="insn-00b9df40"></a> `00b9df40` | `ed 03 0b aa` | mov x13,x11 | `FALL_THROUGH`
<a id="insn-00b9df44"></a> `00b9df44` | `6e 02 0c 8b` | add x14,x19,x12 | `FALL_THROUGH`
<a id="insn-00b9df48"></a> `00b9df48` | `2f 00 0c 8b` | add x15,x1,x12 | `FALL_THROUGH`
<a id="insn-00b9df4c"></a> `00b9df4c` | `e0 05 40 ad` | ldp q0,q1,[x15] | `FALL_THROUGH`
<a id="insn-00b9df50"></a> `00b9df50` | `c2 0d 40 ad` | ldp q2,q3,[x14] | `FALL_THROUGH`
<a id="insn-00b9df54"></a> `00b9df54` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00b9df58"></a> `00b9df58` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00b9df5c"></a> `00b9df5c` | `c0 05 00 ad` | stp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00b9df60"></a> `00b9df60` | `e2 0d 00 ad` | stp q2,q3,[x15] | `FALL_THROUGH`
<a id="insn-00b9df64"></a> `00b9df64` | `01 ff ff 54` | b.ne 0x00b9df44 | `CONDITIONAL_JUMP`
<a id="insn-00b9df68"></a> `00b9df68` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00b9df6c"></a> `00b9df6c` | `61 f6 ff 54` | b.ne 0x00b9de38 | `CONDITIONAL_JUMP`
<a id="insn-00b9df70"></a> `00b9df70` | `b8 ff ff 17` | b 0x00b9de50 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b9ddac`](#insn-00b9ddac) 範囲 `[['00b9ddac', '00b9ddcf']]`
  - `CONDITIONAL_JUMP` [`00b9ddcc`](#insn-00b9ddcc) → [`00b9de58`](#insn-00b9de58)
  - `FALL_THROUGH` [`00b9ddcc`](#insn-00b9ddcc) → [`00b9ddd0`](#insn-00b9ddd0)
- ブロック [`00b9ddd0`](#insn-00b9ddd0) 範囲 `[['00b9ddd0', '00b9dddb']]`
  - `CONDITIONAL_JUMP` [`00b9ddd8`](#insn-00b9ddd8) → [`00b9de7c`](#insn-00b9de7c)
  - `FALL_THROUGH` [`00b9ddd8`](#insn-00b9ddd8) → [`00b9dddc`](#insn-00b9dddc)
- ブロック [`00b9dddc`](#insn-00b9dddc) 範囲 `[['00b9dddc', '00b9ddf3']]`
  - `CONDITIONAL_JUMP` [`00b9ddf0`](#insn-00b9ddf0) → [`00b9dea8`](#insn-00b9dea8)
  - `FALL_THROUGH` [`00b9ddf0`](#insn-00b9ddf0) → [`00b9ddf4`](#insn-00b9ddf4)
- ブロック [`00b9ddf4`](#insn-00b9ddf4) 範囲 `[['00b9ddf4', '00b9ddfb']]`
  - `CONDITIONAL_JUMP` [`00b9ddf8`](#insn-00b9ddf8) → [`00b9df18`](#insn-00b9df18)
  - `FALL_THROUGH` [`00b9ddf8`](#insn-00b9ddf8) → [`00b9ddfc`](#insn-00b9ddfc)
- ブロック [`00b9ddfc`](#insn-00b9ddfc) 範囲 `[['00b9ddfc', '00b9de0f']]`
  - `CONDITIONAL_JUMP` [`00b9de0c`](#insn-00b9de0c) → [`00b9de30`](#insn-00b9de30)
  - `FALL_THROUGH` [`00b9de0c`](#insn-00b9de0c) → [`00b9de10`](#insn-00b9de10)
- ブロック [`00b9de10`](#insn-00b9de10) 範囲 `[['00b9de10', '00b9de23']]`
  - `CONDITIONAL_JUMP` [`00b9de20`](#insn-00b9de20) → [`00b9df2c`](#insn-00b9df2c)
  - `FALL_THROUGH` [`00b9de20`](#insn-00b9de20) → [`00b9de24`](#insn-00b9de24)
- ブロック [`00b9de24`](#insn-00b9de24) 範囲 `[['00b9de24', '00b9de2f']]`
  - `CONDITIONAL_JUMP` [`00b9de2c`](#insn-00b9de2c) → [`00b9df2c`](#insn-00b9df2c)
  - `FALL_THROUGH` [`00b9de2c`](#insn-00b9de2c) → [`00b9de30`](#insn-00b9de30)
- ブロック [`00b9de30`](#insn-00b9de30) 範囲 `[['00b9de30', '00b9de37']]`
  - `FALL_THROUGH` [`00b9de34`](#insn-00b9de34) → [`00b9de38`](#insn-00b9de38)
- ブロック [`00b9de38`](#insn-00b9de38) 範囲 `[['00b9de38', '00b9de4f']]`
  - `CONDITIONAL_JUMP` [`00b9de4c`](#insn-00b9de4c) → [`00b9de38`](#insn-00b9de38)
  - `FALL_THROUGH` [`00b9de4c`](#insn-00b9de4c) → [`00b9de50`](#insn-00b9de50)
- ブロック [`00b9de50`](#insn-00b9de50) 範囲 `[['00b9de50', '00b9de57']]`
  - `UNCONDITIONAL_JUMP` [`00b9de54`](#insn-00b9de54) → [`00b9df18`](#insn-00b9df18)
- ブロック [`00b9de58`](#insn-00b9de58) 範囲 `[['00b9de58', '00b9de67']]`
  - `CONDITIONAL_JUMP` [`00b9de64`](#insn-00b9de64) → [`00b9de70`](#insn-00b9de70)
  - `FALL_THROUGH` [`00b9de64`](#insn-00b9de64) → [`00b9de68`](#insn-00b9de68)
- ブロック [`00b9de68`](#insn-00b9de68) 範囲 `[['00b9de68', '00b9de6f']]`
  - `FALL_THROUGH` [`00b9de6c`](#insn-00b9de6c) → [`00b9de70`](#insn-00b9de70)
- ブロック [`00b9de70`](#insn-00b9de70) 範囲 `[['00b9de70', '00b9de7b']]`
  - `UNCONDITIONAL_JUMP` [`00b9de78`](#insn-00b9de78) → [`00b9df18`](#insn-00b9df18)
- ブロック [`00b9de7c`](#insn-00b9de7c) 範囲 `[['00b9de7c', '00b9de8b']]`
  - `CONDITIONAL_JUMP` [`00b9de88`](#insn-00b9de88) → [`00b9de9c`](#insn-00b9de9c)
  - `FALL_THROUGH` [`00b9de88`](#insn-00b9de88) → [`00b9de8c`](#insn-00b9de8c)
- ブロック [`00b9de8c`](#insn-00b9de8c) 範囲 `[['00b9de8c', '00b9de9b']]`
  - `FALL_THROUGH` [`00b9de98`](#insn-00b9de98) → [`00b9de9c`](#insn-00b9de9c)
- ブロック [`00b9de9c`](#insn-00b9de9c) 範囲 `[['00b9de9c', '00b9dea7']]`
  - `UNCONDITIONAL_JUMP` [`00b9dea4`](#insn-00b9dea4) → [`00b9df18`](#insn-00b9df18)
- ブロック [`00b9dea8`](#insn-00b9dea8) 範囲 `[['00b9dea8', '00b9deaf']]`
  - `FALL_THROUGH` [`00b9deac`](#insn-00b9deac) → [`00b9deb0`](#insn-00b9deb0)
- ブロック [`00b9deb0`](#insn-00b9deb0) 範囲 `[['00b9deb0', '00b9dec3']]`
  - `CONDITIONAL_JUMP` [`00b9dec0`](#insn-00b9dec0) → [`00b9deb0`](#insn-00b9deb0)
  - `FALL_THROUGH` [`00b9dec0`](#insn-00b9dec0) → [`00b9dec4`](#insn-00b9dec4)
- ブロック [`00b9dec4`](#insn-00b9dec4) 範囲 `[['00b9dec4', '00b9dec7']]`
  - `CONDITIONAL_JUMP` [`00b9dec4`](#insn-00b9dec4) → [`00b9df14`](#insn-00b9df14)
  - `FALL_THROUGH` [`00b9dec4`](#insn-00b9dec4) → [`00b9dec8`](#insn-00b9dec8)
- ブロック [`00b9dec8`](#insn-00b9dec8) 範囲 `[['00b9dec8', '00b9decb']]`
  - `FALL_THROUGH` [`00b9dec8`](#insn-00b9dec8) → [`00b9decc`](#insn-00b9decc)
- ブロック [`00b9decc`](#insn-00b9decc) 範囲 `[['00b9decc', '00b9ded7']]`
  - `FALL_THROUGH` [`00b9ded4`](#insn-00b9ded4) → [`00b9ded8`](#insn-00b9ded8)
- ブロック [`00b9ded8`](#insn-00b9ded8) 範囲 `[['00b9ded8', '00b9df07']]`
  - `CONDITIONAL_JUMP` [`00b9df04`](#insn-00b9df04) → [`00b9ded8`](#insn-00b9ded8)
  - `FALL_THROUGH` [`00b9df04`](#insn-00b9df04) → [`00b9df08`](#insn-00b9df08)
- ブロック [`00b9df08`](#insn-00b9df08) 範囲 `[['00b9df08', '00b9df13']]`
  - `CONDITIONAL_JUMP` [`00b9df10`](#insn-00b9df10) → [`00b9decc`](#insn-00b9decc)
  - `FALL_THROUGH` [`00b9df10`](#insn-00b9df10) → [`00b9df14`](#insn-00b9df14)
- ブロック [`00b9df14`](#insn-00b9df14) 範囲 `[['00b9df14', '00b9df17']]`
  - `FALL_THROUGH` [`00b9df14`](#insn-00b9df14) → [`00b9df18`](#insn-00b9df18)
- ブロック [`00b9df18`](#insn-00b9df18) 範囲 `[['00b9df18', '00b9df2b']]`
- ブロック [`00b9df2c`](#insn-00b9df2c) 範囲 `[['00b9df2c', '00b9df43']]`
  - `FALL_THROUGH` [`00b9df40`](#insn-00b9df40) → [`00b9df44`](#insn-00b9df44)
- ブロック [`00b9df44`](#insn-00b9df44) 範囲 `[['00b9df44', '00b9df67']]`
  - `CONDITIONAL_JUMP` [`00b9df64`](#insn-00b9df64) → [`00b9df44`](#insn-00b9df44)
  - `FALL_THROUGH` [`00b9df64`](#insn-00b9df64) → [`00b9df68`](#insn-00b9df68)
- ブロック [`00b9df68`](#insn-00b9df68) 範囲 `[['00b9df68', '00b9df6f']]`
  - `CONDITIONAL_JUMP` [`00b9df6c`](#insn-00b9df6c) → [`00b9de38`](#insn-00b9de38)
  - `FALL_THROUGH` [`00b9df6c`](#insn-00b9df6c) → [`00b9df70`](#insn-00b9df70)
- ブロック [`00b9df70`](#insn-00b9df70) 範囲 `[['00b9df70', '00b9df73']]`
  - `UNCONDITIONAL_JUMP` [`00b9df70`](#insn-00b9df70) → [`00b9de50`](#insn-00b9de50)

## 命令位置別の参照

- [`00b9ddac`](#insn-00b9ddac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddb0`](#insn-00b9ddb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddb4`](#insn-00b9ddb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddcc`](#insn-00b9ddcc) → [`00b9de58`](#insn-00b9de58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddd8`](#insn-00b9ddd8) → [`00b9de7c`](#insn-00b9de7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddf0`](#insn-00b9ddf0) → [`00b9dea8`](#insn-00b9dea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9ddf8`](#insn-00b9ddf8) → [`00b9df18`](#insn-00b9df18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de0c`](#insn-00b9de0c) → [`00b9de30`](#insn-00b9de30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de20`](#insn-00b9de20) → [`00b9df2c`](#insn-00b9df2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de2c`](#insn-00b9de2c) → [`00b9df2c`](#insn-00b9df2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de4c`](#insn-00b9de4c) → [`00b9de38`](#insn-00b9de38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de54`](#insn-00b9de54) → [`00b9df18`](#insn-00b9df18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de64`](#insn-00b9de64) → [`00b9de70`](#insn-00b9de70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de6c`](#insn-00b9de6c) → [`00c58010`](../00c58/00c58010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58010` · 推定シンボル `None` · 推定型 `None`
- [`00b9de78`](#insn-00b9de78) → [`00b9df18`](#insn-00b9df18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de88`](#insn-00b9de88) → [`00b9de9c`](#insn-00b9de9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9de98`](#insn-00b9de98) → [`00c58010`](../00c58/00c58010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58010` · 推定シンボル `None` · 推定型 `None`
- [`00b9dea4`](#insn-00b9dea4) → [`00b9df18`](#insn-00b9df18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9dec0`](#insn-00b9dec0) → [`00b9deb0`](#insn-00b9deb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9dec4`](#insn-00b9dec4) → [`00b9df14`](#insn-00b9df14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df04`](#insn-00b9df04) → [`00b9ded8`](#insn-00b9ded8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df10`](#insn-00b9df10) → [`00b9decc`](#insn-00b9decc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df1c`](#insn-00b9df1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df20`](#insn-00b9df20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df64`](#insn-00b9df64) → [`00b9df44`](#insn-00b9df44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df6c`](#insn-00b9df6c) → [`00b9de38`](#insn-00b9de38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b9df70`](#insn-00b9df70) → [`00b9de50`](#insn-00b9de50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b9ddac`](#insn-00b9ddac)

~~~json
{
  "source": "00b9ddac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddb0`](#insn-00b9ddb0)

~~~json
{
  "source": "00b9ddb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddb4`](#insn-00b9ddb4)

~~~json
{
  "source": "00b9ddb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddcc`](#insn-00b9ddcc)

~~~json
{
  "source": "00b9ddcc",
  "target": "00b9de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddd8`](#insn-00b9ddd8)

~~~json
{
  "source": "00b9ddd8",
  "target": "00b9de7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddf0`](#insn-00b9ddf0)

~~~json
{
  "source": "00b9ddf0",
  "target": "00b9dea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9ddf8`](#insn-00b9ddf8)

~~~json
{
  "source": "00b9ddf8",
  "target": "00b9df18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de0c`](#insn-00b9de0c)

~~~json
{
  "source": "00b9de0c",
  "target": "00b9de30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de20`](#insn-00b9de20)

~~~json
{
  "source": "00b9de20",
  "target": "00b9df2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de2c`](#insn-00b9de2c)

~~~json
{
  "source": "00b9de2c",
  "target": "00b9df2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de4c`](#insn-00b9de4c)

~~~json
{
  "source": "00b9de4c",
  "target": "00b9de38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de54`](#insn-00b9de54)

~~~json
{
  "source": "00b9de54",
  "target": "00b9df18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de64`](#insn-00b9de64)

~~~json
{
  "source": "00b9de64",
  "target": "00b9de70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de6c`](#insn-00b9de6c)

~~~json
{
  "source": "00b9de6c",
  "target": "00c58010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b9de78`](#insn-00b9de78)

~~~json
{
  "source": "00b9de78",
  "target": "00b9df18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de88`](#insn-00b9de88)

~~~json
{
  "source": "00b9de88",
  "target": "00b9de9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9de98`](#insn-00b9de98)

~~~json
{
  "source": "00b9de98",
  "target": "00c58010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b9dea4`](#insn-00b9dea4)

~~~json
{
  "source": "00b9dea4",
  "target": "00b9df18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9dec0`](#insn-00b9dec0)

~~~json
{
  "source": "00b9dec0",
  "target": "00b9deb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9dec4`](#insn-00b9dec4)

~~~json
{
  "source": "00b9dec4",
  "target": "00b9df14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df04`](#insn-00b9df04)

~~~json
{
  "source": "00b9df04",
  "target": "00b9ded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df10`](#insn-00b9df10)

~~~json
{
  "source": "00b9df10",
  "target": "00b9decc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df1c`](#insn-00b9df1c)

~~~json
{
  "source": "00b9df1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df20`](#insn-00b9df20)

~~~json
{
  "source": "00b9df20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df64`](#insn-00b9df64)

~~~json
{
  "source": "00b9df64",
  "target": "00b9df44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df6c`](#insn-00b9df6c)

~~~json
{
  "source": "00b9df6c",
  "target": "00b9de38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b9df70`](#insn-00b9df70)

~~~json
{
  "source": "00b9df70",
  "target": "00b9de50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
