# 00bf9cbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0175.md#review-b9cca1fa3ad619285faa6cb3bf96fa01)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa0e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa0e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-9f9dc9eeb6409c68dee4363b1c2ff879)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9cbc",
  "name": "FUN_00bf9cbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e2f0b70ffd2c194d7ace2e000c4c6d3912749592e02208c0ac1286a40399a71",
  "source_text_sha256": "2e2f0b70ffd2c194d7ace2e000c4c6d3912749592e02208c0ac1286a40399a71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf9cbc",
        "00bf9ce7"
      ]
    ],
    "bytes_sha256": "e26d050abba71c52f282a63c5c68f583fd9d98b0eecbaf79ccebc44da0ef5b8d",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5daf0](../00c5d/00c5daf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_00bf9cbc(void *param_1)

{
  _ZNSt6__ndk114error_categoryD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf9cbc"></a> `00bf9cbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf9cc0"></a> `00bf9cc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bf9cc4"></a> `00bf9cc4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9cc8"></a> `00bf9cc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf9ccc"></a> `00bf9ccc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf9cd0"></a> `00bf9cd0` | `88 8f 01 94` | bl 0x00c5daf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf9cd4"></a> `00bf9cd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf9cd8"></a> `00bf9cd8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf9cdc"></a> `00bf9cdc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bf9ce0"></a> `00bf9ce0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf9ce4"></a> `00bf9ce4` | `73 77 01 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf9cbc`](#insn-00bf9cbc) 範囲 `[['00bf9cbc', '00bf9ce7']]`

## 命令位置別の参照

- [`00bf9cc0`](#insn-00bf9cc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9cc4`](#insn-00bf9cc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9cd0`](#insn-00bf9cd0) → [`00c5daf0`](../00c5d/00c5daf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5daf0` · 推定シンボル `None` · 推定型 `None`
- [`00bf9cd8`](#insn-00bf9cd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9cdc`](#insn-00bf9cdc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf9ce4`](#insn-00bf9ce4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf9cc0`](#insn-00bf9cc0)

~~~json
{
  "source": "00bf9cc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9cc4`](#insn-00bf9cc4)

~~~json
{
  "source": "00bf9cc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9cd0`](#insn-00bf9cd0)

~~~json
{
  "source": "00bf9cd0",
  "target": "00c5daf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf9cd8`](#insn-00bf9cd8)

~~~json
{
  "source": "00bf9cd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9cdc`](#insn-00bf9cdc)

~~~json
{
  "source": "00bf9cdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf9ce4`](#insn-00bf9ce4)

~~~json
{
  "source": "00bf9ce4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
