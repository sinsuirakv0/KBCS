# 009bcbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009870dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009870dc.md) · 移動量 `+0x35ae0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0012.md#compare-4f7ad2c0040e14315edc5d459c667638)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `009bcd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0056.md#compare-6047d1414b90dc54c3b645e860700b98)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009bcbbc",
  "name": "FUN_009bcbbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3",
  "source_text_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009bcbbc",
        "009bcce3"
      ]
    ],
    "bytes_sha256": "337ed6df3590f3624e5dc5cba0a0129af3534847be0340b43b236ef0d85f9c11",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [009bd99c](../009bd/009bd99c.md)
- [009bdae4](../009bd/009bdae4.md)

## 呼び出し先

- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1708 bytes

~~~c

void FUN_009bcbbc(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[1];
                    /* try { // try from 009bcbd0 to 00abcccb has its CatchHandler @ 009bc884 */
  *param_1 = 0;
  param_1[1] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[3];
  param_1[2] = 0;
  param_1[3] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[5];
  param_1[4] = 0;
  param_1[5] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[7];
  param_1[6] = 0;
  param_1[7] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[9];
  param_1[8] = 0;
  param_1[9] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* try { // try from 009bcccc to 00abcce3 has its CatchHandler @ 009bda34 */
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
<a id="insn-009bcbbc"></a> `009bcbbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009bcbc0"></a> `009bcbc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bcbc4"></a> `009bcbc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009bcbc8"></a> `009bcbc8` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009bcbcc"></a> `009bcbcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009bcbd0"></a> `009bcbd0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-009bcbd4"></a> `009bcbd4` | `74 01 00 b4` | cbz x20,0x009bcc00 | `CONDITIONAL_JUMP`
<a id="insn-009bcbd8"></a> `009bcbd8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bcbdc"></a> `009bcbdc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcbe0"></a> `009bcbe0` | `40 5b 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcbe4"></a> `009bcbe4` | `e0 00 00 b5` | cbnz x0,0x009bcc00 | `CONDITIONAL_JUMP`
<a id="insn-009bcbe8"></a> `009bcbe8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bcbec"></a> `009bcbec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcbf0"></a> `009bcbf0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcbf4"></a> `009bcbf4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcbf8"></a> `009bcbf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcbfc"></a> `009bcbfc` | `a1 6b 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc00"></a> `009bcc00` | `74 0e 40 f9` | ldr x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-009bcc04"></a> `009bcc04` | `7f 7e 01 a9` | stp xzr,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-009bcc08"></a> `009bcc08` | `74 01 00 b4` | cbz x20,0x009bcc34 | `CONDITIONAL_JUMP`
<a id="insn-009bcc0c"></a> `009bcc0c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bcc10"></a> `009bcc10` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcc14"></a> `009bcc14` | `33 5b 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc18"></a> `009bcc18` | `e0 00 00 b5` | cbnz x0,0x009bcc34 | `CONDITIONAL_JUMP`
<a id="insn-009bcc1c"></a> `009bcc1c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bcc20"></a> `009bcc20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc24"></a> `009bcc24` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcc28"></a> `009bcc28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcc2c"></a> `009bcc2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc30"></a> `009bcc30` | `94 6b 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc34"></a> `009bcc34` | `74 16 40 f9` | ldr x20,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-009bcc38"></a> `009bcc38` | `7f 7e 02 a9` | stp xzr,xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-009bcc3c"></a> `009bcc3c` | `74 01 00 b4` | cbz x20,0x009bcc68 | `CONDITIONAL_JUMP`
<a id="insn-009bcc40"></a> `009bcc40` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bcc44"></a> `009bcc44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcc48"></a> `009bcc48` | `26 5b 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc4c"></a> `009bcc4c` | `e0 00 00 b5` | cbnz x0,0x009bcc68 | `CONDITIONAL_JUMP`
<a id="insn-009bcc50"></a> `009bcc50` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bcc54"></a> `009bcc54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc58"></a> `009bcc58` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcc5c"></a> `009bcc5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcc60"></a> `009bcc60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc64"></a> `009bcc64` | `87 6b 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc68"></a> `009bcc68` | `74 1e 40 f9` | ldr x20,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-009bcc6c"></a> `009bcc6c` | `7f 7e 03 a9` | stp xzr,xzr,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-009bcc70"></a> `009bcc70` | `74 01 00 b4` | cbz x20,0x009bcc9c | `CONDITIONAL_JUMP`
<a id="insn-009bcc74"></a> `009bcc74` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bcc78"></a> `009bcc78` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bcc7c"></a> `009bcc7c` | `19 5b 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc80"></a> `009bcc80` | `e0 00 00 b5` | cbnz x0,0x009bcc9c | `CONDITIONAL_JUMP`
<a id="insn-009bcc84"></a> `009bcc84` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bcc88"></a> `009bcc88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc8c"></a> `009bcc8c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bcc90"></a> `009bcc90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bcc94"></a> `009bcc94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcc98"></a> `009bcc98` | `7a 6b 0a 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-009bcc9c"></a> `009bcc9c` | `74 26 40 f9` | ldr x20,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-009bcca0"></a> `009bcca0` | `7f 7e 04 a9` | stp xzr,xzr,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-009bcca4"></a> `009bcca4` | `b4 00 00 b4` | cbz x20,0x009bccb8 | `CONDITIONAL_JUMP`
<a id="insn-009bcca8"></a> `009bcca8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009bccac"></a> `009bccac` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009bccb0"></a> `009bccb0` | `0c 5b 0a 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-009bccb4"></a> `009bccb4` | `80 00 00 b4` | cbz x0,0x009bccc4 | `CONDITIONAL_JUMP`
<a id="insn-009bccb8"></a> `009bccb8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bccbc"></a> `009bccbc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009bccc0"></a> `009bccc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009bccc4"></a> `009bccc4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009bccc8"></a> `009bccc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bcccc"></a> `009bcccc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009bccd0"></a> `009bccd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009bccd4"></a> `009bccd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bccd8"></a> `009bccd8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009bccdc"></a> `009bccdc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009bcce0"></a> `009bcce0` | `68 6b 0a 14` | b 0x00c57a80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009bcbbc`](#insn-009bcbbc) 範囲 `[['009bcbbc', '009bcbcf']]`
  - `FALL_THROUGH` [`009bcbcc`](#insn-009bcbcc) → [`009bcbd0`](#insn-009bcbd0)
- ブロック [`009bcbd0`](#insn-009bcbd0) 範囲 `[['009bcbd0', '009bcbd7']]`
  - `CONDITIONAL_JUMP` [`009bcbd4`](#insn-009bcbd4) → [`009bcc00`](#insn-009bcc00)
  - `FALL_THROUGH` [`009bcbd4`](#insn-009bcbd4) → [`009bcbd8`](#insn-009bcbd8)
- ブロック [`009bcbd8`](#insn-009bcbd8) 範囲 `[['009bcbd8', '009bcbe7']]`
  - `CONDITIONAL_JUMP` [`009bcbe4`](#insn-009bcbe4) → [`009bcc00`](#insn-009bcc00)
  - `FALL_THROUGH` [`009bcbe4`](#insn-009bcbe4) → [`009bcbe8`](#insn-009bcbe8)
- ブロック [`009bcbe8`](#insn-009bcbe8) 範囲 `[['009bcbe8', '009bcbff']]`
  - `FALL_THROUGH` [`009bcbfc`](#insn-009bcbfc) → [`009bcc00`](#insn-009bcc00)
- ブロック [`009bcc00`](#insn-009bcc00) 範囲 `[['009bcc00', '009bcc0b']]`
  - `CONDITIONAL_JUMP` [`009bcc08`](#insn-009bcc08) → [`009bcc34`](#insn-009bcc34)
  - `FALL_THROUGH` [`009bcc08`](#insn-009bcc08) → [`009bcc0c`](#insn-009bcc0c)
- ブロック [`009bcc0c`](#insn-009bcc0c) 範囲 `[['009bcc0c', '009bcc1b']]`
  - `CONDITIONAL_JUMP` [`009bcc18`](#insn-009bcc18) → [`009bcc34`](#insn-009bcc34)
  - `FALL_THROUGH` [`009bcc18`](#insn-009bcc18) → [`009bcc1c`](#insn-009bcc1c)
- ブロック [`009bcc1c`](#insn-009bcc1c) 範囲 `[['009bcc1c', '009bcc33']]`
  - `FALL_THROUGH` [`009bcc30`](#insn-009bcc30) → [`009bcc34`](#insn-009bcc34)
- ブロック [`009bcc34`](#insn-009bcc34) 範囲 `[['009bcc34', '009bcc3f']]`
  - `CONDITIONAL_JUMP` [`009bcc3c`](#insn-009bcc3c) → [`009bcc68`](#insn-009bcc68)
  - `FALL_THROUGH` [`009bcc3c`](#insn-009bcc3c) → [`009bcc40`](#insn-009bcc40)
- ブロック [`009bcc40`](#insn-009bcc40) 範囲 `[['009bcc40', '009bcc4f']]`
  - `CONDITIONAL_JUMP` [`009bcc4c`](#insn-009bcc4c) → [`009bcc68`](#insn-009bcc68)
  - `FALL_THROUGH` [`009bcc4c`](#insn-009bcc4c) → [`009bcc50`](#insn-009bcc50)
- ブロック [`009bcc50`](#insn-009bcc50) 範囲 `[['009bcc50', '009bcc67']]`
  - `FALL_THROUGH` [`009bcc64`](#insn-009bcc64) → [`009bcc68`](#insn-009bcc68)
- ブロック [`009bcc68`](#insn-009bcc68) 範囲 `[['009bcc68', '009bcc73']]`
  - `CONDITIONAL_JUMP` [`009bcc70`](#insn-009bcc70) → [`009bcc9c`](#insn-009bcc9c)
  - `FALL_THROUGH` [`009bcc70`](#insn-009bcc70) → [`009bcc74`](#insn-009bcc74)
- ブロック [`009bcc74`](#insn-009bcc74) 範囲 `[['009bcc74', '009bcc83']]`
  - `CONDITIONAL_JUMP` [`009bcc80`](#insn-009bcc80) → [`009bcc9c`](#insn-009bcc9c)
  - `FALL_THROUGH` [`009bcc80`](#insn-009bcc80) → [`009bcc84`](#insn-009bcc84)
- ブロック [`009bcc84`](#insn-009bcc84) 範囲 `[['009bcc84', '009bcc9b']]`
  - `FALL_THROUGH` [`009bcc98`](#insn-009bcc98) → [`009bcc9c`](#insn-009bcc9c)
- ブロック [`009bcc9c`](#insn-009bcc9c) 範囲 `[['009bcc9c', '009bcca7']]`
  - `CONDITIONAL_JUMP` [`009bcca4`](#insn-009bcca4) → [`009bccb8`](#insn-009bccb8)
  - `FALL_THROUGH` [`009bcca4`](#insn-009bcca4) → [`009bcca8`](#insn-009bcca8)
- ブロック [`009bcca8`](#insn-009bcca8) 範囲 `[['009bcca8', '009bccb7']]`
  - `CONDITIONAL_JUMP` [`009bccb4`](#insn-009bccb4) → [`009bccc4`](#insn-009bccc4)
  - `FALL_THROUGH` [`009bccb4`](#insn-009bccb4) → [`009bccb8`](#insn-009bccb8)
- ブロック [`009bccb8`](#insn-009bccb8) 範囲 `[['009bccb8', '009bccc3']]`
- ブロック [`009bccc4`](#insn-009bccc4) 範囲 `[['009bccc4', '009bcccb']]`
  - `FALL_THROUGH` [`009bccc8`](#insn-009bccc8) → [`009bcccc`](#insn-009bcccc)
- ブロック [`009bcccc`](#insn-009bcccc) 範囲 `[['009bcccc', '009bcce3']]`

## 命令位置別の参照

- [`009bcbbc`](#insn-009bcbbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcbc0`](#insn-009bcbc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcbd4`](#insn-009bcbd4) → [`009bcc00`](#insn-009bcc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcbe0`](#insn-009bcbe0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009bcbe4`](#insn-009bcbe4) → [`009bcc00`](#insn-009bcc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcbfc`](#insn-009bcbfc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009bcc08`](#insn-009bcc08) → [`009bcc34`](#insn-009bcc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc14`](#insn-009bcc14) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009bcc18`](#insn-009bcc18) → [`009bcc34`](#insn-009bcc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc30`](#insn-009bcc30) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009bcc3c`](#insn-009bcc3c) → [`009bcc68`](#insn-009bcc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc48`](#insn-009bcc48) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009bcc4c`](#insn-009bcc4c) → [`009bcc68`](#insn-009bcc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc64`](#insn-009bcc64) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009bcc70`](#insn-009bcc70) → [`009bcc9c`](#insn-009bcc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc7c`](#insn-009bcc7c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009bcc80`](#insn-009bcc80) → [`009bcc9c`](#insn-009bcc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcc98`](#insn-009bcc98) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`009bcca4`](#insn-009bcca4) → [`009bccb8`](#insn-009bccb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bccb0`](#insn-009bccb0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`009bccb4`](#insn-009bccb4) → [`009bccc4`](#insn-009bccc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bccb8`](#insn-009bccb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bccbc`](#insn-009bccbc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bccd8`](#insn-009bccd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bccdc`](#insn-009bccdc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bcce0`](#insn-009bcce0) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009bcbbc`](#insn-009bcbbc)

~~~json
{
  "source": "009bcbbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcbc0`](#insn-009bcbc0)

~~~json
{
  "source": "009bcbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcbd4`](#insn-009bcbd4)

~~~json
{
  "source": "009bcbd4",
  "target": "009bcc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcbe0`](#insn-009bcbe0)

~~~json
{
  "source": "009bcbe0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcbe4`](#insn-009bcbe4)

~~~json
{
  "source": "009bcbe4",
  "target": "009bcc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcbfc`](#insn-009bcbfc)

~~~json
{
  "source": "009bcbfc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc08`](#insn-009bcc08)

~~~json
{
  "source": "009bcc08",
  "target": "009bcc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc14`](#insn-009bcc14)

~~~json
{
  "source": "009bcc14",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc18`](#insn-009bcc18)

~~~json
{
  "source": "009bcc18",
  "target": "009bcc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc30`](#insn-009bcc30)

~~~json
{
  "source": "009bcc30",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc3c`](#insn-009bcc3c)

~~~json
{
  "source": "009bcc3c",
  "target": "009bcc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc48`](#insn-009bcc48)

~~~json
{
  "source": "009bcc48",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc4c`](#insn-009bcc4c)

~~~json
{
  "source": "009bcc4c",
  "target": "009bcc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc64`](#insn-009bcc64)

~~~json
{
  "source": "009bcc64",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc70`](#insn-009bcc70)

~~~json
{
  "source": "009bcc70",
  "target": "009bcc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc7c`](#insn-009bcc7c)

~~~json
{
  "source": "009bcc7c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcc80`](#insn-009bcc80)

~~~json
{
  "source": "009bcc80",
  "target": "009bcc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcc98`](#insn-009bcc98)

~~~json
{
  "source": "009bcc98",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bcca4`](#insn-009bcca4)

~~~json
{
  "source": "009bcca4",
  "target": "009bccb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bccb0`](#insn-009bccb0)

~~~json
{
  "source": "009bccb0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bccb4`](#insn-009bccb4)

~~~json
{
  "source": "009bccb4",
  "target": "009bccc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bccb8`](#insn-009bccb8)

~~~json
{
  "source": "009bccb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bccbc`](#insn-009bccbc)

~~~json
{
  "source": "009bccbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bccd8`](#insn-009bccd8)

~~~json
{
  "source": "009bccd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bccdc`](#insn-009bccdc)

~~~json
{
  "source": "009bccdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bcce0`](#insn-009bcce0)

~~~json
{
  "source": "009bcce0",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
