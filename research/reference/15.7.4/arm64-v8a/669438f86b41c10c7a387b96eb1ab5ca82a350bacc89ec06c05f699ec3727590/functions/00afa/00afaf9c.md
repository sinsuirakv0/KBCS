# 00afaf9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afaf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-d0d7f894153241467ce7a4ba7c7ca043)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5ad20`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5ad20.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-8d4e996d2768411864b39180dccecd20)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaf9c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "580519bd9d2f6d49930136fd939123f0c5abddd15bc844ce3cd616787037cbb6",
  "source_text_sha256": "580519bd9d2f6d49930136fd939123f0c5abddd15bc844ce3cd616787037cbb6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaf9c",
        "00afb00f"
      ]
    ],
    "bytes_sha256": "fb2b1ae432779d33447aa3396b6c057944574f4a6261e31ba137769171149869",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde9b0](../00bde/00bde9b0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdddd0](../00bdd/00bdddd0.md)
- [00bde2e0](../00bde/00bde2e0.md)
- [00bde9b0](../00bde/00bde9b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1652 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  void *__ptr;
  
  if (param_2 != (undefined8 *)0x0) {
                    /* try { // try from 00afafb0 to 00bfafc3 has its CatchHandler @ 00aff51c */
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
              (param_1,*param_2);
                    /* try { // try from 00afafc4 to 00bfaff3 has its CatchHandler @ 00af5650 */
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE7destroyEPNS_11__tree_nodeISF_PvEE
              (param_1,param_2[1]);
    __ptr = (void *)param_2[7];
    param_2[7] = 0;
    if (__ptr != (void *)0x0) {
      _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
      _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
      _ZdlPv(__ptr);
    }
    if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* try { // try from 00afaff4 to 00bfb017 has its CatchHandler @ 00b003c0 */
      _ZdlPv((void *)param_2[6]);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaf9c"></a> `00afaf9c` | `81 03 00 b4` | cbz x1,0x00afb00c | `CONDITIONAL_JUMP`
<a id="insn-00afafa0"></a> `00afafa0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afafa4"></a> `00afafa4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afafa8"></a> `00afafa8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afafac"></a> `00afafac` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afafb0"></a> `00afafb0` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00afafb4"></a> `00afafb4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afafb8"></a> `00afafb8` | `7e 8e 03 94` | bl 0x00bde9b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afafbc"></a> `00afafbc` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afafc0"></a> `00afafc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afafc4"></a> `00afafc4` | `7b 8e 03 94` | bl 0x00bde9b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afafc8"></a> `00afafc8` | `74 1e 40 f9` | ldr x20,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afafcc"></a> `00afafcc` | `7f 1e 00 f9` | str xzr,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afafd0"></a> `00afafd0` | `f4 00 00 b4` | cbz x20,0x00afafec | `CONDITIONAL_JUMP`
<a id="insn-00afafd4"></a> `00afafd4` | `80 a2 01 91` | add x0,x20,#0x68 | `FALL_THROUGH`
<a id="insn-00afafd8"></a> `00afafd8` | `c2 8c 03 94` | bl 0x00bde2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afafdc"></a> `00afafdc` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00afafe0"></a> `00afafe0` | `7c 8b 03 94` | bl 0x00bdddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afafe4"></a> `00afafe4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afafe8"></a> `00afafe8` | `1e 80 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afafec"></a> `00afafec` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00afaff0"></a> `00afaff0` | `68 00 00 36` | tbz w8,#0x0,0x00afaffc | `CONDITIONAL_JUMP`
<a id="insn-00afaff4"></a> `00afaff4` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00afaff8"></a> `00afaff8` | `1a 80 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00afaffc"></a> `00afaffc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb000"></a> `00afb000` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afb004"></a> `00afb004` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afb008"></a> `00afb008` | `16 80 03 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-00afb00c"></a> `00afb00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaf9c`](#insn-00afaf9c) 範囲 `[['00afaf9c', '00afaf9f']]`
  - `CONDITIONAL_JUMP` [`00afaf9c`](#insn-00afaf9c) → [`00afb00c`](#insn-00afb00c)
  - `FALL_THROUGH` [`00afaf9c`](#insn-00afaf9c) → [`00afafa0`](#insn-00afafa0)
- ブロック [`00afafa0`](#insn-00afafa0) 範囲 `[['00afafa0', '00afafaf']]`
  - `FALL_THROUGH` [`00afafac`](#insn-00afafac) → [`00afafb0`](#insn-00afafb0)
- ブロック [`00afafb0`](#insn-00afafb0) 範囲 `[['00afafb0', '00afafc3']]`
  - `FALL_THROUGH` [`00afafc0`](#insn-00afafc0) → [`00afafc4`](#insn-00afafc4)
- ブロック [`00afafc4`](#insn-00afafc4) 範囲 `[['00afafc4', '00afafd3']]`
  - `CONDITIONAL_JUMP` [`00afafd0`](#insn-00afafd0) → [`00afafec`](#insn-00afafec)
  - `FALL_THROUGH` [`00afafd0`](#insn-00afafd0) → [`00afafd4`](#insn-00afafd4)
- ブロック [`00afafd4`](#insn-00afafd4) 範囲 `[['00afafd4', '00afafeb']]`
  - `FALL_THROUGH` [`00afafe8`](#insn-00afafe8) → [`00afafec`](#insn-00afafec)
- ブロック [`00afafec`](#insn-00afafec) 範囲 `[['00afafec', '00afaff3']]`
  - `CONDITIONAL_JUMP` [`00afaff0`](#insn-00afaff0) → [`00afaffc`](#insn-00afaffc)
  - `FALL_THROUGH` [`00afaff0`](#insn-00afaff0) → [`00afaff4`](#insn-00afaff4)
- ブロック [`00afaff4`](#insn-00afaff4) 範囲 `[['00afaff4', '00afaffb']]`
  - `FALL_THROUGH` [`00afaff8`](#insn-00afaff8) → [`00afaffc`](#insn-00afaffc)
- ブロック [`00afaffc`](#insn-00afaffc) 範囲 `[['00afaffc', '00afb00b']]`
- ブロック [`00afb00c`](#insn-00afb00c) 範囲 `[['00afb00c', '00afb00f']]`

## 命令位置別の参照

- [`00afaf9c`](#insn-00afaf9c) → [`00afb00c`](#insn-00afb00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafa0`](#insn-00afafa0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafa4`](#insn-00afafa4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafb8`](#insn-00afafb8) → [`00bde9b0`](../00bde/00bde9b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9b0` · 推定シンボル `None` · 推定型 `None`
- [`00afafc4`](#insn-00afafc4) → [`00bde9b0`](../00bde/00bde9b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9b0` · 推定シンボル `None` · 推定型 `None`
- [`00afafd0`](#insn-00afafd0) → [`00afafec`](#insn-00afafec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafd8`](#insn-00afafd8) → [`00bde2e0`](../00bde/00bde2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2e0` · 推定シンボル `None` · 推定型 `None`
- [`00afafe0`](#insn-00afafe0) → [`00bdddd0`](../00bdd/00bdddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddd0` · 推定シンボル `None` · 推定型 `None`
- [`00afafe8`](#insn-00afafe8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaff0`](#insn-00afaff0) → [`00afaffc`](#insn-00afaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaff8`](#insn-00afaff8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00afaffc`](#insn-00afaffc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb008`](#insn-00afb008) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaf9c`](#insn-00afaf9c)

~~~json
{
  "source": "00afaf9c",
  "target": "00afb00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafa0`](#insn-00afafa0)

~~~json
{
  "source": "00afafa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafa4`](#insn-00afafa4)

~~~json
{
  "source": "00afafa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafb8`](#insn-00afafb8)

~~~json
{
  "source": "00afafb8",
  "target": "00bde9b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafc4`](#insn-00afafc4)

~~~json
{
  "source": "00afafc4",
  "target": "00bde9b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafd0`](#insn-00afafd0)

~~~json
{
  "source": "00afafd0",
  "target": "00afafec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafd8`](#insn-00afafd8)

~~~json
{
  "source": "00afafd8",
  "target": "00bde2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafe0`](#insn-00afafe0)

~~~json
{
  "source": "00afafe0",
  "target": "00bdddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafe8`](#insn-00afafe8)

~~~json
{
  "source": "00afafe8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaff0`](#insn-00afaff0)

~~~json
{
  "source": "00afaff0",
  "target": "00afaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaff8`](#insn-00afaff8)

~~~json
{
  "source": "00afaff8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaffc`](#insn-00afaffc)

~~~json
{
  "source": "00afaffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb008`](#insn-00afb008)

~~~json
{
  "source": "00afb008",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
