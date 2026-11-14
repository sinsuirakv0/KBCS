# 008accfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "008accfc",
  "name": "FUN_008accfc",
  "size": 1220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb8a3a4d0d1c706298c18f4bfff40fdbacefc601ba9846793ec2b6f4947a398e",
  "source_text_sha256": "cb8a3a4d0d1c706298c18f4bfff40fdbacefc601ba9846793ec2b6f4947a398e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043df04](../0043d/0043df04.md)
- [00442e98](../00442/00442e98.md)
- [00448254](../00448/00448254.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cdb4](../0046c/0046cdb4.md)
- [0046ce6c](../0046c/0046ce6c.md)
- [0048d1b4](../0048d/0048d1b4.md)
- [00550f88](../00550/00550f88.md)
- [005515d4](../00551/005515d4.md)
- [005517c4](../00551/005517c4.md)
- [0055220c](../00552/0055220c.md)
- [0055aa14](../0055a/0055aa14.md)
- [0055aa24](../0055a/0055aa24.md)
- [0055ca30](../0055c/0055ca30.md)
- [005979b4](../00597/005979b4.md)
- [005c1b8c](../005c1/005c1b8c.md)
- [00691c08](../00691/00691c08.md)
- [008524fc](../00852/008524fc.md)
- [0085bd5c](../0085b/0085bd5c.md)
- [008ad384](../008ad/008ad384.md)
- [008ad958](../008ad/008ad958.md)
- [008ad95c](../008ad/008ad95c.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c594d0](../00c59/00c594d0.md)

## 関連文字列（未確認候補）

~~~text
"scratch_SNS_%03d"
"screenshot.jpg"
~~~

## 疑似コード / UTF-8 9275 bytes

~~~c

void FUN_008accfc(long param_1)

{
  undefined4 uVar1;
  undefined4 uVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  void *pvVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  int iVar13;
  int iVar14;
  ulong uVar15;
  undefined8 uVar16;
  long lVar17;
  long *plVar18;
  byte local_120;
  char cStack_11f;
  char cStack_11e;
  undefined6 uStack_11d;
  undefined7 uStack_117;
  char cStack_110;
  undefined1 uStack_10f;
  undefined6 uStack_10e;
  byte local_108 [16];
  void *local_f8;
  ulong local_f0;
  long *local_e8;
  undefined8 local_e0;
  long *local_d8;
  byte local_d0;
  char acStack_cf [6];
  char cStack_c9;
  char cStack_c8;
  char acStack_c7 [7];
  void *local_c0;
  byte local_b8 [16];
  void *local_a8;
  undefined8 local_a0;
  long *local_98;
  void *local_90;
  undefined1 auStack_88 [8];
  long *local_80;
  long local_70;
  
                    /* try { // try from 008acd18 to 009acd1f has its CatchHandler @ 008ace70 */
  lVar5 = tpidr_el0;
                    /* try { // try from 008acd20 to 009acd2f has its CatchHandler @ 008acebc */
  local_70 = *(long *)(lVar5 + 0x28);
  uVar1 = *(undefined4 *)(PTR_DAT_00c9bc08 + 8);
  uVar2 = *(undefined4 *)(PTR_DAT_00c9bc08 + 0xc);
  pvVar6 = *(void **)(PTR_DAT_00c9bc08 + 8);
  plVar18 = *(long **)(param_1 + 8);
  thunk_FUN_0057eb94(&local_a0);
  local_d0 = 0x1c;
  acStack_c7[6] = 0;
  acStack_cf[0] = s_screenshot_jpg_002a22d8[0];
  acStack_cf[1] = s_screenshot_jpg_002a22d8[1];
  acStack_cf[2] = s_screenshot_jpg_002a22d8[2];
  acStack_cf[3] = s_screenshot_jpg_002a22d8[3];
  acStack_cf[4] = s_screenshot_jpg_002a22d8[4];
  acStack_cf[5] = s_screenshot_jpg_002a22d8[5];
  cStack_c9 = (char)s_screenshot_jpg_002a22d8._6_2_;
  cStack_c8 = SUB21(s_screenshot_jpg_002a22d8._6_2_,1);
  acStack_c7[0] = s_screenshot_jpg_002a22d8[8];
  acStack_c7[1] = s_screenshot_jpg_002a22d8[9];
  acStack_c7[2] = s_screenshot_jpg_002a22d8[10];
  acStack_c7[3] = s_screenshot_jpg_002a22d8[0xb];
  acStack_c7[4] = s_screenshot_jpg_002a22d8[0xc];
  acStack_c7[5] = s_screenshot_jpg_002a22d8[0xd];
                    /* try { // try from 008acd70 to 009acdab has its CatchHandler @ 008acee8 */
  FUN_0043df04(local_b8,&local_a0,&local_d0);
  if ((local_d0 & 1) != 0) {
    _ZdlPv(local_c0);
  }
  if (((byte)local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  FUN_0055220c(&local_e0,uVar1,uVar2);
  local_a0 = &PTR_FUN_00c84740;
  local_98 = plVar18;
  local_90 = pvVar6;
  local_80 = &local_a0;
  FUN_005517c4(local_e0,&local_a0);
                    /* try { // try from 008acdd0 to 009acddf has its CatchHandler @ 008ace78 */
  if (local_80 == &local_a0) {
    lVar17 = 0x20;
    plVar18 = &local_a0;
LAB_008acdf0:
    (**(code **)(*plVar18 + lVar17))();
  }
  else if (local_80 != (long *)0x0) {
                    /* try { // try from 008acde0 to 009acf47 has its CatchHandler @ 008acca8 */
    lVar17 = 0x28;
    plVar18 = local_80;
    goto LAB_008acdf0;
  }
  FUN_008524fc();
  iVar9 = FUN_0046cd24();
  iVar14 = iVar9 + -0x3bf;
  if (0x3bf < iVar9) {
    iVar14 = iVar9 + -0x3c0;
  }
  uVar15 = FUN_0046cdb4(&DAT_00ca5d30);
  iVar14 = iVar14 >> 1;
  if ((uVar15 & 1) != 0) {
    FUN_008524fc();
    uVar15 = FUN_0085bd5c();
    if ((uVar15 & 1) == 0) {
      iVar9 = FUN_0046ce6c(&DAT_00ca5d30);
      iVar14 = iVar9 + iVar14;
    }
  }
  iVar10 = FUN_0055aa24();
  iVar4 = DAT_00ca5d48;
  lVar17 = FUN_008524fc();
  iVar9 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar17);
  iVar11 = FUN_0055aa14();
  iVar8 = DAT_00ca5d4c;
                    /* catch() { ... } // from try @ 008acd18 with catch @ 008ace70 */
  iVar12 = FUN_0055aa24();
  iVar7 = DAT_00ca5d48;
                    /* catch() { ... } // from try @ 008acdd0 with catch @ 008ace78 */
  iVar13 = FUN_0055aa14();
  iVar3 = 0;
  if (iVar4 != 0) {
    iVar3 = (iVar10 * iVar14) / iVar4;
  }
  iVar14 = 0;
  if (iVar8 != 0) {
    iVar14 = ((iVar9 + 0x37) * iVar11) / iVar8;
  }
  iVar9 = 0;
  if (iVar7 != 0) {
    iVar9 = (iVar12 * 0x3c0) / iVar7;
  }
  iVar4 = 0;
  if (DAT_00ca5d4c != 0) {
    iVar4 = (iVar13 * 0x212) / DAT_00ca5d4c;
  }
  FUN_005515d4(&local_f0,local_e0,iVar3,iVar14,iVar9,iVar4);
  plVar18 = local_e8;
                    /* catch() { ... } // from try @ 008acd20 with catch @ 008acebc */
  if (local_f0 == 0) {
                    /* catch() { ... } // from try @ 008accec with catch @ 008acee0 */
    plVar18 = (long *)0x0;
    local_a0 = (undefined **)0x0;
    local_98 = (long *)0x0;
  }
  else {
    local_a0 = (undefined **)local_f0;
    local_98 = local_e8;
    if (local_e8 != (long *)0x0) {
      FUN_00c54d60(1,local_e8 + 1);
    }
  }
                    /* catch() { ... } // from try @ 008acd70 with catch @ 008acee8 */
  uVar15 = thunk_FUN_005803f8(local_f0,2,local_b8);
  if ((plVar18 != (long *)0x0) &&
     (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar18 + 1), lVar17 == 0)) {
    (**(code **)(*plVar18 + 0x10))(plVar18);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
  }
  if ((uVar15 & 1) == 0) goto LAB_008ad10c;
  lVar17 = FUN_008524fc();
  FUN_008ad384(&local_a0,lVar17 + 0x1d58);
  cStack_c8 = '\0';
  acStack_c7[0] = '\0';
  acStack_c7[1] = '\0';
  acStack_c7[2] = '\0';
  acStack_c7[3] = '\0';
  acStack_c7[4] = '\0';
  acStack_c7[5] = '\0';
  acStack_c7[6] = 0;
  local_c0 = (void *)0x0;
  local_d0 = (byte)&cStack_c8;
  acStack_cf = SUB86((ulong)&cStack_c8 >> 8,0);
  cStack_c9 = (char)((ulong)&cStack_c8 >> 0x38);
                    /* try { // try from 008acf48 to 009acfa7 has its CatchHandler @ 008acf48
                       catch() { ... } // from try @ 008acf48 with catch @ 008acf48
                       catch() { ... } // from try @ 008ad2e8 with catch @ 008acf48 */
  FUN_00691c08(&local_d0,local_a0,&local_98);
  FUN_005c1b8c(auStack_88,local_80);
  FUN_005c1b8c(&local_a0,local_98);
  uStack_10f = 0;
  uVar1 = *(undefined4 *)(CONCAT17(cStack_c9,CONCAT61(acStack_cf,local_d0)) + 0x20);
  local_120 = 0x20;
  uStack_117 = (undefined7)s_scratch_SNS__03d_002a7fd9._8_8_;
  cStack_110 = SUB81(s_scratch_SNS__03d_002a7fd9._8_8_,7);
  cStack_11f = (char)s_scratch_SNS__03d_002a7fd9._0_8_;
  cStack_11e = SUB81(s_scratch_SNS__03d_002a7fd9._0_8_,1);
  uStack_11d = SUB86(s_scratch_SNS__03d_002a7fd9._0_8_,2);
  lVar17 = FUN_008524fc();
  FUN_00448254(&local_a0,&local_120,0,*(undefined4 *)(lVar17 + 0x1dd0));
                    /* try { // try from 008acfa8 to 009acfb7 has its CatchHandler @ 008ad550 */
  FUN_0048d1b4(local_108,&local_a0);
  if (((ulong)local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if ((local_120 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_10e,CONCAT11(uStack_10f,cStack_110)));
  }
  uVar15 = (ulong)local_a0 >> 0x28;
  local_a0 = (undefined **)CONCAT35((uint3)uVar15 & 0xffff00,0x3e72623c08);
  local_120 = 2;
  cStack_11f = 10;
  cStack_11e = 0;
  uVar16 = FUN_00442e98(local_108,&local_a0,&local_120,0);
                    /* try { // try from 008ad008 to 009ad013 has its CatchHandler @ 008ad528 */
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_(local_108,uVar16);
  if ((local_120 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_10e,CONCAT11(uStack_10f,cStack_110)));
  }
                    /* try { // try from 008ad028 to 009ad03b has its CatchHandler @ 008ad508 */
  if (((ulong)local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  iVar14 = FUN_0055aa24();
                    /* try { // try from 008ad03c to 009ad04b has its CatchHandler @ 008ad4d4 */
  if (iVar14 < 0) {
    iVar14 = iVar14 + 1;
  }
  iVar9 = FUN_0055aa14();
  FUN_00448254(&local_120,local_108,0,uVar1);
  local_80 = (long *)0x0;
  if (iVar9 < 0) {
    iVar9 = iVar9 + 1;
  }
  thunk_FUN_0058d010((float)(iVar14 >> 1),(float)(iVar9 >> 1),0x3f800000,0x3f800000,&local_120,
                     local_b8,&local_a0);
  if (local_80 == &local_a0) {
    lVar17 = 0x20;
    plVar18 = &local_a0;
LAB_008ad0d4:
                    /* try { // try from 008ad0dc to 009ad0eb has its CatchHandler @ 008ad4a8 */
    (**(code **)(*plVar18 + lVar17))();
  }
  else if (local_80 != (long *)0x0) {
    lVar17 = 0x28;
    plVar18 = local_80;
    goto LAB_008ad0d4;
  }
  if ((local_120 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_10e,CONCAT11(uStack_10f,cStack_110)));
  }
  if ((local_108[0] & 1) != 0) {
    _ZdlPv(local_f8);
  }
  FUN_005c1b8c(&local_d0,CONCAT17(acStack_c7[6],CONCAT61(acStack_c7._0_6_,cStack_c8)));
LAB_008ad10c:
  if ((local_e8 != (long *)0x0) &&
     (lVar17 = FUN_00c54d90(0xffffffffffffffff,local_e8 + 1), lVar17 == 0)) {
    (**(code **)(*local_e8 + 0x10))(local_e8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_e8);
  }
                    /* try { // try from 008ad150 to 009ad163 has its CatchHandler @ 008ad4a4 */
  if ((local_d8 != (long *)0x0) &&
     (lVar17 = FUN_00c54d90(0xffffffffffffffff,local_d8 + 1), lVar17 == 0)) {
    (**(code **)(*local_d8 + 0x10))(local_d8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_d8);
  }
  if ((local_b8[0] & 1) != 0) {
    _ZdlPv(local_a8);
  }
                    /* try { // try from 008ad164 to 009ad173 has its CatchHandler @ 008ad4a0 */
  if (*(long *)(lVar5 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
