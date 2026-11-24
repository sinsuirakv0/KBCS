# 00bac3ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bac3a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bac3a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0022.md#compare-93ece466c1663c3f65c3bc1d67553a35)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c28e34`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28e34.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0005.md#compare-fb58e1ccdb481ce26ce40398da36a368)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac3ec",
  "name": "_ZNKSt6__ndk17codecvtIDsc9mbstate_tE9do_lengthERS1_PKcS5_m",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e9cefb6108be6b976f952cf200a0af6a3593c583658463d146b8d563238a250",
  "source_text_sha256": "5e9cefb6108be6b976f952cf200a0af6a3593c583658463d146b8d563238a250",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac3ec",
        "00bac407"
      ]
    ],
    "bytes_sha256": "831e7dd9e95cc27fa9396fbdd240f607a2531ff4820506061bec0eafd9d342d0",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bac408](../00bac/00bac408.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDsc9mbstate_tE9do_lengthERS1_PKcS5_m
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bac408(param_3,param_4,param_5,0x10ffff,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac3ec"></a> `00bac3ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bac3f0"></a> `00bac3f0` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bac3f4"></a> `00bac3f4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bac3f8"></a> `00bac3f8` | `e2 03 04 aa` | mov x2,x4 | `FALL_THROUGH`
<a id="insn-00bac3fc"></a> `00bac3fc` | `e3 fd bf 12` | mov w3,#0x10ffff | `FALL_THROUGH`
<a id="insn-00bac400"></a> `00bac400` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bac404"></a> `00bac404` | `01 00 00 14` | b 0x00bac408 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bac3ec`](#insn-00bac3ec) 範囲 `[['00bac3ec', '00bac407']]`

## 命令位置別の参照

- [`00bac3fc`](#insn-00bac3fc) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00bac404`](#insn-00bac404) → [`00bac408`](00bac408.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac408` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac3fc`](#insn-00bac3fc)

~~~json
{
  "source": "00bac3fc",
  "target": "0010ffff",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "001002f8",
  "offset": 64775,
  "size": 161136,
  "datatype": "Elf64_Sym[6714]",
  "bytes": "0000000000000000000000000000000000000000000000000100000012000000",
  "capture_start": "001002f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bac404`](#insn-00bac404)

~~~json
{
  "source": "00bac404",
  "target": "00bac408",
  "target_space": "ram",
  "resolution": "function"
}
~~~
