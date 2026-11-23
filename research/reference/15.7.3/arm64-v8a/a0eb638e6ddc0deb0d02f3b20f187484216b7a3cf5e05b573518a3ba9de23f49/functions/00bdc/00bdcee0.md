# 00bdcee0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdce30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-b0b2c96753fec8c172c9e3d5460bb311)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcf30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-a4647f2a2bc4f8ad8bfdad34c9ac00fe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcee0",
  "name": "_ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorENS4_6chrono10time_pointINSE_12system_clockENSE_8durationIxNS4_5ratioILl1ELl1000000EEEEEEENSH_IxNSI_ILl1ELl1EEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32c6910af758c14fb70d0eeb2aedadb7160e25d8b335abb1117fac2d9276fd9a",
  "source_text_sha256": "32c6910af758c14fb70d0eeb2aedadb7160e25d8b335abb1117fac2d9276fd9a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcee0",
        "00bdceef"
      ]
    ],
    "bytes_sha256": "d27c3b05d20672250afeb40695fcf5a54f9d2533bdd39bad3575f68af38425f2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004eef24](../004ee/004eef24.md)

## 呼び出し先

- [004eef84](../004ee/004eef84.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 567 bytes

~~~c

void _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorENS4_6chrono10time_pointINSE_12system_clockENSE_8durationIxNS4_5ratioILl1ELl1000000EEEEEEENSH_IxNSI_ILl1ELl1EEEEE
               (void)

{
  (*(code *)
    PTR__ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorENS4_6chrono10time_pointINSE_12system_clockENSE_8durationIxNS4_5ratioILl1ELl1000000EEEEEEENSH_IxNSI_ILl1ELl1EEEEE_00c1d000
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcee0"></a> `00bdcee0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcee4"></a> `00bdcee4` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bdcee8"></a> `00bdcee8` | `10 02 00 91` | add x16,x16,#0x0 | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcee0`](#insn-00bdcee0) 範囲 `[['00bdcee0', '00bdceef']]`

## 命令位置別の参照

- [`00bdcee4`](#insn-00bdcee4) → `00c1d000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdceec`](#insn-00bdceec) → [`004eef84`](../004ee/004eef84.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004eef84` · 推定シンボル `_ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorENS4_6chrono10time_pointINSE_12system_clockENSE_8durationIxNS4_5ratioILl1ELl1000000EEEEEEENSH_IxNSI_ILl1ELl1EEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcee4`](#insn-00bdcee4)

~~~json
{
  "source": "00bdcee4",
  "target": "00c1d000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdceec`](#insn-00bdceec)

~~~json
{
  "source": "00bdceec",
  "target": "004eef84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
