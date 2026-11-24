# 00bc0bac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc0784`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0784.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-83c1a7bc2671361f2a661bc2c2b8283e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc0c48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc0/00bc0c48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0006.md#compare-eae18445312b9576a19830d8d4825fd3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0bac",
  "name": "_ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "efeedf88a8479f29c1ab2cbd879f00e5e01808ead1b83461c3e883e0fc50959b",
  "source_text_sha256": "efeedf88a8479f29c1ab2cbd879f00e5e01808ead1b83461c3e883e0fc50959b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc0bac",
        "00bc0d53"
      ]
    ],
    "bytes_sha256": "e49cb216b2182beb05defb38e906c7c8d90d0827098f16bbf1aa821b449ffe9c",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d500](../00c5d/00c5d500.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3116 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ushort *puVar12;
  
  lVar7 = *param_2;
  uVar10 = (long)param_1 - lVar7;
  if (((uVar10 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar8 = param_2[1];
    if ((uVar8 < 5) || (uVar9 = uVar8 - 4, uVar9 < uVar10)) {
      return 0;
    }
    lVar6 = param_2[7];
    iVar5 = *param_1;
    uVar1 = (int)lVar6 + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar11 = uVar10 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar11 <= uVar8 - 2)) {
      uVar4 = *(ushort *)(lVar7 + uVar11);
      if ((((uVar4 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar4 & 1) == 0)) {
        if (uVar8 <= uVar4) {
          return 0;
        }
        if (uVar8 - uVar4 < uVar11) {
          return 0;
        }
        puVar12 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar12) {
          if ((ulong)puVar12[2] != 0) {
            uVar10 = uVar10 + puVar12[2];
            if ((uVar10 & 3) == 0) {
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar7 + uVar10) < 1) {
              return 0;
            }
            if (uVar8 - 1 < uVar10 + *(uint *)(lVar7 + uVar10)) {
              return 0;
            }
          }
          if (((ulong)puVar12[2] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[2]),
             puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
            uVar10 = (long)puVar3 - lVar7;
            if ((uVar10 & 3) == 0) {
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            else {
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar9 < uVar10) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar3) {
              return 0;
            }
            uVar9 = (ulong)*puVar3 + 4;
            if (uVar8 - 1 < uVar9 + uVar10) {
              return 0;
            }
            if (uVar8 <= uVar9) {
              return 0;
            }
            if (uVar8 - uVar9 < uVar10) {
              return 0;
            }
            if (*(char *)(lVar7 + uVar9 + uVar10) != '\0') {
              return 0;
            }
          }
        }
        *(int *)(param_2 + 7) = (int)lVar6;
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
<a id="insn-00bc0bac"></a> `00bc0bac` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bc0bb0"></a> `00bc0bb0` | `0d 00 09 cb` | sub x13,x0,x9 | `FALL_THROUGH`
<a id="insn-00bc0bb4"></a> `00bc0bb4` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc0bb8"></a> `00bc0bb8` | `60 00 00 54` | b.eq 0x00bc0bc4 | `CONDITIONAL_JUMP`
<a id="insn-00bc0bbc"></a> `00bc0bbc` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0bc0"></a> `00bc0bc0` | `e8 0b 00 35` | cbnz w8,0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0bc4"></a> `00bc0bc4` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bc0bc8"></a> `00bc0bc8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0bcc"></a> `00bc0bcc` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bc0bd0"></a> `00bc0bd0` | `e3 0b 00 54` | b.cc 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0bd4"></a> `00bc0bd4` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bc0bd8"></a> `00bc0bd8` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0bdc"></a> `00bc0bdc` | `83 0b 00 54` | b.cc 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0be0"></a> `00bc0be0` | `2b 38 47 29` | ldp w11,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc0be4"></a> `00bc0be4` | `2f 10 40 b9` | ldr w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bc0be8"></a> `00bc0be8` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc0bec"></a> `00bc0bec` | `70 05 00 11` | add w16,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0bf0"></a> `00bc0bf0` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0bf4"></a> `00bc0bf4` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bc0bf8"></a> `00bc0bf8` | `30 38 07 29` | stp w16,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc0bfc"></a> `00bc0bfc` | `08 0a 00 54` | b.hi 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c00"></a> `00bc0c00` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00bc0c04"></a> `00bc0c04` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00bc0c08"></a> `00bc0c08` | `a8 09 00 54` | b.hi 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c0c"></a> `00bc0c0c` | `ae 01 08 cb` | sub x14,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0c10"></a> `00bc0c10` | `6e 00 00 36` | tbz w14,#0x0,0x00bc0c1c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c14"></a> `00bc0c14` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0c18"></a> `00bc0c18` | `28 09 00 35` | cbnz w8,0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c1c"></a> `00bc0c1c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bc0c20"></a> `00bc0c20` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00bc0c24"></a> `00bc0c24` | `c3 08 00 54` | b.cc 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c28"></a> `00bc0c28` | `28 69 6e 78` | ldrh w8,[x9, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bc0c2c"></a> `00bc0c2c` | `68 00 00 36` | tbz w8,#0x0,0x00bc0c38 | `CONDITIONAL_JUMP`
<a id="insn-00bc0c30"></a> `00bc0c30` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0c34"></a> `00bc0c34` | `4f 08 00 35` | cbnz w15,0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c38"></a> `00bc0c38` | `28 08 00 37` | tbnz w8,#0x0,0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c3c"></a> `00bc0c3c` | `4f 01 08 eb` | subs x15,x10,x8 | `FALL_THROUGH`
<a id="insn-00bc0c40"></a> `00bc0c40` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0c44"></a> `00bc0c44` | `49 08 00 54` | b.ls 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c48"></a> `00bc0c48` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bc0c4c"></a> `00bc0c4c` | `03 08 00 54` | b.cc 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c50"></a> `00bc0c50` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc0c54"></a> `00bc0c54` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00bc0c58"></a> `00bc0c58` | `c8 01 40 79` | ldrh w8,[x14] | `FALL_THROUGH`
<a id="insn-00bc0c5c"></a> `00bc0c5c` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bc0c60"></a> `00bc0c60` | `23 07 00 54` | b.cc 0x00bc0d44 | `CONDITIONAL_JUMP`
<a id="insn-00bc0c64"></a> `00bc0c64` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bc0c68"></a> `00bc0c68` | `68 02 00 b4` | cbz x8,0x00bc0cb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc0c6c"></a> `00bc0c6c` | `ad 01 08 8b` | add x13,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0c70"></a> `00bc0c70` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc0c74"></a> `00bc0c74` | `e0 00 00 54` | b.eq 0x00bc0c90 | `CONDITIONAL_JUMP`
<a id="insn-00bc0c78"></a> `00bc0c78` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0c7c"></a> `00bc0c7c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0c80"></a> `00bc0c80` | `6f 06 00 35` | cbnz w15,0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c84"></a> `00bc0c84` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0c88"></a> `00bc0c88` | `82 00 00 54` | b.cs 0x00bc0c98 | `CONDITIONAL_JUMP`
<a id="insn-00bc0c8c"></a> `00bc0c8c` | `30 00 00 14` | b 0x00bc0d4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc0c90"></a> `00bc0c90` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0c94"></a> `00bc0c94` | `43 05 00 54` | b.cc 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0c98"></a> `00bc0c98` | `28 69 6d b8` | ldr w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bc0c9c"></a> `00bc0c9c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0ca0"></a> `00bc0ca0` | `eb 04 00 54` | b.lt 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0ca4"></a> `00bc0ca4` | `a8 01 08 8b` | add x8,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0ca8"></a> `00bc0ca8` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0cac"></a> `00bc0cac` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0cb0"></a> `00bc0cb0` | `63 04 00 54` | b.cc 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0cb4"></a> `00bc0cb4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bc0cb8"></a> `00bc0cb8` | `68 04 00 b4` | cbz x8,0x00bc0d44 | `CONDITIONAL_JUMP`
<a id="insn-00bc0cbc"></a> `00bc0cbc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bc0cc0"></a> `00bc0cc0` | `0d 01 40 b9` | ldr w13,[x8] | `FALL_THROUGH`
<a id="insn-00bc0cc4"></a> `00bc0cc4` | `0e 01 0d ab` | adds x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00bc0cc8"></a> `00bc0cc8` | `e0 03 00 54` | b.eq 0x00bc0d44 | `CONDITIONAL_JUMP`
<a id="insn-00bc0ccc"></a> `00bc0ccc` | `cd 01 09 cb` | sub x13,x14,x9 | `FALL_THROUGH`
<a id="insn-00bc0cd0"></a> `00bc0cd0` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc0cd4"></a> `00bc0cd4` | `e0 00 00 54` | b.eq 0x00bc0cf0 | `CONDITIONAL_JUMP`
<a id="insn-00bc0cd8"></a> `00bc0cd8` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0cdc"></a> `00bc0cdc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0ce0"></a> `00bc0ce0` | `6f 03 00 35` | cbnz w15,0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0ce4"></a> `00bc0ce4` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0ce8"></a> `00bc0ce8` | `82 00 00 54` | b.cs 0x00bc0cf8 | `CONDITIONAL_JUMP`
<a id="insn-00bc0cec"></a> `00bc0cec` | `18 00 00 14` | b 0x00bc0d4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc0cf0"></a> `00bc0cf0` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0cf4"></a> `00bc0cf4` | `43 02 00 54` | b.cc 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0cf8"></a> `00bc0cf8` | `c8 01 40 b9` | ldr w8,[x14] | `FALL_THROUGH`
<a id="insn-00bc0cfc"></a> `00bc0cfc` | `2c 10 40 f9` | ldr x12,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bc0d00"></a> `00bc0d00` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bc0d04"></a> `00bc0d04` | `c9 01 00 54` | b.ls 0x00bc0d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc0d08"></a> `00bc0d08` | `0e 11 00 91` | add x14,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bc0d0c"></a> `00bc0d0c` | `cc 01 0d 8b` | add x12,x14,x13 | `FALL_THROUGH`
<a id="insn-00bc0d10"></a> `00bc0d10` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0d14"></a> `00bc0d14` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00bc0d18"></a> `00bc0d18` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0d1c"></a> `00bc0d1c` | `83 01 00 54` | b.cc 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0d20"></a> `00bc0d20` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00bc0d24"></a> `00bc0d24` | `49 01 00 54` | b.ls 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0d28"></a> `00bc0d28` | `4a 01 0e cb` | sub x10,x10,x14 | `FALL_THROUGH`
<a id="insn-00bc0d2c"></a> `00bc0d2c` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00bc0d30"></a> `00bc0d30` | `e3 00 00 54` | b.cc 0x00bc0d4c | `CONDITIONAL_JUMP`
<a id="insn-00bc0d34"></a> `00bc0d34` | `28 69 6c 38` | ldrb w8,[x9, x12, LSL ] | `FALL_THROUGH`
<a id="insn-00bc0d38"></a> `00bc0d38` | `68 00 00 34` | cbz w8,0x00bc0d44 | `CONDITIONAL_JUMP`
<a id="insn-00bc0d3c"></a> `00bc0d3c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bc0d40"></a> `00bc0d40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc0d44"></a> `00bc0d44` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0d48"></a> `00bc0d48` | `2b 38 00 b9` | str w11,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc0d4c"></a> `00bc0d4c` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bc0d50"></a> `00bc0d50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc0bac`](#insn-00bc0bac) 範囲 `[['00bc0bac', '00bc0bbb']]`
  - `CONDITIONAL_JUMP` [`00bc0bb8`](#insn-00bc0bb8) → [`00bc0bc4`](#insn-00bc0bc4)
  - `FALL_THROUGH` [`00bc0bb8`](#insn-00bc0bb8) → [`00bc0bbc`](#insn-00bc0bbc)
- ブロック [`00bc0bbc`](#insn-00bc0bbc) 範囲 `[['00bc0bbc', '00bc0bc3']]`
  - `CONDITIONAL_JUMP` [`00bc0bc0`](#insn-00bc0bc0) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0bc0`](#insn-00bc0bc0) → [`00bc0bc4`](#insn-00bc0bc4)
- ブロック [`00bc0bc4`](#insn-00bc0bc4) 範囲 `[['00bc0bc4', '00bc0bd3']]`
  - `CONDITIONAL_JUMP` [`00bc0bd0`](#insn-00bc0bd0) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0bd0`](#insn-00bc0bd0) → [`00bc0bd4`](#insn-00bc0bd4)
- ブロック [`00bc0bd4`](#insn-00bc0bd4) 範囲 `[['00bc0bd4', '00bc0bdf']]`
  - `CONDITIONAL_JUMP` [`00bc0bdc`](#insn-00bc0bdc) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0bdc`](#insn-00bc0bdc) → [`00bc0be0`](#insn-00bc0be0)
- ブロック [`00bc0be0`](#insn-00bc0be0) 範囲 `[['00bc0be0', '00bc0bff']]`
  - `CONDITIONAL_JUMP` [`00bc0bfc`](#insn-00bc0bfc) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0bfc`](#insn-00bc0bfc) → [`00bc0c00`](#insn-00bc0c00)
- ブロック [`00bc0c00`](#insn-00bc0c00) 範囲 `[['00bc0c00', '00bc0c0b']]`
  - `CONDITIONAL_JUMP` [`00bc0c08`](#insn-00bc0c08) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c08`](#insn-00bc0c08) → [`00bc0c0c`](#insn-00bc0c0c)
- ブロック [`00bc0c0c`](#insn-00bc0c0c) 範囲 `[['00bc0c0c', '00bc0c13']]`
  - `CONDITIONAL_JUMP` [`00bc0c10`](#insn-00bc0c10) → [`00bc0c1c`](#insn-00bc0c1c)
  - `FALL_THROUGH` [`00bc0c10`](#insn-00bc0c10) → [`00bc0c14`](#insn-00bc0c14)
- ブロック [`00bc0c14`](#insn-00bc0c14) 範囲 `[['00bc0c14', '00bc0c1b']]`
  - `CONDITIONAL_JUMP` [`00bc0c18`](#insn-00bc0c18) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c18`](#insn-00bc0c18) → [`00bc0c1c`](#insn-00bc0c1c)
- ブロック [`00bc0c1c`](#insn-00bc0c1c) 範囲 `[['00bc0c1c', '00bc0c27']]`
  - `CONDITIONAL_JUMP` [`00bc0c24`](#insn-00bc0c24) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c24`](#insn-00bc0c24) → [`00bc0c28`](#insn-00bc0c28)
- ブロック [`00bc0c28`](#insn-00bc0c28) 範囲 `[['00bc0c28', '00bc0c2f']]`
  - `CONDITIONAL_JUMP` [`00bc0c2c`](#insn-00bc0c2c) → [`00bc0c38`](#insn-00bc0c38)
  - `FALL_THROUGH` [`00bc0c2c`](#insn-00bc0c2c) → [`00bc0c30`](#insn-00bc0c30)
- ブロック [`00bc0c30`](#insn-00bc0c30) 範囲 `[['00bc0c30', '00bc0c37']]`
  - `CONDITIONAL_JUMP` [`00bc0c34`](#insn-00bc0c34) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c34`](#insn-00bc0c34) → [`00bc0c38`](#insn-00bc0c38)
- ブロック [`00bc0c38`](#insn-00bc0c38) 範囲 `[['00bc0c38', '00bc0c3b']]`
  - `CONDITIONAL_JUMP` [`00bc0c38`](#insn-00bc0c38) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c38`](#insn-00bc0c38) → [`00bc0c3c`](#insn-00bc0c3c)
- ブロック [`00bc0c3c`](#insn-00bc0c3c) 範囲 `[['00bc0c3c', '00bc0c47']]`
  - `CONDITIONAL_JUMP` [`00bc0c44`](#insn-00bc0c44) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0c44`](#insn-00bc0c44) → [`00bc0c48`](#insn-00bc0c48)
- ブロック [`00bc0c48`](#insn-00bc0c48) 範囲 `[['00bc0c48', '00bc0c4f']]`
  - `CONDITIONAL_JUMP` [`00bc0c4c`](#insn-00bc0c4c) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0c4c`](#insn-00bc0c4c) → [`00bc0c50`](#insn-00bc0c50)
- ブロック [`00bc0c50`](#insn-00bc0c50) 範囲 `[['00bc0c50', '00bc0c63']]`
  - `CONDITIONAL_JUMP` [`00bc0c60`](#insn-00bc0c60) → [`00bc0d44`](#insn-00bc0d44)
  - `FALL_THROUGH` [`00bc0c60`](#insn-00bc0c60) → [`00bc0c64`](#insn-00bc0c64)
- ブロック [`00bc0c64`](#insn-00bc0c64) 範囲 `[['00bc0c64', '00bc0c6b']]`
  - `CONDITIONAL_JUMP` [`00bc0c68`](#insn-00bc0c68) → [`00bc0cb4`](#insn-00bc0cb4)
  - `FALL_THROUGH` [`00bc0c68`](#insn-00bc0c68) → [`00bc0c6c`](#insn-00bc0c6c)
- ブロック [`00bc0c6c`](#insn-00bc0c6c) 範囲 `[['00bc0c6c', '00bc0c77']]`
  - `CONDITIONAL_JUMP` [`00bc0c74`](#insn-00bc0c74) → [`00bc0c90`](#insn-00bc0c90)
  - `FALL_THROUGH` [`00bc0c74`](#insn-00bc0c74) → [`00bc0c78`](#insn-00bc0c78)
- ブロック [`00bc0c78`](#insn-00bc0c78) 範囲 `[['00bc0c78', '00bc0c83']]`
  - `CONDITIONAL_JUMP` [`00bc0c80`](#insn-00bc0c80) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0c80`](#insn-00bc0c80) → [`00bc0c84`](#insn-00bc0c84)
- ブロック [`00bc0c84`](#insn-00bc0c84) 範囲 `[['00bc0c84', '00bc0c8b']]`
  - `CONDITIONAL_JUMP` [`00bc0c88`](#insn-00bc0c88) → [`00bc0c98`](#insn-00bc0c98)
  - `FALL_THROUGH` [`00bc0c88`](#insn-00bc0c88) → [`00bc0c8c`](#insn-00bc0c8c)
- ブロック [`00bc0c8c`](#insn-00bc0c8c) 範囲 `[['00bc0c8c', '00bc0c8f']]`
  - `UNCONDITIONAL_JUMP` [`00bc0c8c`](#insn-00bc0c8c) → [`00bc0d4c`](#insn-00bc0d4c)
- ブロック [`00bc0c90`](#insn-00bc0c90) 範囲 `[['00bc0c90', '00bc0c97']]`
  - `CONDITIONAL_JUMP` [`00bc0c94`](#insn-00bc0c94) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0c94`](#insn-00bc0c94) → [`00bc0c98`](#insn-00bc0c98)
- ブロック [`00bc0c98`](#insn-00bc0c98) 範囲 `[['00bc0c98', '00bc0ca3']]`
  - `CONDITIONAL_JUMP` [`00bc0ca0`](#insn-00bc0ca0) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0ca0`](#insn-00bc0ca0) → [`00bc0ca4`](#insn-00bc0ca4)
- ブロック [`00bc0ca4`](#insn-00bc0ca4) 範囲 `[['00bc0ca4', '00bc0cb3']]`
  - `CONDITIONAL_JUMP` [`00bc0cb0`](#insn-00bc0cb0) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0cb0`](#insn-00bc0cb0) → [`00bc0cb4`](#insn-00bc0cb4)
- ブロック [`00bc0cb4`](#insn-00bc0cb4) 範囲 `[['00bc0cb4', '00bc0cbb']]`
  - `CONDITIONAL_JUMP` [`00bc0cb8`](#insn-00bc0cb8) → [`00bc0d44`](#insn-00bc0d44)
  - `FALL_THROUGH` [`00bc0cb8`](#insn-00bc0cb8) → [`00bc0cbc`](#insn-00bc0cbc)
- ブロック [`00bc0cbc`](#insn-00bc0cbc) 範囲 `[['00bc0cbc', '00bc0ccb']]`
  - `CONDITIONAL_JUMP` [`00bc0cc8`](#insn-00bc0cc8) → [`00bc0d44`](#insn-00bc0d44)
  - `FALL_THROUGH` [`00bc0cc8`](#insn-00bc0cc8) → [`00bc0ccc`](#insn-00bc0ccc)
- ブロック [`00bc0ccc`](#insn-00bc0ccc) 範囲 `[['00bc0ccc', '00bc0cd7']]`
  - `CONDITIONAL_JUMP` [`00bc0cd4`](#insn-00bc0cd4) → [`00bc0cf0`](#insn-00bc0cf0)
  - `FALL_THROUGH` [`00bc0cd4`](#insn-00bc0cd4) → [`00bc0cd8`](#insn-00bc0cd8)
- ブロック [`00bc0cd8`](#insn-00bc0cd8) 範囲 `[['00bc0cd8', '00bc0ce3']]`
  - `CONDITIONAL_JUMP` [`00bc0ce0`](#insn-00bc0ce0) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0ce0`](#insn-00bc0ce0) → [`00bc0ce4`](#insn-00bc0ce4)
- ブロック [`00bc0ce4`](#insn-00bc0ce4) 範囲 `[['00bc0ce4', '00bc0ceb']]`
  - `CONDITIONAL_JUMP` [`00bc0ce8`](#insn-00bc0ce8) → [`00bc0cf8`](#insn-00bc0cf8)
  - `FALL_THROUGH` [`00bc0ce8`](#insn-00bc0ce8) → [`00bc0cec`](#insn-00bc0cec)
- ブロック [`00bc0cec`](#insn-00bc0cec) 範囲 `[['00bc0cec', '00bc0cef']]`
  - `UNCONDITIONAL_JUMP` [`00bc0cec`](#insn-00bc0cec) → [`00bc0d4c`](#insn-00bc0d4c)
- ブロック [`00bc0cf0`](#insn-00bc0cf0) 範囲 `[['00bc0cf0', '00bc0cf7']]`
  - `CONDITIONAL_JUMP` [`00bc0cf4`](#insn-00bc0cf4) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0cf4`](#insn-00bc0cf4) → [`00bc0cf8`](#insn-00bc0cf8)
- ブロック [`00bc0cf8`](#insn-00bc0cf8) 範囲 `[['00bc0cf8', '00bc0d07']]`
  - `CONDITIONAL_JUMP` [`00bc0d04`](#insn-00bc0d04) → [`00bc0d3c`](#insn-00bc0d3c)
  - `FALL_THROUGH` [`00bc0d04`](#insn-00bc0d04) → [`00bc0d08`](#insn-00bc0d08)
- ブロック [`00bc0d08`](#insn-00bc0d08) 範囲 `[['00bc0d08', '00bc0d1f']]`
  - `CONDITIONAL_JUMP` [`00bc0d1c`](#insn-00bc0d1c) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0d1c`](#insn-00bc0d1c) → [`00bc0d20`](#insn-00bc0d20)
- ブロック [`00bc0d20`](#insn-00bc0d20) 範囲 `[['00bc0d20', '00bc0d27']]`
  - `CONDITIONAL_JUMP` [`00bc0d24`](#insn-00bc0d24) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0d24`](#insn-00bc0d24) → [`00bc0d28`](#insn-00bc0d28)
- ブロック [`00bc0d28`](#insn-00bc0d28) 範囲 `[['00bc0d28', '00bc0d33']]`
  - `CONDITIONAL_JUMP` [`00bc0d30`](#insn-00bc0d30) → [`00bc0d4c`](#insn-00bc0d4c)
  - `FALL_THROUGH` [`00bc0d30`](#insn-00bc0d30) → [`00bc0d34`](#insn-00bc0d34)
- ブロック [`00bc0d34`](#insn-00bc0d34) 範囲 `[['00bc0d34', '00bc0d3b']]`
  - `CONDITIONAL_JUMP` [`00bc0d38`](#insn-00bc0d38) → [`00bc0d44`](#insn-00bc0d44)
  - `FALL_THROUGH` [`00bc0d38`](#insn-00bc0d38) → [`00bc0d3c`](#insn-00bc0d3c)
- ブロック [`00bc0d3c`](#insn-00bc0d3c) 範囲 `[['00bc0d3c', '00bc0d43']]`
- ブロック [`00bc0d44`](#insn-00bc0d44) 範囲 `[['00bc0d44', '00bc0d4b']]`
  - `FALL_THROUGH` [`00bc0d48`](#insn-00bc0d48) → [`00bc0d4c`](#insn-00bc0d4c)
- ブロック [`00bc0d4c`](#insn-00bc0d4c) 範囲 `[['00bc0d4c', '00bc0d53']]`

## 命令位置別の参照

- [`00bc0bb8`](#insn-00bc0bb8) → [`00bc0bc4`](#insn-00bc0bc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0bc0`](#insn-00bc0bc0) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0bd0`](#insn-00bc0bd0) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0bdc`](#insn-00bc0bdc) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0bfc`](#insn-00bc0bfc) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c08`](#insn-00bc0c08) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c10`](#insn-00bc0c10) → [`00bc0c1c`](#insn-00bc0c1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c18`](#insn-00bc0c18) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c24`](#insn-00bc0c24) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c2c`](#insn-00bc0c2c) → [`00bc0c38`](#insn-00bc0c38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c34`](#insn-00bc0c34) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c38`](#insn-00bc0c38) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c44`](#insn-00bc0c44) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c4c`](#insn-00bc0c4c) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c60`](#insn-00bc0c60) → [`00bc0d44`](#insn-00bc0d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c68`](#insn-00bc0c68) → [`00bc0cb4`](#insn-00bc0cb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c74`](#insn-00bc0c74) → [`00bc0c90`](#insn-00bc0c90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c80`](#insn-00bc0c80) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c88`](#insn-00bc0c88) → [`00bc0c98`](#insn-00bc0c98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c8c`](#insn-00bc0c8c) → [`00bc0d4c`](#insn-00bc0d4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0c94`](#insn-00bc0c94) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0ca0`](#insn-00bc0ca0) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cb0`](#insn-00bc0cb0) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cb8`](#insn-00bc0cb8) → [`00bc0d44`](#insn-00bc0d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cc8`](#insn-00bc0cc8) → [`00bc0d44`](#insn-00bc0d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cd4`](#insn-00bc0cd4) → [`00bc0cf0`](#insn-00bc0cf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0ce0`](#insn-00bc0ce0) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0ce8`](#insn-00bc0ce8) → [`00bc0cf8`](#insn-00bc0cf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cec`](#insn-00bc0cec) → [`00bc0d4c`](#insn-00bc0d4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0cf4`](#insn-00bc0cf4) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0d04`](#insn-00bc0d04) → [`00bc0d3c`](#insn-00bc0d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0d1c`](#insn-00bc0d1c) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0d24`](#insn-00bc0d24) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0d30`](#insn-00bc0d30) → [`00bc0d4c`](#insn-00bc0d4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0d38`](#insn-00bc0d38) → [`00bc0d44`](#insn-00bc0d44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc0bb8`](#insn-00bc0bb8)

~~~json
{
  "source": "00bc0bb8",
  "target": "00bc0bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0bc0`](#insn-00bc0bc0)

~~~json
{
  "source": "00bc0bc0",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0bd0`](#insn-00bc0bd0)

~~~json
{
  "source": "00bc0bd0",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0bdc`](#insn-00bc0bdc)

~~~json
{
  "source": "00bc0bdc",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0bfc`](#insn-00bc0bfc)

~~~json
{
  "source": "00bc0bfc",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c08`](#insn-00bc0c08)

~~~json
{
  "source": "00bc0c08",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c10`](#insn-00bc0c10)

~~~json
{
  "source": "00bc0c10",
  "target": "00bc0c1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c18`](#insn-00bc0c18)

~~~json
{
  "source": "00bc0c18",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c24`](#insn-00bc0c24)

~~~json
{
  "source": "00bc0c24",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c2c`](#insn-00bc0c2c)

~~~json
{
  "source": "00bc0c2c",
  "target": "00bc0c38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c34`](#insn-00bc0c34)

~~~json
{
  "source": "00bc0c34",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c38`](#insn-00bc0c38)

~~~json
{
  "source": "00bc0c38",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c44`](#insn-00bc0c44)

~~~json
{
  "source": "00bc0c44",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c4c`](#insn-00bc0c4c)

~~~json
{
  "source": "00bc0c4c",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c60`](#insn-00bc0c60)

~~~json
{
  "source": "00bc0c60",
  "target": "00bc0d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c68`](#insn-00bc0c68)

~~~json
{
  "source": "00bc0c68",
  "target": "00bc0cb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c74`](#insn-00bc0c74)

~~~json
{
  "source": "00bc0c74",
  "target": "00bc0c90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c80`](#insn-00bc0c80)

~~~json
{
  "source": "00bc0c80",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c88`](#insn-00bc0c88)

~~~json
{
  "source": "00bc0c88",
  "target": "00bc0c98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c8c`](#insn-00bc0c8c)

~~~json
{
  "source": "00bc0c8c",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0c94`](#insn-00bc0c94)

~~~json
{
  "source": "00bc0c94",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0ca0`](#insn-00bc0ca0)

~~~json
{
  "source": "00bc0ca0",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cb0`](#insn-00bc0cb0)

~~~json
{
  "source": "00bc0cb0",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cb8`](#insn-00bc0cb8)

~~~json
{
  "source": "00bc0cb8",
  "target": "00bc0d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cc8`](#insn-00bc0cc8)

~~~json
{
  "source": "00bc0cc8",
  "target": "00bc0d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cd4`](#insn-00bc0cd4)

~~~json
{
  "source": "00bc0cd4",
  "target": "00bc0cf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0ce0`](#insn-00bc0ce0)

~~~json
{
  "source": "00bc0ce0",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0ce8`](#insn-00bc0ce8)

~~~json
{
  "source": "00bc0ce8",
  "target": "00bc0cf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cec`](#insn-00bc0cec)

~~~json
{
  "source": "00bc0cec",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0cf4`](#insn-00bc0cf4)

~~~json
{
  "source": "00bc0cf4",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0d04`](#insn-00bc0d04)

~~~json
{
  "source": "00bc0d04",
  "target": "00bc0d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0d1c`](#insn-00bc0d1c)

~~~json
{
  "source": "00bc0d1c",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0d24`](#insn-00bc0d24)

~~~json
{
  "source": "00bc0d24",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0d30`](#insn-00bc0d30)

~~~json
{
  "source": "00bc0d30",
  "target": "00bc0d4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0d38`](#insn-00bc0d38)

~~~json
{
  "source": "00bc0d38",
  "target": "00bc0d44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
