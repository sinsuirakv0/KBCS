# 00b0eedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0eab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-126e707470984468c84ae6c463d29c66)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b0ef78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0ef78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-e316d0bdb8209f2614bee64e23a813e1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0eedc",
  "name": "FUN_00b0eedc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b",
  "source_text_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0eedc",
        "00b0ef97"
      ]
    ],
    "bytes_sha256": "e3dcabfd98342b87db7e8947b722e2079fa6022b534c0c6c834bac33ca332164",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a223d0](../00a22/00a223d0.md)

## 呼び出し先

- [00480d48](../00480/00480d48.md)
- [00480e28](../00480/00480e28.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 696 bytes

~~~c

void FUN_00b0eedc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480e28(param_2,*param_1);
  FUN_00480e28(param_2,param_1[3]);
  FUN_00480e28(param_2,param_1[5]);
  FUN_00480e28(param_2,param_1[4]);
  FUN_00480e28(param_2,param_1[1]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 7));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1d));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1e));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1f));
  FUN_00480e28(param_2,param_1[2]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 8));
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 9));
  FUN_00480d48(param_2,*(undefined1 *)(param_1 + 0xb));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0eedc"></a> `00b0eedc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b0eee0"></a> `00b0eee0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0eee4"></a> `00b0eee4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0eee8"></a> `00b0eee8` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00b0eeec"></a> `00b0eeec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0eef0"></a> `00b0eef0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b0eef4"></a> `00b0eef4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00b0eef8"></a> `00b0eef8` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00b0eefc"></a> `00b0eefc` | `cb c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef00"></a> `00b0ef00` | `61 0e 40 b9` | ldr w1,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00b0ef04"></a> `00b0ef04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef08"></a> `00b0ef08` | `c8 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef0c"></a> `00b0ef0c` | `61 16 40 b9` | ldr w1,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00b0ef10"></a> `00b0ef10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef14"></a> `00b0ef14` | `c5 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef18"></a> `00b0ef18` | `61 12 40 b9` | ldr w1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ef1c"></a> `00b0ef1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef20"></a> `00b0ef20` | `c2 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef24"></a> `00b0ef24` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00b0ef28"></a> `00b0ef28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef2c"></a> `00b0ef2c` | `bf c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef30"></a> `00b0ef30` | `61 72 40 39` | ldrb w1,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00b0ef34"></a> `00b0ef34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef38"></a> `00b0ef38` | `bc c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef3c"></a> `00b0ef3c` | `61 76 40 39` | ldrb w1,[x19, #0x1d] | `FALL_THROUGH`
<a id="insn-00b0ef40"></a> `00b0ef40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef44"></a> `00b0ef44` | `b9 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef48"></a> `00b0ef48` | `61 7a 40 39` | ldrb w1,[x19, #0x1e] | `FALL_THROUGH`
<a id="insn-00b0ef4c"></a> `00b0ef4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef50"></a> `00b0ef50` | `b6 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef54"></a> `00b0ef54` | `61 7e 40 39` | ldrb w1,[x19, #0x1f] | `FALL_THROUGH`
<a id="insn-00b0ef58"></a> `00b0ef58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef5c"></a> `00b0ef5c` | `b3 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef60"></a> `00b0ef60` | `61 0a 40 b9` | ldr w1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0ef64"></a> `00b0ef64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef68"></a> `00b0ef68` | `b0 c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef6c"></a> `00b0ef6c` | `61 82 40 39` | ldrb w1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ef70"></a> `00b0ef70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef74"></a> `00b0ef74` | `ad c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef78"></a> `00b0ef78` | `61 92 40 39` | ldrb w1,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00b0ef7c"></a> `00b0ef7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef80"></a> `00b0ef80` | `aa c7 e5 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ef84"></a> `00b0ef84` | `61 b2 40 39` | ldrb w1,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00b0ef88"></a> `00b0ef88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0ef8c"></a> `00b0ef8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ef90"></a> `00b0ef90` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b0ef94"></a> `00b0ef94` | `6d c7 e5 17` | b 0x00480d48 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0eedc`](#insn-00b0eedc) 範囲 `[['00b0eedc', '00b0ef97']]`

## 命令位置別の参照

- [`00b0eedc`](#insn-00b0eedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eee0`](#insn-00b0eee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0eefc`](#insn-00b0eefc) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef08`](#insn-00b0ef08) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef14`](#insn-00b0ef14) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef20`](#insn-00b0ef20) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef2c`](#insn-00b0ef2c) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef38`](#insn-00b0ef38) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef44`](#insn-00b0ef44) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef50`](#insn-00b0ef50) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef5c`](#insn-00b0ef5c) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef68`](#insn-00b0ef68) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef74`](#insn-00b0ef74) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef80`](#insn-00b0ef80) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef8c`](#insn-00b0ef8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef90`](#insn-00b0ef90) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ef94`](#insn-00b0ef94) → [`00480d48`](../00480/00480d48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480d48` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0eedc`](#insn-00b0eedc)

~~~json
{
  "source": "00b0eedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eee0`](#insn-00b0eee0)

~~~json
{
  "source": "00b0eee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0eefc`](#insn-00b0eefc)

~~~json
{
  "source": "00b0eefc",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef08`](#insn-00b0ef08)

~~~json
{
  "source": "00b0ef08",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef14`](#insn-00b0ef14)

~~~json
{
  "source": "00b0ef14",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef20`](#insn-00b0ef20)

~~~json
{
  "source": "00b0ef20",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef2c`](#insn-00b0ef2c)

~~~json
{
  "source": "00b0ef2c",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef38`](#insn-00b0ef38)

~~~json
{
  "source": "00b0ef38",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef44`](#insn-00b0ef44)

~~~json
{
  "source": "00b0ef44",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef50`](#insn-00b0ef50)

~~~json
{
  "source": "00b0ef50",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef5c`](#insn-00b0ef5c)

~~~json
{
  "source": "00b0ef5c",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef68`](#insn-00b0ef68)

~~~json
{
  "source": "00b0ef68",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef74`](#insn-00b0ef74)

~~~json
{
  "source": "00b0ef74",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef80`](#insn-00b0ef80)

~~~json
{
  "source": "00b0ef80",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ef8c`](#insn-00b0ef8c)

~~~json
{
  "source": "00b0ef8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ef90`](#insn-00b0ef90)

~~~json
{
  "source": "00b0ef90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ef94`](#insn-00b0ef94)

~~~json
{
  "source": "00b0ef94",
  "target": "00480d48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
