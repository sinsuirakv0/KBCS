# 00bfafc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9fd4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9fd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-a945dce85658a3342ed8c05a56961e44)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfafc8",
  "name": "_ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4134f9d0a3f99d5870489083d96f81b1c3f7aa5592a8bd52e514a5b8ab9f25e8",
  "source_text_sha256": "4134f9d0a3f99d5870489083d96f81b1c3f7aa5592a8bd52e514a5b8ab9f25e8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfafc8",
        "00bfafeb"
      ]
    ],
    "bytes_sha256": "f25beb9c09369e33556c92d1393b45d9aab336beb80e94737d23ea6df6a414ca",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c5f2c0](../00c5f/00c5f2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNSt6__ndk17promiseIvE24set_value_at_thread_exitEv(long *param_1)

{
  if (*param_1 != 0) {
    _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv();
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfafc8"></a> `00bfafc8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfafcc"></a> `00bfafcc` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bfafd0"></a> `00bfafd0` | `40 00 00 b4` | cbz x0,0x00bfafd8 | `CONDITIONAL_JUMP`
<a id="insn-00bfafd4"></a> `00bfafd4` | `bb 90 01 14` | b 0x00c5f2c0 | `CALL_TERMINATOR`
<a id="insn-00bfafd8"></a> `00bfafd8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfafdc"></a> `00bfafdc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfafe0"></a> `00bfafe0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfafe4"></a> `00bfafe4` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bfafe8"></a> `00bfafe8` | `93 7e e1 97` | bl 0x0045aa34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfafc8`](#insn-00bfafc8) 範囲 `[['00bfafc8', '00bfafd3']]`
  - `CONDITIONAL_JUMP` [`00bfafd0`](#insn-00bfafd0) → [`00bfafd8`](#insn-00bfafd8)
  - `FALL_THROUGH` [`00bfafd0`](#insn-00bfafd0) → [`00bfafd4`](#insn-00bfafd4)
- ブロック [`00bfafd4`](#insn-00bfafd4) 範囲 `[['00bfafd4', '00bfafd7']]`
- ブロック [`00bfafd8`](#insn-00bfafd8) 範囲 `[['00bfafd8', '00bfafeb']]`

## 命令位置別の参照

- [`00bfafd0`](#insn-00bfafd0) → [`00bfafd8`](#insn-00bfafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafd4`](#insn-00bfafd4) → [`00c5f2c0`](../00c5f/00c5f2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfafdc`](#insn-00bfafdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafe8`](#insn-00bfafe8) → [`0045aa34`](../0045a/0045aa34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045aa34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfafd0`](#insn-00bfafd0)

~~~json
{
  "source": "00bfafd0",
  "target": "00bfafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafd4`](#insn-00bfafd4)

~~~json
{
  "source": "00bfafd4",
  "target": "00c5f2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfafdc`](#insn-00bfafdc)

~~~json
{
  "source": "00bfafdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafe8`](#insn-00bfafe8)

~~~json
{
  "source": "00bfafe8",
  "target": "0045aa34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
