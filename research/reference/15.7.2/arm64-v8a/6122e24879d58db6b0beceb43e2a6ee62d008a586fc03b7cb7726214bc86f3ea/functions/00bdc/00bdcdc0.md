# 00bdcdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-305eca42998944cc2d8db46dd4c18a13)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZNK5Botan14PKCS10_Request10path_limitEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8fe3a83f15077ed4d1a65f6595de2eac4ba567cd4d65a746d1a4caeb27b470e",
  "source_text_sha256": "e8fe3a83f15077ed4d1a65f6595de2eac4ba567cd4d65a746d1a4caeb27b470e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdc0",
        "00bdcdcf"
      ]
    ],
    "bytes_sha256": "bb101edb063256aeba8f56b1b44c0f749314e53454105780c6ed13d9144b20c9",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec8c8](../004ec/004ec8c8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 236 bytes

~~~c

void _ZNK5Botan14PKCS10_Request10path_limitEv(void)

{
                    /* try { // try from 00bdcdc8 to 00cdcddf has its CatchHandler @ 00bdd1a0 */
  (*(code *)PTR__ZNK5Botan14PKCS10_Request10path_limitEv_00c1cf18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `11 8e 47 f9` | ldr x17,[x16, #0xf18] | `FALL_THROUGH`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `10 62 3c 91` | add x16,x16,#0xf18 | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdc0`](#insn-00bdcdc0) 範囲 `[['00bdcdc0', '00bdcdc7']]`
  - `FALL_THROUGH` [`00bdcdc4`](#insn-00bdcdc4) → [`00bdcdc8`](#insn-00bdcdc8)
- ブロック [`00bdcdc8`](#insn-00bdcdc8) 範囲 `[['00bdcdc8', '00bdcdcf']]`

## 命令位置別の参照

- [`00bdcdc4`](#insn-00bdcdc4) → `00c1cf18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdcc`](#insn-00bdcdcc) → [`004ec8c8`](../004ec/004ec8c8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ec8c8` · 推定シンボル `_ZNK5Botan14PKCS10_Request10path_limitEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdc4`](#insn-00bdcdc4)

~~~json
{
  "source": "00bdcdc4",
  "target": "00c1cf18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdcc`](#insn-00bdcdcc)

~~~json
{
  "source": "00bdcdcc",
  "target": "004ec8c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
