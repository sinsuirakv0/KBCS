# 00bca4dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bca498`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-c482040a41c3b739b7afe0ca4deb17f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c46f24`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-cbadc6d38fb77345c3029fd061edb087)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca4dc",
  "name": "FUN_00bca4dc",
  "size": 452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a54fd0d916de957d622181cc3326c648ee19c3610e8bda0821dcc5e75a5e15e1",
  "source_text_sha256": "a54fd0d916de957d622181cc3326c648ee19c3610e8bda0821dcc5e75a5e15e1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bca4dc",
        "00bca69f"
      ]
    ],
    "bytes_sha256": "9a4f0c6d308b603e0f9cb37d80a4910c6ea116b9378542198413c7c1e41d8a46",
    "instruction_count": 113,
    "instruction_bytes": 452,
    "body_bytes": 452,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)
- [00be1100](../00be1/00be1100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6065 bytes

~~~c

void FUN_00bca4dc(long param_1,undefined8 *param_2)

{
  undefined1 uVar1;
  ulong uVar2;
  ulong uVar3;
  bool bVar4;
  int iVar5;
  void *__ptr;
  char *pcVar6;
  undefined1 *puVar7;
  size_t __size;
  long lVar8;
  undefined1 *puVar9;
  size_t __n;
  byte bVar10;
  byte bVar11;
  byte bVar12;
  byte bVar13;
  byte bVar14;
  byte bVar15;
  char local_50 [40];
  undefined8 local_28;
  
  if (0xf < *(ulong *)(param_1 + 0x18)) {
    pcVar6 = *(char **)(param_1 + 0x10);
    bVar10 = pcVar6[2];
    bVar13 = pcVar6[3];
    bVar11 = pcVar6[4];
    bVar14 = pcVar6[5];
    bVar12 = pcVar6[10];
    bVar15 = pcVar6[0xb];
    puVar9 = (undefined1 *)((ulong)&local_28 | 1);
    uVar2 = CONCAT17(-((byte)pcVar6[0xe] - 0x3a < 0xfffffff6),
                     CONCAT16(-((byte)pcVar6[0xc] - 0x3a < 0xfffffff6),
                              CONCAT15(-(bVar12 - 0x3a < 0xfffffff6),
                                       CONCAT14(-((CONCAT12(bVar12,(ushort)(byte)pcVar6[8]) & 0xffff
                                                  ) - 0x3a < 0xfffffff6),
                                                CONCAT13(-((byte)pcVar6[6] - 0x3a < 0xfffffff6),
                                                         CONCAT12(-(bVar11 - 0x3a < 0xfffffff6),
                                                                  CONCAT11(-(bVar10 - 0x3a <
                                                                            0xfffffff6),
                                                                           -((CONCAT12(bVar11,
                                                  CONCAT11(bVar10,*pcVar6)) & 0xff) - 0x3a <
                                                  0xfffffff6)))))))) & 0x909090909090909;
    uVar3 = CONCAT17(-((byte)pcVar6[0xf] - 0x3a < 0xfffffff6),
                     CONCAT16(-((byte)pcVar6[0xd] - 0x3a < 0xfffffff6),
                              CONCAT15(-(bVar15 - 0x3a < 0xfffffff6),
                                       CONCAT14(-((CONCAT12(bVar15,(ushort)(byte)pcVar6[9]) & 0xffff
                                                  ) - 0x3a < 0xfffffff6),
                                                CONCAT13(-((byte)pcVar6[7] - 0x3a < 0xfffffff6),
                                                         CONCAT12(-(bVar14 - 0x3a < 0xfffffff6),
                                                                  CONCAT11(-(bVar13 - 0x3a <
                                                                            0xfffffff6),
                                                                           -((CONCAT12(bVar14,
                                                  CONCAT11(bVar13,pcVar6[1])) & 0xff) - 0x3a <
                                                  0xfffffff6)))))))) & 0x7979797979797979 ^
            0xd0d0d0d0d0d0d0d0;
    local_28 = CONCAT17((char)(uVar3 >> 0x38) + pcVar6[0xf] +
                        ((char)(uVar2 >> 0x38) + pcVar6[0xe]) * '\x10',
                        CONCAT16((char)(uVar3 >> 0x30) + pcVar6[0xd] +
                                 ((char)(uVar2 >> 0x30) + pcVar6[0xc]) * '\x10',
                                 CONCAT15((char)(uVar3 >> 0x28) + bVar15 +
                                          ((char)(uVar2 >> 0x28) + bVar12) * '\x10',
                                          CONCAT14((char)(uVar3 >> 0x20) + pcVar6[9] +
                                                   ((char)(uVar2 >> 0x20) + pcVar6[8]) * '\x10',
                                                   CONCAT13((char)(uVar3 >> 0x18) + pcVar6[7] +
                                                            ((char)(uVar2 >> 0x18) + pcVar6[6]) *
                                                            '\x10',CONCAT12((char)(uVar3 >> 0x10) +
                                                                            bVar14 + ((char)(uVar2 
                                                  >> 0x10) + bVar11) * '\x10',
                                                  CONCAT11((char)(uVar3 >> 8) + bVar13 +
                                                           ((char)(uVar2 >> 8) + bVar10) * '\x10',
                                                           (char)uVar3 + pcVar6[1] +
                                                           ((char)uVar2 + *pcVar6) * '\x10')))))));
    puVar7 = (undefined1 *)((ulong)&local_28 | 7);
    do {
      uVar1 = puVar9[-1];
      puVar9[-1] = *puVar7;
      *puVar7 = uVar1;
      bVar4 = puVar9 < puVar7 + -1;
      puVar9 = puVar9 + 1;
      puVar7 = puVar7 + -1;
    } while (bVar4);
    local_50[8] = '\0';
    local_50[9] = '\0';
    local_50[10] = '\0';
    local_50[0xb] = '\0';
    local_50[0xc] = '\0';
    local_50[0xd] = '\0';
    local_50[0xe] = '\0';
    local_50[0xf] = '\0';
    local_50[0] = '\0';
    local_50[1] = '\0';
    local_50[2] = '\0';
    local_50[3] = '\0';
    local_50[4] = '\0';
    local_50[5] = '\0';
    local_50[6] = '\0';
    local_50[7] = '\0';
    local_50[0x18] = '\0';
    local_50[0x19] = '\0';
    local_50[0x1a] = '\0';
    local_50[0x1b] = '\0';
    local_50[0x1c] = '\0';
    local_50[0x1d] = '\0';
    local_50[0x1e] = '\0';
    local_50[0x1f] = '\0';
    local_50[0x10] = '\0';
    local_50[0x11] = '\0';
    local_50[0x12] = '\0';
    local_50[0x13] = '\0';
    local_50[0x14] = '\0';
    local_50[0x15] = '\0';
    local_50[0x16] = '\0';
    local_50[0x17] = '\0';
    iVar5 = snprintf(local_50,0x20,"%a",local_28);
    if (iVar5 != 0) {
      lVar8 = param_2[1];
      __n = (size_t)iVar5;
      __ptr = (void *)*param_2;
      if ((ulong)param_2[2] < lVar8 + __n) {
        __size = param_2[2] * 2;
        uVar2 = lVar8 + __n + 0x3e0;
        if (__size < uVar2 || __size - uVar2 == 0) {
          __size = uVar2;
        }
        param_2[2] = __size;
        __ptr = realloc(__ptr,__size);
        *param_2 = __ptr;
        if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
        lVar8 = param_2[1];
      }
      memcpy((void *)((long)__ptr + lVar8),local_50,__n);
      param_2[1] = param_2[1] + __n;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bca4dc"></a> `00bca4dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bca4e0"></a> `00bca4e0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bca4e4"></a> `00bca4e4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca4e8"></a> `00bca4e8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bca4ec"></a> `00bca4ec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bca4f0"></a> `00bca4f0` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bca4f4"></a> `00bca4f4` | `1f 41 00 f1` | cmp x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bca4f8"></a> `00bca4f8` | `83 0c 00 54` | b.cc 0x00bca688 | `CONDITIONAL_JUMP`
<a id="insn-00bca4fc"></a> `00bca4fc` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bca500"></a> `00bca500` | `23 07 01 6f` | mvni v3.4S,#0x39 | `FALL_THROUGH`
<a id="insn-00bca504"></a> `00bca504` | `26 05 00 6f` | mvni v6.4S,#0x9 | `FALL_THROUGH`
<a id="insn-00bca508"></a> `00bca508` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bca50c"></a> `00bca50c` | `00 01 40 3d` | ldr b0,[x8] | `FALL_THROUGH`
<a id="insn-00bca510"></a> `00bca510` | `09 09 00 91` | add x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bca514"></a> `00bca514` | `01 05 40 3d` | ldr b1,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bca518"></a> `00bca518` | `0a 11 00 91` | add x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bca51c"></a> `00bca51c` | `20 05 40 0d` | ld1 {v0.B}[1],[x9] | `FALL_THROUGH`
<a id="insn-00bca520"></a> `00bca520` | `09 0d 00 91` | add x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bca524"></a> `00bca524` | `21 05 40 0d` | ld1 {v1.B}[1],[x9] | `FALL_THROUGH`
<a id="insn-00bca528"></a> `00bca528` | `09 15 00 91` | add x9,x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bca52c"></a> `00bca52c` | `40 09 40 0d` | ld1 {v0.B}[2],[x10] | `FALL_THROUGH`
<a id="insn-00bca530"></a> `00bca530` | `0a 19 00 91` | add x10,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00bca534"></a> `00bca534` | `21 09 40 0d` | ld1 {v1.B}[2],[x9] | `FALL_THROUGH`
<a id="insn-00bca538"></a> `00bca538` | `09 1d 00 91` | add x9,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bca53c"></a> `00bca53c` | `40 0d 40 0d` | ld1 {v0.B}[3],[x10] | `FALL_THROUGH`
<a id="insn-00bca540"></a> `00bca540` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bca544"></a> `00bca544` | `21 0d 40 0d` | ld1 {v1.B}[3],[x9] | `FALL_THROUGH`
<a id="insn-00bca548"></a> `00bca548` | `09 25 00 91` | add x9,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bca54c"></a> `00bca54c` | `40 11 40 0d` | ld1 {v0.B}[4],[x10] | `FALL_THROUGH`
<a id="insn-00bca550"></a> `00bca550` | `0a 29 00 91` | add x10,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bca554"></a> `00bca554` | `21 11 40 0d` | ld1 {v1.B}[4],[x9] | `FALL_THROUGH`
<a id="insn-00bca558"></a> `00bca558` | `09 2d 00 91` | add x9,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bca55c"></a> `00bca55c` | `40 15 40 0d` | ld1 {v0.B}[5],[x10] | `FALL_THROUGH`
<a id="insn-00bca560"></a> `00bca560` | `0a 31 00 91` | add x10,x8,#0xc | `FALL_THROUGH`
<a id="insn-00bca564"></a> `00bca564` | `21 15 40 0d` | ld1 {v1.B}[5],[x9] | `FALL_THROUGH`
<a id="insn-00bca568"></a> `00bca568` | `09 35 00 91` | add x9,x8,#0xd | `FALL_THROUGH`
<a id="insn-00bca56c"></a> `00bca56c` | `40 19 40 0d` | ld1 {v0.B}[6],[x10] | `FALL_THROUGH`
<a id="insn-00bca570"></a> `00bca570` | `0a 39 00 91` | add x10,x8,#0xe | `FALL_THROUGH`
<a id="insn-00bca574"></a> `00bca574` | `08 3d 00 91` | add x8,x8,#0xf | `FALL_THROUGH`
<a id="insn-00bca578"></a> `00bca578` | `21 19 40 0d` | ld1 {v1.B}[6],[x9] | `FALL_THROUGH`
<a id="insn-00bca57c"></a> `00bca57c` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bca580"></a> `00bca580` | `40 1d 40 0d` | ld1 {v0.B}[7],[x10] | `FALL_THROUGH`
<a id="insn-00bca584"></a> `00bca584` | `01 1d 40 0d` | ld1 {v1.B}[7],[x8] | `FALL_THROUGH`
<a id="insn-00bca588"></a> `00bca588` | `28 09 40 b2` | orr x8,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00bca58c"></a> `00bca58c` | `29 01 40 b2` | orr x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca590"></a> `00bca590` | `02 a4 08 2f` | uxtl v2.8H,v0.8B | `FALL_THROUGH`
<a id="insn-00bca594"></a> `00bca594` | `24 a4 08 2f` | uxtl v4.8H,v1.8B | `FALL_THROUGH`
<a id="insn-00bca598"></a> `00bca598` | `65 10 62 2e` | uaddw v5.4S,v3.4S,v2.4H | `FALL_THROUGH`
<a id="insn-00bca59c"></a> `00bca59c` | `62 10 62 6e` | uaddw2 v2.4S,v3.4S,v2.8H | `FALL_THROUGH`
<a id="insn-00bca5a0"></a> `00bca5a0` | `67 10 64 2e` | uaddw v7.4S,v3.4S,v4.4H | `FALL_THROUGH`
<a id="insn-00bca5a4"></a> `00bca5a4` | `63 10 64 6e` | uaddw2 v3.4S,v3.4S,v4.8H | `FALL_THROUGH`
<a id="insn-00bca5a8"></a> `00bca5a8` | `c2 34 a2 6e` | cmhi v2.4S,v6.4S,v2.4S | `FALL_THROUGH`
<a id="insn-00bca5ac"></a> `00bca5ac` | `c4 34 a5 6e` | cmhi v4.4S,v6.4S,v5.4S | `FALL_THROUGH`
<a id="insn-00bca5b0"></a> `00bca5b0` | `c3 34 a3 6e` | cmhi v3.4S,v6.4S,v3.4S | `FALL_THROUGH`
<a id="insn-00bca5b4"></a> `00bca5b4` | `c5 34 a7 6e` | cmhi v5.4S,v6.4S,v7.4S | `FALL_THROUGH`
<a id="insn-00bca5b8"></a> `00bca5b8` | `26 e5 05 0f` | movi v6.8B,#0xa9 | `FALL_THROUGH`
<a id="insn-00bca5bc"></a> `00bca5bc` | `82 18 42 4e` | uzp1 v2.8H,v4.8H,v2.8H | `FALL_THROUGH`
<a id="insn-00bca5c0"></a> `00bca5c0` | `24 e5 00 0f` | movi v4.8B,#0x9 | `FALL_THROUGH`
<a id="insn-00bca5c4"></a> `00bca5c4` | `a3 18 43 4e` | uzp1 v3.8H,v5.8H,v3.8H | `FALL_THROUGH`
<a id="insn-00bca5c8"></a> `00bca5c8` | `05 e6 06 0f` | movi v5.8B,#0xd0 | `FALL_THROUGH`
<a id="insn-00bca5cc"></a> `00bca5cc` | `42 28 21 0e` | xtn v2.8B,v2.8H | `FALL_THROUGH`
<a id="insn-00bca5d0"></a> `00bca5d0` | `63 28 21 0e` | xtn v3.8B,v3.8H | `FALL_THROUGH`
<a id="insn-00bca5d4"></a> `00bca5d4` | `42 1c 24 0e` | and v2.8B,v2.8B,v4.8B | `FALL_THROUGH`
<a id="insn-00bca5d8"></a> `00bca5d8` | `c3 1c 65 2e` | bsl v3.8B,v6.8B,v5.8B | `FALL_THROUGH`
<a id="insn-00bca5dc"></a> `00bca5dc` | `40 84 20 0e` | add v0.8B,v2.8B,v0.8B | `FALL_THROUGH`
<a id="insn-00bca5e0"></a> `00bca5e0` | `61 84 21 0e` | add v1.8B,v3.8B,v1.8B | `FALL_THROUGH`
<a id="insn-00bca5e4"></a> `00bca5e4` | `00 54 0c 0f` | shl v0.8B,v0.8B,0x4 | `FALL_THROUGH`
<a id="insn-00bca5e8"></a> `00bca5e8` | `20 84 20 0e` | add v0.8B,v1.8B,v0.8B | `FALL_THROUGH`
<a id="insn-00bca5ec"></a> `00bca5ec` | `a0 83 1f fc` | stur d0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bca5f0"></a> `00bca5f0` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bca5f4"></a> `00bca5f4` | `2b f1 5f 38` | ldurb w11,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00bca5f8"></a> `00bca5f8` | `2a f1 1f 38` | sturb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00bca5fc"></a> `00bca5fc` | `0b f5 1f 38` | strb w11,[x8], #-0x1 | `FALL_THROUGH`
<a id="insn-00bca600"></a> `00bca600` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bca604"></a> `00bca604` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca608"></a> `00bca608` | `43 ff ff 54` | b.cc 0x00bca5f0 | `CONDITIONAL_JUMP`
<a id="insn-00bca60c"></a> `00bca60c` | `01 e4 00 6f` | movi v1.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bca610"></a> `00bca610` | `a0 83 5f fc` | ldur d0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bca614"></a> `00bca614` | `82 b6 ff d0` | adrp x2,0x29c000 | `FALL_THROUGH`
<a id="insn-00bca618"></a> `00bca618` | `42 dc 0a 91` | add x2,x2,#0x2b7 | `FALL_THROUGH`
<a id="insn-00bca61c"></a> `00bca61c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bca620"></a> `00bca620` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bca624"></a> `00bca624` | `e1 07 00 ad` | stp q1,q1,[sp] | `FALL_THROUGH`
<a id="insn-00bca628"></a> `00bca628` | `b6 5a 00 94` | bl 0x00be1100 | `UNCONDITIONAL_CALL`
<a id="insn-00bca62c"></a> `00bca62c` | `e0 02 00 34` | cbz w0,0x00bca688 | `CONDITIONAL_JUMP`
<a id="insn-00bca630"></a> `00bca630` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca634"></a> `00bca634` | `14 7c 40 93` | sxtw x20,w0 | `FALL_THROUGH`
<a id="insn-00bca638"></a> `00bca638` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bca63c"></a> `00bca63c` | `0a 01 14 8b` | add x10,x8,x20 | `FALL_THROUGH`
<a id="insn-00bca640"></a> `00bca640` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bca644"></a> `00bca644` | `49 01 00 54` | b.ls 0x00bca66c | `CONDITIONAL_JUMP`
<a id="insn-00bca648"></a> `00bca648` | `28 f9 7f d3` | lsl x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bca64c"></a> `00bca64c` | `49 81 0f 91` | add x9,x10,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bca650"></a> `00bca650` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bca654"></a> `00bca654` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bca658"></a> `00bca658` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bca65c"></a> `00bca65c` | `fd 4a 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bca660"></a> `00bca660` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bca664"></a> `00bca664` | `c0 01 00 b4` | cbz x0,0x00bca69c | `CONDITIONAL_JUMP`
<a id="insn-00bca668"></a> `00bca668` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca66c"></a> `00bca66c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bca670"></a> `00bca670` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bca674"></a> `00bca674` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bca678"></a> `00bca678` | `ce 42 00 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bca67c"></a> `00bca67c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca680"></a> `00bca680` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00bca684"></a> `00bca684` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bca688"></a> `00bca688` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bca68c"></a> `00bca68c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca690"></a> `00bca690` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bca694"></a> `00bca694` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bca698"></a> `00bca698` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bca69c"></a> `00bca69c` | `09 4f 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bca4dc`](#insn-00bca4dc) 範囲 `[['00bca4dc', '00bca4fb']]`
  - `CONDITIONAL_JUMP` [`00bca4f8`](#insn-00bca4f8) → [`00bca688`](#insn-00bca688)
  - `FALL_THROUGH` [`00bca4f8`](#insn-00bca4f8) → [`00bca4fc`](#insn-00bca4fc)
- ブロック [`00bca4fc`](#insn-00bca4fc) 範囲 `[['00bca4fc', '00bca5ef']]`
  - `FALL_THROUGH` [`00bca5ec`](#insn-00bca5ec) → [`00bca5f0`](#insn-00bca5f0)
- ブロック [`00bca5f0`](#insn-00bca5f0) 範囲 `[['00bca5f0', '00bca60b']]`
  - `CONDITIONAL_JUMP` [`00bca608`](#insn-00bca608) → [`00bca5f0`](#insn-00bca5f0)
  - `FALL_THROUGH` [`00bca608`](#insn-00bca608) → [`00bca60c`](#insn-00bca60c)
- ブロック [`00bca60c`](#insn-00bca60c) 範囲 `[['00bca60c', '00bca62f']]`
  - `CONDITIONAL_JUMP` [`00bca62c`](#insn-00bca62c) → [`00bca688`](#insn-00bca688)
  - `FALL_THROUGH` [`00bca62c`](#insn-00bca62c) → [`00bca630`](#insn-00bca630)
- ブロック [`00bca630`](#insn-00bca630) 範囲 `[['00bca630', '00bca647']]`
  - `CONDITIONAL_JUMP` [`00bca644`](#insn-00bca644) → [`00bca66c`](#insn-00bca66c)
  - `FALL_THROUGH` [`00bca644`](#insn-00bca644) → [`00bca648`](#insn-00bca648)
- ブロック [`00bca648`](#insn-00bca648) 範囲 `[['00bca648', '00bca667']]`
  - `CONDITIONAL_JUMP` [`00bca664`](#insn-00bca664) → [`00bca69c`](#insn-00bca69c)
  - `FALL_THROUGH` [`00bca664`](#insn-00bca664) → [`00bca668`](#insn-00bca668)
- ブロック [`00bca668`](#insn-00bca668) 範囲 `[['00bca668', '00bca66b']]`
  - `FALL_THROUGH` [`00bca668`](#insn-00bca668) → [`00bca66c`](#insn-00bca66c)
- ブロック [`00bca66c`](#insn-00bca66c) 範囲 `[['00bca66c', '00bca687']]`
  - `FALL_THROUGH` [`00bca684`](#insn-00bca684) → [`00bca688`](#insn-00bca688)
- ブロック [`00bca688`](#insn-00bca688) 範囲 `[['00bca688', '00bca69b']]`
- ブロック [`00bca69c`](#insn-00bca69c) 範囲 `[['00bca69c', '00bca69f']]`

## 命令位置別の参照

- [`00bca4e4`](#insn-00bca4e4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca4e8`](#insn-00bca4e8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca4f8`](#insn-00bca4f8) → [`00bca688`](#insn-00bca688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca5ec`](#insn-00bca5ec) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca608`](#insn-00bca608) → [`00bca5f0`](#insn-00bca5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca610`](#insn-00bca610) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca618`](#insn-00bca618) → `0029c2b7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca624`](#insn-00bca624) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca628`](#insn-00bca628) → [`00be1100`](../00be1/00be1100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1100` · 推定シンボル `None` · 推定型 `None`
- [`00bca62c`](#insn-00bca62c) → [`00bca688`](#insn-00bca688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca644`](#insn-00bca644) → [`00bca66c`](#insn-00bca66c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca65c`](#insn-00bca65c) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bca664`](#insn-00bca664) → [`00bca69c`](#insn-00bca69c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca678`](#insn-00bca678) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bca688`](#insn-00bca688) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca68c`](#insn-00bca68c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca69c`](#insn-00bca69c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bca4e4`](#insn-00bca4e4)

~~~json
{
  "source": "00bca4e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca4e8`](#insn-00bca4e8)

~~~json
{
  "source": "00bca4e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca4f8`](#insn-00bca4f8)

~~~json
{
  "source": "00bca4f8",
  "target": "00bca688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca5ec`](#insn-00bca5ec)

~~~json
{
  "source": "00bca5ec",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca608`](#insn-00bca608)

~~~json
{
  "source": "00bca608",
  "target": "00bca5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca610`](#insn-00bca610)

~~~json
{
  "source": "00bca610",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca618`](#insn-00bca618)

~~~json
{
  "source": "00bca618",
  "target": "0029c2b7",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca624`](#insn-00bca624)

~~~json
{
  "source": "00bca624",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca628`](#insn-00bca628)

~~~json
{
  "source": "00bca628",
  "target": "00be1100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca62c`](#insn-00bca62c)

~~~json
{
  "source": "00bca62c",
  "target": "00bca688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca644`](#insn-00bca644)

~~~json
{
  "source": "00bca644",
  "target": "00bca66c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca65c`](#insn-00bca65c)

~~~json
{
  "source": "00bca65c",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca664`](#insn-00bca664)

~~~json
{
  "source": "00bca664",
  "target": "00bca69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca678`](#insn-00bca678)

~~~json
{
  "source": "00bca678",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca688`](#insn-00bca688)

~~~json
{
  "source": "00bca688",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca68c`](#insn-00bca68c)

~~~json
{
  "source": "00bca68c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca69c`](#insn-00bca69c)

~~~json
{
  "source": "00bca69c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
