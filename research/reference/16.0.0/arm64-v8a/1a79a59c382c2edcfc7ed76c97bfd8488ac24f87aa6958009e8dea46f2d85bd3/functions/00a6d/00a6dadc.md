# 00a6dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0158.md#review-700a5ea107a19c460fa5b15d5b53a95d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a6dcd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6d/00a6dcd4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-f98f6a233b1c475b861da0ee3f823d8b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6dadc",
  "name": "FUN_00a6dadc",
  "size": 1552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "375653e9b3683ddd762f76015aa45d78d43300c7ac356a959dbd6f765cc88477",
  "source_text_sha256": "375653e9b3683ddd762f76015aa45d78d43300c7ac356a959dbd6f765cc88477",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6dadc",
        "00a6e0e7"
      ],
      [
        "00a6e10c",
        "00a6e10f"
      ]
    ],
    "bytes_sha256": "bbc57d8248cab205e0a1bc79e711fac76e255dd2b7b23474b7475b00a18e1dd4",
    "instruction_count": 388,
    "instruction_bytes": 1552,
    "body_bytes": 1552,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

- [00856dec](../00856/00856dec.md)

## 呼び出し先

- [0046c984](../0046c/0046c984.md)
- [0047e89c](../0047e/0047e89c.md)
- [00752b90](../00752/00752b90.md)
- [009cc9e0](../009cc/009cc9e0.md)
- [009d590c](../009d5/009d590c.md)
- [00a6cce4](../00a6c/00a6cce4.md)
- [00ab27e8](../00ab2/00ab27e8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9643 bytes

~~~c

void FUN_00a6dadc(long param_1)

{
  int *piVar1;
  long lVar2;
  int iVar3;
  int iVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  long *plVar8;
  long *plVar9;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
  plVar8 = DAT_00ca4568;
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  DAT_00ca4568 = DAT_00ca4578;
  DAT_00ca4578 = plVar8;
  uVar5 = _Znwm(0x430);
  FUN_00a6cce4(uVar5,param_1);
  piVar1 = (int *)((long)&fde_table_entry_00332070.data_loc + param_1);
  if (DAT_00ca4578 != (long *)0x0) {
    lVar7 = *DAT_00ca4578;
    DAT_00ca4578 = (long *)uVar5;
    (**(code **)(lVar7 + 8))();
    uVar5 = DAT_00ca4578;
  }
  DAT_00ca4578 = (long *)uVar5;
  FUN_009d590c(param_1);
  lVar7 = -0x3bc0;
  do {
    plVar8 = *(long **)(param_1 + lVar7 + 0x74e0);
    lVar6 = param_1 + 0x3918 + lVar7;
    *(undefined8 *)(lVar6 + 0x3bc8) = 0;
    *(undefined8 *)(lVar6 + 0x3bc0) = 0;
    if ((plVar8 != (long *)0x0) && (lVar6 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar6 == 0)
       ) {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    lVar7 = lVar7 + 0x10;
  } while (lVar7 != 0);
  *(undefined8 *)((long)&fde_table_entry_00332a20.data_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 2) = 0;
  *piVar1 = 0;
  *(undefined8 *)((long)&fde_table_entry_00335ee0.data_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00335ed8.data_loc + param_1) = 0;
  *(undefined4 *)((long)&fde_table_entry_00335ee8.initial_loc + param_1 + 3) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f90.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f88.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fa0.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f98.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fb0.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fa8.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fb8.initial_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00335ed8.data_loc + param_1 + 3) = 1;
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
                    /* try { // try from 00a6dfc8 to 00b6dfd7 has its CatchHandler @ 00a77ca8 */
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
                    /* try { // try from 00a6dfd8 to 00b6e047 has its CatchHandler @ 00a63e3c */
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330d10.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x2e,0,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7540);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7540) = plVar8;
  *(undefined8 *)(param_1 + 0x7538) = uVar5;
                    /* try { // try from 00a6dc80 to 00b6dc8f has its CatchHandler @ 00a77d48 */
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
                    /* try { // try from 00a6dccc to 00b6dcdb has its CatchHandler @ 00a77d44 */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330d28.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x18,0,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7550);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7550) = plVar8;
  *(undefined8 *)(param_1 + 0x7548) = uVar5;
                    /* try { // try from 00a6dd18 to 00b6dd27 has its CatchHandler @ 00a77d40 */
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
    (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00a6dd64 to 00b6ddbf has its CatchHandler @ 00a77d50 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  FUN_00752b90();
                    /* try { // try from 00a6e048 to 00b6e057 has its CatchHandler @ 00a77d3c */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330e90.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x16,1,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7580);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7580) = plVar8;
  *(undefined8 *)(param_1 + 0x7578) = uVar5;
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
                    /* try { // try from 00a6ddfc to 00b6de0b has its CatchHandler @ 00a77cbc */
    (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00a6de0c to 00b6de97 has its CatchHandler @ 00a63e3c */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
                    /* try { // try from 00a6e094 to 00b6e0e7 has its CatchHandler @ 00a77d4c */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330ea8.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x16,1,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7590);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7590) = plVar8;
  *(undefined8 *)(param_1 + 0x7588) = uVar5;
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
                    /* try { // try from 00a6de98 to 00b6dea7 has its CatchHandler @ 00a77ca8 */
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
                    /* try { // try from 00a6dea8 to 00b6df2f has its CatchHandler @ 00a63e3c */
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  iVar3 = FUN_0046c984(param_1);
  iVar4 = *(int *)(param_1 + 0xcb48);
  *(undefined4 *)((long)&fde_table_entry_00335f38.data_loc + param_1) = 0xe6;
  *(undefined4 *)((long)&fde_table_entry_00333c88.initial_loc + param_1) = 0x58;
  *(undefined8 *)((long)&fde_table_entry_00333c80.initial_loc + param_1) = DAT_002c3df8;
  *piVar1 = iVar4 * -0xe6;
  *(int *)((long)&fde_table_entry_00333c78.data_loc + param_1) = (int)((double)iVar3 * 0.5 + -255.0)
  ;
  *(undefined4 *)(param_1 + (long)iVar4 * 4 + 0xcb4c) = 1;
  FUN_009cc9e0(param_1);
                    /* try { // try from 00a6df30 to 00b6df3f has its CatchHandler @ 00a77ca8 */
  *(bool *)(param_1 + 0x332a24) = 0x1c < *(int *)(param_1 + 0xcb48);
  iVar4 = FUN_0046c984(param_1);
                    /* try { // try from 00a6df40 to 00b6dfc7 has its CatchHandler @ 00a63e3c */
  *(undefined2 *)((long)&fde_table_entry_00338400.data_loc + param_1) = 0;
  if (iVar4 < 0) {
    iVar4 = iVar4 + 1;
  }
  *(undefined1 *)((long)&fde_table_entry_00338320.initial_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00338328.data_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00338338.initial_loc + param_1) = 0;
  *(int *)((long)&fde_table_entry_00332078.data_loc + param_1) = iVar4 >> 1;
  FUN_00ab27e8(param_1);
  if (*(long *)(lVar2 + 0x28) == local_68) {
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
<a id="insn-00a6dadc"></a> `00a6dadc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a6dae0"></a> `00a6dae0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6dae4"></a> `00a6dae4` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dae8"></a> `00a6dae8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6daec"></a> `00a6daec` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6daf0"></a> `00a6daf0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a6daf4"></a> `00a6daf4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6daf8"></a> `00a6daf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a6dafc"></a> `00a6dafc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a6db00"></a> `00a6db00` | `b5 11 00 f0` | adrp x21,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6db04"></a> `00a6db04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6db08"></a> `00a6db08` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00a6db0c"></a> `00a6db0c` | `00 86 80 52` | mov w0,#0x430 | `FALL_THROUGH`
<a id="insn-00a6db10"></a> `00a6db10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6db14"></a> `00a6db14` | `a8 11 00 f0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6db18"></a> `00a6db18` | `a9 be 42 f9` | ldr x9,[x21, #0x578] | `FALL_THROUGH`
<a id="insn-00a6db1c"></a> `00a6db1c` | `0a b5 42 f9` | ldr x10,[x8, #0x568] | `FALL_THROUGH`
<a id="insn-00a6db20"></a> `00a6db20` | `09 b5 02 f9` | str x9,[x8, #0x568] | `FALL_THROUGH`
<a id="insn-00a6db24"></a> `00a6db24` | `aa be 02 f9` | str x10,[x21, #0x578] | `FALL_THROUGH`
<a id="insn-00a6db28"></a> `00a6db28` | `da a7 07 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6db2c"></a> `00a6db2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a6db30"></a> `00a6db30` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00a6db34"></a> `00a6db34` | `6c fc ff 97` | bl 0x00a6cce4 | `UNCONDITIONAL_CALL`
<a id="insn-00a6db38"></a> `00a6db38` | `68 e2 4c 91` | add x8,x19,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6db3c"></a> `00a6db3c` | `69 d6 4c 91` | add x9,x19,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6db40"></a> `00a6db40` | `6a ce 4c 91` | add x10,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6db44"></a> `00a6db44` | `6b ca 4c 91` | add x11,x19,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6db48"></a> `00a6db48` | `17 81 0c 91` | add x23,x8,#0x320 | `FALL_THROUGH`
<a id="insn-00a6db4c"></a> `00a6db4c` | `a0 be 42 f9` | ldr x0,[x21, #0x578] | `FALL_THROUGH`
<a id="insn-00a6db50"></a> `00a6db50` | `08 a7 8e 52` | mov w8,#0x7538 | `FALL_THROUGH`
<a id="insn-00a6db54"></a> `00a6db54` | `3b 7d 3b 91` | add x27,x9,#0xedf | `FALL_THROUGH`
<a id="insn-00a6db58"></a> `00a6db58` | `5a f1 31 91` | add x26,x10,#0xc7c | `FALL_THROUGH`
<a id="insn-00a6db5c"></a> `00a6db5c` | `78 d1 01 91` | add x24,x11,#0x74 | `FALL_THROUGH`
<a id="insn-00a6db60"></a> `00a6db60` | `7c 02 08 8b` | add x28,x19,x8 | `FALL_THROUGH`
<a id="insn-00a6db64"></a> `00a6db64` | `b4 be 02 f9` | str x20,[x21, #0x578] | `FALL_THROUGH`
<a id="insn-00a6db68"></a> `00a6db68` | `80 00 00 b4` | cbz x0,0x00a6db78 | `CONDITIONAL_JUMP`
<a id="insn-00a6db6c"></a> `00a6db6c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00a6db70"></a> `00a6db70` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a6db74"></a> `00a6db74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6db78"></a> `00a6db78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6db7c"></a> `00a6db7c` | `64 9f fd 97` | bl 0x009d590c | `UNCONDITIONAL_CALL`
<a id="insn-00a6db80"></a> `00a6db80` | `08 23 87 52` | mov w8,#0x3918 | `FALL_THROUGH`
<a id="insn-00a6db84"></a> `00a6db84` | `f9 77 87 92` | mov x25,#-0x3bc0 | `FALL_THROUGH`
<a id="insn-00a6db88"></a> `00a6db88` | `75 02 08 8b` | add x21,x19,x8 | `FALL_THROUGH`
<a id="insn-00a6db8c"></a> `00a6db8c` | `03 00 00 14` | b 0x00a6db98 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6db90"></a> `00a6db90` | `39 43 00 b1` | adds x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00a6db94"></a> `00a6db94` | `40 02 00 54` | b.eq 0x00a6dbdc | `CONDITIONAL_JUMP`
<a id="insn-00a6db98"></a> `00a6db98` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00a6db9c"></a> `00a6db9c` | `68 02 19 8b` | add x8,x19,x25 | `FALL_THROUGH`
<a id="insn-00a6dba0"></a> `00a6dba0` | `14 71 7a f9` | ldr x20,[x8, #0x74e0] | `FALL_THROUGH`
<a id="insn-00a6dba4"></a> `00a6dba4` | `a8 02 19 8b` | add x8,x21,x25 | `FALL_THROUGH`
<a id="insn-00a6dba8"></a> `00a6dba8` | `00 f1 8e 3d` | str q0,[x8, #0x3bc0] | `FALL_THROUGH`
<a id="insn-00a6dbac"></a> `00a6dbac` | `34 ff ff b4` | cbz x20,0x00a6db90 | `CONDITIONAL_JUMP`
<a id="insn-00a6dbb0"></a> `00a6dbb0` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dbb4"></a> `00a6dbb4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dbb8"></a> `00a6dbb8` | `4a 97 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dbbc"></a> `00a6dbbc` | `a0 fe ff b5` | cbnz x0,0x00a6db90 | `CONDITIONAL_JUMP`
<a id="insn-00a6dbc0"></a> `00a6dbc0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6dbc4"></a> `00a6dbc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dbc8"></a> `00a6dbc8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dbcc"></a> `00a6dbcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dbd0"></a> `00a6dbd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dbd4"></a> `00a6dbd4` | `ab a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dbd8"></a> `00a6dbd8` | `ee ff ff 17` | b 0x00a6db90 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6dbdc"></a> `00a6dbdc` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00a6dbe0"></a> `00a6dbe0` | `08 c3 26 91` | add x8,x24,#0x9b0 | `FALL_THROUGH`
<a id="insn-00a6dbe4"></a> `00a6dbe4` | `69 d6 4c 91` | add x9,x19,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6dbe8"></a> `00a6dbe8` | `1f db 04 f9` | str xzr,[x24, #0x9b0] | `FALL_THROUGH`
<a id="insn-00a6dbec"></a> `00a6dbec` | `b9 11 00 f0` | adrp x25,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6dbf0"></a> `00a6dbf0` | `39 e3 2c 91` | add x25,x25,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6dbf4"></a> `00a6dbf4` | `1f 61 00 f8` | stur xzr,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00a6dbf8"></a> `00a6dbf8` | `28 71 3b 91` | add x8,x9,#0xedc | `FALL_THROUGH`
<a id="insn-00a6dbfc"></a> `00a6dbfc` | `69 ce 4c 91` | add x9,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6dc00"></a> `00a6dc00` | `29 21 3e 91` | add x9,x9,#0xf88 | `FALL_THROUGH`
<a id="insn-00a6dc04"></a> `00a6dc04` | `1f 03 00 b9` | str wzr,[x24] | `FALL_THROUGH`
<a id="insn-00a6dc08"></a> `00a6dc08` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00a6dc0c"></a> `00a6dc0c` | `1f f1 00 b8` | stur wzr,[x8, #0xf] | `FALL_THROUGH`
<a id="insn-00a6dc10"></a> `00a6dc10` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a6dc14"></a> `00a6dc14` | `20 01 00 ad` | stp q0,q0,[x9] | `FALL_THROUGH`
<a id="insn-00a6dc18"></a> `00a6dc18` | `20 09 80 3d` | str q0,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a6dc1c"></a> `00a6dc1c` | `3f 19 00 f9` | str xzr,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dc20"></a> `00a6dc20` | `68 03 00 39` | strb w8,[x27] | `FALL_THROUGH`
<a id="insn-00a6dc24"></a> `00a6dc24` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00a6dc28"></a> `00a6dc28` | `68 1b 00 36` | tbz w8,#0x0,0x00a6df94 | `CONDITIONAL_JUMP`
<a id="insn-00a6dc2c"></a> `00a6dc2c` | `62 11 00 b0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00a6dc30"></a> `00a6dc30` | `b4 11 00 f0` | adrp x20,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6dc34"></a> `00a6dc34` | `94 02 2c 91` | add x20,x20,#0xb00 | `FALL_THROUGH`
<a id="insn-00a6dc38"></a> `00a6dc38` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00a6dc3c"></a> `00a6dc3c` | `69 c2 4c 91` | add x9,x19,#0x330, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6dc40"></a> `00a6dc40` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6dc44"></a> `00a6dc44` | `21 41 34 91` | add x1,x9,#0xd10 | `FALL_THROUGH`
<a id="insn-00a6dc48"></a> `00a6dc48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dc4c"></a> `00a6dc4c` | `c3 05 80 52` | mov w3,#0x2e | `FALL_THROUGH`
<a id="insn-00a6dc50"></a> `00a6dc50` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00a6dc54"></a> `00a6dc54` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00a6dc58"></a> `00a6dc58` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00a6dc5c"></a> `00a6dc5c` | `10 43 e8 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc60"></a> `00a6dc60` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6dc64"></a> `00a6dc64` | `75 a2 7a f9` | ldr x21,[x19, #0x7540] | `FALL_THROUGH`
<a id="insn-00a6dc68"></a> `00a6dc68` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00a6dc6c"></a> `00a6dc6c` | `80 03 80 3d` | str q0,[x28] | `FALL_THROUGH`
<a id="insn-00a6dc70"></a> `00a6dc70` | `75 01 00 b4` | cbz x21,0x00a6dc9c | `CONDITIONAL_JUMP`
<a id="insn-00a6dc74"></a> `00a6dc74` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dc78"></a> `00a6dc78` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dc7c"></a> `00a6dc7c` | `19 97 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc80"></a> `00a6dc80` | `e0 00 00 b5` | cbnz x0,0x00a6dc9c | `CONDITIONAL_JUMP`
<a id="insn-00a6dc84"></a> `00a6dc84` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dc88"></a> `00a6dc88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dc8c"></a> `00a6dc8c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dc90"></a> `00a6dc90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dc94"></a> `00a6dc94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dc98"></a> `00a6dc98` | `7a a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc9c"></a> `00a6dc9c` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dca0"></a> `00a6dca0` | `75 01 00 b4` | cbz x21,0x00a6dccc | `CONDITIONAL_JUMP`
<a id="insn-00a6dca4"></a> `00a6dca4` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dca8"></a> `00a6dca8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dcac"></a> `00a6dcac` | `0d 97 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dcb0"></a> `00a6dcb0` | `e0 00 00 b5` | cbnz x0,0x00a6dccc | `CONDITIONAL_JUMP`
<a id="insn-00a6dcb4"></a> `00a6dcb4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dcb8"></a> `00a6dcb8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dcbc"></a> `00a6dcbc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dcc0"></a> `00a6dcc0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dcc4"></a> `00a6dcc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dcc8"></a> `00a6dcc8` | `6e a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dccc"></a> `00a6dccc` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00a6dcd0"></a> `00a6dcd0` | `e8 18 00 36` | tbz w8,#0x0,0x00a6dfec | `CONDITIONAL_JUMP`
<a id="insn-00a6dcd4"></a> `00a6dcd4` | `62 11 00 b0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00a6dcd8"></a> `00a6dcd8` | `69 c2 4c 91` | add x9,x19,#0x330, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6dcdc"></a> `00a6dcdc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6dce0"></a> `00a6dce0` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00a6dce4"></a> `00a6dce4` | `21 a1 34 91` | add x1,x9,#0xd28 | `FALL_THROUGH`
<a id="insn-00a6dce8"></a> `00a6dce8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dcec"></a> `00a6dcec` | `03 03 80 52` | mov w3,#0x18 | `FALL_THROUGH`
<a id="insn-00a6dcf0"></a> `00a6dcf0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00a6dcf4"></a> `00a6dcf4` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00a6dcf8"></a> `00a6dcf8` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00a6dcfc"></a> `00a6dcfc` | `e8 42 e8 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd00"></a> `00a6dd00` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6dd04"></a> `00a6dd04` | `75 aa 7a f9` | ldr x21,[x19, #0x7550] | `FALL_THROUGH`
<a id="insn-00a6dd08"></a> `00a6dd08` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00a6dd0c"></a> `00a6dd0c` | `80 07 80 3d` | str q0,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dd10"></a> `00a6dd10` | `75 01 00 b4` | cbz x21,0x00a6dd3c | `CONDITIONAL_JUMP`
<a id="insn-00a6dd14"></a> `00a6dd14` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dd18"></a> `00a6dd18` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dd1c"></a> `00a6dd1c` | `f1 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd20"></a> `00a6dd20` | `e0 00 00 b5` | cbnz x0,0x00a6dd3c | `CONDITIONAL_JUMP`
<a id="insn-00a6dd24"></a> `00a6dd24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dd28"></a> `00a6dd28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dd2c"></a> `00a6dd2c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dd30"></a> `00a6dd30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dd34"></a> `00a6dd34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dd38"></a> `00a6dd38` | `52 a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd3c"></a> `00a6dd3c` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dd40"></a> `00a6dd40` | `75 01 00 b4` | cbz x21,0x00a6dd6c | `CONDITIONAL_JUMP`
<a id="insn-00a6dd44"></a> `00a6dd44` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dd48"></a> `00a6dd48` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dd4c"></a> `00a6dd4c` | `e5 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd50"></a> `00a6dd50` | `e0 00 00 b5` | cbnz x0,0x00a6dd6c | `CONDITIONAL_JUMP`
<a id="insn-00a6dd54"></a> `00a6dd54` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dd58"></a> `00a6dd58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dd5c"></a> `00a6dd5c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dd60"></a> `00a6dd60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dd64"></a> `00a6dd64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dd68"></a> `00a6dd68` | `46 a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd6c"></a> `00a6dd6c` | `89 93 f3 97` | bl 0x00752b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dd70"></a> `00a6dd70` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00a6dd74"></a> `00a6dd74` | `68 16 00 36` | tbz w8,#0x0,0x00a6e040 | `CONDITIONAL_JUMP`
<a id="insn-00a6dd78"></a> `00a6dd78` | `62 11 00 b0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00a6dd7c"></a> `00a6dd7c` | `69 c2 4c 91` | add x9,x19,#0x330, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6dd80"></a> `00a6dd80` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6dd84"></a> `00a6dd84` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00a6dd88"></a> `00a6dd88` | `21 41 3a 91` | add x1,x9,#0xe90 | `FALL_THROUGH`
<a id="insn-00a6dd8c"></a> `00a6dd8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dd90"></a> `00a6dd90` | `c3 02 80 52` | mov w3,#0x16 | `FALL_THROUGH`
<a id="insn-00a6dd94"></a> `00a6dd94` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00a6dd98"></a> `00a6dd98` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00a6dd9c"></a> `00a6dd9c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00a6dda0"></a> `00a6dda0` | `bf 42 e8 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00a6dda4"></a> `00a6dda4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6dda8"></a> `00a6dda8` | `75 c2 7a f9` | ldr x21,[x19, #0x7580] | `FALL_THROUGH`
<a id="insn-00a6ddac"></a> `00a6ddac` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00a6ddb0"></a> `00a6ddb0` | `80 13 80 3d` | str q0,[x28, #0x40] | `FALL_THROUGH`
<a id="insn-00a6ddb4"></a> `00a6ddb4` | `75 01 00 b4` | cbz x21,0x00a6dde0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ddb8"></a> `00a6ddb8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ddbc"></a> `00a6ddbc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6ddc0"></a> `00a6ddc0` | `c8 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ddc4"></a> `00a6ddc4` | `e0 00 00 b5` | cbnz x0,0x00a6dde0 | `CONDITIONAL_JUMP`
<a id="insn-00a6ddc8"></a> `00a6ddc8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6ddcc"></a> `00a6ddcc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6ddd0"></a> `00a6ddd0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ddd4"></a> `00a6ddd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6ddd8"></a> `00a6ddd8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dddc"></a> `00a6dddc` | `29 a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dde0"></a> `00a6dde0` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dde4"></a> `00a6dde4` | `75 01 00 b4` | cbz x21,0x00a6de10 | `CONDITIONAL_JUMP`
<a id="insn-00a6dde8"></a> `00a6dde8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a6ddec"></a> `00a6ddec` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6ddf0"></a> `00a6ddf0` | `bc 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ddf4"></a> `00a6ddf4` | `e0 00 00 b5` | cbnz x0,0x00a6de10 | `CONDITIONAL_JUMP`
<a id="insn-00a6ddf8"></a> `00a6ddf8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6ddfc"></a> `00a6ddfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6de00"></a> `00a6de00` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6de04"></a> `00a6de04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6de08"></a> `00a6de08` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6de0c"></a> `00a6de0c` | `1d a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6de10"></a> `00a6de10` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00a6de14"></a> `00a6de14` | `08 14 00 36` | tbz w8,#0x0,0x00a6e094 | `CONDITIONAL_JUMP`
<a id="insn-00a6de18"></a> `00a6de18` | `62 11 00 b0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00a6de1c"></a> `00a6de1c` | `69 c2 4c 91` | add x9,x19,#0x330, LSL #12 | `FALL_THROUGH`
<a id="insn-00a6de20"></a> `00a6de20` | `a0 11 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6de24"></a> `00a6de24` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00a6de28"></a> `00a6de28` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00a6de2c"></a> `00a6de2c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6de30"></a> `00a6de30` | `21 a1 3a 91` | add x1,x9,#0xea8 | `FALL_THROUGH`
<a id="insn-00a6de34"></a> `00a6de34` | `c3 02 80 52` | mov w3,#0x16 | `FALL_THROUGH`
<a id="insn-00a6de38"></a> `00a6de38` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00a6de3c"></a> `00a6de3c` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00a6de40"></a> `00a6de40` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00a6de44"></a> `00a6de44` | `96 42 e8 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00a6de48"></a> `00a6de48` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6de4c"></a> `00a6de4c` | `74 ca 7a f9` | ldr x20,[x19, #0x7590] | `FALL_THROUGH`
<a id="insn-00a6de50"></a> `00a6de50` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00a6de54"></a> `00a6de54` | `80 17 80 3d` | str q0,[x28, #0x50] | `FALL_THROUGH`
<a id="insn-00a6de58"></a> `00a6de58` | `74 01 00 b4` | cbz x20,0x00a6de84 | `CONDITIONAL_JUMP`
<a id="insn-00a6de5c"></a> `00a6de5c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a6de60"></a> `00a6de60` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6de64"></a> `00a6de64` | `9f 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6de68"></a> `00a6de68` | `e0 00 00 b5` | cbnz x0,0x00a6de84 | `CONDITIONAL_JUMP`
<a id="insn-00a6de6c"></a> `00a6de6c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6de70"></a> `00a6de70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6de74"></a> `00a6de74` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6de78"></a> `00a6de78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6de7c"></a> `00a6de7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6de80"></a> `00a6de80` | `00 a7 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6de84"></a> `00a6de84` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6de88"></a> `00a6de88` | `74 01 00 b4` | cbz x20,0x00a6deb4 | `CONDITIONAL_JUMP`
<a id="insn-00a6de8c"></a> `00a6de8c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a6de90"></a> `00a6de90` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6de94"></a> `00a6de94` | `93 96 07 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6de98"></a> `00a6de98` | `e0 00 00 b5` | cbnz x0,0x00a6deb4 | `CONDITIONAL_JUMP`
<a id="insn-00a6de9c"></a> `00a6de9c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6dea0"></a> `00a6dea0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6dea4"></a> `00a6dea4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dea8"></a> `00a6dea8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6deac"></a> `00a6deac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6deb0"></a> `00a6deb0` | `f4 a6 07 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00a6deb4"></a> `00a6deb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6deb8"></a> `00a6deb8` | `b3 fa e7 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00a6debc"></a> `00a6debc` | `08 00 dc d2` | mov x8,#0xe00000000000 | `FALL_THROUGH`
<a id="insn-00a6dec0"></a> `00a6dec0` | `00 00 62 1e` | scvtf d0,w0 | `FALL_THROUGH`
<a id="insn-00a6dec4"></a> `00a6dec4` | `01 10 6c 1e` | fmov d1,0x3fe0000000000000 | `FALL_THROUGH`
<a id="insn-00a6dec8"></a> `00a6dec8` | `e8 0d f8 f2` | movk x8,#0xc06f, LSL #48 | `FALL_THROUGH`
<a id="insn-00a6decc"></a> `00a6decc` | `14 69 99 52` | mov w20,#0xcb48 | `FALL_THROUGH`
<a id="insn-00a6ded0"></a> `00a6ded0` | `a9 c2 ff d0` | adrp x9,0x2c3000 | `FALL_THROUGH`
<a id="insn-00a6ded4"></a> `00a6ded4` | `02 01 67 9e` | fmov d2,x8 | `FALL_THROUGH`
<a id="insn-00a6ded8"></a> `00a6ded8` | `6b 6a b4 b8` | ldrsw x11,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a6dedc"></a> `00a6dedc` | `ac 1c 80 12` | mov w12,#0xffffff1a | `FALL_THROUGH`
<a id="insn-00a6dee0"></a> `00a6dee0` | `ca 1c 80 52` | mov w10,#0xe6 | `FALL_THROUGH`
<a id="insn-00a6dee4"></a> `00a6dee4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6dee8"></a> `00a6dee8` | `6a d3 05 b8` | stur w10,[x27, #0x5d] | `FALL_THROUGH`
<a id="insn-00a6deec"></a> `00a6deec` | `0a 0b 80 52` | mov w10,#0x58 | `FALL_THROUGH`
<a id="insn-00a6def0"></a> `00a6def0` | `00 08 41 1f` | fmadd d0,d0,d1,d2 | `FALL_THROUGH`
<a id="insn-00a6def4"></a> `00a6def4` | `4a 0f 00 b9` | str w10,[x26, #0xc] | `FALL_THROUGH`
<a id="insn-00a6def8"></a> `00a6def8` | `8a 69 99 52` | mov w10,#0xcb4c | `FALL_THROUGH`
<a id="insn-00a6defc"></a> `00a6defc` | `08 00 78 1e` | fcvtzs w8,d0 | `FALL_THROUGH`
<a id="insn-00a6df00"></a> `00a6df00` | `20 fd 46 fd` | ldr d0,[x9, #0xdf8] | `FALL_THROUGH`
<a id="insn-00a6df04"></a> `00a6df04` | `69 7d 0c 1b` | mul w9,w11,w12 | `FALL_THROUGH`
<a id="insn-00a6df08"></a> `00a6df08` | `40 43 00 fc` | stur d0,[x26, #0x4] | `FALL_THROUGH`
<a id="insn-00a6df0c"></a> `00a6df0c` | `09 03 00 b9` | str w9,[x24] | `FALL_THROUGH`
<a id="insn-00a6df10"></a> `00a6df10` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a6df14"></a> `00a6df14` | `48 03 00 b9` | str w8,[x26] | `FALL_THROUGH`
<a id="insn-00a6df18"></a> `00a6df18` | `68 0a 0b 8b` | add x8,x19,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00a6df1c"></a> `00a6df1c` | `09 69 2a b8` | str w9,[x8, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a6df20"></a> `00a6df20` | `b0 7a fd 97` | bl 0x009cc9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6df24"></a> `00a6df24` | `68 6a 74 b8` | ldr w8,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a6df28"></a> `00a6df28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6df2c"></a> `00a6df2c` | `1f 71 00 71` | cmp w8,#0x1c | `FALL_THROUGH`
<a id="insn-00a6df30"></a> `00a6df30` | `e8 d7 9f 1a` | cset w8,gt | `FALL_THROUGH`
<a id="insn-00a6df34"></a> `00a6df34` | `08 c3 26 39` | strb w8,[x24, #0x9b0] | `FALL_THROUGH`
<a id="insn-00a6df38"></a> `00a6df38` | `93 fa e7 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00a6df3c"></a> `00a6df3c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00a6df40"></a> `00a6df40` | `ff ca 01 79` | strh wzr,[x23, #0xe4] | `FALL_THROUGH`
<a id="insn-00a6df44"></a> `00a6df44` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-00a6df48"></a> `00a6df48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a6df4c"></a> `00a6df4c` | `ff 02 00 39` | strb wzr,[x23] | `FALL_THROUGH`
<a id="insn-00a6df50"></a> `00a6df50` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a6df54"></a> `00a6df54` | `ff 32 00 39` | strb wzr,[x23, #0xc] | `FALL_THROUGH`
<a id="insn-00a6df58"></a> `00a6df58` | `ff 62 00 39` | strb wzr,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00a6df5c"></a> `00a6df5c` | `08 0b 00 b9` | str w8,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00a6df60"></a> `00a6df60` | `22 12 01 94` | bl 0x00ab27e8 | `UNCONDITIONAL_CALL`
<a id="insn-00a6df64"></a> `00a6df64` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00a6df68"></a> `00a6df68` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6df6c"></a> `00a6df6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6df70"></a> `00a6df70` | `e1 0c 00 54` | b.ne 0x00a6e10c | `CONDITIONAL_JUMP`
<a id="insn-00a6df74"></a> `00a6df74` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a6df78"></a> `00a6df78` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a6df7c"></a> `00a6df7c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6df80"></a> `00a6df80` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6df84"></a> `00a6df84` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6df88"></a> `00a6df88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6df8c"></a> `00a6df8c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a6df90"></a> `00a6df90` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6df94"></a> `00a6df94` | `a0 11 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6df98"></a> `00a6df98` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6df9c"></a> `00a6df9c` | `ad a6 07 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dfa0"></a> `00a6dfa0` | `60 e4 ff 34` | cbz w0,0x00a6dc2c | `CONDITIONAL_JUMP`
<a id="insn-00a6dfa4"></a> `00a6dfa4` | `a1 11 00 f0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6dfa8"></a> `00a6dfa8` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00a6dfac"></a> `00a6dfac` | `80 d0 ff b0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00a6dfb0"></a> `00a6dfb0` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00a6dfb4"></a> `00a6dfb4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00a6dfb8"></a> `00a6dfb8` | `a2 0f 00 b0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00a6dfbc"></a> `00a6dfbc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00a6dfc0"></a> `00a6dfc0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6dfc4"></a> `00a6dfc4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00a6dfc8"></a> `00a6dfc8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00a6dfcc"></a> `00a6dfcc` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00a6dfd0"></a> `00a6dfd0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00a6dfd4"></a> `00a6dfd4` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dfd8"></a> `00a6dfd8` | `96 a6 07 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dfdc"></a> `00a6dfdc` | `a0 11 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6dfe0"></a> `00a6dfe0` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6dfe4"></a> `00a6dfe4` | `a3 a6 07 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dfe8"></a> `00a6dfe8` | `11 ff ff 17` | b 0x00a6dc2c | `UNCONDITIONAL_JUMP`
<a id="insn-00a6dfec"></a> `00a6dfec` | `a0 11 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6dff0"></a> `00a6dff0` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6dff4"></a> `00a6dff4` | `97 a6 07 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dff8"></a> `00a6dff8` | `e0 e6 ff 34` | cbz w0,0x00a6dcd4 | `CONDITIONAL_JUMP`
<a id="insn-00a6dffc"></a> `00a6dffc` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e000"></a> `00a6e000` | `80 d0 ff 90` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00a6e004"></a> `00a6e004` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00a6e008"></a> `00a6e008` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6e00c"></a> `00a6e00c` | `a2 0f 00 90` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00a6e010"></a> `00a6e010` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00a6e014"></a> `00a6e014` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6e018"></a> `00a6e018` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e01c"></a> `00a6e01c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a6e020"></a> `00a6e020` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a6e024"></a> `00a6e024` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00a6e028"></a> `00a6e028` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e02c"></a> `00a6e02c` | `81 a6 07 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e030"></a> `00a6e030` | `a0 11 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6e034"></a> `00a6e034` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6e038"></a> `00a6e038` | `8e a6 07 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e03c"></a> `00a6e03c` | `26 ff ff 17` | b 0x00a6dcd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6e040"></a> `00a6e040` | `a0 11 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6e044"></a> `00a6e044` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6e048"></a> `00a6e048` | `82 a6 07 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e04c"></a> `00a6e04c` | `60 e9 ff 34` | cbz w0,0x00a6dd78 | `CONDITIONAL_JUMP`
<a id="insn-00a6e050"></a> `00a6e050` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e054"></a> `00a6e054` | `80 d0 ff 90` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00a6e058"></a> `00a6e058` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00a6e05c"></a> `00a6e05c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6e060"></a> `00a6e060` | `a2 0f 00 90` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00a6e064"></a> `00a6e064` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00a6e068"></a> `00a6e068` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6e06c"></a> `00a6e06c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e070"></a> `00a6e070` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a6e074"></a> `00a6e074` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a6e078"></a> `00a6e078` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00a6e07c"></a> `00a6e07c` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e080"></a> `00a6e080` | `6c a6 07 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e084"></a> `00a6e084` | `a0 11 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6e088"></a> `00a6e088` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6e08c"></a> `00a6e08c` | `79 a6 07 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e090"></a> `00a6e090` | `3a ff ff 17` | b 0x00a6dd78 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6e094"></a> `00a6e094` | `a0 11 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6e098"></a> `00a6e098` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6e09c"></a> `00a6e09c` | `6d a6 07 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e0a0"></a> `00a6e0a0` | `c0 eb ff 34` | cbz w0,0x00a6de18 | `CONDITIONAL_JUMP`
<a id="insn-00a6e0a4"></a> `00a6e0a4` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e0a8"></a> `00a6e0a8` | `80 d0 ff 90` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00a6e0ac"></a> `00a6e0ac` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00a6e0b0"></a> `00a6e0b0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6e0b4"></a> `00a6e0b4` | `a2 0f 00 90` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00a6e0b8"></a> `00a6e0b8` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00a6e0bc"></a> `00a6e0bc` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6e0c0"></a> `00a6e0c0` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00a6e0c4"></a> `00a6e0c4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a6e0c8"></a> `00a6e0c8` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00a6e0cc"></a> `00a6e0cc` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00a6e0d0"></a> `00a6e0d0` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a6e0d4"></a> `00a6e0d4` | `57 a6 07 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e0d8"></a> `00a6e0d8` | `a0 11 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a6e0dc"></a> `00a6e0dc` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00a6e0e0"></a> `00a6e0e0` | `64 a6 07 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00a6e0e4"></a> `00a6e0e4` | `4d ff ff 17` | b 0x00a6de18 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6e10c"></a> `00a6e10c` | `75 a6 07 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6dadc`](#insn-00a6dadc) 範囲 `[['00a6dadc', '00a6db6b']]`
  - `CONDITIONAL_JUMP` [`00a6db68`](#insn-00a6db68) → [`00a6db78`](#insn-00a6db78)
  - `FALL_THROUGH` [`00a6db68`](#insn-00a6db68) → [`00a6db6c`](#insn-00a6db6c)
- ブロック [`00a6db6c`](#insn-00a6db6c) 範囲 `[['00a6db6c', '00a6db77']]`
  - `FALL_THROUGH` [`00a6db74`](#insn-00a6db74) → [`00a6db78`](#insn-00a6db78)
- ブロック [`00a6db78`](#insn-00a6db78) 範囲 `[['00a6db78', '00a6db8f']]`
  - `UNCONDITIONAL_JUMP` [`00a6db8c`](#insn-00a6db8c) → [`00a6db98`](#insn-00a6db98)
- ブロック [`00a6db90`](#insn-00a6db90) 範囲 `[['00a6db90', '00a6db97']]`
  - `CONDITIONAL_JUMP` [`00a6db94`](#insn-00a6db94) → [`00a6dbdc`](#insn-00a6dbdc)
  - `FALL_THROUGH` [`00a6db94`](#insn-00a6db94) → [`00a6db98`](#insn-00a6db98)
- ブロック [`00a6db98`](#insn-00a6db98) 範囲 `[['00a6db98', '00a6dbaf']]`
  - `CONDITIONAL_JUMP` [`00a6dbac`](#insn-00a6dbac) → [`00a6db90`](#insn-00a6db90)
  - `FALL_THROUGH` [`00a6dbac`](#insn-00a6dbac) → [`00a6dbb0`](#insn-00a6dbb0)
- ブロック [`00a6dbb0`](#insn-00a6dbb0) 範囲 `[['00a6dbb0', '00a6dbbf']]`
  - `CONDITIONAL_JUMP` [`00a6dbbc`](#insn-00a6dbbc) → [`00a6db90`](#insn-00a6db90)
  - `FALL_THROUGH` [`00a6dbbc`](#insn-00a6dbbc) → [`00a6dbc0`](#insn-00a6dbc0)
- ブロック [`00a6dbc0`](#insn-00a6dbc0) 範囲 `[['00a6dbc0', '00a6dbdb']]`
  - `UNCONDITIONAL_JUMP` [`00a6dbd8`](#insn-00a6dbd8) → [`00a6db90`](#insn-00a6db90)
- ブロック [`00a6dbdc`](#insn-00a6dbdc) 範囲 `[['00a6dbdc', '00a6dc2b']]`
  - `CONDITIONAL_JUMP` [`00a6dc28`](#insn-00a6dc28) → [`00a6df94`](#insn-00a6df94)
  - `FALL_THROUGH` [`00a6dc28`](#insn-00a6dc28) → [`00a6dc2c`](#insn-00a6dc2c)
- ブロック [`00a6dc2c`](#insn-00a6dc2c) 範囲 `[['00a6dc2c', '00a6dc73']]`
  - `CONDITIONAL_JUMP` [`00a6dc70`](#insn-00a6dc70) → [`00a6dc9c`](#insn-00a6dc9c)
  - `FALL_THROUGH` [`00a6dc70`](#insn-00a6dc70) → [`00a6dc74`](#insn-00a6dc74)
- ブロック [`00a6dc74`](#insn-00a6dc74) 範囲 `[['00a6dc74', '00a6dc7f']]`
  - `FALL_THROUGH` [`00a6dc7c`](#insn-00a6dc7c) → [`00a6dc80`](#insn-00a6dc80)
- ブロック [`00a6dc80`](#insn-00a6dc80) 範囲 `[['00a6dc80', '00a6dc83']]`
  - `CONDITIONAL_JUMP` [`00a6dc80`](#insn-00a6dc80) → [`00a6dc9c`](#insn-00a6dc9c)
  - `FALL_THROUGH` [`00a6dc80`](#insn-00a6dc80) → [`00a6dc84`](#insn-00a6dc84)
- ブロック [`00a6dc84`](#insn-00a6dc84) 範囲 `[['00a6dc84', '00a6dc9b']]`
  - `FALL_THROUGH` [`00a6dc98`](#insn-00a6dc98) → [`00a6dc9c`](#insn-00a6dc9c)
- ブロック [`00a6dc9c`](#insn-00a6dc9c) 範囲 `[['00a6dc9c', '00a6dca3']]`
  - `CONDITIONAL_JUMP` [`00a6dca0`](#insn-00a6dca0) → [`00a6dccc`](#insn-00a6dccc)
  - `FALL_THROUGH` [`00a6dca0`](#insn-00a6dca0) → [`00a6dca4`](#insn-00a6dca4)
- ブロック [`00a6dca4`](#insn-00a6dca4) 範囲 `[['00a6dca4', '00a6dcb3']]`
  - `CONDITIONAL_JUMP` [`00a6dcb0`](#insn-00a6dcb0) → [`00a6dccc`](#insn-00a6dccc)
  - `FALL_THROUGH` [`00a6dcb0`](#insn-00a6dcb0) → [`00a6dcb4`](#insn-00a6dcb4)
- ブロック [`00a6dcb4`](#insn-00a6dcb4) 範囲 `[['00a6dcb4', '00a6dccb']]`
  - `FALL_THROUGH` [`00a6dcc8`](#insn-00a6dcc8) → [`00a6dccc`](#insn-00a6dccc)
- ブロック [`00a6dccc`](#insn-00a6dccc) 範囲 `[['00a6dccc', '00a6dcd3']]`
  - `CONDITIONAL_JUMP` [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dfec`](#insn-00a6dfec)
  - `FALL_THROUGH` [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dcd4`](#insn-00a6dcd4)
- ブロック [`00a6dcd4`](#insn-00a6dcd4) 範囲 `[['00a6dcd4', '00a6dd13']]`
  - `CONDITIONAL_JUMP` [`00a6dd10`](#insn-00a6dd10) → [`00a6dd3c`](#insn-00a6dd3c)
  - `FALL_THROUGH` [`00a6dd10`](#insn-00a6dd10) → [`00a6dd14`](#insn-00a6dd14)
- ブロック [`00a6dd14`](#insn-00a6dd14) 範囲 `[['00a6dd14', '00a6dd17']]`
  - `FALL_THROUGH` [`00a6dd14`](#insn-00a6dd14) → [`00a6dd18`](#insn-00a6dd18)
- ブロック [`00a6dd18`](#insn-00a6dd18) 範囲 `[['00a6dd18', '00a6dd23']]`
  - `CONDITIONAL_JUMP` [`00a6dd20`](#insn-00a6dd20) → [`00a6dd3c`](#insn-00a6dd3c)
  - `FALL_THROUGH` [`00a6dd20`](#insn-00a6dd20) → [`00a6dd24`](#insn-00a6dd24)
- ブロック [`00a6dd24`](#insn-00a6dd24) 範囲 `[['00a6dd24', '00a6dd3b']]`
  - `FALL_THROUGH` [`00a6dd38`](#insn-00a6dd38) → [`00a6dd3c`](#insn-00a6dd3c)
- ブロック [`00a6dd3c`](#insn-00a6dd3c) 範囲 `[['00a6dd3c', '00a6dd43']]`
  - `CONDITIONAL_JUMP` [`00a6dd40`](#insn-00a6dd40) → [`00a6dd6c`](#insn-00a6dd6c)
  - `FALL_THROUGH` [`00a6dd40`](#insn-00a6dd40) → [`00a6dd44`](#insn-00a6dd44)
- ブロック [`00a6dd44`](#insn-00a6dd44) 範囲 `[['00a6dd44', '00a6dd53']]`
  - `CONDITIONAL_JUMP` [`00a6dd50`](#insn-00a6dd50) → [`00a6dd6c`](#insn-00a6dd6c)
  - `FALL_THROUGH` [`00a6dd50`](#insn-00a6dd50) → [`00a6dd54`](#insn-00a6dd54)
- ブロック [`00a6dd54`](#insn-00a6dd54) 範囲 `[['00a6dd54', '00a6dd63']]`
  - `FALL_THROUGH` [`00a6dd60`](#insn-00a6dd60) → [`00a6dd64`](#insn-00a6dd64)
- ブロック [`00a6dd64`](#insn-00a6dd64) 範囲 `[['00a6dd64', '00a6dd6b']]`
  - `FALL_THROUGH` [`00a6dd68`](#insn-00a6dd68) → [`00a6dd6c`](#insn-00a6dd6c)
- ブロック [`00a6dd6c`](#insn-00a6dd6c) 範囲 `[['00a6dd6c', '00a6dd77']]`
  - `CONDITIONAL_JUMP` [`00a6dd74`](#insn-00a6dd74) → [`00a6e040`](#insn-00a6e040)
  - `FALL_THROUGH` [`00a6dd74`](#insn-00a6dd74) → [`00a6dd78`](#insn-00a6dd78)
- ブロック [`00a6dd78`](#insn-00a6dd78) 範囲 `[['00a6dd78', '00a6ddb7']]`
  - `CONDITIONAL_JUMP` [`00a6ddb4`](#insn-00a6ddb4) → [`00a6dde0`](#insn-00a6dde0)
  - `FALL_THROUGH` [`00a6ddb4`](#insn-00a6ddb4) → [`00a6ddb8`](#insn-00a6ddb8)
- ブロック [`00a6ddb8`](#insn-00a6ddb8) 範囲 `[['00a6ddb8', '00a6ddc7']]`
  - `CONDITIONAL_JUMP` [`00a6ddc4`](#insn-00a6ddc4) → [`00a6dde0`](#insn-00a6dde0)
  - `FALL_THROUGH` [`00a6ddc4`](#insn-00a6ddc4) → [`00a6ddc8`](#insn-00a6ddc8)
- ブロック [`00a6ddc8`](#insn-00a6ddc8) 範囲 `[['00a6ddc8', '00a6dddf']]`
  - `FALL_THROUGH` [`00a6dddc`](#insn-00a6dddc) → [`00a6dde0`](#insn-00a6dde0)
- ブロック [`00a6dde0`](#insn-00a6dde0) 範囲 `[['00a6dde0', '00a6dde7']]`
  - `CONDITIONAL_JUMP` [`00a6dde4`](#insn-00a6dde4) → [`00a6de10`](#insn-00a6de10)
  - `FALL_THROUGH` [`00a6dde4`](#insn-00a6dde4) → [`00a6dde8`](#insn-00a6dde8)
- ブロック [`00a6dde8`](#insn-00a6dde8) 範囲 `[['00a6dde8', '00a6ddf7']]`
  - `CONDITIONAL_JUMP` [`00a6ddf4`](#insn-00a6ddf4) → [`00a6de10`](#insn-00a6de10)
  - `FALL_THROUGH` [`00a6ddf4`](#insn-00a6ddf4) → [`00a6ddf8`](#insn-00a6ddf8)
- ブロック [`00a6ddf8`](#insn-00a6ddf8) 範囲 `[['00a6ddf8', '00a6ddfb']]`
  - `FALL_THROUGH` [`00a6ddf8`](#insn-00a6ddf8) → [`00a6ddfc`](#insn-00a6ddfc)
- ブロック [`00a6ddfc`](#insn-00a6ddfc) 範囲 `[['00a6ddfc', '00a6de0b']]`
  - `FALL_THROUGH` [`00a6de08`](#insn-00a6de08) → [`00a6de0c`](#insn-00a6de0c)
- ブロック [`00a6de0c`](#insn-00a6de0c) 範囲 `[['00a6de0c', '00a6de0f']]`
  - `FALL_THROUGH` [`00a6de0c`](#insn-00a6de0c) → [`00a6de10`](#insn-00a6de10)
- ブロック [`00a6de10`](#insn-00a6de10) 範囲 `[['00a6de10', '00a6de17']]`
  - `CONDITIONAL_JUMP` [`00a6de14`](#insn-00a6de14) → [`00a6e094`](#insn-00a6e094)
  - `FALL_THROUGH` [`00a6de14`](#insn-00a6de14) → [`00a6de18`](#insn-00a6de18)
- ブロック [`00a6de18`](#insn-00a6de18) 範囲 `[['00a6de18', '00a6de5b']]`
  - `CONDITIONAL_JUMP` [`00a6de58`](#insn-00a6de58) → [`00a6de84`](#insn-00a6de84)
  - `FALL_THROUGH` [`00a6de58`](#insn-00a6de58) → [`00a6de5c`](#insn-00a6de5c)
- ブロック [`00a6de5c`](#insn-00a6de5c) 範囲 `[['00a6de5c', '00a6de6b']]`
  - `CONDITIONAL_JUMP` [`00a6de68`](#insn-00a6de68) → [`00a6de84`](#insn-00a6de84)
  - `FALL_THROUGH` [`00a6de68`](#insn-00a6de68) → [`00a6de6c`](#insn-00a6de6c)
- ブロック [`00a6de6c`](#insn-00a6de6c) 範囲 `[['00a6de6c', '00a6de83']]`
  - `FALL_THROUGH` [`00a6de80`](#insn-00a6de80) → [`00a6de84`](#insn-00a6de84)
- ブロック [`00a6de84`](#insn-00a6de84) 範囲 `[['00a6de84', '00a6de8b']]`
  - `CONDITIONAL_JUMP` [`00a6de88`](#insn-00a6de88) → [`00a6deb4`](#insn-00a6deb4)
  - `FALL_THROUGH` [`00a6de88`](#insn-00a6de88) → [`00a6de8c`](#insn-00a6de8c)
- ブロック [`00a6de8c`](#insn-00a6de8c) 範囲 `[['00a6de8c', '00a6de97']]`
  - `FALL_THROUGH` [`00a6de94`](#insn-00a6de94) → [`00a6de98`](#insn-00a6de98)
- ブロック [`00a6de98`](#insn-00a6de98) 範囲 `[['00a6de98', '00a6de9b']]`
  - `CONDITIONAL_JUMP` [`00a6de98`](#insn-00a6de98) → [`00a6deb4`](#insn-00a6deb4)
  - `FALL_THROUGH` [`00a6de98`](#insn-00a6de98) → [`00a6de9c`](#insn-00a6de9c)
- ブロック [`00a6de9c`](#insn-00a6de9c) 範囲 `[['00a6de9c', '00a6dea7']]`
  - `FALL_THROUGH` [`00a6dea4`](#insn-00a6dea4) → [`00a6dea8`](#insn-00a6dea8)
- ブロック [`00a6dea8`](#insn-00a6dea8) 範囲 `[['00a6dea8', '00a6deb3']]`
  - `FALL_THROUGH` [`00a6deb0`](#insn-00a6deb0) → [`00a6deb4`](#insn-00a6deb4)
- ブロック [`00a6deb4`](#insn-00a6deb4) 範囲 `[['00a6deb4', '00a6df2f']]`
  - `FALL_THROUGH` [`00a6df2c`](#insn-00a6df2c) → [`00a6df30`](#insn-00a6df30)
- ブロック [`00a6df30`](#insn-00a6df30) 範囲 `[['00a6df30', '00a6df3f']]`
  - `FALL_THROUGH` [`00a6df3c`](#insn-00a6df3c) → [`00a6df40`](#insn-00a6df40)
- ブロック [`00a6df40`](#insn-00a6df40) 範囲 `[['00a6df40', '00a6df73']]`
  - `CONDITIONAL_JUMP` [`00a6df70`](#insn-00a6df70) → [`00a6e10c`](#insn-00a6e10c)
  - `FALL_THROUGH` [`00a6df70`](#insn-00a6df70) → [`00a6df74`](#insn-00a6df74)
- ブロック [`00a6df74`](#insn-00a6df74) 範囲 `[['00a6df74', '00a6df93']]`
- ブロック [`00a6df94`](#insn-00a6df94) 範囲 `[['00a6df94', '00a6dfa3']]`
  - `CONDITIONAL_JUMP` [`00a6dfa0`](#insn-00a6dfa0) → [`00a6dc2c`](#insn-00a6dc2c)
  - `FALL_THROUGH` [`00a6dfa0`](#insn-00a6dfa0) → [`00a6dfa4`](#insn-00a6dfa4)
- ブロック [`00a6dfa4`](#insn-00a6dfa4) 範囲 `[['00a6dfa4', '00a6dfc7']]`
  - `FALL_THROUGH` [`00a6dfc4`](#insn-00a6dfc4) → [`00a6dfc8`](#insn-00a6dfc8)
- ブロック [`00a6dfc8`](#insn-00a6dfc8) 範囲 `[['00a6dfc8', '00a6dfd7']]`
  - `FALL_THROUGH` [`00a6dfd4`](#insn-00a6dfd4) → [`00a6dfd8`](#insn-00a6dfd8)
- ブロック [`00a6dfd8`](#insn-00a6dfd8) 範囲 `[['00a6dfd8', '00a6dfeb']]`
  - `UNCONDITIONAL_JUMP` [`00a6dfe8`](#insn-00a6dfe8) → [`00a6dc2c`](#insn-00a6dc2c)
- ブロック [`00a6dfec`](#insn-00a6dfec) 範囲 `[['00a6dfec', '00a6dffb']]`
  - `CONDITIONAL_JUMP` [`00a6dff8`](#insn-00a6dff8) → [`00a6dcd4`](#insn-00a6dcd4)
  - `FALL_THROUGH` [`00a6dff8`](#insn-00a6dff8) → [`00a6dffc`](#insn-00a6dffc)
- ブロック [`00a6dffc`](#insn-00a6dffc) 範囲 `[['00a6dffc', '00a6e03f']]`
  - `UNCONDITIONAL_JUMP` [`00a6e03c`](#insn-00a6e03c) → [`00a6dcd4`](#insn-00a6dcd4)
- ブロック [`00a6e040`](#insn-00a6e040) 範囲 `[['00a6e040', '00a6e047']]`
  - `FALL_THROUGH` [`00a6e044`](#insn-00a6e044) → [`00a6e048`](#insn-00a6e048)
- ブロック [`00a6e048`](#insn-00a6e048) 範囲 `[['00a6e048', '00a6e04f']]`
  - `CONDITIONAL_JUMP` [`00a6e04c`](#insn-00a6e04c) → [`00a6dd78`](#insn-00a6dd78)
  - `FALL_THROUGH` [`00a6e04c`](#insn-00a6e04c) → [`00a6e050`](#insn-00a6e050)
- ブロック [`00a6e050`](#insn-00a6e050) 範囲 `[['00a6e050', '00a6e093']]`
  - `UNCONDITIONAL_JUMP` [`00a6e090`](#insn-00a6e090) → [`00a6dd78`](#insn-00a6dd78)
- ブロック [`00a6e094`](#insn-00a6e094) 範囲 `[['00a6e094', '00a6e0a3']]`
  - `CONDITIONAL_JUMP` [`00a6e0a0`](#insn-00a6e0a0) → [`00a6de18`](#insn-00a6de18)
  - `FALL_THROUGH` [`00a6e0a0`](#insn-00a6e0a0) → [`00a6e0a4`](#insn-00a6e0a4)
- ブロック [`00a6e0a4`](#insn-00a6e0a4) 範囲 `[['00a6e0a4', '00a6e0e7']]`
  - `UNCONDITIONAL_JUMP` [`00a6e0e4`](#insn-00a6e0e4) → [`00a6de18`](#insn-00a6de18)
- ブロック [`00a6e10c`](#insn-00a6e10c) 範囲 `[['00a6e10c', '00a6e10f']]`

## 命令位置別の参照

- [`00a6dae0`](#insn-00a6dae0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dae4`](#insn-00a6dae4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dae8`](#insn-00a6dae8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6daec`](#insn-00a6daec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6daf0`](#insn-00a6daf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6daf4`](#insn-00a6daf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6db10`](#insn-00a6db10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6db18`](#insn-00a6db18) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db1c`](#insn-00a6db1c) → `00ca4568`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db20`](#insn-00a6db20) → `00ca4568`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db24`](#insn-00a6db24) → `00ca4578`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db28`](#insn-00a6db28) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00a6db34`](#insn-00a6db34) → [`00a6cce4`](../00a6c/00a6cce4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6cce4` · 推定シンボル `None` · 推定型 `None`
- [`00a6db4c`](#insn-00a6db4c) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db64`](#insn-00a6db64) → `00ca4578`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6db68`](#insn-00a6db68) → [`00a6db78`](#insn-00a6db78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6db7c`](#insn-00a6db7c) → [`009d590c`](../009d5/009d590c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009d590c` · 推定シンボル `None` · 推定型 `None`
- [`00a6db8c`](#insn-00a6db8c) → [`00a6db98`](#insn-00a6db98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6db94`](#insn-00a6db94) → [`00a6dbdc`](#insn-00a6dbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbac`](#insn-00a6dbac) → [`00a6db90`](#insn-00a6db90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbb8`](#insn-00a6dbb8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbbc`](#insn-00a6dbbc) → [`00a6db90`](#insn-00a6db90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbd4`](#insn-00a6dbd4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbd8`](#insn-00a6dbd8) → [`00a6db90`](#insn-00a6db90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbe8`](#insn-00a6dbe8) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dbf4`](#insn-00a6dbf4) → `00332a2a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc04`](#insn-00a6dc04) → `00332074`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc08`](#insn-00a6dc08) → `00335edc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc0c`](#insn-00a6dc0c) → `00335eeb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc14`](#insn-00a6dc14) → `00333f88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc14`](#insn-00a6dc14) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc18`](#insn-00a6dc18) → `00333fa8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc1c`](#insn-00a6dc1c) → `00333fb8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc20`](#insn-00a6dc20) → `00335edf`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6dc24`](#insn-00a6dc24) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dc28`](#insn-00a6dc28) → [`00a6df94`](#insn-00a6df94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc38`](#insn-00a6dc38) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6dc38`](#insn-00a6dc38) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dc48`](#insn-00a6dc48) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dc5c`](#insn-00a6dc5c) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc60`](#insn-00a6dc60) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc68`](#insn-00a6dc68) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc70`](#insn-00a6dc70) → [`00a6dc9c`](#insn-00a6dc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc7c`](#insn-00a6dc7c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc80`](#insn-00a6dc80) → [`00a6dc9c`](#insn-00a6dc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc98`](#insn-00a6dc98) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc9c`](#insn-00a6dc9c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dca0`](#insn-00a6dca0) → [`00a6dccc`](#insn-00a6dccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcac`](#insn-00a6dcac) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcb0`](#insn-00a6dcb0) → [`00a6dccc`](#insn-00a6dccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcc8`](#insn-00a6dcc8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dccc`](#insn-00a6dccc) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dcd0`](#insn-00a6dcd0) → [`00a6dfec`](#insn-00a6dfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dce0`](#insn-00a6dce0) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6dce0`](#insn-00a6dce0) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dce8`](#insn-00a6dce8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dcfc`](#insn-00a6dcfc) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd00`](#insn-00a6dd00) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd08`](#insn-00a6dd08) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd10`](#insn-00a6dd10) → [`00a6dd3c`](#insn-00a6dd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd1c`](#insn-00a6dd1c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd20`](#insn-00a6dd20) → [`00a6dd3c`](#insn-00a6dd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd38`](#insn-00a6dd38) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd3c`](#insn-00a6dd3c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd40`](#insn-00a6dd40) → [`00a6dd6c`](#insn-00a6dd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd4c`](#insn-00a6dd4c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd50`](#insn-00a6dd50) → [`00a6dd6c`](#insn-00a6dd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd68`](#insn-00a6dd68) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd6c`](#insn-00a6dd6c) → [`00752b90`](../00752/00752b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00752b90` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd70`](#insn-00a6dd70) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dd74`](#insn-00a6dd74) → [`00a6e040`](#insn-00a6e040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd84`](#insn-00a6dd84) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6dd84`](#insn-00a6dd84) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dd8c`](#insn-00a6dd8c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dda0`](#insn-00a6dda0) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00a6dda4`](#insn-00a6dda4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddac`](#insn-00a6ddac) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddb4`](#insn-00a6ddb4) → [`00a6dde0`](#insn-00a6dde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddc0`](#insn-00a6ddc0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddc4`](#insn-00a6ddc4) → [`00a6dde0`](#insn-00a6dde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dddc`](#insn-00a6dddc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6dde0`](#insn-00a6dde0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dde4`](#insn-00a6dde4) → [`00a6de10`](#insn-00a6de10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddf0`](#insn-00a6ddf0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6ddf4`](#insn-00a6ddf4) → [`00a6de10`](#insn-00a6de10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de0c`](#insn-00a6de0c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6de10`](#insn-00a6de10) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6de14`](#insn-00a6de14) → [`00a6e094`](#insn-00a6e094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de24`](#insn-00a6de24) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6de28`](#insn-00a6de28) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6de28`](#insn-00a6de28) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6de44`](#insn-00a6de44) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00a6de48`](#insn-00a6de48) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de50`](#insn-00a6de50) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de58`](#insn-00a6de58) → [`00a6de84`](#insn-00a6de84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de64`](#insn-00a6de64) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6de68`](#insn-00a6de68) → [`00a6de84`](#insn-00a6de84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de80`](#insn-00a6de80) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6de84`](#insn-00a6de84) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de88`](#insn-00a6de88) → [`00a6deb4`](#insn-00a6deb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6de94`](#insn-00a6de94) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6de98`](#insn-00a6de98) → [`00a6deb4`](#insn-00a6deb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6deb0`](#insn-00a6deb0) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00a6deb8`](#insn-00a6deb8) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00a6dee8`](#insn-00a6dee8) → `00335f3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6def4`](#insn-00a6def4) → `00333c88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df00`](#insn-00a6df00) → `002c3df8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6df08`](#insn-00a6df08) → `00333c80`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df0c`](#insn-00a6df0c) → `00332074`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df14`](#insn-00a6df14) → `00333c7c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df20`](#insn-00a6df20) → [`009cc9e0`](../009cc/009cc9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009cc9e0` · 推定シンボル `None` · 推定型 `None`
- [`00a6df34`](#insn-00a6df34) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df38`](#insn-00a6df38) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00a6df40`](#insn-00a6df40) → `00338404`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df4c`](#insn-00a6df4c) → `00338320`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df54`](#insn-00a6df54) → `0033832c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df58`](#insn-00a6df58) → `00338338`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df5c`](#insn-00a6df5c) → `0033207c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00a6df60`](#insn-00a6df60) → [`00ab27e8`](../00ab2/00ab27e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab27e8` · 推定シンボル `None` · 推定型 `None`
- [`00a6df68`](#insn-00a6df68) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df70`](#insn-00a6df70) → [`00a6e10c`](#insn-00a6e10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df74`](#insn-00a6df74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df78`](#insn-00a6df78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df7c`](#insn-00a6df7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df80`](#insn-00a6df80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df84`](#insn-00a6df84) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df88`](#insn-00a6df88) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6df98`](#insn-00a6df98) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6df9c`](#insn-00a6df9c) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfa0`](#insn-00a6dfa0) → [`00a6dc2c`](#insn-00a6dc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfa8`](#insn-00a6dfa8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfb0`](#insn-00a6dfb0) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfbc`](#insn-00a6dfbc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6dfc0`](#insn-00a6dfc0) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfc4`](#insn-00a6dfc4) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfc4`](#insn-00a6dfc4) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfcc`](#insn-00a6dfcc) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfcc`](#insn-00a6dfcc) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfd0`](#insn-00a6dfd0) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfd4`](#insn-00a6dfd4) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfd4`](#insn-00a6dfd4) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfd4`](#insn-00a6dfd4) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6dfd8`](#insn-00a6dfd8) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfe0`](#insn-00a6dfe0) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dfe4`](#insn-00a6dfe4) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00a6dfe8`](#insn-00a6dfe8) → [`00a6dc2c`](#insn-00a6dc2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dff0`](#insn-00a6dff0) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6dff4`](#insn-00a6dff4) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00a6dff8`](#insn-00a6dff8) → [`00a6dcd4`](#insn-00a6dcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e004`](#insn-00a6e004) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00a6e008`](#insn-00a6e008) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e010`](#insn-00a6e010) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6e014`](#insn-00a6e014) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e014`](#insn-00a6e014) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e01c`](#insn-00a6e01c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e020`](#insn-00a6e020) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e020`](#insn-00a6e020) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e024`](#insn-00a6e024) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e028`](#insn-00a6e028) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e028`](#insn-00a6e028) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e028`](#insn-00a6e028) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e02c`](#insn-00a6e02c) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00a6e034`](#insn-00a6e034) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6e038`](#insn-00a6e038) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00a6e03c`](#insn-00a6e03c) → [`00a6dcd4`](#insn-00a6dcd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e044`](#insn-00a6e044) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6e048`](#insn-00a6e048) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00a6e04c`](#insn-00a6e04c) → [`00a6dd78`](#insn-00a6dd78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e058`](#insn-00a6e058) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00a6e05c`](#insn-00a6e05c) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e064`](#insn-00a6e064) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6e068`](#insn-00a6e068) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e068`](#insn-00a6e068) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e070`](#insn-00a6e070) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e074`](#insn-00a6e074) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e074`](#insn-00a6e074) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e078`](#insn-00a6e078) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e07c`](#insn-00a6e07c) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e07c`](#insn-00a6e07c) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e07c`](#insn-00a6e07c) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e080`](#insn-00a6e080) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00a6e088`](#insn-00a6e088) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6e08c`](#insn-00a6e08c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00a6e090`](#insn-00a6e090) → [`00a6dd78`](#insn-00a6dd78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e098`](#insn-00a6e098) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6e09c`](#insn-00a6e09c) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00a6e0a0`](#insn-00a6e0a0) → [`00a6de18`](#insn-00a6de18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e0ac`](#insn-00a6e0ac) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00a6e0b0`](#insn-00a6e0b0) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0b8`](#insn-00a6e0b8) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6e0bc`](#insn-00a6e0bc) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0bc`](#insn-00a6e0bc) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0c4`](#insn-00a6e0c4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0c8`](#insn-00a6e0c8) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0c8`](#insn-00a6e0c8) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0cc`](#insn-00a6e0cc) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0d0`](#insn-00a6e0d0) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0d0`](#insn-00a6e0d0) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0d0`](#insn-00a6e0d0) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a6e0d4`](#insn-00a6e0d4) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00a6e0dc`](#insn-00a6e0dc) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a6e0e0`](#insn-00a6e0e0) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00a6e0e4`](#insn-00a6e0e4) → [`00a6de18`](#insn-00a6de18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6e10c`](#insn-00a6e10c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6dae0`](#insn-00a6dae0)

~~~json
{
  "source": "00a6dae0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dae4`](#insn-00a6dae4)

~~~json
{
  "source": "00a6dae4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dae8`](#insn-00a6dae8)

~~~json
{
  "source": "00a6dae8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6daec`](#insn-00a6daec)

~~~json
{
  "source": "00a6daec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6daf0`](#insn-00a6daf0)

~~~json
{
  "source": "00a6daf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6daf4`](#insn-00a6daf4)

~~~json
{
  "source": "00a6daf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6db10`](#insn-00a6db10)

~~~json
{
  "source": "00a6db10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6db18`](#insn-00a6db18)

~~~json
{
  "source": "00a6db18",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db1c`](#insn-00a6db1c)

~~~json
{
  "source": "00a6db1c",
  "target": "00ca4568",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4568",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db20`](#insn-00a6db20)

~~~json
{
  "source": "00a6db20",
  "target": "00ca4568",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4568",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db24`](#insn-00a6db24)

~~~json
{
  "source": "00a6db24",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db28`](#insn-00a6db28)

~~~json
{
  "source": "00a6db28",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6db34`](#insn-00a6db34)

~~~json
{
  "source": "00a6db34",
  "target": "00a6cce4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6db4c`](#insn-00a6db4c)

~~~json
{
  "source": "00a6db4c",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db64`](#insn-00a6db64)

~~~json
{
  "source": "00a6db64",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6db68`](#insn-00a6db68)

~~~json
{
  "source": "00a6db68",
  "target": "00a6db78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6db7c`](#insn-00a6db7c)

~~~json
{
  "source": "00a6db7c",
  "target": "009d590c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6db8c`](#insn-00a6db8c)

~~~json
{
  "source": "00a6db8c",
  "target": "00a6db98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6db94`](#insn-00a6db94)

~~~json
{
  "source": "00a6db94",
  "target": "00a6dbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbac`](#insn-00a6dbac)

~~~json
{
  "source": "00a6dbac",
  "target": "00a6db90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbb8`](#insn-00a6dbb8)

~~~json
{
  "source": "00a6dbb8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dbbc`](#insn-00a6dbbc)

~~~json
{
  "source": "00a6dbbc",
  "target": "00a6db90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbd4`](#insn-00a6dbd4)

~~~json
{
  "source": "00a6dbd4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dbd8`](#insn-00a6dbd8)

~~~json
{
  "source": "00a6dbd8",
  "target": "00a6db90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbe8`](#insn-00a6dbe8)

~~~json
{
  "source": "00a6dbe8",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "38f9680084480900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dbf4`](#insn-00a6dbf4)

~~~json
{
  "source": "00a6dbf4",
  "target": "00332a2a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 2,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3cf9680098480900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc04`](#insn-00a6dc04)

~~~json
{
  "source": "00a6dc04",
  "target": "00332074",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332070",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d40462006c250900",
  "capture_start": "00332070",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc08`](#insn-00a6dc08)

~~~json
{
  "source": "00a6dc08",
  "target": "00335edc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335ed8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "586c750034fe0900",
  "capture_start": "00335ed8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc0c`](#insn-00a6dc0c)

~~~json
{
  "source": "00a6dc0c",
  "target": "00335eeb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335ee8",
  "offset": 3,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "0c6d750080fe0900",
  "capture_start": "00335ee8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc14`](#insn-00a6dc14)

~~~json
{
  "source": "00a6dc14",
  "target": "00333f88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f88",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c06c00e88e0900",
  "capture_start": "00333f88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc14`](#insn-00a6dc14)

~~~json
{
  "source": "00a6dc14",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00cb6c00108f0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc18`](#insn-00a6dc18)

~~~json
{
  "source": "00a6dc18",
  "target": "00333fa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fa8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "48cd6c00908f0900",
  "capture_start": "00333fa8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc1c`](#insn-00a6dc1c)

~~~json
{
  "source": "00a6dc1c",
  "target": "00333fb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fb8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "00d06c00d8271100",
  "capture_start": "00333fb8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc20`](#insn-00a6dc20)

~~~json
{
  "source": "00a6dc20",
  "target": "00335edf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335ed8",
  "offset": 7,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "586c750034fe0900",
  "capture_start": "00335ed8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6dc24`](#insn-00a6dc24)

~~~json
{
  "source": "00a6dc24",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dc28`](#insn-00a6dc28)

~~~json
{
  "source": "00a6dc28",
  "target": "00a6df94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc38`](#insn-00a6dc38)

~~~json
{
  "source": "00a6dc38",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dc38`](#insn-00a6dc38)

~~~json
{
  "source": "00a6dc38",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dc48`](#insn-00a6dc48)

~~~json
{
  "source": "00a6dc48",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dc5c`](#insn-00a6dc5c)

~~~json
{
  "source": "00a6dc5c",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc60`](#insn-00a6dc60)

~~~json
{
  "source": "00a6dc60",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc68`](#insn-00a6dc68)

~~~json
{
  "source": "00a6dc68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc70`](#insn-00a6dc70)

~~~json
{
  "source": "00a6dc70",
  "target": "00a6dc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc7c`](#insn-00a6dc7c)

~~~json
{
  "source": "00a6dc7c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc80`](#insn-00a6dc80)

~~~json
{
  "source": "00a6dc80",
  "target": "00a6dc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc98`](#insn-00a6dc98)

~~~json
{
  "source": "00a6dc98",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc9c`](#insn-00a6dc9c)

~~~json
{
  "source": "00a6dc9c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dca0`](#insn-00a6dca0)

~~~json
{
  "source": "00a6dca0",
  "target": "00a6dccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcac`](#insn-00a6dcac)

~~~json
{
  "source": "00a6dcac",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dcb0`](#insn-00a6dcb0)

~~~json
{
  "source": "00a6dcb0",
  "target": "00a6dccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcc8`](#insn-00a6dcc8)

~~~json
{
  "source": "00a6dcc8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dccc`](#insn-00a6dccc)

~~~json
{
  "source": "00a6dccc",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dcd0`](#insn-00a6dcd0)

~~~json
{
  "source": "00a6dcd0",
  "target": "00a6dfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dce0`](#insn-00a6dce0)

~~~json
{
  "source": "00a6dce0",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dce0`](#insn-00a6dce0)

~~~json
{
  "source": "00a6dce0",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dce8`](#insn-00a6dce8)

~~~json
{
  "source": "00a6dce8",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dcfc`](#insn-00a6dcfc)

~~~json
{
  "source": "00a6dcfc",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd00`](#insn-00a6dd00)

~~~json
{
  "source": "00a6dd00",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd08`](#insn-00a6dd08)

~~~json
{
  "source": "00a6dd08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd10`](#insn-00a6dd10)

~~~json
{
  "source": "00a6dd10",
  "target": "00a6dd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd1c`](#insn-00a6dd1c)

~~~json
{
  "source": "00a6dd1c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd20`](#insn-00a6dd20)

~~~json
{
  "source": "00a6dd20",
  "target": "00a6dd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd38`](#insn-00a6dd38)

~~~json
{
  "source": "00a6dd38",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd3c`](#insn-00a6dd3c)

~~~json
{
  "source": "00a6dd3c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd40`](#insn-00a6dd40)

~~~json
{
  "source": "00a6dd40",
  "target": "00a6dd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd4c`](#insn-00a6dd4c)

~~~json
{
  "source": "00a6dd4c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd50`](#insn-00a6dd50)

~~~json
{
  "source": "00a6dd50",
  "target": "00a6dd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd68`](#insn-00a6dd68)

~~~json
{
  "source": "00a6dd68",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd6c`](#insn-00a6dd6c)

~~~json
{
  "source": "00a6dd6c",
  "target": "00752b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dd70`](#insn-00a6dd70)

~~~json
{
  "source": "00a6dd70",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dd74`](#insn-00a6dd74)

~~~json
{
  "source": "00a6dd74",
  "target": "00a6e040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd84`](#insn-00a6dd84)

~~~json
{
  "source": "00a6dd84",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dd84`](#insn-00a6dd84)

~~~json
{
  "source": "00a6dd84",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dd8c`](#insn-00a6dd8c)

~~~json
{
  "source": "00a6dd8c",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dda0`](#insn-00a6dda0)

~~~json
{
  "source": "00a6dda0",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dda4`](#insn-00a6dda4)

~~~json
{
  "source": "00a6dda4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ddac`](#insn-00a6ddac)

~~~json
{
  "source": "00a6ddac",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ddb4`](#insn-00a6ddb4)

~~~json
{
  "source": "00a6ddb4",
  "target": "00a6dde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ddc0`](#insn-00a6ddc0)

~~~json
{
  "source": "00a6ddc0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ddc4`](#insn-00a6ddc4)

~~~json
{
  "source": "00a6ddc4",
  "target": "00a6dde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dddc`](#insn-00a6dddc)

~~~json
{
  "source": "00a6dddc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dde0`](#insn-00a6dde0)

~~~json
{
  "source": "00a6dde0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dde4`](#insn-00a6dde4)

~~~json
{
  "source": "00a6dde4",
  "target": "00a6de10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ddf0`](#insn-00a6ddf0)

~~~json
{
  "source": "00a6ddf0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ddf4`](#insn-00a6ddf4)

~~~json
{
  "source": "00a6ddf4",
  "target": "00a6de10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de0c`](#insn-00a6de0c)

~~~json
{
  "source": "00a6de0c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6de10`](#insn-00a6de10)

~~~json
{
  "source": "00a6de10",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6de14`](#insn-00a6de14)

~~~json
{
  "source": "00a6de14",
  "target": "00a6e094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de24`](#insn-00a6de24)

~~~json
{
  "source": "00a6de24",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6de28`](#insn-00a6de28)

~~~json
{
  "source": "00a6de28",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6de28`](#insn-00a6de28)

~~~json
{
  "source": "00a6de28",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6de44`](#insn-00a6de44)

~~~json
{
  "source": "00a6de44",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6de48`](#insn-00a6de48)

~~~json
{
  "source": "00a6de48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de50`](#insn-00a6de50)

~~~json
{
  "source": "00a6de50",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de58`](#insn-00a6de58)

~~~json
{
  "source": "00a6de58",
  "target": "00a6de84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de64`](#insn-00a6de64)

~~~json
{
  "source": "00a6de64",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6de68`](#insn-00a6de68)

~~~json
{
  "source": "00a6de68",
  "target": "00a6de84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de80`](#insn-00a6de80)

~~~json
{
  "source": "00a6de80",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6de84`](#insn-00a6de84)

~~~json
{
  "source": "00a6de84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de88`](#insn-00a6de88)

~~~json
{
  "source": "00a6de88",
  "target": "00a6deb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6de94`](#insn-00a6de94)

~~~json
{
  "source": "00a6de94",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6de98`](#insn-00a6de98)

~~~json
{
  "source": "00a6de98",
  "target": "00a6deb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6deb0`](#insn-00a6deb0)

~~~json
{
  "source": "00a6deb0",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6deb8`](#insn-00a6deb8)

~~~json
{
  "source": "00a6deb8",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dee8`](#insn-00a6dee8)

~~~json
{
  "source": "00a6dee8",
  "target": "00335f3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "bc7d750068ff0900",
  "capture_start": "00335f38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6def4`](#insn-00a6def4)

~~~json
{
  "source": "00a6def4",
  "target": "00333c88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c88",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8456b0018820900",
  "capture_start": "00333c88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df00`](#insn-00a6df00)

~~~json
{
  "source": "00a6df00",
  "target": "002c3df8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c3df8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "e50100007d010000",
  "capture_start": "002c3df8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df08`](#insn-00a6df08)

~~~json
{
  "source": "00a6df08",
  "target": "00333c80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c80",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "443b6b00cc810900",
  "capture_start": "00333c80",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df0c`](#insn-00a6df0c)

~~~json
{
  "source": "00a6df0c",
  "target": "00332074",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332070",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d40462006c250900",
  "capture_start": "00332070",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df14`](#insn-00a6df14)

~~~json
{
  "source": "00a6df14",
  "target": "00333c7c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333c78",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "383a6b0094810900",
  "capture_start": "00333c78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df20`](#insn-00a6df20)

~~~json
{
  "source": "00a6df20",
  "target": "009cc9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6df34`](#insn-00a6df34)

~~~json
{
  "source": "00a6df34",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "38f9680084480900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df38`](#insn-00a6df38)

~~~json
{
  "source": "00a6df38",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6df40`](#insn-00a6df40)

~~~json
{
  "source": "00a6df40",
  "target": "00338404",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00338400",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "40d07d00147b0a00",
  "capture_start": "00338400",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df4c`](#insn-00a6df4c)

~~~json
{
  "source": "00a6df4c",
  "target": "00338320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00338320",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "74cc7d004c780a00",
  "capture_start": "00338320",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df54`](#insn-00a6df54)

~~~json
{
  "source": "00a6df54",
  "target": "0033832c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00338328",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "90cc7d0060780a00",
  "capture_start": "00338328",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df58`](#insn-00a6df58)

~~~json
{
  "source": "00a6df58",
  "target": "00338338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00338338",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "a0cc7d0088780a00",
  "capture_start": "00338338",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df5c`](#insn-00a6df5c)

~~~json
{
  "source": "00a6df5c",
  "target": "0033207c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332078",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d804620080250900",
  "capture_start": "00332078",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a6df60`](#insn-00a6df60)

~~~json
{
  "source": "00a6df60",
  "target": "00ab27e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6df68`](#insn-00a6df68)

~~~json
{
  "source": "00a6df68",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df70`](#insn-00a6df70)

~~~json
{
  "source": "00a6df70",
  "target": "00a6e10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df74`](#insn-00a6df74)

~~~json
{
  "source": "00a6df74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df78`](#insn-00a6df78)

~~~json
{
  "source": "00a6df78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df7c`](#insn-00a6df7c)

~~~json
{
  "source": "00a6df7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df80`](#insn-00a6df80)

~~~json
{
  "source": "00a6df80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df84`](#insn-00a6df84)

~~~json
{
  "source": "00a6df84",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df88`](#insn-00a6df88)

~~~json
{
  "source": "00a6df88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6df98`](#insn-00a6df98)

~~~json
{
  "source": "00a6df98",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6df9c`](#insn-00a6df9c)

~~~json
{
  "source": "00a6df9c",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dfa0`](#insn-00a6dfa0)

~~~json
{
  "source": "00a6dfa0",
  "target": "00a6dc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dfa8`](#insn-00a6dfa8)

~~~json
{
  "source": "00a6dfa8",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfb0`](#insn-00a6dfb0)

~~~json
{
  "source": "00a6dfb0",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dfbc`](#insn-00a6dfbc)

~~~json
{
  "source": "00a6dfbc",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dfc0`](#insn-00a6dfc0)

~~~json
{
  "source": "00a6dfc0",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfc4`](#insn-00a6dfc4)

~~~json
{
  "source": "00a6dfc4",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfc4`](#insn-00a6dfc4)

~~~json
{
  "source": "00a6dfc4",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfcc`](#insn-00a6dfcc)

~~~json
{
  "source": "00a6dfcc",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfcc`](#insn-00a6dfcc)

~~~json
{
  "source": "00a6dfcc",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfd0`](#insn-00a6dfd0)

~~~json
{
  "source": "00a6dfd0",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfd4`](#insn-00a6dfd4)

~~~json
{
  "source": "00a6dfd4",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfd4`](#insn-00a6dfd4)

~~~json
{
  "source": "00a6dfd4",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfd4`](#insn-00a6dfd4)

~~~json
{
  "source": "00a6dfd4",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfd8`](#insn-00a6dfd8)

~~~json
{
  "source": "00a6dfd8",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dfe0`](#insn-00a6dfe0)

~~~json
{
  "source": "00a6dfe0",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dfe4`](#insn-00a6dfe4)

~~~json
{
  "source": "00a6dfe4",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dfe8`](#insn-00a6dfe8)

~~~json
{
  "source": "00a6dfe8",
  "target": "00a6dc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dff0`](#insn-00a6dff0)

~~~json
{
  "source": "00a6dff0",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6dff4`](#insn-00a6dff4)

~~~json
{
  "source": "00a6dff4",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dff8`](#insn-00a6dff8)

~~~json
{
  "source": "00a6dff8",
  "target": "00a6dcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e004`](#insn-00a6e004)

~~~json
{
  "source": "00a6e004",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e008`](#insn-00a6e008)

~~~json
{
  "source": "00a6e008",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e010`](#insn-00a6e010)

~~~json
{
  "source": "00a6e010",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6e014`](#insn-00a6e014)

~~~json
{
  "source": "00a6e014",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e014`](#insn-00a6e014)

~~~json
{
  "source": "00a6e014",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e01c`](#insn-00a6e01c)

~~~json
{
  "source": "00a6e01c",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e020`](#insn-00a6e020)

~~~json
{
  "source": "00a6e020",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e020`](#insn-00a6e020)

~~~json
{
  "source": "00a6e020",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e024`](#insn-00a6e024)

~~~json
{
  "source": "00a6e024",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e028`](#insn-00a6e028)

~~~json
{
  "source": "00a6e028",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e028`](#insn-00a6e028)

~~~json
{
  "source": "00a6e028",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e028`](#insn-00a6e028)

~~~json
{
  "source": "00a6e028",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e02c`](#insn-00a6e02c)

~~~json
{
  "source": "00a6e02c",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e034`](#insn-00a6e034)

~~~json
{
  "source": "00a6e034",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e038`](#insn-00a6e038)

~~~json
{
  "source": "00a6e038",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e03c`](#insn-00a6e03c)

~~~json
{
  "source": "00a6e03c",
  "target": "00a6dcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e044`](#insn-00a6e044)

~~~json
{
  "source": "00a6e044",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e048`](#insn-00a6e048)

~~~json
{
  "source": "00a6e048",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e04c`](#insn-00a6e04c)

~~~json
{
  "source": "00a6e04c",
  "target": "00a6dd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e058`](#insn-00a6e058)

~~~json
{
  "source": "00a6e058",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e05c`](#insn-00a6e05c)

~~~json
{
  "source": "00a6e05c",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e064`](#insn-00a6e064)

~~~json
{
  "source": "00a6e064",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6e068`](#insn-00a6e068)

~~~json
{
  "source": "00a6e068",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e068`](#insn-00a6e068)

~~~json
{
  "source": "00a6e068",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e070`](#insn-00a6e070)

~~~json
{
  "source": "00a6e070",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e074`](#insn-00a6e074)

~~~json
{
  "source": "00a6e074",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e074`](#insn-00a6e074)

~~~json
{
  "source": "00a6e074",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e078`](#insn-00a6e078)

~~~json
{
  "source": "00a6e078",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e07c`](#insn-00a6e07c)

~~~json
{
  "source": "00a6e07c",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e07c`](#insn-00a6e07c)

~~~json
{
  "source": "00a6e07c",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e07c`](#insn-00a6e07c)

~~~json
{
  "source": "00a6e07c",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e080`](#insn-00a6e080)

~~~json
{
  "source": "00a6e080",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e088`](#insn-00a6e088)

~~~json
{
  "source": "00a6e088",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e08c`](#insn-00a6e08c)

~~~json
{
  "source": "00a6e08c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e090`](#insn-00a6e090)

~~~json
{
  "source": "00a6e090",
  "target": "00a6dd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e098`](#insn-00a6e098)

~~~json
{
  "source": "00a6e098",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e09c`](#insn-00a6e09c)

~~~json
{
  "source": "00a6e09c",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e0a0`](#insn-00a6e0a0)

~~~json
{
  "source": "00a6e0a0",
  "target": "00a6de18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e0ac`](#insn-00a6e0ac)

~~~json
{
  "source": "00a6e0ac",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e0b0`](#insn-00a6e0b0)

~~~json
{
  "source": "00a6e0b0",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0b8`](#insn-00a6e0b8)

~~~json
{
  "source": "00a6e0b8",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6e0bc`](#insn-00a6e0bc)

~~~json
{
  "source": "00a6e0bc",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0bc`](#insn-00a6e0bc)

~~~json
{
  "source": "00a6e0bc",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0c4`](#insn-00a6e0c4)

~~~json
{
  "source": "00a6e0c4",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0c8`](#insn-00a6e0c8)

~~~json
{
  "source": "00a6e0c8",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0c8`](#insn-00a6e0c8)

~~~json
{
  "source": "00a6e0c8",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0cc`](#insn-00a6e0cc)

~~~json
{
  "source": "00a6e0cc",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0d0`](#insn-00a6e0d0)

~~~json
{
  "source": "00a6e0d0",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0d0`](#insn-00a6e0d0)

~~~json
{
  "source": "00a6e0d0",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0d0`](#insn-00a6e0d0)

~~~json
{
  "source": "00a6e0d0",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0d4`](#insn-00a6e0d4)

~~~json
{
  "source": "00a6e0d4",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e0dc`](#insn-00a6e0dc)

~~~json
{
  "source": "00a6e0dc",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a6e0e0`](#insn-00a6e0e0)

~~~json
{
  "source": "00a6e0e0",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6e0e4`](#insn-00a6e0e4)

~~~json
{
  "source": "00a6e0e4",
  "target": "00a6de18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6e10c`](#insn-00a6e10c)

~~~json
{
  "source": "00a6e10c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
