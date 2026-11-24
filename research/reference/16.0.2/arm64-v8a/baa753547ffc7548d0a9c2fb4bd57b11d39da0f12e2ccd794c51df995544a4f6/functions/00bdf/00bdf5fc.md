# 00bdf5fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdf560`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf560.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-3c712e915c65fcc3fa169427517ad19c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00be05f0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-633f29d6f7bcd9cfe2610f5ee3181bde)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf5fc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa0ffd51eb1094443e8b62212aa80d2183d3f25358881ec0a062fe78dec6aa94",
  "source_text_sha256": "fa0ffd51eb1094443e8b62212aa80d2183d3f25358881ec0a062fe78dec6aa94",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf5fc",
        "00bdf67f"
      ]
    ],
    "bytes_sha256": "f66da8105c4987d759a9a2bcc231ece0af77d0af169a494871a3ef0260c75838",
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

- [00497874](../00497/00497874.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b3c0](../00c5b/00c5b3c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 936 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
                    /* try { // try from 00bdf610 to 00cdf61f has its CatchHandler @ 00be084c */
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
                    /* try { // try from 00bdf628 to 00cdf66b has its CatchHandler @ 00be0858 */
    lVar3 = FUN_00497874(uVar2,lVar1,DAT_01126ee0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00bdf674 to 00cdf677 has its CatchHandler @ 00be07dc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf5fc"></a> `00bdf5fc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdf600"></a> `00bdf600` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf604"></a> `00bdf604` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf608"></a> `00bdf608` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf60c"></a> `00bdf60c` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf610"></a> `00bdf610` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdf614"></a> `00bdf614` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdf618"></a> `00bdf618` | `ce ee 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf61c"></a> `00bdf61c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdf620"></a> `00bdf620` | `f5 00 00 b4` | cbz x21,0x00bdf63c | `CONDITIONAL_JUMP`
<a id="insn-00bdf624"></a> `00bdf624` | `28 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdf628"></a> `00bdf628` | `02 71 47 f9` | ldr x2,[x8, #0xee0] | `FALL_THROUGH`
<a id="insn-00bdf62c"></a> `00bdf62c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf630"></a> `00bdf630` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf634"></a> `00bdf634` | `90 e0 e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf638"></a> `00bdf638` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdf63c"></a> `00bdf63c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf640"></a> `00bdf640` | `7c ee 01 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf644"></a> `00bdf644` | `35 01 00 b4` | cbz x21,0x00bdf668 | `CONDITIONAL_JUMP`
<a id="insn-00bdf648"></a> `00bdf648` | `00 01 00 37` | tbnz w0,#0x0,0x00bdf668 | `CONDITIONAL_JUMP`
<a id="insn-00bdf64c"></a> `00bdf64c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bdf650"></a> `00bdf650` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf654"></a> `00bdf654` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf658"></a> `00bdf658` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf65c"></a> `00bdf65c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf660"></a> `00bdf660` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf664"></a> `00bdf664` | `57 ef 01 14` | b 0x00c5b3c0 | `CALL_TERMINATOR`
<a id="insn-00bdf668"></a> `00bdf668` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdf66c"></a> `00bdf66c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf670"></a> `00bdf670` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf674"></a> `00bdf674` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf678"></a> `00bdf678` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf67c"></a> `00bdf67c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf5fc`](#insn-00bdf5fc) 範囲 `[['00bdf5fc', '00bdf60f']]`
  - `FALL_THROUGH` [`00bdf60c`](#insn-00bdf60c) → [`00bdf610`](#insn-00bdf610)
- ブロック [`00bdf610`](#insn-00bdf610) 範囲 `[['00bdf610', '00bdf623']]`
  - `CONDITIONAL_JUMP` [`00bdf620`](#insn-00bdf620) → [`00bdf63c`](#insn-00bdf63c)
  - `FALL_THROUGH` [`00bdf620`](#insn-00bdf620) → [`00bdf624`](#insn-00bdf624)
- ブロック [`00bdf624`](#insn-00bdf624) 範囲 `[['00bdf624', '00bdf627']]`
  - `FALL_THROUGH` [`00bdf624`](#insn-00bdf624) → [`00bdf628`](#insn-00bdf628)
- ブロック [`00bdf628`](#insn-00bdf628) 範囲 `[['00bdf628', '00bdf63b']]`
  - `FALL_THROUGH` [`00bdf638`](#insn-00bdf638) → [`00bdf63c`](#insn-00bdf63c)
- ブロック [`00bdf63c`](#insn-00bdf63c) 範囲 `[['00bdf63c', '00bdf647']]`
  - `CONDITIONAL_JUMP` [`00bdf644`](#insn-00bdf644) → [`00bdf668`](#insn-00bdf668)
  - `FALL_THROUGH` [`00bdf644`](#insn-00bdf644) → [`00bdf648`](#insn-00bdf648)
- ブロック [`00bdf648`](#insn-00bdf648) 範囲 `[['00bdf648', '00bdf64b']]`
  - `CONDITIONAL_JUMP` [`00bdf648`](#insn-00bdf648) → [`00bdf668`](#insn-00bdf668)
  - `FALL_THROUGH` [`00bdf648`](#insn-00bdf648) → [`00bdf64c`](#insn-00bdf64c)
- ブロック [`00bdf64c`](#insn-00bdf64c) 範囲 `[['00bdf64c', '00bdf667']]`
- ブロック [`00bdf668`](#insn-00bdf668) 範囲 `[['00bdf668', '00bdf673']]`
  - `FALL_THROUGH` [`00bdf670`](#insn-00bdf670) → [`00bdf674`](#insn-00bdf674)
- ブロック [`00bdf674`](#insn-00bdf674) 範囲 `[['00bdf674', '00bdf67f']]`

## 命令位置別の参照

- [`00bdf5fc`](#insn-00bdf5fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf600`](#insn-00bdf600) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf604`](#insn-00bdf604) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf618`](#insn-00bdf618) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdf620`](#insn-00bdf620) → [`00bdf63c`](#insn-00bdf63c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf628`](#insn-00bdf628) → `01126ee0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf634`](#insn-00bdf634) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdf640`](#insn-00bdf640) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bdf644`](#insn-00bdf644) → [`00bdf668`](#insn-00bdf668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf648`](#insn-00bdf648) → [`00bdf668`](#insn-00bdf668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf654`](#insn-00bdf654) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf658`](#insn-00bdf658) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf664`](#insn-00bdf664) → [`00c5b3c0`](../00c5b/00c5b3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b3c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf670`](#insn-00bdf670) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf674`](#insn-00bdf674) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf5fc`](#insn-00bdf5fc)

~~~json
{
  "source": "00bdf5fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf600`](#insn-00bdf600)

~~~json
{
  "source": "00bdf600",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf604`](#insn-00bdf604)

~~~json
{
  "source": "00bdf604",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf618`](#insn-00bdf618)

~~~json
{
  "source": "00bdf618",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf620`](#insn-00bdf620)

~~~json
{
  "source": "00bdf620",
  "target": "00bdf63c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf628`](#insn-00bdf628)

~~~json
{
  "source": "00bdf628",
  "target": "01126ee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf634`](#insn-00bdf634)

~~~json
{
  "source": "00bdf634",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf640`](#insn-00bdf640)

~~~json
{
  "source": "00bdf640",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf644`](#insn-00bdf644)

~~~json
{
  "source": "00bdf644",
  "target": "00bdf668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf648`](#insn-00bdf648)

~~~json
{
  "source": "00bdf648",
  "target": "00bdf668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf654`](#insn-00bdf654)

~~~json
{
  "source": "00bdf654",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf658`](#insn-00bdf658)

~~~json
{
  "source": "00bdf658",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf664`](#insn-00bdf664)

~~~json
{
  "source": "00bdf664",
  "target": "00c5b3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf670`](#insn-00bdf670)

~~~json
{
  "source": "00bdf670",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf674`](#insn-00bdf674)

~~~json
{
  "source": "00bdf674",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
