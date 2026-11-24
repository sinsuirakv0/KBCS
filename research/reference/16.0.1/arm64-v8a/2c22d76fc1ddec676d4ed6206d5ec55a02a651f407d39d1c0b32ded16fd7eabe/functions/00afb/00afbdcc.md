# 00afbdcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afb9a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afb/00afb9a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0036.md#compare-097d611cd1ad1aed5c8e10085cac61c4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afbe68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afb/00afbe68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0036.md#compare-8be5ae67fa3c67fc29a448b253ade023)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbdcc",
  "name": "FUN_00afbdcc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c02f2f6914ffd49f732d168f27f3c8453157e9e76e635ab765a0e3290e33730d",
  "source_text_sha256": "c02f2f6914ffd49f732d168f27f3c8453157e9e76e635ab765a0e3290e33730d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbdcc",
        "00afbe0b"
      ]
    ],
    "bytes_sha256": "bb53df902222cdd6080ac58031f13875d5840cdbbcc15b7a1419d3c236ddd41c",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)
- [00707ee0](../00707/00707ee0.md)
- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)
- [00715500](../00715/00715500.md)
- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afbdcc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbdcc"></a> `00afbdcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afbdd0"></a> `00afbdd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbdd4"></a> `00afbdd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbdd8"></a> `00afbdd8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afbddc"></a> `00afbddc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afbde0"></a> `00afbde0` | `c6 55 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afbde4"></a> `00afbde4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbde8"></a> `00afbde8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbdec"></a> `00afbdec` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbdf0"></a> `00afbdf0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbdf4"></a> `00afbdf4` | `89 3e 89 52` | mov w9,#0x49f4 | `FALL_THROUGH`
<a id="insn-00afbdf8"></a> `00afbdf8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbdfc"></a> `00afbdfc` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbe00"></a> `00afbe00` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe04"></a> `00afbe04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbe08"></a> `00afbe08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbdcc`](#insn-00afbdcc) 範囲 `[['00afbdcc', '00afbe0b']]`

## 命令位置別の参照

- [`00afbdcc`](#insn-00afbdcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbdd0`](#insn-00afbdd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbde0`](#insn-00afbde0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afbe00`](#insn-00afbe00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe04`](#insn-00afbe04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbdcc`](#insn-00afbdcc)

~~~json
{
  "source": "00afbdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbdd0`](#insn-00afbdd0)

~~~json
{
  "source": "00afbdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbde0`](#insn-00afbde0)

~~~json
{
  "source": "00afbde0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe00`](#insn-00afbe00)

~~~json
{
  "source": "00afbe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe04`](#insn-00afbe04)

~~~json
{
  "source": "00afbe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
