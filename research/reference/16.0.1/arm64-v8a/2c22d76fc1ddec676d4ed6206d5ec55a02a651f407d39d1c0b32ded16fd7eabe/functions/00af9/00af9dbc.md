# 00af9dbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af9994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af9994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-1486310c2e5d699e99c4ce84c554c6df)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9e58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9e58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-fb210808d2349c14e7b76809ece7dc8e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9dbc",
  "name": "FUN_00af9dbc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae139c01be89e972701b9f8ffb5502be4e256503a01f077cc882c4bf35b5739f",
  "source_text_sha256": "ae139c01be89e972701b9f8ffb5502be4e256503a01f077cc882c4bf35b5739f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af9dbc",
        "00af9e2b"
      ]
    ],
    "bytes_sha256": "c524eb5435b04a56ea724d54a2d200bc5e892ad84e6f567c03b705187483ca5f",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00af9dbc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_008514f8();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) != 0;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af9dbc"></a> `00af9dbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af9dc0"></a> `00af9dc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9dc4"></a> `00af9dc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af9dc8"></a> `00af9dc8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af9dcc"></a> `00af9dcc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af9dd0"></a> `00af9dd0` | `ca 5d f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af9dd4"></a> `00af9dd4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af9dd8"></a> `00af9dd8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af9ddc"></a> `00af9ddc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9de0"></a> `00af9de0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af9de4"></a> `00af9de4` | `8f b5 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00af9de8"></a> `00af9de8` | `60 00 00 37` | tbnz w0,#0x0,0x00af9df4 | `CONDITIONAL_JUMP`
<a id="insn-00af9dec"></a> `00af9dec` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00af9df0"></a> `00af9df0` | `0c 00 00 14` | b 0x00af9e20 | `UNCONDITIONAL_JUMP`
<a id="insn-00af9df4"></a> `00af9df4` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af9df8"></a> `00af9df8` | `c0 5d f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af9dfc"></a> `00af9dfc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af9e00"></a> `00af9e00` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af9e04"></a> `00af9e04` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9e08"></a> `00af9e08` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af9e0c"></a> `00af9e0c` | `89 61 89 52` | mov w9,#0x4b0c | `FALL_THROUGH`
<a id="insn-00af9e10"></a> `00af9e10` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af9e14"></a> `00af9e14` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af9e18"></a> `00af9e18` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af9e1c"></a> `00af9e1c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00af9e20"></a> `00af9e20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9e24"></a> `00af9e24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af9e28"></a> `00af9e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af9dbc`](#insn-00af9dbc) 範囲 `[['00af9dbc', '00af9deb']]`
  - `CONDITIONAL_JUMP` [`00af9de8`](#insn-00af9de8) → [`00af9df4`](#insn-00af9df4)
  - `FALL_THROUGH` [`00af9de8`](#insn-00af9de8) → [`00af9dec`](#insn-00af9dec)
- ブロック [`00af9dec`](#insn-00af9dec) 範囲 `[['00af9dec', '00af9df3']]`
  - `UNCONDITIONAL_JUMP` [`00af9df0`](#insn-00af9df0) → [`00af9e20`](#insn-00af9e20)
- ブロック [`00af9df4`](#insn-00af9df4) 範囲 `[['00af9df4', '00af9e1f']]`
  - `FALL_THROUGH` [`00af9e1c`](#insn-00af9e1c) → [`00af9e20`](#insn-00af9e20)
- ブロック [`00af9e20`](#insn-00af9e20) 範囲 `[['00af9e20', '00af9e2b']]`

## 命令位置別の参照

- [`00af9dbc`](#insn-00af9dbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9dc0`](#insn-00af9dc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9dd0`](#insn-00af9dd0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af9de4`](#insn-00af9de4) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00af9de8`](#insn-00af9de8) → [`00af9df4`](#insn-00af9df4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9df0`](#insn-00af9df0) → [`00af9e20`](#insn-00af9e20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9df8`](#insn-00af9df8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af9e20`](#insn-00af9e20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9e24`](#insn-00af9e24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af9dbc`](#insn-00af9dbc)

~~~json
{
  "source": "00af9dbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9dc0`](#insn-00af9dc0)

~~~json
{
  "source": "00af9dc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9dd0`](#insn-00af9dd0)

~~~json
{
  "source": "00af9dd0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9de4`](#insn-00af9de4)

~~~json
{
  "source": "00af9de4",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9de8`](#insn-00af9de8)

~~~json
{
  "source": "00af9de8",
  "target": "00af9df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9df0`](#insn-00af9df0)

~~~json
{
  "source": "00af9df0",
  "target": "00af9e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9df8`](#insn-00af9df8)

~~~json
{
  "source": "00af9df8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9e20`](#insn-00af9e20)

~~~json
{
  "source": "00af9e20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9e24`](#insn-00af9e24)

~~~json
{
  "source": "00af9e24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
