# 00acadb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6ce24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ce24.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-f392ad5898313ebe15c7da7f74882abe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acafb4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acafb4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-8d79d6265dfbc2f5316e401da744dc0d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acadb8",
  "name": "FUN_00acadb8",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a60f5170e9dac47a6eb0cc814bc769e66b0fb1b5a816db1ef0bad79e88c8b99",
  "source_text_sha256": "4a60f5170e9dac47a6eb0cc814bc769e66b0fb1b5a816db1ef0bad79e88c8b99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acadb8",
        "00acadfb"
      ]
    ],
    "bytes_sha256": "98f24e49e2e7056539dfea142dd5e11084c0a6e5510f6d214d1dd8f3b72520fb",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00788c6c](../00788/00788c6c.md)
- [0082ede0](../0082e/0082ede0.md)
- [008fe848](../008fe/008fe848.md)
- [00a3dc60](../00a3d/00a3dc60.md)
- [00ac0258](../00ac0/00ac0258.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00acadb8(long param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_2 & 1) == 0) {
    *(undefined4 *)(param_1 + 0x9c) = 2;
    FUN_008514b8();
    uVar1 = 0xe;
  }
  else {
    uVar1 = 0;
    *(undefined4 *)(param_1 + 0x9c) = 3;
  }
  *(undefined4 *)(param_1 + 0x98) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acadb8"></a> `00acadb8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acadbc"></a> `00acadbc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acadc0"></a> `00acadc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acadc4"></a> `00acadc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acadc8"></a> `00acadc8` | `a1 00 00 36` | tbz w1,#0x0,0x00acaddc | `CONDITIONAL_JUMP`
<a id="insn-00acadcc"></a> `00acadcc` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00acadd0"></a> `00acadd0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acadd4"></a> `00acadd4` | `69 9e 00 b9` | str w9,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00acadd8"></a> `00acadd8` | `05 00 00 14` | b 0x00acadec | `UNCONDITIONAL_JUMP`
<a id="insn-00acaddc"></a> `00acaddc` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acade0"></a> `00acade0` | `68 9e 00 b9` | str w8,[x19, #0x9c] | `FALL_THROUGH`
<a id="insn-00acade4"></a> `00acade4` | `b5 19 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acade8"></a> `00acade8` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00acadec"></a> `00acadec` | `68 9a 00 b9` | str w8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00acadf0"></a> `00acadf0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acadf4"></a> `00acadf4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acadf8"></a> `00acadf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acadb8`](#insn-00acadb8) 範囲 `[['00acadb8', '00acadcb']]`
  - `CONDITIONAL_JUMP` [`00acadc8`](#insn-00acadc8) → [`00acaddc`](#insn-00acaddc)
  - `FALL_THROUGH` [`00acadc8`](#insn-00acadc8) → [`00acadcc`](#insn-00acadcc)
- ブロック [`00acadcc`](#insn-00acadcc) 範囲 `[['00acadcc', '00acaddb']]`
  - `UNCONDITIONAL_JUMP` [`00acadd8`](#insn-00acadd8) → [`00acadec`](#insn-00acadec)
- ブロック [`00acaddc`](#insn-00acaddc) 範囲 `[['00acaddc', '00acadeb']]`
  - `FALL_THROUGH` [`00acade8`](#insn-00acade8) → [`00acadec`](#insn-00acadec)
- ブロック [`00acadec`](#insn-00acadec) 範囲 `[['00acadec', '00acadfb']]`

## 命令位置別の参照

- [`00acadb8`](#insn-00acadb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadbc`](#insn-00acadbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadc8`](#insn-00acadc8) → [`00acaddc`](#insn-00acaddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadd8`](#insn-00acadd8) → [`00acadec`](#insn-00acadec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acade4`](#insn-00acade4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00acadf0`](#insn-00acadf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acadf4`](#insn-00acadf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acadb8`](#insn-00acadb8)

~~~json
{
  "source": "00acadb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadbc`](#insn-00acadbc)

~~~json
{
  "source": "00acadbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadc8`](#insn-00acadc8)

~~~json
{
  "source": "00acadc8",
  "target": "00acaddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadd8`](#insn-00acadd8)

~~~json
{
  "source": "00acadd8",
  "target": "00acadec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acade4`](#insn-00acade4)

~~~json
{
  "source": "00acade4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acadf0`](#insn-00acadf0)

~~~json
{
  "source": "00acadf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acadf4`](#insn-00acadf4)

~~~json
{
  "source": "00acadf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
