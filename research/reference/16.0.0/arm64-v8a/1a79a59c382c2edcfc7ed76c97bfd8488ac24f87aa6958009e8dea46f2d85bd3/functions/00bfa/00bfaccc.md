# 00bfaccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e284`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-204325b95b34b13da586ad880ea0f9bc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb0f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb0f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-c2fd5e48d379b85e89b535aafbc16714)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaccc",
  "name": "_ZNSt6__ndk18ios_base6xallocEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be611626be869c2d9b56120ac6ee844106da033895d85ea4e00bbcdfb7461ee7",
  "source_text_sha256": "be611626be869c2d9b56120ac6ee844106da033895d85ea4e00bbcdfb7461ee7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaccc",
        "00bfacf3"
      ]
    ],
    "bytes_sha256": "edfe9708765ba891ffc11f7c89d2f5a973503ce1850365bf10d598bda714d1cb",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53880](../00c53/00c53880.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 124 bytes

~~~c

void _ZNSt6__ndk18ios_base6xallocEv(void)

{
  FUN_00c53880(1,PTR__ZNSt6__ndk18ios_base9__xindex_E_00c9b6f8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaccc"></a> `00bfaccc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfacd0"></a> `00bfacd0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfacd4"></a> `00bfacd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfacd8"></a> `00bfacd8` | `01 05 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfacdc"></a> `00bfacdc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bface0"></a> `00bface0` | `21 7c 43 f9` | ldr x1,[x1, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bface4"></a> `00bface4` | `e7 62 01 94` | bl 0x00c53880 | `UNCONDITIONAL_CALL`
<a id="insn-00bface8"></a> `00bface8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfacec"></a> `00bfacec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfacf0"></a> `00bfacf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaccc`](#insn-00bfaccc) 範囲 `[['00bfaccc', '00bfacf3']]`

## 命令位置別の参照

- [`00bfacd0`](#insn-00bfacd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bface0`](#insn-00bface0) → `00c9b6f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bface0`](#insn-00bface0) → `01126f98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk18ios_base9__xindex_E` · 推定型 `undefined4`
- [`00bface4`](#insn-00bface4) → [`00c53880`](../00c53/00c53880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53880` · 推定シンボル `None` · 推定型 `None`
- [`00bface8`](#insn-00bface8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfacd0`](#insn-00bfacd0)

~~~json
{
  "source": "00bfacd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bface0`](#insn-00bface0)

~~~json
{
  "source": "00bface0",
  "target": "00c9b6f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b6f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bface0`](#insn-00bface0)

~~~json
{
  "source": "00bface0",
  "target": "01126f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f98",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bface4`](#insn-00bface4)

~~~json
{
  "source": "00bface4",
  "target": "00c53880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bface8`](#insn-00bface8)

~~~json
{
  "source": "00bface8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
