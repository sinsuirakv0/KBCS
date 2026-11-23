# 00bdffc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00be0070`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0070.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-dac356f991a0548739f57dcf84bdf344)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdffc0",
  "name": "_ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9906df238029384b81843c4cd3a7ef9647dd28492d09159c4b9f7367b18e705",
  "source_text_sha256": "b9906df238029384b81843c4cd3a7ef9647dd28492d09159c4b9f7367b18e705",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdffc0",
        "00bdffcf"
      ]
    ],
    "bytes_sha256": "49c5343bc1ac88da72112b697a33fc856141083c3fd23988a2a68972e72b97f6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1cedc](../00b1c/00b1cedc.md)

## 呼び出し先

- [00b2eb24](../00b2e/00b2eb24.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 776 bytes

~~~c

void _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_
               (void)

{
                    /* try { // try from 00bdffcc to 00cdffe3 has its CatchHandler @ 00bdffcc
                       catch() { ... } // from try @ 00bdffcc with catch @ 00bdffcc
                       catch() { ... } // from try @ 00bdffec with catch @ 00bdffcc */
  (*(code *)
    PTR__ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA__00c1e818
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdffc0"></a> `00bdffc0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdffc4"></a> `00bdffc4` | `11 0e 44 f9` | ldr x17,[x16, #0x818] | `FALL_THROUGH`
<a id="insn-00bdffc8"></a> `00bdffc8` | `10 62 20 91` | add x16,x16,#0x818 | `FALL_THROUGH`
<a id="insn-00bdffcc"></a> `00bdffcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdffc0`](#insn-00bdffc0) 範囲 `[['00bdffc0', '00bdffcb']]`
  - `FALL_THROUGH` [`00bdffc8`](#insn-00bdffc8) → [`00bdffcc`](#insn-00bdffcc)
- ブロック [`00bdffcc`](#insn-00bdffcc) 範囲 `[['00bdffcc', '00bdffcf']]`

## 命令位置別の参照

- [`00bdffc4`](#insn-00bdffc4) → `00c1e818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdffcc`](#insn-00bdffcc) → [`00b2eb24`](../00b2e/00b2eb24.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b2eb24` · 推定シンボル `_ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdffc4`](#insn-00bdffc4)

~~~json
{
  "source": "00bdffc4",
  "target": "00c1e818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e818",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdffcc`](#insn-00bdffcc)

~~~json
{
  "source": "00bdffcc",
  "target": "00b2eb24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
