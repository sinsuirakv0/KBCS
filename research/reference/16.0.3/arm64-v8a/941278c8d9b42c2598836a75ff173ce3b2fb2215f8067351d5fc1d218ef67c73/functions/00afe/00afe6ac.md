# 00afe6ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afd6b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afd/00afd6b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-99a716aa0078290469c2f6087e4eae71)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afe6ac",
  "name": "FUN_00afe6ac",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fcb423586fee6ec8d7dd227280e96c8947440e51bbc434784ddb5ccebf40a5e",
  "source_text_sha256": "8fcb423586fee6ec8d7dd227280e96c8947440e51bbc434784ddb5ccebf40a5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afe6ac",
        "00afe717"
      ]
    ],
    "bytes_sha256": "f7ad63bfb82af2260befbf63a5998c4eb065cccdef10fa1a1f38fb467dbf67c8",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 356 bytes

~~~c

void FUN_00afe6ac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a50) = param_3;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afe6ac"></a> `00afe6ac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afe6b0"></a> `00afe6b0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe6b4"></a> `00afe6b4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afe6b8"></a> `00afe6b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afe6bc"></a> `00afe6bc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afe6c0"></a> `00afe6c0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afe6c4"></a> `00afe6c4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afe6c8"></a> `00afe6c8` | `8d 4f f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe6cc"></a> `00afe6cc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afe6d0"></a> `00afe6d0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afe6d4"></a> `00afe6d4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe6d8"></a> `00afe6d8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe6dc"></a> `00afe6dc` | `4d a4 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afe6e0"></a> `00afe6e0` | `40 01 00 37` | tbnz w0,#0x0,0x00afe708 | `CONDITIONAL_JUMP`
<a id="insn-00afe6e4"></a> `00afe6e4` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afe6e8"></a> `00afe6e8` | `85 4f f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe6ec"></a> `00afe6ec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afe6f0"></a> `00afe6f0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afe6f4"></a> `00afe6f4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe6f8"></a> `00afe6f8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe6fc"></a> `00afe6fc` | `09 4a 89 52` | mov w9,#0x4a50 | `FALL_THROUGH`
<a id="insn-00afe700"></a> `00afe700` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe704"></a> `00afe704` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe708"></a> `00afe708` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afe70c"></a> `00afe70c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe710"></a> `00afe710` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afe714"></a> `00afe714` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afe6ac`](#insn-00afe6ac) 範囲 `[['00afe6ac', '00afe6e3']]`
  - `CONDITIONAL_JUMP` [`00afe6e0`](#insn-00afe6e0) → [`00afe708`](#insn-00afe708)
  - `FALL_THROUGH` [`00afe6e0`](#insn-00afe6e0) → [`00afe6e4`](#insn-00afe6e4)
- ブロック [`00afe6e4`](#insn-00afe6e4) 範囲 `[['00afe6e4', '00afe707']]`
  - `FALL_THROUGH` [`00afe704`](#insn-00afe704) → [`00afe708`](#insn-00afe708)
- ブロック [`00afe708`](#insn-00afe708) 範囲 `[['00afe708', '00afe717']]`

## 命令位置別の参照

- [`00afe6ac`](#insn-00afe6ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6b0`](#insn-00afe6b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6b4`](#insn-00afe6b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6c8`](#insn-00afe6c8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe6dc`](#insn-00afe6dc) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afe6e0`](#insn-00afe6e0) → [`00afe708`](#insn-00afe708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe6e8`](#insn-00afe6e8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe708`](#insn-00afe708) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe70c`](#insn-00afe70c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe710`](#insn-00afe710) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afe6ac`](#insn-00afe6ac)

~~~json
{
  "source": "00afe6ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6b0`](#insn-00afe6b0)

~~~json
{
  "source": "00afe6b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6b4`](#insn-00afe6b4)

~~~json
{
  "source": "00afe6b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6c8`](#insn-00afe6c8)

~~~json
{
  "source": "00afe6c8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe6dc`](#insn-00afe6dc)

~~~json
{
  "source": "00afe6dc",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe6e0`](#insn-00afe6e0)

~~~json
{
  "source": "00afe6e0",
  "target": "00afe708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe6e8`](#insn-00afe6e8)

~~~json
{
  "source": "00afe6e8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe708`](#insn-00afe708)

~~~json
{
  "source": "00afe708",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe70c`](#insn-00afe70c)

~~~json
{
  "source": "00afe70c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe710`](#insn-00afe710)

~~~json
{
  "source": "00afe710",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
