# 00afefd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-f3b9635da3aca1d9a636c3ee51d40b8a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aff3f8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff3f8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-d09798b51e6cabf4ee0ce4f77e36a3fa)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afefd0",
  "name": "FUN_00afefd0",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55148de7593f17e4f7311190106895ede1a14b8a290f5c1dabe1e5ed9fdfc6e4",
  "source_text_sha256": "55148de7593f17e4f7311190106895ede1a14b8a290f5c1dabe1e5ed9fdfc6e4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afefd0",
        "00aff077"
      ]
    ],
    "bytes_sha256": "b218579304918285736371b5b1984067aa3f90c24e83a47964d6a0aba6feab03",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00afe6c0](../00afe/00afe6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 560 bytes

~~~c

int FUN_00afefd0(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_008514b8();
  uVar4 = FUN_005e73e0(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_008514b8();
  if ((uVar4 & 1) == 0) {
    iVar2 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x17fc);
  }
  else {
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6d4);
    iVar2 = FUN_00afe6c0(param_1,param_2,param_3,0x1c,0);
    iVar2 = iVar2 + iVar1;
  }
  return iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afefd0"></a> `00afefd0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afefd4"></a> `00afefd4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afefd8"></a> `00afefd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afefdc"></a> `00afefdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afefe0"></a> `00afefe0` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afefe4"></a> `00afefe4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afefe8"></a> `00afefe8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afefec"></a> `00afefec` | `33 49 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeff0"></a> `00afeff0` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afeff4"></a> `00afeff4` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afeff8"></a> `00afeff8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afeffc"></a> `00afeffc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aff000"></a> `00aff000` | `f8 a0 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff004"></a> `00aff004` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aff008"></a> `00aff008` | `2c 49 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff00c"></a> `00aff00c` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00aff010"></a> `00aff010` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aff014"></a> `00aff014` | `f6 00 00 37` | tbnz w22,#0x0,0x00aff030 | `CONDITIONAL_JUMP`
<a id="insn-00aff018"></a> `00aff018` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00aff01c"></a> `00aff01c` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aff020"></a> `00aff020` | `89 52 9a 52` | mov w9,#0xd294 | `FALL_THROUGH`
<a id="insn-00aff024"></a> `00aff024` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00aff028"></a> `00aff028` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aff02c"></a> `00aff02c` | `0f 00 00 14` | b 0x00aff068 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff030"></a> `00aff030` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00aff034"></a> `00aff034` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aff038"></a> `00aff038` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aff03c"></a> `00aff03c` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00aff040"></a> `00aff040` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aff044"></a> `00aff044` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00aff048"></a> `00aff048` | `83 03 80 52` | mov w3,#0x1c | `FALL_THROUGH`
<a id="insn-00aff04c"></a> `00aff04c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aff050"></a> `00aff050` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aff054"></a> `00aff054` | `89 da 9e 52` | mov w9,#0xf6d4 | `FALL_THROUGH`
<a id="insn-00aff058"></a> `00aff058` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aff05c"></a> `00aff05c` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aff060"></a> `00aff060` | `98 fd ff 97` | bl 0x00afe6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00aff064"></a> `00aff064` | `00 00 16 0b` | add w0,w0,w22 | `FALL_THROUGH`
<a id="insn-00aff068"></a> `00aff068` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aff06c"></a> `00aff06c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aff070"></a> `00aff070` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aff074"></a> `00aff074` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afefd0`](#insn-00afefd0) 範囲 `[['00afefd0', '00aff017']]`
  - `CONDITIONAL_JUMP` [`00aff014`](#insn-00aff014) → [`00aff030`](#insn-00aff030)
  - `FALL_THROUGH` [`00aff014`](#insn-00aff014) → [`00aff018`](#insn-00aff018)
- ブロック [`00aff018`](#insn-00aff018) 範囲 `[['00aff018', '00aff02f']]`
  - `UNCONDITIONAL_JUMP` [`00aff02c`](#insn-00aff02c) → [`00aff068`](#insn-00aff068)
- ブロック [`00aff030`](#insn-00aff030) 範囲 `[['00aff030', '00aff067']]`
  - `FALL_THROUGH` [`00aff064`](#insn-00aff064) → [`00aff068`](#insn-00aff068)
- ブロック [`00aff068`](#insn-00aff068) 範囲 `[['00aff068', '00aff077']]`

## 命令位置別の参照

- [`00afefd0`](#insn-00afefd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefd4`](#insn-00afefd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefd8`](#insn-00afefd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefec`](#insn-00afefec) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aff000`](#insn-00aff000) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00aff008`](#insn-00aff008) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aff014`](#insn-00aff014) → [`00aff030`](#insn-00aff030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff028`](#insn-00aff028) → `0023d294`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff02c`](#insn-00aff02c) → [`00aff068`](#insn-00aff068) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff060`](#insn-00aff060) → [`00afe6c0`](00afe6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afe6c0` · 推定シンボル `None` · 推定型 `None`
- [`00aff068`](#insn-00aff068) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff06c`](#insn-00aff06c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff070`](#insn-00aff070) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afefd0`](#insn-00afefd0)

~~~json
{
  "source": "00afefd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefd4`](#insn-00afefd4)

~~~json
{
  "source": "00afefd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefd8`](#insn-00afefd8)

~~~json
{
  "source": "00afefd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefec`](#insn-00afefec)

~~~json
{
  "source": "00afefec",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff000`](#insn-00aff000)

~~~json
{
  "source": "00aff000",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff008`](#insn-00aff008)

~~~json
{
  "source": "00aff008",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff014`](#insn-00aff014)

~~~json
{
  "source": "00aff014",
  "target": "00aff030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff028`](#insn-00aff028)

~~~json
{
  "source": "00aff028",
  "target": "0023d294",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6140,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff02c`](#insn-00aff02c)

~~~json
{
  "source": "00aff02c",
  "target": "00aff068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff060`](#insn-00aff060)

~~~json
{
  "source": "00aff060",
  "target": "00afe6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff068`](#insn-00aff068)

~~~json
{
  "source": "00aff068",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff06c`](#insn-00aff06c)

~~~json
{
  "source": "00aff06c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff070`](#insn-00aff070)

~~~json
{
  "source": "00aff070",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
