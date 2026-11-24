# 00bbd4fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbd460`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-4fffdbebe539addb396e03ac0f3ab154)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbe4f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-4722b768005a7160228ec861ebf2b6e5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbd4fc",
  "name": "FUN_00bbd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b",
  "source_text_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbd4fc",
        "00bbd5a3"
      ]
    ],
    "bytes_sha256": "e09bdfc6c5167f194c3cea484a41883b65e86c626809f125868d8477bc4a649b",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5d340](../00c5d/00c5d340.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 976 bytes

~~~c

void FUN_00bbd4fc(undefined8 param_1,undefined8 param_2,int param_3,undefined8 param_4,void *param_5
                 )

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_60 [16];
  undefined1 auStack_50 [8];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZN8firebase9messaging10FutureData3GetEv();
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
                    /* try { // try from 00bbd554 to 00cbd59b has its CatchHandler @ 00bbd73c */
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
            (uVar2,auStack_60,(ulong)(param_3 != 0) << 2,param_4,auStack_50);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbd4fc"></a> `00bbd4fc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbd500"></a> `00bbd500` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd504"></a> `00bbd504` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbd508"></a> `00bbd508` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd50c"></a> `00bbd50c` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbd510"></a> `00bbd510` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bbd514"></a> `00bbd514` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbd518"></a> `00bbd518` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd51c"></a> `00bbd51c` | `5f 00 00 71` | cmp w2,#0x0 | `FALL_THROUGH`
<a id="insn-00bbd520"></a> `00bbd520` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00bbd524"></a> `00bbd524` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bbd528"></a> `00bbd528` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bbd52c"></a> `00bbd52c` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd530"></a> `00bbd530` | `35 75 1e 53` | lsl w21,w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd534"></a> `00bbd534` | `83 7f 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd538"></a> `00bbd538` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbd53c"></a> `00bbd53c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbd540"></a> `00bbd540` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbd544"></a> `00bbd544` | `63 76 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd548"></a> `00bbd548` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbd54c"></a> `00bbd54c` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbd550"></a> `00bbd550` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbd554"></a> `00bbd554` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bbd558"></a> `00bbd558` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbd55c"></a> `00bbd55c` | `45 76 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd560"></a> `00bbd560` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbd564"></a> `00bbd564` | `7f 75 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd568"></a> `00bbd568` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd56c"></a> `00bbd56c` | `7d 75 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd570"></a> `00bbd570` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd574"></a> `00bbd574` | `83 6a 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd578"></a> `00bbd578` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd57c"></a> `00bbd57c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd580"></a> `00bbd580` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd584"></a> `00bbd584` | `e1 00 00 54` | b.ne 0x00bbd5a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd588"></a> `00bbd588` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbd58c"></a> `00bbd58c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd590"></a> `00bbd590` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbd594"></a> `00bbd594` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd598"></a> `00bbd598` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbd59c"></a> `00bbd59c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbd5a0"></a> `00bbd5a0` | `84 6a 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbd4fc`](#insn-00bbd4fc) 範囲 `[['00bbd4fc', '00bbd553']]`
  - `FALL_THROUGH` [`00bbd550`](#insn-00bbd550) → [`00bbd554`](#insn-00bbd554)
- ブロック [`00bbd554`](#insn-00bbd554) 範囲 `[['00bbd554', '00bbd587']]`
  - `CONDITIONAL_JUMP` [`00bbd584`](#insn-00bbd584) → [`00bbd5a0`](#insn-00bbd5a0)
  - `FALL_THROUGH` [`00bbd584`](#insn-00bbd584) → [`00bbd588`](#insn-00bbd588)
- ブロック [`00bbd588`](#insn-00bbd588) 範囲 `[['00bbd588', '00bbd59f']]`
- ブロック [`00bbd5a0`](#insn-00bbd5a0) 範囲 `[['00bbd5a0', '00bbd5a3']]`

## 命令位置別の参照

- [`00bbd500`](#insn-00bbd500) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd504`](#insn-00bbd504) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd508`](#insn-00bbd508) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd50c`](#insn-00bbd50c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd52c`](#insn-00bbd52c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd534`](#insn-00bbd534) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbd544`](#insn-00bbd544) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd55c`](#insn-00bbd55c) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbd564`](#insn-00bbd564) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbd56c`](#insn-00bbd56c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbd574`](#insn-00bbd574) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbd57c`](#insn-00bbd57c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd584`](#insn-00bbd584) → [`00bbd5a0`](#insn-00bbd5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd588`](#insn-00bbd588) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd58c`](#insn-00bbd58c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd590`](#insn-00bbd590) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd594`](#insn-00bbd594) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5a0`](#insn-00bbd5a0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbd500`](#insn-00bbd500)

~~~json
{
  "source": "00bbd500",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd504`](#insn-00bbd504)

~~~json
{
  "source": "00bbd504",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd508`](#insn-00bbd508)

~~~json
{
  "source": "00bbd508",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd50c`](#insn-00bbd50c)

~~~json
{
  "source": "00bbd50c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd52c`](#insn-00bbd52c)

~~~json
{
  "source": "00bbd52c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd534`](#insn-00bbd534)

~~~json
{
  "source": "00bbd534",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd544`](#insn-00bbd544)

~~~json
{
  "source": "00bbd544",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd55c`](#insn-00bbd55c)

~~~json
{
  "source": "00bbd55c",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd564`](#insn-00bbd564)

~~~json
{
  "source": "00bbd564",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd56c`](#insn-00bbd56c)

~~~json
{
  "source": "00bbd56c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd574`](#insn-00bbd574)

~~~json
{
  "source": "00bbd574",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd57c`](#insn-00bbd57c)

~~~json
{
  "source": "00bbd57c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd584`](#insn-00bbd584)

~~~json
{
  "source": "00bbd584",
  "target": "00bbd5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd588`](#insn-00bbd588)

~~~json
{
  "source": "00bbd588",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd58c`](#insn-00bbd58c)

~~~json
{
  "source": "00bbd58c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd590`](#insn-00bbd590)

~~~json
{
  "source": "00bbd590",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd594`](#insn-00bbd594)

~~~json
{
  "source": "00bbd594",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5a0`](#insn-00bbd5a0)

~~~json
{
  "source": "00bbd5a0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
