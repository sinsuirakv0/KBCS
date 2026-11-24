# 009bcdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009bcd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0031.md#compare-fd87fe52524d7cc58358e6254313c31f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009bdd58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009bd/009bdd58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0025.md#compare-e67e34b06fe85f655211e4b00674eafb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009bcdac",
  "name": "FUN_009bcdac",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "056c3d04bc0d0f52a5924e73b5800a0c339218e58738987e970362d85d20e723",
  "source_text_sha256": "056c3d04bc0d0f52a5924e73b5800a0c339218e58738987e970362d85d20e723",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009bcdac",
        "009bced3"
      ]
    ],
    "bytes_sha256": "7bbded7faa1f809554a1c80a7ab33fc887aede90021fb024c17610bc5e62036d",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [009bdb8c](../009bd/009bdb8c.md)
- [009bdcd4](../009bd/009bdcd4.md)

## 呼び出し先

- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1708 bytes

~~~c

void FUN_009bcdac(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[1];
  *param_1 = 0;
  param_1[1] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[3];
  param_1[2] = 0;
  param_1[3] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[5];
  param_1[4] = 0;
  param_1[5] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[7];
  param_1[6] = 0;
  param_1[7] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* try { // try from 009bce7c to 00abce93 has its CatchHandler @ 009bdacc */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[9];
  param_1[8] = 0;
  param_1[9] = 0;
                    /* try { // try from 009bce94 to 00abcf8f has its CatchHandler @ 009bc920 */
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53da0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009bcdac"></a> `009bcdac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009bcdb0"></a> `009bcdb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bcdb4"></a> `009bcdb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009bcdb8"></a> `009bcdb8` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009bcdbc"></a> `009bcdbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009bcdc0"></a> `009bcdc0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-009bcdc4"></a> `009bcdc4` | `74 01 00 b4` | cbz x20,0x009bcdf0 | `CONDITIONAL_JUMP`
<a id="insn-009bcdc8"></a> `009bcdc8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bcdcc"></a> `009bcdcc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcdd0"></a> `009bcdd0` | `f4 5b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcdd4"></a> `009bcdd4` | `e0 00 00 b5` | cbnz x0,0x009bcdf0 | `CONDITIONAL_JUMP`
<a id="insn-009bcdd8"></a> `009bcdd8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bcddc"></a> `009bcddc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcde0"></a> `009bcde0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcde4"></a> `009bcde4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcde8"></a> `009bcde8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcdec"></a> `009bcdec` | `59 6c 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009bcdf0"></a> `009bcdf0` | `74 0e 40 f9` | ldr x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-009bcdf4"></a> `009bcdf4` | `7f 7e 01 a9` | stp xzr,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-009bcdf8"></a> `009bcdf8` | `74 01 00 b4` | cbz x20,0x009bce24 | `CONDITIONAL_JUMP`
<a id="insn-009bcdfc"></a> `009bcdfc` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bce00"></a> `009bce00` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bce04"></a> `009bce04` | `e7 5b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009bce08"></a> `009bce08` | `e0 00 00 b5` | cbnz x0,0x009bce24 | `CONDITIONAL_JUMP`
<a id="insn-009bce0c"></a> `009bce0c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bce10"></a> `009bce10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce14"></a> `009bce14` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bce18"></a> `009bce18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bce1c"></a> `009bce1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce20"></a> `009bce20` | `4c 6c 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009bce24"></a> `009bce24` | `74 16 40 f9` | ldr x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-009bce28"></a> `009bce28` | `7f 7e 02 a9` | stp xzr,xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-009bce2c"></a> `009bce2c` | `74 01 00 b4` | cbz x20,0x009bce58 | `CONDITIONAL_JUMP`
<a id="insn-009bce30"></a> `009bce30` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bce34"></a> `009bce34` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bce38"></a> `009bce38` | `da 5b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009bce3c"></a> `009bce3c` | `e0 00 00 b5` | cbnz x0,0x009bce58 | `CONDITIONAL_JUMP`
<a id="insn-009bce40"></a> `009bce40` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bce44"></a> `009bce44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce48"></a> `009bce48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bce4c"></a> `009bce4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bce50"></a> `009bce50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce54"></a> `009bce54` | `3f 6c 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009bce58"></a> `009bce58` | `74 1e 40 f9` | ldr x20,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-009bce5c"></a> `009bce5c` | `7f 7e 03 a9` | stp xzr,xzr,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-009bce60"></a> `009bce60` | `74 01 00 b4` | cbz x20,0x009bce8c | `CONDITIONAL_JUMP`
<a id="insn-009bce64"></a> `009bce64` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bce68"></a> `009bce68` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bce6c"></a> `009bce6c` | `cd 5b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009bce70"></a> `009bce70` | `e0 00 00 b5` | cbnz x0,0x009bce8c | `CONDITIONAL_JUMP`
<a id="insn-009bce74"></a> `009bce74` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bce78"></a> `009bce78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce7c"></a> `009bce7c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bce80"></a> `009bce80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bce84"></a> `009bce84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bce88"></a> `009bce88` | `32 6c 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009bce8c"></a> `009bce8c` | `74 26 40 f9` | ldr x20,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-009bce90"></a> `009bce90` | `7f 7e 04 a9` | stp xzr,xzr,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-009bce94"></a> `009bce94` | `b4 00 00 b4` | cbz x20,0x009bcea8 | `CONDITIONAL_JUMP`
<a id="insn-009bce98"></a> `009bce98` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bce9c"></a> `009bce9c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcea0"></a> `009bcea0` | `c0 5b 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcea4"></a> `009bcea4` | `80 00 00 b4` | cbz x0,0x009bceb4 | `CONDITIONAL_JUMP`
<a id="insn-009bcea8"></a> `009bcea8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bceac"></a> `009bceac` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009bceb0"></a> `009bceb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009bceb4"></a> `009bceb4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bceb8"></a> `009bceb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcebc"></a> `009bcebc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcec0"></a> `009bcec0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcec4"></a> `009bcec4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcec8"></a> `009bcec8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bcecc"></a> `009bcecc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009bced0"></a> `009bced0` | `20 6c 0a 14` | b 0x00c57f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009bcdac`](#insn-009bcdac) 範囲 `[['009bcdac', '009bcdc7']]`
  - `CONDITIONAL_JUMP` [`009bcdc4`](#insn-009bcdc4) → [`009bcdf0`](#insn-009bcdf0)
  - `FALL_THROUGH` [`009bcdc4`](#insn-009bcdc4) → [`009bcdc8`](#insn-009bcdc8)
- ブロック [`009bcdc8`](#insn-009bcdc8) 範囲 `[['009bcdc8', '009bcdd7']]`
  - `CONDITIONAL_JUMP` [`009bcdd4`](#insn-009bcdd4) → [`009bcdf0`](#insn-009bcdf0)
  - `FALL_THROUGH` [`009bcdd4`](#insn-009bcdd4) → [`009bcdd8`](#insn-009bcdd8)
- ブロック [`009bcdd8`](#insn-009bcdd8) 範囲 `[['009bcdd8', '009bcdef']]`
  - `FALL_THROUGH` [`009bcdec`](#insn-009bcdec) → [`009bcdf0`](#insn-009bcdf0)
- ブロック [`009bcdf0`](#insn-009bcdf0) 範囲 `[['009bcdf0', '009bcdfb']]`
  - `CONDITIONAL_JUMP` [`009bcdf8`](#insn-009bcdf8) → [`009bce24`](#insn-009bce24)
  - `FALL_THROUGH` [`009bcdf8`](#insn-009bcdf8) → [`009bcdfc`](#insn-009bcdfc)
- ブロック [`009bcdfc`](#insn-009bcdfc) 範囲 `[['009bcdfc', '009bce0b']]`
  - `CONDITIONAL_JUMP` [`009bce08`](#insn-009bce08) → [`009bce24`](#insn-009bce24)
  - `FALL_THROUGH` [`009bce08`](#insn-009bce08) → [`009bce0c`](#insn-009bce0c)
- ブロック [`009bce0c`](#insn-009bce0c) 範囲 `[['009bce0c', '009bce23']]`
  - `FALL_THROUGH` [`009bce20`](#insn-009bce20) → [`009bce24`](#insn-009bce24)
- ブロック [`009bce24`](#insn-009bce24) 範囲 `[['009bce24', '009bce2f']]`
  - `CONDITIONAL_JUMP` [`009bce2c`](#insn-009bce2c) → [`009bce58`](#insn-009bce58)
  - `FALL_THROUGH` [`009bce2c`](#insn-009bce2c) → [`009bce30`](#insn-009bce30)
- ブロック [`009bce30`](#insn-009bce30) 範囲 `[['009bce30', '009bce3f']]`
  - `CONDITIONAL_JUMP` [`009bce3c`](#insn-009bce3c) → [`009bce58`](#insn-009bce58)
  - `FALL_THROUGH` [`009bce3c`](#insn-009bce3c) → [`009bce40`](#insn-009bce40)
- ブロック [`009bce40`](#insn-009bce40) 範囲 `[['009bce40', '009bce57']]`
  - `FALL_THROUGH` [`009bce54`](#insn-009bce54) → [`009bce58`](#insn-009bce58)
- ブロック [`009bce58`](#insn-009bce58) 範囲 `[['009bce58', '009bce63']]`
  - `CONDITIONAL_JUMP` [`009bce60`](#insn-009bce60) → [`009bce8c`](#insn-009bce8c)
  - `FALL_THROUGH` [`009bce60`](#insn-009bce60) → [`009bce64`](#insn-009bce64)
- ブロック [`009bce64`](#insn-009bce64) 範囲 `[['009bce64', '009bce73']]`
  - `CONDITIONAL_JUMP` [`009bce70`](#insn-009bce70) → [`009bce8c`](#insn-009bce8c)
  - `FALL_THROUGH` [`009bce70`](#insn-009bce70) → [`009bce74`](#insn-009bce74)
- ブロック [`009bce74`](#insn-009bce74) 範囲 `[['009bce74', '009bce7b']]`
  - `FALL_THROUGH` [`009bce78`](#insn-009bce78) → [`009bce7c`](#insn-009bce7c)
- ブロック [`009bce7c`](#insn-009bce7c) 範囲 `[['009bce7c', '009bce8b']]`
  - `FALL_THROUGH` [`009bce88`](#insn-009bce88) → [`009bce8c`](#insn-009bce8c)
- ブロック [`009bce8c`](#insn-009bce8c) 範囲 `[['009bce8c', '009bce93']]`
  - `FALL_THROUGH` [`009bce90`](#insn-009bce90) → [`009bce94`](#insn-009bce94)
- ブロック [`009bce94`](#insn-009bce94) 範囲 `[['009bce94', '009bce97']]`
  - `CONDITIONAL_JUMP` [`009bce94`](#insn-009bce94) → [`009bcea8`](#insn-009bcea8)
  - `FALL_THROUGH` [`009bce94`](#insn-009bce94) → [`009bce98`](#insn-009bce98)
- ブロック [`009bce98`](#insn-009bce98) 範囲 `[['009bce98', '009bcea7']]`
  - `CONDITIONAL_JUMP` [`009bcea4`](#insn-009bcea4) → [`009bceb4`](#insn-009bceb4)
  - `FALL_THROUGH` [`009bcea4`](#insn-009bcea4) → [`009bcea8`](#insn-009bcea8)
- ブロック [`009bcea8`](#insn-009bcea8) 範囲 `[['009bcea8', '009bceb3']]`
- ブロック [`009bceb4`](#insn-009bceb4) 範囲 `[['009bceb4', '009bced3']]`

## 命令位置別の参照

- [`009bcdac`](#insn-009bcdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcdb0`](#insn-009bcdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcdc4`](#insn-009bcdc4) → [`009bcdf0`](#insn-009bcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcdd0`](#insn-009bcdd0) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009bcdd4`](#insn-009bcdd4) → [`009bcdf0`](#insn-009bcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcdec`](#insn-009bcdec) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009bcdf8`](#insn-009bcdf8) → [`009bce24`](#insn-009bce24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce04`](#insn-009bce04) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009bce08`](#insn-009bce08) → [`009bce24`](#insn-009bce24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce20`](#insn-009bce20) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009bce2c`](#insn-009bce2c) → [`009bce58`](#insn-009bce58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce38`](#insn-009bce38) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009bce3c`](#insn-009bce3c) → [`009bce58`](#insn-009bce58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce54`](#insn-009bce54) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009bce60`](#insn-009bce60) → [`009bce8c`](#insn-009bce8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce6c`](#insn-009bce6c) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009bce70`](#insn-009bce70) → [`009bce8c`](#insn-009bce8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bce88`](#insn-009bce88) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009bce94`](#insn-009bce94) → [`009bcea8`](#insn-009bcea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcea0`](#insn-009bcea0) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009bcea4`](#insn-009bcea4) → [`009bceb4`](#insn-009bceb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcea8`](#insn-009bcea8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bceac`](#insn-009bceac) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcec8`](#insn-009bcec8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcecc`](#insn-009bcecc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bced0`](#insn-009bced0) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009bcdac`](#insn-009bcdac)

~~~json
{
  "source": "009bcdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcdb0`](#insn-009bcdb0)

~~~json
{
  "source": "009bcdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcdc4`](#insn-009bcdc4)

~~~json
{
  "source": "009bcdc4",
  "target": "009bcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcdd0`](#insn-009bcdd0)

~~~json
{
  "source": "009bcdd0",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcdd4`](#insn-009bcdd4)

~~~json
{
  "source": "009bcdd4",
  "target": "009bcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcdec`](#insn-009bcdec)

~~~json
{
  "source": "009bcdec",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcdf8`](#insn-009bcdf8)

~~~json
{
  "source": "009bcdf8",
  "target": "009bce24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce04`](#insn-009bce04)

~~~json
{
  "source": "009bce04",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce08`](#insn-009bce08)

~~~json
{
  "source": "009bce08",
  "target": "009bce24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce20`](#insn-009bce20)

~~~json
{
  "source": "009bce20",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce2c`](#insn-009bce2c)

~~~json
{
  "source": "009bce2c",
  "target": "009bce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce38`](#insn-009bce38)

~~~json
{
  "source": "009bce38",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce3c`](#insn-009bce3c)

~~~json
{
  "source": "009bce3c",
  "target": "009bce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce54`](#insn-009bce54)

~~~json
{
  "source": "009bce54",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce60`](#insn-009bce60)

~~~json
{
  "source": "009bce60",
  "target": "009bce8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce6c`](#insn-009bce6c)

~~~json
{
  "source": "009bce6c",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce70`](#insn-009bce70)

~~~json
{
  "source": "009bce70",
  "target": "009bce8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bce88`](#insn-009bce88)

~~~json
{
  "source": "009bce88",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bce94`](#insn-009bce94)

~~~json
{
  "source": "009bce94",
  "target": "009bcea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcea0`](#insn-009bcea0)

~~~json
{
  "source": "009bcea0",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcea4`](#insn-009bcea4)

~~~json
{
  "source": "009bcea4",
  "target": "009bceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcea8`](#insn-009bcea8)

~~~json
{
  "source": "009bcea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bceac`](#insn-009bceac)

~~~json
{
  "source": "009bceac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcec8`](#insn-009bcec8)

~~~json
{
  "source": "009bcec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcecc`](#insn-009bcecc)

~~~json
{
  "source": "009bcecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bced0`](#insn-009bced0)

~~~json
{
  "source": "009bced0",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
