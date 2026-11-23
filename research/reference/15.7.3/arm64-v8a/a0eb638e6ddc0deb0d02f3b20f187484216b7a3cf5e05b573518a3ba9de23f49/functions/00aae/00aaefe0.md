# 00aaefe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaef18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aaef18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-b45b7e6f1d5c5875fe02a7a3a3d2142c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaf024`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aaf024.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-cf7a85bc469f5a990ae61aff9796b67c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaefe0",
  "name": "FUN_00aaefe0",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d281ff9a589ccf98e41925a244b053bc616ab61a63222b33d3d81b3a463c65f5",
  "source_text_sha256": "d281ff9a589ccf98e41925a244b053bc616ab61a63222b33d3d81b3a463c65f5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaefe0",
        "00aaf09b"
      ]
    ],
    "bytes_sha256": "1bd3cbbf45c9492759c2ffbfa8777e11eacba8bd586d3064d13150115b7fdde1",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009c5338](../009c5/009c5338.md)

## 呼び出し先

- [0045de70](../0045d/0045de70.md)
- [0045df50](../0045d/0045df50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 696 bytes

~~~c

void FUN_00aaefe0(undefined4 *param_1,undefined8 param_2)

{
  FUN_0045df50(param_2,*param_1);
  FUN_0045df50(param_2,param_1[3]);
  FUN_0045df50(param_2,param_1[5]);
  FUN_0045df50(param_2,param_1[4]);
  FUN_0045df50(param_2,param_1[1]);
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 7));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1d));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1e));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1f));
  FUN_0045df50(param_2,param_1[2]);
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 8));
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 9));
  FUN_0045de70(param_2,*(undefined1 *)(param_1 + 0xb));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaefe0"></a> `00aaefe0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aaefe4"></a> `00aaefe4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaefe8"></a> `00aaefe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaefec"></a> `00aaefec` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00aaeff0"></a> `00aaeff0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaeff4"></a> `00aaeff4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aaeff8"></a> `00aaeff8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaeffc"></a> `00aaeffc` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00aaf000"></a> `00aaf000` | `d4 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf004"></a> `00aaf004` | `61 0e 40 b9` | ldr w1,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00aaf008"></a> `00aaf008` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf00c"></a> `00aaf00c` | `d1 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf010"></a> `00aaf010` | `61 16 40 b9` | ldr w1,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00aaf014"></a> `00aaf014` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf018"></a> `00aaf018` | `ce bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf01c"></a> `00aaf01c` | `61 12 40 b9` | ldr w1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aaf020"></a> `00aaf020` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf024"></a> `00aaf024` | `cb bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf028"></a> `00aaf028` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aaf02c"></a> `00aaf02c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf030"></a> `00aaf030` | `c8 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf034"></a> `00aaf034` | `61 72 40 39` | ldrb w1,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaf038"></a> `00aaf038` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf03c"></a> `00aaf03c` | `c5 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf040"></a> `00aaf040` | `61 76 40 39` | ldrb w1,[x19, #0x1d] | `FALL_THROUGH`
<a id="insn-00aaf044"></a> `00aaf044` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf048"></a> `00aaf048` | `c2 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf04c"></a> `00aaf04c` | `61 7a 40 39` | ldrb w1,[x19, #0x1e] | `FALL_THROUGH`
<a id="insn-00aaf050"></a> `00aaf050` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf054"></a> `00aaf054` | `bf bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf058"></a> `00aaf058` | `61 7e 40 39` | ldrb w1,[x19, #0x1f] | `FALL_THROUGH`
<a id="insn-00aaf05c"></a> `00aaf05c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf060"></a> `00aaf060` | `bc bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf064"></a> `00aaf064` | `61 0a 40 b9` | ldr w1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aaf068"></a> `00aaf068` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf06c"></a> `00aaf06c` | `b9 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf070"></a> `00aaf070` | `61 82 40 39` | ldrb w1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aaf074"></a> `00aaf074` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf078"></a> `00aaf078` | `b6 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf07c"></a> `00aaf07c` | `61 92 40 39` | ldrb w1,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00aaf080"></a> `00aaf080` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf084"></a> `00aaf084` | `b3 bb e6 97` | bl 0x0045df50 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf088"></a> `00aaf088` | `61 b2 40 39` | ldrb w1,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaf08c"></a> `00aaf08c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaf090"></a> `00aaf090` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaf094"></a> `00aaf094` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aaf098"></a> `00aaf098` | `76 bb e6 17` | b 0x0045de70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaefe0`](#insn-00aaefe0) 範囲 `[['00aaefe0', '00aaf09b']]`

## 命令位置別の参照

- [`00aaefe0`](#insn-00aaefe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefe4`](#insn-00aaefe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf000`](#insn-00aaf000) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf00c`](#insn-00aaf00c) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf018`](#insn-00aaf018) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf024`](#insn-00aaf024) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf030`](#insn-00aaf030) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf03c`](#insn-00aaf03c) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf048`](#insn-00aaf048) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf054`](#insn-00aaf054) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf060`](#insn-00aaf060) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf06c`](#insn-00aaf06c) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf078`](#insn-00aaf078) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf084`](#insn-00aaf084) → [`0045df50`](../0045d/0045df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045df50` · 推定シンボル `None` · 推定型 `None`
- [`00aaf090`](#insn-00aaf090) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf094`](#insn-00aaf094) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf098`](#insn-00aaf098) → [`0045de70`](../0045d/0045de70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045de70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaefe0`](#insn-00aaefe0)

~~~json
{
  "source": "00aaefe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefe4`](#insn-00aaefe4)

~~~json
{
  "source": "00aaefe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf000`](#insn-00aaf000)

~~~json
{
  "source": "00aaf000",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf00c`](#insn-00aaf00c)

~~~json
{
  "source": "00aaf00c",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf018`](#insn-00aaf018)

~~~json
{
  "source": "00aaf018",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf024`](#insn-00aaf024)

~~~json
{
  "source": "00aaf024",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf030`](#insn-00aaf030)

~~~json
{
  "source": "00aaf030",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf03c`](#insn-00aaf03c)

~~~json
{
  "source": "00aaf03c",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf048`](#insn-00aaf048)

~~~json
{
  "source": "00aaf048",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf054`](#insn-00aaf054)

~~~json
{
  "source": "00aaf054",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf060`](#insn-00aaf060)

~~~json
{
  "source": "00aaf060",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf06c`](#insn-00aaf06c)

~~~json
{
  "source": "00aaf06c",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf078`](#insn-00aaf078)

~~~json
{
  "source": "00aaf078",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf084`](#insn-00aaf084)

~~~json
{
  "source": "00aaf084",
  "target": "0045df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf090`](#insn-00aaf090)

~~~json
{
  "source": "00aaf090",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf094`](#insn-00aaf094)

~~~json
{
  "source": "00aaf094",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf098`](#insn-00aaf098)

~~~json
{
  "source": "00aaf098",
  "target": "0045de70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
