# 00bdffe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00be0090`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-99b3a8e54a774a670ff3055c246b5734)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdffe0",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20501929394b73fa82431a0ca36381b81e32a21ef26fa8fc4e2aeed34e384062",
  "source_text_sha256": "20501929394b73fa82431a0ca36381b81e32a21ef26fa8fc4e2aeed34e384062",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdffe0",
        "00bdffef"
      ]
    ],
    "bytes_sha256": "e7a37950afeb5e24d3644b003df04195fb61e52c29453b02a56bfa3cd65b767c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b261c4](../00b26/00b261c4.md)
- [00b3203c](../00b32/00b3203c.md)
- [00b331b0](../00b33/00b331b0.md)
- [00b33b54](../00b33/00b33b54.md)
- [00b44200](../00b44/00b44200.md)

## 呼び出し先

- [00b33600](../00b33/00b33600.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 709 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_
               (void)

{
                    /* try { // try from 00bdffe4 to 00cdffeb has its CatchHandler @ 00be0008 */
                    /* try { // try from 00bdffec to 00ce001b has its CatchHandler @ 00bdffcc */
  (*(code *)
    PTR__ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8__00c1e828
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdffe0"></a> `00bdffe0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdffe4"></a> `00bdffe4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bdffe8"></a> `00bdffe8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bdffec"></a> `00bdffec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdffe0`](#insn-00bdffe0) 範囲 `[['00bdffe0', '00bdffe3']]`
  - `FALL_THROUGH` [`00bdffe0`](#insn-00bdffe0) → [`00bdffe4`](#insn-00bdffe4)
- ブロック [`00bdffe4`](#insn-00bdffe4) 範囲 `[['00bdffe4', '00bdffeb']]`
  - `FALL_THROUGH` [`00bdffe8`](#insn-00bdffe8) → [`00bdffec`](#insn-00bdffec)
- ブロック [`00bdffec`](#insn-00bdffec) 範囲 `[['00bdffec', '00bdffef']]`

## 命令位置別の参照

- [`00bdffe4`](#insn-00bdffe4) → `00c1e828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdffec`](#insn-00bdffec) → [`00b33600`](../00b33/00b33600.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b33600` · 推定シンボル `_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS8_E9referenceEEE5valueENS_11__wrap_iterIPhEEE4typeENSC_IS6_EES8_S8_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdffe4`](#insn-00bdffe4)

~~~json
{
  "source": "00bdffe4",
  "target": "00c1e828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdffec`](#insn-00bdffec)

~~~json
{
  "source": "00bdffec",
  "target": "00b33600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
