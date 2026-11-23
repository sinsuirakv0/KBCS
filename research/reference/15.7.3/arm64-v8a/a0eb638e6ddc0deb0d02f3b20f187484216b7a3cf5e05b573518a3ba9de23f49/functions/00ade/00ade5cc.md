# 00ade5cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ade504`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ade/00ade504.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-7ed61e8af50c720b4e8a96e64135ba06)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ade610`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-e5a573e7d94c1b492b5d21ae46721867)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ade5cc",
  "name": "FUN_00ade5cc",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "325a1147245a724d47bf8b7fa5a42857b4b62b08d0ddffcae75896e76df716fb",
  "source_text_sha256": "325a1147245a724d47bf8b7fa5a42857b4b62b08d0ddffcae75896e76df716fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ade5cc",
        "00ade6f7"
      ]
    ],
    "bytes_sha256": "8cf705314cc0517add534b660fa1b2cd252ca1bb7124ed80de32339e80d84939",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005a79d8](../005a7/005a79d8.md)
- [005e144c](../005e1/005e144c.md)
- [0065040c](../00650/0065040c.md)
- [00653214](../00653/00653214.md)
- [006a8e60](../006a8/006a8e60.md)
- [0071b5e0](../0071b/0071b5e0.md)
- [0078cd14](../0078c/0078cd14.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007acf88](../007ac/007acf88.md)
- [007dfc70](../007df/007dfc70.md)
- [007e855c](../007e8/007e855c.md)
- [007e8848](../007e8/007e8848.md)
- [007f226c](../007f2/007f226c.md)
- [007f24c4](../007f2/007f24c4.md)
- [007f534c](../007f5/007f534c.md)
- [007f8b0c](../007f8/007f8b0c.md)
- [0082b53c](../0082b/0082b53c.md)
- [008a209c](../008a2/008a209c.md)
- [008e0bc0](../008e0/008e0bc0.md)
- [008e68f8](../008e6/008e68f8.md)
- [0094d124](../0094d/0094d124.md)
- [0094f7d0](../0094f/0094f7d0.md)
- [00957f9c](../00957/00957f9c.md)
- [00963004](../00963/00963004.md)
- [009a9670](../009a9/009a9670.md)
- [009a9774](../009a9/009a9774.md)
- [00a02c30](../00a02/00a02c30.md)
- [00a11cc0](../00a11/00a11cc0.md)
- [00a15464](../00a15/00a15464.md)
- [00a17ce0](../00a17/00a17ce0.md)
- [00a1bb38](../00a1b/00a1bb38.md)
- [00a1fc08](../00a1f/00a1fc08.md)
- [00a5c348](../00a5c/00a5c348.md)
- [00a5c504](../00a5c/00a5c504.md)
- [00a601cc](../00a60/00a601cc.md)
- [00a61490](../00a61/00a61490.md)
- [00aa8e8c](../00aa8/00aa8e8c.md)
- [00ade2f4](../00ade/00ade2f4.md)
- [00adf8e0](../00adf/00adf8e0.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaff0](../00bda/00bdaff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3794 bytes

~~~c

undefined1 FUN_00ade5cc(undefined8 param_1,int param_2)

{
  undefined1 uVar1;
  long lVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long lVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
  lVar2 = FUN_0081f580();
  lVar7 = *(long *)(lVar2 + 0x22a0);
  lVar2 = lVar2 + 0x22a0;
  lVar3 = lVar2;
  if (lVar7 != 0) {
    do {
      if (param_2 <= *(int *)(lVar7 + 0x1c)) {
        lVar3 = lVar7;
      }
      lVar7 = *(long *)(lVar7 + (ulong)(*(int *)(lVar7 + 0x1c) < param_2) * 8);
    } while (lVar7 != 0);
    if ((lVar3 != lVar2) && (*(int *)(lVar3 + 0x1c) <= param_2)) {
      lVar2 = lVar3;
    }
  }
  lVar3 = FUN_0081f580();
  if (lVar2 == lVar3 + 0x22a0) {
                    /* catch() { ... } // from try @ 00ade0c0 with catch @ 00ade6e0 */
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_0081f580();
    puVar5 = *(undefined8 **)(lVar2 + 0x22a0);
    if (*(undefined8 **)(lVar2 + 0x22a0) == (undefined8 *)0x0) {
      puVar8 = (undefined8 *)(lVar2 + 0x22a0);
      puVar9 = (undefined8 *)(lVar2 + 0x22a0);
    }
    else {
      do {
        while (puVar4 = puVar5, puVar8 = puVar4, param_2 < *(int *)((long)puVar4 + 0x1c)) {
                    /* try { // try from 00ade664 to 00bde683 has its CatchHandler @ 00ade6d4 */
          puVar5 = (undefined8 *)*puVar4;
          puVar9 = puVar4;
          if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00ade688;
        }
        if (param_2 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00ade6d8;
        puVar5 = (undefined8 *)puVar4[1];
      } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
                    /* catch() { ... } // from try @ 00ade580 with catch @ 00ade684
                       try { // try from 00ade684 to 00bde74b has its CatchHandler @ 00addf84 */
      puVar9 = puVar4 + 1;
    }
LAB_00ade688:
                    /* catch() { ... } // from try @ 00ade1bc with catch @ 00ade688 */
                    /* catch() { ... } // from try @ 00ade1a8 with catch @ 00ade68c */
                    /* catch() { ... } // from try @ 00ade174 with catch @ 00ade690 */
    puVar4 = (undefined8 *)_Znwm(0x28);
                    /* catch() { ... } // from try @ 00ade090 with catch @ 00ade694
                       catch() { ... } // from try @ 00ade16c with catch @ 00ade694 */
    *puVar4 = 0;
    puVar4[1] = 0;
                    /* catch() { ... } // from try @ 00ade044 with catch @ 00ade698 */
    puVar4[2] = puVar8;
    *puVar9 = puVar4;
    plVar6 = *(long **)(lVar2 + 0x2298);
    *(int *)((long)puVar4 + 0x1c) = param_2;
                    /* catch() { ... } // from try @ 00ade02c with catch @ 00ade6b0 */
    *(undefined1 *)(puVar4 + 4) = 0;
    puVar5 = puVar4;
    if (*plVar6 != 0) {
      *(long *)(lVar2 + 0x2298) = *plVar6;
      puVar5 = (undefined8 *)*puVar9;
    }
    FUN_00419064(*(undefined8 *)(lVar2 + 0x22a0),puVar5);
                    /* catch() { ... } // from try @ 00addff4 with catch @ 00ade6cc */
                    /* catch() { ... } // from try @ 00ade664 with catch @ 00ade6d4 */
    *(long *)(lVar2 + 0x22a8) = *(long *)(lVar2 + 0x22a8) + 1;
LAB_00ade6d8:
                    /* catch() { ... } // from try @ 00ade248 with catch @ 00ade6d8 */
    uVar1 = *(undefined1 *)(puVar4 + 4);
  }
                    /* catch() { ... } // from try @ 00ade410 with catch @ 00ade6e4 */
                    /* catch() { ... } // from try @ 00ade0b4 with catch @ 00ade6e8 */
                    /* catch() { ... } // from try @ 00ade41c with catch @ 00ade6ec
                       catch() { ... } // from try @ 00ade4ec with catch @ 00ade6ec */
                    /* catch() { ... } // from try @ 00ade0cc with catch @ 00ade6f0 */
                    /* catch() { ... } // from try @ 00ade42c with catch @ 00ade6f4 */
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ade5cc"></a> `00ade5cc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ade5d0"></a> `00ade5d0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ade5d4"></a> `00ade5d4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ade5d8"></a> `00ade5d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ade5dc"></a> `00ade5dc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ade5e0"></a> `00ade5e0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00ade5e4"></a> `00ade5e4` | `e7 03 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ade5e8"></a> `00ade5e8` | `09 50 51 f9` | ldr x9,[x0, #0x22a0] | `FALL_THROUGH`
<a id="insn-00ade5ec"></a> `00ade5ec` | `08 54 84 52` | mov w8,#0x22a0 | `FALL_THROUGH`
<a id="insn-00ade5f0"></a> `00ade5f0` | `14 00 08 8b` | add x20,x0,x8 | `FALL_THROUGH`
<a id="insn-00ade5f4"></a> `00ade5f4` | `a9 01 00 b4` | cbz x9,0x00ade628 | `CONDITIONAL_JUMP`
<a id="insn-00ade5f8"></a> `00ade5f8` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00ade5fc"></a> `00ade5fc` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00ade600"></a> `00ade600` | `5f 01 13 6b` | cmp w10,w19 | `FALL_THROUGH`
<a id="insn-00ade604"></a> `00ade604` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00ade608"></a> `00ade608` | `08 b1 89 9a` | csel x8,x8,x9,lt | `FALL_THROUGH`
<a id="insn-00ade60c"></a> `00ade60c` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ade610"></a> `00ade610` | `69 ff ff b5` | cbnz x9,0x00ade5fc | `CONDITIONAL_JUMP`
<a id="insn-00ade614"></a> `00ade614` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00ade618"></a> `00ade618` | `80 00 00 54` | b.eq 0x00ade628 | `CONDITIONAL_JUMP`
<a id="insn-00ade61c"></a> `00ade61c` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ade620"></a> `00ade620` | `3f 01 13 6b` | cmp w9,w19 | `FALL_THROUGH`
<a id="insn-00ade624"></a> `00ade624` | `94 c2 88 9a` | csel x20,x20,x8,gt | `FALL_THROUGH`
<a id="insn-00ade628"></a> `00ade628` | `d6 03 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ade62c"></a> `00ade62c` | `08 54 84 52` | mov w8,#0x22a0 | `FALL_THROUGH`
<a id="insn-00ade630"></a> `00ade630` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00ade634"></a> `00ade634` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00ade638"></a> `00ade638` | `40 05 00 54` | b.eq 0x00ade6e0 | `CONDITIONAL_JUMP`
<a id="insn-00ade63c"></a> `00ade63c` | `d1 03 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ade640"></a> `00ade640` | `08 50 51 f9` | ldr x8,[x0, #0x22a0] | `FALL_THROUGH`
<a id="insn-00ade644"></a> `00ade644` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ade648"></a> `00ade648` | `08 01 00 b5` | cbnz x8,0x00ade668 | `CONDITIONAL_JUMP`
<a id="insn-00ade64c"></a> `00ade64c` | `08 54 84 52` | mov w8,#0x22a0 | `FALL_THROUGH`
<a id="insn-00ade650"></a> `00ade650` | `96 02 08 8b` | add x22,x20,x8 | `FALL_THROUGH`
<a id="insn-00ade654"></a> `00ade654` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ade658"></a> `00ade658` | `0c 00 00 14` | b 0x00ade688 | `UNCONDITIONAL_JUMP`
<a id="insn-00ade65c"></a> `00ade65c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ade660"></a> `00ade660` | `f6 03 15 aa` | mov x22,x21 | `FALL_THROUGH`
<a id="insn-00ade664"></a> `00ade664` | `28 01 00 b4` | cbz x8,0x00ade688 | `CONDITIONAL_JUMP`
<a id="insn-00ade668"></a> `00ade668` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00ade66c"></a> `00ade66c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ade670"></a> `00ade670` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00ade674"></a> `00ade674` | `4c ff ff 54` | b.gt 0x00ade65c | `CONDITIONAL_JUMP`
<a id="insn-00ade678"></a> `00ade678` | `0a 03 00 54` | b.ge 0x00ade6d8 | `CONDITIONAL_JUMP`
<a id="insn-00ade67c"></a> `00ade67c` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ade680"></a> `00ade680` | `48 ff ff b5` | cbnz x8,0x00ade668 | `CONDITIONAL_JUMP`
<a id="insn-00ade684"></a> `00ade684` | `b6 22 00 91` | add x22,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ade688"></a> `00ade688` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ade68c"></a> `00ade68c` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-00ade690"></a> `00ade690` | `58 f2 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ade694"></a> `00ade694` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ade698"></a> `00ade698` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ade69c"></a> `00ade69c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ade6a0"></a> `00ade6a0` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ade6a4"></a> `00ade6a4` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00ade6a8"></a> `00ade6a8` | `88 4e 51 f9` | ldr x8,[x20, #0x2298] | `FALL_THROUGH`
<a id="insn-00ade6ac"></a> `00ade6ac` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ade6b0"></a> `00ade6b0` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ade6b4"></a> `00ade6b4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ade6b8"></a> `00ade6b8` | `68 00 00 b4` | cbz x8,0x00ade6c4 | `CONDITIONAL_JUMP`
<a id="insn-00ade6bc"></a> `00ade6bc` | `88 4e 11 f9` | str x8,[x20, #0x2298] | `FALL_THROUGH`
<a id="insn-00ade6c0"></a> `00ade6c0` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00ade6c4"></a> `00ade6c4` | `80 52 51 f9` | ldr x0,[x20, #0x22a0] | `FALL_THROUGH`
<a id="insn-00ade6c8"></a> `00ade6c8` | `67 ea e4 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ade6cc"></a> `00ade6cc` | `88 56 51 f9` | ldr x8,[x20, #0x22a8] | `FALL_THROUGH`
<a id="insn-00ade6d0"></a> `00ade6d0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ade6d4"></a> `00ade6d4` | `88 56 11 f9` | str x8,[x20, #0x22a8] | `FALL_THROUGH`
<a id="insn-00ade6d8"></a> `00ade6d8` | `a0 82 40 39` | ldrb w0,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ade6dc"></a> `00ade6dc` | `02 00 00 14` | b 0x00ade6e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ade6e0"></a> `00ade6e0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ade6e4"></a> `00ade6e4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ade6e8"></a> `00ade6e8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ade6ec"></a> `00ade6ec` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ade6f0"></a> `00ade6f0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00ade6f4"></a> `00ade6f4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ade5cc`](#insn-00ade5cc) 範囲 `[['00ade5cc', '00ade5f7']]`
  - `CONDITIONAL_JUMP` [`00ade5f4`](#insn-00ade5f4) → [`00ade628`](#insn-00ade628)
  - `FALL_THROUGH` [`00ade5f4`](#insn-00ade5f4) → [`00ade5f8`](#insn-00ade5f8)
- ブロック [`00ade5f8`](#insn-00ade5f8) 範囲 `[['00ade5f8', '00ade5fb']]`
  - `FALL_THROUGH` [`00ade5f8`](#insn-00ade5f8) → [`00ade5fc`](#insn-00ade5fc)
- ブロック [`00ade5fc`](#insn-00ade5fc) 範囲 `[['00ade5fc', '00ade613']]`
  - `CONDITIONAL_JUMP` [`00ade610`](#insn-00ade610) → [`00ade5fc`](#insn-00ade5fc)
  - `FALL_THROUGH` [`00ade610`](#insn-00ade610) → [`00ade614`](#insn-00ade614)
- ブロック [`00ade614`](#insn-00ade614) 範囲 `[['00ade614', '00ade61b']]`
  - `CONDITIONAL_JUMP` [`00ade618`](#insn-00ade618) → [`00ade628`](#insn-00ade628)
  - `FALL_THROUGH` [`00ade618`](#insn-00ade618) → [`00ade61c`](#insn-00ade61c)
- ブロック [`00ade61c`](#insn-00ade61c) 範囲 `[['00ade61c', '00ade627']]`
  - `FALL_THROUGH` [`00ade624`](#insn-00ade624) → [`00ade628`](#insn-00ade628)
- ブロック [`00ade628`](#insn-00ade628) 範囲 `[['00ade628', '00ade63b']]`
  - `CONDITIONAL_JUMP` [`00ade638`](#insn-00ade638) → [`00ade6e0`](#insn-00ade6e0)
  - `FALL_THROUGH` [`00ade638`](#insn-00ade638) → [`00ade63c`](#insn-00ade63c)
- ブロック [`00ade63c`](#insn-00ade63c) 範囲 `[['00ade63c', '00ade64b']]`
  - `CONDITIONAL_JUMP` [`00ade648`](#insn-00ade648) → [`00ade668`](#insn-00ade668)
  - `FALL_THROUGH` [`00ade648`](#insn-00ade648) → [`00ade64c`](#insn-00ade64c)
- ブロック [`00ade64c`](#insn-00ade64c) 範囲 `[['00ade64c', '00ade65b']]`
  - `UNCONDITIONAL_JUMP` [`00ade658`](#insn-00ade658) → [`00ade688`](#insn-00ade688)
- ブロック [`00ade65c`](#insn-00ade65c) 範囲 `[['00ade65c', '00ade663']]`
  - `FALL_THROUGH` [`00ade660`](#insn-00ade660) → [`00ade664`](#insn-00ade664)
- ブロック [`00ade664`](#insn-00ade664) 範囲 `[['00ade664', '00ade667']]`
  - `CONDITIONAL_JUMP` [`00ade664`](#insn-00ade664) → [`00ade688`](#insn-00ade688)
  - `FALL_THROUGH` [`00ade664`](#insn-00ade664) → [`00ade668`](#insn-00ade668)
- ブロック [`00ade668`](#insn-00ade668) 範囲 `[['00ade668', '00ade677']]`
  - `CONDITIONAL_JUMP` [`00ade674`](#insn-00ade674) → [`00ade65c`](#insn-00ade65c)
  - `FALL_THROUGH` [`00ade674`](#insn-00ade674) → [`00ade678`](#insn-00ade678)
- ブロック [`00ade678`](#insn-00ade678) 範囲 `[['00ade678', '00ade67b']]`
  - `CONDITIONAL_JUMP` [`00ade678`](#insn-00ade678) → [`00ade6d8`](#insn-00ade6d8)
  - `FALL_THROUGH` [`00ade678`](#insn-00ade678) → [`00ade67c`](#insn-00ade67c)
- ブロック [`00ade67c`](#insn-00ade67c) 範囲 `[['00ade67c', '00ade683']]`
  - `CONDITIONAL_JUMP` [`00ade680`](#insn-00ade680) → [`00ade668`](#insn-00ade668)
  - `FALL_THROUGH` [`00ade680`](#insn-00ade680) → [`00ade684`](#insn-00ade684)
- ブロック [`00ade684`](#insn-00ade684) 範囲 `[['00ade684', '00ade687']]`
  - `FALL_THROUGH` [`00ade684`](#insn-00ade684) → [`00ade688`](#insn-00ade688)
- ブロック [`00ade688`](#insn-00ade688) 範囲 `[['00ade688', '00ade68b']]`
  - `FALL_THROUGH` [`00ade688`](#insn-00ade688) → [`00ade68c`](#insn-00ade68c)
- ブロック [`00ade68c`](#insn-00ade68c) 範囲 `[['00ade68c', '00ade68f']]`
  - `FALL_THROUGH` [`00ade68c`](#insn-00ade68c) → [`00ade690`](#insn-00ade690)
- ブロック [`00ade690`](#insn-00ade690) 範囲 `[['00ade690', '00ade693']]`
  - `FALL_THROUGH` [`00ade690`](#insn-00ade690) → [`00ade694`](#insn-00ade694)
- ブロック [`00ade694`](#insn-00ade694) 範囲 `[['00ade694', '00ade697']]`
  - `FALL_THROUGH` [`00ade694`](#insn-00ade694) → [`00ade698`](#insn-00ade698)
- ブロック [`00ade698`](#insn-00ade698) 範囲 `[['00ade698', '00ade6af']]`
  - `FALL_THROUGH` [`00ade6ac`](#insn-00ade6ac) → [`00ade6b0`](#insn-00ade6b0)
- ブロック [`00ade6b0`](#insn-00ade6b0) 範囲 `[['00ade6b0', '00ade6bb']]`
  - `CONDITIONAL_JUMP` [`00ade6b8`](#insn-00ade6b8) → [`00ade6c4`](#insn-00ade6c4)
  - `FALL_THROUGH` [`00ade6b8`](#insn-00ade6b8) → [`00ade6bc`](#insn-00ade6bc)
- ブロック [`00ade6bc`](#insn-00ade6bc) 範囲 `[['00ade6bc', '00ade6c3']]`
  - `FALL_THROUGH` [`00ade6c0`](#insn-00ade6c0) → [`00ade6c4`](#insn-00ade6c4)
- ブロック [`00ade6c4`](#insn-00ade6c4) 範囲 `[['00ade6c4', '00ade6cb']]`
  - `FALL_THROUGH` [`00ade6c8`](#insn-00ade6c8) → [`00ade6cc`](#insn-00ade6cc)
- ブロック [`00ade6cc`](#insn-00ade6cc) 範囲 `[['00ade6cc', '00ade6d3']]`
  - `FALL_THROUGH` [`00ade6d0`](#insn-00ade6d0) → [`00ade6d4`](#insn-00ade6d4)
- ブロック [`00ade6d4`](#insn-00ade6d4) 範囲 `[['00ade6d4', '00ade6d7']]`
  - `FALL_THROUGH` [`00ade6d4`](#insn-00ade6d4) → [`00ade6d8`](#insn-00ade6d8)
- ブロック [`00ade6d8`](#insn-00ade6d8) 範囲 `[['00ade6d8', '00ade6df']]`
  - `UNCONDITIONAL_JUMP` [`00ade6dc`](#insn-00ade6dc) → [`00ade6e4`](#insn-00ade6e4)
- ブロック [`00ade6e0`](#insn-00ade6e0) 範囲 `[['00ade6e0', '00ade6e3']]`
  - `FALL_THROUGH` [`00ade6e0`](#insn-00ade6e0) → [`00ade6e4`](#insn-00ade6e4)
- ブロック [`00ade6e4`](#insn-00ade6e4) 範囲 `[['00ade6e4', '00ade6e7']]`
  - `FALL_THROUGH` [`00ade6e4`](#insn-00ade6e4) → [`00ade6e8`](#insn-00ade6e8)
- ブロック [`00ade6e8`](#insn-00ade6e8) 範囲 `[['00ade6e8', '00ade6eb']]`
  - `FALL_THROUGH` [`00ade6e8`](#insn-00ade6e8) → [`00ade6ec`](#insn-00ade6ec)
- ブロック [`00ade6ec`](#insn-00ade6ec) 範囲 `[['00ade6ec', '00ade6ef']]`
  - `FALL_THROUGH` [`00ade6ec`](#insn-00ade6ec) → [`00ade6f0`](#insn-00ade6f0)
- ブロック [`00ade6f0`](#insn-00ade6f0) 範囲 `[['00ade6f0', '00ade6f3']]`
  - `FALL_THROUGH` [`00ade6f0`](#insn-00ade6f0) → [`00ade6f4`](#insn-00ade6f4)
- ブロック [`00ade6f4`](#insn-00ade6f4) 範囲 `[['00ade6f4', '00ade6f7']]`

## 命令位置別の参照

- [`00ade5cc`](#insn-00ade5cc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade5d0`](#insn-00ade5d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade5d4`](#insn-00ade5d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade5d8`](#insn-00ade5d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade5e4`](#insn-00ade5e4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ade5f4`](#insn-00ade5f4) → [`00ade628`](#insn-00ade628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade610`](#insn-00ade610) → [`00ade5fc`](#insn-00ade5fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade618`](#insn-00ade618) → [`00ade628`](#insn-00ade628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade628`](#insn-00ade628) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ade638`](#insn-00ade638) → [`00ade6e0`](#insn-00ade6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade63c`](#insn-00ade63c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ade648`](#insn-00ade648) → [`00ade668`](#insn-00ade668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade658`](#insn-00ade658) → [`00ade688`](#insn-00ade688) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade664`](#insn-00ade664) → [`00ade688`](#insn-00ade688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade674`](#insn-00ade674) → [`00ade65c`](#insn-00ade65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade678`](#insn-00ade678) → [`00ade6d8`](#insn-00ade6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade680`](#insn-00ade680) → [`00ade668`](#insn-00ade668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade690`](#insn-00ade690) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ade6b8`](#insn-00ade6b8) → [`00ade6c4`](#insn-00ade6c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade6c8`](#insn-00ade6c8) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ade6dc`](#insn-00ade6dc) → [`00ade6e4`](#insn-00ade6e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade6e4`](#insn-00ade6e4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade6e8`](#insn-00ade6e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade6ec`](#insn-00ade6ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ade6f0`](#insn-00ade6f0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ade5cc`](#insn-00ade5cc)

~~~json
{
  "source": "00ade5cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade5d0`](#insn-00ade5d0)

~~~json
{
  "source": "00ade5d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade5d4`](#insn-00ade5d4)

~~~json
{
  "source": "00ade5d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade5d8`](#insn-00ade5d8)

~~~json
{
  "source": "00ade5d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade5e4`](#insn-00ade5e4)

~~~json
{
  "source": "00ade5e4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ade5f4`](#insn-00ade5f4)

~~~json
{
  "source": "00ade5f4",
  "target": "00ade628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade610`](#insn-00ade610)

~~~json
{
  "source": "00ade610",
  "target": "00ade5fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade618`](#insn-00ade618)

~~~json
{
  "source": "00ade618",
  "target": "00ade628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade628`](#insn-00ade628)

~~~json
{
  "source": "00ade628",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ade638`](#insn-00ade638)

~~~json
{
  "source": "00ade638",
  "target": "00ade6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade63c`](#insn-00ade63c)

~~~json
{
  "source": "00ade63c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ade648`](#insn-00ade648)

~~~json
{
  "source": "00ade648",
  "target": "00ade668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade658`](#insn-00ade658)

~~~json
{
  "source": "00ade658",
  "target": "00ade688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade664`](#insn-00ade664)

~~~json
{
  "source": "00ade664",
  "target": "00ade688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade674`](#insn-00ade674)

~~~json
{
  "source": "00ade674",
  "target": "00ade65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade678`](#insn-00ade678)

~~~json
{
  "source": "00ade678",
  "target": "00ade6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade680`](#insn-00ade680)

~~~json
{
  "source": "00ade680",
  "target": "00ade668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade690`](#insn-00ade690)

~~~json
{
  "source": "00ade690",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ade6b8`](#insn-00ade6b8)

~~~json
{
  "source": "00ade6b8",
  "target": "00ade6c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade6c8`](#insn-00ade6c8)

~~~json
{
  "source": "00ade6c8",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ade6dc`](#insn-00ade6dc)

~~~json
{
  "source": "00ade6dc",
  "target": "00ade6e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade6e4`](#insn-00ade6e4)

~~~json
{
  "source": "00ade6e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade6e8`](#insn-00ade6e8)

~~~json
{
  "source": "00ade6e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade6ec`](#insn-00ade6ec)

~~~json
{
  "source": "00ade6ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ade6f0`](#insn-00ade6f0)

~~~json
{
  "source": "00ade6f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
