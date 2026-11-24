# 007ecdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007ecdec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ec/007ecdec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0012.md#compare-a6de0b624d4fde0d1a5b7fcc5601580f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0058.md#review-bacb3358b0254629523536b4eadf7a79)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ecdec",
  "name": "FUN_007ecdec",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4988251fa489bd0d905c7e76869ed85affd989d2cf1c1da7d43afe781fa626a",
  "source_text_sha256": "d4988251fa489bd0d905c7e76869ed85affd989d2cf1c1da7d43afe781fa626a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ecdec",
        "007ecf0f"
      ]
    ],
    "bytes_sha256": "7cfa4e1b324e56f13c0e254f360d1ce983534f7f45b644e9454af644f1dc10d1",
    "instruction_count": 73,
    "instruction_bytes": 292,
    "body_bytes": 292,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0099a654](../0099a/0099a654.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [007eca30](../007ec/007eca30.md)
- [007ecd04](../007ec/007ecd04.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2007 bytes

~~~c

byte FUN_007ecdec(long param_1,int param_2,long param_3)

{
  long *plVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  
  plVar5 = (long *)(param_1 + 200);
  plVar6 = (long *)*plVar5;
  plVar7 = plVar5;
  if (plVar6 != (long *)0x0) {
    do {
      if (param_2 <= *(int *)((long)plVar6 + 0x1c)) {
        plVar7 = plVar6;
      }
      plVar6 = (long *)plVar6[*(int *)((long)plVar6 + 0x1c) < param_2];
    } while (plVar6 != (long *)0x0);
                    /* try { // try from 007ece34 to 008ece43 has its CatchHandler @ 007ee4ac */
    if ((plVar7 != plVar5) && (*(int *)((long)plVar7 + 0x1c) <= param_2)) {
      bVar2 = FUN_007ecd04();
      bVar3 = FUN_007eca30(param_1,param_2);
      bVar4 = bVar2 & bVar3;
      if (((bVar2 & 1) != 0) || ((bVar3 & 1) == 0)) goto LAB_007ece40;
      plVar8 = (long *)(param_1 + 0xe0);
      plVar6 = (long *)*plVar8;
      plVar7 = plVar8;
      plVar5 = plVar6;
      if (plVar6 != (long *)0x0) {
        do {
          if (param_2 <= (int)plVar5[4]) {
            plVar7 = plVar5;
          }
          plVar1 = plVar5 + ((int)plVar5[4] < param_2);
          plVar5 = (long *)*plVar1;
        } while ((long *)*plVar1 != (long *)0x0);
        if ((plVar7 != plVar8) && ((int)plVar7[4] <= param_2)) {
          do {
            while (param_2 < (int)plVar6[4]) {
              plVar6 = (long *)*plVar6;
              if (plVar6 == (long *)0x0) goto LAB_007ecef4;
            }
            if (param_2 <= (int)plVar6[4]) {
              bVar4 = plVar6[5] < param_3;
              goto LAB_007ece40;
            }
            plVar6 = (long *)plVar6[1];
          } while (plVar6 != (long *)0x0);
LAB_007ecef4:
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("map::at:  key not found");
        }
      }
    }
  }
  bVar4 = 1;
LAB_007ece40:
                    /* try { // try from 007ece50 to 008ed057 has its CatchHandler @ 007ee4d4 */
  return bVar4 & 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ecdec"></a> `007ecdec` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-007ecdf0"></a> `007ecdf0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ecdf4"></a> `007ecdf4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ecdf8"></a> `007ecdf8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007ecdfc"></a> `007ecdfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007ece00"></a> `007ece00` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-007ece04"></a> `007ece04` | `09 8d 4c f8` | ldr x9,[x8, #0xc8]! | `FALL_THROUGH`
<a id="insn-007ece08"></a> `007ece08` | `a9 01 00 b4` | cbz x9,0x007ece3c | `CONDITIONAL_JUMP`
<a id="insn-007ece0c"></a> `007ece0c` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-007ece10"></a> `007ece10` | `2b 1d 40 b9` | ldr w11,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-007ece14"></a> `007ece14` | `7f 01 01 6b` | cmp w11,w1 | `FALL_THROUGH`
<a id="insn-007ece18"></a> `007ece18` | `eb a7 9f 1a` | cset w11,lt | `FALL_THROUGH`
<a id="insn-007ece1c"></a> `007ece1c` | `4a b1 89 9a` | csel x10,x10,x9,lt | `FALL_THROUGH`
<a id="insn-007ece20"></a> `007ece20` | `29 59 6b f8` | ldr x9,[x9, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-007ece24"></a> `007ece24` | `69 ff ff b5` | cbnz x9,0x007ece10 | `CONDITIONAL_JUMP`
<a id="insn-007ece28"></a> `007ece28` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-007ece2c"></a> `007ece2c` | `80 00 00 54` | b.eq 0x007ece3c | `CONDITIONAL_JUMP`
<a id="insn-007ece30"></a> `007ece30` | `48 1d 40 b9` | ldr w8,[x10, #0x1c] | `FALL_THROUGH`
<a id="insn-007ece34"></a> `007ece34` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-007ece38"></a> `007ece38` | `0d 01 00 54` | b.le 0x007ece58 | `CONDITIONAL_JUMP`
<a id="insn-007ece3c"></a> `007ece3c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-007ece40"></a> `007ece40` | `00 01 00 12` | and w0,w8,#0x1 | `FALL_THROUGH`
<a id="insn-007ece44"></a> `007ece44` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007ece48"></a> `007ece48` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ece4c"></a> `007ece4c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ece50"></a> `007ece50` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-007ece54"></a> `007ece54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ece58"></a> `007ece58` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-007ece5c"></a> `007ece5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ece60"></a> `007ece60` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-007ece64"></a> `007ece64` | `a8 ff ff 97` | bl 0x007ecd04 | `UNCONDITIONAL_CALL`
<a id="insn-007ece68"></a> `007ece68` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-007ece6c"></a> `007ece6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ece70"></a> `007ece70` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-007ece74"></a> `007ece74` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-007ece78"></a> `007ece78` | `f3 03 14 2a` | mov w19,w20 | `FALL_THROUGH`
<a id="insn-007ece7c"></a> `007ece7c` | `ed fe ff 97` | bl 0x007eca30 | `UNCONDITIONAL_CALL`
<a id="insn-007ece80"></a> `007ece80` | `a8 02 00 0a` | and w8,w21,w0 | `FALL_THROUGH`
<a id="insn-007ece84"></a> `007ece84` | `f5 fd 07 37` | tbnz w21,#0x0,0x007ece40 | `CONDITIONAL_JUMP`
<a id="insn-007ece88"></a> `007ece88` | `c0 fd 07 36` | tbz w0,#0x0,0x007ece40 | `CONDITIONAL_JUMP`
<a id="insn-007ece8c"></a> `007ece8c` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-007ece90"></a> `007ece90` | `48 0d 4e f8` | ldr x8,[x10, #0xe0]! | `FALL_THROUGH`
<a id="insn-007ece94"></a> `007ece94` | `48 fd ff b4` | cbz x8,0x007ece3c | `CONDITIONAL_JUMP`
<a id="insn-007ece98"></a> `007ece98` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-007ece9c"></a> `007ece9c` | `ec 03 08 aa` | mov x12,x8 | `FALL_THROUGH`
<a id="insn-007ecea0"></a> `007ecea0` | `e9 03 13 2a` | mov w9,w19 | `FALL_THROUGH`
<a id="insn-007ecea4"></a> `007ecea4` | `8d 21 40 b9` | ldr w13,[x12, #0x20] | `FALL_THROUGH`
<a id="insn-007ecea8"></a> `007ecea8` | `bf 01 09 6b` | cmp w13,w9 | `FALL_THROUGH`
<a id="insn-007eceac"></a> `007eceac` | `ed a7 9f 1a` | cset w13,lt | `FALL_THROUGH`
<a id="insn-007eceb0"></a> `007eceb0` | `6b b1 8c 9a` | csel x11,x11,x12,lt | `FALL_THROUGH`
<a id="insn-007eceb4"></a> `007eceb4` | `8c 59 6d f8` | ldr x12,[x12, w13, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-007eceb8"></a> `007eceb8` | `6c ff ff b5` | cbnz x12,0x007ecea4 | `CONDITIONAL_JUMP`
<a id="insn-007ecebc"></a> `007ecebc` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-007ecec0"></a> `007ecec0` | `e0 fb ff 54` | b.eq 0x007ece3c | `CONDITIONAL_JUMP`
<a id="insn-007ecec4"></a> `007ecec4` | `6a 21 40 b9` | ldr w10,[x11, #0x20] | `FALL_THROUGH`
<a id="insn-007ecec8"></a> `007ecec8` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-007ececc"></a> `007ececc` | `8d 00 00 54` | b.le 0x007ecedc | `CONDITIONAL_JUMP`
<a id="insn-007eced0"></a> `007eced0` | `db ff ff 17` | b 0x007ece3c | `UNCONDITIONAL_JUMP`
<a id="insn-007eced4"></a> `007eced4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-007eced8"></a> `007eced8` | `e8 00 00 b4` | cbz x8,0x007ecef4 | `CONDITIONAL_JUMP`
<a id="insn-007ecedc"></a> `007ecedc` | `0a 21 40 b9` | ldr w10,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-007ecee0"></a> `007ecee0` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-007ecee4"></a> `007ecee4` | `8c ff ff 54` | b.gt 0x007eced4 | `CONDITIONAL_JUMP`
<a id="insn-007ecee8"></a> `007ecee8` | `ca 00 00 54` | b.ge 0x007ecf00 | `CONDITIONAL_JUMP`
<a id="insn-007eceec"></a> `007eceec` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-007ecef0"></a> `007ecef0` | `68 ff ff b5` | cbnz x8,0x007ecedc | `CONDITIONAL_JUMP`
<a id="insn-007ecef4"></a> `007ecef4` | `20 d5 ff 90` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-007ecef8"></a> `007ecef8` | `00 b8 2e 91` | add x0,x0,#0xbae | `FALL_THROUGH`
<a id="insn-007ecefc"></a> `007ecefc` | `bd cb f0 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-007ecf00"></a> `007ecf00` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-007ecf04"></a> `007ecf04` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-007ecf08"></a> `007ecf08` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-007ecf0c"></a> `007ecf0c` | `cd ff ff 17` | b 0x007ece40 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`007ecdec`](#insn-007ecdec) 範囲 `[['007ecdec', '007ece0b']]`
  - `CONDITIONAL_JUMP` [`007ece08`](#insn-007ece08) → [`007ece3c`](#insn-007ece3c)
  - `FALL_THROUGH` [`007ece08`](#insn-007ece08) → [`007ece0c`](#insn-007ece0c)
- ブロック [`007ece0c`](#insn-007ece0c) 範囲 `[['007ece0c', '007ece0f']]`
  - `FALL_THROUGH` [`007ece0c`](#insn-007ece0c) → [`007ece10`](#insn-007ece10)
- ブロック [`007ece10`](#insn-007ece10) 範囲 `[['007ece10', '007ece27']]`
  - `CONDITIONAL_JUMP` [`007ece24`](#insn-007ece24) → [`007ece10`](#insn-007ece10)
  - `FALL_THROUGH` [`007ece24`](#insn-007ece24) → [`007ece28`](#insn-007ece28)
- ブロック [`007ece28`](#insn-007ece28) 範囲 `[['007ece28', '007ece2f']]`
  - `CONDITIONAL_JUMP` [`007ece2c`](#insn-007ece2c) → [`007ece3c`](#insn-007ece3c)
  - `FALL_THROUGH` [`007ece2c`](#insn-007ece2c) → [`007ece30`](#insn-007ece30)
- ブロック [`007ece30`](#insn-007ece30) 範囲 `[['007ece30', '007ece33']]`
  - `FALL_THROUGH` [`007ece30`](#insn-007ece30) → [`007ece34`](#insn-007ece34)
- ブロック [`007ece34`](#insn-007ece34) 範囲 `[['007ece34', '007ece3b']]`
  - `CONDITIONAL_JUMP` [`007ece38`](#insn-007ece38) → [`007ece58`](#insn-007ece58)
  - `FALL_THROUGH` [`007ece38`](#insn-007ece38) → [`007ece3c`](#insn-007ece3c)
- ブロック [`007ece3c`](#insn-007ece3c) 範囲 `[['007ece3c', '007ece3f']]`
  - `FALL_THROUGH` [`007ece3c`](#insn-007ece3c) → [`007ece40`](#insn-007ece40)
- ブロック [`007ece40`](#insn-007ece40) 範囲 `[['007ece40', '007ece4f']]`
  - `FALL_THROUGH` [`007ece4c`](#insn-007ece4c) → [`007ece50`](#insn-007ece50)
- ブロック [`007ece50`](#insn-007ece50) 範囲 `[['007ece50', '007ece57']]`
- ブロック [`007ece58`](#insn-007ece58) 範囲 `[['007ece58', '007ece87']]`
  - `CONDITIONAL_JUMP` [`007ece84`](#insn-007ece84) → [`007ece40`](#insn-007ece40)
  - `FALL_THROUGH` [`007ece84`](#insn-007ece84) → [`007ece88`](#insn-007ece88)
- ブロック [`007ece88`](#insn-007ece88) 範囲 `[['007ece88', '007ece8b']]`
  - `CONDITIONAL_JUMP` [`007ece88`](#insn-007ece88) → [`007ece40`](#insn-007ece40)
  - `FALL_THROUGH` [`007ece88`](#insn-007ece88) → [`007ece8c`](#insn-007ece8c)
- ブロック [`007ece8c`](#insn-007ece8c) 範囲 `[['007ece8c', '007ece97']]`
  - `CONDITIONAL_JUMP` [`007ece94`](#insn-007ece94) → [`007ece3c`](#insn-007ece3c)
  - `FALL_THROUGH` [`007ece94`](#insn-007ece94) → [`007ece98`](#insn-007ece98)
- ブロック [`007ece98`](#insn-007ece98) 範囲 `[['007ece98', '007ecea3']]`
  - `FALL_THROUGH` [`007ecea0`](#insn-007ecea0) → [`007ecea4`](#insn-007ecea4)
- ブロック [`007ecea4`](#insn-007ecea4) 範囲 `[['007ecea4', '007ecebb']]`
  - `CONDITIONAL_JUMP` [`007eceb8`](#insn-007eceb8) → [`007ecea4`](#insn-007ecea4)
  - `FALL_THROUGH` [`007eceb8`](#insn-007eceb8) → [`007ecebc`](#insn-007ecebc)
- ブロック [`007ecebc`](#insn-007ecebc) 範囲 `[['007ecebc', '007ecec3']]`
  - `CONDITIONAL_JUMP` [`007ecec0`](#insn-007ecec0) → [`007ece3c`](#insn-007ece3c)
  - `FALL_THROUGH` [`007ecec0`](#insn-007ecec0) → [`007ecec4`](#insn-007ecec4)
- ブロック [`007ecec4`](#insn-007ecec4) 範囲 `[['007ecec4', '007ececf']]`
  - `CONDITIONAL_JUMP` [`007ececc`](#insn-007ececc) → [`007ecedc`](#insn-007ecedc)
  - `FALL_THROUGH` [`007ececc`](#insn-007ececc) → [`007eced0`](#insn-007eced0)
- ブロック [`007eced0`](#insn-007eced0) 範囲 `[['007eced0', '007eced3']]`
  - `UNCONDITIONAL_JUMP` [`007eced0`](#insn-007eced0) → [`007ece3c`](#insn-007ece3c)
- ブロック [`007eced4`](#insn-007eced4) 範囲 `[['007eced4', '007ecedb']]`
  - `CONDITIONAL_JUMP` [`007eced8`](#insn-007eced8) → [`007ecef4`](#insn-007ecef4)
  - `FALL_THROUGH` [`007eced8`](#insn-007eced8) → [`007ecedc`](#insn-007ecedc)
- ブロック [`007ecedc`](#insn-007ecedc) 範囲 `[['007ecedc', '007ecee7']]`
  - `CONDITIONAL_JUMP` [`007ecee4`](#insn-007ecee4) → [`007eced4`](#insn-007eced4)
  - `FALL_THROUGH` [`007ecee4`](#insn-007ecee4) → [`007ecee8`](#insn-007ecee8)
- ブロック [`007ecee8`](#insn-007ecee8) 範囲 `[['007ecee8', '007eceeb']]`
  - `CONDITIONAL_JUMP` [`007ecee8`](#insn-007ecee8) → [`007ecf00`](#insn-007ecf00)
  - `FALL_THROUGH` [`007ecee8`](#insn-007ecee8) → [`007eceec`](#insn-007eceec)
- ブロック [`007eceec`](#insn-007eceec) 範囲 `[['007eceec', '007ecef3']]`
  - `CONDITIONAL_JUMP` [`007ecef0`](#insn-007ecef0) → [`007ecedc`](#insn-007ecedc)
  - `FALL_THROUGH` [`007ecef0`](#insn-007ecef0) → [`007ecef4`](#insn-007ecef4)
- ブロック [`007ecef4`](#insn-007ecef4) 範囲 `[['007ecef4', '007eceff']]`
- ブロック [`007ecf00`](#insn-007ecf00) 範囲 `[['007ecf00', '007ecf0f']]`
  - `UNCONDITIONAL_JUMP` [`007ecf0c`](#insn-007ecf0c) → [`007ece40`](#insn-007ece40)

## 命令位置別の参照

- [`007ecdec`](#insn-007ecdec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecdf0`](#insn-007ecdf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecdf4`](#insn-007ecdf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecdf8`](#insn-007ecdf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece08`](#insn-007ece08) → [`007ece3c`](#insn-007ece3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece24`](#insn-007ece24) → [`007ece10`](#insn-007ece10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece2c`](#insn-007ece2c) → [`007ece3c`](#insn-007ece3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece38`](#insn-007ece38) → [`007ece58`](#insn-007ece58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece44`](#insn-007ece44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece48`](#insn-007ece48) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece4c`](#insn-007ece4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece50`](#insn-007ece50) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece64`](#insn-007ece64) → [`007ecd04`](007ecd04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ecd04` · 推定シンボル `None` · 推定型 `None`
- [`007ece7c`](#insn-007ece7c) → [`007eca30`](007eca30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007eca30` · 推定シンボル `None` · 推定型 `None`
- [`007ece84`](#insn-007ece84) → [`007ece40`](#insn-007ece40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece88`](#insn-007ece88) → [`007ece40`](#insn-007ece40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ece94`](#insn-007ece94) → [`007ece3c`](#insn-007ece3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007eceb8`](#insn-007eceb8) → [`007ecea4`](#insn-007ecea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecec0`](#insn-007ecec0) → [`007ece3c`](#insn-007ece3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ececc`](#insn-007ececc) → [`007ecedc`](#insn-007ecedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007eced0`](#insn-007eced0) → [`007ece3c`](#insn-007ece3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007eced8`](#insn-007eced8) → [`007ecef4`](#insn-007ecef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecee4`](#insn-007ecee4) → [`007eced4`](#insn-007eced4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecee8`](#insn-007ecee8) → [`007ecf00`](#insn-007ecf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecef0`](#insn-007ecef0) → [`007ecedc`](#insn-007ecedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ecef8`](#insn-007ecef8) → `00290bae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007ecefc`](#insn-007ecefc) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`007ecf0c`](#insn-007ecf0c) → [`007ece40`](#insn-007ece40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ecdec`](#insn-007ecdec)

~~~json
{
  "source": "007ecdec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecdf0`](#insn-007ecdf0)

~~~json
{
  "source": "007ecdf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecdf4`](#insn-007ecdf4)

~~~json
{
  "source": "007ecdf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecdf8`](#insn-007ecdf8)

~~~json
{
  "source": "007ecdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece08`](#insn-007ece08)

~~~json
{
  "source": "007ece08",
  "target": "007ece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece24`](#insn-007ece24)

~~~json
{
  "source": "007ece24",
  "target": "007ece10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece2c`](#insn-007ece2c)

~~~json
{
  "source": "007ece2c",
  "target": "007ece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece38`](#insn-007ece38)

~~~json
{
  "source": "007ece38",
  "target": "007ece58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece44`](#insn-007ece44)

~~~json
{
  "source": "007ece44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece48`](#insn-007ece48)

~~~json
{
  "source": "007ece48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece4c`](#insn-007ece4c)

~~~json
{
  "source": "007ece4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece50`](#insn-007ece50)

~~~json
{
  "source": "007ece50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece64`](#insn-007ece64)

~~~json
{
  "source": "007ece64",
  "target": "007ecd04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ece7c`](#insn-007ece7c)

~~~json
{
  "source": "007ece7c",
  "target": "007eca30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ece84`](#insn-007ece84)

~~~json
{
  "source": "007ece84",
  "target": "007ece40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece88`](#insn-007ece88)

~~~json
{
  "source": "007ece88",
  "target": "007ece40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ece94`](#insn-007ece94)

~~~json
{
  "source": "007ece94",
  "target": "007ece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007eceb8`](#insn-007eceb8)

~~~json
{
  "source": "007eceb8",
  "target": "007ecea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecec0`](#insn-007ecec0)

~~~json
{
  "source": "007ecec0",
  "target": "007ece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ececc`](#insn-007ececc)

~~~json
{
  "source": "007ececc",
  "target": "007ecedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007eced0`](#insn-007eced0)

~~~json
{
  "source": "007eced0",
  "target": "007ece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007eced8`](#insn-007eced8)

~~~json
{
  "source": "007eced8",
  "target": "007ecef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecee4`](#insn-007ecee4)

~~~json
{
  "source": "007ecee4",
  "target": "007eced4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecee8`](#insn-007ecee8)

~~~json
{
  "source": "007ecee8",
  "target": "007ecf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecef0`](#insn-007ecef0)

~~~json
{
  "source": "007ecef0",
  "target": "007ecedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ecef8`](#insn-007ecef8)

~~~json
{
  "source": "007ecef8",
  "target": "00290bae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290bae",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "00290bae",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007ecefc`](#insn-007ecefc)

~~~json
{
  "source": "007ecefc",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ecf0c`](#insn-007ecf0c)

~~~json
{
  "source": "007ecf0c",
  "target": "007ece40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
