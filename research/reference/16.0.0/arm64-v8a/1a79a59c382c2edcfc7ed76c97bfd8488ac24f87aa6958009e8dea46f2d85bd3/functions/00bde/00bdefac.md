# 00bdefac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6faac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6faac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-7adb0be130d35614ea771180ecd9230c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdf3d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf3d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-b264ef7d15a96ecdfa96f351d3cb5a7f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefac",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ce09066525025cec485d27dd2da9dfc8a3ff2f0aaea386735eac552552976bc",
  "source_text_sha256": "0ce09066525025cec485d27dd2da9dfc8a3ff2f0aaea386735eac552552976bc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefac",
        "00bdf02f"
      ]
    ],
    "bytes_sha256": "b6765de85160027c7f2271c9567840d136401079bf9d85b7a821af474a1a8ce1",
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

- [004977f4](../00497/004977f4.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_004977f4(uVar2,lVar1,DAT_011269c0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
                    /* try { // try from 00bdf01c to 00cdf0ab has its CatchHandler @ 00bdf01c
                       catch() { ... } // from try @ 00bdf01c with catch @ 00bdf01c
                       catch() { ... } // from try @ 00bdfeb0 with catch @ 00bdf01c
                       catch() { ... } // from try @ 00be0198 with catch @ 00bdf01c */
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefac"></a> `00bdefac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdefb0"></a> `00bdefb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdefb4"></a> `00bdefb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdefb8"></a> `00bdefb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdefbc"></a> `00bdefbc` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdefc0"></a> `00bdefc0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdefc4"></a> `00bdefc4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdefc8"></a> `00bdefc8` | `2e ef 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefcc"></a> `00bdefcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdefd0"></a> `00bdefd0` | `f5 00 00 b4` | cbz x21,0x00bdefec | `CONDITIONAL_JUMP`
<a id="insn-00bdefd4"></a> `00bdefd4` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdefd8"></a> `00bdefd8` | `02 e1 44 f9` | ldr x2,[x8, #0x9c0] | `FALL_THROUGH`
<a id="insn-00bdefdc"></a> `00bdefdc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdefe0"></a> `00bdefe0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdefe4"></a> `00bdefe4` | `04 e2 e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefe8"></a> `00bdefe8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdefec"></a> `00bdefec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdeff0"></a> `00bdeff0` | `dc ee 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeff4"></a> `00bdeff4` | `35 01 00 b4` | cbz x21,0x00bdf018 | `CONDITIONAL_JUMP`
<a id="insn-00bdeff8"></a> `00bdeff8` | `00 01 00 37` | tbnz w0,#0x0,0x00bdf018 | `CONDITIONAL_JUMP`
<a id="insn-00bdeffc"></a> `00bdeffc` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bdf000"></a> `00bdf000` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf004"></a> `00bdf004` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf008"></a> `00bdf008` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf00c"></a> `00bdf00c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf010"></a> `00bdf010` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf014"></a> `00bdf014` | `df ef 01 14` | b 0x00c5af90 | `CALL_TERMINATOR`
<a id="insn-00bdf018"></a> `00bdf018` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdf01c"></a> `00bdf01c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf020"></a> `00bdf020` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf024"></a> `00bdf024` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf028"></a> `00bdf028` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf02c"></a> `00bdf02c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefac`](#insn-00bdefac) 範囲 `[['00bdefac', '00bdefd3']]`
  - `CONDITIONAL_JUMP` [`00bdefd0`](#insn-00bdefd0) → [`00bdefec`](#insn-00bdefec)
  - `FALL_THROUGH` [`00bdefd0`](#insn-00bdefd0) → [`00bdefd4`](#insn-00bdefd4)
- ブロック [`00bdefd4`](#insn-00bdefd4) 範囲 `[['00bdefd4', '00bdefeb']]`
  - `FALL_THROUGH` [`00bdefe8`](#insn-00bdefe8) → [`00bdefec`](#insn-00bdefec)
- ブロック [`00bdefec`](#insn-00bdefec) 範囲 `[['00bdefec', '00bdeff7']]`
  - `CONDITIONAL_JUMP` [`00bdeff4`](#insn-00bdeff4) → [`00bdf018`](#insn-00bdf018)
  - `FALL_THROUGH` [`00bdeff4`](#insn-00bdeff4) → [`00bdeff8`](#insn-00bdeff8)
- ブロック [`00bdeff8`](#insn-00bdeff8) 範囲 `[['00bdeff8', '00bdeffb']]`
  - `CONDITIONAL_JUMP` [`00bdeff8`](#insn-00bdeff8) → [`00bdf018`](#insn-00bdf018)
  - `FALL_THROUGH` [`00bdeff8`](#insn-00bdeff8) → [`00bdeffc`](#insn-00bdeffc)
- ブロック [`00bdeffc`](#insn-00bdeffc) 範囲 `[['00bdeffc', '00bdf017']]`
- ブロック [`00bdf018`](#insn-00bdf018) 範囲 `[['00bdf018', '00bdf01b']]`
  - `FALL_THROUGH` [`00bdf018`](#insn-00bdf018) → [`00bdf01c`](#insn-00bdf01c)
- ブロック [`00bdf01c`](#insn-00bdf01c) 範囲 `[['00bdf01c', '00bdf02f']]`

## 命令位置別の参照

- [`00bdefac`](#insn-00bdefac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefb0`](#insn-00bdefb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefb4`](#insn-00bdefb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefc8`](#insn-00bdefc8) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdefd0`](#insn-00bdefd0) → [`00bdefec`](#insn-00bdefec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefd8`](#insn-00bdefd8) → `011269c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdefe4`](#insn-00bdefe4) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff0`](#insn-00bdeff0) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff4`](#insn-00bdeff4) → [`00bdf018`](#insn-00bdf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff8`](#insn-00bdeff8) → [`00bdf018`](#insn-00bdf018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf004`](#insn-00bdf004) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf008`](#insn-00bdf008) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf014`](#insn-00bdf014) → [`00c5af90`](../00c5a/00c5af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af90` · 推定シンボル `None` · 推定型 `None`
- [`00bdf020`](#insn-00bdf020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf024`](#insn-00bdf024) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefac`](#insn-00bdefac)

~~~json
{
  "source": "00bdefac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefb0`](#insn-00bdefb0)

~~~json
{
  "source": "00bdefb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefb4`](#insn-00bdefb4)

~~~json
{
  "source": "00bdefb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefc8`](#insn-00bdefc8)

~~~json
{
  "source": "00bdefc8",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdefd0`](#insn-00bdefd0)

~~~json
{
  "source": "00bdefd0",
  "target": "00bdefec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefd8`](#insn-00bdefd8)

~~~json
{
  "source": "00bdefd8",
  "target": "011269c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdefe4`](#insn-00bdefe4)

~~~json
{
  "source": "00bdefe4",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeff0`](#insn-00bdeff0)

~~~json
{
  "source": "00bdeff0",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeff4`](#insn-00bdeff4)

~~~json
{
  "source": "00bdeff4",
  "target": "00bdf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeff8`](#insn-00bdeff8)

~~~json
{
  "source": "00bdeff8",
  "target": "00bdf018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf004`](#insn-00bdf004)

~~~json
{
  "source": "00bdf004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf008`](#insn-00bdf008)

~~~json
{
  "source": "00bdf008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf014`](#insn-00bdf014)

~~~json
{
  "source": "00bdf014",
  "target": "00c5af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf020`](#insn-00bdf020)

~~~json
{
  "source": "00bdf020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf024`](#insn-00bdf024)

~~~json
{
  "source": "00bdf024",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
