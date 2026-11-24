# 007abbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0064.md#review-a11f922c3364af9197a5ee89e498fcd6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007abbbc",
  "name": "FUN_007abbbc",
  "size": 900,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "19d668c379a93b05b8cc13e68240bb4ceaedfa279ec66ad8a48a9dcea4f15b20",
  "source_text_sha256": "19d668c379a93b05b8cc13e68240bb4ceaedfa279ec66ad8a48a9dcea4f15b20",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007abbbc",
        "007abf3b"
      ],
      [
        "007ac068",
        "007ac06b"
      ]
    ],
    "bytes_sha256": "896b6e4fb0284ddf748ea0aacab2024faa22ff18c1c5d53c8a2f48f8e4e0b582",
    "instruction_count": 225,
    "instruction_bytes": 900,
    "body_bytes": 900,
    "indirect": 14,
    "unresolved": 12
  }
}
~~~

## 呼び出し元

- [007ab86c](../007ab/007ab86c.md)

## 呼び出し先

- [00598e94](../00598/00598e94.md)
- [00599054](../00599/00599054.md)
- [0059bc68](../0059b/0059bc68.md)
- [00796258](../00796/00796258.md)
- [00796290](../00796/00796290.md)
- [007afbac](../007af/007afbac.md)
- [007afef8](../007af/007afef8.md)
- [007b027c](../007b0/007b027c.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 関連文字列（未確認候補）

~~~text
"¨{"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5415 bytes

~~~c

void FUN_007abbbc(undefined8 param_1,long *param_2,long *param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 **ppuVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 local_f8;
  long *local_f0;
  undefined8 local_e8;
  long *local_e0;
  undefined1 uStack_d1;
  long local_d0 [4];
  long *local_b0;
  long local_a0 [4];
  long *local_80;
  undefined8 *local_70 [4];
  undefined8 **local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)_Znwm(0x38);
  puVar2[6] = 0;
  puVar2[1] = 0;
  *puVar2 = 0;
  puVar2[3] = 0;
  puVar2[2] = 0;
  puVar2[5] = 0;
  puVar2[4] = 0;
  FUN_0059bc68();
  *puVar2 = &PTR_FUN_00c6fd38;
  local_70[0] = puVar2;
  FUN_007afbac(&local_e8,&uStack_d1,local_70);
  puVar2 = local_70[0];
  local_70[0] = (undefined8 *)0x0;
  if (puVar2 != (undefined8 *)0x0) {
    *puVar2 = &PTR_FUN_00c6eac0;
    if ((*(byte *)(puVar2 + 4) & 1) != 0) {
      _ZdlPv((void *)puVar2[6]);
    }
    if ((*(byte *)(puVar2 + 1) & 1) != 0) {
      _ZdlPv((void *)puVar2[3]);
    }
    _ZdlPv(puVar2);
  }
  uVar5 = local_e8;
  plVar3 = (long *)param_2[4];
  local_80 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_2) {
      local_80 = local_a0;
      (**(code **)(*param_2 + 0x18))(param_2,local_a0);
    }
    else {
      local_80 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_50 = (undefined8 **)0x0;
  ppuVar4 = (undefined8 **)_Znwm(0x40);
  *ppuVar4 = &PTR_FUN_00c7b938;
  puVar2 = (undefined8 *)0x0;
  if (local_80 == (long *)0x0) {
LAB_007abcf0:
    ppuVar4[6] = puVar2;
  }
  else {
    if (local_80 != local_a0) {
      puVar2 = (undefined8 *)(**(code **)(*local_80 + 0x10))();
      goto LAB_007abcf0;
    }
    ppuVar4[6] = ppuVar4 + 2;
    (**(code **)(local_a0[0] + 0x18))(local_a0);
  }
  local_50 = ppuVar4;
  FUN_00598e94(uVar5,local_70);
  if (local_50 == local_70) {
    lVar6 = 0x20;
    ppuVar4 = local_70;
LAB_007abd40:
                    /* try { // try from 007abd48 to 008abd5b has its CatchHandler @ 007ac8a4 */
    (**(code **)((long)*ppuVar4 + lVar6))();
  }
  else if (local_50 != (undefined8 **)0x0) {
    lVar6 = 0x28;
    ppuVar4 = local_50;
    goto LAB_007abd40;
  }
  if (local_80 == local_a0) {
    lVar6 = 0x20;
                    /* try { // try from 007abd6c to 008abd77 has its CatchHandler @ 007ac89c */
    plVar3 = local_a0;
LAB_007abd70:
    (**(code **)(*plVar3 + lVar6))();
  }
  else {
                    /* try { // try from 007abd5c to 008abd67 has its CatchHandler @ 007ac8a0 */
    if (local_80 != (long *)0x0) {
      lVar6 = 0x28;
      plVar3 = local_80;
      goto LAB_007abd70;
    }
  }
  uVar5 = local_e8;
  plVar3 = (long *)param_3[4];
  local_b0 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_3) {
      local_b0 = local_d0;
      (**(code **)(*param_3 + 0x18))(param_3,local_d0);
    }
    else {
      local_b0 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_50 = (undefined8 **)0x0;
                    /* try { // try from 007abdc4 to 008abdd7 has its CatchHandler @ 007ac8c0 */
  ppuVar4 = (undefined8 **)_Znwm(0x40);
                    /* try { // try from 007abdd8 to 008abde3 has its CatchHandler @ 007ac8bc */
  *ppuVar4 = &PTR_FUN_00c7b9b8;
                    /* try { // try from 007abde4 to 008abdef has its CatchHandler @ 007ac8ac */
  puVar2 = (undefined8 *)0x0;
  if (local_b0 == (long *)0x0) {
LAB_007abe00:
    ppuVar4[6] = puVar2;
  }
  else {
    if (local_b0 != local_d0) {
      puVar2 = (undefined8 *)(**(code **)(*local_b0 + 0x10))();
      goto LAB_007abe00;
    }
    ppuVar4[6] = ppuVar4 + 2;
    (**(code **)(local_d0[0] + 0x18))(local_d0);
  }
  local_50 = ppuVar4;
  FUN_00599054(uVar5,local_70);
  if (local_50 == local_70) {
    lVar6 = 0x20;
    ppuVar4 = local_70;
LAB_007abe50:
                    /* try { // try from 007abe58 to 008abe63 has its CatchHandler @ 007ac8bc */
    (**(code **)((long)*ppuVar4 + lVar6))();
  }
  else if (local_50 != (undefined8 **)0x0) {
    lVar6 = 0x28;
    ppuVar4 = local_50;
                    /* try { // try from 007abe44 to 008abe57 has its CatchHandler @ 007ac8c0 */
    goto LAB_007abe50;
  }
                    /* try { // try from 007abe64 to 008abe6f has its CatchHandler @ 007ac8ac */
  if (local_b0 == local_d0) {
    lVar6 = 0x20;
    plVar3 = local_d0;
  }
  else {
    if (local_b0 == (long *)0x0) goto LAB_007abe8c;
    lVar6 = 0x28;
    plVar3 = local_b0;
  }
  (**(code **)(*plVar3 + lVar6))();
LAB_007abe8c:
  uVar5 = FUN_00796258();
  local_f8 = local_e8;
  local_f0 = local_e0;
  if (local_e0 != (long *)0x0) {
                    /* try { // try from 007abe9c to 008abf2b has its CatchHandler @ 007ac8c8 */
    FUN_00c54d60(1,local_e0 + 1);
  }
  FUN_00796290(uVar5,&local_f8);
  plVar3 = local_f0;
  if ((local_f0 != (long *)0x0) &&
     (lVar6 = FUN_00c54d90(0xffffffffffffffff,local_f0 + 1), lVar6 == 0)) {
    (**(code **)(*plVar3 + 0x10))(plVar3);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
  }
  if ((local_e0 != (long *)0x0) &&
     (lVar6 = FUN_00c54d90(0xffffffffffffffff,local_e0 + 1), lVar6 == 0)) {
    (**(code **)(*local_e0 + 0x10))(local_e0);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_e0);
  }
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007abbbc"></a> `007abbbc` | `ff 03 04 d1` | sub sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-007abbc0"></a> `007abbc0` | `fd 7b 0d a9` | stp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007abbc4"></a> `007abbc4` | `f6 57 0e a9` | stp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007abbc8"></a> `007abbc8` | `f4 4f 0f a9` | stp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007abbcc"></a> `007abbcc` | `fd 43 03 91` | add x29,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-007abbd0"></a> `007abbd0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007abbd4"></a> `007abbd4` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-007abbd8"></a> `007abbd8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-007abbdc"></a> `007abbdc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-007abbe0"></a> `007abbe0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007abbe4"></a> `007abbe4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007abbe8"></a> `007abbe8` | `d2 b4 12 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-007abbec"></a> `007abbec` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-007abbf0"></a> `007abbf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007abbf4"></a> `007abbf4` | `1f 18 00 f9` | str xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-007abbf8"></a> `007abbf8` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-007abbfc"></a> `007abbfc` | `00 08 80 3d` | str q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-007abc00"></a> `007abc00` | `1a c0 f7 97` | bl 0x0059bc68 | `UNCONDITIONAL_CALL`
<a id="insn-007abc04"></a> `007abc04` | `28 26 00 90` | adrp x8,0xc6f000 | `FALL_THROUGH`
<a id="insn-007abc08"></a> `007abc08` | `08 a1 34 91` | add x8,x8,#0xd28 | `FALL_THROUGH`
<a id="insn-007abc0c"></a> `007abc0c` | `b4 03 1c f8` | stur x20,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007abc10"></a> `007abc10` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-007abc14"></a> `007abc14` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-007abc18"></a> `007abc18` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007abc1c"></a> `007abc1c` | `e0 bf 00 91` | add x0,sp,#0x2f | `FALL_THROUGH`
<a id="insn-007abc20"></a> `007abc20` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abc24"></a> `007abc24` | `e2 0f 00 94` | bl 0x007afbac | `UNCONDITIONAL_CALL`
<a id="insn-007abc28"></a> `007abc28` | `b4 03 5c f8` | ldur x20,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007abc2c"></a> `007abc2c` | `bf 03 1c f8` | stur xzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007abc30"></a> `007abc30` | `f4 01 00 b4` | cbz x20,0x007abc6c | `CONDITIONAL_JUMP`
<a id="insn-007abc34"></a> `007abc34` | `08 26 00 f0` | adrp x8,0xc6e000 | `FALL_THROUGH`
<a id="insn-007abc38"></a> `007abc38` | `08 c1 2a 91` | add x8,x8,#0xab0 | `FALL_THROUGH`
<a id="insn-007abc3c"></a> `007abc3c` | `89 82 40 39` | ldrb w9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-007abc40"></a> `007abc40` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-007abc44"></a> `007abc44` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-007abc48"></a> `007abc48` | `69 00 00 36` | tbz w9,#0x0,0x007abc54 | `CONDITIONAL_JUMP`
<a id="insn-007abc4c"></a> `007abc4c` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-007abc50"></a> `007abc50` | `c0 b4 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007abc54"></a> `007abc54` | `88 22 40 39` | ldrb w8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-007abc58"></a> `007abc58` | `68 00 00 36` | tbz w8,#0x0,0x007abc64 | `CONDITIONAL_JUMP`
<a id="insn-007abc5c"></a> `007abc5c` | `80 0e 40 f9` | ldr x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-007abc60"></a> `007abc60` | `bc b4 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007abc64"></a> `007abc64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007abc68"></a> `007abc68` | `ba b4 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007abc6c"></a> `007abc6c` | `a0 12 40 f9` | ldr x0,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-007abc70"></a> `007abc70` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007abc74"></a> `007abc74` | `c0 00 00 b4` | cbz x0,0x007abc8c | `CONDITIONAL_JUMP`
<a id="insn-007abc78"></a> `007abc78` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-007abc7c"></a> `007abc7c` | `c0 00 00 54` | b.eq 0x007abc94 | `CONDITIONAL_JUMP`
<a id="insn-007abc80"></a> `007abc80` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007abc84"></a> `007abc84` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abc88"></a> `007abc88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abc8c"></a> `007abc8c` | `e0 43 00 f9` | str x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007abc90"></a> `007abc90` | `08 00 00 14` | b 0x007abcb0 | `UNCONDITIONAL_JUMP`
<a id="insn-007abc94"></a> `007abc94` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abc98"></a> `007abc98` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-007abc9c"></a> `007abc9c` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007abca0"></a> `007abca0` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-007abca4"></a> `007abca4` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abca8"></a> `007abca8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007abcac"></a> `007abcac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abcb0"></a> `007abcb0` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abcb4"></a> `007abcb4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-007abcb8"></a> `007abcb8` | `9e b4 12 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-007abcbc"></a> `007abcbc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007abcc0"></a> `007abcc0` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007abcc4"></a> `007abcc4` | `88 26 00 90` | adrp x8,0xc7b000 | `FALL_THROUGH`
<a id="insn-007abcc8"></a> `007abcc8` | `08 e1 24 91` | add x8,x8,#0x938 | `FALL_THROUGH`
<a id="insn-007abccc"></a> `007abccc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007abcd0"></a> `007abcd0` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007abcd4"></a> `007abcd4` | `e0 00 00 b4` | cbz x0,0x007abcf0 | `CONDITIONAL_JUMP`
<a id="insn-007abcd8"></a> `007abcd8` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abcdc"></a> `007abcdc` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007abce0"></a> `007abce0` | `c0 00 00 54` | b.eq 0x007abcf8 | `CONDITIONAL_JUMP`
<a id="insn-007abce4"></a> `007abce4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007abce8"></a> `007abce8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abcec"></a> `007abcec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abcf0"></a> `007abcf0` | `a0 1a 00 f9` | str x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007abcf4"></a> `007abcf4` | `06 00 00 14` | b 0x007abd0c | `UNCONDITIONAL_JUMP`
<a id="insn-007abcf8"></a> `007abcf8` | `e8 33 40 f9` | ldr x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007abcfc"></a> `007abcfc` | `a1 1a 00 f9` | str x1,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007abd00"></a> `007abd00` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007abd04"></a> `007abd04` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abd08"></a> `007abd08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abd0c"></a> `007abd0c` | `b5 03 1e f8` | stur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abd10"></a> `007abd10` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abd14"></a> `007abd14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007abd18"></a> `007abd18` | `b4 03 01 d1` | sub x20,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abd1c"></a> `007abd1c` | `5e b4 f7 97` | bl 0x00598e94 | `UNCONDITIONAL_CALL`
<a id="insn-007abd20"></a> `007abd20` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abd24"></a> `007abd24` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-007abd28"></a> `007abd28` | `80 00 00 54` | b.eq 0x007abd38 | `CONDITIONAL_JUMP`
<a id="insn-007abd2c"></a> `007abd2c` | `00 01 00 b4` | cbz x0,0x007abd4c | `CONDITIONAL_JUMP`
<a id="insn-007abd30"></a> `007abd30` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007abd34"></a> `007abd34` | `03 00 00 14` | b 0x007abd40 | `UNCONDITIONAL_JUMP`
<a id="insn-007abd38"></a> `007abd38` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007abd3c"></a> `007abd3c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abd40"></a> `007abd40` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007abd44"></a> `007abd44` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007abd48"></a> `007abd48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abd4c"></a> `007abd4c` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007abd50"></a> `007abd50` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abd54"></a> `007abd54` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007abd58"></a> `007abd58` | `80 00 00 54` | b.eq 0x007abd68 | `CONDITIONAL_JUMP`
<a id="insn-007abd5c"></a> `007abd5c` | `00 01 00 b4` | cbz x0,0x007abd7c | `CONDITIONAL_JUMP`
<a id="insn-007abd60"></a> `007abd60` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007abd64"></a> `007abd64` | `03 00 00 14` | b 0x007abd70 | `UNCONDITIONAL_JUMP`
<a id="insn-007abd68"></a> `007abd68` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007abd6c"></a> `007abd6c` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007abd70"></a> `007abd70` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007abd74"></a> `007abd74` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007abd78"></a> `007abd78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abd7c"></a> `007abd7c` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007abd80"></a> `007abd80` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007abd84"></a> `007abd84` | `c0 00 00 b4` | cbz x0,0x007abd9c | `CONDITIONAL_JUMP`
<a id="insn-007abd88"></a> `007abd88` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-007abd8c"></a> `007abd8c` | `c0 00 00 54` | b.eq 0x007abda4 | `CONDITIONAL_JUMP`
<a id="insn-007abd90"></a> `007abd90` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007abd94"></a> `007abd94` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abd98"></a> `007abd98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abd9c"></a> `007abd9c` | `e0 2b 00 f9` | str x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007abda0"></a> `007abda0` | `08 00 00 14` | b 0x007abdc0 | `UNCONDITIONAL_JUMP`
<a id="insn-007abda4"></a> `007abda4` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abda8"></a> `007abda8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-007abdac"></a> `007abdac` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007abdb0"></a> `007abdb0` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-007abdb4"></a> `007abdb4` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abdb8"></a> `007abdb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abdbc"></a> `007abdbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abdc0"></a> `007abdc0` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abdc4"></a> `007abdc4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-007abdc8"></a> `007abdc8` | `5a b4 12 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-007abdcc"></a> `007abdcc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007abdd0"></a> `007abdd0` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007abdd4"></a> `007abdd4` | `88 26 00 90` | adrp x8,0xc7b000 | `FALL_THROUGH`
<a id="insn-007abdd8"></a> `007abdd8` | `08 e1 26 91` | add x8,x8,#0x9b8 | `FALL_THROUGH`
<a id="insn-007abddc"></a> `007abddc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007abde0"></a> `007abde0` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007abde4"></a> `007abde4` | `e0 00 00 b4` | cbz x0,0x007abe00 | `CONDITIONAL_JUMP`
<a id="insn-007abde8"></a> `007abde8` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abdec"></a> `007abdec` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007abdf0"></a> `007abdf0` | `c0 00 00 54` | b.eq 0x007abe08 | `CONDITIONAL_JUMP`
<a id="insn-007abdf4"></a> `007abdf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007abdf8"></a> `007abdf8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abdfc"></a> `007abdfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abe00"></a> `007abe00` | `a0 1a 00 f9` | str x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007abe04"></a> `007abe04` | `06 00 00 14` | b 0x007abe1c | `UNCONDITIONAL_JUMP`
<a id="insn-007abe08"></a> `007abe08` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007abe0c"></a> `007abe0c` | `a1 1a 00 f9` | str x1,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007abe10"></a> `007abe10` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007abe14"></a> `007abe14` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abe18"></a> `007abe18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abe1c"></a> `007abe1c` | `b5 03 1e f8` | stur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abe20"></a> `007abe20` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abe24"></a> `007abe24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007abe28"></a> `007abe28` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abe2c"></a> `007abe2c` | `8a b4 f7 97` | bl 0x00599054 | `UNCONDITIONAL_CALL`
<a id="insn-007abe30"></a> `007abe30` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007abe34"></a> `007abe34` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-007abe38"></a> `007abe38` | `80 00 00 54` | b.eq 0x007abe48 | `CONDITIONAL_JUMP`
<a id="insn-007abe3c"></a> `007abe3c` | `00 01 00 b4` | cbz x0,0x007abe5c | `CONDITIONAL_JUMP`
<a id="insn-007abe40"></a> `007abe40` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007abe44"></a> `007abe44` | `03 00 00 14` | b 0x007abe50 | `UNCONDITIONAL_JUMP`
<a id="insn-007abe48"></a> `007abe48` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007abe4c"></a> `007abe4c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007abe50"></a> `007abe50` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007abe54"></a> `007abe54` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007abe58"></a> `007abe58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abe5c"></a> `007abe5c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007abe60"></a> `007abe60` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abe64"></a> `007abe64` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007abe68"></a> `007abe68` | `80 00 00 54` | b.eq 0x007abe78 | `CONDITIONAL_JUMP`
<a id="insn-007abe6c"></a> `007abe6c` | `00 01 00 b4` | cbz x0,0x007abe8c | `CONDITIONAL_JUMP`
<a id="insn-007abe70"></a> `007abe70` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007abe74"></a> `007abe74` | `03 00 00 14` | b 0x007abe80 | `UNCONDITIONAL_JUMP`
<a id="insn-007abe78"></a> `007abe78` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007abe7c"></a> `007abe7c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007abe80"></a> `007abe80` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007abe84"></a> `007abe84` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007abe88"></a> `007abe88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abe8c"></a> `007abe8c` | `f3 a8 ff 97` | bl 0x00796258 | `UNCONDITIONAL_CALL`
<a id="insn-007abe90"></a> `007abe90` | `e9 a3 41 a9` | ldp x9,x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007abe94"></a> `007abe94` | `e9 a3 00 a9` | stp x9,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007abe98"></a> `007abe98` | `c8 00 00 b4` | cbz x8,0x007abeb0 | `CONDITIONAL_JUMP`
<a id="insn-007abe9c"></a> `007abe9c` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-007abea0"></a> `007abea0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007abea4"></a> `007abea4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007abea8"></a> `007abea8` | `ae a3 12 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-007abeac"></a> `007abeac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abeb0"></a> `007abeb0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007abeb4"></a> `007abeb4` | `f7 a8 ff 97` | bl 0x00796290 | `UNCONDITIONAL_CALL`
<a id="insn-007abeb8"></a> `007abeb8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007abebc"></a> `007abebc` | `73 01 00 b4` | cbz x19,0x007abee8 | `CONDITIONAL_JUMP`
<a id="insn-007abec0"></a> `007abec0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007abec4"></a> `007abec4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007abec8"></a> `007abec8` | `b2 a3 12 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-007abecc"></a> `007abecc` | `e0 00 00 b5` | cbnz x0,0x007abee8 | `CONDITIONAL_JUMP`
<a id="insn-007abed0"></a> `007abed0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007abed4"></a> `007abed4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abed8"></a> `007abed8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abedc"></a> `007abedc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abee0"></a> `007abee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abee4"></a> `007abee4` | `0f b4 12 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-007abee8"></a> `007abee8` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007abeec"></a> `007abeec` | `73 01 00 b4` | cbz x19,0x007abf18 | `CONDITIONAL_JUMP`
<a id="insn-007abef0"></a> `007abef0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007abef4"></a> `007abef4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007abef8"></a> `007abef8` | `a6 a3 12 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-007abefc"></a> `007abefc` | `e0 00 00 b5` | cbnz x0,0x007abf18 | `CONDITIONAL_JUMP`
<a id="insn-007abf00"></a> `007abf00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007abf04"></a> `007abf04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abf08"></a> `007abf08` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007abf0c"></a> `007abf0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007abf10"></a> `007abf10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007abf14"></a> `007abf14` | `03 b4 12 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-007abf18"></a> `007abf18` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-007abf1c"></a> `007abf1c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007abf20"></a> `007abf20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007abf24"></a> `007abf24` | `21 0a 00 54` | b.ne 0x007ac068 | `CONDITIONAL_JUMP`
<a id="insn-007abf28"></a> `007abf28` | `f4 4f 4f a9` | ldp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007abf2c"></a> `007abf2c` | `f6 57 4e a9` | ldp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007abf30"></a> `007abf30` | `fd 7b 4d a9` | ldp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007abf34"></a> `007abf34` | `ff 03 04 91` | add sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-007abf38"></a> `007abf38` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ac068"></a> `007ac068` | `c6 b3 12 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007abbbc`](#insn-007abbbc) 範囲 `[['007abbbc', '007abc33']]`
  - `CONDITIONAL_JUMP` [`007abc30`](#insn-007abc30) → [`007abc6c`](#insn-007abc6c)
  - `FALL_THROUGH` [`007abc30`](#insn-007abc30) → [`007abc34`](#insn-007abc34)
- ブロック [`007abc34`](#insn-007abc34) 範囲 `[['007abc34', '007abc4b']]`
  - `CONDITIONAL_JUMP` [`007abc48`](#insn-007abc48) → [`007abc54`](#insn-007abc54)
  - `FALL_THROUGH` [`007abc48`](#insn-007abc48) → [`007abc4c`](#insn-007abc4c)
- ブロック [`007abc4c`](#insn-007abc4c) 範囲 `[['007abc4c', '007abc53']]`
  - `FALL_THROUGH` [`007abc50`](#insn-007abc50) → [`007abc54`](#insn-007abc54)
- ブロック [`007abc54`](#insn-007abc54) 範囲 `[['007abc54', '007abc5b']]`
  - `CONDITIONAL_JUMP` [`007abc58`](#insn-007abc58) → [`007abc64`](#insn-007abc64)
  - `FALL_THROUGH` [`007abc58`](#insn-007abc58) → [`007abc5c`](#insn-007abc5c)
- ブロック [`007abc5c`](#insn-007abc5c) 範囲 `[['007abc5c', '007abc63']]`
  - `FALL_THROUGH` [`007abc60`](#insn-007abc60) → [`007abc64`](#insn-007abc64)
- ブロック [`007abc64`](#insn-007abc64) 範囲 `[['007abc64', '007abc6b']]`
  - `FALL_THROUGH` [`007abc68`](#insn-007abc68) → [`007abc6c`](#insn-007abc6c)
- ブロック [`007abc6c`](#insn-007abc6c) 範囲 `[['007abc6c', '007abc77']]`
  - `CONDITIONAL_JUMP` [`007abc74`](#insn-007abc74) → [`007abc8c`](#insn-007abc8c)
  - `FALL_THROUGH` [`007abc74`](#insn-007abc74) → [`007abc78`](#insn-007abc78)
- ブロック [`007abc78`](#insn-007abc78) 範囲 `[['007abc78', '007abc7f']]`
  - `CONDITIONAL_JUMP` [`007abc7c`](#insn-007abc7c) → [`007abc94`](#insn-007abc94)
  - `FALL_THROUGH` [`007abc7c`](#insn-007abc7c) → [`007abc80`](#insn-007abc80)
- ブロック [`007abc80`](#insn-007abc80) 範囲 `[['007abc80', '007abc8b']]`
  - `FALL_THROUGH` [`007abc88`](#insn-007abc88) → [`007abc8c`](#insn-007abc8c)
- ブロック [`007abc8c`](#insn-007abc8c) 範囲 `[['007abc8c', '007abc93']]`
  - `UNCONDITIONAL_JUMP` [`007abc90`](#insn-007abc90) → [`007abcb0`](#insn-007abcb0)
- ブロック [`007abc94`](#insn-007abc94) 範囲 `[['007abc94', '007abcaf']]`
  - `FALL_THROUGH` [`007abcac`](#insn-007abcac) → [`007abcb0`](#insn-007abcb0)
- ブロック [`007abcb0`](#insn-007abcb0) 範囲 `[['007abcb0', '007abcd7']]`
  - `CONDITIONAL_JUMP` [`007abcd4`](#insn-007abcd4) → [`007abcf0`](#insn-007abcf0)
  - `FALL_THROUGH` [`007abcd4`](#insn-007abcd4) → [`007abcd8`](#insn-007abcd8)
- ブロック [`007abcd8`](#insn-007abcd8) 範囲 `[['007abcd8', '007abce3']]`
  - `CONDITIONAL_JUMP` [`007abce0`](#insn-007abce0) → [`007abcf8`](#insn-007abcf8)
  - `FALL_THROUGH` [`007abce0`](#insn-007abce0) → [`007abce4`](#insn-007abce4)
- ブロック [`007abce4`](#insn-007abce4) 範囲 `[['007abce4', '007abcef']]`
  - `FALL_THROUGH` [`007abcec`](#insn-007abcec) → [`007abcf0`](#insn-007abcf0)
- ブロック [`007abcf0`](#insn-007abcf0) 範囲 `[['007abcf0', '007abcf7']]`
  - `UNCONDITIONAL_JUMP` [`007abcf4`](#insn-007abcf4) → [`007abd0c`](#insn-007abd0c)
- ブロック [`007abcf8`](#insn-007abcf8) 範囲 `[['007abcf8', '007abd0b']]`
  - `FALL_THROUGH` [`007abd08`](#insn-007abd08) → [`007abd0c`](#insn-007abd0c)
- ブロック [`007abd0c`](#insn-007abd0c) 範囲 `[['007abd0c', '007abd2b']]`
  - `CONDITIONAL_JUMP` [`007abd28`](#insn-007abd28) → [`007abd38`](#insn-007abd38)
  - `FALL_THROUGH` [`007abd28`](#insn-007abd28) → [`007abd2c`](#insn-007abd2c)
- ブロック [`007abd2c`](#insn-007abd2c) 範囲 `[['007abd2c', '007abd2f']]`
  - `CONDITIONAL_JUMP` [`007abd2c`](#insn-007abd2c) → [`007abd4c`](#insn-007abd4c)
  - `FALL_THROUGH` [`007abd2c`](#insn-007abd2c) → [`007abd30`](#insn-007abd30)
- ブロック [`007abd30`](#insn-007abd30) 範囲 `[['007abd30', '007abd37']]`
  - `UNCONDITIONAL_JUMP` [`007abd34`](#insn-007abd34) → [`007abd40`](#insn-007abd40)
- ブロック [`007abd38`](#insn-007abd38) 範囲 `[['007abd38', '007abd3f']]`
  - `FALL_THROUGH` [`007abd3c`](#insn-007abd3c) → [`007abd40`](#insn-007abd40)
- ブロック [`007abd40`](#insn-007abd40) 範囲 `[['007abd40', '007abd47']]`
  - `FALL_THROUGH` [`007abd44`](#insn-007abd44) → [`007abd48`](#insn-007abd48)
- ブロック [`007abd48`](#insn-007abd48) 範囲 `[['007abd48', '007abd4b']]`
  - `FALL_THROUGH` [`007abd48`](#insn-007abd48) → [`007abd4c`](#insn-007abd4c)
- ブロック [`007abd4c`](#insn-007abd4c) 範囲 `[['007abd4c', '007abd5b']]`
  - `CONDITIONAL_JUMP` [`007abd58`](#insn-007abd58) → [`007abd68`](#insn-007abd68)
  - `FALL_THROUGH` [`007abd58`](#insn-007abd58) → [`007abd5c`](#insn-007abd5c)
- ブロック [`007abd5c`](#insn-007abd5c) 範囲 `[['007abd5c', '007abd5f']]`
  - `CONDITIONAL_JUMP` [`007abd5c`](#insn-007abd5c) → [`007abd7c`](#insn-007abd7c)
  - `FALL_THROUGH` [`007abd5c`](#insn-007abd5c) → [`007abd60`](#insn-007abd60)
- ブロック [`007abd60`](#insn-007abd60) 範囲 `[['007abd60', '007abd67']]`
  - `UNCONDITIONAL_JUMP` [`007abd64`](#insn-007abd64) → [`007abd70`](#insn-007abd70)
- ブロック [`007abd68`](#insn-007abd68) 範囲 `[['007abd68', '007abd6b']]`
  - `FALL_THROUGH` [`007abd68`](#insn-007abd68) → [`007abd6c`](#insn-007abd6c)
- ブロック [`007abd6c`](#insn-007abd6c) 範囲 `[['007abd6c', '007abd6f']]`
  - `FALL_THROUGH` [`007abd6c`](#insn-007abd6c) → [`007abd70`](#insn-007abd70)
- ブロック [`007abd70`](#insn-007abd70) 範囲 `[['007abd70', '007abd7b']]`
  - `FALL_THROUGH` [`007abd78`](#insn-007abd78) → [`007abd7c`](#insn-007abd7c)
- ブロック [`007abd7c`](#insn-007abd7c) 範囲 `[['007abd7c', '007abd87']]`
  - `CONDITIONAL_JUMP` [`007abd84`](#insn-007abd84) → [`007abd9c`](#insn-007abd9c)
  - `FALL_THROUGH` [`007abd84`](#insn-007abd84) → [`007abd88`](#insn-007abd88)
- ブロック [`007abd88`](#insn-007abd88) 範囲 `[['007abd88', '007abd8f']]`
  - `CONDITIONAL_JUMP` [`007abd8c`](#insn-007abd8c) → [`007abda4`](#insn-007abda4)
  - `FALL_THROUGH` [`007abd8c`](#insn-007abd8c) → [`007abd90`](#insn-007abd90)
- ブロック [`007abd90`](#insn-007abd90) 範囲 `[['007abd90', '007abd9b']]`
  - `FALL_THROUGH` [`007abd98`](#insn-007abd98) → [`007abd9c`](#insn-007abd9c)
- ブロック [`007abd9c`](#insn-007abd9c) 範囲 `[['007abd9c', '007abda3']]`
  - `UNCONDITIONAL_JUMP` [`007abda0`](#insn-007abda0) → [`007abdc0`](#insn-007abdc0)
- ブロック [`007abda4`](#insn-007abda4) 範囲 `[['007abda4', '007abdbf']]`
  - `FALL_THROUGH` [`007abdbc`](#insn-007abdbc) → [`007abdc0`](#insn-007abdc0)
- ブロック [`007abdc0`](#insn-007abdc0) 範囲 `[['007abdc0', '007abdc3']]`
  - `FALL_THROUGH` [`007abdc0`](#insn-007abdc0) → [`007abdc4`](#insn-007abdc4)
- ブロック [`007abdc4`](#insn-007abdc4) 範囲 `[['007abdc4', '007abdd7']]`
  - `FALL_THROUGH` [`007abdd4`](#insn-007abdd4) → [`007abdd8`](#insn-007abdd8)
- ブロック [`007abdd8`](#insn-007abdd8) 範囲 `[['007abdd8', '007abde3']]`
  - `FALL_THROUGH` [`007abde0`](#insn-007abde0) → [`007abde4`](#insn-007abde4)
- ブロック [`007abde4`](#insn-007abde4) 範囲 `[['007abde4', '007abde7']]`
  - `CONDITIONAL_JUMP` [`007abde4`](#insn-007abde4) → [`007abe00`](#insn-007abe00)
  - `FALL_THROUGH` [`007abde4`](#insn-007abde4) → [`007abde8`](#insn-007abde8)
- ブロック [`007abde8`](#insn-007abde8) 範囲 `[['007abde8', '007abdf3']]`
  - `CONDITIONAL_JUMP` [`007abdf0`](#insn-007abdf0) → [`007abe08`](#insn-007abe08)
  - `FALL_THROUGH` [`007abdf0`](#insn-007abdf0) → [`007abdf4`](#insn-007abdf4)
- ブロック [`007abdf4`](#insn-007abdf4) 範囲 `[['007abdf4', '007abdff']]`
  - `FALL_THROUGH` [`007abdfc`](#insn-007abdfc) → [`007abe00`](#insn-007abe00)
- ブロック [`007abe00`](#insn-007abe00) 範囲 `[['007abe00', '007abe07']]`
  - `UNCONDITIONAL_JUMP` [`007abe04`](#insn-007abe04) → [`007abe1c`](#insn-007abe1c)
- ブロック [`007abe08`](#insn-007abe08) 範囲 `[['007abe08', '007abe1b']]`
  - `FALL_THROUGH` [`007abe18`](#insn-007abe18) → [`007abe1c`](#insn-007abe1c)
- ブロック [`007abe1c`](#insn-007abe1c) 範囲 `[['007abe1c', '007abe3b']]`
  - `CONDITIONAL_JUMP` [`007abe38`](#insn-007abe38) → [`007abe48`](#insn-007abe48)
  - `FALL_THROUGH` [`007abe38`](#insn-007abe38) → [`007abe3c`](#insn-007abe3c)
- ブロック [`007abe3c`](#insn-007abe3c) 範囲 `[['007abe3c', '007abe3f']]`
  - `CONDITIONAL_JUMP` [`007abe3c`](#insn-007abe3c) → [`007abe5c`](#insn-007abe5c)
  - `FALL_THROUGH` [`007abe3c`](#insn-007abe3c) → [`007abe40`](#insn-007abe40)
- ブロック [`007abe40`](#insn-007abe40) 範囲 `[['007abe40', '007abe43']]`
  - `FALL_THROUGH` [`007abe40`](#insn-007abe40) → [`007abe44`](#insn-007abe44)
- ブロック [`007abe44`](#insn-007abe44) 範囲 `[['007abe44', '007abe47']]`
  - `UNCONDITIONAL_JUMP` [`007abe44`](#insn-007abe44) → [`007abe50`](#insn-007abe50)
- ブロック [`007abe48`](#insn-007abe48) 範囲 `[['007abe48', '007abe4f']]`
  - `FALL_THROUGH` [`007abe4c`](#insn-007abe4c) → [`007abe50`](#insn-007abe50)
- ブロック [`007abe50`](#insn-007abe50) 範囲 `[['007abe50', '007abe57']]`
  - `FALL_THROUGH` [`007abe54`](#insn-007abe54) → [`007abe58`](#insn-007abe58)
- ブロック [`007abe58`](#insn-007abe58) 範囲 `[['007abe58', '007abe5b']]`
  - `FALL_THROUGH` [`007abe58`](#insn-007abe58) → [`007abe5c`](#insn-007abe5c)
- ブロック [`007abe5c`](#insn-007abe5c) 範囲 `[['007abe5c', '007abe63']]`
  - `FALL_THROUGH` [`007abe60`](#insn-007abe60) → [`007abe64`](#insn-007abe64)
- ブロック [`007abe64`](#insn-007abe64) 範囲 `[['007abe64', '007abe6b']]`
  - `CONDITIONAL_JUMP` [`007abe68`](#insn-007abe68) → [`007abe78`](#insn-007abe78)
  - `FALL_THROUGH` [`007abe68`](#insn-007abe68) → [`007abe6c`](#insn-007abe6c)
- ブロック [`007abe6c`](#insn-007abe6c) 範囲 `[['007abe6c', '007abe6f']]`
  - `CONDITIONAL_JUMP` [`007abe6c`](#insn-007abe6c) → [`007abe8c`](#insn-007abe8c)
  - `FALL_THROUGH` [`007abe6c`](#insn-007abe6c) → [`007abe70`](#insn-007abe70)
- ブロック [`007abe70`](#insn-007abe70) 範囲 `[['007abe70', '007abe77']]`
  - `UNCONDITIONAL_JUMP` [`007abe74`](#insn-007abe74) → [`007abe80`](#insn-007abe80)
- ブロック [`007abe78`](#insn-007abe78) 範囲 `[['007abe78', '007abe7f']]`
  - `FALL_THROUGH` [`007abe7c`](#insn-007abe7c) → [`007abe80`](#insn-007abe80)
- ブロック [`007abe80`](#insn-007abe80) 範囲 `[['007abe80', '007abe8b']]`
  - `FALL_THROUGH` [`007abe88`](#insn-007abe88) → [`007abe8c`](#insn-007abe8c)
- ブロック [`007abe8c`](#insn-007abe8c) 範囲 `[['007abe8c', '007abe9b']]`
  - `CONDITIONAL_JUMP` [`007abe98`](#insn-007abe98) → [`007abeb0`](#insn-007abeb0)
  - `FALL_THROUGH` [`007abe98`](#insn-007abe98) → [`007abe9c`](#insn-007abe9c)
- ブロック [`007abe9c`](#insn-007abe9c) 範囲 `[['007abe9c', '007abeaf']]`
  - `FALL_THROUGH` [`007abeac`](#insn-007abeac) → [`007abeb0`](#insn-007abeb0)
- ブロック [`007abeb0`](#insn-007abeb0) 範囲 `[['007abeb0', '007abebf']]`
  - `CONDITIONAL_JUMP` [`007abebc`](#insn-007abebc) → [`007abee8`](#insn-007abee8)
  - `FALL_THROUGH` [`007abebc`](#insn-007abebc) → [`007abec0`](#insn-007abec0)
- ブロック [`007abec0`](#insn-007abec0) 範囲 `[['007abec0', '007abecf']]`
  - `CONDITIONAL_JUMP` [`007abecc`](#insn-007abecc) → [`007abee8`](#insn-007abee8)
  - `FALL_THROUGH` [`007abecc`](#insn-007abecc) → [`007abed0`](#insn-007abed0)
- ブロック [`007abed0`](#insn-007abed0) 範囲 `[['007abed0', '007abee7']]`
  - `FALL_THROUGH` [`007abee4`](#insn-007abee4) → [`007abee8`](#insn-007abee8)
- ブロック [`007abee8`](#insn-007abee8) 範囲 `[['007abee8', '007abeef']]`
  - `CONDITIONAL_JUMP` [`007abeec`](#insn-007abeec) → [`007abf18`](#insn-007abf18)
  - `FALL_THROUGH` [`007abeec`](#insn-007abeec) → [`007abef0`](#insn-007abef0)
- ブロック [`007abef0`](#insn-007abef0) 範囲 `[['007abef0', '007abeff']]`
  - `CONDITIONAL_JUMP` [`007abefc`](#insn-007abefc) → [`007abf18`](#insn-007abf18)
  - `FALL_THROUGH` [`007abefc`](#insn-007abefc) → [`007abf00`](#insn-007abf00)
- ブロック [`007abf00`](#insn-007abf00) 範囲 `[['007abf00', '007abf17']]`
  - `FALL_THROUGH` [`007abf14`](#insn-007abf14) → [`007abf18`](#insn-007abf18)
- ブロック [`007abf18`](#insn-007abf18) 範囲 `[['007abf18', '007abf27']]`
  - `CONDITIONAL_JUMP` [`007abf24`](#insn-007abf24) → [`007ac068`](#insn-007ac068)
  - `FALL_THROUGH` [`007abf24`](#insn-007abf24) → [`007abf28`](#insn-007abf28)
- ブロック [`007abf28`](#insn-007abf28) 範囲 `[['007abf28', '007abf3b']]`
- ブロック [`007ac068`](#insn-007ac068) 範囲 `[['007ac068', '007ac06b']]`

## 命令位置別の参照

- [`007abbc0`](#insn-007abbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abbc4`](#insn-007abbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abbc8`](#insn-007abbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abbe4`](#insn-007abbe4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abbe8`](#insn-007abbe8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`007abc00`](#insn-007abc00) → [`0059bc68`](../0059b/0059bc68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0059bc68` · 推定シンボル `None` · 推定型 `None`
- [`007abc0c`](#insn-007abc0c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc14`](#insn-007abc14) → `00c6fd38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abc24`](#insn-007abc24) → [`007afbac`](../007af/007afbac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007afbac` · 推定シンボル `None` · 推定型 `None`
- [`007abc28`](#insn-007abc28) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc2c`](#insn-007abc2c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc30`](#insn-007abc30) → [`007abc6c`](#insn-007abc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc44`](#insn-007abc44) → `00c6eac0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abc48`](#insn-007abc48) → [`007abc54`](#insn-007abc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc50`](#insn-007abc50) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007abc58`](#insn-007abc58) → [`007abc64`](#insn-007abc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc60`](#insn-007abc60) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007abc68`](#insn-007abc68) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007abc70`](#insn-007abc70) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc74`](#insn-007abc74) → [`007abc8c`](#insn-007abc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc7c`](#insn-007abc7c) → [`007abc94`](#insn-007abc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc8c`](#insn-007abc8c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc90`](#insn-007abc90) → [`007abcb0`](#insn-007abcb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abc9c`](#insn-007abc9c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abcb0`](#insn-007abcb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abcb8`](#insn-007abcb8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`007abcc0`](#insn-007abcc0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abcd0`](#insn-007abcd0) → `00c7b938`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abcd4`](#insn-007abcd4) → [`007abcf0`](#insn-007abcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abce0`](#insn-007abce0) → [`007abcf8`](#insn-007abcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abcf4`](#insn-007abcf4) → [`007abd0c`](#insn-007abd0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abcf8`](#insn-007abcf8) → `Stack[-0xa0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd0c`](#insn-007abd0c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd1c`](#insn-007abd1c) → [`00598e94`](../00598/00598e94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00598e94` · 推定シンボル `None` · 推定型 `None`
- [`007abd20`](#insn-007abd20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd28`](#insn-007abd28) → [`007abd38`](#insn-007abd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd2c`](#insn-007abd2c) → [`007abd4c`](#insn-007abd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd34`](#insn-007abd34) → [`007abd40`](#insn-007abd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd40`](#insn-007abd40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd44`](#insn-007abd44) → `00c7b960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abd48`](#insn-007abd48) → [`007afef8`](../007af/007afef8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `007afef8` · 推定シンボル `None` · 推定型 `None`
- [`007abd4c`](#insn-007abd4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd58`](#insn-007abd58) → [`007abd68`](#insn-007abd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd5c`](#insn-007abd5c) → [`007abd7c`](#insn-007abd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd64`](#insn-007abd64) → [`007abd70`](#insn-007abd70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd70`](#insn-007abd70) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd80`](#insn-007abd80) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd84`](#insn-007abd84) → [`007abd9c`](#insn-007abd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd8c`](#insn-007abd8c) → [`007abda4`](#insn-007abda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abd9c`](#insn-007abd9c) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abda0`](#insn-007abda0) → [`007abdc0`](#insn-007abdc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abdac`](#insn-007abdac) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abdc0`](#insn-007abdc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abdc8`](#insn-007abdc8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`007abdd0`](#insn-007abdd0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abde0`](#insn-007abde0) → `00c7b9b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abde4`](#insn-007abde4) → [`007abe00`](#insn-007abe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abdf0`](#insn-007abdf0) → [`007abe08`](#insn-007abe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe04`](#insn-007abe04) → [`007abe1c`](#insn-007abe1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe08`](#insn-007abe08) → `Stack[-0xd0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe1c`](#insn-007abe1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe2c`](#insn-007abe2c) → [`00599054`](../00599/00599054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00599054` · 推定シンボル `None` · 推定型 `None`
- [`007abe30`](#insn-007abe30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe38`](#insn-007abe38) → [`007abe48`](#insn-007abe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe3c`](#insn-007abe3c) → [`007abe5c`](#insn-007abe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe44`](#insn-007abe44) → [`007abe50`](#insn-007abe50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe50`](#insn-007abe50) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe54`](#insn-007abe54) → `00c7b9e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007abe58`](#insn-007abe58) → [`007b027c`](../007b0/007b027c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `007b027c` · 推定シンボル `None` · 推定型 `None`
- [`007abe5c`](#insn-007abe5c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe68`](#insn-007abe68) → [`007abe78`](#insn-007abe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe6c`](#insn-007abe6c) → [`007abe8c`](#insn-007abe8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe74`](#insn-007abe74) → [`007abe80`](#insn-007abe80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe80`](#insn-007abe80) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe8c`](#insn-007abe8c) → [`00796258`](../00796/00796258.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00796258` · 推定シンボル `None` · 推定型 `None`
- [`007abe90`](#insn-007abe90) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe94`](#insn-007abe94) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abe98`](#insn-007abe98) → [`007abeb0`](#insn-007abeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abea8`](#insn-007abea8) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`007abeb4`](#insn-007abeb4) → [`00796290`](../00796/00796290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00796290` · 推定シンボル `None` · 推定型 `None`
- [`007abeb8`](#insn-007abeb8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abebc`](#insn-007abebc) → [`007abee8`](#insn-007abee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abec8`](#insn-007abec8) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`007abecc`](#insn-007abecc) → [`007abee8`](#insn-007abee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abee4`](#insn-007abee4) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`007abee8`](#insn-007abee8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abeec`](#insn-007abeec) → [`007abf18`](#insn-007abf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abef8`](#insn-007abef8) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`007abefc`](#insn-007abefc) → [`007abf18`](#insn-007abf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abf14`](#insn-007abf14) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`007abf1c`](#insn-007abf1c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abf24`](#insn-007abf24) → [`007ac068`](#insn-007ac068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abf28`](#insn-007abf28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abf2c`](#insn-007abf2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007abf30`](#insn-007abf30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ac068`](#insn-007ac068) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007abbc0`](#insn-007abbc0)

~~~json
{
  "source": "007abbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abbc4`](#insn-007abbc4)

~~~json
{
  "source": "007abbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abbc8`](#insn-007abbc8)

~~~json
{
  "source": "007abbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abbe4`](#insn-007abbe4)

~~~json
{
  "source": "007abbe4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abbe8`](#insn-007abbe8)

~~~json
{
  "source": "007abbe8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc00`](#insn-007abc00)

~~~json
{
  "source": "007abc00",
  "target": "0059bc68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc0c`](#insn-007abc0c)

~~~json
{
  "source": "007abc0c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc14`](#insn-007abc14)

~~~json
{
  "source": "007abc14",
  "target": "00c6fd38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6fd38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abc24`](#insn-007abc24)

~~~json
{
  "source": "007abc24",
  "target": "007afbac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc28`](#insn-007abc28)

~~~json
{
  "source": "007abc28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc2c`](#insn-007abc2c)

~~~json
{
  "source": "007abc2c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc30`](#insn-007abc30)

~~~json
{
  "source": "007abc30",
  "target": "007abc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc44`](#insn-007abc44)

~~~json
{
  "source": "007abc44",
  "target": "00c6eac0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6eac0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abc48`](#insn-007abc48)

~~~json
{
  "source": "007abc48",
  "target": "007abc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc50`](#insn-007abc50)

~~~json
{
  "source": "007abc50",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc58`](#insn-007abc58)

~~~json
{
  "source": "007abc58",
  "target": "007abc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc60`](#insn-007abc60)

~~~json
{
  "source": "007abc60",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc68`](#insn-007abc68)

~~~json
{
  "source": "007abc68",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abc70`](#insn-007abc70)

~~~json
{
  "source": "007abc70",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc74`](#insn-007abc74)

~~~json
{
  "source": "007abc74",
  "target": "007abc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc7c`](#insn-007abc7c)

~~~json
{
  "source": "007abc7c",
  "target": "007abc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc8c`](#insn-007abc8c)

~~~json
{
  "source": "007abc8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc90`](#insn-007abc90)

~~~json
{
  "source": "007abc90",
  "target": "007abcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abc9c`](#insn-007abc9c)

~~~json
{
  "source": "007abc9c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abcb0`](#insn-007abcb0)

~~~json
{
  "source": "007abcb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abcb8`](#insn-007abcb8)

~~~json
{
  "source": "007abcb8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abcc0`](#insn-007abcc0)

~~~json
{
  "source": "007abcc0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abcd0`](#insn-007abcd0)

~~~json
{
  "source": "007abcd0",
  "target": "00c7b938",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7b938",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abcd4`](#insn-007abcd4)

~~~json
{
  "source": "007abcd4",
  "target": "007abcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abce0`](#insn-007abce0)

~~~json
{
  "source": "007abce0",
  "target": "007abcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abcf4`](#insn-007abcf4)

~~~json
{
  "source": "007abcf4",
  "target": "007abd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abcf8`](#insn-007abcf8)

~~~json
{
  "source": "007abcf8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd0c`](#insn-007abd0c)

~~~json
{
  "source": "007abd0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd1c`](#insn-007abd1c)

~~~json
{
  "source": "007abd1c",
  "target": "00598e94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abd20`](#insn-007abd20)

~~~json
{
  "source": "007abd20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd28`](#insn-007abd28)

~~~json
{
  "source": "007abd28",
  "target": "007abd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd2c`](#insn-007abd2c)

~~~json
{
  "source": "007abd2c",
  "target": "007abd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd34`](#insn-007abd34)

~~~json
{
  "source": "007abd34",
  "target": "007abd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd40`](#insn-007abd40)

~~~json
{
  "source": "007abd40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd44`](#insn-007abd44)

~~~json
{
  "source": "007abd44",
  "target": "00c7b960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7b960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abd48`](#insn-007abd48)

~~~json
{
  "source": "007abd48",
  "target": "007afef8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abd4c`](#insn-007abd4c)

~~~json
{
  "source": "007abd4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd58`](#insn-007abd58)

~~~json
{
  "source": "007abd58",
  "target": "007abd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd5c`](#insn-007abd5c)

~~~json
{
  "source": "007abd5c",
  "target": "007abd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd64`](#insn-007abd64)

~~~json
{
  "source": "007abd64",
  "target": "007abd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd70`](#insn-007abd70)

~~~json
{
  "source": "007abd70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd80`](#insn-007abd80)

~~~json
{
  "source": "007abd80",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd84`](#insn-007abd84)

~~~json
{
  "source": "007abd84",
  "target": "007abd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd8c`](#insn-007abd8c)

~~~json
{
  "source": "007abd8c",
  "target": "007abda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abd9c`](#insn-007abd9c)

~~~json
{
  "source": "007abd9c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abda0`](#insn-007abda0)

~~~json
{
  "source": "007abda0",
  "target": "007abdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abdac`](#insn-007abdac)

~~~json
{
  "source": "007abdac",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abdc0`](#insn-007abdc0)

~~~json
{
  "source": "007abdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abdc8`](#insn-007abdc8)

~~~json
{
  "source": "007abdc8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abdd0`](#insn-007abdd0)

~~~json
{
  "source": "007abdd0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abde0`](#insn-007abde0)

~~~json
{
  "source": "007abde0",
  "target": "00c7b9b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7b9b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abde4`](#insn-007abde4)

~~~json
{
  "source": "007abde4",
  "target": "007abe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abdf0`](#insn-007abdf0)

~~~json
{
  "source": "007abdf0",
  "target": "007abe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe04`](#insn-007abe04)

~~~json
{
  "source": "007abe04",
  "target": "007abe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe08`](#insn-007abe08)

~~~json
{
  "source": "007abe08",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe1c`](#insn-007abe1c)

~~~json
{
  "source": "007abe1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe2c`](#insn-007abe2c)

~~~json
{
  "source": "007abe2c",
  "target": "00599054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abe30`](#insn-007abe30)

~~~json
{
  "source": "007abe30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe38`](#insn-007abe38)

~~~json
{
  "source": "007abe38",
  "target": "007abe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe3c`](#insn-007abe3c)

~~~json
{
  "source": "007abe3c",
  "target": "007abe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe44`](#insn-007abe44)

~~~json
{
  "source": "007abe44",
  "target": "007abe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe50`](#insn-007abe50)

~~~json
{
  "source": "007abe50",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe54`](#insn-007abe54)

~~~json
{
  "source": "007abe54",
  "target": "00c7b9e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7b9e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007abe58`](#insn-007abe58)

~~~json
{
  "source": "007abe58",
  "target": "007b027c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abe5c`](#insn-007abe5c)

~~~json
{
  "source": "007abe5c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe68`](#insn-007abe68)

~~~json
{
  "source": "007abe68",
  "target": "007abe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe6c`](#insn-007abe6c)

~~~json
{
  "source": "007abe6c",
  "target": "007abe8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe74`](#insn-007abe74)

~~~json
{
  "source": "007abe74",
  "target": "007abe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe80`](#insn-007abe80)

~~~json
{
  "source": "007abe80",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe8c`](#insn-007abe8c)

~~~json
{
  "source": "007abe8c",
  "target": "00796258",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abe90`](#insn-007abe90)

~~~json
{
  "source": "007abe90",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe94`](#insn-007abe94)

~~~json
{
  "source": "007abe94",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abe98`](#insn-007abe98)

~~~json
{
  "source": "007abe98",
  "target": "007abeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abea8`](#insn-007abea8)

~~~json
{
  "source": "007abea8",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abeb4`](#insn-007abeb4)

~~~json
{
  "source": "007abeb4",
  "target": "00796290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abeb8`](#insn-007abeb8)

~~~json
{
  "source": "007abeb8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abebc`](#insn-007abebc)

~~~json
{
  "source": "007abebc",
  "target": "007abee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abec8`](#insn-007abec8)

~~~json
{
  "source": "007abec8",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abecc`](#insn-007abecc)

~~~json
{
  "source": "007abecc",
  "target": "007abee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abee4`](#insn-007abee4)

~~~json
{
  "source": "007abee4",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abee8`](#insn-007abee8)

~~~json
{
  "source": "007abee8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abeec`](#insn-007abeec)

~~~json
{
  "source": "007abeec",
  "target": "007abf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abef8`](#insn-007abef8)

~~~json
{
  "source": "007abef8",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abefc`](#insn-007abefc)

~~~json
{
  "source": "007abefc",
  "target": "007abf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abf14`](#insn-007abf14)

~~~json
{
  "source": "007abf14",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007abf1c`](#insn-007abf1c)

~~~json
{
  "source": "007abf1c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abf24`](#insn-007abf24)

~~~json
{
  "source": "007abf24",
  "target": "007ac068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abf28`](#insn-007abf28)

~~~json
{
  "source": "007abf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abf2c`](#insn-007abf2c)

~~~json
{
  "source": "007abf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007abf30`](#insn-007abf30)

~~~json
{
  "source": "007abf30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ac068`](#insn-007ac068)

~~~json
{
  "source": "007ac068",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
