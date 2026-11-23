# 00bdecf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdec40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-0da6c084ef3f75d7e8bcf409729213ca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bded40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-5da65d3064b51bed06c5a9fd7ef4b30b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecf0",
  "name": "_ZNK8firebase4Path14GetDirectoriesEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42a00e8331379a72f3631bc2a1cfdb36b06128546f55110793e5ac852559028c",
  "source_text_sha256": "42a00e8331379a72f3631bc2a1cfdb36b06128546f55110793e5ac852559028c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdecf0",
        "00bdecff"
      ]
    ],
    "bytes_sha256": "b6eb041b09c80b232c0f36691f554a37065153996d06b73e74658f5319713934",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afdb2c](../00afd/00afdb2c.md)
- [00afdc04](../00afd/00afdc04.md)
- [00afddb4](../00afd/00afddb4.md)

## 呼び出し先

- [00afd844](../00afd/00afd844.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZNK8firebase4Path14GetDirectoriesEv(void)

{
  (*(code *)PTR__ZNK8firebase4Path14GetDirectoriesEv_00c1df08)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdecf0"></a> `00bdecf0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdecf4"></a> `00bdecf4` | `11 86 47 f9` | ldr x17,[x16, #0xf08] | `FALL_THROUGH`
<a id="insn-00bdecf8"></a> `00bdecf8` | `10 22 3c 91` | add x16,x16,#0xf08 | `FALL_THROUGH`
<a id="insn-00bdecfc"></a> `00bdecfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdecf0`](#insn-00bdecf0) 範囲 `[['00bdecf0', '00bdecff']]`

## 命令位置別の参照

- [`00bdecf4`](#insn-00bdecf4) → `00c1df08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdecfc`](#insn-00bdecfc) → [`00afd844`](../00afd/00afd844.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afd844` · 推定シンボル `_ZNK8firebase4Path14GetDirectoriesEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdecf4`](#insn-00bdecf4)

~~~json
{
  "source": "00bdecf4",
  "target": "00c1df08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdecfc`](#insn-00bdecfc)

~~~json
{
  "source": "00bdecfc",
  "target": "00afd844",
  "target_space": "ram",
  "resolution": "function"
}
~~~
