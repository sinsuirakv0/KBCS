# 00bcfbc8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b606c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606c8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/reference_unresolved-0001.md#compare-e398593981e1c3c03232d2e4f43d34f3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfff0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfff0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-9d17ab396219bc492d194f4d7c536743)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfbc8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94c8ebd24429b7d4cf1ca297cdf0feb6779431646a871108df464bbff216ae6a",
  "source_text_sha256": "94c8ebd24429b7d4cf1ca297cdf0feb6779431646a871108df464bbff216ae6a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfbc8",
        "00bcfbdb"
      ]
    ],
    "bytes_sha256": "1f32248c643eb24f1357c02126bb7b159d61ed737b5fd3cd9e19d7f1b13c4b02",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 351 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv(long *param_1)

{
  if (param_1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bcfbd4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))();
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfbc8"></a> `00bcfbc8` | `80 00 00 b4` | cbz x0,0x00bcfbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcfbcc"></a> `00bcfbcc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcfbd0"></a> `00bcfbd0` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfbd4"></a> `00bcfbd4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcfbd8"></a> `00bcfbd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfbc8`](#insn-00bcfbc8) 範囲 `[['00bcfbc8', '00bcfbcb']]`
  - `CONDITIONAL_JUMP` [`00bcfbc8`](#insn-00bcfbc8) → [`00bcfbd8`](#insn-00bcfbd8)
  - `FALL_THROUGH` [`00bcfbc8`](#insn-00bcfbc8) → [`00bcfbcc`](#insn-00bcfbcc)
- ブロック [`00bcfbcc`](#insn-00bcfbcc) 範囲 `[['00bcfbcc', '00bcfbd7']]`
- ブロック [`00bcfbd8`](#insn-00bcfbd8) 範囲 `[['00bcfbd8', '00bcfbdb']]`

## 命令位置別の参照

- [`00bcfbc8`](#insn-00bcfbc8) → [`00bcfbd8`](#insn-00bcfbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfbc8`](#insn-00bcfbc8)

~~~json
{
  "source": "00bcfbc8",
  "target": "00bcfbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
