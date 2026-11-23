# 008fceac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `008fceac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fceac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0047.md#compare-a8098120e1ce2960eb2badc886d17ca0)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `008fceac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fceac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0048.md#compare-0daaab16f2554aa3b0ade5759c298bff)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fceac",
  "name": "FUN_008fceac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4ad0d84915b21a75d4c52d5c966802c222ffd636db28c8cca4de5ab82c81655",
  "source_text_sha256": "b4ad0d84915b21a75d4c52d5c966802c222ffd636db28c8cca4de5ab82c81655",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008fceac",
        "008fcebb"
      ]
    ],
    "bytes_sha256": "6abc0c71421dde6251998fdac3f024b0c3ab370f600574387c478540299afc7e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_008fceac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c08a10;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008fceac"></a> `008fceac` | `68 18 00 90` | adrp x8,0xc08000 | `FALL_THROUGH`
<a id="insn-008fceb0"></a> `008fceb0` | `08 41 28 91` | add x8,x8,#0xa10 | `FALL_THROUGH`
<a id="insn-008fceb4"></a> `008fceb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008fceb8"></a> `008fceb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008fceac`](#insn-008fceac) 範囲 `[['008fceac', '008fcebb']]`

## 命令位置別の参照

- [`008fceb4`](#insn-008fceb4) → `00c08a10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008fceb4`](#insn-008fceb4)

~~~json
{
  "source": "008fceb4",
  "target": "00c08a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c08a10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
