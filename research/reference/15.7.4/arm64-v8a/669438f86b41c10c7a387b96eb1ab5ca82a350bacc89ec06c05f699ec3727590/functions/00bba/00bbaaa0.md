# 00bbaaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaa5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-14e3b96a3e3614c43eb7e3b9493b5b91)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c374e8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374e8.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-d15109b3cc55594335129ef16dcc3266)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaaa0",
  "name": "_ZSt15get_new_handlerv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e",
  "source_text_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaaa0",
        "00bbaab3"
      ]
    ],
    "bytes_sha256": "ab367d774a3ed6ae6d57000fbc43297c3191f74cd2823af22bd677529c5109c2",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1e20](../00be1/00be1e20.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 277 bytes

~~~c

undefined8 _ZSt15get_new_handlerv(void)

{
                    /* catch() { ... } // from try @ 00bb34c4 with catch @ 00bbaaac */
                    /* catch() { ... } // from try @ 00bb3490 with catch @ 00bbaab0 */
  return *(undefined8 *)PTR___cxa_new_handler_00c1c008;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaaa0"></a> `00bbaaa0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbaaa4"></a> `00bbaaa4` | `08 03 00 d0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbaaa8"></a> `00bbaaa8` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbaaac"></a> `00bbaaac` | `00 fd df c8` | ldar x0,[x8] | `FALL_THROUGH`
<a id="insn-00bbaab0"></a> `00bbaab0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaaa0`](#insn-00bbaaa0) 範囲 `[['00bbaaa0', '00bbaaab']]`
  - `FALL_THROUGH` [`00bbaaa8`](#insn-00bbaaa8) → [`00bbaaac`](#insn-00bbaaac)
- ブロック [`00bbaaac`](#insn-00bbaaac) 範囲 `[['00bbaaac', '00bbaaaf']]`
  - `FALL_THROUGH` [`00bbaaac`](#insn-00bbaaac) → [`00bbaab0`](#insn-00bbaab0)
- ブロック [`00bbaab0`](#insn-00bbaab0) 範囲 `[['00bbaab0', '00bbaab3']]`

## 命令位置別の参照

- [`00bbaaa8`](#insn-00bbaaa8) → `00c1c008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbaaac`](#insn-00bbaaac) → `010a3758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `__cxa_new_handler` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaaa8`](#insn-00bbaaa8)

~~~json
{
  "source": "00bbaaa8",
  "target": "00c1c008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaaac`](#insn-00bbaaac)

~~~json
{
  "source": "00bbaaac",
  "target": "010a3758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a3758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
