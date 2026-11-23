# 00bdbec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-81d65bea3999b144a2c979d4d0197faf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbec0",
  "name": "_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "389a3c0be0c3903edc5451f2c3a69954e2ac0947e32b9d81a1c9ae6cca4b9e70",
  "source_text_sha256": "389a3c0be0c3903edc5451f2c3a69954e2ac0947e32b9d81a1c9ae6cca4b9e70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbec0",
        "00bdbecf"
      ]
    ],
    "bytes_sha256": "201c58356bbdeb98dd7db056798c60fa842686c7fa4c6df62936513115c80014",
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
- [004c05ec](../004c0/004c05ec.md)
- [004e97e0](../004e9/004e97e0.md)
- [004fcb38](../004fc/004fcb38.md)

## 呼び出し先

- [00482240](../00482/00482240.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 331 bytes

~~~c

void _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE
               (void)

{
  (*(code *)
    PTR__ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE_00c1c798
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbec0"></a> `00bdbec0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbec4"></a> `00bdbec4` | `11 ce 43 f9` | ldr x17,[x16, #0x798] | `FALL_THROUGH`
<a id="insn-00bdbec8"></a> `00bdbec8` | `10 62 1e 91` | add x16,x16,#0x798 | `FALL_THROUGH`
<a id="insn-00bdbecc"></a> `00bdbecc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbec0`](#insn-00bdbec0) 範囲 `[['00bdbec0', '00bdbecf']]`

## 命令位置別の参照

- [`00bdbec4`](#insn-00bdbec4) → `00c1c798`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbecc`](#insn-00bdbecc) → [`00482240`](../00482/00482240.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00482240` · 推定シンボル `_ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbec4`](#insn-00bdbec4)

~~~json
{
  "source": "00bdbec4",
  "target": "00c1c798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c798",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbecc`](#insn-00bdbecc)

~~~json
{
  "source": "00bdbecc",
  "target": "00482240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
