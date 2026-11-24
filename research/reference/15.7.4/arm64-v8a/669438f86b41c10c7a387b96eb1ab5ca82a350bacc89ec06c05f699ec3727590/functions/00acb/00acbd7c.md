# 00acbd7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acbd38`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd38.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-dabb5543493adea6282dc538b809d4ab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0090.md#review-66bd5397956d413d6cc87e7721b23a60)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbd7c",
  "name": "FUN_00acbd7c",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ba6332849756314d8b11ffbfafb6d188eb393de4e6e7bcef94c64d704687231",
  "source_text_sha256": "7ba6332849756314d8b11ffbfafb6d188eb393de4e6e7bcef94c64d704687231",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbd7c",
        "00acbda3"
      ]
    ],
    "bytes_sha256": "eafed55ad795f10733d351d222739500d4399164e7587ddf1dc28c956996d8b2",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004188e8](../00418/004188e8.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 187 bytes

~~~c

void FUN_00acbd7c(undefined8 param_1,int param_2)

{
  long lVar1;
  
  if (param_2 != 0) {
    return;
  }
  lVar1 = FUN_0081f580();
  *(undefined1 *)(lVar1 + 0x347f) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbd7c"></a> `00acbd7c` | `41 00 00 34` | cbz w1,0x00acbd84 | `CONDITIONAL_JUMP`
<a id="insn-00acbd80"></a> `00acbd80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbd84"></a> `00acbd84` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00acbd88"></a> `00acbd88` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbd8c"></a> `00acbd8c` | `fd 4d f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd90"></a> `00acbd90` | `e8 8f 86 52` | mov w8,#0x347f | `FALL_THROUGH`
<a id="insn-00acbd94"></a> `00acbd94` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acbd98"></a> `00acbd98` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00acbd9c"></a> `00acbd9c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00acbda0"></a> `00acbda0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbd7c`](#insn-00acbd7c) 範囲 `[['00acbd7c', '00acbd7f']]`
  - `CONDITIONAL_JUMP` [`00acbd7c`](#insn-00acbd7c) → [`00acbd84`](#insn-00acbd84)
  - `FALL_THROUGH` [`00acbd7c`](#insn-00acbd7c) → [`00acbd80`](#insn-00acbd80)
- ブロック [`00acbd80`](#insn-00acbd80) 範囲 `[['00acbd80', '00acbd83']]`
- ブロック [`00acbd84`](#insn-00acbd84) 範囲 `[['00acbd84', '00acbda3']]`

## 命令位置別の参照

- [`00acbd7c`](#insn-00acbd7c) → [`00acbd84`](#insn-00acbd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd84`](#insn-00acbd84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd8c`](#insn-00acbd8c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbd9c`](#insn-00acbd9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbd7c`](#insn-00acbd7c)

~~~json
{
  "source": "00acbd7c",
  "target": "00acbd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd84`](#insn-00acbd84)

~~~json
{
  "source": "00acbd84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd8c`](#insn-00acbd8c)

~~~json
{
  "source": "00acbd8c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd9c`](#insn-00acbd9c)

~~~json
{
  "source": "00acbd9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
