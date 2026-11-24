# 00bfa1cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa130`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-38d2c9aed29a2645225a4d4c44489264)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfb1c0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1c0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-8b8f4d65a4a1442df25a6e8efc7186c1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa1cc",
  "name": "_ZNSt6__ndk15mutex4lockEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203",
  "source_text_sha256": "d6a09bf60f6e907cbf77359d35e00face011e0c1ea964fdc0b39b44725fd3203",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfa1cc",
        "00bfa1f7"
      ]
    ],
    "bytes_sha256": "0c38b73378d221231650f3ad85f2bbbca0c16c5d13f2e2daaf75860072abd3b0",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c581b0](../00c58/00c581b0.md)

## 呼び出し先

- [00c581f0](../00c58/00c581f0.md)
- [00c5b770](../00c5b/00c5b770.md)

## 関連文字列（未確認候補）

~~~text
"mutex lock failed"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZNSt6__ndk15mutex4lockEv(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_lock(param_1);
  if (iVar1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"mutex lock failed");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfa1cc"></a> `00bfa1cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfa1d0"></a> `00bfa1d0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfa1d4"></a> `00bfa1d4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfa1d8"></a> `00bfa1d8` | `66 85 01 94` | bl 0x00c5b770 | `UNCONDITIONAL_CALL`
<a id="insn-00bfa1dc"></a> `00bfa1dc` | `80 00 00 35` | cbnz w0,0x00bfa1ec | `CONDITIONAL_JUMP`
<a id="insn-00bfa1e0"></a> `00bfa1e0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfa1e4"></a> `00bfa1e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfa1e8"></a> `00bfa1e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfa1ec"></a> `00bfa1ec` | `a1 b5 ff f0` | adrp x1,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bfa1f0"></a> `00bfa1f0` | `21 08 1d 91` | add x1,x1,#0x742 | `FALL_THROUGH`
<a id="insn-00bfa1f4"></a> `00bfa1f4` | `ff 77 01 94` | bl 0x00c581f0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfa1cc`](#insn-00bfa1cc) 範囲 `[['00bfa1cc', '00bfa1df']]`
  - `CONDITIONAL_JUMP` [`00bfa1dc`](#insn-00bfa1dc) → [`00bfa1ec`](#insn-00bfa1ec)
  - `FALL_THROUGH` [`00bfa1dc`](#insn-00bfa1dc) → [`00bfa1e0`](#insn-00bfa1e0)
- ブロック [`00bfa1e0`](#insn-00bfa1e0) 範囲 `[['00bfa1e0', '00bfa1eb']]`
- ブロック [`00bfa1ec`](#insn-00bfa1ec) 範囲 `[['00bfa1ec', '00bfa1f7']]`

## 命令位置別の参照

- [`00bfa1d0`](#insn-00bfa1d0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa1d8`](#insn-00bfa1d8) → [`00c5b770`](../00c5b/00c5b770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b770` · 推定シンボル `None` · 推定型 `None`
- [`00bfa1dc`](#insn-00bfa1dc) → [`00bfa1ec`](#insn-00bfa1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa1e0`](#insn-00bfa1e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfa1f0`](#insn-00bfa1f0) → `002b1742`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfa1f4`](#insn-00bfa1f4) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfa1d0`](#insn-00bfa1d0)

~~~json
{
  "source": "00bfa1d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa1d8`](#insn-00bfa1d8)

~~~json
{
  "source": "00bfa1d8",
  "target": "00c5b770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfa1dc`](#insn-00bfa1dc)

~~~json
{
  "source": "00bfa1dc",
  "target": "00bfa1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa1e0`](#insn-00bfa1e0)

~~~json
{
  "source": "00bfa1e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfa1f0`](#insn-00bfa1f0)

~~~json
{
  "source": "00bfa1f0",
  "target": "002b1742",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1742",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6d75746578206c6f636b206661696c656400",
  "capture_start": "002b1742",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfa1f4`](#insn-00bfa1f4)

~~~json
{
  "source": "00bfa1f4",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
