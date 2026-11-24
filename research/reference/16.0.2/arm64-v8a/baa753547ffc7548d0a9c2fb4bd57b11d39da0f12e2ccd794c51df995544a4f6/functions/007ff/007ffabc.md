# 007ffabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007ffa64`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0043.md#compare-44c9bbc038e5b48758db003a86c914cd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00800a20`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00800/00800a20.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0043.md#compare-38219faa0bf38b6df30f64f320c2459b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffabc",
  "name": "FUN_007ffabc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5",
  "source_text_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ffabc",
        "007ffb2b"
      ]
    ],
    "bytes_sha256": "b330989478000a568f4b99a122a764266c1a413af2eb9acb641e2e36eccfe4ff",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 928 bytes

~~~c

undefined8 * FUN_007ffabc(long param_1)

{
  byte bVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 007ffac0 to 008ffb23 has its CatchHandler @ 007ff698 */
  puVar3 = (undefined8 *)_Znwm(0x30);
  bVar1 = *(byte *)(param_1 + 0x18);
  uVar4 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined1 *)(param_1 + 0x10);
  *puVar3 = &PTR_FUN_00c7e400;
  puVar3[1] = uVar4;
  *(undefined1 *)(puVar3 + 2) = uVar2;
  if ((bVar1 & 1) == 0) {
    uVar5 = *(undefined8 *)(param_1 + 0x18);
    uVar4 = *(undefined8 *)(param_1 + 0x28);
    puVar3[4] = *(undefined8 *)(param_1 + 0x20);
    puVar3[3] = uVar5;
    puVar3[5] = uVar4;
  }
  else {
    FUN_0043bb60(puVar3 + 3,*(undefined8 *)(param_1 + 0x28),*(undefined8 *)(param_1 + 0x20));
  }
                    /* try { // try from 007ffb24 to 008ffb7b has its CatchHandler @ 007ffdf8 */
  return puVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ffabc"></a> `007ffabc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007ffac0"></a> `007ffac0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ffac4"></a> `007ffac4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007ffac8"></a> `007ffac8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007ffacc"></a> `007ffacc` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-007ffad0"></a> `007ffad0` | `24 61 11 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-007ffad4"></a> `007ffad4` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-007ffad8"></a> `007ffad8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ffadc"></a> `007ffadc` | `e9 23 00 f0` | adrp x9,0xc7e000 | `FALL_THROUGH`
<a id="insn-007ffae0"></a> `007ffae0` | `29 01 10 91` | add x9,x9,#0x400 | `FALL_THROUGH`
<a id="insn-007ffae4"></a> `007ffae4` | `0a 8d 41 38` | ldrb w10,[x8, #0x18]! | `FALL_THROUGH`
<a id="insn-007ffae8"></a> `007ffae8` | `0b 01 5f f8` | ldur x11,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-007ffaec"></a> `007ffaec` | `0c 81 5f 38` | ldurb w12,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-007ffaf0"></a> `007ffaf0` | `09 2c 00 a9` | stp x9,x11,[x0] | `FALL_THROUGH`
<a id="insn-007ffaf4"></a> `007ffaf4` | `0c 40 00 39` | strb w12,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007ffaf8"></a> `007ffaf8` | `ca 00 00 37` | tbnz w10,#0x0,0x007ffb10 | `CONDITIONAL_JUMP`
<a id="insn-007ffafc"></a> `007ffafc` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-007ffb00"></a> `007ffb00` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ffb04"></a> `007ffb04` | `60 82 81 3c` | stur q0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-007ffb08"></a> `007ffb08` | `68 82 02 f8` | stur x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-007ffb0c"></a> `007ffb0c` | `04 00 00 14` | b 0x007ffb1c | `UNCONDITIONAL_JUMP`
<a id="insn-007ffb10"></a> `007ffb10` | `82 06 42 a9` | ldp x2,x1,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-007ffb14"></a> `007ffb14` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-007ffb18"></a> `007ffb18` | `12 f0 f0 97` | bl 0x0043bb60 | `UNCONDITIONAL_CALL`
<a id="insn-007ffb1c"></a> `007ffb1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ffb20"></a> `007ffb20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ffb24"></a> `007ffb24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007ffb28"></a> `007ffb28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ffabc`](#insn-007ffabc) 範囲 `[['007ffabc', '007ffabf']]`
  - `FALL_THROUGH` [`007ffabc`](#insn-007ffabc) → [`007ffac0`](#insn-007ffac0)
- ブロック [`007ffac0`](#insn-007ffac0) 範囲 `[['007ffac0', '007ffafb']]`
  - `CONDITIONAL_JUMP` [`007ffaf8`](#insn-007ffaf8) → [`007ffb10`](#insn-007ffb10)
  - `FALL_THROUGH` [`007ffaf8`](#insn-007ffaf8) → [`007ffafc`](#insn-007ffafc)
- ブロック [`007ffafc`](#insn-007ffafc) 範囲 `[['007ffafc', '007ffb0f']]`
  - `UNCONDITIONAL_JUMP` [`007ffb0c`](#insn-007ffb0c) → [`007ffb1c`](#insn-007ffb1c)
- ブロック [`007ffb10`](#insn-007ffb10) 範囲 `[['007ffb10', '007ffb1b']]`
  - `FALL_THROUGH` [`007ffb18`](#insn-007ffb18) → [`007ffb1c`](#insn-007ffb1c)
- ブロック [`007ffb1c`](#insn-007ffb1c) 範囲 `[['007ffb1c', '007ffb23']]`
  - `FALL_THROUGH` [`007ffb20`](#insn-007ffb20) → [`007ffb24`](#insn-007ffb24)
- ブロック [`007ffb24`](#insn-007ffb24) 範囲 `[['007ffb24', '007ffb2b']]`

## 命令位置別の参照

- [`007ffabc`](#insn-007ffabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffac0`](#insn-007ffac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffad0`](#insn-007ffad0) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`007ffaf0`](#insn-007ffaf0) → `00c7e400`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ffaf8`](#insn-007ffaf8) → [`007ffb10`](#insn-007ffb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffb0c`](#insn-007ffb0c) → [`007ffb1c`](#insn-007ffb1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffb18`](#insn-007ffb18) → [`0043bb60`](../0043b/0043bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb60` · 推定シンボル `None` · 推定型 `None`
- [`007ffb20`](#insn-007ffb20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ffb24`](#insn-007ffb24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ffabc`](#insn-007ffabc)

~~~json
{
  "source": "007ffabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffac0`](#insn-007ffac0)

~~~json
{
  "source": "007ffac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffad0`](#insn-007ffad0)

~~~json
{
  "source": "007ffad0",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ffaf0`](#insn-007ffaf0)

~~~json
{
  "source": "007ffaf0",
  "target": "00c7e400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7e400",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ffaf8`](#insn-007ffaf8)

~~~json
{
  "source": "007ffaf8",
  "target": "007ffb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffb0c`](#insn-007ffb0c)

~~~json
{
  "source": "007ffb0c",
  "target": "007ffb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffb18`](#insn-007ffb18)

~~~json
{
  "source": "007ffb18",
  "target": "0043bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ffb20`](#insn-007ffb20)

~~~json
{
  "source": "007ffb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ffb24`](#insn-007ffb24)

~~~json
{
  "source": "007ffb24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
