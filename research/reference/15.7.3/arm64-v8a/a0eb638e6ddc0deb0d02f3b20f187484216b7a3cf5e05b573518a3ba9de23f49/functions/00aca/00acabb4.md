# 00acabb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acaaec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acaaec.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-98d3e924c5b10eaa9eb2923afb19c1f6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acabf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acabf8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-628e9b7ffdb1151973caa211cda6abb2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acabb4",
  "name": "FUN_00acabb4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f98436ea28bc9709fcec553f6a4c1d16d05d049e990bf9057082b07da686704",
  "source_text_sha256": "1f98436ea28bc9709fcec553f6a4c1d16d05d049e990bf9057082b07da686704",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acabb4",
        "00acabc7"
      ]
    ],
    "bytes_sha256": "33a27ba5de331040e10b9ae9857524692edb5c0bf7f2a895fe20c534e410cd10",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aca940](../00aca/00aca940.md)

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

void FUN_00acabb4(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acabb4"></a> `00acabb4` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acabb8"></a> `00acabb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acabbc"></a> `00acabbc` | `e0 be ff b0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00acabc0"></a> `00acabc0` | `00 0c 0c 91` | add x0,x0,#0x303 | `FALL_THROUGH`
<a id="insn-00acabc4"></a> `00acabc4` | `1d 38 e5 97` | bl 0x00418c38 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acabb4`](#insn-00acabb4) 範囲 `[['00acabb4', '00acabc7']]`

## 命令位置別の参照

- [`00acabb4`](#insn-00acabb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc0`](#insn-00acabc0) → `002a7303`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acabc4`](#insn-00acabc4) → [`00418c38`](../00418/00418c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c38` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acabb4`](#insn-00acabb4)

~~~json
{
  "source": "00acabb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc0`](#insn-00acabc0)

~~~json
{
  "source": "00acabc0",
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
- 参照命令 [`00acabc4`](#insn-00acabc4)

~~~json
{
  "source": "00acabc4",
  "target": "00418c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
