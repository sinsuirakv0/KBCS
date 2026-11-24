# 00bfb0dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e694`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-f42dc1aac09226e1c304af9a933c717c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb504`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-54420962c985a2222da1dcf94c24819d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb0dc",
  "name": "_ZNSt6__ndk18ios_base5clearEj",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c561438effb3311149076e5bd3001bf8bf467dd2d836129baa92bfb3d1f620fb",
  "source_text_sha256": "c561438effb3311149076e5bd3001bf8bf467dd2d836129baa92bfb3d1f620fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb0dc",
        "00bfb11b"
      ]
    ],
    "bytes_sha256": "701a4af62a8cfd45d5a22c63df6e6601b7fb7ce41c8384e19ed8d3ac6b9d6e19",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57ea0](../00c57/00c57ea0.md)

## 呼び出し先

- [00bfb11c](../00bfb/00bfb11c.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZNSt6__ndk18ios_base5clearEj(long param_1,uint param_2)

{
  param_2 = *(long *)(param_1 + 0x28) == 0 | param_2;
  *(uint *)(param_1 + 0x20) = param_2;
  if ((*(uint *)(param_1 + 0x24) & param_2) == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bfb11c("ios_base::clear");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb0dc"></a> `00bfb0dc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfb0e0"></a> `00bfb0e0` | `08 14 40 f9` | ldr x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00bfb0e4"></a> `00bfb0e4` | `09 24 40 b9` | ldr w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfb0e8"></a> `00bfb0e8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bfb0ec"></a> `00bfb0ec` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bfb0f0"></a> `00bfb0f0` | `08 01 01 2a` | orr w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00bfb0f4"></a> `00bfb0f4` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfb0f8"></a> `00bfb0f8` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb0fc"></a> `00bfb0fc` | `41 00 00 54` | b.ne 0x00bfb104 | `CONDITIONAL_JUMP`
<a id="insn-00bfb100"></a> `00bfb100` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb104"></a> `00bfb104` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb108"></a> `00bfb108` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfb10c"></a> `00bfb10c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb110"></a> `00bfb110` | `60 b5 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bfb114"></a> `00bfb114` | `00 68 11 91` | add x0,x0,#0x45a | `FALL_THROUGH`
<a id="insn-00bfb118"></a> `00bfb118` | `01 00 00 94` | bl 0x00bfb11c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb0dc`](#insn-00bfb0dc) 範囲 `[['00bfb0dc', '00bfb0ff']]`
  - `CONDITIONAL_JUMP` [`00bfb0fc`](#insn-00bfb0fc) → [`00bfb104`](#insn-00bfb104)
  - `FALL_THROUGH` [`00bfb0fc`](#insn-00bfb0fc) → [`00bfb100`](#insn-00bfb100)
- ブロック [`00bfb100`](#insn-00bfb100) 範囲 `[['00bfb100', '00bfb103']]`
- ブロック [`00bfb104`](#insn-00bfb104) 範囲 `[['00bfb104', '00bfb11b']]`

## 命令位置別の参照

- [`00bfb0fc`](#insn-00bfb0fc) → [`00bfb104`](#insn-00bfb104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb108`](#insn-00bfb108) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb114`](#insn-00bfb114) → `002a745a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfb118`](#insn-00bfb118) → [`00bfb11c`](00bfb11c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfb11c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb0fc`](#insn-00bfb0fc)

~~~json
{
  "source": "00bfb0fc",
  "target": "00bfb104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb108`](#insn-00bfb108)

~~~json
{
  "source": "00bfb108",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb114`](#insn-00bfb114)

~~~json
{
  "source": "00bfb114",
  "target": "002a745a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a745a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "696f735f626173653a3a636c65617200",
  "capture_start": "002a745a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfb118`](#insn-00bfb118)

~~~json
{
  "source": "00bfb118",
  "target": "00bfb11c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
