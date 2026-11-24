# 00afaf9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9fa8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9fa8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-33b5183febb57d80135fe650d50f4d03)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaf9c",
  "name": "FUN_00afaf9c",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26540d63ff6931715ee5d8e297cdecd4c5505bb070c441ddcf4d068d385798ef",
  "source_text_sha256": "26540d63ff6931715ee5d8e297cdecd4c5505bb070c441ddcf4d068d385798ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaf9c",
        "00afb00b"
      ]
    ],
    "bytes_sha256": "56bcd6523fe194b05307467dc6f4037098725a2e81f7753ecd62363a2bbdc4d6",
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

## 疑似コード / UTF-8 639 bytes

~~~c

void FUN_00afaf9c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
                    /* try { // try from 00afafd4 to 00bfafdf has its CatchHandler @ 00afbae8 */
    lVar1 = FUN_008524fc();
                    /* try { // try from 00afafe4 to 00bfaffb has its CatchHandler @ 00afbad0 */
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) = param_3 & 1;
  }
                    /* try { // try from 00afaffc to 00bfb057 has its CatchHandler @ 00afaee0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaf9c"></a> `00afaf9c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afafa0"></a> `00afafa0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afafa4"></a> `00afafa4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afafa8"></a> `00afafa8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afafac"></a> `00afafac` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afafb0"></a> `00afafb0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afafb4"></a> `00afafb4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afafb8"></a> `00afafb8` | `51 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afafbc"></a> `00afafbc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afafc0"></a> `00afafc0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afafc4"></a> `00afafc4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afafc8"></a> `00afafc8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afafcc"></a> `00afafcc` | `11 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afafd0"></a> `00afafd0` | `60 01 00 36` | tbz w0,#0x0,0x00afaffc | `CONDITIONAL_JUMP`
<a id="insn-00afafd4"></a> `00afafd4` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afafd8"></a> `00afafd8` | `94 02 00 12` | and w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afafdc"></a> `00afafdc` | `48 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afafe0"></a> `00afafe0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afafe4"></a> `00afafe4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afafe8"></a> `00afafe8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afafec"></a> `00afafec` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaff0"></a> `00afaff0` | `89 7b 89 52` | mov w9,#0x4bdc | `FALL_THROUGH`
<a id="insn-00afaff4"></a> `00afaff4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaff8"></a> `00afaff8` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaffc"></a> `00afaffc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb000"></a> `00afb000` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb004"></a> `00afb004` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afb008"></a> `00afb008` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaf9c`](#insn-00afaf9c) 範囲 `[['00afaf9c', '00afafd3']]`
  - `CONDITIONAL_JUMP` [`00afafd0`](#insn-00afafd0) → [`00afaffc`](#insn-00afaffc)
  - `FALL_THROUGH` [`00afafd0`](#insn-00afafd0) → [`00afafd4`](#insn-00afafd4)
- ブロック [`00afafd4`](#insn-00afafd4) 範囲 `[['00afafd4', '00afafe3']]`
  - `FALL_THROUGH` [`00afafe0`](#insn-00afafe0) → [`00afafe4`](#insn-00afafe4)
- ブロック [`00afafe4`](#insn-00afafe4) 範囲 `[['00afafe4', '00afaffb']]`
  - `FALL_THROUGH` [`00afaff8`](#insn-00afaff8) → [`00afaffc`](#insn-00afaffc)
- ブロック [`00afaffc`](#insn-00afaffc) 範囲 `[['00afaffc', '00afb00b']]`

## 命令位置別の参照

- [`00afaf9c`](#insn-00afaf9c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafa0`](#insn-00afafa0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafa4`](#insn-00afafa4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafb8`](#insn-00afafb8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afafcc`](#insn-00afafcc) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afafd0`](#insn-00afafd0) → [`00afaffc`](#insn-00afaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafdc`](#insn-00afafdc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaffc`](#insn-00afaffc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb000`](#insn-00afb000) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb004`](#insn-00afb004) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaf9c`](#insn-00afaf9c)

~~~json
{
  "source": "00afaf9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafa0`](#insn-00afafa0)

~~~json
{
  "source": "00afafa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafa4`](#insn-00afafa4)

~~~json
{
  "source": "00afafa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafb8`](#insn-00afafb8)

~~~json
{
  "source": "00afafb8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafcc`](#insn-00afafcc)

~~~json
{
  "source": "00afafcc",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afafd0`](#insn-00afafd0)

~~~json
{
  "source": "00afafd0",
  "target": "00afaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafdc`](#insn-00afafdc)

~~~json
{
  "source": "00afafdc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaffc`](#insn-00afaffc)

~~~json
{
  "source": "00afaffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb000`](#insn-00afb000)

~~~json
{
  "source": "00afb000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb004`](#insn-00afb004)

~~~json
{
  "source": "00afb004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
