# 008acfdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008acf98`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf98.md) · 移動量 `+0x44`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0048.md#compare-1fb064650b5a753232396695ff06a3d4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `008ad034`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ad/008ad034.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0050.md#compare-d6ee3712bfd82f760e15eebf5ed54d34)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008acfdc",
  "name": "FUN_008acfdc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516",
  "source_text_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008acfdc",
        "008ad023"
      ]
    ],
    "bytes_sha256": "7483d45debe3559839ea1e29c462d0d29830c2f3a0db9f12853e32c9639966a5",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b9178](../008b9/008b9178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 745 bytes

~~~c

void FUN_008acfdc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
                    /* catch() { ... } // from try @ 008ace20 with catch @ 008acfe8 */
  if ((*param_3 == 2) && (*param_4 == 0)) {
                    /* catch() { ... } // from try @ 008acdf0 with catch @ 008acff8 */
    uVar2 = *param_2;
    uVar1 = FUN_0047acf4();
                    /* catch() { ... } // from try @ 008acdcc with catch @ 008ad00c */
    FUN_0047cdd4(uVar1,0xb,0);
                    /* catch() { ... } // from try @ 008acd60 with catch @ 008ad01c */
    FUN_008b9178(uVar2);
    return;
  }
                    /* catch() { ... } // from try @ 008acd50 with catch @ 008ad020 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008acfdc"></a> `008acfdc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008acfe0"></a> `008acfe0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-008acfe4"></a> `008acfe4` | `e1 01 00 54` | b.ne 0x008ad020 | `CONDITIONAL_JUMP`
<a id="insn-008acfe8"></a> `008acfe8` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-008acfec"></a> `008acfec` | `a8 01 00 35` | cbnz w8,0x008ad020 | `CONDITIONAL_JUMP`
<a id="insn-008acff0"></a> `008acff0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008acff4"></a> `008acff4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008acff8"></a> `008acff8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008acffc"></a> `008acffc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-008ad000"></a> `008ad000` | `3d 37 ef 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-008ad004"></a> `008ad004` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008ad008"></a> `008ad008` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-008ad00c"></a> `008ad00c` | `72 3f ef 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-008ad010"></a> `008ad010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad014"></a> `008ad014` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ad018"></a> `008ad018` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008ad01c"></a> `008ad01c` | `57 30 00 14` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-008ad020"></a> `008ad020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008acfdc`](#insn-008acfdc) 範囲 `[['008acfdc', '008acfe7']]`
  - `CONDITIONAL_JUMP` [`008acfe4`](#insn-008acfe4) → [`008ad020`](#insn-008ad020)
  - `FALL_THROUGH` [`008acfe4`](#insn-008acfe4) → [`008acfe8`](#insn-008acfe8)
- ブロック [`008acfe8`](#insn-008acfe8) 範囲 `[['008acfe8', '008acfef']]`
  - `CONDITIONAL_JUMP` [`008acfec`](#insn-008acfec) → [`008ad020`](#insn-008ad020)
  - `FALL_THROUGH` [`008acfec`](#insn-008acfec) → [`008acff0`](#insn-008acff0)
- ブロック [`008acff0`](#insn-008acff0) 範囲 `[['008acff0', '008acff7']]`
  - `FALL_THROUGH` [`008acff4`](#insn-008acff4) → [`008acff8`](#insn-008acff8)
- ブロック [`008acff8`](#insn-008acff8) 範囲 `[['008acff8', '008ad00b']]`
  - `FALL_THROUGH` [`008ad008`](#insn-008ad008) → [`008ad00c`](#insn-008ad00c)
- ブロック [`008ad00c`](#insn-008ad00c) 範囲 `[['008ad00c', '008ad01b']]`
  - `FALL_THROUGH` [`008ad018`](#insn-008ad018) → [`008ad01c`](#insn-008ad01c)
- ブロック [`008ad01c`](#insn-008ad01c) 範囲 `[['008ad01c', '008ad01f']]`
- ブロック [`008ad020`](#insn-008ad020) 範囲 `[['008ad020', '008ad023']]`

## 命令位置別の参照

- [`008acfe4`](#insn-008acfe4) → [`008ad020`](#insn-008ad020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfec`](#insn-008acfec) → [`008ad020`](#insn-008ad020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acff0`](#insn-008acff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acff4`](#insn-008acff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad000`](#insn-008ad000) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`008ad00c`](#insn-008ad00c) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`008ad014`](#insn-008ad014) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad018`](#insn-008ad018) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad01c`](#insn-008ad01c) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008acfe4`](#insn-008acfe4)

~~~json
{
  "source": "008acfe4",
  "target": "008ad020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfec`](#insn-008acfec)

~~~json
{
  "source": "008acfec",
  "target": "008ad020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acff0`](#insn-008acff0)

~~~json
{
  "source": "008acff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acff4`](#insn-008acff4)

~~~json
{
  "source": "008acff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad000`](#insn-008ad000)

~~~json
{
  "source": "008ad000",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad00c`](#insn-008ad00c)

~~~json
{
  "source": "008ad00c",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad014`](#insn-008ad014)

~~~json
{
  "source": "008ad014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad018`](#insn-008ad018)

~~~json
{
  "source": "008ad018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad01c`](#insn-008ad01c)

~~~json
{
  "source": "008ad01c",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
