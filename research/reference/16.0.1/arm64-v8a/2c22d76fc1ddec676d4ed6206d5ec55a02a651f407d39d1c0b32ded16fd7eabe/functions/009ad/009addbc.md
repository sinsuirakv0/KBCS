# 009addbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009adc20`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adc20.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0055.md#compare-40cc6342951f0b4f140c194e95c4f7f8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009ade10`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ade10.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0057.md#compare-94b407c7c23627725ff4ad422f1bf659)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009addbc",
  "name": "FUN_009addbc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c99a4516960d90324aafebcc8598f78425cd264e97e57b2c18db7be50cc60cc0",
  "source_text_sha256": "c99a4516960d90324aafebcc8598f78425cd264e97e57b2c18db7be50cc60cc0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009addbc",
        "009adebf"
      ],
      [
        "009adee4",
        "009adee7"
      ]
    ],
    "bytes_sha256": "a1844ff1040d923758ed0a6e0cad6210d82889aecf83b691ea01c99361179ef3",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0061304c](../00613/0061304c.md)

## 呼び出し先

- [009b5c94](../009b5/009b5c94.md)
- [009b5cd4](../009b5/009b5cd4.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2232 bytes

~~~c

void FUN_009addbc(undefined2 *param_1,undefined8 *param_2,int param_3)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  int iVar6;
  long lVar7;
  long lVar8;
  
                    /* try { // try from 009addc4 to 00aaddd3 has its CatchHandler @ 009ade14 */
                    /* try { // try from 009addd4 to 00aade6f has its CatchHandler @ 009add38 */
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
LAB_009adee4:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    uVar2 = *puVar1;
    plVar4 = (long *)puVar1[1];
    if (plVar4 != (long *)0x0) {
      FUN_00c53cd0(1,plVar4 + 1);
    }
                    /* catch() { ... } // from try @ 009addc4 with catch @ 009ade14 */
    iVar6 = FUN_009b5c94(uVar2);
                    /* catch() { ... } // from try @ 009addb0 with catch @ 009ade2c */
    if ((plVar4 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar7 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* catch() { ... } // from try @ 009add88 with catch @ 009ade40 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    if (iVar6 == param_3) {
                    /* try { // try from 009ade98 to 00aae003 has its CatchHandler @ 009ade98
                       catch() { ... } // from try @ 009ade98 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae0c4 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae34c with catch @ 009ade98
                       catch() { ... } // from try @ 009ae440 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae660 with catch @ 009ade98
                       catch() { ... } // from try @ 009ae6fc with catch @ 009ade98 */
      if (*(long *)(lVar5 + 0x28) == lVar8) {
        FUN_009b5cd4(param_1,uVar2);
        return;
      }
      goto LAB_009adee4;
    }
    puVar1 = puVar1 + 2;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009addbc"></a> `009addbc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009addc0"></a> `009addc0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009addc4"></a> `009addc4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009addc8"></a> `009addc8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009addcc"></a> `009addcc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009addd0"></a> `009addd0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009addd4"></a> `009addd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009addd8"></a> `009addd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009adddc"></a> `009adddc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-009adde0"></a> `009adde0` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009adde4"></a> `009adde4` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009adde8"></a> `009adde8` | `19 68 40 a9` | ldp x25,x26,[x0] | `FALL_THROUGH`
<a id="insn-009addec"></a> `009addec` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009addf0"></a> `009addf0` | `60 03 00 54` | b.eq 0x009ade5c | `CONDITIONAL_JUMP`
<a id="insn-009addf4"></a> `009addf4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-009addf8"></a> `009addf8` | `35 5b 40 a9` | ldp x21,x22,[x25] | `FALL_THROUGH`
<a id="insn-009addfc"></a> `009addfc` | `f5 db 00 a9` | stp x21,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ade00"></a> `009ade00` | `96 00 00 b4` | cbz x22,0x009ade10 | `CONDITIONAL_JUMP`
<a id="insn-009ade04"></a> `009ade04` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009ade08"></a> `009ade08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ade0c"></a> `009ade0c` | `b1 97 0a 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-009ade10"></a> `009ade10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009ade14"></a> `009ade14` | `a0 1f 00 94` | bl 0x009b5c94 | `UNCONDITIONAL_CALL`
<a id="insn-009ade18"></a> `009ade18` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009ade1c"></a> `009ade1c` | `76 01 00 b4` | cbz x22,0x009ade48 | `CONDITIONAL_JUMP`
<a id="insn-009ade20"></a> `009ade20` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009ade24"></a> `009ade24` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009ade28"></a> `009ade28` | `b6 97 0a 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009ade2c"></a> `009ade2c` | `e0 00 00 b5` | cbnz x0,0x009ade48 | `CONDITIONAL_JUMP`
<a id="insn-009ade30"></a> `009ade30` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-009ade34"></a> `009ade34` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ade38"></a> `009ade38` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009ade3c"></a> `009ade3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009ade40"></a> `009ade40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-009ade44"></a> `009ade44` | `0f a8 0a 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009ade48"></a> `009ade48` | `ff 02 14 6b` | cmp w23,w20 | `FALL_THROUGH`
<a id="insn-009ade4c"></a> `009ade4c` | `00 02 00 54` | b.eq 0x009ade8c | `CONDITIONAL_JUMP`
<a id="insn-009ade50"></a> `009ade50` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-009ade54"></a> `009ade54` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009ade58"></a> `009ade58` | `01 fd ff 54` | b.ne 0x009addf8 | `CONDITIONAL_JUMP`
<a id="insn-009ade5c"></a> `009ade5c` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-009ade60"></a> `009ade60` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009ade64"></a> `009ade64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ade68"></a> `009ade68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ade6c"></a> `009ade6c` | `c1 03 00 54` | b.ne 0x009adee4 | `CONDITIONAL_JUMP`
<a id="insn-009ade70"></a> `009ade70` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009ade74"></a> `009ade74` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009ade78"></a> `009ade78` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009ade7c"></a> `009ade7c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ade80"></a> `009ade80` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009ade84"></a> `009ade84` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009ade88"></a> `009ade88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ade8c"></a> `009ade8c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009ade90"></a> `009ade90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ade94"></a> `009ade94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ade98"></a> `009ade98` | `61 02 00 54` | b.ne 0x009adee4 | `CONDITIONAL_JUMP`
<a id="insn-009ade9c"></a> `009ade9c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-009adea0"></a> `009adea0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009adea4"></a> `009adea4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009adea8"></a> `009adea8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009adeac"></a> `009adeac` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009adeb0"></a> `009adeb0` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009adeb4"></a> `009adeb4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009adeb8"></a> `009adeb8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009adebc"></a> `009adebc` | `86 1f 00 14` | b 0x009b5cd4 | `CALL_TERMINATOR`
<a id="insn-009adee4"></a> `009adee4` | `ff a7 0a 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009addbc`](#insn-009addbc) 範囲 `[['009addbc', '009addc3']]`
  - `FALL_THROUGH` [`009addc0`](#insn-009addc0) → [`009addc4`](#insn-009addc4)
- ブロック [`009addc4`](#insn-009addc4) 範囲 `[['009addc4', '009addd3']]`
  - `FALL_THROUGH` [`009addd0`](#insn-009addd0) → [`009addd4`](#insn-009addd4)
- ブロック [`009addd4`](#insn-009addd4) 範囲 `[['009addd4', '009addf3']]`
  - `CONDITIONAL_JUMP` [`009addf0`](#insn-009addf0) → [`009ade5c`](#insn-009ade5c)
  - `FALL_THROUGH` [`009addf0`](#insn-009addf0) → [`009addf4`](#insn-009addf4)
- ブロック [`009addf4`](#insn-009addf4) 範囲 `[['009addf4', '009addf7']]`
  - `FALL_THROUGH` [`009addf4`](#insn-009addf4) → [`009addf8`](#insn-009addf8)
- ブロック [`009addf8`](#insn-009addf8) 範囲 `[['009addf8', '009ade03']]`
  - `CONDITIONAL_JUMP` [`009ade00`](#insn-009ade00) → [`009ade10`](#insn-009ade10)
  - `FALL_THROUGH` [`009ade00`](#insn-009ade00) → [`009ade04`](#insn-009ade04)
- ブロック [`009ade04`](#insn-009ade04) 範囲 `[['009ade04', '009ade0f']]`
  - `FALL_THROUGH` [`009ade0c`](#insn-009ade0c) → [`009ade10`](#insn-009ade10)
- ブロック [`009ade10`](#insn-009ade10) 範囲 `[['009ade10', '009ade13']]`
  - `FALL_THROUGH` [`009ade10`](#insn-009ade10) → [`009ade14`](#insn-009ade14)
- ブロック [`009ade14`](#insn-009ade14) 範囲 `[['009ade14', '009ade1f']]`
  - `CONDITIONAL_JUMP` [`009ade1c`](#insn-009ade1c) → [`009ade48`](#insn-009ade48)
  - `FALL_THROUGH` [`009ade1c`](#insn-009ade1c) → [`009ade20`](#insn-009ade20)
- ブロック [`009ade20`](#insn-009ade20) 範囲 `[['009ade20', '009ade2b']]`
  - `FALL_THROUGH` [`009ade28`](#insn-009ade28) → [`009ade2c`](#insn-009ade2c)
- ブロック [`009ade2c`](#insn-009ade2c) 範囲 `[['009ade2c', '009ade2f']]`
  - `CONDITIONAL_JUMP` [`009ade2c`](#insn-009ade2c) → [`009ade48`](#insn-009ade48)
  - `FALL_THROUGH` [`009ade2c`](#insn-009ade2c) → [`009ade30`](#insn-009ade30)
- ブロック [`009ade30`](#insn-009ade30) 範囲 `[['009ade30', '009ade3f']]`
  - `FALL_THROUGH` [`009ade3c`](#insn-009ade3c) → [`009ade40`](#insn-009ade40)
- ブロック [`009ade40`](#insn-009ade40) 範囲 `[['009ade40', '009ade47']]`
  - `FALL_THROUGH` [`009ade44`](#insn-009ade44) → [`009ade48`](#insn-009ade48)
- ブロック [`009ade48`](#insn-009ade48) 範囲 `[['009ade48', '009ade4f']]`
  - `CONDITIONAL_JUMP` [`009ade4c`](#insn-009ade4c) → [`009ade8c`](#insn-009ade8c)
  - `FALL_THROUGH` [`009ade4c`](#insn-009ade4c) → [`009ade50`](#insn-009ade50)
- ブロック [`009ade50`](#insn-009ade50) 範囲 `[['009ade50', '009ade5b']]`
  - `CONDITIONAL_JUMP` [`009ade58`](#insn-009ade58) → [`009addf8`](#insn-009addf8)
  - `FALL_THROUGH` [`009ade58`](#insn-009ade58) → [`009ade5c`](#insn-009ade5c)
- ブロック [`009ade5c`](#insn-009ade5c) 範囲 `[['009ade5c', '009ade6f']]`
  - `CONDITIONAL_JUMP` [`009ade6c`](#insn-009ade6c) → [`009adee4`](#insn-009adee4)
  - `FALL_THROUGH` [`009ade6c`](#insn-009ade6c) → [`009ade70`](#insn-009ade70)
- ブロック [`009ade70`](#insn-009ade70) 範囲 `[['009ade70', '009ade8b']]`
- ブロック [`009ade8c`](#insn-009ade8c) 範囲 `[['009ade8c', '009ade97']]`
  - `FALL_THROUGH` [`009ade94`](#insn-009ade94) → [`009ade98`](#insn-009ade98)
- ブロック [`009ade98`](#insn-009ade98) 範囲 `[['009ade98', '009ade9b']]`
  - `CONDITIONAL_JUMP` [`009ade98`](#insn-009ade98) → [`009adee4`](#insn-009adee4)
  - `FALL_THROUGH` [`009ade98`](#insn-009ade98) → [`009ade9c`](#insn-009ade9c)
- ブロック [`009ade9c`](#insn-009ade9c) 範囲 `[['009ade9c', '009adebf']]`
- ブロック [`009adee4`](#insn-009adee4) 範囲 `[['009adee4', '009adee7']]`

## 命令位置別の参照

- [`009addc0`](#insn-009addc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addc4`](#insn-009addc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addc8`](#insn-009addc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addcc`](#insn-009addcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addd0`](#insn-009addd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adde4`](#insn-009adde4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addf0`](#insn-009addf0) → [`009ade5c`](#insn-009ade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009addfc`](#insn-009addfc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade00`](#insn-009ade00) → [`009ade10`](#insn-009ade10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade0c`](#insn-009ade0c) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`009ade14`](#insn-009ade14) → [`009b5c94`](../009b5/009b5c94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5c94` · 推定シンボル `None` · 推定型 `None`
- [`009ade1c`](#insn-009ade1c) → [`009ade48`](#insn-009ade48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade28`](#insn-009ade28) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009ade2c`](#insn-009ade2c) → [`009ade48`](#insn-009ade48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade44`](#insn-009ade44) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009ade4c`](#insn-009ade4c) → [`009ade8c`](#insn-009ade8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade58`](#insn-009ade58) → [`009addf8`](#insn-009addf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade64`](#insn-009ade64) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade6c`](#insn-009ade6c) → [`009adee4`](#insn-009adee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade70`](#insn-009ade70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade74`](#insn-009ade74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade78`](#insn-009ade78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade7c`](#insn-009ade7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade80`](#insn-009ade80) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade90`](#insn-009ade90) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ade98`](#insn-009ade98) → [`009adee4`](#insn-009adee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adea4`](#insn-009adea4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adea8`](#insn-009adea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adeac`](#insn-009adeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adeb0`](#insn-009adeb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adeb4`](#insn-009adeb4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adebc`](#insn-009adebc) → [`009b5cd4`](../009b5/009b5cd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5cd4` · 推定シンボル `None` · 推定型 `None`
- [`009adee4`](#insn-009adee4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009addc0`](#insn-009addc0)

~~~json
{
  "source": "009addc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addc4`](#insn-009addc4)

~~~json
{
  "source": "009addc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addc8`](#insn-009addc8)

~~~json
{
  "source": "009addc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addcc`](#insn-009addcc)

~~~json
{
  "source": "009addcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addd0`](#insn-009addd0)

~~~json
{
  "source": "009addd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adde4`](#insn-009adde4)

~~~json
{
  "source": "009adde4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addf0`](#insn-009addf0)

~~~json
{
  "source": "009addf0",
  "target": "009ade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009addfc`](#insn-009addfc)

~~~json
{
  "source": "009addfc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade00`](#insn-009ade00)

~~~json
{
  "source": "009ade00",
  "target": "009ade10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade0c`](#insn-009ade0c)

~~~json
{
  "source": "009ade0c",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ade14`](#insn-009ade14)

~~~json
{
  "source": "009ade14",
  "target": "009b5c94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ade1c`](#insn-009ade1c)

~~~json
{
  "source": "009ade1c",
  "target": "009ade48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade28`](#insn-009ade28)

~~~json
{
  "source": "009ade28",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ade2c`](#insn-009ade2c)

~~~json
{
  "source": "009ade2c",
  "target": "009ade48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade44`](#insn-009ade44)

~~~json
{
  "source": "009ade44",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ade4c`](#insn-009ade4c)

~~~json
{
  "source": "009ade4c",
  "target": "009ade8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade58`](#insn-009ade58)

~~~json
{
  "source": "009ade58",
  "target": "009addf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade64`](#insn-009ade64)

~~~json
{
  "source": "009ade64",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade6c`](#insn-009ade6c)

~~~json
{
  "source": "009ade6c",
  "target": "009adee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade70`](#insn-009ade70)

~~~json
{
  "source": "009ade70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade74`](#insn-009ade74)

~~~json
{
  "source": "009ade74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade78`](#insn-009ade78)

~~~json
{
  "source": "009ade78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade7c`](#insn-009ade7c)

~~~json
{
  "source": "009ade7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade80`](#insn-009ade80)

~~~json
{
  "source": "009ade80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade90`](#insn-009ade90)

~~~json
{
  "source": "009ade90",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ade98`](#insn-009ade98)

~~~json
{
  "source": "009ade98",
  "target": "009adee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adea4`](#insn-009adea4)

~~~json
{
  "source": "009adea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adea8`](#insn-009adea8)

~~~json
{
  "source": "009adea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adeac`](#insn-009adeac)

~~~json
{
  "source": "009adeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adeb0`](#insn-009adeb0)

~~~json
{
  "source": "009adeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adeb4`](#insn-009adeb4)

~~~json
{
  "source": "009adeb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adebc`](#insn-009adebc)

~~~json
{
  "source": "009adebc",
  "target": "009b5cd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009adee4`](#insn-009adee4)

~~~json
{
  "source": "009adee4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
