# 00bdbfa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbef0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-5b79d18897ea8db04874f45ab5243c52)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbff0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-27dc7d3fa3e21fa4bd558e570676d471)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfa0",
  "name": "_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be1b390c0af85f3f4ed6c7c6bf65c2d00841dea96b73edf7697d41d505c74894",
  "source_text_sha256": "be1b390c0af85f3f4ed6c7c6bf65c2d00841dea96b73edf7697d41d505c74894",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfa0",
        "00bdbfaf"
      ]
    ],
    "bytes_sha256": "98f1c26207d527f6e4b453404846ef5d1fb0c850066e26a03ea0f2731e86137a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a0c64](../004a0/004a0c64.md)

## 呼び出し先

- [004a0a28](../004a0/004a0a28.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE_00c1c860
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfa0"></a> `00bdbfa0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfa4"></a> `00bdbfa4` | `11 32 44 f9` | ldr x17,[x16, #0x860] | `FALL_THROUGH`
<a id="insn-00bdbfa8"></a> `00bdbfa8` | `10 82 21 91` | add x16,x16,#0x860 | `FALL_THROUGH`
<a id="insn-00bdbfac"></a> `00bdbfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfa0`](#insn-00bdbfa0) 範囲 `[['00bdbfa0', '00bdbfaf']]`

## 命令位置別の参照

- [`00bdbfa4`](#insn-00bdbfa4) → `00c1c860`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfac`](#insn-00bdbfac) → [`004a0a28`](../004a0/004a0a28.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004a0a28` · 推定シンボル `_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfa4`](#insn-00bdbfa4)

~~~json
{
  "source": "00bdbfa4",
  "target": "00c1c860",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c860",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfac`](#insn-00bdbfac)

~~~json
{
  "source": "00bdbfac",
  "target": "004a0a28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
