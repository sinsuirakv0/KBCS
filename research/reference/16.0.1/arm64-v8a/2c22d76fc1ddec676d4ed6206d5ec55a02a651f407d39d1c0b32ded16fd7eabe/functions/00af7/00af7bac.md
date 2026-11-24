# 00af7bac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af7784`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7784.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0005.md#compare-b8c68eefbd1780c4d9ac3979be054255)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af7c48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af7/00af7c48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-08b6f0cf0e65616f8d65b44727747ca7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7bac",
  "name": "FUN_00af7bac",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45f699ed85237997805ef40c4a926ce8e530f4e391fd4dabdf402a23c79f8daa",
  "source_text_sha256": "45f699ed85237997805ef40c4a926ce8e530f4e391fd4dabdf402a23c79f8daa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af7bac",
        "00af7c0b"
      ]
    ],
    "bytes_sha256": "1a9b9bb7660ef6b925ef047b6243ed415c8a61ce6fe06b7c02c9687344434043",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
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

## 疑似コード / UTF-8 278 bytes

~~~c

void FUN_00af7bac(int param_1,int param_2,int param_3,undefined4 param_4)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)
   (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + (long)(int)(&DAT_0030a398)[param_3] * 4
   + 0x848c8) = param_4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af7bac"></a> `00af7bac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af7bb0"></a> `00af7bb0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7bb4"></a> `00af7bb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7bb8"></a> `00af7bb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af7bbc"></a> `00af7bbc` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00af7bc0"></a> `00af7bc0` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00af7bc4"></a> `00af7bc4` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00af7bc8"></a> `00af7bc8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00af7bcc"></a> `00af7bcc` | `4b 66 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af7bd0"></a> `00af7bd0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af7bd4"></a> `00af7bd4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af7bd8"></a> `00af7bd8` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00af7bdc"></a> `00af7bdc` | `a8 22 29 9b` | smaddl x8,w21,w9,x8 | `FALL_THROUGH`
<a id="insn-00af7be0"></a> `00af7be0` | `89 c0 ff f0` | adrp x9,0x30a000 | `FALL_THROUGH`
<a id="insn-00af7be4"></a> `00af7be4` | `29 61 0e 91` | add x9,x9,#0x398 | `FALL_THROUGH`
<a id="insn-00af7be8"></a> `00af7be8` | `29 d9 b4 b8` | ldrsw x9,[x9, w20, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00af7bec"></a> `00af7bec` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00af7bf0"></a> `00af7bf0` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af7bf4"></a> `00af7bf4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af7bf8"></a> `00af7bf8` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af7bfc"></a> `00af7bfc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7c00"></a> `00af7c00` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7c04"></a> `00af7c04` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af7c08"></a> `00af7c08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af7bac`](#insn-00af7bac) 範囲 `[['00af7bac', '00af7c0b']]`

## 命令位置別の参照

- [`00af7bac`](#insn-00af7bac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7bb0`](#insn-00af7bb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7bb4`](#insn-00af7bb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7bcc`](#insn-00af7bcc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af7be8`](#insn-00af7be8) → `0030a398`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00af7bfc`](#insn-00af7bfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7c00`](#insn-00af7c00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7c04`](#insn-00af7c04) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af7bac`](#insn-00af7bac)

~~~json
{
  "source": "00af7bac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7bb0`](#insn-00af7bb0)

~~~json
{
  "source": "00af7bb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7bb4`](#insn-00af7bb4)

~~~json
{
  "source": "00af7bb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7bcc`](#insn-00af7bcc)

~~~json
{
  "source": "00af7bcc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7be8`](#insn-00af7be8)

~~~json
{
  "source": "00af7be8",
  "target": "0030a398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030a398",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "bytes": "54000000",
  "capture_start": "0030a398",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00af7bfc`](#insn-00af7bfc)

~~~json
{
  "source": "00af7bfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7c00`](#insn-00af7c00)

~~~json
{
  "source": "00af7c00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7c04`](#insn-00af7c04)

~~~json
{
  "source": "00af7c04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
