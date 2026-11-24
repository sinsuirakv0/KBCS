# 00afbdf0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afadfc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afadfc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-3d9f597933ecd9a4e8d85e60bc357193)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbdf0",
  "name": "FUN_00afbdf0",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9afb05e61b3bd6b16e27b546b4d2605b3ff72d53bb68de214b9eb8b14f119a3f",
  "source_text_sha256": "9afb05e61b3bd6b16e27b546b4d2605b3ff72d53bb68de214b9eb8b14f119a3f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbdf0",
        "00afbe3b"
      ]
    ],
    "bytes_sha256": "1c172aeb8b8102830b39c141a2861fc812f18c0f45b5859367f84fd88e4b81b8",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afbdf0(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbe0c to 00bfbf97 has its CatchHandler @ 00afbbcc */
  lVar1 = FUN_008524fc();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a34) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbdf0"></a> `00afbdf0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbdf4"></a> `00afbdf4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbdf8"></a> `00afbdf8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbdfc"></a> `00afbdfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbe00"></a> `00afbe00` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afbe04"></a> `00afbe04` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afbe08"></a> `00afbe08` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afbe0c"></a> `00afbe0c` | `bc 59 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afbe10"></a> `00afbe10` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbe14"></a> `00afbe14` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbe18"></a> `00afbe18` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbe1c"></a> `00afbe1c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbe20"></a> `00afbe20` | `89 46 89 52` | mov w9,#0x4a34 | `FALL_THROUGH`
<a id="insn-00afbe24"></a> `00afbe24` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbe28"></a> `00afbe28` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbe2c"></a> `00afbe2c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbe30"></a> `00afbe30` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe34"></a> `00afbe34` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afbe38"></a> `00afbe38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbdf0`](#insn-00afbdf0) 範囲 `[['00afbdf0', '00afbe0b']]`
  - `FALL_THROUGH` [`00afbe08`](#insn-00afbe08) → [`00afbe0c`](#insn-00afbe0c)
- ブロック [`00afbe0c`](#insn-00afbe0c) 範囲 `[['00afbe0c', '00afbe3b']]`

## 命令位置別の参照

- [`00afbdf0`](#insn-00afbdf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbdf4`](#insn-00afbdf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbdf8`](#insn-00afbdf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe0c`](#insn-00afbe0c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afbe2c`](#insn-00afbe2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe30`](#insn-00afbe30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe34`](#insn-00afbe34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbdf0`](#insn-00afbdf0)

~~~json
{
  "source": "00afbdf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbdf4`](#insn-00afbdf4)

~~~json
{
  "source": "00afbdf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbdf8`](#insn-00afbdf8)

~~~json
{
  "source": "00afbdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe0c`](#insn-00afbe0c)

~~~json
{
  "source": "00afbe0c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe2c`](#insn-00afbe2c)

~~~json
{
  "source": "00afbe2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe30`](#insn-00afbe30)

~~~json
{
  "source": "00afbe30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe34`](#insn-00afbe34)

~~~json
{
  "source": "00afbe34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
