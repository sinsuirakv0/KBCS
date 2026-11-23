# 00bdbab0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdba00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdba00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-11dfcecdd17280109b2881abac4ab5ac)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbb00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-2acd0cfde1cd4d69f03c3e23998c29d4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbab0",
  "name": "_ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9cdb36ae1a506feade8443a85f5bb94bd6fc935d482b7605bbe5a2e2e49a2257",
  "source_text_sha256": "9cdb36ae1a506feade8443a85f5bb94bd6fc935d482b7605bbe5a2e2e49a2257",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbab0",
        "00bdbabf"
      ]
    ],
    "bytes_sha256": "c9b4f288b632832eada607e75872c1279de3a9e7052c0687c844aed0d1ae39b1",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00489150](../00489/00489150.md)
- [0048ff2c](../0048f/0048ff2c.md)
- [00494544](../00494/00494544.md)
- [00494634](../00494/00494634.md)
- [005141ac](../00514/005141ac.md)
- [00514680](../00514/00514680.md)

## 呼び出し先

- [00490728](../00490/00490728.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 141 bytes

~~~c

void _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE(void)

{
  (*(code *)PTR__ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE_00c1c5e8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbab0"></a> `00bdbab0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbab4"></a> `00bdbab4` | `11 f6 42 f9` | ldr x17,[x16, #0x5e8] | `FALL_THROUGH`
<a id="insn-00bdbab8"></a> `00bdbab8` | `10 a2 17 91` | add x16,x16,#0x5e8 | `FALL_THROUGH`
<a id="insn-00bdbabc"></a> `00bdbabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbab0`](#insn-00bdbab0) 範囲 `[['00bdbab0', '00bdbabf']]`

## 命令位置別の参照

- [`00bdbab4`](#insn-00bdbab4) → `00c1c5e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbabc`](#insn-00bdbabc) → [`00490728`](../00490/00490728.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00490728` · 推定シンボル `_ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbab4`](#insn-00bdbab4)

~~~json
{
  "source": "00bdbab4",
  "target": "00c1c5e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c5e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbabc`](#insn-00bdbabc)

~~~json
{
  "source": "00bdbabc",
  "target": "00490728",
  "target_space": "ram",
  "resolution": "function"
}
~~~
