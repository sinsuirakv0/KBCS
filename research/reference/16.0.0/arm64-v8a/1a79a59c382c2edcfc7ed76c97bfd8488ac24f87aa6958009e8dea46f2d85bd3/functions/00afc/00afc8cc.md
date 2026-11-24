# 00afc8cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0019.md#review-e0dace160e8984d29ee1fd37d4efcdcc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afccf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afccf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-8e28121241c599fda57140b7cf20b127)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc8cc",
  "name": "FUN_00afc8cc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9db48495f1681376fffa10ddce01002b27285bd9051141faf644fb37ad32507b",
  "source_text_sha256": "9db48495f1681376fffa10ddce01002b27285bd9051141faf644fb37ad32507b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc8cc",
        "00afc913"
      ]
    ],
    "bytes_sha256": "599dcb05cb9c39f9cb7118e865b36eb07412acc99c8d3990703bbeca9233639e",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 444 bytes

~~~c

bool FUN_00afc8cc(int param_1,int param_2)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afbea4 with catch @ 00afc8d8 */
                    /* catch() { ... } // from try @ 00afb88c with catch @ 00afc8dc */
  lVar1 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00afb840 with catch @ 00afc8f8 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c34) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc8cc"></a> `00afc8cc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afc8d0"></a> `00afc8d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc8d4"></a> `00afc8d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afc8d8"></a> `00afc8d8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afc8dc"></a> `00afc8dc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afc8e0"></a> `00afc8e0` | `f6 52 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afc8e4"></a> `00afc8e4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afc8e8"></a> `00afc8e8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afc8ec"></a> `00afc8ec` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afc8f0"></a> `00afc8f0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afc8f4"></a> `00afc8f4` | `89 86 89 52` | mov w9,#0x4c34 | `FALL_THROUGH`
<a id="insn-00afc8f8"></a> `00afc8f8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afc8fc"></a> `00afc8fc` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afc900"></a> `00afc900` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afc904"></a> `00afc904` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afc908"></a> `00afc908` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc90c"></a> `00afc90c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afc910"></a> `00afc910` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc8cc`](#insn-00afc8cc) 範囲 `[['00afc8cc', '00afc8d7']]`
  - `FALL_THROUGH` [`00afc8d4`](#insn-00afc8d4) → [`00afc8d8`](#insn-00afc8d8)
- ブロック [`00afc8d8`](#insn-00afc8d8) 範囲 `[['00afc8d8', '00afc8db']]`
  - `FALL_THROUGH` [`00afc8d8`](#insn-00afc8d8) → [`00afc8dc`](#insn-00afc8dc)
- ブロック [`00afc8dc`](#insn-00afc8dc) 範囲 `[['00afc8dc', '00afc8f7']]`
  - `FALL_THROUGH` [`00afc8f4`](#insn-00afc8f4) → [`00afc8f8`](#insn-00afc8f8)
- ブロック [`00afc8f8`](#insn-00afc8f8) 範囲 `[['00afc8f8', '00afc913']]`

## 命令位置別の参照

- [`00afc8cc`](#insn-00afc8cc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc8d0`](#insn-00afc8d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc8e0`](#insn-00afc8e0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afc908`](#insn-00afc908) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc90c`](#insn-00afc90c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc8cc`](#insn-00afc8cc)

~~~json
{
  "source": "00afc8cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc8d0`](#insn-00afc8d0)

~~~json
{
  "source": "00afc8d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc8e0`](#insn-00afc8e0)

~~~json
{
  "source": "00afc8e0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc908`](#insn-00afc908)

~~~json
{
  "source": "00afc908",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc90c`](#insn-00afc90c)

~~~json
{
  "source": "00afc90c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
