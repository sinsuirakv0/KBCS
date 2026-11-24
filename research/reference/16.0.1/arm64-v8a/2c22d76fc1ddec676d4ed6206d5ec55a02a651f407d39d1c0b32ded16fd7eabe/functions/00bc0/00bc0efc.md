# 00bc0efc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc0ad4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0ad4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-4c06989bf9d2edf657d95fefee03c962)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc0f98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc0/00bc0f98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0006.md#compare-07fcf3a2b9881a183886a16bcb598775)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0efc",
  "name": "_ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4685ce8c4df36508f5dbe0aac2106c4bcdb50ce94e81fa9555b1ff8909b90872",
  "source_text_sha256": "4685ce8c4df36508f5dbe0aac2106c4bcdb50ce94e81fa9555b1ff8909b90872",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc0efc",
        "00bc10a3"
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

- [00c5d520](../00c5d/00c5d520.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3125 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
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
<a id="insn-00bc0efc"></a> `00bc0efc` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bc0f00"></a> `00bc0f00` | `0d 00 09 cb` | sub x13,x0,x9 | `FALL_THROUGH`
<a id="insn-00bc0f04"></a> `00bc0f04` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc0f08"></a> `00bc0f08` | `60 00 00 54` | b.eq 0x00bc0f14 | `CONDITIONAL_JUMP`
<a id="insn-00bc0f0c"></a> `00bc0f0c` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0f10"></a> `00bc0f10` | `e8 0b 00 35` | cbnz w8,0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f14"></a> `00bc0f14` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bc0f18"></a> `00bc0f18` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0f1c"></a> `00bc0f1c` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00bc0f20"></a> `00bc0f20` | `e3 0b 00 54` | b.cc 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f24"></a> `00bc0f24` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bc0f28"></a> `00bc0f28` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0f2c"></a> `00bc0f2c` | `83 0b 00 54` | b.cc 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f30"></a> `00bc0f30` | `2b 38 47 29` | ldp w11,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc0f34"></a> `00bc0f34` | `2f 10 40 b9` | ldr w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bc0f38"></a> `00bc0f38` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc0f3c"></a> `00bc0f3c` | `70 05 00 11` | add w16,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0f40"></a> `00bc0f40` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0f44"></a> `00bc0f44` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00bc0f48"></a> `00bc0f48` | `30 38 07 29` | stp w16,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc0f4c"></a> `00bc0f4c` | `08 0a 00 54` | b.hi 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f50"></a> `00bc0f50` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00bc0f54"></a> `00bc0f54` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00bc0f58"></a> `00bc0f58` | `a8 09 00 54` | b.hi 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f5c"></a> `00bc0f5c` | `ae 01 08 cb` | sub x14,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0f60"></a> `00bc0f60` | `6e 00 00 36` | tbz w14,#0x0,0x00bc0f6c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f64"></a> `00bc0f64` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0f68"></a> `00bc0f68` | `28 09 00 35` | cbnz w8,0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f6c"></a> `00bc0f6c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bc0f70"></a> `00bc0f70` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00bc0f74"></a> `00bc0f74` | `c3 08 00 54` | b.cc 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f78"></a> `00bc0f78` | `28 69 6e 78` | ldrh w8,[x9, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bc0f7c"></a> `00bc0f7c` | `68 00 00 36` | tbz w8,#0x0,0x00bc0f88 | `CONDITIONAL_JUMP`
<a id="insn-00bc0f80"></a> `00bc0f80` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0f84"></a> `00bc0f84` | `4f 08 00 35` | cbnz w15,0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f88"></a> `00bc0f88` | `28 08 00 37` | tbnz w8,#0x0,0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f8c"></a> `00bc0f8c` | `4f 01 08 eb` | subs x15,x10,x8 | `FALL_THROUGH`
<a id="insn-00bc0f90"></a> `00bc0f90` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0f94"></a> `00bc0f94` | `49 08 00 54` | b.ls 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc0f98"></a> `00bc0f98` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00bc0f9c"></a> `00bc0f9c` | `03 08 00 54` | b.cc 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc0fa0"></a> `00bc0fa0` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc0fa4"></a> `00bc0fa4` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00bc0fa8"></a> `00bc0fa8` | `c8 01 40 79` | ldrh w8,[x14] | `FALL_THROUGH`
<a id="insn-00bc0fac"></a> `00bc0fac` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bc0fb0"></a> `00bc0fb0` | `23 07 00 54` | b.cc 0x00bc1094 | `CONDITIONAL_JUMP`
<a id="insn-00bc0fb4"></a> `00bc0fb4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bc0fb8"></a> `00bc0fb8` | `68 02 00 b4` | cbz x8,0x00bc1004 | `CONDITIONAL_JUMP`
<a id="insn-00bc0fbc"></a> `00bc0fbc` | `ad 01 08 8b` | add x13,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0fc0"></a> `00bc0fc0` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc0fc4"></a> `00bc0fc4` | `e0 00 00 54` | b.eq 0x00bc0fe0 | `CONDITIONAL_JUMP`
<a id="insn-00bc0fc8"></a> `00bc0fc8` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0fcc"></a> `00bc0fcc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc0fd0"></a> `00bc0fd0` | `6f 06 00 35` | cbnz w15,0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc0fd4"></a> `00bc0fd4` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0fd8"></a> `00bc0fd8` | `82 00 00 54` | b.cs 0x00bc0fe8 | `CONDITIONAL_JUMP`
<a id="insn-00bc0fdc"></a> `00bc0fdc` | `30 00 00 14` | b 0x00bc109c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc0fe0"></a> `00bc0fe0` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc0fe4"></a> `00bc0fe4` | `43 05 00 54` | b.cc 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0fe8"></a> `00bc0fe8` | `28 69 6d b8` | ldr w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bc0fec"></a> `00bc0fec` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0ff0"></a> `00bc0ff0` | `eb 04 00 54` | b.lt 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc0ff4"></a> `00bc0ff4` | `a8 01 08 8b` | add x8,x13,x8 | `FALL_THROUGH`
<a id="insn-00bc0ff8"></a> `00bc0ff8` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc0ffc"></a> `00bc0ffc` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00bc1000"></a> `00bc1000` | `63 04 00 54` | b.cc 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc1004"></a> `00bc1004` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00bc1008"></a> `00bc1008` | `68 04 00 b4` | cbz x8,0x00bc1094 | `CONDITIONAL_JUMP`
<a id="insn-00bc100c"></a> `00bc100c` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bc1010"></a> `00bc1010` | `0d 01 40 b9` | ldr w13,[x8] | `FALL_THROUGH`
<a id="insn-00bc1014"></a> `00bc1014` | `0e 01 0d ab` | adds x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00bc1018"></a> `00bc1018` | `e0 03 00 54` | b.eq 0x00bc1094 | `CONDITIONAL_JUMP`
<a id="insn-00bc101c"></a> `00bc101c` | `cd 01 09 cb` | sub x13,x14,x9 | `FALL_THROUGH`
<a id="insn-00bc1020"></a> `00bc1020` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bc1024"></a> `00bc1024` | `e0 00 00 54` | b.eq 0x00bc1040 | `CONDITIONAL_JUMP`
<a id="insn-00bc1028"></a> `00bc1028` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bc102c"></a> `00bc102c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc1030"></a> `00bc1030` | `6f 03 00 35` | cbnz w15,0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc1034"></a> `00bc1034` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc1038"></a> `00bc1038` | `82 00 00 54` | b.cs 0x00bc1048 | `CONDITIONAL_JUMP`
<a id="insn-00bc103c"></a> `00bc103c` | `18 00 00 14` | b 0x00bc109c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc1040"></a> `00bc1040` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00bc1044"></a> `00bc1044` | `43 02 00 54` | b.cc 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc1048"></a> `00bc1048` | `c8 01 40 b9` | ldr w8,[x14] | `FALL_THROUGH`
<a id="insn-00bc104c"></a> `00bc104c` | `2c 10 40 f9` | ldr x12,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bc1050"></a> `00bc1050` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bc1054"></a> `00bc1054` | `c9 01 00 54` | b.ls 0x00bc108c | `CONDITIONAL_JUMP`
<a id="insn-00bc1058"></a> `00bc1058` | `0e 11 00 91` | add x14,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bc105c"></a> `00bc105c` | `cc 01 0d 8b` | add x12,x14,x13 | `FALL_THROUGH`
<a id="insn-00bc1060"></a> `00bc1060` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1064"></a> `00bc1064` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00bc1068"></a> `00bc1068` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bc106c"></a> `00bc106c` | `83 01 00 54` | b.cc 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc1070"></a> `00bc1070` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00bc1074"></a> `00bc1074` | `49 01 00 54` | b.ls 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc1078"></a> `00bc1078` | `4a 01 0e cb` | sub x10,x10,x14 | `FALL_THROUGH`
<a id="insn-00bc107c"></a> `00bc107c` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00bc1080"></a> `00bc1080` | `e3 00 00 54` | b.cc 0x00bc109c | `CONDITIONAL_JUMP`
<a id="insn-00bc1084"></a> `00bc1084` | `28 69 6c 38` | ldrb w8,[x9, x12, LSL ] | `FALL_THROUGH`
<a id="insn-00bc1088"></a> `00bc1088` | `68 00 00 34` | cbz w8,0x00bc1094 | `CONDITIONAL_JUMP`
<a id="insn-00bc108c"></a> `00bc108c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bc1090"></a> `00bc1090` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc1094"></a> `00bc1094` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1098"></a> `00bc1098` | `2b 38 00 b9` | str w11,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00bc109c"></a> `00bc109c` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00bc10a0"></a> `00bc10a0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc0efc`](#insn-00bc0efc) 範囲 `[['00bc0efc', '00bc0f0b']]`
  - `CONDITIONAL_JUMP` [`00bc0f08`](#insn-00bc0f08) → [`00bc0f14`](#insn-00bc0f14)
  - `FALL_THROUGH` [`00bc0f08`](#insn-00bc0f08) → [`00bc0f0c`](#insn-00bc0f0c)
- ブロック [`00bc0f0c`](#insn-00bc0f0c) 範囲 `[['00bc0f0c', '00bc0f13']]`
  - `CONDITIONAL_JUMP` [`00bc0f10`](#insn-00bc0f10) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f10`](#insn-00bc0f10) → [`00bc0f14`](#insn-00bc0f14)
- ブロック [`00bc0f14`](#insn-00bc0f14) 範囲 `[['00bc0f14', '00bc0f23']]`
  - `CONDITIONAL_JUMP` [`00bc0f20`](#insn-00bc0f20) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc0f20`](#insn-00bc0f20) → [`00bc0f24`](#insn-00bc0f24)
- ブロック [`00bc0f24`](#insn-00bc0f24) 範囲 `[['00bc0f24', '00bc0f2f']]`
  - `CONDITIONAL_JUMP` [`00bc0f2c`](#insn-00bc0f2c) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc0f2c`](#insn-00bc0f2c) → [`00bc0f30`](#insn-00bc0f30)
- ブロック [`00bc0f30`](#insn-00bc0f30) 範囲 `[['00bc0f30', '00bc0f4f']]`
  - `CONDITIONAL_JUMP` [`00bc0f4c`](#insn-00bc0f4c) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f4c`](#insn-00bc0f4c) → [`00bc0f50`](#insn-00bc0f50)
- ブロック [`00bc0f50`](#insn-00bc0f50) 範囲 `[['00bc0f50', '00bc0f5b']]`
  - `CONDITIONAL_JUMP` [`00bc0f58`](#insn-00bc0f58) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f58`](#insn-00bc0f58) → [`00bc0f5c`](#insn-00bc0f5c)
- ブロック [`00bc0f5c`](#insn-00bc0f5c) 範囲 `[['00bc0f5c', '00bc0f63']]`
  - `CONDITIONAL_JUMP` [`00bc0f60`](#insn-00bc0f60) → [`00bc0f6c`](#insn-00bc0f6c)
  - `FALL_THROUGH` [`00bc0f60`](#insn-00bc0f60) → [`00bc0f64`](#insn-00bc0f64)
- ブロック [`00bc0f64`](#insn-00bc0f64) 範囲 `[['00bc0f64', '00bc0f6b']]`
  - `CONDITIONAL_JUMP` [`00bc0f68`](#insn-00bc0f68) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f68`](#insn-00bc0f68) → [`00bc0f6c`](#insn-00bc0f6c)
- ブロック [`00bc0f6c`](#insn-00bc0f6c) 範囲 `[['00bc0f6c', '00bc0f77']]`
  - `CONDITIONAL_JUMP` [`00bc0f74`](#insn-00bc0f74) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f74`](#insn-00bc0f74) → [`00bc0f78`](#insn-00bc0f78)
- ブロック [`00bc0f78`](#insn-00bc0f78) 範囲 `[['00bc0f78', '00bc0f7f']]`
  - `CONDITIONAL_JUMP` [`00bc0f7c`](#insn-00bc0f7c) → [`00bc0f88`](#insn-00bc0f88)
  - `FALL_THROUGH` [`00bc0f7c`](#insn-00bc0f7c) → [`00bc0f80`](#insn-00bc0f80)
- ブロック [`00bc0f80`](#insn-00bc0f80) 範囲 `[['00bc0f80', '00bc0f87']]`
  - `CONDITIONAL_JUMP` [`00bc0f84`](#insn-00bc0f84) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f84`](#insn-00bc0f84) → [`00bc0f88`](#insn-00bc0f88)
- ブロック [`00bc0f88`](#insn-00bc0f88) 範囲 `[['00bc0f88', '00bc0f8b']]`
  - `CONDITIONAL_JUMP` [`00bc0f88`](#insn-00bc0f88) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0f88`](#insn-00bc0f88) → [`00bc0f8c`](#insn-00bc0f8c)
- ブロック [`00bc0f8c`](#insn-00bc0f8c) 範囲 `[['00bc0f8c', '00bc0f97']]`
  - `CONDITIONAL_JUMP` [`00bc0f94`](#insn-00bc0f94) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc0f94`](#insn-00bc0f94) → [`00bc0f98`](#insn-00bc0f98)
- ブロック [`00bc0f98`](#insn-00bc0f98) 範囲 `[['00bc0f98', '00bc0f9f']]`
  - `CONDITIONAL_JUMP` [`00bc0f9c`](#insn-00bc0f9c) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc0f9c`](#insn-00bc0f9c) → [`00bc0fa0`](#insn-00bc0fa0)
- ブロック [`00bc0fa0`](#insn-00bc0fa0) 範囲 `[['00bc0fa0', '00bc0fb3']]`
  - `CONDITIONAL_JUMP` [`00bc0fb0`](#insn-00bc0fb0) → [`00bc1094`](#insn-00bc1094)
  - `FALL_THROUGH` [`00bc0fb0`](#insn-00bc0fb0) → [`00bc0fb4`](#insn-00bc0fb4)
- ブロック [`00bc0fb4`](#insn-00bc0fb4) 範囲 `[['00bc0fb4', '00bc0fbb']]`
  - `CONDITIONAL_JUMP` [`00bc0fb8`](#insn-00bc0fb8) → [`00bc1004`](#insn-00bc1004)
  - `FALL_THROUGH` [`00bc0fb8`](#insn-00bc0fb8) → [`00bc0fbc`](#insn-00bc0fbc)
- ブロック [`00bc0fbc`](#insn-00bc0fbc) 範囲 `[['00bc0fbc', '00bc0fc7']]`
  - `CONDITIONAL_JUMP` [`00bc0fc4`](#insn-00bc0fc4) → [`00bc0fe0`](#insn-00bc0fe0)
  - `FALL_THROUGH` [`00bc0fc4`](#insn-00bc0fc4) → [`00bc0fc8`](#insn-00bc0fc8)
- ブロック [`00bc0fc8`](#insn-00bc0fc8) 範囲 `[['00bc0fc8', '00bc0fd3']]`
  - `CONDITIONAL_JUMP` [`00bc0fd0`](#insn-00bc0fd0) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc0fd0`](#insn-00bc0fd0) → [`00bc0fd4`](#insn-00bc0fd4)
- ブロック [`00bc0fd4`](#insn-00bc0fd4) 範囲 `[['00bc0fd4', '00bc0fdb']]`
  - `CONDITIONAL_JUMP` [`00bc0fd8`](#insn-00bc0fd8) → [`00bc0fe8`](#insn-00bc0fe8)
  - `FALL_THROUGH` [`00bc0fd8`](#insn-00bc0fd8) → [`00bc0fdc`](#insn-00bc0fdc)
- ブロック [`00bc0fdc`](#insn-00bc0fdc) 範囲 `[['00bc0fdc', '00bc0fdf']]`
  - `UNCONDITIONAL_JUMP` [`00bc0fdc`](#insn-00bc0fdc) → [`00bc109c`](#insn-00bc109c)
- ブロック [`00bc0fe0`](#insn-00bc0fe0) 範囲 `[['00bc0fe0', '00bc0fe7']]`
  - `CONDITIONAL_JUMP` [`00bc0fe4`](#insn-00bc0fe4) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0fe4`](#insn-00bc0fe4) → [`00bc0fe8`](#insn-00bc0fe8)
- ブロック [`00bc0fe8`](#insn-00bc0fe8) 範囲 `[['00bc0fe8', '00bc0ff3']]`
  - `CONDITIONAL_JUMP` [`00bc0ff0`](#insn-00bc0ff0) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc0ff0`](#insn-00bc0ff0) → [`00bc0ff4`](#insn-00bc0ff4)
- ブロック [`00bc0ff4`](#insn-00bc0ff4) 範囲 `[['00bc0ff4', '00bc1003']]`
  - `CONDITIONAL_JUMP` [`00bc1000`](#insn-00bc1000) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc1000`](#insn-00bc1000) → [`00bc1004`](#insn-00bc1004)
- ブロック [`00bc1004`](#insn-00bc1004) 範囲 `[['00bc1004', '00bc100b']]`
  - `CONDITIONAL_JUMP` [`00bc1008`](#insn-00bc1008) → [`00bc1094`](#insn-00bc1094)
  - `FALL_THROUGH` [`00bc1008`](#insn-00bc1008) → [`00bc100c`](#insn-00bc100c)
- ブロック [`00bc100c`](#insn-00bc100c) 範囲 `[['00bc100c', '00bc101b']]`
  - `CONDITIONAL_JUMP` [`00bc1018`](#insn-00bc1018) → [`00bc1094`](#insn-00bc1094)
  - `FALL_THROUGH` [`00bc1018`](#insn-00bc1018) → [`00bc101c`](#insn-00bc101c)
- ブロック [`00bc101c`](#insn-00bc101c) 範囲 `[['00bc101c', '00bc1027']]`
  - `CONDITIONAL_JUMP` [`00bc1024`](#insn-00bc1024) → [`00bc1040`](#insn-00bc1040)
  - `FALL_THROUGH` [`00bc1024`](#insn-00bc1024) → [`00bc1028`](#insn-00bc1028)
- ブロック [`00bc1028`](#insn-00bc1028) 範囲 `[['00bc1028', '00bc1033']]`
  - `CONDITIONAL_JUMP` [`00bc1030`](#insn-00bc1030) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc1030`](#insn-00bc1030) → [`00bc1034`](#insn-00bc1034)
- ブロック [`00bc1034`](#insn-00bc1034) 範囲 `[['00bc1034', '00bc103b']]`
  - `CONDITIONAL_JUMP` [`00bc1038`](#insn-00bc1038) → [`00bc1048`](#insn-00bc1048)
  - `FALL_THROUGH` [`00bc1038`](#insn-00bc1038) → [`00bc103c`](#insn-00bc103c)
- ブロック [`00bc103c`](#insn-00bc103c) 範囲 `[['00bc103c', '00bc103f']]`
  - `UNCONDITIONAL_JUMP` [`00bc103c`](#insn-00bc103c) → [`00bc109c`](#insn-00bc109c)
- ブロック [`00bc1040`](#insn-00bc1040) 範囲 `[['00bc1040', '00bc1047']]`
  - `CONDITIONAL_JUMP` [`00bc1044`](#insn-00bc1044) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc1044`](#insn-00bc1044) → [`00bc1048`](#insn-00bc1048)
- ブロック [`00bc1048`](#insn-00bc1048) 範囲 `[['00bc1048', '00bc1057']]`
  - `CONDITIONAL_JUMP` [`00bc1054`](#insn-00bc1054) → [`00bc108c`](#insn-00bc108c)
  - `FALL_THROUGH` [`00bc1054`](#insn-00bc1054) → [`00bc1058`](#insn-00bc1058)
- ブロック [`00bc1058`](#insn-00bc1058) 範囲 `[['00bc1058', '00bc106f']]`
  - `CONDITIONAL_JUMP` [`00bc106c`](#insn-00bc106c) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc106c`](#insn-00bc106c) → [`00bc1070`](#insn-00bc1070)
- ブロック [`00bc1070`](#insn-00bc1070) 範囲 `[['00bc1070', '00bc1077']]`
  - `CONDITIONAL_JUMP` [`00bc1074`](#insn-00bc1074) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc1074`](#insn-00bc1074) → [`00bc1078`](#insn-00bc1078)
- ブロック [`00bc1078`](#insn-00bc1078) 範囲 `[['00bc1078', '00bc1083']]`
  - `CONDITIONAL_JUMP` [`00bc1080`](#insn-00bc1080) → [`00bc109c`](#insn-00bc109c)
  - `FALL_THROUGH` [`00bc1080`](#insn-00bc1080) → [`00bc1084`](#insn-00bc1084)
- ブロック [`00bc1084`](#insn-00bc1084) 範囲 `[['00bc1084', '00bc108b']]`
  - `CONDITIONAL_JUMP` [`00bc1088`](#insn-00bc1088) → [`00bc1094`](#insn-00bc1094)
  - `FALL_THROUGH` [`00bc1088`](#insn-00bc1088) → [`00bc108c`](#insn-00bc108c)
- ブロック [`00bc108c`](#insn-00bc108c) 範囲 `[['00bc108c', '00bc1093']]`
- ブロック [`00bc1094`](#insn-00bc1094) 範囲 `[['00bc1094', '00bc109b']]`
  - `FALL_THROUGH` [`00bc1098`](#insn-00bc1098) → [`00bc109c`](#insn-00bc109c)
- ブロック [`00bc109c`](#insn-00bc109c) 範囲 `[['00bc109c', '00bc10a3']]`

## 命令位置別の参照

- [`00bc0f08`](#insn-00bc0f08) → [`00bc0f14`](#insn-00bc0f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f10`](#insn-00bc0f10) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f20`](#insn-00bc0f20) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f2c`](#insn-00bc0f2c) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f4c`](#insn-00bc0f4c) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f58`](#insn-00bc0f58) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f60`](#insn-00bc0f60) → [`00bc0f6c`](#insn-00bc0f6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f68`](#insn-00bc0f68) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f74`](#insn-00bc0f74) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f7c`](#insn-00bc0f7c) → [`00bc0f88`](#insn-00bc0f88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f84`](#insn-00bc0f84) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f88`](#insn-00bc0f88) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f94`](#insn-00bc0f94) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f9c`](#insn-00bc0f9c) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fb0`](#insn-00bc0fb0) → [`00bc1094`](#insn-00bc1094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fb8`](#insn-00bc0fb8) → [`00bc1004`](#insn-00bc1004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fc4`](#insn-00bc0fc4) → [`00bc0fe0`](#insn-00bc0fe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fd0`](#insn-00bc0fd0) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fd8`](#insn-00bc0fd8) → [`00bc0fe8`](#insn-00bc0fe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fdc`](#insn-00bc0fdc) → [`00bc109c`](#insn-00bc109c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0fe4`](#insn-00bc0fe4) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0ff0`](#insn-00bc0ff0) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1000`](#insn-00bc1000) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1008`](#insn-00bc1008) → [`00bc1094`](#insn-00bc1094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1018`](#insn-00bc1018) → [`00bc1094`](#insn-00bc1094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1024`](#insn-00bc1024) → [`00bc1040`](#insn-00bc1040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1030`](#insn-00bc1030) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1038`](#insn-00bc1038) → [`00bc1048`](#insn-00bc1048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc103c`](#insn-00bc103c) → [`00bc109c`](#insn-00bc109c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1044`](#insn-00bc1044) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1054`](#insn-00bc1054) → [`00bc108c`](#insn-00bc108c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc106c`](#insn-00bc106c) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1074`](#insn-00bc1074) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1080`](#insn-00bc1080) → [`00bc109c`](#insn-00bc109c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1088`](#insn-00bc1088) → [`00bc1094`](#insn-00bc1094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc0f08`](#insn-00bc0f08)

~~~json
{
  "source": "00bc0f08",
  "target": "00bc0f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f10`](#insn-00bc0f10)

~~~json
{
  "source": "00bc0f10",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f20`](#insn-00bc0f20)

~~~json
{
  "source": "00bc0f20",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f2c`](#insn-00bc0f2c)

~~~json
{
  "source": "00bc0f2c",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f4c`](#insn-00bc0f4c)

~~~json
{
  "source": "00bc0f4c",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f58`](#insn-00bc0f58)

~~~json
{
  "source": "00bc0f58",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f60`](#insn-00bc0f60)

~~~json
{
  "source": "00bc0f60",
  "target": "00bc0f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f68`](#insn-00bc0f68)

~~~json
{
  "source": "00bc0f68",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f74`](#insn-00bc0f74)

~~~json
{
  "source": "00bc0f74",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f7c`](#insn-00bc0f7c)

~~~json
{
  "source": "00bc0f7c",
  "target": "00bc0f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f84`](#insn-00bc0f84)

~~~json
{
  "source": "00bc0f84",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f88`](#insn-00bc0f88)

~~~json
{
  "source": "00bc0f88",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f94`](#insn-00bc0f94)

~~~json
{
  "source": "00bc0f94",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0f9c`](#insn-00bc0f9c)

~~~json
{
  "source": "00bc0f9c",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fb0`](#insn-00bc0fb0)

~~~json
{
  "source": "00bc0fb0",
  "target": "00bc1094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fb8`](#insn-00bc0fb8)

~~~json
{
  "source": "00bc0fb8",
  "target": "00bc1004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fc4`](#insn-00bc0fc4)

~~~json
{
  "source": "00bc0fc4",
  "target": "00bc0fe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fd0`](#insn-00bc0fd0)

~~~json
{
  "source": "00bc0fd0",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fd8`](#insn-00bc0fd8)

~~~json
{
  "source": "00bc0fd8",
  "target": "00bc0fe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fdc`](#insn-00bc0fdc)

~~~json
{
  "source": "00bc0fdc",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0fe4`](#insn-00bc0fe4)

~~~json
{
  "source": "00bc0fe4",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0ff0`](#insn-00bc0ff0)

~~~json
{
  "source": "00bc0ff0",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1000`](#insn-00bc1000)

~~~json
{
  "source": "00bc1000",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1008`](#insn-00bc1008)

~~~json
{
  "source": "00bc1008",
  "target": "00bc1094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1018`](#insn-00bc1018)

~~~json
{
  "source": "00bc1018",
  "target": "00bc1094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1024`](#insn-00bc1024)

~~~json
{
  "source": "00bc1024",
  "target": "00bc1040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1030`](#insn-00bc1030)

~~~json
{
  "source": "00bc1030",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1038`](#insn-00bc1038)

~~~json
{
  "source": "00bc1038",
  "target": "00bc1048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc103c`](#insn-00bc103c)

~~~json
{
  "source": "00bc103c",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1044`](#insn-00bc1044)

~~~json
{
  "source": "00bc1044",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1054`](#insn-00bc1054)

~~~json
{
  "source": "00bc1054",
  "target": "00bc108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc106c`](#insn-00bc106c)

~~~json
{
  "source": "00bc106c",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1074`](#insn-00bc1074)

~~~json
{
  "source": "00bc1074",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1080`](#insn-00bc1080)

~~~json
{
  "source": "00bc1080",
  "target": "00bc109c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1088`](#insn-00bc1088)

~~~json
{
  "source": "00bc1088",
  "target": "00bc1094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
