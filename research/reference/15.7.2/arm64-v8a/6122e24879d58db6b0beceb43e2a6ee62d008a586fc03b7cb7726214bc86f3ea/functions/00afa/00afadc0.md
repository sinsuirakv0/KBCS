# 00afadc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afae88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-58f0566eebbd6d0b9ecf4d0803bc9f1c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afadc0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bc5033779428ff5df26e41a3413f792872432dbea8e6894f91a4400bced04436",
  "source_text_sha256": "bc5033779428ff5df26e41a3413f792872432dbea8e6894f91a4400bced04436",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afadc0",
        "00afae8f"
      ]
    ],
    "bytes_sha256": "cd37ecda8ac71a991011c4b01a60da24b41a207189cef805ff06a4be4c7b3972",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde8a0](../00bde/00bde8a0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bddcd0](../00bdd/00bddcd0.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bde650](../00bde/00bde650.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1874 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE5eraseENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEE
                 (undefined8 *param_1,void *param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  void *__ptr;
  
  plVar1 = *(long **)((long)param_2 + 8);
  if (*(long **)((long)param_2 + 8) == (long *)0x0) {
    plVar1 = (long *)((long)param_2 + 0x10);
    plVar3 = (long *)*plVar1;
    if ((void *)*plVar3 != param_2) {
      do {
                    /* try { // try from 00afae00 to 00bfae07 has its CatchHandler @ 00aff4fc */
        lVar2 = *plVar1;
        plVar1 = (long *)(lVar2 + 0x10);
        plVar3 = (long *)*plVar1;
      } while (*plVar3 != lVar2);
    }
  }
  else {
    do {
                    /* try { // try from 00afaddc to 00bfadef has its CatchHandler @ 00aff500 */
      plVar3 = plVar1;
      plVar1 = (long *)*plVar3;
    } while ((long *)*plVar3 != (long *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = plVar3;
  }
                    /* try { // try from 00afae30 to 00bfae43 has its CatchHandler @ 00aff4f8 */
  param_1[2] = param_1[2] + -1;
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],param_2);
  __ptr = *(void **)((long)param_2 + 0x38);
  *(undefined8 *)((long)param_2 + 0x38) = 0;
  if (__ptr != (void *)0x0) {
    _ZN8firebase6LoggerD2Ev((long)__ptr + 0x68);
    _ZN8firebase15CleanupNotifierD2Ev((long)__ptr + 8);
    _ZdlPv(__ptr);
  }
                    /* try { // try from 00afae64 to 00bfae6b has its CatchHandler @ 00aff4f4 */
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
<a id="insn-00afadc0"></a> `00afadc0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afadc4"></a> `00afadc4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afadc8"></a> `00afadc8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afadcc"></a> `00afadcc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afadd0"></a> `00afadd0` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afadd4"></a> `00afadd4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afadd8"></a> `00afadd8` | `a8 00 00 b4` | cbz x8,0x00afadec | `CONDITIONAL_JUMP`
<a id="insn-00afaddc"></a> `00afaddc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00afade0"></a> `00afade0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afade4"></a> `00afade4` | `c8 ff ff b5` | cbnz x8,0x00afaddc | `CONDITIONAL_JUMP`
<a id="insn-00afade8"></a> `00afade8` | `0c 00 00 14` | b 0x00afae18 | `UNCONDITIONAL_JUMP`
<a id="insn-00afadec"></a> `00afadec` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afadf0"></a> `00afadf0` | `14 0d 41 f8` | ldr x20,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00afadf4"></a> `00afadf4` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00afadf8"></a> `00afadf8` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00afadfc"></a> `00afadfc` | `e0 00 00 54` | b.eq 0x00afae18 | `CONDITIONAL_JUMP`
<a id="insn-00afae00"></a> `00afae00` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afae04"></a> `00afae04` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00afae08"></a> `00afae08` | `14 0d 41 f8` | ldr x20,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00afae0c"></a> `00afae0c` | `8a 02 40 f9` | ldr x10,[x20] | `FALL_THROUGH`
<a id="insn-00afae10"></a> `00afae10` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00afae14"></a> `00afae14` | `61 ff ff 54` | b.ne 0x00afae00 | `CONDITIONAL_JUMP`
<a id="insn-00afae18"></a> `00afae18` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afae1c"></a> `00afae1c` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afae20"></a> `00afae20` | `41 00 00 54` | b.ne 0x00afae28 | `CONDITIONAL_JUMP`
<a id="insn-00afae24"></a> `00afae24` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00afae28"></a> `00afae28` | `08 a4 40 a9` | ldp x8,x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afae2c"></a> `00afae2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00afae30"></a> `00afae30` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afae34"></a> `00afae34` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afae38"></a> `00afae38` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afae3c"></a> `00afae3c` | `05 8e 03 94` | bl 0x00bde650 | `UNCONDITIONAL_CALL`
<a id="insn-00afae40"></a> `00afae40` | `75 1e 40 f9` | ldr x21,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afae44"></a> `00afae44` | `7f 1e 00 f9` | str xzr,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00afae48"></a> `00afae48` | `f5 00 00 b4` | cbz x21,0x00afae64 | `CONDITIONAL_JUMP`
<a id="insn-00afae4c"></a> `00afae4c` | `a0 a2 01 91` | add x0,x21,#0x68 | `FALL_THROUGH`
<a id="insn-00afae50"></a> `00afae50` | `e4 8c 03 94` | bl 0x00bde1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afae54"></a> `00afae54` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afae58"></a> `00afae58` | `9e 8b 03 94` | bl 0x00bddcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afae5c"></a> `00afae5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afae60"></a> `00afae60` | `40 80 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afae64"></a> `00afae64` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00afae68"></a> `00afae68` | `68 00 00 36` | tbz w8,#0x0,0x00afae74 | `CONDITIONAL_JUMP`
<a id="insn-00afae6c"></a> `00afae6c` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00afae70"></a> `00afae70` | `3c 80 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afae74"></a> `00afae74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afae78"></a> `00afae78` | `3a 80 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afae7c"></a> `00afae7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afae80"></a> `00afae80` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afae84"></a> `00afae84` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afae88"></a> `00afae88` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afae8c"></a> `00afae8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afadc0`](#insn-00afadc0) 範囲 `[['00afadc0', '00afaddb']]`
  - `CONDITIONAL_JUMP` [`00afadd8`](#insn-00afadd8) → [`00afadec`](#insn-00afadec)
  - `FALL_THROUGH` [`00afadd8`](#insn-00afadd8) → [`00afaddc`](#insn-00afaddc)
- ブロック [`00afaddc`](#insn-00afaddc) 範囲 `[['00afaddc', '00afade7']]`
  - `CONDITIONAL_JUMP` [`00afade4`](#insn-00afade4) → [`00afaddc`](#insn-00afaddc)
  - `FALL_THROUGH` [`00afade4`](#insn-00afade4) → [`00afade8`](#insn-00afade8)
- ブロック [`00afade8`](#insn-00afade8) 範囲 `[['00afade8', '00afadeb']]`
  - `UNCONDITIONAL_JUMP` [`00afade8`](#insn-00afade8) → [`00afae18`](#insn-00afae18)
- ブロック [`00afadec`](#insn-00afadec) 範囲 `[['00afadec', '00afadff']]`
  - `CONDITIONAL_JUMP` [`00afadfc`](#insn-00afadfc) → [`00afae18`](#insn-00afae18)
  - `FALL_THROUGH` [`00afadfc`](#insn-00afadfc) → [`00afae00`](#insn-00afae00)
- ブロック [`00afae00`](#insn-00afae00) 範囲 `[['00afae00', '00afae17']]`
  - `CONDITIONAL_JUMP` [`00afae14`](#insn-00afae14) → [`00afae00`](#insn-00afae00)
  - `FALL_THROUGH` [`00afae14`](#insn-00afae14) → [`00afae18`](#insn-00afae18)
- ブロック [`00afae18`](#insn-00afae18) 範囲 `[['00afae18', '00afae23']]`
  - `CONDITIONAL_JUMP` [`00afae20`](#insn-00afae20) → [`00afae28`](#insn-00afae28)
  - `FALL_THROUGH` [`00afae20`](#insn-00afae20) → [`00afae24`](#insn-00afae24)
- ブロック [`00afae24`](#insn-00afae24) 範囲 `[['00afae24', '00afae27']]`
  - `FALL_THROUGH` [`00afae24`](#insn-00afae24) → [`00afae28`](#insn-00afae28)
- ブロック [`00afae28`](#insn-00afae28) 範囲 `[['00afae28', '00afae2f']]`
  - `FALL_THROUGH` [`00afae2c`](#insn-00afae2c) → [`00afae30`](#insn-00afae30)
- ブロック [`00afae30`](#insn-00afae30) 範囲 `[['00afae30', '00afae4b']]`
  - `CONDITIONAL_JUMP` [`00afae48`](#insn-00afae48) → [`00afae64`](#insn-00afae64)
  - `FALL_THROUGH` [`00afae48`](#insn-00afae48) → [`00afae4c`](#insn-00afae4c)
- ブロック [`00afae4c`](#insn-00afae4c) 範囲 `[['00afae4c', '00afae63']]`
  - `FALL_THROUGH` [`00afae60`](#insn-00afae60) → [`00afae64`](#insn-00afae64)
- ブロック [`00afae64`](#insn-00afae64) 範囲 `[['00afae64', '00afae6b']]`
  - `CONDITIONAL_JUMP` [`00afae68`](#insn-00afae68) → [`00afae74`](#insn-00afae74)
  - `FALL_THROUGH` [`00afae68`](#insn-00afae68) → [`00afae6c`](#insn-00afae6c)
- ブロック [`00afae6c`](#insn-00afae6c) 範囲 `[['00afae6c', '00afae73']]`
  - `FALL_THROUGH` [`00afae70`](#insn-00afae70) → [`00afae74`](#insn-00afae74)
- ブロック [`00afae74`](#insn-00afae74) 範囲 `[['00afae74', '00afae8f']]`

## 命令位置別の参照

- [`00afadc0`](#insn-00afadc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadc4`](#insn-00afadc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadc8`](#insn-00afadc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadd8`](#insn-00afadd8) → [`00afadec`](#insn-00afadec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade4`](#insn-00afade4) → [`00afaddc`](#insn-00afaddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afade8`](#insn-00afade8) → [`00afae18`](#insn-00afae18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadfc`](#insn-00afadfc) → [`00afae18`](#insn-00afae18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae14`](#insn-00afae14) → [`00afae00`](#insn-00afae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae20`](#insn-00afae20) → [`00afae28`](#insn-00afae28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae3c`](#insn-00afae3c) → [`00bde650`](../00bde/00bde650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde650` · 推定シンボル `None` · 推定型 `None`
- [`00afae48`](#insn-00afae48) → [`00afae64`](#insn-00afae64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae50`](#insn-00afae50) → [`00bde1e0`](../00bde/00bde1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1e0` · 推定シンボル `None` · 推定型 `None`
- [`00afae58`](#insn-00afae58) → [`00bddcd0`](../00bdd/00bddcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddcd0` · 推定シンボル `None` · 推定型 `None`
- [`00afae60`](#insn-00afae60) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afae68`](#insn-00afae68) → [`00afae74`](#insn-00afae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae70`](#insn-00afae70) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afae78`](#insn-00afae78) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afae80`](#insn-00afae80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afae84`](#insn-00afae84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afadc0`](#insn-00afadc0)

~~~json
{
  "source": "00afadc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadc4`](#insn-00afadc4)

~~~json
{
  "source": "00afadc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadc8`](#insn-00afadc8)

~~~json
{
  "source": "00afadc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadd8`](#insn-00afadd8)

~~~json
{
  "source": "00afadd8",
  "target": "00afadec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade4`](#insn-00afade4)

~~~json
{
  "source": "00afade4",
  "target": "00afaddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afade8`](#insn-00afade8)

~~~json
{
  "source": "00afade8",
  "target": "00afae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadfc`](#insn-00afadfc)

~~~json
{
  "source": "00afadfc",
  "target": "00afae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae14`](#insn-00afae14)

~~~json
{
  "source": "00afae14",
  "target": "00afae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae20`](#insn-00afae20)

~~~json
{
  "source": "00afae20",
  "target": "00afae28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae3c`](#insn-00afae3c)

~~~json
{
  "source": "00afae3c",
  "target": "00bde650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae48`](#insn-00afae48)

~~~json
{
  "source": "00afae48",
  "target": "00afae64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae50`](#insn-00afae50)

~~~json
{
  "source": "00afae50",
  "target": "00bde1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae58`](#insn-00afae58)

~~~json
{
  "source": "00afae58",
  "target": "00bddcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae60`](#insn-00afae60)

~~~json
{
  "source": "00afae60",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae68`](#insn-00afae68)

~~~json
{
  "source": "00afae68",
  "target": "00afae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae70`](#insn-00afae70)

~~~json
{
  "source": "00afae70",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae78`](#insn-00afae78)

~~~json
{
  "source": "00afae78",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afae80`](#insn-00afae80)

~~~json
{
  "source": "00afae80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afae84`](#insn-00afae84)

~~~json
{
  "source": "00afae84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
