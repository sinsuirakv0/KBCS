# 005dbfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005dbf7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005dbf7c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0025.md#compare-39d1152376ab588a2163f091625180e3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `005dc36c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005dc/005dc36c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0025.md#compare-6297a0f6dca707c94fa521ec1c0d4637)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dbfbc",
  "name": "FUN_005dbfbc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fb3e7f2a8a6cd6cdcd1c46311dd8d16d1701f32f6099973c26c37719d2ee92c",
  "source_text_sha256": "5fb3e7f2a8a6cd6cdcd1c46311dd8d16d1701f32f6099973c26c37719d2ee92c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005dbfbc",
        "005dc0a3"
      ]
    ],
    "bytes_sha256": "c027f2b180088d8e37e4c77444950167b371849d6200cbc6b839d78b412e0423",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00687ee4](../00687/00687ee4.md)
- [00689994](../00689/00689994.md)
- [00851550](../00851/00851550.md)
- [008b91d0](../008b9/008b91d0.md)
- [00a1a6f8](../00a1a/00a1a6f8.md)
- [00b3bfbc](../00b3b/00b3bfbc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 938 bytes

~~~c

void FUN_005dbfbc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  long lVar4;
  
  uVar3 = *param_2;
  if ((*param_3 == 2) && (*param_4 == 0)) {
    lVar4 = *(long *)(param_1 + 8);
    lVar1 = FUN_00851550();
    FUN_00b3bfbc(lVar1 + 0xc578,*(undefined4 *)(param_1 + 0x10));
    lVar1 = FUN_00851550();
    FUN_00687ee4(lVar1 + 0x1648,*(undefined4 *)(param_1 + 0x14),
                 *(undefined4 *)(*(long *)(lVar4 + 8) + (long)*(int *)(lVar4 + 0x330) * 0x68 + 100),
                 0xffffffff);
    lVar1 = FUN_00851550();
    FUN_00689994(lVar1 + 0x1648,*(undefined4 *)(param_1 + 0x18),1);
    FUN_00851550();
    FUN_00a1a6f8();
    lVar1 = FUN_00851550();
    BYTE_ARRAY_0042ebdd[lVar1 + 0x23] = 1;
  }
  else if ((*param_3 != 2) || (*param_4 != 1)) {
    return;
  }
  uVar2 = FUN_0047ad34();
  FUN_0047ce14(uVar2,0xb,0);
  FUN_008b91d0(uVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005dbfbc"></a> `005dbfbc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-005dbfc0"></a> `005dbfc0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dbfc4"></a> `005dbfc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dbfc8"></a> `005dbfc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005dbfcc"></a> `005dbfcc` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-005dbfd0"></a> `005dbfd0` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-005dbfd4"></a> `005dbfd4` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-005dbfd8"></a> `005dbfd8` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-005dbfdc"></a> `005dbfdc` | `21 04 00 54` | b.ne 0x005dc060 | `CONDITIONAL_JUMP`
<a id="insn-005dbfe0"></a> `005dbfe0` | `08 04 00 35` | cbnz w8,0x005dc060 | `CONDITIONAL_JUMP`
<a id="insn-005dbfe4"></a> `005dbfe4` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005dbfe8"></a> `005dbfe8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-005dbfec"></a> `005dbfec` | `59 d5 09 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-005dbff0"></a> `005dbff0` | `a1 12 40 b9` | ldr w1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-005dbff4"></a> `005dbff4` | `08 af 98 52` | mov w8,#0xc578 | `FALL_THROUGH`
<a id="insn-005dbff8"></a> `005dbff8` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-005dbffc"></a> `005dbffc` | `f0 7f 15 94` | bl 0x00b3bfbc | `UNCONDITIONAL_CALL`
<a id="insn-005dc000"></a> `005dc000` | `54 d5 09 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-005dc004"></a> `005dc004` | `88 32 83 b9` | ldrsw x8,[x20, #0x330] | `FALL_THROUGH`
<a id="insn-005dc008"></a> `005dc008` | `09 0d 80 52` | mov w9,#0x68 | `FALL_THROUGH`
<a id="insn-005dc00c"></a> `005dc00c` | `8a 06 40 f9` | ldr x10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005dc010"></a> `005dc010` | `a1 16 40 b9` | ldr w1,[x21, #0x14] | `FALL_THROUGH`
<a id="insn-005dc014"></a> `005dc014` | `14 c9 82 52` | mov w20,#0x1648 | `FALL_THROUGH`
<a id="insn-005dc018"></a> `005dc018` | `03 00 80 12` | mov w3,#0xffffffff | `FALL_THROUGH`
<a id="insn-005dc01c"></a> `005dc01c` | `08 29 29 9b` | smaddl x8,w8,w9,x10 | `FALL_THROUGH`
<a id="insn-005dc020"></a> `005dc020` | `00 00 14 8b` | add x0,x0,x20 | `FALL_THROUGH`
<a id="insn-005dc024"></a> `005dc024` | `02 65 40 b9` | ldr w2,[x8, #0x64] | `FALL_THROUGH`
<a id="insn-005dc028"></a> `005dc028` | `af af 02 94` | bl 0x00687ee4 | `UNCONDITIONAL_CALL`
<a id="insn-005dc02c"></a> `005dc02c` | `49 d5 09 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-005dc030"></a> `005dc030` | `a1 1a 40 b9` | ldr w1,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-005dc034"></a> `005dc034` | `00 00 14 8b` | add x0,x0,x20 | `FALL_THROUGH`
<a id="insn-005dc038"></a> `005dc038` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-005dc03c"></a> `005dc03c` | `34 00 80 52` | mov w20,#0x1 | `FALL_THROUGH`
<a id="insn-005dc040"></a> `005dc040` | `55 b6 02 94` | bl 0x00689994 | `UNCONDITIONAL_CALL`
<a id="insn-005dc044"></a> `005dc044` | `43 d5 09 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-005dc048"></a> `005dc048` | `ac f9 10 94` | bl 0x00a1a6f8 | `UNCONDITIONAL_CALL`
<a id="insn-005dc04c"></a> `005dc04c` | `41 d5 09 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-005dc050"></a> `005dc050` | `08 80 9d 52` | mov w8,#0xec00 | `FALL_THROUGH`
<a id="insn-005dc054"></a> `005dc054` | `48 08 a0 72` | movk w8,#0x42, LSL #16 | `FALL_THROUGH`
<a id="insn-005dc058"></a> `005dc058` | `14 68 28 38` | strb w20,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-005dc05c"></a> `005dc05c` | `05 00 00 14` | b 0x005dc070 | `UNCONDITIONAL_JUMP`
<a id="insn-005dc060"></a> `005dc060` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-005dc064"></a> `005dc064` | `81 01 00 54` | b.ne 0x005dc094 | `CONDITIONAL_JUMP`
<a id="insn-005dc068"></a> `005dc068` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-005dc06c"></a> `005dc06c` | `41 01 00 54` | b.ne 0x005dc094 | `CONDITIONAL_JUMP`
<a id="insn-005dc070"></a> `005dc070` | `31 7b fa 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-005dc074"></a> `005dc074` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-005dc078"></a> `005dc078` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-005dc07c"></a> `005dc07c` | `66 83 fa 97` | bl 0x0047ce14 | `UNCONDITIONAL_CALL`
<a id="insn-005dc080"></a> `005dc080` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005dc084"></a> `005dc084` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dc088"></a> `005dc088` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dc08c"></a> `005dc08c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-005dc090"></a> `005dc090` | `50 74 0b 14` | b 0x008b91d0 | `CALL_TERMINATOR`
<a id="insn-005dc094"></a> `005dc094` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dc098"></a> `005dc098` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dc09c"></a> `005dc09c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-005dc0a0"></a> `005dc0a0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005dbfbc`](#insn-005dbfbc) 範囲 `[['005dbfbc', '005dbfdf']]`
  - `CONDITIONAL_JUMP` [`005dbfdc`](#insn-005dbfdc) → [`005dc060`](#insn-005dc060)
  - `FALL_THROUGH` [`005dbfdc`](#insn-005dbfdc) → [`005dbfe0`](#insn-005dbfe0)
- ブロック [`005dbfe0`](#insn-005dbfe0) 範囲 `[['005dbfe0', '005dbfe3']]`
  - `CONDITIONAL_JUMP` [`005dbfe0`](#insn-005dbfe0) → [`005dc060`](#insn-005dc060)
  - `FALL_THROUGH` [`005dbfe0`](#insn-005dbfe0) → [`005dbfe4`](#insn-005dbfe4)
- ブロック [`005dbfe4`](#insn-005dbfe4) 範囲 `[['005dbfe4', '005dc05f']]`
  - `UNCONDITIONAL_JUMP` [`005dc05c`](#insn-005dc05c) → [`005dc070`](#insn-005dc070)
- ブロック [`005dc060`](#insn-005dc060) 範囲 `[['005dc060', '005dc067']]`
  - `CONDITIONAL_JUMP` [`005dc064`](#insn-005dc064) → [`005dc094`](#insn-005dc094)
  - `FALL_THROUGH` [`005dc064`](#insn-005dc064) → [`005dc068`](#insn-005dc068)
- ブロック [`005dc068`](#insn-005dc068) 範囲 `[['005dc068', '005dc06f']]`
  - `CONDITIONAL_JUMP` [`005dc06c`](#insn-005dc06c) → [`005dc094`](#insn-005dc094)
  - `FALL_THROUGH` [`005dc06c`](#insn-005dc06c) → [`005dc070`](#insn-005dc070)
- ブロック [`005dc070`](#insn-005dc070) 範囲 `[['005dc070', '005dc093']]`
- ブロック [`005dc094`](#insn-005dc094) 範囲 `[['005dc094', '005dc0a3']]`

## 命令位置別の参照

- [`005dbfbc`](#insn-005dbfbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dbfc0`](#insn-005dbfc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dbfc4`](#insn-005dbfc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dbfdc`](#insn-005dbfdc) → [`005dc060`](#insn-005dc060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dbfe0`](#insn-005dbfe0) → [`005dc060`](#insn-005dc060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dbfec`](#insn-005dbfec) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`005dbffc`](#insn-005dbffc) → [`00b3bfbc`](../00b3b/00b3bfbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bfbc` · 推定シンボル `None` · 推定型 `None`
- [`005dc000`](#insn-005dc000) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`005dc028`](#insn-005dc028) → [`00687ee4`](../00687/00687ee4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00687ee4` · 推定シンボル `None` · 推定型 `None`
- [`005dc02c`](#insn-005dc02c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`005dc040`](#insn-005dc040) → [`00689994`](../00689/00689994.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00689994` · 推定シンボル `None` · 推定型 `None`
- [`005dc044`](#insn-005dc044) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`005dc048`](#insn-005dc048) → [`00a1a6f8`](../00a1a/00a1a6f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a1a6f8` · 推定シンボル `None` · 推定型 `None`
- [`005dc04c`](#insn-005dc04c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`005dc058`](#insn-005dc058) → `0042ec00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[59]`
- [`005dc05c`](#insn-005dc05c) → [`005dc070`](#insn-005dc070) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc064`](#insn-005dc064) → [`005dc094`](#insn-005dc094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc06c`](#insn-005dc06c) → [`005dc094`](#insn-005dc094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc070`](#insn-005dc070) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`005dc07c`](#insn-005dc07c) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`005dc084`](#insn-005dc084) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc088`](#insn-005dc088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc08c`](#insn-005dc08c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc090`](#insn-005dc090) → [`008b91d0`](../008b9/008b91d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b91d0` · 推定シンボル `None` · 推定型 `None`
- [`005dc094`](#insn-005dc094) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc098`](#insn-005dc098) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dc09c`](#insn-005dc09c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005dbfbc`](#insn-005dbfbc)

~~~json
{
  "source": "005dbfbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dbfc0`](#insn-005dbfc0)

~~~json
{
  "source": "005dbfc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dbfc4`](#insn-005dbfc4)

~~~json
{
  "source": "005dbfc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dbfdc`](#insn-005dbfdc)

~~~json
{
  "source": "005dbfdc",
  "target": "005dc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dbfe0`](#insn-005dbfe0)

~~~json
{
  "source": "005dbfe0",
  "target": "005dc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dbfec`](#insn-005dbfec)

~~~json
{
  "source": "005dbfec",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dbffc`](#insn-005dbffc)

~~~json
{
  "source": "005dbffc",
  "target": "00b3bfbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc000`](#insn-005dc000)

~~~json
{
  "source": "005dc000",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc028`](#insn-005dc028)

~~~json
{
  "source": "005dc028",
  "target": "00687ee4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc02c`](#insn-005dc02c)

~~~json
{
  "source": "005dc02c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc040`](#insn-005dc040)

~~~json
{
  "source": "005dc040",
  "target": "00689994",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc044`](#insn-005dc044)

~~~json
{
  "source": "005dc044",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc048`](#insn-005dc048)

~~~json
{
  "source": "005dc048",
  "target": "00a1a6f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc04c`](#insn-005dc04c)

~~~json
{
  "source": "005dc04c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc058`](#insn-005dc058)

~~~json
{
  "source": "005dc058",
  "target": "0042ec00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0042ebdd",
  "offset": 35,
  "size": 59,
  "datatype": "byte[59]",
  "bytes": "440e8001540c1d289302940495069e089d0a05480c0a680c1f8001540e00d3d4",
  "capture_start": "0042ebdd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`005dc05c`](#insn-005dc05c)

~~~json
{
  "source": "005dc05c",
  "target": "005dc070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc064`](#insn-005dc064)

~~~json
{
  "source": "005dc064",
  "target": "005dc094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc06c`](#insn-005dc06c)

~~~json
{
  "source": "005dc06c",
  "target": "005dc094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc070`](#insn-005dc070)

~~~json
{
  "source": "005dc070",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc07c`](#insn-005dc07c)

~~~json
{
  "source": "005dc07c",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc084`](#insn-005dc084)

~~~json
{
  "source": "005dc084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc088`](#insn-005dc088)

~~~json
{
  "source": "005dc088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc08c`](#insn-005dc08c)

~~~json
{
  "source": "005dc08c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc090`](#insn-005dc090)

~~~json
{
  "source": "005dc090",
  "target": "008b91d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dc094`](#insn-005dc094)

~~~json
{
  "source": "005dc094",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc098`](#insn-005dc098)

~~~json
{
  "source": "005dc098",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dc09c`](#insn-005dc09c)

~~~json
{
  "source": "005dc09c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
