# 00bdfbf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfb40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-2fba28b226dee404830097d6a26428d3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfc40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-052cff811bd8a5bf8fe4cae4ae18be10)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbf0",
  "name": "_ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "27d377647808d4d6d6c9a976cdeed7d845953a86d4d33d7cef23209032010106",
  "source_text_sha256": "27d377647808d4d6d6c9a976cdeed7d845953a86d4d33d7cef23209032010106",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbf0",
        "00bdfbff"
      ]
    ],
    "bytes_sha256": "0d6f75790535f8399a05496de641d44abe6f34046f144e0994ac87d832073a1d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b29458](../00b29/00b29458.md)

## 呼び出し先

- [00b2bde0](../00b2b/00b2bde0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 218 bytes

~~~c

void _ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE(void)

{
  (*(code *)PTR__ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE_00c1e688)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfbf0"></a> `00bdfbf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfbf4"></a> `00bdfbf4` | `11 46 43 f9` | ldr x17,[x16, #0x688] | `FALL_THROUGH`
<a id="insn-00bdfbf8"></a> `00bdfbf8` | `10 22 1a 91` | add x16,x16,#0x688 | `FALL_THROUGH`
<a id="insn-00bdfbfc"></a> `00bdfbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbf0`](#insn-00bdfbf0) 範囲 `[['00bdfbf0', '00bdfbff']]`

## 命令位置別の参照

- [`00bdfbf4`](#insn-00bdfbf4) → `00c1e688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfbfc`](#insn-00bdfbfc) → [`00b2bde0`](../00b2b/00b2bde0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b2bde0` · 推定シンボル `_ZNK11flatbuffers7EnumVal9SerializeEPNS_17FlatBufferBuilderERKNS_6ParserE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbf4`](#insn-00bdfbf4)

~~~json
{
  "source": "00bdfbf4",
  "target": "00c1e688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e688",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfbfc`](#insn-00bdfbfc)

~~~json
{
  "source": "00bdfbfc",
  "target": "00b2bde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
