# 00afa7bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afa720`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afa720.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-0a9b5a73a4ca713f419cdb2b69aefa14)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afb7b0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afb/00afb7b0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-819af9c5aeca702976224438292899e0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa7bc",
  "name": "FUN_00afa7bc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8",
  "source_text_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afa7bc",
        "00afa82b"
      ]
    ],
    "bytes_sha256": "8f659ae51627b087f9f69f491fb7125ea9c679a0f912e246143f773590a680ee",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 579 bytes

~~~c

bool FUN_00afa7bc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_00851550();
                    /* try { // try from 00afa810 to 00bfa823 has its CatchHandler @ 00afab7c */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c28) != 0;
  }
                    /* try { // try from 00afa828 to 00bfa83f has its CatchHandler @ 00afaa48 */
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afa7bc"></a> `00afa7bc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afa7c0"></a> `00afa7c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa7c4"></a> `00afa7c4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afa7c8"></a> `00afa7c8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afa7cc"></a> `00afa7cc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afa7d0"></a> `00afa7d0` | `60 5b f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afa7d4"></a> `00afa7d4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afa7d8"></a> `00afa7d8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afa7dc"></a> `00afa7dc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa7e0"></a> `00afa7e0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afa7e4"></a> `00afa7e4` | `1f b3 eb 97` | bl 0x005e7460 | `UNCONDITIONAL_CALL`
<a id="insn-00afa7e8"></a> `00afa7e8` | `60 00 00 37` | tbnz w0,#0x0,0x00afa7f4 | `CONDITIONAL_JUMP`
<a id="insn-00afa7ec"></a> `00afa7ec` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afa7f0"></a> `00afa7f0` | `0c 00 00 14` | b 0x00afa820 | `UNCONDITIONAL_JUMP`
<a id="insn-00afa7f4"></a> `00afa7f4` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afa7f8"></a> `00afa7f8` | `56 5b f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afa7fc"></a> `00afa7fc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afa800"></a> `00afa800` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afa804"></a> `00afa804` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa808"></a> `00afa808` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afa80c"></a> `00afa80c` | `09 85 89 52` | mov w9,#0x4c28 | `FALL_THROUGH`
<a id="insn-00afa810"></a> `00afa810` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afa814"></a> `00afa814` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afa818"></a> `00afa818` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afa81c"></a> `00afa81c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afa820"></a> `00afa820` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa824"></a> `00afa824` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afa828"></a> `00afa828` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afa7bc`](#insn-00afa7bc) 範囲 `[['00afa7bc', '00afa7eb']]`
  - `CONDITIONAL_JUMP` [`00afa7e8`](#insn-00afa7e8) → [`00afa7f4`](#insn-00afa7f4)
  - `FALL_THROUGH` [`00afa7e8`](#insn-00afa7e8) → [`00afa7ec`](#insn-00afa7ec)
- ブロック [`00afa7ec`](#insn-00afa7ec) 範囲 `[['00afa7ec', '00afa7f3']]`
  - `UNCONDITIONAL_JUMP` [`00afa7f0`](#insn-00afa7f0) → [`00afa820`](#insn-00afa820)
- ブロック [`00afa7f4`](#insn-00afa7f4) 範囲 `[['00afa7f4', '00afa80f']]`
  - `FALL_THROUGH` [`00afa80c`](#insn-00afa80c) → [`00afa810`](#insn-00afa810)
- ブロック [`00afa810`](#insn-00afa810) 範囲 `[['00afa810', '00afa81f']]`
  - `FALL_THROUGH` [`00afa81c`](#insn-00afa81c) → [`00afa820`](#insn-00afa820)
- ブロック [`00afa820`](#insn-00afa820) 範囲 `[['00afa820', '00afa827']]`
  - `FALL_THROUGH` [`00afa824`](#insn-00afa824) → [`00afa828`](#insn-00afa828)
- ブロック [`00afa828`](#insn-00afa828) 範囲 `[['00afa828', '00afa82b']]`

## 命令位置別の参照

- [`00afa7bc`](#insn-00afa7bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa7c0`](#insn-00afa7c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa7d0`](#insn-00afa7d0) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afa7e4`](#insn-00afa7e4) → [`005e7460`](../005e7/005e7460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7460` · 推定シンボル `None` · 推定型 `None`
- [`00afa7e8`](#insn-00afa7e8) → [`00afa7f4`](#insn-00afa7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa7f0`](#insn-00afa7f0) → [`00afa820`](#insn-00afa820) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa7f8`](#insn-00afa7f8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afa820`](#insn-00afa820) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa824`](#insn-00afa824) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afa7bc`](#insn-00afa7bc)

~~~json
{
  "source": "00afa7bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa7c0`](#insn-00afa7c0)

~~~json
{
  "source": "00afa7c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa7d0`](#insn-00afa7d0)

~~~json
{
  "source": "00afa7d0",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa7e4`](#insn-00afa7e4)

~~~json
{
  "source": "00afa7e4",
  "target": "005e7460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa7e8`](#insn-00afa7e8)

~~~json
{
  "source": "00afa7e8",
  "target": "00afa7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa7f0`](#insn-00afa7f0)

~~~json
{
  "source": "00afa7f0",
  "target": "00afa820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa7f8`](#insn-00afa7f8)

~~~json
{
  "source": "00afa7f8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa820`](#insn-00afa820)

~~~json
{
  "source": "00afa820",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa824`](#insn-00afa824)

~~~json
{
  "source": "00afa824",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
