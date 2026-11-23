# 00afceb8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afcdf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdf0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-7b7dfec1496e8480541557decebbf4a3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afcefc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-5a483935a9d03232310a656bf5962a2c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afceb8",
  "name": "_ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb9fa6c2ee70d20b99ce38081f484f75b92fcfb8ad669e609e4eaf8815671de5",
  "source_text_sha256": "bb9fa6c2ee70d20b99ce38081f484f75b92fcfb8ad669e609e4eaf8815671de5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afceb8",
        "00afced3"
      ]
    ],
    "bytes_sha256": "bdacac2b9ac82d8f686cd307f8d7e9ce8877bfae1324f58f9a7b62ac275a3e49",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdece0](../00bde/00bdece0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 403 bytes

~~~c

void _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00afcec4 to 00bfcf27 has its CatchHandler @ 00af560c */
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afceb8"></a> `00afceb8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00afcebc"></a> `00afcebc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcec0"></a> `00afcec0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00afcec4"></a> `00afcec4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00afcec8"></a> `00afcec8` | `86 87 03 94` | bl 0x00bdece0 | `UNCONDITIONAL_CALL`
<a id="insn-00afcecc"></a> `00afcecc` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00afced0"></a> `00afced0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afceb8`](#insn-00afceb8) 範囲 `[['00afceb8', '00afcec3']]`
  - `FALL_THROUGH` [`00afcec0`](#insn-00afcec0) → [`00afcec4`](#insn-00afcec4)
- ブロック [`00afcec4`](#insn-00afcec4) 範囲 `[['00afcec4', '00afced3']]`

## 命令位置別の参照

- [`00afceb8`](#insn-00afceb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcec8`](#insn-00afcec8) → [`00bdece0`](../00bde/00bdece0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdece0` · 推定シンボル `None` · 推定型 `None`
- [`00afcecc`](#insn-00afcecc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afceb8`](#insn-00afceb8)

~~~json
{
  "source": "00afceb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcec8`](#insn-00afcec8)

~~~json
{
  "source": "00afcec8",
  "target": "00bdece0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcecc`](#insn-00afcecc)

~~~json
{
  "source": "00afcecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
