# 00bdcdd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-3fdb8b79eeb3889dd42ec981d63303cc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdd0",
  "name": "_ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bddc313f3b85fe9031e2ba61d5cb7b87000f19f8b88a496decde93834b8165b",
  "source_text_sha256": "0bddc313f3b85fe9031e2ba61d5cb7b87000f19f8b88a496decde93834b8165b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdd0",
        "00bdcddf"
      ]
    ],
    "bytes_sha256": "1d715bc2a23d32cbc559b8f6187843cf38ad1c2234bc3559e6a6bca02f5d5556",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ec8c8](../004ec/004ec8c8.md)
- [004fdfd8](../004fd/004fdfd8.md)

## 呼び出し先

- [004eca70](../004ec/004eca70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 185 bytes

~~~c

void _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv(void)

{
  (*(code *)PTR__ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv_00c1cf20)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdd0"></a> `00bdcdd0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdd4"></a> `00bdcdd4` | `11 92 47 f9` | ldr x17,[x16, #0xf20] | `FALL_THROUGH`
<a id="insn-00bdcdd8"></a> `00bdcdd8` | `10 82 3c 91` | add x16,x16,#0xf20 | `FALL_THROUGH`
<a id="insn-00bdcddc"></a> `00bdcddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdd0`](#insn-00bdcdd0) 範囲 `[['00bdcdd0', '00bdcddf']]`

## 命令位置別の参照

- [`00bdcdd4`](#insn-00bdcdd4) → `00c1cf20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcddc`](#insn-00bdcddc) → [`004eca70`](../004ec/004eca70.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004eca70` · 推定シンボル `_ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdd4`](#insn-00bdcdd4)

~~~json
{
  "source": "00bdcdd4",
  "target": "00c1cf20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf20",
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
  "target": "004eca70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
