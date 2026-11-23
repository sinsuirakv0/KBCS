# 00bdcdd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcd20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-c41ffbb502a939257f3afd1579e349d9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdce20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-93f3fbeb158a5a9b71a484ca9ed5e775)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdd0",
  "name": "_ZN5Botan11BER_Decoder15decode_optionalINS_9X509_TimeEEERS0_RT_NS_8ASN1_TagES6_RKS4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "368cf5fb26888061fe5843a855e3d831ce35e17412c1749b8aaceec54bcdab37",
  "source_text_sha256": "368cf5fb26888061fe5843a855e3d831ce35e17412c1749b8aaceec54bcdab37",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdd0",
        "00bdcddf"
      ]
    ],
    "bytes_sha256": "f4c8d30278fce1dce775e9bfccdfeef57d92019c6f71d91f9df448faafca8cc4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e9fdc](../004e9/004e9fdc.md)

## 呼び出し先

- [004ea2b0](../004ea/004ea2b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 235 bytes

~~~c

void _ZN5Botan11BER_Decoder15decode_optionalINS_9X509_TimeEEERS0_RT_NS_8ASN1_TagES6_RKS4_(void)

{
  (*(code *)
    PTR__ZN5Botan11BER_Decoder15decode_optionalINS_9X509_TimeEEERS0_RT_NS_8ASN1_TagES6_RKS4__00c1cf78
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdd0"></a> `00bdcdd0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdd4"></a> `00bdcdd4` | `11 be 47 f9` | ldr x17,[x16, #0xf78] | `FALL_THROUGH`
<a id="insn-00bdcdd8"></a> `00bdcdd8` | `10 e2 3d 91` | add x16,x16,#0xf78 | `FALL_THROUGH`
<a id="insn-00bdcddc"></a> `00bdcddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdd0`](#insn-00bdcdd0) 範囲 `[['00bdcdd0', '00bdcddf']]`

## 命令位置別の参照

- [`00bdcdd4`](#insn-00bdcdd4) → `00c1cf78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcddc`](#insn-00bdcddc) → [`004ea2b0`](../004ea/004ea2b0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ea2b0` · 推定シンボル `_ZN5Botan11BER_Decoder15decode_optionalINS_9X509_TimeEEERS0_RT_NS_8ASN1_TagES6_RKS4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdd4`](#insn-00bdcdd4)

~~~json
{
  "source": "00bdcdd4",
  "target": "00c1cf78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcddc`](#insn-00bdcddc)

~~~json
{
  "source": "00bdcddc",
  "target": "004ea2b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
