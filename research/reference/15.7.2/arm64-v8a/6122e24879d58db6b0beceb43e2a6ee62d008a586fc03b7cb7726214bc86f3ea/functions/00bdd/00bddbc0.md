# 00bddbc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-4c0e6e5047b4edd40addad052d228d24)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbc0",
  "name": "_ZNK8firebase7Variant8AsStringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21e193f334dcee3e4bffe022b3d0fecf6f0e2c2ae02aa03cf6a01638251af8dd",
  "source_text_sha256": "21e193f334dcee3e4bffe022b3d0fecf6f0e2c2ae02aa03cf6a01638251af8dd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbc0",
        "00bddbcf"
      ]
    ],
    "bytes_sha256": "844716cfde252d6724443ece46beab934db4d22c3fab6177ea0994781675e5dd",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a9ec](../0084a/0084a9ec.md)

## 呼び出し先

- [00b045c4](../00b04/00b045c4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZNK8firebase7Variant8AsStringEv(void)

{
  (*(code *)PTR__ZNK8firebase7Variant8AsStringEv_00c1d618)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbc0"></a> `00bddbc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbc4"></a> `00bddbc4` | `11 0e 43 f9` | ldr x17,[x16, #0x618] | `FALL_THROUGH`
<a id="insn-00bddbc8"></a> `00bddbc8` | `10 62 18 91` | add x16,x16,#0x618 | `FALL_THROUGH`
<a id="insn-00bddbcc"></a> `00bddbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbc0`](#insn-00bddbc0) 範囲 `[['00bddbc0', '00bddbcf']]`

## 命令位置別の参照

- [`00bddbc4`](#insn-00bddbc4) → `00c1d618`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbcc`](#insn-00bddbcc) → [`00b045c4`](../00b04/00b045c4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b045c4` · 推定シンボル `_ZNK8firebase7Variant8AsStringEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbc4`](#insn-00bddbc4)

~~~json
{
  "source": "00bddbc4",
  "target": "00c1d618",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d618",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbcc`](#insn-00bddbcc)

~~~json
{
  "source": "00bddbcc",
  "target": "00b045c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
