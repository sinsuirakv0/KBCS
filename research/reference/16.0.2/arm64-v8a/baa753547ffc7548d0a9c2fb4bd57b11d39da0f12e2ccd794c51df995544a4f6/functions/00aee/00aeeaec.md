# 00aeeaec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeea50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeea50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-7608616a6aa9fe3c7fa9611e555fdbdb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aefae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aefae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-bc9e13891e7d39bfb5ef3de0faf37234)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeeaec",
  "name": "FUN_00aeeaec",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cbd3648d3e25e98306ebbec4fde43ac9416bf6252f7b498b3bc1c77932188f4",
  "source_text_sha256": "1cbd3648d3e25e98306ebbec4fde43ac9416bf6252f7b498b3bc1c77932188f4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeeaec",
        "00aeeb67"
      ]
    ],
    "bytes_sha256": "02363d405c8e288c0f955ce2d5e48ee6d52431017bbcc3562fce9c87d97276f3",
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

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b91d0](../008b9/008b91d0.md)
- [008b98a8](../008b9/008b98a8.md)
- [008bb568](../008bb/008bb568.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 666 bytes

~~~c

void FUN_00aeeaec(long param_1,undefined8 param_2,int *param_3)

{
  undefined8 uVar1;
  long lVar2;
  
  if (*param_3 == 3) {
    lVar2 = *(long *)(param_1 + 8);
    uVar1 = FUN_0047ad34();
    FUN_0047ce14(uVar1,0xb,0);
    uVar1 = FUN_008bb568(lVar2 + 0x2f08);
    FUN_008b98a8(uVar1,2);
    FUN_008bb568(lVar2 + 0x2f08);
    FUN_008b91d0();
    return;
  }
                    /* try { // try from 00aeeb04 to 00beeb0f has its CatchHandler @ 00aeecac */
  if (*param_3 == 0) {
    uVar1 = FUN_0047ad34();
                    /* try { // try from 00aeeb10 to 00beeca7 has its CatchHandler @ 00aee9c4 */
    FUN_0047ce14(uVar1,10,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeeaec"></a> `00aeeaec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeeaf0"></a> `00aeeaf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeaf4"></a> `00aeeaf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aeeaf8"></a> `00aeeaf8` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aeeafc"></a> `00aeeafc` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aeeb00"></a> `00aeeb00` | `00 01 00 54` | b.eq 0x00aeeb20 | `CONDITIONAL_JUMP`
<a id="insn-00aeeb04"></a> `00aeeb04` | `c8 02 00 35` | cbnz w8,0x00aeeb5c | `CONDITIONAL_JUMP`
<a id="insn-00aeeb08"></a> `00aeeb08` | `8b 30 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb0c"></a> `00aeeb0c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aeeb10"></a> `00aeeb10` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeeb14"></a> `00aeeb14` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeb18"></a> `00aeeb18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeeb1c"></a> `00aeeb1c` | `be 38 e6 17` | b 0x0047ce14 | `CALL_TERMINATOR`
<a id="insn-00aeeb20"></a> `00aeeb20` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aeeb24"></a> `00aeeb24` | `84 30 e6 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb28"></a> `00aeeb28` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aeeb2c"></a> `00aeeb2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeeb30"></a> `00aeeb30` | `b9 38 e6 97` | bl 0x0047ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb34"></a> `00aeeb34` | `14 e1 85 52` | mov w20,#0x2f08 | `FALL_THROUGH`
<a id="insn-00aeeb38"></a> `00aeeb38` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00aeeb3c"></a> `00aeeb3c` | `8b 32 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb40"></a> `00aeeb40` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00aeeb44"></a> `00aeeb44` | `59 2b f7 97` | bl 0x008b98a8 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb48"></a> `00aeeb48` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-00aeeb4c"></a> `00aeeb4c` | `87 32 f7 97` | bl 0x008bb568 | `UNCONDITIONAL_CALL`
<a id="insn-00aeeb50"></a> `00aeeb50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeb54"></a> `00aeeb54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeeb58"></a> `00aeeb58` | `9e 29 f7 17` | b 0x008b91d0 | `CALL_TERMINATOR`
<a id="insn-00aeeb5c"></a> `00aeeb5c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeeb60"></a> `00aeeb60` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeeb64"></a> `00aeeb64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeeaec`](#insn-00aeeaec) 範囲 `[['00aeeaec', '00aeeb03']]`
  - `CONDITIONAL_JUMP` [`00aeeb00`](#insn-00aeeb00) → [`00aeeb20`](#insn-00aeeb20)
  - `FALL_THROUGH` [`00aeeb00`](#insn-00aeeb00) → [`00aeeb04`](#insn-00aeeb04)
- ブロック [`00aeeb04`](#insn-00aeeb04) 範囲 `[['00aeeb04', '00aeeb07']]`
  - `CONDITIONAL_JUMP` [`00aeeb04`](#insn-00aeeb04) → [`00aeeb5c`](#insn-00aeeb5c)
  - `FALL_THROUGH` [`00aeeb04`](#insn-00aeeb04) → [`00aeeb08`](#insn-00aeeb08)
- ブロック [`00aeeb08`](#insn-00aeeb08) 範囲 `[['00aeeb08', '00aeeb0f']]`
  - `FALL_THROUGH` [`00aeeb0c`](#insn-00aeeb0c) → [`00aeeb10`](#insn-00aeeb10)
- ブロック [`00aeeb10`](#insn-00aeeb10) 範囲 `[['00aeeb10', '00aeeb1f']]`
- ブロック [`00aeeb20`](#insn-00aeeb20) 範囲 `[['00aeeb20', '00aeeb5b']]`
- ブロック [`00aeeb5c`](#insn-00aeeb5c) 範囲 `[['00aeeb5c', '00aeeb67']]`

## 命令位置別の参照

- [`00aeeaec`](#insn-00aeeaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeaf0`](#insn-00aeeaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb00`](#insn-00aeeb00) → [`00aeeb20`](#insn-00aeeb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb04`](#insn-00aeeb04) → [`00aeeb5c`](#insn-00aeeb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb08`](#insn-00aeeb08) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb14`](#insn-00aeeb14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb18`](#insn-00aeeb18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb1c`](#insn-00aeeb1c) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb24`](#insn-00aeeb24) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb30`](#insn-00aeeb30) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb3c`](#insn-00aeeb3c) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb44`](#insn-00aeeb44) → [`008b98a8`](../008b9/008b98a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b98a8` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb4c`](#insn-00aeeb4c) → [`008bb568`](../008bb/008bb568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb568` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb50`](#insn-00aeeb50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb54`](#insn-00aeeb54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb58`](#insn-00aeeb58) → [`008b91d0`](../008b9/008b91d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b91d0` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb5c`](#insn-00aeeb5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeeb60`](#insn-00aeeb60) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeeaec`](#insn-00aeeaec)

~~~json
{
  "source": "00aeeaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeaf0`](#insn-00aeeaf0)

~~~json
{
  "source": "00aeeaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb00`](#insn-00aeeb00)

~~~json
{
  "source": "00aeeb00",
  "target": "00aeeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb04`](#insn-00aeeb04)

~~~json
{
  "source": "00aeeb04",
  "target": "00aeeb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb08`](#insn-00aeeb08)

~~~json
{
  "source": "00aeeb08",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb14`](#insn-00aeeb14)

~~~json
{
  "source": "00aeeb14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb18`](#insn-00aeeb18)

~~~json
{
  "source": "00aeeb18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb1c`](#insn-00aeeb1c)

~~~json
{
  "source": "00aeeb1c",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb24`](#insn-00aeeb24)

~~~json
{
  "source": "00aeeb24",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb30`](#insn-00aeeb30)

~~~json
{
  "source": "00aeeb30",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb3c`](#insn-00aeeb3c)

~~~json
{
  "source": "00aeeb3c",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb44`](#insn-00aeeb44)

~~~json
{
  "source": "00aeeb44",
  "target": "008b98a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb4c`](#insn-00aeeb4c)

~~~json
{
  "source": "00aeeb4c",
  "target": "008bb568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb50`](#insn-00aeeb50)

~~~json
{
  "source": "00aeeb50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb54`](#insn-00aeeb54)

~~~json
{
  "source": "00aeeb54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb58`](#insn-00aeeb58)

~~~json
{
  "source": "00aeeb58",
  "target": "008b91d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeeb5c`](#insn-00aeeb5c)

~~~json
{
  "source": "00aeeb5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeeb60`](#insn-00aeeb60)

~~~json
{
  "source": "00aeeb60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
