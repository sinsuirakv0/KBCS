# 00ba5dac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0005.md#review-2d2e604abbaec1a1da03222f919406f1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ba727c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba7/00ba727c.md) · 移動量 `+0x14d0`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-db5e8d92c3512c7c986b6e45dadfbf27)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba5dac",
  "name": "FUN_00ba5dac",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edc987e7fae90aca50354b8fa60524d102bfb046d8f6c9045311931be3fc7448",
  "source_text_sha256": "edc987e7fae90aca50354b8fa60524d102bfb046d8f6c9045311931be3fc7448",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba5dac",
        "00ba5f73"
      ]
    ],
    "bytes_sha256": "a53ee1e0177d67f07ad8e79500c405cb583de0a4d3708c4fc3a8c3a3df7c30e8",
    "instruction_count": 114,
    "instruction_bytes": 456,
    "body_bytes": 456,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ba53b8](../00ba5/00ba53b8.md)

## 呼び出し先

- [00c57f40](../00c57/00c57f40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4245 bytes

~~~c

undefined4 * FUN_00ba5dac(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3)

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
  else {
                    /* try { // try from 00ba5dd4 to 00ca5ddf has its CatchHandler @ 00ba6000 */
    if (param_2 + 1 == param_3) {
      uVar4 = param_3[-1];
      sVar5 = (long)(param_3 + -1) - (long)param_1;
      if (sVar5 != 0) {
        param_3 = (undefined4 *)((long)param_3 - sVar5);
        memmove(param_3,param_1,sVar5);
      }
      *param_1 = uVar4;
    }
    else {
                    /* try { // try from 00ba5de0 to 00ca5deb has its CatchHandler @ 00ba5f7c */
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
                    /* try { // try from 00ba5f4c to 00ca5f53 has its CatchHandler @ 00ba6070 */
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
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba5dac"></a> `00ba5dac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ba5db0"></a> `00ba5db0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba5db4"></a> `00ba5db4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba5db8"></a> `00ba5db8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba5dbc"></a> `00ba5dbc` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00ba5dc0"></a> `00ba5dc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba5dc4"></a> `00ba5dc4` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00ba5dc8"></a> `00ba5dc8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00ba5dcc"></a> `00ba5dcc` | `60 04 00 54` | b.eq 0x00ba5e58 | `CONDITIONAL_JUMP`
<a id="insn-00ba5dd0"></a> `00ba5dd0` | `28 10 00 91` | add x8,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00ba5dd4"></a> `00ba5dd4` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00ba5dd8"></a> `00ba5dd8` | `20 05 00 54` | b.eq 0x00ba5e7c | `CONDITIONAL_JUMP`
<a id="insn-00ba5ddc"></a> `00ba5ddc` | `2a 00 13 cb` | sub x10,x1,x19 | `FALL_THROUGH`
<a id="insn-00ba5de0"></a> `00ba5de0` | `88 02 01 cb` | sub x8,x20,x1 | `FALL_THROUGH`
<a id="insn-00ba5de4"></a> `00ba5de4` | `49 fd 42 93` | asr x9,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5de8"></a> `00ba5de8` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5dec"></a> `00ba5dec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00ba5df0"></a> `00ba5df0` | `c1 05 00 54` | b.ne 0x00ba5ea8 | `CONDITIONAL_JUMP`
<a id="insn-00ba5df4"></a> `00ba5df4` | `7f 02 01 eb` | cmp x19,x1 | `FALL_THROUGH`
<a id="insn-00ba5df8"></a> `00ba5df8` | `00 09 00 54` | b.eq 0x00ba5f18 | `CONDITIONAL_JUMP`
<a id="insn-00ba5dfc"></a> `00ba5dfc` | `48 11 00 d1` | sub x8,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00ba5e00"></a> `00ba5e00` | `09 fd 42 d3` | lsr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5e04"></a> `00ba5e04` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba5e08"></a> `00ba5e08` | `5f 21 00 f1` | cmp x10,#0x8 | `FALL_THROUGH`
<a id="insn-00ba5e0c"></a> `00ba5e0c` | `23 01 00 54` | b.cc 0x00ba5e30 | `CONDITIONAL_JUMP`
<a id="insn-00ba5e10"></a> `00ba5e10` | `08 f5 7e 92` | and x8,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba5e14"></a> `00ba5e14` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba5e18"></a> `00ba5e18` | `29 00 08 8b` | add x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00ba5e1c"></a> `00ba5e1c` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00ba5e20"></a> `00ba5e20` | `69 08 00 54` | b.ls 0x00ba5f2c | `CONDITIONAL_JUMP`
<a id="insn-00ba5e24"></a> `00ba5e24` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba5e28"></a> `00ba5e28` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00ba5e2c"></a> `00ba5e2c` | `09 08 00 54` | b.ls 0x00ba5f2c | `CONDITIONAL_JUMP`
<a id="insn-00ba5e30"></a> `00ba5e30` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ba5e34"></a> `00ba5e34` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-00ba5e38"></a> `00ba5e38` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00ba5e3c"></a> `00ba5e3c` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00ba5e40"></a> `00ba5e40` | `2a 45 00 b8` | str w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00ba5e44"></a> `00ba5e44` | `3f 00 09 eb` | cmp x1,x9 | `FALL_THROUGH`
<a id="insn-00ba5e48"></a> `00ba5e48` | `0b 45 00 b8` | str w11,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00ba5e4c"></a> `00ba5e4c` | `61 ff ff 54` | b.ne 0x00ba5e38 | `CONDITIONAL_JUMP`
<a id="insn-00ba5e50"></a> `00ba5e50` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba5e54"></a> `00ba5e54` | `31 00 00 14` | b 0x00ba5f18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba5e58"></a> `00ba5e58` | `75 02 40 b9` | ldr w21,[x19] | `FALL_THROUGH`
<a id="insn-00ba5e5c"></a> `00ba5e5c` | `82 02 01 eb` | subs x2,x20,x1 | `FALL_THROUGH`
<a id="insn-00ba5e60"></a> `00ba5e60` | `54 fc 42 93` | asr x20,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5e64"></a> `00ba5e64` | `60 00 00 54` | b.eq 0x00ba5e70 | `CONDITIONAL_JUMP`
<a id="insn-00ba5e68"></a> `00ba5e68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5e6c"></a> `00ba5e6c` | `35 c8 02 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5e70"></a> `00ba5e70` | `73 0a 14 8b` | add x19,x19,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5e74"></a> `00ba5e74` | `75 02 00 b9` | str w21,[x19] | `FALL_THROUGH`
<a id="insn-00ba5e78"></a> `00ba5e78` | `28 00 00 14` | b 0x00ba5f18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba5e7c"></a> `00ba5e7c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00ba5e80"></a> `00ba5e80` | `15 cd 5f b8` | ldr w21,[x8, #-0x4]! | `FALL_THROUGH`
<a id="insn-00ba5e84"></a> `00ba5e84` | `02 01 13 eb` | subs x2,x8,x19 | `FALL_THROUGH`
<a id="insn-00ba5e88"></a> `00ba5e88` | `a0 00 00 54` | b.eq 0x00ba5e9c | `CONDITIONAL_JUMP`
<a id="insn-00ba5e8c"></a> `00ba5e8c` | `94 02 02 cb` | sub x20,x20,x2 | `FALL_THROUGH`
<a id="insn-00ba5e90"></a> `00ba5e90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba5e94"></a> `00ba5e94` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ba5e98"></a> `00ba5e98` | `2a c8 02 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5e9c"></a> `00ba5e9c` | `75 02 00 b9` | str w21,[x19] | `FALL_THROUGH`
<a id="insn-00ba5ea0"></a> `00ba5ea0` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00ba5ea4"></a> `00ba5ea4` | `1d 00 00 14` | b 0x00ba5f18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba5ea8"></a> `00ba5ea8` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00ba5eac"></a> `00ba5eac` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00ba5eb0"></a> `00ba5eb0` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00ba5eb4"></a> `00ba5eb4` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00ba5eb8"></a> `00ba5eb8` | `8b 0d cb 9a` | sdiv x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00ba5ebc"></a> `00ba5ebc` | `6b b1 0a 9b` | msub x11,x11,x10,x12 | `FALL_THROUGH`
<a id="insn-00ba5ec0"></a> `00ba5ec0` | `8b ff ff b5` | cbnz x11,0x00ba5eb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba5ec4"></a> `00ba5ec4` | `8a 02 00 b4` | cbz x10,0x00ba5f14 | `CONDITIONAL_JUMP`
<a id="insn-00ba5ec8"></a> `00ba5ec8` | `6a 0a 0a 8b` | add x10,x19,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5ecc"></a> `00ba5ecc` | `4b cd 5f b8` | ldr w11,[x10, #-0x4]! | `FALL_THROUGH`
<a id="insn-00ba5ed0"></a> `00ba5ed0` | `4e 09 09 8b` | add x14,x10,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5ed4"></a> `00ba5ed4` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00ba5ed8"></a> `00ba5ed8` | `ec 03 0e aa` | mov x12,x14 | `FALL_THROUGH`
<a id="insn-00ba5edc"></a> `00ba5edc` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00ba5ee0"></a> `00ba5ee0` | `8e 02 0e cb` | sub x14,x20,x14 | `FALL_THROUGH`
<a id="insn-00ba5ee4"></a> `00ba5ee4` | `ce fd 42 93` | asr x14,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5ee8"></a> `00ba5ee8` | `2e 01 0e eb` | subs x14,x9,x14 | `FALL_THROUGH`
<a id="insn-00ba5eec"></a> `00ba5eec` | `90 09 09 8b` | add x16,x12,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5ef0"></a> `00ba5ef0` | `6e 0a 0e 8b` | add x14,x19,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5ef4"></a> `00ba5ef4` | `0e b2 8e 9a` | csel x14,x16,x14,lt | `FALL_THROUGH`
<a id="insn-00ba5ef8"></a> `00ba5ef8` | `df 01 0a eb` | cmp x14,x10 | `FALL_THROUGH`
<a id="insn-00ba5efc"></a> `00ba5efc` | `af 01 00 b9` | str w15,[x13] | `FALL_THROUGH`
<a id="insn-00ba5f00"></a> `00ba5f00` | `ed 03 0c aa` | mov x13,x12 | `FALL_THROUGH`
<a id="insn-00ba5f04"></a> `00ba5f04` | `a1 fe ff 54` | b.ne 0x00ba5ed8 | `CONDITIONAL_JUMP`
<a id="insn-00ba5f08"></a> `00ba5f08` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00ba5f0c"></a> `00ba5f0c` | `8b 01 00 b9` | str w11,[x12] | `FALL_THROUGH`
<a id="insn-00ba5f10"></a> `00ba5f10` | `e1 fd ff 54` | b.ne 0x00ba5ecc | `CONDITIONAL_JUMP`
<a id="insn-00ba5f14"></a> `00ba5f14` | `73 0a 08 8b` | add x19,x19,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5f18"></a> `00ba5f18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5f1c"></a> `00ba5f1c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba5f20"></a> `00ba5f20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba5f24"></a> `00ba5f24` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ba5f28"></a> `00ba5f28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba5f2c"></a> `00ba5f2c` | `4b ed 7d 92` | and x11,x10,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba5f30"></a> `00ba5f30` | `69 f5 7e d3` | lsl x9,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5f34"></a> `00ba5f34` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00ba5f38"></a> `00ba5f38` | `28 00 09 8b` | add x8,x1,x9 | `FALL_THROUGH`
<a id="insn-00ba5f3c"></a> `00ba5f3c` | `69 02 09 8b` | add x9,x19,x9 | `FALL_THROUGH`
<a id="insn-00ba5f40"></a> `00ba5f40` | `ed 03 0b aa` | mov x13,x11 | `FALL_THROUGH`
<a id="insn-00ba5f44"></a> `00ba5f44` | `6e 02 0c 8b` | add x14,x19,x12 | `FALL_THROUGH`
<a id="insn-00ba5f48"></a> `00ba5f48` | `2f 00 0c 8b` | add x15,x1,x12 | `FALL_THROUGH`
<a id="insn-00ba5f4c"></a> `00ba5f4c` | `e0 05 40 ad` | ldp q0,q1,[x15] | `FALL_THROUGH`
<a id="insn-00ba5f50"></a> `00ba5f50` | `c2 0d 40 ad` | ldp q2,q3,[x14] | `FALL_THROUGH`
<a id="insn-00ba5f54"></a> `00ba5f54` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00ba5f58"></a> `00ba5f58` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00ba5f5c"></a> `00ba5f5c` | `c0 05 00 ad` | stp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00ba5f60"></a> `00ba5f60` | `e2 0d 00 ad` | stp q2,q3,[x15] | `FALL_THROUGH`
<a id="insn-00ba5f64"></a> `00ba5f64` | `01 ff ff 54` | b.ne 0x00ba5f44 | `CONDITIONAL_JUMP`
<a id="insn-00ba5f68"></a> `00ba5f68` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00ba5f6c"></a> `00ba5f6c` | `61 f6 ff 54` | b.ne 0x00ba5e38 | `CONDITIONAL_JUMP`
<a id="insn-00ba5f70"></a> `00ba5f70` | `b8 ff ff 17` | b 0x00ba5e50 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00ba5dac`](#insn-00ba5dac) 範囲 `[['00ba5dac', '00ba5dcf']]`
  - `CONDITIONAL_JUMP` [`00ba5dcc`](#insn-00ba5dcc) → [`00ba5e58`](#insn-00ba5e58)
  - `FALL_THROUGH` [`00ba5dcc`](#insn-00ba5dcc) → [`00ba5dd0`](#insn-00ba5dd0)
- ブロック [`00ba5dd0`](#insn-00ba5dd0) 範囲 `[['00ba5dd0', '00ba5dd3']]`
  - `FALL_THROUGH` [`00ba5dd0`](#insn-00ba5dd0) → [`00ba5dd4`](#insn-00ba5dd4)
- ブロック [`00ba5dd4`](#insn-00ba5dd4) 範囲 `[['00ba5dd4', '00ba5ddb']]`
  - `CONDITIONAL_JUMP` [`00ba5dd8`](#insn-00ba5dd8) → [`00ba5e7c`](#insn-00ba5e7c)
  - `FALL_THROUGH` [`00ba5dd8`](#insn-00ba5dd8) → [`00ba5ddc`](#insn-00ba5ddc)
- ブロック [`00ba5ddc`](#insn-00ba5ddc) 範囲 `[['00ba5ddc', '00ba5ddf']]`
  - `FALL_THROUGH` [`00ba5ddc`](#insn-00ba5ddc) → [`00ba5de0`](#insn-00ba5de0)
- ブロック [`00ba5de0`](#insn-00ba5de0) 範囲 `[['00ba5de0', '00ba5df3']]`
  - `CONDITIONAL_JUMP` [`00ba5df0`](#insn-00ba5df0) → [`00ba5ea8`](#insn-00ba5ea8)
  - `FALL_THROUGH` [`00ba5df0`](#insn-00ba5df0) → [`00ba5df4`](#insn-00ba5df4)
- ブロック [`00ba5df4`](#insn-00ba5df4) 範囲 `[['00ba5df4', '00ba5dfb']]`
  - `CONDITIONAL_JUMP` [`00ba5df8`](#insn-00ba5df8) → [`00ba5f18`](#insn-00ba5f18)
  - `FALL_THROUGH` [`00ba5df8`](#insn-00ba5df8) → [`00ba5dfc`](#insn-00ba5dfc)
- ブロック [`00ba5dfc`](#insn-00ba5dfc) 範囲 `[['00ba5dfc', '00ba5e0f']]`
  - `CONDITIONAL_JUMP` [`00ba5e0c`](#insn-00ba5e0c) → [`00ba5e30`](#insn-00ba5e30)
  - `FALL_THROUGH` [`00ba5e0c`](#insn-00ba5e0c) → [`00ba5e10`](#insn-00ba5e10)
- ブロック [`00ba5e10`](#insn-00ba5e10) 範囲 `[['00ba5e10', '00ba5e23']]`
  - `CONDITIONAL_JUMP` [`00ba5e20`](#insn-00ba5e20) → [`00ba5f2c`](#insn-00ba5f2c)
  - `FALL_THROUGH` [`00ba5e20`](#insn-00ba5e20) → [`00ba5e24`](#insn-00ba5e24)
- ブロック [`00ba5e24`](#insn-00ba5e24) 範囲 `[['00ba5e24', '00ba5e2f']]`
  - `CONDITIONAL_JUMP` [`00ba5e2c`](#insn-00ba5e2c) → [`00ba5f2c`](#insn-00ba5f2c)
  - `FALL_THROUGH` [`00ba5e2c`](#insn-00ba5e2c) → [`00ba5e30`](#insn-00ba5e30)
- ブロック [`00ba5e30`](#insn-00ba5e30) 範囲 `[['00ba5e30', '00ba5e37']]`
  - `FALL_THROUGH` [`00ba5e34`](#insn-00ba5e34) → [`00ba5e38`](#insn-00ba5e38)
- ブロック [`00ba5e38`](#insn-00ba5e38) 範囲 `[['00ba5e38', '00ba5e4f']]`
  - `CONDITIONAL_JUMP` [`00ba5e4c`](#insn-00ba5e4c) → [`00ba5e38`](#insn-00ba5e38)
  - `FALL_THROUGH` [`00ba5e4c`](#insn-00ba5e4c) → [`00ba5e50`](#insn-00ba5e50)
- ブロック [`00ba5e50`](#insn-00ba5e50) 範囲 `[['00ba5e50', '00ba5e57']]`
  - `UNCONDITIONAL_JUMP` [`00ba5e54`](#insn-00ba5e54) → [`00ba5f18`](#insn-00ba5f18)
- ブロック [`00ba5e58`](#insn-00ba5e58) 範囲 `[['00ba5e58', '00ba5e67']]`
  - `CONDITIONAL_JUMP` [`00ba5e64`](#insn-00ba5e64) → [`00ba5e70`](#insn-00ba5e70)
  - `FALL_THROUGH` [`00ba5e64`](#insn-00ba5e64) → [`00ba5e68`](#insn-00ba5e68)
- ブロック [`00ba5e68`](#insn-00ba5e68) 範囲 `[['00ba5e68', '00ba5e6f']]`
  - `FALL_THROUGH` [`00ba5e6c`](#insn-00ba5e6c) → [`00ba5e70`](#insn-00ba5e70)
- ブロック [`00ba5e70`](#insn-00ba5e70) 範囲 `[['00ba5e70', '00ba5e7b']]`
  - `UNCONDITIONAL_JUMP` [`00ba5e78`](#insn-00ba5e78) → [`00ba5f18`](#insn-00ba5f18)
- ブロック [`00ba5e7c`](#insn-00ba5e7c) 範囲 `[['00ba5e7c', '00ba5e8b']]`
  - `CONDITIONAL_JUMP` [`00ba5e88`](#insn-00ba5e88) → [`00ba5e9c`](#insn-00ba5e9c)
  - `FALL_THROUGH` [`00ba5e88`](#insn-00ba5e88) → [`00ba5e8c`](#insn-00ba5e8c)
- ブロック [`00ba5e8c`](#insn-00ba5e8c) 範囲 `[['00ba5e8c', '00ba5e9b']]`
  - `FALL_THROUGH` [`00ba5e98`](#insn-00ba5e98) → [`00ba5e9c`](#insn-00ba5e9c)
- ブロック [`00ba5e9c`](#insn-00ba5e9c) 範囲 `[['00ba5e9c', '00ba5ea7']]`
  - `UNCONDITIONAL_JUMP` [`00ba5ea4`](#insn-00ba5ea4) → [`00ba5f18`](#insn-00ba5f18)
- ブロック [`00ba5ea8`](#insn-00ba5ea8) 範囲 `[['00ba5ea8', '00ba5eaf']]`
  - `FALL_THROUGH` [`00ba5eac`](#insn-00ba5eac) → [`00ba5eb0`](#insn-00ba5eb0)
- ブロック [`00ba5eb0`](#insn-00ba5eb0) 範囲 `[['00ba5eb0', '00ba5ec3']]`
  - `CONDITIONAL_JUMP` [`00ba5ec0`](#insn-00ba5ec0) → [`00ba5eb0`](#insn-00ba5eb0)
  - `FALL_THROUGH` [`00ba5ec0`](#insn-00ba5ec0) → [`00ba5ec4`](#insn-00ba5ec4)
- ブロック [`00ba5ec4`](#insn-00ba5ec4) 範囲 `[['00ba5ec4', '00ba5ec7']]`
  - `CONDITIONAL_JUMP` [`00ba5ec4`](#insn-00ba5ec4) → [`00ba5f14`](#insn-00ba5f14)
  - `FALL_THROUGH` [`00ba5ec4`](#insn-00ba5ec4) → [`00ba5ec8`](#insn-00ba5ec8)
- ブロック [`00ba5ec8`](#insn-00ba5ec8) 範囲 `[['00ba5ec8', '00ba5ecb']]`
  - `FALL_THROUGH` [`00ba5ec8`](#insn-00ba5ec8) → [`00ba5ecc`](#insn-00ba5ecc)
- ブロック [`00ba5ecc`](#insn-00ba5ecc) 範囲 `[['00ba5ecc', '00ba5ed7']]`
  - `FALL_THROUGH` [`00ba5ed4`](#insn-00ba5ed4) → [`00ba5ed8`](#insn-00ba5ed8)
- ブロック [`00ba5ed8`](#insn-00ba5ed8) 範囲 `[['00ba5ed8', '00ba5f07']]`
  - `CONDITIONAL_JUMP` [`00ba5f04`](#insn-00ba5f04) → [`00ba5ed8`](#insn-00ba5ed8)
  - `FALL_THROUGH` [`00ba5f04`](#insn-00ba5f04) → [`00ba5f08`](#insn-00ba5f08)
- ブロック [`00ba5f08`](#insn-00ba5f08) 範囲 `[['00ba5f08', '00ba5f13']]`
  - `CONDITIONAL_JUMP` [`00ba5f10`](#insn-00ba5f10) → [`00ba5ecc`](#insn-00ba5ecc)
  - `FALL_THROUGH` [`00ba5f10`](#insn-00ba5f10) → [`00ba5f14`](#insn-00ba5f14)
- ブロック [`00ba5f14`](#insn-00ba5f14) 範囲 `[['00ba5f14', '00ba5f17']]`
  - `FALL_THROUGH` [`00ba5f14`](#insn-00ba5f14) → [`00ba5f18`](#insn-00ba5f18)
- ブロック [`00ba5f18`](#insn-00ba5f18) 範囲 `[['00ba5f18', '00ba5f2b']]`
- ブロック [`00ba5f2c`](#insn-00ba5f2c) 範囲 `[['00ba5f2c', '00ba5f43']]`
  - `FALL_THROUGH` [`00ba5f40`](#insn-00ba5f40) → [`00ba5f44`](#insn-00ba5f44)
- ブロック [`00ba5f44`](#insn-00ba5f44) 範囲 `[['00ba5f44', '00ba5f4b']]`
  - `FALL_THROUGH` [`00ba5f48`](#insn-00ba5f48) → [`00ba5f4c`](#insn-00ba5f4c)
- ブロック [`00ba5f4c`](#insn-00ba5f4c) 範囲 `[['00ba5f4c', '00ba5f67']]`
  - `CONDITIONAL_JUMP` [`00ba5f64`](#insn-00ba5f64) → [`00ba5f44`](#insn-00ba5f44)
  - `FALL_THROUGH` [`00ba5f64`](#insn-00ba5f64) → [`00ba5f68`](#insn-00ba5f68)
- ブロック [`00ba5f68`](#insn-00ba5f68) 範囲 `[['00ba5f68', '00ba5f6f']]`
  - `CONDITIONAL_JUMP` [`00ba5f6c`](#insn-00ba5f6c) → [`00ba5e38`](#insn-00ba5e38)
  - `FALL_THROUGH` [`00ba5f6c`](#insn-00ba5f6c) → [`00ba5f70`](#insn-00ba5f70)
- ブロック [`00ba5f70`](#insn-00ba5f70) 範囲 `[['00ba5f70', '00ba5f73']]`
  - `UNCONDITIONAL_JUMP` [`00ba5f70`](#insn-00ba5f70) → [`00ba5e50`](#insn-00ba5e50)

## 命令位置別の参照

- [`00ba5dac`](#insn-00ba5dac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5db0`](#insn-00ba5db0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5db4`](#insn-00ba5db4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5dcc`](#insn-00ba5dcc) → [`00ba5e58`](#insn-00ba5e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5dd8`](#insn-00ba5dd8) → [`00ba5e7c`](#insn-00ba5e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5df0`](#insn-00ba5df0) → [`00ba5ea8`](#insn-00ba5ea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5df8`](#insn-00ba5df8) → [`00ba5f18`](#insn-00ba5f18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e0c`](#insn-00ba5e0c) → [`00ba5e30`](#insn-00ba5e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e20`](#insn-00ba5e20) → [`00ba5f2c`](#insn-00ba5f2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e2c`](#insn-00ba5e2c) → [`00ba5f2c`](#insn-00ba5f2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e4c`](#insn-00ba5e4c) → [`00ba5e38`](#insn-00ba5e38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e54`](#insn-00ba5e54) → [`00ba5f18`](#insn-00ba5f18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e64`](#insn-00ba5e64) → [`00ba5e70`](#insn-00ba5e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e6c`](#insn-00ba5e6c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e78`](#insn-00ba5e78) → [`00ba5f18`](#insn-00ba5f18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e88`](#insn-00ba5e88) → [`00ba5e9c`](#insn-00ba5e9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5e98`](#insn-00ba5e98) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`00ba5ea4`](#insn-00ba5ea4) → [`00ba5f18`](#insn-00ba5f18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5ec0`](#insn-00ba5ec0) → [`00ba5eb0`](#insn-00ba5eb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5ec4`](#insn-00ba5ec4) → [`00ba5f14`](#insn-00ba5f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f04`](#insn-00ba5f04) → [`00ba5ed8`](#insn-00ba5ed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f10`](#insn-00ba5f10) → [`00ba5ecc`](#insn-00ba5ecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f1c`](#insn-00ba5f1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f20`](#insn-00ba5f20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f64`](#insn-00ba5f64) → [`00ba5f44`](#insn-00ba5f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f6c`](#insn-00ba5f6c) → [`00ba5e38`](#insn-00ba5e38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5f70`](#insn-00ba5f70) → [`00ba5e50`](#insn-00ba5e50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba5dac`](#insn-00ba5dac)

~~~json
{
  "source": "00ba5dac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5db0`](#insn-00ba5db0)

~~~json
{
  "source": "00ba5db0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5db4`](#insn-00ba5db4)

~~~json
{
  "source": "00ba5db4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5dcc`](#insn-00ba5dcc)

~~~json
{
  "source": "00ba5dcc",
  "target": "00ba5e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5dd8`](#insn-00ba5dd8)

~~~json
{
  "source": "00ba5dd8",
  "target": "00ba5e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5df0`](#insn-00ba5df0)

~~~json
{
  "source": "00ba5df0",
  "target": "00ba5ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5df8`](#insn-00ba5df8)

~~~json
{
  "source": "00ba5df8",
  "target": "00ba5f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e0c`](#insn-00ba5e0c)

~~~json
{
  "source": "00ba5e0c",
  "target": "00ba5e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e20`](#insn-00ba5e20)

~~~json
{
  "source": "00ba5e20",
  "target": "00ba5f2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e2c`](#insn-00ba5e2c)

~~~json
{
  "source": "00ba5e2c",
  "target": "00ba5f2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e4c`](#insn-00ba5e4c)

~~~json
{
  "source": "00ba5e4c",
  "target": "00ba5e38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e54`](#insn-00ba5e54)

~~~json
{
  "source": "00ba5e54",
  "target": "00ba5f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e64`](#insn-00ba5e64)

~~~json
{
  "source": "00ba5e64",
  "target": "00ba5e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e6c`](#insn-00ba5e6c)

~~~json
{
  "source": "00ba5e6c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5e78`](#insn-00ba5e78)

~~~json
{
  "source": "00ba5e78",
  "target": "00ba5f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e88`](#insn-00ba5e88)

~~~json
{
  "source": "00ba5e88",
  "target": "00ba5e9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5e98`](#insn-00ba5e98)

~~~json
{
  "source": "00ba5e98",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5ea4`](#insn-00ba5ea4)

~~~json
{
  "source": "00ba5ea4",
  "target": "00ba5f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5ec0`](#insn-00ba5ec0)

~~~json
{
  "source": "00ba5ec0",
  "target": "00ba5eb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5ec4`](#insn-00ba5ec4)

~~~json
{
  "source": "00ba5ec4",
  "target": "00ba5f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f04`](#insn-00ba5f04)

~~~json
{
  "source": "00ba5f04",
  "target": "00ba5ed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f10`](#insn-00ba5f10)

~~~json
{
  "source": "00ba5f10",
  "target": "00ba5ecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f1c`](#insn-00ba5f1c)

~~~json
{
  "source": "00ba5f1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f20`](#insn-00ba5f20)

~~~json
{
  "source": "00ba5f20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f64`](#insn-00ba5f64)

~~~json
{
  "source": "00ba5f64",
  "target": "00ba5f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f6c`](#insn-00ba5f6c)

~~~json
{
  "source": "00ba5f6c",
  "target": "00ba5e38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5f70`](#insn-00ba5f70)

~~~json
{
  "source": "00ba5f70",
  "target": "00ba5e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
