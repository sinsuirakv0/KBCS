# 00bdcff0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcf40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-881d97ed628d9693101b14d511a3bd1b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdd040`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd040.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-b42c51df8102265c06879614b8534e3d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcff0",
  "name": "_ZNK5Botan11X509_Object23hash_used_for_signatureEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b94a810e36efd4b000c7e68a4fd7e77c3cfa4ef50f2cd52cc0e291c6822ad85",
  "source_text_sha256": "7b94a810e36efd4b000c7e68a4fd7e77c3cfa4ef50f2cd52cc0e291c6822ad85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcff0",
        "00bdcfff"
      ]
    ],
    "bytes_sha256": "50b7870660c4e68db6c01b5398b70e19655c8c568315b031f895ef7453b46eb9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00503af8](../00503/00503af8.md)
- [0050a3ac](../0050a/0050a3ac.md)

## 呼び出し先

- [004fc6ac](../004fc/004fc6ac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 256 bytes

~~~c

void _ZNK5Botan11X509_Object23hash_used_for_signatureEv(void)

{
                    /* try { // try from 00bdcff4 to 00cdd04f has its CatchHandler @ 00bdcc94 */
  (*(code *)PTR__ZNK5Botan11X509_Object23hash_used_for_signatureEv_00c1d088)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcff0"></a> `00bdcff0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcff4"></a> `00bdcff4` | `11 46 40 f9` | ldr x17,[x16, #0x88] | `FALL_THROUGH`
<a id="insn-00bdcff8"></a> `00bdcff8` | `10 22 02 91` | add x16,x16,#0x88 | `FALL_THROUGH`
<a id="insn-00bdcffc"></a> `00bdcffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcff0`](#insn-00bdcff0) 範囲 `[['00bdcff0', '00bdcff3']]`
  - `FALL_THROUGH` [`00bdcff0`](#insn-00bdcff0) → [`00bdcff4`](#insn-00bdcff4)
- ブロック [`00bdcff4`](#insn-00bdcff4) 範囲 `[['00bdcff4', '00bdcfff']]`

## 命令位置別の参照

- [`00bdcff4`](#insn-00bdcff4) → `00c1d088`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcffc`](#insn-00bdcffc) → [`004fc6ac`](../004fc/004fc6ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004fc6ac` · 推定シンボル `_ZNK5Botan11X509_Object23hash_used_for_signatureEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcff4`](#insn-00bdcff4)

~~~json
{
  "source": "00bdcff4",
  "target": "00c1d088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d088",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcffc`](#insn-00bdcffc)

~~~json
{
  "source": "00bdcffc",
  "target": "004fc6ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
