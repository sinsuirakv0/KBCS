# 00b0beec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0bea8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0bea8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0009.md#compare-1370dee1babc24b3e69ac1d6deb33b64)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0009.md#review-030435116f63f340f0cc1f99deb73c40)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0beec",
  "name": "_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers8VerifierE",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a696791560a42c2f1a2c2410912a77ee73931d2b907f877b1c2efe71954bcb23",
  "source_text_sha256": "a696791560a42c2f1a2c2410912a77ee73931d2b907f877b1c2efe71954bcb23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0beec",
        "00b0c14b"
      ]
    ],
    "bytes_sha256": "9f49fa3bf6754aead63173cb4091330bcdb8c5b6a1dcc8fee4542ab9395c171c",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdead0](../00bde/00bdead0.md)

## 呼び出し先

- [00bdeac0](../00bde/00bdeac0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4924 bytes

~~~c

undefined4
_ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers8VerifierE(int *param_1,long *param_2)

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
                    /* try { // try from 00b0bf04 to 00c0bf0f has its CatchHandler @ 00b0c320 */
  if (((uVar9 & 3) == 0) || ((char)param_2[5] == '\0')) {
                    /* try { // try from 00b0bf10 to 00c0bf1b has its CatchHandler @ 00b0c304 */
    uVar8 = param_2[1];
                    /* try { // try from 00b0bf1c to 00c0bf2b has its CatchHandler @ 00b0c2f0 */
    if (uVar8 < 5) {
      return 0;
    }
    uVar10 = uVar8 - 4;
    if (uVar10 < uVar9) {
      return 0;
    }
                    /* try { // try from 00b0bf2c to 00c0bf77 has its CatchHandler @ 00b0bea4 */
    iVar5 = *param_1;
    uVar6 = (int)param_2[2] + 1;
    uVar1 = (int)param_2[3] + 1;
    *(uint *)(param_2 + 2) = uVar6;
    *(uint *)(param_2 + 3) = uVar1;
                    /* try { // try from 00b0bf78 to 00c0bf87 has its CatchHandler @ 00b0c2e8 */
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
        if ((ulong)puVar12[2] != 0) {
          uVar11 = uVar9 + puVar12[2];
          if ((uVar11 & 3) == 0) {
                    /* try { // try from 00b0bff4 to 00c0c00b has its CatchHandler @ 00b0c324 */
            if (uVar10 < uVar11) {
              return 0;
            }
          }
          else {
                    /* try { // try from 00b0bfd8 to 00c0bfdf has its CatchHandler @ 00b0c328 */
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
                    /* try { // try from 00b0c080 to 00c0c087 has its CatchHandler @ 00b0c338 */
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
          if (((ulong)puVar12[3] != 0) && (uVar10 < uVar9 + puVar12[3])) {
            return 0;
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
              if (uVar8 - 1 < uVar9 + *(uint *)(lVar7 + uVar9)) {
                return 0;
              }
            }
            if (((ulong)puVar12[4] != 0) &&
               (puVar3 = (uint *)((long)param_1 + (ulong)puVar12[4]),
               lVar7 = (long)puVar3 + (ulong)*puVar3, lVar7 != 0)) {
              uVar9 = _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE(lVar7);
              if ((uVar9 & 1) == 0) {
                return 0;
              }
              uVar6 = *(uint *)(param_2 + 2);
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
<a id="insn-00b0beec"></a> `00b0beec` | `ff 83 00 d1` | sub sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b0bef0"></a> `00b0bef0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bef4"></a> `00b0bef4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0bef8"></a> `00b0bef8` | `2a 00 40 f9` | ldr x10,[x1] | `FALL_THROUGH`
<a id="insn-00b0befc"></a> `00b0befc` | `0c 00 0a cb` | sub x12,x0,x10 | `FALL_THROUGH`
<a id="insn-00b0bf00"></a> `00b0bf00` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bf04"></a> `00b0bf04` | `60 00 00 54` | b.eq 0x00b0bf10 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf08"></a> `00b0bf08` | `28 a0 40 39` | ldrb w8,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bf0c"></a> `00b0bf0c` | `e8 03 00 35` | cbnz w8,0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf10"></a> `00b0bf10` | `2b 04 40 f9` | ldr x11,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b0bf14"></a> `00b0bf14` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bf18"></a> `00b0bf18` | `7f 15 00 f1` | cmp x11,#0x5 | `FALL_THROUGH`
<a id="insn-00b0bf1c"></a> `00b0bf1c` | `83 03 00 54` | b.cc 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0bf20"></a> `00b0bf20` | `6d 11 00 d1` | sub x13,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00b0bf24"></a> `00b0bf24` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0bf28"></a> `00b0bf28` | `23 03 00 54` | b.cc 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0bf2c"></a> `00b0bf2c` | `29 3c 42 29` | ldp w9,w15,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bf30"></a> `00b0bf30` | `2e 18 40 b9` | ldr w14,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b0bf34"></a> `00b0bf34` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0bf38"></a> `00b0bf38` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bf3c"></a> `00b0bf3c` | `ce 05 00 11` | add w14,w14,#0x1 | `FALL_THROUGH`
<a id="insn-00b0bf40"></a> `00b0bf40` | `3f 01 0f 6b` | cmp w9,w15 | `FALL_THROUGH`
<a id="insn-00b0bf44"></a> `00b0bf44` | `29 10 00 b9` | str w9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bf48"></a> `00b0bf48` | `2e 18 00 b9` | str w14,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00b0bf4c"></a> `00b0bf4c` | `e8 01 00 54` | b.hi 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf50"></a> `00b0bf50` | `2f 1c 40 b9` | ldr w15,[x1, #0x1c] | `FALL_THROUGH`
<a id="insn-00b0bf54"></a> `00b0bf54` | `df 01 0f 6b` | cmp w14,w15 | `FALL_THROUGH`
<a id="insn-00b0bf58"></a> `00b0bf58` | `88 01 00 54` | b.hi 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf5c"></a> `00b0bf5c` | `8e 01 08 cb` | sub x14,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bf60"></a> `00b0bf60` | `6e 00 00 36` | tbz w14,#0x0,0x00b0bf6c | `CONDITIONAL_JUMP`
<a id="insn-00b0bf64"></a> `00b0bf64` | `28 a0 40 39` | ldrb w8,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bf68"></a> `00b0bf68` | `08 01 00 35` | cbnz w8,0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf6c"></a> `00b0bf6c` | `68 09 00 d1` | sub x8,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b0bf70"></a> `00b0bf70` | `1f 01 0e eb` | cmp x8,x14 | `FALL_THROUGH`
<a id="insn-00b0bf74"></a> `00b0bf74` | `a3 00 00 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bf78"></a> `00b0bf78` | `48 69 6e 78` | ldrh w8,[x10, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0bf7c"></a> `00b0bf7c` | `08 01 00 36` | tbz w8,#0x0,0x00b0bf9c | `CONDITIONAL_JUMP`
<a id="insn-00b0bf80"></a> `00b0bf80` | `2f a0 40 39` | ldrb w15,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bf84"></a> `00b0bf84` | `cf 00 00 34` | cbz w15,0x00b0bf9c | `CONDITIONAL_JUMP`
<a id="insn-00b0bf88"></a> `00b0bf88` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bf8c"></a> `00b0bf8c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0bf90"></a> `00b0bf90` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-00b0bf94"></a> `00b0bf94` | `ff 83 00 91` | add sp,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b0bf98"></a> `00b0bf98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0bf9c"></a> `00b0bf9c` | `6f 01 08 eb` | subs x15,x11,x8 | `FALL_THROUGH`
<a id="insn-00b0bfa0"></a> `00b0bfa0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bfa4"></a> `00b0bfa4` | `49 ff ff 54` | b.ls 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0bfa8"></a> `00b0bfa8` | `ff 01 0e eb` | cmp x15,x14 | `FALL_THROUGH`
<a id="insn-00b0bfac"></a> `00b0bfac` | `03 ff ff 54` | b.cc 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0bfb0"></a> `00b0bfb0` | `08 00 80 b9` | ldrsw x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0bfb4"></a> `00b0bfb4` | `0e 00 08 cb` | sub x14,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0bfb8"></a> `00b0bfb8` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00b0bfbc"></a> `00b0bfbc` | `ff 15 00 71` | cmp w15,#0x5 | `FALL_THROUGH`
<a id="insn-00b0bfc0"></a> `00b0bfc0` | `e3 0b 00 54` | b.cc 0x00b0c13c | `CONDITIONAL_JUMP`
<a id="insn-00b0bfc4"></a> `00b0bfc4` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b0bfc8"></a> `00b0bfc8` | `68 02 00 b4` | cbz x8,0x00b0c014 | `CONDITIONAL_JUMP`
<a id="insn-00b0bfcc"></a> `00b0bfcc` | `90 01 08 8b` | add x16,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0bfd0"></a> `00b0bfd0` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0bfd4"></a> `00b0bfd4` | `e0 00 00 54` | b.eq 0x00b0bff0 | `CONDITIONAL_JUMP`
<a id="insn-00b0bfd8"></a> `00b0bfd8` | `31 a0 40 39` | ldrb w17,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0bfdc"></a> `00b0bfdc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0bfe0"></a> `00b0bfe0` | `71 fd ff 35` | cbnz w17,0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0bfe4"></a> `00b0bfe4` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bfe8"></a> `00b0bfe8` | `82 00 00 54` | b.cs 0x00b0bff8 | `CONDITIONAL_JUMP`
<a id="insn-00b0bfec"></a> `00b0bfec` | `e8 ff ff 17` | b 0x00b0bf8c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0bff0"></a> `00b0bff0` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0bff4"></a> `00b0bff4` | `a3 fc ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0bff8"></a> `00b0bff8` | `48 69 70 b8` | ldr w8,[x10, x16, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0bffc"></a> `00b0bffc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c000"></a> `00b0c000` | `4b fc ff 54` | b.lt 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c004"></a> `00b0c004` | `08 02 08 8b` | add x8,x16,x8 | `FALL_THROUGH`
<a id="insn-00b0c008"></a> `00b0c008` | `70 05 00 d1` | sub x16,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c00c"></a> `00b0c00c` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00b0c010"></a> `00b0c010` | `c3 fb ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c014"></a> `00b0c014` | `c8 09 40 79` | ldrh w8,[x14, #0x4] | `FALL_THROUGH`
<a id="insn-00b0c018"></a> `00b0c018` | `28 04 00 b4` | cbz x8,0x00b0c09c | `CONDITIONAL_JUMP`
<a id="insn-00b0c01c"></a> `00b0c01c` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0c020"></a> `00b0c020` | `10 01 40 b9` | ldr w16,[x8] | `FALL_THROUGH`
<a id="insn-00b0c024"></a> `00b0c024` | `11 01 10 ab` | adds x17,x8,x16 | `FALL_THROUGH`
<a id="insn-00b0c028"></a> `00b0c028` | `a0 03 00 54` | b.eq 0x00b0c09c | `CONDITIONAL_JUMP`
<a id="insn-00b0c02c"></a> `00b0c02c` | `30 02 0a cb` | sub x16,x17,x10 | `FALL_THROUGH`
<a id="insn-00b0c030"></a> `00b0c030` | `1f 06 40 f2` | tst x16,#0x3 | `FALL_THROUGH`
<a id="insn-00b0c034"></a> `00b0c034` | `e0 00 00 54` | b.eq 0x00b0c050 | `CONDITIONAL_JUMP`
<a id="insn-00b0c038"></a> `00b0c038` | `22 a0 40 39` | ldrb w2,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0c03c"></a> `00b0c03c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0c040"></a> `00b0c040` | `62 fa ff 35` | cbnz w2,0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0c044"></a> `00b0c044` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0c048"></a> `00b0c048` | `82 00 00 54` | b.cs 0x00b0c058 | `CONDITIONAL_JUMP`
<a id="insn-00b0c04c"></a> `00b0c04c` | `d0 ff ff 17` | b 0x00b0bf8c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0c050"></a> `00b0c050` | `bf 01 10 eb` | cmp x13,x16 | `FALL_THROUGH`
<a id="insn-00b0c054"></a> `00b0c054` | `a3 f9 ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c058"></a> `00b0c058` | `28 02 40 b9` | ldr w8,[x17] | `FALL_THROUGH`
<a id="insn-00b0c05c"></a> `00b0c05c` | `f1 77 1f 32` | orr w17,wzr,#0x7ffffffe | `FALL_THROUGH`
<a id="insn-00b0c060"></a> `00b0c060` | `1f 01 11 6b` | cmp w8,w17 | `FALL_THROUGH`
<a id="insn-00b0c064"></a> `00b0c064` | `28 f9 ff 54` | b.hi 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c068"></a> `00b0c068` | `02 11 00 91` | add x2,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b0c06c"></a> `00b0c06c` | `51 00 10 8b` | add x17,x2,x16 | `FALL_THROUGH`
<a id="insn-00b0c070"></a> `00b0c070` | `68 05 00 d1` | sub x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c074"></a> `00b0c074` | `1f 01 11 eb` | cmp x8,x17 | `FALL_THROUGH`
<a id="insn-00b0c078"></a> `00b0c078` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0c07c"></a> `00b0c07c` | `83 f8 ff 54` | b.cc 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0c080"></a> `00b0c080` | `7f 01 02 eb` | cmp x11,x2 | `FALL_THROUGH`
<a id="insn-00b0c084"></a> `00b0c084` | `49 f8 ff 54` | b.ls 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0c088"></a> `00b0c088` | `62 01 02 cb` | sub x2,x11,x2 | `FALL_THROUGH`
<a id="insn-00b0c08c"></a> `00b0c08c` | `5f 00 10 eb` | cmp x2,x16 | `FALL_THROUGH`
<a id="insn-00b0c090"></a> `00b0c090` | `e3 f7 ff 54` | b.cc 0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0c094"></a> `00b0c094` | `48 69 71 38` | ldrb w8,[x10, x17, LSL ] | `FALL_THROUGH`
<a id="insn-00b0c098"></a> `00b0c098` | `88 f7 ff 35` | cbnz w8,0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c09c"></a> `00b0c09c` | `ff 1d 00 71` | cmp w15,#0x7 | `FALL_THROUGH`
<a id="insn-00b0c0a0"></a> `00b0c0a0` | `e3 04 00 54` | b.cc 0x00b0c13c | `CONDITIONAL_JUMP`
<a id="insn-00b0c0a4"></a> `00b0c0a4` | `c8 0d 40 79` | ldrh w8,[x14, #0x6] | `FALL_THROUGH`
<a id="insn-00b0c0a8"></a> `00b0c0a8` | `88 00 00 b4` | cbz x8,0x00b0c0b8 | `CONDITIONAL_JUMP`
<a id="insn-00b0c0ac"></a> `00b0c0ac` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0c0b0"></a> `00b0c0b0` | `bf 01 08 eb` | cmp x13,x8 | `FALL_THROUGH`
<a id="insn-00b0c0b4"></a> `00b0c0b4` | `a3 f6 ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c0b8"></a> `00b0c0b8` | `ff 25 00 71` | cmp w15,#0x9 | `FALL_THROUGH`
<a id="insn-00b0c0bc"></a> `00b0c0bc` | `03 04 00 54` | b.cc 0x00b0c13c | `CONDITIONAL_JUMP`
<a id="insn-00b0c0c0"></a> `00b0c0c0` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b0c0c4"></a> `00b0c0c4` | `68 02 00 b4` | cbz x8,0x00b0c110 | `CONDITIONAL_JUMP`
<a id="insn-00b0c0c8"></a> `00b0c0c8` | `8c 01 08 8b` | add x12,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0c0cc"></a> `00b0c0cc` | `9f 05 40 f2` | tst x12,#0x3 | `FALL_THROUGH`
<a id="insn-00b0c0d0"></a> `00b0c0d0` | `e0 00 00 54` | b.eq 0x00b0c0ec | `CONDITIONAL_JUMP`
<a id="insn-00b0c0d4"></a> `00b0c0d4` | `2f a0 40 39` | ldrb w15,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00b0c0d8"></a> `00b0c0d8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00b0c0dc"></a> `00b0c0dc` | `8f f5 ff 35` | cbnz w15,0x00b0bf8c | `CONDITIONAL_JUMP`
<a id="insn-00b0c0e0"></a> `00b0c0e0` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0c0e4"></a> `00b0c0e4` | `82 00 00 54` | b.cs 0x00b0c0f4 | `CONDITIONAL_JUMP`
<a id="insn-00b0c0e8"></a> `00b0c0e8` | `a9 ff ff 17` | b 0x00b0bf8c | `UNCONDITIONAL_JUMP`
<a id="insn-00b0c0ec"></a> `00b0c0ec` | `bf 01 0c eb` | cmp x13,x12 | `FALL_THROUGH`
<a id="insn-00b0c0f0"></a> `00b0c0f0` | `c3 f4 ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c0f4"></a> `00b0c0f4` | `48 69 6c b8` | ldr w8,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b0c0f8"></a> `00b0c0f8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c0fc"></a> `00b0c0fc` | `6b f4 ff 54` | b.lt 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c100"></a> `00b0c100` | `88 01 08 8b` | add x8,x12,x8 | `FALL_THROUGH`
<a id="insn-00b0c104"></a> `00b0c104` | `6a 05 00 d1` | sub x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c108"></a> `00b0c108` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00b0c10c"></a> `00b0c10c` | `e3 f3 ff 54` | b.cc 0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c110"></a> `00b0c110` | `c8 11 40 79` | ldrh w8,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-00b0c114"></a> `00b0c114` | `48 01 00 b4` | cbz x8,0x00b0c13c | `CONDITIONAL_JUMP`
<a id="insn-00b0c118"></a> `00b0c118` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0c11c"></a> `00b0c11c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b0c120"></a> `00b0c120` | `00 01 0a ab` | adds x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b0c124"></a> `00b0c124` | `c0 00 00 54` | b.eq 0x00b0c13c | `CONDITIONAL_JUMP`
<a id="insn-00b0c128"></a> `00b0c128` | `e1 07 00 f9` | str x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0c12c"></a> `00b0c12c` | `65 4a 03 94` | bl 0x00bdeac0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0c130"></a> `00b0c130` | `c0 f2 07 36` | tbz w0,#0x0,0x00b0bf88 | `CONDITIONAL_JUMP`
<a id="insn-00b0c134"></a> `00b0c134` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0c138"></a> `00b0c138` | `29 10 40 b9` | ldr w9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0c13c"></a> `00b0c13c` | `28 05 00 51` | sub w8,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c140"></a> `00b0c140` | `28 10 00 b9` | str w8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b0c144"></a> `00b0c144` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0c148"></a> `00b0c148` | `91 ff ff 17` | b 0x00b0bf8c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b0beec`](#insn-00b0beec) 範囲 `[['00b0beec', '00b0bf03']]`
  - `FALL_THROUGH` [`00b0bf00`](#insn-00b0bf00) → [`00b0bf04`](#insn-00b0bf04)
- ブロック [`00b0bf04`](#insn-00b0bf04) 範囲 `[['00b0bf04', '00b0bf07']]`
  - `CONDITIONAL_JUMP` [`00b0bf04`](#insn-00b0bf04) → [`00b0bf10`](#insn-00b0bf10)
  - `FALL_THROUGH` [`00b0bf04`](#insn-00b0bf04) → [`00b0bf08`](#insn-00b0bf08)
- ブロック [`00b0bf08`](#insn-00b0bf08) 範囲 `[['00b0bf08', '00b0bf0f']]`
  - `CONDITIONAL_JUMP` [`00b0bf0c`](#insn-00b0bf0c) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bf0c`](#insn-00b0bf0c) → [`00b0bf10`](#insn-00b0bf10)
- ブロック [`00b0bf10`](#insn-00b0bf10) 範囲 `[['00b0bf10', '00b0bf1b']]`
  - `FALL_THROUGH` [`00b0bf18`](#insn-00b0bf18) → [`00b0bf1c`](#insn-00b0bf1c)
- ブロック [`00b0bf1c`](#insn-00b0bf1c) 範囲 `[['00b0bf1c', '00b0bf1f']]`
  - `CONDITIONAL_JUMP` [`00b0bf1c`](#insn-00b0bf1c) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0bf1c`](#insn-00b0bf1c) → [`00b0bf20`](#insn-00b0bf20)
- ブロック [`00b0bf20`](#insn-00b0bf20) 範囲 `[['00b0bf20', '00b0bf2b']]`
  - `CONDITIONAL_JUMP` [`00b0bf28`](#insn-00b0bf28) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0bf28`](#insn-00b0bf28) → [`00b0bf2c`](#insn-00b0bf2c)
- ブロック [`00b0bf2c`](#insn-00b0bf2c) 範囲 `[['00b0bf2c', '00b0bf4f']]`
  - `CONDITIONAL_JUMP` [`00b0bf4c`](#insn-00b0bf4c) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bf4c`](#insn-00b0bf4c) → [`00b0bf50`](#insn-00b0bf50)
- ブロック [`00b0bf50`](#insn-00b0bf50) 範囲 `[['00b0bf50', '00b0bf5b']]`
  - `CONDITIONAL_JUMP` [`00b0bf58`](#insn-00b0bf58) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bf58`](#insn-00b0bf58) → [`00b0bf5c`](#insn-00b0bf5c)
- ブロック [`00b0bf5c`](#insn-00b0bf5c) 範囲 `[['00b0bf5c', '00b0bf63']]`
  - `CONDITIONAL_JUMP` [`00b0bf60`](#insn-00b0bf60) → [`00b0bf6c`](#insn-00b0bf6c)
  - `FALL_THROUGH` [`00b0bf60`](#insn-00b0bf60) → [`00b0bf64`](#insn-00b0bf64)
- ブロック [`00b0bf64`](#insn-00b0bf64) 範囲 `[['00b0bf64', '00b0bf6b']]`
  - `CONDITIONAL_JUMP` [`00b0bf68`](#insn-00b0bf68) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bf68`](#insn-00b0bf68) → [`00b0bf6c`](#insn-00b0bf6c)
- ブロック [`00b0bf6c`](#insn-00b0bf6c) 範囲 `[['00b0bf6c', '00b0bf77']]`
  - `CONDITIONAL_JUMP` [`00b0bf74`](#insn-00b0bf74) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bf74`](#insn-00b0bf74) → [`00b0bf78`](#insn-00b0bf78)
- ブロック [`00b0bf78`](#insn-00b0bf78) 範囲 `[['00b0bf78', '00b0bf7f']]`
  - `CONDITIONAL_JUMP` [`00b0bf7c`](#insn-00b0bf7c) → [`00b0bf9c`](#insn-00b0bf9c)
  - `FALL_THROUGH` [`00b0bf7c`](#insn-00b0bf7c) → [`00b0bf80`](#insn-00b0bf80)
- ブロック [`00b0bf80`](#insn-00b0bf80) 範囲 `[['00b0bf80', '00b0bf87']]`
  - `CONDITIONAL_JUMP` [`00b0bf84`](#insn-00b0bf84) → [`00b0bf9c`](#insn-00b0bf9c)
  - `FALL_THROUGH` [`00b0bf84`](#insn-00b0bf84) → [`00b0bf88`](#insn-00b0bf88)
- ブロック [`00b0bf88`](#insn-00b0bf88) 範囲 `[['00b0bf88', '00b0bf8b']]`
  - `FALL_THROUGH` [`00b0bf88`](#insn-00b0bf88) → [`00b0bf8c`](#insn-00b0bf8c)
- ブロック [`00b0bf8c`](#insn-00b0bf8c) 範囲 `[['00b0bf8c', '00b0bf9b']]`
- ブロック [`00b0bf9c`](#insn-00b0bf9c) 範囲 `[['00b0bf9c', '00b0bfa7']]`
  - `CONDITIONAL_JUMP` [`00b0bfa4`](#insn-00b0bfa4) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0bfa4`](#insn-00b0bfa4) → [`00b0bfa8`](#insn-00b0bfa8)
- ブロック [`00b0bfa8`](#insn-00b0bfa8) 範囲 `[['00b0bfa8', '00b0bfaf']]`
  - `CONDITIONAL_JUMP` [`00b0bfac`](#insn-00b0bfac) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0bfac`](#insn-00b0bfac) → [`00b0bfb0`](#insn-00b0bfb0)
- ブロック [`00b0bfb0`](#insn-00b0bfb0) 範囲 `[['00b0bfb0', '00b0bfc3']]`
  - `CONDITIONAL_JUMP` [`00b0bfc0`](#insn-00b0bfc0) → [`00b0c13c`](#insn-00b0c13c)
  - `FALL_THROUGH` [`00b0bfc0`](#insn-00b0bfc0) → [`00b0bfc4`](#insn-00b0bfc4)
- ブロック [`00b0bfc4`](#insn-00b0bfc4) 範囲 `[['00b0bfc4', '00b0bfcb']]`
  - `CONDITIONAL_JUMP` [`00b0bfc8`](#insn-00b0bfc8) → [`00b0c014`](#insn-00b0c014)
  - `FALL_THROUGH` [`00b0bfc8`](#insn-00b0bfc8) → [`00b0bfcc`](#insn-00b0bfcc)
- ブロック [`00b0bfcc`](#insn-00b0bfcc) 範囲 `[['00b0bfcc', '00b0bfd7']]`
  - `CONDITIONAL_JUMP` [`00b0bfd4`](#insn-00b0bfd4) → [`00b0bff0`](#insn-00b0bff0)
  - `FALL_THROUGH` [`00b0bfd4`](#insn-00b0bfd4) → [`00b0bfd8`](#insn-00b0bfd8)
- ブロック [`00b0bfd8`](#insn-00b0bfd8) 範囲 `[['00b0bfd8', '00b0bfe3']]`
  - `CONDITIONAL_JUMP` [`00b0bfe0`](#insn-00b0bfe0) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0bfe0`](#insn-00b0bfe0) → [`00b0bfe4`](#insn-00b0bfe4)
- ブロック [`00b0bfe4`](#insn-00b0bfe4) 範囲 `[['00b0bfe4', '00b0bfeb']]`
  - `CONDITIONAL_JUMP` [`00b0bfe8`](#insn-00b0bfe8) → [`00b0bff8`](#insn-00b0bff8)
  - `FALL_THROUGH` [`00b0bfe8`](#insn-00b0bfe8) → [`00b0bfec`](#insn-00b0bfec)
- ブロック [`00b0bfec`](#insn-00b0bfec) 範囲 `[['00b0bfec', '00b0bfef']]`
  - `UNCONDITIONAL_JUMP` [`00b0bfec`](#insn-00b0bfec) → [`00b0bf8c`](#insn-00b0bf8c)
- ブロック [`00b0bff0`](#insn-00b0bff0) 範囲 `[['00b0bff0', '00b0bff3']]`
  - `FALL_THROUGH` [`00b0bff0`](#insn-00b0bff0) → [`00b0bff4`](#insn-00b0bff4)
- ブロック [`00b0bff4`](#insn-00b0bff4) 範囲 `[['00b0bff4', '00b0bff7']]`
  - `CONDITIONAL_JUMP` [`00b0bff4`](#insn-00b0bff4) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0bff4`](#insn-00b0bff4) → [`00b0bff8`](#insn-00b0bff8)
- ブロック [`00b0bff8`](#insn-00b0bff8) 範囲 `[['00b0bff8', '00b0c003']]`
  - `CONDITIONAL_JUMP` [`00b0c000`](#insn-00b0c000) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c000`](#insn-00b0c000) → [`00b0c004`](#insn-00b0c004)
- ブロック [`00b0c004`](#insn-00b0c004) 範囲 `[['00b0c004', '00b0c013']]`
  - `CONDITIONAL_JUMP` [`00b0c010`](#insn-00b0c010) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c010`](#insn-00b0c010) → [`00b0c014`](#insn-00b0c014)
- ブロック [`00b0c014`](#insn-00b0c014) 範囲 `[['00b0c014', '00b0c01b']]`
  - `CONDITIONAL_JUMP` [`00b0c018`](#insn-00b0c018) → [`00b0c09c`](#insn-00b0c09c)
  - `FALL_THROUGH` [`00b0c018`](#insn-00b0c018) → [`00b0c01c`](#insn-00b0c01c)
- ブロック [`00b0c01c`](#insn-00b0c01c) 範囲 `[['00b0c01c', '00b0c02b']]`
  - `CONDITIONAL_JUMP` [`00b0c028`](#insn-00b0c028) → [`00b0c09c`](#insn-00b0c09c)
  - `FALL_THROUGH` [`00b0c028`](#insn-00b0c028) → [`00b0c02c`](#insn-00b0c02c)
- ブロック [`00b0c02c`](#insn-00b0c02c) 範囲 `[['00b0c02c', '00b0c037']]`
  - `CONDITIONAL_JUMP` [`00b0c034`](#insn-00b0c034) → [`00b0c050`](#insn-00b0c050)
  - `FALL_THROUGH` [`00b0c034`](#insn-00b0c034) → [`00b0c038`](#insn-00b0c038)
- ブロック [`00b0c038`](#insn-00b0c038) 範囲 `[['00b0c038', '00b0c043']]`
  - `CONDITIONAL_JUMP` [`00b0c040`](#insn-00b0c040) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0c040`](#insn-00b0c040) → [`00b0c044`](#insn-00b0c044)
- ブロック [`00b0c044`](#insn-00b0c044) 範囲 `[['00b0c044', '00b0c04b']]`
  - `CONDITIONAL_JUMP` [`00b0c048`](#insn-00b0c048) → [`00b0c058`](#insn-00b0c058)
  - `FALL_THROUGH` [`00b0c048`](#insn-00b0c048) → [`00b0c04c`](#insn-00b0c04c)
- ブロック [`00b0c04c`](#insn-00b0c04c) 範囲 `[['00b0c04c', '00b0c04f']]`
  - `UNCONDITIONAL_JUMP` [`00b0c04c`](#insn-00b0c04c) → [`00b0bf8c`](#insn-00b0bf8c)
- ブロック [`00b0c050`](#insn-00b0c050) 範囲 `[['00b0c050', '00b0c057']]`
  - `CONDITIONAL_JUMP` [`00b0c054`](#insn-00b0c054) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c054`](#insn-00b0c054) → [`00b0c058`](#insn-00b0c058)
- ブロック [`00b0c058`](#insn-00b0c058) 範囲 `[['00b0c058', '00b0c067']]`
  - `CONDITIONAL_JUMP` [`00b0c064`](#insn-00b0c064) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c064`](#insn-00b0c064) → [`00b0c068`](#insn-00b0c068)
- ブロック [`00b0c068`](#insn-00b0c068) 範囲 `[['00b0c068', '00b0c07f']]`
  - `CONDITIONAL_JUMP` [`00b0c07c`](#insn-00b0c07c) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0c07c`](#insn-00b0c07c) → [`00b0c080`](#insn-00b0c080)
- ブロック [`00b0c080`](#insn-00b0c080) 範囲 `[['00b0c080', '00b0c087']]`
  - `CONDITIONAL_JUMP` [`00b0c084`](#insn-00b0c084) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0c084`](#insn-00b0c084) → [`00b0c088`](#insn-00b0c088)
- ブロック [`00b0c088`](#insn-00b0c088) 範囲 `[['00b0c088', '00b0c093']]`
  - `CONDITIONAL_JUMP` [`00b0c090`](#insn-00b0c090) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0c090`](#insn-00b0c090) → [`00b0c094`](#insn-00b0c094)
- ブロック [`00b0c094`](#insn-00b0c094) 範囲 `[['00b0c094', '00b0c09b']]`
  - `CONDITIONAL_JUMP` [`00b0c098`](#insn-00b0c098) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c098`](#insn-00b0c098) → [`00b0c09c`](#insn-00b0c09c)
- ブロック [`00b0c09c`](#insn-00b0c09c) 範囲 `[['00b0c09c', '00b0c0a3']]`
  - `CONDITIONAL_JUMP` [`00b0c0a0`](#insn-00b0c0a0) → [`00b0c13c`](#insn-00b0c13c)
  - `FALL_THROUGH` [`00b0c0a0`](#insn-00b0c0a0) → [`00b0c0a4`](#insn-00b0c0a4)
- ブロック [`00b0c0a4`](#insn-00b0c0a4) 範囲 `[['00b0c0a4', '00b0c0ab']]`
  - `CONDITIONAL_JUMP` [`00b0c0a8`](#insn-00b0c0a8) → [`00b0c0b8`](#insn-00b0c0b8)
  - `FALL_THROUGH` [`00b0c0a8`](#insn-00b0c0a8) → [`00b0c0ac`](#insn-00b0c0ac)
- ブロック [`00b0c0ac`](#insn-00b0c0ac) 範囲 `[['00b0c0ac', '00b0c0b7']]`
  - `CONDITIONAL_JUMP` [`00b0c0b4`](#insn-00b0c0b4) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c0b4`](#insn-00b0c0b4) → [`00b0c0b8`](#insn-00b0c0b8)
- ブロック [`00b0c0b8`](#insn-00b0c0b8) 範囲 `[['00b0c0b8', '00b0c0bf']]`
  - `CONDITIONAL_JUMP` [`00b0c0bc`](#insn-00b0c0bc) → [`00b0c13c`](#insn-00b0c13c)
  - `FALL_THROUGH` [`00b0c0bc`](#insn-00b0c0bc) → [`00b0c0c0`](#insn-00b0c0c0)
- ブロック [`00b0c0c0`](#insn-00b0c0c0) 範囲 `[['00b0c0c0', '00b0c0c7']]`
  - `CONDITIONAL_JUMP` [`00b0c0c4`](#insn-00b0c0c4) → [`00b0c110`](#insn-00b0c110)
  - `FALL_THROUGH` [`00b0c0c4`](#insn-00b0c0c4) → [`00b0c0c8`](#insn-00b0c0c8)
- ブロック [`00b0c0c8`](#insn-00b0c0c8) 範囲 `[['00b0c0c8', '00b0c0d3']]`
  - `CONDITIONAL_JUMP` [`00b0c0d0`](#insn-00b0c0d0) → [`00b0c0ec`](#insn-00b0c0ec)
  - `FALL_THROUGH` [`00b0c0d0`](#insn-00b0c0d0) → [`00b0c0d4`](#insn-00b0c0d4)
- ブロック [`00b0c0d4`](#insn-00b0c0d4) 範囲 `[['00b0c0d4', '00b0c0df']]`
  - `CONDITIONAL_JUMP` [`00b0c0dc`](#insn-00b0c0dc) → [`00b0bf8c`](#insn-00b0bf8c)
  - `FALL_THROUGH` [`00b0c0dc`](#insn-00b0c0dc) → [`00b0c0e0`](#insn-00b0c0e0)
- ブロック [`00b0c0e0`](#insn-00b0c0e0) 範囲 `[['00b0c0e0', '00b0c0e7']]`
  - `CONDITIONAL_JUMP` [`00b0c0e4`](#insn-00b0c0e4) → [`00b0c0f4`](#insn-00b0c0f4)
  - `FALL_THROUGH` [`00b0c0e4`](#insn-00b0c0e4) → [`00b0c0e8`](#insn-00b0c0e8)
- ブロック [`00b0c0e8`](#insn-00b0c0e8) 範囲 `[['00b0c0e8', '00b0c0eb']]`
  - `UNCONDITIONAL_JUMP` [`00b0c0e8`](#insn-00b0c0e8) → [`00b0bf8c`](#insn-00b0bf8c)
- ブロック [`00b0c0ec`](#insn-00b0c0ec) 範囲 `[['00b0c0ec', '00b0c0f3']]`
  - `CONDITIONAL_JUMP` [`00b0c0f0`](#insn-00b0c0f0) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c0f0`](#insn-00b0c0f0) → [`00b0c0f4`](#insn-00b0c0f4)
- ブロック [`00b0c0f4`](#insn-00b0c0f4) 範囲 `[['00b0c0f4', '00b0c0ff']]`
  - `CONDITIONAL_JUMP` [`00b0c0fc`](#insn-00b0c0fc) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c0fc`](#insn-00b0c0fc) → [`00b0c100`](#insn-00b0c100)
- ブロック [`00b0c100`](#insn-00b0c100) 範囲 `[['00b0c100', '00b0c10f']]`
  - `CONDITIONAL_JUMP` [`00b0c10c`](#insn-00b0c10c) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c10c`](#insn-00b0c10c) → [`00b0c110`](#insn-00b0c110)
- ブロック [`00b0c110`](#insn-00b0c110) 範囲 `[['00b0c110', '00b0c117']]`
  - `CONDITIONAL_JUMP` [`00b0c114`](#insn-00b0c114) → [`00b0c13c`](#insn-00b0c13c)
  - `FALL_THROUGH` [`00b0c114`](#insn-00b0c114) → [`00b0c118`](#insn-00b0c118)
- ブロック [`00b0c118`](#insn-00b0c118) 範囲 `[['00b0c118', '00b0c127']]`
  - `CONDITIONAL_JUMP` [`00b0c124`](#insn-00b0c124) → [`00b0c13c`](#insn-00b0c13c)
  - `FALL_THROUGH` [`00b0c124`](#insn-00b0c124) → [`00b0c128`](#insn-00b0c128)
- ブロック [`00b0c128`](#insn-00b0c128) 範囲 `[['00b0c128', '00b0c133']]`
  - `CONDITIONAL_JUMP` [`00b0c130`](#insn-00b0c130) → [`00b0bf88`](#insn-00b0bf88)
  - `FALL_THROUGH` [`00b0c130`](#insn-00b0c130) → [`00b0c134`](#insn-00b0c134)
- ブロック [`00b0c134`](#insn-00b0c134) 範囲 `[['00b0c134', '00b0c13b']]`
  - `FALL_THROUGH` [`00b0c138`](#insn-00b0c138) → [`00b0c13c`](#insn-00b0c13c)
- ブロック [`00b0c13c`](#insn-00b0c13c) 範囲 `[['00b0c13c', '00b0c14b']]`
  - `UNCONDITIONAL_JUMP` [`00b0c148`](#insn-00b0c148) → [`00b0bf8c`](#insn-00b0bf8c)

## 命令位置別の参照

- [`00b0bef0`](#insn-00b0bef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf04`](#insn-00b0bf04) → [`00b0bf10`](#insn-00b0bf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf0c`](#insn-00b0bf0c) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf1c`](#insn-00b0bf1c) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf28`](#insn-00b0bf28) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf4c`](#insn-00b0bf4c) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf58`](#insn-00b0bf58) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf60`](#insn-00b0bf60) → [`00b0bf6c`](#insn-00b0bf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf68`](#insn-00b0bf68) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf74`](#insn-00b0bf74) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf7c`](#insn-00b0bf7c) → [`00b0bf9c`](#insn-00b0bf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf84`](#insn-00b0bf84) → [`00b0bf9c`](#insn-00b0bf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bf8c`](#insn-00b0bf8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfa4`](#insn-00b0bfa4) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfac`](#insn-00b0bfac) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfc0`](#insn-00b0bfc0) → [`00b0c13c`](#insn-00b0c13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfc8`](#insn-00b0bfc8) → [`00b0c014`](#insn-00b0c014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfd4`](#insn-00b0bfd4) → [`00b0bff0`](#insn-00b0bff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfe0`](#insn-00b0bfe0) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfe8`](#insn-00b0bfe8) → [`00b0bff8`](#insn-00b0bff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bfec`](#insn-00b0bfec) → [`00b0bf8c`](#insn-00b0bf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0bff4`](#insn-00b0bff4) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c000`](#insn-00b0c000) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c010`](#insn-00b0c010) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c018`](#insn-00b0c018) → [`00b0c09c`](#insn-00b0c09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c028`](#insn-00b0c028) → [`00b0c09c`](#insn-00b0c09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c034`](#insn-00b0c034) → [`00b0c050`](#insn-00b0c050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c040`](#insn-00b0c040) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c048`](#insn-00b0c048) → [`00b0c058`](#insn-00b0c058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c04c`](#insn-00b0c04c) → [`00b0bf8c`](#insn-00b0bf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c054`](#insn-00b0c054) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c064`](#insn-00b0c064) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c07c`](#insn-00b0c07c) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c084`](#insn-00b0c084) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c090`](#insn-00b0c090) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c098`](#insn-00b0c098) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0a0`](#insn-00b0c0a0) → [`00b0c13c`](#insn-00b0c13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0a8`](#insn-00b0c0a8) → [`00b0c0b8`](#insn-00b0c0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0b4`](#insn-00b0c0b4) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0bc`](#insn-00b0c0bc) → [`00b0c13c`](#insn-00b0c13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0c4`](#insn-00b0c0c4) → [`00b0c110`](#insn-00b0c110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0d0`](#insn-00b0c0d0) → [`00b0c0ec`](#insn-00b0c0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0dc`](#insn-00b0c0dc) → [`00b0bf8c`](#insn-00b0bf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0e4`](#insn-00b0c0e4) → [`00b0c0f4`](#insn-00b0c0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0e8`](#insn-00b0c0e8) → [`00b0bf8c`](#insn-00b0bf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0f0`](#insn-00b0c0f0) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c0fc`](#insn-00b0c0fc) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c10c`](#insn-00b0c10c) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c114`](#insn-00b0c114) → [`00b0c13c`](#insn-00b0c13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c124`](#insn-00b0c124) → [`00b0c13c`](#insn-00b0c13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c128`](#insn-00b0c128) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c12c`](#insn-00b0c12c) → [`00bdeac0`](../00bde/00bdeac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeac0` · 推定シンボル `None` · 推定型 `None`
- [`00b0c130`](#insn-00b0c130) → [`00b0bf88`](#insn-00b0bf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c134`](#insn-00b0c134) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0c148`](#insn-00b0c148) → [`00b0bf8c`](#insn-00b0bf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0bef0`](#insn-00b0bef0)

~~~json
{
  "source": "00b0bef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf04`](#insn-00b0bf04)

~~~json
{
  "source": "00b0bf04",
  "target": "00b0bf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf0c`](#insn-00b0bf0c)

~~~json
{
  "source": "00b0bf0c",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf1c`](#insn-00b0bf1c)

~~~json
{
  "source": "00b0bf1c",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf28`](#insn-00b0bf28)

~~~json
{
  "source": "00b0bf28",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf4c`](#insn-00b0bf4c)

~~~json
{
  "source": "00b0bf4c",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf58`](#insn-00b0bf58)

~~~json
{
  "source": "00b0bf58",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf60`](#insn-00b0bf60)

~~~json
{
  "source": "00b0bf60",
  "target": "00b0bf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf68`](#insn-00b0bf68)

~~~json
{
  "source": "00b0bf68",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf74`](#insn-00b0bf74)

~~~json
{
  "source": "00b0bf74",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf7c`](#insn-00b0bf7c)

~~~json
{
  "source": "00b0bf7c",
  "target": "00b0bf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf84`](#insn-00b0bf84)

~~~json
{
  "source": "00b0bf84",
  "target": "00b0bf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bf8c`](#insn-00b0bf8c)

~~~json
{
  "source": "00b0bf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfa4`](#insn-00b0bfa4)

~~~json
{
  "source": "00b0bfa4",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfac`](#insn-00b0bfac)

~~~json
{
  "source": "00b0bfac",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfc0`](#insn-00b0bfc0)

~~~json
{
  "source": "00b0bfc0",
  "target": "00b0c13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfc8`](#insn-00b0bfc8)

~~~json
{
  "source": "00b0bfc8",
  "target": "00b0c014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfd4`](#insn-00b0bfd4)

~~~json
{
  "source": "00b0bfd4",
  "target": "00b0bff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfe0`](#insn-00b0bfe0)

~~~json
{
  "source": "00b0bfe0",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfe8`](#insn-00b0bfe8)

~~~json
{
  "source": "00b0bfe8",
  "target": "00b0bff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bfec`](#insn-00b0bfec)

~~~json
{
  "source": "00b0bfec",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0bff4`](#insn-00b0bff4)

~~~json
{
  "source": "00b0bff4",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c000`](#insn-00b0c000)

~~~json
{
  "source": "00b0c000",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c010`](#insn-00b0c010)

~~~json
{
  "source": "00b0c010",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c018`](#insn-00b0c018)

~~~json
{
  "source": "00b0c018",
  "target": "00b0c09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c028`](#insn-00b0c028)

~~~json
{
  "source": "00b0c028",
  "target": "00b0c09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c034`](#insn-00b0c034)

~~~json
{
  "source": "00b0c034",
  "target": "00b0c050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c040`](#insn-00b0c040)

~~~json
{
  "source": "00b0c040",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c048`](#insn-00b0c048)

~~~json
{
  "source": "00b0c048",
  "target": "00b0c058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c04c`](#insn-00b0c04c)

~~~json
{
  "source": "00b0c04c",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c054`](#insn-00b0c054)

~~~json
{
  "source": "00b0c054",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c064`](#insn-00b0c064)

~~~json
{
  "source": "00b0c064",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c07c`](#insn-00b0c07c)

~~~json
{
  "source": "00b0c07c",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c084`](#insn-00b0c084)

~~~json
{
  "source": "00b0c084",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c090`](#insn-00b0c090)

~~~json
{
  "source": "00b0c090",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c098`](#insn-00b0c098)

~~~json
{
  "source": "00b0c098",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0a0`](#insn-00b0c0a0)

~~~json
{
  "source": "00b0c0a0",
  "target": "00b0c13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0a8`](#insn-00b0c0a8)

~~~json
{
  "source": "00b0c0a8",
  "target": "00b0c0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0b4`](#insn-00b0c0b4)

~~~json
{
  "source": "00b0c0b4",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0bc`](#insn-00b0c0bc)

~~~json
{
  "source": "00b0c0bc",
  "target": "00b0c13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0c4`](#insn-00b0c0c4)

~~~json
{
  "source": "00b0c0c4",
  "target": "00b0c110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0d0`](#insn-00b0c0d0)

~~~json
{
  "source": "00b0c0d0",
  "target": "00b0c0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0dc`](#insn-00b0c0dc)

~~~json
{
  "source": "00b0c0dc",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0e4`](#insn-00b0c0e4)

~~~json
{
  "source": "00b0c0e4",
  "target": "00b0c0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0e8`](#insn-00b0c0e8)

~~~json
{
  "source": "00b0c0e8",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0f0`](#insn-00b0c0f0)

~~~json
{
  "source": "00b0c0f0",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c0fc`](#insn-00b0c0fc)

~~~json
{
  "source": "00b0c0fc",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c10c`](#insn-00b0c10c)

~~~json
{
  "source": "00b0c10c",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c114`](#insn-00b0c114)

~~~json
{
  "source": "00b0c114",
  "target": "00b0c13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c124`](#insn-00b0c124)

~~~json
{
  "source": "00b0c124",
  "target": "00b0c13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c128`](#insn-00b0c128)

~~~json
{
  "source": "00b0c128",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c12c`](#insn-00b0c12c)

~~~json
{
  "source": "00b0c12c",
  "target": "00bdeac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0c130`](#insn-00b0c130)

~~~json
{
  "source": "00b0c130",
  "target": "00b0bf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c134`](#insn-00b0c134)

~~~json
{
  "source": "00b0c134",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0c148`](#insn-00b0c148)

~~~json
{
  "source": "00b0c148",
  "target": "00b0bf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
