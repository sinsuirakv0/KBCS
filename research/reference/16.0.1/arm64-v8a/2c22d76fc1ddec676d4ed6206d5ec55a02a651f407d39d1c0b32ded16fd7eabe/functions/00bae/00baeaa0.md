# 00baeaa0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bae678`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae678.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-ffb6c09e3725ab68cee8fe0e8ce9f0ad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baeb3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-670c34508eee0e97947f2191fb5320ab)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeaa0",
  "name": "_ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82ebf1a068c0c6901ca3b65dd23ed6e7b5db7c633352f2a184ffe9f5f5ff060f",
  "source_text_sha256": "82ebf1a068c0c6901ca3b65dd23ed6e7b5db7c633352f2a184ffe9f5f5ff060f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeaa0",
        "00baeadf"
      ]
    ],
    "bytes_sha256": "82f05c76667464c0e56532d59023a759f6abb69b3d89b12e0e67b8a6afc1e3ab",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cfb0](../00c5c/00c5cfb0.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5cfb0](../00c5c/00c5cfb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 651 bytes

~~~c

void _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
              (param_1,*param_2);
    _ZNSt6__ndk16__treeINS_4pairIN11flatbuffers8BaseTypeEPNS2_9StructDefEEENS_4lessIS6_EENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_PvEE
              (param_1,param_2[1]);
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baeaa0"></a> `00baeaa0` | `e1 01 00 b4` | cbz x1,0x00baeadc | `CONDITIONAL_JUMP`
<a id="insn-00baeaa4"></a> `00baeaa4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baeaa8"></a> `00baeaa8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeaac"></a> `00baeaac` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baeab0"></a> `00baeab0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baeab4"></a> `00baeab4` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00baeab8"></a> `00baeab8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baeabc"></a> `00baeabc` | `3d b9 02 94` | bl 0x00c5cfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00baeac0"></a> `00baeac0` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baeac4"></a> `00baeac4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baeac8"></a> `00baeac8` | `3a b9 02 94` | bl 0x00c5cfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00baeacc"></a> `00baeacc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baead0"></a> `00baead0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baead4"></a> `00baead4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baead8"></a> `00baead8` | `f6 a4 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00baeadc"></a> `00baeadc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeaa0`](#insn-00baeaa0) 範囲 `[['00baeaa0', '00baeaa3']]`
  - `CONDITIONAL_JUMP` [`00baeaa0`](#insn-00baeaa0) → [`00baeadc`](#insn-00baeadc)
  - `FALL_THROUGH` [`00baeaa0`](#insn-00baeaa0) → [`00baeaa4`](#insn-00baeaa4)
- ブロック [`00baeaa4`](#insn-00baeaa4) 範囲 `[['00baeaa4', '00baeadb']]`
- ブロック [`00baeadc`](#insn-00baeadc) 範囲 `[['00baeadc', '00baeadf']]`

## 命令位置別の参照

- [`00baeaa0`](#insn-00baeaa0) → [`00baeadc`](#insn-00baeadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeaa4`](#insn-00baeaa4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeaa8`](#insn-00baeaa8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeabc`](#insn-00baeabc) → [`00c5cfb0`](../00c5c/00c5cfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfb0` · 推定シンボル `None` · 推定型 `None`
- [`00baeac8`](#insn-00baeac8) → [`00c5cfb0`](../00c5c/00c5cfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfb0` · 推定シンボル `None` · 推定型 `None`
- [`00baeacc`](#insn-00baeacc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baead8`](#insn-00baead8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeaa0`](#insn-00baeaa0)

~~~json
{
  "source": "00baeaa0",
  "target": "00baeadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeaa4`](#insn-00baeaa4)

~~~json
{
  "source": "00baeaa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeaa8`](#insn-00baeaa8)

~~~json
{
  "source": "00baeaa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeabc`](#insn-00baeabc)

~~~json
{
  "source": "00baeabc",
  "target": "00c5cfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeac8`](#insn-00baeac8)

~~~json
{
  "source": "00baeac8",
  "target": "00c5cfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeacc`](#insn-00baeacc)

~~~json
{
  "source": "00baeacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baead8`](#insn-00baead8)

~~~json
{
  "source": "00baead8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
