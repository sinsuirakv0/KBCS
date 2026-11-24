# 00aaeff4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aae000`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aae/00aae000.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-097ab747b6fbb8c5701450e956b5d76c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaeff4",
  "name": "FUN_00aaeff4",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5006a51ebfd2805244f4e36d691a9d98056887c0850c67f57b67b95da4cc5d2",
  "source_text_sha256": "e5006a51ebfd2805244f4e36d691a9d98056887c0850c67f57b67b95da4cc5d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaeff4",
        "00aaf007"
      ]
    ],
    "bytes_sha256": "3b98a4e1053f6287fd4659c7475747b15f2ab57a085a5efa9a1a90964effcc7f",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006107ac](../00610/006107ac.md)
- [00624b98](../00624/00624b98.md)

## 呼び出し先

- [00aada58](../00aad/00aada58.md)

## 関連文字列（未確認候補）

~~~text
"BcLogDefeated"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00aaeff4(int param_1)

{
  if (param_1 != 0) {
    return;
  }
  FUN_00aada58("BcLogDefeated");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaeff4"></a> `00aaeff4` | `40 00 00 34` | cbz w0,0x00aaeffc | `CONDITIONAL_JUMP`
<a id="insn-00aaeff8"></a> `00aaeff8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaeffc"></a> `00aaeffc` | `80 c0 ff b0` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-00aaf000"></a> `00aaf000` | `00 04 1d 91` | add x0,x0,#0x741 | `FALL_THROUGH`
<a id="insn-00aaf004"></a> `00aaf004` | `95 fa ff 17` | b 0x00aada58 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaeff4`](#insn-00aaeff4) 範囲 `[['00aaeff4', '00aaeff7']]`
  - `CONDITIONAL_JUMP` [`00aaeff4`](#insn-00aaeff4) → [`00aaeffc`](#insn-00aaeffc)
  - `FALL_THROUGH` [`00aaeff4`](#insn-00aaeff4) → [`00aaeff8`](#insn-00aaeff8)
- ブロック [`00aaeff8`](#insn-00aaeff8) 範囲 `[['00aaeff8', '00aaeffb']]`
- ブロック [`00aaeffc`](#insn-00aaeffc) 範囲 `[['00aaeffc', '00aaf007']]`

## 命令位置別の参照

- [`00aaeff4`](#insn-00aaeff4) → [`00aaeffc`](#insn-00aaeffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf000`](#insn-00aaf000) → `002bf741`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaf004`](#insn-00aaf004) → [`00aada58`](../00aad/00aada58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aada58` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaeff4`](#insn-00aaeff4)

~~~json
{
  "source": "00aaeff4",
  "target": "00aaeffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf000`](#insn-00aaf000)

~~~json
{
  "source": "00aaf000",
  "target": "002bf741",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf741",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "42634c6f67446566656174656400",
  "capture_start": "002bf741",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaf004`](#insn-00aaf004)

~~~json
{
  "source": "00aaf004",
  "target": "00aada58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
