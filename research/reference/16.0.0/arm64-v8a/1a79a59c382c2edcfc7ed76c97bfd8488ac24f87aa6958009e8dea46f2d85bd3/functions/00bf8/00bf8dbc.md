# 00bf8dbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7c374`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c374.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-eff88aa618e72bbd1bdcbd725684ce41)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf91e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf91e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0040.md#compare-fdef81356ba40e0640ecd95bbf9e0a13)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf8dbc",
  "name": "_ZNSt6__ndk118condition_variableD2Ev",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74fd08fc12304c0baaa9593947540b9b92c2164ff9cf357cff8ee28f280a5eb9",
  "source_text_sha256": "74fd08fc12304c0baaa9593947540b9b92c2164ff9cf357cff8ee28f280a5eb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf8dbc",
        "00bf8dd7"
      ]
    ],
    "bytes_sha256": "54524d2302be8a916dac29edf97c86a013973b4ce16c47dcad81fe58f3e56b92",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c57cd0](../00c57/00c57cd0.md)

## 呼び出し先

- [00c5d220](../00c5d/00c5d220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 146 bytes

~~~c

int _ZNSt6__ndk118condition_variableD2Ev(pthread_cond_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_cond_destroy(param_1);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf8dbc"></a> `00bf8dbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf8dc0"></a> `00bf8dc0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bf8dc4"></a> `00bf8dc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf8dc8"></a> `00bf8dc8` | `16 91 01 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bf8dcc"></a> `00bf8dcc` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bf8dd0"></a> `00bf8dd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf8dd4"></a> `00bf8dd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf8dbc`](#insn-00bf8dbc) 範囲 `[['00bf8dbc', '00bf8dd7']]`

## 命令位置別の参照

- [`00bf8dc0`](#insn-00bf8dc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf8dc8`](#insn-00bf8dc8) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bf8dcc`](#insn-00bf8dcc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf8dc0`](#insn-00bf8dc0)

~~~json
{
  "source": "00bf8dc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf8dc8`](#insn-00bf8dc8)

~~~json
{
  "source": "00bf8dc8",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf8dcc`](#insn-00bf8dcc)

~~~json
{
  "source": "00bf8dcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
