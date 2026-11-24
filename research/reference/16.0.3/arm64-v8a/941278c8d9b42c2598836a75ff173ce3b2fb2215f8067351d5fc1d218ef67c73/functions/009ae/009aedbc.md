# 009aedbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009ade10`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ade10.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0024.md#compare-3fbf14fd21da1fd6e826b932ff9404d7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aedbc",
  "name": "FUN_009aedbc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a9d42345128faa149b43f47f07abc8b41200185a2164bf18121b21a21f1a197",
  "source_text_sha256": "2a9d42345128faa149b43f47f07abc8b41200185a2164bf18121b21a21f1a197",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009aedbc",
        "009aeebf"
      ],
      [
        "009aeee4",
        "009aeee7"
      ]
    ],
    "bytes_sha256": "5d84507501de5e2ae10289ad4b60f97bd4dac20554e8b4d2ca44f5f8fbe7e02c",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0061343c](../00613/0061343c.md)

## 呼び出し先

- [009b6c94](../009b6/009b6c94.md)
- [009b6cd4](../009b6/009b6cd4.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2232 bytes

~~~c

void FUN_009aedbc(undefined2 *param_1,undefined8 *param_2,int param_3)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  
                    /* try { // try from 009aedc8 to 00aaedd7 has its CatchHandler @ 009aee18 */
                    /* try { // try from 009aedd8 to 00aaee73 has its CatchHandler @ 009aed3c */
  lVar5 = tpidr_el0;
  lVar8 = *(long *)(lVar5 + 0x28);
  puVar1 = (undefined8 *)*param_2;
  puVar3 = (undefined8 *)param_2[1];
  do {
    if (puVar1 == puVar3) {
      *param_1 = 0;
      if (*(long *)(lVar5 + 0x28) == lVar8) {
        return;
      }
LAB_009aeee4:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c54d60(1,plVar4 + 1);
    }
    iVar6 = FUN_009b6c94(uVar2);
                    /* catch() { ... } // from try @ 009aedc8 with catch @ 009aee18 */
    if ((plVar4 != (long *)0x0) && (lVar7 = FUN_00c54d90(0xffffffffffffffff,plVar4 + 1), lVar7 == 0)
       ) {
                    /* catch() { ... } // from try @ 009aedb4 with catch @ 009aee30 */
      (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* catch() { ... } // from try @ 009aed8c with catch @ 009aee44 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    if (iVar6 == param_3) {
      if (*(long *)(lVar5 + 0x28) == lVar8) {
                    /* try { // try from 009aee9c to 00aaf007 has its CatchHandler @ 009aee9c
                       catch() { ... } // from try @ 009aee9c with catch @ 009aee9c
                       catch() { ... } // from try @ 009af0c8 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af350 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af444 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af664 with catch @ 009aee9c
                       catch() { ... } // from try @ 009af700 with catch @ 009aee9c */
        FUN_009b6cd4(param_1,uVar2);
        return;
      }
      goto LAB_009aeee4;
    }
    puVar1 = puVar1 + 2;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009aedbc"></a> `009aedbc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009aedc0"></a> `009aedc0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009aedc4"></a> `009aedc4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009aedc8"></a> `009aedc8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009aedcc"></a> `009aedcc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009aedd0"></a> `009aedd0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009aedd4"></a> `009aedd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009aedd8"></a> `009aedd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009aeddc"></a> `009aeddc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-009aede0"></a> `009aede0` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009aede4"></a> `009aede4` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009aede8"></a> `009aede8` | `19 68 40 a9` | ldp x25,x26,[x0] | `FALL_THROUGH`
<a id="insn-009aedec"></a> `009aedec` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009aedf0"></a> `009aedf0` | `60 03 00 54` | b.eq 0x009aee5c | `CONDITIONAL_JUMP`
<a id="insn-009aedf4"></a> `009aedf4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-009aedf8"></a> `009aedf8` | `35 5b 40 a9` | ldp x21,x22,[x25] | `FALL_THROUGH`
<a id="insn-009aedfc"></a> `009aedfc` | `f5 db 00 a9` | stp x21,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009aee00"></a> `009aee00` | `96 00 00 b4` | cbz x22,0x009aee10 | `CONDITIONAL_JUMP`
<a id="insn-009aee04"></a> `009aee04` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009aee08"></a> `009aee08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009aee0c"></a> `009aee0c` | `d5 97 0a 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-009aee10"></a> `009aee10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009aee14"></a> `009aee14` | `a0 1f 00 94` | bl 0x009b6c94 | `UNCONDITIONAL_CALL`
<a id="insn-009aee18"></a> `009aee18` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009aee1c"></a> `009aee1c` | `76 01 00 b4` | cbz x22,0x009aee48 | `CONDITIONAL_JUMP`
<a id="insn-009aee20"></a> `009aee20` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009aee24"></a> `009aee24` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009aee28"></a> `009aee28` | `da 97 0a 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009aee2c"></a> `009aee2c` | `e0 00 00 b5` | cbnz x0,0x009aee48 | `CONDITIONAL_JUMP`
<a id="insn-009aee30"></a> `009aee30` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-009aee34"></a> `009aee34` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009aee38"></a> `009aee38` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009aee3c"></a> `009aee3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009aee40"></a> `009aee40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009aee44"></a> `009aee44` | `37 a8 0a 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009aee48"></a> `009aee48` | `ff 02 14 6b` | cmp w23,w20 | `FALL_THROUGH`
<a id="insn-009aee4c"></a> `009aee4c` | `00 02 00 54` | b.eq 0x009aee8c | `CONDITIONAL_JUMP`
<a id="insn-009aee50"></a> `009aee50` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-009aee54"></a> `009aee54` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009aee58"></a> `009aee58` | `01 fd ff 54` | b.ne 0x009aedf8 | `CONDITIONAL_JUMP`
<a id="insn-009aee5c"></a> `009aee5c` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-009aee60"></a> `009aee60` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009aee64"></a> `009aee64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009aee68"></a> `009aee68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009aee6c"></a> `009aee6c` | `c1 03 00 54` | b.ne 0x009aeee4 | `CONDITIONAL_JUMP`
<a id="insn-009aee70"></a> `009aee70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009aee74"></a> `009aee74` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009aee78"></a> `009aee78` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009aee7c"></a> `009aee7c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009aee80"></a> `009aee80` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009aee84"></a> `009aee84` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009aee88"></a> `009aee88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009aee8c"></a> `009aee8c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009aee90"></a> `009aee90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009aee94"></a> `009aee94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009aee98"></a> `009aee98` | `61 02 00 54` | b.ne 0x009aeee4 | `CONDITIONAL_JUMP`
<a id="insn-009aee9c"></a> `009aee9c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-009aeea0"></a> `009aeea0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009aeea4"></a> `009aeea4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009aeea8"></a> `009aeea8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009aeeac"></a> `009aeeac` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009aeeb0"></a> `009aeeb0` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009aeeb4"></a> `009aeeb4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009aeeb8"></a> `009aeeb8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009aeebc"></a> `009aeebc` | `86 1f 00 14` | b 0x009b6cd4 | `CALL_TERMINATOR`
<a id="insn-009aeee4"></a> `009aeee4` | `27 a8 0a 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009aedbc`](#insn-009aedbc) 範囲 `[['009aedbc', '009aedc7']]`
  - `FALL_THROUGH` [`009aedc4`](#insn-009aedc4) → [`009aedc8`](#insn-009aedc8)
- ブロック [`009aedc8`](#insn-009aedc8) 範囲 `[['009aedc8', '009aedd7']]`
  - `FALL_THROUGH` [`009aedd4`](#insn-009aedd4) → [`009aedd8`](#insn-009aedd8)
- ブロック [`009aedd8`](#insn-009aedd8) 範囲 `[['009aedd8', '009aedf3']]`
  - `CONDITIONAL_JUMP` [`009aedf0`](#insn-009aedf0) → [`009aee5c`](#insn-009aee5c)
  - `FALL_THROUGH` [`009aedf0`](#insn-009aedf0) → [`009aedf4`](#insn-009aedf4)
- ブロック [`009aedf4`](#insn-009aedf4) 範囲 `[['009aedf4', '009aedf7']]`
  - `FALL_THROUGH` [`009aedf4`](#insn-009aedf4) → [`009aedf8`](#insn-009aedf8)
- ブロック [`009aedf8`](#insn-009aedf8) 範囲 `[['009aedf8', '009aee03']]`
  - `CONDITIONAL_JUMP` [`009aee00`](#insn-009aee00) → [`009aee10`](#insn-009aee10)
  - `FALL_THROUGH` [`009aee00`](#insn-009aee00) → [`009aee04`](#insn-009aee04)
- ブロック [`009aee04`](#insn-009aee04) 範囲 `[['009aee04', '009aee0f']]`
  - `FALL_THROUGH` [`009aee0c`](#insn-009aee0c) → [`009aee10`](#insn-009aee10)
- ブロック [`009aee10`](#insn-009aee10) 範囲 `[['009aee10', '009aee17']]`
  - `FALL_THROUGH` [`009aee14`](#insn-009aee14) → [`009aee18`](#insn-009aee18)
- ブロック [`009aee18`](#insn-009aee18) 範囲 `[['009aee18', '009aee1f']]`
  - `CONDITIONAL_JUMP` [`009aee1c`](#insn-009aee1c) → [`009aee48`](#insn-009aee48)
  - `FALL_THROUGH` [`009aee1c`](#insn-009aee1c) → [`009aee20`](#insn-009aee20)
- ブロック [`009aee20`](#insn-009aee20) 範囲 `[['009aee20', '009aee2f']]`
  - `CONDITIONAL_JUMP` [`009aee2c`](#insn-009aee2c) → [`009aee48`](#insn-009aee48)
  - `FALL_THROUGH` [`009aee2c`](#insn-009aee2c) → [`009aee30`](#insn-009aee30)
- ブロック [`009aee30`](#insn-009aee30) 範囲 `[['009aee30', '009aee43']]`
  - `FALL_THROUGH` [`009aee40`](#insn-009aee40) → [`009aee44`](#insn-009aee44)
- ブロック [`009aee44`](#insn-009aee44) 範囲 `[['009aee44', '009aee47']]`
  - `FALL_THROUGH` [`009aee44`](#insn-009aee44) → [`009aee48`](#insn-009aee48)
- ブロック [`009aee48`](#insn-009aee48) 範囲 `[['009aee48', '009aee4f']]`
  - `CONDITIONAL_JUMP` [`009aee4c`](#insn-009aee4c) → [`009aee8c`](#insn-009aee8c)
  - `FALL_THROUGH` [`009aee4c`](#insn-009aee4c) → [`009aee50`](#insn-009aee50)
- ブロック [`009aee50`](#insn-009aee50) 範囲 `[['009aee50', '009aee5b']]`
  - `CONDITIONAL_JUMP` [`009aee58`](#insn-009aee58) → [`009aedf8`](#insn-009aedf8)
  - `FALL_THROUGH` [`009aee58`](#insn-009aee58) → [`009aee5c`](#insn-009aee5c)
- ブロック [`009aee5c`](#insn-009aee5c) 範囲 `[['009aee5c', '009aee6f']]`
  - `CONDITIONAL_JUMP` [`009aee6c`](#insn-009aee6c) → [`009aeee4`](#insn-009aeee4)
  - `FALL_THROUGH` [`009aee6c`](#insn-009aee6c) → [`009aee70`](#insn-009aee70)
- ブロック [`009aee70`](#insn-009aee70) 範囲 `[['009aee70', '009aee8b']]`
- ブロック [`009aee8c`](#insn-009aee8c) 範囲 `[['009aee8c', '009aee9b']]`
  - `CONDITIONAL_JUMP` [`009aee98`](#insn-009aee98) → [`009aeee4`](#insn-009aeee4)
  - `FALL_THROUGH` [`009aee98`](#insn-009aee98) → [`009aee9c`](#insn-009aee9c)
- ブロック [`009aee9c`](#insn-009aee9c) 範囲 `[['009aee9c', '009aeebf']]`
- ブロック [`009aeee4`](#insn-009aeee4) 範囲 `[['009aeee4', '009aeee7']]`

## 命令位置別の参照

- [`009aedc0`](#insn-009aedc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedc4`](#insn-009aedc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedc8`](#insn-009aedc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedcc`](#insn-009aedcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedd0`](#insn-009aedd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aede4`](#insn-009aede4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedf0`](#insn-009aedf0) → [`009aee5c`](#insn-009aee5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aedfc`](#insn-009aedfc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee00`](#insn-009aee00) → [`009aee10`](#insn-009aee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee0c`](#insn-009aee0c) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`009aee14`](#insn-009aee14) → [`009b6c94`](../009b6/009b6c94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b6c94` · 推定シンボル `None` · 推定型 `None`
- [`009aee1c`](#insn-009aee1c) → [`009aee48`](#insn-009aee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee28`](#insn-009aee28) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009aee2c`](#insn-009aee2c) → [`009aee48`](#insn-009aee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee44`](#insn-009aee44) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009aee4c`](#insn-009aee4c) → [`009aee8c`](#insn-009aee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee58`](#insn-009aee58) → [`009aedf8`](#insn-009aedf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee64`](#insn-009aee64) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee6c`](#insn-009aee6c) → [`009aeee4`](#insn-009aeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee70`](#insn-009aee70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee74`](#insn-009aee74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee78`](#insn-009aee78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee7c`](#insn-009aee7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee80`](#insn-009aee80) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee90`](#insn-009aee90) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aee98`](#insn-009aee98) → [`009aeee4`](#insn-009aeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeea4`](#insn-009aeea4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeea8`](#insn-009aeea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeeac`](#insn-009aeeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeeb0`](#insn-009aeeb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeeb4`](#insn-009aeeb4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009aeebc`](#insn-009aeebc) → [`009b6cd4`](../009b6/009b6cd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b6cd4` · 推定シンボル `None` · 推定型 `None`
- [`009aeee4`](#insn-009aeee4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009aedc0`](#insn-009aedc0)

~~~json
{
  "source": "009aedc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedc4`](#insn-009aedc4)

~~~json
{
  "source": "009aedc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedc8`](#insn-009aedc8)

~~~json
{
  "source": "009aedc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedcc`](#insn-009aedcc)

~~~json
{
  "source": "009aedcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedd0`](#insn-009aedd0)

~~~json
{
  "source": "009aedd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aede4`](#insn-009aede4)

~~~json
{
  "source": "009aede4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedf0`](#insn-009aedf0)

~~~json
{
  "source": "009aedf0",
  "target": "009aee5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aedfc`](#insn-009aedfc)

~~~json
{
  "source": "009aedfc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee00`](#insn-009aee00)

~~~json
{
  "source": "009aee00",
  "target": "009aee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee0c`](#insn-009aee0c)

~~~json
{
  "source": "009aee0c",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aee14`](#insn-009aee14)

~~~json
{
  "source": "009aee14",
  "target": "009b6c94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aee1c`](#insn-009aee1c)

~~~json
{
  "source": "009aee1c",
  "target": "009aee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee28`](#insn-009aee28)

~~~json
{
  "source": "009aee28",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aee2c`](#insn-009aee2c)

~~~json
{
  "source": "009aee2c",
  "target": "009aee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee44`](#insn-009aee44)

~~~json
{
  "source": "009aee44",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aee4c`](#insn-009aee4c)

~~~json
{
  "source": "009aee4c",
  "target": "009aee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee58`](#insn-009aee58)

~~~json
{
  "source": "009aee58",
  "target": "009aedf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee64`](#insn-009aee64)

~~~json
{
  "source": "009aee64",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee6c`](#insn-009aee6c)

~~~json
{
  "source": "009aee6c",
  "target": "009aeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee70`](#insn-009aee70)

~~~json
{
  "source": "009aee70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee74`](#insn-009aee74)

~~~json
{
  "source": "009aee74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee78`](#insn-009aee78)

~~~json
{
  "source": "009aee78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee7c`](#insn-009aee7c)

~~~json
{
  "source": "009aee7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee80`](#insn-009aee80)

~~~json
{
  "source": "009aee80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee90`](#insn-009aee90)

~~~json
{
  "source": "009aee90",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aee98`](#insn-009aee98)

~~~json
{
  "source": "009aee98",
  "target": "009aeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeea4`](#insn-009aeea4)

~~~json
{
  "source": "009aeea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeea8`](#insn-009aeea8)

~~~json
{
  "source": "009aeea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeeac`](#insn-009aeeac)

~~~json
{
  "source": "009aeeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeeb0`](#insn-009aeeb0)

~~~json
{
  "source": "009aeeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeeb4`](#insn-009aeeb4)

~~~json
{
  "source": "009aeeb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009aeebc`](#insn-009aeebc)

~~~json
{
  "source": "009aeebc",
  "target": "009b6cd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009aeee4`](#insn-009aeee4)

~~~json
{
  "source": "009aeee4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
