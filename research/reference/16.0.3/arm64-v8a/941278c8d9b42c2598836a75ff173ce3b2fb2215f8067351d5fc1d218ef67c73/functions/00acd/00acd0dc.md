# 00acd0dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acc0e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acc/00acc0e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-a47de199b872e102f1bc0c2637f72cf1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd0dc",
  "name": "FUN_00acd0dc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ebf3ccc3a82992e29a2035d07d06ac1e657259aca842cdc0cc6fa2ff95c9920c",
  "source_text_sha256": "ebf3ccc3a82992e29a2035d07d06ac1e657259aca842cdc0cc6fa2ff95c9920c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd0dc",
        "00acd113"
      ]
    ],
    "bytes_sha256": "6488905500e6d5f0d9ea66a09aff9b89ebd51319b33d579609359170301f6a67",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00accdb0](../00acc/00accdb0.md)

## 呼び出し先

- [00accaec](../00acc/00accaec.md)
- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 195 bytes

~~~c

void FUN_00acd0dc(long param_1)

{
  void *__ptr;
  
  __ptr = *(void **)(param_1 + 0x18);
  if (__ptr != (void *)0x0) {
    FUN_00accaec(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd0dc"></a> `00acd0dc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acd0e0"></a> `00acd0e0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd0e4"></a> `00acd0e4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acd0e8"></a> `00acd0e8` | `13 0c 40 f9` | ldr x19,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00acd0ec"></a> `00acd0ec` | `f3 00 00 b4` | cbz x19,0x00acd108 | `CONDITIONAL_JUMP`
<a id="insn-00acd0f0"></a> `00acd0f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd0f4"></a> `00acd0f4` | `7e fe ff 97` | bl 0x00accaec | `UNCONDITIONAL_CALL`
<a id="insn-00acd0f8"></a> `00acd0f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acd0fc"></a> `00acd0fc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd100"></a> `00acd100` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acd104"></a> `00acd104` | `93 2f 06 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00acd108"></a> `00acd108` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acd10c"></a> `00acd10c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acd110"></a> `00acd110` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acd0dc`](#insn-00acd0dc) 範囲 `[['00acd0dc', '00acd0ef']]`
  - `CONDITIONAL_JUMP` [`00acd0ec`](#insn-00acd0ec) → [`00acd108`](#insn-00acd108)
  - `FALL_THROUGH` [`00acd0ec`](#insn-00acd0ec) → [`00acd0f0`](#insn-00acd0f0)
- ブロック [`00acd0f0`](#insn-00acd0f0) 範囲 `[['00acd0f0', '00acd107']]`
- ブロック [`00acd108`](#insn-00acd108) 範囲 `[['00acd108', '00acd113']]`

## 命令位置別の参照

- [`00acd0dc`](#insn-00acd0dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd0e0`](#insn-00acd0e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd0ec`](#insn-00acd0ec) → [`00acd108`](#insn-00acd108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd0f4`](#insn-00acd0f4) → [`00accaec`](../00acc/00accaec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00accaec` · 推定シンボル `None` · 推定型 `None`
- [`00acd0fc`](#insn-00acd0fc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd100`](#insn-00acd100) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd104`](#insn-00acd104) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acd108`](#insn-00acd108) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd10c`](#insn-00acd10c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd0dc`](#insn-00acd0dc)

~~~json
{
  "source": "00acd0dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd0e0`](#insn-00acd0e0)

~~~json
{
  "source": "00acd0e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd0ec`](#insn-00acd0ec)

~~~json
{
  "source": "00acd0ec",
  "target": "00acd108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd0f4`](#insn-00acd0f4)

~~~json
{
  "source": "00acd0f4",
  "target": "00accaec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd0fc`](#insn-00acd0fc)

~~~json
{
  "source": "00acd0fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd100`](#insn-00acd100)

~~~json
{
  "source": "00acd100",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd104`](#insn-00acd104)

~~~json
{
  "source": "00acd104",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acd108`](#insn-00acd108)

~~~json
{
  "source": "00acd108",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd10c`](#insn-00acd10c)

~~~json
{
  "source": "00acd10c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
