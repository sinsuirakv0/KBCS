# 007adedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0128.md#review-507ce93bf8a52f355100d260cd8de12b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007adf1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0038.md#compare-9653b011fdc3d6859095c4bbb7b0af5e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007adedc",
  "name": "FUN_007adedc",
  "size": 960,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08afd7b3bc3f89ea555783d7e6c8924f315d95a26312006d197caf3f65840b4a",
  "source_text_sha256": "08afd7b3bc3f89ea555783d7e6c8924f315d95a26312006d197caf3f65840b4a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007adedc",
        "007ae297"
      ],
      [
        "007ae3cc",
        "007ae3cf"
      ]
    ],
    "bytes_sha256": "be73272b4f68808c68a9effdcd1588628622a4b8e26f1a83999c551be5089607",
    "instruction_count": 240,
    "instruction_bytes": 960,
    "body_bytes": 960,
    "indirect": 14,
    "unresolved": 12
  }
}
~~~

## 呼び出し元

- [007add18](../007ad/007add18.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00598af4](../00598/00598af4.md)
- [00598cb4](../00598/00598cb4.md)
- [005a4fd8](../005a4/005a4fd8.md)
- [00795de4](../00795/00795de4.md)
- [00795e1c](../00795/00795e1c.md)
- [007afefc](../007af/007afefc.md)
- [007b0248](../007b0/007b0248.md)
- [007b04b4](../007b0/007b04b4.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"t{"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5598 bytes

~~~c

void FUN_007adedc(undefined8 param_1,ulong *param_2,long *param_3,long *param_4)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  ulong *puVar4;
  ulong uVar5;
  undefined8 uVar6;
  long lVar7;
  undefined8 local_108;
  long *local_100;
  undefined8 *local_f8;
  undefined8 local_f0;
  long *local_e8;
  long local_e0 [4];
  long *local_c0;
  long local_b0 [4];
  long *local_90;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong *local_60;
  long local_48;
  
                    /* catch() { ... } // from try @ 007ae07c with catch @ 007adef0
                       catch() { ... } // from try @ 007ae9b0 with catch @ 007adef0
                       catch() { ... } // from try @ 007aec04 with catch @ 007adef0 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)_Znwm(0x50);
  if ((*param_2 & 1) == 0) {
    uStack_78 = param_2[1];
    local_80 = *param_2;
    local_70 = (void *)param_2[2];
  }
  else {
    FUN_0043bae0(&local_80,param_2[2],param_2[1]);
  }
  FUN_005a4fd8(puVar2,&local_80);
  local_f8 = puVar2;
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  FUN_007afefc(&local_f0,&local_80,&local_f8);
  puVar2 = local_f8;
  local_f8 = (undefined8 *)0x0;
  if (puVar2 != (undefined8 *)0x0) {
    if ((*(byte *)(puVar2 + 7) & 1) != 0) {
      _ZdlPv((void *)puVar2[9]);
    }
                    /* try { // try from 007adf8c to 008adf93 has its CatchHandler @ 007aef4c */
                    /* try { // try from 007adf94 to 008adf9f has its CatchHandler @ 007aef34 */
    *puVar2 = &PTR_FUN_00c6d620;
    if ((*(byte *)(puVar2 + 4) & 1) != 0) {
                    /* try { // try from 007adfa4 to 008adfab has its CatchHandler @ 007aef24 */
      _ZdlPv((void *)puVar2[6]);
    }
    if ((*(byte *)(puVar2 + 1) & 1) != 0) {
      _ZdlPv((void *)puVar2[3]);
    }
    _ZdlPv(puVar2);
  }
  uVar6 = local_f0;
  plVar3 = (long *)param_3[4];
  local_90 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_3) {
      local_90 = local_b0;
      (**(code **)(*param_3 + 0x18))(param_3,local_b0);
    }
    else {
      local_90 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_60 = (ulong *)0x0;
                    /* try { // try from 007ae00c to 008ae017 has its CatchHandler @ 007aeeb0 */
  puVar4 = (ulong *)_Znwm(0x40);
  *puVar4 = (ulong)&PTR_FUN_00c7a698;
  uVar5 = 0;
  if (local_90 == (long *)0x0) {
LAB_007ae048:
    puVar4[6] = uVar5;
  }
  else {
    if (local_90 != local_b0) {
      uVar5 = (**(code **)(*local_90 + 0x10))();
      goto LAB_007ae048;
    }
    puVar4[6] = (ulong)(puVar4 + 2);
                    /* try { // try from 007ae058 to 008ae06b has its CatchHandler @ 007aee84 */
    (**(code **)(local_b0[0] + 0x18))(local_b0);
  }
                    /* try { // try from 007ae06c to 008ae07b has its CatchHandler @ 007aee70 */
  local_60 = puVar4;
  FUN_00598af4(uVar6,&local_80);
                    /* try { // try from 007ae07c to 008ae277 has its CatchHandler @ 007adef0 */
  if (local_60 == &local_80) {
    lVar7 = 0x20;
    puVar4 = &local_80;
LAB_007ae098:
    (**(code **)(*puVar4 + lVar7))();
  }
  else if (local_60 != (ulong *)0x0) {
    lVar7 = 0x28;
    puVar4 = local_60;
    goto LAB_007ae098;
  }
  if (local_90 == local_b0) {
    lVar7 = 0x20;
    plVar3 = local_b0;
LAB_007ae0c8:
    (**(code **)(*plVar3 + lVar7))();
  }
  else if (local_90 != (long *)0x0) {
    lVar7 = 0x28;
    plVar3 = local_90;
    goto LAB_007ae0c8;
  }
  uVar6 = local_f0;
  plVar3 = (long *)param_4[4];
  local_c0 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_4) {
      local_c0 = local_e0;
      (**(code **)(*param_4 + 0x18))(param_4,local_e0);
    }
    else {
      local_c0 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_60 = (ulong *)0x0;
  puVar4 = (ulong *)_Znwm(0x40);
  *puVar4 = (ulong)&PTR_FUN_00c7a718;
  uVar5 = 0;
  if (local_c0 == (long *)0x0) {
LAB_007ae158:
    puVar4[6] = uVar5;
  }
  else {
    if (local_c0 != local_e0) {
      uVar5 = (**(code **)(*local_c0 + 0x10))();
      goto LAB_007ae158;
    }
    puVar4[6] = (ulong)(puVar4 + 2);
    (**(code **)(local_e0[0] + 0x18))(local_e0);
  }
  local_60 = puVar4;
  FUN_00598cb4(uVar6,&local_80);
  if (local_60 == &local_80) {
    lVar7 = 0x20;
    puVar4 = &local_80;
LAB_007ae1a8:
    (**(code **)(*puVar4 + lVar7))();
  }
  else if (local_60 != (ulong *)0x0) {
    lVar7 = 0x28;
    puVar4 = local_60;
    goto LAB_007ae1a8;
  }
  if (local_c0 == local_e0) {
    lVar7 = 0x20;
    plVar3 = local_e0;
  }
  else {
    if (local_c0 == (long *)0x0) goto LAB_007ae1e4;
    lVar7 = 0x28;
    plVar3 = local_c0;
  }
  (**(code **)(*plVar3 + lVar7))();
LAB_007ae1e4:
  uVar6 = FUN_00795de4();
  local_108 = local_f0;
  local_100 = local_e8;
  if (local_e8 != (long *)0x0) {
    FUN_00c538b0(1,local_e8 + 1);
  }
  FUN_00795e1c(uVar6,&local_108);
  plVar3 = local_100;
  if ((local_100 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,local_100 + 1), lVar7 == 0)) {
    (**(code **)(*plVar3 + 0x10))(plVar3);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
  }
  if ((local_e8 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,local_e8 + 1), lVar7 == 0)) {
    (**(code **)(*local_e8 + 0x10))(local_e8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_e8);
  }
                    /* try { // try from 007ae278 to 008ae27b has its CatchHandler @ 007aeff8 */
  if (*(long *)(lVar1 + 0x28) != local_48) {
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
<a id="insn-007adedc"></a> `007adedc` | `ff 43 04 d1` | sub sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-007adee0"></a> `007adee0` | `fd 7b 0d a9` | stp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007adee4"></a> `007adee4` | `f7 73 00 f9` | str x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007adee8"></a> `007adee8` | `f6 57 0f a9` | stp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007adeec"></a> `007adeec` | `f4 4f 10 a9` | stp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007adef0"></a> `007adef0` | `fd 43 03 91` | add x29,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-007adef4"></a> `007adef4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007adef8"></a> `007adef8` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-007adefc"></a> `007adefc` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-007adf00"></a> `007adf00` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-007adf04"></a> `007adf04` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-007adf08"></a> `007adf08` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-007adf0c"></a> `007adf0c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007adf10"></a> `007adf10` | `e0 a6 12 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007adf14"></a> `007adf14` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-007adf18"></a> `007adf18` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007adf1c"></a> `007adf1c` | `c8 00 00 37` | tbnz w8,#0x0,0x007adf34 | `CONDITIONAL_JUMP`
<a id="insn-007adf20"></a> `007adf20` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-007adf24"></a> `007adf24` | `c8 0a 40 f9` | ldr x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-007adf28"></a> `007adf28` | `a0 03 9c 3c` | stur q0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007adf2c"></a> `007adf2c` | `a8 03 1d f8` | stur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007adf30"></a> `007adf30` | `04 00 00 14` | b 0x007adf40 | `UNCONDITIONAL_JUMP`
<a id="insn-007adf34"></a> `007adf34` | `c2 86 40 a9` | ldp x2,x1,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-007adf38"></a> `007adf38` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007adf3c"></a> `007adf3c` | `e9 36 f2 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-007adf40"></a> `007adf40` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007adf44"></a> `007adf44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007adf48"></a> `007adf48` | `24 dc f7 97` | bl 0x005a4fd8 | `UNCONDITIONAL_CALL`
<a id="insn-007adf4c"></a> `007adf4c` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007adf50"></a> `007adf50` | `f5 0f 00 f9` | str x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007adf54"></a> `007adf54` | `68 00 00 36` | tbz w8,#0x0,0x007adf60 | `CONDITIONAL_JUMP`
<a id="insn-007adf58"></a> `007adf58` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007adf5c"></a> `007adf5c` | `d5 a6 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007adf60"></a> `007adf60` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007adf64"></a> `007adf64` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007adf68"></a> `007adf68` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-007adf6c"></a> `007adf6c` | `e4 07 00 94` | bl 0x007afefc | `UNCONDITIONAL_CALL`
<a id="insn-007adf70"></a> `007adf70` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007adf74"></a> `007adf74` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007adf78"></a> `007adf78` | `75 02 00 b4` | cbz x21,0x007adfc4 | `CONDITIONAL_JUMP`
<a id="insn-007adf7c"></a> `007adf7c` | `a8 e2 40 39` | ldrb w8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-007adf80"></a> `007adf80` | `68 00 00 36` | tbz w8,#0x0,0x007adf8c | `CONDITIONAL_JUMP`
<a id="insn-007adf84"></a> `007adf84` | `a0 26 40 f9` | ldr x0,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-007adf88"></a> `007adf88` | `ca a6 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007adf8c"></a> `007adf8c` | `08 26 00 90` | adrp x8,0xc6d000 | `FALL_THROUGH`
<a id="insn-007adf90"></a> `007adf90` | `08 41 18 91` | add x8,x8,#0x610 | `FALL_THROUGH`
<a id="insn-007adf94"></a> `007adf94` | `a9 82 40 39` | ldrb w9,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-007adf98"></a> `007adf98` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-007adf9c"></a> `007adf9c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-007adfa0"></a> `007adfa0` | `69 00 00 36` | tbz w9,#0x0,0x007adfac | `CONDITIONAL_JUMP`
<a id="insn-007adfa4"></a> `007adfa4` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007adfa8"></a> `007adfa8` | `c2 a6 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007adfac"></a> `007adfac` | `a8 22 40 39` | ldrb w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-007adfb0"></a> `007adfb0` | `68 00 00 36` | tbz w8,#0x0,0x007adfbc | `CONDITIONAL_JUMP`
<a id="insn-007adfb4"></a> `007adfb4` | `a0 0e 40 f9` | ldr x0,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-007adfb8"></a> `007adfb8` | `be a6 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007adfbc"></a> `007adfbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007adfc0"></a> `007adfc0` | `bc a6 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007adfc4"></a> `007adfc4` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-007adfc8"></a> `007adfc8` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007adfcc"></a> `007adfcc` | `c0 00 00 b4` | cbz x0,0x007adfe4 | `CONDITIONAL_JUMP`
<a id="insn-007adfd0"></a> `007adfd0` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-007adfd4"></a> `007adfd4` | `c0 00 00 54` | b.eq 0x007adfec | `CONDITIONAL_JUMP`
<a id="insn-007adfd8"></a> `007adfd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007adfdc"></a> `007adfdc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007adfe0"></a> `007adfe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007adfe4"></a> `007adfe4` | `e0 43 00 f9` | str x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007adfe8"></a> `007adfe8` | `08 00 00 14` | b 0x007ae008 | `UNCONDITIONAL_JUMP`
<a id="insn-007adfec"></a> `007adfec` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007adff0"></a> `007adff0` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-007adff4"></a> `007adff4` | `e8 43 00 f9` | str x8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007adff8"></a> `007adff8` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-007adffc"></a> `007adffc` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007ae000"></a> `007ae000` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007ae004"></a> `007ae004` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae008"></a> `007ae008` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae00c"></a> `007ae00c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-007ae010"></a> `007ae010` | `a0 a6 12 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007ae014"></a> `007ae014` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007ae018"></a> `007ae018` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007ae01c"></a> `007ae01c` | `68 26 00 90` | adrp x8,0xc7a000 | `FALL_THROUGH`
<a id="insn-007ae020"></a> `007ae020` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-007ae024"></a> `007ae024` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-007ae028"></a> `007ae028` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007ae02c"></a> `007ae02c` | `e0 00 00 b4` | cbz x0,0x007ae048 | `CONDITIONAL_JUMP`
<a id="insn-007ae030"></a> `007ae030` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007ae034"></a> `007ae034` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007ae038"></a> `007ae038` | `c0 00 00 54` | b.eq 0x007ae050 | `CONDITIONAL_JUMP`
<a id="insn-007ae03c"></a> `007ae03c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007ae040"></a> `007ae040` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ae044"></a> `007ae044` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae048"></a> `007ae048` | `80 1a 00 f9` | str x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-007ae04c"></a> `007ae04c` | `06 00 00 14` | b 0x007ae064 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae050"></a> `007ae050` | `e8 33 40 f9` | ldr x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007ae054"></a> `007ae054` | `81 1a 00 f9` | str x1,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-007ae058"></a> `007ae058` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007ae05c"></a> `007ae05c` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007ae060"></a> `007ae060` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae064"></a> `007ae064` | `b4 03 1e f8` | stur x20,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae068"></a> `007ae068` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae06c"></a> `007ae06c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007ae070"></a> `007ae070` | `b4 03 01 d1` | sub x20,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae074"></a> `007ae074` | `a0 aa f7 97` | bl 0x00598af4 | `UNCONDITIONAL_CALL`
<a id="insn-007ae078"></a> `007ae078` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae07c"></a> `007ae07c` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-007ae080"></a> `007ae080` | `80 00 00 54` | b.eq 0x007ae090 | `CONDITIONAL_JUMP`
<a id="insn-007ae084"></a> `007ae084` | `00 01 00 b4` | cbz x0,0x007ae0a4 | `CONDITIONAL_JUMP`
<a id="insn-007ae088"></a> `007ae088` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007ae08c"></a> `007ae08c` | `03 00 00 14` | b 0x007ae098 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae090"></a> `007ae090` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007ae094"></a> `007ae094` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae098"></a> `007ae098` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007ae09c"></a> `007ae09c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ae0a0"></a> `007ae0a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae0a4"></a> `007ae0a4` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007ae0a8"></a> `007ae0a8` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007ae0ac"></a> `007ae0ac` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007ae0b0"></a> `007ae0b0` | `80 00 00 54` | b.eq 0x007ae0c0 | `CONDITIONAL_JUMP`
<a id="insn-007ae0b4"></a> `007ae0b4` | `00 01 00 b4` | cbz x0,0x007ae0d4 | `CONDITIONAL_JUMP`
<a id="insn-007ae0b8"></a> `007ae0b8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007ae0bc"></a> `007ae0bc` | `03 00 00 14` | b 0x007ae0c8 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae0c0"></a> `007ae0c0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007ae0c4"></a> `007ae0c4` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-007ae0c8"></a> `007ae0c8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007ae0cc"></a> `007ae0cc` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ae0d0"></a> `007ae0d0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae0d4"></a> `007ae0d4` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-007ae0d8"></a> `007ae0d8` | `f4 13 40 f9` | ldr x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ae0dc"></a> `007ae0dc` | `c0 00 00 b4` | cbz x0,0x007ae0f4 | `CONDITIONAL_JUMP`
<a id="insn-007ae0e0"></a> `007ae0e0` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-007ae0e4"></a> `007ae0e4` | `c0 00 00 54` | b.eq 0x007ae0fc | `CONDITIONAL_JUMP`
<a id="insn-007ae0e8"></a> `007ae0e8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007ae0ec"></a> `007ae0ec` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ae0f0"></a> `007ae0f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae0f4"></a> `007ae0f4` | `e0 2b 00 f9` | str x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ae0f8"></a> `007ae0f8` | `08 00 00 14` | b 0x007ae118 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae0fc"></a> `007ae0fc` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae100"></a> `007ae100` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-007ae104"></a> `007ae104` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ae108"></a> `007ae108` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-007ae10c"></a> `007ae10c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae110"></a> `007ae110` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae114"></a> `007ae114` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae118"></a> `007ae118` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae11c"></a> `007ae11c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-007ae120"></a> `007ae120` | `5c a6 12 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007ae124"></a> `007ae124` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007ae128"></a> `007ae128` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ae12c"></a> `007ae12c` | `68 26 00 90` | adrp x8,0xc7a000 | `FALL_THROUGH`
<a id="insn-007ae130"></a> `007ae130` | `08 61 1c 91` | add x8,x8,#0x718 | `FALL_THROUGH`
<a id="insn-007ae134"></a> `007ae134` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007ae138"></a> `007ae138` | `28 04 01 f8` | str x8,[x1], #0x10 | `FALL_THROUGH`
<a id="insn-007ae13c"></a> `007ae13c` | `e0 00 00 b4` | cbz x0,0x007ae158 | `CONDITIONAL_JUMP`
<a id="insn-007ae140"></a> `007ae140` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae144"></a> `007ae144` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007ae148"></a> `007ae148` | `c0 00 00 54` | b.eq 0x007ae160 | `CONDITIONAL_JUMP`
<a id="insn-007ae14c"></a> `007ae14c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007ae150"></a> `007ae150` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ae154"></a> `007ae154` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae158"></a> `007ae158` | `a0 1a 00 f9` | str x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007ae15c"></a> `007ae15c` | `06 00 00 14` | b 0x007ae174 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae160"></a> `007ae160` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007ae164"></a> `007ae164` | `a1 1a 00 f9` | str x1,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-007ae168"></a> `007ae168` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-007ae16c"></a> `007ae16c` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae170"></a> `007ae170` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae174"></a> `007ae174` | `b5 03 1e f8` | stur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae178"></a> `007ae178` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae17c"></a> `007ae17c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-007ae180"></a> `007ae180` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae184"></a> `007ae184` | `cc aa f7 97` | bl 0x00598cb4 | `UNCONDITIONAL_CALL`
<a id="insn-007ae188"></a> `007ae188` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ae18c"></a> `007ae18c` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-007ae190"></a> `007ae190` | `80 00 00 54` | b.eq 0x007ae1a0 | `CONDITIONAL_JUMP`
<a id="insn-007ae194"></a> `007ae194` | `00 01 00 b4` | cbz x0,0x007ae1b4 | `CONDITIONAL_JUMP`
<a id="insn-007ae198"></a> `007ae198` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007ae19c"></a> `007ae19c` | `03 00 00 14` | b 0x007ae1a8 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae1a0"></a> `007ae1a0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007ae1a4"></a> `007ae1a4` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-007ae1a8"></a> `007ae1a8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007ae1ac"></a> `007ae1ac` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ae1b0"></a> `007ae1b0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae1b4"></a> `007ae1b4` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007ae1b8"></a> `007ae1b8` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae1bc"></a> `007ae1bc` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-007ae1c0"></a> `007ae1c0` | `80 00 00 54` | b.eq 0x007ae1d0 | `CONDITIONAL_JUMP`
<a id="insn-007ae1c4"></a> `007ae1c4` | `00 01 00 b4` | cbz x0,0x007ae1e4 | `CONDITIONAL_JUMP`
<a id="insn-007ae1c8"></a> `007ae1c8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-007ae1cc"></a> `007ae1cc` | `03 00 00 14` | b 0x007ae1d8 | `UNCONDITIONAL_JUMP`
<a id="insn-007ae1d0"></a> `007ae1d0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-007ae1d4"></a> `007ae1d4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-007ae1d8"></a> `007ae1d8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007ae1dc"></a> `007ae1dc` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ae1e0"></a> `007ae1e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae1e4"></a> `007ae1e4` | `00 9f ff 97` | bl 0x00795de4 | `UNCONDITIONAL_CALL`
<a id="insn-007ae1e8"></a> `007ae1e8` | `e9 23 42 a9` | ldp x9,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ae1ec"></a> `007ae1ec` | `e9 a3 00 a9` | stp x9,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007ae1f0"></a> `007ae1f0` | `c8 00 00 b4` | cbz x8,0x007ae208 | `CONDITIONAL_JUMP`
<a id="insn-007ae1f4"></a> `007ae1f4` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-007ae1f8"></a> `007ae1f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007ae1fc"></a> `007ae1fc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007ae200"></a> `007ae200` | `ac 95 12 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-007ae204"></a> `007ae204` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae208"></a> `007ae208` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007ae20c"></a> `007ae20c` | `04 9f ff 97` | bl 0x00795e1c | `UNCONDITIONAL_CALL`
<a id="insn-007ae210"></a> `007ae210` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ae214"></a> `007ae214` | `73 01 00 b4` | cbz x19,0x007ae240 | `CONDITIONAL_JUMP`
<a id="insn-007ae218"></a> `007ae218` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007ae21c"></a> `007ae21c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007ae220"></a> `007ae220` | `b0 95 12 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-007ae224"></a> `007ae224` | `e0 00 00 b5` | cbnz x0,0x007ae240 | `CONDITIONAL_JUMP`
<a id="insn-007ae228"></a> `007ae228` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007ae22c"></a> `007ae22c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae230"></a> `007ae230` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ae234"></a> `007ae234` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae238"></a> `007ae238` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae23c"></a> `007ae23c` | `11 a6 12 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007ae240"></a> `007ae240` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007ae244"></a> `007ae244` | `73 01 00 b4` | cbz x19,0x007ae270 | `CONDITIONAL_JUMP`
<a id="insn-007ae248"></a> `007ae248` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007ae24c"></a> `007ae24c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007ae250"></a> `007ae250` | `a4 95 12 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-007ae254"></a> `007ae254` | `e0 00 00 b5` | cbnz x0,0x007ae270 | `CONDITIONAL_JUMP`
<a id="insn-007ae258"></a> `007ae258` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007ae25c"></a> `007ae25c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae260"></a> `007ae260` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ae264"></a> `007ae264` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007ae268"></a> `007ae268` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ae26c"></a> `007ae26c` | `05 a6 12 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007ae270"></a> `007ae270` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-007ae274"></a> `007ae274` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007ae278"></a> `007ae278` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007ae27c"></a> `007ae27c` | `81 0a 00 54` | b.ne 0x007ae3cc | `CONDITIONAL_JUMP`
<a id="insn-007ae280"></a> `007ae280` | `f4 4f 50 a9` | ldp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007ae284"></a> `007ae284` | `f7 73 40 f9` | ldr x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007ae288"></a> `007ae288` | `f6 57 4f a9` | ldp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007ae28c"></a> `007ae28c` | `fd 7b 4d a9` | ldp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-007ae290"></a> `007ae290` | `ff 43 04 91` | add sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-007ae294"></a> `007ae294` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ae3cc"></a> `007ae3cc` | `c5 a5 12 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007adedc`](#insn-007adedc) 範囲 `[['007adedc', '007adeef']]`
  - `FALL_THROUGH` [`007adeec`](#insn-007adeec) → [`007adef0`](#insn-007adef0)
- ブロック [`007adef0`](#insn-007adef0) 範囲 `[['007adef0', '007adf1f']]`
  - `CONDITIONAL_JUMP` [`007adf1c`](#insn-007adf1c) → [`007adf34`](#insn-007adf34)
  - `FALL_THROUGH` [`007adf1c`](#insn-007adf1c) → [`007adf20`](#insn-007adf20)
- ブロック [`007adf20`](#insn-007adf20) 範囲 `[['007adf20', '007adf33']]`
  - `UNCONDITIONAL_JUMP` [`007adf30`](#insn-007adf30) → [`007adf40`](#insn-007adf40)
- ブロック [`007adf34`](#insn-007adf34) 範囲 `[['007adf34', '007adf3f']]`
  - `FALL_THROUGH` [`007adf3c`](#insn-007adf3c) → [`007adf40`](#insn-007adf40)
- ブロック [`007adf40`](#insn-007adf40) 範囲 `[['007adf40', '007adf57']]`
  - `CONDITIONAL_JUMP` [`007adf54`](#insn-007adf54) → [`007adf60`](#insn-007adf60)
  - `FALL_THROUGH` [`007adf54`](#insn-007adf54) → [`007adf58`](#insn-007adf58)
- ブロック [`007adf58`](#insn-007adf58) 範囲 `[['007adf58', '007adf5f']]`
  - `FALL_THROUGH` [`007adf5c`](#insn-007adf5c) → [`007adf60`](#insn-007adf60)
- ブロック [`007adf60`](#insn-007adf60) 範囲 `[['007adf60', '007adf7b']]`
  - `CONDITIONAL_JUMP` [`007adf78`](#insn-007adf78) → [`007adfc4`](#insn-007adfc4)
  - `FALL_THROUGH` [`007adf78`](#insn-007adf78) → [`007adf7c`](#insn-007adf7c)
- ブロック [`007adf7c`](#insn-007adf7c) 範囲 `[['007adf7c', '007adf83']]`
  - `CONDITIONAL_JUMP` [`007adf80`](#insn-007adf80) → [`007adf8c`](#insn-007adf8c)
  - `FALL_THROUGH` [`007adf80`](#insn-007adf80) → [`007adf84`](#insn-007adf84)
- ブロック [`007adf84`](#insn-007adf84) 範囲 `[['007adf84', '007adf8b']]`
  - `FALL_THROUGH` [`007adf88`](#insn-007adf88) → [`007adf8c`](#insn-007adf8c)
- ブロック [`007adf8c`](#insn-007adf8c) 範囲 `[['007adf8c', '007adf93']]`
  - `FALL_THROUGH` [`007adf90`](#insn-007adf90) → [`007adf94`](#insn-007adf94)
- ブロック [`007adf94`](#insn-007adf94) 範囲 `[['007adf94', '007adfa3']]`
  - `CONDITIONAL_JUMP` [`007adfa0`](#insn-007adfa0) → [`007adfac`](#insn-007adfac)
  - `FALL_THROUGH` [`007adfa0`](#insn-007adfa0) → [`007adfa4`](#insn-007adfa4)
- ブロック [`007adfa4`](#insn-007adfa4) 範囲 `[['007adfa4', '007adfab']]`
  - `FALL_THROUGH` [`007adfa8`](#insn-007adfa8) → [`007adfac`](#insn-007adfac)
- ブロック [`007adfac`](#insn-007adfac) 範囲 `[['007adfac', '007adfb3']]`
  - `CONDITIONAL_JUMP` [`007adfb0`](#insn-007adfb0) → [`007adfbc`](#insn-007adfbc)
  - `FALL_THROUGH` [`007adfb0`](#insn-007adfb0) → [`007adfb4`](#insn-007adfb4)
- ブロック [`007adfb4`](#insn-007adfb4) 範囲 `[['007adfb4', '007adfbb']]`
  - `FALL_THROUGH` [`007adfb8`](#insn-007adfb8) → [`007adfbc`](#insn-007adfbc)
- ブロック [`007adfbc`](#insn-007adfbc) 範囲 `[['007adfbc', '007adfc3']]`
  - `FALL_THROUGH` [`007adfc0`](#insn-007adfc0) → [`007adfc4`](#insn-007adfc4)
- ブロック [`007adfc4`](#insn-007adfc4) 範囲 `[['007adfc4', '007adfcf']]`
  - `CONDITIONAL_JUMP` [`007adfcc`](#insn-007adfcc) → [`007adfe4`](#insn-007adfe4)
  - `FALL_THROUGH` [`007adfcc`](#insn-007adfcc) → [`007adfd0`](#insn-007adfd0)
- ブロック [`007adfd0`](#insn-007adfd0) 範囲 `[['007adfd0', '007adfd7']]`
  - `CONDITIONAL_JUMP` [`007adfd4`](#insn-007adfd4) → [`007adfec`](#insn-007adfec)
  - `FALL_THROUGH` [`007adfd4`](#insn-007adfd4) → [`007adfd8`](#insn-007adfd8)
- ブロック [`007adfd8`](#insn-007adfd8) 範囲 `[['007adfd8', '007adfe3']]`
  - `FALL_THROUGH` [`007adfe0`](#insn-007adfe0) → [`007adfe4`](#insn-007adfe4)
- ブロック [`007adfe4`](#insn-007adfe4) 範囲 `[['007adfe4', '007adfeb']]`
  - `UNCONDITIONAL_JUMP` [`007adfe8`](#insn-007adfe8) → [`007ae008`](#insn-007ae008)
- ブロック [`007adfec`](#insn-007adfec) 範囲 `[['007adfec', '007ae007']]`
  - `FALL_THROUGH` [`007ae004`](#insn-007ae004) → [`007ae008`](#insn-007ae008)
- ブロック [`007ae008`](#insn-007ae008) 範囲 `[['007ae008', '007ae00b']]`
  - `FALL_THROUGH` [`007ae008`](#insn-007ae008) → [`007ae00c`](#insn-007ae00c)
- ブロック [`007ae00c`](#insn-007ae00c) 範囲 `[['007ae00c', '007ae02f']]`
  - `CONDITIONAL_JUMP` [`007ae02c`](#insn-007ae02c) → [`007ae048`](#insn-007ae048)
  - `FALL_THROUGH` [`007ae02c`](#insn-007ae02c) → [`007ae030`](#insn-007ae030)
- ブロック [`007ae030`](#insn-007ae030) 範囲 `[['007ae030', '007ae03b']]`
  - `CONDITIONAL_JUMP` [`007ae038`](#insn-007ae038) → [`007ae050`](#insn-007ae050)
  - `FALL_THROUGH` [`007ae038`](#insn-007ae038) → [`007ae03c`](#insn-007ae03c)
- ブロック [`007ae03c`](#insn-007ae03c) 範囲 `[['007ae03c', '007ae047']]`
  - `FALL_THROUGH` [`007ae044`](#insn-007ae044) → [`007ae048`](#insn-007ae048)
- ブロック [`007ae048`](#insn-007ae048) 範囲 `[['007ae048', '007ae04f']]`
  - `UNCONDITIONAL_JUMP` [`007ae04c`](#insn-007ae04c) → [`007ae064`](#insn-007ae064)
- ブロック [`007ae050`](#insn-007ae050) 範囲 `[['007ae050', '007ae057']]`
  - `FALL_THROUGH` [`007ae054`](#insn-007ae054) → [`007ae058`](#insn-007ae058)
- ブロック [`007ae058`](#insn-007ae058) 範囲 `[['007ae058', '007ae063']]`
  - `FALL_THROUGH` [`007ae060`](#insn-007ae060) → [`007ae064`](#insn-007ae064)
- ブロック [`007ae064`](#insn-007ae064) 範囲 `[['007ae064', '007ae06b']]`
  - `FALL_THROUGH` [`007ae068`](#insn-007ae068) → [`007ae06c`](#insn-007ae06c)
- ブロック [`007ae06c`](#insn-007ae06c) 範囲 `[['007ae06c', '007ae07b']]`
  - `FALL_THROUGH` [`007ae078`](#insn-007ae078) → [`007ae07c`](#insn-007ae07c)
- ブロック [`007ae07c`](#insn-007ae07c) 範囲 `[['007ae07c', '007ae083']]`
  - `CONDITIONAL_JUMP` [`007ae080`](#insn-007ae080) → [`007ae090`](#insn-007ae090)
  - `FALL_THROUGH` [`007ae080`](#insn-007ae080) → [`007ae084`](#insn-007ae084)
- ブロック [`007ae084`](#insn-007ae084) 範囲 `[['007ae084', '007ae087']]`
  - `CONDITIONAL_JUMP` [`007ae084`](#insn-007ae084) → [`007ae0a4`](#insn-007ae0a4)
  - `FALL_THROUGH` [`007ae084`](#insn-007ae084) → [`007ae088`](#insn-007ae088)
- ブロック [`007ae088`](#insn-007ae088) 範囲 `[['007ae088', '007ae08f']]`
  - `UNCONDITIONAL_JUMP` [`007ae08c`](#insn-007ae08c) → [`007ae098`](#insn-007ae098)
- ブロック [`007ae090`](#insn-007ae090) 範囲 `[['007ae090', '007ae097']]`
  - `FALL_THROUGH` [`007ae094`](#insn-007ae094) → [`007ae098`](#insn-007ae098)
- ブロック [`007ae098`](#insn-007ae098) 範囲 `[['007ae098', '007ae0a3']]`
  - `FALL_THROUGH` [`007ae0a0`](#insn-007ae0a0) → [`007ae0a4`](#insn-007ae0a4)
- ブロック [`007ae0a4`](#insn-007ae0a4) 範囲 `[['007ae0a4', '007ae0b3']]`
  - `CONDITIONAL_JUMP` [`007ae0b0`](#insn-007ae0b0) → [`007ae0c0`](#insn-007ae0c0)
  - `FALL_THROUGH` [`007ae0b0`](#insn-007ae0b0) → [`007ae0b4`](#insn-007ae0b4)
- ブロック [`007ae0b4`](#insn-007ae0b4) 範囲 `[['007ae0b4', '007ae0b7']]`
  - `CONDITIONAL_JUMP` [`007ae0b4`](#insn-007ae0b4) → [`007ae0d4`](#insn-007ae0d4)
  - `FALL_THROUGH` [`007ae0b4`](#insn-007ae0b4) → [`007ae0b8`](#insn-007ae0b8)
- ブロック [`007ae0b8`](#insn-007ae0b8) 範囲 `[['007ae0b8', '007ae0bf']]`
  - `UNCONDITIONAL_JUMP` [`007ae0bc`](#insn-007ae0bc) → [`007ae0c8`](#insn-007ae0c8)
- ブロック [`007ae0c0`](#insn-007ae0c0) 範囲 `[['007ae0c0', '007ae0c7']]`
  - `FALL_THROUGH` [`007ae0c4`](#insn-007ae0c4) → [`007ae0c8`](#insn-007ae0c8)
- ブロック [`007ae0c8`](#insn-007ae0c8) 範囲 `[['007ae0c8', '007ae0d3']]`
  - `FALL_THROUGH` [`007ae0d0`](#insn-007ae0d0) → [`007ae0d4`](#insn-007ae0d4)
- ブロック [`007ae0d4`](#insn-007ae0d4) 範囲 `[['007ae0d4', '007ae0df']]`
  - `CONDITIONAL_JUMP` [`007ae0dc`](#insn-007ae0dc) → [`007ae0f4`](#insn-007ae0f4)
  - `FALL_THROUGH` [`007ae0dc`](#insn-007ae0dc) → [`007ae0e0`](#insn-007ae0e0)
- ブロック [`007ae0e0`](#insn-007ae0e0) 範囲 `[['007ae0e0', '007ae0e7']]`
  - `CONDITIONAL_JUMP` [`007ae0e4`](#insn-007ae0e4) → [`007ae0fc`](#insn-007ae0fc)
  - `FALL_THROUGH` [`007ae0e4`](#insn-007ae0e4) → [`007ae0e8`](#insn-007ae0e8)
- ブロック [`007ae0e8`](#insn-007ae0e8) 範囲 `[['007ae0e8', '007ae0f3']]`
  - `FALL_THROUGH` [`007ae0f0`](#insn-007ae0f0) → [`007ae0f4`](#insn-007ae0f4)
- ブロック [`007ae0f4`](#insn-007ae0f4) 範囲 `[['007ae0f4', '007ae0fb']]`
  - `UNCONDITIONAL_JUMP` [`007ae0f8`](#insn-007ae0f8) → [`007ae118`](#insn-007ae118)
- ブロック [`007ae0fc`](#insn-007ae0fc) 範囲 `[['007ae0fc', '007ae117']]`
  - `FALL_THROUGH` [`007ae114`](#insn-007ae114) → [`007ae118`](#insn-007ae118)
- ブロック [`007ae118`](#insn-007ae118) 範囲 `[['007ae118', '007ae13f']]`
  - `CONDITIONAL_JUMP` [`007ae13c`](#insn-007ae13c) → [`007ae158`](#insn-007ae158)
  - `FALL_THROUGH` [`007ae13c`](#insn-007ae13c) → [`007ae140`](#insn-007ae140)
- ブロック [`007ae140`](#insn-007ae140) 範囲 `[['007ae140', '007ae14b']]`
  - `CONDITIONAL_JUMP` [`007ae148`](#insn-007ae148) → [`007ae160`](#insn-007ae160)
  - `FALL_THROUGH` [`007ae148`](#insn-007ae148) → [`007ae14c`](#insn-007ae14c)
- ブロック [`007ae14c`](#insn-007ae14c) 範囲 `[['007ae14c', '007ae157']]`
  - `FALL_THROUGH` [`007ae154`](#insn-007ae154) → [`007ae158`](#insn-007ae158)
- ブロック [`007ae158`](#insn-007ae158) 範囲 `[['007ae158', '007ae15f']]`
  - `UNCONDITIONAL_JUMP` [`007ae15c`](#insn-007ae15c) → [`007ae174`](#insn-007ae174)
- ブロック [`007ae160`](#insn-007ae160) 範囲 `[['007ae160', '007ae173']]`
  - `FALL_THROUGH` [`007ae170`](#insn-007ae170) → [`007ae174`](#insn-007ae174)
- ブロック [`007ae174`](#insn-007ae174) 範囲 `[['007ae174', '007ae193']]`
  - `CONDITIONAL_JUMP` [`007ae190`](#insn-007ae190) → [`007ae1a0`](#insn-007ae1a0)
  - `FALL_THROUGH` [`007ae190`](#insn-007ae190) → [`007ae194`](#insn-007ae194)
- ブロック [`007ae194`](#insn-007ae194) 範囲 `[['007ae194', '007ae197']]`
  - `CONDITIONAL_JUMP` [`007ae194`](#insn-007ae194) → [`007ae1b4`](#insn-007ae1b4)
  - `FALL_THROUGH` [`007ae194`](#insn-007ae194) → [`007ae198`](#insn-007ae198)
- ブロック [`007ae198`](#insn-007ae198) 範囲 `[['007ae198', '007ae19f']]`
  - `UNCONDITIONAL_JUMP` [`007ae19c`](#insn-007ae19c) → [`007ae1a8`](#insn-007ae1a8)
- ブロック [`007ae1a0`](#insn-007ae1a0) 範囲 `[['007ae1a0', '007ae1a7']]`
  - `FALL_THROUGH` [`007ae1a4`](#insn-007ae1a4) → [`007ae1a8`](#insn-007ae1a8)
- ブロック [`007ae1a8`](#insn-007ae1a8) 範囲 `[['007ae1a8', '007ae1b3']]`
  - `FALL_THROUGH` [`007ae1b0`](#insn-007ae1b0) → [`007ae1b4`](#insn-007ae1b4)
- ブロック [`007ae1b4`](#insn-007ae1b4) 範囲 `[['007ae1b4', '007ae1c3']]`
  - `CONDITIONAL_JUMP` [`007ae1c0`](#insn-007ae1c0) → [`007ae1d0`](#insn-007ae1d0)
  - `FALL_THROUGH` [`007ae1c0`](#insn-007ae1c0) → [`007ae1c4`](#insn-007ae1c4)
- ブロック [`007ae1c4`](#insn-007ae1c4) 範囲 `[['007ae1c4', '007ae1c7']]`
  - `CONDITIONAL_JUMP` [`007ae1c4`](#insn-007ae1c4) → [`007ae1e4`](#insn-007ae1e4)
  - `FALL_THROUGH` [`007ae1c4`](#insn-007ae1c4) → [`007ae1c8`](#insn-007ae1c8)
- ブロック [`007ae1c8`](#insn-007ae1c8) 範囲 `[['007ae1c8', '007ae1cf']]`
  - `UNCONDITIONAL_JUMP` [`007ae1cc`](#insn-007ae1cc) → [`007ae1d8`](#insn-007ae1d8)
- ブロック [`007ae1d0`](#insn-007ae1d0) 範囲 `[['007ae1d0', '007ae1d7']]`
  - `FALL_THROUGH` [`007ae1d4`](#insn-007ae1d4) → [`007ae1d8`](#insn-007ae1d8)
- ブロック [`007ae1d8`](#insn-007ae1d8) 範囲 `[['007ae1d8', '007ae1e3']]`
  - `FALL_THROUGH` [`007ae1e0`](#insn-007ae1e0) → [`007ae1e4`](#insn-007ae1e4)
- ブロック [`007ae1e4`](#insn-007ae1e4) 範囲 `[['007ae1e4', '007ae1f3']]`
  - `CONDITIONAL_JUMP` [`007ae1f0`](#insn-007ae1f0) → [`007ae208`](#insn-007ae208)
  - `FALL_THROUGH` [`007ae1f0`](#insn-007ae1f0) → [`007ae1f4`](#insn-007ae1f4)
- ブロック [`007ae1f4`](#insn-007ae1f4) 範囲 `[['007ae1f4', '007ae207']]`
  - `FALL_THROUGH` [`007ae204`](#insn-007ae204) → [`007ae208`](#insn-007ae208)
- ブロック [`007ae208`](#insn-007ae208) 範囲 `[['007ae208', '007ae217']]`
  - `CONDITIONAL_JUMP` [`007ae214`](#insn-007ae214) → [`007ae240`](#insn-007ae240)
  - `FALL_THROUGH` [`007ae214`](#insn-007ae214) → [`007ae218`](#insn-007ae218)
- ブロック [`007ae218`](#insn-007ae218) 範囲 `[['007ae218', '007ae227']]`
  - `CONDITIONAL_JUMP` [`007ae224`](#insn-007ae224) → [`007ae240`](#insn-007ae240)
  - `FALL_THROUGH` [`007ae224`](#insn-007ae224) → [`007ae228`](#insn-007ae228)
- ブロック [`007ae228`](#insn-007ae228) 範囲 `[['007ae228', '007ae23f']]`
  - `FALL_THROUGH` [`007ae23c`](#insn-007ae23c) → [`007ae240`](#insn-007ae240)
- ブロック [`007ae240`](#insn-007ae240) 範囲 `[['007ae240', '007ae247']]`
  - `CONDITIONAL_JUMP` [`007ae244`](#insn-007ae244) → [`007ae270`](#insn-007ae270)
  - `FALL_THROUGH` [`007ae244`](#insn-007ae244) → [`007ae248`](#insn-007ae248)
- ブロック [`007ae248`](#insn-007ae248) 範囲 `[['007ae248', '007ae257']]`
  - `CONDITIONAL_JUMP` [`007ae254`](#insn-007ae254) → [`007ae270`](#insn-007ae270)
  - `FALL_THROUGH` [`007ae254`](#insn-007ae254) → [`007ae258`](#insn-007ae258)
- ブロック [`007ae258`](#insn-007ae258) 範囲 `[['007ae258', '007ae26f']]`
  - `FALL_THROUGH` [`007ae26c`](#insn-007ae26c) → [`007ae270`](#insn-007ae270)
- ブロック [`007ae270`](#insn-007ae270) 範囲 `[['007ae270', '007ae277']]`
  - `FALL_THROUGH` [`007ae274`](#insn-007ae274) → [`007ae278`](#insn-007ae278)
- ブロック [`007ae278`](#insn-007ae278) 範囲 `[['007ae278', '007ae27f']]`
  - `CONDITIONAL_JUMP` [`007ae27c`](#insn-007ae27c) → [`007ae3cc`](#insn-007ae3cc)
  - `FALL_THROUGH` [`007ae27c`](#insn-007ae27c) → [`007ae280`](#insn-007ae280)
- ブロック [`007ae280`](#insn-007ae280) 範囲 `[['007ae280', '007ae297']]`
- ブロック [`007ae3cc`](#insn-007ae3cc) 範囲 `[['007ae3cc', '007ae3cf']]`

## 命令位置別の参照

- [`007adee0`](#insn-007adee0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adee4`](#insn-007adee4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adee8`](#insn-007adee8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adeec`](#insn-007adeec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf0c`](#insn-007adf0c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf10`](#insn-007adf10) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007adf1c`](#insn-007adf1c) → [`007adf34`](#insn-007adf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf28`](#insn-007adf28) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf2c`](#insn-007adf2c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf30`](#insn-007adf30) → [`007adf40`](#insn-007adf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf3c`](#insn-007adf3c) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`007adf48`](#insn-007adf48) → [`005a4fd8`](../005a4/005a4fd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005a4fd8` · 推定シンボル `None` · 推定型 `None`
- [`007adf4c`](#insn-007adf4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf50`](#insn-007adf50) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf54`](#insn-007adf54) → [`007adf60`](#insn-007adf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf58`](#insn-007adf58) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf5c`](#insn-007adf5c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007adf6c`](#insn-007adf6c) → [`007afefc`](../007af/007afefc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007afefc` · 推定シンボル `None` · 推定型 `None`
- [`007adf70`](#insn-007adf70) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf74`](#insn-007adf74) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf78`](#insn-007adf78) → [`007adfc4`](#insn-007adfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf80`](#insn-007adf80) → [`007adf8c`](#insn-007adf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adf88`](#insn-007adf88) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007adf9c`](#insn-007adf9c) → `00c6d620`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007adfa0`](#insn-007adfa0) → [`007adfac`](#insn-007adfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfa8`](#insn-007adfa8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007adfb0`](#insn-007adfb0) → [`007adfbc`](#insn-007adfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfb8`](#insn-007adfb8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007adfc0`](#insn-007adfc0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007adfc8`](#insn-007adfc8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfcc`](#insn-007adfcc) → [`007adfe4`](#insn-007adfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfd4`](#insn-007adfd4) → [`007adfec`](#insn-007adfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfe4`](#insn-007adfe4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adfe8`](#insn-007adfe8) → [`007ae008`](#insn-007ae008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007adff4`](#insn-007adff4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae008`](#insn-007ae008) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae010`](#insn-007ae010) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007ae018`](#insn-007ae018) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae028`](#insn-007ae028) → `00c7a698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ae02c`](#insn-007ae02c) → [`007ae048`](#insn-007ae048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae038`](#insn-007ae038) → [`007ae050`](#insn-007ae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae04c`](#insn-007ae04c) → [`007ae064`](#insn-007ae064) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae050`](#insn-007ae050) → `Stack[-0xb0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae064`](#insn-007ae064) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae074`](#insn-007ae074) → [`00598af4`](../00598/00598af4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00598af4` · 推定シンボル `None` · 推定型 `None`
- [`007ae078`](#insn-007ae078) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae080`](#insn-007ae080) → [`007ae090`](#insn-007ae090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae084`](#insn-007ae084) → [`007ae0a4`](#insn-007ae0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae08c`](#insn-007ae08c) → [`007ae098`](#insn-007ae098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae098`](#insn-007ae098) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae09c`](#insn-007ae09c) → `00c7a6c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ae0a0`](#insn-007ae0a0) → [`007b0248`](../007b0/007b0248.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `007b0248` · 推定シンボル `None` · 推定型 `None`
- [`007ae0a4`](#insn-007ae0a4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0b0`](#insn-007ae0b0) → [`007ae0c0`](#insn-007ae0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0b4`](#insn-007ae0b4) → [`007ae0d4`](#insn-007ae0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0bc`](#insn-007ae0bc) → [`007ae0c8`](#insn-007ae0c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0c8`](#insn-007ae0c8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0d8`](#insn-007ae0d8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0dc`](#insn-007ae0dc) → [`007ae0f4`](#insn-007ae0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0e4`](#insn-007ae0e4) → [`007ae0fc`](#insn-007ae0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0f4`](#insn-007ae0f4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae0f8`](#insn-007ae0f8) → [`007ae118`](#insn-007ae118) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae104`](#insn-007ae104) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae118`](#insn-007ae118) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae120`](#insn-007ae120) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007ae128`](#insn-007ae128) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae138`](#insn-007ae138) → `00c7a718`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ae13c`](#insn-007ae13c) → [`007ae158`](#insn-007ae158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae148`](#insn-007ae148) → [`007ae160`](#insn-007ae160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae15c`](#insn-007ae15c) → [`007ae174`](#insn-007ae174) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae160`](#insn-007ae160) → `Stack[-0xe0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae174`](#insn-007ae174) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae184`](#insn-007ae184) → [`00598cb4`](../00598/00598cb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00598cb4` · 推定シンボル `None` · 推定型 `None`
- [`007ae188`](#insn-007ae188) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae190`](#insn-007ae190) → [`007ae1a0`](#insn-007ae1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae194`](#insn-007ae194) → [`007ae1b4`](#insn-007ae1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae19c`](#insn-007ae19c) → [`007ae1a8`](#insn-007ae1a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1a8`](#insn-007ae1a8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1ac`](#insn-007ae1ac) → `00c7a740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007ae1b0`](#insn-007ae1b0) → [`007b04b4`](../007b0/007b04b4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `007b04b4` · 推定シンボル `None` · 推定型 `None`
- [`007ae1b4`](#insn-007ae1b4) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1c0`](#insn-007ae1c0) → [`007ae1d0`](#insn-007ae1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1c4`](#insn-007ae1c4) → [`007ae1e4`](#insn-007ae1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1cc`](#insn-007ae1cc) → [`007ae1d8`](#insn-007ae1d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1d8`](#insn-007ae1d8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1e4`](#insn-007ae1e4) → [`00795de4`](../00795/00795de4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00795de4` · 推定シンボル `None` · 推定型 `None`
- [`007ae1e8`](#insn-007ae1e8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1ec`](#insn-007ae1ec) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae1f0`](#insn-007ae1f0) → [`007ae208`](#insn-007ae208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae200`](#insn-007ae200) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`007ae20c`](#insn-007ae20c) → [`00795e1c`](../00795/00795e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00795e1c` · 推定シンボル `None` · 推定型 `None`
- [`007ae210`](#insn-007ae210) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae214`](#insn-007ae214) → [`007ae240`](#insn-007ae240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae220`](#insn-007ae220) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`007ae224`](#insn-007ae224) → [`007ae240`](#insn-007ae240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae23c`](#insn-007ae23c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007ae240`](#insn-007ae240) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae244`](#insn-007ae244) → [`007ae270`](#insn-007ae270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae250`](#insn-007ae250) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`007ae254`](#insn-007ae254) → [`007ae270`](#insn-007ae270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae26c`](#insn-007ae26c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007ae274`](#insn-007ae274) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae27c`](#insn-007ae27c) → [`007ae3cc`](#insn-007ae3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae280`](#insn-007ae280) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae284`](#insn-007ae284) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae288`](#insn-007ae288) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae28c`](#insn-007ae28c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ae3cc`](#insn-007ae3cc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007adee0`](#insn-007adee0)

~~~json
{
  "source": "007adee0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adee4`](#insn-007adee4)

~~~json
{
  "source": "007adee4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adee8`](#insn-007adee8)

~~~json
{
  "source": "007adee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adeec`](#insn-007adeec)

~~~json
{
  "source": "007adeec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf0c`](#insn-007adf0c)

~~~json
{
  "source": "007adf0c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf10`](#insn-007adf10)

~~~json
{
  "source": "007adf10",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf1c`](#insn-007adf1c)

~~~json
{
  "source": "007adf1c",
  "target": "007adf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf28`](#insn-007adf28)

~~~json
{
  "source": "007adf28",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf2c`](#insn-007adf2c)

~~~json
{
  "source": "007adf2c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf30`](#insn-007adf30)

~~~json
{
  "source": "007adf30",
  "target": "007adf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf3c`](#insn-007adf3c)

~~~json
{
  "source": "007adf3c",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf48`](#insn-007adf48)

~~~json
{
  "source": "007adf48",
  "target": "005a4fd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf4c`](#insn-007adf4c)

~~~json
{
  "source": "007adf4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf50`](#insn-007adf50)

~~~json
{
  "source": "007adf50",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf54`](#insn-007adf54)

~~~json
{
  "source": "007adf54",
  "target": "007adf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf58`](#insn-007adf58)

~~~json
{
  "source": "007adf58",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf5c`](#insn-007adf5c)

~~~json
{
  "source": "007adf5c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf6c`](#insn-007adf6c)

~~~json
{
  "source": "007adf6c",
  "target": "007afefc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf70`](#insn-007adf70)

~~~json
{
  "source": "007adf70",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf74`](#insn-007adf74)

~~~json
{
  "source": "007adf74",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf78`](#insn-007adf78)

~~~json
{
  "source": "007adf78",
  "target": "007adfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf80`](#insn-007adf80)

~~~json
{
  "source": "007adf80",
  "target": "007adf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adf88`](#insn-007adf88)

~~~json
{
  "source": "007adf88",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adf9c`](#insn-007adf9c)

~~~json
{
  "source": "007adf9c",
  "target": "00c6d620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6d620",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007adfa0`](#insn-007adfa0)

~~~json
{
  "source": "007adfa0",
  "target": "007adfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfa8`](#insn-007adfa8)

~~~json
{
  "source": "007adfa8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adfb0`](#insn-007adfb0)

~~~json
{
  "source": "007adfb0",
  "target": "007adfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfb8`](#insn-007adfb8)

~~~json
{
  "source": "007adfb8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adfc0`](#insn-007adfc0)

~~~json
{
  "source": "007adfc0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007adfc8`](#insn-007adfc8)

~~~json
{
  "source": "007adfc8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfcc`](#insn-007adfcc)

~~~json
{
  "source": "007adfcc",
  "target": "007adfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfd4`](#insn-007adfd4)

~~~json
{
  "source": "007adfd4",
  "target": "007adfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfe4`](#insn-007adfe4)

~~~json
{
  "source": "007adfe4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adfe8`](#insn-007adfe8)

~~~json
{
  "source": "007adfe8",
  "target": "007ae008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007adff4`](#insn-007adff4)

~~~json
{
  "source": "007adff4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae008`](#insn-007ae008)

~~~json
{
  "source": "007ae008",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae010`](#insn-007ae010)

~~~json
{
  "source": "007ae010",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae018`](#insn-007ae018)

~~~json
{
  "source": "007ae018",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae028`](#insn-007ae028)

~~~json
{
  "source": "007ae028",
  "target": "00c7a698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a698",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ae02c`](#insn-007ae02c)

~~~json
{
  "source": "007ae02c",
  "target": "007ae048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae038`](#insn-007ae038)

~~~json
{
  "source": "007ae038",
  "target": "007ae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae04c`](#insn-007ae04c)

~~~json
{
  "source": "007ae04c",
  "target": "007ae064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae050`](#insn-007ae050)

~~~json
{
  "source": "007ae050",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae064`](#insn-007ae064)

~~~json
{
  "source": "007ae064",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae074`](#insn-007ae074)

~~~json
{
  "source": "007ae074",
  "target": "00598af4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae078`](#insn-007ae078)

~~~json
{
  "source": "007ae078",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae080`](#insn-007ae080)

~~~json
{
  "source": "007ae080",
  "target": "007ae090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae084`](#insn-007ae084)

~~~json
{
  "source": "007ae084",
  "target": "007ae0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae08c`](#insn-007ae08c)

~~~json
{
  "source": "007ae08c",
  "target": "007ae098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae098`](#insn-007ae098)

~~~json
{
  "source": "007ae098",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae09c`](#insn-007ae09c)

~~~json
{
  "source": "007ae09c",
  "target": "00c7a6c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a6c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ae0a0`](#insn-007ae0a0)

~~~json
{
  "source": "007ae0a0",
  "target": "007b0248",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae0a4`](#insn-007ae0a4)

~~~json
{
  "source": "007ae0a4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0b0`](#insn-007ae0b0)

~~~json
{
  "source": "007ae0b0",
  "target": "007ae0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0b4`](#insn-007ae0b4)

~~~json
{
  "source": "007ae0b4",
  "target": "007ae0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0bc`](#insn-007ae0bc)

~~~json
{
  "source": "007ae0bc",
  "target": "007ae0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0c8`](#insn-007ae0c8)

~~~json
{
  "source": "007ae0c8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0d8`](#insn-007ae0d8)

~~~json
{
  "source": "007ae0d8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0dc`](#insn-007ae0dc)

~~~json
{
  "source": "007ae0dc",
  "target": "007ae0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0e4`](#insn-007ae0e4)

~~~json
{
  "source": "007ae0e4",
  "target": "007ae0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0f4`](#insn-007ae0f4)

~~~json
{
  "source": "007ae0f4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae0f8`](#insn-007ae0f8)

~~~json
{
  "source": "007ae0f8",
  "target": "007ae118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae104`](#insn-007ae104)

~~~json
{
  "source": "007ae104",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae118`](#insn-007ae118)

~~~json
{
  "source": "007ae118",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae120`](#insn-007ae120)

~~~json
{
  "source": "007ae120",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae128`](#insn-007ae128)

~~~json
{
  "source": "007ae128",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae138`](#insn-007ae138)

~~~json
{
  "source": "007ae138",
  "target": "00c7a718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ae13c`](#insn-007ae13c)

~~~json
{
  "source": "007ae13c",
  "target": "007ae158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae148`](#insn-007ae148)

~~~json
{
  "source": "007ae148",
  "target": "007ae160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae15c`](#insn-007ae15c)

~~~json
{
  "source": "007ae15c",
  "target": "007ae174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae160`](#insn-007ae160)

~~~json
{
  "source": "007ae160",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae174`](#insn-007ae174)

~~~json
{
  "source": "007ae174",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae184`](#insn-007ae184)

~~~json
{
  "source": "007ae184",
  "target": "00598cb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae188`](#insn-007ae188)

~~~json
{
  "source": "007ae188",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae190`](#insn-007ae190)

~~~json
{
  "source": "007ae190",
  "target": "007ae1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae194`](#insn-007ae194)

~~~json
{
  "source": "007ae194",
  "target": "007ae1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae19c`](#insn-007ae19c)

~~~json
{
  "source": "007ae19c",
  "target": "007ae1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1a8`](#insn-007ae1a8)

~~~json
{
  "source": "007ae1a8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1ac`](#insn-007ae1ac)

~~~json
{
  "source": "007ae1ac",
  "target": "00c7a740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7a740",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007ae1b0`](#insn-007ae1b0)

~~~json
{
  "source": "007ae1b0",
  "target": "007b04b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae1b4`](#insn-007ae1b4)

~~~json
{
  "source": "007ae1b4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1c0`](#insn-007ae1c0)

~~~json
{
  "source": "007ae1c0",
  "target": "007ae1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1c4`](#insn-007ae1c4)

~~~json
{
  "source": "007ae1c4",
  "target": "007ae1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1cc`](#insn-007ae1cc)

~~~json
{
  "source": "007ae1cc",
  "target": "007ae1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1d8`](#insn-007ae1d8)

~~~json
{
  "source": "007ae1d8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1e4`](#insn-007ae1e4)

~~~json
{
  "source": "007ae1e4",
  "target": "00795de4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae1e8`](#insn-007ae1e8)

~~~json
{
  "source": "007ae1e8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1ec`](#insn-007ae1ec)

~~~json
{
  "source": "007ae1ec",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae1f0`](#insn-007ae1f0)

~~~json
{
  "source": "007ae1f0",
  "target": "007ae208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae200`](#insn-007ae200)

~~~json
{
  "source": "007ae200",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae20c`](#insn-007ae20c)

~~~json
{
  "source": "007ae20c",
  "target": "00795e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae210`](#insn-007ae210)

~~~json
{
  "source": "007ae210",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae214`](#insn-007ae214)

~~~json
{
  "source": "007ae214",
  "target": "007ae240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae220`](#insn-007ae220)

~~~json
{
  "source": "007ae220",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae224`](#insn-007ae224)

~~~json
{
  "source": "007ae224",
  "target": "007ae240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae23c`](#insn-007ae23c)

~~~json
{
  "source": "007ae23c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae240`](#insn-007ae240)

~~~json
{
  "source": "007ae240",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae244`](#insn-007ae244)

~~~json
{
  "source": "007ae244",
  "target": "007ae270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae250`](#insn-007ae250)

~~~json
{
  "source": "007ae250",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae254`](#insn-007ae254)

~~~json
{
  "source": "007ae254",
  "target": "007ae270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae26c`](#insn-007ae26c)

~~~json
{
  "source": "007ae26c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ae274`](#insn-007ae274)

~~~json
{
  "source": "007ae274",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae27c`](#insn-007ae27c)

~~~json
{
  "source": "007ae27c",
  "target": "007ae3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae280`](#insn-007ae280)

~~~json
{
  "source": "007ae280",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae284`](#insn-007ae284)

~~~json
{
  "source": "007ae284",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae288`](#insn-007ae288)

~~~json
{
  "source": "007ae288",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae28c`](#insn-007ae28c)

~~~json
{
  "source": "007ae28c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ae3cc`](#insn-007ae3cc)

~~~json
{
  "source": "007ae3cc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
