# 00bacccc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bacc04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacc04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-b07692bd41d4b44acce04a010ed3d6ad)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bacd10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-651c4f48fa16c6aca06c19b1218f4f1d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacccc",
  "name": "_ZNKSt6__ndk17codecvtIDic9mbstate_tE9do_lengthERS1_PKcS5_m",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8381f350b4a7cad586b8f9fbbf25c841f7eeec8716d6e8ac2dcc7ca00ba221f1",
  "source_text_sha256": "8381f350b4a7cad586b8f9fbbf25c841f7eeec8716d6e8ac2dcc7ca00ba221f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacccc",
        "00bacce7"
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

- [00bacce8](../00bac/00bacce8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDic9mbstate_tE9do_lengthERS1_PKcS5_m
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bacce8(param_3,param_4,param_5,0x10ffff,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacccc"></a> `00bacccc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baccd0"></a> `00baccd0` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baccd4"></a> `00baccd4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00baccd8"></a> `00baccd8` | `e2 03 04 aa` | mov x2,x4 | `FALL_THROUGH`
<a id="insn-00baccdc"></a> `00baccdc` | `e3 fd bf 12` | mov w3,#0x10ffff | `FALL_THROUGH`
<a id="insn-00bacce0"></a> `00bacce0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bacce4"></a> `00bacce4` | `01 00 00 14` | b 0x00bacce8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bacccc`](#insn-00bacccc) 範囲 `[['00bacccc', '00bacce7']]`

## 命令位置別の参照

- [`00baccdc`](#insn-00baccdc) → `0010ffff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6714]`
- [`00bacce4`](#insn-00bacce4) → [`00bacce8`](00bacce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacce8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baccdc`](#insn-00baccdc)

~~~json
{
  "source": "00baccdc",
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
- 参照命令 [`00bacce4`](#insn-00bacce4)

~~~json
{
  "source": "00bacce4",
  "target": "00bacce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
