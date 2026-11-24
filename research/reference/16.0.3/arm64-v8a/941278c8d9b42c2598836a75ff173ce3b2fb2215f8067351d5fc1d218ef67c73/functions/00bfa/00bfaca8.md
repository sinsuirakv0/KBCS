# 00bfaca8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf9cb4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf9cb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-2d6ca0c685a1c2bf3db8db4771738329)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaca8",
  "name": "_ZNSt6__ndk16futureIvE3getEv",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8de37edde5b4f2c2adbca127bf913a7b4c2868870ef6822edd44a669a7e018ab",
  "source_text_sha256": "8de37edde5b4f2c2adbca127bf913a7b4c2868870ef6822edd44a669a7e018ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaca8",
        "00bfad03"
      ]
    ],
    "bytes_sha256": "c474d1a1f49dfc800ec70e8d89448a9fd373c94fb241b1df72cb72c1057fe1d3",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c54d90](../00c54/00c54d90.md)
- [00c5f300](../00c5f/00c5f300.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 494 bytes

~~~c

void _ZNSt6__ndk16futureIvE3getEv(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)*param_1;
  *param_1 = 0;
  _ZNSt6__ndk117__assoc_sub_state4copyEv(plVar2);
  lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1);
  if (lVar1 != 0) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bfad00. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar2 + 0x10))(plVar2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaca8"></a> `00bfaca8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfacac"></a> `00bfacac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfacb0"></a> `00bfacb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfacb4"></a> `00bfacb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfacb8"></a> `00bfacb8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bfacbc"></a> `00bfacbc` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfacc0"></a> `00bfacc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfacc4"></a> `00bfacc4` | `8f 91 01 94` | bl 0x00c5f300 | `UNCONDITIONAL_CALL`
<a id="insn-00bfacc8"></a> `00bfacc8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bfaccc"></a> `00bfaccc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00bfacd0"></a> `00bfacd0` | `30 68 01 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfacd4"></a> `00bfacd4` | `a0 00 00 b4` | cbz x0,0x00bface8 | `CONDITIONAL_JUMP`
<a id="insn-00bfacd8"></a> `00bfacd8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfacdc"></a> `00bfacdc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bface0"></a> `00bface0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bface4"></a> `00bface4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bface8"></a> `00bface8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfacec"></a> `00bfacec` | `10 09 40 f9` | ldr x16,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bfacf0"></a> `00bfacf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfacf4"></a> `00bfacf4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfacf8"></a> `00bfacf8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfacfc"></a> `00bfacfc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfad00"></a> `00bfad00` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfaca8`](#insn-00bfaca8) 範囲 `[['00bfaca8', '00bfacd7']]`
  - `CONDITIONAL_JUMP` [`00bfacd4`](#insn-00bfacd4) → [`00bface8`](#insn-00bface8)
  - `FALL_THROUGH` [`00bfacd4`](#insn-00bfacd4) → [`00bfacd8`](#insn-00bfacd8)
- ブロック [`00bfacd8`](#insn-00bfacd8) 範囲 `[['00bfacd8', '00bface7']]`
- ブロック [`00bface8`](#insn-00bface8) 範囲 `[['00bface8', '00bfad03']]`

## 命令位置別の参照

- [`00bfacac`](#insn-00bfacac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacb0`](#insn-00bfacb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacc4`](#insn-00bfacc4) → [`00c5f300`](../00c5f/00c5f300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f300` · 推定シンボル `None` · 推定型 `None`
- [`00bfacd0`](#insn-00bfacd0) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00bfacd4`](#insn-00bfacd4) → [`00bface8`](#insn-00bface8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacd8`](#insn-00bfacd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacdc`](#insn-00bfacdc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacf4`](#insn-00bfacf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfacf8`](#insn-00bfacf8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfacac`](#insn-00bfacac)

~~~json
{
  "source": "00bfacac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacb0`](#insn-00bfacb0)

~~~json
{
  "source": "00bfacb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacc4`](#insn-00bfacc4)

~~~json
{
  "source": "00bfacc4",
  "target": "00c5f300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfacd0`](#insn-00bfacd0)

~~~json
{
  "source": "00bfacd0",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfacd4`](#insn-00bfacd4)

~~~json
{
  "source": "00bfacd4",
  "target": "00bface8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacd8`](#insn-00bfacd8)

~~~json
{
  "source": "00bfacd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacdc`](#insn-00bfacdc)

~~~json
{
  "source": "00bfacdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacf4`](#insn-00bfacf4)

~~~json
{
  "source": "00bfacf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfacf8`](#insn-00bfacf8)

~~~json
{
  "source": "00bfacf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
