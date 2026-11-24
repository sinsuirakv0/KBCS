# 00bbaa5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaa18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-a6a1926a606d1b1bc0ba4d67aca0f4db)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c374a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-473004bd00d3d917f9da6171928b9e64)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaa5c",
  "name": "_ZSt13get_terminatev",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f4d90946841fe0268c523550ba919278bfc578439a8bb9323e8266acd407760",
  "source_text_sha256": "8f4d90946841fe0268c523550ba919278bfc578439a8bb9323e8266acd407760",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaa5c",
        "00bbaa6f"
      ]
    ],
    "bytes_sha256": "6af12a6931ab866da29ab5e51e03356806dc12943e2b96a3415acf6b660946df",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1e10](../00be1/00be1e10.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

undefined8 _ZSt13get_terminatev(void)

{
  return *(undefined8 *)PTR___cxa_terminate_handler_00c1c000;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaa5c"></a> `00bbaa5c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbaa60"></a> `00bbaa60` | `08 03 00 d0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbaa64"></a> `00bbaa64` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbaa68"></a> `00bbaa68` | `00 fd df c8` | ldar x0,[x8] | `FALL_THROUGH`
<a id="insn-00bbaa6c"></a> `00bbaa6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaa5c`](#insn-00bbaa5c) 範囲 `[['00bbaa5c', '00bbaa6f']]`

## 命令位置別の参照

- [`00bbaa64`](#insn-00bbaa64) → `00c1c000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbaa68`](#insn-00bbaa68) → `00c24990`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `__cxa_terminate_handler` · 推定型 `pointer`
- [`00bbaa68`](#insn-00bbaa68) → [`00bbaab4`](00bbaab4.md) · `DATA` · `ANALYSIS` · 関数 `00bbaab4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaa64`](#insn-00bbaa64)

~~~json
{
  "source": "00bbaa64",
  "target": "00c1c000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaa68`](#insn-00bbaa68)

~~~json
{
  "source": "00bbaa68",
  "target": "00c24990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbaa68`](#insn-00bbaa68)

~~~json
{
  "source": "00bbaa68",
  "target": "00bbaab4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
