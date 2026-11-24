# 008fbdfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008fae50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fae50.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0055.md#compare-1623ae7bc6190496e2348f12d4c8cfaf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fbdfc",
  "name": "FUN_008fbdfc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3a804d3c10d39e0afa82079930694311a2468e2fdf7d77f459ab56c04558ece",
  "source_text_sha256": "f3a804d3c10d39e0afa82079930694311a2468e2fdf7d77f459ab56c04558ece",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fbdfc",
        "008fbe5f"
      ]
    ],
    "bytes_sha256": "62295e2ed3804430128dd2904853d628d7df79f8384f84be2661495b87b9e1b4",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
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
- [008524fc](../00852/008524fc.md)
- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 591 bytes

~~~c

void FUN_008fbdfc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar3 = *param_2;
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008fbd9c with catch @ 008fbe38 */
                    /* catch() { ... } // from try @ 008fbdc0 with catch @ 008fbe48 */
    *(uint *)(lVar2 + 0x4a844) = *(uint *)(lVar2 + 0x4a844) | 8;
    FUN_008ba17c(uVar3);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fbdfc"></a> `008fbdfc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008fbe00"></a> `008fbe00` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-008fbe04"></a> `008fbe04` | `c1 02 00 54` | b.ne 0x008fbe5c | `CONDITIONAL_JUMP`
<a id="insn-008fbe08"></a> `008fbe08` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-008fbe0c"></a> `008fbe0c` | `88 02 00 35` | cbnz w8,0x008fbe5c | `CONDITIONAL_JUMP`
<a id="insn-008fbe10"></a> `008fbe10` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-008fbe14"></a> `008fbe14` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008fbe18"></a> `008fbe18` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008fbe1c"></a> `008fbe1c` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-008fbe20"></a> `008fbe20` | `8d fc ed 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-008fbe24"></a> `008fbe24` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008fbe28"></a> `008fbe28` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-008fbe2c"></a> `008fbe2c` | `c2 04 ee 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-008fbe30"></a> `008fbe30` | `b3 59 fd 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008fbe34"></a> `008fbe34` | `89 08 95 52` | mov w9,#0xa844 | `FALL_THROUGH`
<a id="insn-008fbe38"></a> `008fbe38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-008fbe3c"></a> `008fbe3c` | `89 00 a0 72` | movk w9,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-008fbe40"></a> `008fbe40` | `0a 68 69 b8` | ldr w10,[x0, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008fbe44"></a> `008fbe44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fbe48"></a> `008fbe48` | `4a 01 1d 32` | orr w10,w10,#0x8 | `FALL_THROUGH`
<a id="insn-008fbe4c"></a> `008fbe4c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008fbe50"></a> `008fbe50` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008fbe54"></a> `008fbe54` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-008fbe58"></a> `008fbe58` | `c9 f8 fe 17` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-008fbe5c"></a> `008fbe5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fbdfc`](#insn-008fbdfc) 範囲 `[['008fbdfc', '008fbe07']]`
  - `CONDITIONAL_JUMP` [`008fbe04`](#insn-008fbe04) → [`008fbe5c`](#insn-008fbe5c)
  - `FALL_THROUGH` [`008fbe04`](#insn-008fbe04) → [`008fbe08`](#insn-008fbe08)
- ブロック [`008fbe08`](#insn-008fbe08) 範囲 `[['008fbe08', '008fbe0f']]`
  - `CONDITIONAL_JUMP` [`008fbe0c`](#insn-008fbe0c) → [`008fbe5c`](#insn-008fbe5c)
  - `FALL_THROUGH` [`008fbe0c`](#insn-008fbe0c) → [`008fbe10`](#insn-008fbe10)
- ブロック [`008fbe10`](#insn-008fbe10) 範囲 `[['008fbe10', '008fbe37']]`
  - `FALL_THROUGH` [`008fbe34`](#insn-008fbe34) → [`008fbe38`](#insn-008fbe38)
- ブロック [`008fbe38`](#insn-008fbe38) 範囲 `[['008fbe38', '008fbe47']]`
  - `FALL_THROUGH` [`008fbe44`](#insn-008fbe44) → [`008fbe48`](#insn-008fbe48)
- ブロック [`008fbe48`](#insn-008fbe48) 範囲 `[['008fbe48', '008fbe5b']]`
- ブロック [`008fbe5c`](#insn-008fbe5c) 範囲 `[['008fbe5c', '008fbe5f']]`

## 命令位置別の参照

- [`008fbe04`](#insn-008fbe04) → [`008fbe5c`](#insn-008fbe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe0c`](#insn-008fbe0c) → [`008fbe5c`](#insn-008fbe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe10`](#insn-008fbe10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe14`](#insn-008fbe14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe20`](#insn-008fbe20) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`008fbe2c`](#insn-008fbe2c) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`008fbe30`](#insn-008fbe30) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008fbe50`](#insn-008fbe50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe54`](#insn-008fbe54) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbe58`](#insn-008fbe58) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fbe04`](#insn-008fbe04)

~~~json
{
  "source": "008fbe04",
  "target": "008fbe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe0c`](#insn-008fbe0c)

~~~json
{
  "source": "008fbe0c",
  "target": "008fbe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe10`](#insn-008fbe10)

~~~json
{
  "source": "008fbe10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe14`](#insn-008fbe14)

~~~json
{
  "source": "008fbe14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe20`](#insn-008fbe20)

~~~json
{
  "source": "008fbe20",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbe2c`](#insn-008fbe2c)

~~~json
{
  "source": "008fbe2c",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbe30`](#insn-008fbe30)

~~~json
{
  "source": "008fbe30",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbe50`](#insn-008fbe50)

~~~json
{
  "source": "008fbe50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe54`](#insn-008fbe54)

~~~json
{
  "source": "008fbe54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbe58`](#insn-008fbe58)

~~~json
{
  "source": "008fbe58",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
