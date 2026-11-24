# 00afcdd0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afbddc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afb/00afbddc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-da5e0c3c5dd6d52df822831c112f207a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcdd0",
  "name": "FUN_00afcdd0",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f734448c81657e26fd555bde7bfd45ee647d601d28c76d7cb8dcd9de8c939758",
  "source_text_sha256": "f734448c81657e26fd555bde7bfd45ee647d601d28c76d7cb8dcd9de8c939758",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcdd0",
        "00afce0f"
      ]
    ],
    "bytes_sha256": "b76333015fe97e7ddb599131be19b3a1817a5e9391148b252855e7f50132834a",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afcdd0(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c3c);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcdd0"></a> `00afcdd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcdd4"></a> `00afcdd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcdd8"></a> `00afcdd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcddc"></a> `00afcddc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcde0"></a> `00afcde0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afcde4"></a> `00afcde4` | `c6 55 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afcde8"></a> `00afcde8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcdec"></a> `00afcdec` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcdf0"></a> `00afcdf0` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcdf4"></a> `00afcdf4` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcdf8"></a> `00afcdf8` | `89 87 89 52` | mov w9,#0x4c3c | `FALL_THROUGH`
<a id="insn-00afcdfc"></a> `00afcdfc` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afce00"></a> `00afce00` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afce04"></a> `00afce04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afce08"></a> `00afce08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afce0c"></a> `00afce0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcdd0`](#insn-00afcdd0) 範囲 `[['00afcdd0', '00afce0f']]`

## 命令位置別の参照

- [`00afcdd0`](#insn-00afcdd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcdd4`](#insn-00afcdd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcde4`](#insn-00afcde4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afce04`](#insn-00afce04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afce08`](#insn-00afce08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcdd0`](#insn-00afcdd0)

~~~json
{
  "source": "00afcdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcdd4`](#insn-00afcdd4)

~~~json
{
  "source": "00afcdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcde4`](#insn-00afcde4)

~~~json
{
  "source": "00afcde4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afce04`](#insn-00afce04)

~~~json
{
  "source": "00afce04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afce08`](#insn-00afce08)

~~~json
{
  "source": "00afce08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
