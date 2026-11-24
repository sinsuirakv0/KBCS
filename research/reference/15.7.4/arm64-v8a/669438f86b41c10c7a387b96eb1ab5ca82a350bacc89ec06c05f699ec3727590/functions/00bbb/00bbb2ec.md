# 00bbb2ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb2a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb2a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-c328c9c14d1e0d87efbfff3f80745d98)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37d34`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d34.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-632688b80c6f13047b541efe1fed756d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb2ec",
  "name": "FUN_00bbb2ec",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbb59bf0ea0de3fe0296cc15d55676e5f6b30dc3ad3a316509b004e0b6784baf",
  "source_text_sha256": "cbb59bf0ea0de3fe0296cc15d55676e5f6b30dc3ad3a316509b004e0b6784baf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb2ec",
        "00bbb317"
      ]
    ],
    "bytes_sha256": "437e1d68dab5700f6f6957f78c97b44695333fbd3405931189ca693e2725e86a",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e90](../00be1/00be1e90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

void FUN_00bbb2ec(void *param_1)

{
  _ZNSt9type_infoD2Ev();
                    /* try { // try from 00bbb30c to 00cbb317 has its CatchHandler @ 00bbb904 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb2ec"></a> `00bbb2ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbb2f0"></a> `00bbb2f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbb2f4"></a> `00bbb2f4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb2f8"></a> `00bbb2f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbb2fc"></a> `00bbb2fc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbb300"></a> `00bbb300` | `e4 9a 00 94` | bl 0x00be1e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb304"></a> `00bbb304` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb308"></a> `00bbb308` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb30c"></a> `00bbb30c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbb310"></a> `00bbb310` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbb314"></a> `00bbb314` | `53 7f 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb2ec`](#insn-00bbb2ec) 範囲 `[['00bbb2ec', '00bbb30b']]`
  - `FALL_THROUGH` [`00bbb308`](#insn-00bbb308) → [`00bbb30c`](#insn-00bbb30c)
- ブロック [`00bbb30c`](#insn-00bbb30c) 範囲 `[['00bbb30c', '00bbb317']]`

## 命令位置別の参照

- [`00bbb2f0`](#insn-00bbb2f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb2f4`](#insn-00bbb2f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb300`](#insn-00bbb300) → [`00be1e90`](../00be1/00be1e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e90` · 推定シンボル `None` · 推定型 `None`
- [`00bbb308`](#insn-00bbb308) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb30c`](#insn-00bbb30c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb314`](#insn-00bbb314) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb2f0`](#insn-00bbb2f0)

~~~json
{
  "source": "00bbb2f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb2f4`](#insn-00bbb2f4)

~~~json
{
  "source": "00bbb2f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb300`](#insn-00bbb300)

~~~json
{
  "source": "00bbb300",
  "target": "00be1e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb308`](#insn-00bbb308)

~~~json
{
  "source": "00bbb308",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb30c`](#insn-00bbb30c)

~~~json
{
  "source": "00bbb30c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb314`](#insn-00bbb314)

~~~json
{
  "source": "00bbb314",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
