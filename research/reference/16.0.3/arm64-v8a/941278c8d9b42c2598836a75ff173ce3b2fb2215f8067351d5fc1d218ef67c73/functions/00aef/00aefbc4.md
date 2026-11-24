# 00aefbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeebd0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeebd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-2fd9276f0a604d1538f621c33361e8c6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefbc4",
  "name": "FUN_00aefbc4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07b5c2edadc208e9dac81e8de1b41bde6e6af6638287f8d1d14702a687f4108e",
  "source_text_sha256": "07b5c2edadc208e9dac81e8de1b41bde6e6af6638287f8d1d14702a687f4108e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefbc4",
        "00aefc03"
      ]
    ],
    "bytes_sha256": "d0a6203bb17f629d80af0c7ea27ae485b633358229bb56f4b0d9e0e89c2c51fe",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 276 bytes

~~~c

void FUN_00aefbc4(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    uVar2 = *param_2;
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    FUN_008ba17c(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefbc4"></a> `00aefbc4` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aefbc8"></a> `00aefbc8` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aefbcc"></a> `00aefbcc` | `a1 01 00 54` | b.ne 0x00aefc00 | `CONDITIONAL_JUMP`
<a id="insn-00aefbd0"></a> `00aefbd0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aefbd4"></a> `00aefbd4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefbd8"></a> `00aefbd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefbdc"></a> `00aefbdc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aefbe0"></a> `00aefbe0` | `1d 2d e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00aefbe4"></a> `00aefbe4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aefbe8"></a> `00aefbe8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefbec"></a> `00aefbec` | `52 35 e6 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-00aefbf0"></a> `00aefbf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefbf4"></a> `00aefbf4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefbf8"></a> `00aefbf8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aefbfc"></a> `00aefbfc` | `60 29 f7 17` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-00aefc00"></a> `00aefc00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefbc4`](#insn-00aefbc4) 範囲 `[['00aefbc4', '00aefbcf']]`
  - `CONDITIONAL_JUMP` [`00aefbcc`](#insn-00aefbcc) → [`00aefc00`](#insn-00aefc00)
  - `FALL_THROUGH` [`00aefbcc`](#insn-00aefbcc) → [`00aefbd0`](#insn-00aefbd0)
- ブロック [`00aefbd0`](#insn-00aefbd0) 範囲 `[['00aefbd0', '00aefbff']]`
- ブロック [`00aefc00`](#insn-00aefc00) 範囲 `[['00aefc00', '00aefc03']]`

## 命令位置別の参照

- [`00aefbcc`](#insn-00aefbcc) → [`00aefc00`](#insn-00aefc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbd0`](#insn-00aefbd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbd4`](#insn-00aefbd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbe0`](#insn-00aefbe0) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00aefbec`](#insn-00aefbec) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00aefbf4`](#insn-00aefbf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbf8`](#insn-00aefbf8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbfc`](#insn-00aefbfc) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefbcc`](#insn-00aefbcc)

~~~json
{
  "source": "00aefbcc",
  "target": "00aefc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbd0`](#insn-00aefbd0)

~~~json
{
  "source": "00aefbd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbd4`](#insn-00aefbd4)

~~~json
{
  "source": "00aefbd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbe0`](#insn-00aefbe0)

~~~json
{
  "source": "00aefbe0",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbec`](#insn-00aefbec)

~~~json
{
  "source": "00aefbec",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbf4`](#insn-00aefbf4)

~~~json
{
  "source": "00aefbf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbf8`](#insn-00aefbf8)

~~~json
{
  "source": "00aefbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbfc`](#insn-00aefbfc)

~~~json
{
  "source": "00aefbfc",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
