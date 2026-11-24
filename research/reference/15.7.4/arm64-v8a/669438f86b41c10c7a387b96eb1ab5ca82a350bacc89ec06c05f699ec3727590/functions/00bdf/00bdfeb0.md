# 00bdfeb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfe60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-325b9bcacb2550ef181ef13bdd1ea156)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c9f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9f0.md) · 移動量 `+0x7cb40`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0021.md#compare-2eebb3c62dd7ba953db8b5bfa81f1656)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfeb0",
  "name": "_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d6c223a21be3eafc025c163210e2ccef11a1d99d4615dd02b64811feda3320b",
  "source_text_sha256": "0d6c223a21be3eafc025c163210e2ccef11a1d99d4615dd02b64811feda3320b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfeb0",
        "00bdfebf"
      ]
    ],
    "bytes_sha256": "b73b902560071b14ab307ae8e8bb6715023f59711525d0b343ef029582c38a0d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b218b0](../00b21/00b218b0.md)
- [00b430c0](../00b43/00b430c0.md)

## 呼び出し先

- [00b430c0](../00b43/00b430c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 296 bytes

~~~c

void _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_(void)

{
                    /* try { // try from 00bdfebc to 00ce006f has its CatchHandler @ 00bdfce0 */
  (*(code *)PTR__ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T__00c1e810)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfeb0"></a> `00bdfeb0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfeb4"></a> `00bdfeb4` | `11 0a 44 f9` | ldr x17,[x16, #0x810] | `FALL_THROUGH`
<a id="insn-00bdfeb8"></a> `00bdfeb8` | `10 42 20 91` | add x16,x16,#0x810 | `FALL_THROUGH`
<a id="insn-00bdfebc"></a> `00bdfebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfeb0`](#insn-00bdfeb0) 範囲 `[['00bdfeb0', '00bdfebb']]`
  - `FALL_THROUGH` [`00bdfeb8`](#insn-00bdfeb8) → [`00bdfebc`](#insn-00bdfebc)
- ブロック [`00bdfebc`](#insn-00bdfebc) 範囲 `[['00bdfebc', '00bdfebf']]`

## 命令位置別の参照

- [`00bdfeb4`](#insn-00bdfeb4) → `00c1e810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfebc`](#insn-00bdfebc) → [`00b430c0`](../00b43/00b430c0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b430c0` · 推定シンボル `_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfeb4`](#insn-00bdfeb4)

~~~json
{
  "source": "00bdfeb4",
  "target": "00c1e810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfebc`](#insn-00bdfebc)

~~~json
{
  "source": "00bdfebc",
  "target": "00b430c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
