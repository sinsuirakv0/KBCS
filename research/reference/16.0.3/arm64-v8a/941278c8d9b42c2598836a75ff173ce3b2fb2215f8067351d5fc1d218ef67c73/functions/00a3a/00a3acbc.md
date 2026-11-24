# 00a3acbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a39cc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0010.md#compare-e9ae74a11b18d29e13d3e833f7964e39)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3acbc",
  "name": "FUN_00a3acbc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ead6bc07aee2e5737c5e784daceafe1ad58d5133c3ceb01eb66559b06cf1fd65",
  "source_text_sha256": "ead6bc07aee2e5737c5e784daceafe1ad58d5133c3ceb01eb66559b06cf1fd65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3acbc",
        "00a3ad63"
      ]
    ],
    "bytes_sha256": "3ae2ec40a9eb5f346c795819cee480f67ee1738163ba136257d3186e91ad2094",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a3ac84](../00a3a/00a3ac84.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1266 bytes

~~~c

void FUN_00a3acbc(undefined8 param_1,undefined8 param_2,long param_3,undefined8 param_4,long param_5
                 )

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
  for (; param_3 != param_5; param_3 = param_3 + -0x80) {
    pvVar1 = *(void **)(param_3 + -0x20);
    if (pvVar1 != (void *)0x0) {
      *(void **)(param_3 + -0x18) = pvVar1;
      _ZdlPv(pvVar1);
    }
    pvVar1 = *(void **)(param_3 + -0x48);
    if (pvVar1 != (void *)0x0) {
                    /* try { // try from 00a3ad10 to 00b3ad17 has its CatchHandler @ 00a3b0f4 */
      pvVar3 = *(void **)(param_3 + -0x40);
      pvVar2 = pvVar1;
      if (pvVar3 != pvVar1) {
        do {
          pvVar2 = *(void **)((long)pvVar3 + -0x18);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x10) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar2 = *(void **)((long)pvVar3 + -0x30);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x28) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar3 = (void *)((long)pvVar3 + -0x88);
        } while (pvVar3 != pvVar1);
        pvVar2 = *(void **)(param_3 + -0x48);
      }
      *(void **)(param_3 + -0x40) = pvVar1;
      _ZdlPv(pvVar2);
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3acbc"></a> `00a3acbc` | `5f 00 04 eb` | cmp x2,x4 | `FALL_THROUGH`
<a id="insn-00a3acc0"></a> `00a3acc0` | `00 05 00 54` | b.eq 0x00a3ad60 | `CONDITIONAL_JUMP`
<a id="insn-00a3acc4"></a> `00a3acc4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a3acc8"></a> `00a3acc8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3accc"></a> `00a3accc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3acd0"></a> `00a3acd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3acd4"></a> `00a3acd4` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00a3acd8"></a> `00a3acd8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00a3acdc"></a> `00a3acdc` | `07 00 00 14` | b 0x00a3acf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ace0"></a> `00a3ace0` | `80 82 5b f8` | ldur x0,[x20, #-0x48] | `FALL_THROUGH`
<a id="insn-00a3ace4"></a> `00a3ace4` | `95 02 1c f8` | stur x21,[x20, #-0x40] | `FALL_THROUGH`
<a id="insn-00a3ace8"></a> `00a3ace8` | `9a 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3acec"></a> `00a3acec` | `94 02 02 d1` | sub x20,x20,#0x80 | `FALL_THROUGH`
<a id="insn-00a3acf0"></a> `00a3acf0` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00a3acf4"></a> `00a3acf4` | `00 03 00 54` | b.eq 0x00a3ad54 | `CONDITIONAL_JUMP`
<a id="insn-00a3acf8"></a> `00a3acf8` | `80 02 5e f8` | ldur x0,[x20, #-0x20] | `FALL_THROUGH`
<a id="insn-00a3acfc"></a> `00a3acfc` | `60 00 00 b4` | cbz x0,0x00a3ad08 | `CONDITIONAL_JUMP`
<a id="insn-00a3ad00"></a> `00a3ad00` | `80 82 1e f8` | stur x0,[x20, #-0x18] | `FALL_THROUGH`
<a id="insn-00a3ad04"></a> `00a3ad04` | `93 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ad08"></a> `00a3ad08` | `95 82 5b f8` | ldur x21,[x20, #-0x48] | `FALL_THROUGH`
<a id="insn-00a3ad0c"></a> `00a3ad0c` | `15 ff ff b4` | cbz x21,0x00a3acec | `CONDITIONAL_JUMP`
<a id="insn-00a3ad10"></a> `00a3ad10` | `96 02 5c f8` | ldur x22,[x20, #-0x40] | `FALL_THROUGH`
<a id="insn-00a3ad14"></a> `00a3ad14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a3ad18"></a> `00a3ad18` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00a3ad1c"></a> `00a3ad1c` | `a1 00 00 54` | b.ne 0x00a3ad30 | `CONDITIONAL_JUMP`
<a id="insn-00a3ad20"></a> `00a3ad20` | `f1 ff ff 17` | b 0x00a3ace4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ad24"></a> `00a3ad24` | `d6 22 02 d1` | sub x22,x22,#0x88 | `FALL_THROUGH`
<a id="insn-00a3ad28"></a> `00a3ad28` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00a3ad2c"></a> `00a3ad2c` | `a0 fd ff 54` | b.eq 0x00a3ace0 | `CONDITIONAL_JUMP`
<a id="insn-00a3ad30"></a> `00a3ad30` | `c0 82 5e f8` | ldur x0,[x22, #-0x18] | `FALL_THROUGH`
<a id="insn-00a3ad34"></a> `00a3ad34` | `60 00 00 b4` | cbz x0,0x00a3ad40 | `CONDITIONAL_JUMP`
<a id="insn-00a3ad38"></a> `00a3ad38` | `c0 02 1f f8` | stur x0,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00a3ad3c"></a> `00a3ad3c` | `85 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ad40"></a> `00a3ad40` | `c0 02 5d f8` | ldur x0,[x22, #-0x30] | `FALL_THROUGH`
<a id="insn-00a3ad44"></a> `00a3ad44` | `00 ff ff b4` | cbz x0,0x00a3ad24 | `CONDITIONAL_JUMP`
<a id="insn-00a3ad48"></a> `00a3ad48` | `c0 82 1d f8` | stur x0,[x22, #-0x28] | `FALL_THROUGH`
<a id="insn-00a3ad4c"></a> `00a3ad4c` | `81 78 08 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ad50"></a> `00a3ad50` | `f5 ff ff 17` | b 0x00a3ad24 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3ad54"></a> `00a3ad54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ad58"></a> `00a3ad58` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ad5c"></a> `00a3ad5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a3ad60"></a> `00a3ad60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3acbc`](#insn-00a3acbc) 範囲 `[['00a3acbc', '00a3acc3']]`
  - `CONDITIONAL_JUMP` [`00a3acc0`](#insn-00a3acc0) → [`00a3ad60`](#insn-00a3ad60)
  - `FALL_THROUGH` [`00a3acc0`](#insn-00a3acc0) → [`00a3acc4`](#insn-00a3acc4)
- ブロック [`00a3acc4`](#insn-00a3acc4) 範囲 `[['00a3acc4', '00a3acdf']]`
  - `UNCONDITIONAL_JUMP` [`00a3acdc`](#insn-00a3acdc) → [`00a3acf8`](#insn-00a3acf8)
- ブロック [`00a3ace0`](#insn-00a3ace0) 範囲 `[['00a3ace0', '00a3ace3']]`
  - `FALL_THROUGH` [`00a3ace0`](#insn-00a3ace0) → [`00a3ace4`](#insn-00a3ace4)
- ブロック [`00a3ace4`](#insn-00a3ace4) 範囲 `[['00a3ace4', '00a3aceb']]`
  - `FALL_THROUGH` [`00a3ace8`](#insn-00a3ace8) → [`00a3acec`](#insn-00a3acec)
- ブロック [`00a3acec`](#insn-00a3acec) 範囲 `[['00a3acec', '00a3acf7']]`
  - `CONDITIONAL_JUMP` [`00a3acf4`](#insn-00a3acf4) → [`00a3ad54`](#insn-00a3ad54)
  - `FALL_THROUGH` [`00a3acf4`](#insn-00a3acf4) → [`00a3acf8`](#insn-00a3acf8)
- ブロック [`00a3acf8`](#insn-00a3acf8) 範囲 `[['00a3acf8', '00a3acff']]`
  - `CONDITIONAL_JUMP` [`00a3acfc`](#insn-00a3acfc) → [`00a3ad08`](#insn-00a3ad08)
  - `FALL_THROUGH` [`00a3acfc`](#insn-00a3acfc) → [`00a3ad00`](#insn-00a3ad00)
- ブロック [`00a3ad00`](#insn-00a3ad00) 範囲 `[['00a3ad00', '00a3ad07']]`
  - `FALL_THROUGH` [`00a3ad04`](#insn-00a3ad04) → [`00a3ad08`](#insn-00a3ad08)
- ブロック [`00a3ad08`](#insn-00a3ad08) 範囲 `[['00a3ad08', '00a3ad0f']]`
  - `CONDITIONAL_JUMP` [`00a3ad0c`](#insn-00a3ad0c) → [`00a3acec`](#insn-00a3acec)
  - `FALL_THROUGH` [`00a3ad0c`](#insn-00a3ad0c) → [`00a3ad10`](#insn-00a3ad10)
- ブロック [`00a3ad10`](#insn-00a3ad10) 範囲 `[['00a3ad10', '00a3ad1f']]`
  - `CONDITIONAL_JUMP` [`00a3ad1c`](#insn-00a3ad1c) → [`00a3ad30`](#insn-00a3ad30)
  - `FALL_THROUGH` [`00a3ad1c`](#insn-00a3ad1c) → [`00a3ad20`](#insn-00a3ad20)
- ブロック [`00a3ad20`](#insn-00a3ad20) 範囲 `[['00a3ad20', '00a3ad23']]`
  - `UNCONDITIONAL_JUMP` [`00a3ad20`](#insn-00a3ad20) → [`00a3ace4`](#insn-00a3ace4)
- ブロック [`00a3ad24`](#insn-00a3ad24) 範囲 `[['00a3ad24', '00a3ad2f']]`
  - `CONDITIONAL_JUMP` [`00a3ad2c`](#insn-00a3ad2c) → [`00a3ace0`](#insn-00a3ace0)
  - `FALL_THROUGH` [`00a3ad2c`](#insn-00a3ad2c) → [`00a3ad30`](#insn-00a3ad30)
- ブロック [`00a3ad30`](#insn-00a3ad30) 範囲 `[['00a3ad30', '00a3ad37']]`
  - `CONDITIONAL_JUMP` [`00a3ad34`](#insn-00a3ad34) → [`00a3ad40`](#insn-00a3ad40)
  - `FALL_THROUGH` [`00a3ad34`](#insn-00a3ad34) → [`00a3ad38`](#insn-00a3ad38)
- ブロック [`00a3ad38`](#insn-00a3ad38) 範囲 `[['00a3ad38', '00a3ad3f']]`
  - `FALL_THROUGH` [`00a3ad3c`](#insn-00a3ad3c) → [`00a3ad40`](#insn-00a3ad40)
- ブロック [`00a3ad40`](#insn-00a3ad40) 範囲 `[['00a3ad40', '00a3ad47']]`
  - `CONDITIONAL_JUMP` [`00a3ad44`](#insn-00a3ad44) → [`00a3ad24`](#insn-00a3ad24)
  - `FALL_THROUGH` [`00a3ad44`](#insn-00a3ad44) → [`00a3ad48`](#insn-00a3ad48)
- ブロック [`00a3ad48`](#insn-00a3ad48) 範囲 `[['00a3ad48', '00a3ad53']]`
  - `UNCONDITIONAL_JUMP` [`00a3ad50`](#insn-00a3ad50) → [`00a3ad24`](#insn-00a3ad24)
- ブロック [`00a3ad54`](#insn-00a3ad54) 範囲 `[['00a3ad54', '00a3ad5f']]`
  - `FALL_THROUGH` [`00a3ad5c`](#insn-00a3ad5c) → [`00a3ad60`](#insn-00a3ad60)
- ブロック [`00a3ad60`](#insn-00a3ad60) 範囲 `[['00a3ad60', '00a3ad63']]`

## 命令位置別の参照

- [`00a3acc0`](#insn-00a3acc0) → [`00a3ad60`](#insn-00a3ad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3acc4`](#insn-00a3acc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3acc8`](#insn-00a3acc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3accc`](#insn-00a3accc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3acdc`](#insn-00a3acdc) → [`00a3acf8`](#insn-00a3acf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ace8`](#insn-00a3ace8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3acf4`](#insn-00a3acf4) → [`00a3ad54`](#insn-00a3ad54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3acfc`](#insn-00a3acfc) → [`00a3ad08`](#insn-00a3ad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad04`](#insn-00a3ad04) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad0c`](#insn-00a3ad0c) → [`00a3acec`](#insn-00a3acec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad1c`](#insn-00a3ad1c) → [`00a3ad30`](#insn-00a3ad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad20`](#insn-00a3ad20) → [`00a3ace4`](#insn-00a3ace4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad2c`](#insn-00a3ad2c) → [`00a3ace0`](#insn-00a3ace0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad34`](#insn-00a3ad34) → [`00a3ad40`](#insn-00a3ad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad3c`](#insn-00a3ad3c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad44`](#insn-00a3ad44) → [`00a3ad24`](#insn-00a3ad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad4c`](#insn-00a3ad4c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad50`](#insn-00a3ad50) → [`00a3ad24`](#insn-00a3ad24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad54`](#insn-00a3ad54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad58`](#insn-00a3ad58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ad5c`](#insn-00a3ad5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3acc0`](#insn-00a3acc0)

~~~json
{
  "source": "00a3acc0",
  "target": "00a3ad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3acc4`](#insn-00a3acc4)

~~~json
{
  "source": "00a3acc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3acc8`](#insn-00a3acc8)

~~~json
{
  "source": "00a3acc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3accc`](#insn-00a3accc)

~~~json
{
  "source": "00a3accc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3acdc`](#insn-00a3acdc)

~~~json
{
  "source": "00a3acdc",
  "target": "00a3acf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ace8`](#insn-00a3ace8)

~~~json
{
  "source": "00a3ace8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3acf4`](#insn-00a3acf4)

~~~json
{
  "source": "00a3acf4",
  "target": "00a3ad54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3acfc`](#insn-00a3acfc)

~~~json
{
  "source": "00a3acfc",
  "target": "00a3ad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad04`](#insn-00a3ad04)

~~~json
{
  "source": "00a3ad04",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ad0c`](#insn-00a3ad0c)

~~~json
{
  "source": "00a3ad0c",
  "target": "00a3acec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad1c`](#insn-00a3ad1c)

~~~json
{
  "source": "00a3ad1c",
  "target": "00a3ad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad20`](#insn-00a3ad20)

~~~json
{
  "source": "00a3ad20",
  "target": "00a3ace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad2c`](#insn-00a3ad2c)

~~~json
{
  "source": "00a3ad2c",
  "target": "00a3ace0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad34`](#insn-00a3ad34)

~~~json
{
  "source": "00a3ad34",
  "target": "00a3ad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad3c`](#insn-00a3ad3c)

~~~json
{
  "source": "00a3ad3c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ad44`](#insn-00a3ad44)

~~~json
{
  "source": "00a3ad44",
  "target": "00a3ad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad4c`](#insn-00a3ad4c)

~~~json
{
  "source": "00a3ad4c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ad50`](#insn-00a3ad50)

~~~json
{
  "source": "00a3ad50",
  "target": "00a3ad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad54`](#insn-00a3ad54)

~~~json
{
  "source": "00a3ad54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad58`](#insn-00a3ad58)

~~~json
{
  "source": "00a3ad58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ad5c`](#insn-00a3ad5c)

~~~json
{
  "source": "00a3ad5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
