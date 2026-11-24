# 009dbdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009dbd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbd58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0031.md#compare-d968166fa8dc8ed3c10636ada09f36bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009dcd58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009dc/009dcd58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0025.md#compare-469e8f4e90d715c1cc98a5424aa2fe1f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dbdac",
  "name": "FUN_009dbdac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535",
  "source_text_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dbdac",
        "009dbe23"
      ]
    ],
    "bytes_sha256": "6bc35b1d628e4a322435fb0badd90239a138c41be9b818ff75a3003f234d708e",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [0046bd94](../0046b/0046bd94.md)
- [004700f4](../00470/004700f4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 643 bytes

~~~c

void FUN_009dbdac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
  lVar1 = 0x1480;
  if (param_7 != 0) {
    lVar1 = 0x1aa0;
  }
  lVar2 = 0x1528;
  if (param_7 != 0) {
    lVar2 = 0x1b48;
  }
  FUN_004700f4(param_2 + lVar1,param_2 + lVar2,param_6,0);
                    /* try { // try from 009dbe04 to 00adbe0f has its CatchHandler @ 009dc118 */
                    /* try { // try from 009dbe10 to 00adbe17 has its CatchHandler @ 009dc110 */
  FUN_0046bd94(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dbdac"></a> `009dbdac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-009dbdb0"></a> `009dbdb0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbdb4"></a> `009dbdb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbdb8"></a> `009dbdb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbdbc"></a> `009dbdbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009dbdc0"></a> `009dbdc0` | `df 00 00 71` | cmp w6,#0x0 | `FALL_THROUGH`
<a id="insn-009dbdc4"></a> `009dbdc4` | `08 54 83 52` | mov w8,#0x1aa0 | `FALL_THROUGH`
<a id="insn-009dbdc8"></a> `009dbdc8` | `09 90 82 52` | mov w9,#0x1480 | `FALL_THROUGH`
<a id="insn-009dbdcc"></a> `009dbdcc` | `0a 69 83 52` | mov w10,#0x1b48 | `FALL_THROUGH`
<a id="insn-009dbdd0"></a> `009dbdd0` | `0b a5 82 52` | mov w11,#0x1528 | `FALL_THROUGH`
<a id="insn-009dbdd4"></a> `009dbdd4` | `37 01 88 9a` | csel x23,x9,x8,eq | `FALL_THROUGH`
<a id="insn-009dbdd8"></a> `009dbdd8` | `68 01 8a 9a` | csel x8,x11,x10,eq | `FALL_THROUGH`
<a id="insn-009dbddc"></a> `009dbddc` | `f4 03 03 2a` | mov w20,w3 | `FALL_THROUGH`
<a id="insn-009dbde0"></a> `009dbde0` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-009dbde4"></a> `009dbde4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-009dbde8"></a> `009dbde8` | `20 00 17 8b` | add x0,x1,x23 | `FALL_THROUGH`
<a id="insn-009dbdec"></a> `009dbdec` | `21 00 08 8b` | add x1,x1,x8 | `FALL_THROUGH`
<a id="insn-009dbdf0"></a> `009dbdf0` | `e2 03 05 2a` | mov w2,w5 | `FALL_THROUGH`
<a id="insn-009dbdf4"></a> `009dbdf4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009dbdf8"></a> `009dbdf8` | `f3 03 04 2a` | mov w19,w4 | `FALL_THROUGH`
<a id="insn-009dbdfc"></a> `009dbdfc` | `be 50 ea 97` | bl 0x004700f4 | `UNCONDITIONAL_CALL`
<a id="insn-009dbe00"></a> `009dbe00` | `c1 02 17 8b` | add x1,x22,x23 | `FALL_THROUGH`
<a id="insn-009dbe04"></a> `009dbe04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009dbe08"></a> `009dbe08` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-009dbe0c"></a> `009dbe0c` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-009dbe10"></a> `009dbe10` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dbe14"></a> `009dbe14` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dbe18"></a> `009dbe18` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dbe1c"></a> `009dbe1c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-009dbe20"></a> `009dbe20` | `dd 3f ea 17` | b 0x0046bd94 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009dbdac`](#insn-009dbdac) 範囲 `[['009dbdac', '009dbe03']]`
  - `FALL_THROUGH` [`009dbe00`](#insn-009dbe00) → [`009dbe04`](#insn-009dbe04)
- ブロック [`009dbe04`](#insn-009dbe04) 範囲 `[['009dbe04', '009dbe0f']]`
  - `FALL_THROUGH` [`009dbe0c`](#insn-009dbe0c) → [`009dbe10`](#insn-009dbe10)
- ブロック [`009dbe10`](#insn-009dbe10) 範囲 `[['009dbe10', '009dbe23']]`

## 命令位置別の参照

- [`009dbdac`](#insn-009dbdac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbdb0`](#insn-009dbdb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbdb4`](#insn-009dbdb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbdb8`](#insn-009dbdb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbdfc`](#insn-009dbdfc) → [`004700f4`](../00470/004700f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700f4` · 推定シンボル `None` · 推定型 `None`
- [`009dbe10`](#insn-009dbe10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbe14`](#insn-009dbe14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbe18`](#insn-009dbe18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbe1c`](#insn-009dbe1c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dbe20`](#insn-009dbe20) → [`0046bd94`](../0046b/0046bd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd94` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dbdac`](#insn-009dbdac)

~~~json
{
  "source": "009dbdac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbdb0`](#insn-009dbdb0)

~~~json
{
  "source": "009dbdb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbdb4`](#insn-009dbdb4)

~~~json
{
  "source": "009dbdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbdb8`](#insn-009dbdb8)

~~~json
{
  "source": "009dbdb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbdfc`](#insn-009dbdfc)

~~~json
{
  "source": "009dbdfc",
  "target": "004700f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dbe10`](#insn-009dbe10)

~~~json
{
  "source": "009dbe10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbe14`](#insn-009dbe14)

~~~json
{
  "source": "009dbe14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbe18`](#insn-009dbe18)

~~~json
{
  "source": "009dbe18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbe1c`](#insn-009dbe1c)

~~~json
{
  "source": "009dbe1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dbe20`](#insn-009dbe20)

~~~json
{
  "source": "009dbe20",
  "target": "0046bd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
