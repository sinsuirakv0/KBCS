# 00bdcac0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdca70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-1fa2c1498b1928eacf0f13ea6091a9e4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59510`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59510.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-d0ea4c0eb1abc8bd22f7b96cb62eba05)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcac0",
  "name": "_ZN5Botan14ipv4_to_stringEj",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f8869a1fd00191613f7e03089d3d2fbc08f89010cca683d6ac21bb386a4c8e6",
  "source_text_sha256": "7f8869a1fd00191613f7e03089d3d2fbc08f89010cca683d6ac21bb386a4c8e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcac0",
        "00bdcacf"
      ]
    ],
    "bytes_sha256": "c01673bd8209e7b19f9d2e0313f2fae68c5598112f37ecce343214e990792eef",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004dcf48](../004dc/004dcf48.md)
- [004e3840](../004e3/004e3840.md)

## 呼び出し先

- [004da70c](../004da/004da70c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 113 bytes

~~~c

void _ZN5Botan14ipv4_to_stringEj(void)

{
  (*(code *)PTR__ZN5Botan14ipv4_to_stringEj_00c1ce18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcac0"></a> `00bdcac0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcac4"></a> `00bdcac4` | `11 0e 47 f9` | ldr x17,[x16, #0xe18] | `FALL_THROUGH`
<a id="insn-00bdcac8"></a> `00bdcac8` | `10 62 38 91` | add x16,x16,#0xe18 | `FALL_THROUGH`
<a id="insn-00bdcacc"></a> `00bdcacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcac0`](#insn-00bdcac0) 範囲 `[['00bdcac0', '00bdcacf']]`

## 命令位置別の参照

- [`00bdcac4`](#insn-00bdcac4) → `00c1ce18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcacc`](#insn-00bdcacc) → [`004da70c`](../004da/004da70c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004da70c` · 推定シンボル `_ZN5Botan14ipv4_to_stringEj` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcac4`](#insn-00bdcac4)

~~~json
{
  "source": "00bdcac4",
  "target": "00c1ce18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcacc`](#insn-00bdcacc)

~~~json
{
  "source": "00bdcacc",
  "target": "004da70c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
