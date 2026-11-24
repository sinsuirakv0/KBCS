# 00b4adbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b49dc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0007.md#compare-477fbafedeb55e86f6f1b3b881fe3d5b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4adbc",
  "name": "_ZN8firebase4util4date8GetClassEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ec81bd2012f6a9f460eb7171747044732453ce735c61031a885ae9aaea63aec",
  "source_text_sha256": "2ec81bd2012f6a9f460eb7171747044732453ce735c61031a885ae9aaea63aec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4adbc",
        "00b4adc7"
      ]
    ],
    "bytes_sha256": "b50d371143dc9768004cb58f1cb095ee01f91eaf63e3e7b99233f5f2a006ea85",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
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

## 疑似コード / UTF-8 81 bytes

~~~c

undefined8 _ZN8firebase4util4date8GetClassEv(void)

{
  return DAT_01126ad0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4adbc"></a> `00b4adbc` | `e8 2e 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4adc0"></a> `00b4adc0` | `00 69 45 f9` | ldr x0,[x8, #0xad0] | `FALL_THROUGH`
<a id="insn-00b4adc4"></a> `00b4adc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4adbc`](#insn-00b4adbc) 範囲 `[['00b4adbc', '00b4adc7']]`

## 命令位置別の参照

- [`00b4adc0`](#insn-00b4adc0) → `01126ad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4adc0`](#insn-00b4adc0)

~~~json
{
  "source": "00b4adc0",
  "target": "01126ad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ad0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
