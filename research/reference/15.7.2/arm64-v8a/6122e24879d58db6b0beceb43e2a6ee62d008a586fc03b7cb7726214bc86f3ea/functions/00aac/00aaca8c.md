# 00aaca8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aacb54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-89d4f659d5d43ef25b4c6eed9e329ea0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaca8c",
  "name": "FUN_00aaca8c",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af12fae4c51b0e25cab138ca6f378406fbcf92c3d7a9e956e07998974aa3c916",
  "source_text_sha256": "af12fae4c51b0e25cab138ca6f378406fbcf92c3d7a9e956e07998974aa3c916",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaca8c",
        "00aacc17"
      ]
    ],
    "bytes_sha256": "6733de145682e004346b42f62304a0146aea1a9f9fa22455e6c13fcd48eb0ce7",
    "instruction_count": 99,
    "instruction_bytes": 396,
    "body_bytes": 396,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aaaedc](../00aaa/00aaaedc.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aaca64](../00aac/00aaca64.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2188 bytes

~~~c

undefined8 * FUN_00aaca8c(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  long lVar2;
  void *__ptr;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 uVar8;
  ulong uVar9;
  undefined8 *__ptr_00;
  undefined8 *puVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  
  lVar3 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar3 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
    FUN_00aaca64(param_1);
LAB_00aacc14:
                    /* WARNING: Subroutine does not return */
    FUN_0041e380();
  }
  lVar7 = param_1[2] - *param_1 >> 3;
  uVar9 = lVar7 * 0x5555555555555556;
  if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
    uVar9 = uVar1;
  }
  if (0x555555555555554 < (ulong)(lVar7 * -0x5555555555555555)) {
    uVar9 = 0xaaaaaaaaaaaaaaa;
  }
  if (uVar9 == 0) {
    lVar7 = 0;
  }
  else {
    if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00aacc14;
    lVar7 = _Znwm(uVar9 * 0x18);
  }
  uVar12 = param_2[1];
  uVar11 = *param_2;
  *param_2 = 0;
  param_2[1] = 0;
  puVar5 = (undefined8 *)(lVar7 + lVar3 * 8);
  uVar8 = param_2[2];
  param_2[2] = 0;
  puVar10 = (undefined8 *)*param_1;
  __ptr_00 = (undefined8 *)param_1[1];
  lVar2 = (long)__ptr_00 - (long)puVar10;
  puVar5[1] = uVar12;
  *puVar5 = uVar11;
  puVar5[2] = uVar8;
  if ((long)__ptr_00 - (long)puVar10 != 0) {
    puVar4 = (undefined8 *)(lVar3 * 8 + ((long)__ptr_00 - (long)puVar10 >> 3) * -8 + lVar7 + 0x10);
    puVar6 = puVar10;
    do {
      *puVar4 = 0;
      uVar8 = *puVar6;
      puVar4[-1] = puVar6[1];
      puVar4[-2] = uVar8;
      *puVar4 = puVar6[2];
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar6[2] = 0;
      puVar6 = puVar6 + 3;
      puVar4 = puVar4 + 3;
    } while (puVar6 != __ptr_00);
    do {
      __ptr = (void *)*puVar10;
      if (__ptr != (void *)0x0) {
        puVar10[1] = __ptr;
        _ZdlPv(__ptr);
      }
      puVar10 = puVar10 + 3;
    } while (puVar10 != __ptr_00);
    __ptr_00 = (undefined8 *)*param_1;
  }
  *param_1 = (long)puVar5 - lVar2;
  param_1[1] = (long)(puVar5 + 3);
  param_1[2] = lVar7 + uVar9 * 0x18;
  if (__ptr_00 != (undefined8 *)0x0) {
    _ZdlPv(__ptr_00);
  }
  return puVar5 + 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaca8c"></a> `00aaca8c` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00aaca90"></a> `00aaca90` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaca94"></a> `00aaca94` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaca98"></a> `00aaca98` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaca9c"></a> `00aaca9c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aacaa0"></a> `00aacaa0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aacaa4"></a> `00aacaa4` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00aacaa8"></a> `00aacaa8` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aacaac"></a> `00aacaac` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00aacab0"></a> `00aacab0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aacab4"></a> `00aacab4` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00aacab8"></a> `00aacab8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aacabc"></a> `00aacabc` | `17 7d 0b 9b` | mul x23,x8,x11 | `FALL_THROUGH`
<a id="insn-00aacac0"></a> `00aacac0` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aacac4"></a> `00aacac4` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00aacac8"></a> `00aacac8` | `e9 06 00 91` | add x9,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00aacacc"></a> `00aacacc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aacad0"></a> `00aacad0` | `e8 09 00 54` | b.hi 0x00aacc0c | `CONDITIONAL_JUMP`
<a id="insn-00aacad4"></a> `00aacad4` | `6c 0a 40 f9` | ldr x12,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aacad8"></a> `00aacad8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aacadc"></a> `00aacadc` | `8a 01 0a cb` | sub x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00aacae0"></a> `00aacae0` | `ec f3 00 b2` | orr x12,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00aacae4"></a> `00aacae4` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00aacae8"></a> `00aacae8` | `ac aa e0 f2` | movk x12,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00aacaec"></a> `00aacaec` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00aacaf0"></a> `00aacaf0` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00aacaf4"></a> `00aacaf4` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00aacaf8"></a> `00aacaf8` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00aacafc"></a> `00aacafc` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00aacb00"></a> `00aacb00` | `35 31 88 9a` | csel x21,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aacb04"></a> `00aacb04` | `f5 00 00 b4` | cbz x21,0x00aacb20 | `CONDITIONAL_JUMP`
<a id="insn-00aacb08"></a> `00aacb08` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00aacb0c"></a> `00aacb0c` | `48 08 00 54` | b.hi 0x00aacc14 | `CONDITIONAL_JUMP`
<a id="insn-00aacb10"></a> `00aacb10` | `a8 06 15 8b` | add x8,x21,x21, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00aacb14"></a> `00aacb14` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aacb18"></a> `00aacb18` | `0a b9 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aacb1c"></a> `00aacb1c` | `02 00 00 14` | b 0x00aacb24 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacb20"></a> `00aacb20` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00aacb24"></a> `00aacb24` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00aacb28"></a> `00aacb28` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-00aacb2c"></a> `00aacb2c` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aacb30"></a> `00aacb30` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aacb34"></a> `00aacb34` | `e9 02 08 9b` | madd x9,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-00aacb38"></a> `00aacb38` | `8a 0a 40 f9` | ldr x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aacb3c"></a> `00aacb3c` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aacb40"></a> `00aacb40` | `79 52 40 a9` | ldp x25,x20,[x19] | `FALL_THROUGH`
<a id="insn-00aacb44"></a> `00aacb44` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aacb48"></a> `00aacb48` | `b6 02 08 9b` | madd x22,x21,x8,x0 | `FALL_THROUGH`
<a id="insn-00aacb4c"></a> `00aacb4c` | `8b 02 19 eb` | subs x11,x20,x25 | `FALL_THROUGH`
<a id="insn-00aacb50"></a> `00aacb50` | `88 02 19 eb` | subs x8,x20,x25 | `FALL_THROUGH`
<a id="insn-00aacb54"></a> `00aacb54` | `38 01 0b cb` | sub x24,x9,x11 | `FALL_THROUGH`
<a id="insn-00aacb58"></a> `00aacb58` | `35 61 00 91` | add x21,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00aacb5c"></a> `00aacb5c` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacb60"></a> `00aacb60` | `2a 09 00 f9` | str x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00aacb64"></a> `00aacb64` | `c0 03 00 54` | b.eq 0x00aacbdc | `CONDITIONAL_JUMP`
<a id="insn-00aacb68"></a> `00aacb68` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aacb6c"></a> `00aacb6c` | `e9 f3 00 b2` | orr x9,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00aacb70"></a> `00aacb70` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aacb74"></a> `00aacb74` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00aacb78"></a> `00aacb78` | `ea 7e 09 9b` | mul x10,x23,x9 | `FALL_THROUGH`
<a id="insn-00aacb7c"></a> `00aacb7c` | `08 29 09 9b` | madd x8,x8,x9,x10 | `FALL_THROUGH`
<a id="insn-00aacb80"></a> `00aacb80` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00aacb84"></a> `00aacb84` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-00aacb88"></a> `00aacb88` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aacb8c"></a> `00aacb8c` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00aacb90"></a> `00aacb90` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacb94"></a> `00aacb94` | `00 01 9f 3c` | stur q0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00aacb98"></a> `00aacb98` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00aacb9c"></a> `00aacb9c` | `0a 85 01 f8` | str x10,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00aacba0"></a> `00aacba0` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00aacba4"></a> `00aacba4` | `3f 09 00 f9` | str xzr,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00aacba8"></a> `00aacba8` | `29 61 00 91` | add x9,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00aacbac"></a> `00aacbac` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00aacbb0"></a> `00aacbb0` | `e1 fe ff 54` | b.ne 0x00aacb8c | `CONDITIONAL_JUMP`
<a id="insn-00aacbb4"></a> `00aacbb4` | `04 00 00 14` | b 0x00aacbc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacbb8"></a> `00aacbb8` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00aacbbc"></a> `00aacbbc` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00aacbc0"></a> `00aacbc0` | `c0 00 00 54` | b.eq 0x00aacbd8 | `CONDITIONAL_JUMP`
<a id="insn-00aacbc4"></a> `00aacbc4` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00aacbc8"></a> `00aacbc8` | `80 ff ff b4` | cbz x0,0x00aacbb8 | `CONDITIONAL_JUMP`
<a id="insn-00aacbcc"></a> `00aacbcc` | `20 07 00 f9` | str x0,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00aacbd0"></a> `00aacbd0` | `e4 b8 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aacbd4"></a> `00aacbd4` | `f9 ff ff 17` | b 0x00aacbb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacbd8"></a> `00aacbd8` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00aacbdc"></a> `00aacbdc` | `78 56 00 a9` | stp x24,x21,[x19] | `FALL_THROUGH`
<a id="insn-00aacbe0"></a> `00aacbe0` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aacbe4"></a> `00aacbe4` | `74 00 00 b4` | cbz x20,0x00aacbf0 | `CONDITIONAL_JUMP`
<a id="insn-00aacbe8"></a> `00aacbe8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aacbec"></a> `00aacbec` | `dd b8 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aacbf0"></a> `00aacbf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aacbf4"></a> `00aacbf4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aacbf8"></a> `00aacbf8` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aacbfc"></a> `00aacbfc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aacc00"></a> `00aacc00` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aacc04"></a> `00aacc04` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00aacc08"></a> `00aacc08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aacc0c"></a> `00aacc0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aacc10"></a> `00aacc10` | `95 ff ff 97` | bl 0x00aaca64 | `UNCONDITIONAL_CALL`
<a id="insn-00aacc14"></a> `00aacc14` | `db c5 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaca8c`](#insn-00aaca8c) 範囲 `[['00aaca8c', '00aacad3']]`
  - `CONDITIONAL_JUMP` [`00aacad0`](#insn-00aacad0) → [`00aacc0c`](#insn-00aacc0c)
  - `FALL_THROUGH` [`00aacad0`](#insn-00aacad0) → [`00aacad4`](#insn-00aacad4)
- ブロック [`00aacad4`](#insn-00aacad4) 範囲 `[['00aacad4', '00aacb07']]`
  - `CONDITIONAL_JUMP` [`00aacb04`](#insn-00aacb04) → [`00aacb20`](#insn-00aacb20)
  - `FALL_THROUGH` [`00aacb04`](#insn-00aacb04) → [`00aacb08`](#insn-00aacb08)
- ブロック [`00aacb08`](#insn-00aacb08) 範囲 `[['00aacb08', '00aacb0f']]`
  - `CONDITIONAL_JUMP` [`00aacb0c`](#insn-00aacb0c) → [`00aacc14`](#insn-00aacc14)
  - `FALL_THROUGH` [`00aacb0c`](#insn-00aacb0c) → [`00aacb10`](#insn-00aacb10)
- ブロック [`00aacb10`](#insn-00aacb10) 範囲 `[['00aacb10', '00aacb1f']]`
  - `UNCONDITIONAL_JUMP` [`00aacb1c`](#insn-00aacb1c) → [`00aacb24`](#insn-00aacb24)
- ブロック [`00aacb20`](#insn-00aacb20) 範囲 `[['00aacb20', '00aacb23']]`
  - `FALL_THROUGH` [`00aacb20`](#insn-00aacb20) → [`00aacb24`](#insn-00aacb24)
- ブロック [`00aacb24`](#insn-00aacb24) 範囲 `[['00aacb24', '00aacb67']]`
  - `CONDITIONAL_JUMP` [`00aacb64`](#insn-00aacb64) → [`00aacbdc`](#insn-00aacbdc)
  - `FALL_THROUGH` [`00aacb64`](#insn-00aacb64) → [`00aacb68`](#insn-00aacb68)
- ブロック [`00aacb68`](#insn-00aacb68) 範囲 `[['00aacb68', '00aacb8b']]`
  - `FALL_THROUGH` [`00aacb88`](#insn-00aacb88) → [`00aacb8c`](#insn-00aacb8c)
- ブロック [`00aacb8c`](#insn-00aacb8c) 範囲 `[['00aacb8c', '00aacbb3']]`
  - `CONDITIONAL_JUMP` [`00aacbb0`](#insn-00aacbb0) → [`00aacb8c`](#insn-00aacb8c)
  - `FALL_THROUGH` [`00aacbb0`](#insn-00aacbb0) → [`00aacbb4`](#insn-00aacbb4)
- ブロック [`00aacbb4`](#insn-00aacbb4) 範囲 `[['00aacbb4', '00aacbb7']]`
  - `UNCONDITIONAL_JUMP` [`00aacbb4`](#insn-00aacbb4) → [`00aacbc4`](#insn-00aacbc4)
- ブロック [`00aacbb8`](#insn-00aacbb8) 範囲 `[['00aacbb8', '00aacbc3']]`
  - `CONDITIONAL_JUMP` [`00aacbc0`](#insn-00aacbc0) → [`00aacbd8`](#insn-00aacbd8)
  - `FALL_THROUGH` [`00aacbc0`](#insn-00aacbc0) → [`00aacbc4`](#insn-00aacbc4)
- ブロック [`00aacbc4`](#insn-00aacbc4) 範囲 `[['00aacbc4', '00aacbcb']]`
  - `CONDITIONAL_JUMP` [`00aacbc8`](#insn-00aacbc8) → [`00aacbb8`](#insn-00aacbb8)
  - `FALL_THROUGH` [`00aacbc8`](#insn-00aacbc8) → [`00aacbcc`](#insn-00aacbcc)
- ブロック [`00aacbcc`](#insn-00aacbcc) 範囲 `[['00aacbcc', '00aacbd7']]`
  - `UNCONDITIONAL_JUMP` [`00aacbd4`](#insn-00aacbd4) → [`00aacbb8`](#insn-00aacbb8)
- ブロック [`00aacbd8`](#insn-00aacbd8) 範囲 `[['00aacbd8', '00aacbdb']]`
  - `FALL_THROUGH` [`00aacbd8`](#insn-00aacbd8) → [`00aacbdc`](#insn-00aacbdc)
- ブロック [`00aacbdc`](#insn-00aacbdc) 範囲 `[['00aacbdc', '00aacbe7']]`
  - `CONDITIONAL_JUMP` [`00aacbe4`](#insn-00aacbe4) → [`00aacbf0`](#insn-00aacbf0)
  - `FALL_THROUGH` [`00aacbe4`](#insn-00aacbe4) → [`00aacbe8`](#insn-00aacbe8)
- ブロック [`00aacbe8`](#insn-00aacbe8) 範囲 `[['00aacbe8', '00aacbef']]`
  - `FALL_THROUGH` [`00aacbec`](#insn-00aacbec) → [`00aacbf0`](#insn-00aacbf0)
- ブロック [`00aacbf0`](#insn-00aacbf0) 範囲 `[['00aacbf0', '00aacc0b']]`
- ブロック [`00aacc0c`](#insn-00aacc0c) 範囲 `[['00aacc0c', '00aacc13']]`
  - `FALL_THROUGH` [`00aacc10`](#insn-00aacc10) → [`00aacc14`](#insn-00aacc14)
- ブロック [`00aacc14`](#insn-00aacc14) 範囲 `[['00aacc14', '00aacc17']]`

## 命令位置別の参照

- [`00aaca8c`](#insn-00aaca8c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaca90`](#insn-00aaca90) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaca94`](#insn-00aaca94) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaca98`](#insn-00aaca98) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaca9c`](#insn-00aaca9c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacad0`](#insn-00aacad0) → [`00aacc0c`](#insn-00aacc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacb04`](#insn-00aacb04) → [`00aacb20`](#insn-00aacb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacb0c`](#insn-00aacb0c) → [`00aacc14`](#insn-00aacc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacb18`](#insn-00aacb18) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aacb1c`](#insn-00aacb1c) → [`00aacb24`](#insn-00aacb24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacb64`](#insn-00aacb64) → [`00aacbdc`](#insn-00aacbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbb0`](#insn-00aacbb0) → [`00aacb8c`](#insn-00aacb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbb4`](#insn-00aacbb4) → [`00aacbc4`](#insn-00aacbc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbc0`](#insn-00aacbc0) → [`00aacbd8`](#insn-00aacbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbc8`](#insn-00aacbc8) → [`00aacbb8`](#insn-00aacbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbd0`](#insn-00aacbd0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aacbd4`](#insn-00aacbd4) → [`00aacbb8`](#insn-00aacbb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbe4`](#insn-00aacbe4) → [`00aacbf0`](#insn-00aacbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbec`](#insn-00aacbec) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aacbf4`](#insn-00aacbf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbf8`](#insn-00aacbf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacbfc`](#insn-00aacbfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc00`](#insn-00aacc00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc04`](#insn-00aacc04) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacc10`](#insn-00aacc10) → [`00aaca64`](00aaca64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaca64` · 推定シンボル `None` · 推定型 `None`
- [`00aacc14`](#insn-00aacc14) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaca8c`](#insn-00aaca8c)

~~~json
{
  "source": "00aaca8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaca90`](#insn-00aaca90)

~~~json
{
  "source": "00aaca90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaca94`](#insn-00aaca94)

~~~json
{
  "source": "00aaca94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaca98`](#insn-00aaca98)

~~~json
{
  "source": "00aaca98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaca9c`](#insn-00aaca9c)

~~~json
{
  "source": "00aaca9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacad0`](#insn-00aacad0)

~~~json
{
  "source": "00aacad0",
  "target": "00aacc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacb04`](#insn-00aacb04)

~~~json
{
  "source": "00aacb04",
  "target": "00aacb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacb0c`](#insn-00aacb0c)

~~~json
{
  "source": "00aacb0c",
  "target": "00aacc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacb18`](#insn-00aacb18)

~~~json
{
  "source": "00aacb18",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacb1c`](#insn-00aacb1c)

~~~json
{
  "source": "00aacb1c",
  "target": "00aacb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacb64`](#insn-00aacb64)

~~~json
{
  "source": "00aacb64",
  "target": "00aacbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbb0`](#insn-00aacbb0)

~~~json
{
  "source": "00aacbb0",
  "target": "00aacb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbb4`](#insn-00aacbb4)

~~~json
{
  "source": "00aacbb4",
  "target": "00aacbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbc0`](#insn-00aacbc0)

~~~json
{
  "source": "00aacbc0",
  "target": "00aacbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbc8`](#insn-00aacbc8)

~~~json
{
  "source": "00aacbc8",
  "target": "00aacbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbd0`](#insn-00aacbd0)

~~~json
{
  "source": "00aacbd0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacbd4`](#insn-00aacbd4)

~~~json
{
  "source": "00aacbd4",
  "target": "00aacbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbe4`](#insn-00aacbe4)

~~~json
{
  "source": "00aacbe4",
  "target": "00aacbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbec`](#insn-00aacbec)

~~~json
{
  "source": "00aacbec",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacbf4`](#insn-00aacbf4)

~~~json
{
  "source": "00aacbf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbf8`](#insn-00aacbf8)

~~~json
{
  "source": "00aacbf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacbfc`](#insn-00aacbfc)

~~~json
{
  "source": "00aacbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc00`](#insn-00aacc00)

~~~json
{
  "source": "00aacc00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc04`](#insn-00aacc04)

~~~json
{
  "source": "00aacc04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacc10`](#insn-00aacc10)

~~~json
{
  "source": "00aacc10",
  "target": "00aaca64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacc14`](#insn-00aacc14)

~~~json
{
  "source": "00aacc14",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
