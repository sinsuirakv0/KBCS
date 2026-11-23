# 00bbacec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbadb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbadb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-d530fc52e88af9a6b1d541f63a4120cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacec",
  "name": "_ZNKSt9bad_alloc4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89542cb3da142e704930f11ce8804fce6a9c4aed036007c6f36bd424e1da6be3",
  "source_text_sha256": "89542cb3da142e704930f11ce8804fce6a9c4aed036007c6f36bd424e1da6be3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacec",
        "00bbacfb"
      ]
    ],
    "bytes_sha256": "453999bfaea44e27a76bce2028551fc44d58ffb5add6895a42c972e518770ada",
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

## 関連文字列（未確認候補）

~~~text
"std::bad_alloc"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 332 bytes

~~~c

char * _ZNKSt9bad_alloc4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb57e0 with catch @ 00bbacf0 */
                    /* catch() { ... } // from try @ 00bb57f8 with catch @ 00bbacf4 */
                    /* catch() { ... } // from try @ 00bb5068 with catch @ 00bbacf8 */
  return "std::bad_alloc";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacec"></a> `00bbacec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbacf0"></a> `00bbacf0` | `00 b7 ff 90` | adrp x0,0x29a000 | `FALL_THROUGH`
<a id="insn-00bbacf4"></a> `00bbacf4` | `00 9c 28 91` | add x0,x0,#0xa27 | `FALL_THROUGH`
<a id="insn-00bbacf8"></a> `00bbacf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacec`](#insn-00bbacec) 範囲 `[['00bbacec', '00bbacef']]`
  - `FALL_THROUGH` [`00bbacec`](#insn-00bbacec) → [`00bbacf0`](#insn-00bbacf0)
- ブロック [`00bbacf0`](#insn-00bbacf0) 範囲 `[['00bbacf0', '00bbacf3']]`
  - `FALL_THROUGH` [`00bbacf0`](#insn-00bbacf0) → [`00bbacf4`](#insn-00bbacf4)
- ブロック [`00bbacf4`](#insn-00bbacf4) 範囲 `[['00bbacf4', '00bbacf7']]`
  - `FALL_THROUGH` [`00bbacf4`](#insn-00bbacf4) → [`00bbacf8`](#insn-00bbacf8)
- ブロック [`00bbacf8`](#insn-00bbacf8) 範囲 `[['00bbacf8', '00bbacfb']]`

## 命令位置別の参照

- [`00bbacf4`](#insn-00bbacf4) → `0029aa27`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacf4`](#insn-00bbacf4)

~~~json
{
  "source": "00bbacf4",
  "target": "0029aa27",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029aa27",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "7374643a3a6261645f616c6c6f6300",
  "capture_start": "0029aa27",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
