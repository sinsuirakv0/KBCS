# 00a3deac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3de58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3de58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0061.md#compare-dd31a243e7e34640224f79bb3df28c92)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a3eea0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3eea0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0062.md#compare-726d653f21cfb5ed4314a6c7c1c2ccdd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3deac",
  "name": "FUN_00a3deac",
  "size": 860,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "556940a629d67a17dee56e10754618742b8f360fd54277dedc22d36e7b0fecec",
  "source_text_sha256": "556940a629d67a17dee56e10754618742b8f360fd54277dedc22d36e7b0fecec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3deac",
        "00a3e203"
      ],
      [
        "00a3e264",
        "00a3e267"
      ]
    ],
    "bytes_sha256": "d0466e2dc3fdb9feebce7a258f7853aaea9fdf889ff6918f1af9291f3a54319a",
    "instruction_count": 215,
    "instruction_bytes": 860,
    "body_bytes": 860,
    "indirect": 3,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00856e84](../00856/00856e84.md)

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)
- [0066d11c](../0066d/0066d11c.md)
- [0086a200](../0086a/0086a200.md)
- [009ccbd0](../009cc/009ccbd0.md)
- [00a3ab1c](../00a3a/00a3ab1c.md)
- [00a3f3a0](../00a3f/00a3f3a0.md)
- [00a40d3c](../00a40/00a40d3c.md)
- [00a40d40](../00a40/00a40d40.md)
- [00a40ddc](../00a40/00a40ddc.md)
- [00a40de0](../00a40/00a40de0.md)
- [00ac7b74](../00ac7/00ac7b74.md)
- [00ac9b2c](../00ac9/00ac9b2c.md)
- [00ac9b5c](../00ac9/00ac9b5c.md)
- [00ac9fd0](../00ac9/00ac9fd0.md)
- [00acab44](../00aca/00acab44.md)
- [00acb024](../00acb/00acb024.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7315 bytes

~~~c

void FUN_00a3deac(undefined *param_1)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  void *__ptr;
  long lVar4;
  undefined ***pppuVar5;
  undefined ***pppuVar6;
  long lVar7;
  undefined **local_110;
  undefined *local_108;
  long local_100;
  void *local_f8;
  long *plStack_f0;
  undefined8 local_e8;
  long *local_e0;
  long local_d8;
  long local_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined8 uStack_b0;
  undefined4 local_a8;
  long *local_a0;
  long local_98;
  long local_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined4 uStack_70;
  undefined4 uStack_6c;
  undefined4 uStack_68;
  undefined8 uStack_64;
  long local_58;
  
  pppuVar5 = &local_110;
  pppuVar6 = &local_110;
  lVar1 = tpidr_el0;
                    /* try { // try from 00a3ded4 to 00b3dedb has its CatchHandler @ 00a3e784 */
  local_58 = *(long *)(lVar1 + 0x28);
  FUN_0066d11c(0x51);
  FUN_00a3ab1c(&local_110,*(undefined4 *)(param_1 + 0x1d08));
                    /* try { // try from 00a3defc to 00b3df1f has its CatchHandler @ 00a3e83c */
  FUN_0086a200(param_1 + 0x1c50,*(undefined8 *)(param_1 + 0x1c58));
  *(long *)(param_1 + 0x1c60) = local_100;
  *(undefined ***)(param_1 + 0x1c50) = local_110;
  *(undefined **)(param_1 + 0x1c58) = local_108;
  if (local_100 == 0) {
    *(undefined **)(param_1 + 0x1c50) = param_1 + 0x1c58;
  }
  else {
    local_110 = &local_108;
    *(undefined **)(local_108 + 0x10) = param_1 + 0x1c58;
    local_108 = (undefined *)0x0;
    local_100 = 0;
  }
  __ptr = *(void **)(param_1 + 0x1c68);
                    /* try { // try from 00a3df48 to 00b3df57 has its CatchHandler @ 00a3e2e8 */
  if (__ptr != (void *)0x0) {
    *(void **)(param_1 + 0x1c70) = __ptr;
    _ZdlPv(__ptr);
    *(undefined8 *)(param_1 + 0x1c68) = 0;
    *(undefined8 *)(param_1 + 0x1c70) = 0;
                    /* try { // try from 00a3df58 to 00b3df63 has its CatchHandler @ 00a3e2e4 */
    *(undefined8 *)(param_1 + 0x1c78) = 0;
  }
  uVar3 = local_e8;
  plVar2 = plStack_f0;
                    /* try { // try from 00a3df68 to 00b3df6b has its CatchHandler @ 00a3e2d0 */
                    /* try { // try from 00a3df6c to 00b3df77 has its CatchHandler @ 00a3e2cc */
  plStack_f0 = (void *)0x0;
  local_e8 = 0;
  *(undefined8 *)(param_1 + 0x1c78) = uVar3;
  *(long **)(param_1 + 0x1c70) = plVar2;
  *(void **)(param_1 + 0x1c68) = local_f8;
  local_f8 = (void *)0x0;
  FUN_005c17dc(param_1 + 0x1c80,*(undefined8 *)(param_1 + 0x1c88));
  *(long *)(param_1 + 0x1c90) = local_d0;
  *(long **)(param_1 + 0x1c80) = local_e0;
  *(long *)(param_1 + 0x1c88) = local_d8;
  if (local_d0 == 0) {
    *(undefined **)(param_1 + 0x1c80) = param_1 + 0x1c88;
  }
  else {
    local_e0 = &local_d8;
    *(undefined **)(local_d8 + 0x10) = param_1 + 0x1c88;
    local_d8 = 0;
    local_d0 = 0;
  }
                    /* try { // try from 00a3dfc0 to 00b3dfcf has its CatchHandler @ 00a3e2ac */
                    /* try { // try from 00a3dfd0 to 00b3dfdb has its CatchHandler @ 00a3e278 */
  *(undefined4 *)(param_1 + 0x1cb8) = local_a8;
  *(undefined8 *)(param_1 + 0x1ca0) = uStack_c0;
  *(undefined8 *)(param_1 + 0x1c98) = local_c8;
  *(undefined8 *)(param_1 + 0x1cb0) = uStack_b0;
  *(undefined8 *)(param_1 + 0x1ca8) = local_b8;
  FUN_005c17dc(param_1 + 0x1cc0,*(undefined8 *)(param_1 + 0x1cc8));
  *(long *)(param_1 + 0x1cd0) = local_90;
  *(long **)(param_1 + 0x1cc0) = local_a0;
  *(long *)(param_1 + 0x1cc8) = local_98;
  if (local_90 == 0) {
    *(undefined **)(param_1 + 0x1cc0) = param_1 + 0x1cc8;
  }
  else {
    local_a0 = &local_98;
    *(undefined **)(local_98 + 0x10) = param_1 + 0x1cc8;
    local_98 = 0;
    local_90 = 0;
  }
  *(undefined8 *)(param_1 + 0x1ce0) = uStack_80;
  *(undefined8 *)(param_1 + 0x1cd8) = local_88;
  *(ulong *)(param_1 + 0x1cf0) = CONCAT44(uStack_6c,uStack_70);
  *(undefined8 *)(param_1 + 0x1ce8) = local_78;
  *(undefined8 *)(param_1 + 0x1cfc) = uStack_64;
  *(ulong *)(param_1 + 0x1cf4) = CONCAT44(uStack_68,uStack_6c);
  FUN_005c17dc(&local_a0,local_98);
  FUN_005c17dc(&local_e0,local_d8);
  if (local_f8 != (void *)0x0) {
    plStack_f0 = local_f8;
    _ZdlPv(local_f8);
  }
  FUN_0086a200(&local_110,local_108);
  plVar2 = DAT_00ca4a68;
  DAT_00ca4a68 = DAT_00ca4a78;
  DAT_00ca4a78 = plVar2;
  lVar4 = _Znwm(0x4c8);
  FUN_00a3f3a0(lVar4,param_1);
  if (DAT_00ca4a78 == (long *)0x0) {
LAB_00a3e0c0:
    DAT_00ca4a78 = (long *)lVar4;
    lVar7 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8b460,0);
  }
  else {
    lVar7 = *DAT_00ca4a78;
    DAT_00ca4a78 = (long *)lVar4;
    (**(code **)(lVar7 + 8))();
    lVar7 = 0;
    lVar4 = (long)DAT_00ca4a78;
    if (DAT_00ca4a78 != (long *)0x0) goto LAB_00a3e0c0;
  }
  FUN_009ccbd0(param_1);
  FUN_00ac7b74((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1));
  FUN_00acb024((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1),0);
  local_110 = &PTR_FUN_00c8b6a8;
  plStack_f0 = (long *)&local_110;
  FUN_00acab44((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1),&local_110
              );
  if ((undefined ***)plStack_f0 == &local_110) {
    lVar4 = 0x20;
                    /* try { // try from 00a3e140 to 00b3e15b has its CatchHandler @ 00a3e8bc */
LAB_00a3e144:
    (**(code **)((long)*pppuVar5 + lVar4))();
  }
  else if (plStack_f0 != (long *)0x0) {
    lVar4 = 0x28;
    pppuVar5 = (undefined ***)plStack_f0;
    goto LAB_00a3e144;
  }
  FUN_00ac9b2c((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1),
               *(undefined8 *)(lVar7 + 200),1,*(undefined8 *)(lVar7 + 0x1f8),0);
                    /* try { // try from 00a3e170 to 00b3e173 has its CatchHandler @ 00a3e6c0 */
  local_110 = &PTR_FUN_00c8b728;
  local_108 = param_1;
  plStack_f0 = (long *)&local_110;
                    /* try { // try from 00a3e188 to 00b3e18f has its CatchHandler @ 00a3e484 */
  FUN_00ac9b5c((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1),
               lVar7 + 0xa8,400,&local_110);
  if ((undefined ***)plStack_f0 == &local_110) {
                    /* catch() { ... } // from try @ 00a3d5a0 with catch @ 00a3e1a8
                       try { // try from 00a3e1a8 to 00b3ee93 has its CatchHandler @ 00a3b7c4 */
    lVar4 = 0x20;
  }
  else {
    if (plStack_f0 == (long *)0x0) goto LAB_00a3e1bc;
    lVar4 = 0x28;
    pppuVar6 = (undefined ***)plStack_f0;
                    /* try { // try from 00a3e1a4 to 00b3e1a7 has its CatchHandler @ 00a3e6c0 */
  }
                    /* catch() { ... } // from try @ 00a3d678 with catch @ 00a3e1b0 */
  (**(code **)((long)*pppuVar6 + lVar4))();
LAB_00a3e1bc:
  FUN_00ac9fd0((undefined *)((long)&fde_table_entry_00337d90.initial_loc + (long)param_1),
               lVar7 + 0xa8,*(undefined8 *)(lVar7 + 0xf8),0x191);
  FUN_0066d11c(0x52);
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00a3d668 with catch @ 00a3e1ec */
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00a3d5ac with catch @ 00a3e264 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3deac"></a> `00a3deac` | `ff 43 04 d1` | sub sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00a3deb0"></a> `00a3deb0` | `fd 7b 0c a9` | stp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a3deb4"></a> `00a3deb4` | `fc 67 0d a9` | stp x28,x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a3deb8"></a> `00a3deb8` | `f8 5f 0e a9` | stp x24,x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00a3debc"></a> `00a3debc` | `f6 57 0f a9` | stp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a3dec0"></a> `00a3dec0` | `f4 4f 10 a9` | stp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a3dec4"></a> `00a3dec4` | `fd 03 03 91` | add x29,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00a3dec8"></a> `00a3dec8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a3decc"></a> `00a3decc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3ded0"></a> `00a3ded0` | `20 0a 80 52` | mov w0,#0x51 | `FALL_THROUGH`
<a id="insn-00a3ded4"></a> `00a3ded4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a3ded8"></a> `00a3ded8` | `f4 03 00 91` | mov x20,sp | `FALL_THROUGH`
<a id="insn-00a3dedc"></a> `00a3dedc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3dee0"></a> `00a3dee0` | `8f bc f0 97` | bl 0x0066d11c | `UNCONDITIONAL_CALL`
<a id="insn-00a3dee4"></a> `00a3dee4` | `61 0a 5d b9` | ldr w1,[x19, #0x1d08] | `FALL_THROUGH`
<a id="insn-00a3dee8"></a> `00a3dee8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a3deec"></a> `00a3deec` | `0c f3 ff 97` | bl 0x00a3ab1c | `UNCONDITIONAL_CALL`
<a id="insn-00a3def0"></a> `00a3def0` | `61 2e 4e f9` | ldr x1,[x19, #0x1c58] | `FALL_THROUGH`
<a id="insn-00a3def4"></a> `00a3def4` | `17 8a 83 52` | mov w23,#0x1c50 | `FALL_THROUGH`
<a id="insn-00a3def8"></a> `00a3def8` | `08 8b 83 52` | mov w8,#0x1c58 | `FALL_THROUGH`
<a id="insn-00a3defc"></a> `00a3defc` | `60 02 17 8b` | add x0,x19,x23 | `FALL_THROUGH`
<a id="insn-00a3df00"></a> `00a3df00` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00a3df04"></a> `00a3df04` | `bf b0 f8 97` | bl 0x0086a200 | `UNCONDITIONAL_CALL`
<a id="insn-00a3df08"></a> `00a3df08` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00a3df0c"></a> `00a3df0c` | `ea 0b 40 f9` | ldr x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3df10"></a> `00a3df10` | `6a 32 0e f9` | str x10,[x19, #0x1c60] | `FALL_THROUGH`
<a id="insn-00a3df14"></a> `00a3df14` | `69 2a 0e f9` | str x9,[x19, #0x1c50] | `FALL_THROUGH`
<a id="insn-00a3df18"></a> `00a3df18` | `68 2e 0e f9` | str x8,[x19, #0x1c58] | `FALL_THROUGH`
<a id="insn-00a3df1c"></a> `00a3df1c` | `ca 00 00 b4` | cbz x10,0x00a3df34 | `CONDITIONAL_JUMP`
<a id="insn-00a3df20"></a> `00a3df20` | `89 22 00 91` | add x9,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a3df24"></a> `00a3df24` | `16 09 00 f9` | str x22,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a3df28"></a> `00a3df28` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00a3df2c"></a> `00a3df2c` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00a3df30"></a> `00a3df30` | `02 00 00 14` | b 0x00a3df38 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3df34"></a> `00a3df34` | `76 6a 37 f8` | str x22,[x19, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3df38"></a> `00a3df38` | `60 36 4e f9` | ldr x0,[x19, #0x1c68] | `FALL_THROUGH`
<a id="insn-00a3df3c"></a> `00a3df3c` | `08 8d 83 52` | mov w8,#0x1c68 | `FALL_THROUGH`
<a id="insn-00a3df40"></a> `00a3df40` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-00a3df44"></a> `00a3df44` | `77 02 08 8b` | add x23,x19,x8 | `FALL_THROUGH`
<a id="insn-00a3df48"></a> `00a3df48` | `a0 00 00 b4` | cbz x0,0x00a3df5c | `CONDITIONAL_JUMP`
<a id="insn-00a3df4c"></a> `00a3df4c` | `60 3a 0e f9` | str x0,[x19, #0x1c70] | `FALL_THROUGH`
<a id="insn-00a3df50"></a> `00a3df50` | `0c 68 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a3df54"></a> `00a3df54` | `ff 7e 00 a9` | stp xzr,xzr,[x23] | `FALL_THROUGH`
<a id="insn-00a3df58"></a> `00a3df58` | `ff 0a 00 f9` | str xzr,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a3df5c"></a> `00a3df5c` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a3df60"></a> `00a3df60` | `e0 83 c1 3c` | ldur q0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a3df64"></a> `00a3df64` | `18 90 83 52` | mov w24,#0x1c80 | `FALL_THROUGH`
<a id="insn-00a3df68"></a> `00a3df68` | `61 46 4e f9` | ldr x1,[x19, #0x1c88] | `FALL_THROUGH`
<a id="insn-00a3df6c"></a> `00a3df6c` | `60 02 18 8b` | add x0,x19,x24 | `FALL_THROUGH`
<a id="insn-00a3df70"></a> `00a3df70` | `df 7e 02 a9` | stp xzr,xzr,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00a3df74"></a> `00a3df74` | `68 3e 0e f9` | str x8,[x19, #0x1c78] | `FALL_THROUGH`
<a id="insn-00a3df78"></a> `00a3df78` | `08 91 83 52` | mov w8,#0x1c88 | `FALL_THROUGH`
<a id="insn-00a3df7c"></a> `00a3df7c` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-00a3df80"></a> `00a3df80` | `77 02 08 8b` | add x23,x19,x8 | `FALL_THROUGH`
<a id="insn-00a3df84"></a> `00a3df84` | `df 82 01 f8` | stur xzr,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00a3df88"></a> `00a3df88` | `15 0e ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3df8c"></a> `00a3df8c` | `e9 23 43 a9` | ldp x9,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3df90"></a> `00a3df90` | `ea 23 40 f9` | ldr x10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3df94"></a> `00a3df94` | `6a 4a 0e f9` | str x10,[x19, #0x1c90] | `FALL_THROUGH`
<a id="insn-00a3df98"></a> `00a3df98` | `69 42 0e f9` | str x9,[x19, #0x1c80] | `FALL_THROUGH`
<a id="insn-00a3df9c"></a> `00a3df9c` | `68 46 0e f9` | str x8,[x19, #0x1c88] | `FALL_THROUGH`
<a id="insn-00a3dfa0"></a> `00a3dfa0` | `ca 00 00 b4` | cbz x10,0x00a3dfb8 | `CONDITIONAL_JUMP`
<a id="insn-00a3dfa4"></a> `00a3dfa4` | `c9 e2 00 91` | add x9,x22,#0x38 | `FALL_THROUGH`
<a id="insn-00a3dfa8"></a> `00a3dfa8` | `17 09 00 f9` | str x23,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a3dfac"></a> `00a3dfac` | `e9 1b 00 f9` | str x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3dfb0"></a> `00a3dfb0` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00a3dfb4"></a> `00a3dfb4` | `02 00 00 14` | b 0x00a3dfbc | `UNCONDITIONAL_JUMP`
<a id="insn-00a3dfb8"></a> `00a3dfb8` | `77 6a 38 f8` | str x23,[x19, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3dfbc"></a> `00a3dfbc` | `e8 6b 40 b9` | ldr w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00a3dfc0"></a> `00a3dfc0` | `09 93 83 52` | mov w9,#0x1c98 | `FALL_THROUGH`
<a id="insn-00a3dfc4"></a> `00a3dfc4` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00a3dfc8"></a> `00a3dfc8` | `e1 83 c5 3c` | ldur q1,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00a3dfcc"></a> `00a3dfcc` | `61 66 4e f9` | ldr x1,[x19, #0x1cc8] | `FALL_THROUGH`
<a id="insn-00a3dfd0"></a> `00a3dfd0` | `19 98 83 52` | mov w25,#0x1cc0 | `FALL_THROUGH`
<a id="insn-00a3dfd4"></a> `00a3dfd4` | `69 02 09 8b` | add x9,x19,x9 | `FALL_THROUGH`
<a id="insn-00a3dfd8"></a> `00a3dfd8` | `68 ba 1c b9` | str w8,[x19, #0x1cb8] | `FALL_THROUGH`
<a id="insn-00a3dfdc"></a> `00a3dfdc` | `08 99 83 52` | mov w8,#0x1cc8 | `FALL_THROUGH`
<a id="insn-00a3dfe0"></a> `00a3dfe0` | `60 02 19 8b` | add x0,x19,x25 | `FALL_THROUGH`
<a id="insn-00a3dfe4"></a> `00a3dfe4` | `20 05 00 ad` | stp q0,q1,[x9] | `FALL_THROUGH`
<a id="insn-00a3dfe8"></a> `00a3dfe8` | `f7 03 00 91` | mov x23,sp | `FALL_THROUGH`
<a id="insn-00a3dfec"></a> `00a3dfec` | `78 02 08 8b` | add x24,x19,x8 | `FALL_THROUGH`
<a id="insn-00a3dff0"></a> `00a3dff0` | `fb 0d ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3dff4"></a> `00a3dff4` | `e8 07 47 a9` | ldp x8,x1,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a3dff8"></a> `00a3dff8` | `e9 43 40 f9` | ldr x9,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a3dffc"></a> `00a3dffc` | `69 6a 0e f9` | str x9,[x19, #0x1cd0] | `FALL_THROUGH`
<a id="insn-00a3e000"></a> `00a3e000` | `68 62 0e f9` | str x8,[x19, #0x1cc0] | `FALL_THROUGH`
<a id="insn-00a3e004"></a> `00a3e004` | `61 66 0e f9` | str x1,[x19, #0x1cc8] | `FALL_THROUGH`
<a id="insn-00a3e008"></a> `00a3e008` | `e9 00 00 b4` | cbz x9,0x00a3e024 | `CONDITIONAL_JUMP`
<a id="insn-00a3e00c"></a> `00a3e00c` | `e8 e2 01 91` | add x8,x23,#0x78 | `FALL_THROUGH`
<a id="insn-00a3e010"></a> `00a3e010` | `38 08 00 f9` | str x24,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00a3e014"></a> `00a3e014` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00a3e018"></a> `00a3e018` | `e8 3b 00 f9` | str x8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a3e01c"></a> `00a3e01c` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00a3e020"></a> `00a3e020` | `02 00 00 14` | b 0x00a3e028 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3e024"></a> `00a3e024` | `78 6a 39 f8` | str x24,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3e028"></a> `00a3e028` | `08 9b 83 52` | mov w8,#0x1cd8 | `FALL_THROUGH`
<a id="insn-00a3e02c"></a> `00a3e02c` | `80 82 c8 3c` | ldur q0,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00a3e030"></a> `00a3e030` | `81 82 c9 3c` | ldur q1,[x20, #0x98] | `FALL_THROUGH`
<a id="insn-00a3e034"></a> `00a3e034` | `82 42 ca 3c` | ldur q2,[x20, #0xa4] | `FALL_THROUGH`
<a id="insn-00a3e038"></a> `00a3e038` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00a3e03c"></a> `00a3e03c` | `e0 c2 01 91` | add x0,x23,#0x70 | `FALL_THROUGH`
<a id="insn-00a3e040"></a> `00a3e040` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00a3e044"></a> `00a3e044` | `02 c1 81 3c` | stur q2,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00a3e048"></a> `00a3e048` | `e5 0d ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3e04c"></a> `00a3e04c` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00a3e050"></a> `00a3e050` | `c0 c2 00 91` | add x0,x22,#0x30 | `FALL_THROUGH`
<a id="insn-00a3e054"></a> `00a3e054` | `e2 0d ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3e058"></a> `00a3e058` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a3e05c"></a> `00a3e05c` | `60 00 00 b4` | cbz x0,0x00a3e068 | `CONDITIONAL_JUMP`
<a id="insn-00a3e060"></a> `00a3e060` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3e064"></a> `00a3e064` | `c7 67 08 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e068"></a> `00a3e068` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a3e06c"></a> `00a3e06c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a3e070"></a> `00a3e070` | `64 b0 f8 97` | bl 0x0086a200 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e074"></a> `00a3e074` | `36 13 00 d0` | adrp x22,0xca4000 | `FALL_THROUGH`
<a id="insn-00a3e078"></a> `00a3e078` | `28 13 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00a3e07c"></a> `00a3e07c` | `00 99 80 52` | mov w0,#0x4c8 | `FALL_THROUGH`
<a id="insn-00a3e080"></a> `00a3e080` | `c9 3e 45 f9` | ldr x9,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00a3e084"></a> `00a3e084` | `0a 35 45 f9` | ldr x10,[x8, #0xa68] | `FALL_THROUGH`
<a id="insn-00a3e088"></a> `00a3e088` | `09 35 05 f9` | str x9,[x8, #0xa68] | `FALL_THROUGH`
<a id="insn-00a3e08c"></a> `00a3e08c` | `ca 3e 05 f9` | str x10,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00a3e090"></a> `00a3e090` | `b4 67 08 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e094"></a> `00a3e094` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a3e098"></a> `00a3e098` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00a3e09c"></a> `00a3e09c` | `c1 04 00 94` | bl 0x00a3f3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e0a0"></a> `00a3e0a0` | `c0 3e 45 f9` | ldr x0,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00a3e0a4"></a> `00a3e0a4` | `d4 3e 05 f9` | str x20,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00a3e0a8"></a> `00a3e0a8` | `c0 00 00 b4` | cbz x0,0x00a3e0c0 | `CONDITIONAL_JUMP`
<a id="insn-00a3e0ac"></a> `00a3e0ac` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00a3e0b0"></a> `00a3e0b0` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a3e0b4"></a> `00a3e0b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a3e0b8"></a> `00a3e0b8` | `d4 3e 45 f9` | ldr x20,[x22, #0xa78] | `FALL_THROUGH`
<a id="insn-00a3e0bc"></a> `00a3e0bc` | `34 01 00 b4` | cbz x20,0x00a3e0e0 | `CONDITIONAL_JUMP`
<a id="insn-00a3e0c0"></a> `00a3e0c0` | `21 11 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00a3e0c4"></a> `00a3e0c4` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-00a3e0c8"></a> `00a3e0c8` | `62 12 00 b0` | adrp x2,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a3e0cc"></a> `00a3e0cc` | `42 80 11 91` | add x2,x2,#0x460 | `FALL_THROUGH`
<a id="insn-00a3e0d0"></a> `00a3e0d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a3e0d4"></a> `00a3e0d4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00a3e0d8"></a> `00a3e0d8` | `82 69 08 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e0dc"></a> `00a3e0dc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a3e0e0"></a> `00a3e0e0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3e0e4"></a> `00a3e0e4` | `bb 3a fe 97` | bl 0x009ccbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e0e8"></a> `00a3e0e8` | `16 b2 8f 52` | mov w22,#0x7d90 | `FALL_THROUGH`
<a id="insn-00a3e0ec"></a> `00a3e0ec` | `76 06 a0 72` | movk w22,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3e0f0"></a> `00a3e0f0` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e0f4"></a> `00a3e0f4` | `a0 26 02 94` | bl 0x00ac7b74 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e0f8"></a> `00a3e0f8` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e0fc"></a> `00a3e0fc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a3e100"></a> `00a3e100` | `c9 33 02 94` | bl 0x00acb024 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e104"></a> `00a3e104` | `68 12 00 b0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a3e108"></a> `00a3e108` | `08 a1 1a 91` | add x8,x8,#0x6a8 | `FALL_THROUGH`
<a id="insn-00a3e10c"></a> `00a3e10c` | `f7 03 00 91` | mov x23,sp | `FALL_THROUGH`
<a id="insn-00a3e110"></a> `00a3e110` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00a3e114"></a> `00a3e114` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3e118"></a> `00a3e118` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e11c"></a> `00a3e11c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00a3e120"></a> `00a3e120` | `89 32 02 94` | bl 0x00acab44 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e124"></a> `00a3e124` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3e128"></a> `00a3e128` | `1f 00 17 eb` | cmp x0,x23 | `FALL_THROUGH`
<a id="insn-00a3e12c"></a> `00a3e12c` | `80 00 00 54` | b.eq 0x00a3e13c | `CONDITIONAL_JUMP`
<a id="insn-00a3e130"></a> `00a3e130` | `00 01 00 b4` | cbz x0,0x00a3e150 | `CONDITIONAL_JUMP`
<a id="insn-00a3e134"></a> `00a3e134` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00a3e138"></a> `00a3e138` | `03 00 00 14` | b 0x00a3e144 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3e13c"></a> `00a3e13c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00a3e140"></a> `00a3e140` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a3e144"></a> `00a3e144` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00a3e148"></a> `00a3e148` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3e14c"></a> `00a3e14c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a3e150"></a> `00a3e150` | `81 66 40 f9` | ldr x1,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-00a3e154"></a> `00a3e154` | `83 fe 40 f9` | ldr x3,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00a3e158"></a> `00a3e158` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e15c"></a> `00a3e15c` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00a3e160"></a> `00a3e160` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00a3e164"></a> `00a3e164` | `72 2e 02 94` | bl 0x00ac9b2c | `UNCONDITIONAL_CALL`
<a id="insn-00a3e168"></a> `00a3e168` | `68 12 00 b0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a3e16c"></a> `00a3e16c` | `08 a1 1c 91` | add x8,x8,#0x728 | `FALL_THROUGH`
<a id="insn-00a3e170"></a> `00a3e170` | `f7 03 00 91` | mov x23,sp | `FALL_THROUGH`
<a id="insn-00a3e174"></a> `00a3e174` | `e8 4f 00 a9` | stp x8,x19,[sp] | `FALL_THROUGH`
<a id="insn-00a3e178"></a> `00a3e178` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3e17c"></a> `00a3e17c` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e180"></a> `00a3e180` | `81 a2 02 91` | add x1,x20,#0xa8 | `FALL_THROUGH`
<a id="insn-00a3e184"></a> `00a3e184` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00a3e188"></a> `00a3e188` | `02 32 80 52` | mov w2,#0x190 | `FALL_THROUGH`
<a id="insn-00a3e18c"></a> `00a3e18c` | `74 2e 02 94` | bl 0x00ac9b5c | `UNCONDITIONAL_CALL`
<a id="insn-00a3e190"></a> `00a3e190` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3e194"></a> `00a3e194` | `1f 00 17 eb` | cmp x0,x23 | `FALL_THROUGH`
<a id="insn-00a3e198"></a> `00a3e198` | `80 00 00 54` | b.eq 0x00a3e1a8 | `CONDITIONAL_JUMP`
<a id="insn-00a3e19c"></a> `00a3e19c` | `00 01 00 b4` | cbz x0,0x00a3e1bc | `CONDITIONAL_JUMP`
<a id="insn-00a3e1a0"></a> `00a3e1a0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00a3e1a4"></a> `00a3e1a4` | `03 00 00 14` | b 0x00a3e1b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3e1a8"></a> `00a3e1a8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00a3e1ac"></a> `00a3e1ac` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a3e1b0"></a> `00a3e1b0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00a3e1b4"></a> `00a3e1b4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a3e1b8"></a> `00a3e1b8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a3e1bc"></a> `00a3e1bc` | `82 7e 40 f9` | ldr x2,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-00a3e1c0"></a> `00a3e1c0` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-00a3e1c4"></a> `00a3e1c4` | `81 a2 02 91` | add x1,x20,#0xa8 | `FALL_THROUGH`
<a id="insn-00a3e1c8"></a> `00a3e1c8` | `23 32 80 52` | mov w3,#0x191 | `FALL_THROUGH`
<a id="insn-00a3e1cc"></a> `00a3e1cc` | `81 2f 02 94` | bl 0x00ac9fd0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3e1d0"></a> `00a3e1d0` | `40 0a 80 52` | mov w0,#0x52 | `FALL_THROUGH`
<a id="insn-00a3e1d4"></a> `00a3e1d4` | `d2 bb f0 97` | bl 0x0066d11c | `UNCONDITIONAL_CALL`
<a id="insn-00a3e1d8"></a> `00a3e1d8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a3e1dc"></a> `00a3e1dc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3e1e0"></a> `00a3e1e0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a3e1e4"></a> `00a3e1e4` | `01 04 00 54` | b.ne 0x00a3e264 | `CONDITIONAL_JUMP`
<a id="insn-00a3e1e8"></a> `00a3e1e8` | `f4 4f 50 a9` | ldp x20,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00a3e1ec"></a> `00a3e1ec` | `f6 57 4f a9` | ldp x22,x21,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00a3e1f0"></a> `00a3e1f0` | `f8 5f 4e a9` | ldp x24,x23,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00a3e1f4"></a> `00a3e1f4` | `fc 67 4d a9` | ldp x28,x25,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00a3e1f8"></a> `00a3e1f8` | `fd 7b 4c a9` | ldp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00a3e1fc"></a> `00a3e1fc` | `ff 43 04 91` | add sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00a3e200"></a> `00a3e200` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a3e264"></a> `00a3e264` | `53 67 08 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3deac`](#insn-00a3deac) 範囲 `[['00a3deac', '00a3ded3']]`
  - `FALL_THROUGH` [`00a3ded0`](#insn-00a3ded0) → [`00a3ded4`](#insn-00a3ded4)
- ブロック [`00a3ded4`](#insn-00a3ded4) 範囲 `[['00a3ded4', '00a3defb']]`
  - `FALL_THROUGH` [`00a3def8`](#insn-00a3def8) → [`00a3defc`](#insn-00a3defc)
- ブロック [`00a3defc`](#insn-00a3defc) 範囲 `[['00a3defc', '00a3df1f']]`
  - `CONDITIONAL_JUMP` [`00a3df1c`](#insn-00a3df1c) → [`00a3df34`](#insn-00a3df34)
  - `FALL_THROUGH` [`00a3df1c`](#insn-00a3df1c) → [`00a3df20`](#insn-00a3df20)
- ブロック [`00a3df20`](#insn-00a3df20) 範囲 `[['00a3df20', '00a3df33']]`
  - `UNCONDITIONAL_JUMP` [`00a3df30`](#insn-00a3df30) → [`00a3df38`](#insn-00a3df38)
- ブロック [`00a3df34`](#insn-00a3df34) 範囲 `[['00a3df34', '00a3df37']]`
  - `FALL_THROUGH` [`00a3df34`](#insn-00a3df34) → [`00a3df38`](#insn-00a3df38)
- ブロック [`00a3df38`](#insn-00a3df38) 範囲 `[['00a3df38', '00a3df47']]`
  - `FALL_THROUGH` [`00a3df44`](#insn-00a3df44) → [`00a3df48`](#insn-00a3df48)
- ブロック [`00a3df48`](#insn-00a3df48) 範囲 `[['00a3df48', '00a3df4b']]`
  - `CONDITIONAL_JUMP` [`00a3df48`](#insn-00a3df48) → [`00a3df5c`](#insn-00a3df5c)
  - `FALL_THROUGH` [`00a3df48`](#insn-00a3df48) → [`00a3df4c`](#insn-00a3df4c)
- ブロック [`00a3df4c`](#insn-00a3df4c) 範囲 `[['00a3df4c', '00a3df57']]`
  - `FALL_THROUGH` [`00a3df54`](#insn-00a3df54) → [`00a3df58`](#insn-00a3df58)
- ブロック [`00a3df58`](#insn-00a3df58) 範囲 `[['00a3df58', '00a3df5b']]`
  - `FALL_THROUGH` [`00a3df58`](#insn-00a3df58) → [`00a3df5c`](#insn-00a3df5c)
- ブロック [`00a3df5c`](#insn-00a3df5c) 範囲 `[['00a3df5c', '00a3df67']]`
  - `FALL_THROUGH` [`00a3df64`](#insn-00a3df64) → [`00a3df68`](#insn-00a3df68)
- ブロック [`00a3df68`](#insn-00a3df68) 範囲 `[['00a3df68', '00a3df6b']]`
  - `FALL_THROUGH` [`00a3df68`](#insn-00a3df68) → [`00a3df6c`](#insn-00a3df6c)
- ブロック [`00a3df6c`](#insn-00a3df6c) 範囲 `[['00a3df6c', '00a3dfa3']]`
  - `CONDITIONAL_JUMP` [`00a3dfa0`](#insn-00a3dfa0) → [`00a3dfb8`](#insn-00a3dfb8)
  - `FALL_THROUGH` [`00a3dfa0`](#insn-00a3dfa0) → [`00a3dfa4`](#insn-00a3dfa4)
- ブロック [`00a3dfa4`](#insn-00a3dfa4) 範囲 `[['00a3dfa4', '00a3dfb7']]`
  - `UNCONDITIONAL_JUMP` [`00a3dfb4`](#insn-00a3dfb4) → [`00a3dfbc`](#insn-00a3dfbc)
- ブロック [`00a3dfb8`](#insn-00a3dfb8) 範囲 `[['00a3dfb8', '00a3dfbb']]`
  - `FALL_THROUGH` [`00a3dfb8`](#insn-00a3dfb8) → [`00a3dfbc`](#insn-00a3dfbc)
- ブロック [`00a3dfbc`](#insn-00a3dfbc) 範囲 `[['00a3dfbc', '00a3dfbf']]`
  - `FALL_THROUGH` [`00a3dfbc`](#insn-00a3dfbc) → [`00a3dfc0`](#insn-00a3dfc0)
- ブロック [`00a3dfc0`](#insn-00a3dfc0) 範囲 `[['00a3dfc0', '00a3dfcf']]`
  - `FALL_THROUGH` [`00a3dfcc`](#insn-00a3dfcc) → [`00a3dfd0`](#insn-00a3dfd0)
- ブロック [`00a3dfd0`](#insn-00a3dfd0) 範囲 `[['00a3dfd0', '00a3e00b']]`
  - `CONDITIONAL_JUMP` [`00a3e008`](#insn-00a3e008) → [`00a3e024`](#insn-00a3e024)
  - `FALL_THROUGH` [`00a3e008`](#insn-00a3e008) → [`00a3e00c`](#insn-00a3e00c)
- ブロック [`00a3e00c`](#insn-00a3e00c) 範囲 `[['00a3e00c', '00a3e023']]`
  - `UNCONDITIONAL_JUMP` [`00a3e020`](#insn-00a3e020) → [`00a3e028`](#insn-00a3e028)
- ブロック [`00a3e024`](#insn-00a3e024) 範囲 `[['00a3e024', '00a3e027']]`
  - `FALL_THROUGH` [`00a3e024`](#insn-00a3e024) → [`00a3e028`](#insn-00a3e028)
- ブロック [`00a3e028`](#insn-00a3e028) 範囲 `[['00a3e028', '00a3e05f']]`
  - `CONDITIONAL_JUMP` [`00a3e05c`](#insn-00a3e05c) → [`00a3e068`](#insn-00a3e068)
  - `FALL_THROUGH` [`00a3e05c`](#insn-00a3e05c) → [`00a3e060`](#insn-00a3e060)
- ブロック [`00a3e060`](#insn-00a3e060) 範囲 `[['00a3e060', '00a3e067']]`
  - `FALL_THROUGH` [`00a3e064`](#insn-00a3e064) → [`00a3e068`](#insn-00a3e068)
- ブロック [`00a3e068`](#insn-00a3e068) 範囲 `[['00a3e068', '00a3e0ab']]`
  - `CONDITIONAL_JUMP` [`00a3e0a8`](#insn-00a3e0a8) → [`00a3e0c0`](#insn-00a3e0c0)
  - `FALL_THROUGH` [`00a3e0a8`](#insn-00a3e0a8) → [`00a3e0ac`](#insn-00a3e0ac)
- ブロック [`00a3e0ac`](#insn-00a3e0ac) 範囲 `[['00a3e0ac', '00a3e0bf']]`
  - `CONDITIONAL_JUMP` [`00a3e0bc`](#insn-00a3e0bc) → [`00a3e0e0`](#insn-00a3e0e0)
  - `FALL_THROUGH` [`00a3e0bc`](#insn-00a3e0bc) → [`00a3e0c0`](#insn-00a3e0c0)
- ブロック [`00a3e0c0`](#insn-00a3e0c0) 範囲 `[['00a3e0c0', '00a3e0df']]`
  - `FALL_THROUGH` [`00a3e0dc`](#insn-00a3e0dc) → [`00a3e0e0`](#insn-00a3e0e0)
- ブロック [`00a3e0e0`](#insn-00a3e0e0) 範囲 `[['00a3e0e0', '00a3e12f']]`
  - `CONDITIONAL_JUMP` [`00a3e12c`](#insn-00a3e12c) → [`00a3e13c`](#insn-00a3e13c)
  - `FALL_THROUGH` [`00a3e12c`](#insn-00a3e12c) → [`00a3e130`](#insn-00a3e130)
- ブロック [`00a3e130`](#insn-00a3e130) 範囲 `[['00a3e130', '00a3e133']]`
  - `CONDITIONAL_JUMP` [`00a3e130`](#insn-00a3e130) → [`00a3e150`](#insn-00a3e150)
  - `FALL_THROUGH` [`00a3e130`](#insn-00a3e130) → [`00a3e134`](#insn-00a3e134)
- ブロック [`00a3e134`](#insn-00a3e134) 範囲 `[['00a3e134', '00a3e13b']]`
  - `UNCONDITIONAL_JUMP` [`00a3e138`](#insn-00a3e138) → [`00a3e144`](#insn-00a3e144)
- ブロック [`00a3e13c`](#insn-00a3e13c) 範囲 `[['00a3e13c', '00a3e13f']]`
  - `FALL_THROUGH` [`00a3e13c`](#insn-00a3e13c) → [`00a3e140`](#insn-00a3e140)
- ブロック [`00a3e140`](#insn-00a3e140) 範囲 `[['00a3e140', '00a3e143']]`
  - `FALL_THROUGH` [`00a3e140`](#insn-00a3e140) → [`00a3e144`](#insn-00a3e144)
- ブロック [`00a3e144`](#insn-00a3e144) 範囲 `[['00a3e144', '00a3e14f']]`
  - `FALL_THROUGH` [`00a3e14c`](#insn-00a3e14c) → [`00a3e150`](#insn-00a3e150)
- ブロック [`00a3e150`](#insn-00a3e150) 範囲 `[['00a3e150', '00a3e16f']]`
  - `FALL_THROUGH` [`00a3e16c`](#insn-00a3e16c) → [`00a3e170`](#insn-00a3e170)
- ブロック [`00a3e170`](#insn-00a3e170) 範囲 `[['00a3e170', '00a3e187']]`
  - `FALL_THROUGH` [`00a3e184`](#insn-00a3e184) → [`00a3e188`](#insn-00a3e188)
- ブロック [`00a3e188`](#insn-00a3e188) 範囲 `[['00a3e188', '00a3e19b']]`
  - `CONDITIONAL_JUMP` [`00a3e198`](#insn-00a3e198) → [`00a3e1a8`](#insn-00a3e1a8)
  - `FALL_THROUGH` [`00a3e198`](#insn-00a3e198) → [`00a3e19c`](#insn-00a3e19c)
- ブロック [`00a3e19c`](#insn-00a3e19c) 範囲 `[['00a3e19c', '00a3e19f']]`
  - `CONDITIONAL_JUMP` [`00a3e19c`](#insn-00a3e19c) → [`00a3e1bc`](#insn-00a3e1bc)
  - `FALL_THROUGH` [`00a3e19c`](#insn-00a3e19c) → [`00a3e1a0`](#insn-00a3e1a0)
- ブロック [`00a3e1a0`](#insn-00a3e1a0) 範囲 `[['00a3e1a0', '00a3e1a3']]`
  - `FALL_THROUGH` [`00a3e1a0`](#insn-00a3e1a0) → [`00a3e1a4`](#insn-00a3e1a4)
- ブロック [`00a3e1a4`](#insn-00a3e1a4) 範囲 `[['00a3e1a4', '00a3e1a7']]`
  - `UNCONDITIONAL_JUMP` [`00a3e1a4`](#insn-00a3e1a4) → [`00a3e1b0`](#insn-00a3e1b0)
- ブロック [`00a3e1a8`](#insn-00a3e1a8) 範囲 `[['00a3e1a8', '00a3e1af']]`
  - `FALL_THROUGH` [`00a3e1ac`](#insn-00a3e1ac) → [`00a3e1b0`](#insn-00a3e1b0)
- ブロック [`00a3e1b0`](#insn-00a3e1b0) 範囲 `[['00a3e1b0', '00a3e1bb']]`
  - `FALL_THROUGH` [`00a3e1b8`](#insn-00a3e1b8) → [`00a3e1bc`](#insn-00a3e1bc)
- ブロック [`00a3e1bc`](#insn-00a3e1bc) 範囲 `[['00a3e1bc', '00a3e1e7']]`
  - `CONDITIONAL_JUMP` [`00a3e1e4`](#insn-00a3e1e4) → [`00a3e264`](#insn-00a3e264)
  - `FALL_THROUGH` [`00a3e1e4`](#insn-00a3e1e4) → [`00a3e1e8`](#insn-00a3e1e8)
- ブロック [`00a3e1e8`](#insn-00a3e1e8) 範囲 `[['00a3e1e8', '00a3e1eb']]`
  - `FALL_THROUGH` [`00a3e1e8`](#insn-00a3e1e8) → [`00a3e1ec`](#insn-00a3e1ec)
- ブロック [`00a3e1ec`](#insn-00a3e1ec) 範囲 `[['00a3e1ec', '00a3e203']]`
- ブロック [`00a3e264`](#insn-00a3e264) 範囲 `[['00a3e264', '00a3e267']]`

## 命令位置別の参照

- [`00a3deb0`](#insn-00a3deb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3deb4`](#insn-00a3deb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3deb8`](#insn-00a3deb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3debc`](#insn-00a3debc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dec0`](#insn-00a3dec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dedc`](#insn-00a3dedc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dee0`](#insn-00a3dee0) → [`0066d11c`](../0066d/0066d11c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066d11c` · 推定シンボル `None` · 推定型 `None`
- [`00a3deec`](#insn-00a3deec) → [`00a3ab1c`](../00a3a/00a3ab1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a3ab1c` · 推定シンボル `None` · 推定型 `None`
- [`00a3df04`](#insn-00a3df04) → [`0086a200`](../0086a/0086a200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086a200` · 推定シンボル `None` · 推定型 `None`
- [`00a3df08`](#insn-00a3df08) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df0c`](#insn-00a3df0c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df1c`](#insn-00a3df1c) → [`00a3df34`](#insn-00a3df34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df28`](#insn-00a3df28) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df2c`](#insn-00a3df2c) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df30`](#insn-00a3df30) → [`00a3df38`](#insn-00a3df38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df48`](#insn-00a3df48) → [`00a3df5c`](#insn-00a3df5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df50`](#insn-00a3df50) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a3df5c`](#insn-00a3df5c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df60`](#insn-00a3df60) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df70`](#insn-00a3df70) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df84`](#insn-00a3df84) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df88`](#insn-00a3df88) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3df8c`](#insn-00a3df8c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3df90`](#insn-00a3df90) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfa0`](#insn-00a3dfa0) → [`00a3dfb8`](#insn-00a3dfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfac`](#insn-00a3dfac) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfb0`](#insn-00a3dfb0) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfb4`](#insn-00a3dfb4) → [`00a3dfbc`](#insn-00a3dfbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfbc`](#insn-00a3dfbc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfc4`](#insn-00a3dfc4) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dfc8`](#insn-00a3dfc8) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dff0`](#insn-00a3dff0) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3dff4`](#insn-00a3dff4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3dff8`](#insn-00a3dff8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e008`](#insn-00a3e008) → [`00a3e024`](#insn-00a3e024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e018`](#insn-00a3e018) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e01c`](#insn-00a3e01c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e020`](#insn-00a3e020) → [`00a3e028`](#insn-00a3e028) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e02c`](#insn-00a3e02c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e030`](#insn-00a3e030) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e034`](#insn-00a3e034) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e048`](#insn-00a3e048) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3e04c`](#insn-00a3e04c) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e054`](#insn-00a3e054) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3e058`](#insn-00a3e058) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e05c`](#insn-00a3e05c) → [`00a3e068`](#insn-00a3e068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e060`](#insn-00a3e060) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e064`](#insn-00a3e064) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00a3e068`](#insn-00a3e068) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e070`](#insn-00a3e070) → [`0086a200`](../0086a/0086a200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086a200` · 推定シンボル `None` · 推定型 `None`
- [`00a3e080`](#insn-00a3e080) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e084`](#insn-00a3e084) → `00ca4a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e088`](#insn-00a3e088) → `00ca4a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e08c`](#insn-00a3e08c) → `00ca4a78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e090`](#insn-00a3e090) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00a3e09c`](#insn-00a3e09c) → [`00a3f3a0`](../00a3f/00a3f3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a3f3a0` · 推定シンボル `None` · 推定型 `None`
- [`00a3e0a0`](#insn-00a3e0a0) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e0a4`](#insn-00a3e0a4) → `00ca4a78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e0a8`](#insn-00a3e0a8) → [`00a3e0c0`](#insn-00a3e0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e0b8`](#insn-00a3e0b8) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a3e0bc`](#insn-00a3e0bc) → [`00a3e0e0`](#insn-00a3e0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e0c4`](#insn-00a3e0c4) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00a3e0cc`](#insn-00a3e0cc) → `00c8b460`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00a3e0d8`](#insn-00a3e0d8) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`00a3e0e4`](#insn-00a3e0e4) → [`009ccbd0`](../009cc/009ccbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ccbd0` · 推定シンボル `None` · 推定型 `None`
- [`00a3e0f4`](#insn-00a3e0f4) → [`00ac7b74`](../00ac7/00ac7b74.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac7b74` · 推定シンボル `None` · 推定型 `None`
- [`00a3e100`](#insn-00a3e100) → [`00acb024`](../00acb/00acb024.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb024` · 推定シンボル `None` · 推定型 `None`
- [`00a3e110`](#insn-00a3e110) → `00c8b6a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3e110`](#insn-00a3e110) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e114`](#insn-00a3e114) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e120`](#insn-00a3e120) → [`00acab44`](../00aca/00acab44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acab44` · 推定シンボル `None` · 推定型 `None`
- [`00a3e124`](#insn-00a3e124) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e12c`](#insn-00a3e12c) → [`00a3e13c`](#insn-00a3e13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e130`](#insn-00a3e130) → [`00a3e150`](#insn-00a3e150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e138`](#insn-00a3e138) → [`00a3e144`](#insn-00a3e144) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e144`](#insn-00a3e144) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e148`](#insn-00a3e148) → `00c8b6c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a3e148`](#insn-00a3e148) → `00c8b6d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3e14c`](#insn-00a3e14c) → [`00a40d3c`](../00a40/00a40d3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a40d3c` · 推定シンボル `None` · 推定型 `None`
- [`00a3e14c`](#insn-00a3e14c) → [`00a40d40`](../00a40/00a40d40.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a40d40` · 推定シンボル `None` · 推定型 `None`
- [`00a3e164`](#insn-00a3e164) → [`00ac9b2c`](../00ac9/00ac9b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9b2c` · 推定シンボル `None` · 推定型 `None`
- [`00a3e174`](#insn-00a3e174) → `00c8b728`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3e174`](#insn-00a3e174) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e178`](#insn-00a3e178) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e18c`](#insn-00a3e18c) → [`00ac9b5c`](../00ac9/00ac9b5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9b5c` · 推定シンボル `None` · 推定型 `None`
- [`00a3e190`](#insn-00a3e190) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e198`](#insn-00a3e198) → [`00a3e1a8`](#insn-00a3e1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e19c`](#insn-00a3e19c) → [`00a3e1bc`](#insn-00a3e1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1a4`](#insn-00a3e1a4) → [`00a3e1b0`](#insn-00a3e1b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1b0`](#insn-00a3e1b0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1b4`](#insn-00a3e1b4) → `00c8b748`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a3e1b4`](#insn-00a3e1b4) → `00c8b750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3e1b8`](#insn-00a3e1b8) → [`00a40ddc`](../00a40/00a40ddc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a40ddc` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1b8`](#insn-00a3e1b8) → [`00a40de0`](../00a40/00a40de0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a40de0` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1cc`](#insn-00a3e1cc) → [`00ac9fd0`](../00ac9/00ac9fd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9fd0` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1d4`](#insn-00a3e1d4) → [`0066d11c`](../0066d/0066d11c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0066d11c` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1dc`](#insn-00a3e1dc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1e4`](#insn-00a3e1e4) → [`00a3e264`](#insn-00a3e264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1e8`](#insn-00a3e1e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1ec`](#insn-00a3e1ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1f0`](#insn-00a3e1f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1f4`](#insn-00a3e1f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e1f8`](#insn-00a3e1f8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3e264`](#insn-00a3e264) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3deb0`](#insn-00a3deb0)

~~~json
{
  "source": "00a3deb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3deb4`](#insn-00a3deb4)

~~~json
{
  "source": "00a3deb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3deb8`](#insn-00a3deb8)

~~~json
{
  "source": "00a3deb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3debc`](#insn-00a3debc)

~~~json
{
  "source": "00a3debc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dec0`](#insn-00a3dec0)

~~~json
{
  "source": "00a3dec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dedc`](#insn-00a3dedc)

~~~json
{
  "source": "00a3dedc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dee0`](#insn-00a3dee0)

~~~json
{
  "source": "00a3dee0",
  "target": "0066d11c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3deec`](#insn-00a3deec)

~~~json
{
  "source": "00a3deec",
  "target": "00a3ab1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3df04`](#insn-00a3df04)

~~~json
{
  "source": "00a3df04",
  "target": "0086a200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3df08`](#insn-00a3df08)

~~~json
{
  "source": "00a3df08",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df0c`](#insn-00a3df0c)

~~~json
{
  "source": "00a3df0c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df1c`](#insn-00a3df1c)

~~~json
{
  "source": "00a3df1c",
  "target": "00a3df34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df28`](#insn-00a3df28)

~~~json
{
  "source": "00a3df28",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df2c`](#insn-00a3df2c)

~~~json
{
  "source": "00a3df2c",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df30`](#insn-00a3df30)

~~~json
{
  "source": "00a3df30",
  "target": "00a3df38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df48`](#insn-00a3df48)

~~~json
{
  "source": "00a3df48",
  "target": "00a3df5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df50`](#insn-00a3df50)

~~~json
{
  "source": "00a3df50",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3df5c`](#insn-00a3df5c)

~~~json
{
  "source": "00a3df5c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df60`](#insn-00a3df60)

~~~json
{
  "source": "00a3df60",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df70`](#insn-00a3df70)

~~~json
{
  "source": "00a3df70",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df84`](#insn-00a3df84)

~~~json
{
  "source": "00a3df84",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df88`](#insn-00a3df88)

~~~json
{
  "source": "00a3df88",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3df8c`](#insn-00a3df8c)

~~~json
{
  "source": "00a3df8c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3df90`](#insn-00a3df90)

~~~json
{
  "source": "00a3df90",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfa0`](#insn-00a3dfa0)

~~~json
{
  "source": "00a3dfa0",
  "target": "00a3dfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfac`](#insn-00a3dfac)

~~~json
{
  "source": "00a3dfac",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfb0`](#insn-00a3dfb0)

~~~json
{
  "source": "00a3dfb0",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfb4`](#insn-00a3dfb4)

~~~json
{
  "source": "00a3dfb4",
  "target": "00a3dfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfbc`](#insn-00a3dfbc)

~~~json
{
  "source": "00a3dfbc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfc4`](#insn-00a3dfc4)

~~~json
{
  "source": "00a3dfc4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dfc8`](#insn-00a3dfc8)

~~~json
{
  "source": "00a3dfc8",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dff0`](#insn-00a3dff0)

~~~json
{
  "source": "00a3dff0",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3dff4`](#insn-00a3dff4)

~~~json
{
  "source": "00a3dff4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3dff8`](#insn-00a3dff8)

~~~json
{
  "source": "00a3dff8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e008`](#insn-00a3e008)

~~~json
{
  "source": "00a3e008",
  "target": "00a3e024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e018`](#insn-00a3e018)

~~~json
{
  "source": "00a3e018",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e01c`](#insn-00a3e01c)

~~~json
{
  "source": "00a3e01c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e020`](#insn-00a3e020)

~~~json
{
  "source": "00a3e020",
  "target": "00a3e028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e02c`](#insn-00a3e02c)

~~~json
{
  "source": "00a3e02c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e030`](#insn-00a3e030)

~~~json
{
  "source": "00a3e030",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e034`](#insn-00a3e034)

~~~json
{
  "source": "00a3e034",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e048`](#insn-00a3e048)

~~~json
{
  "source": "00a3e048",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e04c`](#insn-00a3e04c)

~~~json
{
  "source": "00a3e04c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e054`](#insn-00a3e054)

~~~json
{
  "source": "00a3e054",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e058`](#insn-00a3e058)

~~~json
{
  "source": "00a3e058",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e05c`](#insn-00a3e05c)

~~~json
{
  "source": "00a3e05c",
  "target": "00a3e068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e060`](#insn-00a3e060)

~~~json
{
  "source": "00a3e060",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e064`](#insn-00a3e064)

~~~json
{
  "source": "00a3e064",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e068`](#insn-00a3e068)

~~~json
{
  "source": "00a3e068",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e070`](#insn-00a3e070)

~~~json
{
  "source": "00a3e070",
  "target": "0086a200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e080`](#insn-00a3e080)

~~~json
{
  "source": "00a3e080",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e084`](#insn-00a3e084)

~~~json
{
  "source": "00a3e084",
  "target": "00ca4a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e088`](#insn-00a3e088)

~~~json
{
  "source": "00a3e088",
  "target": "00ca4a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e08c`](#insn-00a3e08c)

~~~json
{
  "source": "00a3e08c",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e090`](#insn-00a3e090)

~~~json
{
  "source": "00a3e090",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e09c`](#insn-00a3e09c)

~~~json
{
  "source": "00a3e09c",
  "target": "00a3f3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e0a0`](#insn-00a3e0a0)

~~~json
{
  "source": "00a3e0a0",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e0a4`](#insn-00a3e0a4)

~~~json
{
  "source": "00a3e0a4",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e0a8`](#insn-00a3e0a8)

~~~json
{
  "source": "00a3e0a8",
  "target": "00a3e0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e0b8`](#insn-00a3e0b8)

~~~json
{
  "source": "00a3e0b8",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a3e0bc`](#insn-00a3e0bc)

~~~json
{
  "source": "00a3e0bc",
  "target": "00a3e0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e0c4`](#insn-00a3e0c4)

~~~json
{
  "source": "00a3e0c4",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e0cc`](#insn-00a3e0cc)

~~~json
{
  "source": "00a3e0cc",
  "target": "00c8b460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b460",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e0d8`](#insn-00a3e0d8)

~~~json
{
  "source": "00a3e0d8",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e0e4`](#insn-00a3e0e4)

~~~json
{
  "source": "00a3e0e4",
  "target": "009ccbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e0f4`](#insn-00a3e0f4)

~~~json
{
  "source": "00a3e0f4",
  "target": "00ac7b74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e100`](#insn-00a3e100)

~~~json
{
  "source": "00a3e100",
  "target": "00acb024",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e110`](#insn-00a3e110)

~~~json
{
  "source": "00a3e110",
  "target": "00c8b6a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b6a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e110`](#insn-00a3e110)

~~~json
{
  "source": "00a3e110",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e114`](#insn-00a3e114)

~~~json
{
  "source": "00a3e114",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e120`](#insn-00a3e120)

~~~json
{
  "source": "00a3e120",
  "target": "00acab44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e124`](#insn-00a3e124)

~~~json
{
  "source": "00a3e124",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e12c`](#insn-00a3e12c)

~~~json
{
  "source": "00a3e12c",
  "target": "00a3e13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e130`](#insn-00a3e130)

~~~json
{
  "source": "00a3e130",
  "target": "00a3e150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e138`](#insn-00a3e138)

~~~json
{
  "source": "00a3e138",
  "target": "00a3e144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e144`](#insn-00a3e144)

~~~json
{
  "source": "00a3e144",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e148`](#insn-00a3e148)

~~~json
{
  "source": "00a3e148",
  "target": "00c8b6c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b6c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e148`](#insn-00a3e148)

~~~json
{
  "source": "00a3e148",
  "target": "00c8b6d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b6d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e14c`](#insn-00a3e14c)

~~~json
{
  "source": "00a3e14c",
  "target": "00a40d3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e14c`](#insn-00a3e14c)

~~~json
{
  "source": "00a3e14c",
  "target": "00a40d40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e164`](#insn-00a3e164)

~~~json
{
  "source": "00a3e164",
  "target": "00ac9b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e174`](#insn-00a3e174)

~~~json
{
  "source": "00a3e174",
  "target": "00c8b728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b728",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e174`](#insn-00a3e174)

~~~json
{
  "source": "00a3e174",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e178`](#insn-00a3e178)

~~~json
{
  "source": "00a3e178",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e18c`](#insn-00a3e18c)

~~~json
{
  "source": "00a3e18c",
  "target": "00ac9b5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e190`](#insn-00a3e190)

~~~json
{
  "source": "00a3e190",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e198`](#insn-00a3e198)

~~~json
{
  "source": "00a3e198",
  "target": "00a3e1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e19c`](#insn-00a3e19c)

~~~json
{
  "source": "00a3e19c",
  "target": "00a3e1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1a4`](#insn-00a3e1a4)

~~~json
{
  "source": "00a3e1a4",
  "target": "00a3e1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1b0`](#insn-00a3e1b0)

~~~json
{
  "source": "00a3e1b0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1b4`](#insn-00a3e1b4)

~~~json
{
  "source": "00a3e1b4",
  "target": "00c8b748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b748",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e1b4`](#insn-00a3e1b4)

~~~json
{
  "source": "00a3e1b4",
  "target": "00c8b750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3e1b8`](#insn-00a3e1b8)

~~~json
{
  "source": "00a3e1b8",
  "target": "00a40ddc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e1b8`](#insn-00a3e1b8)

~~~json
{
  "source": "00a3e1b8",
  "target": "00a40de0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e1cc`](#insn-00a3e1cc)

~~~json
{
  "source": "00a3e1cc",
  "target": "00ac9fd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e1d4`](#insn-00a3e1d4)

~~~json
{
  "source": "00a3e1d4",
  "target": "0066d11c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3e1dc`](#insn-00a3e1dc)

~~~json
{
  "source": "00a3e1dc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1e4`](#insn-00a3e1e4)

~~~json
{
  "source": "00a3e1e4",
  "target": "00a3e264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1e8`](#insn-00a3e1e8)

~~~json
{
  "source": "00a3e1e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1ec`](#insn-00a3e1ec)

~~~json
{
  "source": "00a3e1ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1f0`](#insn-00a3e1f0)

~~~json
{
  "source": "00a3e1f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1f4`](#insn-00a3e1f4)

~~~json
{
  "source": "00a3e1f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e1f8`](#insn-00a3e1f8)

~~~json
{
  "source": "00a3e1f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3e264`](#insn-00a3e264)

~~~json
{
  "source": "00a3e264",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
