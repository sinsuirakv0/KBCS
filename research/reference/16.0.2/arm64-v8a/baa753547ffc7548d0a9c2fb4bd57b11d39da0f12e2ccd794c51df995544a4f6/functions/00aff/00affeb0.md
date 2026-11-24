# 00affeb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00affe14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00affe14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-f77157a3516c9806a445a13bea650420)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b00ea4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b00/00b00ea4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-5e137b60cbff1460c75408293891062f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affeb0",
  "name": "FUN_00affeb0",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87",
  "source_text_sha256": "8870f9559e2bc8678b18a241c8f8f44f364f0e236e1bcffc5fcedf2363682e87",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affeb0",
        "00afff77"
      ]
    ],
    "bytes_sha256": "56818a6e5ba6fe52923787566a2ab2c5de28abc8025b225549ad0b2c65b236a0",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)
- [00afeb84](../00afe/00afeb84.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 857 bytes

~~~c

int FUN_00affeb0(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_00851550();
  uVar4 = FUN_005e7460(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
                    /* try { // try from 00affef0 to 00bfff0b has its CatchHandler @ 00afff2c */
  if ((uVar4 & 1) == 0) {
    iVar1 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x1808);
                    /* try { // try from 00afff0c to 00bfff3f has its CatchHandler @ 00affea8 */
  }
  else {
                    /* catch() { ... } // from try @ 00affef0 with catch @ 00afff2c */
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e0);
    iVar2 = FUN_00afeb84(param_1,param_2,param_3,0x3d,0);
    iVar1 = ((100 - iVar2) * iVar1) / 100;
  }
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affeb0"></a> `00affeb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affeb4"></a> `00affeb4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affeb8"></a> `00affeb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affebc"></a> `00affebc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00affec0"></a> `00affec0` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00affec4"></a> `00affec4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00affec8"></a> `00affec8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affecc"></a> `00affecc` | `a1 45 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00affed0"></a> `00affed0` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00affed4"></a> `00affed4` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00affed8"></a> `00affed8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00affedc"></a> `00affedc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00affee0"></a> `00affee0` | `60 9d eb 97` | bl 0x005e7460 | `UNCONDITIONAL_CALL`
<a id="insn-00affee4"></a> `00affee4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00affee8"></a> `00affee8` | `9a 45 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00affeec"></a> `00affeec` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00affef0"></a> `00affef0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00affef4"></a> `00affef4` | `f6 00 00 37` | tbnz w22,#0x0,0x00afff10 | `CONDITIONAL_JUMP`
<a id="insn-00affef8"></a> `00affef8` | `89 38 80 52` | mov w9,#0x1c4 | `FALL_THROUGH`
<a id="insn-00affefc"></a> `00affefc` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00afff00"></a> `00afff00` | `09 54 9a 52` | mov w9,#0xd2a0 | `FALL_THROUGH`
<a id="insn-00afff04"></a> `00afff04` | `69 04 a0 72` | movk w9,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-00afff08"></a> `00afff08` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afff0c"></a> `00afff0c` | `17 00 00 14` | b 0x00afff68 | `UNCONDITIONAL_JUMP`
<a id="insn-00afff10"></a> `00afff10` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00afff14"></a> `00afff14` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00afff18"></a> `00afff18` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00afff1c"></a> `00afff1c` | `08 01 09 9b` | madd x8,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00afff20"></a> `00afff20` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00afff24"></a> `00afff24` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00afff28"></a> `00afff28` | `a3 07 80 52` | mov w3,#0x3d | `FALL_THROUGH`
<a id="insn-00afff2c"></a> `00afff2c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00afff30"></a> `00afff30` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afff34"></a> `00afff34` | `09 dc 9e 52` | mov w9,#0xf6e0 | `FALL_THROUGH`
<a id="insn-00afff38"></a> `00afff38` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00afff3c"></a> `00afff3c` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afff40"></a> `00afff40` | `11 fb ff 97` | bl 0x00afeb84 | `UNCONDITIONAL_CALL`
<a id="insn-00afff44"></a> `00afff44` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00afff48"></a> `00afff48` | `e9 a3 90 52` | mov w9,#0x851f | `FALL_THROUGH`
<a id="insn-00afff4c"></a> `00afff4c` | `08 01 00 4b` | sub w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00afff50"></a> `00afff50` | `69 3d aa 72` | movk w9,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00afff54"></a> `00afff54` | `08 7d 16 1b` | mul w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00afff58"></a> `00afff58` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-00afff5c"></a> `00afff5c` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00afff60"></a> `00afff60` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00afff64"></a> `00afff64` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00afff68"></a> `00afff68` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afff6c"></a> `00afff6c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afff70"></a> `00afff70` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afff74"></a> `00afff74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affeb0`](#insn-00affeb0) 範囲 `[['00affeb0', '00affeef']]`
  - `FALL_THROUGH` [`00affeec`](#insn-00affeec) → [`00affef0`](#insn-00affef0)
- ブロック [`00affef0`](#insn-00affef0) 範囲 `[['00affef0', '00affef7']]`
  - `CONDITIONAL_JUMP` [`00affef4`](#insn-00affef4) → [`00afff10`](#insn-00afff10)
  - `FALL_THROUGH` [`00affef4`](#insn-00affef4) → [`00affef8`](#insn-00affef8)
- ブロック [`00affef8`](#insn-00affef8) 範囲 `[['00affef8', '00afff0b']]`
  - `FALL_THROUGH` [`00afff08`](#insn-00afff08) → [`00afff0c`](#insn-00afff0c)
- ブロック [`00afff0c`](#insn-00afff0c) 範囲 `[['00afff0c', '00afff0f']]`
  - `UNCONDITIONAL_JUMP` [`00afff0c`](#insn-00afff0c) → [`00afff68`](#insn-00afff68)
- ブロック [`00afff10`](#insn-00afff10) 範囲 `[['00afff10', '00afff2b']]`
  - `FALL_THROUGH` [`00afff28`](#insn-00afff28) → [`00afff2c`](#insn-00afff2c)
- ブロック [`00afff2c`](#insn-00afff2c) 範囲 `[['00afff2c', '00afff67']]`
  - `FALL_THROUGH` [`00afff64`](#insn-00afff64) → [`00afff68`](#insn-00afff68)
- ブロック [`00afff68`](#insn-00afff68) 範囲 `[['00afff68', '00afff77']]`

## 命令位置別の参照

- [`00affeb0`](#insn-00affeb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeb4`](#insn-00affeb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affeb8`](#insn-00affeb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affecc`](#insn-00affecc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00affee0`](#insn-00affee0) → [`005e7460`](../005e7/005e7460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7460` · 推定シンボル `None` · 推定型 `None`
- [`00affee8`](#insn-00affee8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00affef4`](#insn-00affef4) → [`00afff10`](#insn-00afff10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff08`](#insn-00afff08) → `0023d2a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afff0c`](#insn-00afff0c) → [`00afff68`](#insn-00afff68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff40`](#insn-00afff40) → [`00afeb84`](../00afe/00afeb84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afeb84` · 推定シンボル `None` · 推定型 `None`
- [`00afff68`](#insn-00afff68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff6c`](#insn-00afff6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afff70`](#insn-00afff70) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affeb0`](#insn-00affeb0)

~~~json
{
  "source": "00affeb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeb4`](#insn-00affeb4)

~~~json
{
  "source": "00affeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affeb8`](#insn-00affeb8)

~~~json
{
  "source": "00affeb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affecc`](#insn-00affecc)

~~~json
{
  "source": "00affecc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affee0`](#insn-00affee0)

~~~json
{
  "source": "00affee0",
  "target": "005e7460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affee8`](#insn-00affee8)

~~~json
{
  "source": "00affee8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affef4`](#insn-00affef4)

~~~json
{
  "source": "00affef4",
  "target": "00afff10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff08`](#insn-00afff08)

~~~json
{
  "source": "00afff08",
  "target": "0023d2a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6152,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "a0bfb9000000000002040000010000000000000000000000a8bfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afff0c`](#insn-00afff0c)

~~~json
{
  "source": "00afff0c",
  "target": "00afff68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff40`](#insn-00afff40)

~~~json
{
  "source": "00afff40",
  "target": "00afeb84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afff68`](#insn-00afff68)

~~~json
{
  "source": "00afff68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff6c`](#insn-00afff6c)

~~~json
{
  "source": "00afff6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afff70`](#insn-00afff70)

~~~json
{
  "source": "00afff70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
