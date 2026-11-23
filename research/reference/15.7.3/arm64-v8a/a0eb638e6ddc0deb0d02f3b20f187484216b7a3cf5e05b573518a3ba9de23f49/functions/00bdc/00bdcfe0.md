# 00bdcfe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcf30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-94585710efd49528a081cc6e2e54207a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdd030`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd030.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-7822efca84125e2b617c1c31d3e438a2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfe0",
  "name": "_ZNK5Botan11X509_Object10BER_encodeEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6051f169e3cc8c10b63beb32697b5cb54918f4df7d3a9f3e52326f2dca4b99d7",
  "source_text_sha256": "6051f169e3cc8c10b63beb32697b5cb54918f4df7d3a9f3e52326f2dca4b99d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfe0",
        "00bdcfef"
      ]
    ],
    "bytes_sha256": "3bf5d1d58d61a409526ee02d3ed35ff4b07fd49c20ff6376df1b06654ac22dc8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004fc5bc](../004fc/004fc5bc.md)
- [0050168c](../00501/0050168c.md)
- [0050645c](../00506/0050645c.md)
- [00506ee0](../00506/00506ee0.md)

## 呼び出し先

- [004fc4b0](../004fc/004fc4b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 133 bytes

~~~c

void _ZNK5Botan11X509_Object10BER_encodeEv(void)

{
  (*(code *)PTR__ZNK5Botan11X509_Object10BER_encodeEv_00c1d080)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfe0"></a> `00bdcfe0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfe4"></a> `00bdcfe4` | `11 42 40 f9` | ldr x17,[x16, #0x80] | `FALL_THROUGH`
<a id="insn-00bdcfe8"></a> `00bdcfe8` | `10 02 02 91` | add x16,x16,#0x80 | `FALL_THROUGH`
<a id="insn-00bdcfec"></a> `00bdcfec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfe0`](#insn-00bdcfe0) 範囲 `[['00bdcfe0', '00bdcfef']]`

## 命令位置別の参照

- [`00bdcfe4`](#insn-00bdcfe4) → `00c1d080`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfec`](#insn-00bdcfec) → [`004fc4b0`](../004fc/004fc4b0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004fc4b0` · 推定シンボル `_ZNK5Botan11X509_Object10BER_encodeEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfe4`](#insn-00bdcfe4)

~~~json
{
  "source": "00bdcfe4",
  "target": "00c1d080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d080",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfec`](#insn-00bdcfec)

~~~json
{
  "source": "00bdcfec",
  "target": "004fc4b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
