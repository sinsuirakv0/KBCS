# 00bddca0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-7e9e4f012135654bf12accff5a51b1dc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a6f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-45ad0a096e70bad1ad5789eb64b4560f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddca0",
  "name": "_ZNK8firebase7Variant7AsInt64Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "245a23d29746b0e991af16a5a58c8437791af5ac8466347994ca8ecce6756eab",
  "source_text_sha256": "245a23d29746b0e991af16a5a58c8437791af5ac8466347994ca8ecce6756eab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddca0",
        "00bddcaf"
      ]
    ],
    "bytes_sha256": "7dca9241a8f05d1753a0a896503943c5d803796cdba1586668f12fe903e16549",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a918](../0084a/0084a918.md)

## 呼び出し先

- [00b0490c](../00b04/00b0490c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

void _ZNK8firebase7Variant7AsInt64Ev(void)

{
  (*(code *)PTR__ZNK8firebase7Variant7AsInt64Ev_00c1d708)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddca0"></a> `00bddca0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddca4"></a> `00bddca4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bddca8"></a> `00bddca8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bddcac"></a> `00bddcac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddca0`](#insn-00bddca0) 範囲 `[['00bddca0', '00bddcaf']]`

## 命令位置別の参照

- [`00bddca4`](#insn-00bddca4) → `00c1d708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcac`](#insn-00bddcac) → [`00b0490c`](../00b04/00b0490c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0490c` · 推定シンボル `_ZNK8firebase7Variant7AsInt64Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddca4`](#insn-00bddca4)

~~~json
{
  "source": "00bddca4",
  "target": "00c1d708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcac`](#insn-00bddcac)

~~~json
{
  "source": "00bddcac",
  "target": "00b0490c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
