# 00bdceb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-27e5187857375fc580422d8b374460b3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59900`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59900.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-76f053b8bbeb6bf3fffab0594ac9dbf3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdceb0",
  "name": "_ZNK5Botan14PKCS10_Request5is_CAEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5ed76e6cb95fb083561162f13ab6aaa676d9ca8568df842b6d67c2a04a950a7",
  "source_text_sha256": "e5ed76e6cb95fb083561162f13ab6aaa676d9ca8568df842b6d67c2a04a950a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdceb0",
        "00bdcebf"
      ]
    ],
    "bytes_sha256": "29ce979ceef3f6e87a87d80a3d473ccb5037b10b1fafbac963c751b75e5dfb8f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec73c](../004ec/004ec73c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZNK5Botan14PKCS10_Request5is_CAEv(void)

{
  (*(code *)PTR__ZNK5Botan14PKCS10_Request5is_CAEv_00c1d010)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdceb0"></a> `00bdceb0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdceb4"></a> `00bdceb4` | `11 0a 40 f9` | ldr x17,[x16, #0x10] | `FALL_THROUGH`
<a id="insn-00bdceb8"></a> `00bdceb8` | `10 42 00 91` | add x16,x16,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcebc"></a> `00bdcebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdceb0`](#insn-00bdceb0) 範囲 `[['00bdceb0', '00bdcebf']]`

## 命令位置別の参照

- [`00bdceb4`](#insn-00bdceb4) → `00c1d010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcebc`](#insn-00bdcebc) → [`004ec73c`](../004ec/004ec73c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ec73c` · 推定シンボル `_ZNK5Botan14PKCS10_Request5is_CAEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdceb4`](#insn-00bdceb4)

~~~json
{
  "source": "00bdceb4",
  "target": "00c1d010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcebc`](#insn-00bdcebc)

~~~json
{
  "source": "00bdcebc",
  "target": "004ec73c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
