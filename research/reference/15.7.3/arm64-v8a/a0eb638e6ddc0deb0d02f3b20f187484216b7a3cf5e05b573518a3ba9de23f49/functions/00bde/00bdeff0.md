# 00bdeff0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdef40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-d34976106564a64dc2bd49f2ed90d0aa)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdf040`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf040.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-f5b69f7c638655b565ea96218cb4c333)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeff0",
  "name": "_ZNK8firebase3App14GetPlatformAppEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f9ad60a8330c09dc79d754a58e63cd017fc1242ccddfcaac0fe7474a3296ae7",
  "source_text_sha256": "6f9ad60a8330c09dc79d754a58e63cd017fc1242ccddfcaac0fe7474a3296ae7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeff0",
        "00bdefff"
      ]
    ],
    "bytes_sha256": "7f1c56509f5c65657645c4d62d0cb65ffb7be3bdd18050f78bf4ef4704061b13",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b54af4](../00b54/00b54af4.md)
- [00b5dce8](../00b5d/00b5dce8.md)
- [00b5e148](../00b5e/00b5e148.md)

## 呼び出し先

- [00b08174](../00b08/00b08174.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZNK8firebase3App14GetPlatformAppEv(void)

{
  (*(code *)PTR__ZNK8firebase3App14GetPlatformAppEv_00c1e088)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeff0"></a> `00bdeff0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdeff4"></a> `00bdeff4` | `11 46 40 f9` | ldr x17,[x16, #0x88] | `FALL_THROUGH`
<a id="insn-00bdeff8"></a> `00bdeff8` | `10 22 02 91` | add x16,x16,#0x88 | `FALL_THROUGH`
<a id="insn-00bdeffc"></a> `00bdeffc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeff0`](#insn-00bdeff0) 範囲 `[['00bdeff0', '00bdefff']]`

## 命令位置別の参照

- [`00bdeff4`](#insn-00bdeff4) → `00c1e088`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeffc`](#insn-00bdeffc) → [`00b08174`](../00b08/00b08174.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b08174` · 推定シンボル `_ZNK8firebase3App14GetPlatformAppEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeff4`](#insn-00bdeff4)

~~~json
{
  "source": "00bdeff4",
  "target": "00c1e088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e088",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeffc`](#insn-00bdeffc)

~~~json
{
  "source": "00bdeffc",
  "target": "00b08174",
  "target_space": "ram",
  "resolution": "function"
}
~~~
