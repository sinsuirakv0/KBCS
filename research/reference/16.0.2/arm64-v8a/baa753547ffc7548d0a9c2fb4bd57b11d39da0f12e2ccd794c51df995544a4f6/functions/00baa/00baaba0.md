# 00baaba0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baab04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baab04.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-de7b55ee86c71760dc16c0ac647a6923)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00babb94`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babb94.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-5d9b13b41809fc91b3f54734ef6247af)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaba0",
  "name": "FUN_00baaba0",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b72ac015a6a1e5728ac5ad8444421111ad0a83164e380374e0c1729eaf9c258c",
  "source_text_sha256": "b72ac015a6a1e5728ac5ad8444421111ad0a83164e380374e0c1729eaf9c258c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaba0",
        "00baadf7"
      ]
    ],
    "bytes_sha256": "e22bf6b8fa66f67b67d193a314a1e23850b9d4efeff7991a3e34bc195e0d9c9b",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b7b314](../00b7b/00b7b314.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c5b210](../00c5b/00c5b210.md)
- [00c5c600](../00c5c/00c5c600.md)
- [00c5d110](../00c5d/00c5d110.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5171 bytes

~~~c

void FUN_00baaba0(char *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong __n;
  void *__src;
  void *__dest;
  undefined8 *puVar7;
  ulong uVar8;
  undefined8 local_130;
  ulong uStack_128;
  void *local_120;
  undefined2 local_118;
  undefined8 local_110;
  undefined8 local_100;
  undefined8 uStack_f8;
  undefined8 uStack_f0;
  undefined8 uStack_e8;
  ulong local_e0;
  ulong uStack_d8;
  void *local_d0;
  undefined2 local_c8;
  undefined8 local_c0;
  undefined8 local_b0;
  undefined2 uStack_a8;
  undefined6 uStack_a6;
  undefined2 uStack_a0;
  undefined6 uStack_9e;
  undefined2 uStack_98;
  undefined6 uStack_96;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  undefined2 local_78;
  long local_68;
  
                    /* try { // try from 00baabbc to 00caabbf has its CatchHandler @ 00babe34 */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  puVar7 = (undefined8 *)*param_2;
  lVar1 = param_2[1];
  uStack_88 = 0;
  local_80 = (void *)0x0;
                    /* try { // try from 00baabf8 to 00caac0b has its CatchHandler @ 00babb50 */
  local_90 = 0x3002;
  local_78 = 0xffff;
  local_b0 = *puVar7;
  uStack_9e = (undefined6)*(undefined8 *)((long)puVar7 + 0x12);
  uStack_98 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 0x12) >> 0x30);
  uStack_a0 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 10) >> 0x30);
  uStack_a8 = (undefined2)puVar7[1];
  uStack_a6 = (undefined6)((ulong)puVar7[1] >> 0x10);
  _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb
            (param_1,lVar1,&local_b0,*(undefined8 *)param_2[2],*(undefined8 *)param_2[3],0,
             *(undefined8 *)param_2[4],1);
  __src = local_80;
  __n = uStack_88;
  uVar6 = local_b0;
  param_1[1] = '\x01';
  if (*param_1 != '\0') goto joined_r0x00baade8;
  uVar3 = CONCAT62(uStack_a6,uStack_a8);
  uVar5 = CONCAT62(uStack_96,uStack_98);
  uVar4 = CONCAT62(uStack_9e,uStack_a0);
                    /* try { // try from 00baac94 to 00caac97 has its CatchHandler @ 00babdc0 */
  local_130 = 0;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  if ((local_90 & 1) == 0) {
                    /* try { // try from 00baacb4 to 00caacbf has its CatchHandler @ 00babd64 */
    local_120 = local_80;
    uStack_128 = uStack_88;
    local_130 = local_90;
  }
  else {
    if (0xffffffffffffffef < uStack_88) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
                    /* try { // try from 00baacd4 to 00caacdf has its CatchHandler @ 00babd60 */
    if (uStack_88 < 0x17) {
      __dest = (void *)((long)&local_130 + 1);
      local_130 = (ulong)(byte)((int)uStack_88 << 1);
      if (uStack_88 != 0) goto LAB_00baad10;
    }
    else {
      uVar8 = uStack_88 + 0x10 & 0xfffffffffffffff0;
      __dest = (void *)_Znwm(uVar8);
                    /* try { // try from 00baad00 to 00caad0b has its CatchHandler @ 00babd1c */
      local_130 = uVar8 | 1;
      uStack_128 = __n;
      local_120 = __dest;
LAB_00baad10:
      memcpy(__dest,__src,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
  }
                    /* try { // try from 00baad24 to 00caad2f has its CatchHandler @ 00babce0 */
  local_d0 = local_120;
  uStack_d8 = uStack_128;
  local_e0 = local_130;
  local_110 = 0;
  local_c0 = 0;
  local_118 = local_78;
  local_100 = uVar6;
  local_c8 = local_78;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  local_130 = 0;
                    /* try { // try from 00baad50 to 00caad5b has its CatchHandler @ 00babcd0 */
  puVar7 = *(undefined8 **)(lVar1 + 0x5b8);
  uStack_f8 = uVar3;
  uStack_f0 = uVar4;
  uStack_e8 = uVar5;
  if (puVar7 < *(undefined8 **)(lVar1 + 0x5c0)) {
                    /* try { // try from 00baad70 to 00caad7b has its CatchHandler @ 00babc90 */
    puVar7[1] = uVar3;
    *puVar7 = uVar6;
    puVar7[3] = uVar5;
    puVar7[2] = uVar4;
    puVar7[6] = local_d0;
    puVar7[5] = uStack_d8;
    puVar7[4] = local_e0;
    uStack_d8 = 0;
    local_d0 = (void *)0x0;
    local_e0 = 0;
    *(undefined2 *)(puVar7 + 7) = local_78;
                    /* try { // try from 00baad9c to 00caada7 has its CatchHandler @ 00babc80 */
    puVar7[8] = 0;
    *(undefined8 **)(lVar1 + 0x5b8) = puVar7 + 9;
  }
  else {
    _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
              (lVar1 + 0x5b0,&local_100);
                    /* try { // try from 00baadc0 to 00caadcb has its CatchHandler @ 00babc60 */
    if ((local_e0 & 1) != 0) {
      _ZdlPv(local_d0);
    }
    if ((local_130 & 1) != 0) {
      _ZdlPv(local_120);
    }
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
joined_r0x00baade8:
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
                    /* try { // try from 00baac5c to 00caac67 has its CatchHandler @ 00babe30 */
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00baac80 to 00caac8b has its CatchHandler @ 00babde0 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaba0"></a> `00baaba0` | `ff 43 05 d1` | sub sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00baaba4"></a> `00baaba4` | `fc 7b 00 f9` | str x28,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00baaba8"></a> `00baaba8` | `fa 67 10 a9` | stp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00baabac"></a> `00baabac` | `f8 5f 11 a9` | stp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00baabb0"></a> `00baabb0` | `f6 57 12 a9` | stp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00baabb4"></a> `00baabb4` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00baabb8"></a> `00baabb8` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00baabbc"></a> `00baabbc` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00baabc0"></a> `00baabc0` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baabc4"></a> `00baabc4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00baabc8"></a> `00baabc8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00baabcc"></a> `00baabcc` | `49 00 86 52` | mov w9,#0x3002 | `FALL_THROUGH`
<a id="insn-00baabd0"></a> `00baabd0` | `ea ff 9f 52` | mov w10,#0xffff | `FALL_THROUGH`
<a id="insn-00baabd4"></a> `00baabd4` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baabd8"></a> `00baabd8` | `a8 83 1a f8` | stur x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00baabdc"></a> `00baabdc` | `08 50 40 a9` | ldp x8,x20,[x0] | `FALL_THROUGH`
<a id="insn-00baabe0"></a> `00baabe0` | `ff ff 0a a9` | stp xzr,xzr,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00baabe4"></a> `00baabe4` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baabe8"></a> `00baabe8` | `ff 73 01 79` | strh wzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00baabec"></a> `00baabec` | `ff 7f 0c a9` | stp xzr,xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baabf0"></a> `00baabf0` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baabf4"></a> `00baabf4` | `e9 83 01 79` | strh w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baabf8"></a> `00baabf8` | `ff 0b 03 39` | strb wzr,[sp, #0xc2] | `FALL_THROUGH`
<a id="insn-00baabfc"></a> `00baabfc` | `ea b3 01 79` | strh w10,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00baac00"></a> `00baac00` | `00 a1 c0 3c` | ldur q0,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00baac04"></a> `00baac04` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-00baac08"></a> `00baac08` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00baac0c"></a> `00baac0c` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00baac10"></a> `00baac10` | `e0 a3 8a 3c` | stur q0,[sp, #0xaa] | `FALL_THROUGH`
<a id="insn-00baac14"></a> `00baac14` | `e1 2b 80 3d` | str q1,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baac18"></a> `00baac18` | `08 24 41 a9` | ldp x8,x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baac1c"></a> `00baac1c` | `0a 10 40 f9` | ldr x10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baac20"></a> `00baac20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baac24"></a> `00baac24` | `f5 83 02 91` | add x21,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baac28"></a> `00baac28` | `02 01 40 f9` | ldr x2,[x8] | `FALL_THROUGH`
<a id="insn-00baac2c"></a> `00baac2c` | `23 01 40 f9` | ldr x3,[x9] | `FALL_THROUGH`
<a id="insn-00baac30"></a> `00baac30` | `45 01 40 f9` | ldr x5,[x10] | `FALL_THROUGH`
<a id="insn-00baac34"></a> `00baac34` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00baac38"></a> `00baac38` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00baac3c"></a> `00baac3c` | `71 c6 02 94` | bl 0x00c5c600 | `UNCONDITIONAL_CALL`
<a id="insn-00baac40"></a> `00baac40` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00baac44"></a> `00baac44` | `76 06 00 39` | strb w22,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00baac48"></a> `00baac48` | `28 02 00 34` | cbz w8,0x00baac8c | `CONDITIONAL_JUMP`
<a id="insn-00baac4c"></a> `00baac4c` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baac50"></a> `00baac50` | `68 00 00 36` | tbz w8,#0x0,0x00baac5c | `CONDITIONAL_JUMP`
<a id="insn-00baac54"></a> `00baac54` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baac58"></a> `00baac58` | `ca b4 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00baac5c"></a> `00baac5c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00baac60"></a> `00baac60` | `a9 83 5a f8` | ldur x9,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00baac64"></a> `00baac64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baac68"></a> `00baac68` | `41 0c 00 54` | b.ne 0x00baadf0 | `CONDITIONAL_JUMP`
<a id="insn-00baac6c"></a> `00baac6c` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00baac70"></a> `00baac70` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00baac74"></a> `00baac74` | `f6 57 52 a9` | ldp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00baac78"></a> `00baac78` | `f8 5f 51 a9` | ldp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00baac7c"></a> `00baac7c` | `fa 67 50 a9` | ldp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00baac80"></a> `00baac80` | `fc 7b 40 f9` | ldr x28,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00baac84"></a> `00baac84` | `ff 43 05 91` | add sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00baac88"></a> `00baac88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baac8c"></a> `00baac8c` | `e1 03 45 ad` | ldp q1,q0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baac90"></a> `00baac90` | `e9 03 43 39` | ldrb w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baac94"></a> `00baac94` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00baac98"></a> `00baac98` | `1a 81 00 91` | add x26,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00baac9c"></a> `00baac9c` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaca0"></a> `00baaca0` | `e1 03 00 ad` | stp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00baaca4"></a> `00baaca4` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaca8"></a> `00baaca8` | `e9 00 00 37` | tbnz w9,#0x0,0x00baacc4 | `CONDITIONAL_JUMP`
<a id="insn-00baacac"></a> `00baacac` | `a8 82 00 91` | add x8,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00baacb0"></a> `00baacb0` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00baacb4"></a> `00baacb4` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00baacb8"></a> `00baacb8` | `49 0b 00 f9` | str x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00baacbc"></a> `00baacbc` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00baacc0"></a> `00baacc0` | `19 00 00 14` | b 0x00baad24 | `UNCONDITIONAL_JUMP`
<a id="insn-00baacc4"></a> `00baacc4` | `f5 67 40 f9` | ldr x21,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00baacc8"></a> `00baacc8` | `bf 42 00 b1` | cmn x21,#0x10 | `FALL_THROUGH`
<a id="insn-00baaccc"></a> `00baaccc` | `42 09 00 54` | b.cs 0x00baadf4 | `CONDITIONAL_JUMP`
<a id="insn-00baacd0"></a> `00baacd0` | `f6 6b 40 f9` | ldr x22,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baacd4"></a> `00baacd4` | `bf 5e 00 f1` | cmp x21,#0x17 | `FALL_THROUGH`
<a id="insn-00baacd8"></a> `00baacd8` | `c2 00 00 54` | b.cs 0x00baacf0 | `CONDITIONAL_JUMP`
<a id="insn-00baacdc"></a> `00baacdc` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00baace0"></a> `00baace0` | `57 07 00 91` | add x23,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00baace4"></a> `00baace4` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baace8"></a> `00baace8` | `55 01 00 b5` | cbnz x21,0x00baad10 | `CONDITIONAL_JUMP`
<a id="insn-00baacec"></a> `00baacec` | `0d 00 00 14` | b 0x00baad20 | `UNCONDITIONAL_JUMP`
<a id="insn-00baacf0"></a> `00baacf0` | `a8 42 00 91` | add x8,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00baacf4"></a> `00baacf4` | `18 ed 7c 92` | and x24,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00baacf8"></a> `00baacf8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00baacfc"></a> `00baacfc` | `99 b4 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00baad00"></a> `00baad00` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00baad04"></a> `00baad04` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00baad08"></a> `00baad08` | `e8 57 02 a9` | stp x8,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baad0c"></a> `00baad0c` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baad10"></a> `00baad10` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00baad14"></a> `00baad14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00baad18"></a> `00baad18` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baad1c"></a> `00baad1c` | `ed b4 02 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad20"></a> `00baad20` | `ff 6a 35 38` | strb wzr,[x23, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00baad24"></a> `00baad24` | `e8 b3 41 79` | ldrh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00baad28"></a> `00baad28` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00baad2c"></a> `00baad2c` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baad30"></a> `00baad30` | `ff 4b 00 f9` | str xzr,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00baad34"></a> `00baad34` | `e8 73 00 79` | strh w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00baad38"></a> `00baad38` | `e1 83 02 ad` | stp q1,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baad3c"></a> `00baad3c` | `e8 13 01 79` | strh w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00baad40"></a> `00baad40` | `40 03 c0 3d` | ldr q0,[x26] | `FALL_THROUGH`
<a id="insn-00baad44"></a> `00baad44` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00baad48"></a> `00baad48` | `5f ff 00 a9` | stp xzr,xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00baad4c"></a> `00baad4c` | `5f 03 00 f9` | str xzr,[x26] | `FALL_THROUGH`
<a id="insn-00baad50"></a> `00baad50` | `e0 1f 80 3d` | str q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baad54"></a> `00baad54` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00baad58"></a> `00baad58` | `88 de 42 f9` | ldr x8,[x20, #0x5b8] | `FALL_THROUGH`
<a id="insn-00baad5c"></a> `00baad5c` | `89 e2 42 f9` | ldr x9,[x20, #0x5c0] | `FALL_THROUGH`
<a id="insn-00baad60"></a> `00baad60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baad64"></a> `00baad64` | `82 02 00 54` | b.cs 0x00baadb4 | `CONDITIONAL_JUMP`
<a id="insn-00baad68"></a> `00baad68` | `e0 87 42 ad` | ldp q0,q1,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baad6c"></a> `00baad6c` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baad70"></a> `00baad70` | `29 81 00 91` | add x9,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00baad74"></a> `00baad74` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00baad78"></a> `00baad78` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00baad7c"></a> `00baad7c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00baad80"></a> `00baad80` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00baad84"></a> `00baad84` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00baad88"></a> `00baad88` | `3f fd 00 a9` | stp xzr,xzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baad8c"></a> `00baad8c` | `3f 01 00 f9` | str xzr,[x9] | `FALL_THROUGH`
<a id="insn-00baad90"></a> `00baad90` | `e9 13 41 79` | ldrh w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00baad94"></a> `00baad94` | `0a 21 01 91` | add x10,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00baad98"></a> `00baad98` | `09 71 00 79` | strh w9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00baad9c"></a> `00baad9c` | `e9 4b 40 f9` | ldr x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00baada0"></a> `00baada0` | `09 21 00 f9` | str x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00baada4"></a> `00baada4` | `8a de 02 f9` | str x10,[x20, #0x5b8] | `FALL_THROUGH`
<a id="insn-00baada8"></a> `00baada8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baadac"></a> `00baadac` | `68 01 00 37` | tbnz w8,#0x0,0x00baadd8 | `CONDITIONAL_JUMP`
<a id="insn-00baadb0"></a> `00baadb0` | `0c 00 00 14` | b 0x00baade0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baadb4"></a> `00baadb4` | `80 c2 16 91` | add x0,x20,#0x5b0 | `FALL_THROUGH`
<a id="insn-00baadb8"></a> `00baadb8` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baadbc"></a> `00baadbc` | `d5 c8 02 94` | bl 0x00c5d110 | `UNCONDITIONAL_CALL`
<a id="insn-00baadc0"></a> `00baadc0` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baadc4"></a> `00baadc4` | `68 00 00 36` | tbz w8,#0x0,0x00baadd0 | `CONDITIONAL_JUMP`
<a id="insn-00baadc8"></a> `00baadc8` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00baadcc"></a> `00baadcc` | `6d b4 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00baadd0"></a> `00baadd0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baadd4"></a> `00baadd4` | `68 00 00 36` | tbz w8,#0x0,0x00baade0 | `CONDITIONAL_JUMP`
<a id="insn-00baadd8"></a> `00baadd8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaddc"></a> `00baaddc` | `69 b4 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00baade0"></a> `00baade0` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00baade4"></a> `00baade4` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baade8"></a> `00baade8` | `68 f3 07 37` | tbnz w8,#0x0,0x00baac54 | `CONDITIONAL_JUMP`
<a id="insn-00baadec"></a> `00baadec` | `9c ff ff 17` | b 0x00baac5c | `UNCONDITIONAL_JUMP`
<a id="insn-00baadf0"></a> `00baadf0` | `70 b4 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`
<a id="insn-00baadf4"></a> `00baadf4` | `07 c1 02 94` | bl 0x00c5b210 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaba0`](#insn-00baaba0) 範囲 `[['00baaba0', '00baabbb']]`
  - `FALL_THROUGH` [`00baabb8`](#insn-00baabb8) → [`00baabbc`](#insn-00baabbc)
- ブロック [`00baabbc`](#insn-00baabbc) 範囲 `[['00baabbc', '00baabf7']]`
  - `FALL_THROUGH` [`00baabf4`](#insn-00baabf4) → [`00baabf8`](#insn-00baabf8)
- ブロック [`00baabf8`](#insn-00baabf8) 範囲 `[['00baabf8', '00baac4b']]`
  - `CONDITIONAL_JUMP` [`00baac48`](#insn-00baac48) → [`00baac8c`](#insn-00baac8c)
  - `FALL_THROUGH` [`00baac48`](#insn-00baac48) → [`00baac4c`](#insn-00baac4c)
- ブロック [`00baac4c`](#insn-00baac4c) 範囲 `[['00baac4c', '00baac53']]`
  - `CONDITIONAL_JUMP` [`00baac50`](#insn-00baac50) → [`00baac5c`](#insn-00baac5c)
  - `FALL_THROUGH` [`00baac50`](#insn-00baac50) → [`00baac54`](#insn-00baac54)
- ブロック [`00baac54`](#insn-00baac54) 範囲 `[['00baac54', '00baac5b']]`
  - `FALL_THROUGH` [`00baac58`](#insn-00baac58) → [`00baac5c`](#insn-00baac5c)
- ブロック [`00baac5c`](#insn-00baac5c) 範囲 `[['00baac5c', '00baac6b']]`
  - `CONDITIONAL_JUMP` [`00baac68`](#insn-00baac68) → [`00baadf0`](#insn-00baadf0)
  - `FALL_THROUGH` [`00baac68`](#insn-00baac68) → [`00baac6c`](#insn-00baac6c)
- ブロック [`00baac6c`](#insn-00baac6c) 範囲 `[['00baac6c', '00baac7f']]`
  - `FALL_THROUGH` [`00baac7c`](#insn-00baac7c) → [`00baac80`](#insn-00baac80)
- ブロック [`00baac80`](#insn-00baac80) 範囲 `[['00baac80', '00baac8b']]`
- ブロック [`00baac8c`](#insn-00baac8c) 範囲 `[['00baac8c', '00baac93']]`
  - `FALL_THROUGH` [`00baac90`](#insn-00baac90) → [`00baac94`](#insn-00baac94)
- ブロック [`00baac94`](#insn-00baac94) 範囲 `[['00baac94', '00baacab']]`
  - `CONDITIONAL_JUMP` [`00baaca8`](#insn-00baaca8) → [`00baacc4`](#insn-00baacc4)
  - `FALL_THROUGH` [`00baaca8`](#insn-00baaca8) → [`00baacac`](#insn-00baacac)
- ブロック [`00baacac`](#insn-00baacac) 範囲 `[['00baacac', '00baacb3']]`
  - `FALL_THROUGH` [`00baacb0`](#insn-00baacb0) → [`00baacb4`](#insn-00baacb4)
- ブロック [`00baacb4`](#insn-00baacb4) 範囲 `[['00baacb4', '00baacc3']]`
  - `UNCONDITIONAL_JUMP` [`00baacc0`](#insn-00baacc0) → [`00baad24`](#insn-00baad24)
- ブロック [`00baacc4`](#insn-00baacc4) 範囲 `[['00baacc4', '00baaccf']]`
  - `CONDITIONAL_JUMP` [`00baaccc`](#insn-00baaccc) → [`00baadf4`](#insn-00baadf4)
  - `FALL_THROUGH` [`00baaccc`](#insn-00baaccc) → [`00baacd0`](#insn-00baacd0)
- ブロック [`00baacd0`](#insn-00baacd0) 範囲 `[['00baacd0', '00baacd3']]`
  - `FALL_THROUGH` [`00baacd0`](#insn-00baacd0) → [`00baacd4`](#insn-00baacd4)
- ブロック [`00baacd4`](#insn-00baacd4) 範囲 `[['00baacd4', '00baacdb']]`
  - `CONDITIONAL_JUMP` [`00baacd8`](#insn-00baacd8) → [`00baacf0`](#insn-00baacf0)
  - `FALL_THROUGH` [`00baacd8`](#insn-00baacd8) → [`00baacdc`](#insn-00baacdc)
- ブロック [`00baacdc`](#insn-00baacdc) 範囲 `[['00baacdc', '00baaceb']]`
  - `CONDITIONAL_JUMP` [`00baace8`](#insn-00baace8) → [`00baad10`](#insn-00baad10)
  - `FALL_THROUGH` [`00baace8`](#insn-00baace8) → [`00baacec`](#insn-00baacec)
- ブロック [`00baacec`](#insn-00baacec) 範囲 `[['00baacec', '00baacef']]`
  - `UNCONDITIONAL_JUMP` [`00baacec`](#insn-00baacec) → [`00baad20`](#insn-00baad20)
- ブロック [`00baacf0`](#insn-00baacf0) 範囲 `[['00baacf0', '00baacff']]`
  - `FALL_THROUGH` [`00baacfc`](#insn-00baacfc) → [`00baad00`](#insn-00baad00)
- ブロック [`00baad00`](#insn-00baad00) 範囲 `[['00baad00', '00baad0f']]`
  - `FALL_THROUGH` [`00baad0c`](#insn-00baad0c) → [`00baad10`](#insn-00baad10)
- ブロック [`00baad10`](#insn-00baad10) 範囲 `[['00baad10', '00baad1f']]`
  - `FALL_THROUGH` [`00baad1c`](#insn-00baad1c) → [`00baad20`](#insn-00baad20)
- ブロック [`00baad20`](#insn-00baad20) 範囲 `[['00baad20', '00baad23']]`
  - `FALL_THROUGH` [`00baad20`](#insn-00baad20) → [`00baad24`](#insn-00baad24)
- ブロック [`00baad24`](#insn-00baad24) 範囲 `[['00baad24', '00baad4f']]`
  - `FALL_THROUGH` [`00baad4c`](#insn-00baad4c) → [`00baad50`](#insn-00baad50)
- ブロック [`00baad50`](#insn-00baad50) 範囲 `[['00baad50', '00baad67']]`
  - `CONDITIONAL_JUMP` [`00baad64`](#insn-00baad64) → [`00baadb4`](#insn-00baadb4)
  - `FALL_THROUGH` [`00baad64`](#insn-00baad64) → [`00baad68`](#insn-00baad68)
- ブロック [`00baad68`](#insn-00baad68) 範囲 `[['00baad68', '00baad6f']]`
  - `FALL_THROUGH` [`00baad6c`](#insn-00baad6c) → [`00baad70`](#insn-00baad70)
- ブロック [`00baad70`](#insn-00baad70) 範囲 `[['00baad70', '00baad9b']]`
  - `FALL_THROUGH` [`00baad98`](#insn-00baad98) → [`00baad9c`](#insn-00baad9c)
- ブロック [`00baad9c`](#insn-00baad9c) 範囲 `[['00baad9c', '00baadaf']]`
  - `CONDITIONAL_JUMP` [`00baadac`](#insn-00baadac) → [`00baadd8`](#insn-00baadd8)
  - `FALL_THROUGH` [`00baadac`](#insn-00baadac) → [`00baadb0`](#insn-00baadb0)
- ブロック [`00baadb0`](#insn-00baadb0) 範囲 `[['00baadb0', '00baadb3']]`
  - `UNCONDITIONAL_JUMP` [`00baadb0`](#insn-00baadb0) → [`00baade0`](#insn-00baade0)
- ブロック [`00baadb4`](#insn-00baadb4) 範囲 `[['00baadb4', '00baadbf']]`
  - `FALL_THROUGH` [`00baadbc`](#insn-00baadbc) → [`00baadc0`](#insn-00baadc0)
- ブロック [`00baadc0`](#insn-00baadc0) 範囲 `[['00baadc0', '00baadc7']]`
  - `CONDITIONAL_JUMP` [`00baadc4`](#insn-00baadc4) → [`00baadd0`](#insn-00baadd0)
  - `FALL_THROUGH` [`00baadc4`](#insn-00baadc4) → [`00baadc8`](#insn-00baadc8)
- ブロック [`00baadc8`](#insn-00baadc8) 範囲 `[['00baadc8', '00baadcf']]`
  - `FALL_THROUGH` [`00baadcc`](#insn-00baadcc) → [`00baadd0`](#insn-00baadd0)
- ブロック [`00baadd0`](#insn-00baadd0) 範囲 `[['00baadd0', '00baadd7']]`
  - `CONDITIONAL_JUMP` [`00baadd4`](#insn-00baadd4) → [`00baade0`](#insn-00baade0)
  - `FALL_THROUGH` [`00baadd4`](#insn-00baadd4) → [`00baadd8`](#insn-00baadd8)
- ブロック [`00baadd8`](#insn-00baadd8) 範囲 `[['00baadd8', '00baaddf']]`
  - `FALL_THROUGH` [`00baaddc`](#insn-00baaddc) → [`00baade0`](#insn-00baade0)
- ブロック [`00baade0`](#insn-00baade0) 範囲 `[['00baade0', '00baadeb']]`
  - `CONDITIONAL_JUMP` [`00baade8`](#insn-00baade8) → [`00baac54`](#insn-00baac54)
  - `FALL_THROUGH` [`00baade8`](#insn-00baade8) → [`00baadec`](#insn-00baadec)
- ブロック [`00baadec`](#insn-00baadec) 範囲 `[['00baadec', '00baadef']]`
  - `UNCONDITIONAL_JUMP` [`00baadec`](#insn-00baadec) → [`00baac5c`](#insn-00baac5c)
- ブロック [`00baadf0`](#insn-00baadf0) 範囲 `[['00baadf0', '00baadf3']]`
- ブロック [`00baadf4`](#insn-00baadf4) 範囲 `[['00baadf4', '00baadf7']]`

## 命令位置別の参照

- [`00baaba4`](#insn-00baaba4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaba8`](#insn-00baaba8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabac`](#insn-00baabac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabb0`](#insn-00baabb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabb4`](#insn-00baabb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabb8`](#insn-00baabb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabd8`](#insn-00baabd8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabe0`](#insn-00baabe0) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabe4`](#insn-00baabe4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabe8`](#insn-00baabe8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabec`](#insn-00baabec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf0`](#insn-00baabf0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf4`](#insn-00baabf4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf8`](#insn-00baabf8) → `Stack[-0x8e]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabfc`](#insn-00baabfc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac10`](#insn-00baac10) → `Stack[-0xa6]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac14`](#insn-00baac14) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac3c`](#insn-00baac3c) → [`00c5c600`](../00c5c/00c5c600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c600` · 推定シンボル `None` · 推定型 `None`
- [`00baac48`](#insn-00baac48) → [`00baac8c`](#insn-00baac8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac4c`](#insn-00baac4c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac50`](#insn-00baac50) → [`00baac5c`](#insn-00baac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac54`](#insn-00baac54) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac58`](#insn-00baac58) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00baac60`](#insn-00baac60) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac68`](#insn-00baac68) → [`00baadf0`](#insn-00baadf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac6c`](#insn-00baac6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac70`](#insn-00baac70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac74`](#insn-00baac74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac78`](#insn-00baac78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac7c`](#insn-00baac7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac80`](#insn-00baac80) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac8c`](#insn-00baac8c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac90`](#insn-00baac90) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac9c`](#insn-00baac9c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaca0`](#insn-00baaca0) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaca4`](#insn-00baaca4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaca8`](#insn-00baaca8) → [`00baacc4`](#insn-00baacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb0`](#insn-00baacb0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb4`](#insn-00baacb4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb8`](#insn-00baacb8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacbc`](#insn-00baacbc) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacc0`](#insn-00baacc0) → [`00baad24`](#insn-00baad24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacc4`](#insn-00baacc4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaccc`](#insn-00baaccc) → [`00baadf4`](#insn-00baadf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd0`](#insn-00baacd0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd8`](#insn-00baacd8) → [`00baacf0`](#insn-00baacf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baace4`](#insn-00baace4) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baace8`](#insn-00baace8) → [`00baad10`](#insn-00baad10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacec`](#insn-00baacec) → [`00baad20`](#insn-00baad20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacfc`](#insn-00baacfc) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00baad08`](#insn-00baad08) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad0c`](#insn-00baad0c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad1c`](#insn-00baad1c) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00baad24`](#insn-00baad24) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad28`](#insn-00baad28) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad2c`](#insn-00baad2c) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad30`](#insn-00baad30) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad34`](#insn-00baad34) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad38`](#insn-00baad38) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad3c`](#insn-00baad3c) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad40`](#insn-00baad40) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad44`](#insn-00baad44) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad48`](#insn-00baad48) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad4c`](#insn-00baad4c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad50`](#insn-00baad50) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad54`](#insn-00baad54) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad64`](#insn-00baad64) → [`00baadb4`](#insn-00baadb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad68`](#insn-00baad68) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad78`](#insn-00baad78) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad7c`](#insn-00baad7c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad88`](#insn-00baad88) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad8c`](#insn-00baad8c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad90`](#insn-00baad90) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad9c`](#insn-00baad9c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada8`](#insn-00baada8) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadac`](#insn-00baadac) → [`00baadd8`](#insn-00baadd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadb0`](#insn-00baadb0) → [`00baade0`](#insn-00baade0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadbc`](#insn-00baadbc) → [`00c5d110`](../00c5d/00c5d110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d110` · 推定シンボル `None` · 推定型 `None`
- [`00baadc0`](#insn-00baadc0) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadc4`](#insn-00baadc4) → [`00baadd0`](#insn-00baadd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadc8`](#insn-00baadc8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadcc`](#insn-00baadcc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00baadd0`](#insn-00baadd0) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd4`](#insn-00baadd4) → [`00baade0`](#insn-00baade0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd8`](#insn-00baadd8) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaddc`](#insn-00baaddc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00baade4`](#insn-00baade4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade8`](#insn-00baade8) → [`00baac54`](#insn-00baac54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadec`](#insn-00baadec) → [`00baac5c`](#insn-00baac5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadf0`](#insn-00baadf0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`00baadf4`](#insn-00baadf4) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaba4`](#insn-00baaba4)

~~~json
{
  "source": "00baaba4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaba8`](#insn-00baaba8)

~~~json
{
  "source": "00baaba8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabac`](#insn-00baabac)

~~~json
{
  "source": "00baabac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabb0`](#insn-00baabb0)

~~~json
{
  "source": "00baabb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabb4`](#insn-00baabb4)

~~~json
{
  "source": "00baabb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabb8`](#insn-00baabb8)

~~~json
{
  "source": "00baabb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabd8`](#insn-00baabd8)

~~~json
{
  "source": "00baabd8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabe0`](#insn-00baabe0)

~~~json
{
  "source": "00baabe0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabe4`](#insn-00baabe4)

~~~json
{
  "source": "00baabe4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabe8`](#insn-00baabe8)

~~~json
{
  "source": "00baabe8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabec`](#insn-00baabec)

~~~json
{
  "source": "00baabec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf0`](#insn-00baabf0)

~~~json
{
  "source": "00baabf0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf4`](#insn-00baabf4)

~~~json
{
  "source": "00baabf4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf8`](#insn-00baabf8)

~~~json
{
  "source": "00baabf8",
  "target": "Stack[-0x8e]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabfc`](#insn-00baabfc)

~~~json
{
  "source": "00baabfc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac10`](#insn-00baac10)

~~~json
{
  "source": "00baac10",
  "target": "Stack[-0xa6]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac14`](#insn-00baac14)

~~~json
{
  "source": "00baac14",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac3c`](#insn-00baac3c)

~~~json
{
  "source": "00baac3c",
  "target": "00c5c600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac48`](#insn-00baac48)

~~~json
{
  "source": "00baac48",
  "target": "00baac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac4c`](#insn-00baac4c)

~~~json
{
  "source": "00baac4c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac50`](#insn-00baac50)

~~~json
{
  "source": "00baac50",
  "target": "00baac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac54`](#insn-00baac54)

~~~json
{
  "source": "00baac54",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac58`](#insn-00baac58)

~~~json
{
  "source": "00baac58",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac60`](#insn-00baac60)

~~~json
{
  "source": "00baac60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac68`](#insn-00baac68)

~~~json
{
  "source": "00baac68",
  "target": "00baadf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac6c`](#insn-00baac6c)

~~~json
{
  "source": "00baac6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac70`](#insn-00baac70)

~~~json
{
  "source": "00baac70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac74`](#insn-00baac74)

~~~json
{
  "source": "00baac74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac78`](#insn-00baac78)

~~~json
{
  "source": "00baac78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac7c`](#insn-00baac7c)

~~~json
{
  "source": "00baac7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac80`](#insn-00baac80)

~~~json
{
  "source": "00baac80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac8c`](#insn-00baac8c)

~~~json
{
  "source": "00baac8c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac90`](#insn-00baac90)

~~~json
{
  "source": "00baac90",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac9c`](#insn-00baac9c)

~~~json
{
  "source": "00baac9c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaca0`](#insn-00baaca0)

~~~json
{
  "source": "00baaca0",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaca4`](#insn-00baaca4)

~~~json
{
  "source": "00baaca4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaca8`](#insn-00baaca8)

~~~json
{
  "source": "00baaca8",
  "target": "00baacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb0`](#insn-00baacb0)

~~~json
{
  "source": "00baacb0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb4`](#insn-00baacb4)

~~~json
{
  "source": "00baacb4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb8`](#insn-00baacb8)

~~~json
{
  "source": "00baacb8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacbc`](#insn-00baacbc)

~~~json
{
  "source": "00baacbc",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacc0`](#insn-00baacc0)

~~~json
{
  "source": "00baacc0",
  "target": "00baad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacc4`](#insn-00baacc4)

~~~json
{
  "source": "00baacc4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaccc`](#insn-00baaccc)

~~~json
{
  "source": "00baaccc",
  "target": "00baadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd0`](#insn-00baacd0)

~~~json
{
  "source": "00baacd0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd8`](#insn-00baacd8)

~~~json
{
  "source": "00baacd8",
  "target": "00baacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baace4`](#insn-00baace4)

~~~json
{
  "source": "00baace4",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baace8`](#insn-00baace8)

~~~json
{
  "source": "00baace8",
  "target": "00baad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacec`](#insn-00baacec)

~~~json
{
  "source": "00baacec",
  "target": "00baad20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacfc`](#insn-00baacfc)

~~~json
{
  "source": "00baacfc",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad08`](#insn-00baad08)

~~~json
{
  "source": "00baad08",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad0c`](#insn-00baad0c)

~~~json
{
  "source": "00baad0c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad1c`](#insn-00baad1c)

~~~json
{
  "source": "00baad1c",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad24`](#insn-00baad24)

~~~json
{
  "source": "00baad24",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad28`](#insn-00baad28)

~~~json
{
  "source": "00baad28",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad2c`](#insn-00baad2c)

~~~json
{
  "source": "00baad2c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad30`](#insn-00baad30)

~~~json
{
  "source": "00baad30",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad34`](#insn-00baad34)

~~~json
{
  "source": "00baad34",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad38`](#insn-00baad38)

~~~json
{
  "source": "00baad38",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad3c`](#insn-00baad3c)

~~~json
{
  "source": "00baad3c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad40`](#insn-00baad40)

~~~json
{
  "source": "00baad40",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad44`](#insn-00baad44)

~~~json
{
  "source": "00baad44",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad48`](#insn-00baad48)

~~~json
{
  "source": "00baad48",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad4c`](#insn-00baad4c)

~~~json
{
  "source": "00baad4c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad50`](#insn-00baad50)

~~~json
{
  "source": "00baad50",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad54`](#insn-00baad54)

~~~json
{
  "source": "00baad54",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad64`](#insn-00baad64)

~~~json
{
  "source": "00baad64",
  "target": "00baadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad68`](#insn-00baad68)

~~~json
{
  "source": "00baad68",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad78`](#insn-00baad78)

~~~json
{
  "source": "00baad78",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad7c`](#insn-00baad7c)

~~~json
{
  "source": "00baad7c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad88`](#insn-00baad88)

~~~json
{
  "source": "00baad88",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad8c`](#insn-00baad8c)

~~~json
{
  "source": "00baad8c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad90`](#insn-00baad90)

~~~json
{
  "source": "00baad90",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad9c`](#insn-00baad9c)

~~~json
{
  "source": "00baad9c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada8`](#insn-00baada8)

~~~json
{
  "source": "00baada8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadac`](#insn-00baadac)

~~~json
{
  "source": "00baadac",
  "target": "00baadd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadb0`](#insn-00baadb0)

~~~json
{
  "source": "00baadb0",
  "target": "00baade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadbc`](#insn-00baadbc)

~~~json
{
  "source": "00baadbc",
  "target": "00c5d110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baadc0`](#insn-00baadc0)

~~~json
{
  "source": "00baadc0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadc4`](#insn-00baadc4)

~~~json
{
  "source": "00baadc4",
  "target": "00baadd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadc8`](#insn-00baadc8)

~~~json
{
  "source": "00baadc8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadcc`](#insn-00baadcc)

~~~json
{
  "source": "00baadcc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baadd0`](#insn-00baadd0)

~~~json
{
  "source": "00baadd0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd4`](#insn-00baadd4)

~~~json
{
  "source": "00baadd4",
  "target": "00baade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd8`](#insn-00baadd8)

~~~json
{
  "source": "00baadd8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaddc`](#insn-00baaddc)

~~~json
{
  "source": "00baaddc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baade4`](#insn-00baade4)

~~~json
{
  "source": "00baade4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade8`](#insn-00baade8)

~~~json
{
  "source": "00baade8",
  "target": "00baac54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadec`](#insn-00baadec)

~~~json
{
  "source": "00baadec",
  "target": "00baac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadf0`](#insn-00baadf0)

~~~json
{
  "source": "00baadf0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baadf4`](#insn-00baadf4)

~~~json
{
  "source": "00baadf4",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
