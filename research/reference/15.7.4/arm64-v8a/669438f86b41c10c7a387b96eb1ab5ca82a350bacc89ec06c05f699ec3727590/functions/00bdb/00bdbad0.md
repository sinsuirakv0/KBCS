# 00bdbad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdba80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-e95af80ffb666e39b0a6ca453ee9a216)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58520`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-b0b56dcbc1842302c5ef7d9f19924889)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbad0",
  "name": "_ZN5Botan6BigIntC1Em",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2477203757735ae09b834664b90f5ce893d4059cf70894fdba64c0426c48f860",
  "source_text_sha256": "2477203757735ae09b834664b90f5ce893d4059cf70894fdba64c0426c48f860",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbad0",
        "00bdbadf"
      ]
    ],
    "bytes_sha256": "83c29ce50603e6119c87eb31a2b08e55f8e52402c4fd3efcc951e885e0e24792",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00488e94](../00488/00488e94.md)
- [0048df5c](../0048d/0048df5c.md)
- [0048fe68](../0048f/0048fe68.md)
- [0048ff2c](../0048f/0048ff2c.md)
- [00490480](../00490/00490480.md)
- [00490728](../00490/00490728.md)
- [00493850](../00493/00493850.md)
- [00495378](../00495/00495378.md)
- [00497874](../00497/00497874.md)
- [004989ec](../00498/004989ec.md)
- [0049f624](../0049f/0049f624.md)
- [004b5004](../004b5/004b5004.md)
- [004b5c14](../004b5/004b5c14.md)
- [004b6640](../004b6/004b6640.md)
- [004b6d50](../004b6/004b6d50.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8210](../004b8/004b8210.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb928](../004bb/004bb928.md)
- [004bbdd8](../004bb/004bbdd8.md)
- [004bc070](../004bc/004bc070.md)
- [004bc440](../004bc/004bc440.md)
- [004bc804](../004bc/004bc804.md)
- [004bdd7c](../004bd/004bdd7c.md)
- [004be0f4](../004be/004be0f4.md)
- [004bf57c](../004bf/004bf57c.md)
- [004c5f28](../004c5/004c5f28.md)
- [004c73c4](../004c7/004c73c4.md)
- [004cf4d8](../004cf/004cf4d8.md)
- [004cf634](../004cf/004cf634.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [004d0c9c](../004d0/004d0c9c.md)
- [004d1904](../004d1/004d1904.md)
- [004e6aac](../004e6/004e6aac.md)
- [004ee7d8](../004ee/004ee7d8.md)
- [004ef204](../004ef/004ef204.md)
- [004f5078](../004f5/004f5078.md)
- [004fa9b0](../004fa/004fa9b0.md)
- [004faccc](../004fa/004faccc.md)
- [0050b45c](../0050b/0050b45c.md)
- [005141ac](../00514/005141ac.md)

## 呼び出し先

- [00497d04](../00497/00497d04.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 99 bytes

~~~c

void _ZN5Botan6BigIntC1Em(void)

{
  (*(code *)PTR__ZN5Botan6BigIntC1Em_00c1c620)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbad0"></a> `00bdbad0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbad4"></a> `00bdbad4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bdbad8"></a> `00bdbad8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bdbadc"></a> `00bdbadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbad0`](#insn-00bdbad0) 範囲 `[['00bdbad0', '00bdbadf']]`

## 命令位置別の参照

- [`00bdbad4`](#insn-00bdbad4) → `00c1c620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbadc`](#insn-00bdbadc) → [`00497d04`](../00497/00497d04.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497d04` · 推定シンボル `_ZN5Botan6BigIntC1Em` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbad4`](#insn-00bdbad4)

~~~json
{
  "source": "00bdbad4",
  "target": "00c1c620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbadc`](#insn-00bdbadc)

~~~json
{
  "source": "00bdbadc",
  "target": "00497d04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
