# 00b2bffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acc56c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-021580ec0a2937dfb1c94c6e61cf85c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b2c424`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0068.md#compare-fce8402ab59a3fa2d6cd989ece756895)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2bffc",
  "name": "FUN_00b2bffc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64",
  "source_text_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2bffc",
        "00b2c027"
      ]
    ],
    "bytes_sha256": "46e7f80b40ff5861910bbc03edcb40802dfa98143113ff5fc6e955c965868e05",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0043b618](../0043b/0043b618.md)

## 呼び出し先

- [0043e90c](../0043e/0043e90c.md)
- [0043f4f4](../0043f/0043f4f4.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047b78c](../0047b/0047b78c.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 202 bytes

~~~c

void FUN_00b2bffc(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_008514b8();
  (**(code **)(*plVar1 + 0x28))();
  FUN_0047acb4();
  FUN_0047b78c();
  FUN_0043e90c();
  FUN_0043f4f4();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2bffc"></a> `00b2bffc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b2c000"></a> `00b2c000` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b2c004"></a> `00b2c004` | `2d 95 f4 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c008"></a> `00b2c008` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b2c00c"></a> `00b2c00c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b2c010"></a> `00b2c010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b2c014"></a> `00b2c014` | `28 3b e5 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2c018"></a> `00b2c018` | `dd 3d e5 97` | bl 0x0047b78c | `UNCONDITIONAL_CALL`
<a id="insn-00b2c01c"></a> `00b2c01c` | `3c 4a e4 97` | bl 0x0043e90c | `UNCONDITIONAL_CALL`
<a id="insn-00b2c020"></a> `00b2c020` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00b2c024"></a> `00b2c024` | `34 4d e4 17` | b 0x0043f4f4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2bffc`](#insn-00b2bffc) 範囲 `[['00b2bffc', '00b2c027']]`

## 命令位置別の参照

- [`00b2bffc`](#insn-00b2bffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c004`](#insn-00b2c004) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b2c014`](#insn-00b2c014) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00b2c018`](#insn-00b2c018) → [`0047b78c`](../0047b/0047b78c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b78c` · 推定シンボル `None` · 推定型 `None`
- [`00b2c01c`](#insn-00b2c01c) → [`0043e90c`](../0043e/0043e90c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043e90c` · 推定シンボル `None` · 推定型 `None`
- [`00b2c020`](#insn-00b2c020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2c024`](#insn-00b2c024) → [`0043f4f4`](../0043f/0043f4f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043f4f4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2bffc`](#insn-00b2bffc)

~~~json
{
  "source": "00b2bffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c004`](#insn-00b2c004)

~~~json
{
  "source": "00b2c004",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c014`](#insn-00b2c014)

~~~json
{
  "source": "00b2c014",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c018`](#insn-00b2c018)

~~~json
{
  "source": "00b2c018",
  "target": "0047b78c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c01c`](#insn-00b2c01c)

~~~json
{
  "source": "00b2c01c",
  "target": "0043e90c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2c020`](#insn-00b2c020)

~~~json
{
  "source": "00b2c020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2c024`](#insn-00b2c024)

~~~json
{
  "source": "00b2c024",
  "target": "0043f4f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
