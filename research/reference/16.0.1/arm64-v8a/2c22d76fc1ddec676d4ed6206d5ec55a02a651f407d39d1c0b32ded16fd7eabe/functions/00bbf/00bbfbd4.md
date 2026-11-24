# 00bbfbd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbf7ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbf7ac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-33cf2ae66d4472d78cd9eb66d4f8924a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbfc70`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbf/00bbfc70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-eb6fa221687d7e22dd1298d2280f7967)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfbd4",
  "name": "_ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 648,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d576c4b4504091f8659167bd3dd6903343e6fee7d512604689844383e0861a6",
  "source_text_sha256": "2d576c4b4504091f8659167bd3dd6903343e6fee7d512604689844383e0861a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfbd4",
        "00bbfe5b"
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

- [00c5d530](../00c5d/00c5d530.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5729 bytes

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
                    /* try { // try from 00bbfc4c to 00cbfc5b has its CatchHandler @ 00bc0374 */
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
                    /* try { // try from 00bbfc78 to 00cbfc97 has its CatchHandler @ 00bc02e8 */
        puVar13 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar13) {
          if ((ulong)puVar13[2] != 0) {
            uVar12 = uVar11 + puVar13[2];
                    /* try { // try from 00bbfc98 to 00cbfd2f has its CatchHandler @ 00bbfaa8 */
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
            if ((int)*(uint *)(lVar8 + uVar12) < 1) {
              return 0;
            }
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
                    /* try { // try from 00bbfd30 to 00cbfd3b has its CatchHandler @ 00bc02e0 */
            uVar3 = (ulong)*puVar4 + 4;
            if (uVar9 - 1 < uVar3 + uVar12) {
              return 0;
            }
                    /* try { // try from 00bbfd48 to 00cbfd57 has its CatchHandler @ 00bc02d4 */
            if (uVar9 <= uVar3) {
              return 0;
            }
                    /* try { // try from 00bbfd58 to 00cbfd83 has its CatchHandler @ 00bc02bc */
            if (uVar9 - uVar3 < uVar12) {
              return 0;
            }
            if (*(char *)(lVar8 + uVar3 + uVar12) != '\0') {
              return 0;
            }
          }
          if (6 < *puVar13) {
            if ((ulong)puVar13[3] != 0) {
              uVar11 = uVar11 + puVar13[3];
              if ((uVar11 & 3) == 0) {
                if (uVar10 < uVar11) {
                  return 0;
                }
              }
              else {
                    /* try { // try from 00bbfd84 to 00cbfe1f has its CatchHandler @ 00bbfaa8 */
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
                    /* try { // try from 00bbfe20 to 00cbfe2b has its CatchHandler @ 00bc02ac */
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
<a id="insn-00bbfbd4"></a> `00bbfbd4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bbfbd8"></a> `00bbfbd8` | `0d 00 09 cb` | sub x13,x0,x9 | `FALL_THROUGH`
<a id="insn-00bbfbdc"></a> `00bbfbdc` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfbe0"></a> `00bbfbe0` | `60 00 00 54` | b.eq 0x00bbfbec | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe4"></a> `00bbfbe4` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfbe8"></a> `00bbfbe8` | `e8 12 00 35` | cbnz w8,0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbec"></a> `00bbfbec` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfbf0"></a> `00bbfbf0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfbf4"></a> `00bbfbf4` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfbf8"></a> `00bbfbf8` | `e3 12 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbfc"></a> `00bbfbfc` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfc00"></a> `00bbfc00` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfc04"></a> `00bbfc04` | `83 12 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc08"></a> `00bbfc08` | `2b 38 47 29` | ldp w11,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfc0c"></a> `00bbfc0c` | `2f 10 40 b9` | ldr w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc10"></a> `00bbfc10` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbfc14"></a> `00bbfc14` | `70 05 00 11` | add w16,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc18"></a> `00bbfc18` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc1c"></a> `00bbfc1c` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bbfc20"></a> `00bbfc20` | `30 38 07 29` | stp w16,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfc24"></a> `00bbfc24` | `08 11 00 54` | b.hi 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc28"></a> `00bbfc28` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00bbfc2c"></a> `00bbfc2c` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00bbfc30"></a> `00bbfc30` | `a8 10 00 54` | b.hi 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc34"></a> `00bbfc34` | `ae 01 08 cb` | sub x14,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbfc38"></a> `00bbfc38` | `6e 00 00 36` | tbz w14,#0x0,0x00bbfc44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc3c"></a> `00bbfc3c` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfc40"></a> `00bbfc40` | `28 10 00 35` | cbnz w8,0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc44"></a> `00bbfc44` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfc48"></a> `00bbfc48` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00bbfc4c"></a> `00bbfc4c` | `c3 0f 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc50"></a> `00bbfc50` | `28 69 6e 78` | ldrh w8,[x9, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfc54"></a> `00bbfc54` | `68 00 00 36` | tbz w8,#0x0,0x00bbfc60 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc58"></a> `00bbfc58` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfc5c"></a> `00bbfc5c` | `4f 0f 00 35` | cbnz w15,0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc60"></a> `00bbfc60` | `28 0f 00 37` | tbnz w8,#0x0,0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc64"></a> `00bbfc64` | `4f 01 08 eb` | subs x15,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbfc68"></a> `00bbfc68` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfc6c"></a> `00bbfc6c` | `49 0f 00 54` | b.ls 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc70"></a> `00bbfc70` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bbfc74"></a> `00bbfc74` | `03 0f 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc78"></a> `00bbfc78` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbfc7c"></a> `00bbfc7c` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfc80"></a> `00bbfc80` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00bbfc84"></a> `00bbfc84` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfc88"></a> `00bbfc88` | `23 0e 00 54` | b.cc 0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc8c"></a> `00bbfc8c` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfc90"></a> `00bbfc90` | `68 02 00 b4` | cbz x8,0x00bbfcdc | `CONDITIONAL_JUMP`
<a id="insn-00bbfc94"></a> `00bbfc94` | `b0 01 08 8b` | add x16,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbfc98"></a> `00bbfc98` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfc9c"></a> `00bbfc9c` | `e0 00 00 54` | b.eq 0x00bbfcb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfca0"></a> `00bbfca0` | `31 60 40 39` | ldrb w17,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfca4"></a> `00bbfca4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfca8"></a> `00bbfca8` | `71 0d 00 35` | cbnz w17,0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcac"></a> `00bbfcac` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbfcb0"></a> `00bbfcb0` | `82 00 00 54` | b.cs 0x00bbfcc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcb4"></a> `00bbfcb4` | `68 00 00 14` | b 0x00bbfe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfcb8"></a> `00bbfcb8` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbfcbc"></a> `00bbfcbc` | `43 0c 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcc0"></a> `00bbfcc0` | `28 69 70 b8` | ldr w8,[x9, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfcc4"></a> `00bbfcc4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfcc8"></a> `00bbfcc8` | `eb 0b 00 54` | b.lt 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfccc"></a> `00bbfccc` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00bbfcd0"></a> `00bbfcd0` | `50 05 00 d1` | sub x16,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfcd4"></a> `00bbfcd4` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00bbfcd8"></a> `00bbfcd8` | `63 0b 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcdc"></a> `00bbfcdc` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bbfce0"></a> `00bbfce0` | `28 04 00 b4` | cbz x8,0x00bbfd64 | `CONDITIONAL_JUMP`
<a id="insn-00bbfce4"></a> `00bbfce4` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfce8"></a> `00bbfce8` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00bbfcec"></a> `00bbfcec` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00bbfcf0"></a> `00bbfcf0` | `a0 03 00 54` | b.eq 0x00bbfd64 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcf4"></a> `00bbfcf4` | `30 02 09 cb` | sub x16,x17,x9 | `FALL_THROUGH`
<a id="insn-00bbfcf8"></a> `00bbfcf8` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfcfc"></a> `00bbfcfc` | `e0 00 00 54` | b.eq 0x00bbfd18 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd00"></a> `00bbfd00` | `22 60 40 39` | ldrb w2,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfd04"></a> `00bbfd04` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfd08"></a> `00bbfd08` | `62 0a 00 35` | cbnz w2,0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd0c"></a> `00bbfd0c` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbfd10"></a> `00bbfd10` | `82 00 00 54` | b.cs 0x00bbfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd14"></a> `00bbfd14` | `50 00 00 14` | b 0x00bbfe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfd18"></a> `00bbfd18` | `9f 01 10 eb` | cmp x12,x16 | `FALL_THROUGH`
<a id="insn-00bbfd1c"></a> `00bbfd1c` | `43 09 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd20"></a> `00bbfd20` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00bbfd24"></a> `00bbfd24` | `31 10 40 f9` | ldr x17,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfd28"></a> `00bbfd28` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bbfd2c"></a> `00bbfd2c` | `c9 08 00 54` | b.ls 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd30"></a> `00bbfd30` | `02 11 00 91` | add x2,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfd34"></a> `00bbfd34` | `51 00 10 8b` | add x17,x2,x16 | `FALL_THROUGH`
<a id="insn-00bbfd38"></a> `00bbfd38` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd3c"></a> `00bbfd3c` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00bbfd40"></a> `00bbfd40` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfd44"></a> `00bbfd44` | `83 08 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd48"></a> `00bbfd48` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-00bbfd4c"></a> `00bbfd4c` | `49 08 00 54` | b.ls 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd50"></a> `00bbfd50` | `42 01 02 cb` | sub x2,x10,x2 | `FALL_THROUGH`
<a id="insn-00bbfd54"></a> `00bbfd54` | `5f 00 10 eb` | cmp x2,x16 | `FALL_THROUGH`
<a id="insn-00bbfd58"></a> `00bbfd58` | `e3 07 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd5c"></a> `00bbfd5c` | `28 69 71 38` | ldrb w8,[x9, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfd60"></a> `00bbfd60` | `28 07 00 35` | cbnz w8,0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd64"></a> `00bbfd64` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00bbfd68"></a> `00bbfd68` | `23 07 00 54` | b.cc 0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd6c"></a> `00bbfd6c` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00bbfd70"></a> `00bbfd70` | `68 02 00 b4` | cbz x8,0x00bbfdbc | `CONDITIONAL_JUMP`
<a id="insn-00bbfd74"></a> `00bbfd74` | `ad 01 08 8b` | add x13,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbfd78"></a> `00bbfd78` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfd7c"></a> `00bbfd7c` | `e0 00 00 54` | b.eq 0x00bbfd98 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd80"></a> `00bbfd80` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfd84"></a> `00bbfd84` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfd88"></a> `00bbfd88` | `6f 06 00 35` | cbnz w15,0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd8c"></a> `00bbfd8c` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfd90"></a> `00bbfd90` | `82 00 00 54` | b.cs 0x00bbfda0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd94"></a> `00bbfd94` | `30 00 00 14` | b 0x00bbfe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfd98"></a> `00bbfd98` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfd9c"></a> `00bbfd9c` | `43 05 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfda0"></a> `00bbfda0` | `28 69 6d b8` | ldr w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bbfda4"></a> `00bbfda4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfda8"></a> `00bbfda8` | `eb 04 00 54` | b.lt 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdac"></a> `00bbfdac` | `a8 01 08 8b` | add x8,x13,x8 | `FALL_THROUGH`
<a id="insn-00bbfdb0"></a> `00bbfdb0` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfdb4"></a> `00bbfdb4` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bbfdb8"></a> `00bbfdb8` | `63 04 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdbc"></a> `00bbfdbc` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00bbfdc0"></a> `00bbfdc0` | `68 04 00 b4` | cbz x8,0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfdc4"></a> `00bbfdc4` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfdc8"></a> `00bbfdc8` | `0d 01 40 b9` | ldr w13,[x8] | `FALL_THROUGH`
<a id="insn-00bbfdcc"></a> `00bbfdcc` | `0e 01 0d ab` | adds x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00bbfdd0"></a> `00bbfdd0` | `e0 03 00 54` | b.eq 0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfdd4"></a> `00bbfdd4` | `cd 01 09 cb` | sub x13,x14,x9 | `FALL_THROUGH`
<a id="insn-00bbfdd8"></a> `00bbfdd8` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfddc"></a> `00bbfddc` | `e0 00 00 54` | b.eq 0x00bbfdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfde0"></a> `00bbfde0` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfde4"></a> `00bbfde4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfde8"></a> `00bbfde8` | `6f 03 00 35` | cbnz w15,0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdec"></a> `00bbfdec` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfdf0"></a> `00bbfdf0` | `82 00 00 54` | b.cs 0x00bbfe00 | `CONDITIONAL_JUMP`
<a id="insn-00bbfdf4"></a> `00bbfdf4` | `18 00 00 14` | b 0x00bbfe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfdf8"></a> `00bbfdf8` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bbfdfc"></a> `00bbfdfc` | `43 02 00 54` | b.cc 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe00"></a> `00bbfe00` | `c8 01 40 b9` | ldr w8,[x14] | `FALL_THROUGH`
<a id="insn-00bbfe04"></a> `00bbfe04` | `2c 10 40 f9` | ldr x12,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfe08"></a> `00bbfe08` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bbfe0c"></a> `00bbfe0c` | `c9 01 00 54` | b.ls 0x00bbfe44 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe10"></a> `00bbfe10` | `0e 11 00 91` | add x14,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfe14"></a> `00bbfe14` | `cc 01 0d 8b` | add x12,x14,x13 | `FALL_THROUGH`
<a id="insn-00bbfe18"></a> `00bbfe18` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfe1c"></a> `00bbfe1c` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00bbfe20"></a> `00bbfe20` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bbfe24"></a> `00bbfe24` | `83 01 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe28"></a> `00bbfe28` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00bbfe2c"></a> `00bbfe2c` | `49 01 00 54` | b.ls 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe30"></a> `00bbfe30` | `4a 01 0e cb` | sub x10,x10,x14 | `FALL_THROUGH`
<a id="insn-00bbfe34"></a> `00bbfe34` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00bbfe38"></a> `00bbfe38` | `e3 00 00 54` | b.cc 0x00bbfe54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfe3c"></a> `00bbfe3c` | `28 69 6c 38` | ldrb w8,[x9, x12, LSL ] | `FALL_THROUGH`
<a id="insn-00bbfe40"></a> `00bbfe40` | `68 00 00 34` | cbz w8,0x00bbfe4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfe44"></a> `00bbfe44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbfe48"></a> `00bbfe48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfe4c"></a> `00bbfe4c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfe50"></a> `00bbfe50` | `2b 38 00 b9` | str w11,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bbfe54"></a> `00bbfe54` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bbfe58"></a> `00bbfe58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfbd4`](#insn-00bbfbd4) 範囲 `[['00bbfbd4', '00bbfbe3']]`
  - `CONDITIONAL_JUMP` [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfbec`](#insn-00bbfbec)
  - `FALL_THROUGH` [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfbe4`](#insn-00bbfbe4)
- ブロック [`00bbfbe4`](#insn-00bbfbe4) 範囲 `[['00bbfbe4', '00bbfbeb']]`
  - `CONDITIONAL_JUMP` [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfbec`](#insn-00bbfbec)
- ブロック [`00bbfbec`](#insn-00bbfbec) 範囲 `[['00bbfbec', '00bbfbfb']]`
  - `CONDITIONAL_JUMP` [`00bbfbf8`](#insn-00bbfbf8) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfbf8`](#insn-00bbfbf8) → [`00bbfbfc`](#insn-00bbfbfc)
- ブロック [`00bbfbfc`](#insn-00bbfbfc) 範囲 `[['00bbfbfc', '00bbfc07']]`
  - `CONDITIONAL_JUMP` [`00bbfc04`](#insn-00bbfc04) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfc04`](#insn-00bbfc04) → [`00bbfc08`](#insn-00bbfc08)
- ブロック [`00bbfc08`](#insn-00bbfc08) 範囲 `[['00bbfc08', '00bbfc27']]`
  - `CONDITIONAL_JUMP` [`00bbfc24`](#insn-00bbfc24) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc24`](#insn-00bbfc24) → [`00bbfc28`](#insn-00bbfc28)
- ブロック [`00bbfc28`](#insn-00bbfc28) 範囲 `[['00bbfc28', '00bbfc33']]`
  - `CONDITIONAL_JUMP` [`00bbfc30`](#insn-00bbfc30) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc30`](#insn-00bbfc30) → [`00bbfc34`](#insn-00bbfc34)
- ブロック [`00bbfc34`](#insn-00bbfc34) 範囲 `[['00bbfc34', '00bbfc3b']]`
  - `CONDITIONAL_JUMP` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc44`](#insn-00bbfc44)
  - `FALL_THROUGH` [`00bbfc38`](#insn-00bbfc38) → [`00bbfc3c`](#insn-00bbfc3c)
- ブロック [`00bbfc3c`](#insn-00bbfc3c) 範囲 `[['00bbfc3c', '00bbfc43']]`
  - `CONDITIONAL_JUMP` [`00bbfc40`](#insn-00bbfc40) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc40`](#insn-00bbfc40) → [`00bbfc44`](#insn-00bbfc44)
- ブロック [`00bbfc44`](#insn-00bbfc44) 範囲 `[['00bbfc44', '00bbfc4b']]`
  - `FALL_THROUGH` [`00bbfc48`](#insn-00bbfc48) → [`00bbfc4c`](#insn-00bbfc4c)
- ブロック [`00bbfc4c`](#insn-00bbfc4c) 範囲 `[['00bbfc4c', '00bbfc4f']]`
  - `CONDITIONAL_JUMP` [`00bbfc4c`](#insn-00bbfc4c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc4c`](#insn-00bbfc4c) → [`00bbfc50`](#insn-00bbfc50)
- ブロック [`00bbfc50`](#insn-00bbfc50) 範囲 `[['00bbfc50', '00bbfc57']]`
  - `CONDITIONAL_JUMP` [`00bbfc54`](#insn-00bbfc54) → [`00bbfc60`](#insn-00bbfc60)
  - `FALL_THROUGH` [`00bbfc54`](#insn-00bbfc54) → [`00bbfc58`](#insn-00bbfc58)
- ブロック [`00bbfc58`](#insn-00bbfc58) 範囲 `[['00bbfc58', '00bbfc5f']]`
  - `CONDITIONAL_JUMP` [`00bbfc5c`](#insn-00bbfc5c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc5c`](#insn-00bbfc5c) → [`00bbfc60`](#insn-00bbfc60)
- ブロック [`00bbfc60`](#insn-00bbfc60) 範囲 `[['00bbfc60', '00bbfc63']]`
  - `CONDITIONAL_JUMP` [`00bbfc60`](#insn-00bbfc60) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfc60`](#insn-00bbfc60) → [`00bbfc64`](#insn-00bbfc64)
- ブロック [`00bbfc64`](#insn-00bbfc64) 範囲 `[['00bbfc64', '00bbfc6f']]`
  - `CONDITIONAL_JUMP` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfc70`](#insn-00bbfc70)
- ブロック [`00bbfc70`](#insn-00bbfc70) 範囲 `[['00bbfc70', '00bbfc77']]`
  - `CONDITIONAL_JUMP` [`00bbfc74`](#insn-00bbfc74) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfc74`](#insn-00bbfc74) → [`00bbfc78`](#insn-00bbfc78)
- ブロック [`00bbfc78`](#insn-00bbfc78) 範囲 `[['00bbfc78', '00bbfc8b']]`
  - `CONDITIONAL_JUMP` [`00bbfc88`](#insn-00bbfc88) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfc88`](#insn-00bbfc88) → [`00bbfc8c`](#insn-00bbfc8c)
- ブロック [`00bbfc8c`](#insn-00bbfc8c) 範囲 `[['00bbfc8c', '00bbfc93']]`
  - `CONDITIONAL_JUMP` [`00bbfc90`](#insn-00bbfc90) → [`00bbfcdc`](#insn-00bbfcdc)
  - `FALL_THROUGH` [`00bbfc90`](#insn-00bbfc90) → [`00bbfc94`](#insn-00bbfc94)
- ブロック [`00bbfc94`](#insn-00bbfc94) 範囲 `[['00bbfc94', '00bbfc97']]`
  - `FALL_THROUGH` [`00bbfc94`](#insn-00bbfc94) → [`00bbfc98`](#insn-00bbfc98)
- ブロック [`00bbfc98`](#insn-00bbfc98) 範囲 `[['00bbfc98', '00bbfc9f']]`
  - `CONDITIONAL_JUMP` [`00bbfc9c`](#insn-00bbfc9c) → [`00bbfcb8`](#insn-00bbfcb8)
  - `FALL_THROUGH` [`00bbfc9c`](#insn-00bbfc9c) → [`00bbfca0`](#insn-00bbfca0)
- ブロック [`00bbfca0`](#insn-00bbfca0) 範囲 `[['00bbfca0', '00bbfcab']]`
  - `CONDITIONAL_JUMP` [`00bbfca8`](#insn-00bbfca8) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfca8`](#insn-00bbfca8) → [`00bbfcac`](#insn-00bbfcac)
- ブロック [`00bbfcac`](#insn-00bbfcac) 範囲 `[['00bbfcac', '00bbfcb3']]`
  - `CONDITIONAL_JUMP` [`00bbfcb0`](#insn-00bbfcb0) → [`00bbfcc0`](#insn-00bbfcc0)
  - `FALL_THROUGH` [`00bbfcb0`](#insn-00bbfcb0) → [`00bbfcb4`](#insn-00bbfcb4)
- ブロック [`00bbfcb4`](#insn-00bbfcb4) 範囲 `[['00bbfcb4', '00bbfcb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbfcb4`](#insn-00bbfcb4) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfcb8`](#insn-00bbfcb8) 範囲 `[['00bbfcb8', '00bbfcbf']]`
  - `CONDITIONAL_JUMP` [`00bbfcbc`](#insn-00bbfcbc) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfcbc`](#insn-00bbfcbc) → [`00bbfcc0`](#insn-00bbfcc0)
- ブロック [`00bbfcc0`](#insn-00bbfcc0) 範囲 `[['00bbfcc0', '00bbfccb']]`
  - `CONDITIONAL_JUMP` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfccc`](#insn-00bbfccc)
- ブロック [`00bbfccc`](#insn-00bbfccc) 範囲 `[['00bbfccc', '00bbfcdb']]`
  - `CONDITIONAL_JUMP` [`00bbfcd8`](#insn-00bbfcd8) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfcd8`](#insn-00bbfcd8) → [`00bbfcdc`](#insn-00bbfcdc)
- ブロック [`00bbfcdc`](#insn-00bbfcdc) 範囲 `[['00bbfcdc', '00bbfce3']]`
  - `CONDITIONAL_JUMP` [`00bbfce0`](#insn-00bbfce0) → [`00bbfd64`](#insn-00bbfd64)
  - `FALL_THROUGH` [`00bbfce0`](#insn-00bbfce0) → [`00bbfce4`](#insn-00bbfce4)
- ブロック [`00bbfce4`](#insn-00bbfce4) 範囲 `[['00bbfce4', '00bbfcf3']]`
  - `CONDITIONAL_JUMP` [`00bbfcf0`](#insn-00bbfcf0) → [`00bbfd64`](#insn-00bbfd64)
  - `FALL_THROUGH` [`00bbfcf0`](#insn-00bbfcf0) → [`00bbfcf4`](#insn-00bbfcf4)
- ブロック [`00bbfcf4`](#insn-00bbfcf4) 範囲 `[['00bbfcf4', '00bbfcff']]`
  - `CONDITIONAL_JUMP` [`00bbfcfc`](#insn-00bbfcfc) → [`00bbfd18`](#insn-00bbfd18)
  - `FALL_THROUGH` [`00bbfcfc`](#insn-00bbfcfc) → [`00bbfd00`](#insn-00bbfd00)
- ブロック [`00bbfd00`](#insn-00bbfd00) 範囲 `[['00bbfd00', '00bbfd0b']]`
  - `CONDITIONAL_JUMP` [`00bbfd08`](#insn-00bbfd08) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfd08`](#insn-00bbfd08) → [`00bbfd0c`](#insn-00bbfd0c)
- ブロック [`00bbfd0c`](#insn-00bbfd0c) 範囲 `[['00bbfd0c', '00bbfd13']]`
  - `CONDITIONAL_JUMP` [`00bbfd10`](#insn-00bbfd10) → [`00bbfd20`](#insn-00bbfd20)
  - `FALL_THROUGH` [`00bbfd10`](#insn-00bbfd10) → [`00bbfd14`](#insn-00bbfd14)
- ブロック [`00bbfd14`](#insn-00bbfd14) 範囲 `[['00bbfd14', '00bbfd17']]`
  - `UNCONDITIONAL_JUMP` [`00bbfd14`](#insn-00bbfd14) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfd18`](#insn-00bbfd18) 範囲 `[['00bbfd18', '00bbfd1f']]`
  - `CONDITIONAL_JUMP` [`00bbfd1c`](#insn-00bbfd1c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfd1c`](#insn-00bbfd1c) → [`00bbfd20`](#insn-00bbfd20)
- ブロック [`00bbfd20`](#insn-00bbfd20) 範囲 `[['00bbfd20', '00bbfd2f']]`
  - `CONDITIONAL_JUMP` [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfd30`](#insn-00bbfd30)
- ブロック [`00bbfd30`](#insn-00bbfd30) 範囲 `[['00bbfd30', '00bbfd47']]`
  - `CONDITIONAL_JUMP` [`00bbfd44`](#insn-00bbfd44) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfd44`](#insn-00bbfd44) → [`00bbfd48`](#insn-00bbfd48)
- ブロック [`00bbfd48`](#insn-00bbfd48) 範囲 `[['00bbfd48', '00bbfd4f']]`
  - `CONDITIONAL_JUMP` [`00bbfd4c`](#insn-00bbfd4c) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfd4c`](#insn-00bbfd4c) → [`00bbfd50`](#insn-00bbfd50)
- ブロック [`00bbfd50`](#insn-00bbfd50) 範囲 `[['00bbfd50', '00bbfd57']]`
  - `FALL_THROUGH` [`00bbfd54`](#insn-00bbfd54) → [`00bbfd58`](#insn-00bbfd58)
- ブロック [`00bbfd58`](#insn-00bbfd58) 範囲 `[['00bbfd58', '00bbfd5b']]`
  - `CONDITIONAL_JUMP` [`00bbfd58`](#insn-00bbfd58) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfd58`](#insn-00bbfd58) → [`00bbfd5c`](#insn-00bbfd5c)
- ブロック [`00bbfd5c`](#insn-00bbfd5c) 範囲 `[['00bbfd5c', '00bbfd63']]`
  - `CONDITIONAL_JUMP` [`00bbfd60`](#insn-00bbfd60) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfd60`](#insn-00bbfd60) → [`00bbfd64`](#insn-00bbfd64)
- ブロック [`00bbfd64`](#insn-00bbfd64) 範囲 `[['00bbfd64', '00bbfd6b']]`
  - `CONDITIONAL_JUMP` [`00bbfd68`](#insn-00bbfd68) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfd68`](#insn-00bbfd68) → [`00bbfd6c`](#insn-00bbfd6c)
- ブロック [`00bbfd6c`](#insn-00bbfd6c) 範囲 `[['00bbfd6c', '00bbfd73']]`
  - `CONDITIONAL_JUMP` [`00bbfd70`](#insn-00bbfd70) → [`00bbfdbc`](#insn-00bbfdbc)
  - `FALL_THROUGH` [`00bbfd70`](#insn-00bbfd70) → [`00bbfd74`](#insn-00bbfd74)
- ブロック [`00bbfd74`](#insn-00bbfd74) 範囲 `[['00bbfd74', '00bbfd7f']]`
  - `CONDITIONAL_JUMP` [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd98`](#insn-00bbfd98)
  - `FALL_THROUGH` [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd80`](#insn-00bbfd80)
- ブロック [`00bbfd80`](#insn-00bbfd80) 範囲 `[['00bbfd80', '00bbfd83']]`
  - `FALL_THROUGH` [`00bbfd80`](#insn-00bbfd80) → [`00bbfd84`](#insn-00bbfd84)
- ブロック [`00bbfd84`](#insn-00bbfd84) 範囲 `[['00bbfd84', '00bbfd8b']]`
  - `CONDITIONAL_JUMP` [`00bbfd88`](#insn-00bbfd88) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfd88`](#insn-00bbfd88) → [`00bbfd8c`](#insn-00bbfd8c)
- ブロック [`00bbfd8c`](#insn-00bbfd8c) 範囲 `[['00bbfd8c', '00bbfd93']]`
  - `CONDITIONAL_JUMP` [`00bbfd90`](#insn-00bbfd90) → [`00bbfda0`](#insn-00bbfda0)
  - `FALL_THROUGH` [`00bbfd90`](#insn-00bbfd90) → [`00bbfd94`](#insn-00bbfd94)
- ブロック [`00bbfd94`](#insn-00bbfd94) 範囲 `[['00bbfd94', '00bbfd97']]`
  - `UNCONDITIONAL_JUMP` [`00bbfd94`](#insn-00bbfd94) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfd98`](#insn-00bbfd98) 範囲 `[['00bbfd98', '00bbfd9f']]`
  - `CONDITIONAL_JUMP` [`00bbfd9c`](#insn-00bbfd9c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfd9c`](#insn-00bbfd9c) → [`00bbfda0`](#insn-00bbfda0)
- ブロック [`00bbfda0`](#insn-00bbfda0) 範囲 `[['00bbfda0', '00bbfdab']]`
  - `CONDITIONAL_JUMP` [`00bbfda8`](#insn-00bbfda8) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfda8`](#insn-00bbfda8) → [`00bbfdac`](#insn-00bbfdac)
- ブロック [`00bbfdac`](#insn-00bbfdac) 範囲 `[['00bbfdac', '00bbfdbb']]`
  - `CONDITIONAL_JUMP` [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfdbc`](#insn-00bbfdbc)
- ブロック [`00bbfdbc`](#insn-00bbfdbc) 範囲 `[['00bbfdbc', '00bbfdc3']]`
  - `CONDITIONAL_JUMP` [`00bbfdc0`](#insn-00bbfdc0) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfdc0`](#insn-00bbfdc0) → [`00bbfdc4`](#insn-00bbfdc4)
- ブロック [`00bbfdc4`](#insn-00bbfdc4) 範囲 `[['00bbfdc4', '00bbfdd3']]`
  - `CONDITIONAL_JUMP` [`00bbfdd0`](#insn-00bbfdd0) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfdd0`](#insn-00bbfdd0) → [`00bbfdd4`](#insn-00bbfdd4)
- ブロック [`00bbfdd4`](#insn-00bbfdd4) 範囲 `[['00bbfdd4', '00bbfddf']]`
  - `CONDITIONAL_JUMP` [`00bbfddc`](#insn-00bbfddc) → [`00bbfdf8`](#insn-00bbfdf8)
  - `FALL_THROUGH` [`00bbfddc`](#insn-00bbfddc) → [`00bbfde0`](#insn-00bbfde0)
- ブロック [`00bbfde0`](#insn-00bbfde0) 範囲 `[['00bbfde0', '00bbfdeb']]`
  - `CONDITIONAL_JUMP` [`00bbfde8`](#insn-00bbfde8) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfde8`](#insn-00bbfde8) → [`00bbfdec`](#insn-00bbfdec)
- ブロック [`00bbfdec`](#insn-00bbfdec) 範囲 `[['00bbfdec', '00bbfdf3']]`
  - `CONDITIONAL_JUMP` [`00bbfdf0`](#insn-00bbfdf0) → [`00bbfe00`](#insn-00bbfe00)
  - `FALL_THROUGH` [`00bbfdf0`](#insn-00bbfdf0) → [`00bbfdf4`](#insn-00bbfdf4)
- ブロック [`00bbfdf4`](#insn-00bbfdf4) 範囲 `[['00bbfdf4', '00bbfdf7']]`
  - `UNCONDITIONAL_JUMP` [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfdf8`](#insn-00bbfdf8) 範囲 `[['00bbfdf8', '00bbfdff']]`
  - `CONDITIONAL_JUMP` [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe00`](#insn-00bbfe00)
- ブロック [`00bbfe00`](#insn-00bbfe00) 範囲 `[['00bbfe00', '00bbfe0f']]`
  - `CONDITIONAL_JUMP` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe44`](#insn-00bbfe44)
  - `FALL_THROUGH` [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe10`](#insn-00bbfe10)
- ブロック [`00bbfe10`](#insn-00bbfe10) 範囲 `[['00bbfe10', '00bbfe1f']]`
  - `FALL_THROUGH` [`00bbfe1c`](#insn-00bbfe1c) → [`00bbfe20`](#insn-00bbfe20)
- ブロック [`00bbfe20`](#insn-00bbfe20) 範囲 `[['00bbfe20', '00bbfe27']]`
  - `CONDITIONAL_JUMP` [`00bbfe24`](#insn-00bbfe24) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfe24`](#insn-00bbfe24) → [`00bbfe28`](#insn-00bbfe28)
- ブロック [`00bbfe28`](#insn-00bbfe28) 範囲 `[['00bbfe28', '00bbfe2f']]`
  - `CONDITIONAL_JUMP` [`00bbfe2c`](#insn-00bbfe2c) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfe2c`](#insn-00bbfe2c) → [`00bbfe30`](#insn-00bbfe30)
- ブロック [`00bbfe30`](#insn-00bbfe30) 範囲 `[['00bbfe30', '00bbfe3b']]`
  - `CONDITIONAL_JUMP` [`00bbfe38`](#insn-00bbfe38) → [`00bbfe54`](#insn-00bbfe54)
  - `FALL_THROUGH` [`00bbfe38`](#insn-00bbfe38) → [`00bbfe3c`](#insn-00bbfe3c)
- ブロック [`00bbfe3c`](#insn-00bbfe3c) 範囲 `[['00bbfe3c', '00bbfe43']]`
  - `CONDITIONAL_JUMP` [`00bbfe40`](#insn-00bbfe40) → [`00bbfe4c`](#insn-00bbfe4c)
  - `FALL_THROUGH` [`00bbfe40`](#insn-00bbfe40) → [`00bbfe44`](#insn-00bbfe44)
- ブロック [`00bbfe44`](#insn-00bbfe44) 範囲 `[['00bbfe44', '00bbfe4b']]`
- ブロック [`00bbfe4c`](#insn-00bbfe4c) 範囲 `[['00bbfe4c', '00bbfe53']]`
  - `FALL_THROUGH` [`00bbfe50`](#insn-00bbfe50) → [`00bbfe54`](#insn-00bbfe54)
- ブロック [`00bbfe54`](#insn-00bbfe54) 範囲 `[['00bbfe54', '00bbfe5b']]`

## 命令位置別の参照

- [`00bbfbe0`](#insn-00bbfbe0) → [`00bbfbec`](#insn-00bbfbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe8`](#insn-00bbfbe8) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf8`](#insn-00bbfbf8) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc04`](#insn-00bbfc04) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc24`](#insn-00bbfc24) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc30`](#insn-00bbfc30) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc38`](#insn-00bbfc38) → [`00bbfc44`](#insn-00bbfc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc40`](#insn-00bbfc40) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc4c`](#insn-00bbfc4c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc54`](#insn-00bbfc54) → [`00bbfc60`](#insn-00bbfc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc5c`](#insn-00bbfc5c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc60`](#insn-00bbfc60) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc74`](#insn-00bbfc74) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc88`](#insn-00bbfc88) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc90`](#insn-00bbfc90) → [`00bbfcdc`](#insn-00bbfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc9c`](#insn-00bbfc9c) → [`00bbfcb8`](#insn-00bbfcb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfca8`](#insn-00bbfca8) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcb0`](#insn-00bbfcb0) → [`00bbfcc0`](#insn-00bbfcc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcb4`](#insn-00bbfcb4) → [`00bbfe54`](#insn-00bbfe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcbc`](#insn-00bbfcbc) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcd8`](#insn-00bbfcd8) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfce0`](#insn-00bbfce0) → [`00bbfd64`](#insn-00bbfd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcf0`](#insn-00bbfcf0) → [`00bbfd64`](#insn-00bbfd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcfc`](#insn-00bbfcfc) → [`00bbfd18`](#insn-00bbfd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd08`](#insn-00bbfd08) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd10`](#insn-00bbfd10) → [`00bbfd20`](#insn-00bbfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd14`](#insn-00bbfd14) → [`00bbfe54`](#insn-00bbfe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd1c`](#insn-00bbfd1c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd44`](#insn-00bbfd44) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd4c`](#insn-00bbfd4c) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd58`](#insn-00bbfd58) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd60`](#insn-00bbfd60) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd68`](#insn-00bbfd68) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd70`](#insn-00bbfd70) → [`00bbfdbc`](#insn-00bbfdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd98`](#insn-00bbfd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd88`](#insn-00bbfd88) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd90`](#insn-00bbfd90) → [`00bbfda0`](#insn-00bbfda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd94`](#insn-00bbfd94) → [`00bbfe54`](#insn-00bbfe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd9c`](#insn-00bbfd9c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda8`](#insn-00bbfda8) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdb8`](#insn-00bbfdb8) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdc0`](#insn-00bbfdc0) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd0`](#insn-00bbfdd0) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfddc`](#insn-00bbfddc) → [`00bbfdf8`](#insn-00bbfdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfde8`](#insn-00bbfde8) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf0`](#insn-00bbfdf0) → [`00bbfe00`](#insn-00bbfe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf4`](#insn-00bbfdf4) → [`00bbfe54`](#insn-00bbfe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdfc`](#insn-00bbfdfc) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe0c`](#insn-00bbfe0c) → [`00bbfe44`](#insn-00bbfe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe24`](#insn-00bbfe24) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe2c`](#insn-00bbfe2c) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe38`](#insn-00bbfe38) → [`00bbfe54`](#insn-00bbfe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfe40`](#insn-00bbfe40) → [`00bbfe4c`](#insn-00bbfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfbe0`](#insn-00bbfbe0)

~~~json
{
  "source": "00bbfbe0",
  "target": "00bbfbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbe8`](#insn-00bbfbe8)

~~~json
{
  "source": "00bbfbe8",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf8`](#insn-00bbfbf8)

~~~json
{
  "source": "00bbfbf8",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc04`](#insn-00bbfc04)

~~~json
{
  "source": "00bbfc04",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc24`](#insn-00bbfc24)

~~~json
{
  "source": "00bbfc24",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc30`](#insn-00bbfc30)

~~~json
{
  "source": "00bbfc30",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc38`](#insn-00bbfc38)

~~~json
{
  "source": "00bbfc38",
  "target": "00bbfc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc40`](#insn-00bbfc40)

~~~json
{
  "source": "00bbfc40",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc4c`](#insn-00bbfc4c)

~~~json
{
  "source": "00bbfc4c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc54`](#insn-00bbfc54)

~~~json
{
  "source": "00bbfc54",
  "target": "00bbfc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc5c`](#insn-00bbfc5c)

~~~json
{
  "source": "00bbfc5c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc60`](#insn-00bbfc60)

~~~json
{
  "source": "00bbfc60",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc6c`](#insn-00bbfc6c)

~~~json
{
  "source": "00bbfc6c",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc74`](#insn-00bbfc74)

~~~json
{
  "source": "00bbfc74",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc88`](#insn-00bbfc88)

~~~json
{
  "source": "00bbfc88",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc90`](#insn-00bbfc90)

~~~json
{
  "source": "00bbfc90",
  "target": "00bbfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc9c`](#insn-00bbfc9c)

~~~json
{
  "source": "00bbfc9c",
  "target": "00bbfcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfca8`](#insn-00bbfca8)

~~~json
{
  "source": "00bbfca8",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcb0`](#insn-00bbfcb0)

~~~json
{
  "source": "00bbfcb0",
  "target": "00bbfcc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcb4`](#insn-00bbfcb4)

~~~json
{
  "source": "00bbfcb4",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcbc`](#insn-00bbfcbc)

~~~json
{
  "source": "00bbfcbc",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcc8`](#insn-00bbfcc8)

~~~json
{
  "source": "00bbfcc8",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcd8`](#insn-00bbfcd8)

~~~json
{
  "source": "00bbfcd8",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfce0`](#insn-00bbfce0)

~~~json
{
  "source": "00bbfce0",
  "target": "00bbfd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcf0`](#insn-00bbfcf0)

~~~json
{
  "source": "00bbfcf0",
  "target": "00bbfd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcfc`](#insn-00bbfcfc)

~~~json
{
  "source": "00bbfcfc",
  "target": "00bbfd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd08`](#insn-00bbfd08)

~~~json
{
  "source": "00bbfd08",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd10`](#insn-00bbfd10)

~~~json
{
  "source": "00bbfd10",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd14`](#insn-00bbfd14)

~~~json
{
  "source": "00bbfd14",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd1c`](#insn-00bbfd1c)

~~~json
{
  "source": "00bbfd1c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd2c`](#insn-00bbfd2c)

~~~json
{
  "source": "00bbfd2c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd44`](#insn-00bbfd44)

~~~json
{
  "source": "00bbfd44",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd4c`](#insn-00bbfd4c)

~~~json
{
  "source": "00bbfd4c",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd58`](#insn-00bbfd58)

~~~json
{
  "source": "00bbfd58",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd60`](#insn-00bbfd60)

~~~json
{
  "source": "00bbfd60",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd68`](#insn-00bbfd68)

~~~json
{
  "source": "00bbfd68",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd70`](#insn-00bbfd70)

~~~json
{
  "source": "00bbfd70",
  "target": "00bbfdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd7c`](#insn-00bbfd7c)

~~~json
{
  "source": "00bbfd7c",
  "target": "00bbfd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd88`](#insn-00bbfd88)

~~~json
{
  "source": "00bbfd88",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd90`](#insn-00bbfd90)

~~~json
{
  "source": "00bbfd90",
  "target": "00bbfda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd94`](#insn-00bbfd94)

~~~json
{
  "source": "00bbfd94",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd9c`](#insn-00bbfd9c)

~~~json
{
  "source": "00bbfd9c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfda8`](#insn-00bbfda8)

~~~json
{
  "source": "00bbfda8",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdb8`](#insn-00bbfdb8)

~~~json
{
  "source": "00bbfdb8",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdc0`](#insn-00bbfdc0)

~~~json
{
  "source": "00bbfdc0",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd0`](#insn-00bbfdd0)

~~~json
{
  "source": "00bbfdd0",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfddc`](#insn-00bbfddc)

~~~json
{
  "source": "00bbfddc",
  "target": "00bbfdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfde8`](#insn-00bbfde8)

~~~json
{
  "source": "00bbfde8",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdf0`](#insn-00bbfdf0)

~~~json
{
  "source": "00bbfdf0",
  "target": "00bbfe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdf4`](#insn-00bbfdf4)

~~~json
{
  "source": "00bbfdf4",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdfc`](#insn-00bbfdfc)

~~~json
{
  "source": "00bbfdfc",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe0c`](#insn-00bbfe0c)

~~~json
{
  "source": "00bbfe0c",
  "target": "00bbfe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe24`](#insn-00bbfe24)

~~~json
{
  "source": "00bbfe24",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe2c`](#insn-00bbfe2c)

~~~json
{
  "source": "00bbfe2c",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe38`](#insn-00bbfe38)

~~~json
{
  "source": "00bbfe38",
  "target": "00bbfe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfe40`](#insn-00bbfe40)

~~~json
{
  "source": "00bbfe40",
  "target": "00bbfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
