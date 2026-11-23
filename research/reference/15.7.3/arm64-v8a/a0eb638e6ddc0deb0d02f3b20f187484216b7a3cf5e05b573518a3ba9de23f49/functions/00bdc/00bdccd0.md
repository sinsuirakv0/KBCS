# 00bdccd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcc20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-c0758d64709e0e1945537f0fe727a2fb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcd20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-c99266377e1633d9ed31fe6a04a3b4a2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccd0",
  "name": "_ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82d37cdbd2258de2fcd01f0832a2932c89046799b168d7d0cb392e4b032d5fe8",
  "source_text_sha256": "82d37cdbd2258de2fcd01f0832a2932c89046799b168d7d0cb392e4b032d5fe8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccd0",
        "00bdccdf"
      ]
    ],
    "bytes_sha256": "7a7f10c2926b32167584f480a5f23631e5ccaf0a7fa3975e8a6d1ce9e2ea6d87",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e4f2c](../004e4/004e4f2c.md)
- [004e5850](../004e5/004e5850.md)
- [004f1650](../004f1/004f1650.md)
- [004f1a6c](../004f1/004f1a6c.md)

## 呼び出し先

- [004f1734](../004f1/004f1734.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 293 bytes

~~~c

void _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1cef8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccd0"></a> `00bdccd0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccd4"></a> `00bdccd4` | `11 7e 47 f9` | ldr x17,[x16, #0xef8] | `FALL_THROUGH`
<a id="insn-00bdccd8"></a> `00bdccd8` | `10 e2 3b 91` | add x16,x16,#0xef8 | `FALL_THROUGH`
<a id="insn-00bdccdc"></a> `00bdccdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccd0`](#insn-00bdccd0) 範囲 `[['00bdccd0', '00bdccdf']]`

## 命令位置別の参照

- [`00bdccd4`](#insn-00bdccd4) → `00c1cef8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccdc`](#insn-00bdccdc) → [`004f1734`](../004f1/004f1734.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f1734` · 推定シンボル `_ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccd4`](#insn-00bdccd4)

~~~json
{
  "source": "00bdccd4",
  "target": "00c1cef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdccdc`](#insn-00bdccdc)

~~~json
{
  "source": "00bdccdc",
  "target": "004f1734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
