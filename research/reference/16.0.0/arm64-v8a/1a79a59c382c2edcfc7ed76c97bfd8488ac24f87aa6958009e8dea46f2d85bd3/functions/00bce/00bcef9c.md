# 00bcef9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5fa9c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-8f11c7eb64d4c25042d9c286d07daaa5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcf3c4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf3c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-6a5a4b45c96dec9ed8b0b919ab91d43e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcef9c",
  "name": "_ZN8firebase4auth4Auth14UseAppLanguageEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11",
  "source_text_sha256": "67526a7909c327e15ebe1e116e5b7fd827281f1a09e9a47c887418c4b5300b11",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcef9c",
        "00bcefef"
      ]
    ],
    "bytes_sha256": "c1a7f2499df7c4da60a32d8bd38f197a4eea58d1c274088f1c97f6233e74f725",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 643 bytes

~~~c

void _ZN8firebase4auth4Auth14UseAppLanguageEv(long *param_1)

{
  undefined8 uVar1;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
                    /* try { // try from 00bcefbc to 00ccf247 has its CatchHandler @ 00bcefbc
                       catch() { ... } // from try @ 00bcefbc with catch @ 00bcefbc
                       catch() { ... } // from try @ 00bcf250 with catch @ 00bcefbc */
    FUN_00574cac(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126358);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcef9c"></a> `00bcef9c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcefa0"></a> `00bcefa0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcefa4"></a> `00bcefa4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcefa8"></a> `00bcefa8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcefac"></a> `00bcefac` | `c8 01 00 b4` | cbz x8,0x00bcefe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcefb0"></a> `00bcefb0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcefb4"></a> `00bcefb4` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcefb8"></a> `00bcefb8` | `32 2f 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcefbc"></a> `00bcefbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcefc0"></a> `00bcefc0` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcefc4"></a> `00bcefc4` | `22 ad 41 f9` | ldr x2,[x9, #0x358] | `FALL_THROUGH`
<a id="insn-00bcefc8"></a> `00bcefc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcefcc"></a> `00bcefcc` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcefd0"></a> `00bcefd0` | `37 97 e6 97` | bl 0x00574cac | `UNCONDITIONAL_CALL`
<a id="insn-00bcefd4"></a> `00bcefd4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcefd8"></a> `00bcefd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcefdc"></a> `00bcefdc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcefe0"></a> `00bcefe0` | `e0 2e 02 14` | b 0x00c5ab60 | `CALL_TERMINATOR`
<a id="insn-00bcefe4"></a> `00bcefe4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcefe8"></a> `00bcefe8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcefec"></a> `00bcefec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcef9c`](#insn-00bcef9c) 範囲 `[['00bcef9c', '00bcefaf']]`
  - `CONDITIONAL_JUMP` [`00bcefac`](#insn-00bcefac) → [`00bcefe4`](#insn-00bcefe4)
  - `FALL_THROUGH` [`00bcefac`](#insn-00bcefac) → [`00bcefb0`](#insn-00bcefb0)
- ブロック [`00bcefb0`](#insn-00bcefb0) 範囲 `[['00bcefb0', '00bcefbb']]`
  - `FALL_THROUGH` [`00bcefb8`](#insn-00bcefb8) → [`00bcefbc`](#insn-00bcefbc)
- ブロック [`00bcefbc`](#insn-00bcefbc) 範囲 `[['00bcefbc', '00bcefe3']]`
- ブロック [`00bcefe4`](#insn-00bcefe4) 範囲 `[['00bcefe4', '00bcefef']]`

## 命令位置別の参照

- [`00bcef9c`](#insn-00bcef9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefa0`](#insn-00bcefa0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefac`](#insn-00bcefac) → [`00bcefe4`](#insn-00bcefe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefb8`](#insn-00bcefb8) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcefc4`](#insn-00bcefc4) → `01126358`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcefd0`](#insn-00bcefd0) → [`00574cac`](../00574/00574cac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cac` · 推定シンボル `None` · 推定型 `None`
- [`00bcefd4`](#insn-00bcefd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcefe0`](#insn-00bcefe0) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcefe4`](#insn-00bcefe4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcef9c`](#insn-00bcef9c)

~~~json
{
  "source": "00bcef9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefa0`](#insn-00bcefa0)

~~~json
{
  "source": "00bcefa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefac`](#insn-00bcefac)

~~~json
{
  "source": "00bcefac",
  "target": "00bcefe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefb8`](#insn-00bcefb8)

~~~json
{
  "source": "00bcefb8",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefc4`](#insn-00bcefc4)

~~~json
{
  "source": "00bcefc4",
  "target": "01126358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126358",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcefd0`](#insn-00bcefd0)

~~~json
{
  "source": "00bcefd0",
  "target": "00574cac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefd4`](#insn-00bcefd4)

~~~json
{
  "source": "00bcefd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcefe0`](#insn-00bcefe0)

~~~json
{
  "source": "00bcefe0",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcefe4`](#insn-00bcefe4)

~~~json
{
  "source": "00bcefe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
