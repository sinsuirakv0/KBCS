# 00bdd8cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdc8d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc8d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-35556dddcf11f3179c02b60c18819f8f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd8cc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "66c809bf6e807cb480335da329a5326261cfdb01fd794550322ebdb5251b7f30",
  "source_text_sha256": "66c809bf6e807cb480335da329a5326261cfdb01fd794550322ebdb5251b7f30",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd8cc",
        "00bdd9b3"
      ]
    ],
    "bytes_sha256": "e52d530df8d89d1d13cebbb16eda673ac21a206fc862a7f50c1dd4fdc5773c1e",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ef10](../00c5e/00c5ef10.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5b990](../00c5b/00c5b990.md)
- [00c5c680](../00c5c/00c5c680.md)
- [00c5ef00](../00c5e/00c5ef00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2185 bytes

~~~c

undefined8 *
_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_
          (long *param_1,undefined8 param_2,undefined8 param_3,long param_4)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined1 auStack_58 [8];
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00bdd904 to 00cdd90f has its CatchHandler @ 00bdfd38 */
  puVar2 = (undefined8 *)
           _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_
                     (param_1,param_2,&local_50,auStack_58,param_3);
  puVar4 = (undefined8 *)*puVar2;
  if (puVar4 == (undefined8 *)0x0) {
                    /* try { // try from 00bdd910 to 00cdd927 has its CatchHandler @ 00bdfd28 */
    puVar4 = (undefined8 *)_Znwm(0x50);
    *(undefined4 *)(puVar4 + 4) = 0;
                    /* try { // try from 00bdd928 to 00cdd98b has its CatchHandler @ 00bd7fb0 */
    _ZN8firebase7VariantaSERKS0_(puVar4 + 4,param_4);
    *(undefined4 *)(puVar4 + 7) = 0;
    _ZN8firebase7VariantaSERKS0_(puVar4 + 7,param_4 + 0x18);
    *puVar4 = 0;
    puVar4[1] = 0;
    puVar4[2] = local_50;
    *puVar2 = puVar4;
    puVar3 = puVar4;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar3 = (undefined8 *)*puVar2;
    }
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar3)
    ;
    param_1[2] = param_1[2] + 1;
  }
                    /* try { // try from 00bdd98c to 00cdd9db has its CatchHandler @ 00bdfe54 */
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return puVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd8cc"></a> `00bdd8cc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdd8d0"></a> `00bdd8d0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd8d4"></a> `00bdd8d4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdd8d8"></a> `00bdd8d8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdd8dc"></a> `00bdd8dc` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdd8e0"></a> `00bdd8e0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdd8e4"></a> `00bdd8e4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdd8e8"></a> `00bdd8e8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdd8ec"></a> `00bdd8ec` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00bdd8f0"></a> `00bdd8f0` | `e4 03 02 aa` | mov x4,x2 | `FALL_THROUGH`
<a id="insn-00bdd8f4"></a> `00bdd8f4` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdd8f8"></a> `00bdd8f8` | `e3 23 00 91` | add x3,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdd8fc"></a> `00bdd8fc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdd900"></a> `00bdd900` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdd904"></a> `00bdd904` | `7f 05 02 94` | bl 0x00c5ef00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd908"></a> `00bdd908` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bdd90c"></a> `00bdd90c` | `d3 03 00 b5` | cbnz x19,0x00bdd984 | `CONDITIONAL_JUMP`
<a id="insn-00bdd910"></a> `00bdd910` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdd914"></a> `00bdd914` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bdd918"></a> `00bdd918` | `86 ed 01 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd91c"></a> `00bdd91c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdd920"></a> `00bdd920` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd924"></a> `00bdd924` | `ff 0e 02 b8` | str wzr,[x23, #0x20]! | `FALL_THROUGH`
<a id="insn-00bdd928"></a> `00bdd928` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bdd92c"></a> `00bdd92c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdd930"></a> `00bdd930` | `18 f8 01 94` | bl 0x00c5b990 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd934"></a> `00bdd934` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd938"></a> `00bdd938` | `c1 62 00 91` | add x1,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00bdd93c"></a> `00bdd93c` | `1f 8c 03 b8` | str wzr,[x0, #0x38]! | `FALL_THROUGH`
<a id="insn-00bdd940"></a> `00bdd940` | `14 f8 01 94` | bl 0x00c5b990 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd944"></a> `00bdd944` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd948"></a> `00bdd948` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdd94c"></a> `00bdd94c` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd950"></a> `00bdd950` | `b3 02 00 f9` | str x19,[x21] | `FALL_THROUGH`
<a id="insn-00bdd954"></a> `00bdd954` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdd958"></a> `00bdd958` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bdd95c"></a> `00bdd95c` | `88 00 00 b4` | cbz x8,0x00bdd96c | `CONDITIONAL_JUMP`
<a id="insn-00bdd960"></a> `00bdd960` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdd964"></a> `00bdd964` | `a1 02 40 f9` | ldr x1,[x21] | `FALL_THROUGH`
<a id="insn-00bdd968"></a> `00bdd968` | `02 00 00 14` | b 0x00bdd970 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdd96c"></a> `00bdd96c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdd970"></a> `00bdd970` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bdd974"></a> `00bdd974` | `43 fb 01 94` | bl 0x00c5c680 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd978"></a> `00bdd978` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd97c"></a> `00bdd97c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdd980"></a> `00bdd980` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd984"></a> `00bdd984` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdd988"></a> `00bdd988` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdd98c"></a> `00bdd98c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdd990"></a> `00bdd990` | `01 01 00 54` | b.ne 0x00bdd9b0 | `CONDITIONAL_JUMP`
<a id="insn-00bdd994"></a> `00bdd994` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd998"></a> `00bdd998` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdd99c"></a> `00bdd99c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdd9a0"></a> `00bdd9a0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdd9a4"></a> `00bdd9a4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd9a8"></a> `00bdd9a8` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdd9ac"></a> `00bdd9ac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdd9b0"></a> `00bdd9b0` | `74 ed 01 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd8cc`](#insn-00bdd8cc) 範囲 `[['00bdd8cc', '00bdd903']]`
  - `FALL_THROUGH` [`00bdd900`](#insn-00bdd900) → [`00bdd904`](#insn-00bdd904)
- ブロック [`00bdd904`](#insn-00bdd904) 範囲 `[['00bdd904', '00bdd90f']]`
  - `CONDITIONAL_JUMP` [`00bdd90c`](#insn-00bdd90c) → [`00bdd984`](#insn-00bdd984)
  - `FALL_THROUGH` [`00bdd90c`](#insn-00bdd90c) → [`00bdd910`](#insn-00bdd910)
- ブロック [`00bdd910`](#insn-00bdd910) 範囲 `[['00bdd910', '00bdd927']]`
  - `FALL_THROUGH` [`00bdd924`](#insn-00bdd924) → [`00bdd928`](#insn-00bdd928)
- ブロック [`00bdd928`](#insn-00bdd928) 範囲 `[['00bdd928', '00bdd95f']]`
  - `CONDITIONAL_JUMP` [`00bdd95c`](#insn-00bdd95c) → [`00bdd96c`](#insn-00bdd96c)
  - `FALL_THROUGH` [`00bdd95c`](#insn-00bdd95c) → [`00bdd960`](#insn-00bdd960)
- ブロック [`00bdd960`](#insn-00bdd960) 範囲 `[['00bdd960', '00bdd96b']]`
  - `UNCONDITIONAL_JUMP` [`00bdd968`](#insn-00bdd968) → [`00bdd970`](#insn-00bdd970)
- ブロック [`00bdd96c`](#insn-00bdd96c) 範囲 `[['00bdd96c', '00bdd96f']]`
  - `FALL_THROUGH` [`00bdd96c`](#insn-00bdd96c) → [`00bdd970`](#insn-00bdd970)
- ブロック [`00bdd970`](#insn-00bdd970) 範囲 `[['00bdd970', '00bdd983']]`
  - `FALL_THROUGH` [`00bdd980`](#insn-00bdd980) → [`00bdd984`](#insn-00bdd984)
- ブロック [`00bdd984`](#insn-00bdd984) 範囲 `[['00bdd984', '00bdd98b']]`
  - `FALL_THROUGH` [`00bdd988`](#insn-00bdd988) → [`00bdd98c`](#insn-00bdd98c)
- ブロック [`00bdd98c`](#insn-00bdd98c) 範囲 `[['00bdd98c', '00bdd993']]`
  - `CONDITIONAL_JUMP` [`00bdd990`](#insn-00bdd990) → [`00bdd9b0`](#insn-00bdd9b0)
  - `FALL_THROUGH` [`00bdd990`](#insn-00bdd990) → [`00bdd994`](#insn-00bdd994)
- ブロック [`00bdd994`](#insn-00bdd994) 範囲 `[['00bdd994', '00bdd9af']]`
- ブロック [`00bdd9b0`](#insn-00bdd9b0) 範囲 `[['00bdd9b0', '00bdd9b3']]`

## 命令位置別の参照

- [`00bdd8d0`](#insn-00bdd8d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8d4`](#insn-00bdd8d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8d8`](#insn-00bdd8d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd8dc`](#insn-00bdd8dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd900`](#insn-00bdd900) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd904`](#insn-00bdd904) → [`00c5ef00`](../00c5e/00c5ef00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ef00` · 推定シンボル `None` · 推定型 `None`
- [`00bdd90c`](#insn-00bdd90c) → [`00bdd984`](#insn-00bdd984) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd918`](#insn-00bdd918) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bdd930`](#insn-00bdd930) → [`00c5b990`](../00c5b/00c5b990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b990` · 推定シンボル `None` · 推定型 `None`
- [`00bdd940`](#insn-00bdd940) → [`00c5b990`](../00c5b/00c5b990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b990` · 推定シンボル `None` · 推定型 `None`
- [`00bdd944`](#insn-00bdd944) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd95c`](#insn-00bdd95c) → [`00bdd96c`](#insn-00bdd96c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd968`](#insn-00bdd968) → [`00bdd970`](#insn-00bdd970) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd974`](#insn-00bdd974) → [`00c5c680`](../00c5c/00c5c680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c680` · 推定シンボル `None` · 推定型 `None`
- [`00bdd988`](#insn-00bdd988) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd990`](#insn-00bdd990) → [`00bdd9b0`](#insn-00bdd9b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd998`](#insn-00bdd998) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd99c`](#insn-00bdd99c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9a0`](#insn-00bdd9a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9a4`](#insn-00bdd9a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd9b0`](#insn-00bdd9b0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd8d0`](#insn-00bdd8d0)

~~~json
{
  "source": "00bdd8d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8d4`](#insn-00bdd8d4)

~~~json
{
  "source": "00bdd8d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8d8`](#insn-00bdd8d8)

~~~json
{
  "source": "00bdd8d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd8dc`](#insn-00bdd8dc)

~~~json
{
  "source": "00bdd8dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd900`](#insn-00bdd900)

~~~json
{
  "source": "00bdd900",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd904`](#insn-00bdd904)

~~~json
{
  "source": "00bdd904",
  "target": "00c5ef00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd90c`](#insn-00bdd90c)

~~~json
{
  "source": "00bdd90c",
  "target": "00bdd984",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd918`](#insn-00bdd918)

~~~json
{
  "source": "00bdd918",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd930`](#insn-00bdd930)

~~~json
{
  "source": "00bdd930",
  "target": "00c5b990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd940`](#insn-00bdd940)

~~~json
{
  "source": "00bdd940",
  "target": "00c5b990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd944`](#insn-00bdd944)

~~~json
{
  "source": "00bdd944",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd95c`](#insn-00bdd95c)

~~~json
{
  "source": "00bdd95c",
  "target": "00bdd96c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd968`](#insn-00bdd968)

~~~json
{
  "source": "00bdd968",
  "target": "00bdd970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd974`](#insn-00bdd974)

~~~json
{
  "source": "00bdd974",
  "target": "00c5c680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd988`](#insn-00bdd988)

~~~json
{
  "source": "00bdd988",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd990`](#insn-00bdd990)

~~~json
{
  "source": "00bdd990",
  "target": "00bdd9b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd998`](#insn-00bdd998)

~~~json
{
  "source": "00bdd998",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd99c`](#insn-00bdd99c)

~~~json
{
  "source": "00bdd99c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9a0`](#insn-00bdd9a0)

~~~json
{
  "source": "00bdd9a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9a4`](#insn-00bdd9a4)

~~~json
{
  "source": "00bdd9a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd9b0`](#insn-00bdd9b0)

~~~json
{
  "source": "00bdd9b0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
