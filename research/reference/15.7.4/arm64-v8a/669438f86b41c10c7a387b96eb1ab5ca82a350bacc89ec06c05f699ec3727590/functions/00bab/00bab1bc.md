# 00bab1bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bab178`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-d2b1fc00ee923d02f33d779dfcac0bd1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c27c04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27c04.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-37e418c35bc10081159a6fab2947ab21)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab1bc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528",
  "source_text_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bab1bc",
        "00bab21b"
      ]
    ],
    "bytes_sha256": "34dcb932116e7c3072ce9930436fc04be133b25e5cd61cd97ceaa503195674ac",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1580](../00be1/00be1580.md)
- [00be1b10](../00be1/00be1b10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 449 bytes

~~~c

int _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc(long param_1,wint_t param_2,int param_3)

{
  int iVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  iVar1 = wctob(param_2);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  if (iVar1 != -1) {
    param_3 = iVar1;
  }
                    /* try { // try from 00bab210 to 00cab21b has its CatchHandler @ 00bab494 */
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bab1bc"></a> `00bab1bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bab1c0"></a> `00bab1c0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bab1c4"></a> `00bab1c4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab1c8"></a> `00bab1c8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab1cc"></a> `00bab1cc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bab1d0"></a> `00bab1d0` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bab1d4"></a> `00bab1d4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00bab1d8"></a> `00bab1d8` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00bab1dc"></a> `00bab1dc` | `e9 d8 00 94` | bl 0x00be1580 | `UNCONDITIONAL_CALL`
<a id="insn-00bab1e0"></a> `00bab1e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bab1e4"></a> `00bab1e4` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bab1e8"></a> `00bab1e8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00bab1ec"></a> `00bab1ec` | `49 da 00 94` | bl 0x00be1b10 | `UNCONDITIONAL_CALL`
<a id="insn-00bab1f0"></a> `00bab1f0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00bab1f4"></a> `00bab1f4` | `74 00 00 b4` | cbz x20,0x00bab200 | `CONDITIONAL_JUMP`
<a id="insn-00bab1f8"></a> `00bab1f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bab1fc"></a> `00bab1fc` | `e1 d8 00 94` | bl 0x00be1580 | `UNCONDITIONAL_CALL`
<a id="insn-00bab200"></a> `00bab200` | `bf 06 00 31` | cmn w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bab204"></a> `00bab204` | `60 02 95 1a` | csel w0,w19,w21,eq | `FALL_THROUGH`
<a id="insn-00bab208"></a> `00bab208` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab20c"></a> `00bab20c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab210"></a> `00bab210` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bab214"></a> `00bab214` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bab218"></a> `00bab218` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bab1bc`](#insn-00bab1bc) 範囲 `[['00bab1bc', '00bab1f7']]`
  - `CONDITIONAL_JUMP` [`00bab1f4`](#insn-00bab1f4) → [`00bab200`](#insn-00bab200)
  - `FALL_THROUGH` [`00bab1f4`](#insn-00bab1f4) → [`00bab1f8`](#insn-00bab1f8)
- ブロック [`00bab1f8`](#insn-00bab1f8) 範囲 `[['00bab1f8', '00bab1ff']]`
  - `FALL_THROUGH` [`00bab1fc`](#insn-00bab1fc) → [`00bab200`](#insn-00bab200)
- ブロック [`00bab200`](#insn-00bab200) 範囲 `[['00bab200', '00bab20f']]`
  - `FALL_THROUGH` [`00bab20c`](#insn-00bab20c) → [`00bab210`](#insn-00bab210)
- ブロック [`00bab210`](#insn-00bab210) 範囲 `[['00bab210', '00bab21b']]`

## 命令位置別の参照

- [`00bab1c0`](#insn-00bab1c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c4`](#insn-00bab1c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c8`](#insn-00bab1c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1dc`](#insn-00bab1dc) → [`00be1580`](../00be1/00be1580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1580` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e4`](#insn-00bab1e4) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1ec`](#insn-00bab1ec) → [`00be1b10`](../00be1/00be1b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b10` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f4`](#insn-00bab1f4) → [`00bab200`](#insn-00bab200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1fc`](#insn-00bab1fc) → [`00be1580`](../00be1/00be1580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1580` · 推定シンボル `None` · 推定型 `None`
- [`00bab208`](#insn-00bab208) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab20c`](#insn-00bab20c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab210`](#insn-00bab210) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab1c0`](#insn-00bab1c0)

~~~json
{
  "source": "00bab1c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1c4`](#insn-00bab1c4)

~~~json
{
  "source": "00bab1c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1c8`](#insn-00bab1c8)

~~~json
{
  "source": "00bab1c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1dc`](#insn-00bab1dc)

~~~json
{
  "source": "00bab1dc",
  "target": "00be1580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab1e4`](#insn-00bab1e4)

~~~json
{
  "source": "00bab1e4",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1ec`](#insn-00bab1ec)

~~~json
{
  "source": "00bab1ec",
  "target": "00be1b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab1f4`](#insn-00bab1f4)

~~~json
{
  "source": "00bab1f4",
  "target": "00bab200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1fc`](#insn-00bab1fc)

~~~json
{
  "source": "00bab1fc",
  "target": "00be1580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab208`](#insn-00bab208)

~~~json
{
  "source": "00bab208",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab20c`](#insn-00bab20c)

~~~json
{
  "source": "00bab20c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab210`](#insn-00bab210)

~~~json
{
  "source": "00bab210",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
