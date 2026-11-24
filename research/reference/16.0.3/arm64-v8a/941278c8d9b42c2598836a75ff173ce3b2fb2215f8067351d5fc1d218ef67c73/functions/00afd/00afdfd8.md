# 00afdfd8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afcfe4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afc/00afcfe4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-12cb23c5405abc370b8445c4fed03614)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdfd8",
  "name": "FUN_00afdfd8",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42c601c718dd57051d674a770b0f43248453e48bdc378887b7b2c2ea8c632c4b",
  "source_text_sha256": "42c601c718dd57051d674a770b0f43248453e48bdc378887b7b2c2ea8c632c4b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdfd8",
        "00afe03f"
      ]
    ],
    "bytes_sha256": "b6b4aeddf7816c1a4083e0d54eea5798e8dead7554b4c25fe21aa96a0ffb7f9b",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 395 bytes

~~~c

undefined4 FUN_00afdfd8(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008524fc();
  uVar3 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_008524fc();
    uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    uVar1 = 0;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afdfd8"></a> `00afdfd8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afdfdc"></a> `00afdfdc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdfe0"></a> `00afdfe0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afdfe4"></a> `00afdfe4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afdfe8"></a> `00afdfe8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afdfec"></a> `00afdfec` | `44 51 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afdff0"></a> `00afdff0` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afdff4"></a> `00afdff4` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afdff8"></a> `00afdff8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afdffc"></a> `00afdffc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe000"></a> `00afe000` | `04 a6 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afe004"></a> `00afe004` | `60 01 00 37` | tbnz w0,#0x0,0x00afe030 | `CONDITIONAL_JUMP`
<a id="insn-00afe008"></a> `00afe008` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afe00c"></a> `00afe00c` | `3c 51 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe010"></a> `00afe010` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afe014"></a> `00afe014` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afe018"></a> `00afe018` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe01c"></a> `00afe01c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe020"></a> `00afe020` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afe024"></a> `00afe024` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe028"></a> `00afe028` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe02c"></a> `00afe02c` | `02 00 00 14` | b 0x00afe034 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe030"></a> `00afe030` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afe034"></a> `00afe034` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe038"></a> `00afe038` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afe03c"></a> `00afe03c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdfd8`](#insn-00afdfd8) 範囲 `[['00afdfd8', '00afe007']]`
  - `CONDITIONAL_JUMP` [`00afe004`](#insn-00afe004) → [`00afe030`](#insn-00afe030)
  - `FALL_THROUGH` [`00afe004`](#insn-00afe004) → [`00afe008`](#insn-00afe008)
- ブロック [`00afe008`](#insn-00afe008) 範囲 `[['00afe008', '00afe02f']]`
  - `UNCONDITIONAL_JUMP` [`00afe02c`](#insn-00afe02c) → [`00afe034`](#insn-00afe034)
- ブロック [`00afe030`](#insn-00afe030) 範囲 `[['00afe030', '00afe033']]`
  - `FALL_THROUGH` [`00afe030`](#insn-00afe030) → [`00afe034`](#insn-00afe034)
- ブロック [`00afe034`](#insn-00afe034) 範囲 `[['00afe034', '00afe03f']]`

## 命令位置別の参照

- [`00afdfd8`](#insn-00afdfd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfdc`](#insn-00afdfdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdfec`](#insn-00afdfec) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe000`](#insn-00afe000) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afe004`](#insn-00afe004) → [`00afe030`](#insn-00afe030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe00c`](#insn-00afe00c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe02c`](#insn-00afe02c) → [`00afe034`](#insn-00afe034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe034`](#insn-00afe034) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe038`](#insn-00afe038) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdfd8`](#insn-00afdfd8)

~~~json
{
  "source": "00afdfd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfdc`](#insn-00afdfdc)

~~~json
{
  "source": "00afdfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdfec`](#insn-00afdfec)

~~~json
{
  "source": "00afdfec",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe000`](#insn-00afe000)

~~~json
{
  "source": "00afe000",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe004`](#insn-00afe004)

~~~json
{
  "source": "00afe004",
  "target": "00afe030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe00c`](#insn-00afe00c)

~~~json
{
  "source": "00afe00c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe02c`](#insn-00afe02c)

~~~json
{
  "source": "00afe02c",
  "target": "00afe034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe034`](#insn-00afe034)

~~~json
{
  "source": "00afe034",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe038`](#insn-00afe038)

~~~json
{
  "source": "00afe038",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
