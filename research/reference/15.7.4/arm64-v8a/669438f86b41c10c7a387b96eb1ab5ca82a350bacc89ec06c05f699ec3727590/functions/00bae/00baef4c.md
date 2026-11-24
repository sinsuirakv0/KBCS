# 00baef4c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baef08`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baef08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-97cc70bc22ebcc3ac3bd30d3306acfd9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2b994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b994.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-245a97cffd1804cc78798c61a48b1761)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baef4c",
  "name": "_ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e8f870b0e68120a1c475c33c13854c50a542807afcae246870e3e433b151e23",
  "source_text_sha256": "9e8f870b0e68120a1c475c33c13854c50a542807afcae246870e3e433b151e23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baef4c",
        "00baef77"
      ]
    ],
    "bytes_sha256": "c76aa732b1afc1dd97e0eda0cfeb9d3f3319c5b23281b1a4cacf9b02e769ccab",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00be1bf0](../00be1/00be1bf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 145 bytes

~~~c

void _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baef4c"></a> `00baef4c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baef50"></a> `00baef50` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baef54"></a> `00baef54` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baef58"></a> `00baef58` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baef5c"></a> `00baef5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baef60"></a> `00baef60` | `24 cb 00 94` | bl 0x00be1bf0 | `UNCONDITIONAL_CALL`
<a id="insn-00baef64"></a> `00baef64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baef68"></a> `00baef68` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baef6c"></a> `00baef6c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baef70"></a> `00baef70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baef74"></a> `00baef74` | `3b b0 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baef4c`](#insn-00baef4c) 範囲 `[['00baef4c', '00baef77']]`

## 命令位置別の参照

- [`00baef50`](#insn-00baef50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef54`](#insn-00baef54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef60`](#insn-00baef60) → [`00be1bf0`](../00be1/00be1bf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1bf0` · 推定シンボル `None` · 推定型 `None`
- [`00baef68`](#insn-00baef68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef6c`](#insn-00baef6c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baef74`](#insn-00baef74) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baef50`](#insn-00baef50)

~~~json
{
  "source": "00baef50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef54`](#insn-00baef54)

~~~json
{
  "source": "00baef54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef60`](#insn-00baef60)

~~~json
{
  "source": "00baef60",
  "target": "00be1bf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baef68`](#insn-00baef68)

~~~json
{
  "source": "00baef68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef6c`](#insn-00baef6c)

~~~json
{
  "source": "00baef6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baef74`](#insn-00baef74)

~~~json
{
  "source": "00baef74",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
