# 00aa2dec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa2d7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa2d7c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-3e3cd8097e039e717fe01f59a1ef53b8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aa3de0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa3/00aa3de0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-161269ca4bbaaac8905009ab54af4db0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2dec",
  "name": "FUN_00aa2dec",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e86789b79749c592de946316583745e79699d066f1d180b69ed47742c716edf6",
  "source_text_sha256": "e86789b79749c592de946316583745e79699d066f1d180b69ed47742c716edf6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2dec",
        "00aa2e67"
      ]
    ],
    "bytes_sha256": "28c07482ea1cc74a52f8092e69c9c8c4f128e011f79811e6532e88bf1de15700",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007ccf44](../007cc/007ccf44.md)

## 呼び出し先

- [00442970](../00442/00442970.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 947 bytes

~~~c

undefined4 FUN_00aa2dec(long param_1,int param_2)

{
  long *plVar1;
  long *plVar2;
  
  plVar1 = *(long **)(param_1 + 0x20);
  plVar2 = plVar1;
  do {
    if (plVar2 == (long *)0x0) {
      return 0;
    }
    if (*(int *)((long)plVar2 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)plVar2 + 0x1c)) {
        do {
          if (param_2 < *(int *)((long)plVar1 + 0x1c)) {
            plVar1 = (long *)*plVar1;
          }
          else {
            if (param_2 <= *(int *)((long)plVar1 + 0x1c)) {
                    /* catch() { ... } // from try @ 00aa314c with catch @ 00aa2e60 */
              return (int)plVar1[4];
            }
            plVar1 = (long *)plVar1[1];
          }
        } while (plVar1 != (long *)0x0);
                    /* WARNING: Subroutine does not return */
        FUN_00442970("map::at:  key not found");
      }
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2dec"></a> `00aa2dec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00aa2df0"></a> `00aa2df0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa2df4"></a> `00aa2df4` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2df8"></a> `00aa2df8` | `c8 02 00 b4` | cbz x8,0x00aa2e50 | `CONDITIONAL_JUMP`
<a id="insn-00aa2dfc"></a> `00aa2dfc` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00aa2e00"></a> `00aa2e00` | `03 00 00 14` | b 0x00aa2e0c | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2e04"></a> `00aa2e04` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aa2e08"></a> `00aa2e08` | `49 02 00 b4` | cbz x9,0x00aa2e50 | `CONDITIONAL_JUMP`
<a id="insn-00aa2e0c"></a> `00aa2e0c` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2e10"></a> `00aa2e10` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-00aa2e14"></a> `00aa2e14` | `8c ff ff 54` | b.gt 0x00aa2e04 | `CONDITIONAL_JUMP`
<a id="insn-00aa2e18"></a> `00aa2e18` | `aa 00 00 54` | b.ge 0x00aa2e2c | `CONDITIONAL_JUMP`
<a id="insn-00aa2e1c"></a> `00aa2e1c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2e20"></a> `00aa2e20` | `f9 ff ff 17` | b 0x00aa2e04 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2e24"></a> `00aa2e24` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aa2e28"></a> `00aa2e28` | `e8 00 00 b4` | cbz x8,0x00aa2e44 | `CONDITIONAL_JUMP`
<a id="insn-00aa2e2c"></a> `00aa2e2c` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2e30"></a> `00aa2e30` | `3f 01 01 6b` | cmp w9,w1 | `FALL_THROUGH`
<a id="insn-00aa2e34"></a> `00aa2e34` | `8c ff ff 54` | b.gt 0x00aa2e24 | `CONDITIONAL_JUMP`
<a id="insn-00aa2e38"></a> `00aa2e38` | `2a 01 00 54` | b.ge 0x00aa2e5c | `CONDITIONAL_JUMP`
<a id="insn-00aa2e3c"></a> `00aa2e3c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aa2e40"></a> `00aa2e40` | `68 ff ff b5` | cbnz x8,0x00aa2e2c | `CONDITIONAL_JUMP`
<a id="insn-00aa2e44"></a> `00aa2e44` | `e0 bf ff d0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aa2e48"></a> `00aa2e48` | `00 c0 05 91` | add x0,x0,#0x170 | `FALL_THROUGH`
<a id="insn-00aa2e4c"></a> `00aa2e4c` | `c9 7e e6 97` | bl 0x00442970 | `CALL_TERMINATOR`
<a id="insn-00aa2e50"></a> `00aa2e50` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa2e54"></a> `00aa2e54` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aa2e58"></a> `00aa2e58` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa2e5c"></a> `00aa2e5c` | `00 21 40 b9` | ldr w0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2e60"></a> `00aa2e60` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aa2e64"></a> `00aa2e64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2dec`](#insn-00aa2dec) 範囲 `[['00aa2dec', '00aa2dfb']]`
  - `CONDITIONAL_JUMP` [`00aa2df8`](#insn-00aa2df8) → [`00aa2e50`](#insn-00aa2e50)
  - `FALL_THROUGH` [`00aa2df8`](#insn-00aa2df8) → [`00aa2dfc`](#insn-00aa2dfc)
- ブロック [`00aa2dfc`](#insn-00aa2dfc) 範囲 `[['00aa2dfc', '00aa2e03']]`
  - `UNCONDITIONAL_JUMP` [`00aa2e00`](#insn-00aa2e00) → [`00aa2e0c`](#insn-00aa2e0c)
- ブロック [`00aa2e04`](#insn-00aa2e04) 範囲 `[['00aa2e04', '00aa2e0b']]`
  - `CONDITIONAL_JUMP` [`00aa2e08`](#insn-00aa2e08) → [`00aa2e50`](#insn-00aa2e50)
  - `FALL_THROUGH` [`00aa2e08`](#insn-00aa2e08) → [`00aa2e0c`](#insn-00aa2e0c)
- ブロック [`00aa2e0c`](#insn-00aa2e0c) 範囲 `[['00aa2e0c', '00aa2e17']]`
  - `CONDITIONAL_JUMP` [`00aa2e14`](#insn-00aa2e14) → [`00aa2e04`](#insn-00aa2e04)
  - `FALL_THROUGH` [`00aa2e14`](#insn-00aa2e14) → [`00aa2e18`](#insn-00aa2e18)
- ブロック [`00aa2e18`](#insn-00aa2e18) 範囲 `[['00aa2e18', '00aa2e1b']]`
  - `CONDITIONAL_JUMP` [`00aa2e18`](#insn-00aa2e18) → [`00aa2e2c`](#insn-00aa2e2c)
  - `FALL_THROUGH` [`00aa2e18`](#insn-00aa2e18) → [`00aa2e1c`](#insn-00aa2e1c)
- ブロック [`00aa2e1c`](#insn-00aa2e1c) 範囲 `[['00aa2e1c', '00aa2e23']]`
  - `UNCONDITIONAL_JUMP` [`00aa2e20`](#insn-00aa2e20) → [`00aa2e04`](#insn-00aa2e04)
- ブロック [`00aa2e24`](#insn-00aa2e24) 範囲 `[['00aa2e24', '00aa2e2b']]`
  - `CONDITIONAL_JUMP` [`00aa2e28`](#insn-00aa2e28) → [`00aa2e44`](#insn-00aa2e44)
  - `FALL_THROUGH` [`00aa2e28`](#insn-00aa2e28) → [`00aa2e2c`](#insn-00aa2e2c)
- ブロック [`00aa2e2c`](#insn-00aa2e2c) 範囲 `[['00aa2e2c', '00aa2e37']]`
  - `CONDITIONAL_JUMP` [`00aa2e34`](#insn-00aa2e34) → [`00aa2e24`](#insn-00aa2e24)
  - `FALL_THROUGH` [`00aa2e34`](#insn-00aa2e34) → [`00aa2e38`](#insn-00aa2e38)
- ブロック [`00aa2e38`](#insn-00aa2e38) 範囲 `[['00aa2e38', '00aa2e3b']]`
  - `CONDITIONAL_JUMP` [`00aa2e38`](#insn-00aa2e38) → [`00aa2e5c`](#insn-00aa2e5c)
  - `FALL_THROUGH` [`00aa2e38`](#insn-00aa2e38) → [`00aa2e3c`](#insn-00aa2e3c)
- ブロック [`00aa2e3c`](#insn-00aa2e3c) 範囲 `[['00aa2e3c', '00aa2e43']]`
  - `CONDITIONAL_JUMP` [`00aa2e40`](#insn-00aa2e40) → [`00aa2e2c`](#insn-00aa2e2c)
  - `FALL_THROUGH` [`00aa2e40`](#insn-00aa2e40) → [`00aa2e44`](#insn-00aa2e44)
- ブロック [`00aa2e44`](#insn-00aa2e44) 範囲 `[['00aa2e44', '00aa2e4f']]`
- ブロック [`00aa2e50`](#insn-00aa2e50) 範囲 `[['00aa2e50', '00aa2e5b']]`
- ブロック [`00aa2e5c`](#insn-00aa2e5c) 範囲 `[['00aa2e5c', '00aa2e5f']]`
  - `FALL_THROUGH` [`00aa2e5c`](#insn-00aa2e5c) → [`00aa2e60`](#insn-00aa2e60)
- ブロック [`00aa2e60`](#insn-00aa2e60) 範囲 `[['00aa2e60', '00aa2e67']]`

## 命令位置別の参照

- [`00aa2dec`](#insn-00aa2dec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2df8`](#insn-00aa2df8) → [`00aa2e50`](#insn-00aa2e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e00`](#insn-00aa2e00) → [`00aa2e0c`](#insn-00aa2e0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e08`](#insn-00aa2e08) → [`00aa2e50`](#insn-00aa2e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e14`](#insn-00aa2e14) → [`00aa2e04`](#insn-00aa2e04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e18`](#insn-00aa2e18) → [`00aa2e2c`](#insn-00aa2e2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e20`](#insn-00aa2e20) → [`00aa2e04`](#insn-00aa2e04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e28`](#insn-00aa2e28) → [`00aa2e44`](#insn-00aa2e44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e34`](#insn-00aa2e34) → [`00aa2e24`](#insn-00aa2e24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e38`](#insn-00aa2e38) → [`00aa2e5c`](#insn-00aa2e5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e40`](#insn-00aa2e40) → [`00aa2e2c`](#insn-00aa2e2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e48`](#insn-00aa2e48) → `002a0170`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa2e4c`](#insn-00aa2e4c) → [`00442970`](../00442/00442970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442970` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e54`](#insn-00aa2e54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2e60`](#insn-00aa2e60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2dec`](#insn-00aa2dec)

~~~json
{
  "source": "00aa2dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2df8`](#insn-00aa2df8)

~~~json
{
  "source": "00aa2df8",
  "target": "00aa2e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e00`](#insn-00aa2e00)

~~~json
{
  "source": "00aa2e00",
  "target": "00aa2e0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e08`](#insn-00aa2e08)

~~~json
{
  "source": "00aa2e08",
  "target": "00aa2e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e14`](#insn-00aa2e14)

~~~json
{
  "source": "00aa2e14",
  "target": "00aa2e04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e18`](#insn-00aa2e18)

~~~json
{
  "source": "00aa2e18",
  "target": "00aa2e2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e20`](#insn-00aa2e20)

~~~json
{
  "source": "00aa2e20",
  "target": "00aa2e04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e28`](#insn-00aa2e28)

~~~json
{
  "source": "00aa2e28",
  "target": "00aa2e44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e34`](#insn-00aa2e34)

~~~json
{
  "source": "00aa2e34",
  "target": "00aa2e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e38`](#insn-00aa2e38)

~~~json
{
  "source": "00aa2e38",
  "target": "00aa2e5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e40`](#insn-00aa2e40)

~~~json
{
  "source": "00aa2e40",
  "target": "00aa2e2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e48`](#insn-00aa2e48)

~~~json
{
  "source": "00aa2e48",
  "target": "002a0170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0170",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "002a0170",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa2e4c`](#insn-00aa2e4c)

~~~json
{
  "source": "00aa2e4c",
  "target": "00442970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2e54`](#insn-00aa2e54)

~~~json
{
  "source": "00aa2e54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2e60`](#insn-00aa2e60)

~~~json
{
  "source": "00aa2e60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
