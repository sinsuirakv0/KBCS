# 00b6fcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6fc78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fc78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-93c0d9406073c39e9774e43a9b84991d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdf1bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf1bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-3bd111fffbc00e18c1c1ccd1708ce38c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6fcbc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf903f4b9183506ada4d07c99f7710de6de8606709ac6038bac385575aabd7d8",
  "source_text_sha256": "bf903f4b9183506ada4d07c99f7710de6de8606709ac6038bac385575aabd7d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6fcbc",
        "00b6fd3f"
      ]
    ],
    "bytes_sha256": "d43b2e578553f3135c687a63ef31f266307bacd44a85bd94ccaf4f921ec3cd9e",
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

- [0047495c](../00474/0047495c.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde510](../00bde/00bde510.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 942 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
                    /* try { // try from 00b6fcd8 to 00c6fcf7 has its CatchHandler @ 00b70738 */
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1ac0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
                    /* try { // try from 00b6fd04 to 00c6fd23 has its CatchHandler @ 00b70728 */
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
                    /* try { // try from 00b6fd24 to 00c6fdb7 has its CatchHandler @ 00b6e440 */
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
<a id="insn-00b6fcbc"></a> `00b6fcbc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6fcc0"></a> `00b6fcc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fcc4"></a> `00b6fcc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fcc8"></a> `00b6fcc8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6fccc"></a> `00b6fccc` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6fcd0"></a> `00b6fcd0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6fcd4"></a> `00b6fcd4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6fcd8"></a> `00b6fcd8` | `4a b9 01 94` | bl 0x00bde200 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fcdc"></a> `00b6fcdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6fce0"></a> `00b6fce0` | `f5 00 00 b4` | cbz x21,0x00b6fcfc | `CONDITIONAL_JUMP`
<a id="insn-00b6fce4"></a> `00b6fce4` | `88 29 00 d0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6fce8"></a> `00b6fce8` | `02 61 45 f9` | ldr x2,[x8, #0xac0] | `FALL_THROUGH`
<a id="insn-00b6fcec"></a> `00b6fcec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fcf0"></a> `00b6fcf0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fcf4"></a> `00b6fcf4` | `1a 13 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6fcf8"></a> `00b6fcf8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6fcfc"></a> `00b6fcfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fd00"></a> `00b6fd00` | `f8 b8 01 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fd04"></a> `00b6fd04` | `35 01 00 b4` | cbz x21,0x00b6fd28 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd08"></a> `00b6fd08` | `00 01 00 37` | tbnz w0,#0x0,0x00b6fd28 | `CONDITIONAL_JUMP`
<a id="insn-00b6fd0c"></a> `00b6fd0c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6fd10"></a> `00b6fd10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fd14"></a> `00b6fd14` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fd18"></a> `00b6fd18` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd1c"></a> `00b6fd1c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fd20"></a> `00b6fd20` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fd24"></a> `00b6fd24` | `fb b9 01 14` | b 0x00bde510 | `CALL_TERMINATOR`
<a id="insn-00b6fd28"></a> `00b6fd28` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6fd2c"></a> `00b6fd2c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd30"></a> `00b6fd30` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fd34"></a> `00b6fd34` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fd38"></a> `00b6fd38` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fd3c"></a> `00b6fd3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6fcbc`](#insn-00b6fcbc) 範囲 `[['00b6fcbc', '00b6fcd7']]`
  - `FALL_THROUGH` [`00b6fcd4`](#insn-00b6fcd4) → [`00b6fcd8`](#insn-00b6fcd8)
- ブロック [`00b6fcd8`](#insn-00b6fcd8) 範囲 `[['00b6fcd8', '00b6fce3']]`
  - `CONDITIONAL_JUMP` [`00b6fce0`](#insn-00b6fce0) → [`00b6fcfc`](#insn-00b6fcfc)
  - `FALL_THROUGH` [`00b6fce0`](#insn-00b6fce0) → [`00b6fce4`](#insn-00b6fce4)
- ブロック [`00b6fce4`](#insn-00b6fce4) 範囲 `[['00b6fce4', '00b6fcfb']]`
  - `FALL_THROUGH` [`00b6fcf8`](#insn-00b6fcf8) → [`00b6fcfc`](#insn-00b6fcfc)
- ブロック [`00b6fcfc`](#insn-00b6fcfc) 範囲 `[['00b6fcfc', '00b6fd03']]`
  - `FALL_THROUGH` [`00b6fd00`](#insn-00b6fd00) → [`00b6fd04`](#insn-00b6fd04)
- ブロック [`00b6fd04`](#insn-00b6fd04) 範囲 `[['00b6fd04', '00b6fd07']]`
  - `CONDITIONAL_JUMP` [`00b6fd04`](#insn-00b6fd04) → [`00b6fd28`](#insn-00b6fd28)
  - `FALL_THROUGH` [`00b6fd04`](#insn-00b6fd04) → [`00b6fd08`](#insn-00b6fd08)
- ブロック [`00b6fd08`](#insn-00b6fd08) 範囲 `[['00b6fd08', '00b6fd0b']]`
  - `CONDITIONAL_JUMP` [`00b6fd08`](#insn-00b6fd08) → [`00b6fd28`](#insn-00b6fd28)
  - `FALL_THROUGH` [`00b6fd08`](#insn-00b6fd08) → [`00b6fd0c`](#insn-00b6fd0c)
- ブロック [`00b6fd0c`](#insn-00b6fd0c) 範囲 `[['00b6fd0c', '00b6fd23']]`
  - `FALL_THROUGH` [`00b6fd20`](#insn-00b6fd20) → [`00b6fd24`](#insn-00b6fd24)
- ブロック [`00b6fd24`](#insn-00b6fd24) 範囲 `[['00b6fd24', '00b6fd27']]`
- ブロック [`00b6fd28`](#insn-00b6fd28) 範囲 `[['00b6fd28', '00b6fd3f']]`

## 命令位置別の参照

- [`00b6fcbc`](#insn-00b6fcbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcc0`](#insn-00b6fcc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcc4`](#insn-00b6fcc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fcd8`](#insn-00b6fcd8) → [`00bde200`](../00bde/00bde200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde200` · 推定シンボル `None` · 推定型 `None`
- [`00b6fce0`](#insn-00b6fce0) → [`00b6fcfc`](#insn-00b6fcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fce8`](#insn-00b6fce8) → `010a1ac0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6fcf4`](#insn-00b6fcf4) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd00`](#insn-00b6fd00) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd04`](#insn-00b6fd04) → [`00b6fd28`](#insn-00b6fd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd08`](#insn-00b6fd08) → [`00b6fd28`](#insn-00b6fd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd14`](#insn-00b6fd14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd18`](#insn-00b6fd18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd24`](#insn-00b6fd24) → [`00bde510`](../00bde/00bde510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde510` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd30`](#insn-00b6fd30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fd34`](#insn-00b6fd34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6fcbc`](#insn-00b6fcbc)

~~~json
{
  "source": "00b6fcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcc0`](#insn-00b6fcc0)

~~~json
{
  "source": "00b6fcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcc4`](#insn-00b6fcc4)

~~~json
{
  "source": "00b6fcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fcd8`](#insn-00b6fcd8)

~~~json
{
  "source": "00b6fcd8",
  "target": "00bde200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fce0`](#insn-00b6fce0)

~~~json
{
  "source": "00b6fce0",
  "target": "00b6fcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fce8`](#insn-00b6fce8)

~~~json
{
  "source": "00b6fce8",
  "target": "010a1ac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1ac0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6fcf4`](#insn-00b6fcf4)

~~~json
{
  "source": "00b6fcf4",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd00`](#insn-00b6fd00)

~~~json
{
  "source": "00b6fd00",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd04`](#insn-00b6fd04)

~~~json
{
  "source": "00b6fd04",
  "target": "00b6fd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd08`](#insn-00b6fd08)

~~~json
{
  "source": "00b6fd08",
  "target": "00b6fd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd14`](#insn-00b6fd14)

~~~json
{
  "source": "00b6fd14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd18`](#insn-00b6fd18)

~~~json
{
  "source": "00b6fd18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd24`](#insn-00b6fd24)

~~~json
{
  "source": "00b6fd24",
  "target": "00bde510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fd30`](#insn-00b6fd30)

~~~json
{
  "source": "00b6fd30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fd34`](#insn-00b6fd34)

~~~json
{
  "source": "00b6fd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
