# 00afb0ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afa0f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa0f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-1ece5e5eae7ff7e668daa3cb9f0a5858)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb0ec",
  "name": "FUN_00afb0ec",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20cbb5288e72b57972e76ce5b7596d73d4a6882171f09bde1446b4ae6bce53d8",
  "source_text_sha256": "20cbb5288e72b57972e76ce5b7596d73d4a6882171f09bde1446b4ae6bce53d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb0ec",
        "00afb17b"
      ]
    ],
    "bytes_sha256": "7132f935fc2aaefc929a9411ee76b62e4ef3e0a97919e0e54ec55987a37cad59",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
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

## 疑似コード / UTF-8 694 bytes

~~~c

void FUN_00afb0ec(int param_1,int param_2,undefined4 param_3,undefined4 param_4)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afb138 to 00bfb15b has its CatchHandler @ 00afb9d0 */
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c5c) = param_3;
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afb164 to 00bfb16b has its CatchHandler @ 00afbab0 */
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60) = param_4;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb0ec"></a> `00afb0ec` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afb0f0"></a> `00afb0f0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb0f4"></a> `00afb0f4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb0f8"></a> `00afb0f8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afb0fc"></a> `00afb0fc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb100"></a> `00afb100` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00afb104"></a> `00afb104` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00afb108"></a> `00afb108` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afb10c"></a> `00afb10c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00afb110"></a> `00afb110` | `fb 5c f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb114"></a> `00afb114` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afb118"></a> `00afb118` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afb11c"></a> `00afb11c` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb120"></a> `00afb120` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afb124"></a> `00afb124` | `bb b1 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afb128"></a> `00afb128` | `00 02 00 36` | tbz w0,#0x0,0x00afb168 | `CONDITIONAL_JUMP`
<a id="insn-00afb12c"></a> `00afb12c` | `d6 7e 40 93` | sxtw x22,w22 | `FALL_THROUGH`
<a id="insn-00afb130"></a> `00afb130` | `f3 5c f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb134"></a> `00afb134` | `97 00 99 52` | mov w23,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb138"></a> `00afb138` | `98 7d 80 52` | mov w24,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb13c"></a> `00afb13c` | `89 8b 89 52` | mov w9,#0x4c5c | `FALL_THROUGH`
<a id="insn-00afb140"></a> `00afb140` | `c8 02 37 9b` | smaddl x8,w22,w23,x0 | `FALL_THROUGH`
<a id="insn-00afb144"></a> `00afb144` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb148"></a> `00afb148` | `88 22 38 9b` | smaddl x8,w20,w24,x8 | `FALL_THROUGH`
<a id="insn-00afb14c"></a> `00afb14c` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb150"></a> `00afb150` | `eb 5c f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afb154"></a> `00afb154` | `c8 02 37 9b` | smaddl x8,w22,w23,x0 | `FALL_THROUGH`
<a id="insn-00afb158"></a> `00afb158` | `09 8c 89 52` | mov w9,#0x4c60 | `FALL_THROUGH`
<a id="insn-00afb15c"></a> `00afb15c` | `88 22 38 9b` | smaddl x8,w20,w24,x8 | `FALL_THROUGH`
<a id="insn-00afb160"></a> `00afb160` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb164"></a> `00afb164` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb168"></a> `00afb168` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afb16c"></a> `00afb16c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb170"></a> `00afb170` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb174"></a> `00afb174` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afb178"></a> `00afb178` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb0ec`](#insn-00afb0ec) 範囲 `[['00afb0ec', '00afb12b']]`
  - `CONDITIONAL_JUMP` [`00afb128`](#insn-00afb128) → [`00afb168`](#insn-00afb168)
  - `FALL_THROUGH` [`00afb128`](#insn-00afb128) → [`00afb12c`](#insn-00afb12c)
- ブロック [`00afb12c`](#insn-00afb12c) 範囲 `[['00afb12c', '00afb137']]`
  - `FALL_THROUGH` [`00afb134`](#insn-00afb134) → [`00afb138`](#insn-00afb138)
- ブロック [`00afb138`](#insn-00afb138) 範囲 `[['00afb138', '00afb163']]`
  - `FALL_THROUGH` [`00afb160`](#insn-00afb160) → [`00afb164`](#insn-00afb164)
- ブロック [`00afb164`](#insn-00afb164) 範囲 `[['00afb164', '00afb167']]`
  - `FALL_THROUGH` [`00afb164`](#insn-00afb164) → [`00afb168`](#insn-00afb168)
- ブロック [`00afb168`](#insn-00afb168) 範囲 `[['00afb168', '00afb17b']]`

## 命令位置別の参照

- [`00afb0ec`](#insn-00afb0ec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb0f0`](#insn-00afb0f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb0f4`](#insn-00afb0f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb0f8`](#insn-00afb0f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb110`](#insn-00afb110) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb124`](#insn-00afb124) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afb128`](#insn-00afb128) → [`00afb168`](#insn-00afb168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb130`](#insn-00afb130) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb150`](#insn-00afb150) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afb168`](#insn-00afb168) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb16c`](#insn-00afb16c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb170`](#insn-00afb170) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb174`](#insn-00afb174) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb0ec`](#insn-00afb0ec)

~~~json
{
  "source": "00afb0ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb0f0`](#insn-00afb0f0)

~~~json
{
  "source": "00afb0f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb0f4`](#insn-00afb0f4)

~~~json
{
  "source": "00afb0f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb0f8`](#insn-00afb0f8)

~~~json
{
  "source": "00afb0f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb110`](#insn-00afb110)

~~~json
{
  "source": "00afb110",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb124`](#insn-00afb124)

~~~json
{
  "source": "00afb124",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb128`](#insn-00afb128)

~~~json
{
  "source": "00afb128",
  "target": "00afb168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb130`](#insn-00afb130)

~~~json
{
  "source": "00afb130",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb150`](#insn-00afb150)

~~~json
{
  "source": "00afb150",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb168`](#insn-00afb168)

~~~json
{
  "source": "00afb168",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb16c`](#insn-00afb16c)

~~~json
{
  "source": "00afb16c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb170`](#insn-00afb170)

~~~json
{
  "source": "00afb170",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb174`](#insn-00afb174)

~~~json
{
  "source": "00afb174",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
