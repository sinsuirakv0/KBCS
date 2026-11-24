# 00bbfcac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbecb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0014.md#compare-955fbef8b7d91e1e95b79c9b3b3b8a34)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfcac",
  "name": "_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "529b51bf3ac21a15738c6b006117b628cc8fa2ab478770ca310ea79577b8629d",
  "source_text_sha256": "529b51bf3ac21a15738c6b006117b628cc8fa2ab478770ca310ea79577b8629d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfcac",
        "00bbfebb"
      ]
    ],
    "bytes_sha256": "50a9ca339f0b4e9b9f14e561e0a53ea3e18df33e9af09d9b4c81a62b268e28ed",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e570](../00c5e/00c5e570.md)

## 呼び出し先

- [00c5e580](../00c5e/00c5e580.md)
- [00c5e5a0](../00c5e/00c5e5a0.md)
- [00c5e5b0](../00c5e/00c5e5b0.md)
- [00c5e5c0](../00c5e/00c5e5c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4399 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ushort *puVar11;
  
  lVar6 = *param_2;
  uVar8 = (long)param_1 - lVar6;
                    /* try { // try from 00bbfcd0 to 00cbfceb has its CatchHandler @ 00bc0414 */
  if (((uVar8 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar7 = param_2[1];
    if (uVar7 < 5) {
      return 0;
    }
    uVar9 = uVar7 - 4;
                    /* try { // try from 00bbfcec to 00cbfd97 has its CatchHandler @ 00bbf85c */
    if (uVar9 < uVar8) {
      return 0;
    }
    iVar5 = *param_1;
    uVar1 = (int)param_2[7] + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar10 = uVar8 - (long)iVar5, (uVar10 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar10 <= uVar7 - 2)) {
      uVar4 = *(ushort *)(lVar6 + uVar10);
      if ((((uVar4 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar4 & 1) == 0)) {
        if (uVar7 <= uVar4) {
          return 0;
        }
        if (uVar7 - uVar4 < uVar10) {
          return 0;
        }
        puVar11 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar11) {
          if (((ulong)puVar11[2] != 0) && (uVar7 - 1 < uVar8 + puVar11[2])) {
            return 0;
          }
          if (*puVar11 < 7) {
            lVar6 = 0;
            uVar4 = puVar11[2];
          }
          else {
            if ((ulong)puVar11[3] != 0) {
              uVar8 = uVar8 + puVar11[3];
                    /* try { // try from 00bbfdb4 to 00cc0157 has its CatchHandler @ 00bbf85c */
              if ((uVar8 & 3) == 0) {
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar6 + uVar8) < 1) {
                return 0;
              }
              if (uVar7 - 1 < uVar8 + *(uint *)(lVar6 + uVar8)) {
                return 0;
              }
            }
            lVar6 = 0;
            if ((ulong)puVar11[3] != 0) {
              puVar3 = (uint *)((long)param_1 + (ulong)puVar11[3]);
              lVar6 = (long)puVar3 + (ulong)*puVar3;
            }
            uVar4 = puVar11[2];
          }
          if ((ulong)uVar4 != 0) {
            switch(*(undefined1 *)((long)param_1 + (ulong)uVar4)) {
            case 1:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 2:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 3:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp30SerializedRegistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 4:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            default:
              goto switchD_00bbfe48_default;
            }
            if ((uVar8 & 1) == 0) {
              return 0;
            }
          }
        }
switchD_00bbfe48_default:
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
                    /* try { // try from 00bbfd98 to 00cbfdb3 has its CatchHandler @ 00bc041c */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfcac"></a> `00bbfcac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbfcb0"></a> `00bbfcb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfcb4"></a> `00bbfcb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbfcb8"></a> `00bbfcb8` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bbfcbc"></a> `00bbfcbc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbfcc0"></a> `00bbfcc0` | `0b 00 09 cb` | sub x11,x0,x9 | `FALL_THROUGH`
<a id="insn-00bbfcc4"></a> `00bbfcc4` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfcc8"></a> `00bbfcc8` | `60 00 00 54` | b.eq 0x00bbfcd4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfccc"></a> `00bbfccc` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfcd0"></a> `00bbfcd0` | `e8 05 00 35` | cbnz w8,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfcd4"></a> `00bbfcd4` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfcd8"></a> `00bbfcd8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfcdc"></a> `00bbfcdc` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfce0"></a> `00bbfce0` | `83 05 00 54` | b.cc 0x00bbfd90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfce4"></a> `00bbfce4` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfce8"></a> `00bbfce8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfcec"></a> `00bbfcec` | `23 05 00 54` | b.cc 0x00bbfd90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcf0"></a> `00bbfcf0` | `6d 3a 47 29` | ldp w13,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfcf4"></a> `00bbfcf4` | `6f 12 40 b9` | ldr w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfcf8"></a> `00bbfcf8` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbfcfc"></a> `00bbfcfc` | `b0 05 00 11` | add w16,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd00"></a> `00bbfd00` | `cd 05 00 11` | add w13,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd04"></a> `00bbfd04` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbfd08"></a> `00bbfd08` | `70 36 07 29` | stp w16,w13,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfd0c"></a> `00bbfd0c` | `08 04 00 54` | b.hi 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd10"></a> `00bbfd10` | `6e 16 40 b9` | ldr w14,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00bbfd14"></a> `00bbfd14` | `bf 01 0e 6b` | cmp w13,w14 | `FALL_THROUGH`
<a id="insn-00bbfd18"></a> `00bbfd18` | `a8 03 00 54` | b.hi 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd1c"></a> `00bbfd1c` | `6d 01 08 cb` | sub x13,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbfd20"></a> `00bbfd20` | `6d 00 00 36` | tbz w13,#0x0,0x00bbfd2c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd24"></a> `00bbfd24` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfd28"></a> `00bbfd28` | `28 03 00 35` | cbnz w8,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd2c"></a> `00bbfd2c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfd30"></a> `00bbfd30` | `1f 01 0d eb` | cmp x8,x13 | `FALL_THROUGH`
<a id="insn-00bbfd34"></a> `00bbfd34` | `c3 02 00 54` | b.cc 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd38"></a> `00bbfd38` | `28 69 6d 78` | ldrh w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfd3c"></a> `00bbfd3c` | `68 00 00 36` | tbz w8,#0x0,0x00bbfd48 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd40"></a> `00bbfd40` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfd44"></a> `00bbfd44` | `4e 02 00 35` | cbnz w14,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd48"></a> `00bbfd48` | `28 02 00 37` | tbnz w8,#0x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd4c"></a> `00bbfd4c` | `4e 01 08 eb` | subs x14,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbfd50"></a> `00bbfd50` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfd54"></a> `00bbfd54` | `e9 01 00 54` | b.ls 0x00bbfd90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd58"></a> `00bbfd58` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00bbfd5c"></a> `00bbfd5c` | `a3 01 00 54` | b.cc 0x00bbfd90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd60"></a> `00bbfd60` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbfd64"></a> `00bbfd64` | `0d 00 08 cb` | sub x13,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfd68"></a> `00bbfd68` | `a8 01 40 79` | ldrh w8,[x13] | `FALL_THROUGH`
<a id="insn-00bbfd6c"></a> `00bbfd6c` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfd70"></a> `00bbfd70` | `c3 09 00 54` | b.cc 0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd74"></a> `00bbfd74` | `ae 09 40 79` | ldrh w14,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfd78"></a> `00bbfd78` | `4e 01 00 b4` | cbz x14,0x00bbfda0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd7c"></a> `00bbfd7c` | `6e 01 0e 8b` | add x14,x11,x14 | `FALL_THROUGH`
<a id="insn-00bbfd80"></a> `00bbfd80` | `4f 05 00 d1` | sub x15,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd84"></a> `00bbfd84` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbfd88"></a> `00bbfd88` | `c2 00 00 54` | b.cs 0x00bbfda0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd8c"></a> `00bbfd8c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfd90"></a> `00bbfd90` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfd94"></a> `00bbfd94` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bbfd98"></a> `00bbfd98` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbfd9c"></a> `00bbfd9c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfda0"></a> `00bbfda0` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-00bbfda4"></a> `00bbfda4` | `83 01 00 54` | b.cc 0x00bbfdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfda8"></a> `00bbfda8` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbfdac"></a> `00bbfdac` | `e8 02 00 b4` | cbz x8,0x00bbfe08 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdb0"></a> `00bbfdb0` | `6b 01 08 8b` | add x11,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbfdb4"></a> `00bbfdb4` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfdb8"></a> `00bbfdb8` | `60 01 00 54` | b.eq 0x00bbfde4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdbc"></a> `00bbfdbc` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfdc0"></a> `00bbfdc0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfdc4"></a> `00bbfdc4` | `6e fe ff 35` | cbnz w14,0x00bbfd90 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdc8"></a> `00bbfdc8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfdcc"></a> `00bbfdcc` | `02 01 00 54` | b.cs 0x00bbfdec | `CONDITIONAL_JUMP`
<a id="insn-00bbfdd0"></a> `00bbfdd0` | `f0 ff ff 17` | b 0x00bbfd90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfdd4"></a> `00bbfdd4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfdd8"></a> `00bbfdd8` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfddc"></a> `00bbfddc` | `49 02 00 b5` | cbnz x9,0x00bbfe24 | `CONDITIONAL_JUMP`
<a id="insn-00bbfde0"></a> `00bbfde0` | `32 00 00 14` | b 0x00bbfea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfde4"></a> `00bbfde4` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbfde8"></a> `00bbfde8` | `23 fd ff 54` | b.cc 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfdec"></a> `00bbfdec` | `28 69 6b b8` | ldr w8,[x9, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfdf0"></a> `00bbfdf0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfdf4"></a> `00bbfdf4` | `cb fc ff 54` | b.lt 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfdf8"></a> `00bbfdf8` | `68 01 08 8b` | add x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbfdfc"></a> `00bbfdfc` | `49 05 00 d1` | sub x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfe00"></a> `00bbfe00` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfe04"></a> `00bbfe04` | `43 fc ff 54` | b.cc 0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe08"></a> `00bbfe08` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbfe0c"></a> `00bbfe0c` | `88 00 00 b4` | cbz x8,0x00bbfe1c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe10"></a> `00bbfe10` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe14"></a> `00bbfe14` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfe18"></a> `00bbfe18` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfe1c"></a> `00bbfe1c` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfe20"></a> `00bbfe20` | `49 04 00 b4` | cbz x9,0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe24"></a> `00bbfe24` | `09 68 69 38` | ldrb w9,[x0, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfe28"></a> `00bbfe28` | `29 05 00 51` | sub w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfe2c"></a> `00bbfe2c` | `3f 0d 00 71` | cmp w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfe30"></a> `00bbfe30` | `c8 03 00 54` | b.hi 0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe34"></a> `00bbfe34` | `6a ba ff f0` | adrp x10,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbfe38"></a> `00bbfe38` | `4a 91 24 91` | add x10,x10,#0x924 | `FALL_THROUGH`
<a id="insn-00bbfe3c"></a> `00bbfe3c` | `8b 00 00 10` | adr x11,0xbbfe4c | `FALL_THROUGH`
<a id="insn-00bbfe40"></a> `00bbfe40` | `4c 69 69 38` | ldrb w12,[x10, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfe44"></a> `00bbfe44` | `6b 09 0c 8b` | add x11,x11,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbfe48"></a> `00bbfe48` | `60 01 1f d6` | br x11 | `COMPUTED_JUMP`
<a id="insn-00bbfe4c"></a> `00bbfe4c` | `e8 02 00 b4` | cbz x8,0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe50"></a> `00bbfe50` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe54"></a> `00bbfe54` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbfe58"></a> `00bbfe58` | `ca 79 02 94` | bl 0x00c5e580 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe5c"></a> `00bbfe5c` | `80 f9 07 36` | tbz w0,#0x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe60"></a> `00bbfe60` | `12 00 00 14` | b 0x00bbfea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfe64"></a> `00bbfe64` | `28 02 00 b4` | cbz x8,0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe68"></a> `00bbfe68` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe6c"></a> `00bbfe6c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbfe70"></a> `00bbfe70` | `cc 79 02 94` | bl 0x00c5e5a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe74"></a> `00bbfe74` | `c0 f8 07 36` | tbz w0,#0x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe78"></a> `00bbfe78` | `0c 00 00 14` | b 0x00bbfea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfe7c"></a> `00bbfe7c` | `68 01 00 b4` | cbz x8,0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe80"></a> `00bbfe80` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe84"></a> `00bbfe84` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbfe88"></a> `00bbfe88` | `ca 79 02 94` | bl 0x00c5e5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfe8c"></a> `00bbfe8c` | `00 f8 07 36` | tbz w0,#0x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe90"></a> `00bbfe90` | `06 00 00 14` | b 0x00bbfea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfe94"></a> `00bbfe94` | `a8 00 00 b4` | cbz x8,0x00bbfea8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe98"></a> `00bbfe98` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfe9c"></a> `00bbfe9c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbfea0"></a> `00bbfea0` | `c8 79 02 94` | bl 0x00c5e5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfea4"></a> `00bbfea4` | `40 f7 07 36` | tbz w0,#0x0,0x00bbfd8c | `CONDITIONAL_JUMP`
<a id="insn-00bbfea8"></a> `00bbfea8` | `68 3a 40 b9` | ldr w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfeac"></a> `00bbfeac` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfeb0"></a> `00bbfeb0` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfeb4"></a> `00bbfeb4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfeb8"></a> `00bbfeb8` | `b6 ff ff 17` | b 0x00bbfd90 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbfcac`](#insn-00bbfcac) 範囲 `[['00bbfcac', '00bbfccb']]`
  - `CONDITIONAL_JUMP` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfcd4`](#insn-00bbfcd4)
  - `FALL_THROUGH` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfccc`](#insn-00bbfccc)
- ブロック [`00bbfccc`](#insn-00bbfccc) 範囲 `[['00bbfccc', '00bbfccf']]`
  - `FALL_THROUGH` [`00bbfccc`](#insn-00bbfccc) → [`00bbfcd0`](#insn-00bbfcd0)
- ブロック [`00bbfcd0`](#insn-00bbfcd0) 範囲 `[['00bbfcd0', '00bbfcd3']]`
  - `CONDITIONAL_JUMP` [`00bbfcd0`](#insn-00bbfcd0) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfcd0`](#insn-00bbfcd0) → [`00bbfcd4`](#insn-00bbfcd4)
- ブロック [`00bbfcd4`](#insn-00bbfcd4) 範囲 `[['00bbfcd4', '00bbfce3']]`
  - `CONDITIONAL_JUMP` [`00bbfce0`](#insn-00bbfce0) → [`00bbfd90`](#insn-00bbfd90)
  - `FALL_THROUGH` [`00bbfce0`](#insn-00bbfce0) → [`00bbfce4`](#insn-00bbfce4)
- ブロック [`00bbfce4`](#insn-00bbfce4) 範囲 `[['00bbfce4', '00bbfceb']]`
  - `FALL_THROUGH` [`00bbfce8`](#insn-00bbfce8) → [`00bbfcec`](#insn-00bbfcec)
- ブロック [`00bbfcec`](#insn-00bbfcec) 範囲 `[['00bbfcec', '00bbfcef']]`
  - `CONDITIONAL_JUMP` [`00bbfcec`](#insn-00bbfcec) → [`00bbfd90`](#insn-00bbfd90)
  - `FALL_THROUGH` [`00bbfcec`](#insn-00bbfcec) → [`00bbfcf0`](#insn-00bbfcf0)
- ブロック [`00bbfcf0`](#insn-00bbfcf0) 範囲 `[['00bbfcf0', '00bbfd0f']]`
  - `CONDITIONAL_JUMP` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd10`](#insn-00bbfd10)
- ブロック [`00bbfd10`](#insn-00bbfd10) 範囲 `[['00bbfd10', '00bbfd1b']]`
  - `CONDITIONAL_JUMP` [`00bbfd18`](#insn-00bbfd18) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd18`](#insn-00bbfd18) → [`00bbfd1c`](#insn-00bbfd1c)
- ブロック [`00bbfd1c`](#insn-00bbfd1c) 範囲 `[['00bbfd1c', '00bbfd23']]`
  - `CONDITIONAL_JUMP` [`00bbfd20`](#insn-00bbfd20) → [`00bbfd2c`](#insn-00bbfd2c)
  - `FALL_THROUGH` [`00bbfd20`](#insn-00bbfd20) → [`00bbfd24`](#insn-00bbfd24)
- ブロック [`00bbfd24`](#insn-00bbfd24) 範囲 `[['00bbfd24', '00bbfd2b']]`
  - `CONDITIONAL_JUMP` [`00bbfd28`](#insn-00bbfd28) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd28`](#insn-00bbfd28) → [`00bbfd2c`](#insn-00bbfd2c)
- ブロック [`00bbfd2c`](#insn-00bbfd2c) 範囲 `[['00bbfd2c', '00bbfd37']]`
  - `CONDITIONAL_JUMP` [`00bbfd34`](#insn-00bbfd34) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd34`](#insn-00bbfd34) → [`00bbfd38`](#insn-00bbfd38)
- ブロック [`00bbfd38`](#insn-00bbfd38) 範囲 `[['00bbfd38', '00bbfd3f']]`
  - `CONDITIONAL_JUMP` [`00bbfd3c`](#insn-00bbfd3c) → [`00bbfd48`](#insn-00bbfd48)
  - `FALL_THROUGH` [`00bbfd3c`](#insn-00bbfd3c) → [`00bbfd40`](#insn-00bbfd40)
- ブロック [`00bbfd40`](#insn-00bbfd40) 範囲 `[['00bbfd40', '00bbfd47']]`
  - `CONDITIONAL_JUMP` [`00bbfd44`](#insn-00bbfd44) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd44`](#insn-00bbfd44) → [`00bbfd48`](#insn-00bbfd48)
- ブロック [`00bbfd48`](#insn-00bbfd48) 範囲 `[['00bbfd48', '00bbfd4b']]`
  - `CONDITIONAL_JUMP` [`00bbfd48`](#insn-00bbfd48) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfd48`](#insn-00bbfd48) → [`00bbfd4c`](#insn-00bbfd4c)
- ブロック [`00bbfd4c`](#insn-00bbfd4c) 範囲 `[['00bbfd4c', '00bbfd57']]`
  - `CONDITIONAL_JUMP` [`00bbfd54`](#insn-00bbfd54) → [`00bbfd90`](#insn-00bbfd90)
  - `FALL_THROUGH` [`00bbfd54`](#insn-00bbfd54) → [`00bbfd58`](#insn-00bbfd58)
- ブロック [`00bbfd58`](#insn-00bbfd58) 範囲 `[['00bbfd58', '00bbfd5f']]`
  - `CONDITIONAL_JUMP` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfd90`](#insn-00bbfd90)
  - `FALL_THROUGH` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfd60`](#insn-00bbfd60)
- ブロック [`00bbfd60`](#insn-00bbfd60) 範囲 `[['00bbfd60', '00bbfd73']]`
  - `CONDITIONAL_JUMP` [`00bbfd70`](#insn-00bbfd70) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfd70`](#insn-00bbfd70) → [`00bbfd74`](#insn-00bbfd74)
- ブロック [`00bbfd74`](#insn-00bbfd74) 範囲 `[['00bbfd74', '00bbfd7b']]`
  - `CONDITIONAL_JUMP` [`00bbfd78`](#insn-00bbfd78) → [`00bbfda0`](#insn-00bbfda0)
  - `FALL_THROUGH` [`00bbfd78`](#insn-00bbfd78) → [`00bbfd7c`](#insn-00bbfd7c)
- ブロック [`00bbfd7c`](#insn-00bbfd7c) 範囲 `[['00bbfd7c', '00bbfd8b']]`
  - `CONDITIONAL_JUMP` [`00bbfd88`](#insn-00bbfd88) → [`00bbfda0`](#insn-00bbfda0)
  - `FALL_THROUGH` [`00bbfd88`](#insn-00bbfd88) → [`00bbfd8c`](#insn-00bbfd8c)
- ブロック [`00bbfd8c`](#insn-00bbfd8c) 範囲 `[['00bbfd8c', '00bbfd8f']]`
  - `FALL_THROUGH` [`00bbfd8c`](#insn-00bbfd8c) → [`00bbfd90`](#insn-00bbfd90)
- ブロック [`00bbfd90`](#insn-00bbfd90) 範囲 `[['00bbfd90', '00bbfd97']]`
  - `FALL_THROUGH` [`00bbfd94`](#insn-00bbfd94) → [`00bbfd98`](#insn-00bbfd98)
- ブロック [`00bbfd98`](#insn-00bbfd98) 範囲 `[['00bbfd98', '00bbfd9f']]`
- ブロック [`00bbfda0`](#insn-00bbfda0) 範囲 `[['00bbfda0', '00bbfda7']]`
  - `CONDITIONAL_JUMP` [`00bbfda4`](#insn-00bbfda4) → [`00bbfdd4`](#insn-00bbfdd4)
  - `FALL_THROUGH` [`00bbfda4`](#insn-00bbfda4) → [`00bbfda8`](#insn-00bbfda8)
- ブロック [`00bbfda8`](#insn-00bbfda8) 範囲 `[['00bbfda8', '00bbfdaf']]`
  - `CONDITIONAL_JUMP` [`00bbfdac`](#insn-00bbfdac) → [`00bbfe08`](#insn-00bbfe08)
  - `FALL_THROUGH` [`00bbfdac`](#insn-00bbfdac) → [`00bbfdb0`](#insn-00bbfdb0)
- ブロック [`00bbfdb0`](#insn-00bbfdb0) 範囲 `[['00bbfdb0', '00bbfdb3']]`
  - `FALL_THROUGH` [`00bbfdb0`](#insn-00bbfdb0) → [`00bbfdb4`](#insn-00bbfdb4)
- ブロック [`00bbfdb4`](#insn-00bbfdb4) 範囲 `[['00bbfdb4', '00bbfdbb']]`
  - `CONDITIONAL_JUMP` [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfde4`](#insn-00bbfde4)
  - `FALL_THROUGH` [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfdbc`](#insn-00bbfdbc)
- ブロック [`00bbfdbc`](#insn-00bbfdbc) 範囲 `[['00bbfdbc', '00bbfdc7']]`
  - `CONDITIONAL_JUMP` [`00bbfdc4`](#insn-00bbfdc4) → [`00bbfd90`](#insn-00bbfd90)
  - `FALL_THROUGH` [`00bbfdc4`](#insn-00bbfdc4) → [`00bbfdc8`](#insn-00bbfdc8)
- ブロック [`00bbfdc8`](#insn-00bbfdc8) 範囲 `[['00bbfdc8', '00bbfdcf']]`
  - `CONDITIONAL_JUMP` [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfdec`](#insn-00bbfdec)
  - `FALL_THROUGH` [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfdd0`](#insn-00bbfdd0)
- ブロック [`00bbfdd0`](#insn-00bbfdd0) 範囲 `[['00bbfdd0', '00bbfdd3']]`
  - `UNCONDITIONAL_JUMP` [`00bbfdd0`](#insn-00bbfdd0) → [`00bbfd90`](#insn-00bbfd90)
- ブロック [`00bbfdd4`](#insn-00bbfdd4) 範囲 `[['00bbfdd4', '00bbfddf']]`
  - `CONDITIONAL_JUMP` [`00bbfddc`](#insn-00bbfddc) → [`00bbfe24`](#insn-00bbfe24)
  - `FALL_THROUGH` [`00bbfddc`](#insn-00bbfddc) → [`00bbfde0`](#insn-00bbfde0)
- ブロック [`00bbfde0`](#insn-00bbfde0) 範囲 `[['00bbfde0', '00bbfde3']]`
  - `UNCONDITIONAL_JUMP` [`00bbfde0`](#insn-00bbfde0) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfde4`](#insn-00bbfde4) 範囲 `[['00bbfde4', '00bbfdeb']]`
  - `CONDITIONAL_JUMP` [`00bbfde8`](#insn-00bbfde8) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfde8`](#insn-00bbfde8) → [`00bbfdec`](#insn-00bbfdec)
- ブロック [`00bbfdec`](#insn-00bbfdec) 範囲 `[['00bbfdec', '00bbfdf7']]`
  - `CONDITIONAL_JUMP` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfdf8`](#insn-00bbfdf8)
- ブロック [`00bbfdf8`](#insn-00bbfdf8) 範囲 `[['00bbfdf8', '00bbfe07']]`
  - `CONDITIONAL_JUMP` [`00bbfe04`](#insn-00bbfe04) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfe04`](#insn-00bbfe04) → [`00bbfe08`](#insn-00bbfe08)
- ブロック [`00bbfe08`](#insn-00bbfe08) 範囲 `[['00bbfe08', '00bbfe0f']]`
  - `CONDITIONAL_JUMP` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe1c`](#insn-00bbfe1c)
  - `FALL_THROUGH` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe10`](#insn-00bbfe10)
- ブロック [`00bbfe10`](#insn-00bbfe10) 範囲 `[['00bbfe10', '00bbfe1b']]`
  - `FALL_THROUGH` [`00bbfe18`](#insn-00bbfe18) → [`00bbfe1c`](#insn-00bbfe1c)
- ブロック [`00bbfe1c`](#insn-00bbfe1c) 範囲 `[['00bbfe1c', '00bbfe23']]`
  - `CONDITIONAL_JUMP` [`00bbfe20`](#insn-00bbfe20) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe20`](#insn-00bbfe20) → [`00bbfe24`](#insn-00bbfe24)
- ブロック [`00bbfe24`](#insn-00bbfe24) 範囲 `[['00bbfe24', '00bbfe33']]`
  - `CONDITIONAL_JUMP` [`00bbfe30`](#insn-00bbfe30) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe30`](#insn-00bbfe30) → [`00bbfe34`](#insn-00bbfe34)
- ブロック [`00bbfe34`](#insn-00bbfe34) 範囲 `[['00bbfe34', '00bbfe47']]`
  - `FALL_THROUGH` [`00bbfe44`](#insn-00bbfe44) → [`00bbfe48`](#insn-00bbfe48)
- ブロック [`00bbfe48`](#insn-00bbfe48) 範囲 `[['00bbfe48', '00bbfe4b']]`
  - `COMPUTED_JUMP` [`00bbfe48`](#insn-00bbfe48) → [`00bbfe4c`](#insn-00bbfe4c)
  - `COMPUTED_JUMP` [`00bbfe48`](#insn-00bbfe48) → [`00bbfe64`](#insn-00bbfe64)
  - `COMPUTED_JUMP` [`00bbfe48`](#insn-00bbfe48) → [`00bbfe7c`](#insn-00bbfe7c)
  - `COMPUTED_JUMP` [`00bbfe48`](#insn-00bbfe48) → [`00bbfe94`](#insn-00bbfe94)
- ブロック [`00bbfe4c`](#insn-00bbfe4c) 範囲 `[['00bbfe4c', '00bbfe4f']]`
  - `CONDITIONAL_JUMP` [`00bbfe4c`](#insn-00bbfe4c) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe4c`](#insn-00bbfe4c) → [`00bbfe50`](#insn-00bbfe50)
- ブロック [`00bbfe50`](#insn-00bbfe50) 範囲 `[['00bbfe50', '00bbfe5f']]`
  - `CONDITIONAL_JUMP` [`00bbfe5c`](#insn-00bbfe5c) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfe5c`](#insn-00bbfe5c) → [`00bbfe60`](#insn-00bbfe60)
- ブロック [`00bbfe60`](#insn-00bbfe60) 範囲 `[['00bbfe60', '00bbfe63']]`
  - `UNCONDITIONAL_JUMP` [`00bbfe60`](#insn-00bbfe60) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfe64`](#insn-00bbfe64) 範囲 `[['00bbfe64', '00bbfe67']]`
  - `CONDITIONAL_JUMP` [`00bbfe64`](#insn-00bbfe64) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe64`](#insn-00bbfe64) → [`00bbfe68`](#insn-00bbfe68)
- ブロック [`00bbfe68`](#insn-00bbfe68) 範囲 `[['00bbfe68', '00bbfe77']]`
  - `CONDITIONAL_JUMP` [`00bbfe74`](#insn-00bbfe74) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfe74`](#insn-00bbfe74) → [`00bbfe78`](#insn-00bbfe78)
- ブロック [`00bbfe78`](#insn-00bbfe78) 範囲 `[['00bbfe78', '00bbfe7b']]`
  - `UNCONDITIONAL_JUMP` [`00bbfe78`](#insn-00bbfe78) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfe7c`](#insn-00bbfe7c) 範囲 `[['00bbfe7c', '00bbfe7f']]`
  - `CONDITIONAL_JUMP` [`00bbfe7c`](#insn-00bbfe7c) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe7c`](#insn-00bbfe7c) → [`00bbfe80`](#insn-00bbfe80)
- ブロック [`00bbfe80`](#insn-00bbfe80) 範囲 `[['00bbfe80', '00bbfe8f']]`
  - `CONDITIONAL_JUMP` [`00bbfe8c`](#insn-00bbfe8c) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfe8c`](#insn-00bbfe8c) → [`00bbfe90`](#insn-00bbfe90)
- ブロック [`00bbfe90`](#insn-00bbfe90) 範囲 `[['00bbfe90', '00bbfe93']]`
  - `UNCONDITIONAL_JUMP` [`00bbfe90`](#insn-00bbfe90) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfe94`](#insn-00bbfe94) 範囲 `[['00bbfe94', '00bbfe97']]`
  - `CONDITIONAL_JUMP` [`00bbfe94`](#insn-00bbfe94) → [`00bbfea8`](#insn-00bbfea8)
  - `FALL_THROUGH` [`00bbfe94`](#insn-00bbfe94) → [`00bbfe98`](#insn-00bbfe98)
- ブロック [`00bbfe98`](#insn-00bbfe98) 範囲 `[['00bbfe98', '00bbfea7']]`
  - `CONDITIONAL_JUMP` [`00bbfea4`](#insn-00bbfea4) → [`00bbfd8c`](#insn-00bbfd8c)
  - `FALL_THROUGH` [`00bbfea4`](#insn-00bbfea4) → [`00bbfea8`](#insn-00bbfea8)
- ブロック [`00bbfea8`](#insn-00bbfea8) 範囲 `[['00bbfea8', '00bbfebb']]`
  - `UNCONDITIONAL_JUMP` [`00bbfeb8`](#insn-00bbfeb8) → [`00bbfd90`](#insn-00bbfd90)

## 命令位置別の参照

- [`00bbfcac`](#insn-00bbfcac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcb0`](#insn-00bbfcb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfcd4`](#insn-00bbfcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcd0`](#insn-00bbfcd0) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfce0`](#insn-00bbfce0) → [`00bbfd90`](#insn-00bbfd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcec`](#insn-00bbfcec) → [`00bbfd90`](#insn-00bbfd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd18`](#insn-00bbfd18) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd20`](#insn-00bbfd20) → [`00bbfd2c`](#insn-00bbfd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd28`](#insn-00bbfd28) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd34`](#insn-00bbfd34) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd3c`](#insn-00bbfd3c) → [`00bbfd48`](#insn-00bbfd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd44`](#insn-00bbfd44) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd48`](#insn-00bbfd48) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd54`](#insn-00bbfd54) → [`00bbfd90`](#insn-00bbfd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfd90`](#insn-00bbfd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd70`](#insn-00bbfd70) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfd78`](#insn-00bbfd78) → [`00bbfda0`](#insn-00bbfda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd88`](#insn-00bbfd88) → [`00bbfda0`](#insn-00bbfda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd90`](#insn-00bbfd90) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda4`](#insn-00bbfda4) → [`00bbfdd4`](#insn-00bbfdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdac`](#insn-00bbfdac) → [`00bbfe08`](#insn-00bbfe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfde4`](#insn-00bbfde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdc4`](#insn-00bbfdc4) → [`00bbfd90`](#insn-00bbfd90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfdec`](#insn-00bbfdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd0`](#insn-00bbfdd0) → [`00bbfd90`](#insn-00bbfd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfddc`](#insn-00bbfddc) → [`00bbfe24`](#insn-00bbfe24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfde0`](#insn-00bbfde0) → [`00bbfea8`](#insn-00bbfea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfde8`](#insn-00bbfde8) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe04`](#insn-00bbfe04) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe1c`](#insn-00bbfe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe20`](#insn-00bbfe20) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe30`](#insn-00bbfe30) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe40`](#insn-00bbfe40) → `0030e924`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbfe48::switchdataD_0030e924` · 推定型 `byte`
- [`00bbfe48`](#insn-00bbfe48) → [`00bbfe4c`](#insn-00bbfe4c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbfe48::caseD_1` · 推定型 `None`
- [`00bbfe48`](#insn-00bbfe48) → [`00bbfe64`](#insn-00bbfe64) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbfe48::caseD_2` · 推定型 `None`
- [`00bbfe48`](#insn-00bbfe48) → [`00bbfe7c`](#insn-00bbfe7c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbfe48::caseD_3` · 推定型 `None`
- [`00bbfe48`](#insn-00bbfe48) → [`00bbfe94`](#insn-00bbfe94) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbfe48::caseD_4` · 推定型 `None`
- [`00bbfe4c`](#insn-00bbfe4c) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe58`](#insn-00bbfe58) → [`00c5e580`](../00c5e/00c5e580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e580` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe5c`](#insn-00bbfe5c) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe60`](#insn-00bbfe60) → [`00bbfea8`](#insn-00bbfea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe64`](#insn-00bbfe64) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe70`](#insn-00bbfe70) → [`00c5e5a0`](../00c5e/00c5e5a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe74`](#insn-00bbfe74) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe78`](#insn-00bbfe78) → [`00bbfea8`](#insn-00bbfea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe7c`](#insn-00bbfe7c) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe88`](#insn-00bbfe88) → [`00c5e5b0`](../00c5e/00c5e5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe8c`](#insn-00bbfe8c) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe90`](#insn-00bbfe90) → [`00bbfea8`](#insn-00bbfea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfe94`](#insn-00bbfe94) → [`00bbfea8`](#insn-00bbfea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbfe48::default` · 推定型 `None`
- [`00bbfea0`](#insn-00bbfea0) → [`00c5e5c0`](../00c5e/00c5e5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfea4`](#insn-00bbfea4) → [`00bbfd8c`](#insn-00bbfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfeb8`](#insn-00bbfeb8) → [`00bbfd90`](#insn-00bbfd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfcac`](#insn-00bbfcac)

~~~json
{
  "source": "00bbfcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcb0`](#insn-00bbfcb0)

~~~json
{
  "source": "00bbfcb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcc8`](#insn-00bbfcc8)

~~~json
{
  "source": "00bbfcc8",
  "target": "00bbfcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcd0`](#insn-00bbfcd0)

~~~json
{
  "source": "00bbfcd0",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfce0`](#insn-00bbfce0)

~~~json
{
  "source": "00bbfce0",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcec`](#insn-00bbfcec)

~~~json
{
  "source": "00bbfcec",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd0c`](#insn-00bbfd0c)

~~~json
{
  "source": "00bbfd0c",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd18`](#insn-00bbfd18)

~~~json
{
  "source": "00bbfd18",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd20`](#insn-00bbfd20)

~~~json
{
  "source": "00bbfd20",
  "target": "00bbfd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd28`](#insn-00bbfd28)

~~~json
{
  "source": "00bbfd28",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd34`](#insn-00bbfd34)

~~~json
{
  "source": "00bbfd34",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd3c`](#insn-00bbfd3c)

~~~json
{
  "source": "00bbfd3c",
  "target": "00bbfd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd44`](#insn-00bbfd44)

~~~json
{
  "source": "00bbfd44",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd48`](#insn-00bbfd48)

~~~json
{
  "source": "00bbfd48",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd54`](#insn-00bbfd54)

~~~json
{
  "source": "00bbfd54",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd5c`](#insn-00bbfd5c)

~~~json
{
  "source": "00bbfd5c",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd70`](#insn-00bbfd70)

~~~json
{
  "source": "00bbfd70",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd78`](#insn-00bbfd78)

~~~json
{
  "source": "00bbfd78",
  "target": "00bbfda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd88`](#insn-00bbfd88)

~~~json
{
  "source": "00bbfd88",
  "target": "00bbfda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd90`](#insn-00bbfd90)

~~~json
{
  "source": "00bbfd90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfda4`](#insn-00bbfda4)

~~~json
{
  "source": "00bbfda4",
  "target": "00bbfdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdac`](#insn-00bbfdac)

~~~json
{
  "source": "00bbfdac",
  "target": "00bbfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdb8`](#insn-00bbfdb8)

~~~json
{
  "source": "00bbfdb8",
  "target": "00bbfde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdc4`](#insn-00bbfdc4)

~~~json
{
  "source": "00bbfdc4",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdcc`](#insn-00bbfdcc)

~~~json
{
  "source": "00bbfdcc",
  "target": "00bbfdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd0`](#insn-00bbfdd0)

~~~json
{
  "source": "00bbfdd0",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfddc`](#insn-00bbfddc)

~~~json
{
  "source": "00bbfddc",
  "target": "00bbfe24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfde0`](#insn-00bbfde0)

~~~json
{
  "source": "00bbfde0",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfde8`](#insn-00bbfde8)

~~~json
{
  "source": "00bbfde8",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdf4`](#insn-00bbfdf4)

~~~json
{
  "source": "00bbfdf4",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe04`](#insn-00bbfe04)

~~~json
{
  "source": "00bbfe04",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe0c`](#insn-00bbfe0c)

~~~json
{
  "source": "00bbfe0c",
  "target": "00bbfe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe20`](#insn-00bbfe20)

~~~json
{
  "source": "00bbfe20",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe30`](#insn-00bbfe30)

~~~json
{
  "source": "00bbfe30",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe40`](#insn-00bbfe40)

~~~json
{
  "source": "00bbfe40",
  "target": "0030e924",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e924",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e924",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbfe48`](#insn-00bbfe48)

~~~json
{
  "source": "00bbfe48",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe48`](#insn-00bbfe48)

~~~json
{
  "source": "00bbfe48",
  "target": "00bbfe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe48`](#insn-00bbfe48)

~~~json
{
  "source": "00bbfe48",
  "target": "00bbfe7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe48`](#insn-00bbfe48)

~~~json
{
  "source": "00bbfe48",
  "target": "00bbfe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe4c`](#insn-00bbfe4c)

~~~json
{
  "source": "00bbfe4c",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe58`](#insn-00bbfe58)

~~~json
{
  "source": "00bbfe58",
  "target": "00c5e580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe5c`](#insn-00bbfe5c)

~~~json
{
  "source": "00bbfe5c",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe60`](#insn-00bbfe60)

~~~json
{
  "source": "00bbfe60",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe64`](#insn-00bbfe64)

~~~json
{
  "source": "00bbfe64",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe70`](#insn-00bbfe70)

~~~json
{
  "source": "00bbfe70",
  "target": "00c5e5a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe74`](#insn-00bbfe74)

~~~json
{
  "source": "00bbfe74",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe78`](#insn-00bbfe78)

~~~json
{
  "source": "00bbfe78",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe7c`](#insn-00bbfe7c)

~~~json
{
  "source": "00bbfe7c",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe88`](#insn-00bbfe88)

~~~json
{
  "source": "00bbfe88",
  "target": "00c5e5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfe8c`](#insn-00bbfe8c)

~~~json
{
  "source": "00bbfe8c",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe90`](#insn-00bbfe90)

~~~json
{
  "source": "00bbfe90",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe94`](#insn-00bbfe94)

~~~json
{
  "source": "00bbfe94",
  "target": "00bbfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfea0`](#insn-00bbfea0)

~~~json
{
  "source": "00bbfea0",
  "target": "00c5e5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfea4`](#insn-00bbfea4)

~~~json
{
  "source": "00bbfea4",
  "target": "00bbfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfeb8`](#insn-00bbfeb8)

~~~json
{
  "source": "00bbfeb8",
  "target": "00bbfd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
