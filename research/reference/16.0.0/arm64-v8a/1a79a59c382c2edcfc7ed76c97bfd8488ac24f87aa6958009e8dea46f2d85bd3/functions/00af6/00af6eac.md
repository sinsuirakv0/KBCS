# 00af6eac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0167.md#review-7b1ead3e5f9480a9022999a85c81e258)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af72d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-7acf184901032ebdf927560eb14f9757)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af6eac",
  "name": "FUN_00af6eac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbe168a32f99fa8d4cf3caea128ac93f7e9871227b125a970da60f5e386bb30e",
  "source_text_sha256": "bbe168a32f99fa8d4cf3caea128ac93f7e9871227b125a970da60f5e386bb30e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af6eac",
        "00af6ef3"
      ]
    ],
    "bytes_sha256": "ffd3a51b4b8329065bb1580b691e743a55b16ea84ce1d7695812116533bb2dd4",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ea1c](../0070e/0070ea1c.md)
- [007119b0](../00711/007119b0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 280 bytes

~~~c

bool FUN_00af6eac(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00af6ebc to 00bf6f07 has its CatchHandler @ 00af728c */
  lVar1 = FUN_008514b8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c98) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af6eac"></a> `00af6eac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af6eb0"></a> `00af6eb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6eb4"></a> `00af6eb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af6eb8"></a> `00af6eb8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af6ebc"></a> `00af6ebc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af6ec0"></a> `00af6ec0` | `7e 69 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af6ec4"></a> `00af6ec4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af6ec8"></a> `00af6ec8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af6ecc"></a> `00af6ecc` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af6ed0"></a> `00af6ed0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af6ed4"></a> `00af6ed4` | `09 93 89 52` | mov w9,#0x4c98 | `FALL_THROUGH`
<a id="insn-00af6ed8"></a> `00af6ed8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af6edc"></a> `00af6edc` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af6ee0"></a> `00af6ee0` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af6ee4"></a> `00af6ee4` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00af6ee8"></a> `00af6ee8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6eec"></a> `00af6eec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af6ef0"></a> `00af6ef0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af6eac`](#insn-00af6eac) 範囲 `[['00af6eac', '00af6ebb']]`
  - `FALL_THROUGH` [`00af6eb8`](#insn-00af6eb8) → [`00af6ebc`](#insn-00af6ebc)
- ブロック [`00af6ebc`](#insn-00af6ebc) 範囲 `[['00af6ebc', '00af6ef3']]`

## 命令位置別の参照

- [`00af6eac`](#insn-00af6eac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6eb0`](#insn-00af6eb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6ec0`](#insn-00af6ec0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af6ee8`](#insn-00af6ee8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6eec`](#insn-00af6eec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af6eac`](#insn-00af6eac)

~~~json
{
  "source": "00af6eac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6eb0`](#insn-00af6eb0)

~~~json
{
  "source": "00af6eb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6ec0`](#insn-00af6ec0)

~~~json
{
  "source": "00af6ec0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6ee8`](#insn-00af6ee8)

~~~json
{
  "source": "00af6ee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6eec`](#insn-00af6eec)

~~~json
{
  "source": "00af6eec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
