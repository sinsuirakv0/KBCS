# 00af6cac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af6c10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6c10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-aa04cac73e2b0c7b98fc74518d5fc106)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af7ca0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af7/00af7ca0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-93144971fc0f11b9756e1819d8222f71)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af6cac",
  "name": "FUN_00af6cac",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5",
  "source_text_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af6cac",
        "00af6d2b"
      ]
    ],
    "bytes_sha256": "2fea64ab050dd1b9c6c19dcea52f0b4536b1389cdf919133803a10c031b5a481",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 400 bytes

~~~c

void FUN_00af6cac(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  
  lVar1 = FUN_00851550();
  uVar2 = FUN_005e7460(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
  lVar1 = 0x44;
  if ((uVar2 & 1) != 0) {
    lVar1 = 0x40;
  }
  *(uint *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + lVar1 + 0x848c8) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af6cac"></a> `00af6cac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af6cb0"></a> `00af6cb0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6cb4"></a> `00af6cb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af6cb8"></a> `00af6cb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af6cbc"></a> `00af6cbc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af6cc0"></a> `00af6cc0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af6cc4"></a> `00af6cc4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af6cc8"></a> `00af6cc8` | `22 6a f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af6ccc"></a> `00af6ccc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af6cd0"></a> `00af6cd0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af6cd4"></a> `00af6cd4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af6cd8"></a> `00af6cd8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af6cdc"></a> `00af6cdc` | `e1 c1 eb 97` | bl 0x005e7460 | `UNCONDITIONAL_CALL`
<a id="insn-00af6ce0"></a> `00af6ce0` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00af6ce4"></a> `00af6ce4` | `73 02 00 12` | and w19,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00af6ce8"></a> `00af6ce8` | `1a 6a f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af6cec"></a> `00af6cec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af6cf0"></a> `00af6cf0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af6cf4"></a> `00af6cf4` | `df 02 00 72` | tst w22,#0x1 | `FALL_THROUGH`
<a id="insn-00af6cf8"></a> `00af6cf8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af6cfc"></a> `00af6cfc` | `8a 08 80 52` | mov w10,#0x44 | `FALL_THROUGH`
<a id="insn-00af6d00"></a> `00af6d00` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af6d04"></a> `00af6d04` | `09 08 80 52` | mov w9,#0x40 | `FALL_THROUGH`
<a id="insn-00af6d08"></a> `00af6d08` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00af6d0c"></a> `00af6d0c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00af6d10"></a> `00af6d10` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af6d14"></a> `00af6d14` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af6d18"></a> `00af6d18` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af6d1c"></a> `00af6d1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af6d20"></a> `00af6d20` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6d24"></a> `00af6d24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af6d28"></a> `00af6d28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af6cac`](#insn-00af6cac) 範囲 `[['00af6cac', '00af6d2b']]`

## 命令位置別の参照

- [`00af6cac`](#insn-00af6cac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6cb0`](#insn-00af6cb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6cb4`](#insn-00af6cb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6cc8`](#insn-00af6cc8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af6cdc`](#insn-00af6cdc) → [`005e7460`](../005e7/005e7460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7460` · 推定シンボル `None` · 推定型 `None`
- [`00af6ce8`](#insn-00af6ce8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af6d1c`](#insn-00af6d1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6d20`](#insn-00af6d20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6d24`](#insn-00af6d24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af6cac`](#insn-00af6cac)

~~~json
{
  "source": "00af6cac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6cb0`](#insn-00af6cb0)

~~~json
{
  "source": "00af6cb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6cb4`](#insn-00af6cb4)

~~~json
{
  "source": "00af6cb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6cc8`](#insn-00af6cc8)

~~~json
{
  "source": "00af6cc8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6cdc`](#insn-00af6cdc)

~~~json
{
  "source": "00af6cdc",
  "target": "005e7460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6ce8`](#insn-00af6ce8)

~~~json
{
  "source": "00af6ce8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6d1c`](#insn-00af6d1c)

~~~json
{
  "source": "00af6d1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6d20`](#insn-00af6d20)

~~~json
{
  "source": "00af6d20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6d24`](#insn-00af6d24)

~~~json
{
  "source": "00af6d24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
