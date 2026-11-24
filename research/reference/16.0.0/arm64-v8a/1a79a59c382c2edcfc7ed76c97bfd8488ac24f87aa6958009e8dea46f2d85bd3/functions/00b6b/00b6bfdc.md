# 00b6bfdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0172.md#review-fcc13590b6ed94f71a1dd50c32988cda)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6c404`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c404.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-96d4f7042c3aea87a1284a9691d44430)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6bfdc",
  "name": "_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 640,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4db6b72ba7917b092ff2aa58c8f10a9f34daf360b48c6a65ad644509b1f8892",
  "source_text_sha256": "c4db6b72ba7917b092ff2aa58c8f10a9f34daf360b48c6a65ad644509b1f8892",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6bfdc",
        "00b6c25b"
      ]
    ],
    "bytes_sha256": "eadf7ee78dd54040849ec0612f175eefa53d38f77bd833c4d3560e6c3282352c",
    "instruction_count": 160,
    "instruction_bytes": 640,
    "body_bytes": 640,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5b570](../00c5b/00c5b570.md)

## 呼び出し先

- [00c5b560](../00c5b/00c5b560.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5395 bytes

~~~c

undefined4
_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

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
  uVar9 = (long)param_1 - lVar7;
  if (((uVar9 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar8 = param_2[1];
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b6c020 to 00c6c0f7 has its CatchHandler @ 00b6c020
                       catch() { ... } // from try @ 00b6c020 with catch @ 00b6c020
                       catch() { ... } // from try @ 00b6c14c with catch @ 00b6c020 */
    iVar5 = *param_1;
    uVar6 = (int)param_2[7] + 1;
    uVar1 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar6;
    *(uint *)((long)param_2 + 0x3c) = uVar1;
    if ((((uVar6 <= *(uint *)(param_2 + 2)) && (uVar1 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar11 = uVar9 - (long)iVar5, (uVar11 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
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
        uVar4 = *puVar12;
        if (4 < uVar4) {
          if ((ulong)puVar12[2] != 0) {
            uVar11 = uVar9 + puVar12[2];
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
            if ((int)*(uint *)(lVar7 + uVar11) < 1) {
              return 0;
            }
            if (uVar8 - 1 < uVar11 + *(uint *)(lVar7 + uVar11)) {
              return 0;
            }
          }
                    /* try { // try from 00b6c0f8 to 00c6c14b has its CatchHandler @ 00b6c228 */
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
              if ((char)param_2[3] != '\0') {
                return 0;
              }
              if (uVar10 < uVar11) {
                return 0;
              }
            }
            if ((ulong)param_2[4] <= (ulong)*puVar3) {
              return 0;
            }
            uVar2 = (ulong)*puVar3 + 4;
                    /* try { // try from 00b6c14c to 00c6c253 has its CatchHandler @ 00b6c020 */
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
          if (6 < uVar4) {
            if ((ulong)puVar12[3] != 0) {
              uVar11 = uVar9 + puVar12[3];
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
            }
            if (8 < uVar4) {
              if ((ulong)puVar12[4] != 0) {
                uVar9 = uVar9 + puVar12[4];
                if ((uVar9 & 3) == 0) {
                  if (uVar10 < uVar9) {
                    return 0;
                  }
                }
                else {
                  if ((char)param_2[3] != '\0') {
                    return 0;
                  }
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
              if (((ulong)puVar12[4] != 0) &&
                 (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[4]),
                 lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
                    /* catch() { ... } // from try @ 00b6c0f8 with catch @ 00b6c228 */
                uVar9 = _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                  (lVar7,param_2);
                if ((uVar9 & 1) == 0) {
                  return 0;
                }
                uVar6 = *(uint *)(param_2 + 7);
              }
            }
          }
        }
        *(uint *)(param_2 + 7) = uVar6 - 1;
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
<a id="insn-00b6bfdc"></a> `00b6bfdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6bfe0"></a> `00b6bfe0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6bfe4"></a> `00b6bfe4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6bfe8"></a> `00b6bfe8` | `2a 00 40 f9` | ldr x10,[x1] | `FALL_THROUGH`
<a id="insn-00b6bfec"></a> `00b6bfec` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b6bff0"></a> `00b6bff0` | `0c 00 0a cb` | sub x12,x0,x10 | `FALL_THROUGH`
<a id="insn-00b6bff4"></a> `00b6bff4` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b6bff8"></a> `00b6bff8` | `60 00 00 54` | b.eq 0x00b6c004 | `CONDITIONAL_JUMP`
<a id="insn-00b6bffc"></a> `00b6bffc` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c000"></a> `00b6c000` | `48 12 00 35` | cbnz w8,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c004"></a> `00b6c004` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6c008"></a> `00b6c008` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c00c"></a> `00b6c00c` | `7f 15 00 f1` | cmp x11,#0x5 | `FALL_THROUGH`
<a id="insn-00b6c010"></a> `00b6c010` | `e3 11 00 54` | b.cc 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c014"></a> `00b6c014` | `6d 11 00 d1` | sub x13,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b6c018"></a> `00b6c018` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b6c01c"></a> `00b6c01c` | `83 11 00 54` | b.cc 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c020"></a> `00b6c020` | `69 3a 47 29` | ldp w9,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6c024"></a> `00b6c024` | `6f 12 40 b9` | ldr w15,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6c028"></a> `00b6c028` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6c02c"></a> `00b6c02c` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c030"></a> `00b6c030` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c034"></a> `00b6c034` | `3f 01 0f 6b` | cmp w9,w15 | `FALL_THROUGH`
<a id="insn-00b6c038"></a> `00b6c038` | `69 3a 07 29` | stp w9,w14,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6c03c"></a> `00b6c03c` | `68 10 00 54` | b.hi 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c040"></a> `00b6c040` | `6f 16 40 b9` | ldr w15,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00b6c044"></a> `00b6c044` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b6c048"></a> `00b6c048` | `08 10 00 54` | b.hi 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c04c"></a> `00b6c04c` | `8e 01 08 cb` | sub x14,x12,x8 | `FALL_THROUGH`
<a id="insn-00b6c050"></a> `00b6c050` | `6e 00 00 36` | tbz w14,#0x0,0x00b6c05c | `CONDITIONAL_JUMP`
<a id="insn-00b6c054"></a> `00b6c054` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c058"></a> `00b6c058` | `88 0f 00 35` | cbnz w8,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c05c"></a> `00b6c05c` | `68 09 00 d1` | sub x8,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b6c060"></a> `00b6c060` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00b6c064"></a> `00b6c064` | `23 0f 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c068"></a> `00b6c068` | `48 69 6e 78` | ldrh w8,[x10, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b6c06c"></a> `00b6c06c` | `68 00 00 36` | tbz w8,#0x0,0x00b6c078 | `CONDITIONAL_JUMP`
<a id="insn-00b6c070"></a> `00b6c070` | `6f 62 40 39` | ldrb w15,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c074"></a> `00b6c074` | `af 0e 00 35` | cbnz w15,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c078"></a> `00b6c078` | `88 0e 00 37` | tbnz w8,#0x0,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c07c"></a> `00b6c07c` | `6f 01 08 eb` | subs x15,x11,x8 | `FALL_THROUGH`
<a id="insn-00b6c080"></a> `00b6c080` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c084"></a> `00b6c084` | `49 0e 00 54` | b.ls 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c088"></a> `00b6c088` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00b6c08c"></a> `00b6c08c` | `03 0e 00 54` | b.cc 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c090"></a> `00b6c090` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b6c094"></a> `00b6c094` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00b6c098"></a> `00b6c098` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00b6c09c"></a> `00b6c09c` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00b6c0a0"></a> `00b6c0a0` | `c3 0c 00 54` | b.cc 0x00b6c238 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0a4"></a> `00b6c0a4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b6c0a8"></a> `00b6c0a8` | `68 02 00 b4` | cbz x8,0x00b6c0f4 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0ac"></a> `00b6c0ac` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b6c0b0"></a> `00b6c0b0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b6c0b4"></a> `00b6c0b4` | `e0 00 00 54` | b.eq 0x00b6c0d0 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0b8"></a> `00b6c0b8` | `71 62 40 39` | ldrb w17,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c0bc"></a> `00b6c0bc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c0c0"></a> `00b6c0c0` | `71 0c 00 35` | cbnz w17,0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c0c4"></a> `00b6c0c4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c0c8"></a> `00b6c0c8` | `82 00 00 54` | b.cs 0x00b6c0d8 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0cc"></a> `00b6c0cc` | `60 00 00 14` | b 0x00b6c24c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6c0d0"></a> `00b6c0d0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c0d4"></a> `00b6c0d4` | `a3 0b 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0d8"></a> `00b6c0d8` | `48 69 70 b8` | ldr w8,[x10, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b6c0dc"></a> `00b6c0dc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c0e0"></a> `00b6c0e0` | `4b 0b 00 54` | b.lt 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0e4"></a> `00b6c0e4` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00b6c0e8"></a> `00b6c0e8` | `70 05 00 d1` | sub x16,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c0ec"></a> `00b6c0ec` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00b6c0f0"></a> `00b6c0f0` | `c3 0a 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c0f4"></a> `00b6c0f4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b6c0f8"></a> `00b6c0f8` | `28 04 00 b4` | cbz x8,0x00b6c17c | `CONDITIONAL_JUMP`
<a id="insn-00b6c0fc"></a> `00b6c0fc` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b6c100"></a> `00b6c100` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00b6c104"></a> `00b6c104` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00b6c108"></a> `00b6c108` | `a0 03 00 54` | b.eq 0x00b6c17c | `CONDITIONAL_JUMP`
<a id="insn-00b6c10c"></a> `00b6c10c` | `30 02 0a cb` | sub x16,x17,x10 | `FALL_THROUGH`
<a id="insn-00b6c110"></a> `00b6c110` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b6c114"></a> `00b6c114` | `e0 00 00 54` | b.eq 0x00b6c130 | `CONDITIONAL_JUMP`
<a id="insn-00b6c118"></a> `00b6c118` | `61 62 40 39` | ldrb w1,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c11c"></a> `00b6c11c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c120"></a> `00b6c120` | `61 09 00 35` | cbnz w1,0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c124"></a> `00b6c124` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c128"></a> `00b6c128` | `82 00 00 54` | b.cs 0x00b6c138 | `CONDITIONAL_JUMP`
<a id="insn-00b6c12c"></a> `00b6c12c` | `48 00 00 14` | b 0x00b6c24c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6c130"></a> `00b6c130` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c134"></a> `00b6c134` | `a3 08 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c138"></a> `00b6c138` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00b6c13c"></a> `00b6c13c` | `71 12 40 f9` | ldr x17,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6c140"></a> `00b6c140` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00b6c144"></a> `00b6c144` | `29 08 00 54` | b.ls 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c148"></a> `00b6c148` | `01 11 00 91` | add x1,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b6c14c"></a> `00b6c14c` | `31 00 10 8b` | add x17,x1,x16 | `FALL_THROUGH`
<a id="insn-00b6c150"></a> `00b6c150` | `68 05 00 d1` | sub x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c154"></a> `00b6c154` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00b6c158"></a> `00b6c158` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c15c"></a> `00b6c15c` | `83 07 00 54` | b.cc 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c160"></a> `00b6c160` | `7f 01 01 eb` | cmp x11,x1 | `FALL_THROUGH`
<a id="insn-00b6c164"></a> `00b6c164` | `49 07 00 54` | b.ls 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c168"></a> `00b6c168` | `61 01 01 cb` | sub x1,x11,x1 | `FALL_THROUGH`
<a id="insn-00b6c16c"></a> `00b6c16c` | `3f 00 10 eb` | cmp x1,x16 | `FALL_THROUGH`
<a id="insn-00b6c170"></a> `00b6c170` | `e3 06 00 54` | b.cc 0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c174"></a> `00b6c174` | `48 69 71 38` | ldrb w8,[x10, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00b6c178"></a> `00b6c178` | `88 06 00 35` | cbnz w8,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c17c"></a> `00b6c17c` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00b6c180"></a> `00b6c180` | `c3 05 00 54` | b.cc 0x00b6c238 | `CONDITIONAL_JUMP`
<a id="insn-00b6c184"></a> `00b6c184` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b6c188"></a> `00b6c188` | `88 01 00 b4` | cbz x8,0x00b6c1b8 | `CONDITIONAL_JUMP`
<a id="insn-00b6c18c"></a> `00b6c18c` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b6c190"></a> `00b6c190` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b6c194"></a> `00b6c194` | `e0 00 00 54` | b.eq 0x00b6c1b0 | `CONDITIONAL_JUMP`
<a id="insn-00b6c198"></a> `00b6c198` | `71 62 40 39` | ldrb w17,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c19c"></a> `00b6c19c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c1a0"></a> `00b6c1a0` | `71 05 00 35` | cbnz w17,0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c1a4"></a> `00b6c1a4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c1a8"></a> `00b6c1a8` | `82 00 00 54` | b.cs 0x00b6c1b8 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1ac"></a> `00b6c1ac` | `28 00 00 14` | b 0x00b6c24c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6c1b0"></a> `00b6c1b0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b6c1b4"></a> `00b6c1b4` | `a3 04 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1b8"></a> `00b6c1b8` | `ff 25 00 71` | cmp w15,#0x9 | `FALL_THROUGH`
<a id="insn-00b6c1bc"></a> `00b6c1bc` | `e3 03 00 54` | b.cc 0x00b6c238 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1c0"></a> `00b6c1c0` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b6c1c4"></a> `00b6c1c4` | `68 02 00 b4` | cbz x8,0x00b6c210 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1c8"></a> `00b6c1c8` | `8c 01 08 8b` | add x12,x12,x8 | `FALL_THROUGH`
<a id="insn-00b6c1cc"></a> `00b6c1cc` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b6c1d0"></a> `00b6c1d0` | `e0 00 00 54` | b.eq 0x00b6c1ec | `CONDITIONAL_JUMP`
<a id="insn-00b6c1d4"></a> `00b6c1d4` | `6f 62 40 39` | ldrb w15,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6c1d8"></a> `00b6c1d8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c1dc"></a> `00b6c1dc` | `8f 03 00 35` | cbnz w15,0x00b6c24c | `CONDITIONAL_JUMP`
<a id="insn-00b6c1e0"></a> `00b6c1e0` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b6c1e4"></a> `00b6c1e4` | `82 00 00 54` | b.cs 0x00b6c1f4 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1e8"></a> `00b6c1e8` | `19 00 00 14` | b 0x00b6c24c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6c1ec"></a> `00b6c1ec` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b6c1f0"></a> `00b6c1f0` | `c3 02 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c1f4"></a> `00b6c1f4` | `48 69 6c b8` | ldr w8,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b6c1f8"></a> `00b6c1f8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c1fc"></a> `00b6c1fc` | `6b 02 00 54` | b.lt 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c200"></a> `00b6c200` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b6c204"></a> `00b6c204` | `6a 05 00 d1` | sub x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c208"></a> `00b6c208` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b6c20c"></a> `00b6c20c` | `e3 01 00 54` | b.cc 0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c210"></a> `00b6c210` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b6c214"></a> `00b6c214` | `28 01 00 b4` | cbz x8,0x00b6c238 | `CONDITIONAL_JUMP`
<a id="insn-00b6c218"></a> `00b6c218` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b6c21c"></a> `00b6c21c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b6c220"></a> `00b6c220` | `00 01 0a ab` | adds x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b6c224"></a> `00b6c224` | `a0 00 00 54` | b.eq 0x00b6c238 | `CONDITIONAL_JUMP`
<a id="insn-00b6c228"></a> `00b6c228` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b6c22c"></a> `00b6c22c` | `cd bc 03 94` | bl 0x00c5b560 | `UNCONDITIONAL_CALL`
<a id="insn-00b6c230"></a> `00b6c230` | `c0 00 00 36` | tbz w0,#0x0,0x00b6c248 | `CONDITIONAL_JUMP`
<a id="insn-00b6c234"></a> `00b6c234` | `69 3a 40 b9` | ldr w9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6c238"></a> `00b6c238` | `28 05 00 51` | sub w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c23c"></a> `00b6c23c` | `68 3a 00 b9` | str w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6c240"></a> `00b6c240` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6c244"></a> `00b6c244` | `02 00 00 14` | b 0x00b6c24c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6c248"></a> `00b6c248` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b6c24c"></a> `00b6c24c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6c250"></a> `00b6c250` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00b6c254"></a> `00b6c254` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6c258"></a> `00b6c258` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6bfdc`](#insn-00b6bfdc) 範囲 `[['00b6bfdc', '00b6bffb']]`
  - `CONDITIONAL_JUMP` [`00b6bff8`](#insn-00b6bff8) → [`00b6c004`](#insn-00b6c004)
  - `FALL_THROUGH` [`00b6bff8`](#insn-00b6bff8) → [`00b6bffc`](#insn-00b6bffc)
- ブロック [`00b6bffc`](#insn-00b6bffc) 範囲 `[['00b6bffc', '00b6c003']]`
  - `CONDITIONAL_JUMP` [`00b6c000`](#insn-00b6c000) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c000`](#insn-00b6c000) → [`00b6c004`](#insn-00b6c004)
- ブロック [`00b6c004`](#insn-00b6c004) 範囲 `[['00b6c004', '00b6c013']]`
  - `CONDITIONAL_JUMP` [`00b6c010`](#insn-00b6c010) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c010`](#insn-00b6c010) → [`00b6c014`](#insn-00b6c014)
- ブロック [`00b6c014`](#insn-00b6c014) 範囲 `[['00b6c014', '00b6c01f']]`
  - `CONDITIONAL_JUMP` [`00b6c01c`](#insn-00b6c01c) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c01c`](#insn-00b6c01c) → [`00b6c020`](#insn-00b6c020)
- ブロック [`00b6c020`](#insn-00b6c020) 範囲 `[['00b6c020', '00b6c03f']]`
  - `CONDITIONAL_JUMP` [`00b6c03c`](#insn-00b6c03c) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c03c`](#insn-00b6c03c) → [`00b6c040`](#insn-00b6c040)
- ブロック [`00b6c040`](#insn-00b6c040) 範囲 `[['00b6c040', '00b6c04b']]`
  - `CONDITIONAL_JUMP` [`00b6c048`](#insn-00b6c048) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c048`](#insn-00b6c048) → [`00b6c04c`](#insn-00b6c04c)
- ブロック [`00b6c04c`](#insn-00b6c04c) 範囲 `[['00b6c04c', '00b6c053']]`
  - `CONDITIONAL_JUMP` [`00b6c050`](#insn-00b6c050) → [`00b6c05c`](#insn-00b6c05c)
  - `FALL_THROUGH` [`00b6c050`](#insn-00b6c050) → [`00b6c054`](#insn-00b6c054)
- ブロック [`00b6c054`](#insn-00b6c054) 範囲 `[['00b6c054', '00b6c05b']]`
  - `CONDITIONAL_JUMP` [`00b6c058`](#insn-00b6c058) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c058`](#insn-00b6c058) → [`00b6c05c`](#insn-00b6c05c)
- ブロック [`00b6c05c`](#insn-00b6c05c) 範囲 `[['00b6c05c', '00b6c067']]`
  - `CONDITIONAL_JUMP` [`00b6c064`](#insn-00b6c064) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c064`](#insn-00b6c064) → [`00b6c068`](#insn-00b6c068)
- ブロック [`00b6c068`](#insn-00b6c068) 範囲 `[['00b6c068', '00b6c06f']]`
  - `CONDITIONAL_JUMP` [`00b6c06c`](#insn-00b6c06c) → [`00b6c078`](#insn-00b6c078)
  - `FALL_THROUGH` [`00b6c06c`](#insn-00b6c06c) → [`00b6c070`](#insn-00b6c070)
- ブロック [`00b6c070`](#insn-00b6c070) 範囲 `[['00b6c070', '00b6c077']]`
  - `CONDITIONAL_JUMP` [`00b6c074`](#insn-00b6c074) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c074`](#insn-00b6c074) → [`00b6c078`](#insn-00b6c078)
- ブロック [`00b6c078`](#insn-00b6c078) 範囲 `[['00b6c078', '00b6c07b']]`
  - `CONDITIONAL_JUMP` [`00b6c078`](#insn-00b6c078) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c078`](#insn-00b6c078) → [`00b6c07c`](#insn-00b6c07c)
- ブロック [`00b6c07c`](#insn-00b6c07c) 範囲 `[['00b6c07c', '00b6c087']]`
  - `CONDITIONAL_JUMP` [`00b6c084`](#insn-00b6c084) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c084`](#insn-00b6c084) → [`00b6c088`](#insn-00b6c088)
- ブロック [`00b6c088`](#insn-00b6c088) 範囲 `[['00b6c088', '00b6c08f']]`
  - `CONDITIONAL_JUMP` [`00b6c08c`](#insn-00b6c08c) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c08c`](#insn-00b6c08c) → [`00b6c090`](#insn-00b6c090)
- ブロック [`00b6c090`](#insn-00b6c090) 範囲 `[['00b6c090', '00b6c0a3']]`
  - `CONDITIONAL_JUMP` [`00b6c0a0`](#insn-00b6c0a0) → [`00b6c238`](#insn-00b6c238)
  - `FALL_THROUGH` [`00b6c0a0`](#insn-00b6c0a0) → [`00b6c0a4`](#insn-00b6c0a4)
- ブロック [`00b6c0a4`](#insn-00b6c0a4) 範囲 `[['00b6c0a4', '00b6c0ab']]`
  - `CONDITIONAL_JUMP` [`00b6c0a8`](#insn-00b6c0a8) → [`00b6c0f4`](#insn-00b6c0f4)
  - `FALL_THROUGH` [`00b6c0a8`](#insn-00b6c0a8) → [`00b6c0ac`](#insn-00b6c0ac)
- ブロック [`00b6c0ac`](#insn-00b6c0ac) 範囲 `[['00b6c0ac', '00b6c0b7']]`
  - `CONDITIONAL_JUMP` [`00b6c0b4`](#insn-00b6c0b4) → [`00b6c0d0`](#insn-00b6c0d0)
  - `FALL_THROUGH` [`00b6c0b4`](#insn-00b6c0b4) → [`00b6c0b8`](#insn-00b6c0b8)
- ブロック [`00b6c0b8`](#insn-00b6c0b8) 範囲 `[['00b6c0b8', '00b6c0c3']]`
  - `CONDITIONAL_JUMP` [`00b6c0c0`](#insn-00b6c0c0) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c0c0`](#insn-00b6c0c0) → [`00b6c0c4`](#insn-00b6c0c4)
- ブロック [`00b6c0c4`](#insn-00b6c0c4) 範囲 `[['00b6c0c4', '00b6c0cb']]`
  - `CONDITIONAL_JUMP` [`00b6c0c8`](#insn-00b6c0c8) → [`00b6c0d8`](#insn-00b6c0d8)
  - `FALL_THROUGH` [`00b6c0c8`](#insn-00b6c0c8) → [`00b6c0cc`](#insn-00b6c0cc)
- ブロック [`00b6c0cc`](#insn-00b6c0cc) 範囲 `[['00b6c0cc', '00b6c0cf']]`
  - `UNCONDITIONAL_JUMP` [`00b6c0cc`](#insn-00b6c0cc) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c0d0`](#insn-00b6c0d0) 範囲 `[['00b6c0d0', '00b6c0d7']]`
  - `CONDITIONAL_JUMP` [`00b6c0d4`](#insn-00b6c0d4) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c0d4`](#insn-00b6c0d4) → [`00b6c0d8`](#insn-00b6c0d8)
- ブロック [`00b6c0d8`](#insn-00b6c0d8) 範囲 `[['00b6c0d8', '00b6c0e3']]`
  - `CONDITIONAL_JUMP` [`00b6c0e0`](#insn-00b6c0e0) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c0e0`](#insn-00b6c0e0) → [`00b6c0e4`](#insn-00b6c0e4)
- ブロック [`00b6c0e4`](#insn-00b6c0e4) 範囲 `[['00b6c0e4', '00b6c0f3']]`
  - `CONDITIONAL_JUMP` [`00b6c0f0`](#insn-00b6c0f0) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c0f0`](#insn-00b6c0f0) → [`00b6c0f4`](#insn-00b6c0f4)
- ブロック [`00b6c0f4`](#insn-00b6c0f4) 範囲 `[['00b6c0f4', '00b6c0f7']]`
  - `FALL_THROUGH` [`00b6c0f4`](#insn-00b6c0f4) → [`00b6c0f8`](#insn-00b6c0f8)
- ブロック [`00b6c0f8`](#insn-00b6c0f8) 範囲 `[['00b6c0f8', '00b6c0fb']]`
  - `CONDITIONAL_JUMP` [`00b6c0f8`](#insn-00b6c0f8) → [`00b6c17c`](#insn-00b6c17c)
  - `FALL_THROUGH` [`00b6c0f8`](#insn-00b6c0f8) → [`00b6c0fc`](#insn-00b6c0fc)
- ブロック [`00b6c0fc`](#insn-00b6c0fc) 範囲 `[['00b6c0fc', '00b6c10b']]`
  - `CONDITIONAL_JUMP` [`00b6c108`](#insn-00b6c108) → [`00b6c17c`](#insn-00b6c17c)
  - `FALL_THROUGH` [`00b6c108`](#insn-00b6c108) → [`00b6c10c`](#insn-00b6c10c)
- ブロック [`00b6c10c`](#insn-00b6c10c) 範囲 `[['00b6c10c', '00b6c117']]`
  - `CONDITIONAL_JUMP` [`00b6c114`](#insn-00b6c114) → [`00b6c130`](#insn-00b6c130)
  - `FALL_THROUGH` [`00b6c114`](#insn-00b6c114) → [`00b6c118`](#insn-00b6c118)
- ブロック [`00b6c118`](#insn-00b6c118) 範囲 `[['00b6c118', '00b6c123']]`
  - `CONDITIONAL_JUMP` [`00b6c120`](#insn-00b6c120) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c120`](#insn-00b6c120) → [`00b6c124`](#insn-00b6c124)
- ブロック [`00b6c124`](#insn-00b6c124) 範囲 `[['00b6c124', '00b6c12b']]`
  - `CONDITIONAL_JUMP` [`00b6c128`](#insn-00b6c128) → [`00b6c138`](#insn-00b6c138)
  - `FALL_THROUGH` [`00b6c128`](#insn-00b6c128) → [`00b6c12c`](#insn-00b6c12c)
- ブロック [`00b6c12c`](#insn-00b6c12c) 範囲 `[['00b6c12c', '00b6c12f']]`
  - `UNCONDITIONAL_JUMP` [`00b6c12c`](#insn-00b6c12c) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c130`](#insn-00b6c130) 範囲 `[['00b6c130', '00b6c137']]`
  - `CONDITIONAL_JUMP` [`00b6c134`](#insn-00b6c134) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c134`](#insn-00b6c134) → [`00b6c138`](#insn-00b6c138)
- ブロック [`00b6c138`](#insn-00b6c138) 範囲 `[['00b6c138', '00b6c147']]`
  - `CONDITIONAL_JUMP` [`00b6c144`](#insn-00b6c144) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c144`](#insn-00b6c144) → [`00b6c148`](#insn-00b6c148)
- ブロック [`00b6c148`](#insn-00b6c148) 範囲 `[['00b6c148', '00b6c14b']]`
  - `FALL_THROUGH` [`00b6c148`](#insn-00b6c148) → [`00b6c14c`](#insn-00b6c14c)
- ブロック [`00b6c14c`](#insn-00b6c14c) 範囲 `[['00b6c14c', '00b6c15f']]`
  - `CONDITIONAL_JUMP` [`00b6c15c`](#insn-00b6c15c) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c15c`](#insn-00b6c15c) → [`00b6c160`](#insn-00b6c160)
- ブロック [`00b6c160`](#insn-00b6c160) 範囲 `[['00b6c160', '00b6c167']]`
  - `CONDITIONAL_JUMP` [`00b6c164`](#insn-00b6c164) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c164`](#insn-00b6c164) → [`00b6c168`](#insn-00b6c168)
- ブロック [`00b6c168`](#insn-00b6c168) 範囲 `[['00b6c168', '00b6c173']]`
  - `CONDITIONAL_JUMP` [`00b6c170`](#insn-00b6c170) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c170`](#insn-00b6c170) → [`00b6c174`](#insn-00b6c174)
- ブロック [`00b6c174`](#insn-00b6c174) 範囲 `[['00b6c174', '00b6c17b']]`
  - `CONDITIONAL_JUMP` [`00b6c178`](#insn-00b6c178) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c178`](#insn-00b6c178) → [`00b6c17c`](#insn-00b6c17c)
- ブロック [`00b6c17c`](#insn-00b6c17c) 範囲 `[['00b6c17c', '00b6c183']]`
  - `CONDITIONAL_JUMP` [`00b6c180`](#insn-00b6c180) → [`00b6c238`](#insn-00b6c238)
  - `FALL_THROUGH` [`00b6c180`](#insn-00b6c180) → [`00b6c184`](#insn-00b6c184)
- ブロック [`00b6c184`](#insn-00b6c184) 範囲 `[['00b6c184', '00b6c18b']]`
  - `CONDITIONAL_JUMP` [`00b6c188`](#insn-00b6c188) → [`00b6c1b8`](#insn-00b6c1b8)
  - `FALL_THROUGH` [`00b6c188`](#insn-00b6c188) → [`00b6c18c`](#insn-00b6c18c)
- ブロック [`00b6c18c`](#insn-00b6c18c) 範囲 `[['00b6c18c', '00b6c197']]`
  - `CONDITIONAL_JUMP` [`00b6c194`](#insn-00b6c194) → [`00b6c1b0`](#insn-00b6c1b0)
  - `FALL_THROUGH` [`00b6c194`](#insn-00b6c194) → [`00b6c198`](#insn-00b6c198)
- ブロック [`00b6c198`](#insn-00b6c198) 範囲 `[['00b6c198', '00b6c1a3']]`
  - `CONDITIONAL_JUMP` [`00b6c1a0`](#insn-00b6c1a0) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c1a0`](#insn-00b6c1a0) → [`00b6c1a4`](#insn-00b6c1a4)
- ブロック [`00b6c1a4`](#insn-00b6c1a4) 範囲 `[['00b6c1a4', '00b6c1ab']]`
  - `CONDITIONAL_JUMP` [`00b6c1a8`](#insn-00b6c1a8) → [`00b6c1b8`](#insn-00b6c1b8)
  - `FALL_THROUGH` [`00b6c1a8`](#insn-00b6c1a8) → [`00b6c1ac`](#insn-00b6c1ac)
- ブロック [`00b6c1ac`](#insn-00b6c1ac) 範囲 `[['00b6c1ac', '00b6c1af']]`
  - `UNCONDITIONAL_JUMP` [`00b6c1ac`](#insn-00b6c1ac) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c1b0`](#insn-00b6c1b0) 範囲 `[['00b6c1b0', '00b6c1b7']]`
  - `CONDITIONAL_JUMP` [`00b6c1b4`](#insn-00b6c1b4) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c1b4`](#insn-00b6c1b4) → [`00b6c1b8`](#insn-00b6c1b8)
- ブロック [`00b6c1b8`](#insn-00b6c1b8) 範囲 `[['00b6c1b8', '00b6c1bf']]`
  - `CONDITIONAL_JUMP` [`00b6c1bc`](#insn-00b6c1bc) → [`00b6c238`](#insn-00b6c238)
  - `FALL_THROUGH` [`00b6c1bc`](#insn-00b6c1bc) → [`00b6c1c0`](#insn-00b6c1c0)
- ブロック [`00b6c1c0`](#insn-00b6c1c0) 範囲 `[['00b6c1c0', '00b6c1c7']]`
  - `CONDITIONAL_JUMP` [`00b6c1c4`](#insn-00b6c1c4) → [`00b6c210`](#insn-00b6c210)
  - `FALL_THROUGH` [`00b6c1c4`](#insn-00b6c1c4) → [`00b6c1c8`](#insn-00b6c1c8)
- ブロック [`00b6c1c8`](#insn-00b6c1c8) 範囲 `[['00b6c1c8', '00b6c1d3']]`
  - `CONDITIONAL_JUMP` [`00b6c1d0`](#insn-00b6c1d0) → [`00b6c1ec`](#insn-00b6c1ec)
  - `FALL_THROUGH` [`00b6c1d0`](#insn-00b6c1d0) → [`00b6c1d4`](#insn-00b6c1d4)
- ブロック [`00b6c1d4`](#insn-00b6c1d4) 範囲 `[['00b6c1d4', '00b6c1df']]`
  - `CONDITIONAL_JUMP` [`00b6c1dc`](#insn-00b6c1dc) → [`00b6c24c`](#insn-00b6c24c)
  - `FALL_THROUGH` [`00b6c1dc`](#insn-00b6c1dc) → [`00b6c1e0`](#insn-00b6c1e0)
- ブロック [`00b6c1e0`](#insn-00b6c1e0) 範囲 `[['00b6c1e0', '00b6c1e7']]`
  - `CONDITIONAL_JUMP` [`00b6c1e4`](#insn-00b6c1e4) → [`00b6c1f4`](#insn-00b6c1f4)
  - `FALL_THROUGH` [`00b6c1e4`](#insn-00b6c1e4) → [`00b6c1e8`](#insn-00b6c1e8)
- ブロック [`00b6c1e8`](#insn-00b6c1e8) 範囲 `[['00b6c1e8', '00b6c1eb']]`
  - `UNCONDITIONAL_JUMP` [`00b6c1e8`](#insn-00b6c1e8) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c1ec`](#insn-00b6c1ec) 範囲 `[['00b6c1ec', '00b6c1f3']]`
  - `CONDITIONAL_JUMP` [`00b6c1f0`](#insn-00b6c1f0) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c1f0`](#insn-00b6c1f0) → [`00b6c1f4`](#insn-00b6c1f4)
- ブロック [`00b6c1f4`](#insn-00b6c1f4) 範囲 `[['00b6c1f4', '00b6c1ff']]`
  - `CONDITIONAL_JUMP` [`00b6c1fc`](#insn-00b6c1fc) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c1fc`](#insn-00b6c1fc) → [`00b6c200`](#insn-00b6c200)
- ブロック [`00b6c200`](#insn-00b6c200) 範囲 `[['00b6c200', '00b6c20f']]`
  - `CONDITIONAL_JUMP` [`00b6c20c`](#insn-00b6c20c) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c20c`](#insn-00b6c20c) → [`00b6c210`](#insn-00b6c210)
- ブロック [`00b6c210`](#insn-00b6c210) 範囲 `[['00b6c210', '00b6c217']]`
  - `CONDITIONAL_JUMP` [`00b6c214`](#insn-00b6c214) → [`00b6c238`](#insn-00b6c238)
  - `FALL_THROUGH` [`00b6c214`](#insn-00b6c214) → [`00b6c218`](#insn-00b6c218)
- ブロック [`00b6c218`](#insn-00b6c218) 範囲 `[['00b6c218', '00b6c227']]`
  - `CONDITIONAL_JUMP` [`00b6c224`](#insn-00b6c224) → [`00b6c238`](#insn-00b6c238)
  - `FALL_THROUGH` [`00b6c224`](#insn-00b6c224) → [`00b6c228`](#insn-00b6c228)
- ブロック [`00b6c228`](#insn-00b6c228) 範囲 `[['00b6c228', '00b6c233']]`
  - `CONDITIONAL_JUMP` [`00b6c230`](#insn-00b6c230) → [`00b6c248`](#insn-00b6c248)
  - `FALL_THROUGH` [`00b6c230`](#insn-00b6c230) → [`00b6c234`](#insn-00b6c234)
- ブロック [`00b6c234`](#insn-00b6c234) 範囲 `[['00b6c234', '00b6c237']]`
  - `FALL_THROUGH` [`00b6c234`](#insn-00b6c234) → [`00b6c238`](#insn-00b6c238)
- ブロック [`00b6c238`](#insn-00b6c238) 範囲 `[['00b6c238', '00b6c247']]`
  - `UNCONDITIONAL_JUMP` [`00b6c244`](#insn-00b6c244) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c248`](#insn-00b6c248) 範囲 `[['00b6c248', '00b6c24b']]`
  - `FALL_THROUGH` [`00b6c248`](#insn-00b6c248) → [`00b6c24c`](#insn-00b6c24c)
- ブロック [`00b6c24c`](#insn-00b6c24c) 範囲 `[['00b6c24c', '00b6c25b']]`

## 命令位置別の参照

- [`00b6bfdc`](#insn-00b6bfdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bfe0`](#insn-00b6bfe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bff8`](#insn-00b6bff8) → [`00b6c004`](#insn-00b6c004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c000`](#insn-00b6c000) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c010`](#insn-00b6c010) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c01c`](#insn-00b6c01c) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c03c`](#insn-00b6c03c) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c048`](#insn-00b6c048) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c050`](#insn-00b6c050) → [`00b6c05c`](#insn-00b6c05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c058`](#insn-00b6c058) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c064`](#insn-00b6c064) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c06c`](#insn-00b6c06c) → [`00b6c078`](#insn-00b6c078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c074`](#insn-00b6c074) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c078`](#insn-00b6c078) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c084`](#insn-00b6c084) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c08c`](#insn-00b6c08c) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0a0`](#insn-00b6c0a0) → [`00b6c238`](#insn-00b6c238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0a8`](#insn-00b6c0a8) → [`00b6c0f4`](#insn-00b6c0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0b4`](#insn-00b6c0b4) → [`00b6c0d0`](#insn-00b6c0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0c0`](#insn-00b6c0c0) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0c8`](#insn-00b6c0c8) → [`00b6c0d8`](#insn-00b6c0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0cc`](#insn-00b6c0cc) → [`00b6c24c`](#insn-00b6c24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0d4`](#insn-00b6c0d4) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0e0`](#insn-00b6c0e0) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0f0`](#insn-00b6c0f0) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c0f8`](#insn-00b6c0f8) → [`00b6c17c`](#insn-00b6c17c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c108`](#insn-00b6c108) → [`00b6c17c`](#insn-00b6c17c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c114`](#insn-00b6c114) → [`00b6c130`](#insn-00b6c130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c120`](#insn-00b6c120) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c128`](#insn-00b6c128) → [`00b6c138`](#insn-00b6c138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c12c`](#insn-00b6c12c) → [`00b6c24c`](#insn-00b6c24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c134`](#insn-00b6c134) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c144`](#insn-00b6c144) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c15c`](#insn-00b6c15c) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c164`](#insn-00b6c164) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c170`](#insn-00b6c170) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c178`](#insn-00b6c178) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c180`](#insn-00b6c180) → [`00b6c238`](#insn-00b6c238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c188`](#insn-00b6c188) → [`00b6c1b8`](#insn-00b6c1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c194`](#insn-00b6c194) → [`00b6c1b0`](#insn-00b6c1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1a0`](#insn-00b6c1a0) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1a8`](#insn-00b6c1a8) → [`00b6c1b8`](#insn-00b6c1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1ac`](#insn-00b6c1ac) → [`00b6c24c`](#insn-00b6c24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1b4`](#insn-00b6c1b4) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1bc`](#insn-00b6c1bc) → [`00b6c238`](#insn-00b6c238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1c4`](#insn-00b6c1c4) → [`00b6c210`](#insn-00b6c210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1d0`](#insn-00b6c1d0) → [`00b6c1ec`](#insn-00b6c1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1dc`](#insn-00b6c1dc) → [`00b6c24c`](#insn-00b6c24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1e4`](#insn-00b6c1e4) → [`00b6c1f4`](#insn-00b6c1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1e8`](#insn-00b6c1e8) → [`00b6c24c`](#insn-00b6c24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1f0`](#insn-00b6c1f0) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c1fc`](#insn-00b6c1fc) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c20c`](#insn-00b6c20c) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c214`](#insn-00b6c214) → [`00b6c238`](#insn-00b6c238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c224`](#insn-00b6c224) → [`00b6c238`](#insn-00b6c238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c22c`](#insn-00b6c22c) → [`00c5b560`](../00c5b/00c5b560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b560` · 推定シンボル `None` · 推定型 `None`
- [`00b6c230`](#insn-00b6c230) → [`00b6c248`](#insn-00b6c248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c244`](#insn-00b6c244) → [`00b6c24c`](#insn-00b6c24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6c24c`](#insn-00b6c24c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6bfdc`](#insn-00b6bfdc)

~~~json
{
  "source": "00b6bfdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bfe0`](#insn-00b6bfe0)

~~~json
{
  "source": "00b6bfe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bff8`](#insn-00b6bff8)

~~~json
{
  "source": "00b6bff8",
  "target": "00b6c004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c000`](#insn-00b6c000)

~~~json
{
  "source": "00b6c000",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c010`](#insn-00b6c010)

~~~json
{
  "source": "00b6c010",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c01c`](#insn-00b6c01c)

~~~json
{
  "source": "00b6c01c",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c03c`](#insn-00b6c03c)

~~~json
{
  "source": "00b6c03c",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c048`](#insn-00b6c048)

~~~json
{
  "source": "00b6c048",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c050`](#insn-00b6c050)

~~~json
{
  "source": "00b6c050",
  "target": "00b6c05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c058`](#insn-00b6c058)

~~~json
{
  "source": "00b6c058",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c064`](#insn-00b6c064)

~~~json
{
  "source": "00b6c064",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c06c`](#insn-00b6c06c)

~~~json
{
  "source": "00b6c06c",
  "target": "00b6c078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c074`](#insn-00b6c074)

~~~json
{
  "source": "00b6c074",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c078`](#insn-00b6c078)

~~~json
{
  "source": "00b6c078",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c084`](#insn-00b6c084)

~~~json
{
  "source": "00b6c084",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c08c`](#insn-00b6c08c)

~~~json
{
  "source": "00b6c08c",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0a0`](#insn-00b6c0a0)

~~~json
{
  "source": "00b6c0a0",
  "target": "00b6c238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0a8`](#insn-00b6c0a8)

~~~json
{
  "source": "00b6c0a8",
  "target": "00b6c0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0b4`](#insn-00b6c0b4)

~~~json
{
  "source": "00b6c0b4",
  "target": "00b6c0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0c0`](#insn-00b6c0c0)

~~~json
{
  "source": "00b6c0c0",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0c8`](#insn-00b6c0c8)

~~~json
{
  "source": "00b6c0c8",
  "target": "00b6c0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0cc`](#insn-00b6c0cc)

~~~json
{
  "source": "00b6c0cc",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0d4`](#insn-00b6c0d4)

~~~json
{
  "source": "00b6c0d4",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0e0`](#insn-00b6c0e0)

~~~json
{
  "source": "00b6c0e0",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0f0`](#insn-00b6c0f0)

~~~json
{
  "source": "00b6c0f0",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c0f8`](#insn-00b6c0f8)

~~~json
{
  "source": "00b6c0f8",
  "target": "00b6c17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c108`](#insn-00b6c108)

~~~json
{
  "source": "00b6c108",
  "target": "00b6c17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c114`](#insn-00b6c114)

~~~json
{
  "source": "00b6c114",
  "target": "00b6c130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c120`](#insn-00b6c120)

~~~json
{
  "source": "00b6c120",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c128`](#insn-00b6c128)

~~~json
{
  "source": "00b6c128",
  "target": "00b6c138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c12c`](#insn-00b6c12c)

~~~json
{
  "source": "00b6c12c",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c134`](#insn-00b6c134)

~~~json
{
  "source": "00b6c134",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c144`](#insn-00b6c144)

~~~json
{
  "source": "00b6c144",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c15c`](#insn-00b6c15c)

~~~json
{
  "source": "00b6c15c",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c164`](#insn-00b6c164)

~~~json
{
  "source": "00b6c164",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c170`](#insn-00b6c170)

~~~json
{
  "source": "00b6c170",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c178`](#insn-00b6c178)

~~~json
{
  "source": "00b6c178",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c180`](#insn-00b6c180)

~~~json
{
  "source": "00b6c180",
  "target": "00b6c238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c188`](#insn-00b6c188)

~~~json
{
  "source": "00b6c188",
  "target": "00b6c1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c194`](#insn-00b6c194)

~~~json
{
  "source": "00b6c194",
  "target": "00b6c1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1a0`](#insn-00b6c1a0)

~~~json
{
  "source": "00b6c1a0",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1a8`](#insn-00b6c1a8)

~~~json
{
  "source": "00b6c1a8",
  "target": "00b6c1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1ac`](#insn-00b6c1ac)

~~~json
{
  "source": "00b6c1ac",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1b4`](#insn-00b6c1b4)

~~~json
{
  "source": "00b6c1b4",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1bc`](#insn-00b6c1bc)

~~~json
{
  "source": "00b6c1bc",
  "target": "00b6c238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1c4`](#insn-00b6c1c4)

~~~json
{
  "source": "00b6c1c4",
  "target": "00b6c210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1d0`](#insn-00b6c1d0)

~~~json
{
  "source": "00b6c1d0",
  "target": "00b6c1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1dc`](#insn-00b6c1dc)

~~~json
{
  "source": "00b6c1dc",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1e4`](#insn-00b6c1e4)

~~~json
{
  "source": "00b6c1e4",
  "target": "00b6c1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1e8`](#insn-00b6c1e8)

~~~json
{
  "source": "00b6c1e8",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1f0`](#insn-00b6c1f0)

~~~json
{
  "source": "00b6c1f0",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c1fc`](#insn-00b6c1fc)

~~~json
{
  "source": "00b6c1fc",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c20c`](#insn-00b6c20c)

~~~json
{
  "source": "00b6c20c",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c214`](#insn-00b6c214)

~~~json
{
  "source": "00b6c214",
  "target": "00b6c238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c224`](#insn-00b6c224)

~~~json
{
  "source": "00b6c224",
  "target": "00b6c238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c22c`](#insn-00b6c22c)

~~~json
{
  "source": "00b6c22c",
  "target": "00c5b560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6c230`](#insn-00b6c230)

~~~json
{
  "source": "00b6c230",
  "target": "00b6c248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c244`](#insn-00b6c244)

~~~json
{
  "source": "00b6c244",
  "target": "00b6c24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6c24c`](#insn-00b6c24c)

~~~json
{
  "source": "00b6c24c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
