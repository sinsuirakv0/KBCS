# 00bfffdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfff40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-97453beba79cd46d73fa30fd9425cf52)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00fd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00fd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0039.md#compare-2f1eee283ca7385b1486d096e60b5edd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfffdc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "351d37c3ec9ec468fa4b026c45dcd60a979d8f71016d0969542a756df55e5109",
  "source_text_sha256": "351d37c3ec9ec468fa4b026c45dcd60a979d8f71016d0969542a756df55e5109",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfffdc",
        "00c000af"
      ]
    ],
    "bytes_sha256": "dcc6ef69587466c532a8e67868cca804de7f3a193469f4c128d4854a9539ab48",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58010](../00c58/00c58010.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1164 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl
               (long *param_1,int *param_2,long param_3)

{
  long lVar1;
  int iVar2;
  void *__src;
  long lVar3;
  long lVar4;
  int *piVar5;
  
  if (param_3 < 1) {
    lVar4 = 0;
  }
  else {
    lVar4 = 0;
    do {
      __src = (void *)param_1[3];
      if (__src < (void *)param_1[4]) {
        lVar3 = param_1[4] - (long)__src >> 2;
        lVar1 = param_3 - lVar4;
        if (lVar3 <= param_3 - lVar4) {
          lVar1 = lVar3;
        }
        lVar3 = lVar1;
        if (0x7ffffffe < lVar1) {
          lVar3 = 0x7fffffff;
        }
        if (lVar1 != 0) {
          memmove(param_2,__src,lVar3 << 2);
          __src = (void *)param_1[3];
        }
        piVar5 = param_2 + lVar3;
        param_1[3] = (long)((long)__src + (long)(int)lVar3 * 4);
      }
      else {
        iVar2 = (**(code **)(*param_1 + 0x50))(param_1);
        if (iVar2 == -1) {
          return lVar4;
        }
        lVar3 = 1;
        piVar5 = param_2 + 1;
        *param_2 = iVar2;
      }
      lVar4 = lVar3 + lVar4;
      param_2 = piVar5;
    } while (lVar4 < param_3);
  }
  return lVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfffdc"></a> `00bfffdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfffe0"></a> `00bfffe0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfffe4"></a> `00bfffe4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfffe8"></a> `00bfffe8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfffec"></a> `00bfffec` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffff0"></a> `00bffff0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffff4"></a> `00bffff4` | `5f 04 00 f1` | cmp x2,#0x1 | `FALL_THROUGH`
<a id="insn-00bffff8"></a> `00bffff8` | `cb 04 00 54` | b.lt 0x00c00090 | `CONDITIONAL_JUMP`
<a id="insn-00bffffc"></a> `00bffffc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00c00000"></a> `00c00000` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00c00004"></a> `00c00004` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c00008"></a> `00c00008` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00c0000c"></a> `00c0000c` | `17 00 b0 12` | mov w23,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00c00010"></a> `00c00010` | `07 00 00 14` | b 0x00c0002c | `UNCONDITIONAL_JUMP`
<a id="insn-00c00014"></a> `00c00014` | `28 c8 38 8b` | add x8,x1,w24, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00c00018"></a> `00c00018` | `b5 0a 18 8b` | add x21,x21,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c0001c"></a> `00c0001c` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c00020"></a> `00c00020` | `14 03 14 8b` | add x20,x24,x20 | `FALL_THROUGH`
<a id="insn-00c00024"></a> `00c00024` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00c00028"></a> `00c00028` | `6a 03 00 54` | b.ge 0x00c00094 | `CONDITIONAL_JUMP`
<a id="insn-00c0002c"></a> `00c0002c` | `c1 a2 41 a9` | ldp x1,x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c00030"></a> `00c00030` | `3f 00 08 eb` | cmp x1,x8 | `FALL_THROUGH`
<a id="insn-00c00034"></a> `00c00034` | `c2 01 00 54` | b.cs 0x00c0006c | `CONDITIONAL_JUMP`
<a id="insn-00c00038"></a> `00c00038` | `08 01 01 cb` | sub x8,x8,x1 | `FALL_THROUGH`
<a id="insn-00c0003c"></a> `00c0003c` | `69 02 14 cb` | sub x9,x19,x20 | `FALL_THROUGH`
<a id="insn-00c00040"></a> `00c00040` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c00044"></a> `00c00044` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c00048"></a> `00c00048` | `28 b1 88 9a` | csel x8,x9,x8,lt | `FALL_THROUGH`
<a id="insn-00c0004c"></a> `00c0004c` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00c00050"></a> `00c00050` | `18 b1 97 9a` | csel x24,x8,x23,lt | `FALL_THROUGH`
<a id="insn-00c00054"></a> `00c00054` | `08 fe ff b4` | cbz x8,0x00c00014 | `CONDITIONAL_JUMP`
<a id="insn-00c00058"></a> `00c00058` | `02 f7 7e d3` | lsl x2,x24,#0x2 | `FALL_THROUGH`
<a id="insn-00c0005c"></a> `00c0005c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c00060"></a> `00c00060` | `ec 5f 01 94` | bl 0x00c58010 | `UNCONDITIONAL_CALL`
<a id="insn-00c00064"></a> `00c00064` | `c1 0e 40 f9` | ldr x1,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c00068"></a> `00c00068` | `eb ff ff 17` | b 0x00c00014 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0006c"></a> `00c0006c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00c00070"></a> `00c00070` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00c00074"></a> `00c00074` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00c00078"></a> `00c00078` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0007c"></a> `00c0007c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c00080"></a> `00c00080` | `a0 00 00 54` | b.eq 0x00c00094 | `CONDITIONAL_JUMP`
<a id="insn-00c00084"></a> `00c00084` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00c00088"></a> `00c00088` | `a0 46 00 b8` | str w0,[x21], #0x4 | `FALL_THROUGH`
<a id="insn-00c0008c"></a> `00c0008c` | `e5 ff ff 17` | b 0x00c00020 | `UNCONDITIONAL_JUMP`
<a id="insn-00c00090"></a> `00c00090` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00c00094"></a> `00c00094` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c00098"></a> `00c00098` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c0009c"></a> `00c0009c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c000a0"></a> `00c000a0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c000a4"></a> `00c000a4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00c000a8"></a> `00c000a8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c000ac"></a> `00c000ac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfffdc`](#insn-00bfffdc) 範囲 `[['00bfffdc', '00bffffb']]`
  - `CONDITIONAL_JUMP` [`00bffff8`](#insn-00bffff8) → [`00c00090`](#insn-00c00090)
  - `FALL_THROUGH` [`00bffff8`](#insn-00bffff8) → [`00bffffc`](#insn-00bffffc)
- ブロック [`00bffffc`](#insn-00bffffc) 範囲 `[['00bffffc', '00c00013']]`
  - `UNCONDITIONAL_JUMP` [`00c00010`](#insn-00c00010) → [`00c0002c`](#insn-00c0002c)
- ブロック [`00c00014`](#insn-00c00014) 範囲 `[['00c00014', '00c0001f']]`
  - `FALL_THROUGH` [`00c0001c`](#insn-00c0001c) → [`00c00020`](#insn-00c00020)
- ブロック [`00c00020`](#insn-00c00020) 範囲 `[['00c00020', '00c0002b']]`
  - `CONDITIONAL_JUMP` [`00c00028`](#insn-00c00028) → [`00c00094`](#insn-00c00094)
  - `FALL_THROUGH` [`00c00028`](#insn-00c00028) → [`00c0002c`](#insn-00c0002c)
- ブロック [`00c0002c`](#insn-00c0002c) 範囲 `[['00c0002c', '00c00037']]`
  - `CONDITIONAL_JUMP` [`00c00034`](#insn-00c00034) → [`00c0006c`](#insn-00c0006c)
  - `FALL_THROUGH` [`00c00034`](#insn-00c00034) → [`00c00038`](#insn-00c00038)
- ブロック [`00c00038`](#insn-00c00038) 範囲 `[['00c00038', '00c00057']]`
  - `CONDITIONAL_JUMP` [`00c00054`](#insn-00c00054) → [`00c00014`](#insn-00c00014)
  - `FALL_THROUGH` [`00c00054`](#insn-00c00054) → [`00c00058`](#insn-00c00058)
- ブロック [`00c00058`](#insn-00c00058) 範囲 `[['00c00058', '00c0006b']]`
  - `UNCONDITIONAL_JUMP` [`00c00068`](#insn-00c00068) → [`00c00014`](#insn-00c00014)
- ブロック [`00c0006c`](#insn-00c0006c) 範囲 `[['00c0006c', '00c00083']]`
  - `CONDITIONAL_JUMP` [`00c00080`](#insn-00c00080) → [`00c00094`](#insn-00c00094)
  - `FALL_THROUGH` [`00c00080`](#insn-00c00080) → [`00c00084`](#insn-00c00084)
- ブロック [`00c00084`](#insn-00c00084) 範囲 `[['00c00084', '00c0008f']]`
  - `UNCONDITIONAL_JUMP` [`00c0008c`](#insn-00c0008c) → [`00c00020`](#insn-00c00020)
- ブロック [`00c00090`](#insn-00c00090) 範囲 `[['00c00090', '00c00093']]`
  - `FALL_THROUGH` [`00c00090`](#insn-00c00090) → [`00c00094`](#insn-00c00094)
- ブロック [`00c00094`](#insn-00c00094) 範囲 `[['00c00094', '00c000af']]`

## 命令位置別の参照

- [`00bfffe0`](#insn-00bfffe0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffe4`](#insn-00bfffe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffe8`](#insn-00bfffe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffec`](#insn-00bfffec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffff8`](#insn-00bffff8) → [`00c00090`](#insn-00c00090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00010`](#insn-00c00010) → [`00c0002c`](#insn-00c0002c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00028`](#insn-00c00028) → [`00c00094`](#insn-00c00094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00034`](#insn-00c00034) → [`00c0006c`](#insn-00c0006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00054`](#insn-00c00054) → [`00c00014`](#insn-00c00014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00060`](#insn-00c00060) → [`00c58010`](../00c58/00c58010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58010` · 推定シンボル `None` · 推定型 `None`
- [`00c00068`](#insn-00c00068) → [`00c00014`](#insn-00c00014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00080`](#insn-00c00080) → [`00c00094`](#insn-00c00094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0008c`](#insn-00c0008c) → [`00c00020`](#insn-00c00020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00098`](#insn-00c00098) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0009c`](#insn-00c0009c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000a0`](#insn-00c000a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000a4`](#insn-00c000a4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfffe0`](#insn-00bfffe0)

~~~json
{
  "source": "00bfffe0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffe4`](#insn-00bfffe4)

~~~json
{
  "source": "00bfffe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffe8`](#insn-00bfffe8)

~~~json
{
  "source": "00bfffe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffec`](#insn-00bfffec)

~~~json
{
  "source": "00bfffec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffff8`](#insn-00bffff8)

~~~json
{
  "source": "00bffff8",
  "target": "00c00090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00010`](#insn-00c00010)

~~~json
{
  "source": "00c00010",
  "target": "00c0002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00028`](#insn-00c00028)

~~~json
{
  "source": "00c00028",
  "target": "00c00094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00034`](#insn-00c00034)

~~~json
{
  "source": "00c00034",
  "target": "00c0006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00054`](#insn-00c00054)

~~~json
{
  "source": "00c00054",
  "target": "00c00014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00060`](#insn-00c00060)

~~~json
{
  "source": "00c00060",
  "target": "00c58010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c00068`](#insn-00c00068)

~~~json
{
  "source": "00c00068",
  "target": "00c00014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00080`](#insn-00c00080)

~~~json
{
  "source": "00c00080",
  "target": "00c00094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0008c`](#insn-00c0008c)

~~~json
{
  "source": "00c0008c",
  "target": "00c00020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00098`](#insn-00c00098)

~~~json
{
  "source": "00c00098",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0009c`](#insn-00c0009c)

~~~json
{
  "source": "00c0009c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000a0`](#insn-00c000a0)

~~~json
{
  "source": "00c000a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000a4`](#insn-00c000a4)

~~~json
{
  "source": "00c000a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
