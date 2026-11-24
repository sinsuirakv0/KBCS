# 00bbadb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-5844462e2d64d9547f7db1d84372cc68)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c377fc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377fc.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-a92bad3ad79e2f8f650bff85619ea51c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbadb4",
  "name": "_ZNSt9bad_allocC2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125",
  "source_text_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbadb4",
        "00bbadcb"
      ]
    ],
    "bytes_sha256": "a6240219e2ae5bb814c08292b3e12f31c57a4e849b032944048aedc268fb8a28",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdbbf0](../00bdb/00bdbbf0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 551 bytes

~~~c

void _ZNSt9bad_allocC2Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb46f8 with catch @ 00bbadb8 */
                    /* catch() { ... } // from try @ 00bb76a0 with catch @ 00bbadbc */
                    /* catch() { ... } // from try @ 00bb76b8 with catch @ 00bbadc0 */
                    /* catch() { ... } // from try @ 00bb72f0 with catch @ 00bbadc4 */
  *param_1 = (long)(PTR__ZTVSt9bad_alloc_00c1c018 + 0x10);
                    /* catch() { ... } // from try @ 00bb7308 with catch @ 00bbadc8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbadb4"></a> `00bbadb4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbadb8"></a> `00bbadb8` | `08 03 00 d0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbadbc"></a> `00bbadbc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bbadc0"></a> `00bbadc0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbadc4"></a> `00bbadc4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbadc8"></a> `00bbadc8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbadb4`](#insn-00bbadb4) 範囲 `[['00bbadb4', '00bbadb7']]`
  - `FALL_THROUGH` [`00bbadb4`](#insn-00bbadb4) → [`00bbadb8`](#insn-00bbadb8)
- ブロック [`00bbadb8`](#insn-00bbadb8) 範囲 `[['00bbadb8', '00bbadbb']]`
  - `FALL_THROUGH` [`00bbadb8`](#insn-00bbadb8) → [`00bbadbc`](#insn-00bbadbc)
- ブロック [`00bbadbc`](#insn-00bbadbc) 範囲 `[['00bbadbc', '00bbadbf']]`
  - `FALL_THROUGH` [`00bbadbc`](#insn-00bbadbc) → [`00bbadc0`](#insn-00bbadc0)
- ブロック [`00bbadc0`](#insn-00bbadc0) 範囲 `[['00bbadc0', '00bbadc3']]`
  - `FALL_THROUGH` [`00bbadc0`](#insn-00bbadc0) → [`00bbadc4`](#insn-00bbadc4)
- ブロック [`00bbadc4`](#insn-00bbadc4) 範囲 `[['00bbadc4', '00bbadc7']]`
  - `FALL_THROUGH` [`00bbadc4`](#insn-00bbadc4) → [`00bbadc8`](#insn-00bbadc8)
- ブロック [`00bbadc8`](#insn-00bbadc8) 範囲 `[['00bbadc8', '00bbadcb']]`

## 命令位置別の参照

- [`00bbadbc`](#insn-00bbadbc) → `00c1c018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbadc4`](#insn-00bbadc4) → `00c16838`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbadbc`](#insn-00bbadbc)

~~~json
{
  "source": "00bbadbc",
  "target": "00c1c018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbadc4`](#insn-00bbadc4)

~~~json
{
  "source": "00bbadc4",
  "target": "00c16838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16828",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
