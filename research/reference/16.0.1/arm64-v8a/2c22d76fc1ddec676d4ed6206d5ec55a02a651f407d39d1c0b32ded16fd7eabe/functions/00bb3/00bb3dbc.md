# 00bb3dbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb3994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-58a6c7994b37b0e35852426a1b6b7339)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb3e58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3e58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0009.md#compare-dbf76781ca5da6f4524600fca4090df6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb3dbc",
  "name": "_ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f170a9898a297888ed880b2d84be1525b3f70c0731d73d099936f188c8ac096",
  "source_text_sha256": "0f170a9898a297888ed880b2d84be1525b3f70c0731d73d099936f188c8ac096",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb3dbc",
        "00bb3e17"
      ]
    ],
    "bytes_sha256": "c45a069e85192136b98af7ed0895065bbe4ff619072b060a85fd175f7b66e024",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b5b0](../00c5b/00c5b5b0.md)
- [00c5b7f0](../00c5b/00c5b7f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1220 bytes

~~~c

void _ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (undefined8 param_1,byte *param_2,undefined8 param_3,undefined8 param_4)

{
  ulong uVar1;
  byte *pbVar2;
  byte bVar3;
  
  uVar1 = *(ulong *)(param_2 + 8);
  pbVar2 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00bb3dc4 to 00cb3dcb has its CatchHandler @ 00bb4ca0 */
  if ((*param_2 & 1) == 0) {
    pbVar2 = param_2 + 1;
    uVar1 = (ulong)(*param_2 >> 1);
  }
                    /* try { // try from 00bb3de4 to 00cb3df3 has its CatchHandler @ 00bb4a28 */
                    /* try { // try from 00bb3df4 to 00cb3dff has its CatchHandler @ 00bb4a1c */
                    /* try { // try from 00bb3e00 to 00cb3e2f has its CatchHandler @ 00bb31a4 */
  if ((1 < uVar1) &&
     (((bVar3 = *pbVar2, bVar3 == 0x27 || (bVar3 == 0x22)) && (bVar3 == pbVar2[uVar1 - 1])))) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
              (param_1,param_2,1,uVar1 - 2,param_2);
    return;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1,param_2,param_4,uVar1 - 2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb3dbc"></a> `00bb3dbc` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb3dc0"></a> `00bb3dc0` | `0b a8 40 a9` | ldp x11,x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bb3dc4"></a> `00bb3dc4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bb3dc8"></a> `00bb3dc8` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3dcc"></a> `00bb3dcc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3dd0"></a> `00bb3dd0` | `49 15 80 9a` | csinc x9,x10,x0,ne | `FALL_THROUGH`
<a id="insn-00bb3dd4"></a> `00bb3dd4` | `8a 01 8b 9a` | csel x10,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00bb3dd8"></a> `00bb3dd8` | `43 09 00 f1` | subs x3,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bb3ddc"></a> `00bb3ddc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb3de0"></a> `00bb3de0` | `a3 01 00 54` | b.cc 0x00bb3e14 | `CONDITIONAL_JUMP`
<a id="insn-00bb3de4"></a> `00bb3de4` | `28 01 40 39` | ldrb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bb3de8"></a> `00bb3de8` | `1f 9d 00 71` | cmp w8,#0x27 | `FALL_THROUGH`
<a id="insn-00bb3dec"></a> `00bb3dec` | `60 00 00 54` | b.eq 0x00bb3df8 | `CONDITIONAL_JUMP`
<a id="insn-00bb3df0"></a> `00bb3df0` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bb3df4"></a> `00bb3df4` | `01 01 00 54` | b.ne 0x00bb3e14 | `CONDITIONAL_JUMP`
<a id="insn-00bb3df8"></a> `00bb3df8` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00bb3dfc"></a> `00bb3dfc` | `29 f1 5f 38` | ldurb w9,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00bb3e00"></a> `00bb3e00` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bb3e04"></a> `00bb3e04` | `81 00 00 54` | b.ne 0x00bb3e14 | `CONDITIONAL_JUMP`
<a id="insn-00bb3e08"></a> `00bb3e08` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bb3e0c"></a> `00bb3e0c` | `e4 03 01 aa` | mov x4,x1 | `FALL_THROUGH`
<a id="insn-00bb3e10"></a> `00bb3e10` | `78 9e 02 14` | b 0x00c5b7f0 | `CALL_TERMINATOR`
<a id="insn-00bb3e14"></a> `00bb3e14` | `e7 9d 02 14` | b 0x00c5b5b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb3dbc`](#insn-00bb3dbc) 範囲 `[['00bb3dbc', '00bb3dc3']]`
  - `FALL_THROUGH` [`00bb3dc0`](#insn-00bb3dc0) → [`00bb3dc4`](#insn-00bb3dc4)
- ブロック [`00bb3dc4`](#insn-00bb3dc4) 範囲 `[['00bb3dc4', '00bb3de3']]`
  - `CONDITIONAL_JUMP` [`00bb3de0`](#insn-00bb3de0) → [`00bb3e14`](#insn-00bb3e14)
  - `FALL_THROUGH` [`00bb3de0`](#insn-00bb3de0) → [`00bb3de4`](#insn-00bb3de4)
- ブロック [`00bb3de4`](#insn-00bb3de4) 範囲 `[['00bb3de4', '00bb3def']]`
  - `CONDITIONAL_JUMP` [`00bb3dec`](#insn-00bb3dec) → [`00bb3df8`](#insn-00bb3df8)
  - `FALL_THROUGH` [`00bb3dec`](#insn-00bb3dec) → [`00bb3df0`](#insn-00bb3df0)
- ブロック [`00bb3df0`](#insn-00bb3df0) 範囲 `[['00bb3df0', '00bb3df3']]`
  - `FALL_THROUGH` [`00bb3df0`](#insn-00bb3df0) → [`00bb3df4`](#insn-00bb3df4)
- ブロック [`00bb3df4`](#insn-00bb3df4) 範囲 `[['00bb3df4', '00bb3df7']]`
  - `CONDITIONAL_JUMP` [`00bb3df4`](#insn-00bb3df4) → [`00bb3e14`](#insn-00bb3e14)
  - `FALL_THROUGH` [`00bb3df4`](#insn-00bb3df4) → [`00bb3df8`](#insn-00bb3df8)
- ブロック [`00bb3df8`](#insn-00bb3df8) 範囲 `[['00bb3df8', '00bb3dff']]`
  - `FALL_THROUGH` [`00bb3dfc`](#insn-00bb3dfc) → [`00bb3e00`](#insn-00bb3e00)
- ブロック [`00bb3e00`](#insn-00bb3e00) 範囲 `[['00bb3e00', '00bb3e07']]`
  - `CONDITIONAL_JUMP` [`00bb3e04`](#insn-00bb3e04) → [`00bb3e14`](#insn-00bb3e14)
  - `FALL_THROUGH` [`00bb3e04`](#insn-00bb3e04) → [`00bb3e08`](#insn-00bb3e08)
- ブロック [`00bb3e08`](#insn-00bb3e08) 範囲 `[['00bb3e08', '00bb3e13']]`
- ブロック [`00bb3e14`](#insn-00bb3e14) 範囲 `[['00bb3e14', '00bb3e17']]`

## 命令位置別の参照

- [`00bb3de0`](#insn-00bb3de0) → [`00bb3e14`](#insn-00bb3e14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3dec`](#insn-00bb3dec) → [`00bb3df8`](#insn-00bb3df8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3df4`](#insn-00bb3df4) → [`00bb3e14`](#insn-00bb3e14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e04`](#insn-00bb3e04) → [`00bb3e14`](#insn-00bb3e14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e10`](#insn-00bb3e10) → [`00c5b7f0`](../00c5b/00c5b7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b7f0` · 推定シンボル `None` · 推定型 `None`
- [`00bb3e14`](#insn-00bb3e14) → [`00c5b5b0`](../00c5b/00c5b5b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb3de0`](#insn-00bb3de0)

~~~json
{
  "source": "00bb3de0",
  "target": "00bb3e14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3dec`](#insn-00bb3dec)

~~~json
{
  "source": "00bb3dec",
  "target": "00bb3df8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3df4`](#insn-00bb3df4)

~~~json
{
  "source": "00bb3df4",
  "target": "00bb3e14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e04`](#insn-00bb3e04)

~~~json
{
  "source": "00bb3e04",
  "target": "00bb3e14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb3e10`](#insn-00bb3e10)

~~~json
{
  "source": "00bb3e10",
  "target": "00c5b7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb3e14`](#insn-00bb3e14)

~~~json
{
  "source": "00bb3e14",
  "target": "00c5b5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
