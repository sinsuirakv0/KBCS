# 007aeccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0064.md#review-d14d2bbcea15344a0e1b5e3e55233788)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aeccc",
  "name": "FUN_007aeccc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1052e7d967bac5a9b3b2fedc3002c18be60dbc2df07198990f6e43275e37211",
  "source_text_sha256": "a1052e7d967bac5a9b3b2fedc3002c18be60dbc2df07198990f6e43275e37211",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007aeccc",
        "007aed3f"
      ]
    ],
    "bytes_sha256": "a94d98a4ccc1e2a13350f22750588897180d06c9f590c8b5daa6bcdf23c3611e",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 767 bytes

~~~c

void FUN_007aeccc(undefined8 *param_1)

{
  undefined8 *__ptr;
  
                    /* try { // try from 007aeccc to 008aecd3 has its CatchHandler @ 007af430 */
  __ptr = (undefined8 *)*param_1;
  *param_1 = 0;
  if (__ptr != (undefined8 *)0x0) {
    if ((*(byte *)(__ptr + 7) & 1) != 0) {
      _ZdlPv((void *)__ptr[9]);
    }
    *__ptr = &PTR_FUN_00c6eac0;
    if ((*(byte *)(__ptr + 4) & 1) != 0) {
      _ZdlPv((void *)__ptr[6]);
    }
                    /* try { // try from 007aed18 to 008aed2b has its CatchHandler @ 007af3d4 */
    if ((*(byte *)(__ptr + 1) & 1) != 0) {
      _ZdlPv((void *)__ptr[3]);
    }
                    /* try { // try from 007aed2c to 008aed3f has its CatchHandler @ 007af3b8 */
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007aeccc"></a> `007aeccc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007aecd0"></a> `007aecd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aecd4"></a> `007aecd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007aecd8"></a> `007aecd8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-007aecdc"></a> `007aecdc` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-007aece0"></a> `007aece0` | `b3 02 00 b4` | cbz x19,0x007aed34 | `CONDITIONAL_JUMP`
<a id="insn-007aece4"></a> `007aece4` | `68 e2 40 39` | ldrb w8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-007aece8"></a> `007aece8` | `68 00 00 36` | tbz w8,#0x0,0x007aecf4 | `CONDITIONAL_JUMP`
<a id="insn-007aecec"></a> `007aecec` | `60 26 40 f9` | ldr x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-007aecf0"></a> `007aecf0` | `98 a8 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007aecf4"></a> `007aecf4` | `08 26 00 90` | adrp x8,0xc6e000 | `FALL_THROUGH`
<a id="insn-007aecf8"></a> `007aecf8` | `08 c1 2a 91` | add x8,x8,#0xab0 | `FALL_THROUGH`
<a id="insn-007aecfc"></a> `007aecfc` | `69 82 40 39` | ldrb w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007aed00"></a> `007aed00` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-007aed04"></a> `007aed04` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-007aed08"></a> `007aed08` | `69 00 00 36` | tbz w9,#0x0,0x007aed14 | `CONDITIONAL_JUMP`
<a id="insn-007aed0c"></a> `007aed0c` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007aed10"></a> `007aed10` | `90 a8 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007aed14"></a> `007aed14` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007aed18"></a> `007aed18` | `68 00 00 36` | tbz w8,#0x0,0x007aed24 | `CONDITIONAL_JUMP`
<a id="insn-007aed1c"></a> `007aed1c` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-007aed20"></a> `007aed20` | `8c a8 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007aed24"></a> `007aed24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007aed28"></a> `007aed28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aed2c"></a> `007aed2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007aed30"></a> `007aed30` | `88 a8 12 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-007aed34"></a> `007aed34` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aed38"></a> `007aed38` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007aed3c"></a> `007aed3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007aeccc`](#insn-007aeccc) 範囲 `[['007aeccc', '007aece3']]`
  - `CONDITIONAL_JUMP` [`007aece0`](#insn-007aece0) → [`007aed34`](#insn-007aed34)
  - `FALL_THROUGH` [`007aece0`](#insn-007aece0) → [`007aece4`](#insn-007aece4)
- ブロック [`007aece4`](#insn-007aece4) 範囲 `[['007aece4', '007aeceb']]`
  - `CONDITIONAL_JUMP` [`007aece8`](#insn-007aece8) → [`007aecf4`](#insn-007aecf4)
  - `FALL_THROUGH` [`007aece8`](#insn-007aece8) → [`007aecec`](#insn-007aecec)
- ブロック [`007aecec`](#insn-007aecec) 範囲 `[['007aecec', '007aecf3']]`
  - `FALL_THROUGH` [`007aecf0`](#insn-007aecf0) → [`007aecf4`](#insn-007aecf4)
- ブロック [`007aecf4`](#insn-007aecf4) 範囲 `[['007aecf4', '007aed0b']]`
  - `CONDITIONAL_JUMP` [`007aed08`](#insn-007aed08) → [`007aed14`](#insn-007aed14)
  - `FALL_THROUGH` [`007aed08`](#insn-007aed08) → [`007aed0c`](#insn-007aed0c)
- ブロック [`007aed0c`](#insn-007aed0c) 範囲 `[['007aed0c', '007aed13']]`
  - `FALL_THROUGH` [`007aed10`](#insn-007aed10) → [`007aed14`](#insn-007aed14)
- ブロック [`007aed14`](#insn-007aed14) 範囲 `[['007aed14', '007aed17']]`
  - `FALL_THROUGH` [`007aed14`](#insn-007aed14) → [`007aed18`](#insn-007aed18)
- ブロック [`007aed18`](#insn-007aed18) 範囲 `[['007aed18', '007aed1b']]`
  - `CONDITIONAL_JUMP` [`007aed18`](#insn-007aed18) → [`007aed24`](#insn-007aed24)
  - `FALL_THROUGH` [`007aed18`](#insn-007aed18) → [`007aed1c`](#insn-007aed1c)
- ブロック [`007aed1c`](#insn-007aed1c) 範囲 `[['007aed1c', '007aed23']]`
  - `FALL_THROUGH` [`007aed20`](#insn-007aed20) → [`007aed24`](#insn-007aed24)
- ブロック [`007aed24`](#insn-007aed24) 範囲 `[['007aed24', '007aed2b']]`
  - `FALL_THROUGH` [`007aed28`](#insn-007aed28) → [`007aed2c`](#insn-007aed2c)
- ブロック [`007aed2c`](#insn-007aed2c) 範囲 `[['007aed2c', '007aed33']]`
- ブロック [`007aed34`](#insn-007aed34) 範囲 `[['007aed34', '007aed3f']]`

## 命令位置別の参照

- [`007aeccc`](#insn-007aeccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aecd0`](#insn-007aecd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aece0`](#insn-007aece0) → [`007aed34`](#insn-007aed34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aece8`](#insn-007aece8) → [`007aecf4`](#insn-007aecf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aecf0`](#insn-007aecf0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007aed04`](#insn-007aed04) → `00c6eac0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007aed08`](#insn-007aed08) → [`007aed14`](#insn-007aed14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aed10`](#insn-007aed10) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007aed18`](#insn-007aed18) → [`007aed24`](#insn-007aed24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aed20`](#insn-007aed20) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007aed28`](#insn-007aed28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aed2c`](#insn-007aed2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aed30`](#insn-007aed30) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007aed34`](#insn-007aed34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aed38`](#insn-007aed38) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007aeccc`](#insn-007aeccc)

~~~json
{
  "source": "007aeccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aecd0`](#insn-007aecd0)

~~~json
{
  "source": "007aecd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aece0`](#insn-007aece0)

~~~json
{
  "source": "007aece0",
  "target": "007aed34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aece8`](#insn-007aece8)

~~~json
{
  "source": "007aece8",
  "target": "007aecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aecf0`](#insn-007aecf0)

~~~json
{
  "source": "007aecf0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aed04`](#insn-007aed04)

~~~json
{
  "source": "007aed04",
  "target": "00c6eac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6eac0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007aed08`](#insn-007aed08)

~~~json
{
  "source": "007aed08",
  "target": "007aed14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aed10`](#insn-007aed10)

~~~json
{
  "source": "007aed10",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aed18`](#insn-007aed18)

~~~json
{
  "source": "007aed18",
  "target": "007aed24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aed20`](#insn-007aed20)

~~~json
{
  "source": "007aed20",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aed28`](#insn-007aed28)

~~~json
{
  "source": "007aed28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aed2c`](#insn-007aed2c)

~~~json
{
  "source": "007aed2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aed30`](#insn-007aed30)

~~~json
{
  "source": "007aed30",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aed34`](#insn-007aed34)

~~~json
{
  "source": "007aed34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aed38`](#insn-007aed38)

~~~json
{
  "source": "007aed38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
