# 00bfcbac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbbb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbbb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-95f4f70f26357a00ea285cb255b70770)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcbac",
  "name": "FUN_00bfcbac",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7861c10f1f2ca0af195a6fed5ee550c5cc17f19b69f258ff258885bd31f88ec4",
  "source_text_sha256": "7861c10f1f2ca0af195a6fed5ee550c5cc17f19b69f258ff258885bd31f88ec4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcbac",
        "00bfcbd7"
      ]
    ],
    "bytes_sha256": "a1a3bdfe3364c8393d9a297349c162c59350303eaebd906ed582ac21d99388de",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c5ef90](../00c5e/00c5ef90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_00bfcbac(void *param_1)

{
  _ZNSt6__ndk114error_categoryD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcbac"></a> `00bfcbac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcbb0"></a> `00bfcbb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfcbb4"></a> `00bfcbb4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcbb8"></a> `00bfcbb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfcbbc"></a> `00bfcbbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfcbc0"></a> `00bfcbc0` | `f4 88 01 94` | bl 0x00c5ef90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcbc4"></a> `00bfcbc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcbc8"></a> `00bfcbc8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcbcc"></a> `00bfcbcc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfcbd0"></a> `00bfcbd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcbd4"></a> `00bfcbd4` | `df 70 01 14` | b 0x00c58f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcbac`](#insn-00bfcbac) 範囲 `[['00bfcbac', '00bfcbd7']]`

## 命令位置別の参照

- [`00bfcbb0`](#insn-00bfcbb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbb4`](#insn-00bfcbb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbc0`](#insn-00bfcbc0) → [`00c5ef90`](../00c5e/00c5ef90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ef90` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbc8`](#insn-00bfcbc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbcc`](#insn-00bfcbcc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcbd4`](#insn-00bfcbd4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcbb0`](#insn-00bfcbb0)

~~~json
{
  "source": "00bfcbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcbb4`](#insn-00bfcbb4)

~~~json
{
  "source": "00bfcbb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcbc0`](#insn-00bfcbc0)

~~~json
{
  "source": "00bfcbc0",
  "target": "00c5ef90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcbc8`](#insn-00bfcbc8)

~~~json
{
  "source": "00bfcbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcbcc`](#insn-00bfcbcc)

~~~json
{
  "source": "00bfcbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcbd4`](#insn-00bfcbd4)

~~~json
{
  "source": "00bfcbd4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
