# 00bfd1ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfc1f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc1f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-b9b90f8b13937303981666c31fd8b449)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfd1ec",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4b68eee8f3c74fc533c83aa741097ea1b752e6b6fc9d5593330ebdd7be7987cb",
  "source_text_sha256": "4b68eee8f3c74fc533c83aa741097ea1b752e6b6fc9d5593330ebdd7be7987cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfd1ec",
        "00bfd257"
      ]
    ],
    "bytes_sha256": "75685915e715780b399019af992fe9321b5f1ce634eb4c08facdfff745a307b7",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5f3c0](../00c5f/00c5f3c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 791 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4swapERS3_(long *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  long lVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined8 uVar6;
  
  lVar1 = *param_2;
  lVar2 = *param_1;
  lVar3 = param_1[1];
  param_1[1] = param_2[1];
  param_2[1] = lVar3;
  lVar2 = (long)param_1 + *(long *)(lVar2 + -0x18);
  lVar1 = (long)param_2 + *(long *)(lVar1 + -0x18);
  _ZNSt6__ndk18ios_base4swapERS0_(lVar2,lVar1);
  uVar6 = *(undefined8 *)(lVar2 + 0x88);
  uVar4 = *(undefined4 *)(lVar1 + 0x90);
  *(undefined8 *)(lVar2 + 0x88) = *(undefined8 *)(lVar1 + 0x88);
  uVar5 = *(undefined4 *)(lVar2 + 0x90);
  *(undefined8 *)(lVar1 + 0x88) = uVar6;
  *(undefined4 *)(lVar2 + 0x90) = uVar4;
  *(undefined4 *)(lVar1 + 0x90) = uVar5;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfd1ec"></a> `00bfd1ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfd1f0"></a> `00bfd1f0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfd1f4"></a> `00bfd1f4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd1f8"></a> `00bfd1f8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfd1fc"></a> `00bfd1fc` | `2b 20 40 a9` | ldp x11,x8,[x1] | `FALL_THROUGH`
<a id="insn-00bfd200"></a> `00bfd200` | `0a 24 40 a9` | ldp x10,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfd204"></a> `00bfd204` | `08 04 00 f9` | str x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd208"></a> `00bfd208` | `29 04 00 f9` | str x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd20c"></a> `00bfd20c` | `48 81 5e f8` | ldur x8,[x10, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd210"></a> `00bfd210` | `69 81 5e f8` | ldur x9,[x11, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd214"></a> `00bfd214` | `13 00 08 8b` | add x19,x0,x8 | `FALL_THROUGH`
<a id="insn-00bfd218"></a> `00bfd218` | `34 00 09 8b` | add x20,x1,x9 | `FALL_THROUGH`
<a id="insn-00bfd21c"></a> `00bfd21c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfd220"></a> `00bfd220` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfd224"></a> `00bfd224` | `67 88 01 94` | bl 0x00c5f3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd228"></a> `00bfd228` | `88 46 40 f9` | ldr x8,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfd22c"></a> `00bfd22c` | `69 46 40 f9` | ldr x9,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfd230"></a> `00bfd230` | `8a 92 40 b9` | ldr w10,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfd234"></a> `00bfd234` | `68 46 00 f9` | str x8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfd238"></a> `00bfd238` | `68 92 40 b9` | ldr w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfd23c"></a> `00bfd23c` | `89 46 00 f9` | str x9,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfd240"></a> `00bfd240` | `6a 92 00 b9` | str w10,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfd244"></a> `00bfd244` | `88 92 00 b9` | str w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfd248"></a> `00bfd248` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd24c"></a> `00bfd24c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfd250"></a> `00bfd250` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfd254"></a> `00bfd254` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfd1ec`](#insn-00bfd1ec) 範囲 `[['00bfd1ec', '00bfd257']]`

## 命令位置別の参照

- [`00bfd1f0`](#insn-00bfd1f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd1f4`](#insn-00bfd1f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd224`](#insn-00bfd224) → [`00c5f3c0`](../00c5f/00c5f3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f3c0` · 推定シンボル `None` · 推定型 `None`
- [`00bfd248`](#insn-00bfd248) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd24c`](#insn-00bfd24c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfd1f0`](#insn-00bfd1f0)

~~~json
{
  "source": "00bfd1f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd1f4`](#insn-00bfd1f4)

~~~json
{
  "source": "00bfd1f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd224`](#insn-00bfd224)

~~~json
{
  "source": "00bfd224",
  "target": "00c5f3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd248`](#insn-00bfd248)

~~~json
{
  "source": "00bfd248",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd24c`](#insn-00bfd24c)

~~~json
{
  "source": "00bfd24c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
