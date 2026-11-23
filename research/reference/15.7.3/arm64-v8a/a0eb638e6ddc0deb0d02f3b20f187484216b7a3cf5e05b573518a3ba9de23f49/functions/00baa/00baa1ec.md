# 00baa1ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baa124`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baa124.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-88cde726d56f4a8acf4e6a9471f67bee)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baa230`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa230.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0022.md#compare-03acaa7712786d50971893de3c9a671f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baa1ec",
  "name": "_ZNKSt6__ndk15ctypeIcE9do_narrowEPKcS3_cPc",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9634302ab696631af5c05235d59f45d9d5fa1fc6229bc6ca9db34fd349e71ce",
  "source_text_sha256": "e9634302ab696631af5c05235d59f45d9d5fa1fc6229bc6ca9db34fd349e71ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baa1ec",
        "00baa2e3"
      ]
    ],
    "bytes_sha256": "2a406a42e964d0e0d508dc3aa65d6f2353ae00e56d3a70dd918793bb5f9873ce",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
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

## 疑似コード / UTF-8 6556 bytes

~~~c

byte * _ZNKSt6__ndk15ctypeIcE9do_narrowEPKcS3_cPc
                 (undefined8 param_1,byte *param_2,byte *param_3,byte param_4,byte *param_5)

{
  byte bVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  byte bVar12;
  byte bVar13;
  byte bVar14;
  byte bVar15;
  byte bVar16;
  byte bVar17;
  byte bVar18;
  byte bVar19;
  byte bVar20;
  byte bVar21;
  byte bVar22;
  byte bVar23;
  byte bVar24;
  byte bVar25;
  byte bVar26;
  byte bVar27;
  byte bVar28;
  byte bVar29;
  byte bVar30;
  byte bVar31;
  byte bVar32;
  ulong uVar33;
  byte *pbVar34;
  byte *pbVar35;
  ulong uVar36;
  long lVar37;
  ulong uVar38;
  ulong *puVar39;
  ulong *puVar40;
  
  if (param_2 == param_3) {
    return param_2;
  }
  uVar33 = (long)param_3 - (long)param_2;
  if ((7 < uVar33) && (0x1f < (ulong)((long)param_5 - (long)param_2))) {
    if (uVar33 < 0x20) {
      uVar36 = 0;
    }
    else {
      uVar36 = uVar33 & 0xffffffffffffffe0;
      pbVar35 = param_2 + 0x10;
      pbVar34 = param_5 + 0x10;
      uVar38 = uVar36;
      do {
        bVar1 = pbVar35[-0x10];
        bVar2 = pbVar35[-0xf];
        bVar3 = pbVar35[-0xe];
        bVar4 = pbVar35[-0xd];
        bVar5 = pbVar35[-0xc];
        bVar6 = pbVar35[-0xb];
        bVar7 = pbVar35[-10];
        bVar8 = pbVar35[-9];
        bVar9 = pbVar35[-8];
        bVar10 = pbVar35[-7];
        bVar11 = pbVar35[-6];
        bVar12 = pbVar35[-5];
        bVar13 = pbVar35[-4];
        bVar14 = pbVar35[-3];
        bVar15 = pbVar35[-2];
        bVar16 = pbVar35[-1];
        bVar17 = *pbVar35;
        bVar18 = pbVar35[1];
        bVar19 = pbVar35[2];
        bVar20 = pbVar35[3];
        bVar21 = pbVar35[4];
        bVar22 = pbVar35[5];
        bVar23 = pbVar35[6];
        bVar24 = pbVar35[7];
        bVar25 = pbVar35[8];
        bVar26 = pbVar35[9];
        bVar27 = pbVar35[10];
        bVar28 = pbVar35[0xb];
        bVar29 = pbVar35[0xc];
        bVar30 = pbVar35[0xd];
        bVar31 = pbVar35[0xe];
        bVar32 = pbVar35[0xf];
        uVar38 = uVar38 - 0x20;
        pbVar35 = pbVar35 + 0x20;
        pbVar34[-8] = bVar9 ^ (bVar9 ^ param_4) & -((char)bVar9 < '\0');
        pbVar34[-7] = bVar10 ^ (bVar10 ^ param_4) & -((char)bVar10 < '\0');
        pbVar34[-6] = bVar11 ^ (bVar11 ^ param_4) & -((char)bVar11 < '\0');
        pbVar34[-5] = bVar12 ^ (bVar12 ^ param_4) & -((char)bVar12 < '\0');
        pbVar34[-4] = bVar13 ^ (bVar13 ^ param_4) & -((char)bVar13 < '\0');
        pbVar34[-3] = bVar14 ^ (bVar14 ^ param_4) & -((char)bVar14 < '\0');
        pbVar34[-2] = bVar15 ^ (bVar15 ^ param_4) & -((char)bVar15 < '\0');
        pbVar34[-1] = bVar16 ^ (bVar16 ^ param_4) & -((char)bVar16 < '\0');
        pbVar34[-0x10] = bVar1 ^ (bVar1 ^ param_4) & -((char)bVar1 < '\0');
        pbVar34[-0xf] = bVar2 ^ (bVar2 ^ param_4) & -((char)bVar2 < '\0');
        pbVar34[-0xe] = bVar3 ^ (bVar3 ^ param_4) & -((char)bVar3 < '\0');
        pbVar34[-0xd] = bVar4 ^ (bVar4 ^ param_4) & -((char)bVar4 < '\0');
        pbVar34[-0xc] = bVar5 ^ (bVar5 ^ param_4) & -((char)bVar5 < '\0');
        pbVar34[-0xb] = bVar6 ^ (bVar6 ^ param_4) & -((char)bVar6 < '\0');
        pbVar34[-10] = bVar7 ^ (bVar7 ^ param_4) & -((char)bVar7 < '\0');
        pbVar34[-9] = bVar8 ^ (bVar8 ^ param_4) & -((char)bVar8 < '\0');
        pbVar34[8] = bVar25 ^ (bVar25 ^ param_4) & -((char)bVar25 < '\0');
        pbVar34[9] = bVar26 ^ (bVar26 ^ param_4) & -((char)bVar26 < '\0');
        pbVar34[10] = bVar27 ^ (bVar27 ^ param_4) & -((char)bVar27 < '\0');
        pbVar34[0xb] = bVar28 ^ (bVar28 ^ param_4) & -((char)bVar28 < '\0');
        pbVar34[0xc] = bVar29 ^ (bVar29 ^ param_4) & -((char)bVar29 < '\0');
        pbVar34[0xd] = bVar30 ^ (bVar30 ^ param_4) & -((char)bVar30 < '\0');
        pbVar34[0xe] = bVar31 ^ (bVar31 ^ param_4) & -((char)bVar31 < '\0');
        pbVar34[0xf] = bVar32 ^ (bVar32 ^ param_4) & -((char)bVar32 < '\0');
        *pbVar34 = bVar17 ^ (bVar17 ^ param_4) & -((char)bVar17 < '\0');
        pbVar34[1] = bVar18 ^ (bVar18 ^ param_4) & -((char)bVar18 < '\0');
        pbVar34[2] = bVar19 ^ (bVar19 ^ param_4) & -((char)bVar19 < '\0');
        pbVar34[3] = bVar20 ^ (bVar20 ^ param_4) & -((char)bVar20 < '\0');
        pbVar34[4] = bVar21 ^ (bVar21 ^ param_4) & -((char)bVar21 < '\0');
        pbVar34[5] = bVar22 ^ (bVar22 ^ param_4) & -((char)bVar22 < '\0');
        pbVar34[6] = bVar23 ^ (bVar23 ^ param_4) & -((char)bVar23 < '\0');
        pbVar34[7] = bVar24 ^ (bVar24 ^ param_4) & -((char)bVar24 < '\0');
        pbVar34 = pbVar34 + 0x20;
      } while (uVar38 != 0);
      if (uVar33 == uVar36) {
        return param_3;
      }
      if ((uVar33 & 0x18) == 0) {
        param_2 = param_2 + uVar36;
        param_5 = param_5 + uVar36;
        goto LAB_00baa2c4;
      }
    }
    uVar38 = uVar33 & 0xfffffffffffffff8;
    lVar37 = uVar36 - uVar38;
    puVar39 = (ulong *)(param_2 + uVar36);
    puVar40 = (ulong *)(param_5 + uVar36);
    do {
      uVar36 = *puVar39;
      lVar37 = lVar37 + 8;
      *puVar40 = uVar36 ^ (uVar36 ^ CONCAT17(param_4,CONCAT16(param_4,CONCAT15(param_4,CONCAT14(
                                                  param_4,CONCAT13(param_4,CONCAT12(param_4,CONCAT11
                                                  (param_4,param_4)))))))) &
                          CONCAT17(-((long)uVar36 < 0),
                                   CONCAT16(-((char)(uVar36 >> 0x30) < '\0'),
                                            CONCAT15(-((char)(uVar36 >> 0x28) < '\0'),
                                                     CONCAT14(-((char)(uVar36 >> 0x20) < '\0'),
                                                              CONCAT13(-((char)(uVar36 >> 0x18) <
                                                                        '\0'),CONCAT12(-((char)(
                                                  uVar36 >> 0x10) < '\0'),
                                                  CONCAT11(-((char)(uVar36 >> 8) < '\0'),
                                                           -((char)uVar36 < '\0'))))))));
      puVar39 = puVar39 + 1;
      puVar40 = puVar40 + 1;
    } while (lVar37 != 0);
    param_5 = param_5 + uVar38;
    param_2 = param_2 + uVar38;
    if (uVar33 == uVar38) {
      return param_3;
    }
  }
LAB_00baa2c4:
  do {
    pbVar35 = param_2 + 1;
    bVar1 = param_4;
    if (-1 < (char)*param_2) {
      bVar1 = *param_2;
    }
    *param_5 = bVar1;
    param_5 = param_5 + 1;
    param_2 = pbVar35;
  } while (pbVar35 != param_3);
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baa1ec"></a> `00baa1ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baa1f0"></a> `00baa1f0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00baa1f4"></a> `00baa1f4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00baa1f8"></a> `00baa1f8` | `40 07 00 54` | b.eq 0x00baa2e0 | `CONDITIONAL_JUMP`
<a id="insn-00baa1fc"></a> `00baa1fc` | `48 00 00 cb` | sub x8,x2,x0 | `FALL_THROUGH`
<a id="insn-00baa200"></a> `00baa200` | `1f 21 00 f1` | cmp x8,#0x8 | `FALL_THROUGH`
<a id="insn-00baa204"></a> `00baa204` | `03 01 00 54` | b.cc 0x00baa224 | `CONDITIONAL_JUMP`
<a id="insn-00baa208"></a> `00baa208` | `89 00 00 cb` | sub x9,x4,x0 | `FALL_THROUGH`
<a id="insn-00baa20c"></a> `00baa20c` | `3f 81 00 f1` | cmp x9,#0x20 | `FALL_THROUGH`
<a id="insn-00baa210"></a> `00baa210` | `a3 00 00 54` | b.cc 0x00baa224 | `CONDITIONAL_JUMP`
<a id="insn-00baa214"></a> `00baa214` | `1f 81 00 f1` | cmp x8,#0x20 | `FALL_THROUGH`
<a id="insn-00baa218"></a> `00baa218` | `c2 00 00 54` | b.cs 0x00baa230 | `CONDITIONAL_JUMP`
<a id="insn-00baa21c"></a> `00baa21c` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00baa220"></a> `00baa220` | `17 00 00 14` | b 0x00baa27c | `UNCONDITIONAL_JUMP`
<a id="insn-00baa224"></a> `00baa224` | `e9 03 04 aa` | mov x9,x4 | `FALL_THROUGH`
<a id="insn-00baa228"></a> `00baa228` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00baa22c"></a> `00baa22c` | `26 00 00 14` | b 0x00baa2c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baa230"></a> `00baa230` | `60 0c 01 4e` | dup v0.16B,w3 | `FALL_THROUGH`
<a id="insn-00baa234"></a> `00baa234` | `0b e9 7b 92` | and x11,x8,#-0x20 | `FALL_THROUGH`
<a id="insn-00baa238"></a> `00baa238` | `09 40 00 91` | add x9,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00baa23c"></a> `00baa23c` | `8a 40 00 91` | add x10,x4,#0x10 | `FALL_THROUGH`
<a id="insn-00baa240"></a> `00baa240` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00baa244"></a> `00baa244` | `21 89 7f ad` | ldp q1,q2,[x9, #-0x10] | `FALL_THROUGH`
<a id="insn-00baa248"></a> `00baa248` | `8c 81 00 f1` | subs x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00baa24c"></a> `00baa24c` | `29 81 00 91` | add x9,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00baa250"></a> `00baa250` | `23 a8 20 4e` | cmlt v3.16B,v1.16B,#0 | `FALL_THROUGH`
<a id="insn-00baa254"></a> `00baa254` | `44 a8 20 4e` | cmlt v4.16B,v2.16B,#0 | `FALL_THROUGH`
<a id="insn-00baa258"></a> `00baa258` | `01 1c a3 6e` | bit v1.16B,v0.16B,v3.16B | `FALL_THROUGH`
<a id="insn-00baa25c"></a> `00baa25c` | `02 1c a4 6e` | bit v2.16B,v0.16B,v4.16B | `FALL_THROUGH`
<a id="insn-00baa260"></a> `00baa260` | `41 89 3f ad` | stp q1,q2,[x10, #-0x10] | `FALL_THROUGH`
<a id="insn-00baa264"></a> `00baa264` | `4a 81 00 91` | add x10,x10,#0x20 | `FALL_THROUGH`
<a id="insn-00baa268"></a> `00baa268` | `e1 fe ff 54` | b.ne 0x00baa244 | `CONDITIONAL_JUMP`
<a id="insn-00baa26c"></a> `00baa26c` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-00baa270"></a> `00baa270` | `60 03 00 54` | b.eq 0x00baa2dc | `CONDITIONAL_JUMP`
<a id="insn-00baa274"></a> `00baa274` | `1f 05 7d f2` | tst x8,#0x18 | `FALL_THROUGH`
<a id="insn-00baa278"></a> `00baa278` | `20 02 00 54` | b.eq 0x00baa2bc | `CONDITIONAL_JUMP`
<a id="insn-00baa27c"></a> `00baa27c` | `60 0c 01 0e` | dup v0.8B,w3 | `FALL_THROUGH`
<a id="insn-00baa280"></a> `00baa280` | `0c f1 7d 92` | and x12,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00baa284"></a> `00baa284` | `0d 00 0b 8b` | add x13,x0,x11 | `FALL_THROUGH`
<a id="insn-00baa288"></a> `00baa288` | `89 00 0c 8b` | add x9,x4,x12 | `FALL_THROUGH`
<a id="insn-00baa28c"></a> `00baa28c` | `0a 00 0c 8b` | add x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00baa290"></a> `00baa290` | `8e 00 0b 8b` | add x14,x4,x11 | `FALL_THROUGH`
<a id="insn-00baa294"></a> `00baa294` | `6b 01 0c cb` | sub x11,x11,x12 | `FALL_THROUGH`
<a id="insn-00baa298"></a> `00baa298` | `a1 85 40 fc` | ldr d1,[x13], #0x8 | `FALL_THROUGH`
<a id="insn-00baa29c"></a> `00baa29c` | `6b 21 00 b1` | adds x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00baa2a0"></a> `00baa2a0` | `22 a8 20 0e` | cmlt v2.8B,v1.8B,#0 | `FALL_THROUGH`
<a id="insn-00baa2a4"></a> `00baa2a4` | `01 1c a2 2e` | bit v1.8B,v0.8B,v2.8B | `FALL_THROUGH`
<a id="insn-00baa2a8"></a> `00baa2a8` | `c1 85 00 fc` | str d1,[x14], #0x8 | `FALL_THROUGH`
<a id="insn-00baa2ac"></a> `00baa2ac` | `61 ff ff 54` | b.ne 0x00baa298 | `CONDITIONAL_JUMP`
<a id="insn-00baa2b0"></a> `00baa2b0` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00baa2b4"></a> `00baa2b4` | `81 00 00 54` | b.ne 0x00baa2c4 | `CONDITIONAL_JUMP`
<a id="insn-00baa2b8"></a> `00baa2b8` | `09 00 00 14` | b 0x00baa2dc | `UNCONDITIONAL_JUMP`
<a id="insn-00baa2bc"></a> `00baa2bc` | `0a 00 0b 8b` | add x10,x0,x11 | `FALL_THROUGH`
<a id="insn-00baa2c0"></a> `00baa2c0` | `89 00 0b 8b` | add x9,x4,x11 | `FALL_THROUGH`
<a id="insn-00baa2c4"></a> `00baa2c4` | `48 15 c0 38` | ldrsb w8,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00baa2c8"></a> `00baa2c8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00baa2cc"></a> `00baa2cc` | `68 b0 88 1a` | csel w8,w3,w8,lt | `FALL_THROUGH`
<a id="insn-00baa2d0"></a> `00baa2d0` | `5f 01 02 eb` | cmp x10,x2 | `FALL_THROUGH`
<a id="insn-00baa2d4"></a> `00baa2d4` | `28 15 00 38` | strb w8,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00baa2d8"></a> `00baa2d8` | `61 ff ff 54` | b.ne 0x00baa2c4 | `CONDITIONAL_JUMP`
<a id="insn-00baa2dc"></a> `00baa2dc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00baa2e0"></a> `00baa2e0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baa1ec`](#insn-00baa1ec) 範囲 `[['00baa1ec', '00baa1fb']]`
  - `CONDITIONAL_JUMP` [`00baa1f8`](#insn-00baa1f8) → [`00baa2e0`](#insn-00baa2e0)
  - `FALL_THROUGH` [`00baa1f8`](#insn-00baa1f8) → [`00baa1fc`](#insn-00baa1fc)
- ブロック [`00baa1fc`](#insn-00baa1fc) 範囲 `[['00baa1fc', '00baa207']]`
  - `CONDITIONAL_JUMP` [`00baa204`](#insn-00baa204) → [`00baa224`](#insn-00baa224)
  - `FALL_THROUGH` [`00baa204`](#insn-00baa204) → [`00baa208`](#insn-00baa208)
- ブロック [`00baa208`](#insn-00baa208) 範囲 `[['00baa208', '00baa213']]`
  - `CONDITIONAL_JUMP` [`00baa210`](#insn-00baa210) → [`00baa224`](#insn-00baa224)
  - `FALL_THROUGH` [`00baa210`](#insn-00baa210) → [`00baa214`](#insn-00baa214)
- ブロック [`00baa214`](#insn-00baa214) 範囲 `[['00baa214', '00baa21b']]`
  - `CONDITIONAL_JUMP` [`00baa218`](#insn-00baa218) → [`00baa230`](#insn-00baa230)
  - `FALL_THROUGH` [`00baa218`](#insn-00baa218) → [`00baa21c`](#insn-00baa21c)
- ブロック [`00baa21c`](#insn-00baa21c) 範囲 `[['00baa21c', '00baa223']]`
  - `UNCONDITIONAL_JUMP` [`00baa220`](#insn-00baa220) → [`00baa27c`](#insn-00baa27c)
- ブロック [`00baa224`](#insn-00baa224) 範囲 `[['00baa224', '00baa22f']]`
  - `UNCONDITIONAL_JUMP` [`00baa22c`](#insn-00baa22c) → [`00baa2c4`](#insn-00baa2c4)
- ブロック [`00baa230`](#insn-00baa230) 範囲 `[['00baa230', '00baa243']]`
  - `FALL_THROUGH` [`00baa240`](#insn-00baa240) → [`00baa244`](#insn-00baa244)
- ブロック [`00baa244`](#insn-00baa244) 範囲 `[['00baa244', '00baa26b']]`
  - `CONDITIONAL_JUMP` [`00baa268`](#insn-00baa268) → [`00baa244`](#insn-00baa244)
  - `FALL_THROUGH` [`00baa268`](#insn-00baa268) → [`00baa26c`](#insn-00baa26c)
- ブロック [`00baa26c`](#insn-00baa26c) 範囲 `[['00baa26c', '00baa273']]`
  - `CONDITIONAL_JUMP` [`00baa270`](#insn-00baa270) → [`00baa2dc`](#insn-00baa2dc)
  - `FALL_THROUGH` [`00baa270`](#insn-00baa270) → [`00baa274`](#insn-00baa274)
- ブロック [`00baa274`](#insn-00baa274) 範囲 `[['00baa274', '00baa27b']]`
  - `CONDITIONAL_JUMP` [`00baa278`](#insn-00baa278) → [`00baa2bc`](#insn-00baa2bc)
  - `FALL_THROUGH` [`00baa278`](#insn-00baa278) → [`00baa27c`](#insn-00baa27c)
- ブロック [`00baa27c`](#insn-00baa27c) 範囲 `[['00baa27c', '00baa297']]`
  - `FALL_THROUGH` [`00baa294`](#insn-00baa294) → [`00baa298`](#insn-00baa298)
- ブロック [`00baa298`](#insn-00baa298) 範囲 `[['00baa298', '00baa2af']]`
  - `CONDITIONAL_JUMP` [`00baa2ac`](#insn-00baa2ac) → [`00baa298`](#insn-00baa298)
  - `FALL_THROUGH` [`00baa2ac`](#insn-00baa2ac) → [`00baa2b0`](#insn-00baa2b0)
- ブロック [`00baa2b0`](#insn-00baa2b0) 範囲 `[['00baa2b0', '00baa2b7']]`
  - `CONDITIONAL_JUMP` [`00baa2b4`](#insn-00baa2b4) → [`00baa2c4`](#insn-00baa2c4)
  - `FALL_THROUGH` [`00baa2b4`](#insn-00baa2b4) → [`00baa2b8`](#insn-00baa2b8)
- ブロック [`00baa2b8`](#insn-00baa2b8) 範囲 `[['00baa2b8', '00baa2bb']]`
  - `UNCONDITIONAL_JUMP` [`00baa2b8`](#insn-00baa2b8) → [`00baa2dc`](#insn-00baa2dc)
- ブロック [`00baa2bc`](#insn-00baa2bc) 範囲 `[['00baa2bc', '00baa2c3']]`
  - `FALL_THROUGH` [`00baa2c0`](#insn-00baa2c0) → [`00baa2c4`](#insn-00baa2c4)
- ブロック [`00baa2c4`](#insn-00baa2c4) 範囲 `[['00baa2c4', '00baa2db']]`
  - `CONDITIONAL_JUMP` [`00baa2d8`](#insn-00baa2d8) → [`00baa2c4`](#insn-00baa2c4)
  - `FALL_THROUGH` [`00baa2d8`](#insn-00baa2d8) → [`00baa2dc`](#insn-00baa2dc)
- ブロック [`00baa2dc`](#insn-00baa2dc) 範囲 `[['00baa2dc', '00baa2df']]`
  - `FALL_THROUGH` [`00baa2dc`](#insn-00baa2dc) → [`00baa2e0`](#insn-00baa2e0)
- ブロック [`00baa2e0`](#insn-00baa2e0) 範囲 `[['00baa2e0', '00baa2e3']]`

## 命令位置別の参照

- [`00baa1f8`](#insn-00baa1f8) → [`00baa2e0`](#insn-00baa2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa204`](#insn-00baa204) → [`00baa224`](#insn-00baa224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa210`](#insn-00baa210) → [`00baa224`](#insn-00baa224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa218`](#insn-00baa218) → [`00baa230`](#insn-00baa230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa220`](#insn-00baa220) → [`00baa27c`](#insn-00baa27c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa22c`](#insn-00baa22c) → [`00baa2c4`](#insn-00baa2c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa268`](#insn-00baa268) → [`00baa244`](#insn-00baa244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa270`](#insn-00baa270) → [`00baa2dc`](#insn-00baa2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa278`](#insn-00baa278) → [`00baa2bc`](#insn-00baa2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa2ac`](#insn-00baa2ac) → [`00baa298`](#insn-00baa298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa2b4`](#insn-00baa2b4) → [`00baa2c4`](#insn-00baa2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa2b8`](#insn-00baa2b8) → [`00baa2dc`](#insn-00baa2dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa2d8`](#insn-00baa2d8) → [`00baa2c4`](#insn-00baa2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baa1f8`](#insn-00baa1f8)

~~~json
{
  "source": "00baa1f8",
  "target": "00baa2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa204`](#insn-00baa204)

~~~json
{
  "source": "00baa204",
  "target": "00baa224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa210`](#insn-00baa210)

~~~json
{
  "source": "00baa210",
  "target": "00baa224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa218`](#insn-00baa218)

~~~json
{
  "source": "00baa218",
  "target": "00baa230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa220`](#insn-00baa220)

~~~json
{
  "source": "00baa220",
  "target": "00baa27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa22c`](#insn-00baa22c)

~~~json
{
  "source": "00baa22c",
  "target": "00baa2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa268`](#insn-00baa268)

~~~json
{
  "source": "00baa268",
  "target": "00baa244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa270`](#insn-00baa270)

~~~json
{
  "source": "00baa270",
  "target": "00baa2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa278`](#insn-00baa278)

~~~json
{
  "source": "00baa278",
  "target": "00baa2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa2ac`](#insn-00baa2ac)

~~~json
{
  "source": "00baa2ac",
  "target": "00baa298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa2b4`](#insn-00baa2b4)

~~~json
{
  "source": "00baa2b4",
  "target": "00baa2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa2b8`](#insn-00baa2b8)

~~~json
{
  "source": "00baa2b8",
  "target": "00baa2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa2d8`](#insn-00baa2d8)

~~~json
{
  "source": "00baa2d8",
  "target": "00baa2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
