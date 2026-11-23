# 00bdcfb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcf00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-577fe9115956bb1c76b90dfe4e59f77f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdd000`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd000.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-70238dbcc037b792e8c1ffce343d4e78)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfb0",
  "name": "_ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63b346ee3c5d4478a64562752167a2ef8f8f48cab862163603052ff337ced170",
  "source_text_sha256": "63b346ee3c5d4478a64562752167a2ef8f8f48cab862163603052ff337ced170",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfb0",
        "00bdcfbf"
      ]
    ],
    "bytes_sha256": "578ce9e4a4cc4f7d120a68c4bb899cc86061b4ad6140f5b8e111db0168e8f16f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004f8244](../004f8/004f8244.md)

## 呼び出し先

- [004f8990](../004f8/004f8990.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 402 bytes

~~~c

void _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (void)

{
                    /* try { // try from 00bdcfbc to 00cdcfc7 has its CatchHandler @ 00bdd254 */
  (*(code *)
    PTR__ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1d068
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfb0"></a> `00bdcfb0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfb4"></a> `00bdcfb4` | `11 36 40 f9` | ldr x17,[x16, #0x68] | `FALL_THROUGH`
<a id="insn-00bdcfb8"></a> `00bdcfb8` | `10 a2 01 91` | add x16,x16,#0x68 | `FALL_THROUGH`
<a id="insn-00bdcfbc"></a> `00bdcfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfb0`](#insn-00bdcfb0) 範囲 `[['00bdcfb0', '00bdcfbb']]`
  - `FALL_THROUGH` [`00bdcfb8`](#insn-00bdcfb8) → [`00bdcfbc`](#insn-00bdcfbc)
- ブロック [`00bdcfbc`](#insn-00bdcfbc) 範囲 `[['00bdcfbc', '00bdcfbf']]`

## 命令位置別の参照

- [`00bdcfb4`](#insn-00bdcfb4) → `00c1d068`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfbc`](#insn-00bdcfbc) → [`004f8990`](../004f8/004f8990.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f8990` · 推定シンボル `_ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfb4`](#insn-00bdcfb4)

~~~json
{
  "source": "00bdcfb4",
  "target": "00c1d068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d068",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfbc`](#insn-00bdcfbc)

~~~json
{
  "source": "00bdcfbc",
  "target": "004f8990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
