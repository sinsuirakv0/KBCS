# 00abefd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00abf09c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf09c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-d90f6fb4e6db5ba339c8b687582d8af6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abefd4",
  "name": "FUN_00abefd4",
  "size": 988,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac9d88c0f319ba5af21072815c37c6b19726e8770d752d9550ceddebd5602c4d",
  "source_text_sha256": "ac9d88c0f319ba5af21072815c37c6b19726e8770d752d9550ceddebd5602c4d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abefd4",
        "00abf3ab"
      ],
      [
        "00abf460",
        "00abf463"
      ]
    ],
    "bytes_sha256": "edc6e0603f80abda31264afa8cc11c7827f104d916f6b32d01e6f9821e29fc68",
    "instruction_count": 247,
    "instruction_bytes": 988,
    "body_bytes": 988,
    "indirect": 10,
    "unresolved": 9
  }
}
~~~

## 呼び出し元

- [00596128](../00596/00596128.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041cc4c](../0041c/0041cc4c.md)
- [0053d984](../0053d/0053d984.md)
- [00574fe4](../00574/00574fe4.md)
- [0084dd1c](../0084d/0084dd1c.md)
- [009a2998](../009a2/009a2998.md)
- [009b79e8](../009b7/009b79e8.md)
- [009bd6b8](../009bd/009bd6b8.md)
- [00aca844](../00aca/00aca844.md)
- [00aca848](../00aca/00aca848.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"agreement_accepted"
"birthday_state"
"gdpr_adid"
"gdpr_privacy"
"limitAdTracking"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9318 bytes

~~~c

uint FUN_00abefd4(long param_1)

{
  int iVar1;
  long lVar2;
  long *plVar3;
  byte bVar4;
  uint uVar5;
  undefined4 uVar6;
  long lVar7;
  byte *pbVar8;
  undefined8 local_b0;
  long *plStack_a8;
  undefined8 local_a0;
  long *plStack_98;
  long *local_90;
  long *local_88;
  byte local_80;
  char cStack_7f;
  undefined5 uStack_7e;
  char cStack_79;
  char cStack_78;
  char cStack_77;
  char cStack_76;
  undefined2 uStack_75;
  char cStack_73;
  char cStack_72;
  char cStack_71;
  char cStack_70;
  undefined2 uStack_6f;
  undefined1 uStack_6d;
  undefined4 uStack_6c;
  byte *local_60;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  uVar5 = FUN_009b79e8();
                    /* try { // try from 00abf004 to 00bbf03f has its CatchHandler @ 00ac4f60 */
  if ((uVar5 & 1) == 0) goto LAB_00abf2b4;
  FUN_009bd6b8(param_1);
  local_80 = 0;
  cStack_7f = 0;
  thunk_FUN_0056bde8(&local_90,&local_80);
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
                    /* try { // try from 00abf044 to 00bbf05b has its CatchHandler @ 00ac525c */
  local_80 = 0x24;
  uStack_6f = 0x6465;
  cStack_77 = (char)s_agreement_accepted_0029fa64._8_8_;
  cStack_76 = SUB81(s_agreement_accepted_0029fa64._8_8_,1);
  uStack_75 = SUB82(s_agreement_accepted_0029fa64._8_8_,2);
  cStack_73 = SUB81(s_agreement_accepted_0029fa64._8_8_,4);
  cStack_72 = SUB81(s_agreement_accepted_0029fa64._8_8_,5);
  cStack_71 = SUB81(s_agreement_accepted_0029fa64._8_8_,6);
  cStack_70 = SUB81(s_agreement_accepted_0029fa64._8_8_,7);
  cStack_7f = (char)s_agreement_accepted_0029fa64._0_8_;
  uStack_7e = SUB85(s_agreement_accepted_0029fa64._0_8_,1);
  cStack_79 = SUB81(s_agreement_accepted_0029fa64._0_8_,6);
  cStack_78 = SUB81(s_agreement_accepted_0029fa64._0_8_,7);
  uStack_6d = 0;
                    /* try { // try from 00abf064 to 00bbf08f has its CatchHandler @ 00ac4f4c */
  bVar4 = (**(code **)(*local_90 + 8))(local_90,&local_80);
  *(byte *)(param_1 + 0x47441a) = bVar4 & 1;
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
                    /* try { // try from 00abf094 to 00bbf0af has its CatchHandler @ 00ac525c */
  local_80 = 0x1c;
  cStack_7f = (char)s_birthday_state_0029d837._0_6_;
  uStack_7e = SUB65(s_birthday_state_0029d837._0_6_,1);
  cStack_79 = (char)s_birthday_state_0029d837._6_2_;
  cStack_78 = SUB21(s_birthday_state_0029d837._6_2_,1);
  cStack_77 = (char)s_birthday_state_0029d837._8_6_;
  cStack_76 = SUB61(s_birthday_state_0029d837._8_6_,1);
  uStack_75 = SUB62(s_birthday_state_0029d837._8_6_,2);
  cStack_73 = SUB61(s_birthday_state_0029d837._8_6_,4);
  cStack_72 = SUB61(s_birthday_state_0029d837._8_6_,5);
  cStack_71 = 0;
                    /* try { // try from 00abf0bc to 00bbf0f3 has its CatchHandler @ 00ac4f58 */
  uVar6 = (**(code **)(*local_90 + 0x20))(local_90,&local_80);
  *(undefined4 *)(param_1 + 0x1cf0) = uVar6;
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
  local_80 = 0x1e;
  cStack_7f = (char)s_limitAdTracking_002a1a50._0_7_;
  uStack_7e = SUB75(s_limitAdTracking_002a1a50._0_7_,1);
  cStack_79 = SUB71(s_limitAdTracking_002a1a50._0_7_,6);
  cStack_78 = s_limitAdTracking_002a1a50[7];
  cStack_77 = (char)s_limitAdTracking_002a1a50._8_7_;
  cStack_76 = SUB71(s_limitAdTracking_002a1a50._8_7_,1);
  uStack_75 = SUB72(s_limitAdTracking_002a1a50._8_7_,2);
  cStack_73 = SUB71(s_limitAdTracking_002a1a50._8_7_,4);
  cStack_72 = SUB71(s_limitAdTracking_002a1a50._8_7_,5);
  cStack_71 = SUB71(s_limitAdTracking_002a1a50._8_7_,6);
                    /* try { // try from 00abf0f8 to 00bbf117 has its CatchHandler @ 00ac4ee4 */
  cStack_70 = 0;
  uVar6 = (**(code **)(*local_90 + 0x20))(local_90,&local_80);
  *(undefined4 *)(param_1 + 0x1cf8) = uVar6;
  if ((local_80 & 1) != 0) {
                    /* try { // try from 00abf11c to 00bbf123 has its CatchHandler @ 00ac4d44 */
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
                    /* try { // try from 00abf128 to 00bbf147 has its CatchHandler @ 00ac4edc */
  local_80 = 0x12;
  cStack_77 = 100;
  cStack_76 = 0;
  cStack_7f = (char)s_gdpr_adid_002ace48._0_8_;
  uStack_7e = SUB85(s_gdpr_adid_002ace48._0_8_,1);
  cStack_79 = SUB81(s_gdpr_adid_002ace48._0_8_,6);
  cStack_78 = SUB81(s_gdpr_adid_002ace48._0_8_,7);
                    /* try { // try from 00abf14c to 00bbf153 has its CatchHandler @ 00ac4d3c */
  uVar6 = (**(code **)(*local_90 + 0x20))(local_90,&local_80);
                    /* try { // try from 00abf158 to 00bbf183 has its CatchHandler @ 00ac4f44 */
  *(undefined4 *)(param_1 + 0x1cfc) = uVar6;
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
  local_80 = 0x10;
  cStack_77 = 0;
                    /* try { // try from 00abf188 to 00bbf1b3 has its CatchHandler @ 00ac4f3c */
  cStack_7f = 0x67;
  uStack_7e = 0x695f727064;
  cStack_79 = 0x69;
  cStack_78 = 100;
  uVar6 = (**(code **)(*local_90 + 0x20))(local_90,&local_80);
  *(undefined4 *)(param_1 + 0x1d00) = uVar6;
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
                    /* try { // try from 00abf1b8 to 00bbf1bf has its CatchHandler @ 00ac525c */
                    /* try { // try from 00abf1c8 to 00bbf1e7 has its CatchHandler @ 00ac4ed4 */
  local_80 = 0x18;
  cStack_77 = 0x76;
  cStack_76 = 0x61;
  uStack_75 = 0x7963;
  cStack_7f = (char)s_gdpr_privacy_002a5bfb._0_8_;
  uStack_7e = SUB85(s_gdpr_privacy_002a5bfb._0_8_,1);
  cStack_79 = SUB81(s_gdpr_privacy_002a5bfb._0_8_,6);
  cStack_78 = SUB81(s_gdpr_privacy_002a5bfb._0_8_,7);
  cStack_73 = 0;
  uVar6 = (**(code **)(*local_90 + 0x20))(local_90,&local_80);
                    /* try { // try from 00abf1fc to 00bbf203 has its CatchHandler @ 00ac51f4 */
  *(undefined4 *)(param_1 + 0x1d04) = uVar6;
  if ((local_80 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
  }
  if (*(int *)(BYTE_ARRAY_00334359 + param_1 + 7) < 9) {
    iVar1 = *(int *)(BYTE_ARRAY_003343dd + param_1 + 0x13);
    *(int *)((long)&fde_0038fb88 + param_1) = iVar1;
                    /* try { // try from 00abf224 to 00bbf22b has its CatchHandler @ 00ac51ec */
  }
  else {
    iVar1 = *(int *)((long)&fde_0038fb88 + param_1);
  }
  if (iVar1 == 0) {
    FUN_009a2998(param_1);
  }
                    /* try { // try from 00abf24c to 00bbf253 has its CatchHandler @ 00ac51e4 */
  if (*(int *)(BYTE_ARRAY_0039a215 + param_1 + 0xf) != 0x24cae) {
    if ((*(byte *)(param_1 + 0x10d9) & 1) == 0) {
                    /* try { // try from 00abf2e0 to 00bbf31b has its CatchHandler @ 00ac525c */
      FUN_0053d984(&local_b0);
      plStack_98 = plStack_a8;
      local_a0 = local_b0;
      local_b0 = 0;
      plStack_a8 = (long *)0x0;
      local_80 = 200;
      cStack_7f = -0xb;
      uStack_7e = 0xc0;
      cStack_79 = '\0';
      local_60 = &local_80;
      FUN_0084dd1c((long)&QWORD_00397060 + param_1,&local_a0,&local_80);
                    /* try { // try from 00abf324 to 00bbf40f has its CatchHandler @ 00ac519c */
      if (local_60 == &local_80) {
        lVar7 = 0x20;
        pbVar8 = &local_80;
LAB_00abf33c:
        (**(code **)(*(long *)pbVar8 + lVar7))();
      }
      else if (local_60 != (byte *)0x0) {
        lVar7 = 0x28;
        pbVar8 = local_60;
        goto LAB_00abf33c;
      }
      plVar3 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,plStack_98 + 1), lVar7 == 0)) {
        (**(code **)(*plVar3 + 0x10))(plVar3);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
      }
      plVar3 = plStack_a8;
      if ((plStack_a8 != (long *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,plStack_a8 + 1), lVar7 == 0)) {
        (**(code **)(*plVar3 + 0x10))(plVar3);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
      }
    }
    pbVar8 = BYTE_ARRAY_0039a215 + param_1 + 0xf;
    pbVar8[0] = 0xae;
    pbVar8[1] = 0x4c;
    pbVar8[2] = 2;
    pbVar8[3] = 0;
                    /* try { // try from 00abf274 to 00bbf27b has its CatchHandler @ 00ac51dc */
    *(undefined8 *)(param_1 + 0xc3a0) = 0;
    pbVar8 = BYTE_ARRAY_003b0f89 + param_1 + 0xf;
    pbVar8[0] = 0;
    pbVar8[1] = 0;
    pbVar8[2] = 0;
    pbVar8[3] = 0;
    pbVar8[4] = 0;
    pbVar8[5] = 0;
    pbVar8[6] = 0;
    pbVar8[7] = 0;
    FUN_0041be0c();
    FUN_0041cc4c();
  }
  if ((local_88 != (long *)0x0) &&
     (lVar7 = FUN_00bd6d90(0xffffffffffffffff,local_88 + 1), lVar7 == 0)) {
                    /* try { // try from 00abf2a0 to 00bbf2a7 has its CatchHandler @ 00ac51d4 */
    (**(code **)(*local_88 + 0x10))(local_88);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_88);
  }
LAB_00abf2b4:
  if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* try { // try from 00abf2c8 to 00bbf2cf has its CatchHandler @ 00ac51cc */
    return uVar5 & 1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abefd4"></a> `00abefd4` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abefd8"></a> `00abefd8` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abefdc"></a> `00abefdc` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abefe0"></a> `00abefe0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abefe4"></a> `00abefe4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abefe8"></a> `00abefe8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abefec"></a> `00abefec` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abeff0"></a> `00abeff0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abeff4"></a> `00abeff4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abeff8"></a> `00abeff8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abeffc"></a> `00abeffc` | `7b e2 fb 97` | bl 0x009b79e8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf000"></a> `00abf000` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00abf004"></a> `00abf004` | `80 15 00 36` | tbz w0,#0x0,0x00abf2b4 | `CONDITIONAL_JUMP`
<a id="insn-00abf008"></a> `00abf008` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf00c"></a> `00abf00c` | `ab f9 fb 97` | bl 0x009bd6b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf010"></a> `00abf010` | `ff 63 00 79` | strh wzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf014"></a> `00abf014` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abf018"></a> `00abf018` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf01c"></a> `00abf01c` | `f2 d7 ea 97` | bl 0x00574fe4 | `UNCONDITIONAL_CALL`
<a id="insn-00abf020"></a> `00abf020` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf024"></a> `00abf024` | `68 00 00 36` | tbz w8,#0x0,0x00abf030 | `CONDITIONAL_JUMP`
<a id="insn-00abf028"></a> `00abf028` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf02c"></a> `00abf02c` | `cd 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf030"></a> `00abf030` | `09 bf ff 90` | adrp x9,0x29f000 | `FALL_THROUGH`
<a id="insn-00abf034"></a> `00abf034` | `29 91 29 91` | add x9,x9,#0xa64 | `FALL_THROUGH`
<a id="insn-00abf038"></a> `00abf038` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00abf03c"></a> `00abf03c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abf040"></a> `00abf040` | `a9 8c 8c 52` | mov w9,#0x6465 | `FALL_THROUGH`
<a id="insn-00abf044"></a> `00abf044` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf048"></a> `00abf048` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf04c"></a> `00abf04c` | `e9 13 04 78` | sturh w9,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00abf050"></a> `00abf050` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf054"></a> `00abf054` | `ff 0f 01 39` | strb wzr,[sp, #0x43] | `FALL_THROUGH`
<a id="insn-00abf058"></a> `00abf058` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf05c"></a> `00abf05c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abf060"></a> `00abf060` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf064"></a> `00abf064` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf068"></a> `00abf068` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf06c"></a> `00abf06c` | `49 83 88 52` | mov w9,#0x441a | `FALL_THROUGH`
<a id="insn-00abf070"></a> `00abf070` | `0a 00 00 12` | and w10,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abf074"></a> `00abf074` | `e9 08 a0 72` | movk w9,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf078"></a> `00abf078` | `8a 6a 29 38` | strb w10,[x20, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00abf07c"></a> `00abf07c` | `68 00 00 36` | tbz w8,#0x0,0x00abf088 | `CONDITIONAL_JUMP`
<a id="insn-00abf080"></a> `00abf080` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf084"></a> `00abf084` | `b7 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf088"></a> `00abf088` | `e9 be ff d0` | adrp x9,0x29d000 | `FALL_THROUGH`
<a id="insn-00abf08c"></a> `00abf08c` | `29 dd 20 91` | add x9,x9,#0x837 | `FALL_THROUGH`
<a id="insn-00abf090"></a> `00abf090` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-00abf094"></a> `00abf094` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abf098"></a> `00abf098` | `29 61 40 f8` | ldur x9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00abf09c"></a> `00abf09c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0a0"></a> `00abf0a0` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0a4"></a> `00abf0a4` | `ea 13 03 f8` | stur x10,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf0a8"></a> `00abf0a8` | `e9 73 03 f8` | stur x9,[sp, #0x37] | `FALL_THROUGH`
<a id="insn-00abf0ac"></a> `00abf0ac` | `ff ff 00 39` | strb wzr,[sp, #0x3f] | `FALL_THROUGH`
<a id="insn-00abf0b0"></a> `00abf0b0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf0b4"></a> `00abf0b4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0b8"></a> `00abf0b8` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf0bc"></a> `00abf0bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf0c0"></a> `00abf0c0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0c4"></a> `00abf0c4` | `80 f2 1c b9` | str w0,[x20, #0x1cf0] | `FALL_THROUGH`
<a id="insn-00abf0c8"></a> `00abf0c8` | `68 00 00 36` | tbz w8,#0x0,0x00abf0d4 | `CONDITIONAL_JUMP`
<a id="insn-00abf0cc"></a> `00abf0cc` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf0d0"></a> `00abf0d0` | `a4 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0d4"></a> `00abf0d4` | `09 bf ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abf0d8"></a> `00abf0d8` | `29 41 29 91` | add x9,x9,#0xa50 | `FALL_THROUGH`
<a id="insn-00abf0dc"></a> `00abf0dc` | `c8 03 80 52` | mov w8,#0x1e | `FALL_THROUGH`
<a id="insn-00abf0e0"></a> `00abf0e0` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abf0e4"></a> `00abf0e4` | `29 71 40 f8` | ldur x9,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00abf0e8"></a> `00abf0e8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0ec"></a> `00abf0ec` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0f0"></a> `00abf0f0` | `ea 13 03 f8` | stur x10,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf0f4"></a> `00abf0f4` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00abf0f8"></a> `00abf0f8` | `ff 03 01 39` | strb wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf0fc"></a> `00abf0fc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf100"></a> `00abf100` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abf104"></a> `00abf104` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf108"></a> `00abf108` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf10c"></a> `00abf10c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf110"></a> `00abf110` | `80 fa 1c b9` | str w0,[x20, #0x1cf8] | `FALL_THROUGH`
<a id="insn-00abf114"></a> `00abf114` | `68 00 00 36` | tbz w8,#0x0,0x00abf120 | `CONDITIONAL_JUMP`
<a id="insn-00abf118"></a> `00abf118` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf11c"></a> `00abf11c` | `91 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf120"></a> `00abf120` | `69 bf ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00abf124"></a> `00abf124` | `29 21 39 91` | add x9,x9,#0xe48 | `FALL_THROUGH`
<a id="insn-00abf128"></a> `00abf128` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00abf12c"></a> `00abf12c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abf130"></a> `00abf130` | `8a 0c 80 52` | mov w10,#0x64 | `FALL_THROUGH`
<a id="insn-00abf134"></a> `00abf134` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf138"></a> `00abf138` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf13c"></a> `00abf13c` | `ea 93 03 78` | sturh w10,[sp, #0x39] | `FALL_THROUGH`
<a id="insn-00abf140"></a> `00abf140` | `e9 13 03 f8` | stur x9,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf144"></a> `00abf144` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf148"></a> `00abf148` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abf14c"></a> `00abf14c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf150"></a> `00abf150` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf154"></a> `00abf154` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf158"></a> `00abf158` | `80 fe 1c b9` | str w0,[x20, #0x1cfc] | `FALL_THROUGH`
<a id="insn-00abf15c"></a> `00abf15c` | `68 00 00 36` | tbz w8,#0x0,0x00abf168 | `CONDITIONAL_JUMP`
<a id="insn-00abf160"></a> `00abf160` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf164"></a> `00abf164` | `7f 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf168"></a> `00abf168` | `e9 8c 8c d2` | mov x9,#0x6467 | `FALL_THROUGH`
<a id="insn-00abf16c"></a> `00abf16c` | `08 02 80 52` | mov w8,#0x10 | `FALL_THROUGH`
<a id="insn-00abf170"></a> `00abf170` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf174"></a> `00abf174` | `09 4e ae f2` | movk x9,#0x7270, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf178"></a> `00abf178` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf17c"></a> `00abf17c` | `e9 2b cd f2` | movk x9,#0x695f, LSL #32 | `FALL_THROUGH`
<a id="insn-00abf180"></a> `00abf180` | `ff e7 00 39` | strb wzr,[sp, #0x39] | `FALL_THROUGH`
<a id="insn-00abf184"></a> `00abf184` | `29 8d ec f2` | movk x9,#0x6469, LSL #48 | `FALL_THROUGH`
<a id="insn-00abf188"></a> `00abf188` | `e9 13 03 f8` | stur x9,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf18c"></a> `00abf18c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf190"></a> `00abf190` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abf194"></a> `00abf194` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf198"></a> `00abf198` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf19c"></a> `00abf19c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf1a0"></a> `00abf1a0` | `80 02 1d b9` | str w0,[x20, #0x1d00] | `FALL_THROUGH`
<a id="insn-00abf1a4"></a> `00abf1a4` | `68 00 00 36` | tbz w8,#0x0,0x00abf1b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf1a8"></a> `00abf1a8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf1ac"></a> `00abf1ac` | `6d 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf1b0"></a> `00abf1b0` | `29 bf ff d0` | adrp x9,0x2a5000 | `FALL_THROUGH`
<a id="insn-00abf1b4"></a> `00abf1b4` | `29 ed 2f 91` | add x9,x9,#0xbfb | `FALL_THROUGH`
<a id="insn-00abf1b8"></a> `00abf1b8` | `ca 2e 8c 52` | mov w10,#0x6176 | `FALL_THROUGH`
<a id="insn-00abf1bc"></a> `00abf1bc` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abf1c0"></a> `00abf1c0` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00abf1c4"></a> `00abf1c4` | `6a 2c af 72` | movk w10,#0x7963, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf1c8"></a> `00abf1c8` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf1cc"></a> `00abf1cc` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf1d0"></a> `00abf1d0` | `ea 93 03 b8` | stur w10,[sp, #0x39] | `FALL_THROUGH`
<a id="insn-00abf1d4"></a> `00abf1d4` | `e9 13 03 f8` | stur x9,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abf1d8"></a> `00abf1d8` | `ff f7 00 39` | strb wzr,[sp, #0x3d] | `FALL_THROUGH`
<a id="insn-00abf1dc"></a> `00abf1dc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abf1e0"></a> `00abf1e0` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abf1e4"></a> `00abf1e4` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf1e8"></a> `00abf1e8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf1ec"></a> `00abf1ec` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf1f0"></a> `00abf1f0` | `89 d2 4c 91` | add x9,x20,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00abf1f4"></a> `00abf1f4` | `15 71 9f 52` | mov w21,#0xfb88 | `FALL_THROUGH`
<a id="insn-00abf1f8"></a> `00abf1f8` | `15 07 a0 72` | movk w21,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf1fc"></a> `00abf1fc` | `37 81 0d 91` | add x23,x9,#0x360 | `FALL_THROUGH`
<a id="insn-00abf200"></a> `00abf200` | `80 06 1d b9` | str w0,[x20, #0x1d04] | `FALL_THROUGH`
<a id="insn-00abf204"></a> `00abf204` | `68 00 00 36` | tbz w8,#0x0,0x00abf210 | `CONDITIONAL_JUMP`
<a id="insn-00abf208"></a> `00abf208` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf20c"></a> `00abf20c` | `55 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abf210"></a> `00abf210` | `e8 02 40 b9` | ldr w8,[x23] | `FALL_THROUGH`
<a id="insn-00abf214"></a> `00abf214` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00abf218"></a> `00abf218` | `aa 00 00 54` | b.ge 0x00abf22c | `CONDITIONAL_JUMP`
<a id="insn-00abf21c"></a> `00abf21c` | `e8 92 40 b9` | ldr w8,[x23, #0x90] | `FALL_THROUGH`
<a id="insn-00abf220"></a> `00abf220` | `88 6a 35 b8` | str w8,[x20, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf224"></a> `00abf224` | `c8 00 00 35` | cbnz w8,0x00abf23c | `CONDITIONAL_JUMP`
<a id="insn-00abf228"></a> `00abf228` | `03 00 00 14` | b 0x00abf234 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf22c"></a> `00abf22c` | `88 6a 75 b8` | ldr w8,[x20, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf230"></a> `00abf230` | `68 00 00 35` | cbnz w8,0x00abf23c | `CONDITIONAL_JUMP`
<a id="insn-00abf234"></a> `00abf234` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf238"></a> `00abf238` | `d8 8d fb 97` | bl 0x009a2998 | `UNCONDITIONAL_CALL`
<a id="insn-00abf23c"></a> `00abf23c` | `97 44 94 52` | mov w23,#0xa224 | `FALL_THROUGH`
<a id="insn-00abf240"></a> `00abf240` | `d8 95 89 52` | mov w24,#0x4cae | `FALL_THROUGH`
<a id="insn-00abf244"></a> `00abf244` | `37 07 a0 72` | movk w23,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf248"></a> `00abf248` | `58 00 a0 72` | movk w24,#0x2, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf24c"></a> `00abf24c` | `88 6a 77 b8` | ldr w8,[x20, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf250"></a> `00abf250` | `1f 01 18 6b` | cmp w8,w24 | `FALL_THROUGH`
<a id="insn-00abf254"></a> `00abf254` | `80 01 00 54` | b.eq 0x00abf284 | `CONDITIONAL_JUMP`
<a id="insn-00abf258"></a> `00abf258` | `28 1b 82 52` | mov w8,#0x10d9 | `FALL_THROUGH`
<a id="insn-00abf25c"></a> `00abf25c` | `88 6a 68 38` | ldrb w8,[x20, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00abf260"></a> `00abf260` | `08 04 00 36` | tbz w8,#0x0,0x00abf2e0 | `CONDITIONAL_JUMP`
<a id="insn-00abf264"></a> `00abf264` | `09 f3 81 52` | mov w9,#0xf98 | `FALL_THROUGH`
<a id="insn-00abf268"></a> `00abf268` | `08 74 98 52` | mov w8,#0xc3a0 | `FALL_THROUGH`
<a id="insn-00abf26c"></a> `00abf26c` | `98 6a 37 b8` | str w24,[x20, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf270"></a> `00abf270` | `69 07 a0 72` | movk w9,#0x3b, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf274"></a> `00abf274` | `9f 6a 28 f8` | str xzr,[x20, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf278"></a> `00abf278` | `9f 6a 29 f8` | str xzr,[x20, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf27c"></a> `00abf27c` | `e4 72 e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00abf280"></a> `00abf280` | `73 76 e5 97` | bl 0x0041cc4c | `UNCONDITIONAL_CALL`
<a id="insn-00abf284"></a> `00abf284` | `f4 17 40 f9` | ldr x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abf288"></a> `00abf288` | `74 01 00 b4` | cbz x20,0x00abf2b4 | `CONDITIONAL_JUMP`
<a id="insn-00abf28c"></a> `00abf28c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abf290"></a> `00abf290` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abf294"></a> `00abf294` | `bf 5e 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00abf298"></a> `00abf298` | `e0 00 00 b5` | cbnz x0,0x00abf2b4 | `CONDITIONAL_JUMP`
<a id="insn-00abf29c"></a> `00abf29c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abf2a0"></a> `00abf2a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf2a4"></a> `00abf2a4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf2a8"></a> `00abf2a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf2ac"></a> `00abf2ac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf2b0"></a> `00abf2b0` | `20 6f 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf2b4"></a> `00abf2b4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abf2b8"></a> `00abf2b8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abf2bc"></a> `00abf2bc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf2c0"></a> `00abf2c0` | `01 0d 00 54` | b.ne 0x00abf460 | `CONDITIONAL_JUMP`
<a id="insn-00abf2c4"></a> `00abf2c4` | `60 02 00 12` | and w0,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00abf2c8"></a> `00abf2c8` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abf2cc"></a> `00abf2cc` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abf2d0"></a> `00abf2d0` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abf2d4"></a> `00abf2d4` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abf2d8"></a> `00abf2d8` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abf2dc"></a> `00abf2dc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abf2e0"></a> `00abf2e0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00abf2e4"></a> `00abf2e4` | `a8 f9 e9 97` | bl 0x0053d984 | `UNCONDITIONAL_CALL`
<a id="insn-00abf2e8"></a> `00abf2e8` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00abf2ec"></a> `00abf2ec` | `88 0a 00 90` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00abf2f0"></a> `00abf2f0` | `08 21 17 91` | add x8,x8,#0x5c8 | `FALL_THROUGH`
<a id="insn-00abf2f4"></a> `00abf2f4` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf2f8"></a> `00abf2f8` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00abf2fc"></a> `00abf2fc` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abf300"></a> `00abf300` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf304"></a> `00abf304` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abf308"></a> `00abf308` | `88 5e 4e 91` | add x8,x20,#0x397, LSL #12 | `FALL_THROUGH`
<a id="insn-00abf30c"></a> `00abf30c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abf310"></a> `00abf310` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf314"></a> `00abf314` | `00 81 01 91` | add x0,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00abf318"></a> `00abf318` | `81 3a f6 97` | bl 0x0084dd1c | `UNCONDITIONAL_CALL`
<a id="insn-00abf31c"></a> `00abf31c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abf320"></a> `00abf320` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00abf324"></a> `00abf324` | `80 00 00 54` | b.eq 0x00abf334 | `CONDITIONAL_JUMP`
<a id="insn-00abf328"></a> `00abf328` | `00 01 00 b4` | cbz x0,0x00abf348 | `CONDITIONAL_JUMP`
<a id="insn-00abf32c"></a> `00abf32c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00abf330"></a> `00abf330` | `03 00 00 14` | b 0x00abf33c | `UNCONDITIONAL_JUMP`
<a id="insn-00abf334"></a> `00abf334` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00abf338"></a> `00abf338` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00abf33c"></a> `00abf33c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00abf340"></a> `00abf340` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abf344"></a> `00abf344` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf348"></a> `00abf348` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abf34c"></a> `00abf34c` | `75 01 00 b4` | cbz x21,0x00abf378 | `CONDITIONAL_JUMP`
<a id="insn-00abf350"></a> `00abf350` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abf354"></a> `00abf354` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abf358"></a> `00abf358` | `8e 5e 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00abf35c"></a> `00abf35c` | `e0 00 00 b5` | cbnz x0,0x00abf378 | `CONDITIONAL_JUMP`
<a id="insn-00abf360"></a> `00abf360` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abf364"></a> `00abf364` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf368"></a> `00abf368` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf36c"></a> `00abf36c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf370"></a> `00abf370` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf374"></a> `00abf374` | `ef 6e 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf378"></a> `00abf378` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf37c"></a> `00abf37c` | `55 f7 ff b4` | cbz x21,0x00abf264 | `CONDITIONAL_JUMP`
<a id="insn-00abf380"></a> `00abf380` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abf384"></a> `00abf384` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abf388"></a> `00abf388` | `82 5e 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00abf38c"></a> `00abf38c` | `c0 f6 ff b5` | cbnz x0,0x00abf264 | `CONDITIONAL_JUMP`
<a id="insn-00abf390"></a> `00abf390` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abf394"></a> `00abf394` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf398"></a> `00abf398` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf39c"></a> `00abf39c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf3a0"></a> `00abf3a0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf3a4"></a> `00abf3a4` | `e3 6e 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf3a8"></a> `00abf3a8` | `af ff ff 17` | b 0x00abf264 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf460"></a> `00abf460` | `cc 6e 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abefd4`](#insn-00abefd4) 範囲 `[['00abefd4', '00abf003']]`
  - `FALL_THROUGH` [`00abf000`](#insn-00abf000) → [`00abf004`](#insn-00abf004)
- ブロック [`00abf004`](#insn-00abf004) 範囲 `[['00abf004', '00abf007']]`
  - `CONDITIONAL_JUMP` [`00abf004`](#insn-00abf004) → [`00abf2b4`](#insn-00abf2b4)
  - `FALL_THROUGH` [`00abf004`](#insn-00abf004) → [`00abf008`](#insn-00abf008)
- ブロック [`00abf008`](#insn-00abf008) 範囲 `[['00abf008', '00abf027']]`
  - `CONDITIONAL_JUMP` [`00abf024`](#insn-00abf024) → [`00abf030`](#insn-00abf030)
  - `FALL_THROUGH` [`00abf024`](#insn-00abf024) → [`00abf028`](#insn-00abf028)
- ブロック [`00abf028`](#insn-00abf028) 範囲 `[['00abf028', '00abf02f']]`
  - `FALL_THROUGH` [`00abf02c`](#insn-00abf02c) → [`00abf030`](#insn-00abf030)
- ブロック [`00abf030`](#insn-00abf030) 範囲 `[['00abf030', '00abf043']]`
  - `FALL_THROUGH` [`00abf040`](#insn-00abf040) → [`00abf044`](#insn-00abf044)
- ブロック [`00abf044`](#insn-00abf044) 範囲 `[['00abf044', '00abf063']]`
  - `FALL_THROUGH` [`00abf060`](#insn-00abf060) → [`00abf064`](#insn-00abf064)
- ブロック [`00abf064`](#insn-00abf064) 範囲 `[['00abf064', '00abf07f']]`
  - `CONDITIONAL_JUMP` [`00abf07c`](#insn-00abf07c) → [`00abf088`](#insn-00abf088)
  - `FALL_THROUGH` [`00abf07c`](#insn-00abf07c) → [`00abf080`](#insn-00abf080)
- ブロック [`00abf080`](#insn-00abf080) 範囲 `[['00abf080', '00abf087']]`
  - `FALL_THROUGH` [`00abf084`](#insn-00abf084) → [`00abf088`](#insn-00abf088)
- ブロック [`00abf088`](#insn-00abf088) 範囲 `[['00abf088', '00abf093']]`
  - `FALL_THROUGH` [`00abf090`](#insn-00abf090) → [`00abf094`](#insn-00abf094)
- ブロック [`00abf094`](#insn-00abf094) 範囲 `[['00abf094', '00abf0bb']]`
  - `FALL_THROUGH` [`00abf0b8`](#insn-00abf0b8) → [`00abf0bc`](#insn-00abf0bc)
- ブロック [`00abf0bc`](#insn-00abf0bc) 範囲 `[['00abf0bc', '00abf0cb']]`
  - `CONDITIONAL_JUMP` [`00abf0c8`](#insn-00abf0c8) → [`00abf0d4`](#insn-00abf0d4)
  - `FALL_THROUGH` [`00abf0c8`](#insn-00abf0c8) → [`00abf0cc`](#insn-00abf0cc)
- ブロック [`00abf0cc`](#insn-00abf0cc) 範囲 `[['00abf0cc', '00abf0d3']]`
  - `FALL_THROUGH` [`00abf0d0`](#insn-00abf0d0) → [`00abf0d4`](#insn-00abf0d4)
- ブロック [`00abf0d4`](#insn-00abf0d4) 範囲 `[['00abf0d4', '00abf0f7']]`
  - `FALL_THROUGH` [`00abf0f4`](#insn-00abf0f4) → [`00abf0f8`](#insn-00abf0f8)
- ブロック [`00abf0f8`](#insn-00abf0f8) 範囲 `[['00abf0f8', '00abf117']]`
  - `CONDITIONAL_JUMP` [`00abf114`](#insn-00abf114) → [`00abf120`](#insn-00abf120)
  - `FALL_THROUGH` [`00abf114`](#insn-00abf114) → [`00abf118`](#insn-00abf118)
- ブロック [`00abf118`](#insn-00abf118) 範囲 `[['00abf118', '00abf11b']]`
  - `FALL_THROUGH` [`00abf118`](#insn-00abf118) → [`00abf11c`](#insn-00abf11c)
- ブロック [`00abf11c`](#insn-00abf11c) 範囲 `[['00abf11c', '00abf11f']]`
  - `FALL_THROUGH` [`00abf11c`](#insn-00abf11c) → [`00abf120`](#insn-00abf120)
- ブロック [`00abf120`](#insn-00abf120) 範囲 `[['00abf120', '00abf127']]`
  - `FALL_THROUGH` [`00abf124`](#insn-00abf124) → [`00abf128`](#insn-00abf128)
- ブロック [`00abf128`](#insn-00abf128) 範囲 `[['00abf128', '00abf14b']]`
  - `FALL_THROUGH` [`00abf148`](#insn-00abf148) → [`00abf14c`](#insn-00abf14c)
- ブロック [`00abf14c`](#insn-00abf14c) 範囲 `[['00abf14c', '00abf157']]`
  - `FALL_THROUGH` [`00abf154`](#insn-00abf154) → [`00abf158`](#insn-00abf158)
- ブロック [`00abf158`](#insn-00abf158) 範囲 `[['00abf158', '00abf15f']]`
  - `CONDITIONAL_JUMP` [`00abf15c`](#insn-00abf15c) → [`00abf168`](#insn-00abf168)
  - `FALL_THROUGH` [`00abf15c`](#insn-00abf15c) → [`00abf160`](#insn-00abf160)
- ブロック [`00abf160`](#insn-00abf160) 範囲 `[['00abf160', '00abf167']]`
  - `FALL_THROUGH` [`00abf164`](#insn-00abf164) → [`00abf168`](#insn-00abf168)
- ブロック [`00abf168`](#insn-00abf168) 範囲 `[['00abf168', '00abf187']]`
  - `FALL_THROUGH` [`00abf184`](#insn-00abf184) → [`00abf188`](#insn-00abf188)
- ブロック [`00abf188`](#insn-00abf188) 範囲 `[['00abf188', '00abf1a7']]`
  - `CONDITIONAL_JUMP` [`00abf1a4`](#insn-00abf1a4) → [`00abf1b0`](#insn-00abf1b0)
  - `FALL_THROUGH` [`00abf1a4`](#insn-00abf1a4) → [`00abf1a8`](#insn-00abf1a8)
- ブロック [`00abf1a8`](#insn-00abf1a8) 範囲 `[['00abf1a8', '00abf1af']]`
  - `FALL_THROUGH` [`00abf1ac`](#insn-00abf1ac) → [`00abf1b0`](#insn-00abf1b0)
- ブロック [`00abf1b0`](#insn-00abf1b0) 範囲 `[['00abf1b0', '00abf1b7']]`
  - `FALL_THROUGH` [`00abf1b4`](#insn-00abf1b4) → [`00abf1b8`](#insn-00abf1b8)
- ブロック [`00abf1b8`](#insn-00abf1b8) 範囲 `[['00abf1b8', '00abf1c7']]`
  - `FALL_THROUGH` [`00abf1c4`](#insn-00abf1c4) → [`00abf1c8`](#insn-00abf1c8)
- ブロック [`00abf1c8`](#insn-00abf1c8) 範囲 `[['00abf1c8', '00abf1fb']]`
  - `FALL_THROUGH` [`00abf1f8`](#insn-00abf1f8) → [`00abf1fc`](#insn-00abf1fc)
- ブロック [`00abf1fc`](#insn-00abf1fc) 範囲 `[['00abf1fc', '00abf207']]`
  - `CONDITIONAL_JUMP` [`00abf204`](#insn-00abf204) → [`00abf210`](#insn-00abf210)
  - `FALL_THROUGH` [`00abf204`](#insn-00abf204) → [`00abf208`](#insn-00abf208)
- ブロック [`00abf208`](#insn-00abf208) 範囲 `[['00abf208', '00abf20f']]`
  - `FALL_THROUGH` [`00abf20c`](#insn-00abf20c) → [`00abf210`](#insn-00abf210)
- ブロック [`00abf210`](#insn-00abf210) 範囲 `[['00abf210', '00abf21b']]`
  - `CONDITIONAL_JUMP` [`00abf218`](#insn-00abf218) → [`00abf22c`](#insn-00abf22c)
  - `FALL_THROUGH` [`00abf218`](#insn-00abf218) → [`00abf21c`](#insn-00abf21c)
- ブロック [`00abf21c`](#insn-00abf21c) 範囲 `[['00abf21c', '00abf223']]`
  - `FALL_THROUGH` [`00abf220`](#insn-00abf220) → [`00abf224`](#insn-00abf224)
- ブロック [`00abf224`](#insn-00abf224) 範囲 `[['00abf224', '00abf227']]`
  - `CONDITIONAL_JUMP` [`00abf224`](#insn-00abf224) → [`00abf23c`](#insn-00abf23c)
  - `FALL_THROUGH` [`00abf224`](#insn-00abf224) → [`00abf228`](#insn-00abf228)
- ブロック [`00abf228`](#insn-00abf228) 範囲 `[['00abf228', '00abf22b']]`
  - `UNCONDITIONAL_JUMP` [`00abf228`](#insn-00abf228) → [`00abf234`](#insn-00abf234)
- ブロック [`00abf22c`](#insn-00abf22c) 範囲 `[['00abf22c', '00abf233']]`
  - `CONDITIONAL_JUMP` [`00abf230`](#insn-00abf230) → [`00abf23c`](#insn-00abf23c)
  - `FALL_THROUGH` [`00abf230`](#insn-00abf230) → [`00abf234`](#insn-00abf234)
- ブロック [`00abf234`](#insn-00abf234) 範囲 `[['00abf234', '00abf23b']]`
  - `FALL_THROUGH` [`00abf238`](#insn-00abf238) → [`00abf23c`](#insn-00abf23c)
- ブロック [`00abf23c`](#insn-00abf23c) 範囲 `[['00abf23c', '00abf24b']]`
  - `FALL_THROUGH` [`00abf248`](#insn-00abf248) → [`00abf24c`](#insn-00abf24c)
- ブロック [`00abf24c`](#insn-00abf24c) 範囲 `[['00abf24c', '00abf257']]`
  - `CONDITIONAL_JUMP` [`00abf254`](#insn-00abf254) → [`00abf284`](#insn-00abf284)
  - `FALL_THROUGH` [`00abf254`](#insn-00abf254) → [`00abf258`](#insn-00abf258)
- ブロック [`00abf258`](#insn-00abf258) 範囲 `[['00abf258', '00abf263']]`
  - `CONDITIONAL_JUMP` [`00abf260`](#insn-00abf260) → [`00abf2e0`](#insn-00abf2e0)
  - `FALL_THROUGH` [`00abf260`](#insn-00abf260) → [`00abf264`](#insn-00abf264)
- ブロック [`00abf264`](#insn-00abf264) 範囲 `[['00abf264', '00abf273']]`
  - `FALL_THROUGH` [`00abf270`](#insn-00abf270) → [`00abf274`](#insn-00abf274)
- ブロック [`00abf274`](#insn-00abf274) 範囲 `[['00abf274', '00abf283']]`
  - `FALL_THROUGH` [`00abf280`](#insn-00abf280) → [`00abf284`](#insn-00abf284)
- ブロック [`00abf284`](#insn-00abf284) 範囲 `[['00abf284', '00abf28b']]`
  - `CONDITIONAL_JUMP` [`00abf288`](#insn-00abf288) → [`00abf2b4`](#insn-00abf2b4)
  - `FALL_THROUGH` [`00abf288`](#insn-00abf288) → [`00abf28c`](#insn-00abf28c)
- ブロック [`00abf28c`](#insn-00abf28c) 範囲 `[['00abf28c', '00abf29b']]`
  - `CONDITIONAL_JUMP` [`00abf298`](#insn-00abf298) → [`00abf2b4`](#insn-00abf2b4)
  - `FALL_THROUGH` [`00abf298`](#insn-00abf298) → [`00abf29c`](#insn-00abf29c)
- ブロック [`00abf29c`](#insn-00abf29c) 範囲 `[['00abf29c', '00abf29f']]`
  - `FALL_THROUGH` [`00abf29c`](#insn-00abf29c) → [`00abf2a0`](#insn-00abf2a0)
- ブロック [`00abf2a0`](#insn-00abf2a0) 範囲 `[['00abf2a0', '00abf2b3']]`
  - `FALL_THROUGH` [`00abf2b0`](#insn-00abf2b0) → [`00abf2b4`](#insn-00abf2b4)
- ブロック [`00abf2b4`](#insn-00abf2b4) 範囲 `[['00abf2b4', '00abf2c3']]`
  - `CONDITIONAL_JUMP` [`00abf2c0`](#insn-00abf2c0) → [`00abf460`](#insn-00abf460)
  - `FALL_THROUGH` [`00abf2c0`](#insn-00abf2c0) → [`00abf2c4`](#insn-00abf2c4)
- ブロック [`00abf2c4`](#insn-00abf2c4) 範囲 `[['00abf2c4', '00abf2c7']]`
  - `FALL_THROUGH` [`00abf2c4`](#insn-00abf2c4) → [`00abf2c8`](#insn-00abf2c8)
- ブロック [`00abf2c8`](#insn-00abf2c8) 範囲 `[['00abf2c8', '00abf2df']]`
- ブロック [`00abf2e0`](#insn-00abf2e0) 範囲 `[['00abf2e0', '00abf323']]`
  - `FALL_THROUGH` [`00abf320`](#insn-00abf320) → [`00abf324`](#insn-00abf324)
- ブロック [`00abf324`](#insn-00abf324) 範囲 `[['00abf324', '00abf327']]`
  - `CONDITIONAL_JUMP` [`00abf324`](#insn-00abf324) → [`00abf334`](#insn-00abf334)
  - `FALL_THROUGH` [`00abf324`](#insn-00abf324) → [`00abf328`](#insn-00abf328)
- ブロック [`00abf328`](#insn-00abf328) 範囲 `[['00abf328', '00abf32b']]`
  - `CONDITIONAL_JUMP` [`00abf328`](#insn-00abf328) → [`00abf348`](#insn-00abf348)
  - `FALL_THROUGH` [`00abf328`](#insn-00abf328) → [`00abf32c`](#insn-00abf32c)
- ブロック [`00abf32c`](#insn-00abf32c) 範囲 `[['00abf32c', '00abf333']]`
  - `UNCONDITIONAL_JUMP` [`00abf330`](#insn-00abf330) → [`00abf33c`](#insn-00abf33c)
- ブロック [`00abf334`](#insn-00abf334) 範囲 `[['00abf334', '00abf33b']]`
  - `FALL_THROUGH` [`00abf338`](#insn-00abf338) → [`00abf33c`](#insn-00abf33c)
- ブロック [`00abf33c`](#insn-00abf33c) 範囲 `[['00abf33c', '00abf347']]`
  - `FALL_THROUGH` [`00abf344`](#insn-00abf344) → [`00abf348`](#insn-00abf348)
- ブロック [`00abf348`](#insn-00abf348) 範囲 `[['00abf348', '00abf34f']]`
  - `CONDITIONAL_JUMP` [`00abf34c`](#insn-00abf34c) → [`00abf378`](#insn-00abf378)
  - `FALL_THROUGH` [`00abf34c`](#insn-00abf34c) → [`00abf350`](#insn-00abf350)
- ブロック [`00abf350`](#insn-00abf350) 範囲 `[['00abf350', '00abf35f']]`
  - `CONDITIONAL_JUMP` [`00abf35c`](#insn-00abf35c) → [`00abf378`](#insn-00abf378)
  - `FALL_THROUGH` [`00abf35c`](#insn-00abf35c) → [`00abf360`](#insn-00abf360)
- ブロック [`00abf360`](#insn-00abf360) 範囲 `[['00abf360', '00abf377']]`
  - `FALL_THROUGH` [`00abf374`](#insn-00abf374) → [`00abf378`](#insn-00abf378)
- ブロック [`00abf378`](#insn-00abf378) 範囲 `[['00abf378', '00abf37f']]`
  - `CONDITIONAL_JUMP` [`00abf37c`](#insn-00abf37c) → [`00abf264`](#insn-00abf264)
  - `FALL_THROUGH` [`00abf37c`](#insn-00abf37c) → [`00abf380`](#insn-00abf380)
- ブロック [`00abf380`](#insn-00abf380) 範囲 `[['00abf380', '00abf38f']]`
  - `CONDITIONAL_JUMP` [`00abf38c`](#insn-00abf38c) → [`00abf264`](#insn-00abf264)
  - `FALL_THROUGH` [`00abf38c`](#insn-00abf38c) → [`00abf390`](#insn-00abf390)
- ブロック [`00abf390`](#insn-00abf390) 範囲 `[['00abf390', '00abf3ab']]`
  - `UNCONDITIONAL_JUMP` [`00abf3a8`](#insn-00abf3a8) → [`00abf264`](#insn-00abf264)
- ブロック [`00abf460`](#insn-00abf460) 範囲 `[['00abf460', '00abf463']]`

## 命令位置別の参照

- [`00abefd8`](#insn-00abefd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefdc`](#insn-00abefdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefe0`](#insn-00abefe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefe4`](#insn-00abefe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeff8`](#insn-00abeff8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeffc`](#insn-00abeffc) → [`009b79e8`](../009b7/009b79e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b79e8` · 推定シンボル `None` · 推定型 `None`
- [`00abf004`](#insn-00abf004) → [`00abf2b4`](#insn-00abf2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf00c`](#insn-00abf00c) → [`009bd6b8`](../009bd/009bd6b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009bd6b8` · 推定シンボル `None` · 推定型 `None`
- [`00abf010`](#insn-00abf010) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf01c`](#insn-00abf01c) → [`00574fe4`](../00574/00574fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574fe4` · 推定シンボル `None` · 推定型 `None`
- [`00abf020`](#insn-00abf020) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf024`](#insn-00abf024) → [`00abf030`](#insn-00abf030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf028`](#insn-00abf028) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf02c`](#insn-00abf02c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf03c`](#insn-00abf03c) → `0029fa64`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf044`](#insn-00abf044) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf048`](#insn-00abf048) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf04c`](#insn-00abf04c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf050`](#insn-00abf050) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf054`](#insn-00abf054) → `Stack[-0x6d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf068`](#insn-00abf068) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf07c`](#insn-00abf07c) → [`00abf088`](#insn-00abf088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf080`](#insn-00abf080) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf084`](#insn-00abf084) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf094`](#insn-00abf094) → `0029d837`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf098`](#insn-00abf098) → `0029d83d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf09c`](#insn-00abf09c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a0`](#insn-00abf0a0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a4`](#insn-00abf0a4) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a8`](#insn-00abf0a8) → `Stack[-0x79]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0ac`](#insn-00abf0ac) → `Stack[-0x71]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0c0`](#insn-00abf0c0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0c8`](#insn-00abf0c8) → [`00abf0d4`](#insn-00abf0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0cc`](#insn-00abf0cc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0d0`](#insn-00abf0d0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf0e0`](#insn-00abf0e0) → `002a1a50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf0e4`](#insn-00abf0e4) → `002a1a57`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf0e8`](#insn-00abf0e8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0ec`](#insn-00abf0ec) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f0`](#insn-00abf0f0) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f4`](#insn-00abf0f4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f8`](#insn-00abf0f8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf10c`](#insn-00abf10c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf114`](#insn-00abf114) → [`00abf120`](#insn-00abf120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf118`](#insn-00abf118) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf11c`](#insn-00abf11c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf12c`](#insn-00abf12c) → `002ace48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf134`](#insn-00abf134) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf138`](#insn-00abf138) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf13c`](#insn-00abf13c) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf140`](#insn-00abf140) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf154`](#insn-00abf154) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf15c`](#insn-00abf15c) → [`00abf168`](#insn-00abf168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf160`](#insn-00abf160) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf164`](#insn-00abf164) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf170`](#insn-00abf170) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf178`](#insn-00abf178) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf180`](#insn-00abf180) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf188`](#insn-00abf188) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf19c`](#insn-00abf19c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1a4`](#insn-00abf1a4) → [`00abf1b0`](#insn-00abf1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1a8`](#insn-00abf1a8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1ac`](#insn-00abf1ac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf1bc`](#insn-00abf1bc) → `002a5bfb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf1c8`](#insn-00abf1c8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1cc`](#insn-00abf1cc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1d0`](#insn-00abf1d0) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1d4`](#insn-00abf1d4) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1d8`](#insn-00abf1d8) → `Stack[-0x73]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1ec`](#insn-00abf1ec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf204`](#insn-00abf204) → [`00abf210`](#insn-00abf210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf208`](#insn-00abf208) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf20c`](#insn-00abf20c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abf210`](#insn-00abf210) → `00334360`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00abf218`](#insn-00abf218) → [`00abf22c`](#insn-00abf22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf21c`](#insn-00abf21c) → `003343f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[51]`
- [`00abf220`](#insn-00abf220) → `0038fb88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0038fb88` · 推定型 `dword`
- [`00abf224`](#insn-00abf224) → [`00abf23c`](#insn-00abf23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf228`](#insn-00abf228) → [`00abf234`](#insn-00abf234) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf22c`](#insn-00abf22c) → `0038fb88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0038fb88` · 推定型 `dword`
- [`00abf230`](#insn-00abf230) → [`00abf23c`](#insn-00abf23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf238`](#insn-00abf238) → [`009a2998`](../009a2/009a2998.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a2998` · 推定シンボル `None` · 推定型 `None`
- [`00abf24c`](#insn-00abf24c) → `0039a224`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[59]`
- [`00abf254`](#insn-00abf254) → [`00abf284`](#insn-00abf284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf260`](#insn-00abf260) → [`00abf2e0`](#insn-00abf2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf26c`](#insn-00abf26c) → `0039a224`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[59]`
- [`00abf278`](#insn-00abf278) → `003b0f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[31]`
- [`00abf27c`](#insn-00abf27c) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00abf280`](#insn-00abf280) → [`0041cc4c`](../0041c/0041cc4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041cc4c` · 推定シンボル `None` · 推定型 `None`
- [`00abf284`](#insn-00abf284) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf288`](#insn-00abf288) → [`00abf2b4`](#insn-00abf2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf294`](#insn-00abf294) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00abf298`](#insn-00abf298) → [`00abf2b4`](#insn-00abf2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2b0`](#insn-00abf2b0) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00abf2b8`](#insn-00abf2b8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2c0`](#insn-00abf2c0) → [`00abf460`](#insn-00abf460) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2c8`](#insn-00abf2c8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2cc`](#insn-00abf2cc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2d0`](#insn-00abf2d0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2d4`](#insn-00abf2d4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2e4`](#insn-00abf2e4) → [`0053d984`](../0053d/0053d984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053d984` · 推定シンボル `None` · 推定型 `None`
- [`00abf2e8`](#insn-00abf2e8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2f8`](#insn-00abf2f8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2fc`](#insn-00abf2fc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf300`](#insn-00abf300) → `00c0f5c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abf300`](#insn-00abf300) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf304`](#insn-00abf304) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf318`](#insn-00abf318) → [`0084dd1c`](../0084d/0084dd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0084dd1c` · 推定シンボル `None` · 推定型 `None`
- [`00abf31c`](#insn-00abf31c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf324`](#insn-00abf324) → [`00abf334`](#insn-00abf334) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf328`](#insn-00abf328) → [`00abf348`](#insn-00abf348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf330`](#insn-00abf330) → [`00abf33c`](#insn-00abf33c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf33c`](#insn-00abf33c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf340`](#insn-00abf340) → `00c0f5e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abf340`](#insn-00abf340) → `00c0f5f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abf344`](#insn-00abf344) → [`00aca844`](../00aca/00aca844.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aca844` · 推定シンボル `None` · 推定型 `None`
- [`00abf344`](#insn-00abf344) → [`00aca848`](../00aca/00aca848.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aca848` · 推定シンボル `None` · 推定型 `None`
- [`00abf348`](#insn-00abf348) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf34c`](#insn-00abf34c) → [`00abf378`](#insn-00abf378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf358`](#insn-00abf358) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00abf35c`](#insn-00abf35c) → [`00abf378`](#insn-00abf378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf374`](#insn-00abf374) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00abf378`](#insn-00abf378) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf37c`](#insn-00abf37c) → [`00abf264`](#insn-00abf264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf388`](#insn-00abf388) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00abf38c`](#insn-00abf38c) → [`00abf264`](#insn-00abf264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf3a4`](#insn-00abf3a4) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00abf3a8`](#insn-00abf3a8) → [`00abf264`](#insn-00abf264) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf460`](#insn-00abf460) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abefd8`](#insn-00abefd8)

~~~json
{
  "source": "00abefd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefdc`](#insn-00abefdc)

~~~json
{
  "source": "00abefdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefe0`](#insn-00abefe0)

~~~json
{
  "source": "00abefe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefe4`](#insn-00abefe4)

~~~json
{
  "source": "00abefe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeff8`](#insn-00abeff8)

~~~json
{
  "source": "00abeff8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeffc`](#insn-00abeffc)

~~~json
{
  "source": "00abeffc",
  "target": "009b79e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf004`](#insn-00abf004)

~~~json
{
  "source": "00abf004",
  "target": "00abf2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf00c`](#insn-00abf00c)

~~~json
{
  "source": "00abf00c",
  "target": "009bd6b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf010`](#insn-00abf010)

~~~json
{
  "source": "00abf010",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf01c`](#insn-00abf01c)

~~~json
{
  "source": "00abf01c",
  "target": "00574fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf020`](#insn-00abf020)

~~~json
{
  "source": "00abf020",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf024`](#insn-00abf024)

~~~json
{
  "source": "00abf024",
  "target": "00abf030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf028`](#insn-00abf028)

~~~json
{
  "source": "00abf028",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf02c`](#insn-00abf02c)

~~~json
{
  "source": "00abf02c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf03c`](#insn-00abf03c)

~~~json
{
  "source": "00abf03c",
  "target": "0029fa64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fa64",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "61677265656d656e745f616363657074656400",
  "capture_start": "0029fa64",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf044`](#insn-00abf044)

~~~json
{
  "source": "00abf044",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf048`](#insn-00abf048)

~~~json
{
  "source": "00abf048",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf04c`](#insn-00abf04c)

~~~json
{
  "source": "00abf04c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf050`](#insn-00abf050)

~~~json
{
  "source": "00abf050",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf054`](#insn-00abf054)

~~~json
{
  "source": "00abf054",
  "target": "Stack[-0x6d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf068`](#insn-00abf068)

~~~json
{
  "source": "00abf068",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf07c`](#insn-00abf07c)

~~~json
{
  "source": "00abf07c",
  "target": "00abf088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf080`](#insn-00abf080)

~~~json
{
  "source": "00abf080",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf084`](#insn-00abf084)

~~~json
{
  "source": "00abf084",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf094`](#insn-00abf094)

~~~json
{
  "source": "00abf094",
  "target": "0029d837",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029d837",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "62697274686461795f737461746500",
  "capture_start": "0029d837",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf098`](#insn-00abf098)

~~~json
{
  "source": "00abf098",
  "target": "0029d83d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029d837",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "62697274686461795f737461746500",
  "capture_start": "0029d837",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf09c`](#insn-00abf09c)

~~~json
{
  "source": "00abf09c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a0`](#insn-00abf0a0)

~~~json
{
  "source": "00abf0a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a4`](#insn-00abf0a4)

~~~json
{
  "source": "00abf0a4",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a8`](#insn-00abf0a8)

~~~json
{
  "source": "00abf0a8",
  "target": "Stack[-0x79]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0ac`](#insn-00abf0ac)

~~~json
{
  "source": "00abf0ac",
  "target": "Stack[-0x71]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0c0`](#insn-00abf0c0)

~~~json
{
  "source": "00abf0c0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0c8`](#insn-00abf0c8)

~~~json
{
  "source": "00abf0c8",
  "target": "00abf0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0cc`](#insn-00abf0cc)

~~~json
{
  "source": "00abf0cc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0d0`](#insn-00abf0d0)

~~~json
{
  "source": "00abf0d0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0e0`](#insn-00abf0e0)

~~~json
{
  "source": "00abf0e0",
  "target": "002a1a50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1a50",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6c696d69744164547261636b696e6700",
  "capture_start": "002a1a50",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf0e4`](#insn-00abf0e4)

~~~json
{
  "source": "00abf0e4",
  "target": "002a1a57",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1a50",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "6c696d69744164547261636b696e6700",
  "capture_start": "002a1a50",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf0e8`](#insn-00abf0e8)

~~~json
{
  "source": "00abf0e8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0ec`](#insn-00abf0ec)

~~~json
{
  "source": "00abf0ec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0f0`](#insn-00abf0f0)

~~~json
{
  "source": "00abf0f0",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0f4`](#insn-00abf0f4)

~~~json
{
  "source": "00abf0f4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0f8`](#insn-00abf0f8)

~~~json
{
  "source": "00abf0f8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf10c`](#insn-00abf10c)

~~~json
{
  "source": "00abf10c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf114`](#insn-00abf114)

~~~json
{
  "source": "00abf114",
  "target": "00abf120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf118`](#insn-00abf118)

~~~json
{
  "source": "00abf118",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf11c`](#insn-00abf11c)

~~~json
{
  "source": "00abf11c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf12c`](#insn-00abf12c)

~~~json
{
  "source": "00abf12c",
  "target": "002ace48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ace48",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "676470725f6164696400",
  "capture_start": "002ace48",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf134`](#insn-00abf134)

~~~json
{
  "source": "00abf134",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf138`](#insn-00abf138)

~~~json
{
  "source": "00abf138",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf13c`](#insn-00abf13c)

~~~json
{
  "source": "00abf13c",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf140`](#insn-00abf140)

~~~json
{
  "source": "00abf140",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf154`](#insn-00abf154)

~~~json
{
  "source": "00abf154",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf15c`](#insn-00abf15c)

~~~json
{
  "source": "00abf15c",
  "target": "00abf168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf160`](#insn-00abf160)

~~~json
{
  "source": "00abf160",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf164`](#insn-00abf164)

~~~json
{
  "source": "00abf164",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf170`](#insn-00abf170)

~~~json
{
  "source": "00abf170",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf178`](#insn-00abf178)

~~~json
{
  "source": "00abf178",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf180`](#insn-00abf180)

~~~json
{
  "source": "00abf180",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf188`](#insn-00abf188)

~~~json
{
  "source": "00abf188",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf19c`](#insn-00abf19c)

~~~json
{
  "source": "00abf19c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1a4`](#insn-00abf1a4)

~~~json
{
  "source": "00abf1a4",
  "target": "00abf1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1a8`](#insn-00abf1a8)

~~~json
{
  "source": "00abf1a8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1ac`](#insn-00abf1ac)

~~~json
{
  "source": "00abf1ac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf1bc`](#insn-00abf1bc)

~~~json
{
  "source": "00abf1bc",
  "target": "002a5bfb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5bfb",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "676470725f7072697661637900",
  "capture_start": "002a5bfb",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf1c8`](#insn-00abf1c8)

~~~json
{
  "source": "00abf1c8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1cc`](#insn-00abf1cc)

~~~json
{
  "source": "00abf1cc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1d0`](#insn-00abf1d0)

~~~json
{
  "source": "00abf1d0",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1d4`](#insn-00abf1d4)

~~~json
{
  "source": "00abf1d4",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1d8`](#insn-00abf1d8)

~~~json
{
  "source": "00abf1d8",
  "target": "Stack[-0x73]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1ec`](#insn-00abf1ec)

~~~json
{
  "source": "00abf1ec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf204`](#insn-00abf204)

~~~json
{
  "source": "00abf204",
  "target": "00abf210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf208`](#insn-00abf208)

~~~json
{
  "source": "00abf208",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf20c`](#insn-00abf20c)

~~~json
{
  "source": "00abf20c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf210`](#insn-00abf210)

~~~json
{
  "source": "00abf210",
  "target": "00334360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334359",
  "offset": 7,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e20480c1d2093049e069d08600c1f20480e00d3dedd",
  "capture_start": "00334359",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf218`](#insn-00abf218)

~~~json
{
  "source": "00abf218",
  "target": "00abf22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf21c`](#insn-00abf21c)

~~~json
{
  "source": "00abf21c",
  "target": "003343f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003343dd",
  "offset": 19,
  "size": 51,
  "datatype": "byte[51]",
  "bytes": "440e304c0c1d3093029404950696089e0a9d0c0a02a80c1f304c0e00d3d4d5d6",
  "capture_start": "003343dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abf220`](#insn-00abf220)

~~~json
{
  "source": "00abf220",
  "target": "0038fb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038fb88",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0038fb88",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf224`](#insn-00abf224)

~~~json
{
  "source": "00abf224",
  "target": "00abf23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf228`](#insn-00abf228)

~~~json
{
  "source": "00abf228",
  "target": "00abf234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf22c`](#insn-00abf22c)

~~~json
{
  "source": "00abf22c",
  "target": "0038fb88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038fb88",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0038fb88",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf230`](#insn-00abf230)

~~~json
{
  "source": "00abf230",
  "target": "00abf23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf238`](#insn-00abf238)

~~~json
{
  "source": "00abf238",
  "target": "009a2998",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf24c`](#insn-00abf24c)

~~~json
{
  "source": "00abf24c",
  "target": "0039a224",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039a215",
  "offset": 15,
  "size": 59,
  "datatype": "byte[59]",
  "bytes": "440ea0015c0c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "0039a215",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abf254`](#insn-00abf254)

~~~json
{
  "source": "00abf254",
  "target": "00abf284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf260`](#insn-00abf260)

~~~json
{
  "source": "00abf260",
  "target": "00abf2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf26c`](#insn-00abf26c)

~~~json
{
  "source": "00abf26c",
  "target": "0039a224",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039a215",
  "offset": 15,
  "size": 59,
  "datatype": "byte[59]",
  "bytes": "440ea0015c0c1d609302940495069608970a980c990e9a109b129c149e169d18",
  "capture_start": "0039a215",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00abf278`](#insn-00abf278)

~~~json
{
  "source": "00abf278",
  "target": "003b0f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b0f89",
  "offset": 15,
  "size": 31,
  "datatype": "byte[31]",
  "bytes": "600c1d109e029d0493069408950a960c970e981099129a149b169c18000000",
  "capture_start": "003b0f89",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf27c`](#insn-00abf27c)

~~~json
{
  "source": "00abf27c",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf280`](#insn-00abf280)

~~~json
{
  "source": "00abf280",
  "target": "0041cc4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf284`](#insn-00abf284)

~~~json
{
  "source": "00abf284",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf288`](#insn-00abf288)

~~~json
{
  "source": "00abf288",
  "target": "00abf2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf294`](#insn-00abf294)

~~~json
{
  "source": "00abf294",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf298`](#insn-00abf298)

~~~json
{
  "source": "00abf298",
  "target": "00abf2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2b0`](#insn-00abf2b0)

~~~json
{
  "source": "00abf2b0",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2b8`](#insn-00abf2b8)

~~~json
{
  "source": "00abf2b8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2c0`](#insn-00abf2c0)

~~~json
{
  "source": "00abf2c0",
  "target": "00abf460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2c8`](#insn-00abf2c8)

~~~json
{
  "source": "00abf2c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2cc`](#insn-00abf2cc)

~~~json
{
  "source": "00abf2cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2d0`](#insn-00abf2d0)

~~~json
{
  "source": "00abf2d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2d4`](#insn-00abf2d4)

~~~json
{
  "source": "00abf2d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2e4`](#insn-00abf2e4)

~~~json
{
  "source": "00abf2e4",
  "target": "0053d984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2e8`](#insn-00abf2e8)

~~~json
{
  "source": "00abf2e8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2f8`](#insn-00abf2f8)

~~~json
{
  "source": "00abf2f8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2fc`](#insn-00abf2fc)

~~~json
{
  "source": "00abf2fc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf300`](#insn-00abf300)

~~~json
{
  "source": "00abf300",
  "target": "00c0f5c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f5c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf300`](#insn-00abf300)

~~~json
{
  "source": "00abf300",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf304`](#insn-00abf304)

~~~json
{
  "source": "00abf304",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf318`](#insn-00abf318)

~~~json
{
  "source": "00abf318",
  "target": "0084dd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf31c`](#insn-00abf31c)

~~~json
{
  "source": "00abf31c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf324`](#insn-00abf324)

~~~json
{
  "source": "00abf324",
  "target": "00abf334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf328`](#insn-00abf328)

~~~json
{
  "source": "00abf328",
  "target": "00abf348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf330`](#insn-00abf330)

~~~json
{
  "source": "00abf330",
  "target": "00abf33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf33c`](#insn-00abf33c)

~~~json
{
  "source": "00abf33c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf340`](#insn-00abf340)

~~~json
{
  "source": "00abf340",
  "target": "00c0f5e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f5e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf340`](#insn-00abf340)

~~~json
{
  "source": "00abf340",
  "target": "00c0f5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f5f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf344`](#insn-00abf344)

~~~json
{
  "source": "00abf344",
  "target": "00aca844",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf344`](#insn-00abf344)

~~~json
{
  "source": "00abf344",
  "target": "00aca848",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf348`](#insn-00abf348)

~~~json
{
  "source": "00abf348",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf34c`](#insn-00abf34c)

~~~json
{
  "source": "00abf34c",
  "target": "00abf378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf358`](#insn-00abf358)

~~~json
{
  "source": "00abf358",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf35c`](#insn-00abf35c)

~~~json
{
  "source": "00abf35c",
  "target": "00abf378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf374`](#insn-00abf374)

~~~json
{
  "source": "00abf374",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf378`](#insn-00abf378)

~~~json
{
  "source": "00abf378",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf37c`](#insn-00abf37c)

~~~json
{
  "source": "00abf37c",
  "target": "00abf264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf388`](#insn-00abf388)

~~~json
{
  "source": "00abf388",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf38c`](#insn-00abf38c)

~~~json
{
  "source": "00abf38c",
  "target": "00abf264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf3a4`](#insn-00abf3a4)

~~~json
{
  "source": "00abf3a4",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf3a8`](#insn-00abf3a8)

~~~json
{
  "source": "00abf3a8",
  "target": "00abf264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf460`](#insn-00abf460)

~~~json
{
  "source": "00abf460",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
