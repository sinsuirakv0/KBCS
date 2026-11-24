# 00bdedf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdeda0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeda0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-09916c976a9e8734b673096ef7efd7a2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5b8b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8b0.md) · 移動量 `+0x7cac0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-17f4b7b2450084824c6928e17efa076e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedf0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl15LastResultProxyEi",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0c3c56096d083ba431352710c8d2c9f334034e367eab69e0ce9cd9ad3e92bea",
  "source_text_sha256": "f0c3c56096d083ba431352710c8d2c9f334034e367eab69e0ce9cd9ad3e92bea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedf0",
        "00bdedff"
      ]
    ],
    "bytes_sha256": "3e593a5f5c0f34ede521c203ea5ddddab10c42ad4f818c70dfa1bb9171f4ee1a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b72670](../00b72/00b72670.md)

## 呼び出し先

- [00b0067c](../00b00/00b0067c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl15LastResultProxyEi(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImpl15LastResultProxyEi_00c1dfb0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedf0"></a> `00bdedf0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedf4"></a> `00bdedf4` | `11 da 47 f9` | ldr x17,[x16, #0xfb0] | `FALL_THROUGH`
<a id="insn-00bdedf8"></a> `00bdedf8` | `10 c2 3e 91` | add x16,x16,#0xfb0 | `FALL_THROUGH`
<a id="insn-00bdedfc"></a> `00bdedfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedf0`](#insn-00bdedf0) 範囲 `[['00bdedf0', '00bdedff']]`

## 命令位置別の参照

- [`00bdedf4`](#insn-00bdedf4) → `00c1dfb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdedfc`](#insn-00bdedfc) → [`00b0067c`](../00b00/00b0067c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0067c` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl15LastResultProxyEi` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedf4`](#insn-00bdedf4)

~~~json
{
  "source": "00bdedf4",
  "target": "00c1dfb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1dfb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdedfc`](#insn-00bdedfc)

~~~json
{
  "source": "00bdedfc",
  "target": "00b0067c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
