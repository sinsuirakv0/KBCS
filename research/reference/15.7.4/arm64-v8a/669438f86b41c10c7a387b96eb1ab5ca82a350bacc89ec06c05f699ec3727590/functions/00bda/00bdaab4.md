# 00bdaab4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdaa74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-44766fbabea9979288543268b164eb62)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c57504`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0079.md#compare-a2b6e1bdf141caa82b73acbaa3aa310b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaab4",
  "name": "FUN_00bdaab4",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82035333d70fc7d1fd7207874d7e08a5463009fabd7f120c6f28f397f9e3980f",
  "source_text_sha256": "82035333d70fc7d1fd7207874d7e08a5463009fabd7f120c6f28f397f9e3980f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaab4",
        "00bdac1b"
      ]
    ],
    "bytes_sha256": "184f08ac3ca9f4d26c92bfcc5465e4187cb6c58c14f41b6ec3263c4336ea9165",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bda3c8](../00bda/00bda3c8.md)

## 呼び出し先

- [00bd75d0](../00bd7/00bd75d0.md)
- [00bd94b0](../00bd9/00bd94b0.md)
- [00bda7cc](../00bda/00bda7cc.md)
- [00bdac1c](../00bda/00bdac1c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2015 bytes

~~~c

undefined8
FUN_00bdaab4(undefined8 param_1,ulong param_2,long param_3,ulong param_4,long param_5,
            undefined8 param_6)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  ulong uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long local_88;
  undefined1 auStack_80 [8];
  ulong local_78;
  long local_70;
  undefined1 local_68;
  
                    /* catch() { ... } // from try @ 00bda9ec with catch @ 00bdaabc */
  lVar4 = param_3 + (param_4 & 0xffffffff);
  uVar1 = FUN_00bda7cc(param_1,param_3,lVar4,auStack_80);
  if (((uVar1 & 1) != 0) && (local_78 != 0)) {
    lVar2 = FUN_00bdac1c(local_68);
    lVar7 = 0;
    do {
      if (local_78 < 2) {
        lVar8 = lVar7 * lVar2;
        break;
      }
      uVar6 = local_78 >> 1;
      lVar8 = (uVar6 + lVar7) * lVar2;
      local_88 = local_70 + lVar8;
      uVar1 = FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
      uVar5 = local_78 - uVar6;
      local_78 = uVar6;
                    /* try { // try from 00bdab64 to 00cdabb3 has its CatchHandler @ 00bdab64
                       catch() { ... } // from try @ 00bdab64 with catch @ 00bdab64
                       catch() { ... } // from try @ 00bdac08 with catch @ 00bdab64 */
      if (uVar1 < param_2) {
        local_78 = uVar5;
        lVar7 = uVar6 + lVar7;
      }
    } while (uVar1 != param_2);
    local_88 = local_70 + lVar8;
    FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
                    /* try { // try from 00bdabb4 to 00cdac07 has its CatchHandler @ 00bdac08 */
    uVar3 = FUN_00bd94b0(param_1,&local_88,lVar4,local_68,param_3);
    lVar4 = FUN_00bd75d0(param_1,uVar3,param_5,param_6,0);
    if (((lVar4 == 0) && (*(ulong *)(param_5 + 0x18) <= param_2)) &&
       (param_2 < *(ulong *)(param_5 + 0x20))) {
      return 1;
    }
  }
                    /* catch() { ... } // from try @ 00bdabb4 with catch @ 00bdac08
                       try { // try from 00bdac08 to 00cdac37 has its CatchHandler @ 00bdab64 */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaab4"></a> `00bdaab4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdaab8"></a> `00bdaab8` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bdaabc"></a> `00bdaabc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdaac0"></a> `00bdaac0` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdaac4"></a> `00bdaac4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdaac8"></a> `00bdaac8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdaacc"></a> `00bdaacc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdaad0"></a> `00bdaad0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdaad4"></a> `00bdaad4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdaad8"></a> `00bdaad8` | `58 40 23 8b` | add x24,x2,w3, UXTW  | `FALL_THROUGH`
<a id="insn-00bdaadc"></a> `00bdaadc` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bdaae0"></a> `00bdaae0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bdaae4"></a> `00bdaae4` | `e3 83 00 91` | add x3,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdaae8"></a> `00bdaae8` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00bdaaec"></a> `00bdaaec` | `f5 03 05 aa` | mov x21,x5 | `FALL_THROUGH`
<a id="insn-00bdaaf0"></a> `00bdaaf0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bdaaf4"></a> `00bdaaf4` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bdaaf8"></a> `00bdaaf8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdaafc"></a> `00bdaafc` | `34 ff ff 97` | bl 0x00bda7cc | `UNCONDITIONAL_CALL`
<a id="insn-00bdab00"></a> `00bdab00` | `a0 07 00 36` | tbz w0,#0x0,0x00bdabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdab04"></a> `00bdab04` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdab08"></a> `00bdab08` | `68 07 00 b4` | cbz x8,0x00bdabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdab0c"></a> `00bdab0c` | `e0 e3 40 39` | ldrb w0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdab10"></a> `00bdab10` | `f5 cf 00 a9` | stp x21,x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdab14"></a> `00bdab14` | `42 00 00 94` | bl 0x00bdac1c | `UNCONDITIONAL_CALL`
<a id="insn-00bdab18"></a> `00bdab18` | `fb 17 40 f9` | ldr x27,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdab1c"></a> `00bdab1c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdab20"></a> `00bdab20` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00bdab24"></a> `00bdab24` | `7f 07 00 f1` | cmp x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bdab28"></a> `00bdab28` | `69 02 00 54` | b.ls 0x00bdab74 | `CONDITIONAL_JUMP`
<a id="insn-00bdab2c"></a> `00bdab2c` | `75 ff 41 d3` | lsr x21,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bdab30"></a> `00bdab30` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdab34"></a> `00bdab34` | `e3 e3 40 39` | ldrb w3,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdab38"></a> `00bdab38` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdab3c"></a> `00bdab3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdab40"></a> `00bdab40` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bdab44"></a> `00bdab44` | `b3 02 1a 8b` | add x19,x21,x26 | `FALL_THROUGH`
<a id="insn-00bdab48"></a> `00bdab48` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdab4c"></a> `00bdab4c` | `7c 7e 19 9b` | mul x28,x19,x25 | `FALL_THROUGH`
<a id="insn-00bdab50"></a> `00bdab50` | `08 01 1c 8b` | add x8,x8,x28 | `FALL_THROUGH`
<a id="insn-00bdab54"></a> `00bdab54` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdab58"></a> `00bdab58` | `56 fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab5c"></a> `00bdab5c` | `68 03 15 cb` | sub x8,x27,x21 | `FALL_THROUGH`
<a id="insn-00bdab60"></a> `00bdab60` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00bdab64"></a> `00bdab64` | `5a 23 93 9a` | csel x26,x26,x19,cs | `FALL_THROUGH`
<a id="insn-00bdab68"></a> `00bdab68` | `bb 22 88 9a` | csel x27,x21,x8,cs | `FALL_THROUGH`
<a id="insn-00bdab6c"></a> `00bdab6c` | `c1 fd ff 54` | b.ne 0x00bdab24 | `CONDITIONAL_JUMP`
<a id="insn-00bdab70"></a> `00bdab70` | `02 00 00 14` | b 0x00bdab78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdab74"></a> `00bdab74` | `5c 7f 19 9b` | mul x28,x26,x25 | `FALL_THROUGH`
<a id="insn-00bdab78"></a> `00bdab78` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdab7c"></a> `00bdab7c` | `f9 e3 40 39` | ldrb w25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdab80"></a> `00bdab80` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdab84"></a> `00bdab84` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdab88"></a> `00bdab88` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bdab8c"></a> `00bdab8c` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdab90"></a> `00bdab90` | `08 01 1c 8b` | add x8,x8,x28 | `FALL_THROUGH`
<a id="insn-00bdab94"></a> `00bdab94` | `e3 03 19 2a` | mov w3,w25 | `FALL_THROUGH`
<a id="insn-00bdab98"></a> `00bdab98` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdab9c"></a> `00bdab9c` | `45 fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaba0"></a> `00bdaba0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bdaba4"></a> `00bdaba4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdaba8"></a> `00bdaba8` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bdabac"></a> `00bdabac` | `e3 03 19 2a` | mov w3,w25 | `FALL_THROUGH`
<a id="insn-00bdabb0"></a> `00bdabb0` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdabb4"></a> `00bdabb4` | `3f fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabb8"></a> `00bdabb8` | `e3 cf 40 a9` | ldp x3,x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdabbc"></a> `00bdabbc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdabc0"></a> `00bdabc0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdabc4"></a> `00bdabc4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdabc8"></a> `00bdabc8` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bdabcc"></a> `00bdabcc` | `81 f2 ff 97` | bl 0x00bd75d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabd0"></a> `00bdabd0` | `20 01 00 b5` | cbnz x0,0x00bdabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdabd4"></a> `00bdabd4` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bdabd8"></a> `00bdabd8` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bdabdc"></a> `00bdabdc` | `c8 00 00 54` | b.hi 0x00bdabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdabe0"></a> `00bdabe0` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bdabe4"></a> `00bdabe4` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bdabe8"></a> `00bdabe8` | `69 00 00 54` | b.ls 0x00bdabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdabec"></a> `00bdabec` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdabf0"></a> `00bdabf0` | `02 00 00 14` | b 0x00bdabf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdabf4"></a> `00bdabf4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdabf8"></a> `00bdabf8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdabfc"></a> `00bdabfc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdac00"></a> `00bdac00` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdac04"></a> `00bdac04` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdac08"></a> `00bdac08` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdac0c"></a> `00bdac0c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdac10"></a> `00bdac10` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bdac14"></a> `00bdac14` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdac18"></a> `00bdac18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaab4`](#insn-00bdaab4) 範囲 `[['00bdaab4', '00bdaabb']]`
  - `FALL_THROUGH` [`00bdaab8`](#insn-00bdaab8) → [`00bdaabc`](#insn-00bdaabc)
- ブロック [`00bdaabc`](#insn-00bdaabc) 範囲 `[['00bdaabc', '00bdab03']]`
  - `CONDITIONAL_JUMP` [`00bdab00`](#insn-00bdab00) → [`00bdabf4`](#insn-00bdabf4)
  - `FALL_THROUGH` [`00bdab00`](#insn-00bdab00) → [`00bdab04`](#insn-00bdab04)
- ブロック [`00bdab04`](#insn-00bdab04) 範囲 `[['00bdab04', '00bdab0b']]`
  - `CONDITIONAL_JUMP` [`00bdab08`](#insn-00bdab08) → [`00bdabf4`](#insn-00bdabf4)
  - `FALL_THROUGH` [`00bdab08`](#insn-00bdab08) → [`00bdab0c`](#insn-00bdab0c)
- ブロック [`00bdab0c`](#insn-00bdab0c) 範囲 `[['00bdab0c', '00bdab23']]`
  - `FALL_THROUGH` [`00bdab20`](#insn-00bdab20) → [`00bdab24`](#insn-00bdab24)
- ブロック [`00bdab24`](#insn-00bdab24) 範囲 `[['00bdab24', '00bdab2b']]`
  - `CONDITIONAL_JUMP` [`00bdab28`](#insn-00bdab28) → [`00bdab74`](#insn-00bdab74)
  - `FALL_THROUGH` [`00bdab28`](#insn-00bdab28) → [`00bdab2c`](#insn-00bdab2c)
- ブロック [`00bdab2c`](#insn-00bdab2c) 範囲 `[['00bdab2c', '00bdab63']]`
  - `FALL_THROUGH` [`00bdab60`](#insn-00bdab60) → [`00bdab64`](#insn-00bdab64)
- ブロック [`00bdab64`](#insn-00bdab64) 範囲 `[['00bdab64', '00bdab6f']]`
  - `CONDITIONAL_JUMP` [`00bdab6c`](#insn-00bdab6c) → [`00bdab24`](#insn-00bdab24)
  - `FALL_THROUGH` [`00bdab6c`](#insn-00bdab6c) → [`00bdab70`](#insn-00bdab70)
- ブロック [`00bdab70`](#insn-00bdab70) 範囲 `[['00bdab70', '00bdab73']]`
  - `UNCONDITIONAL_JUMP` [`00bdab70`](#insn-00bdab70) → [`00bdab78`](#insn-00bdab78)
- ブロック [`00bdab74`](#insn-00bdab74) 範囲 `[['00bdab74', '00bdab77']]`
  - `FALL_THROUGH` [`00bdab74`](#insn-00bdab74) → [`00bdab78`](#insn-00bdab78)
- ブロック [`00bdab78`](#insn-00bdab78) 範囲 `[['00bdab78', '00bdabb3']]`
  - `FALL_THROUGH` [`00bdabb0`](#insn-00bdabb0) → [`00bdabb4`](#insn-00bdabb4)
- ブロック [`00bdabb4`](#insn-00bdabb4) 範囲 `[['00bdabb4', '00bdabd3']]`
  - `CONDITIONAL_JUMP` [`00bdabd0`](#insn-00bdabd0) → [`00bdabf4`](#insn-00bdabf4)
  - `FALL_THROUGH` [`00bdabd0`](#insn-00bdabd0) → [`00bdabd4`](#insn-00bdabd4)
- ブロック [`00bdabd4`](#insn-00bdabd4) 範囲 `[['00bdabd4', '00bdabdf']]`
  - `CONDITIONAL_JUMP` [`00bdabdc`](#insn-00bdabdc) → [`00bdabf4`](#insn-00bdabf4)
  - `FALL_THROUGH` [`00bdabdc`](#insn-00bdabdc) → [`00bdabe0`](#insn-00bdabe0)
- ブロック [`00bdabe0`](#insn-00bdabe0) 範囲 `[['00bdabe0', '00bdabeb']]`
  - `CONDITIONAL_JUMP` [`00bdabe8`](#insn-00bdabe8) → [`00bdabf4`](#insn-00bdabf4)
  - `FALL_THROUGH` [`00bdabe8`](#insn-00bdabe8) → [`00bdabec`](#insn-00bdabec)
- ブロック [`00bdabec`](#insn-00bdabec) 範囲 `[['00bdabec', '00bdabf3']]`
  - `UNCONDITIONAL_JUMP` [`00bdabf0`](#insn-00bdabf0) → [`00bdabf8`](#insn-00bdabf8)
- ブロック [`00bdabf4`](#insn-00bdabf4) 範囲 `[['00bdabf4', '00bdabf7']]`
  - `FALL_THROUGH` [`00bdabf4`](#insn-00bdabf4) → [`00bdabf8`](#insn-00bdabf8)
- ブロック [`00bdabf8`](#insn-00bdabf8) 範囲 `[['00bdabf8', '00bdac07']]`
  - `FALL_THROUGH` [`00bdac04`](#insn-00bdac04) → [`00bdac08`](#insn-00bdac08)
- ブロック [`00bdac08`](#insn-00bdac08) 範囲 `[['00bdac08', '00bdac1b']]`

## 命令位置別の参照

- [`00bdaabc`](#insn-00bdaabc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaac0`](#insn-00bdaac0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaac4`](#insn-00bdaac4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaac8`](#insn-00bdaac8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaacc`](#insn-00bdaacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaad0`](#insn-00bdaad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaafc`](#insn-00bdaafc) → [`00bda7cc`](00bda7cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bda7cc` · 推定シンボル `None` · 推定型 `None`
- [`00bdab00`](#insn-00bdab00) → [`00bdabf4`](#insn-00bdabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab04`](#insn-00bdab04) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab08`](#insn-00bdab08) → [`00bdabf4`](#insn-00bdabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab0c`](#insn-00bdab0c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab10`](#insn-00bdab10) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab14`](#insn-00bdab14) → [`00bdac1c`](00bdac1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdac1c` · 推定シンボル `None` · 推定型 `None`
- [`00bdab18`](#insn-00bdab18) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab28`](#insn-00bdab28) → [`00bdab74`](#insn-00bdab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab30`](#insn-00bdab30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab34`](#insn-00bdab34) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab54`](#insn-00bdab54) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab58`](#insn-00bdab58) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdab6c`](#insn-00bdab6c) → [`00bdab24`](#insn-00bdab24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab70`](#insn-00bdab70) → [`00bdab78`](#insn-00bdab78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab78`](#insn-00bdab78) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab7c`](#insn-00bdab7c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab98`](#insn-00bdab98) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab9c`](#insn-00bdab9c) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdabb4`](#insn-00bdabb4) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdabb8`](#insn-00bdabb8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabcc`](#insn-00bdabcc) → [`00bd75d0`](../00bd7/00bd75d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd75d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdabd0`](#insn-00bdabd0) → [`00bdabf4`](#insn-00bdabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabdc`](#insn-00bdabdc) → [`00bdabf4`](#insn-00bdabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabe8`](#insn-00bdabe8) → [`00bdabf4`](#insn-00bdabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabf0`](#insn-00bdabf0) → [`00bdabf8`](#insn-00bdabf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabf8`](#insn-00bdabf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabfc`](#insn-00bdabfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac00`](#insn-00bdac00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac04`](#insn-00bdac04) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac08`](#insn-00bdac08) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac0c`](#insn-00bdac0c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaabc`](#insn-00bdaabc)

~~~json
{
  "source": "00bdaabc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaac0`](#insn-00bdaac0)

~~~json
{
  "source": "00bdaac0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaac4`](#insn-00bdaac4)

~~~json
{
  "source": "00bdaac4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaac8`](#insn-00bdaac8)

~~~json
{
  "source": "00bdaac8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaacc`](#insn-00bdaacc)

~~~json
{
  "source": "00bdaacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaad0`](#insn-00bdaad0)

~~~json
{
  "source": "00bdaad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaafc`](#insn-00bdaafc)

~~~json
{
  "source": "00bdaafc",
  "target": "00bda7cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab00`](#insn-00bdab00)

~~~json
{
  "source": "00bdab00",
  "target": "00bdabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab04`](#insn-00bdab04)

~~~json
{
  "source": "00bdab04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab08`](#insn-00bdab08)

~~~json
{
  "source": "00bdab08",
  "target": "00bdabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab0c`](#insn-00bdab0c)

~~~json
{
  "source": "00bdab0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab10`](#insn-00bdab10)

~~~json
{
  "source": "00bdab10",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab14`](#insn-00bdab14)

~~~json
{
  "source": "00bdab14",
  "target": "00bdac1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab18`](#insn-00bdab18)

~~~json
{
  "source": "00bdab18",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab28`](#insn-00bdab28)

~~~json
{
  "source": "00bdab28",
  "target": "00bdab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab30`](#insn-00bdab30)

~~~json
{
  "source": "00bdab30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab34`](#insn-00bdab34)

~~~json
{
  "source": "00bdab34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab54`](#insn-00bdab54)

~~~json
{
  "source": "00bdab54",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab58`](#insn-00bdab58)

~~~json
{
  "source": "00bdab58",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab6c`](#insn-00bdab6c)

~~~json
{
  "source": "00bdab6c",
  "target": "00bdab24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab70`](#insn-00bdab70)

~~~json
{
  "source": "00bdab70",
  "target": "00bdab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab78`](#insn-00bdab78)

~~~json
{
  "source": "00bdab78",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab7c`](#insn-00bdab7c)

~~~json
{
  "source": "00bdab7c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab98`](#insn-00bdab98)

~~~json
{
  "source": "00bdab98",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab9c`](#insn-00bdab9c)

~~~json
{
  "source": "00bdab9c",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabb4`](#insn-00bdabb4)

~~~json
{
  "source": "00bdabb4",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabb8`](#insn-00bdabb8)

~~~json
{
  "source": "00bdabb8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabcc`](#insn-00bdabcc)

~~~json
{
  "source": "00bdabcc",
  "target": "00bd75d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabd0`](#insn-00bdabd0)

~~~json
{
  "source": "00bdabd0",
  "target": "00bdabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabdc`](#insn-00bdabdc)

~~~json
{
  "source": "00bdabdc",
  "target": "00bdabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabe8`](#insn-00bdabe8)

~~~json
{
  "source": "00bdabe8",
  "target": "00bdabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabf0`](#insn-00bdabf0)

~~~json
{
  "source": "00bdabf0",
  "target": "00bdabf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabf8`](#insn-00bdabf8)

~~~json
{
  "source": "00bdabf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabfc`](#insn-00bdabfc)

~~~json
{
  "source": "00bdabfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac00`](#insn-00bdac00)

~~~json
{
  "source": "00bdac00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac04`](#insn-00bdac04)

~~~json
{
  "source": "00bdac04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac08`](#insn-00bdac08)

~~~json
{
  "source": "00bdac08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac0c`](#insn-00bdac0c)

~~~json
{
  "source": "00bdac0c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
