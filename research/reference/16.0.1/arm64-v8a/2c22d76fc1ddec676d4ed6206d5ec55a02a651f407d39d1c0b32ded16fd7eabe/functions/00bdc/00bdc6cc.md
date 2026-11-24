# 00bdc6cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc2a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc2a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-dcd6de7be73f87f66e25f908b7c3a8c5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdc768`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc768.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-3dc4920c0df47b5f83891f1e3f46ef7f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc6cc",
  "name": "_ZN8firebase4auth18AdditionalUserInfoC2ERKS1_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56b0cde10a21b4873f79356a852a6b9f6ebe10262ee18051a5b75331e8d628e8",
  "source_text_sha256": "56b0cde10a21b4873f79356a852a6b9f6ebe10262ee18051a5b75331e8d628e8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdc6cc",
        "00bdc7c7"
      ]
    ],
    "bytes_sha256": "0d549ae2aaaef83e1939c03c1b4f0e11c86d77f308d62477d3c42d5fccfda1a9",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5de20](../00c5d/00c5de20.md)

## 呼び出し先

- [00c5b5b0](../00c5b/00c5b5b0.md)
- [00c5dd60](../00c5d/00c5dd60.md)
- [00c5de70](../00c5d/00c5de70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1964 bytes

~~~c

void _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_(long param_1,long param_2)

{
  bool bVar1;
  long *plVar2;
  long lVar3;
  undefined8 *puVar4;
  long *plVar5;
  
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_();
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x18,param_2 + 0x18);
  puVar4 = (undefined8 *)(param_1 + 0x38);
  *puVar4 = 0;
  *(undefined8 *)(param_1 + 0x30) = puVar4;
  *(undefined8 *)(param_1 + 0x40) = 0;
  plVar5 = *(long **)(param_2 + 0x30);
  while (plVar5 != (long *)(param_2 + 0x38)) {
    _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emplace_hint_unique_key_argsIS3_JRKNS_4pairIKS3_S3_EEEEENS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEENS_21__tree_const_iteratorIS4_SM_lEERKT_DpOT0_
              ((undefined8 *)(param_1 + 0x30),puVar4,plVar5 + 4,plVar5 + 4);
    plVar2 = (long *)plVar5[1];
    if ((long *)plVar5[1] == (long *)0x0) {
      plVar2 = plVar5 + 2;
      bVar1 = *(long **)*plVar2 != plVar5;
      plVar5 = (long *)*plVar2;
      if (bVar1) {
        do {
          lVar3 = *plVar2;
                    /* try { // try from 00bdc77c to 00cdc79b has its CatchHandler @ 00bdebdc */
          plVar2 = (long *)(lVar3 + 0x10);
          plVar5 = (long *)*plVar2;
        } while (*plVar5 != lVar3);
      }
    }
    else {
      do {
        plVar5 = plVar2;
        plVar2 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
    }
  }
  *(undefined8 *)(param_1 + 0x48) = 0;
                    /* try { // try from 00bdc79c to 00cdc89f has its CatchHandler @ 00bd6f4c */
  *(undefined4 *)(param_1 + 0x50) = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 *)(param_1 + 0x60) = 0;
  *(undefined8 *)(param_1 + 0x68) = 0;
  _ZN8firebase4auth10CredentialaSERKS1_((undefined8 *)(param_1 + 0x48),param_2 + 0x48);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdc6cc"></a> `00bdc6cc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bdc6d0"></a> `00bdc6d0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc6d4"></a> `00bdc6d4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc6d8"></a> `00bdc6d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdc6dc"></a> `00bdc6dc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdc6e0"></a> `00bdc6e0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdc6e4"></a> `00bdc6e4` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bdc6e8"></a> `00bdc6e8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdc6ec"></a> `00bdc6ec` | `b1 fb 01 94` | bl 0x00c5b5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc6f0"></a> `00bdc6f0` | `74 62 00 91` | add x20,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bdc6f4"></a> `00bdc6f4` | `e1 62 00 91` | add x1,x23,#0x18 | `FALL_THROUGH`
<a id="insn-00bdc6f8"></a> `00bdc6f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdc6fc"></a> `00bdc6fc` | `ad fb 01 94` | bl 0x00c5b5b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc700"></a> `00bdc700` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00bdc704"></a> `00bdc704` | `df 8e 03 f8` | str xzr,[x22, #0x38]! | `FALL_THROUGH`
<a id="insn-00bdc708"></a> `00bdc708` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00bdc70c"></a> `00bdc70c` | `b6 0e 03 f8` | str x22,[x21, #0x30]! | `FALL_THROUGH`
<a id="insn-00bdc710"></a> `00bdc710` | `bf 0a 00 f9` | str xzr,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc714"></a> `00bdc714` | `f9 1a 40 f9` | ldr x25,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bdc718"></a> `00bdc718` | `f8 e2 00 91` | add x24,x23,#0x38 | `FALL_THROUGH`
<a id="insn-00bdc71c"></a> `00bdc71c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bdc720"></a> `00bdc720` | `a1 00 00 54` | b.ne 0x00bdc734 | `CONDITIONAL_JUMP`
<a id="insn-00bdc724"></a> `00bdc724` | `1b 00 00 14` | b 0x00bdc790 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdc728"></a> `00bdc728` | `f9 03 09 aa` | mov x25,x9 | `FALL_THROUGH`
<a id="insn-00bdc72c"></a> `00bdc72c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bdc730"></a> `00bdc730` | `00 03 00 54` | b.eq 0x00bdc790 | `CONDITIONAL_JUMP`
<a id="insn-00bdc734"></a> `00bdc734` | `22 83 00 91` | add x2,x25,#0x20 | `FALL_THROUGH`
<a id="insn-00bdc738"></a> `00bdc738` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc73c"></a> `00bdc73c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdc740"></a> `00bdc740` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdc744"></a> `00bdc744` | `cb 05 02 94` | bl 0x00c5de70 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc748"></a> `00bdc748` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bdc74c"></a> `00bdc74c` | `a8 00 00 b4` | cbz x8,0x00bdc760 | `CONDITIONAL_JUMP`
<a id="insn-00bdc750"></a> `00bdc750` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00bdc754"></a> `00bdc754` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bdc758"></a> `00bdc758` | `c8 ff ff b5` | cbnz x8,0x00bdc750 | `CONDITIONAL_JUMP`
<a id="insn-00bdc75c"></a> `00bdc75c` | `f4 ff ff 17` | b 0x00bdc72c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdc760"></a> `00bdc760` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00bdc764"></a> `00bdc764` | `09 0d 41 f8` | ldr x9,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdc768"></a> `00bdc768` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bdc76c"></a> `00bdc76c` | `5f 01 19 eb` | cmp x10,x25 | `FALL_THROUGH`
<a id="insn-00bdc770"></a> `00bdc770` | `c0 fd ff 54` | b.eq 0x00bdc728 | `CONDITIONAL_JUMP`
<a id="insn-00bdc774"></a> `00bdc774` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bdc778"></a> `00bdc778` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bdc77c"></a> `00bdc77c` | `19 0d 41 f8` | ldr x25,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdc780"></a> `00bdc780` | `2a 03 40 f9` | ldr x10,[x25] | `FALL_THROUGH`
<a id="insn-00bdc784"></a> `00bdc784` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bdc788"></a> `00bdc788` | `61 ff ff 54` | b.ne 0x00bdc774 | `CONDITIONAL_JUMP`
<a id="insn-00bdc78c"></a> `00bdc78c` | `e8 ff ff 17` | b 0x00bdc72c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdc790"></a> `00bdc790` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdc794"></a> `00bdc794` | `1f 8c 04 f8` | str xzr,[x0, #0x48]! | `FALL_THROUGH`
<a id="insn-00bdc798"></a> `00bdc798` | `e1 22 01 91` | add x1,x23,#0x48 | `FALL_THROUGH`
<a id="insn-00bdc79c"></a> `00bdc79c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdc7a0"></a> `00bdc7a0` | `1f 08 00 b9` | str wzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bdc7a4"></a> `00bdc7a4` | `ff 0e 01 f8` | str xzr,[x23, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdc7a8"></a> `00bdc7a8` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bdc7ac"></a> `00bdc7ac` | `6d 05 02 94` | bl 0x00c5dd60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc7b0"></a> `00bdc7b0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdc7b4"></a> `00bdc7b4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdc7b8"></a> `00bdc7b8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc7bc"></a> `00bdc7bc` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc7c0"></a> `00bdc7c0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdc7c4"></a> `00bdc7c4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdc6cc`](#insn-00bdc6cc) 範囲 `[['00bdc6cc', '00bdc723']]`
  - `CONDITIONAL_JUMP` [`00bdc720`](#insn-00bdc720) → [`00bdc734`](#insn-00bdc734)
  - `FALL_THROUGH` [`00bdc720`](#insn-00bdc720) → [`00bdc724`](#insn-00bdc724)
- ブロック [`00bdc724`](#insn-00bdc724) 範囲 `[['00bdc724', '00bdc727']]`
  - `UNCONDITIONAL_JUMP` [`00bdc724`](#insn-00bdc724) → [`00bdc790`](#insn-00bdc790)
- ブロック [`00bdc728`](#insn-00bdc728) 範囲 `[['00bdc728', '00bdc72b']]`
  - `FALL_THROUGH` [`00bdc728`](#insn-00bdc728) → [`00bdc72c`](#insn-00bdc72c)
- ブロック [`00bdc72c`](#insn-00bdc72c) 範囲 `[['00bdc72c', '00bdc733']]`
  - `CONDITIONAL_JUMP` [`00bdc730`](#insn-00bdc730) → [`00bdc790`](#insn-00bdc790)
  - `FALL_THROUGH` [`00bdc730`](#insn-00bdc730) → [`00bdc734`](#insn-00bdc734)
- ブロック [`00bdc734`](#insn-00bdc734) 範囲 `[['00bdc734', '00bdc74f']]`
  - `CONDITIONAL_JUMP` [`00bdc74c`](#insn-00bdc74c) → [`00bdc760`](#insn-00bdc760)
  - `FALL_THROUGH` [`00bdc74c`](#insn-00bdc74c) → [`00bdc750`](#insn-00bdc750)
- ブロック [`00bdc750`](#insn-00bdc750) 範囲 `[['00bdc750', '00bdc75b']]`
  - `CONDITIONAL_JUMP` [`00bdc758`](#insn-00bdc758) → [`00bdc750`](#insn-00bdc750)
  - `FALL_THROUGH` [`00bdc758`](#insn-00bdc758) → [`00bdc75c`](#insn-00bdc75c)
- ブロック [`00bdc75c`](#insn-00bdc75c) 範囲 `[['00bdc75c', '00bdc75f']]`
  - `UNCONDITIONAL_JUMP` [`00bdc75c`](#insn-00bdc75c) → [`00bdc72c`](#insn-00bdc72c)
- ブロック [`00bdc760`](#insn-00bdc760) 範囲 `[['00bdc760', '00bdc773']]`
  - `CONDITIONAL_JUMP` [`00bdc770`](#insn-00bdc770) → [`00bdc728`](#insn-00bdc728)
  - `FALL_THROUGH` [`00bdc770`](#insn-00bdc770) → [`00bdc774`](#insn-00bdc774)
- ブロック [`00bdc774`](#insn-00bdc774) 範囲 `[['00bdc774', '00bdc77b']]`
  - `FALL_THROUGH` [`00bdc778`](#insn-00bdc778) → [`00bdc77c`](#insn-00bdc77c)
- ブロック [`00bdc77c`](#insn-00bdc77c) 範囲 `[['00bdc77c', '00bdc78b']]`
  - `CONDITIONAL_JUMP` [`00bdc788`](#insn-00bdc788) → [`00bdc774`](#insn-00bdc774)
  - `FALL_THROUGH` [`00bdc788`](#insn-00bdc788) → [`00bdc78c`](#insn-00bdc78c)
- ブロック [`00bdc78c`](#insn-00bdc78c) 範囲 `[['00bdc78c', '00bdc78f']]`
  - `UNCONDITIONAL_JUMP` [`00bdc78c`](#insn-00bdc78c) → [`00bdc72c`](#insn-00bdc72c)
- ブロック [`00bdc790`](#insn-00bdc790) 範囲 `[['00bdc790', '00bdc79b']]`
  - `FALL_THROUGH` [`00bdc798`](#insn-00bdc798) → [`00bdc79c`](#insn-00bdc79c)
- ブロック [`00bdc79c`](#insn-00bdc79c) 範囲 `[['00bdc79c', '00bdc7c7']]`

## 命令位置別の参照

- [`00bdc6cc`](#insn-00bdc6cc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6d0`](#insn-00bdc6d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6d4`](#insn-00bdc6d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6d8`](#insn-00bdc6d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6dc`](#insn-00bdc6dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6ec`](#insn-00bdc6ec) → [`00c5b5b0`](../00c5b/00c5b5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc6fc`](#insn-00bdc6fc) → [`00c5b5b0`](../00c5b/00c5b5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc720`](#insn-00bdc720) → [`00bdc734`](#insn-00bdc734) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc724`](#insn-00bdc724) → [`00bdc790`](#insn-00bdc790) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc730`](#insn-00bdc730) → [`00bdc790`](#insn-00bdc790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc744`](#insn-00bdc744) → [`00c5de70`](../00c5d/00c5de70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de70` · 推定シンボル `None` · 推定型 `None`
- [`00bdc74c`](#insn-00bdc74c) → [`00bdc760`](#insn-00bdc760) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc758`](#insn-00bdc758) → [`00bdc750`](#insn-00bdc750) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc75c`](#insn-00bdc75c) → [`00bdc72c`](#insn-00bdc72c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc770`](#insn-00bdc770) → [`00bdc728`](#insn-00bdc728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc788`](#insn-00bdc788) → [`00bdc774`](#insn-00bdc774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc78c`](#insn-00bdc78c) → [`00bdc72c`](#insn-00bdc72c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc7ac`](#insn-00bdc7ac) → [`00c5dd60`](../00c5d/00c5dd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd60` · 推定シンボル `None` · 推定型 `None`
- [`00bdc7b0`](#insn-00bdc7b0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc7b4`](#insn-00bdc7b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc7b8`](#insn-00bdc7b8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc7bc`](#insn-00bdc7bc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdc6cc`](#insn-00bdc6cc)

~~~json
{
  "source": "00bdc6cc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc6d0`](#insn-00bdc6d0)

~~~json
{
  "source": "00bdc6d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc6d4`](#insn-00bdc6d4)

~~~json
{
  "source": "00bdc6d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc6d8`](#insn-00bdc6d8)

~~~json
{
  "source": "00bdc6d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc6dc`](#insn-00bdc6dc)

~~~json
{
  "source": "00bdc6dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc6ec`](#insn-00bdc6ec)

~~~json
{
  "source": "00bdc6ec",
  "target": "00c5b5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc6fc`](#insn-00bdc6fc)

~~~json
{
  "source": "00bdc6fc",
  "target": "00c5b5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc720`](#insn-00bdc720)

~~~json
{
  "source": "00bdc720",
  "target": "00bdc734",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc724`](#insn-00bdc724)

~~~json
{
  "source": "00bdc724",
  "target": "00bdc790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc730`](#insn-00bdc730)

~~~json
{
  "source": "00bdc730",
  "target": "00bdc790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc744`](#insn-00bdc744)

~~~json
{
  "source": "00bdc744",
  "target": "00c5de70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc74c`](#insn-00bdc74c)

~~~json
{
  "source": "00bdc74c",
  "target": "00bdc760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc758`](#insn-00bdc758)

~~~json
{
  "source": "00bdc758",
  "target": "00bdc750",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc75c`](#insn-00bdc75c)

~~~json
{
  "source": "00bdc75c",
  "target": "00bdc72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc770`](#insn-00bdc770)

~~~json
{
  "source": "00bdc770",
  "target": "00bdc728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc788`](#insn-00bdc788)

~~~json
{
  "source": "00bdc788",
  "target": "00bdc774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc78c`](#insn-00bdc78c)

~~~json
{
  "source": "00bdc78c",
  "target": "00bdc72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc7ac`](#insn-00bdc7ac)

~~~json
{
  "source": "00bdc7ac",
  "target": "00c5dd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc7b0`](#insn-00bdc7b0)

~~~json
{
  "source": "00bdc7b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc7b4`](#insn-00bdc7b4)

~~~json
{
  "source": "00bdc7b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc7b8`](#insn-00bdc7b8)

~~~json
{
  "source": "00bdc7b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc7bc`](#insn-00bdc7bc)

~~~json
{
  "source": "00bdc7bc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
