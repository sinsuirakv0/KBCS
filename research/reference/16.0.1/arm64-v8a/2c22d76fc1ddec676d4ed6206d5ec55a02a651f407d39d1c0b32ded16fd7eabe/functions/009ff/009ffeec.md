# 009ffeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009ffd50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffd50.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0058.md#compare-a2e02a7bde6ecd20699ab9309c2ae1db)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009fff40`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009fff40.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0060.md#compare-e40c77cb3cb8dfda5faac504311201ac)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009ffeec",
  "name": "FUN_009ffeec",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51d1bffb301ca667925f956e35ebfd3c28a2d25676102514ff6dd723a0a24cbc",
  "source_text_sha256": "51d1bffb301ca667925f956e35ebfd3c28a2d25676102514ff6dd723a0a24cbc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009ffeec",
        "009fff6b"
      ]
    ],
    "bytes_sha256": "d179379b2bab275cc182edd9b99b802cfc53e5fcbcd03077358bafb45348f5ba",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 752 bytes

~~~c

void FUN_009ffeec(long param_1,undefined8 *param_2)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  plVar1 = *(long **)(param_1 + 0x30);
  *param_2 = &PTR_FUN_00c8a810;
  if (plVar1 == (long *)0x0) {
    param_2[6] = 0;
  }
  else if (plVar1 == (long *)(param_1 + 0x10)) {
    param_2[6] = param_2 + 2;
    (**(code **)(**(long **)(param_1 + 0x30) + 0x18))();
  }
  else {
    uVar2 = (**(code **)(*plVar1 + 0x10))();
    param_2[6] = uVar2;
  }
  uVar3 = *(undefined8 *)(param_1 + 0x48);
  uVar2 = *(undefined8 *)(param_1 + 0x40);
                    /* try { // try from 009fff58 to 00afff77 has its CatchHandler @ 00a00f94 */
  param_2[10] = *(undefined8 *)(param_1 + 0x50);
  param_2[9] = uVar3;
  param_2[8] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009ffeec"></a> `009ffeec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009ffef0"></a> `009ffef0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ffef4"></a> `009ffef4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009ffef8"></a> `009ffef8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-009ffefc"></a> `009ffefc` | `00 18 40 f9` | ldr x0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-009fff00"></a> `009fff00` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-009fff04"></a> `009fff04` | `48 14 00 f0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fff08"></a> `009fff08` | `08 41 20 91` | add x8,x8,#0x810 | `FALL_THROUGH`
<a id="insn-009fff0c"></a> `009fff0c` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-009fff10"></a> `009fff10` | `20 01 00 b4` | cbz x0,0x009fff34 | `CONDITIONAL_JUMP`
<a id="insn-009fff14"></a> `009fff14` | `88 42 00 91` | add x8,x20,#0x10 | `FALL_THROUGH`
<a id="insn-009fff18"></a> `009fff18` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-009fff1c"></a> `009fff1c` | `00 01 00 54` | b.eq 0x009fff3c | `CONDITIONAL_JUMP`
<a id="insn-009fff20"></a> `009fff20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fff24"></a> `009fff24` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fff28"></a> `009fff28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fff2c"></a> `009fff2c` | `60 1a 00 f9` | str x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-009fff30"></a> `009fff30` | `08 00 00 14` | b 0x009fff50 | `UNCONDITIONAL_JUMP`
<a id="insn-009fff34"></a> `009fff34` | `7f 1a 00 f9` | str xzr,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-009fff38"></a> `009fff38` | `06 00 00 14` | b 0x009fff50 | `UNCONDITIONAL_JUMP`
<a id="insn-009fff3c"></a> `009fff3c` | `61 1a 00 f9` | str x1,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-009fff40"></a> `009fff40` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-009fff44"></a> `009fff44` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fff48"></a> `009fff48` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-009fff4c"></a> `009fff4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fff50"></a> `009fff50` | `88 2a 40 f9` | ldr x8,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-009fff54"></a> `009fff54` | `80 12 c0 3d` | ldr q0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-009fff58"></a> `009fff58` | `68 2a 00 f9` | str x8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-009fff5c"></a> `009fff5c` | `60 12 80 3d` | str q0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-009fff60"></a> `009fff60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fff64"></a> `009fff64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009fff68"></a> `009fff68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009ffeec`](#insn-009ffeec) 範囲 `[['009ffeec', '009fff13']]`
  - `CONDITIONAL_JUMP` [`009fff10`](#insn-009fff10) → [`009fff34`](#insn-009fff34)
  - `FALL_THROUGH` [`009fff10`](#insn-009fff10) → [`009fff14`](#insn-009fff14)
- ブロック [`009fff14`](#insn-009fff14) 範囲 `[['009fff14', '009fff1f']]`
  - `CONDITIONAL_JUMP` [`009fff1c`](#insn-009fff1c) → [`009fff3c`](#insn-009fff3c)
  - `FALL_THROUGH` [`009fff1c`](#insn-009fff1c) → [`009fff20`](#insn-009fff20)
- ブロック [`009fff20`](#insn-009fff20) 範囲 `[['009fff20', '009fff33']]`
  - `UNCONDITIONAL_JUMP` [`009fff30`](#insn-009fff30) → [`009fff50`](#insn-009fff50)
- ブロック [`009fff34`](#insn-009fff34) 範囲 `[['009fff34', '009fff3b']]`
  - `UNCONDITIONAL_JUMP` [`009fff38`](#insn-009fff38) → [`009fff50`](#insn-009fff50)
- ブロック [`009fff3c`](#insn-009fff3c) 範囲 `[['009fff3c', '009fff4f']]`
  - `FALL_THROUGH` [`009fff4c`](#insn-009fff4c) → [`009fff50`](#insn-009fff50)
- ブロック [`009fff50`](#insn-009fff50) 範囲 `[['009fff50', '009fff57']]`
  - `FALL_THROUGH` [`009fff54`](#insn-009fff54) → [`009fff58`](#insn-009fff58)
- ブロック [`009fff58`](#insn-009fff58) 範囲 `[['009fff58', '009fff6b']]`

## 命令位置別の参照

- [`009ffeec`](#insn-009ffeec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ffef0`](#insn-009ffef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff0c`](#insn-009fff0c) → `00c8a810`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fff10`](#insn-009fff10) → [`009fff34`](#insn-009fff34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff1c`](#insn-009fff1c) → [`009fff3c`](#insn-009fff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff30`](#insn-009fff30) → [`009fff50`](#insn-009fff50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff38`](#insn-009fff38) → [`009fff50`](#insn-009fff50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff60`](#insn-009fff60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fff64`](#insn-009fff64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009ffeec`](#insn-009ffeec)

~~~json
{
  "source": "009ffeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ffef0`](#insn-009ffef0)

~~~json
{
  "source": "009ffef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff0c`](#insn-009fff0c)

~~~json
{
  "source": "009fff0c",
  "target": "00c8a810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fff10`](#insn-009fff10)

~~~json
{
  "source": "009fff10",
  "target": "009fff34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff1c`](#insn-009fff1c)

~~~json
{
  "source": "009fff1c",
  "target": "009fff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff30`](#insn-009fff30)

~~~json
{
  "source": "009fff30",
  "target": "009fff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff38`](#insn-009fff38)

~~~json
{
  "source": "009fff38",
  "target": "009fff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff60`](#insn-009fff60)

~~~json
{
  "source": "009fff60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fff64`](#insn-009fff64)

~~~json
{
  "source": "009fff64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
