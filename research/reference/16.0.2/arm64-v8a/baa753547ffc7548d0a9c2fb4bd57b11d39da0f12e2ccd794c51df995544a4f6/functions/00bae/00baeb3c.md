# 00baeb3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baeaa0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeaa0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-670c34508eee0e97947f2191fb5320ab)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bafb30`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb30.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-1a54fa52fa3e394018b59282db2cb94f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeb3c",
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
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeb3c",
        "00baeb7b"
      ]
    ],
    "bytes_sha256": "9295eab526f75ad44da95b475ffc00ac86431e2bb590945ef2cc767d56506ace",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d080](../00c5d/00c5d080.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5d080](../00c5d/00c5d080.md)

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
<a id="insn-00baeb3c"></a> `00baeb3c` | `e1 01 00 b4` | cbz x1,0x00baeb78 | `CONDITIONAL_JUMP`
<a id="insn-00baeb40"></a> `00baeb40` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baeb44"></a> `00baeb44` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeb48"></a> `00baeb48` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baeb4c"></a> `00baeb4c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baeb50"></a> `00baeb50` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00baeb54"></a> `00baeb54` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baeb58"></a> `00baeb58` | `4a b9 02 94` | bl 0x00c5d080 | `UNCONDITIONAL_CALL`
<a id="insn-00baeb5c"></a> `00baeb5c` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00baeb60"></a> `00baeb60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baeb64"></a> `00baeb64` | `47 b9 02 94` | bl 0x00c5d080 | `UNCONDITIONAL_CALL`
<a id="insn-00baeb68"></a> `00baeb68` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeb6c"></a> `00baeb6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baeb70"></a> `00baeb70` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baeb74"></a> `00baeb74` | `03 a5 02 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00baeb78"></a> `00baeb78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeb3c`](#insn-00baeb3c) 範囲 `[['00baeb3c', '00baeb3f']]`
  - `CONDITIONAL_JUMP` [`00baeb3c`](#insn-00baeb3c) → [`00baeb78`](#insn-00baeb78)
  - `FALL_THROUGH` [`00baeb3c`](#insn-00baeb3c) → [`00baeb40`](#insn-00baeb40)
- ブロック [`00baeb40`](#insn-00baeb40) 範囲 `[['00baeb40', '00baeb77']]`
- ブロック [`00baeb78`](#insn-00baeb78) 範囲 `[['00baeb78', '00baeb7b']]`

## 命令位置別の参照

- [`00baeb3c`](#insn-00baeb3c) → [`00baeb78`](#insn-00baeb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb40`](#insn-00baeb40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb44`](#insn-00baeb44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb58`](#insn-00baeb58) → [`00c5d080`](../00c5d/00c5d080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d080` · 推定シンボル `None` · 推定型 `None`
- [`00baeb64`](#insn-00baeb64) → [`00c5d080`](../00c5d/00c5d080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d080` · 推定シンボル `None` · 推定型 `None`
- [`00baeb68`](#insn-00baeb68) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb74`](#insn-00baeb74) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeb3c`](#insn-00baeb3c)

~~~json
{
  "source": "00baeb3c",
  "target": "00baeb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb40`](#insn-00baeb40)

~~~json
{
  "source": "00baeb40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb44`](#insn-00baeb44)

~~~json
{
  "source": "00baeb44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb58`](#insn-00baeb58)

~~~json
{
  "source": "00baeb58",
  "target": "00c5d080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeb64`](#insn-00baeb64)

~~~json
{
  "source": "00baeb64",
  "target": "00c5d080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeb68`](#insn-00baeb68)

~~~json
{
  "source": "00baeb68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb74`](#insn-00baeb74)

~~~json
{
  "source": "00baeb74",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
