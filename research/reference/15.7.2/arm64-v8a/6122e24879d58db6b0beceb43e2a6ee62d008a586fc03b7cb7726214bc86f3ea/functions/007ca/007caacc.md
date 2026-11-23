# 007caacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `007caacc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007caacc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/reference_unresolved-0011.md#compare-ea466a8bd68cd6fa8279d24d0015d23b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007caacc",
  "name": "FUN_007caacc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eba502c3ac7b553eac0a6837b18fe9949814504f4cc079b63dcec9edce452203",
  "source_text_sha256": "eba502c3ac7b553eac0a6837b18fe9949814504f4cc079b63dcec9edce452203",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007caacc",
        "007cab13"
      ]
    ],
    "bytes_sha256": "5096f12a505769dd858172e58a29d129673aaeaac8dc6ec6f5a2711f2c565278",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00885f80](../00885/00885f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 407 bytes

~~~c

void FUN_007caacc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
                    /* try { // try from 007caad4 to 008cac03 has its CatchHandler @ 007c86d0 */
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar2 = *param_2;
    uVar1 = FUN_00457e1c();
    FUN_00459efc(uVar1,0xb,0);
    FUN_00885f80(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007caacc"></a> `007caacc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007caad0"></a> `007caad0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007caad4"></a> `007caad4` | `e1 01 00 54` | b.ne 0x007cab10 | `CONDITIONAL_JUMP`
<a id="insn-007caad8"></a> `007caad8` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007caadc"></a> `007caadc` | `a8 01 00 35` | cbnz w8,0x007cab10 | `CONDITIONAL_JUMP`
<a id="insn-007caae0"></a> `007caae0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007caae4"></a> `007caae4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007caae8"></a> `007caae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007caaec"></a> `007caaec` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007caaf0"></a> `007caaf0` | `cb 34 f2 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-007caaf4"></a> `007caaf4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007caaf8"></a> `007caaf8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007caafc"></a> `007caafc` | `00 3d f2 97` | bl 0x00459efc | `UNCONDITIONAL_CALL`
<a id="insn-007cab00"></a> `007cab00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007cab04"></a> `007cab04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cab08"></a> `007cab08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007cab0c"></a> `007cab0c` | `1d ed 02 14` | b 0x00885f80 | `CALL_TERMINATOR`
<a id="insn-007cab10"></a> `007cab10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007caacc`](#insn-007caacc) 範囲 `[['007caacc', '007caad3']]`
  - `FALL_THROUGH` [`007caad0`](#insn-007caad0) → [`007caad4`](#insn-007caad4)
- ブロック [`007caad4`](#insn-007caad4) 範囲 `[['007caad4', '007caad7']]`
  - `CONDITIONAL_JUMP` [`007caad4`](#insn-007caad4) → [`007cab10`](#insn-007cab10)
  - `FALL_THROUGH` [`007caad4`](#insn-007caad4) → [`007caad8`](#insn-007caad8)
- ブロック [`007caad8`](#insn-007caad8) 範囲 `[['007caad8', '007caadf']]`
  - `CONDITIONAL_JUMP` [`007caadc`](#insn-007caadc) → [`007cab10`](#insn-007cab10)
  - `FALL_THROUGH` [`007caadc`](#insn-007caadc) → [`007caae0`](#insn-007caae0)
- ブロック [`007caae0`](#insn-007caae0) 範囲 `[['007caae0', '007cab0f']]`
- ブロック [`007cab10`](#insn-007cab10) 範囲 `[['007cab10', '007cab13']]`

## 命令位置別の参照

- [`007caad4`](#insn-007caad4) → [`007cab10`](#insn-007cab10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007caadc`](#insn-007caadc) → [`007cab10`](#insn-007cab10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007caae0`](#insn-007caae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007caae4`](#insn-007caae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007caaf0`](#insn-007caaf0) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`007caafc`](#insn-007caafc) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`007cab04`](#insn-007cab04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cab08`](#insn-007cab08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cab0c`](#insn-007cab0c) → [`00885f80`](../00885/00885f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00885f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007caad4`](#insn-007caad4)

~~~json
{
  "source": "007caad4",
  "target": "007cab10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007caadc`](#insn-007caadc)

~~~json
{
  "source": "007caadc",
  "target": "007cab10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007caae0`](#insn-007caae0)

~~~json
{
  "source": "007caae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007caae4`](#insn-007caae4)

~~~json
{
  "source": "007caae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007caaf0`](#insn-007caaf0)

~~~json
{
  "source": "007caaf0",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007caafc`](#insn-007caafc)

~~~json
{
  "source": "007caafc",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cab04`](#insn-007cab04)

~~~json
{
  "source": "007cab04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cab08`](#insn-007cab08)

~~~json
{
  "source": "007cab08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cab0c`](#insn-007cab0c)

~~~json
{
  "source": "007cab0c",
  "target": "00885f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
