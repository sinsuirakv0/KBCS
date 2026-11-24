# 00baa6dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-d2406087049a1d3f0219978413afae8f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baab04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baab04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-f3f1fd9dbfaf800578f0228113183445)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baa6dc",
  "name": "FUN_00baa6dc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16fb3248daae4abff53821a947195b3471d4d1d71ddf12629e3ca6795de835bb",
  "source_text_sha256": "16fb3248daae4abff53821a947195b3471d4d1d71ddf12629e3ca6795de835bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baa6dc",
        "00baa933"
      ]
    ],
    "bytes_sha256": "501eb85a25f62001d03beeda599f62bce4da7dd1cbeeb4c5acda8c8355c644c5",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b7ae50](../00b7a/00b7ae50.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5c130](../00c5c/00c5c130.md)
- [00c5cc40](../00c5c/00c5cc40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4977 bytes

~~~c

void FUN_00baa6dc(char *param_1,long *param_2)

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
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00baa710 to 00caa71b has its CatchHandler @ 00babe10 */
  puVar7 = (undefined8 *)*param_2;
  lVar1 = param_2[1];
  uStack_88 = 0;
  local_80 = (void *)0x0;
                    /* try { // try from 00baa734 to 00caa73f has its CatchHandler @ 00babe00 */
  local_90 = 0x3002;
  local_78 = 0xffff;
  local_b0 = *puVar7;
  uStack_9e = (undefined6)*(undefined8 *)((long)puVar7 + 0x12);
  uStack_98 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 0x12) >> 0x30);
                    /* try { // try from 00baa748 to 00caa74b has its CatchHandler @ 00babda0 */
  uStack_a0 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 10) >> 0x30);
  uStack_a8 = (undefined2)puVar7[1];
  uStack_a6 = (undefined6)((ulong)puVar7[1] >> 0x10);
                    /* try { // try from 00baa768 to 00caa773 has its CatchHandler @ 00babd60 */
  _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb
            (param_1,lVar1,&local_b0,*(undefined8 *)param_2[2],*(undefined8 *)param_2[3],0,
             *(undefined8 *)param_2[4],1);
  __src = local_80;
  __n = uStack_88;
  uVar6 = local_b0;
  param_1[1] = '\x01';
  if (*param_1 != '\0') goto joined_r0x00baa924;
  uVar3 = CONCAT62(uStack_a6,uStack_a8);
  uVar5 = CONCAT62(uStack_96,uStack_98);
  uVar4 = CONCAT62(uStack_9e,uStack_a0);
                    /* try { // try from 00baa7d8 to 00caa7e3 has its CatchHandler @ 00babd00 */
  local_130 = 0;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  if ((local_90 & 1) == 0) {
    local_120 = local_80;
    uStack_128 = uStack_88;
    local_130 = local_90;
  }
  else {
                    /* try { // try from 00baa804 to 00caa80f has its CatchHandler @ 00babcc0 */
    if (0xffffffffffffffef < uStack_88) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uStack_88 < 0x17) {
      __dest = (void *)((long)&local_130 + 1);
      local_130 = (ulong)(byte)((int)uStack_88 << 1);
      if (uStack_88 != 0) goto LAB_00baa84c;
    }
    else {
      uVar8 = uStack_88 + 0x10 & 0xfffffffffffffff0;
                    /* try { // try from 00baa834 to 00caa853 has its CatchHandler @ 00babe60 */
      __dest = (void *)_Znwm(uVar8);
      local_130 = uVar8 | 1;
      uStack_128 = __n;
      local_120 = __dest;
LAB_00baa84c:
                    /* try { // try from 00baa854 to 00caa88b has its CatchHandler @ 00babed0 */
      memcpy(__dest,__src,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
  }
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
  puVar7 = *(undefined8 **)(lVar1 + 0x5b8);
  uStack_f8 = uVar3;
  uStack_f0 = uVar4;
  uStack_e8 = uVar5;
  if (puVar7 < *(undefined8 **)(lVar1 + 0x5c0)) {
    puVar7[1] = uVar3;
    *puVar7 = uVar6;
    puVar7[3] = uVar5;
    puVar7[2] = uVar4;
    puVar7[6] = local_d0;
    puVar7[5] = uStack_d8;
    puVar7[4] = local_e0;
    uStack_d8 = 0;
    local_d0 = (void *)0x0;
                    /* try { // try from 00baa8c8 to 00caa8cb has its CatchHandler @ 00babbcc */
    local_e0 = 0;
    *(undefined2 *)(puVar7 + 7) = local_78;
    puVar7[8] = 0;
    *(undefined8 **)(lVar1 + 0x5b8) = puVar7 + 9;
  }
  else {
    _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
              (lVar1 + 0x5b0,&local_100);
    if ((local_e0 & 1) != 0) {
                    /* try { // try from 00baa908 to 00caa91b has its CatchHandler @ 00bab8e8 */
      _ZdlPv(local_d0);
    }
    if ((local_130 & 1) != 0) {
      _ZdlPv(local_120);
    }
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
joined_r0x00baa924:
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00baa7b4 to 00caa7bf has its CatchHandler @ 00babd10 */
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
<a id="insn-00baa6dc"></a> `00baa6dc` | `ff 43 05 d1` | sub sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00baa6e0"></a> `00baa6e0` | `fc 7b 00 f9` | str x28,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00baa6e4"></a> `00baa6e4` | `fa 67 10 a9` | stp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00baa6e8"></a> `00baa6e8` | `f8 5f 11 a9` | stp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00baa6ec"></a> `00baa6ec` | `f6 57 12 a9` | stp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00baa6f0"></a> `00baa6f0` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00baa6f4"></a> `00baa6f4` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00baa6f8"></a> `00baa6f8` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00baa6fc"></a> `00baa6fc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baa700"></a> `00baa700` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00baa704"></a> `00baa704` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00baa708"></a> `00baa708` | `49 00 86 52` | mov w9,#0x3002 | `FALL_THROUGH`
<a id="insn-00baa70c"></a> `00baa70c` | `ea ff 9f 52` | mov w10,#0xffff | `FALL_THROUGH`
<a id="insn-00baa710"></a> `00baa710` | `e1 83 02 91` | add x1,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baa714"></a> `00baa714` | `a8 83 1a f8` | stur x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00baa718"></a> `00baa718` | `08 50 40 a9` | ldp x8,x20,[x0] | `FALL_THROUGH`
<a id="insn-00baa71c"></a> `00baa71c` | `ff ff 0a a9` | stp xzr,xzr,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00baa720"></a> `00baa720` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baa724"></a> `00baa724` | `ff 73 01 79` | strh wzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00baa728"></a> `00baa728` | `ff 7f 0c a9` | stp xzr,xzr,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baa72c"></a> `00baa72c` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baa730"></a> `00baa730` | `e9 83 01 79` | strh w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baa734"></a> `00baa734` | `ff 0b 03 39` | strb wzr,[sp, #0xc2] | `FALL_THROUGH`
<a id="insn-00baa738"></a> `00baa738` | `ea b3 01 79` | strh w10,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00baa73c"></a> `00baa73c` | `00 a1 c0 3c` | ldur q0,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00baa740"></a> `00baa740` | `01 01 c0 3d` | ldr q1,[x8] | `FALL_THROUGH`
<a id="insn-00baa744"></a> `00baa744` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-00baa748"></a> `00baa748` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00baa74c"></a> `00baa74c` | `e0 a3 8a 3c` | stur q0,[sp, #0xaa] | `FALL_THROUGH`
<a id="insn-00baa750"></a> `00baa750` | `e1 2b 80 3d` | str q1,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baa754"></a> `00baa754` | `08 24 41 a9` | ldp x8,x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baa758"></a> `00baa758` | `0a 10 40 f9` | ldr x10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00baa75c"></a> `00baa75c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baa760"></a> `00baa760` | `f5 83 02 91` | add x21,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00baa764"></a> `00baa764` | `02 01 40 f9` | ldr x2,[x8] | `FALL_THROUGH`
<a id="insn-00baa768"></a> `00baa768` | `23 01 40 f9` | ldr x3,[x9] | `FALL_THROUGH`
<a id="insn-00baa76c"></a> `00baa76c` | `45 01 40 f9` | ldr x5,[x10] | `FALL_THROUGH`
<a id="insn-00baa770"></a> `00baa770` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00baa774"></a> `00baa774` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00baa778"></a> `00baa778` | `6e c6 02 94` | bl 0x00c5c130 | `UNCONDITIONAL_CALL`
<a id="insn-00baa77c"></a> `00baa77c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00baa780"></a> `00baa780` | `76 06 00 39` | strb w22,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00baa784"></a> `00baa784` | `28 02 00 34` | cbz w8,0x00baa7c8 | `CONDITIONAL_JUMP`
<a id="insn-00baa788"></a> `00baa788` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baa78c"></a> `00baa78c` | `68 00 00 36` | tbz w8,#0x0,0x00baa798 | `CONDITIONAL_JUMP`
<a id="insn-00baa790"></a> `00baa790` | `e0 6b 40 f9` | ldr x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baa794"></a> `00baa794` | `c7 b4 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00baa798"></a> `00baa798` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00baa79c"></a> `00baa79c` | `a9 83 5a f8` | ldur x9,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00baa7a0"></a> `00baa7a0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baa7a4"></a> `00baa7a4` | `41 0c 00 54` | b.ne 0x00baa92c | `CONDITIONAL_JUMP`
<a id="insn-00baa7a8"></a> `00baa7a8` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00baa7ac"></a> `00baa7ac` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00baa7b0"></a> `00baa7b0` | `f6 57 52 a9` | ldp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00baa7b4"></a> `00baa7b4` | `f8 5f 51 a9` | ldp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00baa7b8"></a> `00baa7b8` | `fa 67 50 a9` | ldp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00baa7bc"></a> `00baa7bc` | `fc 7b 40 f9` | ldr x28,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00baa7c0"></a> `00baa7c0` | `ff 43 05 91` | add sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00baa7c4"></a> `00baa7c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baa7c8"></a> `00baa7c8` | `e1 03 45 ad` | ldp q1,q0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00baa7cc"></a> `00baa7cc` | `e9 03 43 39` | ldrb w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baa7d0"></a> `00baa7d0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00baa7d4"></a> `00baa7d4` | `1a 81 00 91` | add x26,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00baa7d8"></a> `00baa7d8` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa7dc"></a> `00baa7dc` | `e1 03 00 ad` | stp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00baa7e0"></a> `00baa7e0` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baa7e4"></a> `00baa7e4` | `e9 00 00 37` | tbnz w9,#0x0,0x00baa800 | `CONDITIONAL_JUMP`
<a id="insn-00baa7e8"></a> `00baa7e8` | `a8 82 00 91` | add x8,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00baa7ec"></a> `00baa7ec` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00baa7f0"></a> `00baa7f0` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00baa7f4"></a> `00baa7f4` | `49 0b 00 f9` | str x9,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00baa7f8"></a> `00baa7f8` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00baa7fc"></a> `00baa7fc` | `19 00 00 14` | b 0x00baa860 | `UNCONDITIONAL_JUMP`
<a id="insn-00baa800"></a> `00baa800` | `f5 67 40 f9` | ldr x21,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00baa804"></a> `00baa804` | `bf 42 00 b1` | cmn x21,#0x10 | `FALL_THROUGH`
<a id="insn-00baa808"></a> `00baa808` | `42 09 00 54` | b.cs 0x00baa930 | `CONDITIONAL_JUMP`
<a id="insn-00baa80c"></a> `00baa80c` | `f6 6b 40 f9` | ldr x22,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00baa810"></a> `00baa810` | `bf 5e 00 f1` | cmp x21,#0x17 | `FALL_THROUGH`
<a id="insn-00baa814"></a> `00baa814` | `c2 00 00 54` | b.cs 0x00baa82c | `CONDITIONAL_JUMP`
<a id="insn-00baa818"></a> `00baa818` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00baa81c"></a> `00baa81c` | `57 07 00 91` | add x23,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00baa820"></a> `00baa820` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa824"></a> `00baa824` | `55 01 00 b5` | cbnz x21,0x00baa84c | `CONDITIONAL_JUMP`
<a id="insn-00baa828"></a> `00baa828` | `0d 00 00 14` | b 0x00baa85c | `UNCONDITIONAL_JUMP`
<a id="insn-00baa82c"></a> `00baa82c` | `a8 42 00 91` | add x8,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00baa830"></a> `00baa830` | `18 ed 7c 92` | and x24,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00baa834"></a> `00baa834` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00baa838"></a> `00baa838` | `96 b4 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00baa83c"></a> `00baa83c` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00baa840"></a> `00baa840` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00baa844"></a> `00baa844` | `e8 57 02 a9` | stp x8,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa848"></a> `00baa848` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baa84c"></a> `00baa84c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00baa850"></a> `00baa850` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00baa854"></a> `00baa854` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00baa858"></a> `00baa858` | `ea b4 02 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00baa85c"></a> `00baa85c` | `ff 6a 35 38` | strb wzr,[x23, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00baa860"></a> `00baa860` | `e8 b3 41 79` | ldrh w8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00baa864"></a> `00baa864` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00baa868"></a> `00baa868` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baa86c"></a> `00baa86c` | `ff 4b 00 f9` | str xzr,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00baa870"></a> `00baa870` | `e8 73 00 79` | strh w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00baa874"></a> `00baa874` | `e1 83 02 ad` | stp q1,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baa878"></a> `00baa878` | `e8 13 01 79` | strh w8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00baa87c"></a> `00baa87c` | `40 03 c0 3d` | ldr q0,[x26] | `FALL_THROUGH`
<a id="insn-00baa880"></a> `00baa880` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00baa884"></a> `00baa884` | `5f ff 00 a9` | stp xzr,xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00baa888"></a> `00baa888` | `5f 03 00 f9` | str xzr,[x26] | `FALL_THROUGH`
<a id="insn-00baa88c"></a> `00baa88c` | `e0 1f 80 3d` | str q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baa890"></a> `00baa890` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00baa894"></a> `00baa894` | `88 de 42 f9` | ldr x8,[x20, #0x5b8] | `FALL_THROUGH`
<a id="insn-00baa898"></a> `00baa898` | `89 e2 42 f9` | ldr x9,[x20, #0x5c0] | `FALL_THROUGH`
<a id="insn-00baa89c"></a> `00baa89c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baa8a0"></a> `00baa8a0` | `82 02 00 54` | b.cs 0x00baa8f0 | `CONDITIONAL_JUMP`
<a id="insn-00baa8a4"></a> `00baa8a4` | `e0 87 42 ad` | ldp q0,q1,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baa8a8"></a> `00baa8a8` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baa8ac"></a> `00baa8ac` | `29 81 00 91` | add x9,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00baa8b0"></a> `00baa8b0` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00baa8b4"></a> `00baa8b4` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00baa8b8"></a> `00baa8b8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00baa8bc"></a> `00baa8bc` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00baa8c0"></a> `00baa8c0` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00baa8c4"></a> `00baa8c4` | `3f fd 00 a9` | stp xzr,xzr,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00baa8c8"></a> `00baa8c8` | `3f 01 00 f9` | str xzr,[x9] | `FALL_THROUGH`
<a id="insn-00baa8cc"></a> `00baa8cc` | `e9 13 41 79` | ldrh w9,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00baa8d0"></a> `00baa8d0` | `0a 21 01 91` | add x10,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00baa8d4"></a> `00baa8d4` | `09 71 00 79` | strh w9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00baa8d8"></a> `00baa8d8` | `e9 4b 40 f9` | ldr x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00baa8dc"></a> `00baa8dc` | `09 21 00 f9` | str x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00baa8e0"></a> `00baa8e0` | `8a de 02 f9` | str x10,[x20, #0x5b8] | `FALL_THROUGH`
<a id="insn-00baa8e4"></a> `00baa8e4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa8e8"></a> `00baa8e8` | `68 01 00 37` | tbnz w8,#0x0,0x00baa914 | `CONDITIONAL_JUMP`
<a id="insn-00baa8ec"></a> `00baa8ec` | `0c 00 00 14` | b 0x00baa91c | `UNCONDITIONAL_JUMP`
<a id="insn-00baa8f0"></a> `00baa8f0` | `80 c2 16 91` | add x0,x20,#0x5b0 | `FALL_THROUGH`
<a id="insn-00baa8f4"></a> `00baa8f4` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baa8f8"></a> `00baa8f8` | `d2 c8 02 94` | bl 0x00c5cc40 | `UNCONDITIONAL_CALL`
<a id="insn-00baa8fc"></a> `00baa8fc` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baa900"></a> `00baa900` | `68 00 00 36` | tbz w8,#0x0,0x00baa90c | `CONDITIONAL_JUMP`
<a id="insn-00baa904"></a> `00baa904` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00baa908"></a> `00baa908` | `6a b4 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00baa90c"></a> `00baa90c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baa910"></a> `00baa910` | `68 00 00 36` | tbz w8,#0x0,0x00baa91c | `CONDITIONAL_JUMP`
<a id="insn-00baa914"></a> `00baa914` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baa918"></a> `00baa918` | `66 b4 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00baa91c"></a> `00baa91c` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00baa920"></a> `00baa920` | `e8 03 43 39` | ldrb w8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00baa924"></a> `00baa924` | `68 f3 07 37` | tbnz w8,#0x0,0x00baa790 | `CONDITIONAL_JUMP`
<a id="insn-00baa928"></a> `00baa928` | `9c ff ff 17` | b 0x00baa798 | `UNCONDITIONAL_JUMP`
<a id="insn-00baa92c"></a> `00baa92c` | `6d b4 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`
<a id="insn-00baa930"></a> `00baa930` | `04 c1 02 94` | bl 0x00c5ad40 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baa6dc`](#insn-00baa6dc) 範囲 `[['00baa6dc', '00baa70f']]`
  - `FALL_THROUGH` [`00baa70c`](#insn-00baa70c) → [`00baa710`](#insn-00baa710)
- ブロック [`00baa710`](#insn-00baa710) 範囲 `[['00baa710', '00baa733']]`
  - `FALL_THROUGH` [`00baa730`](#insn-00baa730) → [`00baa734`](#insn-00baa734)
- ブロック [`00baa734`](#insn-00baa734) 範囲 `[['00baa734', '00baa747']]`
  - `FALL_THROUGH` [`00baa744`](#insn-00baa744) → [`00baa748`](#insn-00baa748)
- ブロック [`00baa748`](#insn-00baa748) 範囲 `[['00baa748', '00baa767']]`
  - `FALL_THROUGH` [`00baa764`](#insn-00baa764) → [`00baa768`](#insn-00baa768)
- ブロック [`00baa768`](#insn-00baa768) 範囲 `[['00baa768', '00baa787']]`
  - `CONDITIONAL_JUMP` [`00baa784`](#insn-00baa784) → [`00baa7c8`](#insn-00baa7c8)
  - `FALL_THROUGH` [`00baa784`](#insn-00baa784) → [`00baa788`](#insn-00baa788)
- ブロック [`00baa788`](#insn-00baa788) 範囲 `[['00baa788', '00baa78f']]`
  - `CONDITIONAL_JUMP` [`00baa78c`](#insn-00baa78c) → [`00baa798`](#insn-00baa798)
  - `FALL_THROUGH` [`00baa78c`](#insn-00baa78c) → [`00baa790`](#insn-00baa790)
- ブロック [`00baa790`](#insn-00baa790) 範囲 `[['00baa790', '00baa797']]`
  - `FALL_THROUGH` [`00baa794`](#insn-00baa794) → [`00baa798`](#insn-00baa798)
- ブロック [`00baa798`](#insn-00baa798) 範囲 `[['00baa798', '00baa7a7']]`
  - `CONDITIONAL_JUMP` [`00baa7a4`](#insn-00baa7a4) → [`00baa92c`](#insn-00baa92c)
  - `FALL_THROUGH` [`00baa7a4`](#insn-00baa7a4) → [`00baa7a8`](#insn-00baa7a8)
- ブロック [`00baa7a8`](#insn-00baa7a8) 範囲 `[['00baa7a8', '00baa7b3']]`
  - `FALL_THROUGH` [`00baa7b0`](#insn-00baa7b0) → [`00baa7b4`](#insn-00baa7b4)
- ブロック [`00baa7b4`](#insn-00baa7b4) 範囲 `[['00baa7b4', '00baa7c7']]`
- ブロック [`00baa7c8`](#insn-00baa7c8) 範囲 `[['00baa7c8', '00baa7d7']]`
  - `FALL_THROUGH` [`00baa7d4`](#insn-00baa7d4) → [`00baa7d8`](#insn-00baa7d8)
- ブロック [`00baa7d8`](#insn-00baa7d8) 範囲 `[['00baa7d8', '00baa7e7']]`
  - `CONDITIONAL_JUMP` [`00baa7e4`](#insn-00baa7e4) → [`00baa800`](#insn-00baa800)
  - `FALL_THROUGH` [`00baa7e4`](#insn-00baa7e4) → [`00baa7e8`](#insn-00baa7e8)
- ブロック [`00baa7e8`](#insn-00baa7e8) 範囲 `[['00baa7e8', '00baa7ff']]`
  - `UNCONDITIONAL_JUMP` [`00baa7fc`](#insn-00baa7fc) → [`00baa860`](#insn-00baa860)
- ブロック [`00baa800`](#insn-00baa800) 範囲 `[['00baa800', '00baa803']]`
  - `FALL_THROUGH` [`00baa800`](#insn-00baa800) → [`00baa804`](#insn-00baa804)
- ブロック [`00baa804`](#insn-00baa804) 範囲 `[['00baa804', '00baa80b']]`
  - `CONDITIONAL_JUMP` [`00baa808`](#insn-00baa808) → [`00baa930`](#insn-00baa930)
  - `FALL_THROUGH` [`00baa808`](#insn-00baa808) → [`00baa80c`](#insn-00baa80c)
- ブロック [`00baa80c`](#insn-00baa80c) 範囲 `[['00baa80c', '00baa817']]`
  - `CONDITIONAL_JUMP` [`00baa814`](#insn-00baa814) → [`00baa82c`](#insn-00baa82c)
  - `FALL_THROUGH` [`00baa814`](#insn-00baa814) → [`00baa818`](#insn-00baa818)
- ブロック [`00baa818`](#insn-00baa818) 範囲 `[['00baa818', '00baa827']]`
  - `CONDITIONAL_JUMP` [`00baa824`](#insn-00baa824) → [`00baa84c`](#insn-00baa84c)
  - `FALL_THROUGH` [`00baa824`](#insn-00baa824) → [`00baa828`](#insn-00baa828)
- ブロック [`00baa828`](#insn-00baa828) 範囲 `[['00baa828', '00baa82b']]`
  - `UNCONDITIONAL_JUMP` [`00baa828`](#insn-00baa828) → [`00baa85c`](#insn-00baa85c)
- ブロック [`00baa82c`](#insn-00baa82c) 範囲 `[['00baa82c', '00baa833']]`
  - `FALL_THROUGH` [`00baa830`](#insn-00baa830) → [`00baa834`](#insn-00baa834)
- ブロック [`00baa834`](#insn-00baa834) 範囲 `[['00baa834', '00baa84b']]`
  - `FALL_THROUGH` [`00baa848`](#insn-00baa848) → [`00baa84c`](#insn-00baa84c)
- ブロック [`00baa84c`](#insn-00baa84c) 範囲 `[['00baa84c', '00baa853']]`
  - `FALL_THROUGH` [`00baa850`](#insn-00baa850) → [`00baa854`](#insn-00baa854)
- ブロック [`00baa854`](#insn-00baa854) 範囲 `[['00baa854', '00baa85b']]`
  - `FALL_THROUGH` [`00baa858`](#insn-00baa858) → [`00baa85c`](#insn-00baa85c)
- ブロック [`00baa85c`](#insn-00baa85c) 範囲 `[['00baa85c', '00baa85f']]`
  - `FALL_THROUGH` [`00baa85c`](#insn-00baa85c) → [`00baa860`](#insn-00baa860)
- ブロック [`00baa860`](#insn-00baa860) 範囲 `[['00baa860', '00baa8a3']]`
  - `CONDITIONAL_JUMP` [`00baa8a0`](#insn-00baa8a0) → [`00baa8f0`](#insn-00baa8f0)
  - `FALL_THROUGH` [`00baa8a0`](#insn-00baa8a0) → [`00baa8a4`](#insn-00baa8a4)
- ブロック [`00baa8a4`](#insn-00baa8a4) 範囲 `[['00baa8a4', '00baa8c7']]`
  - `FALL_THROUGH` [`00baa8c4`](#insn-00baa8c4) → [`00baa8c8`](#insn-00baa8c8)
- ブロック [`00baa8c8`](#insn-00baa8c8) 範囲 `[['00baa8c8', '00baa8eb']]`
  - `CONDITIONAL_JUMP` [`00baa8e8`](#insn-00baa8e8) → [`00baa914`](#insn-00baa914)
  - `FALL_THROUGH` [`00baa8e8`](#insn-00baa8e8) → [`00baa8ec`](#insn-00baa8ec)
- ブロック [`00baa8ec`](#insn-00baa8ec) 範囲 `[['00baa8ec', '00baa8ef']]`
  - `UNCONDITIONAL_JUMP` [`00baa8ec`](#insn-00baa8ec) → [`00baa91c`](#insn-00baa91c)
- ブロック [`00baa8f0`](#insn-00baa8f0) 範囲 `[['00baa8f0', '00baa903']]`
  - `CONDITIONAL_JUMP` [`00baa900`](#insn-00baa900) → [`00baa90c`](#insn-00baa90c)
  - `FALL_THROUGH` [`00baa900`](#insn-00baa900) → [`00baa904`](#insn-00baa904)
- ブロック [`00baa904`](#insn-00baa904) 範囲 `[['00baa904', '00baa907']]`
  - `FALL_THROUGH` [`00baa904`](#insn-00baa904) → [`00baa908`](#insn-00baa908)
- ブロック [`00baa908`](#insn-00baa908) 範囲 `[['00baa908', '00baa90b']]`
  - `FALL_THROUGH` [`00baa908`](#insn-00baa908) → [`00baa90c`](#insn-00baa90c)
- ブロック [`00baa90c`](#insn-00baa90c) 範囲 `[['00baa90c', '00baa913']]`
  - `CONDITIONAL_JUMP` [`00baa910`](#insn-00baa910) → [`00baa91c`](#insn-00baa91c)
  - `FALL_THROUGH` [`00baa910`](#insn-00baa910) → [`00baa914`](#insn-00baa914)
- ブロック [`00baa914`](#insn-00baa914) 範囲 `[['00baa914', '00baa91b']]`
  - `FALL_THROUGH` [`00baa918`](#insn-00baa918) → [`00baa91c`](#insn-00baa91c)
- ブロック [`00baa91c`](#insn-00baa91c) 範囲 `[['00baa91c', '00baa927']]`
  - `CONDITIONAL_JUMP` [`00baa924`](#insn-00baa924) → [`00baa790`](#insn-00baa790)
  - `FALL_THROUGH` [`00baa924`](#insn-00baa924) → [`00baa928`](#insn-00baa928)
- ブロック [`00baa928`](#insn-00baa928) 範囲 `[['00baa928', '00baa92b']]`
  - `UNCONDITIONAL_JUMP` [`00baa928`](#insn-00baa928) → [`00baa798`](#insn-00baa798)
- ブロック [`00baa92c`](#insn-00baa92c) 範囲 `[['00baa92c', '00baa92f']]`
- ブロック [`00baa930`](#insn-00baa930) 範囲 `[['00baa930', '00baa933']]`

## 命令位置別の参照

- [`00baa6e0`](#insn-00baa6e0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa6e4`](#insn-00baa6e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa6e8`](#insn-00baa6e8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa6ec`](#insn-00baa6ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa6f0`](#insn-00baa6f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa6f4`](#insn-00baa6f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa714`](#insn-00baa714) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa71c`](#insn-00baa71c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa720`](#insn-00baa720) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa724`](#insn-00baa724) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa728`](#insn-00baa728) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa72c`](#insn-00baa72c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa730`](#insn-00baa730) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa734`](#insn-00baa734) → `Stack[-0x8e]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa738`](#insn-00baa738) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa74c`](#insn-00baa74c) → `Stack[-0xa6]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa750`](#insn-00baa750) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa778`](#insn-00baa778) → [`00c5c130`](../00c5c/00c5c130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c130` · 推定シンボル `None` · 推定型 `None`
- [`00baa784`](#insn-00baa784) → [`00baa7c8`](#insn-00baa7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa788`](#insn-00baa788) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa78c`](#insn-00baa78c) → [`00baa798`](#insn-00baa798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa790`](#insn-00baa790) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa794`](#insn-00baa794) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00baa79c`](#insn-00baa79c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7a4`](#insn-00baa7a4) → [`00baa92c`](#insn-00baa92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7a8`](#insn-00baa7a8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7ac`](#insn-00baa7ac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7b0`](#insn-00baa7b0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7b4`](#insn-00baa7b4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7b8`](#insn-00baa7b8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7bc`](#insn-00baa7bc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7c8`](#insn-00baa7c8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7cc`](#insn-00baa7cc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7d8`](#insn-00baa7d8) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7dc`](#insn-00baa7dc) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7e0`](#insn-00baa7e0) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7e4`](#insn-00baa7e4) → [`00baa800`](#insn-00baa800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7ec`](#insn-00baa7ec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7f0`](#insn-00baa7f0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7f4`](#insn-00baa7f4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7f8`](#insn-00baa7f8) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa7fc`](#insn-00baa7fc) → [`00baa860`](#insn-00baa860) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa800`](#insn-00baa800) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa808`](#insn-00baa808) → [`00baa930`](#insn-00baa930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa80c`](#insn-00baa80c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa814`](#insn-00baa814) → [`00baa82c`](#insn-00baa82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa820`](#insn-00baa820) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa824`](#insn-00baa824) → [`00baa84c`](#insn-00baa84c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa828`](#insn-00baa828) → [`00baa85c`](#insn-00baa85c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa838`](#insn-00baa838) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00baa844`](#insn-00baa844) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa848`](#insn-00baa848) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa858`](#insn-00baa858) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00baa860`](#insn-00baa860) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa864`](#insn-00baa864) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa868`](#insn-00baa868) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa86c`](#insn-00baa86c) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa870`](#insn-00baa870) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa874`](#insn-00baa874) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa878`](#insn-00baa878) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa87c`](#insn-00baa87c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa880`](#insn-00baa880) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa884`](#insn-00baa884) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa888`](#insn-00baa888) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa88c`](#insn-00baa88c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa890`](#insn-00baa890) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8a0`](#insn-00baa8a0) → [`00baa8f0`](#insn-00baa8f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8a4`](#insn-00baa8a4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8b4`](#insn-00baa8b4) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8b8`](#insn-00baa8b8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8c4`](#insn-00baa8c4) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8c8`](#insn-00baa8c8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8cc`](#insn-00baa8cc) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8d8`](#insn-00baa8d8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8e4`](#insn-00baa8e4) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8e8`](#insn-00baa8e8) → [`00baa914`](#insn-00baa914) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8ec`](#insn-00baa8ec) → [`00baa91c`](#insn-00baa91c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa8f8`](#insn-00baa8f8) → [`00c5cc40`](../00c5c/00c5cc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc40` · 推定シンボル `None` · 推定型 `None`
- [`00baa8fc`](#insn-00baa8fc) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa900`](#insn-00baa900) → [`00baa90c`](#insn-00baa90c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa904`](#insn-00baa904) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa908`](#insn-00baa908) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00baa90c`](#insn-00baa90c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa910`](#insn-00baa910) → [`00baa91c`](#insn-00baa91c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa914`](#insn-00baa914) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa918`](#insn-00baa918) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00baa920`](#insn-00baa920) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa924`](#insn-00baa924) → [`00baa790`](#insn-00baa790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa928`](#insn-00baa928) → [`00baa798`](#insn-00baa798) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baa92c`](#insn-00baa92c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`
- [`00baa930`](#insn-00baa930) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baa6e0`](#insn-00baa6e0)

~~~json
{
  "source": "00baa6e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa6e4`](#insn-00baa6e4)

~~~json
{
  "source": "00baa6e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa6e8`](#insn-00baa6e8)

~~~json
{
  "source": "00baa6e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa6ec`](#insn-00baa6ec)

~~~json
{
  "source": "00baa6ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa6f0`](#insn-00baa6f0)

~~~json
{
  "source": "00baa6f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa6f4`](#insn-00baa6f4)

~~~json
{
  "source": "00baa6f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa714`](#insn-00baa714)

~~~json
{
  "source": "00baa714",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa71c`](#insn-00baa71c)

~~~json
{
  "source": "00baa71c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa720`](#insn-00baa720)

~~~json
{
  "source": "00baa720",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa724`](#insn-00baa724)

~~~json
{
  "source": "00baa724",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa728`](#insn-00baa728)

~~~json
{
  "source": "00baa728",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa72c`](#insn-00baa72c)

~~~json
{
  "source": "00baa72c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa730`](#insn-00baa730)

~~~json
{
  "source": "00baa730",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa734`](#insn-00baa734)

~~~json
{
  "source": "00baa734",
  "target": "Stack[-0x8e]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa738`](#insn-00baa738)

~~~json
{
  "source": "00baa738",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa74c`](#insn-00baa74c)

~~~json
{
  "source": "00baa74c",
  "target": "Stack[-0xa6]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa750`](#insn-00baa750)

~~~json
{
  "source": "00baa750",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa778`](#insn-00baa778)

~~~json
{
  "source": "00baa778",
  "target": "00c5c130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa784`](#insn-00baa784)

~~~json
{
  "source": "00baa784",
  "target": "00baa7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa788`](#insn-00baa788)

~~~json
{
  "source": "00baa788",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa78c`](#insn-00baa78c)

~~~json
{
  "source": "00baa78c",
  "target": "00baa798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa790`](#insn-00baa790)

~~~json
{
  "source": "00baa790",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa794`](#insn-00baa794)

~~~json
{
  "source": "00baa794",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa79c`](#insn-00baa79c)

~~~json
{
  "source": "00baa79c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7a4`](#insn-00baa7a4)

~~~json
{
  "source": "00baa7a4",
  "target": "00baa92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7a8`](#insn-00baa7a8)

~~~json
{
  "source": "00baa7a8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7ac`](#insn-00baa7ac)

~~~json
{
  "source": "00baa7ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7b0`](#insn-00baa7b0)

~~~json
{
  "source": "00baa7b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7b4`](#insn-00baa7b4)

~~~json
{
  "source": "00baa7b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7b8`](#insn-00baa7b8)

~~~json
{
  "source": "00baa7b8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7bc`](#insn-00baa7bc)

~~~json
{
  "source": "00baa7bc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7c8`](#insn-00baa7c8)

~~~json
{
  "source": "00baa7c8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7cc`](#insn-00baa7cc)

~~~json
{
  "source": "00baa7cc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7d8`](#insn-00baa7d8)

~~~json
{
  "source": "00baa7d8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7dc`](#insn-00baa7dc)

~~~json
{
  "source": "00baa7dc",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7e0`](#insn-00baa7e0)

~~~json
{
  "source": "00baa7e0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7e4`](#insn-00baa7e4)

~~~json
{
  "source": "00baa7e4",
  "target": "00baa800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7ec`](#insn-00baa7ec)

~~~json
{
  "source": "00baa7ec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7f0`](#insn-00baa7f0)

~~~json
{
  "source": "00baa7f0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7f4`](#insn-00baa7f4)

~~~json
{
  "source": "00baa7f4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7f8`](#insn-00baa7f8)

~~~json
{
  "source": "00baa7f8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa7fc`](#insn-00baa7fc)

~~~json
{
  "source": "00baa7fc",
  "target": "00baa860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa800`](#insn-00baa800)

~~~json
{
  "source": "00baa800",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa808`](#insn-00baa808)

~~~json
{
  "source": "00baa808",
  "target": "00baa930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa80c`](#insn-00baa80c)

~~~json
{
  "source": "00baa80c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa814`](#insn-00baa814)

~~~json
{
  "source": "00baa814",
  "target": "00baa82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa820`](#insn-00baa820)

~~~json
{
  "source": "00baa820",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa824`](#insn-00baa824)

~~~json
{
  "source": "00baa824",
  "target": "00baa84c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa828`](#insn-00baa828)

~~~json
{
  "source": "00baa828",
  "target": "00baa85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa838`](#insn-00baa838)

~~~json
{
  "source": "00baa838",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa844`](#insn-00baa844)

~~~json
{
  "source": "00baa844",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa848`](#insn-00baa848)

~~~json
{
  "source": "00baa848",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa858`](#insn-00baa858)

~~~json
{
  "source": "00baa858",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa860`](#insn-00baa860)

~~~json
{
  "source": "00baa860",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa864`](#insn-00baa864)

~~~json
{
  "source": "00baa864",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa868`](#insn-00baa868)

~~~json
{
  "source": "00baa868",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa86c`](#insn-00baa86c)

~~~json
{
  "source": "00baa86c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa870`](#insn-00baa870)

~~~json
{
  "source": "00baa870",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa874`](#insn-00baa874)

~~~json
{
  "source": "00baa874",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa878`](#insn-00baa878)

~~~json
{
  "source": "00baa878",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa87c`](#insn-00baa87c)

~~~json
{
  "source": "00baa87c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa880`](#insn-00baa880)

~~~json
{
  "source": "00baa880",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa884`](#insn-00baa884)

~~~json
{
  "source": "00baa884",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa888`](#insn-00baa888)

~~~json
{
  "source": "00baa888",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa88c`](#insn-00baa88c)

~~~json
{
  "source": "00baa88c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa890`](#insn-00baa890)

~~~json
{
  "source": "00baa890",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8a0`](#insn-00baa8a0)

~~~json
{
  "source": "00baa8a0",
  "target": "00baa8f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8a4`](#insn-00baa8a4)

~~~json
{
  "source": "00baa8a4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8b4`](#insn-00baa8b4)

~~~json
{
  "source": "00baa8b4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8b8`](#insn-00baa8b8)

~~~json
{
  "source": "00baa8b8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8c4`](#insn-00baa8c4)

~~~json
{
  "source": "00baa8c4",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8c8`](#insn-00baa8c8)

~~~json
{
  "source": "00baa8c8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8cc`](#insn-00baa8cc)

~~~json
{
  "source": "00baa8cc",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8d8`](#insn-00baa8d8)

~~~json
{
  "source": "00baa8d8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8e4`](#insn-00baa8e4)

~~~json
{
  "source": "00baa8e4",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8e8`](#insn-00baa8e8)

~~~json
{
  "source": "00baa8e8",
  "target": "00baa914",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8ec`](#insn-00baa8ec)

~~~json
{
  "source": "00baa8ec",
  "target": "00baa91c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa8f8`](#insn-00baa8f8)

~~~json
{
  "source": "00baa8f8",
  "target": "00c5cc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa8fc`](#insn-00baa8fc)

~~~json
{
  "source": "00baa8fc",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa900`](#insn-00baa900)

~~~json
{
  "source": "00baa900",
  "target": "00baa90c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa904`](#insn-00baa904)

~~~json
{
  "source": "00baa904",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa908`](#insn-00baa908)

~~~json
{
  "source": "00baa908",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa90c`](#insn-00baa90c)

~~~json
{
  "source": "00baa90c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa910`](#insn-00baa910)

~~~json
{
  "source": "00baa910",
  "target": "00baa91c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa914`](#insn-00baa914)

~~~json
{
  "source": "00baa914",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa918`](#insn-00baa918)

~~~json
{
  "source": "00baa918",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa920`](#insn-00baa920)

~~~json
{
  "source": "00baa920",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa924`](#insn-00baa924)

~~~json
{
  "source": "00baa924",
  "target": "00baa790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa928`](#insn-00baa928)

~~~json
{
  "source": "00baa928",
  "target": "00baa798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baa92c`](#insn-00baa92c)

~~~json
{
  "source": "00baa92c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baa930`](#insn-00baa930)

~~~json
{
  "source": "00baa930",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
