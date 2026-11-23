# 00bdbef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbfa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbfa0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-5b79d18897ea8db04874f45ab5243c52)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbef0",
  "name": "_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2836f3d54b7a074e76f022f959d6ccd8cd15c3f6b53b7de96b11541629949694",
  "source_text_sha256": "2836f3d54b7a074e76f022f959d6ccd8cd15c3f6b53b7de96b11541629949694",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbef0",
        "00bdbeff"
      ]
    ],
    "bytes_sha256": "db85d7d493e2d63cbedba75ec036a06817444d839c33d338e0bd823e8a7a63e3",
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
    PTR__ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE_00c1c7b0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbef0"></a> `00bdbef0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbef4"></a> `00bdbef4` | `11 da 43 f9` | ldr x17,[x16, #0x7b0] | `FALL_THROUGH`
<a id="insn-00bdbef8"></a> `00bdbef8` | `10 c2 1e 91` | add x16,x16,#0x7b0 | `FALL_THROUGH`
<a id="insn-00bdbefc"></a> `00bdbefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbef0`](#insn-00bdbef0) 範囲 `[['00bdbef0', '00bdbeff']]`

## 命令位置別の参照

- [`00bdbef4`](#insn-00bdbef4) → `00c1c7b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbefc`](#insn-00bdbefc) → [`004a0a28`](../004a0/004a0a28.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004a0a28` · 推定シンボル `_ZN5Botan15Entropy_SourcesC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbef4`](#insn-00bdbef4)

~~~json
{
  "source": "00bdbef4",
  "target": "00c1c7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbefc`](#insn-00bdbefc)

~~~json
{
  "source": "00bdbefc",
  "target": "004a0a28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
