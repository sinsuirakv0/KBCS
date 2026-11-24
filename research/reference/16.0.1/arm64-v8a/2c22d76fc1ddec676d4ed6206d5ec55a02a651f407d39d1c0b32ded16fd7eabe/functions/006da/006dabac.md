# 006dabac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006dab6c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0021.md#compare-45eb0a624fb96a5316b8f624933cf680)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `006dac04`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0032.md#compare-69bb4d1550afd18cff2e32c274ab7bec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dabac",
  "name": "FUN_006dabac",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4062b819a8bbce9188351d2b798942bec33776733938e238c5ddae50c9bdb8b0",
  "source_text_sha256": "4062b819a8bbce9188351d2b798942bec33776733938e238c5ddae50c9bdb8b0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dabac",
        "006dad43"
      ]
    ],
    "bytes_sha256": "00bb5d9ce1e49d4d267d725a15ef56ae90de604a5030781f6c2fc372ddf817f7",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [006dad74](../006da/006dad74.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [006f9ed8](../006f9/006f9ed8.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3206 bytes

~~~c

void FUN_006dabac(undefined4 *param_1,long *param_2)

{
  ulong uVar1;
  ulong *puVar2;
  ulong *puVar3;
  undefined4 uVar4;
  int iVar5;
  ulong uVar6;
  long lVar7;
  void *__dest;
  undefined8 *puVar8;
  ulong uVar9;
  ulong uVar10;
  int iVar11;
  void *__src;
  ulong *puVar12;
  long lVar13;
  
  puVar8 = (undefined8 *)(param_1 + 2);
                    /* try { // try from 006dabb0 to 007dabf7 has its CatchHandler @ 006daf20 */
  *puVar8 = 0;
  *(undefined8 *)(param_1 + 4) = 0;
  *(undefined8 *)(param_1 + 6) = 0;
  FUN_0048791c(param_2);
  uVar4 = FUN_0048793c(param_2,0);
                    /* try { // try from 006dabf8 to 007dac0b has its CatchHandler @ 006daf0c */
  *param_1 = uVar4;
  uVar4 = FUN_0048793c(param_2,1);
  param_1[1] = uVar4;
  *(undefined8 *)(param_1 + 4) = *(undefined8 *)(param_1 + 2);
  FUN_0048791c(param_2);
  iVar11 = 0;
  do {
                    /* try { // try from 006dac40 to 007dac47 has its CatchHandler @ 006daef8 */
    iVar5 = (**(code **)(*param_2 + 0x28))(param_2);
    if (iVar5 <= iVar11) {
                    /* try { // try from 006dad28 to 007dad3b has its CatchHandler @ 006daed0 */
      return;
    }
    uVar6 = FUN_0048793c(param_2,iVar11);
    lVar7 = FUN_0048793c(param_2,iVar11 + 1);
    puVar3 = *(ulong **)(param_1 + 4);
    if (puVar3 < *(ulong **)(param_1 + 6)) {
      puVar12 = puVar3 + 1;
      *puVar3 = uVar6 & 0xffffffff | lVar7 << 0x20;
    }
    else {
                    /* try { // try from 006dac80 to 007dac87 has its CatchHandler @ 006daee4 */
      __src = (void *)*puVar8;
      lVar13 = (long)puVar3 - (long)__src >> 3;
                    /* try { // try from 006dac90 to 007dac97 has its CatchHandler @ 006daec0 */
      uVar1 = lVar13 + 1;
      if (uVar1 >> 0x3d != 0) {
        FUN_006f9ed8(puVar8);
LAB_006dad40:
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 006dad40 to 007dad77 has its CatchHandler @ 006daeec */
        FUN_00440ec0();
      }
      uVar9 = (long)*(ulong **)(param_1 + 6) - (long)__src;
      uVar10 = (long)uVar9 >> 2;
                    /* try { // try from 006daca8 to 007dacb7 has its CatchHandler @ 006daeb8 */
      if (uVar10 <= uVar1) {
        uVar10 = uVar1;
      }
                    /* try { // try from 006dacb8 to 007dacc7 has its CatchHandler @ 006daeb4 */
      if (0x7ffffffffffffff7 < uVar9) {
        uVar10 = 0x1fffffffffffffff;
      }
      if (uVar10 == 0) {
        __dest = (void *)0x0;
      }
      else {
        if (uVar10 >> 0x3d != 0) goto LAB_006dad40;
        __dest = (void *)_Znwm(uVar10 << 3);
      }
      puVar2 = (ulong *)((long)__dest + lVar13 * 8);
                    /* try { // try from 006dacf4 to 007dad07 has its CatchHandler @ 006daeac */
      puVar12 = puVar2 + 1;
      *puVar2 = uVar6 & 0xffffffff | lVar7 << 0x20;
      memcpy(__dest,__src,(long)puVar3 - (long)__src);
      *(void **)(param_1 + 2) = __dest;
      *(ulong **)(param_1 + 4) = puVar12;
      *(void **)(param_1 + 6) = (void *)((long)__dest + uVar10 * 8);
      if (__src != (void *)0x0) {
        _ZdlPv(__src);
      }
    }
    *(ulong **)(param_1 + 4) = puVar12;
    iVar11 = iVar11 + 2;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dabac"></a> `006dabac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006dabb0"></a> `006dabb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dabb4"></a> `006dabb4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dabb8"></a> `006dabb8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dabbc"></a> `006dabbc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006dabc0"></a> `006dabc0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006dabc4"></a> `006dabc4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006dabc8"></a> `006dabc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-006dabcc"></a> `006dabcc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-006dabd0"></a> `006dabd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006dabd4"></a> `006dabd4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-006dabd8"></a> `006dabd8` | `1f fd 80 a9` | stp xzr,xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-006dabdc"></a> `006dabdc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dabe0"></a> `006dabe0` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006dabe4"></a> `006dabe4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-006dabe8"></a> `006dabe8` | `4d b3 f6 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-006dabec"></a> `006dabec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dabf0"></a> `006dabf0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006dabf4"></a> `006dabf4` | `52 b3 f6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-006dabf8"></a> `006dabf8` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-006dabfc"></a> `006dabfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dac00"></a> `006dac00` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006dac04"></a> `006dac04` | `4e b3 f6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-006dac08"></a> `006dac08` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006dac0c"></a> `006dac0c` | `60 06 00 b9` | str w0,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-006dac10"></a> `006dac10` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006dac14"></a> `006dac14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dac18"></a> `006dac18` | `41 b3 f6 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-006dac1c"></a> `006dac1c` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-006dac20"></a> `006dac20` | `06 00 00 14` | b 0x006dac38 | `UNCONDITIONAL_JUMP`
<a id="insn-006dac24"></a> `006dac24` | `e8 03 17 2a` | mov w8,w23 | `FALL_THROUGH`
<a id="insn-006dac28"></a> `006dac28` | `08 81 19 aa` | orr x8,x8,x25, LSL #0x20 | `FALL_THROUGH`
<a id="insn-006dac2c"></a> `006dac2c` | `88 87 00 f8` | str x8,[x28], #0x8 | `FALL_THROUGH`
<a id="insn-006dac30"></a> `006dac30` | `7c 0a 00 f9` | str x28,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006dac34"></a> `006dac34` | `d6 06 00 11` | add w22,w22,#0x1 | `FALL_THROUGH`
<a id="insn-006dac38"></a> `006dac38` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006dac3c"></a> `006dac3c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-006dac40"></a> `006dac40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dac44"></a> `006dac44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006dac48"></a> `006dac48` | `df 02 00 6b` | cmp w22,w0 | `FALL_THROUGH`
<a id="insn-006dac4c"></a> `006dac4c` | `6a 06 00 54` | b.ge 0x006dad18 | `CONDITIONAL_JUMP`
<a id="insn-006dac50"></a> `006dac50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dac54"></a> `006dac54` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-006dac58"></a> `006dac58` | `39 b3 f6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-006dac5c"></a> `006dac5c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006dac60"></a> `006dac60` | `d6 06 00 11` | add w22,w22,#0x1 | `FALL_THROUGH`
<a id="insn-006dac64"></a> `006dac64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006dac68"></a> `006dac68` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-006dac6c"></a> `006dac6c` | `34 b3 f6 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-006dac70"></a> `006dac70` | `7c 22 41 a9` | ldp x28,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006dac74"></a> `006dac74` | `f9 03 00 2a` | mov w25,w0 | `FALL_THROUGH`
<a id="insn-006dac78"></a> `006dac78` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-006dac7c"></a> `006dac7c` | `43 fd ff 54` | b.cc 0x006dac24 | `CONDITIONAL_JUMP`
<a id="insn-006dac80"></a> `006dac80` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dac84"></a> `006dac84` | `38 01 40 f9` | ldr x24,[x9] | `FALL_THROUGH`
<a id="insn-006dac88"></a> `006dac88` | `9a 03 18 cb` | sub x26,x28,x24 | `FALL_THROUGH`
<a id="insn-006dac8c"></a> `006dac8c` | `5c ff 43 93` | asr x28,x26,#0x3 | `FALL_THROUGH`
<a id="insn-006dac90"></a> `006dac90` | `89 07 00 91` | add x9,x28,#0x1 | `FALL_THROUGH`
<a id="insn-006dac94"></a> `006dac94` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-006dac98"></a> `006dac98` | `0a 05 00 b5` | cbnz x10,0x006dad38 | `CONDITIONAL_JUMP`
<a id="insn-006dac9c"></a> `006dac9c` | `08 01 18 cb` | sub x8,x8,x24 | `FALL_THROUGH`
<a id="insn-006daca0"></a> `006daca0` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006daca4"></a> `006daca4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-006daca8"></a> `006daca8` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-006dacac"></a> `006dacac` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006dacb0"></a> `006dacb0` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-006dacb4"></a> `006dacb4` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-006dacb8"></a> `006dacb8` | `34 31 88 9a` | csel x20,x9,x8,cc | `FALL_THROUGH`
<a id="insn-006dacbc"></a> `006dacbc` | `f4 00 00 b4` | cbz x20,0x006dacd8 | `CONDITIONAL_JUMP`
<a id="insn-006dacc0"></a> `006dacc0` | `88 fe 7d d3` | lsr x8,x20,#0x3d | `FALL_THROUGH`
<a id="insn-006dacc4"></a> `006dacc4` | `e8 03 00 b5` | cbnz x8,0x006dad40 | `CONDITIONAL_JUMP`
<a id="insn-006dacc8"></a> `006dacc8` | `80 f2 7d d3` | lsl x0,x20,#0x3 | `FALL_THROUGH`
<a id="insn-006daccc"></a> `006daccc` | `71 f4 15 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-006dacd0"></a> `006dacd0` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-006dacd4"></a> `006dacd4` | `02 00 00 14` | b 0x006dacdc | `UNCONDITIONAL_JUMP`
<a id="insn-006dacd8"></a> `006dacd8` | `fb 03 1f aa` | mov x27,xzr | `FALL_THROUGH`
<a id="insn-006dacdc"></a> `006dacdc` | `e8 03 17 2a` | mov w8,w23 | `FALL_THROUGH`
<a id="insn-006dace0"></a> `006dace0` | `7c 0f 1c 8b` | add x28,x27,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006dace4"></a> `006dace4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-006dace8"></a> `006dace8` | `08 81 19 aa` | orr x8,x8,x25, LSL #0x20 | `FALL_THROUGH`
<a id="insn-006dacec"></a> `006dacec` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-006dacf0"></a> `006dacf0` | `e2 03 1a aa` | mov x2,x26 | `FALL_THROUGH`
<a id="insn-006dacf4"></a> `006dacf4` | `74 0f 14 8b` | add x20,x27,x20, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006dacf8"></a> `006dacf8` | `88 87 00 f8` | str x8,[x28], #0x8 | `FALL_THROUGH`
<a id="insn-006dacfc"></a> `006dacfc` | `c1 f4 15 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-006dad00"></a> `006dad00` | `7b f2 00 a9` | stp x27,x28,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006dad04"></a> `006dad04` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-006dad08"></a> `006dad08` | `58 f9 ff b4` | cbz x24,0x006dac30 | `CONDITIONAL_JUMP`
<a id="insn-006dad0c"></a> `006dad0c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-006dad10"></a> `006dad10` | `68 f4 15 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-006dad14"></a> `006dad14` | `c7 ff ff 17` | b 0x006dac30 | `UNCONDITIONAL_JUMP`
<a id="insn-006dad18"></a> `006dad18` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006dad1c"></a> `006dad1c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006dad20"></a> `006dad20` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006dad24"></a> `006dad24` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dad28"></a> `006dad28` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dad2c"></a> `006dad2c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dad30"></a> `006dad30` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006dad34"></a> `006dad34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006dad38"></a> `006dad38` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006dad3c"></a> `006dad3c` | `67 7c 00 94` | bl 0x006f9ed8 | `UNCONDITIONAL_CALL`
<a id="insn-006dad40"></a> `006dad40` | `60 98 f5 97` | bl 0x00440ec0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dabac`](#insn-006dabac) 範囲 `[['006dabac', '006dabaf']]`
  - `FALL_THROUGH` [`006dabac`](#insn-006dabac) → [`006dabb0`](#insn-006dabb0)
- ブロック [`006dabb0`](#insn-006dabb0) 範囲 `[['006dabb0', '006dabf7']]`
  - `FALL_THROUGH` [`006dabf4`](#insn-006dabf4) → [`006dabf8`](#insn-006dabf8)
- ブロック [`006dabf8`](#insn-006dabf8) 範囲 `[['006dabf8', '006dac23']]`
  - `UNCONDITIONAL_JUMP` [`006dac20`](#insn-006dac20) → [`006dac38`](#insn-006dac38)
- ブロック [`006dac24`](#insn-006dac24) 範囲 `[['006dac24', '006dac2f']]`
  - `FALL_THROUGH` [`006dac2c`](#insn-006dac2c) → [`006dac30`](#insn-006dac30)
- ブロック [`006dac30`](#insn-006dac30) 範囲 `[['006dac30', '006dac37']]`
  - `FALL_THROUGH` [`006dac34`](#insn-006dac34) → [`006dac38`](#insn-006dac38)
- ブロック [`006dac38`](#insn-006dac38) 範囲 `[['006dac38', '006dac3f']]`
  - `FALL_THROUGH` [`006dac3c`](#insn-006dac3c) → [`006dac40`](#insn-006dac40)
- ブロック [`006dac40`](#insn-006dac40) 範囲 `[['006dac40', '006dac4f']]`
  - `CONDITIONAL_JUMP` [`006dac4c`](#insn-006dac4c) → [`006dad18`](#insn-006dad18)
  - `FALL_THROUGH` [`006dac4c`](#insn-006dac4c) → [`006dac50`](#insn-006dac50)
- ブロック [`006dac50`](#insn-006dac50) 範囲 `[['006dac50', '006dac7f']]`
  - `CONDITIONAL_JUMP` [`006dac7c`](#insn-006dac7c) → [`006dac24`](#insn-006dac24)
  - `FALL_THROUGH` [`006dac7c`](#insn-006dac7c) → [`006dac80`](#insn-006dac80)
- ブロック [`006dac80`](#insn-006dac80) 範囲 `[['006dac80', '006dac8f']]`
  - `FALL_THROUGH` [`006dac8c`](#insn-006dac8c) → [`006dac90`](#insn-006dac90)
- ブロック [`006dac90`](#insn-006dac90) 範囲 `[['006dac90', '006dac9b']]`
  - `CONDITIONAL_JUMP` [`006dac98`](#insn-006dac98) → [`006dad38`](#insn-006dad38)
  - `FALL_THROUGH` [`006dac98`](#insn-006dac98) → [`006dac9c`](#insn-006dac9c)
- ブロック [`006dac9c`](#insn-006dac9c) 範囲 `[['006dac9c', '006daca7']]`
  - `FALL_THROUGH` [`006daca4`](#insn-006daca4) → [`006daca8`](#insn-006daca8)
- ブロック [`006daca8`](#insn-006daca8) 範囲 `[['006daca8', '006dacb7']]`
  - `FALL_THROUGH` [`006dacb4`](#insn-006dacb4) → [`006dacb8`](#insn-006dacb8)
- ブロック [`006dacb8`](#insn-006dacb8) 範囲 `[['006dacb8', '006dacbf']]`
  - `CONDITIONAL_JUMP` [`006dacbc`](#insn-006dacbc) → [`006dacd8`](#insn-006dacd8)
  - `FALL_THROUGH` [`006dacbc`](#insn-006dacbc) → [`006dacc0`](#insn-006dacc0)
- ブロック [`006dacc0`](#insn-006dacc0) 範囲 `[['006dacc0', '006dacc7']]`
  - `CONDITIONAL_JUMP` [`006dacc4`](#insn-006dacc4) → [`006dad40`](#insn-006dad40)
  - `FALL_THROUGH` [`006dacc4`](#insn-006dacc4) → [`006dacc8`](#insn-006dacc8)
- ブロック [`006dacc8`](#insn-006dacc8) 範囲 `[['006dacc8', '006dacd7']]`
  - `UNCONDITIONAL_JUMP` [`006dacd4`](#insn-006dacd4) → [`006dacdc`](#insn-006dacdc)
- ブロック [`006dacd8`](#insn-006dacd8) 範囲 `[['006dacd8', '006dacdb']]`
  - `FALL_THROUGH` [`006dacd8`](#insn-006dacd8) → [`006dacdc`](#insn-006dacdc)
- ブロック [`006dacdc`](#insn-006dacdc) 範囲 `[['006dacdc', '006dacf3']]`
  - `FALL_THROUGH` [`006dacf0`](#insn-006dacf0) → [`006dacf4`](#insn-006dacf4)
- ブロック [`006dacf4`](#insn-006dacf4) 範囲 `[['006dacf4', '006dad0b']]`
  - `CONDITIONAL_JUMP` [`006dad08`](#insn-006dad08) → [`006dac30`](#insn-006dac30)
  - `FALL_THROUGH` [`006dad08`](#insn-006dad08) → [`006dad0c`](#insn-006dad0c)
- ブロック [`006dad0c`](#insn-006dad0c) 範囲 `[['006dad0c', '006dad17']]`
  - `UNCONDITIONAL_JUMP` [`006dad14`](#insn-006dad14) → [`006dac30`](#insn-006dac30)
- ブロック [`006dad18`](#insn-006dad18) 範囲 `[['006dad18', '006dad27']]`
  - `FALL_THROUGH` [`006dad24`](#insn-006dad24) → [`006dad28`](#insn-006dad28)
- ブロック [`006dad28`](#insn-006dad28) 範囲 `[['006dad28', '006dad37']]`
- ブロック [`006dad38`](#insn-006dad38) 範囲 `[['006dad38', '006dad3f']]`
  - `FALL_THROUGH` [`006dad3c`](#insn-006dad3c) → [`006dad40`](#insn-006dad40)
- ブロック [`006dad40`](#insn-006dad40) 範囲 `[['006dad40', '006dad43']]`

## 命令位置別の参照

- [`006dabb0`](#insn-006dabb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabb4`](#insn-006dabb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabb8`](#insn-006dabb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabbc`](#insn-006dabbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabc0`](#insn-006dabc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabc4`](#insn-006dabc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabdc`](#insn-006dabdc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dabe8`](#insn-006dabe8) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`006dabf4`](#insn-006dabf4) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`006dac04`](#insn-006dac04) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`006dac18`](#insn-006dac18) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`006dac20`](#insn-006dac20) → [`006dac38`](#insn-006dac38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dac4c`](#insn-006dac4c) → [`006dad18`](#insn-006dad18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dac58`](#insn-006dac58) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`006dac6c`](#insn-006dac6c) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`006dac7c`](#insn-006dac7c) → [`006dac24`](#insn-006dac24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dac80`](#insn-006dac80) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dac98`](#insn-006dac98) → [`006dad38`](#insn-006dad38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dacbc`](#insn-006dacbc) → [`006dacd8`](#insn-006dacd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dacc4`](#insn-006dacc4) → [`006dad40`](#insn-006dad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006daccc`](#insn-006daccc) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`006dacd4`](#insn-006dacd4) → [`006dacdc`](#insn-006dacdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dacfc`](#insn-006dacfc) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`006dad08`](#insn-006dad08) → [`006dac30`](#insn-006dac30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad10`](#insn-006dad10) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`006dad14`](#insn-006dad14) → [`006dac30`](#insn-006dac30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad18`](#insn-006dad18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad1c`](#insn-006dad1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad20`](#insn-006dad20) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad24`](#insn-006dad24) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad28`](#insn-006dad28) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad2c`](#insn-006dad2c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad38`](#insn-006dad38) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dad3c`](#insn-006dad3c) → [`006f9ed8`](../006f9/006f9ed8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f9ed8` · 推定シンボル `None` · 推定型 `None`
- [`006dad40`](#insn-006dad40) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dabb0`](#insn-006dabb0)

~~~json
{
  "source": "006dabb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabb4`](#insn-006dabb4)

~~~json
{
  "source": "006dabb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabb8`](#insn-006dabb8)

~~~json
{
  "source": "006dabb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabbc`](#insn-006dabbc)

~~~json
{
  "source": "006dabbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabc0`](#insn-006dabc0)

~~~json
{
  "source": "006dabc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabc4`](#insn-006dabc4)

~~~json
{
  "source": "006dabc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabdc`](#insn-006dabdc)

~~~json
{
  "source": "006dabdc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dabe8`](#insn-006dabe8)

~~~json
{
  "source": "006dabe8",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dabf4`](#insn-006dabf4)

~~~json
{
  "source": "006dabf4",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dac04`](#insn-006dac04)

~~~json
{
  "source": "006dac04",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dac18`](#insn-006dac18)

~~~json
{
  "source": "006dac18",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dac20`](#insn-006dac20)

~~~json
{
  "source": "006dac20",
  "target": "006dac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dac4c`](#insn-006dac4c)

~~~json
{
  "source": "006dac4c",
  "target": "006dad18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dac58`](#insn-006dac58)

~~~json
{
  "source": "006dac58",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dac6c`](#insn-006dac6c)

~~~json
{
  "source": "006dac6c",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dac7c`](#insn-006dac7c)

~~~json
{
  "source": "006dac7c",
  "target": "006dac24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dac80`](#insn-006dac80)

~~~json
{
  "source": "006dac80",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dac98`](#insn-006dac98)

~~~json
{
  "source": "006dac98",
  "target": "006dad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dacbc`](#insn-006dacbc)

~~~json
{
  "source": "006dacbc",
  "target": "006dacd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dacc4`](#insn-006dacc4)

~~~json
{
  "source": "006dacc4",
  "target": "006dad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006daccc`](#insn-006daccc)

~~~json
{
  "source": "006daccc",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dacd4`](#insn-006dacd4)

~~~json
{
  "source": "006dacd4",
  "target": "006dacdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dacfc`](#insn-006dacfc)

~~~json
{
  "source": "006dacfc",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dad08`](#insn-006dad08)

~~~json
{
  "source": "006dad08",
  "target": "006dac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad10`](#insn-006dad10)

~~~json
{
  "source": "006dad10",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dad14`](#insn-006dad14)

~~~json
{
  "source": "006dad14",
  "target": "006dac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad18`](#insn-006dad18)

~~~json
{
  "source": "006dad18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad1c`](#insn-006dad1c)

~~~json
{
  "source": "006dad1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad20`](#insn-006dad20)

~~~json
{
  "source": "006dad20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad24`](#insn-006dad24)

~~~json
{
  "source": "006dad24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad28`](#insn-006dad28)

~~~json
{
  "source": "006dad28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad2c`](#insn-006dad2c)

~~~json
{
  "source": "006dad2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad38`](#insn-006dad38)

~~~json
{
  "source": "006dad38",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dad3c`](#insn-006dad3c)

~~~json
{
  "source": "006dad3c",
  "target": "006f9ed8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dad40`](#insn-006dad40)

~~~json
{
  "source": "006dad40",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
