# 00aaf0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaf014`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-65aa5bd29ec9314c8ab69086e5b86ea6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaf120`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf120.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-135839fbf2f454997fb464e2d1144e00)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaf0dc",
  "name": "FUN_00aaf0dc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509",
  "source_text_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaf0dc",
        "00aaf113"
      ]
    ],
    "bytes_sha256": "207cd96b79482eb6af4105cdc1c8ad153bb243440f4c3d502bed258431dc8092",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009c5338](../009c5/009c5338.md)

## 呼び出し先

- [0045df50](../0045d/0045df50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 145 bytes

~~~c

void FUN_00aaf0dc(undefined4 *param_1,undefined8 param_2)

{
  FUN_0045df50(param_2,*param_1);
  FUN_0045df50(param_2,param_1[1]);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaf0dc"></a> `00aaf0dc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aaf0e0"></a> `00aaf0e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaf0e4"></a> `00aaf0e4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaf0e8"></a> `00aaf0e8` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00aaf0ec"></a> `00aaf0ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaf0f0"></a> `00aaf0f0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aaf0f4"></a> `00aaf0f4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaf0f8"></a> `00aaf0f8` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00aaf0fc"></a> `00aaf0fc` | `95 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf100"></a> `00aaf100` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aaf104"></a> `00aaf104` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf108"></a> `00aaf108` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaf10c"></a> `00aaf10c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aaf110"></a> `00aaf110` | `90 bb e6 17` | b 0x0045df50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaf0dc`](#insn-00aaf0dc) 範囲 `[['00aaf0dc', '00aaf113']]`

## 命令位置別の参照

- [`00aaf0dc`](#insn-00aaf0dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf0e0`](#insn-00aaf0e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf0fc`](#insn-00aaf0fc) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf108`](#insn-00aaf108) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf10c`](#insn-00aaf10c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf110`](#insn-00aaf110) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaf0dc`](#insn-00aaf0dc)

~~~json
{
  "source": "00aaf0dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf0e0`](#insn-00aaf0e0)

~~~json
{
  "source": "00aaf0e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf0fc`](#insn-00aaf0fc)

~~~json
{
  "source": "00aaf0fc",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf108`](#insn-00aaf108)

~~~json
{
  "source": "00aaf108",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf10c`](#insn-00aaf10c)

~~~json
{
  "source": "00aaf10c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf110`](#insn-00aaf110)

~~~json
{
  "source": "00aaf110",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
