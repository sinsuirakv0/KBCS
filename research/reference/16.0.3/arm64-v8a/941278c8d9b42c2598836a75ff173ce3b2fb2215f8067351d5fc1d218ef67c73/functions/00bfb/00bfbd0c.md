# 00bfbd0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfad18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfad18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-e68544a74a00aeba07ade381774c5141)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbd0c",
  "name": "FUN_00bfbd0c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c70326a5cc4a5593cb73625d4fa898e8a394dbc7ba639179434414fd8b44d92",
  "source_text_sha256": "5c70326a5cc4a5593cb73625d4fa898e8a394dbc7ba639179434414fd8b44d92",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbd0c",
        "00bfbd43"
      ]
    ],
    "bytes_sha256": "09c14a04dc191473d69c1ce3b1ca42c5279cfe48c21cafea457fcc56b1b45e5d",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c591f0](../00c59/00c591f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 160 bytes

~~~c

void FUN_00bfbd0c(void *param_1)

{
  if (param_1 != (void *)0x0) {
    _ZNSt6__ndk115__thread_structD1Ev();
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbd0c"></a> `00bfbd0c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbd10"></a> `00bfbd10` | `80 01 00 b4` | cbz x0,0x00bfbd40 | `CONDITIONAL_JUMP`
<a id="insn-00bfbd14"></a> `00bfbd14` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbd18"></a> `00bfbd18` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbd1c"></a> `00bfbd1c` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbd20"></a> `00bfbd20` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbd24"></a> `00bfbd24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbd28"></a> `00bfbd28` | `32 75 01 94` | bl 0x00c591f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbd2c"></a> `00bfbd2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbd30"></a> `00bfbd30` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbd34"></a> `00bfbd34` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbd38"></a> `00bfbd38` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbd3c"></a> `00bfbd3c` | `85 74 01 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bfbd40"></a> `00bfbd40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbd0c`](#insn-00bfbd0c) 範囲 `[['00bfbd0c', '00bfbd13']]`
  - `CONDITIONAL_JUMP` [`00bfbd10`](#insn-00bfbd10) → [`00bfbd40`](#insn-00bfbd40)
  - `FALL_THROUGH` [`00bfbd10`](#insn-00bfbd10) → [`00bfbd14`](#insn-00bfbd14)
- ブロック [`00bfbd14`](#insn-00bfbd14) 範囲 `[['00bfbd14', '00bfbd3f']]`
- ブロック [`00bfbd40`](#insn-00bfbd40) 範囲 `[['00bfbd40', '00bfbd43']]`

## 命令位置別の参照

- [`00bfbd10`](#insn-00bfbd10) → [`00bfbd40`](#insn-00bfbd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd18`](#insn-00bfbd18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd1c`](#insn-00bfbd1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd28`](#insn-00bfbd28) → [`00c591f0`](../00c59/00c591f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c591f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd30`](#insn-00bfbd30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd34`](#insn-00bfbd34) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbd3c`](#insn-00bfbd3c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbd10`](#insn-00bfbd10)

~~~json
{
  "source": "00bfbd10",
  "target": "00bfbd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd18`](#insn-00bfbd18)

~~~json
{
  "source": "00bfbd18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd1c`](#insn-00bfbd1c)

~~~json
{
  "source": "00bfbd1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd28`](#insn-00bfbd28)

~~~json
{
  "source": "00bfbd28",
  "target": "00c591f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbd30`](#insn-00bfbd30)

~~~json
{
  "source": "00bfbd30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd34`](#insn-00bfbd34)

~~~json
{
  "source": "00bfbd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbd3c`](#insn-00bfbd3c)

~~~json
{
  "source": "00bfbd3c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
