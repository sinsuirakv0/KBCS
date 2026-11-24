# 00aaf9fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaf9b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-9b9194fff41c412987f17f83c1433d34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0f48c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-fa5d6477e5ca4ad9d2f9ec9e930275b0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaf9fc",
  "name": "FUN_00aaf9fc",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e02a54f546100577788137add3a420d0a72be8beab09181eb2be405df42388d",
  "source_text_sha256": "0e02a54f546100577788137add3a420d0a72be8beab09181eb2be405df42388d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaf9fc",
        "00aafb5f"
      ]
    ],
    "bytes_sha256": "55f7189b53c97c5579ba719a5d45b87047973674b6a9ce197b3ecf126770ace7",
    "instruction_count": 89,
    "instruction_bytes": 356,
    "body_bytes": 356,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a2720c](../00a27/00a2720c.md)
- [00aafb60](../00aaf/00aafb60.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [00ab0e7c](../00ab0/00ab0e7c.md)
- [00bd70ec](../00bd7/00bd70ec.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2655 bytes

~~~c

void FUN_00aaf9fc(long *param_1,long param_2)

{
  long *plVar1;
  void *__dest;
  undefined8 uVar2;
  long *plVar3;
  long lVar4;
  void *pvVar5;
  long *plVar6;
  long *plVar7;
  size_t __n;
  
  plVar1 = (long *)(param_2 + 8);
  plVar6 = (long *)*plVar1;
  plVar3 = plVar1;
  plVar7 = plVar6;
  if (plVar6 != (long *)0x0) {
    do {
      if (-1 < (int)*(uint *)(plVar7 + 4)) {
        plVar3 = plVar7;
      }
      plVar7 = *(long **)((long)plVar7 + ((ulong)(*(uint *)(plVar7 + 4) >> 0x1c) & 8));
    } while (plVar7 != (long *)0x0);
    if ((plVar3 == plVar1) || (0 < (int)plVar3[4])) {
      do {
        while (0 < (int)plVar6[4]) {
          plVar6 = (long *)*plVar6;
          if (plVar6 == (long *)0x0) goto LAB_00aafa98;
        }
        if (-1 < (int)plVar6[4]) {
          lVar4 = plVar6[5];
          param_1[2] = 0;
          param_1[3] = 0;
          param_1[1] = 0;
          *param_1 = lVar4;
          pvVar5 = (void *)plVar6[6];
          __n = plVar6[7] - (long)pvVar5;
          if (__n == 0) {
            return;
          }
          if (-1 < (long)__n) {
            __dest = (void *)_Znwm(__n);
            goto LAB_00aafb00;
          }
          FUN_00ab0e7c(param_1 + 1);
          goto LAB_00aafb34;
        }
        plVar6 = (long *)plVar6[1];
      } while (plVar6 != (long *)0x0);
    }
    else {
      do {
        while (0 < (int)plVar6[4]) {
          plVar6 = (long *)*plVar6;
          if (plVar6 == (long *)0x0) goto LAB_00aafa98;
        }
        if (-1 < (int)plVar6[4]) {
          lVar4 = plVar6[5];
          param_1[2] = 0;
          param_1[3] = 0;
          param_1[1] = 0;
          *param_1 = lVar4;
          pvVar5 = (void *)plVar6[6];
          __n = plVar6[7] - (long)pvVar5;
          if (__n != 0) {
            if ((long)__n < 0) {
LAB_00aafb34:
              uVar2 = FUN_00ab0e7c(param_1 + 1);
              pvVar5 = (void *)param_1[1];
              if (pvVar5 != (void *)0x0) {
                param_1[2] = (long)pvVar5;
                _ZdlPv(pvVar5);
              }
                    /* WARNING: Subroutine does not return */
              FUN_00bd70ec(uVar2);
            }
            __dest = (void *)_Znwm(__n);
LAB_00aafb00:
            param_1[1] = (long)__dest;
            param_1[2] = (long)__dest;
            param_1[3] = (long)__dest + __n;
            memcpy(__dest,pvVar5,__n);
            param_1[2] = (long)__dest + __n;
          }
          return;
        }
        plVar6 = (long *)plVar6[1];
      } while (plVar6 != (long *)0x0);
    }
  }
LAB_00aafa98:
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaf9fc"></a> `00aaf9fc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aafa00"></a> `00aafa00` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafa04"></a> `00aafa04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aafa08"></a> `00aafa08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aafa0c"></a> `00aafa0c` | `09 8c 40 f8` | ldr x9,[x0, #0x8]! | `FALL_THROUGH`
<a id="insn-00aafa10"></a> `00aafa10` | `49 04 00 b4` | cbz x9,0x00aafa98 | `CONDITIONAL_JUMP`
<a id="insn-00aafa14"></a> `00aafa14` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00aafa18"></a> `00aafa18` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aafa1c"></a> `00aafa1c` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00aafa20"></a> `00aafa20` | `4b 21 40 b9` | ldr w11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00aafa24"></a> `00aafa24` | `6c fd 5c d3` | lsr x12,x11,#0x1c | `FALL_THROUGH`
<a id="insn-00aafa28"></a> `00aafa28` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-00aafa2c"></a> `00aafa2c` | `08 b1 8a 9a` | csel x8,x8,x10,lt | `FALL_THROUGH`
<a id="insn-00aafa30"></a> `00aafa30` | `8c 01 7d 92` | and x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-00aafa34"></a> `00aafa34` | `4a 69 6c f8` | ldr x10,[x10, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aafa38"></a> `00aafa38` | `4a ff ff b5` | cbnz x10,0x00aafa20 | `CONDITIONAL_JUMP`
<a id="insn-00aafa3c"></a> `00aafa3c` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00aafa40"></a> `00aafa40` | `e0 00 00 54` | b.eq 0x00aafa5c | `CONDITIONAL_JUMP`
<a id="insn-00aafa44"></a> `00aafa44` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafa48"></a> `00aafa48` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00aafa4c"></a> `00aafa4c` | `8c 00 00 54` | b.gt 0x00aafa5c | `CONDITIONAL_JUMP`
<a id="insn-00aafa50"></a> `00aafa50` | `0c 00 00 14` | b 0x00aafa80 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafa54"></a> `00aafa54` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aafa58"></a> `00aafa58` | `09 02 00 b4` | cbz x9,0x00aafa98 | `CONDITIONAL_JUMP`
<a id="insn-00aafa5c"></a> `00aafa5c` | `28 21 40 b9` | ldr w8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aafa60"></a> `00aafa60` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafa64"></a> `00aafa64` | `8a ff ff 54` | b.ge 0x00aafa54 | `CONDITIONAL_JUMP`
<a id="insn-00aafa68"></a> `00aafa68` | `e8 01 f8 36` | tbz w8,#0x1f,0x00aafaa4 | `CONDITIONAL_JUMP`
<a id="insn-00aafa6c"></a> `00aafa6c` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00aafa70"></a> `00aafa70` | `69 ff ff b5` | cbnz x9,0x00aafa5c | `CONDITIONAL_JUMP`
<a id="insn-00aafa74"></a> `00aafa74` | `09 00 00 14` | b 0x00aafa98 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafa78"></a> `00aafa78` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aafa7c"></a> `00aafa7c` | `e9 00 00 b4` | cbz x9,0x00aafa98 | `CONDITIONAL_JUMP`
<a id="insn-00aafa80"></a> `00aafa80` | `28 21 40 b9` | ldr w8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aafa84"></a> `00aafa84` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafa88"></a> `00aafa88` | `8a ff ff 54` | b.ge 0x00aafa78 | `CONDITIONAL_JUMP`
<a id="insn-00aafa8c"></a> `00aafa8c` | `48 02 f8 36` | tbz w8,#0x1f,0x00aafad4 | `CONDITIONAL_JUMP`
<a id="insn-00aafa90"></a> `00aafa90` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00aafa94"></a> `00aafa94` | `69 ff ff b5` | cbnz x9,0x00aafa80 | `CONDITIONAL_JUMP`
<a id="insn-00aafa98"></a> `00aafa98` | `00 bf ff b0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00aafa9c"></a> `00aafa9c` | `00 b8 2e 91` | add x0,x0,#0xbae | `FALL_THROUGH`
<a id="insn-00aafaa0"></a> `00aafaa0` | `d4 c0 e5 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-00aafaa4"></a> `00aafaa4` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aafaa8"></a> `00aafaa8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00aafaac"></a> `00aafaac` | `7f 7e 01 a9` | stp xzr,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafab0"></a> `00aafab0` | `9f 8e 00 f8` | str xzr,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00aafab4"></a> `00aafab4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafab8"></a> `00aafab8` | `35 21 43 a9` | ldp x21,x8,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00aafabc"></a> `00aafabc` | `16 01 15 eb` | subs x22,x8,x21 | `FALL_THROUGH`
<a id="insn-00aafac0"></a> `00aafac0` | `e0 02 00 54` | b.eq 0x00aafb1c | `CONDITIONAL_JUMP`
<a id="insn-00aafac4"></a> `00aafac4` | `56 03 f8 b7` | tbnz x22,#0x3f,0x00aafb2c | `CONDITIONAL_JUMP`
<a id="insn-00aafac8"></a> `00aafac8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aafacc"></a> `00aafacc` | `5d ad 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aafad0"></a> `00aafad0` | `0c 00 00 14` | b 0x00aafb00 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafad4"></a> `00aafad4` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aafad8"></a> `00aafad8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00aafadc"></a> `00aafadc` | `7f 7e 01 a9` | stp xzr,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafae0"></a> `00aafae0` | `9f 8e 00 f8` | str xzr,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00aafae4"></a> `00aafae4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafae8"></a> `00aafae8` | `35 21 43 a9` | ldp x21,x8,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00aafaec"></a> `00aafaec` | `16 01 15 eb` | subs x22,x8,x21 | `FALL_THROUGH`
<a id="insn-00aafaf0"></a> `00aafaf0` | `60 01 00 54` | b.eq 0x00aafb1c | `CONDITIONAL_JUMP`
<a id="insn-00aafaf4"></a> `00aafaf4` | `16 02 f8 b7` | tbnz x22,#0x3f,0x00aafb34 | `CONDITIONAL_JUMP`
<a id="insn-00aafaf8"></a> `00aafaf8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aafafc"></a> `00aafafc` | `51 ad 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb00"></a> `00aafb00` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-00aafb04"></a> `00aafb04` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aafb08"></a> `00aafb08` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00aafb0c"></a> `00aafb0c` | `60 82 00 a9` | stp x0,x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aafb10"></a> `00aafb10` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aafb14"></a> `00aafb14` | `a7 ad 04 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb18"></a> `00aafb18` | `74 0a 00 f9` | str x20,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb1c"></a> `00aafb1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aafb20"></a> `00aafb20` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb24"></a> `00aafb24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aafb28"></a> `00aafb28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aafb2c"></a> `00aafb2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aafb30"></a> `00aafb30` | `d3 04 00 94` | bl 0x00ab0e7c | `UNCONDITIONAL_CALL`
<a id="insn-00aafb34"></a> `00aafb34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aafb38"></a> `00aafb38` | `d1 04 00 94` | bl 0x00ab0e7c | `UNCONDITIONAL_CALL`
<a id="insn-00aafb3c"></a> `00aafb3c` | `01 00 00 14` | b 0x00aafb40 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafb40"></a> `00aafb40` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aafb44"></a> `00aafb44` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aafb48"></a> `00aafb48` | `88 00 00 b4` | cbz x8,0x00aafb58 | `CONDITIONAL_JUMP`
<a id="insn-00aafb4c"></a> `00aafb4c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aafb50"></a> `00aafb50` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb54"></a> `00aafb54` | `43 ad 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb58"></a> `00aafb58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aafb5c"></a> `00aafb5c` | `64 9d 04 94` | bl 0x00bd70ec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaf9fc`](#insn-00aaf9fc) 範囲 `[['00aaf9fc', '00aafa13']]`
  - `CONDITIONAL_JUMP` [`00aafa10`](#insn-00aafa10) → [`00aafa98`](#insn-00aafa98)
  - `FALL_THROUGH` [`00aafa10`](#insn-00aafa10) → [`00aafa14`](#insn-00aafa14)
- ブロック [`00aafa14`](#insn-00aafa14) 範囲 `[['00aafa14', '00aafa1f']]`
  - `FALL_THROUGH` [`00aafa1c`](#insn-00aafa1c) → [`00aafa20`](#insn-00aafa20)
- ブロック [`00aafa20`](#insn-00aafa20) 範囲 `[['00aafa20', '00aafa3b']]`
  - `CONDITIONAL_JUMP` [`00aafa38`](#insn-00aafa38) → [`00aafa20`](#insn-00aafa20)
  - `FALL_THROUGH` [`00aafa38`](#insn-00aafa38) → [`00aafa3c`](#insn-00aafa3c)
- ブロック [`00aafa3c`](#insn-00aafa3c) 範囲 `[['00aafa3c', '00aafa43']]`
  - `CONDITIONAL_JUMP` [`00aafa40`](#insn-00aafa40) → [`00aafa5c`](#insn-00aafa5c)
  - `FALL_THROUGH` [`00aafa40`](#insn-00aafa40) → [`00aafa44`](#insn-00aafa44)
- ブロック [`00aafa44`](#insn-00aafa44) 範囲 `[['00aafa44', '00aafa4f']]`
  - `CONDITIONAL_JUMP` [`00aafa4c`](#insn-00aafa4c) → [`00aafa5c`](#insn-00aafa5c)
  - `FALL_THROUGH` [`00aafa4c`](#insn-00aafa4c) → [`00aafa50`](#insn-00aafa50)
- ブロック [`00aafa50`](#insn-00aafa50) 範囲 `[['00aafa50', '00aafa53']]`
  - `UNCONDITIONAL_JUMP` [`00aafa50`](#insn-00aafa50) → [`00aafa80`](#insn-00aafa80)
- ブロック [`00aafa54`](#insn-00aafa54) 範囲 `[['00aafa54', '00aafa5b']]`
  - `CONDITIONAL_JUMP` [`00aafa58`](#insn-00aafa58) → [`00aafa98`](#insn-00aafa98)
  - `FALL_THROUGH` [`00aafa58`](#insn-00aafa58) → [`00aafa5c`](#insn-00aafa5c)
- ブロック [`00aafa5c`](#insn-00aafa5c) 範囲 `[['00aafa5c', '00aafa67']]`
  - `CONDITIONAL_JUMP` [`00aafa64`](#insn-00aafa64) → [`00aafa54`](#insn-00aafa54)
  - `FALL_THROUGH` [`00aafa64`](#insn-00aafa64) → [`00aafa68`](#insn-00aafa68)
- ブロック [`00aafa68`](#insn-00aafa68) 範囲 `[['00aafa68', '00aafa6b']]`
  - `CONDITIONAL_JUMP` [`00aafa68`](#insn-00aafa68) → [`00aafaa4`](#insn-00aafaa4)
  - `FALL_THROUGH` [`00aafa68`](#insn-00aafa68) → [`00aafa6c`](#insn-00aafa6c)
- ブロック [`00aafa6c`](#insn-00aafa6c) 範囲 `[['00aafa6c', '00aafa73']]`
  - `CONDITIONAL_JUMP` [`00aafa70`](#insn-00aafa70) → [`00aafa5c`](#insn-00aafa5c)
  - `FALL_THROUGH` [`00aafa70`](#insn-00aafa70) → [`00aafa74`](#insn-00aafa74)
- ブロック [`00aafa74`](#insn-00aafa74) 範囲 `[['00aafa74', '00aafa77']]`
  - `UNCONDITIONAL_JUMP` [`00aafa74`](#insn-00aafa74) → [`00aafa98`](#insn-00aafa98)
- ブロック [`00aafa78`](#insn-00aafa78) 範囲 `[['00aafa78', '00aafa7f']]`
  - `CONDITIONAL_JUMP` [`00aafa7c`](#insn-00aafa7c) → [`00aafa98`](#insn-00aafa98)
  - `FALL_THROUGH` [`00aafa7c`](#insn-00aafa7c) → [`00aafa80`](#insn-00aafa80)
- ブロック [`00aafa80`](#insn-00aafa80) 範囲 `[['00aafa80', '00aafa8b']]`
  - `CONDITIONAL_JUMP` [`00aafa88`](#insn-00aafa88) → [`00aafa78`](#insn-00aafa78)
  - `FALL_THROUGH` [`00aafa88`](#insn-00aafa88) → [`00aafa8c`](#insn-00aafa8c)
- ブロック [`00aafa8c`](#insn-00aafa8c) 範囲 `[['00aafa8c', '00aafa8f']]`
  - `CONDITIONAL_JUMP` [`00aafa8c`](#insn-00aafa8c) → [`00aafad4`](#insn-00aafad4)
  - `FALL_THROUGH` [`00aafa8c`](#insn-00aafa8c) → [`00aafa90`](#insn-00aafa90)
- ブロック [`00aafa90`](#insn-00aafa90) 範囲 `[['00aafa90', '00aafa97']]`
  - `CONDITIONAL_JUMP` [`00aafa94`](#insn-00aafa94) → [`00aafa80`](#insn-00aafa80)
  - `FALL_THROUGH` [`00aafa94`](#insn-00aafa94) → [`00aafa98`](#insn-00aafa98)
- ブロック [`00aafa98`](#insn-00aafa98) 範囲 `[['00aafa98', '00aafaa3']]`
- ブロック [`00aafaa4`](#insn-00aafaa4) 範囲 `[['00aafaa4', '00aafac3']]`
  - `CONDITIONAL_JUMP` [`00aafac0`](#insn-00aafac0) → [`00aafb1c`](#insn-00aafb1c)
  - `FALL_THROUGH` [`00aafac0`](#insn-00aafac0) → [`00aafac4`](#insn-00aafac4)
- ブロック [`00aafac4`](#insn-00aafac4) 範囲 `[['00aafac4', '00aafac7']]`
  - `CONDITIONAL_JUMP` [`00aafac4`](#insn-00aafac4) → [`00aafb2c`](#insn-00aafb2c)
  - `FALL_THROUGH` [`00aafac4`](#insn-00aafac4) → [`00aafac8`](#insn-00aafac8)
- ブロック [`00aafac8`](#insn-00aafac8) 範囲 `[['00aafac8', '00aafad3']]`
  - `UNCONDITIONAL_JUMP` [`00aafad0`](#insn-00aafad0) → [`00aafb00`](#insn-00aafb00)
- ブロック [`00aafad4`](#insn-00aafad4) 範囲 `[['00aafad4', '00aafaf3']]`
  - `CONDITIONAL_JUMP` [`00aafaf0`](#insn-00aafaf0) → [`00aafb1c`](#insn-00aafb1c)
  - `FALL_THROUGH` [`00aafaf0`](#insn-00aafaf0) → [`00aafaf4`](#insn-00aafaf4)
- ブロック [`00aafaf4`](#insn-00aafaf4) 範囲 `[['00aafaf4', '00aafaf7']]`
  - `CONDITIONAL_JUMP` [`00aafaf4`](#insn-00aafaf4) → [`00aafb34`](#insn-00aafb34)
  - `FALL_THROUGH` [`00aafaf4`](#insn-00aafaf4) → [`00aafaf8`](#insn-00aafaf8)
- ブロック [`00aafaf8`](#insn-00aafaf8) 範囲 `[['00aafaf8', '00aafaff']]`
  - `FALL_THROUGH` [`00aafafc`](#insn-00aafafc) → [`00aafb00`](#insn-00aafb00)
- ブロック [`00aafb00`](#insn-00aafb00) 範囲 `[['00aafb00', '00aafb1b']]`
  - `FALL_THROUGH` [`00aafb18`](#insn-00aafb18) → [`00aafb1c`](#insn-00aafb1c)
- ブロック [`00aafb1c`](#insn-00aafb1c) 範囲 `[['00aafb1c', '00aafb2b']]`
- ブロック [`00aafb2c`](#insn-00aafb2c) 範囲 `[['00aafb2c', '00aafb33']]`
  - `FALL_THROUGH` [`00aafb30`](#insn-00aafb30) → [`00aafb34`](#insn-00aafb34)
- ブロック [`00aafb34`](#insn-00aafb34) 範囲 `[['00aafb34', '00aafb3f']]`
  - `UNCONDITIONAL_JUMP` [`00aafb3c`](#insn-00aafb3c) → [`00aafb40`](#insn-00aafb40)
- ブロック [`00aafb40`](#insn-00aafb40) 範囲 `[['00aafb40', '00aafb4b']]`
  - `CONDITIONAL_JUMP` [`00aafb48`](#insn-00aafb48) → [`00aafb58`](#insn-00aafb58)
  - `FALL_THROUGH` [`00aafb48`](#insn-00aafb48) → [`00aafb4c`](#insn-00aafb4c)
- ブロック [`00aafb4c`](#insn-00aafb4c) 範囲 `[['00aafb4c', '00aafb57']]`
  - `FALL_THROUGH` [`00aafb54`](#insn-00aafb54) → [`00aafb58`](#insn-00aafb58)
- ブロック [`00aafb58`](#insn-00aafb58) 範囲 `[['00aafb58', '00aafb5f']]`

## 命令位置別の参照

- [`00aaf9fc`](#insn-00aaf9fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa00`](#insn-00aafa00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa04`](#insn-00aafa04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa10`](#insn-00aafa10) → [`00aafa98`](#insn-00aafa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa38`](#insn-00aafa38) → [`00aafa20`](#insn-00aafa20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa40`](#insn-00aafa40) → [`00aafa5c`](#insn-00aafa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa4c`](#insn-00aafa4c) → [`00aafa5c`](#insn-00aafa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa50`](#insn-00aafa50) → [`00aafa80`](#insn-00aafa80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa58`](#insn-00aafa58) → [`00aafa98`](#insn-00aafa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa64`](#insn-00aafa64) → [`00aafa54`](#insn-00aafa54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa68`](#insn-00aafa68) → [`00aafaa4`](#insn-00aafaa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa70`](#insn-00aafa70) → [`00aafa5c`](#insn-00aafa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa74`](#insn-00aafa74) → [`00aafa98`](#insn-00aafa98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa7c`](#insn-00aafa7c) → [`00aafa98`](#insn-00aafa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa88`](#insn-00aafa88) → [`00aafa78`](#insn-00aafa78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa8c`](#insn-00aafa8c) → [`00aafad4`](#insn-00aafad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa94`](#insn-00aafa94) → [`00aafa80`](#insn-00aafa80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafa9c`](#insn-00aafa9c) → `00290bae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aafaa0`](#insn-00aafaa0) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`00aafac0`](#insn-00aafac0) → [`00aafb1c`](#insn-00aafb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafac4`](#insn-00aafac4) → [`00aafb2c`](#insn-00aafb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafacc`](#insn-00aafacc) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aafad0`](#insn-00aafad0) → [`00aafb00`](#insn-00aafb00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafaf0`](#insn-00aafaf0) → [`00aafb1c`](#insn-00aafb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafaf4`](#insn-00aafaf4) → [`00aafb34`](#insn-00aafb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafafc`](#insn-00aafafc) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aafb14`](#insn-00aafb14) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00aafb1c`](#insn-00aafb1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb20`](#insn-00aafb20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb24`](#insn-00aafb24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb30`](#insn-00aafb30) → [`00ab0e7c`](../00ab0/00ab0e7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab0e7c` · 推定シンボル `None` · 推定型 `None`
- [`00aafb38`](#insn-00aafb38) → [`00ab0e7c`](../00ab0/00ab0e7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab0e7c` · 推定シンボル `None` · 推定型 `None`
- [`00aafb3c`](#insn-00aafb3c) → [`00aafb40`](#insn-00aafb40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb48`](#insn-00aafb48) → [`00aafb58`](#insn-00aafb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb54`](#insn-00aafb54) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aafb5c`](#insn-00aafb5c) → [`00bd70ec`](../00bd7/00bd70ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd70ec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaf9fc`](#insn-00aaf9fc)

~~~json
{
  "source": "00aaf9fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa00`](#insn-00aafa00)

~~~json
{
  "source": "00aafa00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa04`](#insn-00aafa04)

~~~json
{
  "source": "00aafa04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa10`](#insn-00aafa10)

~~~json
{
  "source": "00aafa10",
  "target": "00aafa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa38`](#insn-00aafa38)

~~~json
{
  "source": "00aafa38",
  "target": "00aafa20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa40`](#insn-00aafa40)

~~~json
{
  "source": "00aafa40",
  "target": "00aafa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa4c`](#insn-00aafa4c)

~~~json
{
  "source": "00aafa4c",
  "target": "00aafa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa50`](#insn-00aafa50)

~~~json
{
  "source": "00aafa50",
  "target": "00aafa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa58`](#insn-00aafa58)

~~~json
{
  "source": "00aafa58",
  "target": "00aafa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa64`](#insn-00aafa64)

~~~json
{
  "source": "00aafa64",
  "target": "00aafa54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa68`](#insn-00aafa68)

~~~json
{
  "source": "00aafa68",
  "target": "00aafaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa70`](#insn-00aafa70)

~~~json
{
  "source": "00aafa70",
  "target": "00aafa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa74`](#insn-00aafa74)

~~~json
{
  "source": "00aafa74",
  "target": "00aafa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa7c`](#insn-00aafa7c)

~~~json
{
  "source": "00aafa7c",
  "target": "00aafa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa88`](#insn-00aafa88)

~~~json
{
  "source": "00aafa88",
  "target": "00aafa78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa8c`](#insn-00aafa8c)

~~~json
{
  "source": "00aafa8c",
  "target": "00aafad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa94`](#insn-00aafa94)

~~~json
{
  "source": "00aafa94",
  "target": "00aafa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafa9c`](#insn-00aafa9c)

~~~json
{
  "source": "00aafa9c",
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
- 参照命令 [`00aafaa0`](#insn-00aafaa0)

~~~json
{
  "source": "00aafaa0",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafac0`](#insn-00aafac0)

~~~json
{
  "source": "00aafac0",
  "target": "00aafb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafac4`](#insn-00aafac4)

~~~json
{
  "source": "00aafac4",
  "target": "00aafb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafacc`](#insn-00aafacc)

~~~json
{
  "source": "00aafacc",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafad0`](#insn-00aafad0)

~~~json
{
  "source": "00aafad0",
  "target": "00aafb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafaf0`](#insn-00aafaf0)

~~~json
{
  "source": "00aafaf0",
  "target": "00aafb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafaf4`](#insn-00aafaf4)

~~~json
{
  "source": "00aafaf4",
  "target": "00aafb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafafc`](#insn-00aafafc)

~~~json
{
  "source": "00aafafc",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb14`](#insn-00aafb14)

~~~json
{
  "source": "00aafb14",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb1c`](#insn-00aafb1c)

~~~json
{
  "source": "00aafb1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb20`](#insn-00aafb20)

~~~json
{
  "source": "00aafb20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb24`](#insn-00aafb24)

~~~json
{
  "source": "00aafb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb30`](#insn-00aafb30)

~~~json
{
  "source": "00aafb30",
  "target": "00ab0e7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb38`](#insn-00aafb38)

~~~json
{
  "source": "00aafb38",
  "target": "00ab0e7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb3c`](#insn-00aafb3c)

~~~json
{
  "source": "00aafb3c",
  "target": "00aafb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb48`](#insn-00aafb48)

~~~json
{
  "source": "00aafb48",
  "target": "00aafb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb54`](#insn-00aafb54)

~~~json
{
  "source": "00aafb54",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb5c`](#insn-00aafb5c)

~~~json
{
  "source": "00aafb5c",
  "target": "00bd70ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
