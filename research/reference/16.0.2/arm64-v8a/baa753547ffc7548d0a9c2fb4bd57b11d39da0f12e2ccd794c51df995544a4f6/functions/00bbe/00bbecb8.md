# 00bbecb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbec1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-eb028551d2f0c83cc08a3a0d2f1fdcf5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbfcac`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfcac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0014.md#compare-955fbef8b7d91e1e95b79c9b3b3b8a34)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbecb8",
  "name": "_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "343ae5b253d53c4cf5f9a7b9773dbf3a64f4d70350feb75408f1e6585a902ebd",
  "source_text_sha256": "343ae5b253d53c4cf5f9a7b9773dbf3a64f4d70350feb75408f1e6585a902ebd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbecb8",
        "00bbeec7"
      ]
    ],
    "bytes_sha256": "35cee11b15266117aaa737d4bb55f6640b2b5ef6605e2451ded60c092deafbf5",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d5a0](../00c5d/00c5d5a0.md)

## 呼び出し先

- [00c5d5b0](../00c5d/00c5d5b0.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)
- [00c5d5e0](../00c5d/00c5d5e0.md)
- [00c5d5f0](../00c5d/00c5d5f0.md)

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
                    /* try { // try from 00bbecdc to 00cbecf7 has its CatchHandler @ 00bbf420 */
  if (((uVar8 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar7 = param_2[1];
    if (uVar7 < 5) {
      return 0;
    }
    uVar9 = uVar7 - 4;
                    /* try { // try from 00bbecf8 to 00cbeda3 has its CatchHandler @ 00bbe868 */
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
                    /* try { // try from 00bbedc0 to 00cbf163 has its CatchHandler @ 00bbe868 */
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
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 2:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 3:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp30SerializedRegistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 4:
              if (lVar6 == 0) goto switchD_00bbee54_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            default:
              goto switchD_00bbee54_default;
            }
            if ((uVar8 & 1) == 0) {
              return 0;
            }
          }
        }
switchD_00bbee54_default:
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
                    /* try { // try from 00bbeda4 to 00cbedbf has its CatchHandler @ 00bbf428 */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbecb8"></a> `00bbecb8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbecbc"></a> `00bbecbc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbecc0"></a> `00bbecc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbecc4"></a> `00bbecc4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bbecc8"></a> `00bbecc8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbeccc"></a> `00bbeccc` | `0b 00 09 cb` | sub x11,x0,x9 | `FALL_THROUGH`
<a id="insn-00bbecd0"></a> `00bbecd0` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbecd4"></a> `00bbecd4` | `60 00 00 54` | b.eq 0x00bbece0 | `CONDITIONAL_JUMP`
<a id="insn-00bbecd8"></a> `00bbecd8` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbecdc"></a> `00bbecdc` | `e8 05 00 35` | cbnz w8,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbece0"></a> `00bbece0` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbece4"></a> `00bbece4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbece8"></a> `00bbece8` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbecec"></a> `00bbecec` | `83 05 00 54` | b.cc 0x00bbed9c | `CONDITIONAL_JUMP`
<a id="insn-00bbecf0"></a> `00bbecf0` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbecf4"></a> `00bbecf4` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbecf8"></a> `00bbecf8` | `23 05 00 54` | b.cc 0x00bbed9c | `CONDITIONAL_JUMP`
<a id="insn-00bbecfc"></a> `00bbecfc` | `6d 3a 47 29` | ldp w13,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbed00"></a> `00bbed00` | `6f 12 40 b9` | ldr w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbed04"></a> `00bbed04` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbed08"></a> `00bbed08` | `b0 05 00 11` | add w16,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed0c"></a> `00bbed0c` | `cd 05 00 11` | add w13,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed10"></a> `00bbed10` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbed14"></a> `00bbed14` | `70 36 07 29` | stp w16,w13,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbed18"></a> `00bbed18` | `08 04 00 54` | b.hi 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed1c"></a> `00bbed1c` | `6e 16 40 b9` | ldr w14,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00bbed20"></a> `00bbed20` | `bf 01 0e 6b` | cmp w13,w14 | `FALL_THROUGH`
<a id="insn-00bbed24"></a> `00bbed24` | `a8 03 00 54` | b.hi 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed28"></a> `00bbed28` | `6d 01 08 cb` | sub x13,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbed2c"></a> `00bbed2c` | `6d 00 00 36` | tbz w13,#0x0,0x00bbed38 | `CONDITIONAL_JUMP`
<a id="insn-00bbed30"></a> `00bbed30` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbed34"></a> `00bbed34` | `28 03 00 35` | cbnz w8,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed38"></a> `00bbed38` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbed3c"></a> `00bbed3c` | `1f 01 0d eb` | cmp x8,x13 | `FALL_THROUGH`
<a id="insn-00bbed40"></a> `00bbed40` | `c3 02 00 54` | b.cc 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed44"></a> `00bbed44` | `28 69 6d 78` | ldrh w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbed48"></a> `00bbed48` | `68 00 00 36` | tbz w8,#0x0,0x00bbed54 | `CONDITIONAL_JUMP`
<a id="insn-00bbed4c"></a> `00bbed4c` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbed50"></a> `00bbed50` | `4e 02 00 35` | cbnz w14,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed54"></a> `00bbed54` | `28 02 00 37` | tbnz w8,#0x0,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbed58"></a> `00bbed58` | `4e 01 08 eb` | subs x14,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbed5c"></a> `00bbed5c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbed60"></a> `00bbed60` | `e9 01 00 54` | b.ls 0x00bbed9c | `CONDITIONAL_JUMP`
<a id="insn-00bbed64"></a> `00bbed64` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00bbed68"></a> `00bbed68` | `a3 01 00 54` | b.cc 0x00bbed9c | `CONDITIONAL_JUMP`
<a id="insn-00bbed6c"></a> `00bbed6c` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbed70"></a> `00bbed70` | `0d 00 08 cb` | sub x13,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbed74"></a> `00bbed74` | `a8 01 40 79` | ldrh w8,[x13] | `FALL_THROUGH`
<a id="insn-00bbed78"></a> `00bbed78` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbed7c"></a> `00bbed7c` | `c3 09 00 54` | b.cc 0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbed80"></a> `00bbed80` | `ae 09 40 79` | ldrh w14,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbed84"></a> `00bbed84` | `4e 01 00 b4` | cbz x14,0x00bbedac | `CONDITIONAL_JUMP`
<a id="insn-00bbed88"></a> `00bbed88` | `6e 01 0e 8b` | add x14,x11,x14 | `FALL_THROUGH`
<a id="insn-00bbed8c"></a> `00bbed8c` | `4f 05 00 d1` | sub x15,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed90"></a> `00bbed90` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbed94"></a> `00bbed94` | `c2 00 00 54` | b.cs 0x00bbedac | `CONDITIONAL_JUMP`
<a id="insn-00bbed98"></a> `00bbed98` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbed9c"></a> `00bbed9c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeda0"></a> `00bbeda0` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bbeda4"></a> `00bbeda4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbeda8"></a> `00bbeda8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbedac"></a> `00bbedac` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-00bbedb0"></a> `00bbedb0` | `83 01 00 54` | b.cc 0x00bbede0 | `CONDITIONAL_JUMP`
<a id="insn-00bbedb4"></a> `00bbedb4` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbedb8"></a> `00bbedb8` | `e8 02 00 b4` | cbz x8,0x00bbee14 | `CONDITIONAL_JUMP`
<a id="insn-00bbedbc"></a> `00bbedbc` | `6b 01 08 8b` | add x11,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbedc0"></a> `00bbedc0` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbedc4"></a> `00bbedc4` | `60 01 00 54` | b.eq 0x00bbedf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbedc8"></a> `00bbedc8` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbedcc"></a> `00bbedcc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbedd0"></a> `00bbedd0` | `6e fe ff 35` | cbnz w14,0x00bbed9c | `CONDITIONAL_JUMP`
<a id="insn-00bbedd4"></a> `00bbedd4` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbedd8"></a> `00bbedd8` | `02 01 00 54` | b.cs 0x00bbedf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbeddc"></a> `00bbeddc` | `f0 ff ff 17` | b 0x00bbed9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbede0"></a> `00bbede0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbede4"></a> `00bbede4` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbede8"></a> `00bbede8` | `49 02 00 b5` | cbnz x9,0x00bbee30 | `CONDITIONAL_JUMP`
<a id="insn-00bbedec"></a> `00bbedec` | `32 00 00 14` | b 0x00bbeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbedf0"></a> `00bbedf0` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbedf4"></a> `00bbedf4` | `23 fd ff 54` | b.cc 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbedf8"></a> `00bbedf8` | `28 69 6b b8` | ldr w8,[x9, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbedfc"></a> `00bbedfc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee00"></a> `00bbee00` | `cb fc ff 54` | b.lt 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbee04"></a> `00bbee04` | `68 01 08 8b` | add x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbee08"></a> `00bbee08` | `49 05 00 d1` | sub x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee0c"></a> `00bbee0c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbee10"></a> `00bbee10` | `43 fc ff 54` | b.cc 0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbee14"></a> `00bbee14` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbee18"></a> `00bbee18` | `88 00 00 b4` | cbz x8,0x00bbee28 | `CONDITIONAL_JUMP`
<a id="insn-00bbee1c"></a> `00bbee1c` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbee20"></a> `00bbee20` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbee24"></a> `00bbee24` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbee28"></a> `00bbee28` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbee2c"></a> `00bbee2c` | `49 04 00 b4` | cbz x9,0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbee30"></a> `00bbee30` | `09 68 69 38` | ldrb w9,[x0, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbee34"></a> `00bbee34` | `29 05 00 51` | sub w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee38"></a> `00bbee38` | `3f 0d 00 71` | cmp w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbee3c"></a> `00bbee3c` | `c8 03 00 54` | b.hi 0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbee40"></a> `00bbee40` | `8a ba ff 90` | adrp x10,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbee44"></a> `00bbee44` | `4a 91 23 91` | add x10,x10,#0x8e4 | `FALL_THROUGH`
<a id="insn-00bbee48"></a> `00bbee48` | `8b 00 00 10` | adr x11,0xbbee58 | `FALL_THROUGH`
<a id="insn-00bbee4c"></a> `00bbee4c` | `4c 69 69 38` | ldrb w12,[x10, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbee50"></a> `00bbee50` | `6b 09 0c 8b` | add x11,x11,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbee54"></a> `00bbee54` | `60 01 1f d6` | br x11 | `COMPUTED_JUMP`
<a id="insn-00bbee58"></a> `00bbee58` | `e8 02 00 b4` | cbz x8,0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbee5c"></a> `00bbee5c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbee60"></a> `00bbee60` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbee64"></a> `00bbee64` | `d3 79 02 94` | bl 0x00c5d5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee68"></a> `00bbee68` | `80 f9 07 36` | tbz w0,#0x0,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbee6c"></a> `00bbee6c` | `12 00 00 14` | b 0x00bbeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbee70"></a> `00bbee70` | `28 02 00 b4` | cbz x8,0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbee74"></a> `00bbee74` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbee78"></a> `00bbee78` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbee7c"></a> `00bbee7c` | `d5 79 02 94` | bl 0x00c5d5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee80"></a> `00bbee80` | `c0 f8 07 36` | tbz w0,#0x0,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbee84"></a> `00bbee84` | `0c 00 00 14` | b 0x00bbeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbee88"></a> `00bbee88` | `68 01 00 b4` | cbz x8,0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbee8c"></a> `00bbee8c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbee90"></a> `00bbee90` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbee94"></a> `00bbee94` | `d3 79 02 94` | bl 0x00c5d5e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee98"></a> `00bbee98` | `00 f8 07 36` | tbz w0,#0x0,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbee9c"></a> `00bbee9c` | `06 00 00 14` | b 0x00bbeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeea0"></a> `00bbeea0` | `a8 00 00 b4` | cbz x8,0x00bbeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbeea4"></a> `00bbeea4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbeea8"></a> `00bbeea8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbeeac"></a> `00bbeeac` | `d1 79 02 94` | bl 0x00c5d5f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeeb0"></a> `00bbeeb0` | `40 f7 07 36` | tbz w0,#0x0,0x00bbed98 | `CONDITIONAL_JUMP`
<a id="insn-00bbeeb4"></a> `00bbeeb4` | `68 3a 40 b9` | ldr w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbeeb8"></a> `00bbeeb8` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbeebc"></a> `00bbeebc` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbeec0"></a> `00bbeec0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbeec4"></a> `00bbeec4` | `b6 ff ff 17` | b 0x00bbed9c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbecb8`](#insn-00bbecb8) 範囲 `[['00bbecb8', '00bbecd7']]`
  - `CONDITIONAL_JUMP` [`00bbecd4`](#insn-00bbecd4) → [`00bbece0`](#insn-00bbece0)
  - `FALL_THROUGH` [`00bbecd4`](#insn-00bbecd4) → [`00bbecd8`](#insn-00bbecd8)
- ブロック [`00bbecd8`](#insn-00bbecd8) 範囲 `[['00bbecd8', '00bbecdb']]`
  - `FALL_THROUGH` [`00bbecd8`](#insn-00bbecd8) → [`00bbecdc`](#insn-00bbecdc)
- ブロック [`00bbecdc`](#insn-00bbecdc) 範囲 `[['00bbecdc', '00bbecdf']]`
  - `CONDITIONAL_JUMP` [`00bbecdc`](#insn-00bbecdc) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbecdc`](#insn-00bbecdc) → [`00bbece0`](#insn-00bbece0)
- ブロック [`00bbece0`](#insn-00bbece0) 範囲 `[['00bbece0', '00bbecef']]`
  - `CONDITIONAL_JUMP` [`00bbecec`](#insn-00bbecec) → [`00bbed9c`](#insn-00bbed9c)
  - `FALL_THROUGH` [`00bbecec`](#insn-00bbecec) → [`00bbecf0`](#insn-00bbecf0)
- ブロック [`00bbecf0`](#insn-00bbecf0) 範囲 `[['00bbecf0', '00bbecf7']]`
  - `FALL_THROUGH` [`00bbecf4`](#insn-00bbecf4) → [`00bbecf8`](#insn-00bbecf8)
- ブロック [`00bbecf8`](#insn-00bbecf8) 範囲 `[['00bbecf8', '00bbecfb']]`
  - `CONDITIONAL_JUMP` [`00bbecf8`](#insn-00bbecf8) → [`00bbed9c`](#insn-00bbed9c)
  - `FALL_THROUGH` [`00bbecf8`](#insn-00bbecf8) → [`00bbecfc`](#insn-00bbecfc)
- ブロック [`00bbecfc`](#insn-00bbecfc) 範囲 `[['00bbecfc', '00bbed1b']]`
  - `CONDITIONAL_JUMP` [`00bbed18`](#insn-00bbed18) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed18`](#insn-00bbed18) → [`00bbed1c`](#insn-00bbed1c)
- ブロック [`00bbed1c`](#insn-00bbed1c) 範囲 `[['00bbed1c', '00bbed27']]`
  - `CONDITIONAL_JUMP` [`00bbed24`](#insn-00bbed24) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed24`](#insn-00bbed24) → [`00bbed28`](#insn-00bbed28)
- ブロック [`00bbed28`](#insn-00bbed28) 範囲 `[['00bbed28', '00bbed2f']]`
  - `CONDITIONAL_JUMP` [`00bbed2c`](#insn-00bbed2c) → [`00bbed38`](#insn-00bbed38)
  - `FALL_THROUGH` [`00bbed2c`](#insn-00bbed2c) → [`00bbed30`](#insn-00bbed30)
- ブロック [`00bbed30`](#insn-00bbed30) 範囲 `[['00bbed30', '00bbed37']]`
  - `CONDITIONAL_JUMP` [`00bbed34`](#insn-00bbed34) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed34`](#insn-00bbed34) → [`00bbed38`](#insn-00bbed38)
- ブロック [`00bbed38`](#insn-00bbed38) 範囲 `[['00bbed38', '00bbed43']]`
  - `CONDITIONAL_JUMP` [`00bbed40`](#insn-00bbed40) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed40`](#insn-00bbed40) → [`00bbed44`](#insn-00bbed44)
- ブロック [`00bbed44`](#insn-00bbed44) 範囲 `[['00bbed44', '00bbed4b']]`
  - `CONDITIONAL_JUMP` [`00bbed48`](#insn-00bbed48) → [`00bbed54`](#insn-00bbed54)
  - `FALL_THROUGH` [`00bbed48`](#insn-00bbed48) → [`00bbed4c`](#insn-00bbed4c)
- ブロック [`00bbed4c`](#insn-00bbed4c) 範囲 `[['00bbed4c', '00bbed53']]`
  - `CONDITIONAL_JUMP` [`00bbed50`](#insn-00bbed50) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed50`](#insn-00bbed50) → [`00bbed54`](#insn-00bbed54)
- ブロック [`00bbed54`](#insn-00bbed54) 範囲 `[['00bbed54', '00bbed57']]`
  - `CONDITIONAL_JUMP` [`00bbed54`](#insn-00bbed54) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbed54`](#insn-00bbed54) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbed58`](#insn-00bbed58) 範囲 `[['00bbed58', '00bbed63']]`
  - `CONDITIONAL_JUMP` [`00bbed60`](#insn-00bbed60) → [`00bbed9c`](#insn-00bbed9c)
  - `FALL_THROUGH` [`00bbed60`](#insn-00bbed60) → [`00bbed64`](#insn-00bbed64)
- ブロック [`00bbed64`](#insn-00bbed64) 範囲 `[['00bbed64', '00bbed6b']]`
  - `CONDITIONAL_JUMP` [`00bbed68`](#insn-00bbed68) → [`00bbed9c`](#insn-00bbed9c)
  - `FALL_THROUGH` [`00bbed68`](#insn-00bbed68) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbed6c`](#insn-00bbed6c) 範囲 `[['00bbed6c', '00bbed7f']]`
  - `CONDITIONAL_JUMP` [`00bbed7c`](#insn-00bbed7c) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbed7c`](#insn-00bbed7c) → [`00bbed80`](#insn-00bbed80)
- ブロック [`00bbed80`](#insn-00bbed80) 範囲 `[['00bbed80', '00bbed87']]`
  - `CONDITIONAL_JUMP` [`00bbed84`](#insn-00bbed84) → [`00bbedac`](#insn-00bbedac)
  - `FALL_THROUGH` [`00bbed84`](#insn-00bbed84) → [`00bbed88`](#insn-00bbed88)
- ブロック [`00bbed88`](#insn-00bbed88) 範囲 `[['00bbed88', '00bbed97']]`
  - `CONDITIONAL_JUMP` [`00bbed94`](#insn-00bbed94) → [`00bbedac`](#insn-00bbedac)
  - `FALL_THROUGH` [`00bbed94`](#insn-00bbed94) → [`00bbed98`](#insn-00bbed98)
- ブロック [`00bbed98`](#insn-00bbed98) 範囲 `[['00bbed98', '00bbed9b']]`
  - `FALL_THROUGH` [`00bbed98`](#insn-00bbed98) → [`00bbed9c`](#insn-00bbed9c)
- ブロック [`00bbed9c`](#insn-00bbed9c) 範囲 `[['00bbed9c', '00bbeda3']]`
  - `FALL_THROUGH` [`00bbeda0`](#insn-00bbeda0) → [`00bbeda4`](#insn-00bbeda4)
- ブロック [`00bbeda4`](#insn-00bbeda4) 範囲 `[['00bbeda4', '00bbedab']]`
- ブロック [`00bbedac`](#insn-00bbedac) 範囲 `[['00bbedac', '00bbedb3']]`
  - `CONDITIONAL_JUMP` [`00bbedb0`](#insn-00bbedb0) → [`00bbede0`](#insn-00bbede0)
  - `FALL_THROUGH` [`00bbedb0`](#insn-00bbedb0) → [`00bbedb4`](#insn-00bbedb4)
- ブロック [`00bbedb4`](#insn-00bbedb4) 範囲 `[['00bbedb4', '00bbedbb']]`
  - `CONDITIONAL_JUMP` [`00bbedb8`](#insn-00bbedb8) → [`00bbee14`](#insn-00bbee14)
  - `FALL_THROUGH` [`00bbedb8`](#insn-00bbedb8) → [`00bbedbc`](#insn-00bbedbc)
- ブロック [`00bbedbc`](#insn-00bbedbc) 範囲 `[['00bbedbc', '00bbedbf']]`
  - `FALL_THROUGH` [`00bbedbc`](#insn-00bbedbc) → [`00bbedc0`](#insn-00bbedc0)
- ブロック [`00bbedc0`](#insn-00bbedc0) 範囲 `[['00bbedc0', '00bbedc7']]`
  - `CONDITIONAL_JUMP` [`00bbedc4`](#insn-00bbedc4) → [`00bbedf0`](#insn-00bbedf0)
  - `FALL_THROUGH` [`00bbedc4`](#insn-00bbedc4) → [`00bbedc8`](#insn-00bbedc8)
- ブロック [`00bbedc8`](#insn-00bbedc8) 範囲 `[['00bbedc8', '00bbedd3']]`
  - `CONDITIONAL_JUMP` [`00bbedd0`](#insn-00bbedd0) → [`00bbed9c`](#insn-00bbed9c)
  - `FALL_THROUGH` [`00bbedd0`](#insn-00bbedd0) → [`00bbedd4`](#insn-00bbedd4)
- ブロック [`00bbedd4`](#insn-00bbedd4) 範囲 `[['00bbedd4', '00bbeddb']]`
  - `CONDITIONAL_JUMP` [`00bbedd8`](#insn-00bbedd8) → [`00bbedf8`](#insn-00bbedf8)
  - `FALL_THROUGH` [`00bbedd8`](#insn-00bbedd8) → [`00bbeddc`](#insn-00bbeddc)
- ブロック [`00bbeddc`](#insn-00bbeddc) 範囲 `[['00bbeddc', '00bbeddf']]`
  - `UNCONDITIONAL_JUMP` [`00bbeddc`](#insn-00bbeddc) → [`00bbed9c`](#insn-00bbed9c)
- ブロック [`00bbede0`](#insn-00bbede0) 範囲 `[['00bbede0', '00bbedeb']]`
  - `CONDITIONAL_JUMP` [`00bbede8`](#insn-00bbede8) → [`00bbee30`](#insn-00bbee30)
  - `FALL_THROUGH` [`00bbede8`](#insn-00bbede8) → [`00bbedec`](#insn-00bbedec)
- ブロック [`00bbedec`](#insn-00bbedec) 範囲 `[['00bbedec', '00bbedef']]`
  - `UNCONDITIONAL_JUMP` [`00bbedec`](#insn-00bbedec) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbedf0`](#insn-00bbedf0) 範囲 `[['00bbedf0', '00bbedf7']]`
  - `CONDITIONAL_JUMP` [`00bbedf4`](#insn-00bbedf4) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbedf4`](#insn-00bbedf4) → [`00bbedf8`](#insn-00bbedf8)
- ブロック [`00bbedf8`](#insn-00bbedf8) 範囲 `[['00bbedf8', '00bbee03']]`
  - `CONDITIONAL_JUMP` [`00bbee00`](#insn-00bbee00) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbee00`](#insn-00bbee00) → [`00bbee04`](#insn-00bbee04)
- ブロック [`00bbee04`](#insn-00bbee04) 範囲 `[['00bbee04', '00bbee13']]`
  - `CONDITIONAL_JUMP` [`00bbee10`](#insn-00bbee10) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbee10`](#insn-00bbee10) → [`00bbee14`](#insn-00bbee14)
- ブロック [`00bbee14`](#insn-00bbee14) 範囲 `[['00bbee14', '00bbee1b']]`
  - `CONDITIONAL_JUMP` [`00bbee18`](#insn-00bbee18) → [`00bbee28`](#insn-00bbee28)
  - `FALL_THROUGH` [`00bbee18`](#insn-00bbee18) → [`00bbee1c`](#insn-00bbee1c)
- ブロック [`00bbee1c`](#insn-00bbee1c) 範囲 `[['00bbee1c', '00bbee27']]`
  - `FALL_THROUGH` [`00bbee24`](#insn-00bbee24) → [`00bbee28`](#insn-00bbee28)
- ブロック [`00bbee28`](#insn-00bbee28) 範囲 `[['00bbee28', '00bbee2f']]`
  - `CONDITIONAL_JUMP` [`00bbee2c`](#insn-00bbee2c) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbee2c`](#insn-00bbee2c) → [`00bbee30`](#insn-00bbee30)
- ブロック [`00bbee30`](#insn-00bbee30) 範囲 `[['00bbee30', '00bbee3f']]`
  - `CONDITIONAL_JUMP` [`00bbee3c`](#insn-00bbee3c) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbee3c`](#insn-00bbee3c) → [`00bbee40`](#insn-00bbee40)
- ブロック [`00bbee40`](#insn-00bbee40) 範囲 `[['00bbee40', '00bbee53']]`
  - `FALL_THROUGH` [`00bbee50`](#insn-00bbee50) → [`00bbee54`](#insn-00bbee54)
- ブロック [`00bbee54`](#insn-00bbee54) 範囲 `[['00bbee54', '00bbee57']]`
  - `COMPUTED_JUMP` [`00bbee54`](#insn-00bbee54) → [`00bbee58`](#insn-00bbee58)
  - `COMPUTED_JUMP` [`00bbee54`](#insn-00bbee54) → [`00bbee70`](#insn-00bbee70)
  - `COMPUTED_JUMP` [`00bbee54`](#insn-00bbee54) → [`00bbee88`](#insn-00bbee88)
  - `COMPUTED_JUMP` [`00bbee54`](#insn-00bbee54) → [`00bbeea0`](#insn-00bbeea0)
- ブロック [`00bbee58`](#insn-00bbee58) 範囲 `[['00bbee58', '00bbee5b']]`
  - `CONDITIONAL_JUMP` [`00bbee58`](#insn-00bbee58) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbee58`](#insn-00bbee58) → [`00bbee5c`](#insn-00bbee5c)
- ブロック [`00bbee5c`](#insn-00bbee5c) 範囲 `[['00bbee5c', '00bbee6b']]`
  - `CONDITIONAL_JUMP` [`00bbee68`](#insn-00bbee68) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbee68`](#insn-00bbee68) → [`00bbee6c`](#insn-00bbee6c)
- ブロック [`00bbee6c`](#insn-00bbee6c) 範囲 `[['00bbee6c', '00bbee6f']]`
  - `UNCONDITIONAL_JUMP` [`00bbee6c`](#insn-00bbee6c) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbee70`](#insn-00bbee70) 範囲 `[['00bbee70', '00bbee73']]`
  - `CONDITIONAL_JUMP` [`00bbee70`](#insn-00bbee70) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbee70`](#insn-00bbee70) → [`00bbee74`](#insn-00bbee74)
- ブロック [`00bbee74`](#insn-00bbee74) 範囲 `[['00bbee74', '00bbee83']]`
  - `CONDITIONAL_JUMP` [`00bbee80`](#insn-00bbee80) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbee80`](#insn-00bbee80) → [`00bbee84`](#insn-00bbee84)
- ブロック [`00bbee84`](#insn-00bbee84) 範囲 `[['00bbee84', '00bbee87']]`
  - `UNCONDITIONAL_JUMP` [`00bbee84`](#insn-00bbee84) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbee88`](#insn-00bbee88) 範囲 `[['00bbee88', '00bbee8b']]`
  - `CONDITIONAL_JUMP` [`00bbee88`](#insn-00bbee88) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbee88`](#insn-00bbee88) → [`00bbee8c`](#insn-00bbee8c)
- ブロック [`00bbee8c`](#insn-00bbee8c) 範囲 `[['00bbee8c', '00bbee9b']]`
  - `CONDITIONAL_JUMP` [`00bbee98`](#insn-00bbee98) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbee98`](#insn-00bbee98) → [`00bbee9c`](#insn-00bbee9c)
- ブロック [`00bbee9c`](#insn-00bbee9c) 範囲 `[['00bbee9c', '00bbee9f']]`
  - `UNCONDITIONAL_JUMP` [`00bbee9c`](#insn-00bbee9c) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbeea0`](#insn-00bbeea0) 範囲 `[['00bbeea0', '00bbeea3']]`
  - `CONDITIONAL_JUMP` [`00bbeea0`](#insn-00bbeea0) → [`00bbeeb4`](#insn-00bbeeb4)
  - `FALL_THROUGH` [`00bbeea0`](#insn-00bbeea0) → [`00bbeea4`](#insn-00bbeea4)
- ブロック [`00bbeea4`](#insn-00bbeea4) 範囲 `[['00bbeea4', '00bbeeb3']]`
  - `CONDITIONAL_JUMP` [`00bbeeb0`](#insn-00bbeeb0) → [`00bbed98`](#insn-00bbed98)
  - `FALL_THROUGH` [`00bbeeb0`](#insn-00bbeeb0) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbeeb4`](#insn-00bbeeb4) 範囲 `[['00bbeeb4', '00bbeec7']]`
  - `UNCONDITIONAL_JUMP` [`00bbeec4`](#insn-00bbeec4) → [`00bbed9c`](#insn-00bbed9c)

## 命令位置別の参照

- [`00bbecb8`](#insn-00bbecb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecbc`](#insn-00bbecbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecd4`](#insn-00bbecd4) → [`00bbece0`](#insn-00bbece0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecdc`](#insn-00bbecdc) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecec`](#insn-00bbecec) → [`00bbed9c`](#insn-00bbed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecf8`](#insn-00bbecf8) → [`00bbed9c`](#insn-00bbed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed18`](#insn-00bbed18) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed24`](#insn-00bbed24) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed2c`](#insn-00bbed2c) → [`00bbed38`](#insn-00bbed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed34`](#insn-00bbed34) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed40`](#insn-00bbed40) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed48`](#insn-00bbed48) → [`00bbed54`](#insn-00bbed54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed50`](#insn-00bbed50) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed54`](#insn-00bbed54) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed60`](#insn-00bbed60) → [`00bbed9c`](#insn-00bbed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → [`00bbed9c`](#insn-00bbed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed7c`](#insn-00bbed7c) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbed84`](#insn-00bbed84) → [`00bbedac`](#insn-00bbedac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed94`](#insn-00bbed94) → [`00bbedac`](#insn-00bbedac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed9c`](#insn-00bbed9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb0`](#insn-00bbedb0) → [`00bbede0`](#insn-00bbede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb8`](#insn-00bbedb8) → [`00bbee14`](#insn-00bbee14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedc4`](#insn-00bbedc4) → [`00bbedf0`](#insn-00bbedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedd0`](#insn-00bbedd0) → [`00bbed9c`](#insn-00bbed9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedd8`](#insn-00bbedd8) → [`00bbedf8`](#insn-00bbedf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeddc`](#insn-00bbeddc) → [`00bbed9c`](#insn-00bbed9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbede8`](#insn-00bbede8) → [`00bbee30`](#insn-00bbee30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedec`](#insn-00bbedec) → [`00bbeeb4`](#insn-00bbeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbedf4`](#insn-00bbedf4) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee00`](#insn-00bbee00) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee10`](#insn-00bbee10) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee18`](#insn-00bbee18) → [`00bbee28`](#insn-00bbee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee2c`](#insn-00bbee2c) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee3c`](#insn-00bbee3c) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee4c`](#insn-00bbee4c) → `0030e8e4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbee54::switchdataD_0030e8e4` · 推定型 `byte`
- [`00bbee54`](#insn-00bbee54) → [`00bbee58`](#insn-00bbee58) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbee54::caseD_1` · 推定型 `None`
- [`00bbee54`](#insn-00bbee54) → [`00bbee70`](#insn-00bbee70) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbee54::caseD_2` · 推定型 `None`
- [`00bbee54`](#insn-00bbee54) → [`00bbee88`](#insn-00bbee88) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbee54::caseD_3` · 推定型 `None`
- [`00bbee54`](#insn-00bbee54) → [`00bbeea0`](#insn-00bbeea0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbee54::caseD_4` · 推定型 `None`
- [`00bbee58`](#insn-00bbee58) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee64`](#insn-00bbee64) → [`00c5d5b0`](../00c5d/00c5d5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbee68`](#insn-00bbee68) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee6c`](#insn-00bbee6c) → [`00bbeeb4`](#insn-00bbeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee70`](#insn-00bbee70) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee7c`](#insn-00bbee7c) → [`00c5d5d0`](../00c5d/00c5d5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbee80`](#insn-00bbee80) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee84`](#insn-00bbee84) → [`00bbeeb4`](#insn-00bbeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee88`](#insn-00bbee88) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbee94`](#insn-00bbee94) → [`00c5d5e0`](../00c5d/00c5d5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbee98`](#insn-00bbee98) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee9c`](#insn-00bbee9c) → [`00bbeeb4`](#insn-00bbeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbeea0`](#insn-00bbeea0) → [`00bbeeb4`](#insn-00bbeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbee54::default` · 推定型 `None`
- [`00bbeeac`](#insn-00bbeeac) → [`00c5d5f0`](../00c5d/00c5d5f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbeeb0`](#insn-00bbeeb0) → [`00bbed98`](#insn-00bbed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeec4`](#insn-00bbeec4) → [`00bbed9c`](#insn-00bbed9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbecb8`](#insn-00bbecb8)

~~~json
{
  "source": "00bbecb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecbc`](#insn-00bbecbc)

~~~json
{
  "source": "00bbecbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecd4`](#insn-00bbecd4)

~~~json
{
  "source": "00bbecd4",
  "target": "00bbece0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecdc`](#insn-00bbecdc)

~~~json
{
  "source": "00bbecdc",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecec`](#insn-00bbecec)

~~~json
{
  "source": "00bbecec",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecf8`](#insn-00bbecf8)

~~~json
{
  "source": "00bbecf8",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed18`](#insn-00bbed18)

~~~json
{
  "source": "00bbed18",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed24`](#insn-00bbed24)

~~~json
{
  "source": "00bbed24",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed2c`](#insn-00bbed2c)

~~~json
{
  "source": "00bbed2c",
  "target": "00bbed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed34`](#insn-00bbed34)

~~~json
{
  "source": "00bbed34",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed40`](#insn-00bbed40)

~~~json
{
  "source": "00bbed40",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed48`](#insn-00bbed48)

~~~json
{
  "source": "00bbed48",
  "target": "00bbed54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed50`](#insn-00bbed50)

~~~json
{
  "source": "00bbed50",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed54`](#insn-00bbed54)

~~~json
{
  "source": "00bbed54",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed60`](#insn-00bbed60)

~~~json
{
  "source": "00bbed60",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed7c`](#insn-00bbed7c)

~~~json
{
  "source": "00bbed7c",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed84`](#insn-00bbed84)

~~~json
{
  "source": "00bbed84",
  "target": "00bbedac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed94`](#insn-00bbed94)

~~~json
{
  "source": "00bbed94",
  "target": "00bbedac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed9c`](#insn-00bbed9c)

~~~json
{
  "source": "00bbed9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb0`](#insn-00bbedb0)

~~~json
{
  "source": "00bbedb0",
  "target": "00bbede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "00bbee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedc4`](#insn-00bbedc4)

~~~json
{
  "source": "00bbedc4",
  "target": "00bbedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedd0`](#insn-00bbedd0)

~~~json
{
  "source": "00bbedd0",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedd8`](#insn-00bbedd8)

~~~json
{
  "source": "00bbedd8",
  "target": "00bbedf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeddc`](#insn-00bbeddc)

~~~json
{
  "source": "00bbeddc",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede8`](#insn-00bbede8)

~~~json
{
  "source": "00bbede8",
  "target": "00bbee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedec`](#insn-00bbedec)

~~~json
{
  "source": "00bbedec",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedf4`](#insn-00bbedf4)

~~~json
{
  "source": "00bbedf4",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee00`](#insn-00bbee00)

~~~json
{
  "source": "00bbee00",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee10`](#insn-00bbee10)

~~~json
{
  "source": "00bbee10",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee18`](#insn-00bbee18)

~~~json
{
  "source": "00bbee18",
  "target": "00bbee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee2c`](#insn-00bbee2c)

~~~json
{
  "source": "00bbee2c",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee3c`](#insn-00bbee3c)

~~~json
{
  "source": "00bbee3c",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee4c`](#insn-00bbee4c)

~~~json
{
  "source": "00bbee4c",
  "target": "0030e8e4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8e4",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e8e4",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbee54`](#insn-00bbee54)

~~~json
{
  "source": "00bbee54",
  "target": "00bbee58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee54`](#insn-00bbee54)

~~~json
{
  "source": "00bbee54",
  "target": "00bbee70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee54`](#insn-00bbee54)

~~~json
{
  "source": "00bbee54",
  "target": "00bbee88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee54`](#insn-00bbee54)

~~~json
{
  "source": "00bbee54",
  "target": "00bbeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee58`](#insn-00bbee58)

~~~json
{
  "source": "00bbee58",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee64`](#insn-00bbee64)

~~~json
{
  "source": "00bbee64",
  "target": "00c5d5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee68`](#insn-00bbee68)

~~~json
{
  "source": "00bbee68",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee6c`](#insn-00bbee6c)

~~~json
{
  "source": "00bbee6c",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee70`](#insn-00bbee70)

~~~json
{
  "source": "00bbee70",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee7c`](#insn-00bbee7c)

~~~json
{
  "source": "00bbee7c",
  "target": "00c5d5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee80`](#insn-00bbee80)

~~~json
{
  "source": "00bbee80",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee84`](#insn-00bbee84)

~~~json
{
  "source": "00bbee84",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee88`](#insn-00bbee88)

~~~json
{
  "source": "00bbee88",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee94`](#insn-00bbee94)

~~~json
{
  "source": "00bbee94",
  "target": "00c5d5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee98`](#insn-00bbee98)

~~~json
{
  "source": "00bbee98",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee9c`](#insn-00bbee9c)

~~~json
{
  "source": "00bbee9c",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeea0`](#insn-00bbeea0)

~~~json
{
  "source": "00bbeea0",
  "target": "00bbeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeeac`](#insn-00bbeeac)

~~~json
{
  "source": "00bbeeac",
  "target": "00c5d5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeeb0`](#insn-00bbeeb0)

~~~json
{
  "source": "00bbeeb0",
  "target": "00bbed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeec4`](#insn-00bbeec4)

~~~json
{
  "source": "00bbeec4",
  "target": "00bbed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
