# 00acd8ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acd824`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd824.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0042.md#compare-d8849bd81c4b81401bf328d60f9c99dd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acd930`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd930.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0042.md#compare-5f3e6c28b74e64634416a5c00a5f8f38)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd8ec",
  "name": "FUN_00acd8ec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0c3bba4e26fdf266eed18918aa3604d61944705925992e02ae82e8c071b6b2f",
  "source_text_sha256": "a0c3bba4e26fdf266eed18918aa3604d61944705925992e02ae82e8c071b6b2f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd8ec",
        "00acd8ff"
      ]
    ],
    "bytes_sha256": "dcc9942178abaf1413db1455de6df5776695f4a2afc80d5506dae1229aa54d70",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 149 bytes

~~~c

void FUN_00acd8ec(long param_1)

{
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    return;
  }
  _ZdlPv(*(void **)(param_1 + 0x20));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd8ec"></a> `00acd8ec` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acd8f0"></a> `00acd8f0` | `48 00 00 37` | tbnz w8,#0x0,0x00acd8f8 | `CONDITIONAL_JUMP`
<a id="insn-00acd8f4"></a> `00acd8f4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acd8f8"></a> `00acd8f8` | `00 10 40 f9` | ldr x0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acd8fc"></a> `00acd8fc` | `c5 35 04 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acd8ec`](#insn-00acd8ec) 範囲 `[['00acd8ec', '00acd8f3']]`
  - `CONDITIONAL_JUMP` [`00acd8f0`](#insn-00acd8f0) → [`00acd8f8`](#insn-00acd8f8)
  - `FALL_THROUGH` [`00acd8f0`](#insn-00acd8f0) → [`00acd8f4`](#insn-00acd8f4)
- ブロック [`00acd8f4`](#insn-00acd8f4) 範囲 `[['00acd8f4', '00acd8f7']]`
- ブロック [`00acd8f8`](#insn-00acd8f8) 範囲 `[['00acd8f8', '00acd8ff']]`

## 命令位置別の参照

- [`00acd8f0`](#insn-00acd8f0) → [`00acd8f8`](#insn-00acd8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd8fc`](#insn-00acd8fc) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd8f0`](#insn-00acd8f0)

~~~json
{
  "source": "00acd8f0",
  "target": "00acd8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd8fc`](#insn-00acd8fc)

~~~json
{
  "source": "00acd8fc",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
