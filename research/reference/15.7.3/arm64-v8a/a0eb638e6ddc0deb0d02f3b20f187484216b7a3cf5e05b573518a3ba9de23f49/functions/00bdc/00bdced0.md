# 00bdced0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdce20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-f6199428197b091da648c815d77fffc5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcf20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-48444bd059a85eb35fd2eb890ca8baa0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdced0",
  "name": "_ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "217244c01fab16af24efbb55486813a7af2b3b0c50443346de8c9e327864d7a7",
  "source_text_sha256": "217244c01fab16af24efbb55486813a7af2b3b0c50443346de8c9e327864d7a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdced0",
        "00bdcedf"
      ]
    ],
    "bytes_sha256": "5a03dd51b1dc105495733aab9383a35ff7b5352b66e94f21283a22709fb9654e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004eedec](../004ee/004eedec.md)
- [004eee9c](../004ee/004eee9c.md)
- [004eef84](../004ee/004eef84.md)

## 呼び出し先

- [004ef204](../004ef/004ef204.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 533 bytes

~~~c

void _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE
               (void)

{
  (*(code *)
    PTR__ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE_00c1cff8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdced0"></a> `00bdced0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdced4"></a> `00bdced4` | `11 fe 47 f9` | ldr x17,[x16, #0xff8] | `FALL_THROUGH`
<a id="insn-00bdced8"></a> `00bdced8` | `10 e2 3f 91` | add x16,x16,#0xff8 | `FALL_THROUGH`
<a id="insn-00bdcedc"></a> `00bdcedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdced0`](#insn-00bdced0) 範囲 `[['00bdced0', '00bdcedf']]`

## 命令位置別の参照

- [`00bdced4`](#insn-00bdced4) → `00c1cff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcedc`](#insn-00bdcedc) → [`004ef204`](../004ef/004ef204.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ef204` · 推定シンボル `_ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB_12system_clockENSB_8durationIxNS1_5ratioILl1ELl1000000EEEEEEENSE_IxNSF_ILl1ELl1EEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdced4`](#insn-00bdced4)

~~~json
{
  "source": "00bdced4",
  "target": "00c1cff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcedc`](#insn-00bdcedc)

~~~json
{
  "source": "00bdcedc",
  "target": "004ef204",
  "target_space": "ram",
  "resolution": "function"
}
~~~
