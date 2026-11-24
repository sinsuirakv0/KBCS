# 009ebedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0155.md#review-dde020b29e3d1b8841a7a2c26eaa931e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009ec078`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec078.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0033.md#compare-9772687418b5645080fc006d41b7a313)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009ebedc",
  "name": "FUN_009ebedc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "500354848f4eb5220cf1801b8e18c6aa51ce1131b666325a5b54829a62efcf2d",
  "source_text_sha256": "500354848f4eb5220cf1801b8e18c6aa51ce1131b666325a5b54829a62efcf2d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009ebedc",
        "009ebf23"
      ]
    ],
    "bytes_sha256": "84a9d7d280610155899a04f3a4feb10d63d0a6d014451e63bd6010c4b8d14426",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009eade8](../009ea/009eade8.md)

## 呼び出し先

- [009f2cc8](../009f2/009f2cc8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 666 bytes

~~~c

void FUN_009ebedc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  
                    /* try { // try from 009ebedc to 00aebeeb has its CatchHandler @ 009ebf90 */
                    /* try { // try from 009ebeec to 00aec02f has its CatchHandler @ 009ebe14 */
  puVar1 = *(undefined8 **)(param_1 + 8);
  if (puVar1 < *(undefined8 **)(param_1 + 0x10)) {
    uVar3 = *param_2;
    puVar2 = puVar1 + 2;
    puVar1[1] = param_2[1];
    *puVar1 = uVar3;
    *param_2 = 0;
    param_2[1] = 0;
  }
  else {
    puVar2 = (undefined8 *)FUN_009f2cc8(param_1);
  }
  *(undefined8 **)(param_1 + 8) = puVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009ebedc"></a> `009ebedc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009ebee0"></a> `009ebee0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ebee4"></a> `009ebee4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009ebee8"></a> `009ebee8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009ebeec"></a> `009ebeec` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009ebef0"></a> `009ebef0` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-009ebef4"></a> `009ebef4` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-009ebef8"></a> `009ebef8` | `a2 00 00 54` | b.cs 0x009ebf0c | `CONDITIONAL_JUMP`
<a id="insn-009ebefc"></a> `009ebefc` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-009ebf00"></a> `009ebf00` | `00 04 81 3c` | str q0,[x0], #0x10 | `FALL_THROUGH`
<a id="insn-009ebf04"></a> `009ebf04` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-009ebf08"></a> `009ebf08` | `03 00 00 14` | b 0x009ebf14 | `UNCONDITIONAL_JUMP`
<a id="insn-009ebf0c"></a> `009ebf0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009ebf10"></a> `009ebf10` | `6e 1b 00 94` | bl 0x009f2cc8 | `UNCONDITIONAL_CALL`
<a id="insn-009ebf14"></a> `009ebf14` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-009ebf18"></a> `009ebf18` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009ebf1c"></a> `009ebf1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009ebf20"></a> `009ebf20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009ebedc`](#insn-009ebedc) 範囲 `[['009ebedc', '009ebeeb']]`
  - `FALL_THROUGH` [`009ebee8`](#insn-009ebee8) → [`009ebeec`](#insn-009ebeec)
- ブロック [`009ebeec`](#insn-009ebeec) 範囲 `[['009ebeec', '009ebefb']]`
  - `CONDITIONAL_JUMP` [`009ebef8`](#insn-009ebef8) → [`009ebf0c`](#insn-009ebf0c)
  - `FALL_THROUGH` [`009ebef8`](#insn-009ebef8) → [`009ebefc`](#insn-009ebefc)
- ブロック [`009ebefc`](#insn-009ebefc) 範囲 `[['009ebefc', '009ebf0b']]`
  - `UNCONDITIONAL_JUMP` [`009ebf08`](#insn-009ebf08) → [`009ebf14`](#insn-009ebf14)
- ブロック [`009ebf0c`](#insn-009ebf0c) 範囲 `[['009ebf0c', '009ebf13']]`
  - `FALL_THROUGH` [`009ebf10`](#insn-009ebf10) → [`009ebf14`](#insn-009ebf14)
- ブロック [`009ebf14`](#insn-009ebf14) 範囲 `[['009ebf14', '009ebf23']]`

## 命令位置別の参照

- [`009ebedc`](#insn-009ebedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ebee0`](#insn-009ebee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ebef8`](#insn-009ebef8) → [`009ebf0c`](#insn-009ebf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ebf08`](#insn-009ebf08) → [`009ebf14`](#insn-009ebf14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ebf10`](#insn-009ebf10) → [`009f2cc8`](../009f2/009f2cc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009f2cc8` · 推定シンボル `None` · 推定型 `None`
- [`009ebf18`](#insn-009ebf18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ebf1c`](#insn-009ebf1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009ebedc`](#insn-009ebedc)

~~~json
{
  "source": "009ebedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ebee0`](#insn-009ebee0)

~~~json
{
  "source": "009ebee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ebef8`](#insn-009ebef8)

~~~json
{
  "source": "009ebef8",
  "target": "009ebf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ebf08`](#insn-009ebf08)

~~~json
{
  "source": "009ebf08",
  "target": "009ebf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ebf10`](#insn-009ebf10)

~~~json
{
  "source": "009ebf10",
  "target": "009f2cc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ebf18`](#insn-009ebf18)

~~~json
{
  "source": "009ebf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ebf1c`](#insn-009ebf1c)

~~~json
{
  "source": "009ebf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
