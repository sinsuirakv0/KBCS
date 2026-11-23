# 00bdbed0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-fcd89d407c77bef6e40319ea64e631d2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbed0",
  "name": "_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "488bf890b88d217df6c07bf8375101921b67112d44af74518895bb286338cfe4",
  "source_text_sha256": "488bf890b88d217df6c07bf8375101921b67112d44af74518895bb286338cfe4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbed0",
        "00bdbedf"
      ]
    ],
    "bytes_sha256": "d48f1893c001e6b7dbf8a2e7762bb9d551dce2f2c9327a11e32004e4fe4c5c00",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049f624](../0049f/0049f624.md)
- [004bf57c](../004bf/004bf57c.md)
- [004fcb38](../004fc/004fcb38.md)

## 呼び出し先

- [0047f40c](../0047f/0047f40c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 337 bytes

~~~c

void _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE_00c1c7a0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbed0"></a> `00bdbed0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbed4"></a> `00bdbed4` | `11 d2 43 f9` | ldr x17,[x16, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bdbed8"></a> `00bdbed8` | `10 82 1e 91` | add x16,x16,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bdbedc"></a> `00bdbedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbed0`](#insn-00bdbed0) 範囲 `[['00bdbed0', '00bdbedf']]`

## 命令位置別の参照

- [`00bdbed4`](#insn-00bdbed4) → `00c1c7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbedc`](#insn-00bdbedc) → [`0047f40c`](../0047f/0047f40c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0047f40c` · 推定シンボル `_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbed4`](#insn-00bdbed4)

~~~json
{
  "source": "00bdbed4",
  "target": "00c1c7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbedc`](#insn-00bdbedc)

~~~json
{
  "source": "00bdbedc",
  "target": "0047f40c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
