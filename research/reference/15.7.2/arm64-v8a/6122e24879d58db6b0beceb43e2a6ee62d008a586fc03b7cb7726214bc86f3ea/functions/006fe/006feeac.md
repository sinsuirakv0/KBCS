# 006feeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `006feeac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fe/006feeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0009.md#compare-a6f4b60c99369c132a258cc20215de6b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006feeac",
  "name": "FUN_006feeac",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b5f2d284329b7dc26293869f955ea6a7af6b745822d1782dba3fbfb9296be827",
  "source_text_sha256": "b5f2d284329b7dc26293869f955ea6a7af6b745822d1782dba3fbfb9296be827",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006feeac",
        "006feecf"
      ]
    ],
    "bytes_sha256": "e991ef461d4c0c65db0b58cb15d222388e78eccb47f44eaec481febcc3c42089",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)
- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 175 bytes

~~~c

undefined4 FUN_006feeac(int param_1)

{
  if (param_1 + 0x1aU < 0x1f) {
    return *(undefined4 *)(&DAT_002d02d8 + (ulong)(param_1 + 0x1aU) * 4);
  }
  return 0xffffffff;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006feeac"></a> `006feeac` | `08 68 00 11` | add w8,w0,#0x1a | `FALL_THROUGH`
<a id="insn-006feeb0"></a> `006feeb0` | `1f 79 00 71` | cmp w8,#0x1e | `FALL_THROUGH`
<a id="insn-006feeb4"></a> `006feeb4` | `a8 00 00 54` | b.hi 0x006feec8 | `CONDITIONAL_JUMP`
<a id="insn-006feeb8"></a> `006feeb8` | `89 de ff d0` | adrp x9,0x2d0000 | `FALL_THROUGH`
<a id="insn-006feebc"></a> `006feebc` | `29 61 0b 91` | add x9,x9,#0x2d8 | `FALL_THROUGH`
<a id="insn-006feec0"></a> `006feec0` | `20 59 68 b8` | ldr w0,[x9, w8, UXTW #0x2] | `FALL_THROUGH`
<a id="insn-006feec4"></a> `006feec4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006feec8"></a> `006feec8` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-006feecc"></a> `006feecc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006feeac`](#insn-006feeac) 範囲 `[['006feeac', '006feeb7']]`
  - `CONDITIONAL_JUMP` [`006feeb4`](#insn-006feeb4) → [`006feec8`](#insn-006feec8)
  - `FALL_THROUGH` [`006feeb4`](#insn-006feeb4) → [`006feeb8`](#insn-006feeb8)
- ブロック [`006feeb8`](#insn-006feeb8) 範囲 `[['006feeb8', '006feec7']]`
- ブロック [`006feec8`](#insn-006feec8) 範囲 `[['006feec8', '006feecf']]`

## 命令位置別の参照

- [`006feeb4`](#insn-006feeb4) → [`006feec8`](#insn-006feec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006feec0`](#insn-006feec0) → `002d02d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006feeb4`](#insn-006feeb4)

~~~json
{
  "source": "006feeb4",
  "target": "006feec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006feec0`](#insn-006feec0)

~~~json
{
  "source": "006feec0",
  "target": "002d02d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
