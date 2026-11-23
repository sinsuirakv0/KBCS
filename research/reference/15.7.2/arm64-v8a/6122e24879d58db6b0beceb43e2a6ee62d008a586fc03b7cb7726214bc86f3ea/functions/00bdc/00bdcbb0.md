# 00bdcbb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-efde0107afc0e5aa9c4f25938f876c20)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbb0",
  "name": "_ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "466349cf773eb369cb4d97b52f685c0c31a5481351e98d3b88297e77c70580a1",
  "source_text_sha256": "466349cf773eb369cb4d97b52f685c0c31a5481351e98d3b88297e77c70580a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbb0",
        "00bdcbbf"
      ]
    ],
    "bytes_sha256": "23c4920d42db4548304eb418ead8073469ea5ecbb1b695875445de995fd39a4b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e1f38](../004e1/004e1f38.md)
- [004e20fc](../004e2/004e20fc.md)
- [004e40b8](../004e4/004e40b8.md)
- [004e5850](../004e5/004e5850.md)
- [004f10f4](../004f1/004f10f4.md)
- [004f1394](../004f1/004f1394.md)
- [0050af44](../0050a/0050af44.md)

## 呼び出し先

- [004f11e0](../004f1/004f11e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE_00c1ce10
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbb0"></a> `00bdcbb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbb4"></a> `00bdcbb4` | `11 0a 47 f9` | ldr x17,[x16, #0xe10] | `FALL_THROUGH`
<a id="insn-00bdcbb8"></a> `00bdcbb8` | `10 42 38 91` | add x16,x16,#0xe10 | `FALL_THROUGH`
<a id="insn-00bdcbbc"></a> `00bdcbbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbb0`](#insn-00bdcbb0) 範囲 `[['00bdcbb0', '00bdcbbf']]`

## 命令位置別の参照

- [`00bdcbb4`](#insn-00bdcbb4) → `00c1ce10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbbc`](#insn-00bdcbbc) → [`004f11e0`](../004f1/004f11e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f11e0` · 推定シンボル `_ZN5Botan7X509_DN13add_attributeERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbb4`](#insn-00bdcbb4)

~~~json
{
  "source": "00bdcbb4",
  "target": "00c1ce10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbbc`](#insn-00bdcbbc)

~~~json
{
  "source": "00bdcbbc",
  "target": "004f11e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
