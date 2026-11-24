# 00bfdabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b81074`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-a635135956b8086890484c8450baab8b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfdee4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdee4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-55f6fe04cd72333891f7f148aec12d98)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdabc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df79b1c749842e650ed15e3574e94853553cac4159344cff4acc14aac3673391",
  "source_text_sha256": "df79b1c749842e650ed15e3574e94853553cac4159344cff4acc14aac3673391",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdabc",
        "00bfdc23"
      ]
    ],
    "bytes_sha256": "e3bb315079678fe19b20cf46e3c4ce69ebac1b73e1b7f0fc23f8860c9e92fe86",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1832 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli
                 (long *param_1,long param_2,uint param_3)

{
  byte *pbVar1;
  uint uVar2;
  long *plVar3;
  long lVar4;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return param_1;
  }
  if (param_2 == 0x7fffffffffffffff) {
    do {
      plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      pbVar1 = (byte *)plVar3[3];
      if (pbVar1 == (byte *)plVar3[4]) {
        uVar2 = (**(code **)(*plVar3 + 0x50))();
        if (uVar2 == 0xffffffff) goto LAB_00bfdbec;
      }
      else {
        plVar3[3] = (long)(pbVar1 + 1);
        uVar2 = (uint)*pbVar1;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    } while (uVar2 != param_3);
  }
  else {
    lVar4 = param_1[1];
    if (lVar4 < param_2) {
      do {
        plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        pbVar1 = (byte *)plVar3[3];
        if (pbVar1 == (byte *)plVar3[4]) {
          uVar2 = (**(code **)(*plVar3 + 0x50))();
          if (uVar2 == 0xffffffff) goto LAB_00bfdbec;
          lVar4 = param_1[1];
          if (lVar4 != 0x7fffffffffffffff) goto LAB_00bfdb90;
          lVar4 = param_1[1];
        }
        else {
          plVar3[3] = (long)(pbVar1 + 1);
          uVar2 = (uint)*pbVar1;
LAB_00bfdb90:
          lVar4 = lVar4 + 1;
          param_1[1] = lVar4;
        }
      } while (uVar2 != param_3 && lVar4 < param_2);
    }
  }
  uVar2 = 0;
LAB_00bfdbf0:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar2);
  return param_1;
LAB_00bfdbec:
  uVar2 = 2;
  goto LAB_00bfdbf0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfdabc"></a> `00bfdabc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdac0"></a> `00bfdac0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfdac4"></a> `00bfdac4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdac8"></a> `00bfdac8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdacc"></a> `00bfdacc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdad0"></a> `00bfdad0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfdad4"></a> `00bfdad4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdad8"></a> `00bfdad8` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00bfdadc"></a> `00bfdadc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfdae0"></a> `00bfdae0` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdae4"></a> `00bfdae4` | `a0 73 00 91` | add x0,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfdae8"></a> `00bfdae8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfdaec"></a> `00bfdaec` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdaf0"></a> `00bfdaf0` | `b8 6f 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdaf4"></a> `00bfdaf4` | `a8 73 40 39` | ldrb w8,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfdaf8"></a> `00bfdaf8` | `88 08 00 34` | cbz w8,0x00bfdc08 | `CONDITIONAL_JUMP`
<a id="insn-00bfdafc"></a> `00bfdafc` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdb00"></a> `00bfdb00` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00bfdb04"></a> `00bfdb04` | `41 03 00 54` | b.ne 0x00bfdb6c | `CONDITIONAL_JUMP`
<a id="insn-00bfdb08"></a> `00bfdb08` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdb0c"></a> `00bfdb0c` | `03 00 00 14` | b 0x00bfdb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb10"></a> `00bfdb10` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00bfdb14"></a> `00bfdb14` | `80 06 00 54` | b.eq 0x00bfdbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb18"></a> `00bfdb18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdb1c"></a> `00bfdb1c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdb20"></a> `00bfdb20` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdb24"></a> `00bfdb24` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdb28"></a> `00bfdb28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdb2c"></a> `00bfdb2c` | `a0 00 00 54` | b.eq 0x00bfdb40 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb30"></a> `00bfdb30` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb34"></a> `00bfdb34` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdb38"></a> `00bfdb38` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfdb3c"></a> `00bfdb3c` | `06 00 00 14` | b 0x00bfdb54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb40"></a> `00bfdb40` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdb44"></a> `00bfdb44` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdb48"></a> `00bfdb48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdb4c"></a> `00bfdb4c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb50"></a> `00bfdb50` | `e0 04 00 54` | b.eq 0x00bfdbec | `CONDITIONAL_JUMP`
<a id="insn-00bfdb54"></a> `00bfdb54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb58"></a> `00bfdb58` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfdb5c"></a> `00bfdb5c` | `a0 fd ff 54` | b.eq 0x00bfdb10 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb60"></a> `00bfdb60` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb64"></a> `00bfdb64` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb68"></a> `00bfdb68` | `ea ff ff 17` | b 0x00bfdb10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb6c"></a> `00bfdb6c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb70"></a> `00bfdb70` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bfdb74"></a> `00bfdb74` | `8a 03 00 54` | b.ge 0x00bfdbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb78"></a> `00bfdb78` | `76 a2 00 91` | add x22,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdb7c"></a> `00bfdb7c` | `17 00 f0 92` | mov x23,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdb80"></a> `00bfdb80` | `09 00 00 14` | b 0x00bfdba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb84"></a> `00bfdb84` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb88"></a> `00bfdb88` | `0a 0c 00 f9` | str x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdb8c"></a> `00bfdb8c` | `20 01 40 39` | ldrb w0,[x9] | `FALL_THROUGH`
<a id="insn-00bfdb90"></a> `00bfdb90` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb94"></a> `00bfdb94` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb98"></a> `00bfdb98` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00bfdb9c"></a> `00bfdb9c` | `00 11 55 fa` | ccmp x8,x21,#0x0,ne | `FALL_THROUGH`
<a id="insn-00bfdba0"></a> `00bfdba0` | `2a 02 00 54` | b.ge 0x00bfdbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bfdba4"></a> `00bfdba4` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfdba8"></a> `00bfdba8` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdbac"></a> `00bfdbac` | `c0 6a 69 f8` | ldr x0,[x22, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdbb0"></a> `00bfdbb0` | `09 a8 41 a9` | ldp x9,x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdbb4"></a> `00bfdbb4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfdbb8"></a> `00bfdbb8` | `61 fe ff 54` | b.ne 0x00bfdb84 | `CONDITIONAL_JUMP`
<a id="insn-00bfdbbc"></a> `00bfdbbc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdbc0"></a> `00bfdbc0` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdbc4"></a> `00bfdbc4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdbc8"></a> `00bfdbc8` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdbcc"></a> `00bfdbcc` | `00 01 00 54` | b.eq 0x00bfdbec | `CONDITIONAL_JUMP`
<a id="insn-00bfdbd0"></a> `00bfdbd0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdbd4"></a> `00bfdbd4` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfdbd8"></a> `00bfdbd8` | `c1 fd ff 54` | b.ne 0x00bfdb90 | `CONDITIONAL_JUMP`
<a id="insn-00bfdbdc"></a> `00bfdbdc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdbe0"></a> `00bfdbe0` | `ee ff ff 17` | b 0x00bfdb98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdbe4"></a> `00bfdbe4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfdbe8"></a> `00bfdbe8` | `02 00 00 14` | b 0x00bfdbf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdbec"></a> `00bfdbec` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfdbf0"></a> `00bfdbf0` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfdbf4"></a> `00bfdbf4` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdbf8"></a> `00bfdbf8` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfdbfc"></a> `00bfdbfc` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdc00"></a> `00bfdc00` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfdc04"></a> `00bfdc04` | `a7 68 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdc08"></a> `00bfdc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfdc0c"></a> `00bfdc0c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdc10"></a> `00bfdc10` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdc14"></a> `00bfdc14` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdc18"></a> `00bfdc18` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfdc1c"></a> `00bfdc1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfdc20"></a> `00bfdc20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdabc`](#insn-00bfdabc) 範囲 `[['00bfdabc', '00bfdafb']]`
  - `CONDITIONAL_JUMP` [`00bfdaf8`](#insn-00bfdaf8) → [`00bfdc08`](#insn-00bfdc08)
  - `FALL_THROUGH` [`00bfdaf8`](#insn-00bfdaf8) → [`00bfdafc`](#insn-00bfdafc)
- ブロック [`00bfdafc`](#insn-00bfdafc) 範囲 `[['00bfdafc', '00bfdb07']]`
  - `CONDITIONAL_JUMP` [`00bfdb04`](#insn-00bfdb04) → [`00bfdb6c`](#insn-00bfdb6c)
  - `FALL_THROUGH` [`00bfdb04`](#insn-00bfdb04) → [`00bfdb08`](#insn-00bfdb08)
- ブロック [`00bfdb08`](#insn-00bfdb08) 範囲 `[['00bfdb08', '00bfdb0f']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb0c`](#insn-00bfdb0c) → [`00bfdb18`](#insn-00bfdb18)
- ブロック [`00bfdb10`](#insn-00bfdb10) 範囲 `[['00bfdb10', '00bfdb17']]`
  - `CONDITIONAL_JUMP` [`00bfdb14`](#insn-00bfdb14) → [`00bfdbe4`](#insn-00bfdbe4)
  - `FALL_THROUGH` [`00bfdb14`](#insn-00bfdb14) → [`00bfdb18`](#insn-00bfdb18)
- ブロック [`00bfdb18`](#insn-00bfdb18) 範囲 `[['00bfdb18', '00bfdb2f']]`
  - `CONDITIONAL_JUMP` [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdb40`](#insn-00bfdb40)
  - `FALL_THROUGH` [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdb30`](#insn-00bfdb30)
- ブロック [`00bfdb30`](#insn-00bfdb30) 範囲 `[['00bfdb30', '00bfdb3f']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb3c`](#insn-00bfdb3c) → [`00bfdb54`](#insn-00bfdb54)
- ブロック [`00bfdb40`](#insn-00bfdb40) 範囲 `[['00bfdb40', '00bfdb53']]`
  - `CONDITIONAL_JUMP` [`00bfdb50`](#insn-00bfdb50) → [`00bfdbec`](#insn-00bfdbec)
  - `FALL_THROUGH` [`00bfdb50`](#insn-00bfdb50) → [`00bfdb54`](#insn-00bfdb54)
- ブロック [`00bfdb54`](#insn-00bfdb54) 範囲 `[['00bfdb54', '00bfdb5f']]`
  - `CONDITIONAL_JUMP` [`00bfdb5c`](#insn-00bfdb5c) → [`00bfdb10`](#insn-00bfdb10)
  - `FALL_THROUGH` [`00bfdb5c`](#insn-00bfdb5c) → [`00bfdb60`](#insn-00bfdb60)
- ブロック [`00bfdb60`](#insn-00bfdb60) 範囲 `[['00bfdb60', '00bfdb6b']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb68`](#insn-00bfdb68) → [`00bfdb10`](#insn-00bfdb10)
- ブロック [`00bfdb6c`](#insn-00bfdb6c) 範囲 `[['00bfdb6c', '00bfdb77']]`
  - `CONDITIONAL_JUMP` [`00bfdb74`](#insn-00bfdb74) → [`00bfdbe4`](#insn-00bfdbe4)
  - `FALL_THROUGH` [`00bfdb74`](#insn-00bfdb74) → [`00bfdb78`](#insn-00bfdb78)
- ブロック [`00bfdb78`](#insn-00bfdb78) 範囲 `[['00bfdb78', '00bfdb83']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb80`](#insn-00bfdb80) → [`00bfdba4`](#insn-00bfdba4)
- ブロック [`00bfdb84`](#insn-00bfdb84) 範囲 `[['00bfdb84', '00bfdb8f']]`
  - `FALL_THROUGH` [`00bfdb8c`](#insn-00bfdb8c) → [`00bfdb90`](#insn-00bfdb90)
- ブロック [`00bfdb90`](#insn-00bfdb90) 範囲 `[['00bfdb90', '00bfdb97']]`
  - `FALL_THROUGH` [`00bfdb94`](#insn-00bfdb94) → [`00bfdb98`](#insn-00bfdb98)
- ブロック [`00bfdb98`](#insn-00bfdb98) 範囲 `[['00bfdb98', '00bfdba3']]`
  - `CONDITIONAL_JUMP` [`00bfdba0`](#insn-00bfdba0) → [`00bfdbe4`](#insn-00bfdbe4)
  - `FALL_THROUGH` [`00bfdba0`](#insn-00bfdba0) → [`00bfdba4`](#insn-00bfdba4)
- ブロック [`00bfdba4`](#insn-00bfdba4) 範囲 `[['00bfdba4', '00bfdbbb']]`
  - `CONDITIONAL_JUMP` [`00bfdbb8`](#insn-00bfdbb8) → [`00bfdb84`](#insn-00bfdb84)
  - `FALL_THROUGH` [`00bfdbb8`](#insn-00bfdbb8) → [`00bfdbbc`](#insn-00bfdbbc)
- ブロック [`00bfdbbc`](#insn-00bfdbbc) 範囲 `[['00bfdbbc', '00bfdbcf']]`
  - `CONDITIONAL_JUMP` [`00bfdbcc`](#insn-00bfdbcc) → [`00bfdbec`](#insn-00bfdbec)
  - `FALL_THROUGH` [`00bfdbcc`](#insn-00bfdbcc) → [`00bfdbd0`](#insn-00bfdbd0)
- ブロック [`00bfdbd0`](#insn-00bfdbd0) 範囲 `[['00bfdbd0', '00bfdbdb']]`
  - `CONDITIONAL_JUMP` [`00bfdbd8`](#insn-00bfdbd8) → [`00bfdb90`](#insn-00bfdb90)
  - `FALL_THROUGH` [`00bfdbd8`](#insn-00bfdbd8) → [`00bfdbdc`](#insn-00bfdbdc)
- ブロック [`00bfdbdc`](#insn-00bfdbdc) 範囲 `[['00bfdbdc', '00bfdbe3']]`
  - `UNCONDITIONAL_JUMP` [`00bfdbe0`](#insn-00bfdbe0) → [`00bfdb98`](#insn-00bfdb98)
- ブロック [`00bfdbe4`](#insn-00bfdbe4) 範囲 `[['00bfdbe4', '00bfdbeb']]`
  - `UNCONDITIONAL_JUMP` [`00bfdbe8`](#insn-00bfdbe8) → [`00bfdbf0`](#insn-00bfdbf0)
- ブロック [`00bfdbec`](#insn-00bfdbec) 範囲 `[['00bfdbec', '00bfdbef']]`
  - `FALL_THROUGH` [`00bfdbec`](#insn-00bfdbec) → [`00bfdbf0`](#insn-00bfdbf0)
- ブロック [`00bfdbf0`](#insn-00bfdbf0) 範囲 `[['00bfdbf0', '00bfdc07']]`
  - `FALL_THROUGH` [`00bfdc04`](#insn-00bfdc04) → [`00bfdc08`](#insn-00bfdc08)
- ブロック [`00bfdc08`](#insn-00bfdc08) 範囲 `[['00bfdc08', '00bfdc23']]`

## 命令位置別の参照

- [`00bfdac0`](#insn-00bfdac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdac4`](#insn-00bfdac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdac8`](#insn-00bfdac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdacc`](#insn-00bfdacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdaf0`](#insn-00bfdaf0) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdaf4`](#insn-00bfdaf4) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdaf8`](#insn-00bfdaf8) → [`00bfdc08`](#insn-00bfdc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb04`](#insn-00bfdb04) → [`00bfdb6c`](#insn-00bfdb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb0c`](#insn-00bfdb0c) → [`00bfdb18`](#insn-00bfdb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb14`](#insn-00bfdb14) → [`00bfdbe4`](#insn-00bfdbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdb40`](#insn-00bfdb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb3c`](#insn-00bfdb3c) → [`00bfdb54`](#insn-00bfdb54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb50`](#insn-00bfdb50) → [`00bfdbec`](#insn-00bfdbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb5c`](#insn-00bfdb5c) → [`00bfdb10`](#insn-00bfdb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb68`](#insn-00bfdb68) → [`00bfdb10`](#insn-00bfdb10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb74`](#insn-00bfdb74) → [`00bfdbe4`](#insn-00bfdbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb80`](#insn-00bfdb80) → [`00bfdba4`](#insn-00bfdba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdba0`](#insn-00bfdba0) → [`00bfdbe4`](#insn-00bfdbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbb8`](#insn-00bfdbb8) → [`00bfdb84`](#insn-00bfdb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbcc`](#insn-00bfdbcc) → [`00bfdbec`](#insn-00bfdbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbd8`](#insn-00bfdbd8) → [`00bfdb90`](#insn-00bfdb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbe0`](#insn-00bfdbe0) → [`00bfdb98`](#insn-00bfdb98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbe8`](#insn-00bfdbe8) → [`00bfdbf0`](#insn-00bfdbf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc04`](#insn-00bfdc04) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc0c`](#insn-00bfdc0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc10`](#insn-00bfdc10) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc14`](#insn-00bfdc14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdc18`](#insn-00bfdc18) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdac0`](#insn-00bfdac0)

~~~json
{
  "source": "00bfdac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdac4`](#insn-00bfdac4)

~~~json
{
  "source": "00bfdac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdac8`](#insn-00bfdac8)

~~~json
{
  "source": "00bfdac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdacc`](#insn-00bfdacc)

~~~json
{
  "source": "00bfdacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdaf0`](#insn-00bfdaf0)

~~~json
{
  "source": "00bfdaf0",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdaf4`](#insn-00bfdaf4)

~~~json
{
  "source": "00bfdaf4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdaf8`](#insn-00bfdaf8)

~~~json
{
  "source": "00bfdaf8",
  "target": "00bfdc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb04`](#insn-00bfdb04)

~~~json
{
  "source": "00bfdb04",
  "target": "00bfdb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb0c`](#insn-00bfdb0c)

~~~json
{
  "source": "00bfdb0c",
  "target": "00bfdb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb14`](#insn-00bfdb14)

~~~json
{
  "source": "00bfdb14",
  "target": "00bfdbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb2c`](#insn-00bfdb2c)

~~~json
{
  "source": "00bfdb2c",
  "target": "00bfdb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb3c`](#insn-00bfdb3c)

~~~json
{
  "source": "00bfdb3c",
  "target": "00bfdb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb50`](#insn-00bfdb50)

~~~json
{
  "source": "00bfdb50",
  "target": "00bfdbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb5c`](#insn-00bfdb5c)

~~~json
{
  "source": "00bfdb5c",
  "target": "00bfdb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb68`](#insn-00bfdb68)

~~~json
{
  "source": "00bfdb68",
  "target": "00bfdb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb74`](#insn-00bfdb74)

~~~json
{
  "source": "00bfdb74",
  "target": "00bfdbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb80`](#insn-00bfdb80)

~~~json
{
  "source": "00bfdb80",
  "target": "00bfdba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdba0`](#insn-00bfdba0)

~~~json
{
  "source": "00bfdba0",
  "target": "00bfdbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbb8`](#insn-00bfdbb8)

~~~json
{
  "source": "00bfdbb8",
  "target": "00bfdb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbcc`](#insn-00bfdbcc)

~~~json
{
  "source": "00bfdbcc",
  "target": "00bfdbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbd8`](#insn-00bfdbd8)

~~~json
{
  "source": "00bfdbd8",
  "target": "00bfdb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbe0`](#insn-00bfdbe0)

~~~json
{
  "source": "00bfdbe0",
  "target": "00bfdb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbe8`](#insn-00bfdbe8)

~~~json
{
  "source": "00bfdbe8",
  "target": "00bfdbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc04`](#insn-00bfdc04)

~~~json
{
  "source": "00bfdc04",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdc0c`](#insn-00bfdc0c)

~~~json
{
  "source": "00bfdc0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc10`](#insn-00bfdc10)

~~~json
{
  "source": "00bfdc10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc14`](#insn-00bfdc14)

~~~json
{
  "source": "00bfdc14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdc18`](#insn-00bfdc18)

~~~json
{
  "source": "00bfdc18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
