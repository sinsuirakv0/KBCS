# 00afacfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9d08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9d08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-623c215593a25e71ef96bbe1420c446d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afacfc",
  "name": "FUN_00afacfc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea17b44cb1ddd2d1712ab153a740655ee88bfd1f8135a585c567974cf12edf84",
  "source_text_sha256": "ea17b44cb1ddd2d1712ab153a740655ee88bfd1f8135a585c567974cf12edf84",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afacfc",
        "00afad6b"
      ]
    ],
    "bytes_sha256": "66f402aadbc42bf505cc7ae87f05fc95df2092164cfcc2de3030ba41db8df64a",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 697 bytes

~~~c

void FUN_00afacfc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
                    /* try { // try from 00afad10 to 00bfadab has its CatchHandler @ 00afad10
                       catch() { ... } // from try @ 00afad10 with catch @ 00afad10
                       catch() { ... } // from try @ 00afadb0 with catch @ 00afad10
                       catch() { ... } // from try @ 00afae44 with catch @ 00afad10 */
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) = param_3 & 1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afacfc"></a> `00afacfc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afad00"></a> `00afad00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad04"></a> `00afad04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad08"></a> `00afad08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afad0c"></a> `00afad0c` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afad10"></a> `00afad10` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afad14"></a> `00afad14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afad18"></a> `00afad18` | `f9 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afad1c"></a> `00afad1c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afad20"></a> `00afad20` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afad24"></a> `00afad24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afad28"></a> `00afad28` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afad2c"></a> `00afad2c` | `b9 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afad30"></a> `00afad30` | `60 01 00 36` | tbz w0,#0x0,0x00afad5c | `CONDITIONAL_JUMP`
<a id="insn-00afad34"></a> `00afad34` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afad38"></a> `00afad38` | `94 02 00 12` | and w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afad3c"></a> `00afad3c` | `f0 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afad40"></a> `00afad40` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afad44"></a> `00afad44` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afad48"></a> `00afad48` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afad4c"></a> `00afad4c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afad50"></a> `00afad50` | `09 4f 89 52` | mov w9,#0x4a78 | `FALL_THROUGH`
<a id="insn-00afad54"></a> `00afad54` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afad58"></a> `00afad58` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afad5c"></a> `00afad5c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad60"></a> `00afad60` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad64"></a> `00afad64` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afad68"></a> `00afad68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afacfc`](#insn-00afacfc) 範囲 `[['00afacfc', '00afad0f']]`
  - `FALL_THROUGH` [`00afad0c`](#insn-00afad0c) → [`00afad10`](#insn-00afad10)
- ブロック [`00afad10`](#insn-00afad10) 範囲 `[['00afad10', '00afad33']]`
  - `CONDITIONAL_JUMP` [`00afad30`](#insn-00afad30) → [`00afad5c`](#insn-00afad5c)
  - `FALL_THROUGH` [`00afad30`](#insn-00afad30) → [`00afad34`](#insn-00afad34)
- ブロック [`00afad34`](#insn-00afad34) 範囲 `[['00afad34', '00afad5b']]`
  - `FALL_THROUGH` [`00afad58`](#insn-00afad58) → [`00afad5c`](#insn-00afad5c)
- ブロック [`00afad5c`](#insn-00afad5c) 範囲 `[['00afad5c', '00afad6b']]`

## 命令位置別の参照

- [`00afacfc`](#insn-00afacfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad00`](#insn-00afad00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad04`](#insn-00afad04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad18`](#insn-00afad18) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afad2c`](#insn-00afad2c) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afad30`](#insn-00afad30) → [`00afad5c`](#insn-00afad5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad3c`](#insn-00afad3c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afad5c`](#insn-00afad5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad60`](#insn-00afad60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad64`](#insn-00afad64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afacfc`](#insn-00afacfc)

~~~json
{
  "source": "00afacfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad00`](#insn-00afad00)

~~~json
{
  "source": "00afad00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad04`](#insn-00afad04)

~~~json
{
  "source": "00afad04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad18`](#insn-00afad18)

~~~json
{
  "source": "00afad18",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad2c`](#insn-00afad2c)

~~~json
{
  "source": "00afad2c",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad30`](#insn-00afad30)

~~~json
{
  "source": "00afad30",
  "target": "00afad5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad3c`](#insn-00afad3c)

~~~json
{
  "source": "00afad3c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad5c`](#insn-00afad5c)

~~~json
{
  "source": "00afad5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad60`](#insn-00afad60)

~~~json
{
  "source": "00afad60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad64`](#insn-00afad64)

~~~json
{
  "source": "00afad64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
