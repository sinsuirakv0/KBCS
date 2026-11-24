# 00af0abc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aefac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aef/00aefac8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-902659b7eb045df32f3541c9cde79c60)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0abc",
  "name": "FUN_00af0abc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b10d7c74d1f05181470338cea8b79af75ea853ab334c06ecfc0fcd45949fcdd8",
  "source_text_sha256": "b10d7c74d1f05181470338cea8b79af75ea853ab334c06ecfc0fcd45949fcdd8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af0abc",
        "00af0aeb"
      ]
    ],
    "bytes_sha256": "5b46c0952f8d8529fb88e54714a716655e30abee0df90e757fc560c1377da618",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b7a60](../008b7/008b7a60.md)
- [008b7f14](../008b7/008b7f14.md)
- [008b89cc](../008b8/008b89cc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 387 bytes

~~~c

void FUN_00af0abc(long param_1)

{
  undefined8 uVar1;
  
                    /* try { // try from 00af0ac8 to 00bf0acf has its CatchHandler @ 00af0dac */
                    /* try { // try from 00af0ad0 to 00bf0b47 has its CatchHandler @ 00af08e0 */
  uVar1 = FUN_008b89cc(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b7f14(uVar1,1);
  FUN_008b7a60(uVar1,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af0abc"></a> `00af0abc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00af0ac0"></a> `00af0ac0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af0ac4"></a> `00af0ac4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af0ac8"></a> `00af0ac8` | `09 e7 85 52` | mov w9,#0x2f38 | `FALL_THROUGH`
<a id="insn-00af0acc"></a> `00af0acc` | `c1 64 80 52` | mov w1,#0x326 | `FALL_THROUGH`
<a id="insn-00af0ad0"></a> `00af0ad0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af0ad4"></a> `00af0ad4` | `be 1f f7 97` | bl 0x008b89cc | `UNCONDITIONAL_CALL`
<a id="insn-00af0ad8"></a> `00af0ad8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00af0adc"></a> `00af0adc` | `0e 1d f7 97` | bl 0x008b7f14 | `UNCONDITIONAL_CALL`
<a id="insn-00af0ae0"></a> `00af0ae0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af0ae4"></a> `00af0ae4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00af0ae8"></a> `00af0ae8` | `de 1b f7 17` | b 0x008b7a60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af0abc`](#insn-00af0abc) 範囲 `[['00af0abc', '00af0ac7']]`
  - `FALL_THROUGH` [`00af0ac4`](#insn-00af0ac4) → [`00af0ac8`](#insn-00af0ac8)
- ブロック [`00af0ac8`](#insn-00af0ac8) 範囲 `[['00af0ac8', '00af0acf']]`
  - `FALL_THROUGH` [`00af0acc`](#insn-00af0acc) → [`00af0ad0`](#insn-00af0ad0)
- ブロック [`00af0ad0`](#insn-00af0ad0) 範囲 `[['00af0ad0', '00af0aeb']]`

## 命令位置別の参照

- [`00af0abc`](#insn-00af0abc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ad4`](#insn-00af0ad4) → [`008b89cc`](../008b8/008b89cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b89cc` · 推定シンボル `None` · 推定型 `None`
- [`00af0adc`](#insn-00af0adc) → [`008b7f14`](../008b7/008b7f14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7f14` · 推定シンボル `None` · 推定型 `None`
- [`00af0ae4`](#insn-00af0ae4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ae8`](#insn-00af0ae8) → [`008b7a60`](../008b7/008b7a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7a60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af0abc`](#insn-00af0abc)

~~~json
{
  "source": "00af0abc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ad4`](#insn-00af0ad4)

~~~json
{
  "source": "00af0ad4",
  "target": "008b89cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0adc`](#insn-00af0adc)

~~~json
{
  "source": "00af0adc",
  "target": "008b7f14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0ae4`](#insn-00af0ae4)

~~~json
{
  "source": "00af0ae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ae8`](#insn-00af0ae8)

~~~json
{
  "source": "00af0ae8",
  "target": "008b7a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
