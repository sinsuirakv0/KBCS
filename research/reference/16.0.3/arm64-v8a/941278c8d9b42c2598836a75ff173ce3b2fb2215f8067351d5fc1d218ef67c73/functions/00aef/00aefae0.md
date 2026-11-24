# 00aefae0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeeaec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeeaec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-bc9e13891e7d39bfb5ef3de0faf37234)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefae0",
  "name": "FUN_00aefae0",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97611cfd4de4bfbd71aadf9127be242e068296ee6f941e8ff2a1087da6b4558e",
  "source_text_sha256": "97611cfd4de4bfbd71aadf9127be242e068296ee6f941e8ff2a1087da6b4558e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefae0",
        "00aefb5b"
      ]
    ],
    "bytes_sha256": "1a0376711f581a60721ecfc9b18871b97a1b606e2528777625463d048959d34c",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)
- [008ba854](../008ba/008ba854.md)
- [008bc514](../008bc/008bc514.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 472 bytes

~~~c

void FUN_00aefae0(long param_1,undefined8 param_2,int *param_3)

{
  undefined8 uVar1;
  long lVar2;
  
  if (*param_3 == 3) {
    lVar2 = *(long *)(param_1 + 8);
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    uVar1 = FUN_008bc514(lVar2 + 0x2f08);
    FUN_008ba854(uVar1,2);
    FUN_008bc514(lVar2 + 0x2f08);
    FUN_008ba17c();
    return;
  }
  if (*param_3 == 0) {
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,10,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefae0"></a> `00aefae0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aefae4"></a> `00aefae4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefae8"></a> `00aefae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefaec"></a> `00aefaec` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aefaf0"></a> `00aefaf0` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aefaf4"></a> `00aefaf4` | `00 01 00 54` | b.eq 0x00aefb14 | `CONDITIONAL_JUMP`
<a id="insn-00aefaf8"></a> `00aefaf8` | `c8 02 00 35` | cbnz w8,0x00aefb50 | `CONDITIONAL_JUMP`
<a id="insn-00aefafc"></a> `00aefafc` | `56 2d e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb00"></a> `00aefb00` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aefb04"></a> `00aefb04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefb08"></a> `00aefb08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefb0c"></a> `00aefb0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aefb10"></a> `00aefb10` | `89 35 e6 17` | b 0x0047d134 | `CALL_TERMINATOR`
<a id="insn-00aefb14"></a> `00aefb14` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefb18"></a> `00aefb18` | `4f 2d e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb1c"></a> `00aefb1c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aefb20"></a> `00aefb20` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefb24"></a> `00aefb24` | `84 35 e6 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb28"></a> `00aefb28` | `14 e1 85 52` | mov w20,#0x2f08 | `FALL_THROUGH`
<a id="insn-00aefb2c"></a> `00aefb2c` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00aefb30"></a> `00aefb30` | `79 32 f7 97` | bl 0x008bc514 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb34"></a> `00aefb34` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00aefb38"></a> `00aefb38` | `47 2b f7 97` | bl 0x008ba854 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb3c"></a> `00aefb3c` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00aefb40"></a> `00aefb40` | `75 32 f7 97` | bl 0x008bc514 | `UNCONDITIONAL_CALL`
<a id="insn-00aefb44"></a> `00aefb44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefb48"></a> `00aefb48` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aefb4c"></a> `00aefb4c` | `8c 29 f7 17` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-00aefb50"></a> `00aefb50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefb54"></a> `00aefb54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aefb58"></a> `00aefb58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefae0`](#insn-00aefae0) 範囲 `[['00aefae0', '00aefaf7']]`
  - `CONDITIONAL_JUMP` [`00aefaf4`](#insn-00aefaf4) → [`00aefb14`](#insn-00aefb14)
  - `FALL_THROUGH` [`00aefaf4`](#insn-00aefaf4) → [`00aefaf8`](#insn-00aefaf8)
- ブロック [`00aefaf8`](#insn-00aefaf8) 範囲 `[['00aefaf8', '00aefafb']]`
  - `CONDITIONAL_JUMP` [`00aefaf8`](#insn-00aefaf8) → [`00aefb50`](#insn-00aefb50)
  - `FALL_THROUGH` [`00aefaf8`](#insn-00aefaf8) → [`00aefafc`](#insn-00aefafc)
- ブロック [`00aefafc`](#insn-00aefafc) 範囲 `[['00aefafc', '00aefb13']]`
- ブロック [`00aefb14`](#insn-00aefb14) 範囲 `[['00aefb14', '00aefb4f']]`
- ブロック [`00aefb50`](#insn-00aefb50) 範囲 `[['00aefb50', '00aefb5b']]`

## 命令位置別の参照

- [`00aefae0`](#insn-00aefae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefae4`](#insn-00aefae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefaf4`](#insn-00aefaf4) → [`00aefb14`](#insn-00aefb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefaf8`](#insn-00aefaf8) → [`00aefb50`](#insn-00aefb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefafc`](#insn-00aefafc) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00aefb08`](#insn-00aefb08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb0c`](#insn-00aefb0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb10`](#insn-00aefb10) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00aefb18`](#insn-00aefb18) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00aefb24`](#insn-00aefb24) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00aefb30`](#insn-00aefb30) → [`008bc514`](../008bc/008bc514.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bc514` · 推定シンボル `None` · 推定型 `None`
- [`00aefb38`](#insn-00aefb38) → [`008ba854`](../008ba/008ba854.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba854` · 推定シンボル `None` · 推定型 `None`
- [`00aefb40`](#insn-00aefb40) → [`008bc514`](../008bc/008bc514.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bc514` · 推定シンボル `None` · 推定型 `None`
- [`00aefb44`](#insn-00aefb44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb48`](#insn-00aefb48) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb4c`](#insn-00aefb4c) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`
- [`00aefb50`](#insn-00aefb50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefb54`](#insn-00aefb54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefae0`](#insn-00aefae0)

~~~json
{
  "source": "00aefae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefae4`](#insn-00aefae4)

~~~json
{
  "source": "00aefae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefaf4`](#insn-00aefaf4)

~~~json
{
  "source": "00aefaf4",
  "target": "00aefb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefaf8`](#insn-00aefaf8)

~~~json
{
  "source": "00aefaf8",
  "target": "00aefb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefafc`](#insn-00aefafc)

~~~json
{
  "source": "00aefafc",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb08`](#insn-00aefb08)

~~~json
{
  "source": "00aefb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb0c`](#insn-00aefb0c)

~~~json
{
  "source": "00aefb0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb10`](#insn-00aefb10)

~~~json
{
  "source": "00aefb10",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb18`](#insn-00aefb18)

~~~json
{
  "source": "00aefb18",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb24`](#insn-00aefb24)

~~~json
{
  "source": "00aefb24",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb30`](#insn-00aefb30)

~~~json
{
  "source": "00aefb30",
  "target": "008bc514",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb38`](#insn-00aefb38)

~~~json
{
  "source": "00aefb38",
  "target": "008ba854",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb40`](#insn-00aefb40)

~~~json
{
  "source": "00aefb40",
  "target": "008bc514",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb44`](#insn-00aefb44)

~~~json
{
  "source": "00aefb44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb48`](#insn-00aefb48)

~~~json
{
  "source": "00aefb48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb4c`](#insn-00aefb4c)

~~~json
{
  "source": "00aefb4c",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefb50`](#insn-00aefb50)

~~~json
{
  "source": "00aefb50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefb54`](#insn-00aefb54)

~~~json
{
  "source": "00aefb54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
