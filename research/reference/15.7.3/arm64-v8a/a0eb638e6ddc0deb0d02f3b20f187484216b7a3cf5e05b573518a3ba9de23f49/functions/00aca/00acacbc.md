# 00acacbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acabf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acabf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-e474e59ef97504d273f760cc731210e3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acad00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acad00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-37f85cd7951780c751dce0718f0789e7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acacbc",
  "name": "FUN_00acacbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7df875ac0c017c2eac0f257838918237f1cb04afba71e5c707c02f93b6a1d1bd",
  "source_text_sha256": "7df875ac0c017c2eac0f257838918237f1cb04afba71e5c707c02f93b6a1d1bd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acacbc",
        "00acaccf"
      ]
    ],
    "bytes_sha256": "d5ce553789c47a1b2775caf36c6b23c34d151c9e5629517076573da615b55987",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abf52c](../00abf/00abf52c.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00acacbc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acacbc"></a> `00acacbc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acacc0"></a> `00acacc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acacc4"></a> `00acacc4` | `e0 be ff b0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00acacc8"></a> `00acacc8` | `00 0c 0c 91` | add x0,x0,#0x303 | `FALL_THROUGH`
<a id="insn-00acaccc"></a> `00acaccc` | `db 37 e5 97` | bl 0x00418c38 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acacbc`](#insn-00acacbc) 範囲 `[['00acacbc', '00acaccf']]`

## 命令位置別の参照

- [`00acacbc`](#insn-00acacbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacc8`](#insn-00acacc8) → `002a7303`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acaccc`](#insn-00acaccc) → [`00418c38`](../00418/00418c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c38` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acacbc`](#insn-00acacbc)

~~~json
{
  "source": "00acacbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacc8`](#insn-00acacc8)

~~~json
{
  "source": "00acacc8",
  "target": "002a7303",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7303",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002a7303",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acaccc`](#insn-00acaccc)

~~~json
{
  "source": "00acaccc",
  "target": "00418c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
