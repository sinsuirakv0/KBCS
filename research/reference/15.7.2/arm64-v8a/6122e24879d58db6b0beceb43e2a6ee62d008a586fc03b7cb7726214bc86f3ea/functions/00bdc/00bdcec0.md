# 00bdcec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcf70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-ead6f382a8592f12562378d3c59d10b4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcec0",
  "name": "_ZN5Botan11BER_Decoder15decode_optionalIbEERS0_RT_NS_8ASN1_TagES5_RKS3_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f6ce4e62a128d74677f5710ed0f05ae86df73c9124b20220ed07f4b4a8ecd1a",
  "source_text_sha256": "1f6ce4e62a128d74677f5710ed0f05ae86df73c9124b20220ed07f4b4a8ecd1a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcec0",
        "00bdcecf"
      ]
    ],
    "bytes_sha256": "143eb5c5027d1584737f5a7ed6f0c56f6f1e83ac7b7c48cbc3e765ee6a1547b9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004f4778](../004f4/004f4778.md)
- [004f52c8](../004f5/004f52c8.md)

## 呼び出し先

- [004f4ba8](../004f4/004f4ba8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 201 bytes

~~~c

void _ZN5Botan11BER_Decoder15decode_optionalIbEERS0_RT_NS_8ASN1_TagES5_RKS3_(void)

{
  (*(code *)PTR__ZN5Botan11BER_Decoder15decode_optionalIbEERS0_RT_NS_8ASN1_TagES5_RKS3__00c1cf98)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcec0"></a> `00bdcec0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcec4"></a> `00bdcec4` | `11 ce 47 f9` | ldr x17,[x16, #0xf98] | `FALL_THROUGH`
<a id="insn-00bdcec8"></a> `00bdcec8` | `10 62 3e 91` | add x16,x16,#0xf98 | `FALL_THROUGH`
<a id="insn-00bdcecc"></a> `00bdcecc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcec0`](#insn-00bdcec0) 範囲 `[['00bdcec0', '00bdcecf']]`

## 命令位置別の参照

- [`00bdcec4`](#insn-00bdcec4) → `00c1cf98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcecc`](#insn-00bdcecc) → [`004f4ba8`](../004f4/004f4ba8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f4ba8` · 推定シンボル `_ZN5Botan11BER_Decoder15decode_optionalIbEERS0_RT_NS_8ASN1_TagES5_RKS3_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcec4`](#insn-00bdcec4)

~~~json
{
  "source": "00bdcec4",
  "target": "00c1cf98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcecc`](#insn-00bdcecc)

~~~json
{
  "source": "00bdcecc",
  "target": "004f4ba8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
