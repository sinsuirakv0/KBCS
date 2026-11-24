# 00bcbde4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb9bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c767a083e76b5ee6c0fa601c32945be0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbe80`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-c52473b6a69a22026258f74bc1d2214f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbde4",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5b9dec41c134fa4358eab4193cf27bfd23899ea9708bb2bb33d35d2258dd330",
  "source_text_sha256": "c5b9dec41c134fa4358eab4193cf27bfd23899ea9708bb2bb33d35d2258dd330",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbde4",
        "00bcbe23"
      ]
    ],
    "bytes_sha256": "2a0d347888dd501026fe180f89c8ba3f9c990c67a94ab7c9e33306bda6469619",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dac0](../00c5d/00c5dac0.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5dac0](../00c5d/00c5dac0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 765 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
              (param_1,*param_2);
    _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
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
<a id="insn-00bcbde4"></a> `00bcbde4` | `e1 01 00 b4` | cbz x1,0x00bcbe20 | `CONDITIONAL_JUMP`
<a id="insn-00bcbde8"></a> `00bcbde8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbdec"></a> `00bcbdec` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbdf8"></a> `00bcbdf8` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00bcbdfc"></a> `00bcbdfc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbe00"></a> `00bcbe00` | `30 47 02 94` | bl 0x00c5dac0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbe04"></a> `00bcbe04` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe08"></a> `00bcbe08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbe0c"></a> `00bcbe0c` | `2d 47 02 94` | bl 0x00c5dac0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbe10"></a> `00bcbe10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe14"></a> `00bcbe14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbe18"></a> `00bcbe18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbe1c"></a> `00bcbe1c` | `25 30 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bcbe20"></a> `00bcbe20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbde4`](#insn-00bcbde4) 範囲 `[['00bcbde4', '00bcbde7']]`
  - `CONDITIONAL_JUMP` [`00bcbde4`](#insn-00bcbde4) → [`00bcbe20`](#insn-00bcbe20)
  - `FALL_THROUGH` [`00bcbde4`](#insn-00bcbde4) → [`00bcbde8`](#insn-00bcbde8)
- ブロック [`00bcbde8`](#insn-00bcbde8) 範囲 `[['00bcbde8', '00bcbe1f']]`
- ブロック [`00bcbe20`](#insn-00bcbe20) 範囲 `[['00bcbe20', '00bcbe23']]`

## 命令位置別の参照

- [`00bcbde4`](#insn-00bcbde4) → [`00bcbe20`](#insn-00bcbe20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde8`](#insn-00bcbde8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdec`](#insn-00bcbdec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe00`](#insn-00bcbe00) → [`00c5dac0`](../00c5d/00c5dac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dac0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe0c`](#insn-00bcbe0c) → [`00c5dac0`](../00c5d/00c5dac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dac0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe10`](#insn-00bcbe10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe1c`](#insn-00bcbe1c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbde4`](#insn-00bcbde4)

~~~json
{
  "source": "00bcbde4",
  "target": "00bcbe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbde8`](#insn-00bcbde8)

~~~json
{
  "source": "00bcbde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdec`](#insn-00bcbdec)

~~~json
{
  "source": "00bcbdec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe00`](#insn-00bcbe00)

~~~json
{
  "source": "00bcbe00",
  "target": "00c5dac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbe0c`](#insn-00bcbe0c)

~~~json
{
  "source": "00bcbe0c",
  "target": "00c5dac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbe10`](#insn-00bcbe10)

~~~json
{
  "source": "00bcbe10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe1c`](#insn-00bcbe1c)

~~~json
{
  "source": "00bcbe1c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
