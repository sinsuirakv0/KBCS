# 00bbec1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbe7f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe7f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-fefcc007cee7a3596602cc8c592f930d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbecb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-eb028551d2f0c83cc08a3a0d2f1fdcf5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbec1c",
  "name": "_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f6c991895324170b30393fbc8d2252b7fb67f139b1ea9400d82fef6025df0bb",
  "source_text_sha256": "6f6c991895324170b30393fbc8d2252b7fb67f139b1ea9400d82fef6025df0bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbec1c",
        "00bbee2b"
      ]
    ],
    "bytes_sha256": "84533ca61bd6a4eaea70866404f855e6915727423f49e9a6831fb0785a457eda",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d4d0](../00c5d/00c5d4d0.md)

## 呼び出し先

- [00c5d4e0](../00c5d/00c5d4e0.md)
- [00c5d500](../00c5d/00c5d500.md)
- [00c5d510](../00c5d/00c5d510.md)
- [00c5d520](../00c5d/00c5d520.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4496 bytes

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
                    /* try { // try from 00bbec2c to 00cbec3b has its CatchHandler @ 00bbf3e0 */
  uVar8 = (long)param_1 - lVar6;
                    /* try { // try from 00bbec3c to 00cbec43 has its CatchHandler @ 00bbf3a0 */
  if (((uVar8 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar7 = param_2[1];
    if (uVar7 < 5) {
      return 0;
    }
    uVar9 = uVar7 - 4;
    if (uVar9 < uVar8) {
      return 0;
    }
    iVar5 = *param_1;
                    /* try { // try from 00bbec6c to 00cbec87 has its CatchHandler @ 00bbf3b0 */
    uVar1 = (int)param_2[7] + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
                    /* try { // try from 00bbec88 to 00cbed33 has its CatchHandler @ 00bbe7f8 */
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
              if ((uVar8 & 3) == 0) {
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              else {
                    /* try { // try from 00bbed34 to 00cbed4f has its CatchHandler @ 00bbf3b8 */
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
              if (lVar6 == 0) goto switchD_00bbedb8_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 2:
              if (lVar6 == 0) goto switchD_00bbedb8_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 3:
              if (lVar6 == 0) goto switchD_00bbedb8_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp30SerializedRegistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 4:
              if (lVar6 == 0) goto switchD_00bbedb8_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            default:
              goto switchD_00bbedb8_default;
            }
            if ((uVar8 & 1) == 0) {
              return 0;
            }
          }
        }
switchD_00bbedb8_default:
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbec1c"></a> `00bbec1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbec20"></a> `00bbec20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbec24"></a> `00bbec24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbec28"></a> `00bbec28` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bbec2c"></a> `00bbec2c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbec30"></a> `00bbec30` | `0b 00 09 cb` | sub x11,x0,x9 | `FALL_THROUGH`
<a id="insn-00bbec34"></a> `00bbec34` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbec38"></a> `00bbec38` | `60 00 00 54` | b.eq 0x00bbec44 | `CONDITIONAL_JUMP`
<a id="insn-00bbec3c"></a> `00bbec3c` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbec40"></a> `00bbec40` | `e8 05 00 35` | cbnz w8,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec44"></a> `00bbec44` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec48"></a> `00bbec48` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbec4c"></a> `00bbec4c` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbec50"></a> `00bbec50` | `83 05 00 54` | b.cc 0x00bbed00 | `CONDITIONAL_JUMP`
<a id="insn-00bbec54"></a> `00bbec54` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbec58"></a> `00bbec58` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbec5c"></a> `00bbec5c` | `23 05 00 54` | b.cc 0x00bbed00 | `CONDITIONAL_JUMP`
<a id="insn-00bbec60"></a> `00bbec60` | `6d 3a 47 29` | ldp w13,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbec64"></a> `00bbec64` | `6f 12 40 b9` | ldr w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbec68"></a> `00bbec68` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbec6c"></a> `00bbec6c` | `b0 05 00 11` | add w16,w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bbec70"></a> `00bbec70` | `cd 05 00 11` | add w13,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbec74"></a> `00bbec74` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbec78"></a> `00bbec78` | `70 36 07 29` | stp w16,w13,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbec7c"></a> `00bbec7c` | `08 04 00 54` | b.hi 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec80"></a> `00bbec80` | `6e 16 40 b9` | ldr w14,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00bbec84"></a> `00bbec84` | `bf 01 0e 6b` | cmp w13,w14 | `FALL_THROUGH`
<a id="insn-00bbec88"></a> `00bbec88` | `a8 03 00 54` | b.hi 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec8c"></a> `00bbec8c` | `6d 01 08 cb` | sub x13,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbec90"></a> `00bbec90` | `6d 00 00 36` | tbz w13,#0x0,0x00bbec9c | `CONDITIONAL_JUMP`
<a id="insn-00bbec94"></a> `00bbec94` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbec98"></a> `00bbec98` | `28 03 00 35` | cbnz w8,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbec9c"></a> `00bbec9c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbeca0"></a> `00bbeca0` | `1f 01 0d eb` | cmp x8,x13 | `FALL_THROUGH`
<a id="insn-00bbeca4"></a> `00bbeca4` | `c3 02 00 54` | b.cc 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbeca8"></a> `00bbeca8` | `28 69 6d 78` | ldrh w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbecac"></a> `00bbecac` | `68 00 00 36` | tbz w8,#0x0,0x00bbecb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbecb0"></a> `00bbecb0` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbecb4"></a> `00bbecb4` | `4e 02 00 35` | cbnz w14,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbecb8"></a> `00bbecb8` | `28 02 00 37` | tbnz w8,#0x0,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbecbc"></a> `00bbecbc` | `4e 01 08 eb` | subs x14,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbecc0"></a> `00bbecc0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbecc4"></a> `00bbecc4` | `e9 01 00 54` | b.ls 0x00bbed00 | `CONDITIONAL_JUMP`
<a id="insn-00bbecc8"></a> `00bbecc8` | `df 01 0d eb` | cmp x14,x13 | `FALL_THROUGH`
<a id="insn-00bbeccc"></a> `00bbeccc` | `a3 01 00 54` | b.cc 0x00bbed00 | `CONDITIONAL_JUMP`
<a id="insn-00bbecd0"></a> `00bbecd0` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbecd4"></a> `00bbecd4` | `0d 00 08 cb` | sub x13,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbecd8"></a> `00bbecd8` | `a8 01 40 79` | ldrh w8,[x13] | `FALL_THROUGH`
<a id="insn-00bbecdc"></a> `00bbecdc` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbece0"></a> `00bbece0` | `c3 09 00 54` | b.cc 0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbece4"></a> `00bbece4` | `ae 09 40 79` | ldrh w14,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbece8"></a> `00bbece8` | `4e 01 00 b4` | cbz x14,0x00bbed10 | `CONDITIONAL_JUMP`
<a id="insn-00bbecec"></a> `00bbecec` | `6e 01 0e 8b` | add x14,x11,x14 | `FALL_THROUGH`
<a id="insn-00bbecf0"></a> `00bbecf0` | `4f 05 00 d1` | sub x15,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbecf4"></a> `00bbecf4` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbecf8"></a> `00bbecf8` | `c2 00 00 54` | b.cs 0x00bbed10 | `CONDITIONAL_JUMP`
<a id="insn-00bbecfc"></a> `00bbecfc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbed00"></a> `00bbed00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbed04"></a> `00bbed04` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bbed08"></a> `00bbed08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbed0c"></a> `00bbed0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbed10"></a> `00bbed10` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-00bbed14"></a> `00bbed14` | `83 01 00 54` | b.cc 0x00bbed44 | `CONDITIONAL_JUMP`
<a id="insn-00bbed18"></a> `00bbed18` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbed1c"></a> `00bbed1c` | `e8 02 00 b4` | cbz x8,0x00bbed78 | `CONDITIONAL_JUMP`
<a id="insn-00bbed20"></a> `00bbed20` | `6b 01 08 8b` | add x11,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbed24"></a> `00bbed24` | `7f 05 40 f2` | tst x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bbed28"></a> `00bbed28` | `60 01 00 54` | b.eq 0x00bbed54 | `CONDITIONAL_JUMP`
<a id="insn-00bbed2c"></a> `00bbed2c` | `6e 62 40 39` | ldrb w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbed30"></a> `00bbed30` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbed34"></a> `00bbed34` | `6e fe ff 35` | cbnz w14,0x00bbed00 | `CONDITIONAL_JUMP`
<a id="insn-00bbed38"></a> `00bbed38` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbed3c"></a> `00bbed3c` | `02 01 00 54` | b.cs 0x00bbed5c | `CONDITIONAL_JUMP`
<a id="insn-00bbed40"></a> `00bbed40` | `f0 ff ff 17` | b 0x00bbed00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbed44"></a> `00bbed44` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbed48"></a> `00bbed48` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbed4c"></a> `00bbed4c` | `49 02 00 b5` | cbnz x9,0x00bbed94 | `CONDITIONAL_JUMP`
<a id="insn-00bbed50"></a> `00bbed50` | `32 00 00 14` | b 0x00bbee18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbed54"></a> `00bbed54` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bbed58"></a> `00bbed58` | `23 fd ff 54` | b.cc 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbed5c"></a> `00bbed5c` | `28 69 6b b8` | ldr w8,[x9, x11, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbed60"></a> `00bbed60` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed64"></a> `00bbed64` | `cb fc ff 54` | b.lt 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbed68"></a> `00bbed68` | `68 01 08 8b` | add x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00bbed6c"></a> `00bbed6c` | `49 05 00 d1` | sub x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed70"></a> `00bbed70` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbed74"></a> `00bbed74` | `43 fc ff 54` | b.cc 0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbed78"></a> `00bbed78` | `a8 0d 40 79` | ldrh w8,[x13, #0x6] | `FALL_THROUGH`
<a id="insn-00bbed7c"></a> `00bbed7c` | `88 00 00 b4` | cbz x8,0x00bbed8c | `CONDITIONAL_JUMP`
<a id="insn-00bbed80"></a> `00bbed80` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbed84"></a> `00bbed84` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbed88"></a> `00bbed88` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbed8c"></a> `00bbed8c` | `a9 09 40 79` | ldrh w9,[x13, #0x4] | `FALL_THROUGH`
<a id="insn-00bbed90"></a> `00bbed90` | `49 04 00 b4` | cbz x9,0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbed94"></a> `00bbed94` | `09 68 69 38` | ldrb w9,[x0, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbed98"></a> `00bbed98` | `29 05 00 51` | sub w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbed9c"></a> `00bbed9c` | `3f 0d 00 71` | cmp w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bbeda0"></a> `00bbeda0` | `c8 03 00 54` | b.hi 0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbeda4"></a> `00bbeda4` | `8a ba ff 90` | adrp x10,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbeda8"></a> `00bbeda8` | `4a 91 22 91` | add x10,x10,#0x8a4 | `FALL_THROUGH`
<a id="insn-00bbedac"></a> `00bbedac` | `8b 00 00 10` | adr x11,0xbbedbc | `FALL_THROUGH`
<a id="insn-00bbedb0"></a> `00bbedb0` | `4c 69 69 38` | ldrb w12,[x10, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bbedb4"></a> `00bbedb4` | `6b 09 0c 8b` | add x11,x11,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbedb8"></a> `00bbedb8` | `60 01 1f d6` | br x11 | `COMPUTED_JUMP`
<a id="insn-00bbedbc"></a> `00bbedbc` | `e8 02 00 b4` | cbz x8,0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbedc0"></a> `00bbedc0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbedc4"></a> `00bbedc4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbedc8"></a> `00bbedc8` | `c6 79 02 94` | bl 0x00c5d4e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedcc"></a> `00bbedcc` | `80 f9 07 36` | tbz w0,#0x0,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbedd0"></a> `00bbedd0` | `12 00 00 14` | b 0x00bbee18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbedd4"></a> `00bbedd4` | `28 02 00 b4` | cbz x8,0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbedd8"></a> `00bbedd8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbeddc"></a> `00bbeddc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbede0"></a> `00bbede0` | `c8 79 02 94` | bl 0x00c5d500 | `UNCONDITIONAL_CALL`
<a id="insn-00bbede4"></a> `00bbede4` | `c0 f8 07 36` | tbz w0,#0x0,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbede8"></a> `00bbede8` | `0c 00 00 14` | b 0x00bbee18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbedec"></a> `00bbedec` | `68 01 00 b4` | cbz x8,0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbedf0"></a> `00bbedf0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbedf4"></a> `00bbedf4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbedf8"></a> `00bbedf8` | `c6 79 02 94` | bl 0x00c5d510 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedfc"></a> `00bbedfc` | `00 f8 07 36` | tbz w0,#0x0,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbee00"></a> `00bbee00` | `06 00 00 14` | b 0x00bbee18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbee04"></a> `00bbee04` | `a8 00 00 b4` | cbz x8,0x00bbee18 | `CONDITIONAL_JUMP`
<a id="insn-00bbee08"></a> `00bbee08` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbee0c"></a> `00bbee0c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbee10"></a> `00bbee10` | `c4 79 02 94` | bl 0x00c5d520 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee14"></a> `00bbee14` | `40 f7 07 36` | tbz w0,#0x0,0x00bbecfc | `CONDITIONAL_JUMP`
<a id="insn-00bbee18"></a> `00bbee18` | `68 3a 40 b9` | ldr w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbee1c"></a> `00bbee1c` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee20"></a> `00bbee20` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bbee24"></a> `00bbee24` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee28"></a> `00bbee28` | `b6 ff ff 17` | b 0x00bbed00 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbec1c`](#insn-00bbec1c) 範囲 `[['00bbec1c', '00bbec2b']]`
  - `FALL_THROUGH` [`00bbec28`](#insn-00bbec28) → [`00bbec2c`](#insn-00bbec2c)
- ブロック [`00bbec2c`](#insn-00bbec2c) 範囲 `[['00bbec2c', '00bbec3b']]`
  - `CONDITIONAL_JUMP` [`00bbec38`](#insn-00bbec38) → [`00bbec44`](#insn-00bbec44)
  - `FALL_THROUGH` [`00bbec38`](#insn-00bbec38) → [`00bbec3c`](#insn-00bbec3c)
- ブロック [`00bbec3c`](#insn-00bbec3c) 範囲 `[['00bbec3c', '00bbec43']]`
  - `CONDITIONAL_JUMP` [`00bbec40`](#insn-00bbec40) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbec40`](#insn-00bbec40) → [`00bbec44`](#insn-00bbec44)
- ブロック [`00bbec44`](#insn-00bbec44) 範囲 `[['00bbec44', '00bbec53']]`
  - `CONDITIONAL_JUMP` [`00bbec50`](#insn-00bbec50) → [`00bbed00`](#insn-00bbed00)
  - `FALL_THROUGH` [`00bbec50`](#insn-00bbec50) → [`00bbec54`](#insn-00bbec54)
- ブロック [`00bbec54`](#insn-00bbec54) 範囲 `[['00bbec54', '00bbec5f']]`
  - `CONDITIONAL_JUMP` [`00bbec5c`](#insn-00bbec5c) → [`00bbed00`](#insn-00bbed00)
  - `FALL_THROUGH` [`00bbec5c`](#insn-00bbec5c) → [`00bbec60`](#insn-00bbec60)
- ブロック [`00bbec60`](#insn-00bbec60) 範囲 `[['00bbec60', '00bbec6b']]`
  - `FALL_THROUGH` [`00bbec68`](#insn-00bbec68) → [`00bbec6c`](#insn-00bbec6c)
- ブロック [`00bbec6c`](#insn-00bbec6c) 範囲 `[['00bbec6c', '00bbec7f']]`
  - `CONDITIONAL_JUMP` [`00bbec7c`](#insn-00bbec7c) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbec7c`](#insn-00bbec7c) → [`00bbec80`](#insn-00bbec80)
- ブロック [`00bbec80`](#insn-00bbec80) 範囲 `[['00bbec80', '00bbec87']]`
  - `FALL_THROUGH` [`00bbec84`](#insn-00bbec84) → [`00bbec88`](#insn-00bbec88)
- ブロック [`00bbec88`](#insn-00bbec88) 範囲 `[['00bbec88', '00bbec8b']]`
  - `CONDITIONAL_JUMP` [`00bbec88`](#insn-00bbec88) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbec88`](#insn-00bbec88) → [`00bbec8c`](#insn-00bbec8c)
- ブロック [`00bbec8c`](#insn-00bbec8c) 範囲 `[['00bbec8c', '00bbec93']]`
  - `CONDITIONAL_JUMP` [`00bbec90`](#insn-00bbec90) → [`00bbec9c`](#insn-00bbec9c)
  - `FALL_THROUGH` [`00bbec90`](#insn-00bbec90) → [`00bbec94`](#insn-00bbec94)
- ブロック [`00bbec94`](#insn-00bbec94) 範囲 `[['00bbec94', '00bbec9b']]`
  - `CONDITIONAL_JUMP` [`00bbec98`](#insn-00bbec98) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbec98`](#insn-00bbec98) → [`00bbec9c`](#insn-00bbec9c)
- ブロック [`00bbec9c`](#insn-00bbec9c) 範囲 `[['00bbec9c', '00bbeca7']]`
  - `CONDITIONAL_JUMP` [`00bbeca4`](#insn-00bbeca4) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbeca4`](#insn-00bbeca4) → [`00bbeca8`](#insn-00bbeca8)
- ブロック [`00bbeca8`](#insn-00bbeca8) 範囲 `[['00bbeca8', '00bbecaf']]`
  - `CONDITIONAL_JUMP` [`00bbecac`](#insn-00bbecac) → [`00bbecb8`](#insn-00bbecb8)
  - `FALL_THROUGH` [`00bbecac`](#insn-00bbecac) → [`00bbecb0`](#insn-00bbecb0)
- ブロック [`00bbecb0`](#insn-00bbecb0) 範囲 `[['00bbecb0', '00bbecb7']]`
  - `CONDITIONAL_JUMP` [`00bbecb4`](#insn-00bbecb4) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbecb4`](#insn-00bbecb4) → [`00bbecb8`](#insn-00bbecb8)
- ブロック [`00bbecb8`](#insn-00bbecb8) 範囲 `[['00bbecb8', '00bbecbb']]`
  - `CONDITIONAL_JUMP` [`00bbecb8`](#insn-00bbecb8) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbecb8`](#insn-00bbecb8) → [`00bbecbc`](#insn-00bbecbc)
- ブロック [`00bbecbc`](#insn-00bbecbc) 範囲 `[['00bbecbc', '00bbecc7']]`
  - `CONDITIONAL_JUMP` [`00bbecc4`](#insn-00bbecc4) → [`00bbed00`](#insn-00bbed00)
  - `FALL_THROUGH` [`00bbecc4`](#insn-00bbecc4) → [`00bbecc8`](#insn-00bbecc8)
- ブロック [`00bbecc8`](#insn-00bbecc8) 範囲 `[['00bbecc8', '00bbeccf']]`
  - `CONDITIONAL_JUMP` [`00bbeccc`](#insn-00bbeccc) → [`00bbed00`](#insn-00bbed00)
  - `FALL_THROUGH` [`00bbeccc`](#insn-00bbeccc) → [`00bbecd0`](#insn-00bbecd0)
- ブロック [`00bbecd0`](#insn-00bbecd0) 範囲 `[['00bbecd0', '00bbece3']]`
  - `CONDITIONAL_JUMP` [`00bbece0`](#insn-00bbece0) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbece0`](#insn-00bbece0) → [`00bbece4`](#insn-00bbece4)
- ブロック [`00bbece4`](#insn-00bbece4) 範囲 `[['00bbece4', '00bbeceb']]`
  - `CONDITIONAL_JUMP` [`00bbece8`](#insn-00bbece8) → [`00bbed10`](#insn-00bbed10)
  - `FALL_THROUGH` [`00bbece8`](#insn-00bbece8) → [`00bbecec`](#insn-00bbecec)
- ブロック [`00bbecec`](#insn-00bbecec) 範囲 `[['00bbecec', '00bbecfb']]`
  - `CONDITIONAL_JUMP` [`00bbecf8`](#insn-00bbecf8) → [`00bbed10`](#insn-00bbed10)
  - `FALL_THROUGH` [`00bbecf8`](#insn-00bbecf8) → [`00bbecfc`](#insn-00bbecfc)
- ブロック [`00bbecfc`](#insn-00bbecfc) 範囲 `[['00bbecfc', '00bbecff']]`
  - `FALL_THROUGH` [`00bbecfc`](#insn-00bbecfc) → [`00bbed00`](#insn-00bbed00)
- ブロック [`00bbed00`](#insn-00bbed00) 範囲 `[['00bbed00', '00bbed0f']]`
- ブロック [`00bbed10`](#insn-00bbed10) 範囲 `[['00bbed10', '00bbed17']]`
  - `CONDITIONAL_JUMP` [`00bbed14`](#insn-00bbed14) → [`00bbed44`](#insn-00bbed44)
  - `FALL_THROUGH` [`00bbed14`](#insn-00bbed14) → [`00bbed18`](#insn-00bbed18)
- ブロック [`00bbed18`](#insn-00bbed18) 範囲 `[['00bbed18', '00bbed1f']]`
  - `CONDITIONAL_JUMP` [`00bbed1c`](#insn-00bbed1c) → [`00bbed78`](#insn-00bbed78)
  - `FALL_THROUGH` [`00bbed1c`](#insn-00bbed1c) → [`00bbed20`](#insn-00bbed20)
- ブロック [`00bbed20`](#insn-00bbed20) 範囲 `[['00bbed20', '00bbed2b']]`
  - `CONDITIONAL_JUMP` [`00bbed28`](#insn-00bbed28) → [`00bbed54`](#insn-00bbed54)
  - `FALL_THROUGH` [`00bbed28`](#insn-00bbed28) → [`00bbed2c`](#insn-00bbed2c)
- ブロック [`00bbed2c`](#insn-00bbed2c) 範囲 `[['00bbed2c', '00bbed33']]`
  - `FALL_THROUGH` [`00bbed30`](#insn-00bbed30) → [`00bbed34`](#insn-00bbed34)
- ブロック [`00bbed34`](#insn-00bbed34) 範囲 `[['00bbed34', '00bbed37']]`
  - `CONDITIONAL_JUMP` [`00bbed34`](#insn-00bbed34) → [`00bbed00`](#insn-00bbed00)
  - `FALL_THROUGH` [`00bbed34`](#insn-00bbed34) → [`00bbed38`](#insn-00bbed38)
- ブロック [`00bbed38`](#insn-00bbed38) 範囲 `[['00bbed38', '00bbed3f']]`
  - `CONDITIONAL_JUMP` [`00bbed3c`](#insn-00bbed3c) → [`00bbed5c`](#insn-00bbed5c)
  - `FALL_THROUGH` [`00bbed3c`](#insn-00bbed3c) → [`00bbed40`](#insn-00bbed40)
- ブロック [`00bbed40`](#insn-00bbed40) 範囲 `[['00bbed40', '00bbed43']]`
  - `UNCONDITIONAL_JUMP` [`00bbed40`](#insn-00bbed40) → [`00bbed00`](#insn-00bbed00)
- ブロック [`00bbed44`](#insn-00bbed44) 範囲 `[['00bbed44', '00bbed4f']]`
  - `CONDITIONAL_JUMP` [`00bbed4c`](#insn-00bbed4c) → [`00bbed94`](#insn-00bbed94)
  - `FALL_THROUGH` [`00bbed4c`](#insn-00bbed4c) → [`00bbed50`](#insn-00bbed50)
- ブロック [`00bbed50`](#insn-00bbed50) 範囲 `[['00bbed50', '00bbed53']]`
  - `UNCONDITIONAL_JUMP` [`00bbed50`](#insn-00bbed50) → [`00bbee18`](#insn-00bbee18)
- ブロック [`00bbed54`](#insn-00bbed54) 範囲 `[['00bbed54', '00bbed5b']]`
  - `CONDITIONAL_JUMP` [`00bbed58`](#insn-00bbed58) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbed58`](#insn-00bbed58) → [`00bbed5c`](#insn-00bbed5c)
- ブロック [`00bbed5c`](#insn-00bbed5c) 範囲 `[['00bbed5c', '00bbed67']]`
  - `CONDITIONAL_JUMP` [`00bbed64`](#insn-00bbed64) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbed64`](#insn-00bbed64) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbed68`](#insn-00bbed68) 範囲 `[['00bbed68', '00bbed77']]`
  - `CONDITIONAL_JUMP` [`00bbed74`](#insn-00bbed74) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbed74`](#insn-00bbed74) → [`00bbed78`](#insn-00bbed78)
- ブロック [`00bbed78`](#insn-00bbed78) 範囲 `[['00bbed78', '00bbed7f']]`
  - `CONDITIONAL_JUMP` [`00bbed7c`](#insn-00bbed7c) → [`00bbed8c`](#insn-00bbed8c)
  - `FALL_THROUGH` [`00bbed7c`](#insn-00bbed7c) → [`00bbed80`](#insn-00bbed80)
- ブロック [`00bbed80`](#insn-00bbed80) 範囲 `[['00bbed80', '00bbed8b']]`
  - `FALL_THROUGH` [`00bbed88`](#insn-00bbed88) → [`00bbed8c`](#insn-00bbed8c)
- ブロック [`00bbed8c`](#insn-00bbed8c) 範囲 `[['00bbed8c', '00bbed93']]`
  - `CONDITIONAL_JUMP` [`00bbed90`](#insn-00bbed90) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbed90`](#insn-00bbed90) → [`00bbed94`](#insn-00bbed94)
- ブロック [`00bbed94`](#insn-00bbed94) 範囲 `[['00bbed94', '00bbeda3']]`
  - `CONDITIONAL_JUMP` [`00bbeda0`](#insn-00bbeda0) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbeda0`](#insn-00bbeda0) → [`00bbeda4`](#insn-00bbeda4)
- ブロック [`00bbeda4`](#insn-00bbeda4) 範囲 `[['00bbeda4', '00bbedb7']]`
  - `FALL_THROUGH` [`00bbedb4`](#insn-00bbedb4) → [`00bbedb8`](#insn-00bbedb8)
- ブロック [`00bbedb8`](#insn-00bbedb8) 範囲 `[['00bbedb8', '00bbedbb']]`
  - `COMPUTED_JUMP` [`00bbedb8`](#insn-00bbedb8) → [`00bbedbc`](#insn-00bbedbc)
  - `COMPUTED_JUMP` [`00bbedb8`](#insn-00bbedb8) → [`00bbedd4`](#insn-00bbedd4)
  - `COMPUTED_JUMP` [`00bbedb8`](#insn-00bbedb8) → [`00bbedec`](#insn-00bbedec)
  - `COMPUTED_JUMP` [`00bbedb8`](#insn-00bbedb8) → [`00bbee04`](#insn-00bbee04)
- ブロック [`00bbedbc`](#insn-00bbedbc) 範囲 `[['00bbedbc', '00bbedbf']]`
  - `CONDITIONAL_JUMP` [`00bbedbc`](#insn-00bbedbc) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbedbc`](#insn-00bbedbc) → [`00bbedc0`](#insn-00bbedc0)
- ブロック [`00bbedc0`](#insn-00bbedc0) 範囲 `[['00bbedc0', '00bbedcf']]`
  - `CONDITIONAL_JUMP` [`00bbedcc`](#insn-00bbedcc) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbedcc`](#insn-00bbedcc) → [`00bbedd0`](#insn-00bbedd0)
- ブロック [`00bbedd0`](#insn-00bbedd0) 範囲 `[['00bbedd0', '00bbedd3']]`
  - `UNCONDITIONAL_JUMP` [`00bbedd0`](#insn-00bbedd0) → [`00bbee18`](#insn-00bbee18)
- ブロック [`00bbedd4`](#insn-00bbedd4) 範囲 `[['00bbedd4', '00bbedd7']]`
  - `CONDITIONAL_JUMP` [`00bbedd4`](#insn-00bbedd4) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbedd4`](#insn-00bbedd4) → [`00bbedd8`](#insn-00bbedd8)
- ブロック [`00bbedd8`](#insn-00bbedd8) 範囲 `[['00bbedd8', '00bbede7']]`
  - `CONDITIONAL_JUMP` [`00bbede4`](#insn-00bbede4) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbede4`](#insn-00bbede4) → [`00bbede8`](#insn-00bbede8)
- ブロック [`00bbede8`](#insn-00bbede8) 範囲 `[['00bbede8', '00bbedeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbede8`](#insn-00bbede8) → [`00bbee18`](#insn-00bbee18)
- ブロック [`00bbedec`](#insn-00bbedec) 範囲 `[['00bbedec', '00bbedef']]`
  - `CONDITIONAL_JUMP` [`00bbedec`](#insn-00bbedec) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbedec`](#insn-00bbedec) → [`00bbedf0`](#insn-00bbedf0)
- ブロック [`00bbedf0`](#insn-00bbedf0) 範囲 `[['00bbedf0', '00bbedff']]`
  - `CONDITIONAL_JUMP` [`00bbedfc`](#insn-00bbedfc) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbedfc`](#insn-00bbedfc) → [`00bbee00`](#insn-00bbee00)
- ブロック [`00bbee00`](#insn-00bbee00) 範囲 `[['00bbee00', '00bbee03']]`
  - `UNCONDITIONAL_JUMP` [`00bbee00`](#insn-00bbee00) → [`00bbee18`](#insn-00bbee18)
- ブロック [`00bbee04`](#insn-00bbee04) 範囲 `[['00bbee04', '00bbee07']]`
  - `CONDITIONAL_JUMP` [`00bbee04`](#insn-00bbee04) → [`00bbee18`](#insn-00bbee18)
  - `FALL_THROUGH` [`00bbee04`](#insn-00bbee04) → [`00bbee08`](#insn-00bbee08)
- ブロック [`00bbee08`](#insn-00bbee08) 範囲 `[['00bbee08', '00bbee17']]`
  - `CONDITIONAL_JUMP` [`00bbee14`](#insn-00bbee14) → [`00bbecfc`](#insn-00bbecfc)
  - `FALL_THROUGH` [`00bbee14`](#insn-00bbee14) → [`00bbee18`](#insn-00bbee18)
- ブロック [`00bbee18`](#insn-00bbee18) 範囲 `[['00bbee18', '00bbee2b']]`
  - `UNCONDITIONAL_JUMP` [`00bbee28`](#insn-00bbee28) → [`00bbed00`](#insn-00bbed00)

## 命令位置別の参照

- [`00bbec1c`](#insn-00bbec1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec20`](#insn-00bbec20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec38`](#insn-00bbec38) → [`00bbec44`](#insn-00bbec44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec40`](#insn-00bbec40) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec50`](#insn-00bbec50) → [`00bbed00`](#insn-00bbed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec5c`](#insn-00bbec5c) → [`00bbed00`](#insn-00bbed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec7c`](#insn-00bbec7c) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec88`](#insn-00bbec88) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec90`](#insn-00bbec90) → [`00bbec9c`](#insn-00bbec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec98`](#insn-00bbec98) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeca4`](#insn-00bbeca4) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecac`](#insn-00bbecac) → [`00bbecb8`](#insn-00bbecb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecb4`](#insn-00bbecb4) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecb8`](#insn-00bbecb8) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecc4`](#insn-00bbecc4) → [`00bbed00`](#insn-00bbed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeccc`](#insn-00bbeccc) → [`00bbed00`](#insn-00bbed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbece0`](#insn-00bbece0) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbece8`](#insn-00bbece8) → [`00bbed10`](#insn-00bbed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecf8`](#insn-00bbecf8) → [`00bbed10`](#insn-00bbed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed00`](#insn-00bbed00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed14`](#insn-00bbed14) → [`00bbed44`](#insn-00bbed44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed1c`](#insn-00bbed1c) → [`00bbed78`](#insn-00bbed78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed28`](#insn-00bbed28) → [`00bbed54`](#insn-00bbed54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed34`](#insn-00bbed34) → [`00bbed00`](#insn-00bbed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed3c`](#insn-00bbed3c) → [`00bbed5c`](#insn-00bbed5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed40`](#insn-00bbed40) → [`00bbed00`](#insn-00bbed00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed4c`](#insn-00bbed4c) → [`00bbed94`](#insn-00bbed94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed50`](#insn-00bbed50) → [`00bbee18`](#insn-00bbee18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbed58`](#insn-00bbed58) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed64`](#insn-00bbed64) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed74`](#insn-00bbed74) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed7c`](#insn-00bbed7c) → [`00bbed8c`](#insn-00bbed8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed90`](#insn-00bbed90) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbeda0`](#insn-00bbeda0) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbedb0`](#insn-00bbedb0) → `0030e8a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbedb8::switchdataD_0030e8a4` · 推定型 `byte`
- [`00bbedb8`](#insn-00bbedb8) → [`00bbedbc`](#insn-00bbedbc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbedb8::caseD_1` · 推定型 `None`
- [`00bbedb8`](#insn-00bbedb8) → [`00bbedd4`](#insn-00bbedd4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbedb8::caseD_2` · 推定型 `None`
- [`00bbedb8`](#insn-00bbedb8) → [`00bbedec`](#insn-00bbedec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbedb8::caseD_3` · 推定型 `None`
- [`00bbedb8`](#insn-00bbedb8) → [`00bbee04`](#insn-00bbee04) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbedb8::caseD_4` · 推定型 `None`
- [`00bbedbc`](#insn-00bbedbc) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbedc8`](#insn-00bbedc8) → [`00c5d4e0`](../00c5d/00c5d4e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d4e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbedcc`](#insn-00bbedcc) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedd0`](#insn-00bbedd0) → [`00bbee18`](#insn-00bbee18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbedd4`](#insn-00bbedd4) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbede0`](#insn-00bbede0) → [`00c5d500`](../00c5d/00c5d500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d500` · 推定シンボル `None` · 推定型 `None`
- [`00bbede4`](#insn-00bbede4) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbede8`](#insn-00bbede8) → [`00bbee18`](#insn-00bbee18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbedec`](#insn-00bbedec) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbedf8`](#insn-00bbedf8) → [`00c5d510`](../00c5d/00c5d510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d510` · 推定シンボル `None` · 推定型 `None`
- [`00bbedfc`](#insn-00bbedfc) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee00`](#insn-00bbee00) → [`00bbee18`](#insn-00bbee18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbee04`](#insn-00bbee04) → [`00bbee18`](#insn-00bbee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbedb8::default` · 推定型 `None`
- [`00bbee10`](#insn-00bbee10) → [`00c5d520`](../00c5d/00c5d520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d520` · 推定シンボル `None` · 推定型 `None`
- [`00bbee14`](#insn-00bbee14) → [`00bbecfc`](#insn-00bbecfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee28`](#insn-00bbee28) → [`00bbed00`](#insn-00bbed00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbec1c`](#insn-00bbec1c)

~~~json
{
  "source": "00bbec1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec20`](#insn-00bbec20)

~~~json
{
  "source": "00bbec20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec38`](#insn-00bbec38)

~~~json
{
  "source": "00bbec38",
  "target": "00bbec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec40`](#insn-00bbec40)

~~~json
{
  "source": "00bbec40",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec50`](#insn-00bbec50)

~~~json
{
  "source": "00bbec50",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec5c`](#insn-00bbec5c)

~~~json
{
  "source": "00bbec5c",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec7c`](#insn-00bbec7c)

~~~json
{
  "source": "00bbec7c",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec88`](#insn-00bbec88)

~~~json
{
  "source": "00bbec88",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec90`](#insn-00bbec90)

~~~json
{
  "source": "00bbec90",
  "target": "00bbec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec98`](#insn-00bbec98)

~~~json
{
  "source": "00bbec98",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeca4`](#insn-00bbeca4)

~~~json
{
  "source": "00bbeca4",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecac`](#insn-00bbecac)

~~~json
{
  "source": "00bbecac",
  "target": "00bbecb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecb4`](#insn-00bbecb4)

~~~json
{
  "source": "00bbecb4",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecb8`](#insn-00bbecb8)

~~~json
{
  "source": "00bbecb8",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecc4`](#insn-00bbecc4)

~~~json
{
  "source": "00bbecc4",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeccc`](#insn-00bbeccc)

~~~json
{
  "source": "00bbeccc",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbece0`](#insn-00bbece0)

~~~json
{
  "source": "00bbece0",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbece8`](#insn-00bbece8)

~~~json
{
  "source": "00bbece8",
  "target": "00bbed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecf8`](#insn-00bbecf8)

~~~json
{
  "source": "00bbecf8",
  "target": "00bbed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed00`](#insn-00bbed00)

~~~json
{
  "source": "00bbed00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed14`](#insn-00bbed14)

~~~json
{
  "source": "00bbed14",
  "target": "00bbed44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed1c`](#insn-00bbed1c)

~~~json
{
  "source": "00bbed1c",
  "target": "00bbed78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed28`](#insn-00bbed28)

~~~json
{
  "source": "00bbed28",
  "target": "00bbed54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed34`](#insn-00bbed34)

~~~json
{
  "source": "00bbed34",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed3c`](#insn-00bbed3c)

~~~json
{
  "source": "00bbed3c",
  "target": "00bbed5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed40`](#insn-00bbed40)

~~~json
{
  "source": "00bbed40",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed4c`](#insn-00bbed4c)

~~~json
{
  "source": "00bbed4c",
  "target": "00bbed94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed50`](#insn-00bbed50)

~~~json
{
  "source": "00bbed50",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed58`](#insn-00bbed58)

~~~json
{
  "source": "00bbed58",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed64`](#insn-00bbed64)

~~~json
{
  "source": "00bbed64",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed74`](#insn-00bbed74)

~~~json
{
  "source": "00bbed74",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed7c`](#insn-00bbed7c)

~~~json
{
  "source": "00bbed7c",
  "target": "00bbed8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed90`](#insn-00bbed90)

~~~json
{
  "source": "00bbed90",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeda0`](#insn-00bbeda0)

~~~json
{
  "source": "00bbeda0",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb0`](#insn-00bbedb0)

~~~json
{
  "source": "00bbedb0",
  "target": "0030e8a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e8a4",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e8a4",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "00bbedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "00bbedd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "00bbedec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "00bbee04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedbc`](#insn-00bbedbc)

~~~json
{
  "source": "00bbedbc",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedc8`](#insn-00bbedc8)

~~~json
{
  "source": "00bbedc8",
  "target": "00c5d4e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedcc`](#insn-00bbedcc)

~~~json
{
  "source": "00bbedcc",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedd0`](#insn-00bbedd0)

~~~json
{
  "source": "00bbedd0",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedd4`](#insn-00bbedd4)

~~~json
{
  "source": "00bbedd4",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede0`](#insn-00bbede0)

~~~json
{
  "source": "00bbede0",
  "target": "00c5d500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbede4`](#insn-00bbede4)

~~~json
{
  "source": "00bbede4",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbede8`](#insn-00bbede8)

~~~json
{
  "source": "00bbede8",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedec`](#insn-00bbedec)

~~~json
{
  "source": "00bbedec",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedf8`](#insn-00bbedf8)

~~~json
{
  "source": "00bbedf8",
  "target": "00c5d510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedfc`](#insn-00bbedfc)

~~~json
{
  "source": "00bbedfc",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee00`](#insn-00bbee00)

~~~json
{
  "source": "00bbee00",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee04`](#insn-00bbee04)

~~~json
{
  "source": "00bbee04",
  "target": "00bbee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee10`](#insn-00bbee10)

~~~json
{
  "source": "00bbee10",
  "target": "00c5d520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee14`](#insn-00bbee14)

~~~json
{
  "source": "00bbee14",
  "target": "00bbecfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee28`](#insn-00bbee28)

~~~json
{
  "source": "00bbee28",
  "target": "00bbed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
