# 004ccabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004cc79c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc79c.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0007.md#compare-ad74e032ad28e959bfdbde62b2b2a785)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ccabc",
  "name": "_ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97bfba8ffde36ccc779f72a7f8dd159bbac466780f43bf9fc30db48889797a90",
  "source_text_sha256": "97bfba8ffde36ccc779f72a7f8dd159bbac466780f43bf9fc30db48889797a90",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ccabc",
        "004ccb47"
      ]
    ],
    "bytes_sha256": "22fb9e220d751b801db45efb4bb338cfc760ed49e422d0f72607a3a7fcebe92c",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004b3868](../004b3/004b3868.md)
- [0054084c](../00540/0054084c.md)
- [00c59b80](../00c59/00c59b80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 722 bytes

~~~c

void _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
               (long *param_1,byte *param_2,undefined4 param_3)

{
  byte *pbVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar2 = *(ulong *)(param_2 + 8);
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
    uVar2 = (ulong)(*param_2 >> 1);
  }
  FUN_004b3868(param_1,(uVar2 >> 1) + 1);
  uVar2 = _ZN5Botan10hex_decodeEPhPKcmb(*param_1,pbVar1,uVar2,param_3);
  uVar3 = param_1[1] - *param_1;
  if (uVar2 < uVar3 || uVar2 - uVar3 == 0) {
    if (uVar2 < uVar3) {
      param_1[1] = *param_1 + uVar2;
    }
  }
  else {
    FUN_0054084c(param_1,uVar2 - uVar3);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ccabc"></a> `004ccabc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-004ccac0"></a> `004ccac0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ccac4"></a> `004ccac4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ccac8"></a> `004ccac8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004ccacc"></a> `004ccacc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004ccad0"></a> `004ccad0` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-004ccad4"></a> `004ccad4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-004ccad8"></a> `004ccad8` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004ccadc"></a> `004ccadc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004ccae0"></a> `004ccae0` | `09 a0 40 a9` | ldp x9,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004ccae4"></a> `004ccae4` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004ccae8"></a> `004ccae8` | `16 15 80 9a` | csinc x22,x8,x0,ne | `FALL_THROUGH`
<a id="insn-004ccaec"></a> `004ccaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ccaf0"></a> `004ccaf0` | `a9 fe 41 d3` | lsr x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-004ccaf4"></a> `004ccaf4` | `21 05 00 91` | add x1,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004ccaf8"></a> `004ccaf8` | `5c 9b ff 97` | bl 0x004b3868 | `UNCONDITIONAL_CALL`
<a id="insn-004ccafc"></a> `004ccafc` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-004ccb00"></a> `004ccb00` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004ccb04"></a> `004ccb04` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004ccb08"></a> `004ccb08` | `e3 03 14 2a` | mov w3,w20 | `FALL_THROUGH`
<a id="insn-004ccb0c"></a> `004ccb0c` | `1d 34 1e 94` | bl 0x00c59b80 | `UNCONDITIONAL_CALL`
<a id="insn-004ccb10"></a> `004ccb10` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-004ccb14"></a> `004ccb14` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004ccb18"></a> `004ccb18` | `01 00 09 eb` | subs x1,x0,x9 | `FALL_THROUGH`
<a id="insn-004ccb1c"></a> `004ccb1c` | `89 00 00 54` | b.ls 0x004ccb2c | `CONDITIONAL_JUMP`
<a id="insn-004ccb20"></a> `004ccb20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004ccb24"></a> `004ccb24` | `4a cf 01 94` | bl 0x0054084c | `UNCONDITIONAL_CALL`
<a id="insn-004ccb28"></a> `004ccb28` | `04 00 00 14` | b 0x004ccb38 | `UNCONDITIONAL_JUMP`
<a id="insn-004ccb2c"></a> `004ccb2c` | `62 00 00 54` | b.cs 0x004ccb38 | `CONDITIONAL_JUMP`
<a id="insn-004ccb30"></a> `004ccb30` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-004ccb34"></a> `004ccb34` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004ccb38"></a> `004ccb38` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ccb3c"></a> `004ccb3c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004ccb40"></a> `004ccb40` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-004ccb44"></a> `004ccb44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ccabc`](#insn-004ccabc) 範囲 `[['004ccabc', '004ccb1f']]`
  - `CONDITIONAL_JUMP` [`004ccb1c`](#insn-004ccb1c) → [`004ccb2c`](#insn-004ccb2c)
  - `FALL_THROUGH` [`004ccb1c`](#insn-004ccb1c) → [`004ccb20`](#insn-004ccb20)
- ブロック [`004ccb20`](#insn-004ccb20) 範囲 `[['004ccb20', '004ccb2b']]`
  - `UNCONDITIONAL_JUMP` [`004ccb28`](#insn-004ccb28) → [`004ccb38`](#insn-004ccb38)
- ブロック [`004ccb2c`](#insn-004ccb2c) 範囲 `[['004ccb2c', '004ccb2f']]`
  - `CONDITIONAL_JUMP` [`004ccb2c`](#insn-004ccb2c) → [`004ccb38`](#insn-004ccb38)
  - `FALL_THROUGH` [`004ccb2c`](#insn-004ccb2c) → [`004ccb30`](#insn-004ccb30)
- ブロック [`004ccb30`](#insn-004ccb30) 範囲 `[['004ccb30', '004ccb37']]`
  - `FALL_THROUGH` [`004ccb34`](#insn-004ccb34) → [`004ccb38`](#insn-004ccb38)
- ブロック [`004ccb38`](#insn-004ccb38) 範囲 `[['004ccb38', '004ccb47']]`

## 命令位置別の参照

- [`004ccabc`](#insn-004ccabc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccac0`](#insn-004ccac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccac4`](#insn-004ccac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccaf8`](#insn-004ccaf8) → [`004b3868`](../004b3/004b3868.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004b3868` · 推定シンボル `None` · 推定型 `None`
- [`004ccb0c`](#insn-004ccb0c) → [`00c59b80`](../00c59/00c59b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59b80` · 推定シンボル `None` · 推定型 `None`
- [`004ccb1c`](#insn-004ccb1c) → [`004ccb2c`](#insn-004ccb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccb24`](#insn-004ccb24) → [`0054084c`](../00540/0054084c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054084c` · 推定シンボル `None` · 推定型 `None`
- [`004ccb28`](#insn-004ccb28) → [`004ccb38`](#insn-004ccb38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccb2c`](#insn-004ccb2c) → [`004ccb38`](#insn-004ccb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccb38`](#insn-004ccb38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccb3c`](#insn-004ccb3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ccb40`](#insn-004ccb40) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ccabc`](#insn-004ccabc)

~~~json
{
  "source": "004ccabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccac0`](#insn-004ccac0)

~~~json
{
  "source": "004ccac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccac4`](#insn-004ccac4)

~~~json
{
  "source": "004ccac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccaf8`](#insn-004ccaf8)

~~~json
{
  "source": "004ccaf8",
  "target": "004b3868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccb0c`](#insn-004ccb0c)

~~~json
{
  "source": "004ccb0c",
  "target": "00c59b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccb1c`](#insn-004ccb1c)

~~~json
{
  "source": "004ccb1c",
  "target": "004ccb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccb24`](#insn-004ccb24)

~~~json
{
  "source": "004ccb24",
  "target": "0054084c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ccb28`](#insn-004ccb28)

~~~json
{
  "source": "004ccb28",
  "target": "004ccb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccb2c`](#insn-004ccb2c)

~~~json
{
  "source": "004ccb2c",
  "target": "004ccb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccb38`](#insn-004ccb38)

~~~json
{
  "source": "004ccb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccb3c`](#insn-004ccb3c)

~~~json
{
  "source": "004ccb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ccb40`](#insn-004ccb40)

~~~json
{
  "source": "004ccb40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
