# 00af9dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-5c4c727bd9310717ca8fb278819b78fc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afa214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-059ae8ad589e02a828eb0f20581e4f2d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9dec",
  "name": "FUN_00af9dec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad57a7239cfd81ad34e91b4a9b1b10c1abe97c2ee91a56b83b95f91f6b0b9d39",
  "source_text_sha256": "ad57a7239cfd81ad34e91b4a9b1b10c1abe97c2ee91a56b83b95f91f6b0b9d39",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af9dec",
        "00af9e2b"
      ]
    ],
    "bytes_sha256": "ebb9fc38ef1a76b54106f9a29d538c52e7ba993f5d7c5ad73382f8a5d3baaf49",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00713ce4](../00713/00713ce4.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af9dec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af9dec"></a> `00af9dec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af9df0"></a> `00af9df0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9df4"></a> `00af9df4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af9df8"></a> `00af9df8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af9dfc"></a> `00af9dfc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af9e00"></a> `00af9e00` | `ae 5d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af9e04"></a> `00af9e04` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af9e08"></a> `00af9e08` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af9e0c"></a> `00af9e0c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9e10"></a> `00af9e10` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af9e14"></a> `00af9e14` | `09 5b 89 52` | mov w9,#0x4ad8 | `FALL_THROUGH`
<a id="insn-00af9e18"></a> `00af9e18` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af9e1c"></a> `00af9e1c` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af9e20"></a> `00af9e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9e24"></a> `00af9e24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af9e28"></a> `00af9e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af9dec`](#insn-00af9dec) 範囲 `[['00af9dec', '00af9e2b']]`

## 命令位置別の参照

- [`00af9dec`](#insn-00af9dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9df0`](#insn-00af9df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9e00`](#insn-00af9e00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af9e20`](#insn-00af9e20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9e24`](#insn-00af9e24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af9dec`](#insn-00af9dec)

~~~json
{
  "source": "00af9dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9df0`](#insn-00af9df0)

~~~json
{
  "source": "00af9df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9e00`](#insn-00af9e00)

~~~json
{
  "source": "00af9e00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9e20`](#insn-00af9e20)

~~~json
{
  "source": "00af9e20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9e24`](#insn-00af9e24)

~~~json
{
  "source": "00af9e24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
