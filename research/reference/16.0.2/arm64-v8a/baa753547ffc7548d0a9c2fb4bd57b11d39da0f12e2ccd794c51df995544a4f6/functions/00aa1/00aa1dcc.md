# 00aa1dcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa1d5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1d5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-080ff49f1dcfdc17bb87f876cc0b8410)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aa2dc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa2/00aa2dc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-96e974d5a82e56288a85147b0bdbce5b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1dcc",
  "name": "FUN_00aa1dcc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f",
  "source_text_sha256": "681c19c16fce87a04e503be4ca3f3f4198600a21a4ddd489867afde8698f812f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1dcc",
        "00aa1e1b"
      ]
    ],
    "bytes_sha256": "c58a5d2c9344a208bd72dfa98ff478c6d30ed3f96898e30fd3b50eccfd146338",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa02d8](../00aa0/00aa02d8.md)
- [00aa1dcc](../00aa1/00aa1dcc.md)

## 呼び出し先

- [00aa1dcc](../00aa1/00aa1dcc.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 359 bytes

~~~c

void FUN_00aa1dcc(undefined8 param_1,undefined8 *param_2)

{
  void *__ptr;
  
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aa1dcc(param_1,*param_2);
    FUN_00aa1dcc(param_1,param_2[1]);
    __ptr = (void *)param_2[5];
    if (__ptr != (void *)0x0) {
      param_2[6] = __ptr;
      _ZdlPv(__ptr);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa1dcc"></a> `00aa1dcc` | `61 02 00 b4` | cbz x1,0x00aa1e18 | `CONDITIONAL_JUMP`
<a id="insn-00aa1dd0"></a> `00aa1dd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aa1dd4"></a> `00aa1dd4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1dd8"></a> `00aa1dd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa1ddc"></a> `00aa1ddc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aa1de0"></a> `00aa1de0` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00aa1de4"></a> `00aa1de4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa1de8"></a> `00aa1de8` | `f9 ff ff 97` | bl 0x00aa1dcc | `UNCONDITIONAL_CALL`
<a id="insn-00aa1dec"></a> `00aa1dec` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1df0"></a> `00aa1df0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa1df4"></a> `00aa1df4` | `f6 ff ff 97` | bl 0x00aa1dcc | `UNCONDITIONAL_CALL`
<a id="insn-00aa1df8"></a> `00aa1df8` | `60 16 40 f9` | ldr x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1dfc"></a> `00aa1dfc` | `60 00 00 b4` | cbz x0,0x00aa1e08 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e00"></a> `00aa1e00` | `60 1a 00 f9` | str x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1e04"></a> `00aa1e04` | `5f d8 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e08"></a> `00aa1e08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1e0c"></a> `00aa1e0c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e10"></a> `00aa1e10` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aa1e14"></a> `00aa1e14` | `5b d8 06 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00aa1e18"></a> `00aa1e18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1dcc`](#insn-00aa1dcc) 範囲 `[['00aa1dcc', '00aa1dcf']]`
  - `CONDITIONAL_JUMP` [`00aa1dcc`](#insn-00aa1dcc) → [`00aa1e18`](#insn-00aa1e18)
  - `FALL_THROUGH` [`00aa1dcc`](#insn-00aa1dcc) → [`00aa1dd0`](#insn-00aa1dd0)
- ブロック [`00aa1dd0`](#insn-00aa1dd0) 範囲 `[['00aa1dd0', '00aa1dff']]`
  - `CONDITIONAL_JUMP` [`00aa1dfc`](#insn-00aa1dfc) → [`00aa1e08`](#insn-00aa1e08)
  - `FALL_THROUGH` [`00aa1dfc`](#insn-00aa1dfc) → [`00aa1e00`](#insn-00aa1e00)
- ブロック [`00aa1e00`](#insn-00aa1e00) 範囲 `[['00aa1e00', '00aa1e07']]`
  - `FALL_THROUGH` [`00aa1e04`](#insn-00aa1e04) → [`00aa1e08`](#insn-00aa1e08)
- ブロック [`00aa1e08`](#insn-00aa1e08) 範囲 `[['00aa1e08', '00aa1e17']]`
- ブロック [`00aa1e18`](#insn-00aa1e18) 範囲 `[['00aa1e18', '00aa1e1b']]`

## 命令位置別の参照

- [`00aa1dcc`](#insn-00aa1dcc) → [`00aa1e18`](#insn-00aa1e18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd0`](#insn-00aa1dd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd4`](#insn-00aa1dd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1de8`](#insn-00aa1de8) → [`00aa1dcc`](#insn-00aa1dcc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa1dcc` · 推定シンボル `None` · 推定型 `None`
- [`00aa1df4`](#insn-00aa1df4) → [`00aa1dcc`](#insn-00aa1dcc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa1dcc` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dfc`](#insn-00aa1dfc) → [`00aa1e08`](#insn-00aa1e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e04`](#insn-00aa1e04) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e0c`](#insn-00aa1e0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e10`](#insn-00aa1e10) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e14`](#insn-00aa1e14) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1dcc`](#insn-00aa1dcc)

~~~json
{
  "source": "00aa1dcc",
  "target": "00aa1e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd0`](#insn-00aa1dd0)

~~~json
{
  "source": "00aa1dd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd4`](#insn-00aa1dd4)

~~~json
{
  "source": "00aa1dd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1de8`](#insn-00aa1de8)

~~~json
{
  "source": "00aa1de8",
  "target": "00aa1dcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1df4`](#insn-00aa1df4)

~~~json
{
  "source": "00aa1df4",
  "target": "00aa1dcc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1dfc`](#insn-00aa1dfc)

~~~json
{
  "source": "00aa1dfc",
  "target": "00aa1e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e04`](#insn-00aa1e04)

~~~json
{
  "source": "00aa1e04",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e0c`](#insn-00aa1e0c)

~~~json
{
  "source": "00aa1e0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e10`](#insn-00aa1e10)

~~~json
{
  "source": "00aa1e10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e14`](#insn-00aa1e14)

~~~json
{
  "source": "00aa1e14",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
