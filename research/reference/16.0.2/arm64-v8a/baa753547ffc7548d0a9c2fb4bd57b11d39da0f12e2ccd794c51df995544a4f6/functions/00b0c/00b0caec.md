# 00b0caec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b0ca50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-3f4bc19a21260a66c6800b50304b5823)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b0dae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0d/00b0dae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0030.md#compare-0e4f20c009504ff9bf524445d973befc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0caec",
  "name": "FUN_00b0caec",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4c73caa9efe1b563ef7efa498cdc55d72edd57e68ae383eb338d93cd694a269",
  "source_text_sha256": "a4c73caa9efe1b563ef7efa498cdc55d72edd57e68ae383eb338d93cd694a269",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0caec",
        "00b0cc77"
      ]
    ],
    "bytes_sha256": "042b920ca8875aea1a1bd21e5e7983ce1cb60e61a0f01157bcf684cb5ef6af88",
    "instruction_count": 99,
    "instruction_bytes": 396,
    "body_bytes": 396,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0af3c](../00b0a/00b0af3c.md)

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [00b0cac4](../00b0c/00b0cac4.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2188 bytes

~~~c

undefined8 * FUN_00b0caec(long *param_1,undefined8 *param_2)

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
    FUN_00b0cac4(param_1);
LAB_00b0cc74:
                    /* WARNING: Subroutine does not return */
    FUN_00440f00();
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
    if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00b0cc74;
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
<a id="insn-00b0caec"></a> `00b0caec` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b0caf0"></a> `00b0caf0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0caf4"></a> `00b0caf4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0caf8"></a> `00b0caf8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0cafc"></a> `00b0cafc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0cb00"></a> `00b0cb00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0cb04"></a> `00b0cb04` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0cb08"></a> `00b0cb08` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b0cb0c"></a> `00b0cb0c` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00b0cb10"></a> `00b0cb10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0cb14"></a> `00b0cb14` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b0cb18"></a> `00b0cb18` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cb1c"></a> `00b0cb1c` | `17 7d 0b 9b` | mul x23,x8,x11 | `FALL_THROUGH`
<a id="insn-00b0cb20"></a> `00b0cb20` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b0cb24"></a> `00b0cb24` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00b0cb28"></a> `00b0cb28` | `e9 06 00 91` | add x9,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cb2c"></a> `00b0cb2c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b0cb30"></a> `00b0cb30` | `e8 09 00 54` | b.hi 0x00b0cc6c | `CONDITIONAL_JUMP`
<a id="insn-00b0cb34"></a> `00b0cb34` | `6c 0a 40 f9` | ldr x12,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cb38"></a> `00b0cb38` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b0cb3c"></a> `00b0cb3c` | `8a 01 0a cb` | sub x10,x12,x10 | `FALL_THROUGH`
<a id="insn-00b0cb40"></a> `00b0cb40` | `ec f3 00 b2` | orr x12,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00b0cb44"></a> `00b0cb44` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cb48"></a> `00b0cb48` | `ac aa e0 f2` | movk x12,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00b0cb4c"></a> `00b0cb4c` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b0cb50"></a> `00b0cb50` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b0cb54"></a> `00b0cb54` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00b0cb58"></a> `00b0cb58` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00b0cb5c"></a> `00b0cb5c` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00b0cb60"></a> `00b0cb60` | `35 31 88 9a` | csel x21,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00b0cb64"></a> `00b0cb64` | `f5 00 00 b4` | cbz x21,0x00b0cb80 | `CONDITIONAL_JUMP`
<a id="insn-00b0cb68"></a> `00b0cb68` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00b0cb6c"></a> `00b0cb6c` | `48 08 00 54` | b.hi 0x00b0cc74 | `CONDITIONAL_JUMP`
<a id="insn-00b0cb70"></a> `00b0cb70` | `a8 06 15 8b` | add x8,x21,x21, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00b0cb74"></a> `00b0cb74` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cb78"></a> `00b0cb78` | `fa 2c 05 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cb7c"></a> `00b0cb7c` | `02 00 00 14` | b 0x00b0cb84 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cb80"></a> `00b0cb80` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00b0cb84"></a> `00b0cb84` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00b0cb88"></a> `00b0cb88` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-00b0cb8c"></a> `00b0cb8c` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00b0cb90"></a> `00b0cb90` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b0cb94"></a> `00b0cb94` | `e9 02 08 9b` | madd x9,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0cb98"></a> `00b0cb98` | `8a 0a 40 f9` | ldr x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cb9c"></a> `00b0cb9c` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cba0"></a> `00b0cba0` | `79 52 40 a9` | ldp x25,x20,[x19] | `FALL_THROUGH`
<a id="insn-00b0cba4"></a> `00b0cba4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b0cba8"></a> `00b0cba8` | `b6 02 08 9b` | madd x22,x21,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0cbac"></a> `00b0cbac` | `8b 02 19 eb` | subs x11,x20,x25 | `FALL_THROUGH`
<a id="insn-00b0cbb0"></a> `00b0cbb0` | `88 02 19 eb` | subs x8,x20,x25 | `FALL_THROUGH`
<a id="insn-00b0cbb4"></a> `00b0cbb4` | `38 01 0b cb` | sub x24,x9,x11 | `FALL_THROUGH`
<a id="insn-00b0cbb8"></a> `00b0cbb8` | `35 61 00 91` | add x21,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00b0cbbc"></a> `00b0cbbc` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00b0cbc0"></a> `00b0cbc0` | `2a 09 00 f9` | str x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cbc4"></a> `00b0cbc4` | `c0 03 00 54` | b.eq 0x00b0cc3c | `CONDITIONAL_JUMP`
<a id="insn-00b0cbc8"></a> `00b0cbc8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b0cbcc"></a> `00b0cbcc` | `e9 f3 00 b2` | orr x9,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00b0cbd0"></a> `00b0cbd0` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b0cbd4"></a> `00b0cbd4` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00b0cbd8"></a> `00b0cbd8` | `ea 7e 09 9b` | mul x10,x23,x9 | `FALL_THROUGH`
<a id="insn-00b0cbdc"></a> `00b0cbdc` | `08 29 09 9b` | madd x8,x8,x9,x10 | `FALL_THROUGH`
<a id="insn-00b0cbe0"></a> `00b0cbe0` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00b0cbe4"></a> `00b0cbe4` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0cbe8"></a> `00b0cbe8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b0cbec"></a> `00b0cbec` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00b0cbf0"></a> `00b0cbf0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b0cbf4"></a> `00b0cbf4` | `00 01 9f 3c` | stur q0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00b0cbf8"></a> `00b0cbf8` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cbfc"></a> `00b0cbfc` | `0a 85 01 f8` | str x10,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00b0cc00"></a> `00b0cc00` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00b0cc04"></a> `00b0cc04` | `3f 09 00 f9` | str xzr,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc08"></a> `00b0cc08` | `29 61 00 91` | add x9,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00b0cc0c"></a> `00b0cc0c` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00b0cc10"></a> `00b0cc10` | `e1 fe ff 54` | b.ne 0x00b0cbec | `CONDITIONAL_JUMP`
<a id="insn-00b0cc14"></a> `00b0cc14` | `04 00 00 14` | b 0x00b0cc24 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cc18"></a> `00b0cc18` | `39 63 00 91` | add x25,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00b0cc1c"></a> `00b0cc1c` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00b0cc20"></a> `00b0cc20` | `c0 00 00 54` | b.eq 0x00b0cc38 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc24"></a> `00b0cc24` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00b0cc28"></a> `00b0cc28` | `80 ff ff b4` | cbz x0,0x00b0cc18 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc2c"></a> `00b0cc2c` | `20 07 00 f9` | str x0,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cc30"></a> `00b0cc30` | `d4 2c 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cc34"></a> `00b0cc34` | `f9 ff ff 17` | b 0x00b0cc18 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cc38"></a> `00b0cc38` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00b0cc3c"></a> `00b0cc3c` | `78 56 00 a9` | stp x24,x21,[x19] | `FALL_THROUGH`
<a id="insn-00b0cc40"></a> `00b0cc40` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc44"></a> `00b0cc44` | `74 00 00 b4` | cbz x20,0x00b0cc50 | `CONDITIONAL_JUMP`
<a id="insn-00b0cc48"></a> `00b0cc48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0cc4c"></a> `00b0cc4c` | `cd 2c 05 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cc50"></a> `00b0cc50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b0cc54"></a> `00b0cc54` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0cc58"></a> `00b0cc58` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cc5c"></a> `00b0cc5c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0cc60"></a> `00b0cc60` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0cc64"></a> `00b0cc64` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b0cc68"></a> `00b0cc68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0cc6c"></a> `00b0cc6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0cc70"></a> `00b0cc70` | `95 ff ff 97` | bl 0x00b0cac4 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cc74"></a> `00b0cc74` | `a3 d0 e4 97` | bl 0x00440f00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0caec`](#insn-00b0caec) 範囲 `[['00b0caec', '00b0cb33']]`
  - `CONDITIONAL_JUMP` [`00b0cb30`](#insn-00b0cb30) → [`00b0cc6c`](#insn-00b0cc6c)
  - `FALL_THROUGH` [`00b0cb30`](#insn-00b0cb30) → [`00b0cb34`](#insn-00b0cb34)
- ブロック [`00b0cb34`](#insn-00b0cb34) 範囲 `[['00b0cb34', '00b0cb67']]`
  - `CONDITIONAL_JUMP` [`00b0cb64`](#insn-00b0cb64) → [`00b0cb80`](#insn-00b0cb80)
  - `FALL_THROUGH` [`00b0cb64`](#insn-00b0cb64) → [`00b0cb68`](#insn-00b0cb68)
- ブロック [`00b0cb68`](#insn-00b0cb68) 範囲 `[['00b0cb68', '00b0cb6f']]`
  - `CONDITIONAL_JUMP` [`00b0cb6c`](#insn-00b0cb6c) → [`00b0cc74`](#insn-00b0cc74)
  - `FALL_THROUGH` [`00b0cb6c`](#insn-00b0cb6c) → [`00b0cb70`](#insn-00b0cb70)
- ブロック [`00b0cb70`](#insn-00b0cb70) 範囲 `[['00b0cb70', '00b0cb7f']]`
  - `UNCONDITIONAL_JUMP` [`00b0cb7c`](#insn-00b0cb7c) → [`00b0cb84`](#insn-00b0cb84)
- ブロック [`00b0cb80`](#insn-00b0cb80) 範囲 `[['00b0cb80', '00b0cb83']]`
  - `FALL_THROUGH` [`00b0cb80`](#insn-00b0cb80) → [`00b0cb84`](#insn-00b0cb84)
- ブロック [`00b0cb84`](#insn-00b0cb84) 範囲 `[['00b0cb84', '00b0cbc7']]`
  - `CONDITIONAL_JUMP` [`00b0cbc4`](#insn-00b0cbc4) → [`00b0cc3c`](#insn-00b0cc3c)
  - `FALL_THROUGH` [`00b0cbc4`](#insn-00b0cbc4) → [`00b0cbc8`](#insn-00b0cbc8)
- ブロック [`00b0cbc8`](#insn-00b0cbc8) 範囲 `[['00b0cbc8', '00b0cbeb']]`
  - `FALL_THROUGH` [`00b0cbe8`](#insn-00b0cbe8) → [`00b0cbec`](#insn-00b0cbec)
- ブロック [`00b0cbec`](#insn-00b0cbec) 範囲 `[['00b0cbec', '00b0cc13']]`
  - `CONDITIONAL_JUMP` [`00b0cc10`](#insn-00b0cc10) → [`00b0cbec`](#insn-00b0cbec)
  - `FALL_THROUGH` [`00b0cc10`](#insn-00b0cc10) → [`00b0cc14`](#insn-00b0cc14)
- ブロック [`00b0cc14`](#insn-00b0cc14) 範囲 `[['00b0cc14', '00b0cc17']]`
  - `UNCONDITIONAL_JUMP` [`00b0cc14`](#insn-00b0cc14) → [`00b0cc24`](#insn-00b0cc24)
- ブロック [`00b0cc18`](#insn-00b0cc18) 範囲 `[['00b0cc18', '00b0cc23']]`
  - `CONDITIONAL_JUMP` [`00b0cc20`](#insn-00b0cc20) → [`00b0cc38`](#insn-00b0cc38)
  - `FALL_THROUGH` [`00b0cc20`](#insn-00b0cc20) → [`00b0cc24`](#insn-00b0cc24)
- ブロック [`00b0cc24`](#insn-00b0cc24) 範囲 `[['00b0cc24', '00b0cc2b']]`
  - `CONDITIONAL_JUMP` [`00b0cc28`](#insn-00b0cc28) → [`00b0cc18`](#insn-00b0cc18)
  - `FALL_THROUGH` [`00b0cc28`](#insn-00b0cc28) → [`00b0cc2c`](#insn-00b0cc2c)
- ブロック [`00b0cc2c`](#insn-00b0cc2c) 範囲 `[['00b0cc2c', '00b0cc37']]`
  - `UNCONDITIONAL_JUMP` [`00b0cc34`](#insn-00b0cc34) → [`00b0cc18`](#insn-00b0cc18)
- ブロック [`00b0cc38`](#insn-00b0cc38) 範囲 `[['00b0cc38', '00b0cc3b']]`
  - `FALL_THROUGH` [`00b0cc38`](#insn-00b0cc38) → [`00b0cc3c`](#insn-00b0cc3c)
- ブロック [`00b0cc3c`](#insn-00b0cc3c) 範囲 `[['00b0cc3c', '00b0cc47']]`
  - `CONDITIONAL_JUMP` [`00b0cc44`](#insn-00b0cc44) → [`00b0cc50`](#insn-00b0cc50)
  - `FALL_THROUGH` [`00b0cc44`](#insn-00b0cc44) → [`00b0cc48`](#insn-00b0cc48)
- ブロック [`00b0cc48`](#insn-00b0cc48) 範囲 `[['00b0cc48', '00b0cc4f']]`
  - `FALL_THROUGH` [`00b0cc4c`](#insn-00b0cc4c) → [`00b0cc50`](#insn-00b0cc50)
- ブロック [`00b0cc50`](#insn-00b0cc50) 範囲 `[['00b0cc50', '00b0cc6b']]`
- ブロック [`00b0cc6c`](#insn-00b0cc6c) 範囲 `[['00b0cc6c', '00b0cc73']]`
  - `FALL_THROUGH` [`00b0cc70`](#insn-00b0cc70) → [`00b0cc74`](#insn-00b0cc74)
- ブロック [`00b0cc74`](#insn-00b0cc74) 範囲 `[['00b0cc74', '00b0cc77']]`

## 命令位置別の参照

- [`00b0caec`](#insn-00b0caec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0caf0`](#insn-00b0caf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0caf4`](#insn-00b0caf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0caf8`](#insn-00b0caf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cafc`](#insn-00b0cafc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cb30`](#insn-00b0cb30) → [`00b0cc6c`](#insn-00b0cc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cb64`](#insn-00b0cb64) → [`00b0cb80`](#insn-00b0cb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cb6c`](#insn-00b0cb6c) → [`00b0cc74`](#insn-00b0cc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cb78`](#insn-00b0cb78) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00b0cb7c`](#insn-00b0cb7c) → [`00b0cb84`](#insn-00b0cb84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cbc4`](#insn-00b0cbc4) → [`00b0cc3c`](#insn-00b0cc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc10`](#insn-00b0cc10) → [`00b0cbec`](#insn-00b0cbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc14`](#insn-00b0cc14) → [`00b0cc24`](#insn-00b0cc24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc20`](#insn-00b0cc20) → [`00b0cc38`](#insn-00b0cc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc28`](#insn-00b0cc28) → [`00b0cc18`](#insn-00b0cc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc30`](#insn-00b0cc30) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc34`](#insn-00b0cc34) → [`00b0cc18`](#insn-00b0cc18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc44`](#insn-00b0cc44) → [`00b0cc50`](#insn-00b0cc50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc4c`](#insn-00b0cc4c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc54`](#insn-00b0cc54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc58`](#insn-00b0cc58) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc5c`](#insn-00b0cc5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc60`](#insn-00b0cc60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc64`](#insn-00b0cc64) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc70`](#insn-00b0cc70) → [`00b0cac4`](00b0cac4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0cac4` · 推定シンボル `None` · 推定型 `None`
- [`00b0cc74`](#insn-00b0cc74) → [`00440f00`](../00440/00440f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440f00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0caec`](#insn-00b0caec)

~~~json
{
  "source": "00b0caec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0caf0`](#insn-00b0caf0)

~~~json
{
  "source": "00b0caf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0caf4`](#insn-00b0caf4)

~~~json
{
  "source": "00b0caf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0caf8`](#insn-00b0caf8)

~~~json
{
  "source": "00b0caf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cafc`](#insn-00b0cafc)

~~~json
{
  "source": "00b0cafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cb30`](#insn-00b0cb30)

~~~json
{
  "source": "00b0cb30",
  "target": "00b0cc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cb64`](#insn-00b0cb64)

~~~json
{
  "source": "00b0cb64",
  "target": "00b0cb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cb6c`](#insn-00b0cb6c)

~~~json
{
  "source": "00b0cb6c",
  "target": "00b0cc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cb78`](#insn-00b0cb78)

~~~json
{
  "source": "00b0cb78",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cb7c`](#insn-00b0cb7c)

~~~json
{
  "source": "00b0cb7c",
  "target": "00b0cb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cbc4`](#insn-00b0cbc4)

~~~json
{
  "source": "00b0cbc4",
  "target": "00b0cc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc10`](#insn-00b0cc10)

~~~json
{
  "source": "00b0cc10",
  "target": "00b0cbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc14`](#insn-00b0cc14)

~~~json
{
  "source": "00b0cc14",
  "target": "00b0cc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc20`](#insn-00b0cc20)

~~~json
{
  "source": "00b0cc20",
  "target": "00b0cc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc28`](#insn-00b0cc28)

~~~json
{
  "source": "00b0cc28",
  "target": "00b0cc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc30`](#insn-00b0cc30)

~~~json
{
  "source": "00b0cc30",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cc34`](#insn-00b0cc34)

~~~json
{
  "source": "00b0cc34",
  "target": "00b0cc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc44`](#insn-00b0cc44)

~~~json
{
  "source": "00b0cc44",
  "target": "00b0cc50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc4c`](#insn-00b0cc4c)

~~~json
{
  "source": "00b0cc4c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cc54`](#insn-00b0cc54)

~~~json
{
  "source": "00b0cc54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc58`](#insn-00b0cc58)

~~~json
{
  "source": "00b0cc58",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc5c`](#insn-00b0cc5c)

~~~json
{
  "source": "00b0cc5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc60`](#insn-00b0cc60)

~~~json
{
  "source": "00b0cc60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc64`](#insn-00b0cc64)

~~~json
{
  "source": "00b0cc64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cc70`](#insn-00b0cc70)

~~~json
{
  "source": "00b0cc70",
  "target": "00b0cac4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cc74`](#insn-00b0cc74)

~~~json
{
  "source": "00b0cc74",
  "target": "00440f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
