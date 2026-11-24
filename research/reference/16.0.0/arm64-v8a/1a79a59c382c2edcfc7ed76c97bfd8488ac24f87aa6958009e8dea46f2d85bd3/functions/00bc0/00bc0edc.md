# 00bc0edc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b52578`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52578.md) · 移動量 `+0x6e964`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-b8a555e5a0bc6266b0db48d72a1b1098)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc1304`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1304.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0009.md#compare-de8e9ffcedc875b3d719e1b6bf3f1d91)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc0edc",
  "name": "_ZN8firebase13remote_config10FutureData3GetEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f123a8fb845b9009d3be8d4c3fa862cd7af34f86c55a9aced3828860c5172834",
  "source_text_sha256": "f123a8fb845b9009d3be8d4c3fa862cd7af34f86c55a9aced3828860c5172834",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc0edc",
        "00bc0eeb"
      ]
    ],
    "bytes_sha256": "85eaac93aeaf1b910096f9479bd2712eb99772fe31e56d0056e0631b191c5e36",
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

## 疑似コード / UTF-8 165 bytes

~~~c

undefined8 _ZN8firebase13remote_config10FutureData3GetEv(void)

{
  return *(undefined8 *)PTR__ZN8firebase13remote_config10FutureData14s_future_data_E_00c9b518;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc0edc"></a> `00bc0edc` | `c8 06 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bc0ee0"></a> `00bc0ee0` | `08 8d 42 f9` | ldr x8,[x8, #0x518] | `FALL_THROUGH`
<a id="insn-00bc0ee4"></a> `00bc0ee4` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bc0ee8"></a> `00bc0ee8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc0edc`](#insn-00bc0edc) 範囲 `[['00bc0edc', '00bc0eeb']]`

## 命令位置別の参照

- [`00bc0ee0`](#insn-00bc0ee0) → `00c9b518`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc0ee4`](#insn-00bc0ee4) → `01126030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config10FutureData14s_future_data_E` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc0ee0`](#insn-00bc0ee0)

~~~json
{
  "source": "00bc0ee0",
  "target": "00c9b518",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b518",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc0ee4`](#insn-00bc0ee4)

~~~json
{
  "source": "00bc0ee4",
  "target": "01126030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
