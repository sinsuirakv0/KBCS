# 00bbf7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0019.md#review-f9937720c3f64d1a03a46d07c797a343)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbfbd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfbd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-33cf2ae66d4472d78cd9eb66d4f8924a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbf7ac",
  "name": "_ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 648,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "223deea9cd94b4f8d65dc06d836a8289dfc977ca8e46df8d67d6af0558438628",
  "source_text_sha256": "223deea9cd94b4f8d65dc06d836a8289dfc977ca8e46df8d67d6af0558438628",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbf7ac",
        "00bbfa33"
      ]
    ],
    "bytes_sha256": "6a7b6d514f7228d92047126c4e966e53f077f80232c3d9c7473d3c7f23466c9c",
    "instruction_count": 162,
    "instruction_bytes": 648,
    "body_bytes": 648,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d130](../00c5d/00c5d130.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5741 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  uint *puVar4;
  ushort uVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  ushort *puVar13;
  
  lVar8 = *param_2;
  uVar11 = (long)param_1 - lVar8;
  if (((uVar11 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar9 = param_2[1];
    if ((uVar9 < 5) || (uVar10 = uVar9 - 4, uVar10 < uVar11)) {
      return 0;
    }
    lVar7 = param_2[7];
    iVar6 = *param_1;
    uVar1 = (int)lVar7 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar12 = uVar11 - (long)iVar6, (uVar12 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar12 <= uVar9 - 2)) {
      uVar5 = *(ushort *)(lVar8 + uVar12);
      if ((((uVar5 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar5 & 1) == 0)) {
        if (uVar9 <= uVar5) {
          return 0;
        }
        if (uVar9 - uVar5 < uVar12) {
          return 0;
        }
        puVar13 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar13) {
          if ((ulong)puVar13[2] != 0) {
            uVar12 = uVar11 + puVar13[2];
            if ((uVar12 & 3) == 0) {
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            else {
                    /* catch() { ... } // from try @ 00bbf754 with catch @ 00bbf87c */
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar8 + uVar12) < 1) {
              return 0;
            }
                    /* catch() { ... } // from try @ 00bbf95c with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfa9c with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfb88 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfcf8 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bbfda8 with catch @ 00bbf8ac
                       catch() { ... } // from try @ 00bc0080 with catch @ 00bbf8ac */
            if (uVar9 - 1 < uVar12 + *(uint *)(lVar8 + uVar12)) {
              return 0;
            }
          }
          if (((ulong)puVar13[2] != 0) &&
             (puVar4 = (uint *)((long)param_1 + (ulong)puVar13[2]),
             puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
            uVar12 = (long)puVar4 - lVar8;
            if ((uVar12 & 3) == 0) {
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar12) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar4) {
              return 0;
            }
            uVar3 = (ulong)*puVar4 + 4;
            if (uVar9 - 1 < uVar3 + uVar12) {
              return 0;
            }
            if (uVar9 <= uVar3) {
              return 0;
            }
            if (uVar9 - uVar3 < uVar12) {
              return 0;
            }
            if (*(char *)(lVar8 + uVar3 + uVar12) != '\0') {
              return 0;
            }
          }
                    /* try { // try from 00bbf93c to 00cbf95b has its CatchHandler @ 00bc0130 */
          if (6 < *puVar13) {
            if ((ulong)puVar13[3] != 0) {
              uVar11 = uVar11 + puVar13[3];
              if ((uVar11 & 3) == 0) {
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              else {
                    /* try { // try from 00bbf95c to 00cbfa4f has its CatchHandler @ 00bbf8ac */
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar8 + uVar11) < 1) {
                return 0;
              }
              if (uVar9 - 1 < uVar11 + *(uint *)(lVar8 + uVar11)) {
                return 0;
              }
            }
            if (((ulong)puVar13[3] != 0) &&
               (puVar4 = (uint *)((long)param_1 + (ulong)puVar13[3]),
               puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4), puVar4 != (uint *)0x0)) {
              uVar11 = (long)puVar4 - lVar8;
              if ((uVar11 & 3) == 0) {
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              if ((ulong)param_2[4] <= (ulong)*puVar4) {
                return 0;
              }
              uVar10 = (ulong)*puVar4 + 4;
              if (uVar9 - 1 < uVar10 + uVar11) {
                return 0;
              }
              if (uVar9 <= uVar10) {
                return 0;
              }
              if (uVar9 - uVar10 < uVar11) {
                return 0;
              }
              if (*(char *)(lVar8 + uVar10 + uVar11) != '\0') {
                return 0;
              }
            }
          }
        }
        *(int *)(param_2 + 7) = (int)lVar7;
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
<a id="insn-00bbf7ac"></a> `00bbf7ac` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bbf7b0"></a> `00bbf7b0` | `0d 00 09 cb` | sub x13,x0,x9 | `FALL_THROUGH`
<a id="insn-00bbf7b4"></a> `00bbf7b4` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf7b8"></a> `00bbf7b8` | `60 00 00 54` | b.eq 0x00bbf7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf7bc"></a> `00bbf7bc` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf7c0"></a> `00bbf7c0` | `e8 12 00 35` | cbnz w8,0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf7c4"></a> `00bbf7c4` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbf7c8"></a> `00bbf7c8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf7cc"></a> `00bbf7cc` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf7d0"></a> `00bbf7d0` | `e3 12 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf7d4"></a> `00bbf7d4` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf7d8"></a> `00bbf7d8` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf7dc"></a> `00bbf7dc` | `83 12 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf7e0"></a> `00bbf7e0` | `2b 38 47 29` | ldp w11,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbf7e4"></a> `00bbf7e4` | `2f 10 40 b9` | ldr w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf7e8"></a> `00bbf7e8` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbf7ec"></a> `00bbf7ec` | `70 05 00 11` | add w16,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf7f0"></a> `00bbf7f0` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf7f4"></a> `00bbf7f4` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbf7f8"></a> `00bbf7f8` | `30 38 07 29` | stp w16,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbf7fc"></a> `00bbf7fc` | `08 11 00 54` | b.hi 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf800"></a> `00bbf800` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00bbf804"></a> `00bbf804` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00bbf808"></a> `00bbf808` | `a8 10 00 54` | b.hi 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf80c"></a> `00bbf80c` | `ae 01 08 cb` | sub x14,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbf810"></a> `00bbf810` | `6e 00 00 36` | tbz w14,#0x0,0x00bbf81c | `CONDITIONAL_JUMP`
<a id="insn-00bbf814"></a> `00bbf814` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf818"></a> `00bbf818` | `28 10 00 35` | cbnz w8,0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf81c"></a> `00bbf81c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf820"></a> `00bbf820` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00bbf824"></a> `00bbf824` | `c3 0f 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf828"></a> `00bbf828` | `28 69 6e 78` | ldrh w8,[x9, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf82c"></a> `00bbf82c` | `68 00 00 36` | tbz w8,#0x0,0x00bbf838 | `CONDITIONAL_JUMP`
<a id="insn-00bbf830"></a> `00bbf830` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf834"></a> `00bbf834` | `4f 0f 00 35` | cbnz w15,0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf838"></a> `00bbf838` | `28 0f 00 37` | tbnz w8,#0x0,0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf83c"></a> `00bbf83c` | `4f 01 08 eb` | subs x15,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbf840"></a> `00bbf840` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf844"></a> `00bbf844` | `49 0f 00 54` | b.ls 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf848"></a> `00bbf848` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbf84c"></a> `00bbf84c` | `03 0f 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf850"></a> `00bbf850` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbf854"></a> `00bbf854` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbf858"></a> `00bbf858` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00bbf85c"></a> `00bbf85c` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00bbf860"></a> `00bbf860` | `23 0e 00 54` | b.cc 0x00bbfa24 | `CONDITIONAL_JUMP`
<a id="insn-00bbf864"></a> `00bbf864` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bbf868"></a> `00bbf868` | `68 02 00 b4` | cbz x8,0x00bbf8b4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf86c"></a> `00bbf86c` | `b0 01 08 8b` | add x16,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbf870"></a> `00bbf870` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf874"></a> `00bbf874` | `e0 00 00 54` | b.eq 0x00bbf890 | `CONDITIONAL_JUMP`
<a id="insn-00bbf878"></a> `00bbf878` | `31 60 40 39` | ldrb w17,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf87c"></a> `00bbf87c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf880"></a> `00bbf880` | `71 0d 00 35` | cbnz w17,0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf884"></a> `00bbf884` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbf888"></a> `00bbf888` | `82 00 00 54` | b.cs 0x00bbf898 | `CONDITIONAL_JUMP`
<a id="insn-00bbf88c"></a> `00bbf88c` | `68 00 00 14` | b 0x00bbfa2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf890"></a> `00bbf890` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbf894"></a> `00bbf894` | `43 0c 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf898"></a> `00bbf898` | `28 69 70 b8` | ldr w8,[x9, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf89c"></a> `00bbf89c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf8a0"></a> `00bbf8a0` | `eb 0b 00 54` | b.lt 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8a4"></a> `00bbf8a4` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00bbf8a8"></a> `00bbf8a8` | `50 05 00 d1` | sub x16,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf8ac"></a> `00bbf8ac` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00bbf8b0"></a> `00bbf8b0` | `63 0b 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8b4"></a> `00bbf8b4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bbf8b8"></a> `00bbf8b8` | `28 04 00 b4` | cbz x8,0x00bbf93c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8bc"></a> `00bbf8bc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbf8c0"></a> `00bbf8c0` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00bbf8c4"></a> `00bbf8c4` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00bbf8c8"></a> `00bbf8c8` | `a0 03 00 54` | b.eq 0x00bbf93c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8cc"></a> `00bbf8cc` | `30 02 09 cb` | sub x16,x17,x9 | `FALL_THROUGH`
<a id="insn-00bbf8d0"></a> `00bbf8d0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf8d4"></a> `00bbf8d4` | `e0 00 00 54` | b.eq 0x00bbf8f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8d8"></a> `00bbf8d8` | `22 60 40 39` | ldrb w2,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf8dc"></a> `00bbf8dc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf8e0"></a> `00bbf8e0` | `62 0a 00 35` | cbnz w2,0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8e4"></a> `00bbf8e4` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbf8e8"></a> `00bbf8e8` | `82 00 00 54` | b.cs 0x00bbf8f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf8ec"></a> `00bbf8ec` | `50 00 00 14` | b 0x00bbfa2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf8f0"></a> `00bbf8f0` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbf8f4"></a> `00bbf8f4` | `43 09 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf8f8"></a> `00bbf8f8` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00bbf8fc"></a> `00bbf8fc` | `31 10 40 f9` | ldr x17,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf900"></a> `00bbf900` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bbf904"></a> `00bbf904` | `c9 08 00 54` | b.ls 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf908"></a> `00bbf908` | `02 11 00 91` | add x2,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf90c"></a> `00bbf90c` | `51 00 10 8b` | add x17,x2,x16 | `FALL_THROUGH`
<a id="insn-00bbf910"></a> `00bbf910` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf914"></a> `00bbf914` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00bbf918"></a> `00bbf918` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf91c"></a> `00bbf91c` | `83 08 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf920"></a> `00bbf920` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-00bbf924"></a> `00bbf924` | `49 08 00 54` | b.ls 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf928"></a> `00bbf928` | `42 01 02 cb` | sub x2,x10,x2 | `FALL_THROUGH`
<a id="insn-00bbf92c"></a> `00bbf92c` | `5f 00 10 eb` | cmp x2,x16 | `FALL_THROUGH`
<a id="insn-00bbf930"></a> `00bbf930` | `e3 07 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf934"></a> `00bbf934` | `28 69 71 38` | ldrb w8,[x9, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00bbf938"></a> `00bbf938` | `28 07 00 35` | cbnz w8,0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf93c"></a> `00bbf93c` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00bbf940"></a> `00bbf940` | `23 07 00 54` | b.cc 0x00bbfa24 | `CONDITIONAL_JUMP`
<a id="insn-00bbf944"></a> `00bbf944` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00bbf948"></a> `00bbf948` | `68 02 00 b4` | cbz x8,0x00bbf994 | `CONDITIONAL_JUMP`
<a id="insn-00bbf94c"></a> `00bbf94c` | `ad 01 08 8b` | add x13,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbf950"></a> `00bbf950` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf954"></a> `00bbf954` | `e0 00 00 54` | b.eq 0x00bbf970 | `CONDITIONAL_JUMP`
<a id="insn-00bbf958"></a> `00bbf958` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf95c"></a> `00bbf95c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf960"></a> `00bbf960` | `6f 06 00 35` | cbnz w15,0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf964"></a> `00bbf964` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf968"></a> `00bbf968` | `82 00 00 54` | b.cs 0x00bbf978 | `CONDITIONAL_JUMP`
<a id="insn-00bbf96c"></a> `00bbf96c` | `30 00 00 14` | b 0x00bbfa2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf970"></a> `00bbf970` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf974"></a> `00bbf974` | `43 05 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf978"></a> `00bbf978` | `28 69 6d b8` | ldr w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbf97c"></a> `00bbf97c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf980"></a> `00bbf980` | `eb 04 00 54` | b.lt 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf984"></a> `00bbf984` | `a8 01 08 8b` | add x8,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbf988"></a> `00bbf988` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf98c"></a> `00bbf98c` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bbf990"></a> `00bbf990` | `63 04 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf994"></a> `00bbf994` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00bbf998"></a> `00bbf998` | `68 04 00 b4` | cbz x8,0x00bbfa24 | `CONDITIONAL_JUMP`
<a id="insn-00bbf99c"></a> `00bbf99c` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbf9a0"></a> `00bbf9a0` | `0d 01 40 b9` | ldr w13,[x8] | `FALL_THROUGH`
<a id="insn-00bbf9a4"></a> `00bbf9a4` | `0e 01 0d ab` | adds x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00bbf9a8"></a> `00bbf9a8` | `e0 03 00 54` | b.eq 0x00bbfa24 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9ac"></a> `00bbf9ac` | `cd 01 09 cb` | sub x13,x14,x9 | `FALL_THROUGH`
<a id="insn-00bbf9b0"></a> `00bbf9b0` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbf9b4"></a> `00bbf9b4` | `e0 00 00 54` | b.eq 0x00bbf9d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9b8"></a> `00bbf9b8` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbf9bc"></a> `00bbf9bc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf9c0"></a> `00bbf9c0` | `6f 03 00 35` | cbnz w15,0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbf9c4"></a> `00bbf9c4` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf9c8"></a> `00bbf9c8` | `82 00 00 54` | b.cs 0x00bbf9d8 | `CONDITIONAL_JUMP`
<a id="insn-00bbf9cc"></a> `00bbf9cc` | `18 00 00 14` | b 0x00bbfa2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf9d0"></a> `00bbf9d0` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbf9d4"></a> `00bbf9d4` | `43 02 00 54` | b.cc 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf9d8"></a> `00bbf9d8` | `c8 01 40 b9` | ldr w8,[x14] | `FALL_THROUGH`
<a id="insn-00bbf9dc"></a> `00bbf9dc` | `2c 10 40 f9` | ldr x12,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf9e0"></a> `00bbf9e0` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bbf9e4"></a> `00bbf9e4` | `c9 01 00 54` | b.ls 0x00bbfa1c | `CONDITIONAL_JUMP`
<a id="insn-00bbf9e8"></a> `00bbf9e8` | `0e 11 00 91` | add x14,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbf9ec"></a> `00bbf9ec` | `cc 01 0d 8b` | add x12,x14,x13 | `FALL_THROUGH`
<a id="insn-00bbf9f0"></a> `00bbf9f0` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf9f4"></a> `00bbf9f4` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00bbf9f8"></a> `00bbf9f8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbf9fc"></a> `00bbf9fc` | `83 01 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbfa00"></a> `00bbfa00` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00bbfa04"></a> `00bbfa04` | `49 01 00 54` | b.ls 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbfa08"></a> `00bbfa08` | `4a 01 0e cb` | sub x10,x10,x14 | `FALL_THROUGH`
<a id="insn-00bbfa0c"></a> `00bbfa0c` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00bbfa10"></a> `00bbfa10` | `e3 00 00 54` | b.cc 0x00bbfa2c | `CONDITIONAL_JUMP`
<a id="insn-00bbfa14"></a> `00bbfa14` | `28 69 6c 38` | ldrb w8,[x9, x12, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfa18"></a> `00bbfa18` | `68 00 00 34` | cbz w8,0x00bbfa24 | `CONDITIONAL_JUMP`
<a id="insn-00bbfa1c"></a> `00bbfa1c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfa20"></a> `00bbfa20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfa24"></a> `00bbfa24` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfa28"></a> `00bbfa28` | `2b 38 00 b9` | str w11,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfa2c"></a> `00bbfa2c` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bbfa30"></a> `00bbfa30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbf7ac`](#insn-00bbf7ac) 範囲 `[['00bbf7ac', '00bbf7bb']]`
  - `CONDITIONAL_JUMP` [`00bbf7b8`](#insn-00bbf7b8) → [`00bbf7c4`](#insn-00bbf7c4)
  - `FALL_THROUGH` [`00bbf7b8`](#insn-00bbf7b8) → [`00bbf7bc`](#insn-00bbf7bc)
- ブロック [`00bbf7bc`](#insn-00bbf7bc) 範囲 `[['00bbf7bc', '00bbf7c3']]`
  - `CONDITIONAL_JUMP` [`00bbf7c0`](#insn-00bbf7c0) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf7c0`](#insn-00bbf7c0) → [`00bbf7c4`](#insn-00bbf7c4)
- ブロック [`00bbf7c4`](#insn-00bbf7c4) 範囲 `[['00bbf7c4', '00bbf7d3']]`
  - `CONDITIONAL_JUMP` [`00bbf7d0`](#insn-00bbf7d0) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf7d0`](#insn-00bbf7d0) → [`00bbf7d4`](#insn-00bbf7d4)
- ブロック [`00bbf7d4`](#insn-00bbf7d4) 範囲 `[['00bbf7d4', '00bbf7df']]`
  - `CONDITIONAL_JUMP` [`00bbf7dc`](#insn-00bbf7dc) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf7dc`](#insn-00bbf7dc) → [`00bbf7e0`](#insn-00bbf7e0)
- ブロック [`00bbf7e0`](#insn-00bbf7e0) 範囲 `[['00bbf7e0', '00bbf7ff']]`
  - `CONDITIONAL_JUMP` [`00bbf7fc`](#insn-00bbf7fc) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf7fc`](#insn-00bbf7fc) → [`00bbf800`](#insn-00bbf800)
- ブロック [`00bbf800`](#insn-00bbf800) 範囲 `[['00bbf800', '00bbf80b']]`
  - `CONDITIONAL_JUMP` [`00bbf808`](#insn-00bbf808) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf808`](#insn-00bbf808) → [`00bbf80c`](#insn-00bbf80c)
- ブロック [`00bbf80c`](#insn-00bbf80c) 範囲 `[['00bbf80c', '00bbf813']]`
  - `CONDITIONAL_JUMP` [`00bbf810`](#insn-00bbf810) → [`00bbf81c`](#insn-00bbf81c)
  - `FALL_THROUGH` [`00bbf810`](#insn-00bbf810) → [`00bbf814`](#insn-00bbf814)
- ブロック [`00bbf814`](#insn-00bbf814) 範囲 `[['00bbf814', '00bbf81b']]`
  - `CONDITIONAL_JUMP` [`00bbf818`](#insn-00bbf818) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf818`](#insn-00bbf818) → [`00bbf81c`](#insn-00bbf81c)
- ブロック [`00bbf81c`](#insn-00bbf81c) 範囲 `[['00bbf81c', '00bbf827']]`
  - `CONDITIONAL_JUMP` [`00bbf824`](#insn-00bbf824) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf824`](#insn-00bbf824) → [`00bbf828`](#insn-00bbf828)
- ブロック [`00bbf828`](#insn-00bbf828) 範囲 `[['00bbf828', '00bbf82f']]`
  - `CONDITIONAL_JUMP` [`00bbf82c`](#insn-00bbf82c) → [`00bbf838`](#insn-00bbf838)
  - `FALL_THROUGH` [`00bbf82c`](#insn-00bbf82c) → [`00bbf830`](#insn-00bbf830)
- ブロック [`00bbf830`](#insn-00bbf830) 範囲 `[['00bbf830', '00bbf837']]`
  - `CONDITIONAL_JUMP` [`00bbf834`](#insn-00bbf834) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf834`](#insn-00bbf834) → [`00bbf838`](#insn-00bbf838)
- ブロック [`00bbf838`](#insn-00bbf838) 範囲 `[['00bbf838', '00bbf83b']]`
  - `CONDITIONAL_JUMP` [`00bbf838`](#insn-00bbf838) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf838`](#insn-00bbf838) → [`00bbf83c`](#insn-00bbf83c)
- ブロック [`00bbf83c`](#insn-00bbf83c) 範囲 `[['00bbf83c', '00bbf847']]`
  - `CONDITIONAL_JUMP` [`00bbf844`](#insn-00bbf844) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf844`](#insn-00bbf844) → [`00bbf848`](#insn-00bbf848)
- ブロック [`00bbf848`](#insn-00bbf848) 範囲 `[['00bbf848', '00bbf84f']]`
  - `CONDITIONAL_JUMP` [`00bbf84c`](#insn-00bbf84c) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf84c`](#insn-00bbf84c) → [`00bbf850`](#insn-00bbf850)
- ブロック [`00bbf850`](#insn-00bbf850) 範囲 `[['00bbf850', '00bbf863']]`
  - `CONDITIONAL_JUMP` [`00bbf860`](#insn-00bbf860) → [`00bbfa24`](#insn-00bbfa24)
  - `FALL_THROUGH` [`00bbf860`](#insn-00bbf860) → [`00bbf864`](#insn-00bbf864)
- ブロック [`00bbf864`](#insn-00bbf864) 範囲 `[['00bbf864', '00bbf86b']]`
  - `CONDITIONAL_JUMP` [`00bbf868`](#insn-00bbf868) → [`00bbf8b4`](#insn-00bbf8b4)
  - `FALL_THROUGH` [`00bbf868`](#insn-00bbf868) → [`00bbf86c`](#insn-00bbf86c)
- ブロック [`00bbf86c`](#insn-00bbf86c) 範囲 `[['00bbf86c', '00bbf877']]`
  - `CONDITIONAL_JUMP` [`00bbf874`](#insn-00bbf874) → [`00bbf890`](#insn-00bbf890)
  - `FALL_THROUGH` [`00bbf874`](#insn-00bbf874) → [`00bbf878`](#insn-00bbf878)
- ブロック [`00bbf878`](#insn-00bbf878) 範囲 `[['00bbf878', '00bbf87b']]`
  - `FALL_THROUGH` [`00bbf878`](#insn-00bbf878) → [`00bbf87c`](#insn-00bbf87c)
- ブロック [`00bbf87c`](#insn-00bbf87c) 範囲 `[['00bbf87c', '00bbf883']]`
  - `CONDITIONAL_JUMP` [`00bbf880`](#insn-00bbf880) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf880`](#insn-00bbf880) → [`00bbf884`](#insn-00bbf884)
- ブロック [`00bbf884`](#insn-00bbf884) 範囲 `[['00bbf884', '00bbf88b']]`
  - `CONDITIONAL_JUMP` [`00bbf888`](#insn-00bbf888) → [`00bbf898`](#insn-00bbf898)
  - `FALL_THROUGH` [`00bbf888`](#insn-00bbf888) → [`00bbf88c`](#insn-00bbf88c)
- ブロック [`00bbf88c`](#insn-00bbf88c) 範囲 `[['00bbf88c', '00bbf88f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf88c`](#insn-00bbf88c) → [`00bbfa2c`](#insn-00bbfa2c)
- ブロック [`00bbf890`](#insn-00bbf890) 範囲 `[['00bbf890', '00bbf897']]`
  - `CONDITIONAL_JUMP` [`00bbf894`](#insn-00bbf894) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf894`](#insn-00bbf894) → [`00bbf898`](#insn-00bbf898)
- ブロック [`00bbf898`](#insn-00bbf898) 範囲 `[['00bbf898', '00bbf8a3']]`
  - `CONDITIONAL_JUMP` [`00bbf8a0`](#insn-00bbf8a0) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf8a0`](#insn-00bbf8a0) → [`00bbf8a4`](#insn-00bbf8a4)
- ブロック [`00bbf8a4`](#insn-00bbf8a4) 範囲 `[['00bbf8a4', '00bbf8ab']]`
  - `FALL_THROUGH` [`00bbf8a8`](#insn-00bbf8a8) → [`00bbf8ac`](#insn-00bbf8ac)
- ブロック [`00bbf8ac`](#insn-00bbf8ac) 範囲 `[['00bbf8ac', '00bbf8b3']]`
  - `CONDITIONAL_JUMP` [`00bbf8b0`](#insn-00bbf8b0) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf8b0`](#insn-00bbf8b0) → [`00bbf8b4`](#insn-00bbf8b4)
- ブロック [`00bbf8b4`](#insn-00bbf8b4) 範囲 `[['00bbf8b4', '00bbf8bb']]`
  - `CONDITIONAL_JUMP` [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf93c`](#insn-00bbf93c)
  - `FALL_THROUGH` [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf8bc`](#insn-00bbf8bc)
- ブロック [`00bbf8bc`](#insn-00bbf8bc) 範囲 `[['00bbf8bc', '00bbf8cb']]`
  - `CONDITIONAL_JUMP` [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf93c`](#insn-00bbf93c)
  - `FALL_THROUGH` [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf8cc`](#insn-00bbf8cc)
- ブロック [`00bbf8cc`](#insn-00bbf8cc) 範囲 `[['00bbf8cc', '00bbf8d7']]`
  - `CONDITIONAL_JUMP` [`00bbf8d4`](#insn-00bbf8d4) → [`00bbf8f0`](#insn-00bbf8f0)
  - `FALL_THROUGH` [`00bbf8d4`](#insn-00bbf8d4) → [`00bbf8d8`](#insn-00bbf8d8)
- ブロック [`00bbf8d8`](#insn-00bbf8d8) 範囲 `[['00bbf8d8', '00bbf8e3']]`
  - `CONDITIONAL_JUMP` [`00bbf8e0`](#insn-00bbf8e0) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf8e0`](#insn-00bbf8e0) → [`00bbf8e4`](#insn-00bbf8e4)
- ブロック [`00bbf8e4`](#insn-00bbf8e4) 範囲 `[['00bbf8e4', '00bbf8eb']]`
  - `CONDITIONAL_JUMP` [`00bbf8e8`](#insn-00bbf8e8) → [`00bbf8f8`](#insn-00bbf8f8)
  - `FALL_THROUGH` [`00bbf8e8`](#insn-00bbf8e8) → [`00bbf8ec`](#insn-00bbf8ec)
- ブロック [`00bbf8ec`](#insn-00bbf8ec) 範囲 `[['00bbf8ec', '00bbf8ef']]`
  - `UNCONDITIONAL_JUMP` [`00bbf8ec`](#insn-00bbf8ec) → [`00bbfa2c`](#insn-00bbfa2c)
- ブロック [`00bbf8f0`](#insn-00bbf8f0) 範囲 `[['00bbf8f0', '00bbf8f7']]`
  - `CONDITIONAL_JUMP` [`00bbf8f4`](#insn-00bbf8f4) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf8f4`](#insn-00bbf8f4) → [`00bbf8f8`](#insn-00bbf8f8)
- ブロック [`00bbf8f8`](#insn-00bbf8f8) 範囲 `[['00bbf8f8', '00bbf907']]`
  - `CONDITIONAL_JUMP` [`00bbf904`](#insn-00bbf904) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf904`](#insn-00bbf904) → [`00bbf908`](#insn-00bbf908)
- ブロック [`00bbf908`](#insn-00bbf908) 範囲 `[['00bbf908', '00bbf91f']]`
  - `CONDITIONAL_JUMP` [`00bbf91c`](#insn-00bbf91c) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf91c`](#insn-00bbf91c) → [`00bbf920`](#insn-00bbf920)
- ブロック [`00bbf920`](#insn-00bbf920) 範囲 `[['00bbf920', '00bbf927']]`
  - `CONDITIONAL_JUMP` [`00bbf924`](#insn-00bbf924) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf924`](#insn-00bbf924) → [`00bbf928`](#insn-00bbf928)
- ブロック [`00bbf928`](#insn-00bbf928) 範囲 `[['00bbf928', '00bbf933']]`
  - `CONDITIONAL_JUMP` [`00bbf930`](#insn-00bbf930) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf930`](#insn-00bbf930) → [`00bbf934`](#insn-00bbf934)
- ブロック [`00bbf934`](#insn-00bbf934) 範囲 `[['00bbf934', '00bbf93b']]`
  - `CONDITIONAL_JUMP` [`00bbf938`](#insn-00bbf938) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf938`](#insn-00bbf938) → [`00bbf93c`](#insn-00bbf93c)
- ブロック [`00bbf93c`](#insn-00bbf93c) 範囲 `[['00bbf93c', '00bbf943']]`
  - `CONDITIONAL_JUMP` [`00bbf940`](#insn-00bbf940) → [`00bbfa24`](#insn-00bbfa24)
  - `FALL_THROUGH` [`00bbf940`](#insn-00bbf940) → [`00bbf944`](#insn-00bbf944)
- ブロック [`00bbf944`](#insn-00bbf944) 範囲 `[['00bbf944', '00bbf94b']]`
  - `CONDITIONAL_JUMP` [`00bbf948`](#insn-00bbf948) → [`00bbf994`](#insn-00bbf994)
  - `FALL_THROUGH` [`00bbf948`](#insn-00bbf948) → [`00bbf94c`](#insn-00bbf94c)
- ブロック [`00bbf94c`](#insn-00bbf94c) 範囲 `[['00bbf94c', '00bbf957']]`
  - `CONDITIONAL_JUMP` [`00bbf954`](#insn-00bbf954) → [`00bbf970`](#insn-00bbf970)
  - `FALL_THROUGH` [`00bbf954`](#insn-00bbf954) → [`00bbf958`](#insn-00bbf958)
- ブロック [`00bbf958`](#insn-00bbf958) 範囲 `[['00bbf958', '00bbf95b']]`
  - `FALL_THROUGH` [`00bbf958`](#insn-00bbf958) → [`00bbf95c`](#insn-00bbf95c)
- ブロック [`00bbf95c`](#insn-00bbf95c) 範囲 `[['00bbf95c', '00bbf963']]`
  - `CONDITIONAL_JUMP` [`00bbf960`](#insn-00bbf960) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf960`](#insn-00bbf960) → [`00bbf964`](#insn-00bbf964)
- ブロック [`00bbf964`](#insn-00bbf964) 範囲 `[['00bbf964', '00bbf96b']]`
  - `CONDITIONAL_JUMP` [`00bbf968`](#insn-00bbf968) → [`00bbf978`](#insn-00bbf978)
  - `FALL_THROUGH` [`00bbf968`](#insn-00bbf968) → [`00bbf96c`](#insn-00bbf96c)
- ブロック [`00bbf96c`](#insn-00bbf96c) 範囲 `[['00bbf96c', '00bbf96f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf96c`](#insn-00bbf96c) → [`00bbfa2c`](#insn-00bbfa2c)
- ブロック [`00bbf970`](#insn-00bbf970) 範囲 `[['00bbf970', '00bbf977']]`
  - `CONDITIONAL_JUMP` [`00bbf974`](#insn-00bbf974) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf974`](#insn-00bbf974) → [`00bbf978`](#insn-00bbf978)
- ブロック [`00bbf978`](#insn-00bbf978) 範囲 `[['00bbf978', '00bbf983']]`
  - `CONDITIONAL_JUMP` [`00bbf980`](#insn-00bbf980) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf980`](#insn-00bbf980) → [`00bbf984`](#insn-00bbf984)
- ブロック [`00bbf984`](#insn-00bbf984) 範囲 `[['00bbf984', '00bbf993']]`
  - `CONDITIONAL_JUMP` [`00bbf990`](#insn-00bbf990) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf990`](#insn-00bbf990) → [`00bbf994`](#insn-00bbf994)
- ブロック [`00bbf994`](#insn-00bbf994) 範囲 `[['00bbf994', '00bbf99b']]`
  - `CONDITIONAL_JUMP` [`00bbf998`](#insn-00bbf998) → [`00bbfa24`](#insn-00bbfa24)
  - `FALL_THROUGH` [`00bbf998`](#insn-00bbf998) → [`00bbf99c`](#insn-00bbf99c)
- ブロック [`00bbf99c`](#insn-00bbf99c) 範囲 `[['00bbf99c', '00bbf9ab']]`
  - `CONDITIONAL_JUMP` [`00bbf9a8`](#insn-00bbf9a8) → [`00bbfa24`](#insn-00bbfa24)
  - `FALL_THROUGH` [`00bbf9a8`](#insn-00bbf9a8) → [`00bbf9ac`](#insn-00bbf9ac)
- ブロック [`00bbf9ac`](#insn-00bbf9ac) 範囲 `[['00bbf9ac', '00bbf9b7']]`
  - `CONDITIONAL_JUMP` [`00bbf9b4`](#insn-00bbf9b4) → [`00bbf9d0`](#insn-00bbf9d0)
  - `FALL_THROUGH` [`00bbf9b4`](#insn-00bbf9b4) → [`00bbf9b8`](#insn-00bbf9b8)
- ブロック [`00bbf9b8`](#insn-00bbf9b8) 範囲 `[['00bbf9b8', '00bbf9c3']]`
  - `CONDITIONAL_JUMP` [`00bbf9c0`](#insn-00bbf9c0) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf9c0`](#insn-00bbf9c0) → [`00bbf9c4`](#insn-00bbf9c4)
- ブロック [`00bbf9c4`](#insn-00bbf9c4) 範囲 `[['00bbf9c4', '00bbf9cb']]`
  - `CONDITIONAL_JUMP` [`00bbf9c8`](#insn-00bbf9c8) → [`00bbf9d8`](#insn-00bbf9d8)
  - `FALL_THROUGH` [`00bbf9c8`](#insn-00bbf9c8) → [`00bbf9cc`](#insn-00bbf9cc)
- ブロック [`00bbf9cc`](#insn-00bbf9cc) 範囲 `[['00bbf9cc', '00bbf9cf']]`
  - `UNCONDITIONAL_JUMP` [`00bbf9cc`](#insn-00bbf9cc) → [`00bbfa2c`](#insn-00bbfa2c)
- ブロック [`00bbf9d0`](#insn-00bbf9d0) 範囲 `[['00bbf9d0', '00bbf9d7']]`
  - `CONDITIONAL_JUMP` [`00bbf9d4`](#insn-00bbf9d4) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf9d4`](#insn-00bbf9d4) → [`00bbf9d8`](#insn-00bbf9d8)
- ブロック [`00bbf9d8`](#insn-00bbf9d8) 範囲 `[['00bbf9d8', '00bbf9e7']]`
  - `CONDITIONAL_JUMP` [`00bbf9e4`](#insn-00bbf9e4) → [`00bbfa1c`](#insn-00bbfa1c)
  - `FALL_THROUGH` [`00bbf9e4`](#insn-00bbf9e4) → [`00bbf9e8`](#insn-00bbf9e8)
- ブロック [`00bbf9e8`](#insn-00bbf9e8) 範囲 `[['00bbf9e8', '00bbf9ff']]`
  - `CONDITIONAL_JUMP` [`00bbf9fc`](#insn-00bbf9fc) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbf9fc`](#insn-00bbf9fc) → [`00bbfa00`](#insn-00bbfa00)
- ブロック [`00bbfa00`](#insn-00bbfa00) 範囲 `[['00bbfa00', '00bbfa07']]`
  - `CONDITIONAL_JUMP` [`00bbfa04`](#insn-00bbfa04) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbfa04`](#insn-00bbfa04) → [`00bbfa08`](#insn-00bbfa08)
- ブロック [`00bbfa08`](#insn-00bbfa08) 範囲 `[['00bbfa08', '00bbfa13']]`
  - `CONDITIONAL_JUMP` [`00bbfa10`](#insn-00bbfa10) → [`00bbfa2c`](#insn-00bbfa2c)
  - `FALL_THROUGH` [`00bbfa10`](#insn-00bbfa10) → [`00bbfa14`](#insn-00bbfa14)
- ブロック [`00bbfa14`](#insn-00bbfa14) 範囲 `[['00bbfa14', '00bbfa1b']]`
  - `CONDITIONAL_JUMP` [`00bbfa18`](#insn-00bbfa18) → [`00bbfa24`](#insn-00bbfa24)
  - `FALL_THROUGH` [`00bbfa18`](#insn-00bbfa18) → [`00bbfa1c`](#insn-00bbfa1c)
- ブロック [`00bbfa1c`](#insn-00bbfa1c) 範囲 `[['00bbfa1c', '00bbfa23']]`
- ブロック [`00bbfa24`](#insn-00bbfa24) 範囲 `[['00bbfa24', '00bbfa2b']]`
  - `FALL_THROUGH` [`00bbfa28`](#insn-00bbfa28) → [`00bbfa2c`](#insn-00bbfa2c)
- ブロック [`00bbfa2c`](#insn-00bbfa2c) 範囲 `[['00bbfa2c', '00bbfa33']]`

## 命令位置別の参照

- [`00bbf7b8`](#insn-00bbf7b8) → [`00bbf7c4`](#insn-00bbf7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7c0`](#insn-00bbf7c0) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7d0`](#insn-00bbf7d0) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7dc`](#insn-00bbf7dc) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf7fc`](#insn-00bbf7fc) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf808`](#insn-00bbf808) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf810`](#insn-00bbf810) → [`00bbf81c`](#insn-00bbf81c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf818`](#insn-00bbf818) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf824`](#insn-00bbf824) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf82c`](#insn-00bbf82c) → [`00bbf838`](#insn-00bbf838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf834`](#insn-00bbf834) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf838`](#insn-00bbf838) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf844`](#insn-00bbf844) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf84c`](#insn-00bbf84c) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf860`](#insn-00bbf860) → [`00bbfa24`](#insn-00bbfa24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf868`](#insn-00bbf868) → [`00bbf8b4`](#insn-00bbf8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf874`](#insn-00bbf874) → [`00bbf890`](#insn-00bbf890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf880`](#insn-00bbf880) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf888`](#insn-00bbf888) → [`00bbf898`](#insn-00bbf898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf88c`](#insn-00bbf88c) → [`00bbfa2c`](#insn-00bbfa2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf894`](#insn-00bbf894) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8a0`](#insn-00bbf8a0) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8b0`](#insn-00bbf8b0) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8b8`](#insn-00bbf8b8) → [`00bbf93c`](#insn-00bbf93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8c8`](#insn-00bbf8c8) → [`00bbf93c`](#insn-00bbf93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8d4`](#insn-00bbf8d4) → [`00bbf8f0`](#insn-00bbf8f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8e0`](#insn-00bbf8e0) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8e8`](#insn-00bbf8e8) → [`00bbf8f8`](#insn-00bbf8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8ec`](#insn-00bbf8ec) → [`00bbfa2c`](#insn-00bbfa2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf8f4`](#insn-00bbf8f4) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf904`](#insn-00bbf904) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf91c`](#insn-00bbf91c) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf924`](#insn-00bbf924) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf930`](#insn-00bbf930) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf938`](#insn-00bbf938) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf940`](#insn-00bbf940) → [`00bbfa24`](#insn-00bbfa24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf948`](#insn-00bbf948) → [`00bbf994`](#insn-00bbf994) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf954`](#insn-00bbf954) → [`00bbf970`](#insn-00bbf970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf960`](#insn-00bbf960) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf968`](#insn-00bbf968) → [`00bbf978`](#insn-00bbf978) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf96c`](#insn-00bbf96c) → [`00bbfa2c`](#insn-00bbfa2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf974`](#insn-00bbf974) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf980`](#insn-00bbf980) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf990`](#insn-00bbf990) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf998`](#insn-00bbf998) → [`00bbfa24`](#insn-00bbfa24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9a8`](#insn-00bbf9a8) → [`00bbfa24`](#insn-00bbfa24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9b4`](#insn-00bbf9b4) → [`00bbf9d0`](#insn-00bbf9d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9c0`](#insn-00bbf9c0) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9c8`](#insn-00bbf9c8) → [`00bbf9d8`](#insn-00bbf9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9cc`](#insn-00bbf9cc) → [`00bbfa2c`](#insn-00bbfa2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9d4`](#insn-00bbf9d4) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9e4`](#insn-00bbf9e4) → [`00bbfa1c`](#insn-00bbfa1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf9fc`](#insn-00bbf9fc) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa04`](#insn-00bbfa04) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa10`](#insn-00bbfa10) → [`00bbfa2c`](#insn-00bbfa2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfa18`](#insn-00bbfa18) → [`00bbfa24`](#insn-00bbfa24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbf7b8`](#insn-00bbf7b8)

~~~json
{
  "source": "00bbf7b8",
  "target": "00bbf7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7c0`](#insn-00bbf7c0)

~~~json
{
  "source": "00bbf7c0",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7d0`](#insn-00bbf7d0)

~~~json
{
  "source": "00bbf7d0",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7dc`](#insn-00bbf7dc)

~~~json
{
  "source": "00bbf7dc",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf7fc`](#insn-00bbf7fc)

~~~json
{
  "source": "00bbf7fc",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf808`](#insn-00bbf808)

~~~json
{
  "source": "00bbf808",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf810`](#insn-00bbf810)

~~~json
{
  "source": "00bbf810",
  "target": "00bbf81c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf818`](#insn-00bbf818)

~~~json
{
  "source": "00bbf818",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf824`](#insn-00bbf824)

~~~json
{
  "source": "00bbf824",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf82c`](#insn-00bbf82c)

~~~json
{
  "source": "00bbf82c",
  "target": "00bbf838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf834`](#insn-00bbf834)

~~~json
{
  "source": "00bbf834",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf838`](#insn-00bbf838)

~~~json
{
  "source": "00bbf838",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf844`](#insn-00bbf844)

~~~json
{
  "source": "00bbf844",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf84c`](#insn-00bbf84c)

~~~json
{
  "source": "00bbf84c",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf860`](#insn-00bbf860)

~~~json
{
  "source": "00bbf860",
  "target": "00bbfa24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf868`](#insn-00bbf868)

~~~json
{
  "source": "00bbf868",
  "target": "00bbf8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf874`](#insn-00bbf874)

~~~json
{
  "source": "00bbf874",
  "target": "00bbf890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf880`](#insn-00bbf880)

~~~json
{
  "source": "00bbf880",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf888`](#insn-00bbf888)

~~~json
{
  "source": "00bbf888",
  "target": "00bbf898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf88c`](#insn-00bbf88c)

~~~json
{
  "source": "00bbf88c",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf894`](#insn-00bbf894)

~~~json
{
  "source": "00bbf894",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8a0`](#insn-00bbf8a0)

~~~json
{
  "source": "00bbf8a0",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8b0`](#insn-00bbf8b0)

~~~json
{
  "source": "00bbf8b0",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8b8`](#insn-00bbf8b8)

~~~json
{
  "source": "00bbf8b8",
  "target": "00bbf93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8c8`](#insn-00bbf8c8)

~~~json
{
  "source": "00bbf8c8",
  "target": "00bbf93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8d4`](#insn-00bbf8d4)

~~~json
{
  "source": "00bbf8d4",
  "target": "00bbf8f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8e0`](#insn-00bbf8e0)

~~~json
{
  "source": "00bbf8e0",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8e8`](#insn-00bbf8e8)

~~~json
{
  "source": "00bbf8e8",
  "target": "00bbf8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8ec`](#insn-00bbf8ec)

~~~json
{
  "source": "00bbf8ec",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf8f4`](#insn-00bbf8f4)

~~~json
{
  "source": "00bbf8f4",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf904`](#insn-00bbf904)

~~~json
{
  "source": "00bbf904",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf91c`](#insn-00bbf91c)

~~~json
{
  "source": "00bbf91c",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf924`](#insn-00bbf924)

~~~json
{
  "source": "00bbf924",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf930`](#insn-00bbf930)

~~~json
{
  "source": "00bbf930",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf938`](#insn-00bbf938)

~~~json
{
  "source": "00bbf938",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf940`](#insn-00bbf940)

~~~json
{
  "source": "00bbf940",
  "target": "00bbfa24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf948`](#insn-00bbf948)

~~~json
{
  "source": "00bbf948",
  "target": "00bbf994",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf954`](#insn-00bbf954)

~~~json
{
  "source": "00bbf954",
  "target": "00bbf970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf960`](#insn-00bbf960)

~~~json
{
  "source": "00bbf960",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf968`](#insn-00bbf968)

~~~json
{
  "source": "00bbf968",
  "target": "00bbf978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf96c`](#insn-00bbf96c)

~~~json
{
  "source": "00bbf96c",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf974`](#insn-00bbf974)

~~~json
{
  "source": "00bbf974",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf980`](#insn-00bbf980)

~~~json
{
  "source": "00bbf980",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf990`](#insn-00bbf990)

~~~json
{
  "source": "00bbf990",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf998`](#insn-00bbf998)

~~~json
{
  "source": "00bbf998",
  "target": "00bbfa24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9a8`](#insn-00bbf9a8)

~~~json
{
  "source": "00bbf9a8",
  "target": "00bbfa24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9b4`](#insn-00bbf9b4)

~~~json
{
  "source": "00bbf9b4",
  "target": "00bbf9d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9c0`](#insn-00bbf9c0)

~~~json
{
  "source": "00bbf9c0",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9c8`](#insn-00bbf9c8)

~~~json
{
  "source": "00bbf9c8",
  "target": "00bbf9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9cc`](#insn-00bbf9cc)

~~~json
{
  "source": "00bbf9cc",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9d4`](#insn-00bbf9d4)

~~~json
{
  "source": "00bbf9d4",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9e4`](#insn-00bbf9e4)

~~~json
{
  "source": "00bbf9e4",
  "target": "00bbfa1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf9fc`](#insn-00bbf9fc)

~~~json
{
  "source": "00bbf9fc",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa04`](#insn-00bbfa04)

~~~json
{
  "source": "00bbfa04",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa10`](#insn-00bbfa10)

~~~json
{
  "source": "00bbfa10",
  "target": "00bbfa2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfa18`](#insn-00bbfa18)

~~~json
{
  "source": "00bbfa18",
  "target": "00bbfa24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
