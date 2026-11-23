# 00bdbcd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-9f08f6c785fa80fe9f773399663ebf83)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcd0",
  "name": "_ZN5Botan6BigIntC2ENS0_4SignEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35a388d75b65cfee7152c91f0f678c05858a96b8a1eb5b4bb8408e8e23e08b76",
  "source_text_sha256": "35a388d75b65cfee7152c91f0f678c05858a96b8a1eb5b4bb8408e8e23e08b76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcd0",
        "00bdbcdf"
      ]
    ],
    "bytes_sha256": "b7d29897f34676b88d06db3625692a3a9574f1bebdcc0511ee85421fad392010",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [00496ee0](../00496/00496ee0.md)
- [00497068](../00497/00497068.md)
- [0049731c](../00497/0049731c.md)
- [00497724](../00497/00497724.md)
- [00497874](../00497/00497874.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8210](../004b8/004b8210.md)
- [004b868c](../004b8/004b868c.md)
- [004b87c8](../004b8/004b87c8.md)
- [004bc804](../004bc/004bc804.md)
- [004bd550](../004bd/004bd550.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00497d5c](../00497/00497d5c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN5Botan6BigIntC2ENS0_4SignEm(void)

{
  (*(code *)PTR__ZN5Botan6BigIntC2ENS0_4SignEm_00c1c6a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcd0"></a> `00bdbcd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcd4"></a> `00bdbcd4` | `11 52 43 f9` | ldr x17,[x16, #0x6a0] | `FALL_THROUGH`
<a id="insn-00bdbcd8"></a> `00bdbcd8` | `10 82 1a 91` | add x16,x16,#0x6a0 | `FALL_THROUGH`
<a id="insn-00bdbcdc"></a> `00bdbcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcd0`](#insn-00bdbcd0) 範囲 `[['00bdbcd0', '00bdbcdf']]`

## 命令位置別の参照

- [`00bdbcd4`](#insn-00bdbcd4) → `00c1c6a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcdc`](#insn-00bdbcdc) → [`00497d5c`](../00497/00497d5c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497d5c` · 推定シンボル `_ZN5Botan6BigIntC2ENS0_4SignEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcd4`](#insn-00bdbcd4)

~~~json
{
  "source": "00bdbcd4",
  "target": "00c1c6a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcdc`](#insn-00bdbcdc)

~~~json
{
  "source": "00bdbcdc",
  "target": "00497d5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
