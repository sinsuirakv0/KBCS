# 00a9cbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9cbb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cbb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0003.md#compare-80255d228840b4801a1255f96ff7406f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0087.md#review-456f9c90d82fe73094363bc15a24bd5a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9cbfc",
  "name": "FUN_00a9cbfc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "813a2665583b1c4393a6ad8465b4d66279cb28055239f919113b6f7d5a3fe335",
  "source_text_sha256": "813a2665583b1c4393a6ad8465b4d66279cb28055239f919113b6f7d5a3fe335",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9cbfc",
        "00a9cc43"
      ]
    ],
    "bytes_sha256": "693f0a0228753212136ae586f9a3e2eeb70259bf5928018814d5b86cbe2178b6",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00a9cbfc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84318) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9cbfc"></a> `00a9cbfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a9cc00"></a> `00a9cc00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9cc04"></a> `00a9cc04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9cc08"></a> `00a9cc08` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00a9cc0c"></a> `00a9cc0c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9cc10"></a> `00a9cc10` | `5c 0a f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9cc14"></a> `00a9cc14` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9cc18"></a> `00a9cc18` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9cc1c"></a> `00a9cc1c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9cc20"></a> `00a9cc20` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9cc24"></a> `00a9cc24` | `09 63 88 52` | mov w9,#0x4318 | `FALL_THROUGH`
<a id="insn-00a9cc28"></a> `00a9cc28` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9cc2c"></a> `00a9cc2c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9cc30"></a> `00a9cc30` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00a9cc34"></a> `00a9cc34` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00a9cc38"></a> `00a9cc38` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9cc3c"></a> `00a9cc3c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a9cc40"></a> `00a9cc40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9cbfc`](#insn-00a9cbfc) 範囲 `[['00a9cbfc', '00a9cc43']]`

## 命令位置別の参照

- [`00a9cbfc`](#insn-00a9cbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cc00`](#insn-00a9cc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cc10`](#insn-00a9cc10) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9cc38`](#insn-00a9cc38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9cc3c`](#insn-00a9cc3c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9cbfc`](#insn-00a9cbfc)

~~~json
{
  "source": "00a9cbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cc00`](#insn-00a9cc00)

~~~json
{
  "source": "00a9cc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cc10`](#insn-00a9cc10)

~~~json
{
  "source": "00a9cc10",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9cc38`](#insn-00a9cc38)

~~~json
{
  "source": "00a9cc38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9cc3c`](#insn-00a9cc3c)

~~~json
{
  "source": "00a9cc3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
