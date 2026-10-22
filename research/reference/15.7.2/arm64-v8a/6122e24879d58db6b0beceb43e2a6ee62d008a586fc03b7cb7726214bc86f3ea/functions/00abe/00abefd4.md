# 00abefd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00abefd4.md)

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
  "source_sha256": "f2fdf4996720003cea14168585fa49362372d81de874ffe7c4b53d7a69b511c4",
  "source_text_sha256": "f2fdf4996720003cea14168585fa49362372d81de874ffe7c4b53d7a69b511c4"
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
## 疑似コード 1/1 / UTF-8 9751 bytes

~~~c

uint FUN_00abefd4(long param_1)

{
  int iVar1;
  long lVar2;
  __shared_weak_count *p_Var3;
  byte bVar4;
  uint uVar5;
  undefined4 uVar6;
  long lVar7;
  byte *pbVar8;
  undefined8 local_b0;
  __shared_weak_count *p_Stack_a8;
  undefined8 local_a0;
  __shared_weak_count *p_Stack_98;
  long *local_90;
  __shared_weak_count *local_88;
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
    operator_delete((void *)CONCAT44(uStack_6c,CONCAT13(uStack_6d,CONCAT21(uStack_6f,cStack_70))));
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
      p_Stack_98 = p_Stack_a8;
      local_a0 = local_b0;
      local_b0 = 0;
      p_Stack_a8 = (__shared_weak_count *)0x0;
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
      p_Var3 = p_Stack_98;
      if ((p_Stack_98 != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Stack_98 + 8), lVar7 == 0)) {
        (**(code **)(*(long *)p_Var3 + 0x10))(p_Var3);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var3);
      }
      p_Var3 = p_Stack_a8;
      if ((p_Stack_a8 != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Stack_a8 + 8), lVar7 == 0)) {
        (**(code **)(*(long *)p_Var3 + 0x10))(p_Var3);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var3);
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
  if ((local_88 != (__shared_weak_count *)0x0) &&
     (lVar7 = FUN_00bd6d90(0xffffffffffffffff,local_88 + 8), lVar7 == 0)) {
                    /* try { // try from 00abf2a0 to 00bbf2a7 has its CatchHandler @ 00ac51d4 */
    (**(code **)(*(long *)local_88 + 0x10))(local_88);
    std::__ndk1::__shared_weak_count::__release_weak(local_88);
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
