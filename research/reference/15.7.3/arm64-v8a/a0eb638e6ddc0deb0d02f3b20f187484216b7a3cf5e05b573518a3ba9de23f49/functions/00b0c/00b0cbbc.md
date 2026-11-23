# 00b0cbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0caf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0064.md#compare-c84b996e31f6db5c896c181e2811a959)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b0cc00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cc00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0009.md#compare-07e9d440cc89d7a1b00cca13a3b3e64f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cbbc",
  "name": "_ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE",
  "size": 832,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87f050f7c5abffe1e4d9d7a450474fb5d5d6672cb7dee50a41043ec1b2a86f19",
  "source_text_sha256": "87f050f7c5abffe1e4d9d7a450474fb5d5d6672cb7dee50a41043ec1b2a86f19",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0cbbc",
        "00b0cefb"
      ]
    ],
    "bytes_sha256": "11676119dbbf3f65d12a6086c9ca91da4a2935e2f6c41b1229bc76fc94f334e9",
    "instruction_count": 208,
    "instruction_bytes": 832,
    "body_bytes": 832,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdea50](../00bde/00bdea50.md)

## 呼び出し先

- [00bdeab0](../00bde/00bdeab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7735 bytes

~~~c

undefined4
_ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE(int *param_1,long *param_2)

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
  
                    /* try { // try from 00b0cbc0 to 00c0cbcb has its CatchHandler @ 00b0cc40 */
  lVar7 = *param_2;
  uVar9 = (long)param_1 - lVar7;
                    /* try { // try from 00b0cbdc to 00c0cbe7 has its CatchHandler @ 00b0cc3c */
  if (((uVar9 & 3) == 0) || ((char)param_2[5] == '\0')) {
    uVar8 = param_2[1];
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
                    /* try { // try from 00b0cbf8 to 00c0cc03 has its CatchHandler @ 00b0cc38 */
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b0cc04 to 00c0cc6f has its CatchHandler @ 00b0cb5c */
    iVar5 = *param_1;
    uVar6 = (int)param_2[2] + 1;
    uVar1 = (int)param_2[3] + 1;
    *(uint *)(param_2 + 2) = uVar6;
    *(uint *)(param_2 + 3) = uVar1;
                    /* catch() { ... } // from try @ 00b0cbf8 with catch @ 00b0cc38 */
                    /* catch() { ... } // from try @ 00b0cbdc with catch @ 00b0cc3c */
                    /* catch() { ... } // from try @ 00b0cbc0 with catch @ 00b0cc40 */
                    /* catch() { ... } // from try @ 00b0cba4 with catch @ 00b0cc44 */
                    /* catch() { ... } // from try @ 00b0cb98 with catch @ 00b0cc48 */
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
      uVar4 = *puVar12;
      if (4 < uVar4) {
        if (((ulong)puVar12[2] != 0) && (uVar10 < uVar9 + puVar12[2])) {
          return 0;
        }
        if (6 < uVar4) {
          if ((ulong)puVar12[3] != 0) {
            uVar11 = uVar9 + puVar12[3];
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
            if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
              return 0;
            }
          }
          if (((ulong)puVar12[3] != 0) &&
             (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[3]),
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
          if (8 < uVar4) {
            if ((ulong)puVar12[4] != 0) {
              uVar11 = uVar9 + puVar12[4];
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
              if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
                return 0;
              }
            }
                    /* try { // try from 00b0cdf4 to 00c0ce5f has its CatchHandler @ 00b0cdf4
                       catch() { ... } // from try @ 00b0cdf4 with catch @ 00b0cdf4
                       catch() { ... } // from try @ 00b0ce68 with catch @ 00b0cdf4
                       catch() { ... } // from try @ 00b0cfa4 with catch @ 00b0cdf4 */
            if (((ulong)puVar12[4] != 0) &&
               (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[4]),
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
                    /* try { // try from 00b0ce60 to 00c0ce67 has its CatchHandler @ 00b0cfb8 */
              if (uVar8 - uVar2 < uVar11) {
                return 0;
              }
                    /* try { // try from 00b0ce68 to 00c0ce97 has its CatchHandler @ 00b0cdf4 */
              if (*(char *)(lVar7 + uVar2 + uVar11) != '\0') {
                return 0;
              }
            }
            if (10 < uVar4) {
              if ((ulong)puVar12[5] != 0) {
                uVar9 = uVar9 + puVar12[5];
                if ((uVar9 & 3) == 0) {
                  if (uVar10 < uVar9) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[5] != '\0') {
                    return 0;
                  }
                    /* try { // try from 00b0ce98 to 00c0cea3 has its CatchHandler @ 00b0cfac */
                  if (uVar10 < uVar9) {
                    return 0;
                  }
                }
                if ((int)*(uint *)(lVar7 + uVar9) < 1) {
                  return 0;
                }
                if (uVar8 - 1 < uVar9 + *(uint *)(lVar7 + uVar9)) {
                  return 0;
                }
              }
                    /* try { // try from 00b0ced8 to 00c0cedf has its CatchHandler @ 00b0cfa8 */
              if (((ulong)puVar12[5] != 0) &&
                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[5]),
                 lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
                uVar9 = _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers8VerifierE
                                  (lVar7,param_2);
                if ((uVar9 & 1) == 0) {
                  return 0;
                }
                uVar6 = *(uint *)(param_2 + 2);
              }
            }
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
<a id="insn-00b0cbbc"></a> `00b0cbbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b0cbc0"></a> `00b0cbc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cbc4"></a> `00b0cbc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0cbc8"></a> `00b0cbc8` | `2a 00 40 f9` | ldr x10,[x1] | `FALL_THROUGH`
<a id="insn-00b0cbcc"></a> `00b0cbcc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b0cbd0"></a> `00b0cbd0` | `0c 00 0a cb` | sub x12,x0,x10 | `FALL_THROUGH`
<a id="insn-00b0cbd4"></a> `00b0cbd4` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cbd8"></a> `00b0cbd8` | `60 00 00 54` | b.eq 0x00b0cbe4 | `CONDITIONAL_JUMP`
<a id="insn-00b0cbdc"></a> `00b0cbdc` | `68 a2 40 39` | ldrb w8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cbe0"></a> `00b0cbe0` | `e8 03 00 35` | cbnz w8,0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cbe4"></a> `00b0cbe4` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cbe8"></a> `00b0cbe8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cbec"></a> `00b0cbec` | `7f 15 00 f1` | cmp x11,#0x5 | `FALL_THROUGH`
<a id="insn-00b0cbf0"></a> `00b0cbf0` | `83 03 00 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cbf4"></a> `00b0cbf4` | `6d 11 00 d1` | sub x13,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b0cbf8"></a> `00b0cbf8` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0cbfc"></a> `00b0cbfc` | `23 03 00 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc00"></a> `00b0cc00` | `69 3e 42 29` | ldp w9,w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc04"></a> `00b0cc04` | `6e 1a 40 b9` | ldr w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b0cc08"></a> `00b0cc08` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0cc0c"></a> `00b0cc0c` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cc10"></a> `00b0cc10` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cc14"></a> `00b0cc14` | `3f 01 0f 6b` | cmp w9,w15 | `FALL_THROUGH`
<a id="insn-00b0cc18"></a> `00b0cc18` | `69 12 00 b9` | str w9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc1c"></a> `00b0cc1c` | `6e 1a 00 b9` | str w14,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b0cc20"></a> `00b0cc20` | `e8 01 00 54` | b.hi 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cc24"></a> `00b0cc24` | `6f 1e 40 b9` | ldr w15,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00b0cc28"></a> `00b0cc28` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b0cc2c"></a> `00b0cc2c` | `88 01 00 54` | b.hi 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cc30"></a> `00b0cc30` | `8e 01 08 cb` | sub x14,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0cc34"></a> `00b0cc34` | `6e 00 00 36` | tbz w14,#0x0,0x00b0cc40 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc38"></a> `00b0cc38` | `68 a2 40 39` | ldrb w8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cc3c"></a> `00b0cc3c` | `08 01 00 35` | cbnz w8,0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cc40"></a> `00b0cc40` | `68 09 00 d1` | sub x8,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b0cc44"></a> `00b0cc44` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00b0cc48"></a> `00b0cc48` | `a3 00 00 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cc4c"></a> `00b0cc4c` | `48 69 6e 78` | ldrh w8,[x10, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0cc50"></a> `00b0cc50` | `08 01 00 36` | tbz w8,#0x0,0x00b0cc70 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc54"></a> `00b0cc54` | `6f a2 40 39` | ldrb w15,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cc58"></a> `00b0cc58` | `cf 00 00 34` | cbz w15,0x00b0cc70 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc5c"></a> `00b0cc5c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cc60"></a> `00b0cc60` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc64"></a> `00b0cc64` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00b0cc68"></a> `00b0cc68` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b0cc6c"></a> `00b0cc6c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0cc70"></a> `00b0cc70` | `6f 01 08 eb` | subs x15,x11,x8 | `FALL_THROUGH`
<a id="insn-00b0cc74"></a> `00b0cc74` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cc78"></a> `00b0cc78` | `49 ff ff 54` | b.ls 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc7c"></a> `00b0cc7c` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00b0cc80"></a> `00b0cc80` | `03 ff ff 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc84"></a> `00b0cc84` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0cc88"></a> `00b0cc88` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0cc8c"></a> `00b0cc8c` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00b0cc90"></a> `00b0cc90` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00b0cc94"></a> `00b0cc94` | `c3 12 00 54` | b.cc 0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0cc98"></a> `00b0cc98` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b0cc9c"></a> `00b0cc9c` | `88 00 00 b4` | cbz x8,0x00b0ccac | `CONDITIONAL_JUMP`
<a id="insn-00b0cca0"></a> `00b0cca0` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0cca4"></a> `00b0cca4` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00b0cca8"></a> `00b0cca8` | `a3 fd ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ccac"></a> `00b0ccac` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00b0ccb0"></a> `00b0ccb0` | `e3 11 00 54` | b.cc 0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0ccb4"></a> `00b0ccb4` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b0ccb8"></a> `00b0ccb8` | `68 02 00 b4` | cbz x8,0x00b0cd04 | `CONDITIONAL_JUMP`
<a id="insn-00b0ccbc"></a> `00b0ccbc` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0ccc0"></a> `00b0ccc0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0ccc4"></a> `00b0ccc4` | `e0 00 00 54` | b.eq 0x00b0cce0 | `CONDITIONAL_JUMP`
<a id="insn-00b0ccc8"></a> `00b0ccc8` | `71 a2 40 39` | ldrb w17,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cccc"></a> `00b0cccc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0ccd0"></a> `00b0ccd0` | `91 fc ff 35` | cbnz w17,0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ccd4"></a> `00b0ccd4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0ccd8"></a> `00b0ccd8` | `82 00 00 54` | b.cs 0x00b0cce8 | `CONDITIONAL_JUMP`
<a id="insn-00b0ccdc"></a> `00b0ccdc` | `e1 ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cce0"></a> `00b0cce0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0cce4"></a> `00b0cce4` | `c3 fb ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cce8"></a> `00b0cce8` | `48 69 70 b8` | ldr w8,[x10, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0ccec"></a> `00b0ccec` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ccf0"></a> `00b0ccf0` | `6b fb ff 54` | b.lt 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ccf4"></a> `00b0ccf4` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00b0ccf8"></a> `00b0ccf8` | `70 05 00 d1` | sub x16,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ccfc"></a> `00b0ccfc` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00b0cd00"></a> `00b0cd00` | `e3 fa ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd04"></a> `00b0cd04` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b0cd08"></a> `00b0cd08` | `28 04 00 b4` | cbz x8,0x00b0cd8c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd0c"></a> `00b0cd0c` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0cd10"></a> `00b0cd10` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00b0cd14"></a> `00b0cd14` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00b0cd18"></a> `00b0cd18` | `a0 03 00 54` | b.eq 0x00b0cd8c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd1c"></a> `00b0cd1c` | `30 02 0a cb` | sub x16,x17,x10 | `FALL_THROUGH`
<a id="insn-00b0cd20"></a> `00b0cd20` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cd24"></a> `00b0cd24` | `e0 00 00 54` | b.eq 0x00b0cd40 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd28"></a> `00b0cd28` | `61 a2 40 39` | ldrb w1,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cd2c"></a> `00b0cd2c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cd30"></a> `00b0cd30` | `81 f9 ff 35` | cbnz w1,0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd34"></a> `00b0cd34` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0cd38"></a> `00b0cd38` | `82 00 00 54` | b.cs 0x00b0cd48 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd3c"></a> `00b0cd3c` | `c9 ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cd40"></a> `00b0cd40` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0cd44"></a> `00b0cd44` | `c3 f8 ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd48"></a> `00b0cd48` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00b0cd4c"></a> `00b0cd4c` | `f1 77 1f 32` | orr w17,wzr,#0x7ffffffe | `FALL_THROUGH`
<a id="insn-00b0cd50"></a> `00b0cd50` | `1f 01 11 6b` | cmp w8,w17 | `FALL_THROUGH`
<a id="insn-00b0cd54"></a> `00b0cd54` | `48 f8 ff 54` | b.hi 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd58"></a> `00b0cd58` | `01 11 00 91` | add x1,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b0cd5c"></a> `00b0cd5c` | `31 00 10 8b` | add x17,x1,x16 | `FALL_THROUGH`
<a id="insn-00b0cd60"></a> `00b0cd60` | `68 05 00 d1` | sub x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cd64"></a> `00b0cd64` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00b0cd68"></a> `00b0cd68` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cd6c"></a> `00b0cd6c` | `a3 f7 ff 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd70"></a> `00b0cd70` | `7f 01 01 eb` | cmp x11,x1 | `FALL_THROUGH`
<a id="insn-00b0cd74"></a> `00b0cd74` | `69 f7 ff 54` | b.ls 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd78"></a> `00b0cd78` | `61 01 01 cb` | sub x1,x11,x1 | `FALL_THROUGH`
<a id="insn-00b0cd7c"></a> `00b0cd7c` | `3f 00 10 eb` | cmp x1,x16 | `FALL_THROUGH`
<a id="insn-00b0cd80"></a> `00b0cd80` | `03 f7 ff 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd84"></a> `00b0cd84` | `48 69 71 38` | ldrb w8,[x10, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00b0cd88"></a> `00b0cd88` | `a8 f6 ff 35` | cbnz w8,0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cd8c"></a> `00b0cd8c` | `ff 25 00 71` | cmp w15,#0x9 | `FALL_THROUGH`
<a id="insn-00b0cd90"></a> `00b0cd90` | `e3 0a 00 54` | b.cc 0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0cd94"></a> `00b0cd94` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cd98"></a> `00b0cd98` | `68 02 00 b4` | cbz x8,0x00b0cde4 | `CONDITIONAL_JUMP`
<a id="insn-00b0cd9c"></a> `00b0cd9c` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0cda0"></a> `00b0cda0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cda4"></a> `00b0cda4` | `e0 00 00 54` | b.eq 0x00b0cdc0 | `CONDITIONAL_JUMP`
<a id="insn-00b0cda8"></a> `00b0cda8` | `71 a2 40 39` | ldrb w17,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cdac"></a> `00b0cdac` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0cdb0"></a> `00b0cdb0` | `91 f5 ff 35` | cbnz w17,0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0cdb4"></a> `00b0cdb4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0cdb8"></a> `00b0cdb8` | `82 00 00 54` | b.cs 0x00b0cdc8 | `CONDITIONAL_JUMP`
<a id="insn-00b0cdbc"></a> `00b0cdbc` | `a9 ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cdc0"></a> `00b0cdc0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0cdc4"></a> `00b0cdc4` | `c3 f4 ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cdc8"></a> `00b0cdc8` | `48 69 70 b8` | ldr w8,[x10, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0cdcc"></a> `00b0cdcc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cdd0"></a> `00b0cdd0` | `6b f4 ff 54` | b.lt 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cdd4"></a> `00b0cdd4` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00b0cdd8"></a> `00b0cdd8` | `70 05 00 d1` | sub x16,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cddc"></a> `00b0cddc` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00b0cde0"></a> `00b0cde0` | `e3 f3 ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cde4"></a> `00b0cde4` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cde8"></a> `00b0cde8` | `28 04 00 b4` | cbz x8,0x00b0ce6c | `CONDITIONAL_JUMP`
<a id="insn-00b0cdec"></a> `00b0cdec` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0cdf0"></a> `00b0cdf0` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00b0cdf4"></a> `00b0cdf4` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00b0cdf8"></a> `00b0cdf8` | `a0 03 00 54` | b.eq 0x00b0ce6c | `CONDITIONAL_JUMP`
<a id="insn-00b0cdfc"></a> `00b0cdfc` | `30 02 0a cb` | sub x16,x17,x10 | `FALL_THROUGH`
<a id="insn-00b0ce00"></a> `00b0ce00` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0ce04"></a> `00b0ce04` | `e0 00 00 54` | b.eq 0x00b0ce20 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce08"></a> `00b0ce08` | `61 a2 40 39` | ldrb w1,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0ce0c"></a> `00b0ce0c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0ce10"></a> `00b0ce10` | `81 f2 ff 35` | cbnz w1,0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce14"></a> `00b0ce14` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0ce18"></a> `00b0ce18` | `82 00 00 54` | b.cs 0x00b0ce28 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce1c"></a> `00b0ce1c` | `91 ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0ce20"></a> `00b0ce20` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0ce24"></a> `00b0ce24` | `c3 f1 ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ce28"></a> `00b0ce28` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00b0ce2c"></a> `00b0ce2c` | `f1 77 1f 32` | orr w17,wzr,#0x7ffffffe | `FALL_THROUGH`
<a id="insn-00b0ce30"></a> `00b0ce30` | `1f 01 11 6b` | cmp w8,w17 | `FALL_THROUGH`
<a id="insn-00b0ce34"></a> `00b0ce34` | `48 f1 ff 54` | b.hi 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ce38"></a> `00b0ce38` | `01 11 00 91` | add x1,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b0ce3c"></a> `00b0ce3c` | `31 00 10 8b` | add x17,x1,x16 | `FALL_THROUGH`
<a id="insn-00b0ce40"></a> `00b0ce40` | `68 05 00 d1` | sub x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ce44"></a> `00b0ce44` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00b0ce48"></a> `00b0ce48` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0ce4c"></a> `00b0ce4c` | `a3 f0 ff 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce50"></a> `00b0ce50` | `7f 01 01 eb` | cmp x11,x1 | `FALL_THROUGH`
<a id="insn-00b0ce54"></a> `00b0ce54` | `69 f0 ff 54` | b.ls 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce58"></a> `00b0ce58` | `61 01 01 cb` | sub x1,x11,x1 | `FALL_THROUGH`
<a id="insn-00b0ce5c"></a> `00b0ce5c` | `3f 00 10 eb` | cmp x1,x16 | `FALL_THROUGH`
<a id="insn-00b0ce60"></a> `00b0ce60` | `03 f0 ff 54` | b.cc 0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce64"></a> `00b0ce64` | `48 69 71 38` | ldrb w8,[x10, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00b0ce68"></a> `00b0ce68` | `a8 ef ff 35` | cbnz w8,0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ce6c"></a> `00b0ce6c` | `ff 2d 00 71` | cmp w15,#0xb | `FALL_THROUGH`
<a id="insn-00b0ce70"></a> `00b0ce70` | `e3 03 00 54` | b.cc 0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0ce74"></a> `00b0ce74` | `c8 15 40 79` | ldrh w8,[x14, #0xa] | `FALL_THROUGH`
<a id="insn-00b0ce78"></a> `00b0ce78` | `68 02 00 b4` | cbz x8,0x00b0cec4 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce7c"></a> `00b0ce7c` | `8c 01 08 8b` | add x12,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0ce80"></a> `00b0ce80` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0ce84"></a> `00b0ce84` | `e0 00 00 54` | b.eq 0x00b0cea0 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce88"></a> `00b0ce88` | `6f a2 40 39` | ldrb w15,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0ce8c"></a> `00b0ce8c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0ce90"></a> `00b0ce90` | `8f ee ff 35` | cbnz w15,0x00b0cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce94"></a> `00b0ce94` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0ce98"></a> `00b0ce98` | `82 00 00 54` | b.cs 0x00b0cea8 | `CONDITIONAL_JUMP`
<a id="insn-00b0ce9c"></a> `00b0ce9c` | `71 ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cea0"></a> `00b0cea0` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0cea4"></a> `00b0cea4` | `c3 ed ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cea8"></a> `00b0cea8` | `48 69 6c b8` | ldr w8,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0ceac"></a> `00b0ceac` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0ceb0"></a> `00b0ceb0` | `6b ed ff 54` | b.lt 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0ceb4"></a> `00b0ceb4` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0ceb8"></a> `00b0ceb8` | `6a 05 00 d1` | sub x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cebc"></a> `00b0cebc` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b0cec0"></a> `00b0cec0` | `e3 ec ff 54` | b.cc 0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cec4"></a> `00b0cec4` | `c8 15 40 79` | ldrh w8,[x14, #0xa] | `FALL_THROUGH`
<a id="insn-00b0cec8"></a> `00b0cec8` | `28 01 00 b4` | cbz x8,0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0cecc"></a> `00b0cecc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0ced0"></a> `00b0ced0` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b0ced4"></a> `00b0ced4` | `00 01 0a ab` | adds x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b0ced8"></a> `00b0ced8` | `a0 00 00 54` | b.eq 0x00b0ceec | `CONDITIONAL_JUMP`
<a id="insn-00b0cedc"></a> `00b0cedc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b0cee0"></a> `00b0cee0` | `f4 46 03 94` | bl 0x00bdeab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cee4"></a> `00b0cee4` | `c0 eb 07 36` | tbz w0,#0x0,0x00b0cc5c | `CONDITIONAL_JUMP`
<a id="insn-00b0cee8"></a> `00b0cee8` | `69 12 40 b9` | ldr w9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ceec"></a> `00b0ceec` | `28 05 00 51` | sub w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cef0"></a> `00b0cef0` | `68 12 00 b9` | str w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cef4"></a> `00b0cef4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cef8"></a> `00b0cef8` | `5a ff ff 17` | b 0x00b0cc60 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b0cbbc`](#insn-00b0cbbc) 範囲 `[['00b0cbbc', '00b0cbbf']]`
  - `FALL_THROUGH` [`00b0cbbc`](#insn-00b0cbbc) → [`00b0cbc0`](#insn-00b0cbc0)
- ブロック [`00b0cbc0`](#insn-00b0cbc0) 範囲 `[['00b0cbc0', '00b0cbdb']]`
  - `CONDITIONAL_JUMP` [`00b0cbd8`](#insn-00b0cbd8) → [`00b0cbe4`](#insn-00b0cbe4)
  - `FALL_THROUGH` [`00b0cbd8`](#insn-00b0cbd8) → [`00b0cbdc`](#insn-00b0cbdc)
- ブロック [`00b0cbdc`](#insn-00b0cbdc) 範囲 `[['00b0cbdc', '00b0cbe3']]`
  - `CONDITIONAL_JUMP` [`00b0cbe0`](#insn-00b0cbe0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cbe0`](#insn-00b0cbe0) → [`00b0cbe4`](#insn-00b0cbe4)
- ブロック [`00b0cbe4`](#insn-00b0cbe4) 範囲 `[['00b0cbe4', '00b0cbf3']]`
  - `CONDITIONAL_JUMP` [`00b0cbf0`](#insn-00b0cbf0) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cbf0`](#insn-00b0cbf0) → [`00b0cbf4`](#insn-00b0cbf4)
- ブロック [`00b0cbf4`](#insn-00b0cbf4) 範囲 `[['00b0cbf4', '00b0cbf7']]`
  - `FALL_THROUGH` [`00b0cbf4`](#insn-00b0cbf4) → [`00b0cbf8`](#insn-00b0cbf8)
- ブロック [`00b0cbf8`](#insn-00b0cbf8) 範囲 `[['00b0cbf8', '00b0cbff']]`
  - `CONDITIONAL_JUMP` [`00b0cbfc`](#insn-00b0cbfc) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cbfc`](#insn-00b0cbfc) → [`00b0cc00`](#insn-00b0cc00)
- ブロック [`00b0cc00`](#insn-00b0cc00) 範囲 `[['00b0cc00', '00b0cc03']]`
  - `FALL_THROUGH` [`00b0cc00`](#insn-00b0cc00) → [`00b0cc04`](#insn-00b0cc04)
- ブロック [`00b0cc04`](#insn-00b0cc04) 範囲 `[['00b0cc04', '00b0cc23']]`
  - `CONDITIONAL_JUMP` [`00b0cc20`](#insn-00b0cc20) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cc20`](#insn-00b0cc20) → [`00b0cc24`](#insn-00b0cc24)
- ブロック [`00b0cc24`](#insn-00b0cc24) 範囲 `[['00b0cc24', '00b0cc2f']]`
  - `CONDITIONAL_JUMP` [`00b0cc2c`](#insn-00b0cc2c) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cc2c`](#insn-00b0cc2c) → [`00b0cc30`](#insn-00b0cc30)
- ブロック [`00b0cc30`](#insn-00b0cc30) 範囲 `[['00b0cc30', '00b0cc37']]`
  - `CONDITIONAL_JUMP` [`00b0cc34`](#insn-00b0cc34) → [`00b0cc40`](#insn-00b0cc40)
  - `FALL_THROUGH` [`00b0cc34`](#insn-00b0cc34) → [`00b0cc38`](#insn-00b0cc38)
- ブロック [`00b0cc38`](#insn-00b0cc38) 範囲 `[['00b0cc38', '00b0cc3b']]`
  - `FALL_THROUGH` [`00b0cc38`](#insn-00b0cc38) → [`00b0cc3c`](#insn-00b0cc3c)
- ブロック [`00b0cc3c`](#insn-00b0cc3c) 範囲 `[['00b0cc3c', '00b0cc3f']]`
  - `CONDITIONAL_JUMP` [`00b0cc3c`](#insn-00b0cc3c) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cc3c`](#insn-00b0cc3c) → [`00b0cc40`](#insn-00b0cc40)
- ブロック [`00b0cc40`](#insn-00b0cc40) 範囲 `[['00b0cc40', '00b0cc43']]`
  - `FALL_THROUGH` [`00b0cc40`](#insn-00b0cc40) → [`00b0cc44`](#insn-00b0cc44)
- ブロック [`00b0cc44`](#insn-00b0cc44) 範囲 `[['00b0cc44', '00b0cc47']]`
  - `FALL_THROUGH` [`00b0cc44`](#insn-00b0cc44) → [`00b0cc48`](#insn-00b0cc48)
- ブロック [`00b0cc48`](#insn-00b0cc48) 範囲 `[['00b0cc48', '00b0cc4b']]`
  - `CONDITIONAL_JUMP` [`00b0cc48`](#insn-00b0cc48) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cc48`](#insn-00b0cc48) → [`00b0cc4c`](#insn-00b0cc4c)
- ブロック [`00b0cc4c`](#insn-00b0cc4c) 範囲 `[['00b0cc4c', '00b0cc53']]`
  - `CONDITIONAL_JUMP` [`00b0cc50`](#insn-00b0cc50) → [`00b0cc70`](#insn-00b0cc70)
  - `FALL_THROUGH` [`00b0cc50`](#insn-00b0cc50) → [`00b0cc54`](#insn-00b0cc54)
- ブロック [`00b0cc54`](#insn-00b0cc54) 範囲 `[['00b0cc54', '00b0cc5b']]`
  - `CONDITIONAL_JUMP` [`00b0cc58`](#insn-00b0cc58) → [`00b0cc70`](#insn-00b0cc70)
  - `FALL_THROUGH` [`00b0cc58`](#insn-00b0cc58) → [`00b0cc5c`](#insn-00b0cc5c)
- ブロック [`00b0cc5c`](#insn-00b0cc5c) 範囲 `[['00b0cc5c', '00b0cc5f']]`
  - `FALL_THROUGH` [`00b0cc5c`](#insn-00b0cc5c) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0cc60`](#insn-00b0cc60) 範囲 `[['00b0cc60', '00b0cc6f']]`
- ブロック [`00b0cc70`](#insn-00b0cc70) 範囲 `[['00b0cc70', '00b0cc7b']]`
  - `CONDITIONAL_JUMP` [`00b0cc78`](#insn-00b0cc78) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cc78`](#insn-00b0cc78) → [`00b0cc7c`](#insn-00b0cc7c)
- ブロック [`00b0cc7c`](#insn-00b0cc7c) 範囲 `[['00b0cc7c', '00b0cc83']]`
  - `CONDITIONAL_JUMP` [`00b0cc80`](#insn-00b0cc80) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cc80`](#insn-00b0cc80) → [`00b0cc84`](#insn-00b0cc84)
- ブロック [`00b0cc84`](#insn-00b0cc84) 範囲 `[['00b0cc84', '00b0cc97']]`
  - `CONDITIONAL_JUMP` [`00b0cc94`](#insn-00b0cc94) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0cc94`](#insn-00b0cc94) → [`00b0cc98`](#insn-00b0cc98)
- ブロック [`00b0cc98`](#insn-00b0cc98) 範囲 `[['00b0cc98', '00b0cc9f']]`
  - `CONDITIONAL_JUMP` [`00b0cc9c`](#insn-00b0cc9c) → [`00b0ccac`](#insn-00b0ccac)
  - `FALL_THROUGH` [`00b0cc9c`](#insn-00b0cc9c) → [`00b0cca0`](#insn-00b0cca0)
- ブロック [`00b0cca0`](#insn-00b0cca0) 範囲 `[['00b0cca0', '00b0ccab']]`
  - `CONDITIONAL_JUMP` [`00b0cca8`](#insn-00b0cca8) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cca8`](#insn-00b0cca8) → [`00b0ccac`](#insn-00b0ccac)
- ブロック [`00b0ccac`](#insn-00b0ccac) 範囲 `[['00b0ccac', '00b0ccb3']]`
  - `CONDITIONAL_JUMP` [`00b0ccb0`](#insn-00b0ccb0) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0ccb0`](#insn-00b0ccb0) → [`00b0ccb4`](#insn-00b0ccb4)
- ブロック [`00b0ccb4`](#insn-00b0ccb4) 範囲 `[['00b0ccb4', '00b0ccbb']]`
  - `CONDITIONAL_JUMP` [`00b0ccb8`](#insn-00b0ccb8) → [`00b0cd04`](#insn-00b0cd04)
  - `FALL_THROUGH` [`00b0ccb8`](#insn-00b0ccb8) → [`00b0ccbc`](#insn-00b0ccbc)
- ブロック [`00b0ccbc`](#insn-00b0ccbc) 範囲 `[['00b0ccbc', '00b0ccc7']]`
  - `CONDITIONAL_JUMP` [`00b0ccc4`](#insn-00b0ccc4) → [`00b0cce0`](#insn-00b0cce0)
  - `FALL_THROUGH` [`00b0ccc4`](#insn-00b0ccc4) → [`00b0ccc8`](#insn-00b0ccc8)
- ブロック [`00b0ccc8`](#insn-00b0ccc8) 範囲 `[['00b0ccc8', '00b0ccd3']]`
  - `CONDITIONAL_JUMP` [`00b0ccd0`](#insn-00b0ccd0) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ccd0`](#insn-00b0ccd0) → [`00b0ccd4`](#insn-00b0ccd4)
- ブロック [`00b0ccd4`](#insn-00b0ccd4) 範囲 `[['00b0ccd4', '00b0ccdb']]`
  - `CONDITIONAL_JUMP` [`00b0ccd8`](#insn-00b0ccd8) → [`00b0cce8`](#insn-00b0cce8)
  - `FALL_THROUGH` [`00b0ccd8`](#insn-00b0ccd8) → [`00b0ccdc`](#insn-00b0ccdc)
- ブロック [`00b0ccdc`](#insn-00b0ccdc) 範囲 `[['00b0ccdc', '00b0ccdf']]`
  - `UNCONDITIONAL_JUMP` [`00b0ccdc`](#insn-00b0ccdc) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0cce0`](#insn-00b0cce0) 範囲 `[['00b0cce0', '00b0cce7']]`
  - `CONDITIONAL_JUMP` [`00b0cce4`](#insn-00b0cce4) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cce4`](#insn-00b0cce4) → [`00b0cce8`](#insn-00b0cce8)
- ブロック [`00b0cce8`](#insn-00b0cce8) 範囲 `[['00b0cce8', '00b0ccf3']]`
  - `CONDITIONAL_JUMP` [`00b0ccf0`](#insn-00b0ccf0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0ccf0`](#insn-00b0ccf0) → [`00b0ccf4`](#insn-00b0ccf4)
- ブロック [`00b0ccf4`](#insn-00b0ccf4) 範囲 `[['00b0ccf4', '00b0cd03']]`
  - `CONDITIONAL_JUMP` [`00b0cd00`](#insn-00b0cd00) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cd00`](#insn-00b0cd00) → [`00b0cd04`](#insn-00b0cd04)
- ブロック [`00b0cd04`](#insn-00b0cd04) 範囲 `[['00b0cd04', '00b0cd0b']]`
  - `CONDITIONAL_JUMP` [`00b0cd08`](#insn-00b0cd08) → [`00b0cd8c`](#insn-00b0cd8c)
  - `FALL_THROUGH` [`00b0cd08`](#insn-00b0cd08) → [`00b0cd0c`](#insn-00b0cd0c)
- ブロック [`00b0cd0c`](#insn-00b0cd0c) 範囲 `[['00b0cd0c', '00b0cd1b']]`
  - `CONDITIONAL_JUMP` [`00b0cd18`](#insn-00b0cd18) → [`00b0cd8c`](#insn-00b0cd8c)
  - `FALL_THROUGH` [`00b0cd18`](#insn-00b0cd18) → [`00b0cd1c`](#insn-00b0cd1c)
- ブロック [`00b0cd1c`](#insn-00b0cd1c) 範囲 `[['00b0cd1c', '00b0cd27']]`
  - `CONDITIONAL_JUMP` [`00b0cd24`](#insn-00b0cd24) → [`00b0cd40`](#insn-00b0cd40)
  - `FALL_THROUGH` [`00b0cd24`](#insn-00b0cd24) → [`00b0cd28`](#insn-00b0cd28)
- ブロック [`00b0cd28`](#insn-00b0cd28) 範囲 `[['00b0cd28', '00b0cd33']]`
  - `CONDITIONAL_JUMP` [`00b0cd30`](#insn-00b0cd30) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cd30`](#insn-00b0cd30) → [`00b0cd34`](#insn-00b0cd34)
- ブロック [`00b0cd34`](#insn-00b0cd34) 範囲 `[['00b0cd34', '00b0cd3b']]`
  - `CONDITIONAL_JUMP` [`00b0cd38`](#insn-00b0cd38) → [`00b0cd48`](#insn-00b0cd48)
  - `FALL_THROUGH` [`00b0cd38`](#insn-00b0cd38) → [`00b0cd3c`](#insn-00b0cd3c)
- ブロック [`00b0cd3c`](#insn-00b0cd3c) 範囲 `[['00b0cd3c', '00b0cd3f']]`
  - `UNCONDITIONAL_JUMP` [`00b0cd3c`](#insn-00b0cd3c) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0cd40`](#insn-00b0cd40) 範囲 `[['00b0cd40', '00b0cd47']]`
  - `CONDITIONAL_JUMP` [`00b0cd44`](#insn-00b0cd44) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cd44`](#insn-00b0cd44) → [`00b0cd48`](#insn-00b0cd48)
- ブロック [`00b0cd48`](#insn-00b0cd48) 範囲 `[['00b0cd48', '00b0cd57']]`
  - `CONDITIONAL_JUMP` [`00b0cd54`](#insn-00b0cd54) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cd54`](#insn-00b0cd54) → [`00b0cd58`](#insn-00b0cd58)
- ブロック [`00b0cd58`](#insn-00b0cd58) 範囲 `[['00b0cd58', '00b0cd6f']]`
  - `CONDITIONAL_JUMP` [`00b0cd6c`](#insn-00b0cd6c) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cd6c`](#insn-00b0cd6c) → [`00b0cd70`](#insn-00b0cd70)
- ブロック [`00b0cd70`](#insn-00b0cd70) 範囲 `[['00b0cd70', '00b0cd77']]`
  - `CONDITIONAL_JUMP` [`00b0cd74`](#insn-00b0cd74) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cd74`](#insn-00b0cd74) → [`00b0cd78`](#insn-00b0cd78)
- ブロック [`00b0cd78`](#insn-00b0cd78) 範囲 `[['00b0cd78', '00b0cd83']]`
  - `CONDITIONAL_JUMP` [`00b0cd80`](#insn-00b0cd80) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cd80`](#insn-00b0cd80) → [`00b0cd84`](#insn-00b0cd84)
- ブロック [`00b0cd84`](#insn-00b0cd84) 範囲 `[['00b0cd84', '00b0cd8b']]`
  - `CONDITIONAL_JUMP` [`00b0cd88`](#insn-00b0cd88) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cd88`](#insn-00b0cd88) → [`00b0cd8c`](#insn-00b0cd8c)
- ブロック [`00b0cd8c`](#insn-00b0cd8c) 範囲 `[['00b0cd8c', '00b0cd93']]`
  - `CONDITIONAL_JUMP` [`00b0cd90`](#insn-00b0cd90) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0cd90`](#insn-00b0cd90) → [`00b0cd94`](#insn-00b0cd94)
- ブロック [`00b0cd94`](#insn-00b0cd94) 範囲 `[['00b0cd94', '00b0cd9b']]`
  - `CONDITIONAL_JUMP` [`00b0cd98`](#insn-00b0cd98) → [`00b0cde4`](#insn-00b0cde4)
  - `FALL_THROUGH` [`00b0cd98`](#insn-00b0cd98) → [`00b0cd9c`](#insn-00b0cd9c)
- ブロック [`00b0cd9c`](#insn-00b0cd9c) 範囲 `[['00b0cd9c', '00b0cda7']]`
  - `CONDITIONAL_JUMP` [`00b0cda4`](#insn-00b0cda4) → [`00b0cdc0`](#insn-00b0cdc0)
  - `FALL_THROUGH` [`00b0cda4`](#insn-00b0cda4) → [`00b0cda8`](#insn-00b0cda8)
- ブロック [`00b0cda8`](#insn-00b0cda8) 範囲 `[['00b0cda8', '00b0cdb3']]`
  - `CONDITIONAL_JUMP` [`00b0cdb0`](#insn-00b0cdb0) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0cdb0`](#insn-00b0cdb0) → [`00b0cdb4`](#insn-00b0cdb4)
- ブロック [`00b0cdb4`](#insn-00b0cdb4) 範囲 `[['00b0cdb4', '00b0cdbb']]`
  - `CONDITIONAL_JUMP` [`00b0cdb8`](#insn-00b0cdb8) → [`00b0cdc8`](#insn-00b0cdc8)
  - `FALL_THROUGH` [`00b0cdb8`](#insn-00b0cdb8) → [`00b0cdbc`](#insn-00b0cdbc)
- ブロック [`00b0cdbc`](#insn-00b0cdbc) 範囲 `[['00b0cdbc', '00b0cdbf']]`
  - `UNCONDITIONAL_JUMP` [`00b0cdbc`](#insn-00b0cdbc) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0cdc0`](#insn-00b0cdc0) 範囲 `[['00b0cdc0', '00b0cdc7']]`
  - `CONDITIONAL_JUMP` [`00b0cdc4`](#insn-00b0cdc4) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cdc4`](#insn-00b0cdc4) → [`00b0cdc8`](#insn-00b0cdc8)
- ブロック [`00b0cdc8`](#insn-00b0cdc8) 範囲 `[['00b0cdc8', '00b0cdd3']]`
  - `CONDITIONAL_JUMP` [`00b0cdd0`](#insn-00b0cdd0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cdd0`](#insn-00b0cdd0) → [`00b0cdd4`](#insn-00b0cdd4)
- ブロック [`00b0cdd4`](#insn-00b0cdd4) 範囲 `[['00b0cdd4', '00b0cde3']]`
  - `CONDITIONAL_JUMP` [`00b0cde0`](#insn-00b0cde0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cde0`](#insn-00b0cde0) → [`00b0cde4`](#insn-00b0cde4)
- ブロック [`00b0cde4`](#insn-00b0cde4) 範囲 `[['00b0cde4', '00b0cdeb']]`
  - `CONDITIONAL_JUMP` [`00b0cde8`](#insn-00b0cde8) → [`00b0ce6c`](#insn-00b0ce6c)
  - `FALL_THROUGH` [`00b0cde8`](#insn-00b0cde8) → [`00b0cdec`](#insn-00b0cdec)
- ブロック [`00b0cdec`](#insn-00b0cdec) 範囲 `[['00b0cdec', '00b0cdf3']]`
  - `FALL_THROUGH` [`00b0cdf0`](#insn-00b0cdf0) → [`00b0cdf4`](#insn-00b0cdf4)
- ブロック [`00b0cdf4`](#insn-00b0cdf4) 範囲 `[['00b0cdf4', '00b0cdfb']]`
  - `CONDITIONAL_JUMP` [`00b0cdf8`](#insn-00b0cdf8) → [`00b0ce6c`](#insn-00b0ce6c)
  - `FALL_THROUGH` [`00b0cdf8`](#insn-00b0cdf8) → [`00b0cdfc`](#insn-00b0cdfc)
- ブロック [`00b0cdfc`](#insn-00b0cdfc) 範囲 `[['00b0cdfc', '00b0ce07']]`
  - `CONDITIONAL_JUMP` [`00b0ce04`](#insn-00b0ce04) → [`00b0ce20`](#insn-00b0ce20)
  - `FALL_THROUGH` [`00b0ce04`](#insn-00b0ce04) → [`00b0ce08`](#insn-00b0ce08)
- ブロック [`00b0ce08`](#insn-00b0ce08) 範囲 `[['00b0ce08', '00b0ce13']]`
  - `CONDITIONAL_JUMP` [`00b0ce10`](#insn-00b0ce10) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ce10`](#insn-00b0ce10) → [`00b0ce14`](#insn-00b0ce14)
- ブロック [`00b0ce14`](#insn-00b0ce14) 範囲 `[['00b0ce14', '00b0ce1b']]`
  - `CONDITIONAL_JUMP` [`00b0ce18`](#insn-00b0ce18) → [`00b0ce28`](#insn-00b0ce28)
  - `FALL_THROUGH` [`00b0ce18`](#insn-00b0ce18) → [`00b0ce1c`](#insn-00b0ce1c)
- ブロック [`00b0ce1c`](#insn-00b0ce1c) 範囲 `[['00b0ce1c', '00b0ce1f']]`
  - `UNCONDITIONAL_JUMP` [`00b0ce1c`](#insn-00b0ce1c) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0ce20`](#insn-00b0ce20) 範囲 `[['00b0ce20', '00b0ce27']]`
  - `CONDITIONAL_JUMP` [`00b0ce24`](#insn-00b0ce24) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0ce24`](#insn-00b0ce24) → [`00b0ce28`](#insn-00b0ce28)
- ブロック [`00b0ce28`](#insn-00b0ce28) 範囲 `[['00b0ce28', '00b0ce37']]`
  - `CONDITIONAL_JUMP` [`00b0ce34`](#insn-00b0ce34) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0ce34`](#insn-00b0ce34) → [`00b0ce38`](#insn-00b0ce38)
- ブロック [`00b0ce38`](#insn-00b0ce38) 範囲 `[['00b0ce38', '00b0ce4f']]`
  - `CONDITIONAL_JUMP` [`00b0ce4c`](#insn-00b0ce4c) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ce4c`](#insn-00b0ce4c) → [`00b0ce50`](#insn-00b0ce50)
- ブロック [`00b0ce50`](#insn-00b0ce50) 範囲 `[['00b0ce50', '00b0ce57']]`
  - `CONDITIONAL_JUMP` [`00b0ce54`](#insn-00b0ce54) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ce54`](#insn-00b0ce54) → [`00b0ce58`](#insn-00b0ce58)
- ブロック [`00b0ce58`](#insn-00b0ce58) 範囲 `[['00b0ce58', '00b0ce5f']]`
  - `FALL_THROUGH` [`00b0ce5c`](#insn-00b0ce5c) → [`00b0ce60`](#insn-00b0ce60)
- ブロック [`00b0ce60`](#insn-00b0ce60) 範囲 `[['00b0ce60', '00b0ce63']]`
  - `CONDITIONAL_JUMP` [`00b0ce60`](#insn-00b0ce60) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ce60`](#insn-00b0ce60) → [`00b0ce64`](#insn-00b0ce64)
- ブロック [`00b0ce64`](#insn-00b0ce64) 範囲 `[['00b0ce64', '00b0ce67']]`
  - `FALL_THROUGH` [`00b0ce64`](#insn-00b0ce64) → [`00b0ce68`](#insn-00b0ce68)
- ブロック [`00b0ce68`](#insn-00b0ce68) 範囲 `[['00b0ce68', '00b0ce6b']]`
  - `CONDITIONAL_JUMP` [`00b0ce68`](#insn-00b0ce68) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0ce68`](#insn-00b0ce68) → [`00b0ce6c`](#insn-00b0ce6c)
- ブロック [`00b0ce6c`](#insn-00b0ce6c) 範囲 `[['00b0ce6c', '00b0ce73']]`
  - `CONDITIONAL_JUMP` [`00b0ce70`](#insn-00b0ce70) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0ce70`](#insn-00b0ce70) → [`00b0ce74`](#insn-00b0ce74)
- ブロック [`00b0ce74`](#insn-00b0ce74) 範囲 `[['00b0ce74', '00b0ce7b']]`
  - `CONDITIONAL_JUMP` [`00b0ce78`](#insn-00b0ce78) → [`00b0cec4`](#insn-00b0cec4)
  - `FALL_THROUGH` [`00b0ce78`](#insn-00b0ce78) → [`00b0ce7c`](#insn-00b0ce7c)
- ブロック [`00b0ce7c`](#insn-00b0ce7c) 範囲 `[['00b0ce7c', '00b0ce87']]`
  - `CONDITIONAL_JUMP` [`00b0ce84`](#insn-00b0ce84) → [`00b0cea0`](#insn-00b0cea0)
  - `FALL_THROUGH` [`00b0ce84`](#insn-00b0ce84) → [`00b0ce88`](#insn-00b0ce88)
- ブロック [`00b0ce88`](#insn-00b0ce88) 範囲 `[['00b0ce88', '00b0ce93']]`
  - `CONDITIONAL_JUMP` [`00b0ce90`](#insn-00b0ce90) → [`00b0cc60`](#insn-00b0cc60)
  - `FALL_THROUGH` [`00b0ce90`](#insn-00b0ce90) → [`00b0ce94`](#insn-00b0ce94)
- ブロック [`00b0ce94`](#insn-00b0ce94) 範囲 `[['00b0ce94', '00b0ce97']]`
  - `FALL_THROUGH` [`00b0ce94`](#insn-00b0ce94) → [`00b0ce98`](#insn-00b0ce98)
- ブロック [`00b0ce98`](#insn-00b0ce98) 範囲 `[['00b0ce98', '00b0ce9b']]`
  - `CONDITIONAL_JUMP` [`00b0ce98`](#insn-00b0ce98) → [`00b0cea8`](#insn-00b0cea8)
  - `FALL_THROUGH` [`00b0ce98`](#insn-00b0ce98) → [`00b0ce9c`](#insn-00b0ce9c)
- ブロック [`00b0ce9c`](#insn-00b0ce9c) 範囲 `[['00b0ce9c', '00b0ce9f']]`
  - `UNCONDITIONAL_JUMP` [`00b0ce9c`](#insn-00b0ce9c) → [`00b0cc60`](#insn-00b0cc60)
- ブロック [`00b0cea0`](#insn-00b0cea0) 範囲 `[['00b0cea0', '00b0cea7']]`
  - `CONDITIONAL_JUMP` [`00b0cea4`](#insn-00b0cea4) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cea4`](#insn-00b0cea4) → [`00b0cea8`](#insn-00b0cea8)
- ブロック [`00b0cea8`](#insn-00b0cea8) 範囲 `[['00b0cea8', '00b0ceb3']]`
  - `CONDITIONAL_JUMP` [`00b0ceb0`](#insn-00b0ceb0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0ceb0`](#insn-00b0ceb0) → [`00b0ceb4`](#insn-00b0ceb4)
- ブロック [`00b0ceb4`](#insn-00b0ceb4) 範囲 `[['00b0ceb4', '00b0cec3']]`
  - `CONDITIONAL_JUMP` [`00b0cec0`](#insn-00b0cec0) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cec0`](#insn-00b0cec0) → [`00b0cec4`](#insn-00b0cec4)
- ブロック [`00b0cec4`](#insn-00b0cec4) 範囲 `[['00b0cec4', '00b0cecb']]`
  - `CONDITIONAL_JUMP` [`00b0cec8`](#insn-00b0cec8) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0cec8`](#insn-00b0cec8) → [`00b0cecc`](#insn-00b0cecc)
- ブロック [`00b0cecc`](#insn-00b0cecc) 範囲 `[['00b0cecc', '00b0ced7']]`
  - `FALL_THROUGH` [`00b0ced4`](#insn-00b0ced4) → [`00b0ced8`](#insn-00b0ced8)
- ブロック [`00b0ced8`](#insn-00b0ced8) 範囲 `[['00b0ced8', '00b0cedb']]`
  - `CONDITIONAL_JUMP` [`00b0ced8`](#insn-00b0ced8) → [`00b0ceec`](#insn-00b0ceec)
  - `FALL_THROUGH` [`00b0ced8`](#insn-00b0ced8) → [`00b0cedc`](#insn-00b0cedc)
- ブロック [`00b0cedc`](#insn-00b0cedc) 範囲 `[['00b0cedc', '00b0cee7']]`
  - `CONDITIONAL_JUMP` [`00b0cee4`](#insn-00b0cee4) → [`00b0cc5c`](#insn-00b0cc5c)
  - `FALL_THROUGH` [`00b0cee4`](#insn-00b0cee4) → [`00b0cee8`](#insn-00b0cee8)
- ブロック [`00b0cee8`](#insn-00b0cee8) 範囲 `[['00b0cee8', '00b0ceeb']]`
  - `FALL_THROUGH` [`00b0cee8`](#insn-00b0cee8) → [`00b0ceec`](#insn-00b0ceec)
- ブロック [`00b0ceec`](#insn-00b0ceec) 範囲 `[['00b0ceec', '00b0cefb']]`
  - `UNCONDITIONAL_JUMP` [`00b0cef8`](#insn-00b0cef8) → [`00b0cc60`](#insn-00b0cc60)

## 命令位置別の参照

- [`00b0cbbc`](#insn-00b0cbbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbc0`](#insn-00b0cbc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbd8`](#insn-00b0cbd8) → [`00b0cbe4`](#insn-00b0cbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbe0`](#insn-00b0cbe0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbf0`](#insn-00b0cbf0) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbfc`](#insn-00b0cbfc) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc20`](#insn-00b0cc20) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc2c`](#insn-00b0cc2c) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc34`](#insn-00b0cc34) → [`00b0cc40`](#insn-00b0cc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc3c`](#insn-00b0cc3c) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc48`](#insn-00b0cc48) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc50`](#insn-00b0cc50) → [`00b0cc70`](#insn-00b0cc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc58`](#insn-00b0cc58) → [`00b0cc70`](#insn-00b0cc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc60`](#insn-00b0cc60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc78`](#insn-00b0cc78) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc80`](#insn-00b0cc80) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc94`](#insn-00b0cc94) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc9c`](#insn-00b0cc9c) → [`00b0ccac`](#insn-00b0ccac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cca8`](#insn-00b0cca8) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccb0`](#insn-00b0ccb0) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccb8`](#insn-00b0ccb8) → [`00b0cd04`](#insn-00b0cd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccc4`](#insn-00b0ccc4) → [`00b0cce0`](#insn-00b0cce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccd0`](#insn-00b0ccd0) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccd8`](#insn-00b0ccd8) → [`00b0cce8`](#insn-00b0cce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccdc`](#insn-00b0ccdc) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cce4`](#insn-00b0cce4) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ccf0`](#insn-00b0ccf0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd00`](#insn-00b0cd00) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd08`](#insn-00b0cd08) → [`00b0cd8c`](#insn-00b0cd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd18`](#insn-00b0cd18) → [`00b0cd8c`](#insn-00b0cd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd24`](#insn-00b0cd24) → [`00b0cd40`](#insn-00b0cd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd30`](#insn-00b0cd30) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd38`](#insn-00b0cd38) → [`00b0cd48`](#insn-00b0cd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd3c`](#insn-00b0cd3c) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd44`](#insn-00b0cd44) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd54`](#insn-00b0cd54) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd6c`](#insn-00b0cd6c) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd74`](#insn-00b0cd74) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd80`](#insn-00b0cd80) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd88`](#insn-00b0cd88) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd90`](#insn-00b0cd90) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cd98`](#insn-00b0cd98) → [`00b0cde4`](#insn-00b0cde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cda4`](#insn-00b0cda4) → [`00b0cdc0`](#insn-00b0cdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdb0`](#insn-00b0cdb0) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdb8`](#insn-00b0cdb8) → [`00b0cdc8`](#insn-00b0cdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdbc`](#insn-00b0cdbc) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdc4`](#insn-00b0cdc4) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdd0`](#insn-00b0cdd0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cde0`](#insn-00b0cde0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cde8`](#insn-00b0cde8) → [`00b0ce6c`](#insn-00b0ce6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cdf8`](#insn-00b0cdf8) → [`00b0ce6c`](#insn-00b0ce6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce04`](#insn-00b0ce04) → [`00b0ce20`](#insn-00b0ce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce10`](#insn-00b0ce10) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce18`](#insn-00b0ce18) → [`00b0ce28`](#insn-00b0ce28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce1c`](#insn-00b0ce1c) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce24`](#insn-00b0ce24) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce34`](#insn-00b0ce34) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce4c`](#insn-00b0ce4c) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce54`](#insn-00b0ce54) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce60`](#insn-00b0ce60) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce68`](#insn-00b0ce68) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce70`](#insn-00b0ce70) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce78`](#insn-00b0ce78) → [`00b0cec4`](#insn-00b0cec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce84`](#insn-00b0ce84) → [`00b0cea0`](#insn-00b0cea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce90`](#insn-00b0ce90) → [`00b0cc60`](#insn-00b0cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce98`](#insn-00b0ce98) → [`00b0cea8`](#insn-00b0cea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ce9c`](#insn-00b0ce9c) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cea4`](#insn-00b0cea4) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ceb0`](#insn-00b0ceb0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cec0`](#insn-00b0cec0) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cec8`](#insn-00b0cec8) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ced8`](#insn-00b0ced8) → [`00b0ceec`](#insn-00b0ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cee0`](#insn-00b0cee0) → [`00bdeab0`](../00bde/00bdeab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0cee4`](#insn-00b0cee4) → [`00b0cc5c`](#insn-00b0cc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cef8`](#insn-00b0cef8) → [`00b0cc60`](#insn-00b0cc60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0cbbc`](#insn-00b0cbbc)

~~~json
{
  "source": "00b0cbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbc0`](#insn-00b0cbc0)

~~~json
{
  "source": "00b0cbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbd8`](#insn-00b0cbd8)

~~~json
{
  "source": "00b0cbd8",
  "target": "00b0cbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbe0`](#insn-00b0cbe0)

~~~json
{
  "source": "00b0cbe0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbf0`](#insn-00b0cbf0)

~~~json
{
  "source": "00b0cbf0",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbfc`](#insn-00b0cbfc)

~~~json
{
  "source": "00b0cbfc",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc20`](#insn-00b0cc20)

~~~json
{
  "source": "00b0cc20",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc2c`](#insn-00b0cc2c)

~~~json
{
  "source": "00b0cc2c",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc34`](#insn-00b0cc34)

~~~json
{
  "source": "00b0cc34",
  "target": "00b0cc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc3c`](#insn-00b0cc3c)

~~~json
{
  "source": "00b0cc3c",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc48`](#insn-00b0cc48)

~~~json
{
  "source": "00b0cc48",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc50`](#insn-00b0cc50)

~~~json
{
  "source": "00b0cc50",
  "target": "00b0cc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc58`](#insn-00b0cc58)

~~~json
{
  "source": "00b0cc58",
  "target": "00b0cc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc60`](#insn-00b0cc60)

~~~json
{
  "source": "00b0cc60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc78`](#insn-00b0cc78)

~~~json
{
  "source": "00b0cc78",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc80`](#insn-00b0cc80)

~~~json
{
  "source": "00b0cc80",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc94`](#insn-00b0cc94)

~~~json
{
  "source": "00b0cc94",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc9c`](#insn-00b0cc9c)

~~~json
{
  "source": "00b0cc9c",
  "target": "00b0ccac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cca8`](#insn-00b0cca8)

~~~json
{
  "source": "00b0cca8",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccb0`](#insn-00b0ccb0)

~~~json
{
  "source": "00b0ccb0",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccb8`](#insn-00b0ccb8)

~~~json
{
  "source": "00b0ccb8",
  "target": "00b0cd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccc4`](#insn-00b0ccc4)

~~~json
{
  "source": "00b0ccc4",
  "target": "00b0cce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccd0`](#insn-00b0ccd0)

~~~json
{
  "source": "00b0ccd0",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccd8`](#insn-00b0ccd8)

~~~json
{
  "source": "00b0ccd8",
  "target": "00b0cce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccdc`](#insn-00b0ccdc)

~~~json
{
  "source": "00b0ccdc",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cce4`](#insn-00b0cce4)

~~~json
{
  "source": "00b0cce4",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ccf0`](#insn-00b0ccf0)

~~~json
{
  "source": "00b0ccf0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd00`](#insn-00b0cd00)

~~~json
{
  "source": "00b0cd00",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd08`](#insn-00b0cd08)

~~~json
{
  "source": "00b0cd08",
  "target": "00b0cd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd18`](#insn-00b0cd18)

~~~json
{
  "source": "00b0cd18",
  "target": "00b0cd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd24`](#insn-00b0cd24)

~~~json
{
  "source": "00b0cd24",
  "target": "00b0cd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd30`](#insn-00b0cd30)

~~~json
{
  "source": "00b0cd30",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd38`](#insn-00b0cd38)

~~~json
{
  "source": "00b0cd38",
  "target": "00b0cd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd3c`](#insn-00b0cd3c)

~~~json
{
  "source": "00b0cd3c",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd44`](#insn-00b0cd44)

~~~json
{
  "source": "00b0cd44",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd54`](#insn-00b0cd54)

~~~json
{
  "source": "00b0cd54",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd6c`](#insn-00b0cd6c)

~~~json
{
  "source": "00b0cd6c",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd74`](#insn-00b0cd74)

~~~json
{
  "source": "00b0cd74",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd80`](#insn-00b0cd80)

~~~json
{
  "source": "00b0cd80",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd88`](#insn-00b0cd88)

~~~json
{
  "source": "00b0cd88",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd90`](#insn-00b0cd90)

~~~json
{
  "source": "00b0cd90",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cd98`](#insn-00b0cd98)

~~~json
{
  "source": "00b0cd98",
  "target": "00b0cde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cda4`](#insn-00b0cda4)

~~~json
{
  "source": "00b0cda4",
  "target": "00b0cdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdb0`](#insn-00b0cdb0)

~~~json
{
  "source": "00b0cdb0",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdb8`](#insn-00b0cdb8)

~~~json
{
  "source": "00b0cdb8",
  "target": "00b0cdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdbc`](#insn-00b0cdbc)

~~~json
{
  "source": "00b0cdbc",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdc4`](#insn-00b0cdc4)

~~~json
{
  "source": "00b0cdc4",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdd0`](#insn-00b0cdd0)

~~~json
{
  "source": "00b0cdd0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cde0`](#insn-00b0cde0)

~~~json
{
  "source": "00b0cde0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cde8`](#insn-00b0cde8)

~~~json
{
  "source": "00b0cde8",
  "target": "00b0ce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cdf8`](#insn-00b0cdf8)

~~~json
{
  "source": "00b0cdf8",
  "target": "00b0ce6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce04`](#insn-00b0ce04)

~~~json
{
  "source": "00b0ce04",
  "target": "00b0ce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce10`](#insn-00b0ce10)

~~~json
{
  "source": "00b0ce10",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce18`](#insn-00b0ce18)

~~~json
{
  "source": "00b0ce18",
  "target": "00b0ce28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce1c`](#insn-00b0ce1c)

~~~json
{
  "source": "00b0ce1c",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce24`](#insn-00b0ce24)

~~~json
{
  "source": "00b0ce24",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce34`](#insn-00b0ce34)

~~~json
{
  "source": "00b0ce34",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce4c`](#insn-00b0ce4c)

~~~json
{
  "source": "00b0ce4c",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce54`](#insn-00b0ce54)

~~~json
{
  "source": "00b0ce54",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce60`](#insn-00b0ce60)

~~~json
{
  "source": "00b0ce60",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce68`](#insn-00b0ce68)

~~~json
{
  "source": "00b0ce68",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce70`](#insn-00b0ce70)

~~~json
{
  "source": "00b0ce70",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce78`](#insn-00b0ce78)

~~~json
{
  "source": "00b0ce78",
  "target": "00b0cec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce84`](#insn-00b0ce84)

~~~json
{
  "source": "00b0ce84",
  "target": "00b0cea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce90`](#insn-00b0ce90)

~~~json
{
  "source": "00b0ce90",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce98`](#insn-00b0ce98)

~~~json
{
  "source": "00b0ce98",
  "target": "00b0cea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ce9c`](#insn-00b0ce9c)

~~~json
{
  "source": "00b0ce9c",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cea4`](#insn-00b0cea4)

~~~json
{
  "source": "00b0cea4",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ceb0`](#insn-00b0ceb0)

~~~json
{
  "source": "00b0ceb0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cec0`](#insn-00b0cec0)

~~~json
{
  "source": "00b0cec0",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cec8`](#insn-00b0cec8)

~~~json
{
  "source": "00b0cec8",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ced8`](#insn-00b0ced8)

~~~json
{
  "source": "00b0ced8",
  "target": "00b0ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cee0`](#insn-00b0cee0)

~~~json
{
  "source": "00b0cee0",
  "target": "00bdeab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cee4`](#insn-00b0cee4)

~~~json
{
  "source": "00b0cee4",
  "target": "00b0cc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cef8`](#insn-00b0cef8)

~~~json
{
  "source": "00b0cef8",
  "target": "00b0cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
