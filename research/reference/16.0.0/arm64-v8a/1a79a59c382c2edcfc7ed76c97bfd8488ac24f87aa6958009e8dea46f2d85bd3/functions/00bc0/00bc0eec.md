# 00bc0eec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b52588`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md) · 移動量 `+0x6e964`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0065.md#compare-909668c482a5af66ba4b7b30e404ba0b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc1314`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-c84c733bc119dd9be3fce7d5778e3346)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0eec",
  "name": "_INIT_287",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350",
  "source_text_sha256": "aaa99cbe98d3db842b74fee27c340d156e2491a7111eab2812850f24732a6350",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc0eec",
        "00bc0f1b"
      ]
    ],
    "bytes_sha256": "56bbb4353bc76172709e8027d325b817891f642723affc1771a413bd8fb92168",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7c0](../00c5a/00c5a7c0.md)

## 関連文字列（未確認候補）

~~~text
"remote_config"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 203 bytes

~~~c

void _INIT_287(void)

{
  DAT_01126010 = "remote_config";
  DAT_01126018 = FUN_00bc0e44;
  DAT_01126020 = FUN_00bc0e4c;
  DAT_01126028 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc0eec"></a> `00bc0eec` | `20 2b 00 d0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc0ef0"></a> `00bc0ef0` | `48 b7 ff b0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bc0ef4"></a> `00bc0ef4` | `09 00 00 90` | adrp x9,0xbc0000 | `FALL_THROUGH`
<a id="insn-00bc0ef8"></a> `00bc0ef8` | `0a 00 00 90` | adrp x10,0xbc0000 | `FALL_THROUGH`
<a id="insn-00bc0efc"></a> `00bc0efc` | `00 40 00 91` | add x0,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bc0f00"></a> `00bc0f00` | `08 21 1d 91` | add x8,x8,#0x748 | `FALL_THROUGH`
<a id="insn-00bc0f04"></a> `00bc0f04` | `29 11 39 91` | add x9,x9,#0xe44 | `FALL_THROUGH`
<a id="insn-00bc0f08"></a> `00bc0f08` | `4a 31 39 91` | add x10,x10,#0xe4c | `FALL_THROUGH`
<a id="insn-00bc0f0c"></a> `00bc0f0c` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bc0f10"></a> `00bc0f10` | `0a 08 00 f9` | str x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc0f14"></a> `00bc0f14` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0f18"></a> `00bc0f18` | `2a 66 02 14` | b 0x00c5a7c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc0eec`](#insn-00bc0eec) 範囲 `[['00bc0eec', '00bc0f1b']]`

## 命令位置別の参照

- [`00bc0efc`](#insn-00bc0efc) → `01126010`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc0f0c`](#insn-00bc0f0c) → `01126010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc0f0c`](#insn-00bc0f0c) → `002a9748`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0f0c`](#insn-00bc0f0c) → `01126018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc0f0c`](#insn-00bc0f0c) → [`00bc0e44`](00bc0e44.md) · `DATA` · `ANALYSIS` · 関数 `00bc0e44` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f10`](#insn-00bc0f10) → `01126020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc0f10`](#insn-00bc0f10) → [`00bc0e4c`](00bc0e4c.md) · `DATA` · `ANALYSIS` · 関数 `00bc0e4c` · 推定シンボル `None` · 推定型 `None`
- [`00bc0f14`](#insn-00bc0f14) → `01126028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc0f18`](#insn-00bc0f18) → [`00c5a7c0`](../00c5a/00c5a7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc0efc`](#insn-00bc0efc)

~~~json
{
  "source": "00bc0efc",
  "target": "01126010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc0f0c`](#insn-00bc0f0c)

~~~json
{
  "source": "00bc0f0c",
  "target": "01126010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc0f0c`](#insn-00bc0f0c)

~~~json
{
  "source": "00bc0f0c",
  "target": "002a9748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9748",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "72656d6f74655f636f6e66696700",
  "capture_start": "002a9748",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc0f0c`](#insn-00bc0f0c)

~~~json
{
  "source": "00bc0f0c",
  "target": "01126018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc0f0c`](#insn-00bc0f0c)

~~~json
{
  "source": "00bc0f0c",
  "target": "00bc0e44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc0f10`](#insn-00bc0f10)

~~~json
{
  "source": "00bc0f10",
  "target": "01126020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc0f10`](#insn-00bc0f10)

~~~json
{
  "source": "00bc0f10",
  "target": "00bc0e4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc0f14`](#insn-00bc0f14)

~~~json
{
  "source": "00bc0f14",
  "target": "01126028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126028",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc0f18`](#insn-00bc0f18)

~~~json
{
  "source": "00bc0f18",
  "target": "00c5a7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
