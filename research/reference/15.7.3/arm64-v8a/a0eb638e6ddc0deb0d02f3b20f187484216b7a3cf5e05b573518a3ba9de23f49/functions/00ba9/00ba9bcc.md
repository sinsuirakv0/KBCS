# 00ba9bcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ba9b04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9b04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-31be7f8b0753e82fce40e867e46649a9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba9c10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9c10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0022.md#compare-d0bfb7487c852f26f1ec420d523c2780)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba9bcc",
  "name": "_ZNKSt6__ndk15ctypeIwE9do_narrowEPKwS3_cPc",
  "size": 392,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46c9e2739dbd522bdf39dbaf04a078eaf610e546b0bfd669e4885c44bd0fc710",
  "source_text_sha256": "46c9e2739dbd522bdf39dbaf04a078eaf610e546b0bfd669e4885c44bd0fc710",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba9bcc",
        "00ba9d53"
      ]
    ],
    "bytes_sha256": "979f4778d209f829660695a17b3622fe7aa4273589f89ae64a6dcc1d5824aa9b",
    "instruction_count": 98,
    "instruction_bytes": 392,
    "body_bytes": 392,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8450 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

uint * _ZNKSt6__ndk15ctypeIwE9do_narrowEPKwS3_cPc
                 (undefined8 param_1,uint *param_2,uint *param_3,uint param_4,undefined1 *param_5)

{
  ulong uVar1;
  undefined1 (*pauVar2) [12];
  undefined1 auVar3 [16];
  undefined1 auVar4 [16];
  undefined8 uVar5;
  uint6 uVar6;
  uint3 uVar7;
  undefined1 auVar8 [16];
  undefined1 auVar9 [16];
  undefined8 uVar10;
  undefined1 auVar11 [16];
  undefined8 uVar12;
  undefined1 auVar13 [16];
  undefined8 uVar14;
  undefined1 auVar15 [16];
  undefined1 auVar16 [16];
  uint *puVar17;
  undefined1 (*pauVar18) [12];
  undefined1 (*pauVar19) [12];
  undefined1 (*pauVar20) [12];
  undefined1 auVar21 [16];
  undefined1 uVar22;
  ulong uVar23;
  ulong uVar24;
  long lVar25;
  uint *puVar26;
  undefined1 (*pauVar27) [12];
  undefined8 *puVar28;
  undefined1 (*pauVar29) [16];
  ulong *puVar30;
  undefined1 auVar31 [16];
  undefined1 auVar32 [16];
  undefined1 auVar33 [16];
  uint uVar34;
  uint uVar35;
  uint uVar36;
  uint uVar37;
  uint uVar38;
  
  auVar21 = _DAT_002b1600;
  if (param_2 == param_3) {
    return param_2;
  }
  uVar23 = (long)param_3 + (-4 - (long)param_2);
  if ((0x1b < uVar23) &&
     (((undefined1 *)((long)param_2 + (uVar23 & 0xfffffffffffffffc) + 4) <= param_5 ||
      (param_5 + (uVar23 >> 2) + 1 <= param_2)))) {
    uVar1 = (uVar23 >> 2) + 1;
    uVar22 = (undefined1)param_4;
    if (uVar23 < 0x7c) {
      uVar24 = 0;
    }
    else {
      uVar24 = uVar1 & 0x7fffffffffffffe0;
      pauVar27 = (undefined1 (*) [12])(param_2 + 0x10);
      puVar28 = (undefined8 *)(param_5 + 0x10);
      uVar23 = uVar24;
      do {
        auVar4 = *(undefined1 (*) [16])((long)pauVar27[-6] + 8);
        auVar15 = *(undefined1 (*) [16])(pauVar27 + -4);
        uVar23 = uVar23 - 0x20;
        puVar17 = (uint *)*pauVar27;
        uVar35 = (uint)((ulong)*(undefined8 *)(puVar17 + 2) >> 0x20);
        puVar26 = (uint *)*pauVar27;
        pauVar2 = pauVar27 + 2;
        uVar36 = (uint)((ulong)*(undefined8 *)*pauVar2 >> 0x20);
        uVar10 = *(undefined8 *)*(undefined1 (*) [12])((long)pauVar27[1] + 4);
        auVar16 = *(undefined1 (*) [16])((long)pauVar27[-3] + 4);
        pauVar18 = pauVar27 + -1;
        uVar34 = (uint)((ulong)*(undefined8 *)((long)*pauVar18 + 4) >> 0x20);
        uVar5 = *(undefined8 *)*(undefined1 (*) [12])((long)pauVar27[-2] + 8);
        pauVar19 = pauVar27 + 3;
        uVar37 = (uint)((ulong)*(undefined8 *)((long)*pauVar19 + 4) >> 0x20);
        uVar12 = *(undefined8 *)*(undefined1 (*) [12])((long)pauVar27[2] + 8);
        pauVar20 = pauVar27 + 4;
        uVar38 = (uint)((ulong)*(undefined8 *)((long)*pauVar20 + 8) >> 0x20);
        uVar14 = *(undefined8 *)pauVar27[4];
        auVar31._12_4_ = uVar34;
        auVar31._0_12_ = *(undefined1 (*) [12])((long)pauVar27[-2] + 8);
        auVar31 = a64_TBL(ZEXT816(0),auVar4,auVar15,auVar16,auVar31,auVar21);
        auVar33._12_4_ = uVar35;
        auVar33._0_12_ = *pauVar27;
        auVar9._12_4_ = uVar36;
        auVar9._0_12_ = *(undefined1 (*) [12])((long)pauVar27[1] + 4);
        auVar11._12_4_ = uVar37;
        auVar11._0_12_ = *(undefined1 (*) [12])((long)pauVar27[2] + 8);
        auVar13._12_4_ = uVar38;
        auVar13._0_12_ = pauVar27[4];
        auVar33 = a64_TBL(ZEXT816(0),auVar33,auVar9,auVar11,auVar13,auVar21);
        pauVar27 = (undefined1 (*) [12])((long)pauVar27[10] + 8);
        uVar6 = (uint6)CONCAT14(-(0x7f < (uint)((ulong)uVar5 >> 0x20)),-(uint)(0x7f < (uint)uVar5))
                & 0xffff0000ffff;
        uVar7 = CONCAT12(-(0x7f < auVar16._4_4_),-(ushort)(0x7f < auVar16._0_4_)) & 0xff00ff;
        auVar32[1] = -(0x7f < (uint)((ulong)*(undefined8 *)puVar26 >> 0x20));
        auVar32[0] = -(0x7f < (uint)*(undefined8 *)puVar26);
        auVar32[2] = -(0x7f < (uint)*(undefined8 *)(puVar17 + 2));
        auVar32[3] = -(0x7f < uVar35);
        auVar32[4] = -(0x7f < (uint)uVar10);
        auVar32[5] = -(0x7f < (uint)((ulong)uVar10 >> 0x20));
        auVar32[6] = -(0x7f < (uint)*(undefined8 *)*pauVar2);
        auVar32[7] = -(0x7f < uVar36);
        auVar32[8] = -(0x7f < (uint)uVar12);
        auVar32[9] = -(0x7f < (uint)((ulong)uVar12 >> 0x20));
        auVar32[10] = -(0x7f < (uint)*(undefined8 *)((long)*pauVar19 + 4));
        auVar32[0xb] = -(0x7f < uVar37);
        auVar32[0xc] = -(0x7f < (uint)uVar14);
        auVar32[0xd] = -(0x7f < (uint)((ulong)uVar14 >> 0x20));
        auVar32[0xe] = -(0x7f < (uint)*(undefined8 *)((long)*pauVar20 + 8));
        auVar32[0xf] = -(0x7f < uVar38);
        auVar3[1] = uVar22;
        auVar3[0] = uVar22;
        auVar3[2] = uVar22;
        auVar3[3] = uVar22;
        auVar3[4] = uVar22;
        auVar3[5] = uVar22;
        auVar3[6] = uVar22;
        auVar3[7] = uVar22;
        auVar3[8] = uVar22;
        auVar3[9] = uVar22;
        auVar3[10] = uVar22;
        auVar3[0xb] = uVar22;
        auVar3[0xc] = uVar22;
        auVar3[0xd] = uVar22;
        auVar3[0xe] = uVar22;
        auVar3[0xf] = uVar22;
        auVar8[1] = -(0x7f < auVar4._4_4_);
        auVar8[0] = -(0x7f < auVar4._0_4_);
        auVar8[2] = -(0x7f < auVar4._8_4_);
        auVar8[3] = -(0x7f < auVar4._12_4_);
        auVar8[4] = -(0x7f < auVar15._0_4_);
        auVar8[5] = -(0x7f < auVar15._4_4_);
        auVar8[6] = -(0x7f < auVar15._8_4_);
        auVar8[7] = -(0x7f < auVar15._12_4_);
        auVar8[8] = (char)uVar7;
        auVar8[9] = (char)(uVar7 >> 0x10);
        auVar8[10] = -(0x7f < auVar16._8_4_);
        auVar8[0xb] = -(0x7f < auVar16._12_4_);
        auVar8[0xc] = (char)uVar6;
        auVar8[0xd] = (char)(uVar6 >> 0x20);
        auVar8[0xe] = -(0x7f < (uint)*(undefined8 *)((long)*pauVar18 + 4));
        auVar8[0xf] = -(0x7f < uVar34);
        auVar31 = auVar31 ^ (auVar31 ^ auVar3) & auVar8;
        auVar4[1] = uVar22;
        auVar4[0] = uVar22;
        auVar4[2] = uVar22;
        auVar4[3] = uVar22;
        auVar4[4] = uVar22;
        auVar4[5] = uVar22;
        auVar4[6] = uVar22;
        auVar4[7] = uVar22;
        auVar4[8] = uVar22;
        auVar4[9] = uVar22;
        auVar4[10] = uVar22;
        auVar4[0xb] = uVar22;
        auVar4[0xc] = uVar22;
        auVar4[0xd] = uVar22;
        auVar4[0xe] = uVar22;
        auVar4[0xf] = uVar22;
        auVar33 = auVar33 ^ (auVar33 ^ auVar4) & auVar32;
        puVar28[-1] = auVar31._8_8_;
        puVar28[-2] = auVar31._0_8_;
        puVar28[1] = auVar33._8_8_;
        *puVar28 = auVar33._0_8_;
        puVar28 = puVar28 + 4;
      } while (uVar23 != 0);
      if (uVar1 == uVar24) {
        return param_3;
      }
      if ((uVar1 & 0x18) == 0) {
        param_2 = param_2 + uVar24;
        param_5 = param_5 + uVar24;
        goto LAB_00ba9c18;
      }
    }
    auVar21 = _DAT_002b0e50;
    uVar23 = uVar1 & 0x7ffffffffffffff8;
    lVar25 = uVar24 - uVar23;
    pauVar29 = (undefined1 (*) [16])(param_2 + uVar24);
    puVar30 = (ulong *)(param_5 + uVar24);
    do {
      auVar3 = *pauVar29;
      auVar4 = pauVar29[1];
      lVar25 = lVar25 + 8;
      auVar31 = a64_TBL(ZEXT816(0),auVar3,auVar4,auVar21);
      *puVar30 = auVar31._0_8_ ^
                 (auVar31._0_8_ ^
                 CONCAT17(uVar22,CONCAT16(uVar22,CONCAT15(uVar22,CONCAT14(uVar22,CONCAT13(uVar22,
                                                  CONCAT12(uVar22,CONCAT11(uVar22,uVar22)))))))) &
                 CONCAT17(-(0x7f < auVar4._12_4_),
                          CONCAT16(-(0x7f < auVar4._8_4_),
                                   CONCAT15(-(0x7f < auVar4._4_4_),
                                            CONCAT14(-(0x7f < auVar4._0_4_),
                                                     CONCAT13(-(0x7f < auVar3._12_4_),
                                                              CONCAT12(-(0x7f < auVar3._8_4_),
                                                                       CONCAT11(-(0x7f < auVar3.
                                                  _4_4_),-(0x7f < auVar3._0_4_))))))));
      pauVar29 = pauVar29 + 2;
      puVar30 = puVar30 + 1;
    } while (lVar25 != 0);
    param_2 = param_2 + uVar23;
    param_5 = param_5 + uVar23;
    if (uVar1 == uVar23) {
      return param_3;
    }
  }
LAB_00ba9c18:
  do {
    puVar26 = param_2 + 1;
    uVar34 = param_4;
    if (*param_2 < 0x80) {
      uVar34 = *param_2;
    }
    *param_5 = (char)uVar34;
    param_2 = puVar26;
    param_5 = param_5 + 1;
  } while (puVar26 != param_3);
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba9bcc"></a> `00ba9bcc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00ba9bd0"></a> `00ba9bd0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00ba9bd4"></a> `00ba9bd4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00ba9bd8"></a> `00ba9bd8` | `e0 02 00 54` | b.eq 0x00ba9c34 | `CONDITIONAL_JUMP`
<a id="insn-00ba9bdc"></a> `00ba9bdc` | `48 00 00 cb` | sub x8,x2,x0 | `FALL_THROUGH`
<a id="insn-00ba9be0"></a> `00ba9be0` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba9be4"></a> `00ba9be4` | `1f 71 00 f1` | cmp x8,#0x1c | `FALL_THROUGH`
<a id="insn-00ba9be8"></a> `00ba9be8` | `43 01 00 54` | b.cc 0x00ba9c10 | `CONDITIONAL_JUMP`
<a id="insn-00ba9bec"></a> `00ba9bec` | `09 f5 7e 92` | and x9,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba9bf0"></a> `00ba9bf0` | `09 00 09 8b` | add x9,x0,x9 | `FALL_THROUGH`
<a id="insn-00ba9bf4"></a> `00ba9bf4` | `29 11 00 91` | add x9,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00ba9bf8"></a> `00ba9bf8` | `3f 01 04 eb` | cmp x9,x4 | `FALL_THROUGH`
<a id="insn-00ba9bfc"></a> `00ba9bfc` | `e9 01 00 54` | b.ls 0x00ba9c38 | `CONDITIONAL_JUMP`
<a id="insn-00ba9c00"></a> `00ba9c00` | `89 08 48 8b` | add x9,x4,x8, LSR #0x2 | `FALL_THROUGH`
<a id="insn-00ba9c04"></a> `00ba9c04` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9c08"></a> `00ba9c08` | `3f 01 00 eb` | cmp x9,x0 | `FALL_THROUGH`
<a id="insn-00ba9c0c"></a> `00ba9c0c` | `69 01 00 54` | b.ls 0x00ba9c38 | `CONDITIONAL_JUMP`
<a id="insn-00ba9c10"></a> `00ba9c10` | `eb 03 04 aa` | mov x11,x4 | `FALL_THROUGH`
<a id="insn-00ba9c14"></a> `00ba9c14` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00ba9c18"></a> `00ba9c18` | `48 45 40 b8` | ldr w8,[x10], #0x4 | `FALL_THROUGH`
<a id="insn-00ba9c1c"></a> `00ba9c1c` | `1f fd 01 71` | cmp w8,#0x7f | `FALL_THROUGH`
<a id="insn-00ba9c20"></a> `00ba9c20` | `68 80 88 1a` | csel w8,w3,w8,hi | `FALL_THROUGH`
<a id="insn-00ba9c24"></a> `00ba9c24` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-00ba9c28"></a> `00ba9c28` | `68 15 00 38` | strb w8,[x11], #0x1 | `FALL_THROUGH`
<a id="insn-00ba9c2c"></a> `00ba9c2c` | `61 ff ff 54` | b.ne 0x00ba9c18 | `CONDITIONAL_JUMP`
<a id="insn-00ba9c30"></a> `00ba9c30` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00ba9c34"></a> `00ba9c34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba9c38"></a> `00ba9c38` | `09 fd 42 d3` | lsr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba9c3c"></a> `00ba9c3c` | `1f f1 01 f1` | cmp x8,#0x7c | `FALL_THROUGH`
<a id="insn-00ba9c40"></a> `00ba9c40` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba9c44"></a> `00ba9c44` | `62 00 00 54` | b.cs 0x00ba9c50 | `CONDITIONAL_JUMP`
<a id="insn-00ba9c48"></a> `00ba9c48` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00ba9c4c"></a> `00ba9c4c` | `28 00 00 14` | b 0x00ba9cec | `UNCONDITIONAL_JUMP`
<a id="insn-00ba9c50"></a> `00ba9c50` | `e0 07 03 4f` | movi v0.4S,#0x7f | `FALL_THROUGH`
<a id="insn-00ba9c54"></a> `00ba9c54` | `61 0c 01 4e` | dup v1.16B,w3 | `FALL_THROUGH`
<a id="insn-00ba9c58"></a> `00ba9c58` | `4a b8 ff 90` | adrp x10,0x2b1000 | `FALL_THROUGH`
<a id="insn-00ba9c5c"></a> `00ba9c5c` | `09 e5 7b 92` | and x9,x8,#0x7fffffffffffffe0 | `FALL_THROUGH`
<a id="insn-00ba9c60"></a> `00ba9c60` | `42 81 c1 3d` | ldr q2,[x10, #0x600] | `FALL_THROUGH`
<a id="insn-00ba9c64"></a> `00ba9c64` | `0a 00 01 91` | add x10,x0,#0x40 | `FALL_THROUGH`
<a id="insn-00ba9c68"></a> `00ba9c68` | `8b 40 00 91` | add x11,x4,#0x10 | `FALL_THROUGH`
<a id="insn-00ba9c6c"></a> `00ba9c6c` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00ba9c70"></a> `00ba9c70` | `43 11 7e ad` | ldp q3,q4,[x10, #-0x40] | `FALL_THROUGH`
<a id="insn-00ba9c74"></a> `00ba9c74` | `8c 81 00 f1` | subs x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00ba9c78"></a> `00ba9c78` | `50 45 40 ad` | ldp q16,q17,[x10] | `FALL_THROUGH`
<a id="insn-00ba9c7c"></a> `00ba9c7c` | `45 19 7f ad` | ldp q5,q6,[x10, #-0x20] | `FALL_THROUGH`
<a id="insn-00ba9c80"></a> `00ba9c80` | `52 4d 41 ad` | ldp q18,q19,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00ba9c84"></a> `00ba9c84` | `95 34 a0 6e` | cmhi v21.4S,v4.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c88"></a> `00ba9c88` | `76 34 a0 6e` | cmhi v22.4S,v3.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c8c"></a> `00ba9c8c` | `39 36 a0 6e` | cmhi v25.4S,v17.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c90"></a> `00ba9c90` | `1a 36 a0 6e` | cmhi v26.4S,v16.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c94"></a> `00ba9c94` | `c7 34 a0 6e` | cmhi v7.4S,v6.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c98"></a> `00ba9c98` | `b4 34 a0 6e` | cmhi v20.4S,v5.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9c9c"></a> `00ba9c9c` | `63 60 02 4e` | tbl v3.16B,{v3.16B,v4.16B,v5.16B,v6.16B},v2.16B | `FALL_THROUGH`
<a id="insn-00ba9ca0"></a> `00ba9ca0` | `77 36 a0 6e` | cmhi v23.4S,v19.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9ca4"></a> `00ba9ca4` | `58 36 a0 6e` | cmhi v24.4S,v18.4S,v0.4S | `FALL_THROUGH`
<a id="insn-00ba9ca8"></a> `00ba9ca8` | `05 62 02 4e` | tbl v5.16B,{v16.16B,v17.16B,v18.16B,v19.16B},v2.16B | `FALL_THROUGH`
<a id="insn-00ba9cac"></a> `00ba9cac` | `4a 01 02 91` | add x10,x10,#0x80 | `FALL_THROUGH`
<a id="insn-00ba9cb0"></a> `00ba9cb0` | `87 1a 47 4e` | uzp1 v7.8H,v20.8H,v7.8H | `FALL_THROUGH`
<a id="insn-00ba9cb4"></a> `00ba9cb4` | `d4 1a 55 4e` | uzp1 v20.8H,v22.8H,v21.8H | `FALL_THROUGH`
<a id="insn-00ba9cb8"></a> `00ba9cb8` | `56 1b 59 4e` | uzp1 v22.8H,v26.8H,v25.8H | `FALL_THROUGH`
<a id="insn-00ba9cbc"></a> `00ba9cbc` | `15 1b 57 4e` | uzp1 v21.8H,v24.8H,v23.8H | `FALL_THROUGH`
<a id="insn-00ba9cc0"></a> `00ba9cc0` | `87 1a 07 4e` | uzp1 v7.16B,v20.16B,v7.16B | `FALL_THROUGH`
<a id="insn-00ba9cc4"></a> `00ba9cc4` | `c4 1a 15 4e` | uzp1 v4.16B,v22.16B,v21.16B | `FALL_THROUGH`
<a id="insn-00ba9cc8"></a> `00ba9cc8` | `23 1c a7 6e` | bit v3.16B,v1.16B,v7.16B | `FALL_THROUGH`
<a id="insn-00ba9ccc"></a> `00ba9ccc` | `24 1c 65 6e` | bsl v4.16B,v1.16B,v5.16B | `FALL_THROUGH`
<a id="insn-00ba9cd0"></a> `00ba9cd0` | `63 91 3f ad` | stp q3,q4,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00ba9cd4"></a> `00ba9cd4` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00ba9cd8"></a> `00ba9cd8` | `c1 fc ff 54` | b.ne 0x00ba9c70 | `CONDITIONAL_JUMP`
<a id="insn-00ba9cdc"></a> `00ba9cdc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba9ce0"></a> `00ba9ce0` | `80 fa ff 54` | b.eq 0x00ba9c30 | `CONDITIONAL_JUMP`
<a id="insn-00ba9ce4"></a> `00ba9ce4` | `1f 05 7d f2` | tst x8,#0x18 | `FALL_THROUGH`
<a id="insn-00ba9ce8"></a> `00ba9ce8` | `00 03 00 54` | b.eq 0x00ba9d48 | `CONDITIONAL_JUMP`
<a id="insn-00ba9cec"></a> `00ba9cec` | `60 0c 01 0e` | dup v0.8B,w3 | `FALL_THROUGH`
<a id="insn-00ba9cf0"></a> `00ba9cf0` | `e1 07 03 4f` | movi v1.4S,#0x7f | `FALL_THROUGH`
<a id="insn-00ba9cf4"></a> `00ba9cf4` | `0c ed 7d 92` | and x12,x8,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba9cf8"></a> `00ba9cf8` | `2b b8 ff f0` | adrp x11,0x2b0000 | `FALL_THROUGH`
<a id="insn-00ba9cfc"></a> `00ba9cfc` | `0a 08 0c 8b` | add x10,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba9d00"></a> `00ba9d00` | `0d 08 09 8b` | add x13,x0,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba9d04"></a> `00ba9d04` | `62 95 c3 3d` | ldr q2,[x11, #0xe50] | `FALL_THROUGH`
<a id="insn-00ba9d08"></a> `00ba9d08` | `8b 00 0c 8b` | add x11,x4,x12 | `FALL_THROUGH`
<a id="insn-00ba9d0c"></a> `00ba9d0c` | `8e 00 09 8b` | add x14,x4,x9 | `FALL_THROUGH`
<a id="insn-00ba9d10"></a> `00ba9d10` | `29 01 0c cb` | sub x9,x9,x12 | `FALL_THROUGH`
<a id="insn-00ba9d14"></a> `00ba9d14` | `a3 11 c1 ac` | ldp q3,q4,[x13], #0x20 | `FALL_THROUGH`
<a id="insn-00ba9d18"></a> `00ba9d18` | `29 21 00 b1` | adds x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00ba9d1c"></a> `00ba9d1c` | `85 34 a1 6e` | cmhi v5.4S,v4.4S,v1.4S | `FALL_THROUGH`
<a id="insn-00ba9d20"></a> `00ba9d20` | `66 34 a1 6e` | cmhi v6.4S,v3.4S,v1.4S | `FALL_THROUGH`
<a id="insn-00ba9d24"></a> `00ba9d24` | `63 20 02 4e` | tbl v3.16B,{v3.16B,v4.16B},v2.16B | `FALL_THROUGH`
<a id="insn-00ba9d28"></a> `00ba9d28` | `c5 18 45 4e` | uzp1 v5.8H,v6.8H,v5.8H | `FALL_THROUGH`
<a id="insn-00ba9d2c"></a> `00ba9d2c` | `a5 28 21 0e` | xtn v5.8B,v5.8H | `FALL_THROUGH`
<a id="insn-00ba9d30"></a> `00ba9d30` | `03 1c a5 2e` | bit v3.8B,v0.8B,v5.8B | `FALL_THROUGH`
<a id="insn-00ba9d34"></a> `00ba9d34` | `c3 85 00 fc` | str d3,[x14], #0x8 | `FALL_THROUGH`
<a id="insn-00ba9d38"></a> `00ba9d38` | `e1 fe ff 54` | b.ne 0x00ba9d14 | `CONDITIONAL_JUMP`
<a id="insn-00ba9d3c"></a> `00ba9d3c` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00ba9d40"></a> `00ba9d40` | `c1 f6 ff 54` | b.ne 0x00ba9c18 | `CONDITIONAL_JUMP`
<a id="insn-00ba9d44"></a> `00ba9d44` | `bb ff ff 17` | b 0x00ba9c30 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba9d48"></a> `00ba9d48` | `0a 08 09 8b` | add x10,x0,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba9d4c"></a> `00ba9d4c` | `8b 00 09 8b` | add x11,x4,x9 | `FALL_THROUGH`
<a id="insn-00ba9d50"></a> `00ba9d50` | `b2 ff ff 17` | b 0x00ba9c18 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00ba9bcc`](#insn-00ba9bcc) 範囲 `[['00ba9bcc', '00ba9bdb']]`
  - `CONDITIONAL_JUMP` [`00ba9bd8`](#insn-00ba9bd8) → [`00ba9c34`](#insn-00ba9c34)
  - `FALL_THROUGH` [`00ba9bd8`](#insn-00ba9bd8) → [`00ba9bdc`](#insn-00ba9bdc)
- ブロック [`00ba9bdc`](#insn-00ba9bdc) 範囲 `[['00ba9bdc', '00ba9beb']]`
  - `CONDITIONAL_JUMP` [`00ba9be8`](#insn-00ba9be8) → [`00ba9c10`](#insn-00ba9c10)
  - `FALL_THROUGH` [`00ba9be8`](#insn-00ba9be8) → [`00ba9bec`](#insn-00ba9bec)
- ブロック [`00ba9bec`](#insn-00ba9bec) 範囲 `[['00ba9bec', '00ba9bff']]`
  - `CONDITIONAL_JUMP` [`00ba9bfc`](#insn-00ba9bfc) → [`00ba9c38`](#insn-00ba9c38)
  - `FALL_THROUGH` [`00ba9bfc`](#insn-00ba9bfc) → [`00ba9c00`](#insn-00ba9c00)
- ブロック [`00ba9c00`](#insn-00ba9c00) 範囲 `[['00ba9c00', '00ba9c0f']]`
  - `CONDITIONAL_JUMP` [`00ba9c0c`](#insn-00ba9c0c) → [`00ba9c38`](#insn-00ba9c38)
  - `FALL_THROUGH` [`00ba9c0c`](#insn-00ba9c0c) → [`00ba9c10`](#insn-00ba9c10)
- ブロック [`00ba9c10`](#insn-00ba9c10) 範囲 `[['00ba9c10', '00ba9c17']]`
  - `FALL_THROUGH` [`00ba9c14`](#insn-00ba9c14) → [`00ba9c18`](#insn-00ba9c18)
- ブロック [`00ba9c18`](#insn-00ba9c18) 範囲 `[['00ba9c18', '00ba9c2f']]`
  - `CONDITIONAL_JUMP` [`00ba9c2c`](#insn-00ba9c2c) → [`00ba9c18`](#insn-00ba9c18)
  - `FALL_THROUGH` [`00ba9c2c`](#insn-00ba9c2c) → [`00ba9c30`](#insn-00ba9c30)
- ブロック [`00ba9c30`](#insn-00ba9c30) 範囲 `[['00ba9c30', '00ba9c33']]`
  - `FALL_THROUGH` [`00ba9c30`](#insn-00ba9c30) → [`00ba9c34`](#insn-00ba9c34)
- ブロック [`00ba9c34`](#insn-00ba9c34) 範囲 `[['00ba9c34', '00ba9c37']]`
- ブロック [`00ba9c38`](#insn-00ba9c38) 範囲 `[['00ba9c38', '00ba9c47']]`
  - `CONDITIONAL_JUMP` [`00ba9c44`](#insn-00ba9c44) → [`00ba9c50`](#insn-00ba9c50)
  - `FALL_THROUGH` [`00ba9c44`](#insn-00ba9c44) → [`00ba9c48`](#insn-00ba9c48)
- ブロック [`00ba9c48`](#insn-00ba9c48) 範囲 `[['00ba9c48', '00ba9c4f']]`
  - `UNCONDITIONAL_JUMP` [`00ba9c4c`](#insn-00ba9c4c) → [`00ba9cec`](#insn-00ba9cec)
- ブロック [`00ba9c50`](#insn-00ba9c50) 範囲 `[['00ba9c50', '00ba9c6f']]`
  - `FALL_THROUGH` [`00ba9c6c`](#insn-00ba9c6c) → [`00ba9c70`](#insn-00ba9c70)
- ブロック [`00ba9c70`](#insn-00ba9c70) 範囲 `[['00ba9c70', '00ba9cdb']]`
  - `CONDITIONAL_JUMP` [`00ba9cd8`](#insn-00ba9cd8) → [`00ba9c70`](#insn-00ba9c70)
  - `FALL_THROUGH` [`00ba9cd8`](#insn-00ba9cd8) → [`00ba9cdc`](#insn-00ba9cdc)
- ブロック [`00ba9cdc`](#insn-00ba9cdc) 範囲 `[['00ba9cdc', '00ba9ce3']]`
  - `CONDITIONAL_JUMP` [`00ba9ce0`](#insn-00ba9ce0) → [`00ba9c30`](#insn-00ba9c30)
  - `FALL_THROUGH` [`00ba9ce0`](#insn-00ba9ce0) → [`00ba9ce4`](#insn-00ba9ce4)
- ブロック [`00ba9ce4`](#insn-00ba9ce4) 範囲 `[['00ba9ce4', '00ba9ceb']]`
  - `CONDITIONAL_JUMP` [`00ba9ce8`](#insn-00ba9ce8) → [`00ba9d48`](#insn-00ba9d48)
  - `FALL_THROUGH` [`00ba9ce8`](#insn-00ba9ce8) → [`00ba9cec`](#insn-00ba9cec)
- ブロック [`00ba9cec`](#insn-00ba9cec) 範囲 `[['00ba9cec', '00ba9d13']]`
  - `FALL_THROUGH` [`00ba9d10`](#insn-00ba9d10) → [`00ba9d14`](#insn-00ba9d14)
- ブロック [`00ba9d14`](#insn-00ba9d14) 範囲 `[['00ba9d14', '00ba9d3b']]`
  - `CONDITIONAL_JUMP` [`00ba9d38`](#insn-00ba9d38) → [`00ba9d14`](#insn-00ba9d14)
  - `FALL_THROUGH` [`00ba9d38`](#insn-00ba9d38) → [`00ba9d3c`](#insn-00ba9d3c)
- ブロック [`00ba9d3c`](#insn-00ba9d3c) 範囲 `[['00ba9d3c', '00ba9d43']]`
  - `CONDITIONAL_JUMP` [`00ba9d40`](#insn-00ba9d40) → [`00ba9c18`](#insn-00ba9c18)
  - `FALL_THROUGH` [`00ba9d40`](#insn-00ba9d40) → [`00ba9d44`](#insn-00ba9d44)
- ブロック [`00ba9d44`](#insn-00ba9d44) 範囲 `[['00ba9d44', '00ba9d47']]`
  - `UNCONDITIONAL_JUMP` [`00ba9d44`](#insn-00ba9d44) → [`00ba9c30`](#insn-00ba9c30)
- ブロック [`00ba9d48`](#insn-00ba9d48) 範囲 `[['00ba9d48', '00ba9d53']]`
  - `UNCONDITIONAL_JUMP` [`00ba9d50`](#insn-00ba9d50) → [`00ba9c18`](#insn-00ba9c18)

## 命令位置別の参照

- [`00ba9bd8`](#insn-00ba9bd8) → [`00ba9c34`](#insn-00ba9c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9be8`](#insn-00ba9be8) → [`00ba9c10`](#insn-00ba9c10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9bfc`](#insn-00ba9bfc) → [`00ba9c38`](#insn-00ba9c38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9c0c`](#insn-00ba9c0c) → [`00ba9c38`](#insn-00ba9c38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9c2c`](#insn-00ba9c2c) → [`00ba9c18`](#insn-00ba9c18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9c44`](#insn-00ba9c44) → [`00ba9c50`](#insn-00ba9c50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9c4c`](#insn-00ba9c4c) → [`00ba9cec`](#insn-00ba9cec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9c60`](#insn-00ba9c60) → `002b1600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9cd8`](#insn-00ba9cd8) → [`00ba9c70`](#insn-00ba9c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9ce0`](#insn-00ba9ce0) → [`00ba9c30`](#insn-00ba9c30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9ce8`](#insn-00ba9ce8) → [`00ba9d48`](#insn-00ba9d48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9d04`](#insn-00ba9d04) → `002b0e50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9d38`](#insn-00ba9d38) → [`00ba9d14`](#insn-00ba9d14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9d40`](#insn-00ba9d40) → [`00ba9c18`](#insn-00ba9c18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9d44`](#insn-00ba9d44) → [`00ba9c30`](#insn-00ba9c30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba9d50`](#insn-00ba9d50) → [`00ba9c18`](#insn-00ba9c18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba9bd8`](#insn-00ba9bd8)

~~~json
{
  "source": "00ba9bd8",
  "target": "00ba9c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9be8`](#insn-00ba9be8)

~~~json
{
  "source": "00ba9be8",
  "target": "00ba9c10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9bfc`](#insn-00ba9bfc)

~~~json
{
  "source": "00ba9bfc",
  "target": "00ba9c38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9c0c`](#insn-00ba9c0c)

~~~json
{
  "source": "00ba9c0c",
  "target": "00ba9c38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9c2c`](#insn-00ba9c2c)

~~~json
{
  "source": "00ba9c2c",
  "target": "00ba9c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9c44`](#insn-00ba9c44)

~~~json
{
  "source": "00ba9c44",
  "target": "00ba9c50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9c4c`](#insn-00ba9c4c)

~~~json
{
  "source": "00ba9c4c",
  "target": "00ba9cec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9c60`](#insn-00ba9c60)

~~~json
{
  "source": "00ba9c60",
  "target": "002b1600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9cd8`](#insn-00ba9cd8)

~~~json
{
  "source": "00ba9cd8",
  "target": "00ba9c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9ce0`](#insn-00ba9ce0)

~~~json
{
  "source": "00ba9ce0",
  "target": "00ba9c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9ce8`](#insn-00ba9ce8)

~~~json
{
  "source": "00ba9ce8",
  "target": "00ba9d48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9d04`](#insn-00ba9d04)

~~~json
{
  "source": "00ba9d04",
  "target": "002b0e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9d38`](#insn-00ba9d38)

~~~json
{
  "source": "00ba9d38",
  "target": "00ba9d14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9d40`](#insn-00ba9d40)

~~~json
{
  "source": "00ba9d40",
  "target": "00ba9c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9d44`](#insn-00ba9d44)

~~~json
{
  "source": "00ba9d44",
  "target": "00ba9c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba9d50`](#insn-00ba9d50)

~~~json
{
  "source": "00ba9d50",
  "target": "00ba9c18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
