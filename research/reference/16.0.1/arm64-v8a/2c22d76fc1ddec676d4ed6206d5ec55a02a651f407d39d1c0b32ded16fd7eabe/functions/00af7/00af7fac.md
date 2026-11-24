# 00af7fac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af7b84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7b84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0005.md#compare-25333646068d3b75b55eebb24fc8f897)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af8048`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8048.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-272a7c72308b306c96aa0540627c97a9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7fac",
  "name": "FUN_00af7fac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc",
  "source_text_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af7fac",
        "00af7ff7"
      ]
    ],
    "bytes_sha256": "8005f3510968d899530a221e183199ca5548a4701a0094677af34841123c74a6",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af7fac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af7fe0 to 00bf7feb has its CatchHandler @ 00af8554 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af0) = param_3;
                    /* try { // try from 00af7fec to 00bf802f has its CatchHandler @ 00af7de0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af7fac"></a> `00af7fac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af7fb0"></a> `00af7fb0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7fb4"></a> `00af7fb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7fb8"></a> `00af7fb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af7fbc"></a> `00af7fbc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af7fc0"></a> `00af7fc0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af7fc4"></a> `00af7fc4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af7fc8"></a> `00af7fc8` | `4c 65 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af7fcc"></a> `00af7fcc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af7fd0"></a> `00af7fd0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af7fd4"></a> `00af7fd4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af7fd8"></a> `00af7fd8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af7fdc"></a> `00af7fdc` | `09 5e 89 52` | mov w9,#0x4af0 | `FALL_THROUGH`
<a id="insn-00af7fe0"></a> `00af7fe0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af7fe4"></a> `00af7fe4` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af7fe8"></a> `00af7fe8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7fec"></a> `00af7fec` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7ff0"></a> `00af7ff0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af7ff4"></a> `00af7ff4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af7fac`](#insn-00af7fac) 範囲 `[['00af7fac', '00af7fdf']]`
  - `FALL_THROUGH` [`00af7fdc`](#insn-00af7fdc) → [`00af7fe0`](#insn-00af7fe0)
- ブロック [`00af7fe0`](#insn-00af7fe0) 範囲 `[['00af7fe0', '00af7feb']]`
  - `FALL_THROUGH` [`00af7fe8`](#insn-00af7fe8) → [`00af7fec`](#insn-00af7fec)
- ブロック [`00af7fec`](#insn-00af7fec) 範囲 `[['00af7fec', '00af7ff7']]`

## 命令位置別の参照

- [`00af7fac`](#insn-00af7fac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fb0`](#insn-00af7fb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fb4`](#insn-00af7fb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fc8`](#insn-00af7fc8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af7fe8`](#insn-00af7fe8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fec`](#insn-00af7fec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ff0`](#insn-00af7ff0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af7fac`](#insn-00af7fac)

~~~json
{
  "source": "00af7fac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fb0`](#insn-00af7fb0)

~~~json
{
  "source": "00af7fb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fb4`](#insn-00af7fb4)

~~~json
{
  "source": "00af7fb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fc8`](#insn-00af7fc8)

~~~json
{
  "source": "00af7fc8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7fe8`](#insn-00af7fe8)

~~~json
{
  "source": "00af7fe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fec`](#insn-00af7fec)

~~~json
{
  "source": "00af7fec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ff0`](#insn-00af7ff0)

~~~json
{
  "source": "00af7ff0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
