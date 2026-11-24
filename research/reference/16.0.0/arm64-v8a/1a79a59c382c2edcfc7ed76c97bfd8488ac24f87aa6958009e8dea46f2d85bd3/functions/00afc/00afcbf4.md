# 00afcbf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-2790d2d6514e2223e981a7c2e23dae8b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afd01c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd01c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-7b53e914e35123b6c2d08840ceeff901)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcbf4",
  "name": "FUN_00afcbf4",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "795eb84a7076584132d1af7587022c02060dce2d24acf856d33560d0b1748118",
  "source_text_sha256": "795eb84a7076584132d1af7587022c02060dce2d24acf856d33560d0b1748118",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcbf4",
        "00afcca7"
      ]
    ],
    "bytes_sha256": "f18d6f8dbddd7375168f0697493f562d684eaeedfc6a6cf1b732ffa881ff53b7",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00afcbf4(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c) = iVar3 + param_3;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcbf4"></a> `00afcbf4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afcbf8"></a> `00afcbf8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcbfc"></a> `00afcbfc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcc00"></a> `00afcc00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcc04"></a> `00afcc04` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afcc08"></a> `00afcc08` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcc0c"></a> `00afcc0c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afcc10"></a> `00afcc10` | `2a 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc14"></a> `00afcc14` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcc18"></a> `00afcc18` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcc1c"></a> `00afcc1c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcc20"></a> `00afcc20` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afcc24"></a> `00afcc24` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcc28"></a> `00afcc28` | `ee a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc2c"></a> `00afcc2c` | `40 01 00 37` | tbnz w0,#0x0,0x00afcc54 | `CONDITIONAL_JUMP`
<a id="insn-00afcc30"></a> `00afcc30` | `22 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc34"></a> `00afcc34` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcc38"></a> `00afcc38` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcc3c"></a> `00afcc3c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcc40"></a> `00afcc40` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcc44"></a> `00afcc44` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afcc48"></a> `00afcc48` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcc4c"></a> `00afcc4c` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcc50"></a> `00afcc50` | `02 00 00 14` | b 0x00afcc58 | `UNCONDITIONAL_JUMP`
<a id="insn-00afcc54"></a> `00afcc54` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00afcc58"></a> `00afcc58` | `18 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc5c"></a> `00afcc5c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afcc60"></a> `00afcc60` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afcc64"></a> `00afcc64` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcc68"></a> `00afcc68` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afcc6c"></a> `00afcc6c` | `dd a9 eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc70"></a> `00afcc70` | `40 01 00 37` | tbnz w0,#0x0,0x00afcc98 | `CONDITIONAL_JUMP`
<a id="insn-00afcc74"></a> `00afcc74` | `d4 02 14 0b` | add w20,w22,w20 | `FALL_THROUGH`
<a id="insn-00afcc78"></a> `00afcc78` | `10 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afcc7c"></a> `00afcc7c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcc80"></a> `00afcc80` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcc84"></a> `00afcc84` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcc88"></a> `00afcc88` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcc8c"></a> `00afcc8c` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afcc90"></a> `00afcc90` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcc94"></a> `00afcc94` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcc98"></a> `00afcc98` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afcc9c"></a> `00afcc9c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcca0"></a> `00afcca0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afcca4"></a> `00afcca4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcbf4`](#insn-00afcbf4) 範囲 `[['00afcbf4', '00afcc2f']]`
  - `CONDITIONAL_JUMP` [`00afcc2c`](#insn-00afcc2c) → [`00afcc54`](#insn-00afcc54)
  - `FALL_THROUGH` [`00afcc2c`](#insn-00afcc2c) → [`00afcc30`](#insn-00afcc30)
- ブロック [`00afcc30`](#insn-00afcc30) 範囲 `[['00afcc30', '00afcc53']]`
  - `UNCONDITIONAL_JUMP` [`00afcc50`](#insn-00afcc50) → [`00afcc58`](#insn-00afcc58)
- ブロック [`00afcc54`](#insn-00afcc54) 範囲 `[['00afcc54', '00afcc57']]`
  - `FALL_THROUGH` [`00afcc54`](#insn-00afcc54) → [`00afcc58`](#insn-00afcc58)
- ブロック [`00afcc58`](#insn-00afcc58) 範囲 `[['00afcc58', '00afcc73']]`
  - `CONDITIONAL_JUMP` [`00afcc70`](#insn-00afcc70) → [`00afcc98`](#insn-00afcc98)
  - `FALL_THROUGH` [`00afcc70`](#insn-00afcc70) → [`00afcc74`](#insn-00afcc74)
- ブロック [`00afcc74`](#insn-00afcc74) 範囲 `[['00afcc74', '00afcc97']]`
  - `FALL_THROUGH` [`00afcc94`](#insn-00afcc94) → [`00afcc98`](#insn-00afcc98)
- ブロック [`00afcc98`](#insn-00afcc98) 範囲 `[['00afcc98', '00afcca7']]`

## 命令位置別の参照

- [`00afcbf4`](#insn-00afcbf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbf8`](#insn-00afcbf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcbfc`](#insn-00afcbfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc10`](#insn-00afcc10) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcc28`](#insn-00afcc28) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afcc2c`](#insn-00afcc2c) → [`00afcc54`](#insn-00afcc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc30`](#insn-00afcc30) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcc50`](#insn-00afcc50) → [`00afcc58`](#insn-00afcc58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc58`](#insn-00afcc58) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcc6c`](#insn-00afcc6c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00afcc70`](#insn-00afcc70) → [`00afcc98`](#insn-00afcc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc78`](#insn-00afcc78) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afcc98`](#insn-00afcc98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcc9c`](#insn-00afcc9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcca0`](#insn-00afcca0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcbf4`](#insn-00afcbf4)

~~~json
{
  "source": "00afcbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbf8`](#insn-00afcbf8)

~~~json
{
  "source": "00afcbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcbfc`](#insn-00afcbfc)

~~~json
{
  "source": "00afcbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc10`](#insn-00afcc10)

~~~json
{
  "source": "00afcc10",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc28`](#insn-00afcc28)

~~~json
{
  "source": "00afcc28",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc2c`](#insn-00afcc2c)

~~~json
{
  "source": "00afcc2c",
  "target": "00afcc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc30`](#insn-00afcc30)

~~~json
{
  "source": "00afcc30",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc50`](#insn-00afcc50)

~~~json
{
  "source": "00afcc50",
  "target": "00afcc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc58`](#insn-00afcc58)

~~~json
{
  "source": "00afcc58",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc6c`](#insn-00afcc6c)

~~~json
{
  "source": "00afcc6c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc70`](#insn-00afcc70)

~~~json
{
  "source": "00afcc70",
  "target": "00afcc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc78`](#insn-00afcc78)

~~~json
{
  "source": "00afcc78",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcc98`](#insn-00afcc98)

~~~json
{
  "source": "00afcc98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcc9c`](#insn-00afcc9c)

~~~json
{
  "source": "00afcc9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcca0`](#insn-00afcca0)

~~~json
{
  "source": "00afcca0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
