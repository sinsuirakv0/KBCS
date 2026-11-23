# 00bbaec8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaf90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf90.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-1d27a920a8f9062ace5dd9d4988f6759)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaec8",
  "name": "_ZNSt12length_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef0227429fdf6497c07f5e10f12261b19e26deb569805575c4e512b52863ee6a",
  "source_text_sha256": "ef0227429fdf6497c07f5e10f12261b19e26deb569805575c4e512b52863ee6a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaec8",
        "00bbaef3"
      ]
    ],
    "bytes_sha256": "9379cd22db794e5b3ff5f0e65ac74fb4b058b9f1d3224cace3556b37a1b21b5f",
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

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdafb0](../00bda/00bdafb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZNSt12length_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
                    /* try { // try from 00bbaee4 to 00cbaeef has its CatchHandler @ 00bbb7c8 */
                    /* try { // try from 00bbaef0 to 00cbaeff has its CatchHandler @ 00bbb790 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaec8"></a> `00bbaec8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaecc"></a> `00bbaecc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaed0"></a> `00bbaed0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaed4"></a> `00bbaed4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaed8"></a> `00bbaed8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaedc"></a> `00bbaedc` | `35 80 00 94` | bl 0x00bdafb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaee0"></a> `00bbaee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaee4"></a> `00bbaee4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaee8"></a> `00bbaee8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaeec"></a> `00bbaeec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaef0"></a> `00bbaef0` | `1c 80 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaec8`](#insn-00bbaec8) 範囲 `[['00bbaec8', '00bbaee3']]`
  - `FALL_THROUGH` [`00bbaee0`](#insn-00bbaee0) → [`00bbaee4`](#insn-00bbaee4)
- ブロック [`00bbaee4`](#insn-00bbaee4) 範囲 `[['00bbaee4', '00bbaeef']]`
  - `FALL_THROUGH` [`00bbaeec`](#insn-00bbaeec) → [`00bbaef0`](#insn-00bbaef0)
- ブロック [`00bbaef0`](#insn-00bbaef0) 範囲 `[['00bbaef0', '00bbaef3']]`

## 命令位置別の参照

- [`00bbaecc`](#insn-00bbaecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaed0`](#insn-00bbaed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaedc`](#insn-00bbaedc) → [`00bdafb0`](../00bda/00bdafb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee4`](#insn-00bbaee4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaee8`](#insn-00bbaee8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaef0`](#insn-00bbaef0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaecc`](#insn-00bbaecc)

~~~json
{
  "source": "00bbaecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaed0`](#insn-00bbaed0)

~~~json
{
  "source": "00bbaed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaedc`](#insn-00bbaedc)

~~~json
{
  "source": "00bbaedc",
  "target": "00bdafb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaee4`](#insn-00bbaee4)

~~~json
{
  "source": "00bbaee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaee8`](#insn-00bbaee8)

~~~json
{
  "source": "00bbaee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaef0`](#insn-00bbaef0)

~~~json
{
  "source": "00bbaef0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
