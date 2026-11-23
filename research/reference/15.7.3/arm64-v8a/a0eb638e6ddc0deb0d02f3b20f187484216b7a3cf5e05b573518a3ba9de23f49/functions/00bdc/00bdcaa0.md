# 00bdcaa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdc9f0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc9f0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-314f7c5b0ec9ee4e710458414256bac5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcaf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcaf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-9099344296ef9daf93b01dde7ae2acb3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcaa0",
  "name": "_ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fa6b2897a9e1737d700ed66663e9ddb8306f75af3431968c2bed897e4874367",
  "source_text_sha256": "6fa6b2897a9e1737d700ed66663e9ddb8306f75af3431968c2bed897e4874367",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcaa0",
        "00bdcaaf"
      ]
    ],
    "bytes_sha256": "c1f56c8b10bb7e2337c91550933adc4b1194d0d1a3eaa7859365c0abd6e86be7",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004db550](../004db/004db550.md)

## 呼び出し先

- [004db3c8](../004db/004db3c8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

void _ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE(void)

{
  (*(code *)
    PTR__ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_00c1cde0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcaa0"></a> `00bdcaa0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcaa4"></a> `00bdcaa4` | `11 f2 46 f9` | ldr x17,[x16, #0xde0] | `FALL_THROUGH`
<a id="insn-00bdcaa8"></a> `00bdcaa8` | `10 82 37 91` | add x16,x16,#0xde0 | `FALL_THROUGH`
<a id="insn-00bdcaac"></a> `00bdcaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcaa0`](#insn-00bdcaa0) 範囲 `[['00bdcaa0', '00bdcaaf']]`

## 命令位置別の参照

- [`00bdcaa4`](#insn-00bdcaa4) → `00c1cde0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcaac`](#insn-00bdcaac) → [`004db3c8`](../004db/004db3c8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004db3c8` · 推定シンボル `_ZN5Botan8clean_wsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcaa4`](#insn-00bdcaa4)

~~~json
{
  "source": "00bdcaa4",
  "target": "00c1cde0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cde0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcaac`](#insn-00bdcaac)

~~~json
{
  "source": "00bdcaac",
  "target": "004db3c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
