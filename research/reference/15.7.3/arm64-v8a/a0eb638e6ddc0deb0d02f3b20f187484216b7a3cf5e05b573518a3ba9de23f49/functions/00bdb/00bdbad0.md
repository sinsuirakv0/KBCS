# 00bdbad0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdba20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdba20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-2274a76beadaab5499fa27c8b6ad390a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbb20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-c756dbaa313fa936b37e10661fe86a02)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbad0",
  "name": "_ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a38d00e5b85123b9ea157005a591326fdcdd1a9d4ea94ef6fe2b9e647955dd22",
  "source_text_sha256": "a38d00e5b85123b9ea157005a591326fdcdd1a9d4ea94ef6fe2b9e647955dd22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbad0",
        "00bdbadf"
      ]
    ],
    "bytes_sha256": "39f2ddc65e74f1e8a8b6d4c6872624cc1834e3092a2a9a20657c91ae942bf5fb",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048a2e0](../0048a/0048a2e0.md)
- [004d6550](../004d6/004d6550.md)

## 呼び出し先

- [0048a2e8](../0048a/0048a2e8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 273 bytes

~~~c

void _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_00c1c5f8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbad0"></a> `00bdbad0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbad4"></a> `00bdbad4` | `11 fe 42 f9` | ldr x17,[x16, #0x5f8] | `FALL_THROUGH`
<a id="insn-00bdbad8"></a> `00bdbad8` | `10 e2 17 91` | add x16,x16,#0x5f8 | `FALL_THROUGH`
<a id="insn-00bdbadc"></a> `00bdbadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbad0`](#insn-00bdbad0) 範囲 `[['00bdbad0', '00bdbadf']]`

## 命令位置別の参照

- [`00bdbad4`](#insn-00bdbad4) → `00c1c5f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbadc`](#insn-00bdbadc) → [`0048a2e8`](../0048a/0048a2e8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048a2e8` · 推定シンボル `_ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbad4`](#insn-00bdbad4)

~~~json
{
  "source": "00bdbad4",
  "target": "00c1c5f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c5f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbadc`](#insn-00bdbadc)

~~~json
{
  "source": "00bdbadc",
  "target": "0048a2e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
