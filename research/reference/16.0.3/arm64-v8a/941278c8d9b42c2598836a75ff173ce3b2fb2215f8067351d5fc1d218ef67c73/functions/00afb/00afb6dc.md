# 00afb6dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afa6e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa6e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-25be770e6c4ba569cc309af19d06af97)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb6dc",
  "name": "FUN_00afb6dc",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fb167a795ade8fc4dd55c5233f7c30b6907f99e8dbec20249240b697e7a2c95",
  "source_text_sha256": "3fb167a795ade8fc4dd55c5233f7c30b6907f99e8dbec20249240b697e7a2c95",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb6dc",
        "00afb743"
      ]
    ],
    "bytes_sha256": "2c3a62016af2bd8a16af19fa420cd352f14eaca6bff744865bdbb579c2ed3468",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00711df8](../00711/00711df8.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 492 bytes

~~~c

undefined4 FUN_00afb6dc(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00afb6dc to 00bfb7bb has its CatchHandler @ 00afaee0 */
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_008524fc();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c0c);
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb6dc"></a> `00afb6dc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afb6e0"></a> `00afb6e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb6e4"></a> `00afb6e4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb6e8"></a> `00afb6e8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afb6ec"></a> `00afb6ec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afb6f0"></a> `00afb6f0` | `83 5b f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb6f4"></a> `00afb6f4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afb6f8"></a> `00afb6f8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afb6fc"></a> `00afb6fc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb700"></a> `00afb700` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afb704"></a> `00afb704` | `43 b0 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afb708"></a> `00afb708` | `60 00 00 37` | tbnz w0,#0x0,0x00afb714 | `CONDITIONAL_JUMP`
<a id="insn-00afb70c"></a> `00afb70c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afb710"></a> `00afb710` | `0a 00 00 14` | b 0x00afb738 | `UNCONDITIONAL_JUMP`
<a id="insn-00afb714"></a> `00afb714` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afb718"></a> `00afb718` | `79 5b f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb71c"></a> `00afb71c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb720"></a> `00afb720` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb724"></a> `00afb724` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb728"></a> `00afb728` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb72c"></a> `00afb72c` | `89 81 89 52` | mov w9,#0x4c0c | `FALL_THROUGH`
<a id="insn-00afb730"></a> `00afb730` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb734"></a> `00afb734` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb738"></a> `00afb738` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb73c"></a> `00afb73c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afb740"></a> `00afb740` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb6dc`](#insn-00afb6dc) 範囲 `[['00afb6dc', '00afb70b']]`
  - `CONDITIONAL_JUMP` [`00afb708`](#insn-00afb708) → [`00afb714`](#insn-00afb714)
  - `FALL_THROUGH` [`00afb708`](#insn-00afb708) → [`00afb70c`](#insn-00afb70c)
- ブロック [`00afb70c`](#insn-00afb70c) 範囲 `[['00afb70c', '00afb713']]`
  - `UNCONDITIONAL_JUMP` [`00afb710`](#insn-00afb710) → [`00afb738`](#insn-00afb738)
- ブロック [`00afb714`](#insn-00afb714) 範囲 `[['00afb714', '00afb737']]`
  - `FALL_THROUGH` [`00afb734`](#insn-00afb734) → [`00afb738`](#insn-00afb738)
- ブロック [`00afb738`](#insn-00afb738) 範囲 `[['00afb738', '00afb743']]`

## 命令位置別の参照

- [`00afb6dc`](#insn-00afb6dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6e0`](#insn-00afb6e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6f0`](#insn-00afb6f0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb704`](#insn-00afb704) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afb708`](#insn-00afb708) → [`00afb714`](#insn-00afb714) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb710`](#insn-00afb710) → [`00afb738`](#insn-00afb738) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb718`](#insn-00afb718) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb738`](#insn-00afb738) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb73c`](#insn-00afb73c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb6dc`](#insn-00afb6dc)

~~~json
{
  "source": "00afb6dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6e0`](#insn-00afb6e0)

~~~json
{
  "source": "00afb6e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6f0`](#insn-00afb6f0)

~~~json
{
  "source": "00afb6f0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb704`](#insn-00afb704)

~~~json
{
  "source": "00afb704",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb708`](#insn-00afb708)

~~~json
{
  "source": "00afb708",
  "target": "00afb714",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb710`](#insn-00afb710)

~~~json
{
  "source": "00afb710",
  "target": "00afb738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb718`](#insn-00afb718)

~~~json
{
  "source": "00afb718",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb738`](#insn-00afb738)

~~~json
{
  "source": "00afb738",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb73c`](#insn-00afb73c)

~~~json
{
  "source": "00afb73c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
