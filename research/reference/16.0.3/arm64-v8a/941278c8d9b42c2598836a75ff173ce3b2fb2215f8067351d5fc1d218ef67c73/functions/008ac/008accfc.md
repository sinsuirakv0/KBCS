# 008accfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008abd50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ab/008abd50.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0051.md#compare-2fca9f105608bba545ffaf58fdc01150)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "cb8a3a4d0d1c706298c18f4bfff40fdbacefc601ba9846793ec2b6f4947a398e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008accfc",
        "008ad1bb"
      ],
      [
        "008ad358",
        "008ad35b"
      ]
    ],
    "bytes_sha256": "13d11247eced72f758e9d5e31cc4c32fe5073c626368eeaae078804f72cb9ea1",
    "instruction_count": 305,
    "instruction_bytes": 1220,
    "body_bytes": 1220,
    "indirect": 5,
    "unresolved": 4
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008accfc"></a> `008accfc` | `ff c3 04 d1` | sub sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-008acd00"></a> `008acd00` | `fd 7b 0d a9` | stp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008acd04"></a> `008acd04` | `fc 6f 0e a9` | stp x28,x27,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-008acd08"></a> `008acd08` | `fa 67 0f a9` | stp x26,x25,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-008acd0c"></a> `008acd0c` | `f8 5f 10 a9` | stp x24,x23,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-008acd10"></a> `008acd10` | `f6 57 11 a9` | stp x22,x21,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-008acd14"></a> `008acd14` | `f4 4f 12 a9` | stp x20,x19,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-008acd18"></a> `008acd18` | `fd 43 03 91` | add x29,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-008acd1c"></a> `008acd1c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008acd20"></a> `008acd20` | `69 1f 00 f0` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-008acd24"></a> `008acd24` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008acd28"></a> `008acd28` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-008acd2c"></a> `008acd2c` | `29 05 46 f9` | ldr x9,[x9, #0xc08] | `FALL_THROUGH`
<a id="insn-008acd30"></a> `008acd30` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008acd34"></a> `008acd34` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acd38"></a> `008acd38` | `33 51 41 29` | ldp w19,w20,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-008acd3c"></a> `008acd3c` | `15 04 40 f9` | ldr x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008acd40"></a> `008acd40` | `92 90 f2 97` | bl 0x00550f88 | `UNCONDITIONAL_CALL`
<a id="insn-008acd44"></a> `008acd44` | `a9 cf ff d0` | adrp x9,0x2a2000 | `FALL_THROUGH`
<a id="insn-008acd48"></a> `008acd48` | `29 61 0b 91` | add x9,x9,#0x2d8 | `FALL_THROUGH`
<a id="insn-008acd4c"></a> `008acd4c` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-008acd50"></a> `008acd50` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-008acd54"></a> `008acd54` | `29 61 40 f8` | ldur x9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-008acd58"></a> `008acd58` | `e8 83 01 39` | strb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008acd5c"></a> `008acd5c` | `ff bf 01 39` | strb wzr,[sp, #0x6f] | `FALL_THROUGH`
<a id="insn-008acd60"></a> `008acd60` | `ea 13 06 f8` | stur x10,[sp, #0x61] | `FALL_THROUGH`
<a id="insn-008acd64"></a> `008acd64` | `e9 73 06 f8` | stur x9,[sp, #0x67] | `FALL_THROUGH`
<a id="insn-008acd68"></a> `008acd68` | `a8 63 01 d1` | sub x8,x29,#0x58 | `FALL_THROUGH`
<a id="insn-008acd6c"></a> `008acd6c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acd70"></a> `008acd70` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008acd74"></a> `008acd74` | `64 44 ee 97` | bl 0x0043df04 | `UNCONDITIONAL_CALL`
<a id="insn-008acd78"></a> `008acd78` | `e8 83 41 39` | ldrb w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008acd7c"></a> `008acd7c` | `68 00 00 36` | tbz w8,#0x0,0x008acd88 | `CONDITIONAL_JUMP`
<a id="insn-008acd80"></a> `008acd80` | `e0 3b 40 f9` | ldr x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008acd84"></a> `008acd84` | `73 b0 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008acd88"></a> `008acd88` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acd8c"></a> `008acd8c` | `68 00 00 36` | tbz w8,#0x0,0x008acd98 | `CONDITIONAL_JUMP`
<a id="insn-008acd90"></a> `008acd90` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-008acd94"></a> `008acd94` | `6f b0 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008acd98"></a> `008acd98` | `e8 43 01 91` | add x8,sp,#0x50 | `FALL_THROUGH`
<a id="insn-008acd9c"></a> `008acd9c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-008acda0"></a> `008acda0` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-008acda4"></a> `008acda4` | `1a 95 f2 97` | bl 0x0055220c | `UNCONDITIONAL_CALL`
<a id="insn-008acda8"></a> `008acda8` | `68 82 14 aa` | orr x8,x19,x20, LSL #0x20 | `FALL_THROUGH`
<a id="insn-008acdac"></a> `008acdac` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008acdb0"></a> `008acdb0` | `c9 1e 00 90` | adrp x9,0xc84000 | `FALL_THROUGH`
<a id="insn-008acdb4"></a> `008acdb4` | `29 01 1d 91` | add x9,x9,#0x740 | `FALL_THROUGH`
<a id="insn-008acdb8"></a> `008acdb8` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acdbc"></a> `008acdbc` | `a9 57 3c a9` | stp x9,x21,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acdc0"></a> `008acdc0` | `a8 03 1d f8` | stur x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-008acdc4"></a> `008acdc4` | `b3 03 1e f8` | stur x19,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008acdc8"></a> `008acdc8` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acdcc"></a> `008acdcc` | `7e 92 f2 97` | bl 0x005517c4 | `UNCONDITIONAL_CALL`
<a id="insn-008acdd0"></a> `008acdd0` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008acdd4"></a> `008acdd4` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-008acdd8"></a> `008acdd8` | `80 00 00 54` | b.eq 0x008acde8 | `CONDITIONAL_JUMP`
<a id="insn-008acddc"></a> `008acddc` | `00 01 00 b4` | cbz x0,0x008acdfc | `CONDITIONAL_JUMP`
<a id="insn-008acde0"></a> `008acde0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008acde4"></a> `008acde4` | `03 00 00 14` | b 0x008acdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-008acde8"></a> `008acde8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008acdec"></a> `008acdec` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acdf0"></a> `008acdf0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008acdf4"></a> `008acdf4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008acdf8"></a> `008acdf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008acdfc"></a> `008acdfc` | `f3 2b 40 f9` | ldr x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008ace00"></a> `008ace00` | `bf 95 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008ace04"></a> `008ace04` | `c8 ff ee 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-008ace08"></a> `008ace08` | `08 00 0f 71` | subs w8,w0,#0x3c0 | `FALL_THROUGH`
<a id="insn-008ace0c"></a> `008ace0c` | `09 fc 0e 51` | sub w9,w0,#0x3bf | `FALL_THROUGH`
<a id="insn-008ace10"></a> `008ace10` | `35 b1 88 1a` | csel w21,w9,w8,lt | `FALL_THROUGH`
<a id="insn-008ace14"></a> `008ace14` | `d4 1f 00 b0` | adrp x20,0xca5000 | `FALL_THROUGH`
<a id="insn-008ace18"></a> `008ace18` | `94 c2 34 91` | add x20,x20,#0xd30 | `FALL_THROUGH`
<a id="insn-008ace1c"></a> `008ace1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008ace20"></a> `008ace20` | `e5 ff ee 97` | bl 0x0046cdb4 | `UNCONDITIONAL_CALL`
<a id="insn-008ace24"></a> `008ace24` | `b9 7e 01 13` | asr w25,w21,#0x1 | `FALL_THROUGH`
<a id="insn-008ace28"></a> `008ace28` | `00 01 00 36` | tbz w0,#0x0,0x008ace48 | `CONDITIONAL_JUMP`
<a id="insn-008ace2c"></a> `008ace2c` | `b4 95 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008ace30"></a> `008ace30` | `cb bb fe 97` | bl 0x0085bd5c | `UNCONDITIONAL_CALL`
<a id="insn-008ace34"></a> `008ace34` | `a0 00 00 37` | tbnz w0,#0x0,0x008ace48 | `CONDITIONAL_JUMP`
<a id="insn-008ace38"></a> `008ace38` | `c0 1f 00 b0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008ace3c"></a> `008ace3c` | `00 c0 34 91` | add x0,x0,#0xd30 | `FALL_THROUGH`
<a id="insn-008ace40"></a> `008ace40` | `0b 00 ef 97` | bl 0x0046ce6c | `UNCONDITIONAL_CALL`
<a id="insn-008ace44"></a> `008ace44` | `19 00 19 0b` | add w25,w0,w25 | `FALL_THROUGH`
<a id="insn-008ace48"></a> `008ace48` | `f7 b6 f2 97` | bl 0x0055aa24 | `UNCONDITIONAL_CALL`
<a id="insn-008ace4c"></a> `008ace4c` | `9a 1a 40 b9` | ldr w26,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-008ace50"></a> `008ace50` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-008ace54"></a> `008ace54` | `aa 95 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008ace58"></a> `008ace58` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-008ace5c"></a> `008ace5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-008ace60"></a> `008ace60` | `1b 68 68 b8` | ldr w27,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ace64"></a> `008ace64` | `ec b6 f2 97` | bl 0x0055aa14 | `UNCONDITIONAL_CALL`
<a id="insn-008ace68"></a> `008ace68` | `9c 1e 40 b9` | ldr w28,[x20, #0x1c] | `FALL_THROUGH`
<a id="insn-008ace6c"></a> `008ace6c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-008ace70"></a> `008ace70` | `ed b6 f2 97` | bl 0x0055aa24 | `UNCONDITIONAL_CALL`
<a id="insn-008ace74"></a> `008ace74` | `98 1a 40 b9` | ldr w24,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-008ace78"></a> `008ace78` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-008ace7c"></a> `008ace7c` | `e6 b6 f2 97` | bl 0x0055aa14 | `UNCONDITIONAL_CALL`
<a id="insn-008ace80"></a> `008ace80` | `a8 7e 19 1b` | mul w8,w21,w25 | `FALL_THROUGH`
<a id="insn-008ace84"></a> `008ace84` | `89 1e 40 b9` | ldr w9,[x20, #0x1c] | `FALL_THROUGH`
<a id="insn-008ace88"></a> `008ace88` | `01 0d da 1a` | sdiv w1,w8,w26 | `FALL_THROUGH`
<a id="insn-008ace8c"></a> `008ace8c` | `68 df 00 11` | add w8,w27,#0x37 | `FALL_THROUGH`
<a id="insn-008ace90"></a> `008ace90` | `08 7d 16 1b` | mul w8,w8,w22 | `FALL_THROUGH`
<a id="insn-008ace94"></a> `008ace94` | `02 0d dc 1a` | sdiv w2,w8,w28 | `FALL_THROUGH`
<a id="insn-008ace98"></a> `008ace98` | `e8 56 16 53` | lsl w8,w23,#0xa | `FALL_THROUGH`
<a id="insn-008ace9c"></a> `008ace9c` | `08 19 17 4b` | sub w8,w8,w23, LSL #0x6 | `FALL_THROUGH`
<a id="insn-008acea0"></a> `008acea0` | `03 0d d8 1a` | sdiv w3,w8,w24 | `FALL_THROUGH`
<a id="insn-008acea4"></a> `008acea4` | `48 42 80 52` | mov w8,#0x212 | `FALL_THROUGH`
<a id="insn-008acea8"></a> `008acea8` | `08 7c 08 1b` | mul w8,w0,w8 | `FALL_THROUGH`
<a id="insn-008aceac"></a> `008aceac` | `04 0d c9 1a` | sdiv w4,w8,w9 | `FALL_THROUGH`
<a id="insn-008aceb0"></a> `008aceb0` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008aceb4"></a> `008aceb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008aceb8"></a> `008aceb8` | `c7 91 f2 97` | bl 0x005515d4 | `UNCONDITIONAL_CALL`
<a id="insn-008acebc"></a> `008acebc` | `f4 23 40 f9` | ldr x20,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008acec0"></a> `008acec0` | `14 01 00 b4` | cbz x20,0x008acee0 | `CONDITIONAL_JUMP`
<a id="insn-008acec4"></a> `008acec4` | `f3 27 40 f9` | ldr x19,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-008acec8"></a> `008acec8` | `b4 4f 3c a9` | stp x20,x19,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acecc"></a> `008acecc` | `f3 00 00 b4` | cbz x19,0x008acee8 | `CONDITIONAL_JUMP`
<a id="insn-008aced0"></a> `008aced0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008aced4"></a> `008aced4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-008aced8"></a> `008aced8` | `a2 9f 0e 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-008acedc"></a> `008acedc` | `03 00 00 14` | b 0x008acee8 | `UNCONDITIONAL_JUMP`
<a id="insn-008acee0"></a> `008acee0` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-008acee4"></a> `008acee4` | `bf 7f 3c a9` | stp xzr,xzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acee8"></a> `008acee8` | `a2 63 01 d1` | sub x2,x29,#0x58 | `FALL_THROUGH`
<a id="insn-008aceec"></a> `008aceec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008acef0"></a> `008acef0` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-008acef4"></a> `008acef4` | `cf be f2 97` | bl 0x0055ca30 | `UNCONDITIONAL_CALL`
<a id="insn-008acef8"></a> `008acef8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-008acefc"></a> `008acefc` | `b3 00 00 b4` | cbz x19,0x008acf10 | `CONDITIONAL_JUMP`
<a id="insn-008acf00"></a> `008acf00` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008acf04"></a> `008acf04` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008acf08"></a> `008acf08` | `a2 9f 0e 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-008acf0c"></a> `008acf0c` | `00 0d 00 b4` | cbz x0,0x008ad0ac | `CONDITIONAL_JUMP`
<a id="insn-008acf10"></a> `008acf10` | `f4 0f 00 36` | tbz w20,#0x0,0x008ad10c | `CONDITIONAL_JUMP`
<a id="insn-008acf14"></a> `008acf14` | `7a 95 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008acf18"></a> `008acf18` | `09 ab 83 52` | mov w9,#0x1d58 | `FALL_THROUGH`
<a id="insn-008acf1c"></a> `008acf1c` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acf20"></a> `008acf20` | `00 00 09 8b` | add x0,x0,x9 | `FALL_THROUGH`
<a id="insn-008acf24"></a> `008acf24` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acf28"></a> `008acf28` | `17 01 00 94` | bl 0x008ad384 | `UNCONDITIONAL_CALL`
<a id="insn-008acf2c"></a> `008acf2c` | `e8 83 01 91` | add x8,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008acf30"></a> `008acf30` | `a1 03 5c f8` | ldur x1,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acf34"></a> `008acf34` | `ff ff 06 a9` | stp xzr,xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-008acf38"></a> `008acf38` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-008acf3c"></a> `008acf3c` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008acf40"></a> `008acf40` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008acf44"></a> `008acf44` | `62 22 00 91` | add x2,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008acf48"></a> `008acf48` | `30 93 f7 97` | bl 0x00691c08 | `UNCONDITIONAL_CALL`
<a id="insn-008acf4c"></a> `008acf4c` | `a1 03 5e f8` | ldur x1,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008acf50"></a> `008acf50` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acf54"></a> `008acf54` | `00 61 00 91` | add x0,x8,#0x18 | `FALL_THROUGH`
<a id="insn-008acf58"></a> `008acf58` | `0d 53 f4 97` | bl 0x005c1b8c | `UNCONDITIONAL_CALL`
<a id="insn-008acf5c"></a> `008acf5c` | `a1 83 5c f8` | ldur x1,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-008acf60"></a> `008acf60` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acf64"></a> `008acf64` | `0a 53 f4 97` | bl 0x005c1b8c | `UNCONDITIONAL_CALL`
<a id="insn-008acf68"></a> `008acf68` | `e8 33 40 f9` | ldr x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008acf6c"></a> `008acf6c` | `ca cf ff f0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-008acf70"></a> `008acf70` | `4a 65 3f 91` | add x10,x10,#0xfd9 | `FALL_THROUGH`
<a id="insn-008acf74"></a> `008acf74` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-008acf78"></a> `008acf78` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-008acf7c"></a> `008acf7c` | `ff 87 00 39` | strb wzr,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008acf80"></a> `008acf80` | `13 21 40 b9` | ldr w19,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-008acf84"></a> `008acf84` | `e9 43 00 39` | strb w9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008acf88"></a> `008acf88` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-008acf8c"></a> `008acf8c` | `5c 95 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008acf90"></a> `008acf90` | `02 d0 5d b9` | ldr w2,[x0, #0x1dd0] | `FALL_THROUGH`
<a id="insn-008acf94"></a> `008acf94` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acf98"></a> `008acf98` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008acf9c"></a> `008acf9c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-008acfa0"></a> `008acfa0` | `ad 6c ee 97` | bl 0x00448254 | `UNCONDITIONAL_CALL`
<a id="insn-008acfa4"></a> `008acfa4` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008acfa8"></a> `008acfa8` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acfac"></a> `008acfac` | `82 80 ef 97` | bl 0x0048d1b4 | `UNCONDITIONAL_CALL`
<a id="insn-008acfb0"></a> `008acfb0` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acfb4"></a> `008acfb4` | `68 00 00 36` | tbz w8,#0x0,0x008acfc0 | `CONDITIONAL_JUMP`
<a id="insn-008acfb8"></a> `008acfb8` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-008acfbc"></a> `008acfbc` | `e5 af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008acfc0"></a> `008acfc0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008acfc4"></a> `008acfc4` | `68 00 00 36` | tbz w8,#0x0,0x008acfd0 | `CONDITIONAL_JUMP`
<a id="insn-008acfc8"></a> `008acfc8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008acfcc"></a> `008acfcc` | `e1 af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008acfd0"></a> `008acfd0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-008acfd4"></a> `008acfd4` | `89 47 8c 52` | mov w9,#0x623c | `FALL_THROUGH`
<a id="insn-008acfd8"></a> `008acfd8` | `bf 53 1c 38` | sturb wzr,[x29, #-0x3b] | `FALL_THROUGH`
<a id="insn-008acfdc"></a> `008acfdc` | `49 ce a7 72` | movk w9,#0x3e72, LSL #16 | `FALL_THROUGH`
<a id="insn-008acfe0"></a> `008acfe0` | `a8 03 1c 38` | sturb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008acfe4"></a> `008acfe4` | `48 40 81 52` | mov w8,#0xa02 | `FALL_THROUGH`
<a id="insn-008acfe8"></a> `008acfe8` | `a9 13 1c b8` | stur w9,[x29, #-0x3f] | `FALL_THROUGH`
<a id="insn-008acfec"></a> `008acfec` | `e8 23 00 79` | strh w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008acff0"></a> `008acff0` | `ff 4b 00 39` | strb wzr,[sp, #0x12] | `FALL_THROUGH`
<a id="insn-008acff4"></a> `008acff4` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008acff8"></a> `008acff8` | `a1 03 01 d1` | sub x1,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008acffc"></a> `008acffc` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008ad000"></a> `008ad000` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-008ad004"></a> `008ad004` | `a5 57 ee 97` | bl 0x00442e98 | `UNCONDITIONAL_CALL`
<a id="insn-008ad008"></a> `008ad008` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-008ad00c"></a> `008ad00c` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ad010"></a> `008ad010` | `30 b1 0e 94` | bl 0x00c594d0 | `UNCONDITIONAL_CALL`
<a id="insn-008ad014"></a> `008ad014` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ad018"></a> `008ad018` | `68 00 00 36` | tbz w8,#0x0,0x008ad024 | `CONDITIONAL_JUMP`
<a id="insn-008ad01c"></a> `008ad01c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ad020"></a> `008ad020` | `cc af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008ad024"></a> `008ad024` | `a8 03 5c 38` | ldurb w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-008ad028"></a> `008ad028` | `68 00 00 36` | tbz w8,#0x0,0x008ad034 | `CONDITIONAL_JUMP`
<a id="insn-008ad02c"></a> `008ad02c` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-008ad030"></a> `008ad030` | `c8 af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008ad034"></a> `008ad034` | `7c b6 f2 97` | bl 0x0055aa24 | `UNCONDITIONAL_CALL`
<a id="insn-008ad038"></a> `008ad038` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-008ad03c"></a> `008ad03c` | `15 a4 80 1a` | cinc w21,w0,lt | `FALL_THROUGH`
<a id="insn-008ad040"></a> `008ad040` | `75 b6 f2 97` | bl 0x0055aa14 | `UNCONDITIONAL_CALL`
<a id="insn-008ad044"></a> `008ad044` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-008ad048"></a> `008ad048` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008ad04c"></a> `008ad04c` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008ad050"></a> `008ad050` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-008ad054"></a> `008ad054` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-008ad058"></a> `008ad058` | `7f 6c ee 97` | bl 0x00448254 | `UNCONDITIONAL_CALL`
<a id="insn-008ad05c"></a> `008ad05c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-008ad060"></a> `008ad060` | `a9 7e 01 13` | asr w9,w21,#0x1 | `FALL_THROUGH`
<a id="insn-008ad064"></a> `008ad064` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008ad068"></a> `008ad068` | `88 a6 94 1a` | cinc w8,w20,lt | `FALL_THROUGH`
<a id="insn-008ad06c"></a> `008ad06c` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-008ad070"></a> `008ad070` | `20 01 22 1e` | scvtf s0,w9 | `FALL_THROUGH`
<a id="insn-008ad074"></a> `008ad074` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-008ad078"></a> `008ad078` | `02 10 2e 1e` | fmov s2,0x3f800000 | `FALL_THROUGH`
<a id="insn-008ad07c"></a> `008ad07c` | `03 10 2e 1e` | fmov s3,0x3f800000 | `FALL_THROUGH`
<a id="insn-008ad080"></a> `008ad080` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008ad084"></a> `008ad084` | `a1 63 01 d1` | sub x1,x29,#0x58 | `FALL_THROUGH`
<a id="insn-008ad088"></a> `008ad088` | `a2 03 01 d1` | sub x2,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008ad08c"></a> `008ad08c` | `b3 03 01 d1` | sub x19,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008ad090"></a> `008ad090` | `49 aa f3 97` | bl 0x005979b4 | `UNCONDITIONAL_CALL`
<a id="insn-008ad094"></a> `008ad094` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008ad098"></a> `008ad098` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-008ad09c"></a> `008ad09c` | `80 01 00 54` | b.eq 0x008ad0cc | `CONDITIONAL_JUMP`
<a id="insn-008ad0a0"></a> `008ad0a0` | `00 02 00 b4` | cbz x0,0x008ad0e0 | `CONDITIONAL_JUMP`
<a id="insn-008ad0a4"></a> `008ad0a4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008ad0a8"></a> `008ad0a8` | `0b 00 00 14` | b 0x008ad0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-008ad0ac"></a> `008ad0ac` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008ad0b0"></a> `008ad0b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad0b4"></a> `008ad0b4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008ad0b8"></a> `008ad0b8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008ad0bc"></a> `008ad0bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad0c0"></a> `008ad0c0` | `98 af 0e 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-008ad0c4"></a> `008ad0c4` | `94 f2 07 37` | tbnz w20,#0x0,0x008acf14 | `CONDITIONAL_JUMP`
<a id="insn-008ad0c8"></a> `008ad0c8` | `11 00 00 14` | b 0x008ad10c | `UNCONDITIONAL_JUMP`
<a id="insn-008ad0cc"></a> `008ad0cc` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008ad0d0"></a> `008ad0d0` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-008ad0d4"></a> `008ad0d4` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008ad0d8"></a> `008ad0d8` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ad0dc"></a> `008ad0dc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008ad0e0"></a> `008ad0e0` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ad0e4"></a> `008ad0e4` | `68 00 00 36` | tbz w8,#0x0,0x008ad0f0 | `CONDITIONAL_JUMP`
<a id="insn-008ad0e8"></a> `008ad0e8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ad0ec"></a> `008ad0ec` | `99 af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008ad0f0"></a> `008ad0f0` | `e8 a3 40 39` | ldrb w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008ad0f4"></a> `008ad0f4` | `68 00 00 36` | tbz w8,#0x0,0x008ad100 | `CONDITIONAL_JUMP`
<a id="insn-008ad0f8"></a> `008ad0f8` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-008ad0fc"></a> `008ad0fc` | `95 af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008ad100"></a> `008ad100` | `e1 37 40 f9` | ldr x1,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-008ad104"></a> `008ad104` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008ad108"></a> `008ad108` | `a1 52 f4 97` | bl 0x005c1b8c | `UNCONDITIONAL_CALL`
<a id="insn-008ad10c"></a> `008ad10c` | `f3 27 40 f9` | ldr x19,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-008ad110"></a> `008ad110` | `73 01 00 b4` | cbz x19,0x008ad13c | `CONDITIONAL_JUMP`
<a id="insn-008ad114"></a> `008ad114` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008ad118"></a> `008ad118` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008ad11c"></a> `008ad11c` | `1d 9f 0e 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-008ad120"></a> `008ad120` | `e0 00 00 b5` | cbnz x0,0x008ad13c | `CONDITIONAL_JUMP`
<a id="insn-008ad124"></a> `008ad124` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008ad128"></a> `008ad128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad12c"></a> `008ad12c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008ad130"></a> `008ad130` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008ad134"></a> `008ad134` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad138"></a> `008ad138` | `7a af 0e 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-008ad13c"></a> `008ad13c` | `f3 2f 40 f9` | ldr x19,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-008ad140"></a> `008ad140` | `b3 00 00 b4` | cbz x19,0x008ad154 | `CONDITIONAL_JUMP`
<a id="insn-008ad144"></a> `008ad144` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008ad148"></a> `008ad148` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008ad14c"></a> `008ad14c` | `11 9f 0e 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-008ad150"></a> `008ad150` | `40 02 00 b4` | cbz x0,0x008ad198 | `CONDITIONAL_JUMP`
<a id="insn-008ad154"></a> `008ad154` | `a8 83 5a 38` | ldurb w8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-008ad158"></a> `008ad158` | `68 00 00 36` | tbz w8,#0x0,0x008ad164 | `CONDITIONAL_JUMP`
<a id="insn-008ad15c"></a> `008ad15c` | `a0 83 5b f8` | ldur x0,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-008ad160"></a> `008ad160` | `7c af 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008ad164"></a> `008ad164` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008ad168"></a> `008ad168` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-008ad16c"></a> `008ad16c` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008ad170"></a> `008ad170` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008ad174"></a> `008ad174` | `21 0f 00 54` | b.ne 0x008ad358 | `CONDITIONAL_JUMP`
<a id="insn-008ad178"></a> `008ad178` | `f4 4f 52 a9` | ldp x20,x19,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-008ad17c"></a> `008ad17c` | `f6 57 51 a9` | ldp x22,x21,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-008ad180"></a> `008ad180` | `f8 5f 50 a9` | ldp x24,x23,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-008ad184"></a> `008ad184` | `fa 67 4f a9` | ldp x26,x25,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-008ad188"></a> `008ad188` | `fc 6f 4e a9` | ldp x28,x27,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-008ad18c"></a> `008ad18c` | `fd 7b 4d a9` | ldp x29,x30,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008ad190"></a> `008ad190` | `ff c3 04 91` | add sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-008ad194"></a> `008ad194` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008ad198"></a> `008ad198` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008ad19c"></a> `008ad19c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad1a0"></a> `008ad1a0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008ad1a4"></a> `008ad1a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008ad1a8"></a> `008ad1a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ad1ac"></a> `008ad1ac` | `5d af 0e 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-008ad1b0"></a> `008ad1b0` | `a8 83 5a 38` | ldurb w8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-008ad1b4"></a> `008ad1b4` | `48 fd 07 37` | tbnz w8,#0x0,0x008ad15c | `CONDITIONAL_JUMP`
<a id="insn-008ad1b8"></a> `008ad1b8` | `eb ff ff 17` | b 0x008ad164 | `UNCONDITIONAL_JUMP`
<a id="insn-008ad358"></a> `008ad358` | `0a af 0e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008accfc`](#insn-008accfc) 範囲 `[['008accfc', '008acd17']]`
  - `FALL_THROUGH` [`008acd14`](#insn-008acd14) → [`008acd18`](#insn-008acd18)
- ブロック [`008acd18`](#insn-008acd18) 範囲 `[['008acd18', '008acd1f']]`
  - `FALL_THROUGH` [`008acd1c`](#insn-008acd1c) → [`008acd20`](#insn-008acd20)
- ブロック [`008acd20`](#insn-008acd20) 範囲 `[['008acd20', '008acd6f']]`
  - `FALL_THROUGH` [`008acd6c`](#insn-008acd6c) → [`008acd70`](#insn-008acd70)
- ブロック [`008acd70`](#insn-008acd70) 範囲 `[['008acd70', '008acd7f']]`
  - `CONDITIONAL_JUMP` [`008acd7c`](#insn-008acd7c) → [`008acd88`](#insn-008acd88)
  - `FALL_THROUGH` [`008acd7c`](#insn-008acd7c) → [`008acd80`](#insn-008acd80)
- ブロック [`008acd80`](#insn-008acd80) 範囲 `[['008acd80', '008acd87']]`
  - `FALL_THROUGH` [`008acd84`](#insn-008acd84) → [`008acd88`](#insn-008acd88)
- ブロック [`008acd88`](#insn-008acd88) 範囲 `[['008acd88', '008acd8f']]`
  - `CONDITIONAL_JUMP` [`008acd8c`](#insn-008acd8c) → [`008acd98`](#insn-008acd98)
  - `FALL_THROUGH` [`008acd8c`](#insn-008acd8c) → [`008acd90`](#insn-008acd90)
- ブロック [`008acd90`](#insn-008acd90) 範囲 `[['008acd90', '008acd97']]`
  - `FALL_THROUGH` [`008acd94`](#insn-008acd94) → [`008acd98`](#insn-008acd98)
- ブロック [`008acd98`](#insn-008acd98) 範囲 `[['008acd98', '008acdcf']]`
  - `FALL_THROUGH` [`008acdcc`](#insn-008acdcc) → [`008acdd0`](#insn-008acdd0)
- ブロック [`008acdd0`](#insn-008acdd0) 範囲 `[['008acdd0', '008acddb']]`
  - `CONDITIONAL_JUMP` [`008acdd8`](#insn-008acdd8) → [`008acde8`](#insn-008acde8)
  - `FALL_THROUGH` [`008acdd8`](#insn-008acdd8) → [`008acddc`](#insn-008acddc)
- ブロック [`008acddc`](#insn-008acddc) 範囲 `[['008acddc', '008acddf']]`
  - `CONDITIONAL_JUMP` [`008acddc`](#insn-008acddc) → [`008acdfc`](#insn-008acdfc)
  - `FALL_THROUGH` [`008acddc`](#insn-008acddc) → [`008acde0`](#insn-008acde0)
- ブロック [`008acde0`](#insn-008acde0) 範囲 `[['008acde0', '008acde7']]`
  - `UNCONDITIONAL_JUMP` [`008acde4`](#insn-008acde4) → [`008acdf0`](#insn-008acdf0)
- ブロック [`008acde8`](#insn-008acde8) 範囲 `[['008acde8', '008acdef']]`
  - `FALL_THROUGH` [`008acdec`](#insn-008acdec) → [`008acdf0`](#insn-008acdf0)
- ブロック [`008acdf0`](#insn-008acdf0) 範囲 `[['008acdf0', '008acdfb']]`
  - `FALL_THROUGH` [`008acdf8`](#insn-008acdf8) → [`008acdfc`](#insn-008acdfc)
- ブロック [`008acdfc`](#insn-008acdfc) 範囲 `[['008acdfc', '008ace2b']]`
  - `CONDITIONAL_JUMP` [`008ace28`](#insn-008ace28) → [`008ace48`](#insn-008ace48)
  - `FALL_THROUGH` [`008ace28`](#insn-008ace28) → [`008ace2c`](#insn-008ace2c)
- ブロック [`008ace2c`](#insn-008ace2c) 範囲 `[['008ace2c', '008ace37']]`
  - `CONDITIONAL_JUMP` [`008ace34`](#insn-008ace34) → [`008ace48`](#insn-008ace48)
  - `FALL_THROUGH` [`008ace34`](#insn-008ace34) → [`008ace38`](#insn-008ace38)
- ブロック [`008ace38`](#insn-008ace38) 範囲 `[['008ace38', '008ace47']]`
  - `FALL_THROUGH` [`008ace44`](#insn-008ace44) → [`008ace48`](#insn-008ace48)
- ブロック [`008ace48`](#insn-008ace48) 範囲 `[['008ace48', '008ace6f']]`
  - `FALL_THROUGH` [`008ace6c`](#insn-008ace6c) → [`008ace70`](#insn-008ace70)
- ブロック [`008ace70`](#insn-008ace70) 範囲 `[['008ace70', '008ace77']]`
  - `FALL_THROUGH` [`008ace74`](#insn-008ace74) → [`008ace78`](#insn-008ace78)
- ブロック [`008ace78`](#insn-008ace78) 範囲 `[['008ace78', '008acebb']]`
  - `FALL_THROUGH` [`008aceb8`](#insn-008aceb8) → [`008acebc`](#insn-008acebc)
- ブロック [`008acebc`](#insn-008acebc) 範囲 `[['008acebc', '008acec3']]`
  - `CONDITIONAL_JUMP` [`008acec0`](#insn-008acec0) → [`008acee0`](#insn-008acee0)
  - `FALL_THROUGH` [`008acec0`](#insn-008acec0) → [`008acec4`](#insn-008acec4)
- ブロック [`008acec4`](#insn-008acec4) 範囲 `[['008acec4', '008acecf']]`
  - `CONDITIONAL_JUMP` [`008acecc`](#insn-008acecc) → [`008acee8`](#insn-008acee8)
  - `FALL_THROUGH` [`008acecc`](#insn-008acecc) → [`008aced0`](#insn-008aced0)
- ブロック [`008aced0`](#insn-008aced0) 範囲 `[['008aced0', '008acedf']]`
  - `UNCONDITIONAL_JUMP` [`008acedc`](#insn-008acedc) → [`008acee8`](#insn-008acee8)
- ブロック [`008acee0`](#insn-008acee0) 範囲 `[['008acee0', '008acee7']]`
  - `FALL_THROUGH` [`008acee4`](#insn-008acee4) → [`008acee8`](#insn-008acee8)
- ブロック [`008acee8`](#insn-008acee8) 範囲 `[['008acee8', '008aceff']]`
  - `CONDITIONAL_JUMP` [`008acefc`](#insn-008acefc) → [`008acf10`](#insn-008acf10)
  - `FALL_THROUGH` [`008acefc`](#insn-008acefc) → [`008acf00`](#insn-008acf00)
- ブロック [`008acf00`](#insn-008acf00) 範囲 `[['008acf00', '008acf0f']]`
  - `CONDITIONAL_JUMP` [`008acf0c`](#insn-008acf0c) → [`008ad0ac`](#insn-008ad0ac)
  - `FALL_THROUGH` [`008acf0c`](#insn-008acf0c) → [`008acf10`](#insn-008acf10)
- ブロック [`008acf10`](#insn-008acf10) 範囲 `[['008acf10', '008acf13']]`
  - `CONDITIONAL_JUMP` [`008acf10`](#insn-008acf10) → [`008ad10c`](#insn-008ad10c)
  - `FALL_THROUGH` [`008acf10`](#insn-008acf10) → [`008acf14`](#insn-008acf14)
- ブロック [`008acf14`](#insn-008acf14) 範囲 `[['008acf14', '008acf47']]`
  - `FALL_THROUGH` [`008acf44`](#insn-008acf44) → [`008acf48`](#insn-008acf48)
- ブロック [`008acf48`](#insn-008acf48) 範囲 `[['008acf48', '008acfa7']]`
  - `FALL_THROUGH` [`008acfa4`](#insn-008acfa4) → [`008acfa8`](#insn-008acfa8)
- ブロック [`008acfa8`](#insn-008acfa8) 範囲 `[['008acfa8', '008acfb7']]`
  - `CONDITIONAL_JUMP` [`008acfb4`](#insn-008acfb4) → [`008acfc0`](#insn-008acfc0)
  - `FALL_THROUGH` [`008acfb4`](#insn-008acfb4) → [`008acfb8`](#insn-008acfb8)
- ブロック [`008acfb8`](#insn-008acfb8) 範囲 `[['008acfb8', '008acfbf']]`
  - `FALL_THROUGH` [`008acfbc`](#insn-008acfbc) → [`008acfc0`](#insn-008acfc0)
- ブロック [`008acfc0`](#insn-008acfc0) 範囲 `[['008acfc0', '008acfc7']]`
  - `CONDITIONAL_JUMP` [`008acfc4`](#insn-008acfc4) → [`008acfd0`](#insn-008acfd0)
  - `FALL_THROUGH` [`008acfc4`](#insn-008acfc4) → [`008acfc8`](#insn-008acfc8)
- ブロック [`008acfc8`](#insn-008acfc8) 範囲 `[['008acfc8', '008acfcf']]`
  - `FALL_THROUGH` [`008acfcc`](#insn-008acfcc) → [`008acfd0`](#insn-008acfd0)
- ブロック [`008acfd0`](#insn-008acfd0) 範囲 `[['008acfd0', '008ad007']]`
  - `FALL_THROUGH` [`008ad004`](#insn-008ad004) → [`008ad008`](#insn-008ad008)
- ブロック [`008ad008`](#insn-008ad008) 範囲 `[['008ad008', '008ad01b']]`
  - `CONDITIONAL_JUMP` [`008ad018`](#insn-008ad018) → [`008ad024`](#insn-008ad024)
  - `FALL_THROUGH` [`008ad018`](#insn-008ad018) → [`008ad01c`](#insn-008ad01c)
- ブロック [`008ad01c`](#insn-008ad01c) 範囲 `[['008ad01c', '008ad023']]`
  - `FALL_THROUGH` [`008ad020`](#insn-008ad020) → [`008ad024`](#insn-008ad024)
- ブロック [`008ad024`](#insn-008ad024) 範囲 `[['008ad024', '008ad027']]`
  - `FALL_THROUGH` [`008ad024`](#insn-008ad024) → [`008ad028`](#insn-008ad028)
- ブロック [`008ad028`](#insn-008ad028) 範囲 `[['008ad028', '008ad02b']]`
  - `CONDITIONAL_JUMP` [`008ad028`](#insn-008ad028) → [`008ad034`](#insn-008ad034)
  - `FALL_THROUGH` [`008ad028`](#insn-008ad028) → [`008ad02c`](#insn-008ad02c)
- ブロック [`008ad02c`](#insn-008ad02c) 範囲 `[['008ad02c', '008ad033']]`
  - `FALL_THROUGH` [`008ad030`](#insn-008ad030) → [`008ad034`](#insn-008ad034)
- ブロック [`008ad034`](#insn-008ad034) 範囲 `[['008ad034', '008ad03b']]`
  - `FALL_THROUGH` [`008ad038`](#insn-008ad038) → [`008ad03c`](#insn-008ad03c)
- ブロック [`008ad03c`](#insn-008ad03c) 範囲 `[['008ad03c', '008ad09f']]`
  - `CONDITIONAL_JUMP` [`008ad09c`](#insn-008ad09c) → [`008ad0cc`](#insn-008ad0cc)
  - `FALL_THROUGH` [`008ad09c`](#insn-008ad09c) → [`008ad0a0`](#insn-008ad0a0)
- ブロック [`008ad0a0`](#insn-008ad0a0) 範囲 `[['008ad0a0', '008ad0a3']]`
  - `CONDITIONAL_JUMP` [`008ad0a0`](#insn-008ad0a0) → [`008ad0e0`](#insn-008ad0e0)
  - `FALL_THROUGH` [`008ad0a0`](#insn-008ad0a0) → [`008ad0a4`](#insn-008ad0a4)
- ブロック [`008ad0a4`](#insn-008ad0a4) 範囲 `[['008ad0a4', '008ad0ab']]`
  - `UNCONDITIONAL_JUMP` [`008ad0a8`](#insn-008ad0a8) → [`008ad0d4`](#insn-008ad0d4)
- ブロック [`008ad0ac`](#insn-008ad0ac) 範囲 `[['008ad0ac', '008ad0c7']]`
  - `CONDITIONAL_JUMP` [`008ad0c4`](#insn-008ad0c4) → [`008acf14`](#insn-008acf14)
  - `FALL_THROUGH` [`008ad0c4`](#insn-008ad0c4) → [`008ad0c8`](#insn-008ad0c8)
- ブロック [`008ad0c8`](#insn-008ad0c8) 範囲 `[['008ad0c8', '008ad0cb']]`
  - `UNCONDITIONAL_JUMP` [`008ad0c8`](#insn-008ad0c8) → [`008ad10c`](#insn-008ad10c)
- ブロック [`008ad0cc`](#insn-008ad0cc) 範囲 `[['008ad0cc', '008ad0d3']]`
  - `FALL_THROUGH` [`008ad0d0`](#insn-008ad0d0) → [`008ad0d4`](#insn-008ad0d4)
- ブロック [`008ad0d4`](#insn-008ad0d4) 範囲 `[['008ad0d4', '008ad0db']]`
  - `FALL_THROUGH` [`008ad0d8`](#insn-008ad0d8) → [`008ad0dc`](#insn-008ad0dc)
- ブロック [`008ad0dc`](#insn-008ad0dc) 範囲 `[['008ad0dc', '008ad0df']]`
  - `FALL_THROUGH` [`008ad0dc`](#insn-008ad0dc) → [`008ad0e0`](#insn-008ad0e0)
- ブロック [`008ad0e0`](#insn-008ad0e0) 範囲 `[['008ad0e0', '008ad0e7']]`
  - `CONDITIONAL_JUMP` [`008ad0e4`](#insn-008ad0e4) → [`008ad0f0`](#insn-008ad0f0)
  - `FALL_THROUGH` [`008ad0e4`](#insn-008ad0e4) → [`008ad0e8`](#insn-008ad0e8)
- ブロック [`008ad0e8`](#insn-008ad0e8) 範囲 `[['008ad0e8', '008ad0ef']]`
  - `FALL_THROUGH` [`008ad0ec`](#insn-008ad0ec) → [`008ad0f0`](#insn-008ad0f0)
- ブロック [`008ad0f0`](#insn-008ad0f0) 範囲 `[['008ad0f0', '008ad0f7']]`
  - `CONDITIONAL_JUMP` [`008ad0f4`](#insn-008ad0f4) → [`008ad100`](#insn-008ad100)
  - `FALL_THROUGH` [`008ad0f4`](#insn-008ad0f4) → [`008ad0f8`](#insn-008ad0f8)
- ブロック [`008ad0f8`](#insn-008ad0f8) 範囲 `[['008ad0f8', '008ad0ff']]`
  - `FALL_THROUGH` [`008ad0fc`](#insn-008ad0fc) → [`008ad100`](#insn-008ad100)
- ブロック [`008ad100`](#insn-008ad100) 範囲 `[['008ad100', '008ad10b']]`
  - `FALL_THROUGH` [`008ad108`](#insn-008ad108) → [`008ad10c`](#insn-008ad10c)
- ブロック [`008ad10c`](#insn-008ad10c) 範囲 `[['008ad10c', '008ad113']]`
  - `CONDITIONAL_JUMP` [`008ad110`](#insn-008ad110) → [`008ad13c`](#insn-008ad13c)
  - `FALL_THROUGH` [`008ad110`](#insn-008ad110) → [`008ad114`](#insn-008ad114)
- ブロック [`008ad114`](#insn-008ad114) 範囲 `[['008ad114', '008ad123']]`
  - `CONDITIONAL_JUMP` [`008ad120`](#insn-008ad120) → [`008ad13c`](#insn-008ad13c)
  - `FALL_THROUGH` [`008ad120`](#insn-008ad120) → [`008ad124`](#insn-008ad124)
- ブロック [`008ad124`](#insn-008ad124) 範囲 `[['008ad124', '008ad13b']]`
  - `FALL_THROUGH` [`008ad138`](#insn-008ad138) → [`008ad13c`](#insn-008ad13c)
- ブロック [`008ad13c`](#insn-008ad13c) 範囲 `[['008ad13c', '008ad143']]`
  - `CONDITIONAL_JUMP` [`008ad140`](#insn-008ad140) → [`008ad154`](#insn-008ad154)
  - `FALL_THROUGH` [`008ad140`](#insn-008ad140) → [`008ad144`](#insn-008ad144)
- ブロック [`008ad144`](#insn-008ad144) 範囲 `[['008ad144', '008ad14f']]`
  - `FALL_THROUGH` [`008ad14c`](#insn-008ad14c) → [`008ad150`](#insn-008ad150)
- ブロック [`008ad150`](#insn-008ad150) 範囲 `[['008ad150', '008ad153']]`
  - `CONDITIONAL_JUMP` [`008ad150`](#insn-008ad150) → [`008ad198`](#insn-008ad198)
  - `FALL_THROUGH` [`008ad150`](#insn-008ad150) → [`008ad154`](#insn-008ad154)
- ブロック [`008ad154`](#insn-008ad154) 範囲 `[['008ad154', '008ad15b']]`
  - `CONDITIONAL_JUMP` [`008ad158`](#insn-008ad158) → [`008ad164`](#insn-008ad164)
  - `FALL_THROUGH` [`008ad158`](#insn-008ad158) → [`008ad15c`](#insn-008ad15c)
- ブロック [`008ad15c`](#insn-008ad15c) 範囲 `[['008ad15c', '008ad163']]`
  - `FALL_THROUGH` [`008ad160`](#insn-008ad160) → [`008ad164`](#insn-008ad164)
- ブロック [`008ad164`](#insn-008ad164) 範囲 `[['008ad164', '008ad177']]`
  - `CONDITIONAL_JUMP` [`008ad174`](#insn-008ad174) → [`008ad358`](#insn-008ad358)
  - `FALL_THROUGH` [`008ad174`](#insn-008ad174) → [`008ad178`](#insn-008ad178)
- ブロック [`008ad178`](#insn-008ad178) 範囲 `[['008ad178', '008ad197']]`
- ブロック [`008ad198`](#insn-008ad198) 範囲 `[['008ad198', '008ad1b7']]`
  - `CONDITIONAL_JUMP` [`008ad1b4`](#insn-008ad1b4) → [`008ad15c`](#insn-008ad15c)
  - `FALL_THROUGH` [`008ad1b4`](#insn-008ad1b4) → [`008ad1b8`](#insn-008ad1b8)
- ブロック [`008ad1b8`](#insn-008ad1b8) 範囲 `[['008ad1b8', '008ad1bb']]`
  - `UNCONDITIONAL_JUMP` [`008ad1b8`](#insn-008ad1b8) → [`008ad164`](#insn-008ad164)
- ブロック [`008ad358`](#insn-008ad358) 範囲 `[['008ad358', '008ad35b']]`

## 命令位置別の参照

- [`008acd00`](#insn-008acd00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd04`](#insn-008acd04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd08`](#insn-008acd08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd0c`](#insn-008acd0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd10`](#insn-008acd10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd14`](#insn-008acd14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd24`](#insn-008acd24) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd2c`](#insn-008acd2c) → `00c9bc08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008acd30`](#insn-008acd30) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd38`](#insn-008acd38) → `00ca5d38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008acd38`](#insn-008acd38) → `00ca5d3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008acd40`](#insn-008acd40) → [`00550f88`](../00550/00550f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00550f88` · 推定シンボル `None` · 推定型 `None`
- [`008acd50`](#insn-008acd50) → `002a22d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008acd54`](#insn-008acd54) → `002a22de`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008acd58`](#insn-008acd58) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd5c`](#insn-008acd5c) → `Stack[-0xc1]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd60`](#insn-008acd60) → `Stack[-0xcf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd64`](#insn-008acd64) → `Stack[-0xc9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd74`](#insn-008acd74) → [`0043df04`](../0043d/0043df04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043df04` · 推定シンボル `None` · 推定型 `None`
- [`008acd78`](#insn-008acd78) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd7c`](#insn-008acd7c) → [`008acd88`](#insn-008acd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd80`](#insn-008acd80) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd84`](#insn-008acd84) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008acd88`](#insn-008acd88) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd8c`](#insn-008acd8c) → [`008acd98`](#insn-008acd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd90`](#insn-008acd90) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acd94`](#insn-008acd94) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008acda4`](#insn-008acda4) → [`0055220c`](../00552/0055220c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055220c` · 推定シンボル `None` · 推定型 `None`
- [`008acdac`](#insn-008acdac) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdbc`](#insn-008acdbc) → `00c84740`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008acdbc`](#insn-008acdbc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdc0`](#insn-008acdc0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdc4`](#insn-008acdc4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdcc`](#insn-008acdcc) → [`005517c4`](../00551/005517c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005517c4` · 推定シンボル `None` · 推定型 `None`
- [`008acdd0`](#insn-008acdd0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdd8`](#insn-008acdd8) → [`008acde8`](#insn-008acde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acddc`](#insn-008acddc) → [`008acdfc`](#insn-008acdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acde4`](#insn-008acde4) → [`008acdf0`](#insn-008acdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdf0`](#insn-008acdf0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acdf4`](#insn-008acdf4) → `00c84760`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008acdf4`](#insn-008acdf4) → `00c84768`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`008acdf8`](#insn-008acdf8) → [`008ad958`](../008ad/008ad958.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `008ad958` · 推定シンボル `None` · 推定型 `None`
- [`008acdf8`](#insn-008acdf8) → [`008ad95c`](../008ad/008ad95c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `008ad95c` · 推定シンボル `None` · 推定型 `None`
- [`008acdfc`](#insn-008acdfc) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace00`](#insn-008ace00) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008ace04`](#insn-008ace04) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`008ace1c`](#insn-008ace1c) → `00ca5d30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008ace20`](#insn-008ace20) → [`0046cdb4`](../0046c/0046cdb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cdb4` · 推定シンボル `None` · 推定型 `None`
- [`008ace28`](#insn-008ace28) → [`008ace48`](#insn-008ace48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace2c`](#insn-008ace2c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008ace30`](#insn-008ace30) → [`0085bd5c`](../0085b/0085bd5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085bd5c` · 推定シンボル `None` · 推定型 `None`
- [`008ace34`](#insn-008ace34) → [`008ace48`](#insn-008ace48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ace3c`](#insn-008ace3c) → `00ca5d30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008ace40`](#insn-008ace40) → [`0046ce6c`](../0046c/0046ce6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ce6c` · 推定シンボル `None` · 推定型 `None`
- [`008ace48`](#insn-008ace48) → [`0055aa24`](../0055a/0055aa24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa24` · 推定シンボル `None` · 推定型 `None`
- [`008ace4c`](#insn-008ace4c) → `00ca5d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008ace54`](#insn-008ace54) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008ace60`](#insn-008ace60) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008ace64`](#insn-008ace64) → [`0055aa14`](../0055a/0055aa14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa14` · 推定シンボル `None` · 推定型 `None`
- [`008ace68`](#insn-008ace68) → `00ca5d4c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008ace70`](#insn-008ace70) → [`0055aa24`](../0055a/0055aa24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa24` · 推定シンボル `None` · 推定型 `None`
- [`008ace74`](#insn-008ace74) → `00ca5d48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008ace7c`](#insn-008ace7c) → [`0055aa14`](../0055a/0055aa14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa14` · 推定シンボル `None` · 推定型 `None`
- [`008ace84`](#insn-008ace84) → `00ca5d4c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`008aceb8`](#insn-008aceb8) → [`005515d4`](../00551/005515d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005515d4` · 推定シンボル `None` · 推定型 `None`
- [`008acebc`](#insn-008acebc) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acec0`](#insn-008acec0) → [`008acee0`](#insn-008acee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acec4`](#insn-008acec4) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acec8`](#insn-008acec8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acecc`](#insn-008acecc) → [`008acee8`](#insn-008acee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008aced8`](#insn-008aced8) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`008acedc`](#insn-008acedc) → [`008acee8`](#insn-008acee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acee4`](#insn-008acee4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acef4`](#insn-008acef4) → [`0055ca30`](../0055c/0055ca30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055ca30` · 推定シンボル `None` · 推定型 `None`
- [`008acefc`](#insn-008acefc) → [`008acf10`](#insn-008acf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf08`](#insn-008acf08) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`008acf0c`](#insn-008acf0c) → [`008ad0ac`](#insn-008ad0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf10`](#insn-008acf10) → [`008ad10c`](#insn-008ad10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf14`](#insn-008acf14) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008acf28`](#insn-008acf28) → [`008ad384`](../008ad/008ad384.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ad384` · 推定シンボル `None` · 推定型 `None`
- [`008acf30`](#insn-008acf30) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf34`](#insn-008acf34) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf3c`](#insn-008acf3c) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf48`](#insn-008acf48) → [`00691c08`](../00691/00691c08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00691c08` · 推定シンボル `None` · 推定型 `None`
- [`008acf4c`](#insn-008acf4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf58`](#insn-008acf58) → [`005c1b8c`](../005c1/005c1b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c1b8c` · 推定シンボル `None` · 推定型 `None`
- [`008acf5c`](#insn-008acf5c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf64`](#insn-008acf64) → [`005c1b8c`](../005c1/005c1b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c1b8c` · 推定シンボル `None` · 推定型 `None`
- [`008acf68`](#insn-008acf68) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf74`](#insn-008acf74) → `002a7fd9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008acf7c`](#insn-008acf7c) → `Stack[-0x10f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf80`](#insn-008acf80) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf84`](#insn-008acf84) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf88`](#insn-008acf88) → `Stack[-0x11f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acf8c`](#insn-008acf8c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008acfa0`](#insn-008acfa0) → [`00448254`](../00448/00448254.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00448254` · 推定シンボル `None` · 推定型 `None`
- [`008acfac`](#insn-008acfac) → [`0048d1b4`](../0048d/0048d1b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048d1b4` · 推定シンボル `None` · 推定型 `None`
- [`008acfb0`](#insn-008acfb0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfb4`](#insn-008acfb4) → [`008acfc0`](#insn-008acfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfb8`](#insn-008acfb8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfbc`](#insn-008acfbc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008acfc0`](#insn-008acfc0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfc4`](#insn-008acfc4) → [`008acfd0`](#insn-008acfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfc8`](#insn-008acfc8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfcc`](#insn-008acfcc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008acfd8`](#insn-008acfd8) → `Stack[-0x9b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfe0`](#insn-008acfe0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfe8`](#insn-008acfe8) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acfec`](#insn-008acfec) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008acff0`](#insn-008acff0) → `Stack[-0x11e]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad004`](#insn-008ad004) → [`00442e98`](../00442/00442e98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442e98` · 推定シンボル `None` · 推定型 `None`
- [`008ad010`](#insn-008ad010) → [`00c594d0`](../00c59/00c594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c594d0` · 推定シンボル `None` · 推定型 `None`
- [`008ad014`](#insn-008ad014) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad018`](#insn-008ad018) → [`008ad024`](#insn-008ad024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad01c`](#insn-008ad01c) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad020`](#insn-008ad020) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008ad024`](#insn-008ad024) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad028`](#insn-008ad028) → [`008ad034`](#insn-008ad034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad02c`](#insn-008ad02c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad030`](#insn-008ad030) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008ad034`](#insn-008ad034) → [`0055aa24`](../0055a/0055aa24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa24` · 推定シンボル `None` · 推定型 `None`
- [`008ad040`](#insn-008ad040) → [`0055aa14`](../0055a/0055aa14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0055aa14` · 推定シンボル `None` · 推定型 `None`
- [`008ad058`](#insn-008ad058) → [`00448254`](../00448/00448254.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00448254` · 推定シンボル `None` · 推定型 `None`
- [`008ad064`](#insn-008ad064) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad090`](#insn-008ad090) → [`005979b4`](../00597/005979b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005979b4` · 推定シンボル `None` · 推定型 `None`
- [`008ad094`](#insn-008ad094) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad09c`](#insn-008ad09c) → [`008ad0cc`](#insn-008ad0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0a0`](#insn-008ad0a0) → [`008ad0e0`](#insn-008ad0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0a8`](#insn-008ad0a8) → [`008ad0d4`](#insn-008ad0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0c0`](#insn-008ad0c0) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`008ad0c4`](#insn-008ad0c4) → [`008acf14`](#insn-008acf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0c8`](#insn-008ad0c8) → [`008ad10c`](#insn-008ad10c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0d4`](#insn-008ad0d4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0e0`](#insn-008ad0e0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0e4`](#insn-008ad0e4) → [`008ad0f0`](#insn-008ad0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0e8`](#insn-008ad0e8) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0ec`](#insn-008ad0ec) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008ad0f0`](#insn-008ad0f0) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0f4`](#insn-008ad0f4) → [`008ad100`](#insn-008ad100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0f8`](#insn-008ad0f8) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad0fc`](#insn-008ad0fc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008ad100`](#insn-008ad100) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad108`](#insn-008ad108) → [`005c1b8c`](../005c1/005c1b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c1b8c` · 推定シンボル `None` · 推定型 `None`
- [`008ad10c`](#insn-008ad10c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad110`](#insn-008ad110) → [`008ad13c`](#insn-008ad13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad11c`](#insn-008ad11c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`008ad120`](#insn-008ad120) → [`008ad13c`](#insn-008ad13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad138`](#insn-008ad138) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`008ad13c`](#insn-008ad13c) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad140`](#insn-008ad140) → [`008ad154`](#insn-008ad154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad14c`](#insn-008ad14c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`008ad150`](#insn-008ad150) → [`008ad198`](#insn-008ad198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad154`](#insn-008ad154) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad158`](#insn-008ad158) → [`008ad164`](#insn-008ad164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad15c`](#insn-008ad15c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad160`](#insn-008ad160) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008ad164`](#insn-008ad164) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad16c`](#insn-008ad16c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad174`](#insn-008ad174) → [`008ad358`](#insn-008ad358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad178`](#insn-008ad178) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad17c`](#insn-008ad17c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad180`](#insn-008ad180) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad184`](#insn-008ad184) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad188`](#insn-008ad188) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad18c`](#insn-008ad18c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad1ac`](#insn-008ad1ac) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`008ad1b0`](#insn-008ad1b0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad1b4`](#insn-008ad1b4) → [`008ad15c`](#insn-008ad15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad1b8`](#insn-008ad1b8) → [`008ad164`](#insn-008ad164) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ad358`](#insn-008ad358) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008acd00`](#insn-008acd00)

~~~json
{
  "source": "008acd00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd04`](#insn-008acd04)

~~~json
{
  "source": "008acd04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd08`](#insn-008acd08)

~~~json
{
  "source": "008acd08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd0c`](#insn-008acd0c)

~~~json
{
  "source": "008acd0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd10`](#insn-008acd10)

~~~json
{
  "source": "008acd10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd14`](#insn-008acd14)

~~~json
{
  "source": "008acd14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd24`](#insn-008acd24)

~~~json
{
  "source": "008acd24",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd2c`](#insn-008acd2c)

~~~json
{
  "source": "008acd2c",
  "target": "00c9bc08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acd30`](#insn-008acd30)

~~~json
{
  "source": "008acd30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd38`](#insn-008acd38)

~~~json
{
  "source": "008acd38",
  "target": "00ca5d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d38",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008acd38`](#insn-008acd38)

~~~json
{
  "source": "008acd38",
  "target": "00ca5d3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d3c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008acd40`](#insn-008acd40)

~~~json
{
  "source": "008acd40",
  "target": "00550f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acd50`](#insn-008acd50)

~~~json
{
  "source": "008acd50",
  "target": "002a22d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a22d8",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "73637265656e73686f742e6a706700",
  "capture_start": "002a22d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008acd54`](#insn-008acd54)

~~~json
{
  "source": "008acd54",
  "target": "002a22de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a22d8",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "73637265656e73686f742e6a706700",
  "capture_start": "002a22d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008acd58`](#insn-008acd58)

~~~json
{
  "source": "008acd58",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd5c`](#insn-008acd5c)

~~~json
{
  "source": "008acd5c",
  "target": "Stack[-0xc1]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd60`](#insn-008acd60)

~~~json
{
  "source": "008acd60",
  "target": "Stack[-0xcf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd64`](#insn-008acd64)

~~~json
{
  "source": "008acd64",
  "target": "Stack[-0xc9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd74`](#insn-008acd74)

~~~json
{
  "source": "008acd74",
  "target": "0043df04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acd78`](#insn-008acd78)

~~~json
{
  "source": "008acd78",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd7c`](#insn-008acd7c)

~~~json
{
  "source": "008acd7c",
  "target": "008acd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd80`](#insn-008acd80)

~~~json
{
  "source": "008acd80",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd84`](#insn-008acd84)

~~~json
{
  "source": "008acd84",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acd88`](#insn-008acd88)

~~~json
{
  "source": "008acd88",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd8c`](#insn-008acd8c)

~~~json
{
  "source": "008acd8c",
  "target": "008acd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd90`](#insn-008acd90)

~~~json
{
  "source": "008acd90",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acd94`](#insn-008acd94)

~~~json
{
  "source": "008acd94",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acda4`](#insn-008acda4)

~~~json
{
  "source": "008acda4",
  "target": "0055220c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdac`](#insn-008acdac)

~~~json
{
  "source": "008acdac",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdbc`](#insn-008acdbc)

~~~json
{
  "source": "008acdbc",
  "target": "00c84740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c84740",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acdbc`](#insn-008acdbc)

~~~json
{
  "source": "008acdbc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdc0`](#insn-008acdc0)

~~~json
{
  "source": "008acdc0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdc4`](#insn-008acdc4)

~~~json
{
  "source": "008acdc4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdcc`](#insn-008acdcc)

~~~json
{
  "source": "008acdcc",
  "target": "005517c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdd0`](#insn-008acdd0)

~~~json
{
  "source": "008acdd0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdd8`](#insn-008acdd8)

~~~json
{
  "source": "008acdd8",
  "target": "008acde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acddc`](#insn-008acddc)

~~~json
{
  "source": "008acddc",
  "target": "008acdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acde4`](#insn-008acde4)

~~~json
{
  "source": "008acde4",
  "target": "008acdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdf0`](#insn-008acdf0)

~~~json
{
  "source": "008acdf0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acdf4`](#insn-008acdf4)

~~~json
{
  "source": "008acdf4",
  "target": "00c84760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c84760",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acdf4`](#insn-008acdf4)

~~~json
{
  "source": "008acdf4",
  "target": "00c84768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c84768",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008acdf8`](#insn-008acdf8)

~~~json
{
  "source": "008acdf8",
  "target": "008ad958",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdf8`](#insn-008acdf8)

~~~json
{
  "source": "008acdf8",
  "target": "008ad95c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acdfc`](#insn-008acdfc)

~~~json
{
  "source": "008acdfc",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace00`](#insn-008ace00)

~~~json
{
  "source": "008ace00",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace04`](#insn-008ace04)

~~~json
{
  "source": "008ace04",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace1c`](#insn-008ace1c)

~~~json
{
  "source": "008ace1c",
  "target": "00ca5d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ace20`](#insn-008ace20)

~~~json
{
  "source": "008ace20",
  "target": "0046cdb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace28`](#insn-008ace28)

~~~json
{
  "source": "008ace28",
  "target": "008ace48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace2c`](#insn-008ace2c)

~~~json
{
  "source": "008ace2c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace30`](#insn-008ace30)

~~~json
{
  "source": "008ace30",
  "target": "0085bd5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace34`](#insn-008ace34)

~~~json
{
  "source": "008ace34",
  "target": "008ace48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ace3c`](#insn-008ace3c)

~~~json
{
  "source": "008ace3c",
  "target": "00ca5d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ace40`](#insn-008ace40)

~~~json
{
  "source": "008ace40",
  "target": "0046ce6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace48`](#insn-008ace48)

~~~json
{
  "source": "008ace48",
  "target": "0055aa24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace4c`](#insn-008ace4c)

~~~json
{
  "source": "008ace4c",
  "target": "00ca5d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d48",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ace54`](#insn-008ace54)

~~~json
{
  "source": "008ace54",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace60`](#insn-008ace60)

~~~json
{
  "source": "008ace60",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c36a0094780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ace64`](#insn-008ace64)

~~~json
{
  "source": "008ace64",
  "target": "0055aa14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace68`](#insn-008ace68)

~~~json
{
  "source": "008ace68",
  "target": "00ca5d4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d4c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ace70`](#insn-008ace70)

~~~json
{
  "source": "008ace70",
  "target": "0055aa24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace74`](#insn-008ace74)

~~~json
{
  "source": "008ace74",
  "target": "00ca5d48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d48",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008ace7c`](#insn-008ace7c)

~~~json
{
  "source": "008ace7c",
  "target": "0055aa14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ace84`](#insn-008ace84)

~~~json
{
  "source": "008ace84",
  "target": "00ca5d4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5d4c",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008aceb8`](#insn-008aceb8)

~~~json
{
  "source": "008aceb8",
  "target": "005515d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acebc`](#insn-008acebc)

~~~json
{
  "source": "008acebc",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acec0`](#insn-008acec0)

~~~json
{
  "source": "008acec0",
  "target": "008acee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acec4`](#insn-008acec4)

~~~json
{
  "source": "008acec4",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acec8`](#insn-008acec8)

~~~json
{
  "source": "008acec8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acecc`](#insn-008acecc)

~~~json
{
  "source": "008acecc",
  "target": "008acee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008aced8`](#insn-008aced8)

~~~json
{
  "source": "008aced8",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acedc`](#insn-008acedc)

~~~json
{
  "source": "008acedc",
  "target": "008acee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acee4`](#insn-008acee4)

~~~json
{
  "source": "008acee4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acef4`](#insn-008acef4)

~~~json
{
  "source": "008acef4",
  "target": "0055ca30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acefc`](#insn-008acefc)

~~~json
{
  "source": "008acefc",
  "target": "008acf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf08`](#insn-008acf08)

~~~json
{
  "source": "008acf08",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf0c`](#insn-008acf0c)

~~~json
{
  "source": "008acf0c",
  "target": "008ad0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf10`](#insn-008acf10)

~~~json
{
  "source": "008acf10",
  "target": "008ad10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf14`](#insn-008acf14)

~~~json
{
  "source": "008acf14",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf28`](#insn-008acf28)

~~~json
{
  "source": "008acf28",
  "target": "008ad384",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf30`](#insn-008acf30)

~~~json
{
  "source": "008acf30",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf34`](#insn-008acf34)

~~~json
{
  "source": "008acf34",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf3c`](#insn-008acf3c)

~~~json
{
  "source": "008acf3c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf48`](#insn-008acf48)

~~~json
{
  "source": "008acf48",
  "target": "00691c08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf4c`](#insn-008acf4c)

~~~json
{
  "source": "008acf4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf58`](#insn-008acf58)

~~~json
{
  "source": "008acf58",
  "target": "005c1b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf5c`](#insn-008acf5c)

~~~json
{
  "source": "008acf5c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf64`](#insn-008acf64)

~~~json
{
  "source": "008acf64",
  "target": "005c1b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acf68`](#insn-008acf68)

~~~json
{
  "source": "008acf68",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf74`](#insn-008acf74)

~~~json
{
  "source": "008acf74",
  "target": "002a7fd9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7fd9",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "736372617463685f534e535f2530336400",
  "capture_start": "002a7fd9",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008acf7c`](#insn-008acf7c)

~~~json
{
  "source": "008acf7c",
  "target": "Stack[-0x10f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf80`](#insn-008acf80)

~~~json
{
  "source": "008acf80",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf84`](#insn-008acf84)

~~~json
{
  "source": "008acf84",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf88`](#insn-008acf88)

~~~json
{
  "source": "008acf88",
  "target": "Stack[-0x11f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acf8c`](#insn-008acf8c)

~~~json
{
  "source": "008acf8c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acfa0`](#insn-008acfa0)

~~~json
{
  "source": "008acfa0",
  "target": "00448254",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acfac`](#insn-008acfac)

~~~json
{
  "source": "008acfac",
  "target": "0048d1b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acfb0`](#insn-008acfb0)

~~~json
{
  "source": "008acfb0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfb4`](#insn-008acfb4)

~~~json
{
  "source": "008acfb4",
  "target": "008acfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfb8`](#insn-008acfb8)

~~~json
{
  "source": "008acfb8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfbc`](#insn-008acfbc)

~~~json
{
  "source": "008acfbc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acfc0`](#insn-008acfc0)

~~~json
{
  "source": "008acfc0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfc4`](#insn-008acfc4)

~~~json
{
  "source": "008acfc4",
  "target": "008acfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfc8`](#insn-008acfc8)

~~~json
{
  "source": "008acfc8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfcc`](#insn-008acfcc)

~~~json
{
  "source": "008acfcc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008acfd8`](#insn-008acfd8)

~~~json
{
  "source": "008acfd8",
  "target": "Stack[-0x9b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfe0`](#insn-008acfe0)

~~~json
{
  "source": "008acfe0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfe8`](#insn-008acfe8)

~~~json
{
  "source": "008acfe8",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acfec`](#insn-008acfec)

~~~json
{
  "source": "008acfec",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008acff0`](#insn-008acff0)

~~~json
{
  "source": "008acff0",
  "target": "Stack[-0x11e]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad004`](#insn-008ad004)

~~~json
{
  "source": "008ad004",
  "target": "00442e98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad010`](#insn-008ad010)

~~~json
{
  "source": "008ad010",
  "target": "00c594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad014`](#insn-008ad014)

~~~json
{
  "source": "008ad014",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad018`](#insn-008ad018)

~~~json
{
  "source": "008ad018",
  "target": "008ad024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad01c`](#insn-008ad01c)

~~~json
{
  "source": "008ad01c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad020`](#insn-008ad020)

~~~json
{
  "source": "008ad020",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad024`](#insn-008ad024)

~~~json
{
  "source": "008ad024",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad028`](#insn-008ad028)

~~~json
{
  "source": "008ad028",
  "target": "008ad034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad02c`](#insn-008ad02c)

~~~json
{
  "source": "008ad02c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad030`](#insn-008ad030)

~~~json
{
  "source": "008ad030",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad034`](#insn-008ad034)

~~~json
{
  "source": "008ad034",
  "target": "0055aa24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad040`](#insn-008ad040)

~~~json
{
  "source": "008ad040",
  "target": "0055aa14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad058`](#insn-008ad058)

~~~json
{
  "source": "008ad058",
  "target": "00448254",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad064`](#insn-008ad064)

~~~json
{
  "source": "008ad064",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad090`](#insn-008ad090)

~~~json
{
  "source": "008ad090",
  "target": "005979b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad094`](#insn-008ad094)

~~~json
{
  "source": "008ad094",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad09c`](#insn-008ad09c)

~~~json
{
  "source": "008ad09c",
  "target": "008ad0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0a0`](#insn-008ad0a0)

~~~json
{
  "source": "008ad0a0",
  "target": "008ad0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0a8`](#insn-008ad0a8)

~~~json
{
  "source": "008ad0a8",
  "target": "008ad0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0c0`](#insn-008ad0c0)

~~~json
{
  "source": "008ad0c0",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad0c4`](#insn-008ad0c4)

~~~json
{
  "source": "008ad0c4",
  "target": "008acf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0c8`](#insn-008ad0c8)

~~~json
{
  "source": "008ad0c8",
  "target": "008ad10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0d4`](#insn-008ad0d4)

~~~json
{
  "source": "008ad0d4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0e0`](#insn-008ad0e0)

~~~json
{
  "source": "008ad0e0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0e4`](#insn-008ad0e4)

~~~json
{
  "source": "008ad0e4",
  "target": "008ad0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0e8`](#insn-008ad0e8)

~~~json
{
  "source": "008ad0e8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0ec`](#insn-008ad0ec)

~~~json
{
  "source": "008ad0ec",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad0f0`](#insn-008ad0f0)

~~~json
{
  "source": "008ad0f0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0f4`](#insn-008ad0f4)

~~~json
{
  "source": "008ad0f4",
  "target": "008ad100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0f8`](#insn-008ad0f8)

~~~json
{
  "source": "008ad0f8",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad0fc`](#insn-008ad0fc)

~~~json
{
  "source": "008ad0fc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad100`](#insn-008ad100)

~~~json
{
  "source": "008ad100",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad108`](#insn-008ad108)

~~~json
{
  "source": "008ad108",
  "target": "005c1b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad10c`](#insn-008ad10c)

~~~json
{
  "source": "008ad10c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad110`](#insn-008ad110)

~~~json
{
  "source": "008ad110",
  "target": "008ad13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad11c`](#insn-008ad11c)

~~~json
{
  "source": "008ad11c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad120`](#insn-008ad120)

~~~json
{
  "source": "008ad120",
  "target": "008ad13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad138`](#insn-008ad138)

~~~json
{
  "source": "008ad138",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad13c`](#insn-008ad13c)

~~~json
{
  "source": "008ad13c",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad140`](#insn-008ad140)

~~~json
{
  "source": "008ad140",
  "target": "008ad154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad14c`](#insn-008ad14c)

~~~json
{
  "source": "008ad14c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad150`](#insn-008ad150)

~~~json
{
  "source": "008ad150",
  "target": "008ad198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad154`](#insn-008ad154)

~~~json
{
  "source": "008ad154",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad158`](#insn-008ad158)

~~~json
{
  "source": "008ad158",
  "target": "008ad164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad15c`](#insn-008ad15c)

~~~json
{
  "source": "008ad15c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad160`](#insn-008ad160)

~~~json
{
  "source": "008ad160",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad164`](#insn-008ad164)

~~~json
{
  "source": "008ad164",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad16c`](#insn-008ad16c)

~~~json
{
  "source": "008ad16c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad174`](#insn-008ad174)

~~~json
{
  "source": "008ad174",
  "target": "008ad358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad178`](#insn-008ad178)

~~~json
{
  "source": "008ad178",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad17c`](#insn-008ad17c)

~~~json
{
  "source": "008ad17c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad180`](#insn-008ad180)

~~~json
{
  "source": "008ad180",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad184`](#insn-008ad184)

~~~json
{
  "source": "008ad184",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad188`](#insn-008ad188)

~~~json
{
  "source": "008ad188",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad18c`](#insn-008ad18c)

~~~json
{
  "source": "008ad18c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad1ac`](#insn-008ad1ac)

~~~json
{
  "source": "008ad1ac",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ad1b0`](#insn-008ad1b0)

~~~json
{
  "source": "008ad1b0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad1b4`](#insn-008ad1b4)

~~~json
{
  "source": "008ad1b4",
  "target": "008ad15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad1b8`](#insn-008ad1b8)

~~~json
{
  "source": "008ad1b8",
  "target": "008ad164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ad358`](#insn-008ad358)

~~~json
{
  "source": "008ad358",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
