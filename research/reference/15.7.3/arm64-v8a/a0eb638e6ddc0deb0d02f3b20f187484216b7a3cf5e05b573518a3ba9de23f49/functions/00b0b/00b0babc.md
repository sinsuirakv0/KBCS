# 00b0babc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0b9f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0b/00b0b9f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-1826060761fede52ed77db7094ce6843)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b0bb00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0b/00b0bb00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0009.md#compare-945d0d33d914866cc6b601180c2d618d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0babc",
  "name": "_ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE",
  "size": 580,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea7a91420ddb345ec1070474ff6f242e24c6cad1563ad2110efbf73267078ddc",
  "source_text_sha256": "ea7a91420ddb345ec1070474ff6f242e24c6cad1563ad2110efbf73267078ddc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0babc",
        "00b0bcff"
      ]
    ],
    "bytes_sha256": "6d8f8e1a7dc8d9f8798fee219f70f40a3bfb8dfb23c47a70d8c344f8b4015da3",
    "instruction_count": 145,
    "instruction_bytes": 580,
    "body_bytes": 580,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdea60](../00bde/00bdea60.md)

## 呼び出し先

- [00bdead0](../00bde/00bdead0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4471 bytes

~~~c

undefined4
_ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE(int *param_1,long *param_2)

{
  uint uVar1;
  ulong uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  uint uVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ulong uVar11;
  ushort *puVar12;
  
  lVar7 = *param_2;
                    /* catch() { ... } // from try @ 00b0b8f8 with catch @ 00b0bacc */
  uVar9 = (long)param_1 - lVar7;
  if (((uVar9 & 3) == 0) || ((char)param_2[5] == '\0')) {
    uVar8 = param_2[1];
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
    iVar5 = *param_1;
    uVar6 = (int)param_2[2] + 1;
    uVar1 = (int)param_2[3] + 1;
    *(uint *)(param_2 + 2) = uVar6;
    *(uint *)(param_2 + 3) = uVar1;
    if (((((uVar6 <= *(uint *)((long)param_2 + 0x14)) && (uVar1 <= *(uint *)((long)param_2 + 0x1c)))
         && ((uVar11 = uVar9 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[5] == '\0')))) &&
        (uVar11 <= uVar8 - 2)) &&
       ((uVar4 = *(ushort *)(lVar7 + uVar11), (uVar4 & 1) == 0 || ((char)param_2[5] == '\0')))) {
      if (uVar8 <= uVar4) {
        return 0;
      }
      if (uVar8 - uVar4 < uVar11) {
        return 0;
      }
      puVar12 = (ushort *)((long)param_1 - (long)*param_1);
      if (4 < *puVar12) {
        if ((ulong)puVar12[2] != 0) {
          uVar11 = uVar9 + puVar12[2];
          if ((uVar11 & 3) == 0) {
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          else {
            if ((char)param_2[5] != '\0') {
              return 0;
            }
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          if ((int)*(uint *)(lVar7 + uVar11) < 1) {
            return 0;
          }
                    /* try { // try from 00b0bbd8 to 00c0bcbb has its CatchHandler @ 00b0bbd8
                       catch() { ... } // from try @ 00b0bbd8 with catch @ 00b0bbd8
                       catch() { ... } // from try @ 00b0bcc4 with catch @ 00b0bbd8 */
          if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
            return 0;
          }
        }
        if (((ulong)puVar12[2] != 0) &&
           (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[2]),
           puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3), puVar3 != (uint *)0x0)) {
          uVar11 = (long)puVar3 - lVar7;
          if ((uVar11 & 3) == 0) {
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          else {
            if ((char)param_2[5] != '\0') {
              return 0;
            }
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          if (0x7ffffffe < *puVar3) {
            return 0;
          }
          uVar2 = (ulong)*puVar3 + 4;
          if (uVar8 - 1 < uVar2 + uVar11) {
            return 0;
          }
          if (uVar8 <= uVar2) {
            return 0;
          }
          if (uVar8 - uVar2 < uVar11) {
            return 0;
          }
          if (*(char *)(lVar7 + uVar2 + uVar11) != '\0') {
            return 0;
          }
        }
        if (6 < *puVar12) {
          if ((ulong)puVar12[3] != 0) {
            uVar9 = uVar9 + puVar12[3];
            if ((uVar9 & 3) == 0) {
              if (uVar10 < uVar9) {
                return 0;
              }
            }
            else {
              if ((char)param_2[5] != '\0') {
                return 0;
              }
              if (uVar10 < uVar9) {
                return 0;
              }
            }
            if ((int)*(uint *)(lVar7 + uVar9) < 1) {
              return 0;
            }
                    /* try { // try from 00b0bcbc to 00c0bcc3 has its CatchHandler @ 00b0be04 */
            if (uVar8 - 1 < uVar9 + *(uint *)(lVar7 + uVar9)) {
              return 0;
            }
          }
                    /* try { // try from 00b0bcc4 to 00c0be2b has its CatchHandler @ 00b0bbd8 */
          if (((ulong)puVar12[3] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[3]),
             lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
            uVar9 = _ZNK8firebase3fbs17AndroidClientInfo6VerifyERN11flatbuffers8VerifierE(lVar7);
            if ((uVar9 & 1) == 0) {
              return 0;
            }
            uVar6 = *(uint *)(param_2 + 2);
          }
        }
      }
      *(uint *)(param_2 + 2) = uVar6 - 1;
      return 1;
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0babc"></a> `00b0babc` | `ff 83 00 d1` | sub sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b0bac0"></a> `00b0bac0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bac4"></a> `00b0bac4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0bac8"></a> `00b0bac8` | `2a 00 40 f9` | ldr x10,[x1] | `FALL_THROUGH`
<a id="insn-00b0bacc"></a> `00b0bacc` | `0c 00 0a cb` | sub x12,x0,x10 | `FALL_THROUGH`
<a id="insn-00b0bad0"></a> `00b0bad0` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bad4"></a> `00b0bad4` | `60 00 00 54` | b.eq 0x00b0bae0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bad8"></a> `00b0bad8` | `28 a0 40 39` | ldrb w8,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0badc"></a> `00b0badc` | `e8 03 00 35` | cbnz w8,0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bae0"></a> `00b0bae0` | `2b 04 40 f9` | ldr x11,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b0bae4"></a> `00b0bae4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bae8"></a> `00b0bae8` | `7f 15 00 f1` | cmp x11,#0x5 | `FALL_THROUGH`
<a id="insn-00b0baec"></a> `00b0baec` | `83 03 00 54` | b.cc 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0baf0"></a> `00b0baf0` | `6d 11 00 d1` | sub x13,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b0baf4"></a> `00b0baf4` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0baf8"></a> `00b0baf8` | `23 03 00 54` | b.cc 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bafc"></a> `00b0bafc` | `29 3c 42 29` | ldp w9,w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bb00"></a> `00b0bb00` | `2e 18 40 b9` | ldr w14,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b0bb04"></a> `00b0bb04` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0bb08"></a> `00b0bb08` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bb0c"></a> `00b0bb0c` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bb10"></a> `00b0bb10` | `3f 01 0f 6b` | cmp w9,w15 | `FALL_THROUGH`
<a id="insn-00b0bb14"></a> `00b0bb14` | `29 10 00 b9` | str w9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bb18"></a> `00b0bb18` | `2e 18 00 b9` | str w14,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b0bb1c"></a> `00b0bb1c` | `e8 01 00 54` | b.hi 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb20"></a> `00b0bb20` | `2f 1c 40 b9` | ldr w15,[x1, #0x1c] | `FALL_THROUGH`
<a id="insn-00b0bb24"></a> `00b0bb24` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b0bb28"></a> `00b0bb28` | `88 01 00 54` | b.hi 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb2c"></a> `00b0bb2c` | `8e 01 08 cb` | sub x14,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bb30"></a> `00b0bb30` | `6e 00 00 36` | tbz w14,#0x0,0x00b0bb3c | `CONDITIONAL_JUMP`
<a id="insn-00b0bb34"></a> `00b0bb34` | `28 a0 40 39` | ldrb w8,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bb38"></a> `00b0bb38` | `08 01 00 35` | cbnz w8,0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb3c"></a> `00b0bb3c` | `68 09 00 d1` | sub x8,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b0bb40"></a> `00b0bb40` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00b0bb44"></a> `00b0bb44` | `a3 00 00 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb48"></a> `00b0bb48` | `48 69 6e 78` | ldrh w8,[x10, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0bb4c"></a> `00b0bb4c` | `08 01 00 36` | tbz w8,#0x0,0x00b0bb6c | `CONDITIONAL_JUMP`
<a id="insn-00b0bb50"></a> `00b0bb50` | `2f a0 40 39` | ldrb w15,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bb54"></a> `00b0bb54` | `cf 00 00 34` | cbz w15,0x00b0bb6c | `CONDITIONAL_JUMP`
<a id="insn-00b0bb58"></a> `00b0bb58` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bb5c"></a> `00b0bb5c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bb60"></a> `00b0bb60` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00b0bb64"></a> `00b0bb64` | `ff 83 00 91` | add sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b0bb68"></a> `00b0bb68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0bb6c"></a> `00b0bb6c` | `6f 01 08 eb` | subs x15,x11,x8 | `FALL_THROUGH`
<a id="insn-00b0bb70"></a> `00b0bb70` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bb74"></a> `00b0bb74` | `49 ff ff 54` | b.ls 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bb78"></a> `00b0bb78` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00b0bb7c"></a> `00b0bb7c` | `03 ff ff 54` | b.cc 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bb80"></a> `00b0bb80` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0bb84"></a> `00b0bb84` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0bb88"></a> `00b0bb88` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00b0bb8c"></a> `00b0bb8c` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00b0bb90"></a> `00b0bb90` | `03 0b 00 54` | b.cc 0x00b0bcf0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb94"></a> `00b0bb94` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b0bb98"></a> `00b0bb98` | `68 02 00 b4` | cbz x8,0x00b0bbe4 | `CONDITIONAL_JUMP`
<a id="insn-00b0bb9c"></a> `00b0bb9c` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bba0"></a> `00b0bba0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bba4"></a> `00b0bba4` | `e0 00 00 54` | b.eq 0x00b0bbc0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bba8"></a> `00b0bba8` | `31 a0 40 39` | ldrb w17,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bbac"></a> `00b0bbac` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bbb0"></a> `00b0bbb0` | `71 fd ff 35` | cbnz w17,0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bbb4"></a> `00b0bbb4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bbb8"></a> `00b0bbb8` | `82 00 00 54` | b.cs 0x00b0bbc8 | `CONDITIONAL_JUMP`
<a id="insn-00b0bbbc"></a> `00b0bbbc` | `e8 ff ff 17` | b 0x00b0bb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0bbc0"></a> `00b0bbc0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bbc4"></a> `00b0bbc4` | `a3 fc ff 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bbc8"></a> `00b0bbc8` | `48 69 70 b8` | ldr w8,[x10, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0bbcc"></a> `00b0bbcc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bbd0"></a> `00b0bbd0` | `4b fc ff 54` | b.lt 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bbd4"></a> `00b0bbd4` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00b0bbd8"></a> `00b0bbd8` | `70 05 00 d1` | sub x16,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bbdc"></a> `00b0bbdc` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00b0bbe0"></a> `00b0bbe0` | `c3 fb ff 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bbe4"></a> `00b0bbe4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b0bbe8"></a> `00b0bbe8` | `28 04 00 b4` | cbz x8,0x00b0bc6c | `CONDITIONAL_JUMP`
<a id="insn-00b0bbec"></a> `00b0bbec` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0bbf0"></a> `00b0bbf0` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00b0bbf4"></a> `00b0bbf4` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00b0bbf8"></a> `00b0bbf8` | `a0 03 00 54` | b.eq 0x00b0bc6c | `CONDITIONAL_JUMP`
<a id="insn-00b0bbfc"></a> `00b0bbfc` | `30 02 0a cb` | sub x16,x17,x10 | `FALL_THROUGH`
<a id="insn-00b0bc00"></a> `00b0bc00` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bc04"></a> `00b0bc04` | `e0 00 00 54` | b.eq 0x00b0bc20 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc08"></a> `00b0bc08` | `22 a0 40 39` | ldrb w2,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bc0c"></a> `00b0bc0c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bc10"></a> `00b0bc10` | `62 fa ff 35` | cbnz w2,0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bc14"></a> `00b0bc14` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bc18"></a> `00b0bc18` | `82 00 00 54` | b.cs 0x00b0bc28 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc1c"></a> `00b0bc1c` | `d0 ff ff 17` | b 0x00b0bb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0bc20"></a> `00b0bc20` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bc24"></a> `00b0bc24` | `a3 f9 ff 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc28"></a> `00b0bc28` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00b0bc2c"></a> `00b0bc2c` | `f1 77 1f 32` | orr w17,wzr,#0x7ffffffe | `FALL_THROUGH`
<a id="insn-00b0bc30"></a> `00b0bc30` | `1f 01 11 6b` | cmp w8,w17 | `FALL_THROUGH`
<a id="insn-00b0bc34"></a> `00b0bc34` | `28 f9 ff 54` | b.hi 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc38"></a> `00b0bc38` | `02 11 00 91` | add x2,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b0bc3c"></a> `00b0bc3c` | `51 00 10 8b` | add x17,x2,x16 | `FALL_THROUGH`
<a id="insn-00b0bc40"></a> `00b0bc40` | `68 05 00 d1` | sub x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bc44"></a> `00b0bc44` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00b0bc48"></a> `00b0bc48` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bc4c"></a> `00b0bc4c` | `83 f8 ff 54` | b.cc 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bc50"></a> `00b0bc50` | `7f 01 02 eb` | cmp x11,x2 | `FALL_THROUGH`
<a id="insn-00b0bc54"></a> `00b0bc54` | `49 f8 ff 54` | b.ls 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bc58"></a> `00b0bc58` | `62 01 02 cb` | sub x2,x11,x2 | `FALL_THROUGH`
<a id="insn-00b0bc5c"></a> `00b0bc5c` | `5f 00 10 eb` | cmp x2,x16 | `FALL_THROUGH`
<a id="insn-00b0bc60"></a> `00b0bc60` | `e3 f7 ff 54` | b.cc 0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bc64"></a> `00b0bc64` | `48 69 71 38` | ldrb w8,[x10, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00b0bc68"></a> `00b0bc68` | `88 f7 ff 35` | cbnz w8,0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc6c"></a> `00b0bc6c` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00b0bc70"></a> `00b0bc70` | `03 04 00 54` | b.cc 0x00b0bcf0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc74"></a> `00b0bc74` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b0bc78"></a> `00b0bc78` | `68 02 00 b4` | cbz x8,0x00b0bcc4 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc7c"></a> `00b0bc7c` | `8c 01 08 8b` | add x12,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bc80"></a> `00b0bc80` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bc84"></a> `00b0bc84` | `e0 00 00 54` | b.eq 0x00b0bca0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc88"></a> `00b0bc88` | `2f a0 40 39` | ldrb w15,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bc8c"></a> `00b0bc8c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bc90"></a> `00b0bc90` | `6f f6 ff 35` | cbnz w15,0x00b0bb5c | `CONDITIONAL_JUMP`
<a id="insn-00b0bc94"></a> `00b0bc94` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0bc98"></a> `00b0bc98` | `82 00 00 54` | b.cs 0x00b0bca8 | `CONDITIONAL_JUMP`
<a id="insn-00b0bc9c"></a> `00b0bc9c` | `b0 ff ff 17` | b 0x00b0bb5c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0bca0"></a> `00b0bca0` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0bca4"></a> `00b0bca4` | `a3 f5 ff 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bca8"></a> `00b0bca8` | `48 69 6c b8` | ldr w8,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0bcac"></a> `00b0bcac` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bcb0"></a> `00b0bcb0` | `4b f5 ff 54` | b.lt 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bcb4"></a> `00b0bcb4` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bcb8"></a> `00b0bcb8` | `6a 05 00 d1` | sub x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bcbc"></a> `00b0bcbc` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b0bcc0"></a> `00b0bcc0` | `c3 f4 ff 54` | b.cc 0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bcc4"></a> `00b0bcc4` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b0bcc8"></a> `00b0bcc8` | `48 01 00 b4` | cbz x8,0x00b0bcf0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bccc"></a> `00b0bccc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0bcd0"></a> `00b0bcd0` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b0bcd4"></a> `00b0bcd4` | `00 01 0a ab` | adds x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b0bcd8"></a> `00b0bcd8` | `c0 00 00 54` | b.eq 0x00b0bcf0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bcdc"></a> `00b0bcdc` | `e1 07 00 f9` | str x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0bce0"></a> `00b0bce0` | `7c 4b 03 94` | bl 0x00bdead0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0bce4"></a> `00b0bce4` | `a0 f3 07 36` | tbz w0,#0x0,0x00b0bb58 | `CONDITIONAL_JUMP`
<a id="insn-00b0bce8"></a> `00b0bce8` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0bcec"></a> `00b0bcec` | `29 10 40 b9` | ldr w9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bcf0"></a> `00b0bcf0` | `28 05 00 51` | sub w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bcf4"></a> `00b0bcf4` | `28 10 00 b9` | str w8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bcf8"></a> `00b0bcf8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bcfc"></a> `00b0bcfc` | `98 ff ff 17` | b 0x00b0bb5c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b0babc`](#insn-00b0babc) 範囲 `[['00b0babc', '00b0bacb']]`
  - `FALL_THROUGH` [`00b0bac8`](#insn-00b0bac8) → [`00b0bacc`](#insn-00b0bacc)
- ブロック [`00b0bacc`](#insn-00b0bacc) 範囲 `[['00b0bacc', '00b0bad7']]`
  - `CONDITIONAL_JUMP` [`00b0bad4`](#insn-00b0bad4) → [`00b0bae0`](#insn-00b0bae0)
  - `FALL_THROUGH` [`00b0bad4`](#insn-00b0bad4) → [`00b0bad8`](#insn-00b0bad8)
- ブロック [`00b0bad8`](#insn-00b0bad8) 範囲 `[['00b0bad8', '00b0badf']]`
  - `CONDITIONAL_JUMP` [`00b0badc`](#insn-00b0badc) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0badc`](#insn-00b0badc) → [`00b0bae0`](#insn-00b0bae0)
- ブロック [`00b0bae0`](#insn-00b0bae0) 範囲 `[['00b0bae0', '00b0baef']]`
  - `CONDITIONAL_JUMP` [`00b0baec`](#insn-00b0baec) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0baec`](#insn-00b0baec) → [`00b0baf0`](#insn-00b0baf0)
- ブロック [`00b0baf0`](#insn-00b0baf0) 範囲 `[['00b0baf0', '00b0bafb']]`
  - `CONDITIONAL_JUMP` [`00b0baf8`](#insn-00b0baf8) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0baf8`](#insn-00b0baf8) → [`00b0bafc`](#insn-00b0bafc)
- ブロック [`00b0bafc`](#insn-00b0bafc) 範囲 `[['00b0bafc', '00b0bb1f']]`
  - `CONDITIONAL_JUMP` [`00b0bb1c`](#insn-00b0bb1c) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bb1c`](#insn-00b0bb1c) → [`00b0bb20`](#insn-00b0bb20)
- ブロック [`00b0bb20`](#insn-00b0bb20) 範囲 `[['00b0bb20', '00b0bb2b']]`
  - `CONDITIONAL_JUMP` [`00b0bb28`](#insn-00b0bb28) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bb28`](#insn-00b0bb28) → [`00b0bb2c`](#insn-00b0bb2c)
- ブロック [`00b0bb2c`](#insn-00b0bb2c) 範囲 `[['00b0bb2c', '00b0bb33']]`
  - `CONDITIONAL_JUMP` [`00b0bb30`](#insn-00b0bb30) → [`00b0bb3c`](#insn-00b0bb3c)
  - `FALL_THROUGH` [`00b0bb30`](#insn-00b0bb30) → [`00b0bb34`](#insn-00b0bb34)
- ブロック [`00b0bb34`](#insn-00b0bb34) 範囲 `[['00b0bb34', '00b0bb3b']]`
  - `CONDITIONAL_JUMP` [`00b0bb38`](#insn-00b0bb38) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bb38`](#insn-00b0bb38) → [`00b0bb3c`](#insn-00b0bb3c)
- ブロック [`00b0bb3c`](#insn-00b0bb3c) 範囲 `[['00b0bb3c', '00b0bb47']]`
  - `CONDITIONAL_JUMP` [`00b0bb44`](#insn-00b0bb44) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bb44`](#insn-00b0bb44) → [`00b0bb48`](#insn-00b0bb48)
- ブロック [`00b0bb48`](#insn-00b0bb48) 範囲 `[['00b0bb48', '00b0bb4f']]`
  - `CONDITIONAL_JUMP` [`00b0bb4c`](#insn-00b0bb4c) → [`00b0bb6c`](#insn-00b0bb6c)
  - `FALL_THROUGH` [`00b0bb4c`](#insn-00b0bb4c) → [`00b0bb50`](#insn-00b0bb50)
- ブロック [`00b0bb50`](#insn-00b0bb50) 範囲 `[['00b0bb50', '00b0bb57']]`
  - `CONDITIONAL_JUMP` [`00b0bb54`](#insn-00b0bb54) → [`00b0bb6c`](#insn-00b0bb6c)
  - `FALL_THROUGH` [`00b0bb54`](#insn-00b0bb54) → [`00b0bb58`](#insn-00b0bb58)
- ブロック [`00b0bb58`](#insn-00b0bb58) 範囲 `[['00b0bb58', '00b0bb5b']]`
  - `FALL_THROUGH` [`00b0bb58`](#insn-00b0bb58) → [`00b0bb5c`](#insn-00b0bb5c)
- ブロック [`00b0bb5c`](#insn-00b0bb5c) 範囲 `[['00b0bb5c', '00b0bb6b']]`
- ブロック [`00b0bb6c`](#insn-00b0bb6c) 範囲 `[['00b0bb6c', '00b0bb77']]`
  - `CONDITIONAL_JUMP` [`00b0bb74`](#insn-00b0bb74) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bb74`](#insn-00b0bb74) → [`00b0bb78`](#insn-00b0bb78)
- ブロック [`00b0bb78`](#insn-00b0bb78) 範囲 `[['00b0bb78', '00b0bb7f']]`
  - `CONDITIONAL_JUMP` [`00b0bb7c`](#insn-00b0bb7c) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bb7c`](#insn-00b0bb7c) → [`00b0bb80`](#insn-00b0bb80)
- ブロック [`00b0bb80`](#insn-00b0bb80) 範囲 `[['00b0bb80', '00b0bb93']]`
  - `CONDITIONAL_JUMP` [`00b0bb90`](#insn-00b0bb90) → [`00b0bcf0`](#insn-00b0bcf0)
  - `FALL_THROUGH` [`00b0bb90`](#insn-00b0bb90) → [`00b0bb94`](#insn-00b0bb94)
- ブロック [`00b0bb94`](#insn-00b0bb94) 範囲 `[['00b0bb94', '00b0bb9b']]`
  - `CONDITIONAL_JUMP` [`00b0bb98`](#insn-00b0bb98) → [`00b0bbe4`](#insn-00b0bbe4)
  - `FALL_THROUGH` [`00b0bb98`](#insn-00b0bb98) → [`00b0bb9c`](#insn-00b0bb9c)
- ブロック [`00b0bb9c`](#insn-00b0bb9c) 範囲 `[['00b0bb9c', '00b0bba7']]`
  - `CONDITIONAL_JUMP` [`00b0bba4`](#insn-00b0bba4) → [`00b0bbc0`](#insn-00b0bbc0)
  - `FALL_THROUGH` [`00b0bba4`](#insn-00b0bba4) → [`00b0bba8`](#insn-00b0bba8)
- ブロック [`00b0bba8`](#insn-00b0bba8) 範囲 `[['00b0bba8', '00b0bbb3']]`
  - `CONDITIONAL_JUMP` [`00b0bbb0`](#insn-00b0bbb0) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bbb0`](#insn-00b0bbb0) → [`00b0bbb4`](#insn-00b0bbb4)
- ブロック [`00b0bbb4`](#insn-00b0bbb4) 範囲 `[['00b0bbb4', '00b0bbbb']]`
  - `CONDITIONAL_JUMP` [`00b0bbb8`](#insn-00b0bbb8) → [`00b0bbc8`](#insn-00b0bbc8)
  - `FALL_THROUGH` [`00b0bbb8`](#insn-00b0bbb8) → [`00b0bbbc`](#insn-00b0bbbc)
- ブロック [`00b0bbbc`](#insn-00b0bbbc) 範囲 `[['00b0bbbc', '00b0bbbf']]`
  - `UNCONDITIONAL_JUMP` [`00b0bbbc`](#insn-00b0bbbc) → [`00b0bb5c`](#insn-00b0bb5c)
- ブロック [`00b0bbc0`](#insn-00b0bbc0) 範囲 `[['00b0bbc0', '00b0bbc7']]`
  - `CONDITIONAL_JUMP` [`00b0bbc4`](#insn-00b0bbc4) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bbc4`](#insn-00b0bbc4) → [`00b0bbc8`](#insn-00b0bbc8)
- ブロック [`00b0bbc8`](#insn-00b0bbc8) 範囲 `[['00b0bbc8', '00b0bbd3']]`
  - `CONDITIONAL_JUMP` [`00b0bbd0`](#insn-00b0bbd0) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bbd0`](#insn-00b0bbd0) → [`00b0bbd4`](#insn-00b0bbd4)
- ブロック [`00b0bbd4`](#insn-00b0bbd4) 範囲 `[['00b0bbd4', '00b0bbd7']]`
  - `FALL_THROUGH` [`00b0bbd4`](#insn-00b0bbd4) → [`00b0bbd8`](#insn-00b0bbd8)
- ブロック [`00b0bbd8`](#insn-00b0bbd8) 範囲 `[['00b0bbd8', '00b0bbe3']]`
  - `CONDITIONAL_JUMP` [`00b0bbe0`](#insn-00b0bbe0) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bbe0`](#insn-00b0bbe0) → [`00b0bbe4`](#insn-00b0bbe4)
- ブロック [`00b0bbe4`](#insn-00b0bbe4) 範囲 `[['00b0bbe4', '00b0bbeb']]`
  - `CONDITIONAL_JUMP` [`00b0bbe8`](#insn-00b0bbe8) → [`00b0bc6c`](#insn-00b0bc6c)
  - `FALL_THROUGH` [`00b0bbe8`](#insn-00b0bbe8) → [`00b0bbec`](#insn-00b0bbec)
- ブロック [`00b0bbec`](#insn-00b0bbec) 範囲 `[['00b0bbec', '00b0bbfb']]`
  - `CONDITIONAL_JUMP` [`00b0bbf8`](#insn-00b0bbf8) → [`00b0bc6c`](#insn-00b0bc6c)
  - `FALL_THROUGH` [`00b0bbf8`](#insn-00b0bbf8) → [`00b0bbfc`](#insn-00b0bbfc)
- ブロック [`00b0bbfc`](#insn-00b0bbfc) 範囲 `[['00b0bbfc', '00b0bc07']]`
  - `CONDITIONAL_JUMP` [`00b0bc04`](#insn-00b0bc04) → [`00b0bc20`](#insn-00b0bc20)
  - `FALL_THROUGH` [`00b0bc04`](#insn-00b0bc04) → [`00b0bc08`](#insn-00b0bc08)
- ブロック [`00b0bc08`](#insn-00b0bc08) 範囲 `[['00b0bc08', '00b0bc13']]`
  - `CONDITIONAL_JUMP` [`00b0bc10`](#insn-00b0bc10) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bc10`](#insn-00b0bc10) → [`00b0bc14`](#insn-00b0bc14)
- ブロック [`00b0bc14`](#insn-00b0bc14) 範囲 `[['00b0bc14', '00b0bc1b']]`
  - `CONDITIONAL_JUMP` [`00b0bc18`](#insn-00b0bc18) → [`00b0bc28`](#insn-00b0bc28)
  - `FALL_THROUGH` [`00b0bc18`](#insn-00b0bc18) → [`00b0bc1c`](#insn-00b0bc1c)
- ブロック [`00b0bc1c`](#insn-00b0bc1c) 範囲 `[['00b0bc1c', '00b0bc1f']]`
  - `UNCONDITIONAL_JUMP` [`00b0bc1c`](#insn-00b0bc1c) → [`00b0bb5c`](#insn-00b0bb5c)
- ブロック [`00b0bc20`](#insn-00b0bc20) 範囲 `[['00b0bc20', '00b0bc27']]`
  - `CONDITIONAL_JUMP` [`00b0bc24`](#insn-00b0bc24) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bc24`](#insn-00b0bc24) → [`00b0bc28`](#insn-00b0bc28)
- ブロック [`00b0bc28`](#insn-00b0bc28) 範囲 `[['00b0bc28', '00b0bc37']]`
  - `CONDITIONAL_JUMP` [`00b0bc34`](#insn-00b0bc34) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bc34`](#insn-00b0bc34) → [`00b0bc38`](#insn-00b0bc38)
- ブロック [`00b0bc38`](#insn-00b0bc38) 範囲 `[['00b0bc38', '00b0bc4f']]`
  - `CONDITIONAL_JUMP` [`00b0bc4c`](#insn-00b0bc4c) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bc4c`](#insn-00b0bc4c) → [`00b0bc50`](#insn-00b0bc50)
- ブロック [`00b0bc50`](#insn-00b0bc50) 範囲 `[['00b0bc50', '00b0bc57']]`
  - `CONDITIONAL_JUMP` [`00b0bc54`](#insn-00b0bc54) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bc54`](#insn-00b0bc54) → [`00b0bc58`](#insn-00b0bc58)
- ブロック [`00b0bc58`](#insn-00b0bc58) 範囲 `[['00b0bc58', '00b0bc63']]`
  - `CONDITIONAL_JUMP` [`00b0bc60`](#insn-00b0bc60) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bc60`](#insn-00b0bc60) → [`00b0bc64`](#insn-00b0bc64)
- ブロック [`00b0bc64`](#insn-00b0bc64) 範囲 `[['00b0bc64', '00b0bc6b']]`
  - `CONDITIONAL_JUMP` [`00b0bc68`](#insn-00b0bc68) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bc68`](#insn-00b0bc68) → [`00b0bc6c`](#insn-00b0bc6c)
- ブロック [`00b0bc6c`](#insn-00b0bc6c) 範囲 `[['00b0bc6c', '00b0bc73']]`
  - `CONDITIONAL_JUMP` [`00b0bc70`](#insn-00b0bc70) → [`00b0bcf0`](#insn-00b0bcf0)
  - `FALL_THROUGH` [`00b0bc70`](#insn-00b0bc70) → [`00b0bc74`](#insn-00b0bc74)
- ブロック [`00b0bc74`](#insn-00b0bc74) 範囲 `[['00b0bc74', '00b0bc7b']]`
  - `CONDITIONAL_JUMP` [`00b0bc78`](#insn-00b0bc78) → [`00b0bcc4`](#insn-00b0bcc4)
  - `FALL_THROUGH` [`00b0bc78`](#insn-00b0bc78) → [`00b0bc7c`](#insn-00b0bc7c)
- ブロック [`00b0bc7c`](#insn-00b0bc7c) 範囲 `[['00b0bc7c', '00b0bc87']]`
  - `CONDITIONAL_JUMP` [`00b0bc84`](#insn-00b0bc84) → [`00b0bca0`](#insn-00b0bca0)
  - `FALL_THROUGH` [`00b0bc84`](#insn-00b0bc84) → [`00b0bc88`](#insn-00b0bc88)
- ブロック [`00b0bc88`](#insn-00b0bc88) 範囲 `[['00b0bc88', '00b0bc93']]`
  - `CONDITIONAL_JUMP` [`00b0bc90`](#insn-00b0bc90) → [`00b0bb5c`](#insn-00b0bb5c)
  - `FALL_THROUGH` [`00b0bc90`](#insn-00b0bc90) → [`00b0bc94`](#insn-00b0bc94)
- ブロック [`00b0bc94`](#insn-00b0bc94) 範囲 `[['00b0bc94', '00b0bc9b']]`
  - `CONDITIONAL_JUMP` [`00b0bc98`](#insn-00b0bc98) → [`00b0bca8`](#insn-00b0bca8)
  - `FALL_THROUGH` [`00b0bc98`](#insn-00b0bc98) → [`00b0bc9c`](#insn-00b0bc9c)
- ブロック [`00b0bc9c`](#insn-00b0bc9c) 範囲 `[['00b0bc9c', '00b0bc9f']]`
  - `UNCONDITIONAL_JUMP` [`00b0bc9c`](#insn-00b0bc9c) → [`00b0bb5c`](#insn-00b0bb5c)
- ブロック [`00b0bca0`](#insn-00b0bca0) 範囲 `[['00b0bca0', '00b0bca7']]`
  - `CONDITIONAL_JUMP` [`00b0bca4`](#insn-00b0bca4) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bca4`](#insn-00b0bca4) → [`00b0bca8`](#insn-00b0bca8)
- ブロック [`00b0bca8`](#insn-00b0bca8) 範囲 `[['00b0bca8', '00b0bcb3']]`
  - `CONDITIONAL_JUMP` [`00b0bcb0`](#insn-00b0bcb0) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bcb0`](#insn-00b0bcb0) → [`00b0bcb4`](#insn-00b0bcb4)
- ブロック [`00b0bcb4`](#insn-00b0bcb4) 範囲 `[['00b0bcb4', '00b0bcbb']]`
  - `FALL_THROUGH` [`00b0bcb8`](#insn-00b0bcb8) → [`00b0bcbc`](#insn-00b0bcbc)
- ブロック [`00b0bcbc`](#insn-00b0bcbc) 範囲 `[['00b0bcbc', '00b0bcc3']]`
  - `CONDITIONAL_JUMP` [`00b0bcc0`](#insn-00b0bcc0) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bcc0`](#insn-00b0bcc0) → [`00b0bcc4`](#insn-00b0bcc4)
- ブロック [`00b0bcc4`](#insn-00b0bcc4) 範囲 `[['00b0bcc4', '00b0bccb']]`
  - `CONDITIONAL_JUMP` [`00b0bcc8`](#insn-00b0bcc8) → [`00b0bcf0`](#insn-00b0bcf0)
  - `FALL_THROUGH` [`00b0bcc8`](#insn-00b0bcc8) → [`00b0bccc`](#insn-00b0bccc)
- ブロック [`00b0bccc`](#insn-00b0bccc) 範囲 `[['00b0bccc', '00b0bcdb']]`
  - `CONDITIONAL_JUMP` [`00b0bcd8`](#insn-00b0bcd8) → [`00b0bcf0`](#insn-00b0bcf0)
  - `FALL_THROUGH` [`00b0bcd8`](#insn-00b0bcd8) → [`00b0bcdc`](#insn-00b0bcdc)
- ブロック [`00b0bcdc`](#insn-00b0bcdc) 範囲 `[['00b0bcdc', '00b0bce7']]`
  - `CONDITIONAL_JUMP` [`00b0bce4`](#insn-00b0bce4) → [`00b0bb58`](#insn-00b0bb58)
  - `FALL_THROUGH` [`00b0bce4`](#insn-00b0bce4) → [`00b0bce8`](#insn-00b0bce8)
- ブロック [`00b0bce8`](#insn-00b0bce8) 範囲 `[['00b0bce8', '00b0bcef']]`
  - `FALL_THROUGH` [`00b0bcec`](#insn-00b0bcec) → [`00b0bcf0`](#insn-00b0bcf0)
- ブロック [`00b0bcf0`](#insn-00b0bcf0) 範囲 `[['00b0bcf0', '00b0bcff']]`
  - `UNCONDITIONAL_JUMP` [`00b0bcfc`](#insn-00b0bcfc) → [`00b0bb5c`](#insn-00b0bb5c)

## 命令位置別の参照

- [`00b0bac0`](#insn-00b0bac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bad4`](#insn-00b0bad4) → [`00b0bae0`](#insn-00b0bae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0badc`](#insn-00b0badc) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0baec`](#insn-00b0baec) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0baf8`](#insn-00b0baf8) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb1c`](#insn-00b0bb1c) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb28`](#insn-00b0bb28) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb30`](#insn-00b0bb30) → [`00b0bb3c`](#insn-00b0bb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb38`](#insn-00b0bb38) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb44`](#insn-00b0bb44) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb4c`](#insn-00b0bb4c) → [`00b0bb6c`](#insn-00b0bb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb54`](#insn-00b0bb54) → [`00b0bb6c`](#insn-00b0bb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb5c`](#insn-00b0bb5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb74`](#insn-00b0bb74) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb7c`](#insn-00b0bb7c) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb90`](#insn-00b0bb90) → [`00b0bcf0`](#insn-00b0bcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bb98`](#insn-00b0bb98) → [`00b0bbe4`](#insn-00b0bbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bba4`](#insn-00b0bba4) → [`00b0bbc0`](#insn-00b0bbc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbb0`](#insn-00b0bbb0) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbb8`](#insn-00b0bbb8) → [`00b0bbc8`](#insn-00b0bbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbbc`](#insn-00b0bbbc) → [`00b0bb5c`](#insn-00b0bb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbc4`](#insn-00b0bbc4) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbd0`](#insn-00b0bbd0) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbe0`](#insn-00b0bbe0) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbe8`](#insn-00b0bbe8) → [`00b0bc6c`](#insn-00b0bc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bbf8`](#insn-00b0bbf8) → [`00b0bc6c`](#insn-00b0bc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc04`](#insn-00b0bc04) → [`00b0bc20`](#insn-00b0bc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc10`](#insn-00b0bc10) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc18`](#insn-00b0bc18) → [`00b0bc28`](#insn-00b0bc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc1c`](#insn-00b0bc1c) → [`00b0bb5c`](#insn-00b0bb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc24`](#insn-00b0bc24) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc34`](#insn-00b0bc34) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc4c`](#insn-00b0bc4c) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc54`](#insn-00b0bc54) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc60`](#insn-00b0bc60) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc68`](#insn-00b0bc68) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc70`](#insn-00b0bc70) → [`00b0bcf0`](#insn-00b0bcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc78`](#insn-00b0bc78) → [`00b0bcc4`](#insn-00b0bcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc84`](#insn-00b0bc84) → [`00b0bca0`](#insn-00b0bca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc90`](#insn-00b0bc90) → [`00b0bb5c`](#insn-00b0bb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc98`](#insn-00b0bc98) → [`00b0bca8`](#insn-00b0bca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bc9c`](#insn-00b0bc9c) → [`00b0bb5c`](#insn-00b0bb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bca4`](#insn-00b0bca4) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcb0`](#insn-00b0bcb0) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcc0`](#insn-00b0bcc0) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcc8`](#insn-00b0bcc8) → [`00b0bcf0`](#insn-00b0bcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcd8`](#insn-00b0bcd8) → [`00b0bcf0`](#insn-00b0bcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcdc`](#insn-00b0bcdc) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bce0`](#insn-00b0bce0) → [`00bdead0`](../00bde/00bdead0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdead0` · 推定シンボル `None` · 推定型 `None`
- [`00b0bce4`](#insn-00b0bce4) → [`00b0bb58`](#insn-00b0bb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bce8`](#insn-00b0bce8) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bcfc`](#insn-00b0bcfc) → [`00b0bb5c`](#insn-00b0bb5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0bac0`](#insn-00b0bac0)

~~~json
{
  "source": "00b0bac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bad4`](#insn-00b0bad4)

~~~json
{
  "source": "00b0bad4",
  "target": "00b0bae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0badc`](#insn-00b0badc)

~~~json
{
  "source": "00b0badc",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0baec`](#insn-00b0baec)

~~~json
{
  "source": "00b0baec",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0baf8`](#insn-00b0baf8)

~~~json
{
  "source": "00b0baf8",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb1c`](#insn-00b0bb1c)

~~~json
{
  "source": "00b0bb1c",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb28`](#insn-00b0bb28)

~~~json
{
  "source": "00b0bb28",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb30`](#insn-00b0bb30)

~~~json
{
  "source": "00b0bb30",
  "target": "00b0bb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb38`](#insn-00b0bb38)

~~~json
{
  "source": "00b0bb38",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb44`](#insn-00b0bb44)

~~~json
{
  "source": "00b0bb44",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb4c`](#insn-00b0bb4c)

~~~json
{
  "source": "00b0bb4c",
  "target": "00b0bb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb54`](#insn-00b0bb54)

~~~json
{
  "source": "00b0bb54",
  "target": "00b0bb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb5c`](#insn-00b0bb5c)

~~~json
{
  "source": "00b0bb5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb74`](#insn-00b0bb74)

~~~json
{
  "source": "00b0bb74",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb7c`](#insn-00b0bb7c)

~~~json
{
  "source": "00b0bb7c",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb90`](#insn-00b0bb90)

~~~json
{
  "source": "00b0bb90",
  "target": "00b0bcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bb98`](#insn-00b0bb98)

~~~json
{
  "source": "00b0bb98",
  "target": "00b0bbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bba4`](#insn-00b0bba4)

~~~json
{
  "source": "00b0bba4",
  "target": "00b0bbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbb0`](#insn-00b0bbb0)

~~~json
{
  "source": "00b0bbb0",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbb8`](#insn-00b0bbb8)

~~~json
{
  "source": "00b0bbb8",
  "target": "00b0bbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbbc`](#insn-00b0bbbc)

~~~json
{
  "source": "00b0bbbc",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbc4`](#insn-00b0bbc4)

~~~json
{
  "source": "00b0bbc4",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbd0`](#insn-00b0bbd0)

~~~json
{
  "source": "00b0bbd0",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbe0`](#insn-00b0bbe0)

~~~json
{
  "source": "00b0bbe0",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbe8`](#insn-00b0bbe8)

~~~json
{
  "source": "00b0bbe8",
  "target": "00b0bc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bbf8`](#insn-00b0bbf8)

~~~json
{
  "source": "00b0bbf8",
  "target": "00b0bc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc04`](#insn-00b0bc04)

~~~json
{
  "source": "00b0bc04",
  "target": "00b0bc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc10`](#insn-00b0bc10)

~~~json
{
  "source": "00b0bc10",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc18`](#insn-00b0bc18)

~~~json
{
  "source": "00b0bc18",
  "target": "00b0bc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc1c`](#insn-00b0bc1c)

~~~json
{
  "source": "00b0bc1c",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc24`](#insn-00b0bc24)

~~~json
{
  "source": "00b0bc24",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc34`](#insn-00b0bc34)

~~~json
{
  "source": "00b0bc34",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc4c`](#insn-00b0bc4c)

~~~json
{
  "source": "00b0bc4c",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc54`](#insn-00b0bc54)

~~~json
{
  "source": "00b0bc54",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc60`](#insn-00b0bc60)

~~~json
{
  "source": "00b0bc60",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc68`](#insn-00b0bc68)

~~~json
{
  "source": "00b0bc68",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc70`](#insn-00b0bc70)

~~~json
{
  "source": "00b0bc70",
  "target": "00b0bcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc78`](#insn-00b0bc78)

~~~json
{
  "source": "00b0bc78",
  "target": "00b0bcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc84`](#insn-00b0bc84)

~~~json
{
  "source": "00b0bc84",
  "target": "00b0bca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc90`](#insn-00b0bc90)

~~~json
{
  "source": "00b0bc90",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc98`](#insn-00b0bc98)

~~~json
{
  "source": "00b0bc98",
  "target": "00b0bca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bc9c`](#insn-00b0bc9c)

~~~json
{
  "source": "00b0bc9c",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bca4`](#insn-00b0bca4)

~~~json
{
  "source": "00b0bca4",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcb0`](#insn-00b0bcb0)

~~~json
{
  "source": "00b0bcb0",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcc0`](#insn-00b0bcc0)

~~~json
{
  "source": "00b0bcc0",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcc8`](#insn-00b0bcc8)

~~~json
{
  "source": "00b0bcc8",
  "target": "00b0bcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcd8`](#insn-00b0bcd8)

~~~json
{
  "source": "00b0bcd8",
  "target": "00b0bcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcdc`](#insn-00b0bcdc)

~~~json
{
  "source": "00b0bcdc",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bce0`](#insn-00b0bce0)

~~~json
{
  "source": "00b0bce0",
  "target": "00bdead0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0bce4`](#insn-00b0bce4)

~~~json
{
  "source": "00b0bce4",
  "target": "00b0bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bce8`](#insn-00b0bce8)

~~~json
{
  "source": "00b0bce8",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bcfc`](#insn-00b0bcfc)

~~~json
{
  "source": "00b0bcfc",
  "target": "00b0bb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
