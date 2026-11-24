# 00af7fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0016.md#review-4de4b8127facc2cba0e999aebb81b3a1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af8404`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8404.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-cff7af2b27b14338d89023494e897846)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7fdc",
  "name": "FUN_00af7fdc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e390f4dbb6af2ba71b3a23792b8b149feb32171f0c859ff8a7568f92a78ff83",
  "source_text_sha256": "4e390f4dbb6af2ba71b3a23792b8b149feb32171f0c859ff8a7568f92a78ff83",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af7fdc",
        "00af8027"
      ]
    ],
    "bytes_sha256": "a91453217d912c3622f6f38eff9549800ca3d1e4a36c74f705ed500be4784e09",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af7fdc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af7ff0 to 00bf7ff3 has its CatchHandler @ 00af83f4 */
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b8c) = param_3;
                    /* try { // try from 00af8018 to 00bf803b has its CatchHandler @ 00af8358 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af7fdc"></a> `00af7fdc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af7fe0"></a> `00af7fe0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7fe4"></a> `00af7fe4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7fe8"></a> `00af7fe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af7fec"></a> `00af7fec` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af7ff0"></a> `00af7ff0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af7ff4"></a> `00af7ff4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af7ff8"></a> `00af7ff8` | `30 65 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af7ffc"></a> `00af7ffc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af8000"></a> `00af8000` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af8004"></a> `00af8004` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af8008"></a> `00af8008` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af800c"></a> `00af800c` | `89 71 89 52` | mov w9,#0x4b8c | `FALL_THROUGH`
<a id="insn-00af8010"></a> `00af8010` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af8014"></a> `00af8014` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af8018"></a> `00af8018` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af801c"></a> `00af801c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8020"></a> `00af8020` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af8024"></a> `00af8024` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af7fdc`](#insn-00af7fdc) 範囲 `[['00af7fdc', '00af7fef']]`
  - `FALL_THROUGH` [`00af7fec`](#insn-00af7fec) → [`00af7ff0`](#insn-00af7ff0)
- ブロック [`00af7ff0`](#insn-00af7ff0) 範囲 `[['00af7ff0', '00af8017']]`
  - `FALL_THROUGH` [`00af8014`](#insn-00af8014) → [`00af8018`](#insn-00af8018)
- ブロック [`00af8018`](#insn-00af8018) 範囲 `[['00af8018', '00af8027']]`

## 命令位置別の参照

- [`00af7fdc`](#insn-00af7fdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fe0`](#insn-00af7fe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7fe4`](#insn-00af7fe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ff8`](#insn-00af7ff8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af8018`](#insn-00af8018) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af801c`](#insn-00af801c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8020`](#insn-00af8020) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af7fdc`](#insn-00af7fdc)

~~~json
{
  "source": "00af7fdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fe0`](#insn-00af7fe0)

~~~json
{
  "source": "00af7fe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7fe4`](#insn-00af7fe4)

~~~json
{
  "source": "00af7fe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ff8`](#insn-00af7ff8)

~~~json
{
  "source": "00af7ff8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af8018`](#insn-00af8018)

~~~json
{
  "source": "00af8018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af801c`](#insn-00af801c)

~~~json
{
  "source": "00af801c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8020`](#insn-00af8020)

~~~json
{
  "source": "00af8020",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
