# 00bdf4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdf0b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-d6250dc506d099154ee6c20927eec39b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdf578`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-3a6bfb742a991cefd3e58dcda6e20787)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf4dc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a8567ffe22efd1f1cbc03976c15276957a74a64ce119b98277349c2579e5239",
  "source_text_sha256": "8a8567ffe22efd1f1cbc03976c15276957a74a64ce119b98277349c2579e5239",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf4dc",
        "00bdf55f"
      ]
    ],
    "bytes_sha256": "f1488cc36f325cdb39da2479794fce050560e9ccb86b826ba2b717f45ce48173",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b390](../00c5b/00c5b390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 749 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_00497834(uVar2,lVar1,DAT_01126dd0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
                    /* try { // try from 00bdf524 to 00cdf577 has its CatchHandler @ 00be07b4 */
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf4dc"></a> `00bdf4dc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdf4e0"></a> `00bdf4e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf4e4"></a> `00bdf4e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf4e8"></a> `00bdf4e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf4ec"></a> `00bdf4ec` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf4f0"></a> `00bdf4f0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdf4f4"></a> `00bdf4f4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdf4f8"></a> `00bdf4f8` | `e2 ee 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf4fc"></a> `00bdf4fc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdf500"></a> `00bdf500` | `f5 00 00 b4` | cbz x21,0x00bdf51c | `CONDITIONAL_JUMP`
<a id="insn-00bdf504"></a> `00bdf504` | `28 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdf508"></a> `00bdf508` | `02 e9 46 f9` | ldr x2,[x8, #0xdd0] | `FALL_THROUGH`
<a id="insn-00bdf50c"></a> `00bdf50c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf510"></a> `00bdf510` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf514"></a> `00bdf514` | `c8 e0 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf518"></a> `00bdf518` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdf51c"></a> `00bdf51c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf520"></a> `00bdf520` | `90 ee 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf524"></a> `00bdf524` | `35 01 00 b4` | cbz x21,0x00bdf548 | `CONDITIONAL_JUMP`
<a id="insn-00bdf528"></a> `00bdf528` | `00 01 00 37` | tbnz w0,#0x0,0x00bdf548 | `CONDITIONAL_JUMP`
<a id="insn-00bdf52c"></a> `00bdf52c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bdf530"></a> `00bdf530` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf534"></a> `00bdf534` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf538"></a> `00bdf538` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf53c"></a> `00bdf53c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf540"></a> `00bdf540` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf544"></a> `00bdf544` | `93 ef 01 14` | b 0x00c5b390 | `CALL_TERMINATOR`
<a id="insn-00bdf548"></a> `00bdf548` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdf54c"></a> `00bdf54c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf550"></a> `00bdf550` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf554"></a> `00bdf554` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf558"></a> `00bdf558` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf55c"></a> `00bdf55c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf4dc`](#insn-00bdf4dc) 範囲 `[['00bdf4dc', '00bdf503']]`
  - `CONDITIONAL_JUMP` [`00bdf500`](#insn-00bdf500) → [`00bdf51c`](#insn-00bdf51c)
  - `FALL_THROUGH` [`00bdf500`](#insn-00bdf500) → [`00bdf504`](#insn-00bdf504)
- ブロック [`00bdf504`](#insn-00bdf504) 範囲 `[['00bdf504', '00bdf51b']]`
  - `FALL_THROUGH` [`00bdf518`](#insn-00bdf518) → [`00bdf51c`](#insn-00bdf51c)
- ブロック [`00bdf51c`](#insn-00bdf51c) 範囲 `[['00bdf51c', '00bdf523']]`
  - `FALL_THROUGH` [`00bdf520`](#insn-00bdf520) → [`00bdf524`](#insn-00bdf524)
- ブロック [`00bdf524`](#insn-00bdf524) 範囲 `[['00bdf524', '00bdf527']]`
  - `CONDITIONAL_JUMP` [`00bdf524`](#insn-00bdf524) → [`00bdf548`](#insn-00bdf548)
  - `FALL_THROUGH` [`00bdf524`](#insn-00bdf524) → [`00bdf528`](#insn-00bdf528)
- ブロック [`00bdf528`](#insn-00bdf528) 範囲 `[['00bdf528', '00bdf52b']]`
  - `CONDITIONAL_JUMP` [`00bdf528`](#insn-00bdf528) → [`00bdf548`](#insn-00bdf548)
  - `FALL_THROUGH` [`00bdf528`](#insn-00bdf528) → [`00bdf52c`](#insn-00bdf52c)
- ブロック [`00bdf52c`](#insn-00bdf52c) 範囲 `[['00bdf52c', '00bdf547']]`
- ブロック [`00bdf548`](#insn-00bdf548) 範囲 `[['00bdf548', '00bdf55f']]`

## 命令位置別の参照

- [`00bdf4dc`](#insn-00bdf4dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf4e0`](#insn-00bdf4e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf4e4`](#insn-00bdf4e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf4f8`](#insn-00bdf4f8) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdf500`](#insn-00bdf500) → [`00bdf51c`](#insn-00bdf51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf508`](#insn-00bdf508) → `01126dd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf514`](#insn-00bdf514) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdf520`](#insn-00bdf520) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf524`](#insn-00bdf524) → [`00bdf548`](#insn-00bdf548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf528`](#insn-00bdf528) → [`00bdf548`](#insn-00bdf548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf534`](#insn-00bdf534) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf538`](#insn-00bdf538) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf544`](#insn-00bdf544) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bdf550`](#insn-00bdf550) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf554`](#insn-00bdf554) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf4dc`](#insn-00bdf4dc)

~~~json
{
  "source": "00bdf4dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf4e0`](#insn-00bdf4e0)

~~~json
{
  "source": "00bdf4e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf4e4`](#insn-00bdf4e4)

~~~json
{
  "source": "00bdf4e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf4f8`](#insn-00bdf4f8)

~~~json
{
  "source": "00bdf4f8",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf500`](#insn-00bdf500)

~~~json
{
  "source": "00bdf500",
  "target": "00bdf51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf508`](#insn-00bdf508)

~~~json
{
  "source": "00bdf508",
  "target": "01126dd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf514`](#insn-00bdf514)

~~~json
{
  "source": "00bdf514",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf520`](#insn-00bdf520)

~~~json
{
  "source": "00bdf520",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf524`](#insn-00bdf524)

~~~json
{
  "source": "00bdf524",
  "target": "00bdf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf528`](#insn-00bdf528)

~~~json
{
  "source": "00bdf528",
  "target": "00bdf548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf534`](#insn-00bdf534)

~~~json
{
  "source": "00bdf534",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf538`](#insn-00bdf538)

~~~json
{
  "source": "00bdf538",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf544`](#insn-00bdf544)

~~~json
{
  "source": "00bdf544",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf550`](#insn-00bdf550)

~~~json
{
  "source": "00bdf550",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf554`](#insn-00bdf554)

~~~json
{
  "source": "00bdf554",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
