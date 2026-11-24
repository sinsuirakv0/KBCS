# 00aefac8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aefa2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefa2c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-58be251b59c09e7b7bbcd50ec2d7b7da)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af0abc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af0/00af0abc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-902659b7eb045df32f3541c9cde79c60)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefac8",
  "name": "FUN_00aefac8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d",
  "source_text_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefac8",
        "00aefaf7"
      ]
    ],
    "bytes_sha256": "65c48c45535ec5cae69cbdf3f24484500fab2b7472d1178939fe14eae84f8aa8",
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

- [008b6ab4](../008b6/008b6ab4.md)
- [008b6f68](../008b6/008b6f68.md)
- [008b7a20](../008b7/008b7a20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 193 bytes

~~~c

void FUN_00aefac8(long param_1)

{
  undefined8 uVar1;
  
  uVar1 = FUN_008b7a20(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b6f68(uVar1,1);
  FUN_008b6ab4(uVar1,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefac8"></a> `00aefac8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00aefacc"></a> `00aefacc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefad0"></a> `00aefad0` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefad4"></a> `00aefad4` | `09 e7 85 52` | mov w9,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aefad8"></a> `00aefad8` | `c1 64 80 52` | mov w1,#0x326 | `FALL_THROUGH`
<a id="insn-00aefadc"></a> `00aefadc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aefae0"></a> `00aefae0` | `d0 1f f7 97` | bl 0x008b7a20 | `UNCONDITIONAL_CALL`
<a id="insn-00aefae4"></a> `00aefae4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aefae8"></a> `00aefae8` | `20 1d f7 97` | bl 0x008b6f68 | `UNCONDITIONAL_CALL`
<a id="insn-00aefaec"></a> `00aefaec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aefaf0"></a> `00aefaf0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aefaf4"></a> `00aefaf4` | `f0 1b f7 17` | b 0x008b6ab4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefac8`](#insn-00aefac8) 範囲 `[['00aefac8', '00aefaf7']]`

## 命令位置別の参照

- [`00aefac8`](#insn-00aefac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefae0`](#insn-00aefae0) → [`008b7a20`](../008b7/008b7a20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7a20` · 推定シンボル `None` · 推定型 `None`
- [`00aefae8`](#insn-00aefae8) → [`008b6f68`](../008b6/008b6f68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f68` · 推定シンボル `None` · 推定型 `None`
- [`00aefaf0`](#insn-00aefaf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefaf4`](#insn-00aefaf4) → [`008b6ab4`](../008b6/008b6ab4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6ab4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefac8`](#insn-00aefac8)

~~~json
{
  "source": "00aefac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefae0`](#insn-00aefae0)

~~~json
{
  "source": "00aefae0",
  "target": "008b7a20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefae8`](#insn-00aefae8)

~~~json
{
  "source": "00aefae8",
  "target": "008b6f68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefaf0`](#insn-00aefaf0)

~~~json
{
  "source": "00aefaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefaf4`](#insn-00aefaf4)

~~~json
{
  "source": "00aefaf4",
  "target": "008b6ab4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
