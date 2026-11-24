# 00bddcd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-8882d0646c68ccc6f7497b56ad45a12d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a720`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-55ddfb34e4d09c92aabe51e31d5249bb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcd0",
  "name": "_ZNK8firebase7Variant16assert_is_stringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93fd2db08d77e68eca804e87e53d69cd149a1c9890914aff4a5e544cdca339fa",
  "source_text_sha256": "93fd2db08d77e68eca804e87e53d69cd149a1c9890914aff4a5e544cdca339fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcd0",
        "00bddcdf"
      ]
    ],
    "bytes_sha256": "2fc681d7a3523f1704d13610c295d7ef3953f2078f2942600095f74562a49af3",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a9ec](../0084a/0084a9ec.md)
- [00ae1c64](../00ae1/00ae1c64.md)
- [00ae1e20](../00ae1/00ae1e20.md)
- [00af1a00](../00af1/00af1a00.md)
- [00b57438](../00b57/00b57438.md)

## 呼び出し先

- [00b04608](../00b04/00b04608.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 141 bytes

~~~c

void _ZNK8firebase7Variant16assert_is_stringEv(void)

{
  (*(code *)PTR__ZNK8firebase7Variant16assert_is_stringEv_00c1d720)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcd0"></a> `00bddcd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcd4"></a> `00bddcd4` | `11 92 43 f9` | ldr x17,[x16, #0x720] | `FALL_THROUGH`
<a id="insn-00bddcd8"></a> `00bddcd8` | `10 82 1c 91` | add x16,x16,#0x720 | `FALL_THROUGH`
<a id="insn-00bddcdc"></a> `00bddcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcd0`](#insn-00bddcd0) 範囲 `[['00bddcd0', '00bddcdf']]`

## 命令位置別の参照

- [`00bddcd4`](#insn-00bddcd4) → `00c1d720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcdc`](#insn-00bddcdc) → [`00b04608`](../00b04/00b04608.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b04608` · 推定シンボル `_ZNK8firebase7Variant16assert_is_stringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcd4`](#insn-00bddcd4)

~~~json
{
  "source": "00bddcd4",
  "target": "00c1d720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d720",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcdc`](#insn-00bddcdc)

~~~json
{
  "source": "00bddcdc",
  "target": "00b04608",
  "target_space": "ram",
  "resolution": "function"
}
~~~
