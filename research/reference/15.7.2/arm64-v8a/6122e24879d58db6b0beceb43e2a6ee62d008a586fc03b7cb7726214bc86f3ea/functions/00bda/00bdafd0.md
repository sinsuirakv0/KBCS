# 00bdafd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdb080`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb080.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-171d0c01db86bfc10e9d80a4f8446089)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafd0",
  "name": "__cxa_free_exception",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f4a4b255c15d2deca908ab65233b092b0f920fbd51c7718fbbaa107fd7918d3",
  "source_text_sha256": "8f4a4b255c15d2deca908ab65233b092b0f920fbd51c7718fbbaa107fd7918d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafd0",
        "00bdafdf"
      ]
    ],
    "bytes_sha256": "e4077cd60fb269bc52f4ffea4920c30ef28933ae5ad3c94be24a861e9b3d3ce9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005054cc](../00505/005054cc.md)
- [005060a8](../00506/005060a8.md)

## 呼び出し先

- [00bd4fe8](../00bd4/00bd4fe8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 186 bytes

~~~c

void __cxa_free_exception(void)

{
                    /* catch() { ... } // from try @ 00bdaf74 with catch @ 00bdafdc */
  (*(code *)PTR___cxa_free_exception_00c1c020)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafd0"></a> `00bdafd0` | `10 02 00 d0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdafd4"></a> `00bdafd4` | `11 12 40 f9` | ldr x17,[x16, #0x20] | `FALL_THROUGH`
<a id="insn-00bdafd8"></a> `00bdafd8` | `10 82 00 91` | add x16,x16,#0x20 | `FALL_THROUGH`
<a id="insn-00bdafdc"></a> `00bdafdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafd0`](#insn-00bdafd0) 範囲 `[['00bdafd0', '00bdafdb']]`
  - `FALL_THROUGH` [`00bdafd8`](#insn-00bdafd8) → [`00bdafdc`](#insn-00bdafdc)
- ブロック [`00bdafdc`](#insn-00bdafdc) 範囲 `[['00bdafdc', '00bdafdf']]`

## 命令位置別の参照

- [`00bdafd4`](#insn-00bdafd4) → `00c1c020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdafdc`](#insn-00bdafdc) → [`00bd4fe8`](../00bd4/00bd4fe8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bd4fe8` · 推定シンボル `__cxa_free_exception` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafd4`](#insn-00bdafd4)

~~~json
{
  "source": "00bdafd4",
  "target": "00c1c020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c020",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdafdc`](#insn-00bdafdc)

~~~json
{
  "source": "00bdafdc",
  "target": "00bd4fe8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
