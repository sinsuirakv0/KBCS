# 00a9cafc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a9cafc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9c/00a9cafc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0024.md#compare-c2d0ca9b4401cfb9f13b2b7da36cfc14)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a9cb40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9cb40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0003.md#compare-82b84860fd6bcdab82525d8f21426994)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9cafc",
  "name": "FUN_00a9cafc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24bcbf503c3e49725a49590c826b5fdd234f6947904c443a72f451529c136da9",
  "source_text_sha256": "24bcbf503c3e49725a49590c826b5fdd234f6947904c443a72f451529c136da9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9cafc",
        "00a9cb57"
      ]
    ],
    "bytes_sha256": "0d12767e13a8e65cf04b75aac64857349f1254f8353b66a82ac207e8ede44774",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006dde48](../006dd/006dde48.md)
- [006ddfb8](../006dd/006ddfb8.md)
- [006e3f80](../006e3/006e3f80.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 475 bytes

~~~c

undefined4 FUN_00a9cafc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00a9cb0c to 00b9cb0f has its CatchHandler @ 00a9d544 */
                    /* try { // try from 00a9cb10 to 00b9cb5b has its CatchHandler @ 00a9a654 */
  lVar1 = FUN_0081f580();
  return *(undefined4 *)
          (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec +
           (long)*(int *)(&DAT_002f4804 + (long)param_3 * 4) * 4 + 0x84080);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9cafc"></a> `00a9cafc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00a9cb00"></a> `00a9cb00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9cb04"></a> `00a9cb04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9cb08"></a> `00a9cb08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9cb0c"></a> `00a9cb0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00a9cb10"></a> `00a9cb10` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00a9cb14"></a> `00a9cb14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00a9cb18"></a> `00a9cb18` | `9a 0a f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9cb1c"></a> `00a9cb1c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9cb20"></a> `00a9cb20` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9cb24"></a> `00a9cb24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9cb28"></a> `00a9cb28` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9cb2c"></a> `00a9cb2c` | `c9 c2 ff 90` | adrp x9,0x2f4000 | `FALL_THROUGH`
<a id="insn-00a9cb30"></a> `00a9cb30` | `29 11 20 91` | add x9,x9,#0x804 | `FALL_THROUGH`
<a id="insn-00a9cb34"></a> `00a9cb34` | `29 d9 b3 b8` | ldrsw x9,[x9, w19, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00a9cb38"></a> `00a9cb38` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a9cb3c"></a> `00a9cb3c` | `09 10 88 52` | mov w9,#0x4080 | `FALL_THROUGH`
<a id="insn-00a9cb40"></a> `00a9cb40` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9cb44"></a> `00a9cb44` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9cb48"></a> `00a9cb48` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9cb4c"></a> `00a9cb4c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9cb50"></a> `00a9cb50` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00a9cb54"></a> `00a9cb54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9cafc`](#insn-00a9cafc) 範囲 `[['00a9cafc', '00a9cb0b']]`
  - `FALL_THROUGH` [`00a9cb08`](#insn-00a9cb08) → [`00a9cb0c`](#insn-00a9cb0c)
- ブロック [`00a9cb0c`](#insn-00a9cb0c) 範囲 `[['00a9cb0c', '00a9cb0f']]`
  - `FALL_THROUGH` [`00a9cb0c`](#insn-00a9cb0c) → [`00a9cb10`](#insn-00a9cb10)
- ブロック [`00a9cb10`](#insn-00a9cb10) 範囲 `[['00a9cb10', '00a9cb57']]`

## 命令位置別の参照

- [`00a9cafc`](#insn-00a9cafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb00`](#insn-00a9cb00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb04`](#insn-00a9cb04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb18`](#insn-00a9cb18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb34`](#insn-00a9cb34) → `002f4804`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb48`](#insn-00a9cb48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb4c`](#insn-00a9cb4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cb50`](#insn-00a9cb50) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9cafc`](#insn-00a9cafc)

~~~json
{
  "source": "00a9cafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb00`](#insn-00a9cb00)

~~~json
{
  "source": "00a9cb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb04`](#insn-00a9cb04)

~~~json
{
  "source": "00a9cb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb18`](#insn-00a9cb18)

~~~json
{
  "source": "00a9cb18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9cb34`](#insn-00a9cb34)

~~~json
{
  "source": "00a9cb34",
  "target": "002f4804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb48`](#insn-00a9cb48)

~~~json
{
  "source": "00a9cb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb4c`](#insn-00a9cb4c)

~~~json
{
  "source": "00a9cb4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cb50`](#insn-00a9cb50)

~~~json
{
  "source": "00a9cb50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
