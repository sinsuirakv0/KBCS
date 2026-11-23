# 00bbaef4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbafbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbafbc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-331fe9bd2b0e366392bd2127bdf714bf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaef4",
  "name": "_ZNSt12out_of_rangeD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "746e92c5a788746dfe68eb99bec18041f680aaebb160a871bf2ad37adf5c2607",
  "source_text_sha256": "746e92c5a788746dfe68eb99bec18041f680aaebb160a871bf2ad37adf5c2607",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaef4",
        "00bbaf1f"
      ]
    ],
    "bytes_sha256": "e82fefe191f63cc759e13f82dc1d705f7a2aaccef48ffe152ff06bfd3b895694",
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
- [00bdb150](../00bdb/00bdb150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 205 bytes

~~~c

void _ZNSt12out_of_rangeD0Ev(void *param_1)

{
                    /* try { // try from 00bbaf00 to 00cbaf13 has its CatchHandler @ 00bbb778 */
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaef4"></a> `00bbaef4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaef8"></a> `00bbaef8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaefc"></a> `00bbaefc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf00"></a> `00bbaf00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaf04"></a> `00bbaf04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaf08"></a> `00bbaf08` | `92 80 00 94` | bl 0x00bdb150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf0c"></a> `00bbaf0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf10"></a> `00bbaf10` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf14"></a> `00bbaf14` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaf18"></a> `00bbaf18` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaf1c"></a> `00bbaf1c` | `11 80 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaef4`](#insn-00bbaef4) 範囲 `[['00bbaef4', '00bbaeff']]`
  - `FALL_THROUGH` [`00bbaefc`](#insn-00bbaefc) → [`00bbaf00`](#insn-00bbaf00)
- ブロック [`00bbaf00`](#insn-00bbaf00) 範囲 `[['00bbaf00', '00bbaf1f']]`

## 命令位置別の参照

- [`00bbaef8`](#insn-00bbaef8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaefc`](#insn-00bbaefc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf08`](#insn-00bbaf08) → [`00bdb150`](../00bdb/00bdb150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb150` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf10`](#insn-00bbaf10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf14`](#insn-00bbaf14) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf1c`](#insn-00bbaf1c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaef8`](#insn-00bbaef8)

~~~json
{
  "source": "00bbaef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaefc`](#insn-00bbaefc)

~~~json
{
  "source": "00bbaefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf08`](#insn-00bbaf08)

~~~json
{
  "source": "00bbaf08",
  "target": "00bdb150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf10`](#insn-00bbaf10)

~~~json
{
  "source": "00bbaf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf14`](#insn-00bbaf14)

~~~json
{
  "source": "00bbaf14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf1c`](#insn-00bbaf1c)

~~~json
{
  "source": "00bbaf1c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
