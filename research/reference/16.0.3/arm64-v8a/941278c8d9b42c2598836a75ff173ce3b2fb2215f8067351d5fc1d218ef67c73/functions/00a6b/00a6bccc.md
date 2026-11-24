# 00a6bccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a6acd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6a/00a6acd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0012.md#compare-85b4405c43c424fe9ac4f69f20d84319)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6bccc",
  "name": "FUN_00a6bccc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "841ef45efd7e22230c16931357d189e9bd87434d65fadd4ced56eeb65589a5a5",
  "source_text_sha256": "841ef45efd7e22230c16931357d189e9bd87434d65fadd4ced56eeb65589a5a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6bccc",
        "00a6bceb"
      ]
    ],
    "bytes_sha256": "afee01c95e89d3fae0944fb5f2feb13d22080f7d414a9e1ccaa1b47a65e92178",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 320 bytes

~~~c

void FUN_00a6bccc(long param_1)

{
  if ((*(int *)(param_1 + 0x84) != 0) && (*(int *)(param_1 + 0x84) <= *(int *)(param_1 + 0x80))) {
                    /* try { // try from 00a6bcdc to 00b6bceb has its CatchHandler @ 00a78e60 */
    return;
  }
  *(int *)(param_1 + 0x80) = *(int *)(param_1 + 0x80) + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6bccc"></a> `00a6bccc` | `08 24 50 29` | ldp w8,w9,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00a6bcd0"></a> `00a6bcd0` | `89 00 00 34` | cbz w9,0x00a6bce0 | `CONDITIONAL_JUMP`
<a id="insn-00a6bcd4"></a> `00a6bcd4` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00a6bcd8"></a> `00a6bcd8` | `4c 00 00 54` | b.gt 0x00a6bce0 | `CONDITIONAL_JUMP`
<a id="insn-00a6bcdc"></a> `00a6bcdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6bce0"></a> `00a6bce0` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a6bce4"></a> `00a6bce4` | `08 80 00 b9` | str w8,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00a6bce8"></a> `00a6bce8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6bccc`](#insn-00a6bccc) 範囲 `[['00a6bccc', '00a6bcd3']]`
  - `CONDITIONAL_JUMP` [`00a6bcd0`](#insn-00a6bcd0) → [`00a6bce0`](#insn-00a6bce0)
  - `FALL_THROUGH` [`00a6bcd0`](#insn-00a6bcd0) → [`00a6bcd4`](#insn-00a6bcd4)
- ブロック [`00a6bcd4`](#insn-00a6bcd4) 範囲 `[['00a6bcd4', '00a6bcdb']]`
  - `CONDITIONAL_JUMP` [`00a6bcd8`](#insn-00a6bcd8) → [`00a6bce0`](#insn-00a6bce0)
  - `FALL_THROUGH` [`00a6bcd8`](#insn-00a6bcd8) → [`00a6bcdc`](#insn-00a6bcdc)
- ブロック [`00a6bcdc`](#insn-00a6bcdc) 範囲 `[['00a6bcdc', '00a6bcdf']]`
- ブロック [`00a6bce0`](#insn-00a6bce0) 範囲 `[['00a6bce0', '00a6bceb']]`

## 命令位置別の参照

- [`00a6bcd0`](#insn-00a6bcd0) → [`00a6bce0`](#insn-00a6bce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6bcd8`](#insn-00a6bcd8) → [`00a6bce0`](#insn-00a6bce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6bcd0`](#insn-00a6bcd0)

~~~json
{
  "source": "00a6bcd0",
  "target": "00a6bce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6bcd8`](#insn-00a6bcd8)

~~~json
{
  "source": "00a6bcd8",
  "target": "00a6bce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
