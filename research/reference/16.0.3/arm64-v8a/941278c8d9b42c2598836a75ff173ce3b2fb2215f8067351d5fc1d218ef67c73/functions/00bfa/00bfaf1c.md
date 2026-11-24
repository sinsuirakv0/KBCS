# 00bfaf1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9f28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9f28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-35b15bc3815fc1d2968b4ac94c70860f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaf1c",
  "name": "_ZNSt6__ndk17promiseIvE10get_futureEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3733d4989622986d0017d55ceea19654002257bc8e021136e8d1598a4978cfd9",
  "source_text_sha256": "3733d4989622986d0017d55ceea19654002257bc8e021136e8d1598a4978cfd9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaf1c",
        "00bfaf43"
      ]
    ],
    "bytes_sha256": "a008dbaafd966427b90728ceb3c802aa141cd34b71dd92470fb168a81f7765d1",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c595c0](../00c59/00c595c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 268 bytes

~~~c

void _ZNSt6__ndk17promiseIvE10get_futureEv(undefined8 param_1,long *param_2)

{
  if (*param_2 != 0) {
    _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE(param_1);
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
<a id="insn-00bfaf1c"></a> `00bfaf1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfaf20"></a> `00bfaf20` | `01 00 40 f9` | ldr x1,[x0] | `FALL_THROUGH`
<a id="insn-00bfaf24"></a> `00bfaf24` | `61 00 00 b4` | cbz x1,0x00bfaf30 | `CONDITIONAL_JUMP`
<a id="insn-00bfaf28"></a> `00bfaf28` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfaf2c"></a> `00bfaf2c` | `a5 79 01 14` | b 0x00c595c0 | `CALL_TERMINATOR`
<a id="insn-00bfaf30"></a> `00bfaf30` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaf34"></a> `00bfaf34` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfaf38"></a> `00bfaf38` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaf3c"></a> `00bfaf3c` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bfaf40"></a> `00bfaf40` | `bd 7e e1 97` | bl 0x0045aa34 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaf1c`](#insn-00bfaf1c) 範囲 `[['00bfaf1c', '00bfaf27']]`
  - `CONDITIONAL_JUMP` [`00bfaf24`](#insn-00bfaf24) → [`00bfaf30`](#insn-00bfaf30)
  - `FALL_THROUGH` [`00bfaf24`](#insn-00bfaf24) → [`00bfaf28`](#insn-00bfaf28)
- ブロック [`00bfaf28`](#insn-00bfaf28) 範囲 `[['00bfaf28', '00bfaf2f']]`
- ブロック [`00bfaf30`](#insn-00bfaf30) 範囲 `[['00bfaf30', '00bfaf43']]`

## 命令位置別の参照

- [`00bfaf24`](#insn-00bfaf24) → [`00bfaf30`](#insn-00bfaf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf2c`](#insn-00bfaf2c) → [`00c595c0`](../00c59/00c595c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c595c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf34`](#insn-00bfaf34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf40`](#insn-00bfaf40) → [`0045aa34`](../0045a/0045aa34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045aa34` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaf24`](#insn-00bfaf24)

~~~json
{
  "source": "00bfaf24",
  "target": "00bfaf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf2c`](#insn-00bfaf2c)

~~~json
{
  "source": "00bfaf2c",
  "target": "00c595c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaf34`](#insn-00bfaf34)

~~~json
{
  "source": "00bfaf34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf40`](#insn-00bfaf40)

~~~json
{
  "source": "00bfaf40",
  "target": "0045aa34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
