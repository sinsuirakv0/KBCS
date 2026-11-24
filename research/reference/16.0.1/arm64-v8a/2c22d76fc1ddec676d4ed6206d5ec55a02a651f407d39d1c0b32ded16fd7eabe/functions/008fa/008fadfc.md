# 008fadfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `008fac60`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac60.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0051.md#compare-364594fad21cffd0c7c47e7ed2784b23)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `008fae50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fae50.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0053.md#compare-520f1057f99952ca5dd10c841d4fa6aa)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fadfc",
  "name": "FUN_008fadfc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a815ecb14940f02f45c1ccf1d13add7fe49446796991160ef7f69f2bb3fa9def",
  "source_text_sha256": "a815ecb14940f02f45c1ccf1d13add7fe49446796991160ef7f69f2bb3fa9def",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fadfc",
        "008fae5f"
      ]
    ],
    "bytes_sha256": "f4de52fac1bf891ab7174ebfe370d7b8d8335be005cb483c26e1bc2b81ea1425",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
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
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 611 bytes

~~~c

void FUN_008fadfc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  
                    /* try { // try from 008fae04 to 009fae27 has its CatchHandler @ 008fae8c */
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar3 = *param_2;
    uVar1 = FUN_0047acf4();
                    /* try { // try from 008fae28 to 009faf13 has its CatchHandler @ 008fa990 */
    FUN_0047cdd4(uVar1,0xb,0);
    lVar2 = FUN_008514f8();
    *(uint *)(lVar2 + 0x4a844) = *(uint *)(lVar2 + 0x4a844) | 8;
    FUN_008b9178(uVar3);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fadfc"></a> `008fadfc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008fae00"></a> `008fae00` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-008fae04"></a> `008fae04` | `c1 02 00 54` | b.ne 0x008fae5c | `CONDITIONAL_JUMP`
<a id="insn-008fae08"></a> `008fae08` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-008fae0c"></a> `008fae0c` | `88 02 00 35` | cbnz w8,0x008fae5c | `CONDITIONAL_JUMP`
<a id="insn-008fae10"></a> `008fae10` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008fae14"></a> `008fae14` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008fae18"></a> `008fae18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008fae1c"></a> `008fae1c` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-008fae20"></a> `008fae20` | `b5 ff ed 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-008fae24"></a> `008fae24` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008fae28"></a> `008fae28` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-008fae2c"></a> `008fae2c` | `ea 07 ee 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-008fae30"></a> `008fae30` | `b2 59 fd 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-008fae34"></a> `008fae34` | `89 08 95 52` | mov w9,#0xa844 | `FALL_THROUGH`
<a id="insn-008fae38"></a> `008fae38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-008fae3c"></a> `008fae3c` | `89 00 a0 72` | movk w9,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-008fae40"></a> `008fae40` | `0a 68 69 b8` | ldr w10,[x0, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008fae44"></a> `008fae44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fae48"></a> `008fae48` | `4a 01 1d 32` | orr w10,w10,#0x8 | `FALL_THROUGH`
<a id="insn-008fae4c"></a> `008fae4c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008fae50"></a> `008fae50` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008fae54"></a> `008fae54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008fae58"></a> `008fae58` | `c8 f8 fe 17` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-008fae5c"></a> `008fae5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fadfc`](#insn-008fadfc) 範囲 `[['008fadfc', '008fae03']]`
  - `FALL_THROUGH` [`008fae00`](#insn-008fae00) → [`008fae04`](#insn-008fae04)
- ブロック [`008fae04`](#insn-008fae04) 範囲 `[['008fae04', '008fae07']]`
  - `CONDITIONAL_JUMP` [`008fae04`](#insn-008fae04) → [`008fae5c`](#insn-008fae5c)
  - `FALL_THROUGH` [`008fae04`](#insn-008fae04) → [`008fae08`](#insn-008fae08)
- ブロック [`008fae08`](#insn-008fae08) 範囲 `[['008fae08', '008fae0f']]`
  - `CONDITIONAL_JUMP` [`008fae0c`](#insn-008fae0c) → [`008fae5c`](#insn-008fae5c)
  - `FALL_THROUGH` [`008fae0c`](#insn-008fae0c) → [`008fae10`](#insn-008fae10)
- ブロック [`008fae10`](#insn-008fae10) 範囲 `[['008fae10', '008fae27']]`
  - `FALL_THROUGH` [`008fae24`](#insn-008fae24) → [`008fae28`](#insn-008fae28)
- ブロック [`008fae28`](#insn-008fae28) 範囲 `[['008fae28', '008fae5b']]`
- ブロック [`008fae5c`](#insn-008fae5c) 範囲 `[['008fae5c', '008fae5f']]`

## 命令位置別の参照

- [`008fae04`](#insn-008fae04) → [`008fae5c`](#insn-008fae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae0c`](#insn-008fae0c) → [`008fae5c`](#insn-008fae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae10`](#insn-008fae10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae14`](#insn-008fae14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae20`](#insn-008fae20) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`008fae2c`](#insn-008fae2c) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`008fae30`](#insn-008fae30) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`008fae50`](#insn-008fae50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae54`](#insn-008fae54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae58`](#insn-008fae58) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fae04`](#insn-008fae04)

~~~json
{
  "source": "008fae04",
  "target": "008fae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae0c`](#insn-008fae0c)

~~~json
{
  "source": "008fae0c",
  "target": "008fae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae10`](#insn-008fae10)

~~~json
{
  "source": "008fae10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae14`](#insn-008fae14)

~~~json
{
  "source": "008fae14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae20`](#insn-008fae20)

~~~json
{
  "source": "008fae20",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae2c`](#insn-008fae2c)

~~~json
{
  "source": "008fae2c",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae30`](#insn-008fae30)

~~~json
{
  "source": "008fae30",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae50`](#insn-008fae50)

~~~json
{
  "source": "008fae50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae54`](#insn-008fae54)

~~~json
{
  "source": "008fae54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae58`](#insn-008fae58)

~~~json
{
  "source": "008fae58",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
