# 00afaac8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afa6a0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa6a0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-568056fa1ac927134ca82edaeafcef77)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afab64`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afab64.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-78e7575c2c58fda1fd38e01e39366595)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaac8",
  "name": "FUN_00afaac8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6c21cb668c2a71ffc69098409a9a955156d34c9c33575451003af9c5bb8ea3c",
  "source_text_sha256": "a6c21cb668c2a71ffc69098409a9a955156d34c9c33575451003af9c5bb8ea3c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaac8",
        "00afab0f"
      ]
    ],
    "bytes_sha256": "671f063892fa21b291db7525786a364f8dbaf28fee70e9a7110192c792e208f0",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f7940](../005f7/005f7940.md)
- [005fb93c](../005fb/005fb93c.md)
- [00714be8](../00714/00714be8.md)
- [00714db8](../00714/00714db8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1047 bytes

~~~c

bool FUN_00afaac8(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afa068 with catch @ 00afaac8 */
                    /* catch() { ... } // from try @ 00afa058 with catch @ 00afaacc */
                    /* catch() { ... } // from try @ 00af9fe4 with catch @ 00afaad0 */
  lVar1 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00af9fd4 with catch @ 00afaae8 */
                    /* catch() { ... } // from try @ 00afa5f4 with catch @ 00afab00 */
                    /* catch() { ... } // from try @ 00afa5c4 with catch @ 00afab04
                       catch() { ... } // from try @ 00afa690 with catch @ 00afab04 */
                    /* catch() { ... } // from try @ 00afa3e8 with catch @ 00afab08 */
                    /* catch() { ... } // from try @ 00afa3b8 with catch @ 00afab0c
                       catch() { ... } // from try @ 00afa494 with catch @ 00afab0c */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a24) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaac8"></a> `00afaac8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afaacc"></a> `00afaacc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaad0"></a> `00afaad0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaad4"></a> `00afaad4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaad8"></a> `00afaad8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaadc"></a> `00afaadc` | `87 5a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afaae0"></a> `00afaae0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaae4"></a> `00afaae4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaae8"></a> `00afaae8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaaec"></a> `00afaaec` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaaf0"></a> `00afaaf0` | `89 44 89 52` | mov w9,#0x4a24 | `FALL_THROUGH`
<a id="insn-00afaaf4"></a> `00afaaf4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaaf8"></a> `00afaaf8` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afab00"></a> `00afab00` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afab04"></a> `00afab04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaac8`](#insn-00afaac8) 範囲 `[['00afaac8', '00afaacb']]`
  - `FALL_THROUGH` [`00afaac8`](#insn-00afaac8) → [`00afaacc`](#insn-00afaacc)
- ブロック [`00afaacc`](#insn-00afaacc) 範囲 `[['00afaacc', '00afaacf']]`
  - `FALL_THROUGH` [`00afaacc`](#insn-00afaacc) → [`00afaad0`](#insn-00afaad0)
- ブロック [`00afaad0`](#insn-00afaad0) 範囲 `[['00afaad0', '00afaae7']]`
  - `FALL_THROUGH` [`00afaae4`](#insn-00afaae4) → [`00afaae8`](#insn-00afaae8)
- ブロック [`00afaae8`](#insn-00afaae8) 範囲 `[['00afaae8', '00afaaff']]`
  - `FALL_THROUGH` [`00afaafc`](#insn-00afaafc) → [`00afab00`](#insn-00afab00)
- ブロック [`00afab00`](#insn-00afab00) 範囲 `[['00afab00', '00afab03']]`
  - `FALL_THROUGH` [`00afab00`](#insn-00afab00) → [`00afab04`](#insn-00afab04)
- ブロック [`00afab04`](#insn-00afab04) 範囲 `[['00afab04', '00afab07']]`
  - `FALL_THROUGH` [`00afab04`](#insn-00afab04) → [`00afab08`](#insn-00afab08)
- ブロック [`00afab08`](#insn-00afab08) 範囲 `[['00afab08', '00afab0b']]`
  - `FALL_THROUGH` [`00afab08`](#insn-00afab08) → [`00afab0c`](#insn-00afab0c)
- ブロック [`00afab0c`](#insn-00afab0c) 範囲 `[['00afab0c', '00afab0f']]`

## 命令位置別の参照

- [`00afaac8`](#insn-00afaac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaacc`](#insn-00afaacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaadc`](#insn-00afaadc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afab04`](#insn-00afab04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab08`](#insn-00afab08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaac8`](#insn-00afaac8)

~~~json
{
  "source": "00afaac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaacc`](#insn-00afaacc)

~~~json
{
  "source": "00afaacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaadc`](#insn-00afaadc)

~~~json
{
  "source": "00afaadc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab04`](#insn-00afab04)

~~~json
{
  "source": "00afab04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab08`](#insn-00afab08)

~~~json
{
  "source": "00afab08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
