# 00bf7bac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf6bb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf6/00bf6bb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0011.md#compare-9b740687bc9b80565157d7da99285290)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf7bac",
  "name": "_ZNSt6__ndk110to_wstringEi",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5123c61641a8c2905427bcc8b520cb10550dd43394a7927195727aec9e968877",
  "source_text_sha256": "5123c61641a8c2905427bcc8b520cb10550dd43394a7927195727aec9e968877",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf7bac",
        "00bf7d83"
      ]
    ],
    "bytes_sha256": "2fb26899765c625bed9e7e86f2eece9057b10ee1111939757569915dbb8a5977",
    "instruction_count": 118,
    "instruction_bytes": 472,
    "body_bytes": 472,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00441220](../00441/00441220.md)
- [006d7aa8](../006d7/006d7aa8.md)
- [00bf92e8](../00bf9/00bf92e8.md)
- [00c58f30](../00c58/00c58f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3884 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNSt6__ndk110to_wstringEi(ulong *param_1,uint param_2)

{
  uint uVar1;
  undefined1 auVar2 [16];
  undefined1 auVar3 [16];
  undefined1 auVar4 [16];
  undefined1 auVar5 [16];
  byte *pbVar6;
  byte *pbVar7;
  byte *pbVar8;
  uint *puVar9;
  ulong uVar10;
  undefined1 (*pauVar11) [16];
  ulong uVar12;
  uint *puVar13;
  ulong uVar14;
  undefined1 auVar15 [16];
  undefined1 auVar16 [16];
  undefined1 auVar17 [16];
  undefined1 auVar18 [16];
  undefined1 auVar19 [16];
  undefined1 auVar20 [16];
  byte local_3c [11];
  byte bStack_31;
  
  pbVar6 = local_3c;
  pbVar7 = &bStack_31;
  if ((int)param_2 < 0) {
    pbVar6 = (byte *)((ulong)pbVar6 | 1);
    param_2 = -param_2;
    local_3c[0] = 0x2d;
  }
  if ((9 < (long)pbVar7 - (long)pbVar6) ||
     (uVar1 = (uint)((0x20 - (int)LZCOUNT(param_2 | 1)) * 0x4d1) >> 0xc,
     (long)(ulong)((uVar1 - (param_2 < *(uint *)(&DAT_00310878 + (ulong)uVar1 * 4))) + 1) <=
     (long)pbVar7 - (long)pbVar6)) {
    pbVar7 = (byte *)FUN_00bf92e8();
  }
  uVar14 = (long)pbVar7 - (long)local_3c;
  if (0x3ffffffffffffff7 < uVar14) {
    FUN_006d7aa8(param_1);
LAB_00bf7d80:
                    /* WARNING: Subroutine does not return */
    FUN_00441220();
  }
  if (uVar14 < 5) {
    puVar13 = (uint *)((long)param_1 + 4);
    *(char *)param_1 = (char)((int)uVar14 << 1);
  }
  else {
    uVar12 = (uVar14 & 0x3ffffffffffffffe) + 2;
    if ((uVar14 | 1) != 5) {
      uVar12 = uVar14 | 1;
    }
    if (0x3ffffffffffffffe < uVar12) goto LAB_00bf7d80;
    puVar13 = (uint *)_Znwm((uVar12 + 1) * 4);
    param_1[1] = uVar14;
    param_1[2] = (ulong)puVar13;
    *param_1 = uVar12 + 1 | 1;
  }
  auVar5 = _DAT_002c31e0;
  auVar4 = _DAT_002c2d90;
  auVar3 = _DAT_002c28d0;
  auVar2 = _DAT_002c21b0;
  pbVar6 = local_3c;
  if (pbVar6 != pbVar7) {
    uVar14 = (long)pbVar7 - (long)pbVar6;
    if (0x1f < uVar14) {
      uVar10 = uVar14 & 0xffffffffffffffe0;
      puVar9 = puVar13 + uVar10;
      pbVar6 = local_3c + uVar10;
      pauVar11 = (undefined1 (*) [16])&stack0xffffffffffffffd4;
      puVar13 = puVar13 + 0x10;
      uVar12 = uVar10;
      do {
        auVar15 = pauVar11[-1];
        auVar16 = *pauVar11;
        uVar12 = uVar12 - 0x20;
        pauVar11 = pauVar11 + 2;
        auVar17 = a64_TBL(ZEXT816(0),auVar15,auVar2);
        auVar18 = a64_TBL(ZEXT816(0),auVar15,auVar4);
        auVar19 = a64_TBL(ZEXT816(0),auVar15,auVar5);
        auVar15 = a64_TBL(ZEXT816(0),auVar15,auVar3);
        auVar20 = a64_TBL(ZEXT816(0),auVar16,auVar2);
        *(long *)(puVar13 + -6) = auVar18._8_8_;
        *(long *)(puVar13 + -8) = auVar18._0_8_;
        *(long *)(puVar13 + -2) = auVar17._8_8_;
        *(long *)(puVar13 + -4) = auVar17._0_8_;
        auVar17 = a64_TBL(ZEXT816(0),auVar16,auVar4);
        auVar18 = a64_TBL(ZEXT816(0),auVar16,auVar5);
        auVar16 = a64_TBL(ZEXT816(0),auVar16,auVar3);
        *(long *)(puVar13 + -0xe) = auVar15._8_8_;
        *(long *)(puVar13 + -0x10) = auVar15._0_8_;
        *(long *)(puVar13 + -10) = auVar19._8_8_;
        *(long *)(puVar13 + -0xc) = auVar19._0_8_;
        *(long *)(puVar13 + 10) = auVar17._8_8_;
        *(long *)(puVar13 + 8) = auVar17._0_8_;
        *(long *)(puVar13 + 0xe) = auVar20._8_8_;
        *(long *)(puVar13 + 0xc) = auVar20._0_8_;
        *(long *)(puVar13 + 2) = auVar16._8_8_;
        *(long *)puVar13 = auVar16._0_8_;
        *(long *)(puVar13 + 6) = auVar18._8_8_;
        *(long *)(puVar13 + 4) = auVar18._0_8_;
        puVar13 = puVar13 + 0x20;
      } while (uVar12 != 0);
      puVar13 = puVar9;
      if (uVar14 == uVar10) goto LAB_00bf7d5c;
    }
    do {
      pbVar8 = pbVar6 + 1;
      puVar9 = puVar13 + 1;
      *puVar13 = (uint)*pbVar6;
      pbVar6 = pbVar8;
      puVar13 = puVar9;
    } while (pbVar8 != pbVar7);
  }
LAB_00bf7d5c:
  *puVar13 = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf7bac"></a> `00bf7bac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf7bb0"></a> `00bf7bb0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bf7bb4"></a> `00bf7bb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7bb8"></a> `00bf7bb8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf7bbc"></a> `00bf7bbc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf7bc0"></a> `00bf7bc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bf7bc4"></a> `00bf7bc4` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00bf7bc8"></a> `00bf7bc8` | `e0 13 00 91` | add x0,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7bcc"></a> `00bf7bcc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bf7bd0"></a> `00bf7bd0` | `13 2c 00 91` | add x19,x0,#0xb | `FALL_THROUGH`
<a id="insn-00bf7bd4"></a> `00bf7bd4` | `a1 00 f8 36` | tbz w1,#0x1f,0x00bf7be8 | `CONDITIONAL_JUMP`
<a id="insn-00bf7bd8"></a> `00bf7bd8` | `a8 05 80 52` | mov w8,#0x2d | `FALL_THROUGH`
<a id="insn-00bf7bdc"></a> `00bf7bdc` | `00 00 40 b2` | orr x0,x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7be0"></a> `00bf7be0` | `e1 03 01 4b` | neg w1,w1 | `FALL_THROUGH`
<a id="insn-00bf7be4"></a> `00bf7be4` | `e8 13 00 39` | strb w8,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00bf7be8"></a> `00bf7be8` | `68 02 00 cb` | sub x8,x19,x0 | `FALL_THROUGH`
<a id="insn-00bf7bec"></a> `00bf7bec` | `1f 25 00 f1` | cmp x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bf7bf0"></a> `00bf7bf0` | `2c 02 00 54` | b.gt 0x00bf7c34 | `CONDITIONAL_JUMP`
<a id="insn-00bf7bf4"></a> `00bf7bf4` | `29 00 00 32` | orr w9,w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7bf8"></a> `00bf7bf8` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-00bf7bfc"></a> `00bf7bfc` | `29 11 c0 5a` | clz w9,w9 | `FALL_THROUGH`
<a id="insn-00bf7c00"></a> `00bf7c00` | `49 01 09 4b` | sub w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00bf7c04"></a> `00bf7c04` | `2a 9a 80 52` | mov w10,#0x4d1 | `FALL_THROUGH`
<a id="insn-00bf7c08"></a> `00bf7c08` | `29 7d 0a 1b` | mul w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00bf7c0c"></a> `00bf7c0c` | `ca b8 ff b0` | adrp x10,0x310000 | `FALL_THROUGH`
<a id="insn-00bf7c10"></a> `00bf7c10` | `4a e1 21 91` | add x10,x10,#0x878 | `FALL_THROUGH`
<a id="insn-00bf7c14"></a> `00bf7c14` | `29 7d 0c 53` | lsr w9,w9,#0xc | `FALL_THROUGH`
<a id="insn-00bf7c18"></a> `00bf7c18` | `4a 59 69 b8` | ldr w10,[x10, w9, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-00bf7c1c"></a> `00bf7c1c` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-00bf7c20"></a> `00bf7c20` | `ea 97 9f 1a` | cset w10,hi | `FALL_THROUGH`
<a id="insn-00bf7c24"></a> `00bf7c24` | `29 01 0a 4b` | sub w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00bf7c28"></a> `00bf7c28` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7c2c"></a> `00bf7c2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bf7c30"></a> `00bf7c30` | `6b 00 00 54` | b.lt 0x00bf7c3c | `CONDITIONAL_JUMP`
<a id="insn-00bf7c34"></a> `00bf7c34` | `ad 05 00 94` | bl 0x00bf92e8 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7c38"></a> `00bf7c38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf7c3c"></a> `00bf7c3c` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7c40"></a> `00bf7c40` | `75 02 08 cb` | sub x21,x19,x8 | `FALL_THROUGH`
<a id="insn-00bf7c44"></a> `00bf7c44` | `e8 eb 7d b2` | orr x8,xzr,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00bf7c48"></a> `00bf7c48` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bf7c4c"></a> `00bf7c4c` | `62 09 00 54` | b.cs 0x00bf7d78 | `CONDITIONAL_JUMP`
<a id="insn-00bf7c50"></a> `00bf7c50` | `bf 12 00 f1` | cmp x21,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7c54"></a> `00bf7c54` | `88 00 00 54` | b.hi 0x00bf7c64 | `CONDITIONAL_JUMP`
<a id="insn-00bf7c58"></a> `00bf7c58` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7c5c"></a> `00bf7c5c` | `88 46 00 38` | strb w8,[x20], #0x4 | `FALL_THROUGH`
<a id="insn-00bf7c60"></a> `00bf7c60` | `10 00 00 14` | b 0x00bf7ca0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf7c64"></a> `00bf7c64` | `a8 f2 7f 92` | and x8,x21,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bf7c68"></a> `00bf7c68` | `a9 02 40 b2` | orr x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7c6c"></a> `00bf7c6c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bf7c70"></a> `00bf7c70` | `3f 15 00 f1` | cmp x9,#0x5 | `FALL_THROUGH`
<a id="insn-00bf7c74"></a> `00bf7c74` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00bf7c78"></a> `00bf7c78` | `09 00 f8 92` | mov x9,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bf7c7c"></a> `00bf7c7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bf7c80"></a> `00bf7c80` | `02 08 00 54` | b.cs 0x00bf7d80 | `CONDITIONAL_JUMP`
<a id="insn-00bf7c84"></a> `00bf7c84` | `16 05 00 91` | add x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7c88"></a> `00bf7c88` | `c0 f6 7e d3` | lsl x0,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00bf7c8c"></a> `00bf7c8c` | `a9 84 01 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7c90"></a> `00bf7c90` | `c8 02 40 b2` | orr x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bf7c94"></a> `00bf7c94` | `95 82 00 a9` | stp x21,x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bf7c98"></a> `00bf7c98` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bf7c9c"></a> `00bf7c9c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bf7ca0"></a> `00bf7ca0` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7ca4"></a> `00bf7ca4` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bf7ca8"></a> `00bf7ca8` | `c0 00 00 54` | b.eq 0x00bf7cc0 | `CONDITIONAL_JUMP`
<a id="insn-00bf7cac"></a> `00bf7cac` | `6a 02 08 cb` | sub x10,x19,x8 | `FALL_THROUGH`
<a id="insn-00bf7cb0"></a> `00bf7cb0` | `5f 81 00 f1` | cmp x10,#0x20 | `FALL_THROUGH`
<a id="insn-00bf7cb4"></a> `00bf7cb4` | `a2 00 00 54` | b.cs 0x00bf7cc8 | `CONDITIONAL_JUMP`
<a id="insn-00bf7cb8"></a> `00bf7cb8` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-00bf7cbc"></a> `00bf7cbc` | `24 00 00 14` | b 0x00bf7d4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf7cc0"></a> `00bf7cc0` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-00bf7cc4"></a> `00bf7cc4` | `26 00 00 14` | b 0x00bf7d5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf7cc8"></a> `00bf7cc8` | `49 b6 ff f0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00bf7ccc"></a> `00bf7ccc` | `6c b6 ff 90` | adrp x12,0x2c3000 | `FALL_THROUGH`
<a id="insn-00bf7cd0"></a> `00bf7cd0` | `4b e9 7b 92` | and x11,x10,#-0x20 | `FALL_THROUGH`
<a id="insn-00bf7cd4"></a> `00bf7cd4` | `20 35 c2 3d` | ldr q0,[x9, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bf7cd8"></a> `00bf7cd8` | `81 79 c0 3d` | ldr q1,[x12, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bf7cdc"></a> `00bf7cdc` | `49 b6 ff f0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00bf7ce0"></a> `00bf7ce0` | `4c b6 ff f0` | adrp x12,0x2c2000 | `FALL_THROUGH`
<a id="insn-00bf7ce4"></a> `00bf7ce4` | `ed 13 00 91` | add x13,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00bf7ce8"></a> `00bf7ce8` | `22 65 c3 3d` | ldr q2,[x9, #0xd90] | `FALL_THROUGH`
<a id="insn-00bf7cec"></a> `00bf7cec` | `89 0a 0b 8b` | add x9,x20,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bf7cf0"></a> `00bf7cf0` | `83 6d c0 3d` | ldr q3,[x12, #0x1b0] | `FALL_THROUGH`
<a id="insn-00bf7cf4"></a> `00bf7cf4` | `a8 01 0b 8b` | add x8,x13,x11 | `FALL_THROUGH`
<a id="insn-00bf7cf8"></a> `00bf7cf8` | `8c 02 01 91` | add x12,x20,#0x40 | `FALL_THROUGH`
<a id="insn-00bf7cfc"></a> `00bf7cfc` | `ad 41 00 91` | add x13,x13,#0x10 | `FALL_THROUGH`
<a id="insn-00bf7d00"></a> `00bf7d00` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bf7d04"></a> `00bf7d04` | `a4 95 7f ad` | ldp q4,q5,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf7d08"></a> `00bf7d08` | `ce 81 00 f1` | subs x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bf7d0c"></a> `00bf7d0c` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00bf7d10"></a> `00bf7d10` | `86 00 03 4e` | tbl v6.16B,{v4.16B},v3.16B | `FALL_THROUGH`
<a id="insn-00bf7d14"></a> `00bf7d14` | `87 00 02 4e` | tbl v7.16B,{v4.16B},v2.16B | `FALL_THROUGH`
<a id="insn-00bf7d18"></a> `00bf7d18` | `90 00 01 4e` | tbl v16.16B,{v4.16B},v1.16B | `FALL_THROUGH`
<a id="insn-00bf7d1c"></a> `00bf7d1c` | `84 00 00 4e` | tbl v4.16B,{v4.16B},v0.16B | `FALL_THROUGH`
<a id="insn-00bf7d20"></a> `00bf7d20` | `b1 00 03 4e` | tbl v17.16B,{v5.16B},v3.16B | `FALL_THROUGH`
<a id="insn-00bf7d24"></a> `00bf7d24` | `87 19 3f ad` | stp q7,q6,[x12, #-0x20] | `FALL_THROUGH`
<a id="insn-00bf7d28"></a> `00bf7d28` | `a6 00 02 4e` | tbl v6.16B,{v5.16B},v2.16B | `FALL_THROUGH`
<a id="insn-00bf7d2c"></a> `00bf7d2c` | `a7 00 01 4e` | tbl v7.16B,{v5.16B},v1.16B | `FALL_THROUGH`
<a id="insn-00bf7d30"></a> `00bf7d30` | `a5 00 00 4e` | tbl v5.16B,{v5.16B},v0.16B | `FALL_THROUGH`
<a id="insn-00bf7d34"></a> `00bf7d34` | `84 41 3e ad` | stp q4,q16,[x12, #-0x40] | `FALL_THROUGH`
<a id="insn-00bf7d38"></a> `00bf7d38` | `86 45 01 ad` | stp q6,q17,[x12, #0x20] | `FALL_THROUGH`
<a id="insn-00bf7d3c"></a> `00bf7d3c` | `85 1d 84 ac` | stp q5,q7,[x12], #0x80 | `FALL_THROUGH`
<a id="insn-00bf7d40"></a> `00bf7d40` | `21 fe ff 54` | b.ne 0x00bf7d04 | `CONDITIONAL_JUMP`
<a id="insn-00bf7d44"></a> `00bf7d44` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bf7d48"></a> `00bf7d48` | `a0 00 00 54` | b.eq 0x00bf7d5c | `CONDITIONAL_JUMP`
<a id="insn-00bf7d4c"></a> `00bf7d4c` | `0a 15 40 38` | ldrb w10,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bf7d50"></a> `00bf7d50` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bf7d54"></a> `00bf7d54` | `2a 45 00 b8` | str w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00bf7d58"></a> `00bf7d58` | `a1 ff ff 54` | b.ne 0x00bf7d4c | `CONDITIONAL_JUMP`
<a id="insn-00bf7d5c"></a> `00bf7d5c` | `3f 01 00 b9` | str wzr,[x9] | `FALL_THROUGH`
<a id="insn-00bf7d60"></a> `00bf7d60` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf7d64"></a> `00bf7d64` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf7d68"></a> `00bf7d68` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf7d6c"></a> `00bf7d6c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bf7d70"></a> `00bf7d70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf7d74"></a> `00bf7d74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf7d78"></a> `00bf7d78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf7d7c"></a> `00bf7d7c` | `4b 7f eb 97` | bl 0x006d7aa8 | `UNCONDITIONAL_CALL`
<a id="insn-00bf7d80"></a> `00bf7d80` | `28 25 e1 97` | bl 0x00441220 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf7bac`](#insn-00bf7bac) 範囲 `[['00bf7bac', '00bf7bd7']]`
  - `CONDITIONAL_JUMP` [`00bf7bd4`](#insn-00bf7bd4) → [`00bf7be8`](#insn-00bf7be8)
  - `FALL_THROUGH` [`00bf7bd4`](#insn-00bf7bd4) → [`00bf7bd8`](#insn-00bf7bd8)
- ブロック [`00bf7bd8`](#insn-00bf7bd8) 範囲 `[['00bf7bd8', '00bf7be7']]`
  - `FALL_THROUGH` [`00bf7be4`](#insn-00bf7be4) → [`00bf7be8`](#insn-00bf7be8)
- ブロック [`00bf7be8`](#insn-00bf7be8) 範囲 `[['00bf7be8', '00bf7bf3']]`
  - `CONDITIONAL_JUMP` [`00bf7bf0`](#insn-00bf7bf0) → [`00bf7c34`](#insn-00bf7c34)
  - `FALL_THROUGH` [`00bf7bf0`](#insn-00bf7bf0) → [`00bf7bf4`](#insn-00bf7bf4)
- ブロック [`00bf7bf4`](#insn-00bf7bf4) 範囲 `[['00bf7bf4', '00bf7c33']]`
  - `CONDITIONAL_JUMP` [`00bf7c30`](#insn-00bf7c30) → [`00bf7c3c`](#insn-00bf7c3c)
  - `FALL_THROUGH` [`00bf7c30`](#insn-00bf7c30) → [`00bf7c34`](#insn-00bf7c34)
- ブロック [`00bf7c34`](#insn-00bf7c34) 範囲 `[['00bf7c34', '00bf7c3b']]`
  - `FALL_THROUGH` [`00bf7c38`](#insn-00bf7c38) → [`00bf7c3c`](#insn-00bf7c3c)
- ブロック [`00bf7c3c`](#insn-00bf7c3c) 範囲 `[['00bf7c3c', '00bf7c4f']]`
  - `CONDITIONAL_JUMP` [`00bf7c4c`](#insn-00bf7c4c) → [`00bf7d78`](#insn-00bf7d78)
  - `FALL_THROUGH` [`00bf7c4c`](#insn-00bf7c4c) → [`00bf7c50`](#insn-00bf7c50)
- ブロック [`00bf7c50`](#insn-00bf7c50) 範囲 `[['00bf7c50', '00bf7c57']]`
  - `CONDITIONAL_JUMP` [`00bf7c54`](#insn-00bf7c54) → [`00bf7c64`](#insn-00bf7c64)
  - `FALL_THROUGH` [`00bf7c54`](#insn-00bf7c54) → [`00bf7c58`](#insn-00bf7c58)
- ブロック [`00bf7c58`](#insn-00bf7c58) 範囲 `[['00bf7c58', '00bf7c63']]`
  - `UNCONDITIONAL_JUMP` [`00bf7c60`](#insn-00bf7c60) → [`00bf7ca0`](#insn-00bf7ca0)
- ブロック [`00bf7c64`](#insn-00bf7c64) 範囲 `[['00bf7c64', '00bf7c83']]`
  - `CONDITIONAL_JUMP` [`00bf7c80`](#insn-00bf7c80) → [`00bf7d80`](#insn-00bf7d80)
  - `FALL_THROUGH` [`00bf7c80`](#insn-00bf7c80) → [`00bf7c84`](#insn-00bf7c84)
- ブロック [`00bf7c84`](#insn-00bf7c84) 範囲 `[['00bf7c84', '00bf7c9f']]`
  - `FALL_THROUGH` [`00bf7c9c`](#insn-00bf7c9c) → [`00bf7ca0`](#insn-00bf7ca0)
- ブロック [`00bf7ca0`](#insn-00bf7ca0) 範囲 `[['00bf7ca0', '00bf7cab']]`
  - `CONDITIONAL_JUMP` [`00bf7ca8`](#insn-00bf7ca8) → [`00bf7cc0`](#insn-00bf7cc0)
  - `FALL_THROUGH` [`00bf7ca8`](#insn-00bf7ca8) → [`00bf7cac`](#insn-00bf7cac)
- ブロック [`00bf7cac`](#insn-00bf7cac) 範囲 `[['00bf7cac', '00bf7cb7']]`
  - `CONDITIONAL_JUMP` [`00bf7cb4`](#insn-00bf7cb4) → [`00bf7cc8`](#insn-00bf7cc8)
  - `FALL_THROUGH` [`00bf7cb4`](#insn-00bf7cb4) → [`00bf7cb8`](#insn-00bf7cb8)
- ブロック [`00bf7cb8`](#insn-00bf7cb8) 範囲 `[['00bf7cb8', '00bf7cbf']]`
  - `UNCONDITIONAL_JUMP` [`00bf7cbc`](#insn-00bf7cbc) → [`00bf7d4c`](#insn-00bf7d4c)
- ブロック [`00bf7cc0`](#insn-00bf7cc0) 範囲 `[['00bf7cc0', '00bf7cc7']]`
  - `UNCONDITIONAL_JUMP` [`00bf7cc4`](#insn-00bf7cc4) → [`00bf7d5c`](#insn-00bf7d5c)
- ブロック [`00bf7cc8`](#insn-00bf7cc8) 範囲 `[['00bf7cc8', '00bf7d03']]`
  - `FALL_THROUGH` [`00bf7d00`](#insn-00bf7d00) → [`00bf7d04`](#insn-00bf7d04)
- ブロック [`00bf7d04`](#insn-00bf7d04) 範囲 `[['00bf7d04', '00bf7d43']]`
  - `CONDITIONAL_JUMP` [`00bf7d40`](#insn-00bf7d40) → [`00bf7d04`](#insn-00bf7d04)
  - `FALL_THROUGH` [`00bf7d40`](#insn-00bf7d40) → [`00bf7d44`](#insn-00bf7d44)
- ブロック [`00bf7d44`](#insn-00bf7d44) 範囲 `[['00bf7d44', '00bf7d4b']]`
  - `CONDITIONAL_JUMP` [`00bf7d48`](#insn-00bf7d48) → [`00bf7d5c`](#insn-00bf7d5c)
  - `FALL_THROUGH` [`00bf7d48`](#insn-00bf7d48) → [`00bf7d4c`](#insn-00bf7d4c)
- ブロック [`00bf7d4c`](#insn-00bf7d4c) 範囲 `[['00bf7d4c', '00bf7d5b']]`
  - `CONDITIONAL_JUMP` [`00bf7d58`](#insn-00bf7d58) → [`00bf7d4c`](#insn-00bf7d4c)
  - `FALL_THROUGH` [`00bf7d58`](#insn-00bf7d58) → [`00bf7d5c`](#insn-00bf7d5c)
- ブロック [`00bf7d5c`](#insn-00bf7d5c) 範囲 `[['00bf7d5c', '00bf7d77']]`
- ブロック [`00bf7d78`](#insn-00bf7d78) 範囲 `[['00bf7d78', '00bf7d7f']]`
  - `FALL_THROUGH` [`00bf7d7c`](#insn-00bf7d7c) → [`00bf7d80`](#insn-00bf7d80)
- ブロック [`00bf7d80`](#insn-00bf7d80) 範囲 `[['00bf7d80', '00bf7d83']]`

## 命令位置別の参照

- [`00bf7bb4`](#insn-00bf7bb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7bb8`](#insn-00bf7bb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7bbc`](#insn-00bf7bbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7bd4`](#insn-00bf7bd4) → [`00bf7be8`](#insn-00bf7be8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7be4`](#insn-00bf7be4) → `Stack[-0x3c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7bf0`](#insn-00bf7bf0) → [`00bf7c34`](#insn-00bf7c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c18`](#insn-00bf7c18) → `00310878`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c30`](#insn-00bf7c30) → [`00bf7c3c`](#insn-00bf7c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c34`](#insn-00bf7c34) → [`00bf92e8`](../00bf9/00bf92e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf92e8` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c4c`](#insn-00bf7c4c) → [`00bf7d78`](#insn-00bf7d78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c54`](#insn-00bf7c54) → [`00bf7c64`](#insn-00bf7c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c60`](#insn-00bf7c60) → [`00bf7ca0`](#insn-00bf7ca0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c80`](#insn-00bf7c80) → [`00bf7d80`](#insn-00bf7d80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7c8c`](#insn-00bf7c8c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bf7ca8`](#insn-00bf7ca8) → [`00bf7cc0`](#insn-00bf7cc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cb4`](#insn-00bf7cb4) → [`00bf7cc8`](#insn-00bf7cc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cbc`](#insn-00bf7cbc) → [`00bf7d4c`](#insn-00bf7d4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cc4`](#insn-00bf7cc4) → [`00bf7d5c`](#insn-00bf7d5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cd4`](#insn-00bf7cd4) → `002c28d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cd8`](#insn-00bf7cd8) → `002c31e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7ce8`](#insn-00bf7ce8) → `002c2d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7cf0`](#insn-00bf7cf0) → `002c21b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d04`](#insn-00bf7d04) → `Stack[-0x3c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d40`](#insn-00bf7d40) → [`00bf7d04`](#insn-00bf7d04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d48`](#insn-00bf7d48) → [`00bf7d5c`](#insn-00bf7d5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d58`](#insn-00bf7d58) → [`00bf7d4c`](#insn-00bf7d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d60`](#insn-00bf7d60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d64`](#insn-00bf7d64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d68`](#insn-00bf7d68) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d7c`](#insn-00bf7d7c) → [`006d7aa8`](../006d7/006d7aa8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d7aa8` · 推定シンボル `None` · 推定型 `None`
- [`00bf7d80`](#insn-00bf7d80) → [`00441220`](../00441/00441220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00441220` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf7bb4`](#insn-00bf7bb4)

~~~json
{
  "source": "00bf7bb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7bb8`](#insn-00bf7bb8)

~~~json
{
  "source": "00bf7bb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7bbc`](#insn-00bf7bbc)

~~~json
{
  "source": "00bf7bbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7bd4`](#insn-00bf7bd4)

~~~json
{
  "source": "00bf7bd4",
  "target": "00bf7be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7be4`](#insn-00bf7be4)

~~~json
{
  "source": "00bf7be4",
  "target": "Stack[-0x3c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7bf0`](#insn-00bf7bf0)

~~~json
{
  "source": "00bf7bf0",
  "target": "00bf7c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c18`](#insn-00bf7c18)

~~~json
{
  "source": "00bf7c18",
  "target": "00310878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c30`](#insn-00bf7c30)

~~~json
{
  "source": "00bf7c30",
  "target": "00bf7c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c34`](#insn-00bf7c34)

~~~json
{
  "source": "00bf7c34",
  "target": "00bf92e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7c4c`](#insn-00bf7c4c)

~~~json
{
  "source": "00bf7c4c",
  "target": "00bf7d78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c54`](#insn-00bf7c54)

~~~json
{
  "source": "00bf7c54",
  "target": "00bf7c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c60`](#insn-00bf7c60)

~~~json
{
  "source": "00bf7c60",
  "target": "00bf7ca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c80`](#insn-00bf7c80)

~~~json
{
  "source": "00bf7c80",
  "target": "00bf7d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7c8c`](#insn-00bf7c8c)

~~~json
{
  "source": "00bf7c8c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7ca8`](#insn-00bf7ca8)

~~~json
{
  "source": "00bf7ca8",
  "target": "00bf7cc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cb4`](#insn-00bf7cb4)

~~~json
{
  "source": "00bf7cb4",
  "target": "00bf7cc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cbc`](#insn-00bf7cbc)

~~~json
{
  "source": "00bf7cbc",
  "target": "00bf7d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cc4`](#insn-00bf7cc4)

~~~json
{
  "source": "00bf7cc4",
  "target": "00bf7d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cd4`](#insn-00bf7cd4)

~~~json
{
  "source": "00bf7cd4",
  "target": "002c28d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cd8`](#insn-00bf7cd8)

~~~json
{
  "source": "00bf7cd8",
  "target": "002c31e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7ce8`](#insn-00bf7ce8)

~~~json
{
  "source": "00bf7ce8",
  "target": "002c2d90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7cf0`](#insn-00bf7cf0)

~~~json
{
  "source": "00bf7cf0",
  "target": "002c21b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d04`](#insn-00bf7d04)

~~~json
{
  "source": "00bf7d04",
  "target": "Stack[-0x3c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d40`](#insn-00bf7d40)

~~~json
{
  "source": "00bf7d40",
  "target": "00bf7d04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d48`](#insn-00bf7d48)

~~~json
{
  "source": "00bf7d48",
  "target": "00bf7d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d58`](#insn-00bf7d58)

~~~json
{
  "source": "00bf7d58",
  "target": "00bf7d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d60`](#insn-00bf7d60)

~~~json
{
  "source": "00bf7d60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d64`](#insn-00bf7d64)

~~~json
{
  "source": "00bf7d64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d68`](#insn-00bf7d68)

~~~json
{
  "source": "00bf7d68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf7d7c`](#insn-00bf7d7c)

~~~json
{
  "source": "00bf7d7c",
  "target": "006d7aa8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf7d80`](#insn-00bf7d80)

~~~json
{
  "source": "00bf7d80",
  "target": "00441220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
