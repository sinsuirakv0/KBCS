# 00aae1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aae17c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae17c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-e5847ff9b77246716f85f3cc84123332)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aaf1e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aaf/00aaf1e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-bf45e6a0440cee6004036873728d6722)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aae1ec",
  "name": "FUN_00aae1ec",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903",
  "source_text_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aae1ec",
        "00aae23b"
      ]
    ],
    "bytes_sha256": "d23e9ed9278a95055287ce84389ea1cb294ebed5757d89c9032c56510722d327",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa5998](../00aa5/00aa5998.md)
- [00aa6150](../00aa6/00aa6150.md)
- [00aae1ec](../00aae/00aae1ec.md)

## 呼び出し先

- [005b9f24](../005b9/005b9f24.md)
- [00aae1ec](../00aae/00aae1ec.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00aae1ec(undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aae1ec(param_1,*param_2);
    FUN_00aae1ec(param_1,param_2[1]);
    FUN_005b9f24(param_2 + 5,param_2[6]);
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aae1ec"></a> `00aae1ec` | `61 02 00 b4` | cbz x1,0x00aae238 | `CONDITIONAL_JUMP`
<a id="insn-00aae1f0"></a> `00aae1f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aae1f4"></a> `00aae1f4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae1f8"></a> `00aae1f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aae1fc"></a> `00aae1fc` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00aae200"></a> `00aae200` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aae204"></a> `00aae204` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aae208"></a> `00aae208` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aae20c"></a> `00aae20c` | `f8 ff ff 97` | bl 0x00aae1ec | `UNCONDITIONAL_CALL`
<a id="insn-00aae210"></a> `00aae210` | `81 06 40 f9` | ldr x1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aae214"></a> `00aae214` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aae218"></a> `00aae218` | `f5 ff ff 97` | bl 0x00aae1ec | `UNCONDITIONAL_CALL`
<a id="insn-00aae21c"></a> `00aae21c` | `81 1a 40 f9` | ldr x1,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aae220"></a> `00aae220` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aae224"></a> `00aae224` | `40 2f ec 97` | bl 0x005b9f24 | `UNCONDITIONAL_CALL`
<a id="insn-00aae228"></a> `00aae228` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aae22c"></a> `00aae22c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae230"></a> `00aae230` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aae234"></a> `00aae234` | `53 a7 06 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00aae238"></a> `00aae238` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aae1ec`](#insn-00aae1ec) 範囲 `[['00aae1ec', '00aae1ef']]`
  - `CONDITIONAL_JUMP` [`00aae1ec`](#insn-00aae1ec) → [`00aae238`](#insn-00aae238)
  - `FALL_THROUGH` [`00aae1ec`](#insn-00aae1ec) → [`00aae1f0`](#insn-00aae1f0)
- ブロック [`00aae1f0`](#insn-00aae1f0) 範囲 `[['00aae1f0', '00aae237']]`
- ブロック [`00aae238`](#insn-00aae238) 範囲 `[['00aae238', '00aae23b']]`

## 命令位置別の参照

- [`00aae1ec`](#insn-00aae1ec) → [`00aae238`](#insn-00aae238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae1f0`](#insn-00aae1f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae1f4`](#insn-00aae1f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae20c`](#insn-00aae20c) → [`00aae1ec`](#insn-00aae1ec) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aae1ec` · 推定シンボル `None` · 推定型 `None`
- [`00aae218`](#insn-00aae218) → [`00aae1ec`](#insn-00aae1ec) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aae1ec` · 推定シンボル `None` · 推定型 `None`
- [`00aae224`](#insn-00aae224) → [`005b9f24`](../005b9/005b9f24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005b9f24` · 推定シンボル `None` · 推定型 `None`
- [`00aae22c`](#insn-00aae22c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae230`](#insn-00aae230) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae234`](#insn-00aae234) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aae1ec`](#insn-00aae1ec)

~~~json
{
  "source": "00aae1ec",
  "target": "00aae238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae1f0`](#insn-00aae1f0)

~~~json
{
  "source": "00aae1f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae1f4`](#insn-00aae1f4)

~~~json
{
  "source": "00aae1f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae20c`](#insn-00aae20c)

~~~json
{
  "source": "00aae20c",
  "target": "00aae1ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae218`](#insn-00aae218)

~~~json
{
  "source": "00aae218",
  "target": "00aae1ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae224`](#insn-00aae224)

~~~json
{
  "source": "00aae224",
  "target": "005b9f24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae22c`](#insn-00aae22c)

~~~json
{
  "source": "00aae22c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae230`](#insn-00aae230)

~~~json
{
  "source": "00aae230",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae234`](#insn-00aae234)

~~~json
{
  "source": "00aae234",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
