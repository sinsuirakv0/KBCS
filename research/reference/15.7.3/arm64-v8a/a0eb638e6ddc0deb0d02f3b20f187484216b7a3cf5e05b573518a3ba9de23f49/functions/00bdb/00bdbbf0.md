# 00bdbbf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbb40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-fed5bc607f3ca776aa4438134646e511)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbc40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-83089d768e096e70f49da31ad877254b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbf0",
  "name": "_ZN5Botan6BigInt13binary_decodeEPKhm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b69550cae17c19103d246af2f7b2a54dc2337ed1f545d97fd35419ddf83de266",
  "source_text_sha256": "b69550cae17c19103d246af2f7b2a54dc2337ed1f545d97fd35419ddf83de266",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbf0",
        "00bdbbff"
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

- [0048ddf0](../0048d/0048ddf0.md)
- [0048df5c](../0048d/0048df5c.md)
- [00497a4c](../00497/00497a4c.md)
- [004b5004](../004b5/004b5004.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004e0734](../004e0/004e0734.md)
- [004e66d0](../004e6/004e66d0.md)
- [004e939c](../004e9/004e939c.md)

## 呼び出し先

- [00494840](../00494/00494840.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZN5Botan6BigInt13binary_decodeEPKhm(void)

{
  (*(code *)PTR__ZN5Botan6BigInt13binary_decodeEPKhm_00c1c688)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbf0"></a> `00bdbbf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbf4"></a> `00bdbbf4` | `11 46 43 f9` | ldr x17,[x16, #0x688] | `FALL_THROUGH`
<a id="insn-00bdbbf8"></a> `00bdbbf8` | `10 22 1a 91` | add x16,x16,#0x688 | `FALL_THROUGH`
<a id="insn-00bdbbfc"></a> `00bdbbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbf0`](#insn-00bdbbf0) 範囲 `[['00bdbbf0', '00bdbbff']]`

## 命令位置別の参照

- [`00bdbbf4`](#insn-00bdbbf4) → `00c1c688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbfc`](#insn-00bdbbfc) → [`00494840`](../00494/00494840.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00494840` · 推定シンボル `_ZN5Botan6BigInt13binary_decodeEPKhm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbf4`](#insn-00bdbbf4)

~~~json
{
  "source": "00bdbbf4",
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
- 参照命令 [`00bdbbfc`](#insn-00bdbbfc)

~~~json
{
  "source": "00bdbbfc",
  "target": "00494840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
