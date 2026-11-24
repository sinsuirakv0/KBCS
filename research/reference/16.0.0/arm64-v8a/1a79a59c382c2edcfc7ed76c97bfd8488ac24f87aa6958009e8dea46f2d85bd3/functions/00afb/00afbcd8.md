# 00afbcd8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-5d27ad2e4cb5b52ed1b3d4cd3d6bce9c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afc100`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc100.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-9db4647bc394e46d1454fb4569068185)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbcd8",
  "name": "FUN_00afbcd8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f52fed429aa2388891a26de79ab0f6dd4ef3c7c08a91a974e420d1a2b160aa16",
  "source_text_sha256": "f52fed429aa2388891a26de79ab0f6dd4ef3c7c08a91a974e420d1a2b160aa16",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbcd8",
        "00afbd2b"
      ]
    ],
    "bytes_sha256": "ec543ec26593bce21d71a47710966a6f714dbcb001dd9845a83edc770dbd742a",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 345 bytes

~~~c

void FUN_00afbcd8(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbcd8 to 00bfbceb has its CatchHandler @ 00afcadc */
  lVar1 = FUN_008514b8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84b20) = *(int *)(lVar1 + 0x84b20) + param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbcd8"></a> `00afbcd8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbcdc"></a> `00afbcdc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbce0"></a> `00afbce0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbce4"></a> `00afbce4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbce8"></a> `00afbce8` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afbcec"></a> `00afbcec` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afbcf0"></a> `00afbcf0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afbcf4"></a> `00afbcf4` | `f1 55 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afbcf8"></a> `00afbcf8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbcfc"></a> `00afbcfc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbd00"></a> `00afbd00` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbd04"></a> `00afbd04` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbd08"></a> `00afbd08` | `09 64 89 52` | mov w9,#0x4b20 | `FALL_THROUGH`
<a id="insn-00afbd0c"></a> `00afbd0c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbd10"></a> `00afbd10` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbd14"></a> `00afbd14` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afbd18"></a> `00afbd18` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbd1c"></a> `00afbd1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbd20"></a> `00afbd20` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbd24"></a> `00afbd24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afbd28"></a> `00afbd28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbcd8`](#insn-00afbcd8) 範囲 `[['00afbcd8', '00afbd2b']]`

## 命令位置別の参照

- [`00afbcd8`](#insn-00afbcd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbcdc`](#insn-00afbcdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbce0`](#insn-00afbce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbcf4`](#insn-00afbcf4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afbd1c`](#insn-00afbd1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd20`](#insn-00afbd20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd24`](#insn-00afbd24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbcd8`](#insn-00afbcd8)

~~~json
{
  "source": "00afbcd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbcdc`](#insn-00afbcdc)

~~~json
{
  "source": "00afbcdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbce0`](#insn-00afbce0)

~~~json
{
  "source": "00afbce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbcf4`](#insn-00afbcf4)

~~~json
{
  "source": "00afbcf4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd1c`](#insn-00afbd1c)

~~~json
{
  "source": "00afbd1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd20`](#insn-00afbd20)

~~~json
{
  "source": "00afbd20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd24`](#insn-00afbd24)

~~~json
{
  "source": "00afbd24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
