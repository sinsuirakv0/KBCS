# 00af9cec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af8cf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af8/00af8cf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-2ccaddf30bb70854c4d1b51bfbfbabce)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9cec",
  "name": "FUN_00af9cec",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44b4ba221680d0c6d8fd333f82a3857452a871ee828d6dd43076ba5d83e64427",
  "source_text_sha256": "44b4ba221680d0c6d8fd333f82a3857452a871ee828d6dd43076ba5d83e64427",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af9cec",
        "00af9d37"
      ]
    ],
    "bytes_sha256": "ab159195ca4561694be0d4f91119513f68abc3c1cc1ff541e3117b45390f12c8",
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

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00af9cec(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84cb0) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af9cec"></a> `00af9cec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af9cf0"></a> `00af9cf0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9cf4"></a> `00af9cf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af9cf8"></a> `00af9cf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af9cfc"></a> `00af9cfc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af9d00"></a> `00af9d00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af9d04"></a> `00af9d04` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af9d08"></a> `00af9d08` | `fd 61 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af9d0c"></a> `00af9d0c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af9d10"></a> `00af9d10` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af9d14"></a> `00af9d14` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9d18"></a> `00af9d18` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af9d1c"></a> `00af9d1c` | `09 96 89 52` | mov w9,#0x4cb0 | `FALL_THROUGH`
<a id="insn-00af9d20"></a> `00af9d20` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af9d24"></a> `00af9d24` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af9d28"></a> `00af9d28` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af9d2c"></a> `00af9d2c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9d30"></a> `00af9d30` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af9d34"></a> `00af9d34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af9cec`](#insn-00af9cec) 範囲 `[['00af9cec', '00af9d37']]`

## 命令位置別の参照

- [`00af9cec`](#insn-00af9cec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9cf0`](#insn-00af9cf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9cf4`](#insn-00af9cf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9d08`](#insn-00af9d08) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af9d28`](#insn-00af9d28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9d2c`](#insn-00af9d2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9d30`](#insn-00af9d30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af9cec`](#insn-00af9cec)

~~~json
{
  "source": "00af9cec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9cf0`](#insn-00af9cf0)

~~~json
{
  "source": "00af9cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9cf4`](#insn-00af9cf4)

~~~json
{
  "source": "00af9cf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9d08`](#insn-00af9d08)

~~~json
{
  "source": "00af9d08",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9d28`](#insn-00af9d28)

~~~json
{
  "source": "00af9d28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9d2c`](#insn-00af9d2c)

~~~json
{
  "source": "00af9d2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9d30`](#insn-00af9d30)

~~~json
{
  "source": "00af9d30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
