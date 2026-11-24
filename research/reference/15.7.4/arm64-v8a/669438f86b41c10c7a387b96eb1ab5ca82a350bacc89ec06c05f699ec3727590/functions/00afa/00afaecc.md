# 00afaecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afae88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-035ce3079453cc7236c102138edff07c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5ac50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ac50.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-98ceeaa6e9dce23666f9a2e85d2924a1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaecc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eb6a43b2e56057b97ba9ef64898150f4281a04abc5bb3a74f5dde2faaa213b2",
  "source_text_sha256": "9eb6a43b2e56057b97ba9ef64898150f4281a04abc5bb3a74f5dde2faaa213b2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaecc",
        "00afaf9b"
      ]
    ],
    "bytes_sha256": "77c01d37b94e1f1784653edb68ea3848f08f83cb117081ab59e2e6d5eff45c83",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde9a0](../00bde/00bde9a0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdddd0](../00bdd/00bdddd0.md)
- [00bde2e0](../00bde/00bde2e0.md)
- [00bde750](../00bde/00bde750.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1777 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE
                 (undefined8 *param_1,void *param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  void *__ptr;
  
                    /* try { // try from 00afaed8 to 00bfaedf has its CatchHandler @ 00aff530 */
  plVar1 = *(long **)((long)param_2 + 8);
  if (*(long **)((long)param_2 + 8) == (long *)0x0) {
    plVar1 = (long *)((long)param_2 + 0x10);
    plVar3 = (long *)*plVar1;
                    /* try { // try from 00afaf08 to 00bfaf27 has its CatchHandler @ 00aff52c */
    if ((void *)*plVar3 != param_2) {
      do {
        lVar2 = *plVar1;
        plVar1 = (long *)(lVar2 + 0x10);
        plVar3 = (long *)*plVar1;
      } while (*plVar3 != lVar2);
    }
  }
  else {
    do {
      plVar3 = plVar1;
      plVar1 = (long *)*plVar3;
    } while ((long *)*plVar3 != (long *)0x0);
  }
                    /* try { // try from 00afaf28 to 00bfafaf has its CatchHandler @ 00af5650 */
  if ((void *)*param_1 == param_2) {
    *param_1 = plVar3;
  }
  param_1[2] = param_1[2] + -1;
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],param_2);
  __ptr = *(void **)((long)param_2 + 0x38);
  *(undefined8 *)((long)param_2 + 0x38) = 0;
  if (__ptr != (void *)0x0) {
    _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
    _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
    _ZdlPv(__ptr);
  }
  if ((*(byte *)((long)param_2 + 0x20) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_2 + 0x30));
  }
  _ZdlPv(param_2);
  return plVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaecc"></a> `00afaecc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaed0"></a> `00afaed0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaed4"></a> `00afaed4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaed8"></a> `00afaed8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afaedc"></a> `00afaedc` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afaee0"></a> `00afaee0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afaee4"></a> `00afaee4` | `a8 00 00 b4` | cbz x8,0x00afaef8 | `CONDITIONAL_JUMP`
<a id="insn-00afaee8"></a> `00afaee8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afaeec"></a> `00afaeec` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afaef0"></a> `00afaef0` | `c8 ff ff b5` | cbnz x8,0x00afaee8 | `CONDITIONAL_JUMP`
<a id="insn-00afaef4"></a> `00afaef4` | `0c 00 00 14` | b 0x00afaf24 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaef8"></a> `00afaef8` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afaefc"></a> `00afaefc` | `14 0d 41 f8` | ldr x20,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00afaf00"></a> `00afaf00` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00afaf04"></a> `00afaf04` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00afaf08"></a> `00afaf08` | `e0 00 00 54` | b.eq 0x00afaf24 | `CONDITIONAL_JUMP`
<a id="insn-00afaf0c"></a> `00afaf0c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afaf10"></a> `00afaf10` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00afaf14"></a> `00afaf14` | `14 0d 41 f8` | ldr x20,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00afaf18"></a> `00afaf18` | `8a 02 40 f9` | ldr x10,[x20] | `FALL_THROUGH`
<a id="insn-00afaf1c"></a> `00afaf1c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00afaf20"></a> `00afaf20` | `61 ff ff 54` | b.ne 0x00afaf0c | `CONDITIONAL_JUMP`
<a id="insn-00afaf24"></a> `00afaf24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afaf28"></a> `00afaf28` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afaf2c"></a> `00afaf2c` | `41 00 00 54` | b.ne 0x00afaf34 | `CONDITIONAL_JUMP`
<a id="insn-00afaf30"></a> `00afaf30` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00afaf34"></a> `00afaf34` | `08 a4 40 a9` | ldp x8,x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afaf38"></a> `00afaf38` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00afaf3c"></a> `00afaf3c` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afaf40"></a> `00afaf40` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf44"></a> `00afaf44` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afaf48"></a> `00afaf48` | `02 8e 03 94` | bl 0x00bde750 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf4c"></a> `00afaf4c` | `75 1e 40 f9` | ldr x21,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afaf50"></a> `00afaf50` | `7f 1e 00 f9` | str xzr,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afaf54"></a> `00afaf54` | `f5 00 00 b4` | cbz x21,0x00afaf70 | `CONDITIONAL_JUMP`
<a id="insn-00afaf58"></a> `00afaf58` | `a0 a2 01 91` | add x0,x21,#0x68 | `FALL_THROUGH`
<a id="insn-00afaf5c"></a> `00afaf5c` | `e1 8c 03 94` | bl 0x00bde2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf60"></a> `00afaf60` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afaf64"></a> `00afaf64` | `9b 8b 03 94` | bl 0x00bdddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf68"></a> `00afaf68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afaf6c"></a> `00afaf6c` | `3d 80 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf70"></a> `00afaf70` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf74"></a> `00afaf74` | `68 00 00 36` | tbz w8,#0x0,0x00afaf80 | `CONDITIONAL_JUMP`
<a id="insn-00afaf78"></a> `00afaf78` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00afaf7c"></a> `00afaf7c` | `39 80 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf80"></a> `00afaf80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afaf84"></a> `00afaf84` | `37 80 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf88"></a> `00afaf88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afaf8c"></a> `00afaf8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf90"></a> `00afaf90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf94"></a> `00afaf94` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afaf98"></a> `00afaf98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaecc`](#insn-00afaecc) 範囲 `[['00afaecc', '00afaed7']]`
  - `FALL_THROUGH` [`00afaed4`](#insn-00afaed4) → [`00afaed8`](#insn-00afaed8)
- ブロック [`00afaed8`](#insn-00afaed8) 範囲 `[['00afaed8', '00afaee7']]`
  - `CONDITIONAL_JUMP` [`00afaee4`](#insn-00afaee4) → [`00afaef8`](#insn-00afaef8)
  - `FALL_THROUGH` [`00afaee4`](#insn-00afaee4) → [`00afaee8`](#insn-00afaee8)
- ブロック [`00afaee8`](#insn-00afaee8) 範囲 `[['00afaee8', '00afaef3']]`
  - `CONDITIONAL_JUMP` [`00afaef0`](#insn-00afaef0) → [`00afaee8`](#insn-00afaee8)
  - `FALL_THROUGH` [`00afaef0`](#insn-00afaef0) → [`00afaef4`](#insn-00afaef4)
- ブロック [`00afaef4`](#insn-00afaef4) 範囲 `[['00afaef4', '00afaef7']]`
  - `UNCONDITIONAL_JUMP` [`00afaef4`](#insn-00afaef4) → [`00afaf24`](#insn-00afaf24)
- ブロック [`00afaef8`](#insn-00afaef8) 範囲 `[['00afaef8', '00afaf07']]`
  - `FALL_THROUGH` [`00afaf04`](#insn-00afaf04) → [`00afaf08`](#insn-00afaf08)
- ブロック [`00afaf08`](#insn-00afaf08) 範囲 `[['00afaf08', '00afaf0b']]`
  - `CONDITIONAL_JUMP` [`00afaf08`](#insn-00afaf08) → [`00afaf24`](#insn-00afaf24)
  - `FALL_THROUGH` [`00afaf08`](#insn-00afaf08) → [`00afaf0c`](#insn-00afaf0c)
- ブロック [`00afaf0c`](#insn-00afaf0c) 範囲 `[['00afaf0c', '00afaf23']]`
  - `CONDITIONAL_JUMP` [`00afaf20`](#insn-00afaf20) → [`00afaf0c`](#insn-00afaf0c)
  - `FALL_THROUGH` [`00afaf20`](#insn-00afaf20) → [`00afaf24`](#insn-00afaf24)
- ブロック [`00afaf24`](#insn-00afaf24) 範囲 `[['00afaf24', '00afaf27']]`
  - `FALL_THROUGH` [`00afaf24`](#insn-00afaf24) → [`00afaf28`](#insn-00afaf28)
- ブロック [`00afaf28`](#insn-00afaf28) 範囲 `[['00afaf28', '00afaf2f']]`
  - `CONDITIONAL_JUMP` [`00afaf2c`](#insn-00afaf2c) → [`00afaf34`](#insn-00afaf34)
  - `FALL_THROUGH` [`00afaf2c`](#insn-00afaf2c) → [`00afaf30`](#insn-00afaf30)
- ブロック [`00afaf30`](#insn-00afaf30) 範囲 `[['00afaf30', '00afaf33']]`
  - `FALL_THROUGH` [`00afaf30`](#insn-00afaf30) → [`00afaf34`](#insn-00afaf34)
- ブロック [`00afaf34`](#insn-00afaf34) 範囲 `[['00afaf34', '00afaf57']]`
  - `CONDITIONAL_JUMP` [`00afaf54`](#insn-00afaf54) → [`00afaf70`](#insn-00afaf70)
  - `FALL_THROUGH` [`00afaf54`](#insn-00afaf54) → [`00afaf58`](#insn-00afaf58)
- ブロック [`00afaf58`](#insn-00afaf58) 範囲 `[['00afaf58', '00afaf6f']]`
  - `FALL_THROUGH` [`00afaf6c`](#insn-00afaf6c) → [`00afaf70`](#insn-00afaf70)
- ブロック [`00afaf70`](#insn-00afaf70) 範囲 `[['00afaf70', '00afaf77']]`
  - `CONDITIONAL_JUMP` [`00afaf74`](#insn-00afaf74) → [`00afaf80`](#insn-00afaf80)
  - `FALL_THROUGH` [`00afaf74`](#insn-00afaf74) → [`00afaf78`](#insn-00afaf78)
- ブロック [`00afaf78`](#insn-00afaf78) 範囲 `[['00afaf78', '00afaf7f']]`
  - `FALL_THROUGH` [`00afaf7c`](#insn-00afaf7c) → [`00afaf80`](#insn-00afaf80)
- ブロック [`00afaf80`](#insn-00afaf80) 範囲 `[['00afaf80', '00afaf9b']]`

## 命令位置別の参照

- [`00afaecc`](#insn-00afaecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaed0`](#insn-00afaed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaed4`](#insn-00afaed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaee4`](#insn-00afaee4) → [`00afaef8`](#insn-00afaef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaef0`](#insn-00afaef0) → [`00afaee8`](#insn-00afaee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaef4`](#insn-00afaef4) → [`00afaf24`](#insn-00afaf24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf08`](#insn-00afaf08) → [`00afaf24`](#insn-00afaf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf20`](#insn-00afaf20) → [`00afaf0c`](#insn-00afaf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf2c`](#insn-00afaf2c) → [`00afaf34`](#insn-00afaf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf48`](#insn-00afaf48) → [`00bde750`](../00bde/00bde750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde750` · 推定シンボル `None` · 推定型 `None`
- [`00afaf54`](#insn-00afaf54) → [`00afaf70`](#insn-00afaf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf5c`](#insn-00afaf5c) → [`00bde2e0`](../00bde/00bde2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2e0` · 推定シンボル `None` · 推定型 `None`
- [`00afaf64`](#insn-00afaf64) → [`00bdddd0`](../00bdd/00bdddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddd0` · 推定シンボル `None` · 推定型 `None`
- [`00afaf6c`](#insn-00afaf6c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaf74`](#insn-00afaf74) → [`00afaf80`](#insn-00afaf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf7c`](#insn-00afaf7c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaf84`](#insn-00afaf84) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaf8c`](#insn-00afaf8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf90`](#insn-00afaf90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaecc`](#insn-00afaecc)

~~~json
{
  "source": "00afaecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaed0`](#insn-00afaed0)

~~~json
{
  "source": "00afaed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaed4`](#insn-00afaed4)

~~~json
{
  "source": "00afaed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaee4`](#insn-00afaee4)

~~~json
{
  "source": "00afaee4",
  "target": "00afaef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaef0`](#insn-00afaef0)

~~~json
{
  "source": "00afaef0",
  "target": "00afaee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaef4`](#insn-00afaef4)

~~~json
{
  "source": "00afaef4",
  "target": "00afaf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf08`](#insn-00afaf08)

~~~json
{
  "source": "00afaf08",
  "target": "00afaf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf20`](#insn-00afaf20)

~~~json
{
  "source": "00afaf20",
  "target": "00afaf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf2c`](#insn-00afaf2c)

~~~json
{
  "source": "00afaf2c",
  "target": "00afaf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf48`](#insn-00afaf48)

~~~json
{
  "source": "00afaf48",
  "target": "00bde750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf54`](#insn-00afaf54)

~~~json
{
  "source": "00afaf54",
  "target": "00afaf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf5c`](#insn-00afaf5c)

~~~json
{
  "source": "00afaf5c",
  "target": "00bde2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf64`](#insn-00afaf64)

~~~json
{
  "source": "00afaf64",
  "target": "00bdddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf6c`](#insn-00afaf6c)

~~~json
{
  "source": "00afaf6c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf74`](#insn-00afaf74)

~~~json
{
  "source": "00afaf74",
  "target": "00afaf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf7c`](#insn-00afaf7c)

~~~json
{
  "source": "00afaf7c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf84`](#insn-00afaf84)

~~~json
{
  "source": "00afaf84",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf8c`](#insn-00afaf8c)

~~~json
{
  "source": "00afaf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf90`](#insn-00afaf90)

~~~json
{
  "source": "00afaf90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
