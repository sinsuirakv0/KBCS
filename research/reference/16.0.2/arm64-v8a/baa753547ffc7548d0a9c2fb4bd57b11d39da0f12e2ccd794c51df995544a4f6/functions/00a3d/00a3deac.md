# 00a3deac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "556940a629d67a17dee56e10754618742b8f360fd54277dedc22d36e7b0fecec"
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
