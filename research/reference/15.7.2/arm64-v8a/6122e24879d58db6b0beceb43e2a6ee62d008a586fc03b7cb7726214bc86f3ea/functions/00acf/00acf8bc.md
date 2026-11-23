# 00acf8bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acf984`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf984.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-be53069dca3df9c7d5c13f1acd58ebff)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acf8bc",
  "name": "FUN_00acf8bc",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8648ba9c326fdce1cb23084ef27d4207841bcea0f95ba1d3b536e44f299c902e",
  "source_text_sha256": "8648ba9c326fdce1cb23084ef27d4207841bcea0f95ba1d3b536e44f299c902e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acf8bc",
        "00acf93f"
      ]
    ],
    "bytes_sha256": "d181d669633dbb6907605e866a97fabf6ee35b2d3e802a0f6b44028458fb1acc",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0072f020](../0072f/0072f020.md)
- [00957f9c](../00957/00957f9c.md)
- [00960f9c](../00960/00960f9c.md)
- [009a9ce0](../009a9/009a9ce0.md)

## 呼び出し先

- [00adbf54](../00adb/00adbf54.md)
- [00adbf88](../00adb/00adbf88.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 576 bytes

~~~c

void FUN_00acf8bc(undefined8 param_1,int param_2)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  undefined8 uVar4;
  
  uVar4 = FUN_00adbf88();
  uVar1 = 50000;
  if ((uint)uVar4 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar4 >> 0x10) & 0xffff;
  }
  uVar1 = uVar1 + param_2;
  uVar3 = FUN_00adbf88(param_1);
  uVar3 = uVar3 & 0xffff;
  if (49999 < uVar3) {
    uVar3 = 50000;
  }
  uVar2 = 0xc3500000;
  if ((int)uVar1 < 0xc351) {
    uVar2 = (uVar1 & ((int)uVar1 >> 0x1f ^ 0xffffffffU)) << 0x10;
  }
  FUN_00adbf54(param_1,uVar2 | uVar3);
  DAT_00c23eb4 = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acf8bc"></a> `00acf8bc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acf8c0"></a> `00acf8c0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf8c4"></a> `00acf8c4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf8c8"></a> `00acf8c8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acf8cc"></a> `00acf8cc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acf8d0"></a> `00acf8d0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acf8d4"></a> `00acf8d4` | `ad 31 00 94` | bl 0x00adbf88 | `UNCONDITIONAL_CALL`
<a id="insn-00acf8d8"></a> `00acf8d8` | `e8 95 a7 12` | mov w8,#0xc350ffff | `FALL_THROUGH`
<a id="insn-00acf8dc"></a> `00acf8dc` | `09 7c 10 53` | lsr w9,w0,#0x10 | `FALL_THROUGH`
<a id="insn-00acf8e0"></a> `00acf8e0` | `15 6a 98 52` | mov w21,#0xc350 | `FALL_THROUGH`
<a id="insn-00acf8e4"></a> `00acf8e4` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00acf8e8"></a> `00acf8e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acf8ec"></a> `00acf8ec` | `a8 82 89 1a` | csel w8,w21,w9,hi | `FALL_THROUGH`
<a id="insn-00acf8f0"></a> `00acf8f0` | `13 01 13 0b` | add w19,w8,w19 | `FALL_THROUGH`
<a id="insn-00acf8f4"></a> `00acf8f4` | `a5 31 00 94` | bl 0x00adbf88 | `UNCONDITIONAL_CALL`
<a id="insn-00acf8f8"></a> `00acf8f8` | `68 7e b3 0a` | bic w8,w19,w19, ASR #0x1f | `FALL_THROUGH`
<a id="insn-00acf8fc"></a> `00acf8fc` | `09 3c 00 12` | and w9,w0,#0xffff | `FALL_THROUGH`
<a id="insn-00acf900"></a> `00acf900` | `0a 6a b8 52` | mov w10,#0xc3500000 | `FALL_THROUGH`
<a id="insn-00acf904"></a> `00acf904` | `3f 01 15 6b` | cmp w9,w21 | `FALL_THROUGH`
<a id="insn-00acf908"></a> `00acf908` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acf90c"></a> `00acf90c` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00acf910"></a> `00acf910` | `29 31 95 1a` | csel w9,w9,w21,cc | `FALL_THROUGH`
<a id="insn-00acf914"></a> `00acf914` | `7f 02 15 6b` | cmp w19,w21 | `FALL_THROUGH`
<a id="insn-00acf918"></a> `00acf918` | `48 c1 88 1a` | csel w8,w10,w8,gt | `FALL_THROUGH`
<a id="insn-00acf91c"></a> `00acf91c` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00acf920"></a> `00acf920` | `8d 31 00 94` | bl 0x00adbf54 | `UNCONDITIONAL_CALL`
<a id="insn-00acf924"></a> `00acf924` | `a8 0a 00 90` | adrp x8,0xc23000 | `FALL_THROUGH`
<a id="insn-00acf928"></a> `00acf928` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acf92c"></a> `00acf92c` | `09 d1 3a 39` | strb w9,[x8, #0xeb4] | `FALL_THROUGH`
<a id="insn-00acf930"></a> `00acf930` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf934"></a> `00acf934` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf938"></a> `00acf938` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acf93c"></a> `00acf93c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acf8bc`](#insn-00acf8bc) 範囲 `[['00acf8bc', '00acf93f']]`

## 命令位置別の参照

- [`00acf8bc`](#insn-00acf8bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf8c0`](#insn-00acf8c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf8c4`](#insn-00acf8c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf8d4`](#insn-00acf8d4) → [`00adbf88`](../00adb/00adbf88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adbf88` · 推定シンボル `None` · 推定型 `None`
- [`00acf8f4`](#insn-00acf8f4) → [`00adbf88`](../00adb/00adbf88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adbf88` · 推定シンボル `None` · 推定型 `None`
- [`00acf920`](#insn-00acf920) → [`00adbf54`](../00adb/00adbf54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adbf54` · 推定シンボル `None` · 推定型 `None`
- [`00acf92c`](#insn-00acf92c) → `00c23eb4`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf930`](#insn-00acf930) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf934`](#insn-00acf934) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf938`](#insn-00acf938) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acf8bc`](#insn-00acf8bc)

~~~json
{
  "source": "00acf8bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf8c0`](#insn-00acf8c0)

~~~json
{
  "source": "00acf8c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf8c4`](#insn-00acf8c4)

~~~json
{
  "source": "00acf8c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf8d4`](#insn-00acf8d4)

~~~json
{
  "source": "00acf8d4",
  "target": "00adbf88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf8f4`](#insn-00acf8f4)

~~~json
{
  "source": "00acf8f4",
  "target": "00adbf88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf920`](#insn-00acf920)

~~~json
{
  "source": "00acf920",
  "target": "00adbf54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf92c`](#insn-00acf92c)

~~~json
{
  "source": "00acf92c",
  "target": "00c23eb4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c23eb4",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf930`](#insn-00acf930)

~~~json
{
  "source": "00acf930",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf934`](#insn-00acf934)

~~~json
{
  "source": "00acf934",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf938`](#insn-00acf938)

~~~json
{
  "source": "00acf938",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
