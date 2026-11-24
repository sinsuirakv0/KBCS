# 00beffe0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b733d8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733d8.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-98b76730c3b48ceb8584286ee6bc2cfe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf0408`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0408.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-43fbe4341915c829f196964509255bff)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beffe0",
  "name": "_ZNKSt6__ndk112bad_weak_ptr4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7dab321352cf6b6d30e62fad4539996c5a241aece0386d329c7434fb8b8caec",
  "source_text_sha256": "c7dab321352cf6b6d30e62fad4539996c5a241aece0386d329c7434fb8b8caec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beffe0",
        "00beffef"
      ]
    ],
    "bytes_sha256": "2b84e35280e969031c9c3b5577c23f445e319ad14e138adaa7aa3437ef741627",
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
"bad_weak_ptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 80 bytes

~~~c

char * _ZNKSt6__ndk112bad_weak_ptr4whatEv(void)

{
  return "bad_weak_ptr";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beffe0"></a> `00beffe0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beffe4"></a> `00beffe4` | `60 b6 ff 90` | adrp x0,0x2bb000 | `FALL_THROUGH`
<a id="insn-00beffe8"></a> `00beffe8` | `00 2c 03 91` | add x0,x0,#0xcb | `FALL_THROUGH`
<a id="insn-00beffec"></a> `00beffec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beffe0`](#insn-00beffe0) 範囲 `[['00beffe0', '00beffef']]`

## 命令位置別の参照

- [`00beffe8`](#insn-00beffe8) → `002bb0cb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beffe8`](#insn-00beffe8)

~~~json
{
  "source": "00beffe8",
  "target": "002bb0cb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb0cb",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "6261645f7765616b5f70747200",
  "capture_start": "002bb0cb",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
