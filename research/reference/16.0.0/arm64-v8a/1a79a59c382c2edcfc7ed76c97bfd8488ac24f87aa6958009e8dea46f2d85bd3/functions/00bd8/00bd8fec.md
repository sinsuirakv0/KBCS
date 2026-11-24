# 00bd8fec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b69aec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69aec.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-bc4c2e1c4d2a88d97c82bfacc969e17e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd9414`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9414.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0084.md#compare-ccdbfe7cd3f605c40525636092eb9b4c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd8fec",
  "name": "_ZNK8firebase4auth10Credential8is_validEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d422f2cc6309550715c94d1bd75ee23ffd2cd811041d64b3296e02aa0555f749",
  "source_text_sha256": "d422f2cc6309550715c94d1bd75ee23ffd2cd811041d64b3296e02aa0555f749",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd8fec",
        "00bd8ffb"
      ]
    ],
    "bytes_sha256": "281f50b1250d415b872fa75dc5beda75d9e1221cbc5b5dcf20409c624d6c030e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 190 bytes

~~~c

bool _ZNK8firebase4auth10Credential8is_validEv(long *param_1)

{
                    /* try { // try from 00bd8ff8 to 00cd9027 has its CatchHandler @ 00bd6d50 */
  return *param_1 != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd8fec"></a> `00bd8fec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd8ff0"></a> `00bd8ff0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bd8ff4"></a> `00bd8ff4` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bd8ff8"></a> `00bd8ff8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd8fec`](#insn-00bd8fec) 範囲 `[['00bd8fec', '00bd8ff7']]`
  - `FALL_THROUGH` [`00bd8ff4`](#insn-00bd8ff4) → [`00bd8ff8`](#insn-00bd8ff8)
- ブロック [`00bd8ff8`](#insn-00bd8ff8) 範囲 `[['00bd8ff8', '00bd8ffb']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

