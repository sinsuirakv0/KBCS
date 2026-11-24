# 00bdbbc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-5be63bfb7e5f6857beb92f09bd1be642)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58610`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58610.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-1c0d049c87e3d020fefed7e605f560a1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbc0",
  "name": "_ZNSt6__ndk16chrono12system_clock11from_time_tEl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45347ad60b7df517c6833809024c8a47369342f3967b13c931b9ff7101d56330",
  "source_text_sha256": "45347ad60b7df517c6833809024c8a47369342f3967b13c931b9ff7101d56330",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbc0",
        "00bdbbcf"
      ]
    ],
    "bytes_sha256": "634f93533397387bd5e513f2651721bd95243d258ed44f78d924a677b380459b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048c2e0](../0048c/0048c2e0.md)

## 呼び出し先

- [00b729c4](../00b72/00b729c4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZNSt6__ndk16chrono12system_clock11from_time_tEl(void)

{
  (*(code *)PTR__ZNSt6__ndk16chrono12system_clock11from_time_tEl_00c1c698)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbc0"></a> `00bdbbc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbc4"></a> `00bdbbc4` | `11 4e 43 f9` | ldr x17,[x16, #0x698] | `FALL_THROUGH`
<a id="insn-00bdbbc8"></a> `00bdbbc8` | `10 62 1a 91` | add x16,x16,#0x698 | `FALL_THROUGH`
<a id="insn-00bdbbcc"></a> `00bdbbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbc0`](#insn-00bdbbc0) 範囲 `[['00bdbbc0', '00bdbbcf']]`

## 命令位置別の参照

- [`00bdbbc4`](#insn-00bdbbc4) → `00c1c698`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbcc`](#insn-00bdbbcc) → [`00b729c4`](../00b72/00b729c4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b729c4` · 推定シンボル `_ZNSt6__ndk16chrono12system_clock11from_time_tEl` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbc4`](#insn-00bdbbc4)

~~~json
{
  "source": "00bdbbc4",
  "target": "00c1c698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c698",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbcc`](#insn-00bdbbcc)

~~~json
{
  "source": "00bdbbcc",
  "target": "00b729c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
