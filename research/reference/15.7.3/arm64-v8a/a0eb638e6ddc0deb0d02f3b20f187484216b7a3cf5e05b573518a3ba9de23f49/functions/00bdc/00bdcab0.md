# 00bdcab0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdca00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdca00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-f6d69743171519c449b619fff2289c68)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcb00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-f80a239ceddd7b810ffe92971771862c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcab0",
  "name": "_ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb51e826775a4a5ed26ed036999d63001facecf64a88013767235165b52a71a5",
  "source_text_sha256": "fb51e826775a4a5ed26ed036999d63001facecf64a88013767235165b52a71a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcab0",
        "00bdcabf"
      ]
    ],
    "bytes_sha256": "9939e7763fb369dfa26761b0bd269e303d837bc86f7bb5eac24f74d1e3b11936",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004dbf98](../004db/004dbf98.md)
- [004dcf48](../004dc/004dcf48.md)
- [004e21a8](../004e2/004e21a8.md)
- [004eb16c](../004eb/004eb16c.md)

## 呼び出し先

- [004dc168](../004dc/004dc168.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 311 bytes

~~~c

void _ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9__00c1cde8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcab0"></a> `00bdcab0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcab4"></a> `00bdcab4` | `11 f6 46 f9` | ldr x17,[x16, #0xde8] | `FALL_THROUGH`
<a id="insn-00bdcab8"></a> `00bdcab8` | `10 a2 37 91` | add x16,x16,#0xde8 | `FALL_THROUGH`
<a id="insn-00bdcabc"></a> `00bdcabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcab0`](#insn-00bdcab0) 範囲 `[['00bdcab0', '00bdcabf']]`

## 命令位置別の参照

- [`00bdcab4`](#insn-00bdcab4) → `00c1cde8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcabc`](#insn-00bdcabc) → [`004dc168`](../004dc/004dc168.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004dc168` · 推定シンボル `_ZN5Botan15AlternativeName13add_attributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcab4`](#insn-00bdcab4)

~~~json
{
  "source": "00bdcab4",
  "target": "00c1cde8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cde8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcabc`](#insn-00bdcabc)

~~~json
{
  "source": "00bdcabc",
  "target": "004dc168",
  "target_space": "ram",
  "resolution": "function"
}
~~~
