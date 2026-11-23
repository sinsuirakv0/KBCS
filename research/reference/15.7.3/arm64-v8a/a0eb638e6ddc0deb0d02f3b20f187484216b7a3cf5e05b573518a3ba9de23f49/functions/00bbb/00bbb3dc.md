# 00bbb3dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbb314`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb314.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-b8fca75f339421a79939d34ca02c2b3d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbb420`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb420.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-db9a95e854956cdc2142eb0f87c70007)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb3dc",
  "name": "FUN_00bbb3dc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a742fd167566851b4b6f6915fbb372e868d8f57132e1224c908d3263f3c33c2d",
  "source_text_sha256": "a742fd167566851b4b6f6915fbb372e868d8f57132e1224c908d3263f3c33c2d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb3dc",
        "00bbb407"
      ]
    ],
    "bytes_sha256": "87c1c03a3c03f22bf12067ead8638c5fa2589632400d4001e7153f620bd0cc47",
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

- [00bdb010](../00bdb/00bdb010.md)
- [00be1e40](../00be1/00be1e40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 94 bytes

~~~c

void FUN_00bbb3dc(void *param_1)

{
  _ZNSt9type_infoD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb3dc"></a> `00bbb3dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbb3e0"></a> `00bbb3e0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbb3e4"></a> `00bbb3e4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb3e8"></a> `00bbb3e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbb3ec"></a> `00bbb3ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbb3f0"></a> `00bbb3f0` | `94 9a 00 94` | bl 0x00be1e40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb3f4"></a> `00bbb3f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb3f8"></a> `00bbb3f8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb3fc"></a> `00bbb3fc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbb400"></a> `00bbb400` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbb404"></a> `00bbb404` | `03 7f 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb3dc`](#insn-00bbb3dc) 範囲 `[['00bbb3dc', '00bbb407']]`

## 命令位置別の参照

- [`00bbb3e0`](#insn-00bbb3e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3e4`](#insn-00bbb3e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3f0`](#insn-00bbb3f0) → [`00be1e40`](../00be1/00be1e40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e40` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3f8`](#insn-00bbb3f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb3fc`](#insn-00bbb3fc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb404`](#insn-00bbb404) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb3e0`](#insn-00bbb3e0)

~~~json
{
  "source": "00bbb3e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3e4`](#insn-00bbb3e4)

~~~json
{
  "source": "00bbb3e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3f0`](#insn-00bbb3f0)

~~~json
{
  "source": "00bbb3f0",
  "target": "00be1e40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb3f8`](#insn-00bbb3f8)

~~~json
{
  "source": "00bbb3f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb3fc`](#insn-00bbb3fc)

~~~json
{
  "source": "00bbb3fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb404`](#insn-00bbb404)

~~~json
{
  "source": "00bbb404",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
