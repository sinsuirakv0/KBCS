# 00c2cccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2bcd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bcd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0009.md#compare-0e0a41c745dd8c7179d8e2821b13e6f4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2cccc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83261b419ffbed6ea324e6d5d185f288a5265a4d6bd6e5b70d3d1e7ab1bc317d",
  "source_text_sha256": "83261b419ffbed6ea324e6d5d185f288a5265a4d6bd6e5b70d3d1e7ab1bc317d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2cccc",
        "00c2cceb"
      ]
    ],
    "bytes_sha256": "22814a76afbdb542d86f24aa28db928a37a08ba9a078f2af4af1f3ccef7b86fe",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2a308](../00c2a/00c2a308.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 334 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00c2a308(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2cccc"></a> `00c2cccc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2ccd0"></a> `00c2ccd0` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2ccd4"></a> `00c2ccd4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00c2ccd8"></a> `00c2ccd8` | `03 08 40 f9` | ldr x3,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c2ccdc"></a> `00c2ccdc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00c2cce0"></a> `00c2cce0` | `e2 03 04 aa` | mov x2,x4 | `FALL_THROUGH`
<a id="insn-00c2cce4"></a> `00c2cce4` | `e4 03 08 2a` | mov w4,w8 | `FALL_THROUGH`
<a id="insn-00c2cce8"></a> `00c2cce8` | `88 f5 ff 17` | b 0x00c2a308 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2cccc`](#insn-00c2cccc) 範囲 `[['00c2cccc', '00c2cceb']]`

## 命令位置別の参照

- [`00c2cce8`](#insn-00c2cce8) → [`00c2a308`](../00c2a/00c2a308.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c2a308` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2cce8`](#insn-00c2cce8)

~~~json
{
  "source": "00c2cce8",
  "target": "00c2a308",
  "target_space": "ram",
  "resolution": "function"
}
~~~
