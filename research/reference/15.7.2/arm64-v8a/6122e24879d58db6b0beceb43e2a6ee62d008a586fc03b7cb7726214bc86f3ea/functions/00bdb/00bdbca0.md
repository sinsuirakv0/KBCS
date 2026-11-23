# 00bdbca0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-df49fc57881c47958e54266dbc65b6f6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbca0",
  "name": "_ZN5Botan13base64_decodeEPhPKcmb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d03e4b68de75e9d2c3c3b31df4f53c7549f73b654a0a2720ac9f3aa65dc6b0c",
  "source_text_sha256": "3d03e4b68de75e9d2c3c3b31df4f53c7549f73b654a0a2720ac9f3aa65dc6b0c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbca0",
        "00bdbcaf"
      ]
    ],
    "bytes_sha256": "c551fd8061e7b6a53739f2b69b985af191d9026a6f82e7cd42988cbcbc842e74",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493268](../00493/00493268.md)
- [00493288](../00493/00493288.md)
- [00493354](../00493/00493354.md)
- [004c2f88](../004c2/004c2f88.md)

## 呼び出し先

- [00493150](../00493/00493150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN5Botan13base64_decodeEPhPKcmb(void)

{
  (*(code *)PTR__ZN5Botan13base64_decodeEPhPKcmb_00c1c688)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbca0"></a> `00bdbca0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbca4"></a> `00bdbca4` | `11 46 43 f9` | ldr x17,[x16, #0x688] | `FALL_THROUGH`
<a id="insn-00bdbca8"></a> `00bdbca8` | `10 22 1a 91` | add x16,x16,#0x688 | `FALL_THROUGH`
<a id="insn-00bdbcac"></a> `00bdbcac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbca0`](#insn-00bdbca0) 範囲 `[['00bdbca0', '00bdbcaf']]`

## 命令位置別の参照

- [`00bdbca4`](#insn-00bdbca4) → `00c1c688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcac`](#insn-00bdbcac) → [`00493150`](../00493/00493150.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00493150` · 推定シンボル `_ZN5Botan13base64_decodeEPhPKcmb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbca4`](#insn-00bdbca4)

~~~json
{
  "source": "00bdbca4",
  "target": "00c1c688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c688",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcac`](#insn-00bdbcac)

~~~json
{
  "source": "00bdbcac",
  "target": "00493150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
