# 00b6cbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0172.md#review-cb2c01e6433fc93a97c9ddf7209fc7f2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6cfd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-279dd4a28e059a6717290a274e521476)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6cbac",
  "name": "_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d62325fe6ec5b110f99140ba539caf10eb9b51628ad42032e0a7d128b2af99c1",
  "source_text_sha256": "d62325fe6ec5b110f99140ba539caf10eb9b51628ad42032e0a7d128b2af99c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6cbac",
        "00b6cd53"
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

- [00c5b5b0](../00c5b/00c5b5b0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4029 bytes

~~~c

undefined4
_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
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
                    /* catch() { ... } // from try @ 00b6caa8 with catch @ 00b6cc14 */
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
                    /* try { // try from 00b6cce4 to 00c6cdb3 has its CatchHandler @ 00b6cce4
                       catch() { ... } // from try @ 00b6cce4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cdd4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cee4 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6cf64 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d038 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d16c with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d370 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d490 with catch @ 00b6cce4
                       catch() { ... } // from try @ 00b6d600 with catch @ 00b6cce4 */
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
<a id="insn-00b6cbac"></a> `00b6cbac` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00b6cbb0"></a> `00b6cbb0` | `0d 00 09 cb` | sub x13,x0,x9 | `FALL_THROUGH`
<a id="insn-00b6cbb4"></a> `00b6cbb4` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00b6cbb8"></a> `00b6cbb8` | `60 00 00 54` | b.eq 0x00b6cbc4 | `CONDITIONAL_JUMP`
<a id="insn-00b6cbbc"></a> `00b6cbbc` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b6cbc0"></a> `00b6cbc0` | `e8 0b 00 35` | cbnz w8,0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cbc4"></a> `00b6cbc4` | `2a 04 40 f9` | ldr x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b6cbc8"></a> `00b6cbc8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6cbcc"></a> `00b6cbcc` | `5f 15 00 f1` | cmp x10,#0x5 | `FALL_THROUGH`
<a id="insn-00b6cbd0"></a> `00b6cbd0` | `e3 0b 00 54` | b.cc 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cbd4"></a> `00b6cbd4` | `4c 11 00 d1` | sub x12,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00b6cbd8"></a> `00b6cbd8` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00b6cbdc"></a> `00b6cbdc` | `83 0b 00 54` | b.cc 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cbe0"></a> `00b6cbe0` | `2b 38 47 29` | ldp w11,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00b6cbe4"></a> `00b6cbe4` | `2f 10 40 b9` | ldr w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b6cbe8"></a> `00b6cbe8` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6cbec"></a> `00b6cbec` | `70 05 00 11` | add w16,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00b6cbf0"></a> `00b6cbf0` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b6cbf4"></a> `00b6cbf4` | `1f 02 0f 6b` | cmp w16,w15 | `FALL_THROUGH`
<a id="insn-00b6cbf8"></a> `00b6cbf8` | `30 38 07 29` | stp w16,w14,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00b6cbfc"></a> `00b6cbfc` | `08 0a 00 54` | b.hi 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc00"></a> `00b6cc00` | `2f 14 40 b9` | ldr w15,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-00b6cc04"></a> `00b6cc04` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b6cc08"></a> `00b6cc08` | `a8 09 00 54` | b.hi 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc0c"></a> `00b6cc0c` | `ae 01 08 cb` | sub x14,x13,x8 | `FALL_THROUGH`
<a id="insn-00b6cc10"></a> `00b6cc10` | `6e 00 00 36` | tbz w14,#0x0,0x00b6cc1c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc14"></a> `00b6cc14` | `28 60 40 39` | ldrb w8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b6cc18"></a> `00b6cc18` | `28 09 00 35` | cbnz w8,0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc1c"></a> `00b6cc1c` | `48 09 00 d1` | sub x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00b6cc20"></a> `00b6cc20` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00b6cc24"></a> `00b6cc24` | `c3 08 00 54` | b.cc 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc28"></a> `00b6cc28` | `28 69 6e 78` | ldrh w8,[x9, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b6cc2c"></a> `00b6cc2c` | `68 00 00 36` | tbz w8,#0x0,0x00b6cc38 | `CONDITIONAL_JUMP`
<a id="insn-00b6cc30"></a> `00b6cc30` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b6cc34"></a> `00b6cc34` | `4f 08 00 35` | cbnz w15,0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc38"></a> `00b6cc38` | `28 08 00 37` | tbnz w8,#0x0,0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc3c"></a> `00b6cc3c` | `4f 01 08 eb` | subs x15,x10,x8 | `FALL_THROUGH`
<a id="insn-00b6cc40"></a> `00b6cc40` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6cc44"></a> `00b6cc44` | `49 08 00 54` | b.ls 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc48"></a> `00b6cc48` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00b6cc4c"></a> `00b6cc4c` | `03 08 00 54` | b.cc 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc50"></a> `00b6cc50` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6cc54"></a> `00b6cc54` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00b6cc58"></a> `00b6cc58` | `c8 01 40 79` | ldrh w8,[x14] | `FALL_THROUGH`
<a id="insn-00b6cc5c"></a> `00b6cc5c` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00b6cc60"></a> `00b6cc60` | `23 07 00 54` | b.cc 0x00b6cd44 | `CONDITIONAL_JUMP`
<a id="insn-00b6cc64"></a> `00b6cc64` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b6cc68"></a> `00b6cc68` | `68 02 00 b4` | cbz x8,0x00b6ccb4 | `CONDITIONAL_JUMP`
<a id="insn-00b6cc6c"></a> `00b6cc6c` | `ad 01 08 8b` | add x13,x13,x8 | `FALL_THROUGH`
<a id="insn-00b6cc70"></a> `00b6cc70` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00b6cc74"></a> `00b6cc74` | `e0 00 00 54` | b.eq 0x00b6cc90 | `CONDITIONAL_JUMP`
<a id="insn-00b6cc78"></a> `00b6cc78` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b6cc7c"></a> `00b6cc7c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6cc80"></a> `00b6cc80` | `6f 06 00 35` | cbnz w15,0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc84"></a> `00b6cc84` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00b6cc88"></a> `00b6cc88` | `82 00 00 54` | b.cs 0x00b6cc98 | `CONDITIONAL_JUMP`
<a id="insn-00b6cc8c"></a> `00b6cc8c` | `30 00 00 14` | b 0x00b6cd4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6cc90"></a> `00b6cc90` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00b6cc94"></a> `00b6cc94` | `43 05 00 54` | b.cc 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cc98"></a> `00b6cc98` | `28 69 6d b8` | ldr w8,[x9, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b6cc9c"></a> `00b6cc9c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6cca0"></a> `00b6cca0` | `eb 04 00 54` | b.lt 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cca4"></a> `00b6cca4` | `a8 01 08 8b` | add x8,x13,x8 | `FALL_THROUGH`
<a id="insn-00b6cca8"></a> `00b6cca8` | `4d 05 00 d1` | sub x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ccac"></a> `00b6ccac` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00b6ccb0"></a> `00b6ccb0` | `63 04 00 54` | b.cc 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6ccb4"></a> `00b6ccb4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b6ccb8"></a> `00b6ccb8` | `68 04 00 b4` | cbz x8,0x00b6cd44 | `CONDITIONAL_JUMP`
<a id="insn-00b6ccbc"></a> `00b6ccbc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b6ccc0"></a> `00b6ccc0` | `0d 01 40 b9` | ldr w13,[x8] | `FALL_THROUGH`
<a id="insn-00b6ccc4"></a> `00b6ccc4` | `0e 01 0d ab` | adds x14,x8,x13 | `FALL_THROUGH`
<a id="insn-00b6ccc8"></a> `00b6ccc8` | `e0 03 00 54` | b.eq 0x00b6cd44 | `CONDITIONAL_JUMP`
<a id="insn-00b6cccc"></a> `00b6cccc` | `cd 01 09 cb` | sub x13,x14,x9 | `FALL_THROUGH`
<a id="insn-00b6ccd0"></a> `00b6ccd0` | `bf 05 40 f2` | tst x13,#0x3 | `FALL_THROUGH`
<a id="insn-00b6ccd4"></a> `00b6ccd4` | `e0 00 00 54` | b.eq 0x00b6ccf0 | `CONDITIONAL_JUMP`
<a id="insn-00b6ccd8"></a> `00b6ccd8` | `2f 60 40 39` | ldrb w15,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b6ccdc"></a> `00b6ccdc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6cce0"></a> `00b6cce0` | `6f 03 00 35` | cbnz w15,0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cce4"></a> `00b6cce4` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00b6cce8"></a> `00b6cce8` | `82 00 00 54` | b.cs 0x00b6ccf8 | `CONDITIONAL_JUMP`
<a id="insn-00b6ccec"></a> `00b6ccec` | `18 00 00 14` | b 0x00b6cd4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ccf0"></a> `00b6ccf0` | `9f 01 0d eb` | cmp x12,x13 | `FALL_THROUGH`
<a id="insn-00b6ccf4"></a> `00b6ccf4` | `43 02 00 54` | b.cc 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6ccf8"></a> `00b6ccf8` | `c8 01 40 b9` | ldr w8,[x14] | `FALL_THROUGH`
<a id="insn-00b6ccfc"></a> `00b6ccfc` | `2c 10 40 f9` | ldr x12,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00b6cd00"></a> `00b6cd00` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00b6cd04"></a> `00b6cd04` | `c9 01 00 54` | b.ls 0x00b6cd3c | `CONDITIONAL_JUMP`
<a id="insn-00b6cd08"></a> `00b6cd08` | `0e 11 00 91` | add x14,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b6cd0c"></a> `00b6cd0c` | `cc 01 0d 8b` | add x12,x14,x13 | `FALL_THROUGH`
<a id="insn-00b6cd10"></a> `00b6cd10` | `48 05 00 d1` | sub x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b6cd14"></a> `00b6cd14` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00b6cd18"></a> `00b6cd18` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6cd1c"></a> `00b6cd1c` | `83 01 00 54` | b.cc 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cd20"></a> `00b6cd20` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00b6cd24"></a> `00b6cd24` | `49 01 00 54` | b.ls 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cd28"></a> `00b6cd28` | `4a 01 0e cb` | sub x10,x10,x14 | `FALL_THROUGH`
<a id="insn-00b6cd2c"></a> `00b6cd2c` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00b6cd30"></a> `00b6cd30` | `e3 00 00 54` | b.cc 0x00b6cd4c | `CONDITIONAL_JUMP`
<a id="insn-00b6cd34"></a> `00b6cd34` | `28 69 6c 38` | ldrb w8,[x9, x12, LSL ] | `FALL_THROUGH`
<a id="insn-00b6cd38"></a> `00b6cd38` | `68 00 00 34` | cbz w8,0x00b6cd44 | `CONDITIONAL_JUMP`
<a id="insn-00b6cd3c"></a> `00b6cd3c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b6cd40"></a> `00b6cd40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6cd44"></a> `00b6cd44` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6cd48"></a> `00b6cd48` | `2b 38 00 b9` | str w11,[x1, #0x38] | `FALL_THROUGH`
<a id="insn-00b6cd4c"></a> `00b6cd4c` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00b6cd50"></a> `00b6cd50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6cbac`](#insn-00b6cbac) 範囲 `[['00b6cbac', '00b6cbbb']]`
  - `CONDITIONAL_JUMP` [`00b6cbb8`](#insn-00b6cbb8) → [`00b6cbc4`](#insn-00b6cbc4)
  - `FALL_THROUGH` [`00b6cbb8`](#insn-00b6cbb8) → [`00b6cbbc`](#insn-00b6cbbc)
- ブロック [`00b6cbbc`](#insn-00b6cbbc) 範囲 `[['00b6cbbc', '00b6cbc3']]`
  - `CONDITIONAL_JUMP` [`00b6cbc0`](#insn-00b6cbc0) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cbc0`](#insn-00b6cbc0) → [`00b6cbc4`](#insn-00b6cbc4)
- ブロック [`00b6cbc4`](#insn-00b6cbc4) 範囲 `[['00b6cbc4', '00b6cbd3']]`
  - `CONDITIONAL_JUMP` [`00b6cbd0`](#insn-00b6cbd0) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cbd0`](#insn-00b6cbd0) → [`00b6cbd4`](#insn-00b6cbd4)
- ブロック [`00b6cbd4`](#insn-00b6cbd4) 範囲 `[['00b6cbd4', '00b6cbdf']]`
  - `CONDITIONAL_JUMP` [`00b6cbdc`](#insn-00b6cbdc) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cbdc`](#insn-00b6cbdc) → [`00b6cbe0`](#insn-00b6cbe0)
- ブロック [`00b6cbe0`](#insn-00b6cbe0) 範囲 `[['00b6cbe0', '00b6cbff']]`
  - `CONDITIONAL_JUMP` [`00b6cbfc`](#insn-00b6cbfc) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cbfc`](#insn-00b6cbfc) → [`00b6cc00`](#insn-00b6cc00)
- ブロック [`00b6cc00`](#insn-00b6cc00) 範囲 `[['00b6cc00', '00b6cc0b']]`
  - `CONDITIONAL_JUMP` [`00b6cc08`](#insn-00b6cc08) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc08`](#insn-00b6cc08) → [`00b6cc0c`](#insn-00b6cc0c)
- ブロック [`00b6cc0c`](#insn-00b6cc0c) 範囲 `[['00b6cc0c', '00b6cc13']]`
  - `CONDITIONAL_JUMP` [`00b6cc10`](#insn-00b6cc10) → [`00b6cc1c`](#insn-00b6cc1c)
  - `FALL_THROUGH` [`00b6cc10`](#insn-00b6cc10) → [`00b6cc14`](#insn-00b6cc14)
- ブロック [`00b6cc14`](#insn-00b6cc14) 範囲 `[['00b6cc14', '00b6cc1b']]`
  - `CONDITIONAL_JUMP` [`00b6cc18`](#insn-00b6cc18) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc18`](#insn-00b6cc18) → [`00b6cc1c`](#insn-00b6cc1c)
- ブロック [`00b6cc1c`](#insn-00b6cc1c) 範囲 `[['00b6cc1c', '00b6cc27']]`
  - `CONDITIONAL_JUMP` [`00b6cc24`](#insn-00b6cc24) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc24`](#insn-00b6cc24) → [`00b6cc28`](#insn-00b6cc28)
- ブロック [`00b6cc28`](#insn-00b6cc28) 範囲 `[['00b6cc28', '00b6cc2f']]`
  - `CONDITIONAL_JUMP` [`00b6cc2c`](#insn-00b6cc2c) → [`00b6cc38`](#insn-00b6cc38)
  - `FALL_THROUGH` [`00b6cc2c`](#insn-00b6cc2c) → [`00b6cc30`](#insn-00b6cc30)
- ブロック [`00b6cc30`](#insn-00b6cc30) 範囲 `[['00b6cc30', '00b6cc37']]`
  - `CONDITIONAL_JUMP` [`00b6cc34`](#insn-00b6cc34) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc34`](#insn-00b6cc34) → [`00b6cc38`](#insn-00b6cc38)
- ブロック [`00b6cc38`](#insn-00b6cc38) 範囲 `[['00b6cc38', '00b6cc3b']]`
  - `CONDITIONAL_JUMP` [`00b6cc38`](#insn-00b6cc38) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc38`](#insn-00b6cc38) → [`00b6cc3c`](#insn-00b6cc3c)
- ブロック [`00b6cc3c`](#insn-00b6cc3c) 範囲 `[['00b6cc3c', '00b6cc47']]`
  - `CONDITIONAL_JUMP` [`00b6cc44`](#insn-00b6cc44) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cc44`](#insn-00b6cc44) → [`00b6cc48`](#insn-00b6cc48)
- ブロック [`00b6cc48`](#insn-00b6cc48) 範囲 `[['00b6cc48', '00b6cc4f']]`
  - `CONDITIONAL_JUMP` [`00b6cc4c`](#insn-00b6cc4c) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cc4c`](#insn-00b6cc4c) → [`00b6cc50`](#insn-00b6cc50)
- ブロック [`00b6cc50`](#insn-00b6cc50) 範囲 `[['00b6cc50', '00b6cc63']]`
  - `CONDITIONAL_JUMP` [`00b6cc60`](#insn-00b6cc60) → [`00b6cd44`](#insn-00b6cd44)
  - `FALL_THROUGH` [`00b6cc60`](#insn-00b6cc60) → [`00b6cc64`](#insn-00b6cc64)
- ブロック [`00b6cc64`](#insn-00b6cc64) 範囲 `[['00b6cc64', '00b6cc6b']]`
  - `CONDITIONAL_JUMP` [`00b6cc68`](#insn-00b6cc68) → [`00b6ccb4`](#insn-00b6ccb4)
  - `FALL_THROUGH` [`00b6cc68`](#insn-00b6cc68) → [`00b6cc6c`](#insn-00b6cc6c)
- ブロック [`00b6cc6c`](#insn-00b6cc6c) 範囲 `[['00b6cc6c', '00b6cc77']]`
  - `CONDITIONAL_JUMP` [`00b6cc74`](#insn-00b6cc74) → [`00b6cc90`](#insn-00b6cc90)
  - `FALL_THROUGH` [`00b6cc74`](#insn-00b6cc74) → [`00b6cc78`](#insn-00b6cc78)
- ブロック [`00b6cc78`](#insn-00b6cc78) 範囲 `[['00b6cc78', '00b6cc83']]`
  - `CONDITIONAL_JUMP` [`00b6cc80`](#insn-00b6cc80) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cc80`](#insn-00b6cc80) → [`00b6cc84`](#insn-00b6cc84)
- ブロック [`00b6cc84`](#insn-00b6cc84) 範囲 `[['00b6cc84', '00b6cc8b']]`
  - `CONDITIONAL_JUMP` [`00b6cc88`](#insn-00b6cc88) → [`00b6cc98`](#insn-00b6cc98)
  - `FALL_THROUGH` [`00b6cc88`](#insn-00b6cc88) → [`00b6cc8c`](#insn-00b6cc8c)
- ブロック [`00b6cc8c`](#insn-00b6cc8c) 範囲 `[['00b6cc8c', '00b6cc8f']]`
  - `UNCONDITIONAL_JUMP` [`00b6cc8c`](#insn-00b6cc8c) → [`00b6cd4c`](#insn-00b6cd4c)
- ブロック [`00b6cc90`](#insn-00b6cc90) 範囲 `[['00b6cc90', '00b6cc97']]`
  - `CONDITIONAL_JUMP` [`00b6cc94`](#insn-00b6cc94) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cc94`](#insn-00b6cc94) → [`00b6cc98`](#insn-00b6cc98)
- ブロック [`00b6cc98`](#insn-00b6cc98) 範囲 `[['00b6cc98', '00b6cca3']]`
  - `CONDITIONAL_JUMP` [`00b6cca0`](#insn-00b6cca0) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cca0`](#insn-00b6cca0) → [`00b6cca4`](#insn-00b6cca4)
- ブロック [`00b6cca4`](#insn-00b6cca4) 範囲 `[['00b6cca4', '00b6ccb3']]`
  - `CONDITIONAL_JUMP` [`00b6ccb0`](#insn-00b6ccb0) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6ccb0`](#insn-00b6ccb0) → [`00b6ccb4`](#insn-00b6ccb4)
- ブロック [`00b6ccb4`](#insn-00b6ccb4) 範囲 `[['00b6ccb4', '00b6ccbb']]`
  - `CONDITIONAL_JUMP` [`00b6ccb8`](#insn-00b6ccb8) → [`00b6cd44`](#insn-00b6cd44)
  - `FALL_THROUGH` [`00b6ccb8`](#insn-00b6ccb8) → [`00b6ccbc`](#insn-00b6ccbc)
- ブロック [`00b6ccbc`](#insn-00b6ccbc) 範囲 `[['00b6ccbc', '00b6cccb']]`
  - `CONDITIONAL_JUMP` [`00b6ccc8`](#insn-00b6ccc8) → [`00b6cd44`](#insn-00b6cd44)
  - `FALL_THROUGH` [`00b6ccc8`](#insn-00b6ccc8) → [`00b6cccc`](#insn-00b6cccc)
- ブロック [`00b6cccc`](#insn-00b6cccc) 範囲 `[['00b6cccc', '00b6ccd7']]`
  - `CONDITIONAL_JUMP` [`00b6ccd4`](#insn-00b6ccd4) → [`00b6ccf0`](#insn-00b6ccf0)
  - `FALL_THROUGH` [`00b6ccd4`](#insn-00b6ccd4) → [`00b6ccd8`](#insn-00b6ccd8)
- ブロック [`00b6ccd8`](#insn-00b6ccd8) 範囲 `[['00b6ccd8', '00b6cce3']]`
  - `CONDITIONAL_JUMP` [`00b6cce0`](#insn-00b6cce0) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cce0`](#insn-00b6cce0) → [`00b6cce4`](#insn-00b6cce4)
- ブロック [`00b6cce4`](#insn-00b6cce4) 範囲 `[['00b6cce4', '00b6cceb']]`
  - `CONDITIONAL_JUMP` [`00b6cce8`](#insn-00b6cce8) → [`00b6ccf8`](#insn-00b6ccf8)
  - `FALL_THROUGH` [`00b6cce8`](#insn-00b6cce8) → [`00b6ccec`](#insn-00b6ccec)
- ブロック [`00b6ccec`](#insn-00b6ccec) 範囲 `[['00b6ccec', '00b6ccef']]`
  - `UNCONDITIONAL_JUMP` [`00b6ccec`](#insn-00b6ccec) → [`00b6cd4c`](#insn-00b6cd4c)
- ブロック [`00b6ccf0`](#insn-00b6ccf0) 範囲 `[['00b6ccf0', '00b6ccf7']]`
  - `CONDITIONAL_JUMP` [`00b6ccf4`](#insn-00b6ccf4) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6ccf4`](#insn-00b6ccf4) → [`00b6ccf8`](#insn-00b6ccf8)
- ブロック [`00b6ccf8`](#insn-00b6ccf8) 範囲 `[['00b6ccf8', '00b6cd07']]`
  - `CONDITIONAL_JUMP` [`00b6cd04`](#insn-00b6cd04) → [`00b6cd3c`](#insn-00b6cd3c)
  - `FALL_THROUGH` [`00b6cd04`](#insn-00b6cd04) → [`00b6cd08`](#insn-00b6cd08)
- ブロック [`00b6cd08`](#insn-00b6cd08) 範囲 `[['00b6cd08', '00b6cd1f']]`
  - `CONDITIONAL_JUMP` [`00b6cd1c`](#insn-00b6cd1c) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cd1c`](#insn-00b6cd1c) → [`00b6cd20`](#insn-00b6cd20)
- ブロック [`00b6cd20`](#insn-00b6cd20) 範囲 `[['00b6cd20', '00b6cd27']]`
  - `CONDITIONAL_JUMP` [`00b6cd24`](#insn-00b6cd24) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cd24`](#insn-00b6cd24) → [`00b6cd28`](#insn-00b6cd28)
- ブロック [`00b6cd28`](#insn-00b6cd28) 範囲 `[['00b6cd28', '00b6cd33']]`
  - `CONDITIONAL_JUMP` [`00b6cd30`](#insn-00b6cd30) → [`00b6cd4c`](#insn-00b6cd4c)
  - `FALL_THROUGH` [`00b6cd30`](#insn-00b6cd30) → [`00b6cd34`](#insn-00b6cd34)
- ブロック [`00b6cd34`](#insn-00b6cd34) 範囲 `[['00b6cd34', '00b6cd3b']]`
  - `CONDITIONAL_JUMP` [`00b6cd38`](#insn-00b6cd38) → [`00b6cd44`](#insn-00b6cd44)
  - `FALL_THROUGH` [`00b6cd38`](#insn-00b6cd38) → [`00b6cd3c`](#insn-00b6cd3c)
- ブロック [`00b6cd3c`](#insn-00b6cd3c) 範囲 `[['00b6cd3c', '00b6cd43']]`
- ブロック [`00b6cd44`](#insn-00b6cd44) 範囲 `[['00b6cd44', '00b6cd4b']]`
  - `FALL_THROUGH` [`00b6cd48`](#insn-00b6cd48) → [`00b6cd4c`](#insn-00b6cd4c)
- ブロック [`00b6cd4c`](#insn-00b6cd4c) 範囲 `[['00b6cd4c', '00b6cd53']]`

## 命令位置別の参照

- [`00b6cbb8`](#insn-00b6cbb8) → [`00b6cbc4`](#insn-00b6cbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cbc0`](#insn-00b6cbc0) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cbd0`](#insn-00b6cbd0) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cbdc`](#insn-00b6cbdc) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cbfc`](#insn-00b6cbfc) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc08`](#insn-00b6cc08) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc10`](#insn-00b6cc10) → [`00b6cc1c`](#insn-00b6cc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc18`](#insn-00b6cc18) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc24`](#insn-00b6cc24) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc2c`](#insn-00b6cc2c) → [`00b6cc38`](#insn-00b6cc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc34`](#insn-00b6cc34) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc38`](#insn-00b6cc38) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc44`](#insn-00b6cc44) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc4c`](#insn-00b6cc4c) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc60`](#insn-00b6cc60) → [`00b6cd44`](#insn-00b6cd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc68`](#insn-00b6cc68) → [`00b6ccb4`](#insn-00b6ccb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc74`](#insn-00b6cc74) → [`00b6cc90`](#insn-00b6cc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc80`](#insn-00b6cc80) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc88`](#insn-00b6cc88) → [`00b6cc98`](#insn-00b6cc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc8c`](#insn-00b6cc8c) → [`00b6cd4c`](#insn-00b6cd4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cc94`](#insn-00b6cc94) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cca0`](#insn-00b6cca0) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccb0`](#insn-00b6ccb0) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccb8`](#insn-00b6ccb8) → [`00b6cd44`](#insn-00b6cd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccc8`](#insn-00b6ccc8) → [`00b6cd44`](#insn-00b6cd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccd4`](#insn-00b6ccd4) → [`00b6ccf0`](#insn-00b6ccf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cce0`](#insn-00b6cce0) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cce8`](#insn-00b6cce8) → [`00b6ccf8`](#insn-00b6ccf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccec`](#insn-00b6ccec) → [`00b6cd4c`](#insn-00b6cd4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ccf4`](#insn-00b6ccf4) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cd04`](#insn-00b6cd04) → [`00b6cd3c`](#insn-00b6cd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cd1c`](#insn-00b6cd1c) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cd24`](#insn-00b6cd24) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cd30`](#insn-00b6cd30) → [`00b6cd4c`](#insn-00b6cd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6cd38`](#insn-00b6cd38) → [`00b6cd44`](#insn-00b6cd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6cbb8`](#insn-00b6cbb8)

~~~json
{
  "source": "00b6cbb8",
  "target": "00b6cbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cbc0`](#insn-00b6cbc0)

~~~json
{
  "source": "00b6cbc0",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cbd0`](#insn-00b6cbd0)

~~~json
{
  "source": "00b6cbd0",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cbdc`](#insn-00b6cbdc)

~~~json
{
  "source": "00b6cbdc",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cbfc`](#insn-00b6cbfc)

~~~json
{
  "source": "00b6cbfc",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc08`](#insn-00b6cc08)

~~~json
{
  "source": "00b6cc08",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc10`](#insn-00b6cc10)

~~~json
{
  "source": "00b6cc10",
  "target": "00b6cc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc18`](#insn-00b6cc18)

~~~json
{
  "source": "00b6cc18",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc24`](#insn-00b6cc24)

~~~json
{
  "source": "00b6cc24",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc2c`](#insn-00b6cc2c)

~~~json
{
  "source": "00b6cc2c",
  "target": "00b6cc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc34`](#insn-00b6cc34)

~~~json
{
  "source": "00b6cc34",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc38`](#insn-00b6cc38)

~~~json
{
  "source": "00b6cc38",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc44`](#insn-00b6cc44)

~~~json
{
  "source": "00b6cc44",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc4c`](#insn-00b6cc4c)

~~~json
{
  "source": "00b6cc4c",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc60`](#insn-00b6cc60)

~~~json
{
  "source": "00b6cc60",
  "target": "00b6cd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc68`](#insn-00b6cc68)

~~~json
{
  "source": "00b6cc68",
  "target": "00b6ccb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc74`](#insn-00b6cc74)

~~~json
{
  "source": "00b6cc74",
  "target": "00b6cc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc80`](#insn-00b6cc80)

~~~json
{
  "source": "00b6cc80",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc88`](#insn-00b6cc88)

~~~json
{
  "source": "00b6cc88",
  "target": "00b6cc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc8c`](#insn-00b6cc8c)

~~~json
{
  "source": "00b6cc8c",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cc94`](#insn-00b6cc94)

~~~json
{
  "source": "00b6cc94",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cca0`](#insn-00b6cca0)

~~~json
{
  "source": "00b6cca0",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccb0`](#insn-00b6ccb0)

~~~json
{
  "source": "00b6ccb0",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccb8`](#insn-00b6ccb8)

~~~json
{
  "source": "00b6ccb8",
  "target": "00b6cd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccc8`](#insn-00b6ccc8)

~~~json
{
  "source": "00b6ccc8",
  "target": "00b6cd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccd4`](#insn-00b6ccd4)

~~~json
{
  "source": "00b6ccd4",
  "target": "00b6ccf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cce0`](#insn-00b6cce0)

~~~json
{
  "source": "00b6cce0",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cce8`](#insn-00b6cce8)

~~~json
{
  "source": "00b6cce8",
  "target": "00b6ccf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccec`](#insn-00b6ccec)

~~~json
{
  "source": "00b6ccec",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ccf4`](#insn-00b6ccf4)

~~~json
{
  "source": "00b6ccf4",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cd04`](#insn-00b6cd04)

~~~json
{
  "source": "00b6cd04",
  "target": "00b6cd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cd1c`](#insn-00b6cd1c)

~~~json
{
  "source": "00b6cd1c",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cd24`](#insn-00b6cd24)

~~~json
{
  "source": "00b6cd24",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cd30`](#insn-00b6cd30)

~~~json
{
  "source": "00b6cd30",
  "target": "00b6cd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6cd38`](#insn-00b6cd38)

~~~json
{
  "source": "00b6cd38",
  "target": "00b6cd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
