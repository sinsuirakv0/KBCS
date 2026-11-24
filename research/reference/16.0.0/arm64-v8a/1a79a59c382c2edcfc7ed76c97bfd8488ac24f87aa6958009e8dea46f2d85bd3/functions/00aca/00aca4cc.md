# 00aca4cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6c538`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c538.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-c17a1e3007fddd976293bc0bafc4e039)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aca6c8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca6c8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-b90de41d20bd22fcffdd7e1217a2c1d2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca4cc",
  "name": "FUN_00aca4cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd969811cc57415e09c371a02acbca34c8a4889f9c1fbe1f908ebec817e29c48",
  "source_text_sha256": "fd969811cc57415e09c371a02acbca34c8a4889f9c1fbe1f908ebec817e29c48",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca4cc",
        "00aca5eb"
      ]
    ],
    "bytes_sha256": "b1cb6d4d01e28cee27915f77d827710cbff66b8238ad9865affadeec524938b8",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467b20](../00467/00467b20.md)
- [00468b9c](../00468/00468b9c.md)
- [00468c20](../00468/00468c20.md)
- [00468f48](../00468/00468f48.md)
- [0046c984](../0046c/0046c984.md)
- [0046d934](../0046d/0046d934.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 808 bytes

~~~c

void FUN_00aca4cc(int *param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  float fVar3;
  
  if ((char)param_1[0xf] != '\0') {
    uVar2 = FUN_00467820();
    FUN_00467b20(uVar2,0xff,0xff,0xff,0xff);
    FUN_00468b9c(uVar2,0x72);
    if (0 < param_1[0x18]) {
      fVar3 = (float)FUN_0046d934((float)(*param_1 * 0x1e));
      FUN_00468f48(uVar2,param_2,(int)(fVar3 * 10.0 + 24.0),param_3 + 0xff,8);
    }
    FUN_00468c20(uVar2,1);
    if (param_1[0x18] < param_1[0x17] + -1) {
      FUN_008514b8();
      iVar1 = FUN_0046c984();
      fVar3 = (float)FUN_0046d934((float)(*param_1 * 0x1e));
      FUN_00468f48(uVar2,param_2,(int)((float)(iVar1 + -0x56) + fVar3 * -10.0),param_3 + 0xff,8);
    }
    FUN_00468c20(uVar2,0);
    FUN_00468b9c(uVar2,0xff);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca4cc"></a> `00aca4cc` | `08 f0 40 39` | ldrb w8,[x0, #0x3c] | `FALL_THROUGH`
<a id="insn-00aca4d0"></a> `00aca4d0` | `c8 08 00 34` | cbz w8,0x00aca5e8 | `CONDITIONAL_JUMP`
<a id="insn-00aca4d4"></a> `00aca4d4` | `e8 0f 1c fc` | str d8,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aca4d8"></a> `00aca4d8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca4dc"></a> `00aca4dc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca4e0"></a> `00aca4e0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca4e4"></a> `00aca4e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aca4e8"></a> `00aca4e8` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00aca4ec"></a> `00aca4ec` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aca4f0"></a> `00aca4f0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00aca4f4"></a> `00aca4f4` | `cb 74 e6 97` | bl 0x00467820 | `UNCONDITIONAL_CALL`
<a id="insn-00aca4f8"></a> `00aca4f8` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aca4fc"></a> `00aca4fc` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aca500"></a> `00aca500` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aca504"></a> `00aca504` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aca508"></a> `00aca508` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca50c"></a> `00aca50c` | `85 75 e6 97` | bl 0x00467b20 | `UNCONDITIONAL_CALL`
<a id="insn-00aca510"></a> `00aca510` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca514"></a> `00aca514` | `41 0e 80 52` | mov w1,#0x72 | `FALL_THROUGH`
<a id="insn-00aca518"></a> `00aca518` | `a1 79 e6 97` | bl 0x00468b9c | `UNCONDITIONAL_CALL`
<a id="insn-00aca51c"></a> `00aca51c` | `c8 62 40 b9` | ldr w8,[x22, #0x60] | `FALL_THROUGH`
<a id="insn-00aca520"></a> `00aca520` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aca524"></a> `00aca524` | `eb 01 00 54` | b.lt 0x00aca560 | `CONDITIONAL_JUMP`
<a id="insn-00aca528"></a> `00aca528` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00aca52c"></a> `00aca52c` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aca530"></a> `00aca530` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00aca534"></a> `00aca534` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00aca538"></a> `00aca538` | `ff 8c e6 97` | bl 0x0046d934 | `UNCONDITIONAL_CALL`
<a id="insn-00aca53c"></a> `00aca53c` | `01 10 27 1e` | fmov s1,0x41c00000 | `FALL_THROUGH`
<a id="insn-00aca540"></a> `00aca540` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-00aca544"></a> `00aca544` | `83 fe 03 11` | add w3,w20,#0xff | `FALL_THROUGH`
<a id="insn-00aca548"></a> `00aca548` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca54c"></a> `00aca54c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aca550"></a> `00aca550` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-00aca554"></a> `00aca554` | `00 04 02 1f` | fmadd s0,s0,s2,s1 | `FALL_THROUGH`
<a id="insn-00aca558"></a> `00aca558` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00aca55c"></a> `00aca55c` | `7b 7a e6 97` | bl 0x00468f48 | `UNCONDITIONAL_CALL`
<a id="insn-00aca560"></a> `00aca560` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca564"></a> `00aca564` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aca568"></a> `00aca568` | `ae 79 e6 97` | bl 0x00468c20 | `UNCONDITIONAL_CALL`
<a id="insn-00aca56c"></a> `00aca56c` | `c8 a6 4b 29` | ldp w8,w9,[x22, #0x5c] | `FALL_THROUGH`
<a id="insn-00aca570"></a> `00aca570` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aca574"></a> `00aca574` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00aca578"></a> `00aca578` | `4a 02 00 54` | b.ge 0x00aca5c0 | `CONDITIONAL_JUMP`
<a id="insn-00aca57c"></a> `00aca57c` | `cf 1b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aca580"></a> `00aca580` | `01 89 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00aca584"></a> `00aca584` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00aca588"></a> `00aca588` | `09 58 01 51` | sub w9,w0,#0x56 | `FALL_THROUGH`
<a id="insn-00aca58c"></a> `00aca58c` | `28 01 22 1e` | scvtf s8,w9 | `FALL_THROUGH`
<a id="insn-00aca590"></a> `00aca590` | `0a 69 1b 53` | lsl w10,w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aca594"></a> `00aca594` | `48 05 08 4b` | sub w8,w10,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00aca598"></a> `00aca598` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00aca59c"></a> `00aca59c` | `e6 8c e6 97` | bl 0x0046d934 | `UNCONDITIONAL_CALL`
<a id="insn-00aca5a0"></a> `00aca5a0` | `01 90 34 1e` | fmov s1,0xc1200000 | `FALL_THROUGH`
<a id="insn-00aca5a4"></a> `00aca5a4` | `83 fe 03 11` | add w3,w20,#0xff | `FALL_THROUGH`
<a id="insn-00aca5a8"></a> `00aca5a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca5ac"></a> `00aca5ac` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aca5b0"></a> `00aca5b0` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-00aca5b4"></a> `00aca5b4` | `00 20 01 1f` | fmadd s0,s0,s1,s8 | `FALL_THROUGH`
<a id="insn-00aca5b8"></a> `00aca5b8` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00aca5bc"></a> `00aca5bc` | `63 7a e6 97` | bl 0x00468f48 | `UNCONDITIONAL_CALL`
<a id="insn-00aca5c0"></a> `00aca5c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca5c4"></a> `00aca5c4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca5c8"></a> `00aca5c8` | `96 79 e6 97` | bl 0x00468c20 | `UNCONDITIONAL_CALL`
<a id="insn-00aca5cc"></a> `00aca5cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca5d0"></a> `00aca5d0` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aca5d4"></a> `00aca5d4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aca5d8"></a> `00aca5d8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca5dc"></a> `00aca5dc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca5e0"></a> `00aca5e0` | `e8 07 44 fc` | ldr d8,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aca5e4"></a> `00aca5e4` | `6e 79 e6 17` | b 0x00468b9c | `CALL_TERMINATOR`
<a id="insn-00aca5e8"></a> `00aca5e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca4cc`](#insn-00aca4cc) 範囲 `[['00aca4cc', '00aca4d3']]`
  - `CONDITIONAL_JUMP` [`00aca4d0`](#insn-00aca4d0) → [`00aca5e8`](#insn-00aca5e8)
  - `FALL_THROUGH` [`00aca4d0`](#insn-00aca4d0) → [`00aca4d4`](#insn-00aca4d4)
- ブロック [`00aca4d4`](#insn-00aca4d4) 範囲 `[['00aca4d4', '00aca527']]`
  - `CONDITIONAL_JUMP` [`00aca524`](#insn-00aca524) → [`00aca560`](#insn-00aca560)
  - `FALL_THROUGH` [`00aca524`](#insn-00aca524) → [`00aca528`](#insn-00aca528)
- ブロック [`00aca528`](#insn-00aca528) 範囲 `[['00aca528', '00aca55f']]`
  - `FALL_THROUGH` [`00aca55c`](#insn-00aca55c) → [`00aca560`](#insn-00aca560)
- ブロック [`00aca560`](#insn-00aca560) 範囲 `[['00aca560', '00aca57b']]`
  - `CONDITIONAL_JUMP` [`00aca578`](#insn-00aca578) → [`00aca5c0`](#insn-00aca5c0)
  - `FALL_THROUGH` [`00aca578`](#insn-00aca578) → [`00aca57c`](#insn-00aca57c)
- ブロック [`00aca57c`](#insn-00aca57c) 範囲 `[['00aca57c', '00aca5bf']]`
  - `FALL_THROUGH` [`00aca5bc`](#insn-00aca5bc) → [`00aca5c0`](#insn-00aca5c0)
- ブロック [`00aca5c0`](#insn-00aca5c0) 範囲 `[['00aca5c0', '00aca5e7']]`
- ブロック [`00aca5e8`](#insn-00aca5e8) 範囲 `[['00aca5e8', '00aca5eb']]`

## 命令位置別の参照

- [`00aca4d0`](#insn-00aca4d0) → [`00aca5e8`](#insn-00aca5e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4d4`](#insn-00aca4d4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4d8`](#insn-00aca4d8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4dc`](#insn-00aca4dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4e0`](#insn-00aca4e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4f4`](#insn-00aca4f4) → [`00467820`](../00467/00467820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467820` · 推定シンボル `None` · 推定型 `None`
- [`00aca50c`](#insn-00aca50c) → [`00467b20`](../00467/00467b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b20` · 推定シンボル `None` · 推定型 `None`
- [`00aca518`](#insn-00aca518) → [`00468b9c`](../00468/00468b9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468b9c` · 推定シンボル `None` · 推定型 `None`
- [`00aca524`](#insn-00aca524) → [`00aca560`](#insn-00aca560) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca538`](#insn-00aca538) → [`0046d934`](../0046d/0046d934.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d934` · 推定シンボル `None` · 推定型 `None`
- [`00aca55c`](#insn-00aca55c) → [`00468f48`](../00468/00468f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f48` · 推定シンボル `None` · 推定型 `None`
- [`00aca568`](#insn-00aca568) → [`00468c20`](../00468/00468c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c20` · 推定シンボル `None` · 推定型 `None`
- [`00aca578`](#insn-00aca578) → [`00aca5c0`](#insn-00aca5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca57c`](#insn-00aca57c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aca580`](#insn-00aca580) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00aca59c`](#insn-00aca59c) → [`0046d934`](../0046d/0046d934.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d934` · 推定シンボル `None` · 推定型 `None`
- [`00aca5bc`](#insn-00aca5bc) → [`00468f48`](../00468/00468f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f48` · 推定シンボル `None` · 推定型 `None`
- [`00aca5c8`](#insn-00aca5c8) → [`00468c20`](../00468/00468c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c20` · 推定シンボル `None` · 推定型 `None`
- [`00aca5d4`](#insn-00aca5d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca5d8`](#insn-00aca5d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca5dc`](#insn-00aca5dc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca5e4`](#insn-00aca5e4) → [`00468b9c`](../00468/00468b9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468b9c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca4d0`](#insn-00aca4d0)

~~~json
{
  "source": "00aca4d0",
  "target": "00aca5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4d4`](#insn-00aca4d4)

~~~json
{
  "source": "00aca4d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4d8`](#insn-00aca4d8)

~~~json
{
  "source": "00aca4d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4dc`](#insn-00aca4dc)

~~~json
{
  "source": "00aca4dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4e0`](#insn-00aca4e0)

~~~json
{
  "source": "00aca4e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4f4`](#insn-00aca4f4)

~~~json
{
  "source": "00aca4f4",
  "target": "00467820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca50c`](#insn-00aca50c)

~~~json
{
  "source": "00aca50c",
  "target": "00467b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca518`](#insn-00aca518)

~~~json
{
  "source": "00aca518",
  "target": "00468b9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca524`](#insn-00aca524)

~~~json
{
  "source": "00aca524",
  "target": "00aca560",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca538`](#insn-00aca538)

~~~json
{
  "source": "00aca538",
  "target": "0046d934",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca55c`](#insn-00aca55c)

~~~json
{
  "source": "00aca55c",
  "target": "00468f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca568`](#insn-00aca568)

~~~json
{
  "source": "00aca568",
  "target": "00468c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca578`](#insn-00aca578)

~~~json
{
  "source": "00aca578",
  "target": "00aca5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca57c`](#insn-00aca57c)

~~~json
{
  "source": "00aca57c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca580`](#insn-00aca580)

~~~json
{
  "source": "00aca580",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca59c`](#insn-00aca59c)

~~~json
{
  "source": "00aca59c",
  "target": "0046d934",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca5bc`](#insn-00aca5bc)

~~~json
{
  "source": "00aca5bc",
  "target": "00468f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca5c8`](#insn-00aca5c8)

~~~json
{
  "source": "00aca5c8",
  "target": "00468c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca5d4`](#insn-00aca5d4)

~~~json
{
  "source": "00aca5d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca5d8`](#insn-00aca5d8)

~~~json
{
  "source": "00aca5d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca5dc`](#insn-00aca5dc)

~~~json
{
  "source": "00aca5dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca5e4`](#insn-00aca5e4)

~~~json
{
  "source": "00aca5e4",
  "target": "00468b9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
