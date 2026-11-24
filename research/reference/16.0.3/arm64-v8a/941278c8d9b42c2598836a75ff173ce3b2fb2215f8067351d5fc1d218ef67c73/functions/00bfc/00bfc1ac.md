# 00bfc1ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfb1b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb1b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-ad3bfcaa7a22840ede6674ff5e4236c7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfc1ac",
  "name": "_ZNSt6__ndk18ios_base5iwordEi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33f2d0f183873c5a5deaa58d13deb82383a36ad6c632f98e4105f1b526678d31",
  "source_text_sha256": "33f2d0f183873c5a5deaa58d13deb82383a36ad6c632f98e4105f1b526678d31",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfc1ac",
        "00bfc2bf"
      ]
    ],
    "bytes_sha256": "abe64104fbe46ae5d2841c4ebfe2b87c87e3d6dc5c45bf341163e59860e8f7e9",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bfc5d4](../00bfc/00bfc5d4.md)
- [00c59130](../00c59/00c59130.md)
- [00c5b140](../00c5b/00c5b140.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1570 bytes

~~~c

undefined8 * _ZNSt6__ndk18ios_base5iwordEi(long param_1,int param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  void *__s;
  uint uVar4;
  void *pvVar5;
  ulong uVar6;
  ulong uVar7;
  
  uVar1 = (long)param_2 + 1;
  if (*(ulong *)(param_1 + 0x68) < uVar1) {
    uVar6 = *(ulong *)(param_1 + 0x68) * 2;
    if (uVar6 < uVar1 || uVar6 - uVar1 == 0) {
      uVar6 = uVar1;
    }
    if (0xffffffffffffffe < uVar1) {
      uVar6 = 0x1fffffffffffffff;
    }
    pvVar5 = realloc(*(void **)(param_1 + 0x58),uVar6 * 8);
    if (pvVar5 == (void *)0x0) {
      uVar4 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar4;
      if ((*(uint *)(param_1 + 0x24) & uVar4) == 0) {
        DAT_01128460 = 0;
        return &DAT_01128460;
      }
                    /* WARNING: Subroutine does not return */
      FUN_00bfc5d4("ios_base::clear");
    }
    uVar7 = *(ulong *)(param_1 + 0x60);
    *(void **)(param_1 + 0x58) = pvVar5;
    if ((long)uVar7 < (long)uVar6) {
      pvVar3 = (void *)(uVar6 * 8 + (long)pvVar5);
      __s = (void *)((long)pvVar5 + uVar7 * 8);
      pvVar2 = (void *)((long)__s + 8);
      if (pvVar2 <= pvVar3) {
        pvVar2 = pvVar3;
      }
      memset(__s,0,((long)pvVar2 + uVar7 * -8 + ~(ulong)pvVar5 & 0xfffffffffffffff8) + 8);
    }
    *(ulong *)(param_1 + 0x68) = uVar6;
  }
  else {
    pvVar5 = *(void **)(param_1 + 0x58);
    uVar7 = *(ulong *)(param_1 + 0x60);
  }
  if (uVar7 <= uVar1) {
    uVar7 = uVar1;
  }
  *(ulong *)(param_1 + 0x60) = uVar7;
  return (undefined8 *)((long)pvVar5 + (long)param_2 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfc1ac"></a> `00bfc1ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfc1b0"></a> `00bfc1b0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfc1b4"></a> `00bfc1b4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc1b8"></a> `00bfc1b8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc1bc"></a> `00bfc1bc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc1c0"></a> `00bfc1c0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfc1c4"></a> `00bfc1c4` | `35 7c 40 93` | sxtw x21,w1 | `FALL_THROUGH`
<a id="insn-00bfc1c8"></a> `00bfc1c8` | `08 34 40 f9` | ldr x8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00bfc1cc"></a> `00bfc1cc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfc1d0"></a> `00bfc1d0` | `b6 06 00 91` | add x22,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc1d4"></a> `00bfc1d4` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bfc1d8"></a> `00bfc1d8` | `69 04 00 54` | b.ls 0x00bfc264 | `CONDITIONAL_JUMP`
<a id="insn-00bfc1dc"></a> `00bfc1dc` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc1e0"></a> `00bfc1e0` | `09 00 fe 92` | mov x9,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfc1e4"></a> `00bfc1e4` | `60 2e 40 f9` | ldr x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfc1e8"></a> `00bfc1e8` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfc1ec"></a> `00bfc1ec` | `08 81 96 9a` | csel x8,x8,x22,hi | `FALL_THROUGH`
<a id="insn-00bfc1f0"></a> `00bfc1f0` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bfc1f4"></a> `00bfc1f4` | `09 00 fc 92` | mov x9,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfc1f8"></a> `00bfc1f8` | `17 31 89 9a` | csel x23,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bfc1fc"></a> `00bfc1fc` | `f4 f2 7d d3` | lsl x20,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00bfc200"></a> `00bfc200` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfc204"></a> `00bfc204` | `cf 7b 01 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc208"></a> `00bfc208` | `40 04 00 b4` | cbz x0,0x00bfc290 | `CONDITIONAL_JUMP`
<a id="insn-00bfc20c"></a> `00bfc20c` | `78 32 40 f9` | ldr x24,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bfc210"></a> `00bfc210` | `60 2e 00 f9` | str x0,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfc214"></a> `00bfc214` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bfc218"></a> `00bfc218` | `2a 02 00 54` | b.ge 0x00bfc25c | `CONDITIONAL_JUMP`
<a id="insn-00bfc21c"></a> `00bfc21c` | `09 f3 7d d3` | lsl x9,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00bfc220"></a> `00bfc220` | `8b 02 00 8b` | add x11,x20,x0 | `FALL_THROUGH`
<a id="insn-00bfc224"></a> `00bfc224` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfc228"></a> `00bfc228` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bfc22c"></a> `00bfc22c` | `08 00 09 8b` | add x8,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfc230"></a> `00bfc230` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc234"></a> `00bfc234` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bfc238"></a> `00bfc238` | `4a 81 8b 9a` | csel x10,x10,x11,hi | `FALL_THROUGH`
<a id="insn-00bfc23c"></a> `00bfc23c` | `eb 03 20 aa` | mvn x11,x0 | `FALL_THROUGH`
<a id="insn-00bfc240"></a> `00bfc240` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfc244"></a> `00bfc244` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bfc248"></a> `00bfc248` | `49 01 09 cb` | sub x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00bfc24c"></a> `00bfc24c` | `29 f1 7d 92` | and x9,x9,#-0x8 | `FALL_THROUGH`
<a id="insn-00bfc250"></a> `00bfc250` | `22 21 00 91` | add x2,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc254"></a> `00bfc254` | `b7 73 01 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc258"></a> `00bfc258` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfc25c"></a> `00bfc25c` | `77 36 00 f9` | str x23,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bfc260"></a> `00bfc260` | `02 00 00 14` | b 0x00bfc268 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc264"></a> `00bfc264` | `60 e2 45 a9` | ldp x0,x24,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bfc268"></a> `00bfc268` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bfc26c"></a> `00bfc26c` | `00 0c 15 8b` | add x0,x0,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfc270"></a> `00bfc270` | `08 83 96 9a` | csel x8,x24,x22,hi | `FALL_THROUGH`
<a id="insn-00bfc274"></a> `00bfc274` | `68 32 00 f9` | str x8,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bfc278"></a> `00bfc278` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc27c"></a> `00bfc27c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc280"></a> `00bfc280` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc284"></a> `00bfc284` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfc288"></a> `00bfc288` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfc28c"></a> `00bfc28c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfc290"></a> `00bfc290` | `68 26 44 29` | ldp w8,w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc294"></a> `00bfc294` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfc298"></a> `00bfc298` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfc29c"></a> `00bfc29c` | `68 22 00 b9` | str w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc2a0"></a> `00bfc2a0` | `a1 00 00 54` | b.ne 0x00bfc2b4 | `CONDITIONAL_JUMP`
<a id="insn-00bfc2a4"></a> `00bfc2a4` | `60 29 00 90` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfc2a8"></a> `00bfc2a8` | `00 80 11 91` | add x0,x0,#0x460 | `FALL_THROUGH`
<a id="insn-00bfc2ac"></a> `00bfc2ac` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfc2b0"></a> `00bfc2b0` | `f2 ff ff 17` | b 0x00bfc278 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc2b4"></a> `00bfc2b4` | `40 b5 ff f0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bfc2b8"></a> `00bfc2b8` | `00 c8 18 91` | add x0,x0,#0x632 | `FALL_THROUGH`
<a id="insn-00bfc2bc"></a> `00bfc2bc` | `c6 00 00 94` | bl 0x00bfc5d4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfc1ac`](#insn-00bfc1ac) 範囲 `[['00bfc1ac', '00bfc1db']]`
  - `CONDITIONAL_JUMP` [`00bfc1d8`](#insn-00bfc1d8) → [`00bfc264`](#insn-00bfc264)
  - `FALL_THROUGH` [`00bfc1d8`](#insn-00bfc1d8) → [`00bfc1dc`](#insn-00bfc1dc)
- ブロック [`00bfc1dc`](#insn-00bfc1dc) 範囲 `[['00bfc1dc', '00bfc20b']]`
  - `CONDITIONAL_JUMP` [`00bfc208`](#insn-00bfc208) → [`00bfc290`](#insn-00bfc290)
  - `FALL_THROUGH` [`00bfc208`](#insn-00bfc208) → [`00bfc20c`](#insn-00bfc20c)
- ブロック [`00bfc20c`](#insn-00bfc20c) 範囲 `[['00bfc20c', '00bfc21b']]`
  - `CONDITIONAL_JUMP` [`00bfc218`](#insn-00bfc218) → [`00bfc25c`](#insn-00bfc25c)
  - `FALL_THROUGH` [`00bfc218`](#insn-00bfc218) → [`00bfc21c`](#insn-00bfc21c)
- ブロック [`00bfc21c`](#insn-00bfc21c) 範囲 `[['00bfc21c', '00bfc25b']]`
  - `FALL_THROUGH` [`00bfc258`](#insn-00bfc258) → [`00bfc25c`](#insn-00bfc25c)
- ブロック [`00bfc25c`](#insn-00bfc25c) 範囲 `[['00bfc25c', '00bfc263']]`
  - `UNCONDITIONAL_JUMP` [`00bfc260`](#insn-00bfc260) → [`00bfc268`](#insn-00bfc268)
- ブロック [`00bfc264`](#insn-00bfc264) 範囲 `[['00bfc264', '00bfc267']]`
  - `FALL_THROUGH` [`00bfc264`](#insn-00bfc264) → [`00bfc268`](#insn-00bfc268)
- ブロック [`00bfc268`](#insn-00bfc268) 範囲 `[['00bfc268', '00bfc277']]`
  - `FALL_THROUGH` [`00bfc274`](#insn-00bfc274) → [`00bfc278`](#insn-00bfc278)
- ブロック [`00bfc278`](#insn-00bfc278) 範囲 `[['00bfc278', '00bfc28f']]`
- ブロック [`00bfc290`](#insn-00bfc290) 範囲 `[['00bfc290', '00bfc2a3']]`
  - `CONDITIONAL_JUMP` [`00bfc2a0`](#insn-00bfc2a0) → [`00bfc2b4`](#insn-00bfc2b4)
  - `FALL_THROUGH` [`00bfc2a0`](#insn-00bfc2a0) → [`00bfc2a4`](#insn-00bfc2a4)
- ブロック [`00bfc2a4`](#insn-00bfc2a4) 範囲 `[['00bfc2a4', '00bfc2b3']]`
  - `UNCONDITIONAL_JUMP` [`00bfc2b0`](#insn-00bfc2b0) → [`00bfc278`](#insn-00bfc278)
- ブロック [`00bfc2b4`](#insn-00bfc2b4) 範囲 `[['00bfc2b4', '00bfc2bf']]`

## 命令位置別の参照

- [`00bfc1b0`](#insn-00bfc1b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc1b4`](#insn-00bfc1b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc1b8`](#insn-00bfc1b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc1bc`](#insn-00bfc1bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc1d8`](#insn-00bfc1d8) → [`00bfc264`](#insn-00bfc264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc204`](#insn-00bfc204) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00bfc208`](#insn-00bfc208) → [`00bfc290`](#insn-00bfc290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc218`](#insn-00bfc218) → [`00bfc25c`](#insn-00bfc25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc254`](#insn-00bfc254) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`00bfc260`](#insn-00bfc260) → [`00bfc268`](#insn-00bfc268) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc278`](#insn-00bfc278) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc27c`](#insn-00bfc27c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc280`](#insn-00bfc280) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc284`](#insn-00bfc284) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc2a0`](#insn-00bfc2a0) → [`00bfc2b4`](#insn-00bfc2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc2a8`](#insn-00bfc2a8) → `01128460`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfc2ac`](#insn-00bfc2ac) → `01128460`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfc2b0`](#insn-00bfc2b0) → [`00bfc278`](#insn-00bfc278) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc2b8`](#insn-00bfc2b8) → `002a7632`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfc2bc`](#insn-00bfc2bc) → [`00bfc5d4`](00bfc5d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfc5d4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfc1b0`](#insn-00bfc1b0)

~~~json
{
  "source": "00bfc1b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc1b4`](#insn-00bfc1b4)

~~~json
{
  "source": "00bfc1b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc1b8`](#insn-00bfc1b8)

~~~json
{
  "source": "00bfc1b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc1bc`](#insn-00bfc1bc)

~~~json
{
  "source": "00bfc1bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc1d8`](#insn-00bfc1d8)

~~~json
{
  "source": "00bfc1d8",
  "target": "00bfc264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc204`](#insn-00bfc204)

~~~json
{
  "source": "00bfc204",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc208`](#insn-00bfc208)

~~~json
{
  "source": "00bfc208",
  "target": "00bfc290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc218`](#insn-00bfc218)

~~~json
{
  "source": "00bfc218",
  "target": "00bfc25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc254`](#insn-00bfc254)

~~~json
{
  "source": "00bfc254",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc260`](#insn-00bfc260)

~~~json
{
  "source": "00bfc260",
  "target": "00bfc268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc278`](#insn-00bfc278)

~~~json
{
  "source": "00bfc278",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc27c`](#insn-00bfc27c)

~~~json
{
  "source": "00bfc27c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc280`](#insn-00bfc280)

~~~json
{
  "source": "00bfc280",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc284`](#insn-00bfc284)

~~~json
{
  "source": "00bfc284",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc2a0`](#insn-00bfc2a0)

~~~json
{
  "source": "00bfc2a0",
  "target": "00bfc2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc2a8`](#insn-00bfc2a8)

~~~json
{
  "source": "00bfc2a8",
  "target": "01128460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfc2ac`](#insn-00bfc2ac)

~~~json
{
  "source": "00bfc2ac",
  "target": "01128460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfc2b0`](#insn-00bfc2b0)

~~~json
{
  "source": "00bfc2b0",
  "target": "00bfc278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc2b8`](#insn-00bfc2b8)

~~~json
{
  "source": "00bfc2b8",
  "target": "002a7632",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7632",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "696f735f626173653a3a636c65617200",
  "capture_start": "002a7632",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfc2bc`](#insn-00bfc2bc)

~~~json
{
  "source": "00bfc2bc",
  "target": "00bfc5d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
