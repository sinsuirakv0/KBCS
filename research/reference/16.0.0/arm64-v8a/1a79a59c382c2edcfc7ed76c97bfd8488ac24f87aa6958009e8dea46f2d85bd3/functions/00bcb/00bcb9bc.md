# 00bcb9bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c4bc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-cc6b24f09debd7185948192d181e216e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbde4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbde4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c767a083e76b5ee6c0fa601c32945be0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb9bc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a16434114214babe0d0ae237d786a4716f90b2e7ea07bbe16fe7d6677f00195",
  "source_text_sha256": "7a16434114214babe0d0ae237d786a4716f90b2e7ea07bbe16fe7d6677f00195",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb9bc",
        "00bcb9fb"
      ]
    ],
    "bytes_sha256": "8eacac51e59bde5c04adb3c11c886d31058e105ebf12af73598fd2217db70550",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d6c0](../00c5d/00c5d6c0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c5d6c0](../00c5d/00c5d6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 959 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
                    /* try { // try from 00bcb9cc to 00ccb9d7 has its CatchHandler @ 00bcba30 */
                    /* try { // try from 00bcb9d8 to 00ccba57 has its CatchHandler @ 00bcb960 */
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
<a id="insn-00bcb9bc"></a> `00bcb9bc` | `e1 01 00 b4` | cbz x1,0x00bcb9f8 | `CONDITIONAL_JUMP`
<a id="insn-00bcb9c0"></a> `00bcb9c0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcb9c4"></a> `00bcb9c4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb9c8"></a> `00bcb9c8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcb9cc"></a> `00bcb9cc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcb9d0"></a> `00bcb9d0` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00bcb9d4"></a> `00bcb9d4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcb9d8"></a> `00bcb9d8` | `3a 47 02 94` | bl 0x00c5d6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb9dc"></a> `00bcb9dc` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb9e0"></a> `00bcb9e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcb9e4"></a> `00bcb9e4` | `37 47 02 94` | bl 0x00c5d6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb9e8"></a> `00bcb9e8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb9ec"></a> `00bcb9ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb9f0"></a> `00bcb9f0` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcb9f4"></a> `00bcb9f4` | `2f 30 02 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00bcb9f8"></a> `00bcb9f8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb9bc`](#insn-00bcb9bc) 範囲 `[['00bcb9bc', '00bcb9bf']]`
  - `CONDITIONAL_JUMP` [`00bcb9bc`](#insn-00bcb9bc) → [`00bcb9f8`](#insn-00bcb9f8)
  - `FALL_THROUGH` [`00bcb9bc`](#insn-00bcb9bc) → [`00bcb9c0`](#insn-00bcb9c0)
- ブロック [`00bcb9c0`](#insn-00bcb9c0) 範囲 `[['00bcb9c0', '00bcb9cb']]`
  - `FALL_THROUGH` [`00bcb9c8`](#insn-00bcb9c8) → [`00bcb9cc`](#insn-00bcb9cc)
- ブロック [`00bcb9cc`](#insn-00bcb9cc) 範囲 `[['00bcb9cc', '00bcb9d7']]`
  - `FALL_THROUGH` [`00bcb9d4`](#insn-00bcb9d4) → [`00bcb9d8`](#insn-00bcb9d8)
- ブロック [`00bcb9d8`](#insn-00bcb9d8) 範囲 `[['00bcb9d8', '00bcb9f7']]`
- ブロック [`00bcb9f8`](#insn-00bcb9f8) 範囲 `[['00bcb9f8', '00bcb9fb']]`

## 命令位置別の参照

- [`00bcb9bc`](#insn-00bcb9bc) → [`00bcb9f8`](#insn-00bcb9f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9c0`](#insn-00bcb9c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9c4`](#insn-00bcb9c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9d8`](#insn-00bcb9d8) → [`00c5d6c0`](../00c5d/00c5d6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9e4`](#insn-00bcb9e4) → [`00c5d6c0`](../00c5d/00c5d6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9e8`](#insn-00bcb9e8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb9f4`](#insn-00bcb9f4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb9bc`](#insn-00bcb9bc)

~~~json
{
  "source": "00bcb9bc",
  "target": "00bcb9f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb9c0`](#insn-00bcb9c0)

~~~json
{
  "source": "00bcb9c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb9c4`](#insn-00bcb9c4)

~~~json
{
  "source": "00bcb9c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb9d8`](#insn-00bcb9d8)

~~~json
{
  "source": "00bcb9d8",
  "target": "00c5d6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb9e4`](#insn-00bcb9e4)

~~~json
{
  "source": "00bcb9e4",
  "target": "00c5d6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb9e8`](#insn-00bcb9e8)

~~~json
{
  "source": "00bcb9e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb9f4`](#insn-00bcb9f4)

~~~json
{
  "source": "00bcb9f4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
